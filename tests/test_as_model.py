import math
from statistics import fmean, pstdev

import pytest

from lobreplay import as_model, model_world
from lobreplay.as_model import INVENTORY, SYMMETRIC, ASParams
from lobreplay.stats import bootstrap_mean, paired_difference

# The parameters of Avellaneda & Stoikov (2008), section 3.3.
PAPER = ASParams(sigma=2.0, A=140.0, k=1.5, gamma=0.1)


def test_formulas_match_the_paper():
    assert as_model.reservation_price(100.0, 3, PAPER, 0.5) == pytest.approx(100.0 - 3 * 0.1 * 4.0 * 0.5)
    assert as_model.total_spread(PAPER, 1.0) == pytest.approx(0.1 * 4.0 + (2 / 0.1) * math.log(1 + 0.1 / 1.5))
    bid, ask = as_model.quotes(INVENTORY, 100.0, 3, PAPER, 0.5)
    assert (bid + ask) / 2 == pytest.approx(as_model.reservation_price(100.0, 3, PAPER, 0.5))
    assert ask - bid == pytest.approx(as_model.total_spread(PAPER, 0.5))


def test_symmetric_quotes_ignore_inventory_entirely():
    flat = as_model.quotes(SYMMETRIC, 100.0, 0, PAPER, 0.5)
    for q in (-7, -1, 1, 50):
        assert as_model.quotes(SYMMETRIC, 100.0, q, PAPER, 0.5) == flat
    assert (flat[0] + flat[1]) / 2 == pytest.approx(100.0)
    assert flat[1] - flat[0] == pytest.approx(as_model.total_spread(PAPER, 0.5))   # same spread as inventory


def test_inventory_strategy_skews_against_its_position():
    long_bid, long_ask = as_model.quotes(INVENTORY, 100.0, 2, PAPER, 0.5)
    short_bid, short_ask = as_model.quotes(INVENTORY, 100.0, -2, PAPER, 0.5)
    assert long_bid < short_bid and long_ask < short_ask


def test_gamma_for_penalty_round_trips():
    gamma = as_model.gamma_for_penalty(0.02, sigma=0.001, horizon=1800.0)
    p = ASParams(0.001, 1.0, 100.0, gamma)
    assert 100.0 - as_model.reservation_price(100.0, 1, p, 1800.0) == pytest.approx(0.02)


@pytest.mark.parametrize("bad", [dict(sigma=0), dict(k=0), dict(gamma=-1), dict(A=0)])
def test_parameters_must_be_positive(bad):
    with pytest.raises(ValueError):
        ASParams(**{**dict(sigma=1.0, A=1.0, k=1.0, gamma=1.0), **bad})


def test_unknown_strategy_is_rejected():
    with pytest.raises(ValueError):
        as_model.quotes("clever", 100.0, 0, PAPER, 1.0)
    with pytest.raises(ValueError):
        model_world.simulate("clever", PAPER, 1.0)


# -- model world ----------------------------------------------------------------

@pytest.fixture(scope="module")
def paper_runs():
    return {s: model_world.simulate(s, PAPER, 1.0, n_paths=400, dt=0.005, lot=1, seed=7) for s in as_model.STRATEGIES}


def test_model_world_reproduces_the_papers_headline(paper_runs):
    """Inventory strategy: much tighter inventory and P&L, slightly lower mean profit (paper, table for gamma = 0.1)."""
    inv, sym = paper_runs[INVENTORY], paper_runs[SYMMETRIC]
    assert pstdev(p.end_inventory for p in inv) < 0.5 * pstdev(p.end_inventory for p in sym)
    assert pstdev(p.pnl for p in inv) < 0.7 * pstdev(p.pnl for p in sym)
    assert 55 < fmean(p.pnl for p in inv) < 72
    assert 60 < fmean(p.pnl for p in sym) < 76


def test_model_world_accounting_identity(paper_runs):
    for paths in paper_runs.values():
        for p in paths:
            assert p.pnl == pytest.approx(p.spread_capture + p.inventory_pnl)


def test_model_world_fills_carry_no_information(paper_runs):
    """Inventory P&L averages to zero: a fill says nothing about the next move."""
    e = bootstrap_mean([p.inventory_pnl for p in paper_runs[SYMMETRIC]], n_boot=500)
    assert not e.excludes_zero


def test_model_world_survives_extreme_skew():
    p = ASParams(sigma=0.05, A=5.0, k=2000.0, gamma=50.0)
    paths = model_world.simulate(INVENTORY, p, 600.0, n_paths=3, dt=1.0)
    assert all(math.isfinite(x.pnl) for x in paths)


# -- bootstrap --------------------------------------------------------------------

def test_bootstrap_interval_brackets_the_mean_and_is_reproducible():
    values = [1.0, 2.0, 3.0, 4.0, 10.0]
    e = bootstrap_mean(values, n_boot=500, seed=1)
    assert e.lo <= e.mean == 4.0 <= e.hi and e.n == 5
    assert e == bootstrap_mean(values, n_boot=500, seed=1)


def test_bootstrap_edge_cases():
    assert bootstrap_mean([]).n == 0 and not bootstrap_mean([]).excludes_zero
    one = bootstrap_mean([3.0])
    assert (one.lo, one.hi) == (3.0, 3.0) and not one.excludes_zero   # one window proves nothing


def test_paired_difference_sees_a_consistent_gap_that_unpaired_noise_would_hide():
    a = [10.0, 50.0, 90.0, 130.0]
    b = [x - 1.0 for x in a]
    assert paired_difference(a, b, n_boot=300).excludes_zero
    with pytest.raises(ValueError):
        paired_difference([1.0], [1.0, 2.0])
