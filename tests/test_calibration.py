import math
import random

import pytest

from lobreplay.calibration import (
    CalibrationConfig,
    MidSeries,
    Probe,
    calibrate,
    fit_intensity,
    rate_table,
    variance_ratio,
)
from lobreplay.lobster_format import NS_PER_S, PRICE_SCALE, Direction
from lobreplay.parser import LobsterFiles, iter_messages
from lobreplay.queue_tracker import FillRule
from lobreplay.session import SESSION_START_NS
from lobreplay.synthetic import SyntheticConfig, generate

CONS, OPT = FillRule.CONSERVATIVE, FillRule.OPTIMISTIC


# -- fit_intensity ------------------------------------------------------------

def simulated_probes(A, k, n, seed, max_rest=60.0):
    rng = random.Random(seed)
    deltas, exposures, filled = [], [], []
    for _ in range(n):
        d = rng.choice((0.005, 0.015, 0.025, 0.035))
        t = rng.expovariate(A * math.exp(-k * d))
        deltas.append(d)
        exposures.append(min(t, max_rest))
        filled.append(t <= max_rest)
    return deltas, exposures, filled


def test_fit_recovers_known_parameters_with_censoring():
    fit = fit_intensity(*simulated_probes(A=0.2, k=90.0, n=20_000, seed=1))
    assert fit.usable
    assert fit.k == pytest.approx(90.0, rel=0.05)
    assert fit.A == pytest.approx(0.2, rel=0.05)


def test_fit_satisfies_both_likelihood_equations():
    deltas, exposures, filled = simulated_probes(A=0.1, k=50.0, n=3000, seed=2)
    fit = fit_intensity(deltas, exposures, filled)
    expected = [fit.A * math.exp(-fit.k * d) * t for d, t in zip(deltas, exposures)]
    assert sum(expected) == pytest.approx(sum(filled), rel=1e-9)                       # d/dA = 0
    assert sum(e * d for e, d in zip(expected, deltas)) == pytest.approx(
        sum(d for d, f in zip(deltas, filled) if f), rel=1e-9)                          # d/dk = 0


def test_fit_without_fills_is_not_usable():
    fit = fit_intensity([0.01, 0.02], [60.0, 60.0], [False, False])
    assert not fit.usable and fit.n_fills == 0


def test_fill_rate_that_does_not_fall_with_distance_gives_k_zero():
    fit = fit_intensity([0.01, 0.02], [10.0, 10.0], [False, True])   # only the far quote filled
    assert fit.k == 0.0 and not fit.interior and not fit.usable
    assert fit.A == pytest.approx(1 / 20)


def test_all_fills_at_the_nearest_distance_is_reported_not_crashed():
    fit = fit_intensity([0.01, 0.02, 0.03], [5.0, 60.0, 60.0], [True, False, False])
    assert not fit.usable


def test_rate_table_groups_by_depth():
    probes = [Probe(Direction.BUY, 0, 0.005, 0, 10.0, True), Probe(Direction.BUY, 0, 0.005, 0, 30.0, False),
              Probe(Direction.SELL, 1, 0.015, 0, 60.0, False)]
    fit = fit_intensity([p.delta for p in probes], [p.rest_s for p in probes], [p.filled for p in probes])
    rows = rate_table(probes, fit)
    assert [(r.depth_ticks, r.probes, r.fills, r.exposure_s) for r in rows] == [(0, 2, 1, 40.0), (1, 1, 0, 60.0)]
    assert rows[0].empirical == pytest.approx(1 / 40)


# -- sigma --------------------------------------------------------------------

def series_from(path_dollars):
    s = MidSeries()
    for i, v in enumerate(path_dollars):
        s.add(i * NS_PER_S, v * PRICE_SCALE)
    return s


def test_mid_series_returns_last_value_at_or_before():
    s = MidSeries()
    s.add(10, 1.0)
    s.add(20, None)     # no mid: skipped
    s.add(30, 3.0)
    assert s.at(5) is None and s.at(10) == 1.0 and s.at(29) == 1.0 and s.at(30) == 3.0
    assert s.covers(30) and not s.covers(31)


def test_variance_ratio_is_flat_for_a_random_walk():
    rng = random.Random(0)
    path, x = [], 100.0
    for _ in range(40_000):
        path.append(x)
        x += rng.gauss(0, 0.01)
    vr = variance_ratio(series_from(path), 0, 40_000 * NS_PER_S, (1, 10, 60))
    assert [p.horizon_s for p in vr] == [1, 10, 60]
    for p in vr:
        assert p.sigma == pytest.approx(0.01, rel=0.1)
        assert p.ratio == pytest.approx(1.0, abs=0.2)


def test_variance_ratio_shows_short_horizon_noise():
    rng = random.Random(0)
    path, x = [], 100.0
    for _ in range(40_000):
        path.append(x + rng.choice((-0.02, 0.02)))    # bounce around a slow random walk
        x += rng.gauss(0, 0.002)
    vr = variance_ratio(series_from(path), 0, 40_000 * NS_PER_S, (1, 60))
    assert vr[0].ratio > 5 and vr[-1].ratio == 1.0


# -- a calibration pass ---------------------------------------------------------

@pytest.fixture(scope="module")
def files(tmp_path_factory):
    return generate(SyntheticConfig(n_messages=8000, levels=10, seed=5), tmp_path_factory.mktemp("cal"))


START = SESSION_START_NS + 60 * NS_PER_S
END = START + 2 * 3600 * NS_PER_S
CFG = CalibrationConfig(probe_every_s=10.0, probe_max_rest_s=60.0, seed=3)


def test_calibrate_on_synthetic_data(files):
    cal = calibrate(files, START, END, CFG)
    assert cal.sigma is not None and cal.sigma > 0
    assert cal.spread.total_ns > 0
    assert sum(cal.spread.share(t) for t in cal.spread.ns_by_ticks) == pytest.approx(1.0)
    for rule in FillRule:
        probes = cal.probes[rule]
        assert len(probes) > 500
        assert all(START <= p.posted_ns < END for p in probes)
        assert all(0 <= p.rest_s <= CFG.probe_max_rest_s for p in probes)
        assert all(p.posted_ns + p.rest_s * NS_PER_S <= END + 1 for p in probes)   # nothing rests past the window
        assert all(p.delta > 0 for p in probes)
        assert cal.fits[rule].n_fills == sum(p.filled for p in probes) > 0
    # Same probes under both rules; optimistic can only fill sooner.
    for c, o in zip(cal.probes[CONS], cal.probes[OPT]):
        assert (c.side, c.depth_ticks, c.posted_ns) == (o.side, o.depth_ticks, o.posted_ns)
        assert o.filled >= c.filled
        if c.filled:
            assert o.rest_s <= c.rest_s


def test_calibration_does_not_read_past_its_window(files, tmp_path):
    """Chop the file off just after the window: the calibration must be identical."""
    keep = 0
    for keep, m in enumerate(iter_messages(files.message_path), start=1):
        if m.time_ns >= END:
            break
    cut_msg = tmp_path / files.message_path.name
    cut_ob = tmp_path / files.orderbook_path.name
    for src, dst in ((files.message_path, cut_msg), (files.orderbook_path, cut_ob)):
        with open(src) as fh:
            dst.write_text("".join(line for _, line in zip(range(keep), fh)))
    cut = LobsterFiles(files.ticker, files.date, files.levels, cut_msg, cut_ob)

    full, short = calibrate(files, START, END, CFG), calibrate(cut, START, END, CFG)
    assert full.messages == short.messages == keep
    assert full.sigma == short.sigma
    assert full.fits == short.fits
    assert full.probes == short.probes
    assert full.spread.ns_by_ticks == short.spread.ns_by_ticks


def test_calibration_is_reproducible(files):
    assert calibrate(files, START, END, CFG).fits == calibrate(files, START, END, CFG).fits
