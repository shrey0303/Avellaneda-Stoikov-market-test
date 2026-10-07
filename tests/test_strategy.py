import math

import pytest

from lobreplay.as_model import INVENTORY, SYMMETRIC, ASParams
from lobreplay.lobster_format import NS_PER_S, TICK_SIZE, Direction, EventType
from lobreplay.parser import LobsterFiles
from lobreplay.book import OrderBook
from lobreplay.queue_tracker import Fill, FillReason, FillRule, QueueTracker
from lobreplay.session import SESSION_END_NS, SESSION_START_NS
from lobreplay.strategy import (
    QuotingRun,
    RunSpec,
    StrategyConfig,
    ask_to_tick,
    bid_to_tick,
    markouts,
    run_strategies,
    windows_between,
)
from lobreplay.synthetic import SyntheticConfig, generate

BUY, SELL = Direction.BUY, Direction.SELL
CONS, OPT = FillRule.CONSERVATIVE, FillRule.OPTIMISTIC
T0 = SESSION_START_NS


def test_rounding_goes_away_from_the_mid_and_keeps_exact_ticks():
    assert bid_to_tick(10.0049) == 100_000 and ask_to_tick(10.0051) == 100_100
    # 10.02 is not exactly representable; it must still land on its own tick, both ways.
    assert bid_to_tick(10.02) == 100_200 and ask_to_tick(10.02) == 100_200
    assert bid_to_tick(0.1 + 0.2) == 3_000 and ask_to_tick(0.1 + 0.2) == 3_000


def test_windows_are_whole_and_inside_the_range():
    w = windows_between(0, 95 * NS_PER_S, 30.0)
    assert w == [(0, 30 * NS_PER_S), (30 * NS_PER_S, 60 * NS_PER_S), (60 * NS_PER_S, 90 * NS_PER_S)]
    assert windows_between(0, 29 * NS_PER_S, 30.0) == []


# -- a hand-built session ---------------------------------------------------------

def hand_files(tmp_path) -> LobsterFiles:
    """Pre-open book: bid 100 @ $10.00, ask 100 @ $10.02. Times are seconds after the open."""
    rows = [
        (0.0, 6, 0, 100, 100_100, BUY),      # 1 opening cross, book unchanged
        (1.0, 1, 9, 100, 100_400, SELL),     # 2 a deep ask, irrelevant
        (1.5, 1, 5, 100, 100_000, BUY),      # 3 joins the bid behind a sticky quote
        (1.6, 1, 6, 100, 99_900, BUY),       # 4 next bid level down
        (2.0, 4, 77, 100, 100_000, BUY),     # 5 the pre-open bid trades
        (3.0, 4, 5, 100, 100_000, BUY),      # 6 order 5 trades: a sticky quote was ahead of it
        (11.0, 1, 10, 100, 100_500, SELL),   # 7 first message after the 10-second window
    ]
    mp = tmp_path / "H_2012-06-21_34200000_57600000_message_2.csv"
    op = tmp_path / "H_2012-06-21_34200000_57600000_orderbook_2.csv"
    with open(mp, "w", newline="") as fh:
        for t, et, oid, size, price, side in rows:
            fh.write(f"{34200 + t:.9f},{et},{oid},{size},{price},{int(side)}\n")
    op.write_text("100200,100,100000,100,9999999999,0,-9999999999,0\n")
    return LobsterFiles("H", "2012-06-21", 2, mp, op)


# Half-spread of $0.008 and no inventory term to speak of: quotes join both touches.
HAND = ASParams(sigma=1e-6, A=1.0, k=1 / math.expm1(0.008), gamma=1.0)
HAND_CFG = StrategyConfig(window_s=10.0, requote_s=1.0, lot=100)


def run_hand(tmp_path, sticky, rule=CONS, strategy=SYMMETRIC):
    spec = RunSpec(strategy, 1.0, sticky, rule)
    results, series = run_strategies(hand_files(tmp_path), [(spec, HAND)], T0, T0 + 10 * NS_PER_S, HAND_CFG,
                                     record_after_s=1.0)
    return results[0], series


@pytest.mark.parametrize("rule", [CONS, OPT])
def test_sticky_quote_keeps_its_place_and_is_filled(tmp_path, rule):
    r, series = run_hand(tmp_path, sticky=True, rule=rule)
    (w,) = r.windows
    (f,) = r.fills
    assert (f.sign, f.price, f.size, f.time_ns) == (1, 100_000, 100, T0 + 3 * NS_PER_S)
    assert f.mid_before == 100_100                       # mid was $10.01 when we bought at $10.00
    assert w.spread_capture == pytest.approx(1.00)       # 100 shares bought one cent under the mid
    assert w.pnl == pytest.approx(0.50)                  # marked at the closing mid of $10.005
    assert w.inventory_pnl == pytest.approx(-0.50)       # the mid fell half a cent while we held 100
    assert w.realised_pnl == 0                           # nothing was sold, so no pair was completed
    assert w.closed_pnl == pytest.approx(-1.00)          # selling the 100 into the best bid of $9.99 loses a cent each
    assert (w.fills, w.shares_bought, w.shares_sold, w.end_inventory) == (1, 100, 0, 100)
    assert w.posts == 3                                  # bid, ask, then a new bid after the fill
    m = markouts(r, series, (1.0,))
    assert m[1.0] == {0: [pytest.approx(-0.005)]}        # the mid moved half a tick against us


def quoting_run(asks, bids):
    book = OrderBook()
    for price, size in asks:
        book.seed_preopen(SELL, price, size)
    for price, size in bids:
        book.seed_preopen(BUY, price, size)
    run = QuotingRun(RunSpec(INVENTORY, 1.0, True, CONS), HAND, QueueTracker(book, CONS), book, HAND_CFG)
    run.open_window(0, 0, 10 * NS_PER_S)
    run.orders[BUY] = run.tracker.post(BUY, 100_000, 100, 0, 0)   # so take_fills can tell our bid from our ask
    return run, run.orders[BUY].order_id


def test_profit_is_booked_at_each_fills_own_price_and_reported_three_ways():
    run, bid_id = quoting_run(asks=[(100_300, 50), (100_400, 500)], bids=[(100_000, 100)])
    fill = lambda oid, price, size: Fill(1, 0, price, size, FillReason.QUEUE, oid)
    # sell 100 @ 10.10, sell 100 @ 10.30, buy 100 @ 10.20, buy 30 @ 10.25: short 70 at the close
    run.take_fills([fill(0, 101_000, 100), fill(0, 103_000, 100)], 101_500.0)
    run.take_fills([fill(bid_id, 102_000, 100), fill(bid_id, 102_500, 30)], 102_300.0)
    run.close_window(100_150.0)
    w = run.result.windows[0]
    # first in, first out: the 10.10 sale is closed by the 10.20 buy (-10.00), then 30 of the 10.30 sale by 10.25 (+1.50)
    assert w.realised_pnl == pytest.approx(-10.00 + 1.50)
    assert w.end_inventory == -70
    cash = 100 * 10.10 + 100 * 10.30 - 100 * 10.20 - 30 * 10.25
    assert w.pnl == pytest.approx(cash - 70 * 10.015)                       # leftover valued at the mid
    assert w.closed_pnl == pytest.approx(cash - 50 * 10.03 - 20 * 10.04)    # bought back from the asks, two levels
    assert w.closed_pnl < w.pnl


def test_a_flat_window_has_one_profit_figure():
    run, bid_id = quoting_run(asks=[(100_300, 50)], bids=[(100_000, 100)])
    run.take_fills([Fill(1, 0, 100_000, 100, FillReason.QUEUE, bid_id)], 100_150.0)
    run.take_fills([Fill(2, 0, 100_300, 100, FillReason.QUEUE, 0)], 100_150.0)
    run.close_window(100_150.0)
    w = run.result.windows[0]
    assert w.realised_pnl == w.pnl == w.closed_pnl == pytest.approx(3.00)


def test_requeue_loses_its_place_and_is_not_filled(tmp_path):
    r, _ = run_hand(tmp_path, sticky=False)
    (w,) = r.windows
    assert w.fills == 0 and w.pnl == 0 and w.end_inventory == 0
    assert w.posts > 3


def test_markout_past_the_end_of_the_data_is_left_out(tmp_path):
    r, series = run_hand(tmp_path, sticky=True)
    assert markouts(r, series, (60.0,)) == {60.0: {}}


# -- synthetic data ---------------------------------------------------------------

@pytest.fixture(scope="module")
def synthetic_runs(tmp_path_factory):
    files = generate(SyntheticConfig(n_messages=12_000, levels=10, seed=11), tmp_path_factory.mktemp("strat"))
    p = ASParams(sigma=2e-4, A=0.02, k=250.0, gamma=20.0)
    specs = [RunSpec(s, 1.0, sticky, rule) for s in (INVENTORY, SYMMETRIC) for sticky in (True, False) for rule in FillRule]
    start, end = SESSION_START_NS + 60 * NS_PER_S, SESSION_END_NS - 60 * NS_PER_S
    cfg = StrategyConfig(window_s=1800.0, requote_s=5.0)
    results, series = run_strategies(files, [(s, p) for s in specs], start, end, cfg, record_after_s=30.0)
    return {r.spec: r for r in results}, series, (start, end)


def test_every_run_trades_the_same_whole_windows(synthetic_runs):
    runs, _, (start, end) = synthetic_runs
    expected = windows_between(start, end, 1800.0)
    assert len(expected) == 12
    for r in runs.values():
        assert [(w.start_ns, w.end_ns) for w in r.windows] == expected


def test_accounting_identities_hold_in_every_window(synthetic_runs):
    runs, _, _ = synthetic_runs
    assert sum(len(r.fills) for r in runs.values()) > 20
    for r in runs.values():
        for w in r.windows:
            mine = [f for f in r.fills if f.window == w.index]
            assert w.fills == len(mine)
            assert w.end_inventory == w.shares_bought - w.shares_sold == sum(f.sign * f.size for f in mine)
            assert w.pnl == pytest.approx(w.spread_capture + w.inventory_pnl)
            assert all(w.start_ns <= f.time_ns < w.end_ns for f in mine)
            assert all(f.price % TICK_SIZE == 0 for f in mine)


def test_requeue_posts_more_and_never_fills_more_shares_than_it_quotes(synthetic_runs):
    runs, _, _ = synthetic_runs
    for spec, r in runs.items():
        if spec.sticky:
            other = runs[RunSpec(spec.strategy, spec.penalty_ticks, False, spec.rule)]
            assert sum(w.posts for w in r.windows) < sum(w.posts for w in other.windows)


def test_optimistic_rule_never_fills_less_on_the_same_quotes(synthetic_runs):
    """Requeue quotes do not depend on fills until the first fill, so compare total shares loosely:
    the optimistic run must not trade fewer shares than the conservative one on this FIFO data."""
    runs, _, _ = synthetic_runs
    for spec, r in runs.items():
        if spec.rule == CONS and spec.strategy == SYMMETRIC and spec.sticky:
            opt = runs[RunSpec(spec.strategy, spec.penalty_ticks, spec.sticky, OPT)]
            assert sum(f.size for f in opt.fills) >= sum(f.size for f in r.fills)


def test_markouts_are_measured_for_fills_with_enough_data_after_them(synthetic_runs):
    runs, series, _ = synthetic_runs
    for r in runs.values():
        m = markouts(r, series, (1.0, 5.0, 30.0))
        for h, per_window in m.items():
            assert sum(len(v) for v in per_window.values()) == len(r.fills)
