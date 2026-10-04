import random

import pytest

from lobreplay.book import OrderBook
from lobreplay.lobster_format import Direction, EventType
from lobreplay.parser import Message, iter_messages, iter_orderbook
from lobreplay.queue_tracker import FillReason, FillRule, QueueTracker, QuoteError
from lobreplay.replay import seed_book
from lobreplay.synthetic import SyntheticConfig, generate

BUY, SELL = Direction.BUY, Direction.SELL
CONS, OPT = FillRule.CONSERVATIVE, FillRule.OPTIMISTIC


def msg(et, oid, size, price, side):
    return Message(0, EventType(et), oid, size, price, side)


class Harness:
    """A book plus one tracker per rule, driven message by message."""

    def __init__(self):
        self.book = OrderBook()
        self.k = 0
        self.t = {rule: QueueTracker(self.book, rule) for rule in FillRule}

    def feed(self, *messages):
        for m in messages:
            self.k += 1
            for tr in self.t.values():
                tr.observe(m, self.k)
            self.book.apply(m)
            for tr in self.t.values():
                tr.settle()

    def post(self, side, price, size=100):
        return {rule: tr.post(side, price, size, self.k, 0) for rule, tr in self.t.items()}


def bid_level_with_three():
    """Bids at 1000: #1 x200, #2 x100, #3 x300. Best ask 1010."""
    h = Harness()
    h.feed(msg(1, 1, 200, 1000, BUY), msg(1, 2, 100, 1000, BUY), msg(1, 3, 300, 1000, BUY), msg(1, 9, 500, 1010, SELL))
    return h


def test_snapshot_puts_everything_present_ahead():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)[CONS]
    assert o.ahead == {1: 200, 2: 100, 3: 300}
    assert o.ahead_shares == 600


def test_executions_of_ahead_orders_shrink_queue_without_filling():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)
    h.feed(msg(4, 1, 200, 1000, BUY), msg(4, 2, 40, 1000, BUY))
    for rule in FillRule:
        assert o[rule].ahead == {2: 60, 3: 300}
        assert o[rule].fills == []


def test_cancels_and_deletes_ahead_shrink_queue():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)[CONS]
    h.feed(msg(2, 3, 100, 1000, BUY), msg(3, 1, 200, 1000, BUY))
    assert o.ahead == {2: 100, 3: 200}


def test_orders_arriving_later_are_behind_and_ignored():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)[CONS]
    h.feed(msg(1, 4, 500, 1000, BUY), msg(2, 4, 100, 1000, BUY), msg(3, 4, 400, 1000, BUY))
    assert o.ahead_shares == 600


def test_fill_only_after_queue_ahead_is_gone_both_rules():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)
    h.feed(msg(1, 4, 300, 1000, BUY))          # behind us
    h.feed(msg(4, 1, 200, 1000, BUY), msg(3, 2, 100, 1000, BUY), msg(4, 3, 300, 1000, BUY))
    for rule in FillRule:
        assert o[rule].ahead_shares == 0 and o[rule].fills == []
    h.feed(msg(4, 4, 150, 1000, BUY))          # the order behind us executes -> it was our fill
    for rule in FillRule:
        (f,) = o[rule].fills
        assert (f.size, f.price, f.reason, f.index) == (100, 1000, FillReason.QUEUE, 9)
        assert not o[rule].active


def test_partial_fills_accumulate():
    h = Harness()
    h.feed(msg(1, 9, 500, 1010, SELL))
    o = h.post(BUY, 1000)[CONS]              # alone at a fresh level
    h.feed(msg(1, 4, 300, 1000, BUY), msg(4, 4, 60, 1000, BUY))
    assert o.filled == 60 and o.remaining == 40
    h.feed(msg(4, 4, 100, 1000, BUY))
    assert [f.size for f in o.fills] == [60, 40] and not o.active


def test_trade_through_fills_everything_even_with_queue_ahead():
    h = bid_level_with_three()
    h.feed(msg(1, 5, 100, 990, BUY))
    o = h.post(BUY, 1000)
    h.feed(msg(4, 5, 100, 990, BUY))         # a bid BELOW ours traded: sellers went through 1000
    for rule in FillRule:
        (f,) = o[rule].fills
        assert (f.size, f.reason) == (100, FillReason.TRADE_THROUGH)


def test_ask_side_is_symmetric():
    h = Harness()
    h.feed(msg(1, 1, 100, 1010, SELL), msg(1, 2, 100, 1020, SELL), msg(1, 9, 100, 1000, BUY))
    o = h.post(SELL, 1010)[CONS]
    assert o.ahead == {1: 100}
    h.feed(msg(4, 2, 100, 1020, SELL))       # an ask ABOVE ours traded
    assert o.fills[0].reason == FillReason.TRADE_THROUGH


def test_hidden_executions_neither_shrink_nor_fill():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)
    h.feed(msg(5, 0, 600, 1000, BUY), msg(5, 0, 600, 990, BUY))
    for rule in FillRule:
        assert o[rule].ahead_shares == 600 and o[rule].fills == []


def test_preopen_liquidity_is_ahead_and_shrinks_with_unknown_ids():
    h = Harness()
    h.book.seed_preopen(BUY, 1000, 500)
    h.book.seed_preopen(SELL, 1010, 500)
    o = h.post(BUY, 1000)[CONS]
    assert o.ahead == {-1: 500}
    h.feed(msg(4, 777, 300, 1000, BUY), msg(3, 778, 200, 1000, BUY))
    assert o.ahead == {}
    h.feed(msg(1, 4, 100, 1000, BUY), msg(4, 4, 100, 1000, BUY))
    assert o.fills[0].reason == FillReason.QUEUE


def test_vacated_level_separates_the_rules():
    h = bid_level_with_three()
    h.feed(msg(1, 6, 100, 1005, BUY))        # a better bid above ours
    o = h.post(BUY, 1000)
    h.feed(msg(3, 1, 200, 1000, BUY), msg(3, 2, 100, 1000, BUY), msg(3, 3, 300, 1000, BUY))
    assert o[OPT].level_vacated and o[CONS].level_vacated
    h.feed(msg(4, 6, 100, 1005, BUY))        # a seller hits the better bid, not our price
    assert o[CONS].fills == []
    assert o[OPT].fills[0].reason == FillReason.VACATED


def test_fresh_level_is_not_vacated():
    h = Harness()
    h.feed(msg(1, 1, 100, 990, BUY), msg(1, 9, 100, 1010, SELL))
    o = h.post(BUY, 1000)[OPT]
    h.feed(msg(1, 2, 100, 980, BUY))
    assert not o.level_vacated


def test_cancelled_order_stops_filling_and_repost_goes_to_back():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)
    h.feed(msg(4, 1, 200, 1000, BUY))
    h.t[CONS].cancel(o[CONS])
    o2 = h.t[CONS].post(BUY, 1000, 100, h.k, 0)
    assert o2.ahead == {2: 100, 3: 300}       # what's there now, not our old place
    h.feed(msg(4, 2, 100, 1000, BUY), msg(4, 3, 300, 1000, BUY), msg(1, 4, 100, 1000, BUY), msg(4, 4, 100, 1000, BUY))
    assert o[CONS].fills == [] and o2.fills


def test_cancel_behind_us_changes_nothing():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)[CONS]
    h.feed(msg(1, 4, 100, 1000, BUY), msg(3, 4, 100, 1000, BUY))
    assert o.ahead_shares == 600 and o.fills == []


@pytest.mark.parametrize("side,price", [(BUY, 1010), (BUY, 1020), (SELL, 1000), (SELL, 990)])
def test_quotes_that_lock_or_cross_are_rejected(side, price):
    h = bid_level_with_three()
    with pytest.raises(QuoteError):
        h.post(side, price)


def test_priority_anomaly_counted_not_filled():
    h = bid_level_with_three()
    o = h.post(BUY, 1000)[CONS]
    h.feed(msg(1, 4, 100, 1000, BUY), msg(4, 4, 100, 1000, BUY))   # behind-us order executes first
    assert o.fills == [] and h.t[CONS].priority_anomalies == 1


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_on_synthetic_data_optimistic_never_fills_less(tmp_path, seed):
    files = generate(SyntheticConfig(n_messages=4000, levels=10, seed=seed), tmp_path)
    rng = random.Random(seed)
    msgs = iter_messages(files.message_path)
    rows = iter_orderbook(files.orderbook_path, files.levels)
    first, row = next(msgs), next(rows)
    book = seed_book(first, row, files.levels)
    trackers = {rule: QueueTracker(book, rule) for rule in FillRule}
    book.apply(first)
    pairs = []
    for k, m in enumerate(msgs, start=2):
        for tr in trackers.values():
            tr.observe(m, k)
        book.apply(m)
        for tr in trackers.values():
            tr.settle()
        if rng.random() < 0.02:
            side = rng.choice((BUY, SELL))
            best = book.side(side).best()
            if best is not None:
                pairs.append(tuple(tr.post(side, best, 100, k, m.time_ns) for tr in trackers.values()))
    assert len(pairs) > 20
    filled_any = 0
    for cons, opt in pairs:
        assert cons.filled <= opt.filled
        assert all(f.price == cons.price for f in cons.fills + opt.fills)
        assert cons.filled <= cons.size
        filled_any += cons.filled > 0
    assert filled_any > 0
    assert trackers[FillRule.CONSERVATIVE].priority_anomalies == 0  # synthetic book is strict FIFO
