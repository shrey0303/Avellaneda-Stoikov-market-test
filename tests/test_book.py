import pytest

from lobreplay.book import PREOPEN, BookError, OrderBook
from lobreplay.lobster_format import Direction, EventType
from lobreplay.parser import Message

BUY, SELL = Direction.BUY, Direction.SELL


def msg(et, oid, size, price, side, t=0):
    return Message(t, EventType(et), oid, size, price, side)


def test_add_and_top_ordering():
    b = OrderBook()
    b.apply(msg(1, 1, 100, 1000, BUY))
    b.apply(msg(1, 2, 200, 1010, BUY))
    b.apply(msg(1, 3, 50, 1020, SELL))
    b.apply(msg(1, 4, 70, 1030, SELL))
    b.apply(msg(1, 5, 30, 1010, BUY))
    top = b.top(5)
    assert top.bids == ((1010, 230), (1000, 100))
    assert top.asks == ((1020, 50), (1030, 70))
    assert b.top(1).bids == ((1010, 230),)


def test_fifo_queue_and_partial_cancel_keeps_priority():
    b = OrderBook()
    for oid in (1, 2, 3):
        b.apply(msg(1, oid, 100, 1000, BUY))
    b.apply(msg(2, 1, 40, 1000, BUY))   # partial cancel: stays first
    assert b.queue(BUY, 1000) == [(1, 60), (2, 100), (3, 100)]
    b.apply(msg(4, 1, 60, 1000, BUY))   # executed fully
    b.apply(msg(3, 3, 100, 1000, BUY))  # deleted
    assert b.queue(BUY, 1000) == [(2, 100)]
    assert b.order(1) is None and b.order(2) == (BUY, 1000, 100)


def test_level_removed_when_empty():
    b = OrderBook()
    b.apply(msg(1, 1, 100, 1000, SELL))
    b.apply(msg(4, 1, 100, 1000, SELL))
    assert b.top(5).asks == ()
    assert len(b) == 0


def test_hidden_cross_halt_do_not_touch_book():
    b = OrderBook()
    b.apply(msg(1, 1, 100, 1000, BUY))
    before = b.top(5)
    b.apply(msg(5, 0, 300, 1000, BUY))
    b.apply(msg(6, 0, 300, 1000, BUY))
    b.apply(msg(7, 0, 0, -1, SELL))
    assert b.top(5) == before


@pytest.mark.parametrize(
    "bad",
    [
        msg(1, 1, 100, 1000, BUY),           # duplicate id
        msg(2, 1, 101, 1000, BUY),           # cancel more than resting
        msg(3, 1, 50, 1000, BUY),            # delete size != remaining
        msg(4, 1, 100, 1001, BUY),           # wrong price
        msg(4, 1, 100, 1000, SELL),          # wrong side
    ],
)
def test_inconsistent_messages_raise(bad):
    b = OrderBook()
    b.apply(msg(1, 1, 100, 1000, BUY))
    with pytest.raises(BookError):
        b.apply(bad)


def test_unknown_ids_consume_preopen_block_first_in_queue():
    b = OrderBook()
    b.seed_preopen(BUY, 1000, 500)
    b.apply(msg(1, 10, 100, 1000, BUY))       # arrives behind pre-open liquidity
    assert b.queue(BUY, 1000) == [(PREOPEN, 500), (10, 100)]
    b.apply(msg(4, 999, 200, 1000, BUY))      # unknown id executes against the block
    b.apply(msg(3, 998, 300, 1000, BUY))      # unknown id deletes the rest
    assert b.queue(BUY, 1000) == [(10, 100)]
    assert b.top(1).bids == ((1000, 100),)


def test_unknown_id_beyond_preopen_block_raises():
    b = OrderBook()
    b.seed_preopen(SELL, 1000, 100)
    b.set_unseen_beyond(SELL, 1000)
    with pytest.raises(BookError):
        b.apply(msg(2, 999, 150, 1000, SELL))


def test_unknown_id_at_unseen_depth_is_counted_not_raised():
    b = OrderBook()
    b.seed_preopen(SELL, 1000, 100)
    b.set_unseen_beyond(SELL, 1000)           # asks above 1000 were never visible
    b.apply(msg(3, 999, 100, 1050, SELL))
    assert b.unseen_reductions == 1
    with pytest.raises(BookError):            # but inside the visible range it is an error
        b.apply(msg(3, 998, 100, 990, SELL))


def test_crossed_detection():
    b = OrderBook()
    b.apply(msg(1, 1, 100, 1000, BUY))
    b.apply(msg(1, 2, 100, 1001, SELL))
    assert not b.is_crossed()
    b.apply(msg(1, 3, 100, 1001, BUY))
    assert b.is_crossed()
