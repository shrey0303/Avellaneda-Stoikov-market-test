import math

import pytest

from lobreplay.as_model import INVENTORY, ASParams
from lobreplay.book import OrderBook
from lobreplay.lobster_format import NS_PER_S, TICK_SIZE, Direction, EventType
from lobreplay.parser import Message
from lobreplay.queue_tracker import FillRule
from lobreplay.session import SESSION_END_NS, SESSION_START_NS
from lobreplay.signals import (
    OFI,
    QUEUE_IMBALANCE,
    SIGNALS,
    TRADE_IMBALANCE,
    LiveSignals,
    SignalConfig,
    SignalSamples,
    SkewModel,
    analyse,
    choose_skew,
    fit,
    record,
    score,
)
from lobreplay.strategy import SIGNAL, RunSpec, StrategyConfig, run_strategies, windows_between
from lobreplay.synthetic import SyntheticConfig, generate

BUY, SELL = Direction.BUY, Direction.SELL
S = NS_PER_S


def msg(t_s, et, oid, size, price, side):
    return Message(int(t_s * S), EventType(et), oid, size, price, side)


def book_and_signals(lookback_s=5.0):
    """Bid 300 @ 1000, ask 100 @ 1010."""
    book = OrderBook()
    book.seed_preopen(BUY, 1000, 300)
    book.seed_preopen(SELL, 1010, 100)
    return book, LiveSignals(book, lookback_s)


def feed(book, live, *messages):
    for m in messages:
        book.apply(m)
        live.update(m)


# -- live signal values -------------------------------------------------------------

def test_queue_imbalance_leans_to_the_bigger_side():
    book, live = book_and_signals()
    assert live.value(QUEUE_IMBALANCE, 0) == pytest.approx((300 - 100) / 400)
    feed(book, live, msg(1, 1, 1, 500, 1010, SELL))
    assert live.value(QUEUE_IMBALANCE, 1 * S) == pytest.approx((300 - 600) / 900)


def test_ofi_counts_size_added_and_removed_at_the_touch():
    book, live = book_and_signals()
    feed(book, live, msg(1, 1, 1, 200, 1000, BUY))        # +200 at the best bid
    assert live.value(OFI, 1 * S) == pytest.approx(2.0)
    feed(book, live, msg(2, 1, 2, 100, 1010, SELL))       # +100 at the best ask counts against
    assert live.value(OFI, 2 * S) == pytest.approx(1.0)
    feed(book, live, msg(3, 3, 1, 200, 1000, BUY))        # the bid order is deleted again
    assert live.value(OFI, 3 * S) == pytest.approx(-1.0)


def test_ofi_on_a_price_improvement_counts_the_new_level():
    book, live = book_and_signals()
    feed(book, live, msg(1, 1, 1, 100, 1005, BUY))        # new best bid above the old one
    assert live.value(OFI, 1 * S) == pytest.approx(1.0)
    feed(book, live, msg(2, 3, 1, 100, 1005, BUY))        # it leaves: best bid falls back to 1000 x 300
    assert live.value(OFI, 2 * S) == pytest.approx(0.0)   # +100 then -100


def test_trade_imbalance_is_signed_by_the_aggressor():
    book, live = book_and_signals()
    feed(book, live, msg(1, 4, 900, 100, 1010, SELL))     # a resting sell was hit: a buyer crossed
    assert live.value(TRADE_IMBALANCE, 1 * S) == pytest.approx(1.0)
    feed(book, live, msg(2, 4, 901, 200, 1000, BUY))      # a resting buy was hit: a seller crossed
    assert live.value(TRADE_IMBALANCE, 2 * S) == pytest.approx(-1.0)
    feed(book, live, msg(3, 5, 0, 500, 1005, BUY))        # hidden executions are not counted
    assert live.value(TRADE_IMBALANCE, 3 * S) == pytest.approx(-1.0)


def test_flow_signals_forget_events_older_than_the_lookback():
    book, live = book_and_signals(lookback_s=5.0)
    feed(book, live, msg(1, 1, 1, 200, 1000, BUY))
    assert live.value(OFI, 5 * S) == pytest.approx(2.0)
    assert live.value(OFI, 6 * S) == 0.0                   # exactly 5 s old is out
    with pytest.raises(ValueError):
        live.value("nope", 6 * S)


# -- fitting and scoring ------------------------------------------------------------

def samples_where_mid_follows(signal_values, lead_steps=1, noise=None):
    """Mid moves by `x` ticks `lead_steps` seconds after the signal showed x."""
    s = SignalSamples(1)
    mid = 1_000_000.0
    pending = [0.0] * lead_steps
    for i, x in enumerate(signal_values):
        mid += pending.pop(0) * TICK_SIZE + (noise[i] * TICK_SIZE if noise else 0.0)
        pending.append(x)
        s.times.append(i * S)
        s.mids.append(mid)
        for name in SIGNALS:
            s.features[name].append(x if name == QUEUE_IMBALANCE else 0.0)
    return s


def test_fit_recovers_a_known_slope_and_scores_it_perfectly():
    xs = [math.sin(i) for i in range(600)]
    s = samples_where_mid_follows(xs)
    f = fit(s, QUEUE_IMBALANCE, 1, 0, 300 * S)
    assert f.slope == pytest.approx(1.0) and f.intercept == pytest.approx(0.0, abs=1e-9)
    assert f.corr == pytest.approx(1.0)
    sc = score(s, f, [(300 * S, 450 * S), (450 * S, 600 * S)])
    assert sc.corr == pytest.approx(1.0) and sc.r2 == pytest.approx(1.0) and sc.hit_rate == 1.0
    assert len(sc.window_corrs) == 2


def test_a_signal_with_no_variation_cannot_be_fitted():
    s = samples_where_mid_follows([math.sin(i) for i in range(600)])
    assert fit(s, OFI, 1, 0, 300 * S) is None              # OFI is all zeros in this fixture
    assert fit(s, QUEUE_IMBALANCE, 1, 0, 100 * S) is None  # fewer than min_samples


def test_fit_never_uses_a_target_that_ends_at_or_after_the_split():
    s = samples_where_mid_follows([math.sin(i) for i in range(600)])
    for h in (1, 5, 30):
        f = fit(s, QUEUE_IMBALANCE, h, 0, 300 * S)
        assert f.n == 300 - h                              # the last h samples before the split are dropped


def test_a_useless_signal_scores_near_zero_out_of_sample():
    import random
    rng = random.Random(0)
    xs = [rng.uniform(-1, 1) for _ in range(4000)]
    noise = [rng.gauss(0, 1) for _ in range(4000)]
    s = samples_where_mid_follows([0.0] * 4000, noise=noise)
    s.features[QUEUE_IMBALANCE] = xs                       # unrelated to the mid
    f = fit(s, QUEUE_IMBALANCE, 1, 0, 2000 * S)
    sc = score(s, f, [(2000 * S, 3000 * S), (3000 * S, 4000 * S)])
    assert abs(sc.corr) < 0.1 and sc.r2 < 0.01
    assert 0.4 < sc.hit_rate < 0.6


def test_choose_skew_takes_the_strongest_fit_at_the_skew_horizon():
    cfg = SignalConfig(skew_horizon_s=5)
    xs = [math.sin(i / 3) for i in range(900)]
    s = samples_where_mid_follows(xs, lead_steps=1)
    fits = [f for h in (1, 5) for name in SIGNALS if (f := fit(s, name, h, 0, 900 * S)) is not None]
    skew = choose_skew(fits, cfg)
    assert skew.signal == QUEUE_IMBALANCE and skew.horizon_s == 5
    five = next(f for f in fits if f.horizon_s == 5)
    assert skew.slope_dollars == pytest.approx(five.slope * 0.01)
    assert choose_skew([f for f in fits if f.horizon_s == 1], cfg) is None


# -- on synthetic files -------------------------------------------------------------

@pytest.fixture(scope="module")
def files(tmp_path_factory):
    return generate(SyntheticConfig(n_messages=12_000, levels=10, seed=11), tmp_path_factory.mktemp("sig"))


def test_record_samples_every_grid_second(files):
    start, end = SESSION_START_NS + 60 * S, SESSION_START_NS + 660 * S
    s = record(files, start, end)
    assert s.times == list(range(start, end, S))
    assert all(len(v) == len(s.times) for v in s.features.values())
    assert all(-1.0 <= x <= 1.0 for x in s.features[QUEUE_IMBALANCE])
    assert any(x != 0 for x in s.features[OFI]) and any(x != 0 for x in s.features[TRADE_IMBALANCE])


def test_analyse_fits_the_morning_and_scores_the_afternoon(files):
    start, split, end = SESSION_START_NS + 60 * S, 45_900 * S, SESSION_END_NS - 60 * S
    windows = windows_between(split, end, 1800.0)
    sg = analyse(files, start, split, end, windows)
    assert {(f.signal, f.horizon_s) for f in sg.fits} == {(n, h) for n in SIGNALS for h in (1, 5, 10, 30, 60)}
    assert sg.samples_fit == (split - start) // S
    assert 5_000 < sg.samples_test <= (end - split) // S   # the synthetic day stops before 15:59
    assert all(f.n <= sg.samples_fit for f in sg.fits)
    assert all(sc.n <= sg.samples_test for sc in sg.scores)
    assert sg.skew is not None and sg.skew.horizon_s == 5


P = ASParams(sigma=2e-4, A=0.02, k=250.0, gamma=20.0)
CFG = StrategyConfig(window_s=1800.0, requote_s=5.0)


def run_pair(files, slope):
    start, end = SESSION_START_NS + 60 * S, SESSION_END_NS - 60 * S
    specs = [(RunSpec(name, 1.0, True, FillRule.CONSERVATIVE), P) for name in (INVENTORY, SIGNAL)]
    results, _ = run_strategies(files, specs, start, end, CFG, skew=SkewModel(QUEUE_IMBALANCE, 5, 5.0, slope))
    return results


def test_signal_strategy_with_zero_skew_is_the_inventory_strategy(files):
    inv, lean = run_pair(files, 0.0)
    assert lean.fills == inv.fills and len(inv.fills) > 0
    assert [w.pnl for w in lean.windows] == [w.pnl for w in inv.windows]
    assert sum(w.skew_moved for w in lean.windows) == 0


def test_a_large_skew_moves_quotes_and_changes_what_fills(files):
    inv, lean = run_pair(files, 0.05)                      # five cents per unit of imbalance
    assert sum(w.skew_moved for w in lean.windows) > 0
    assert sum(w.skew_moved for w in inv.windows) == 0
    assert lean.fills != inv.fills
    assert all(f.price % TICK_SIZE == 0 for f in lean.fills)
