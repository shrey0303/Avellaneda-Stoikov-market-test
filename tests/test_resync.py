"""Levels that enter the view from beyond the top N (the message file omits events out there)."""

import pytest

from lobreplay.book import PREOPEN, BookError, OrderBook
from lobreplay.lobster_format import Direction, EventType
from lobreplay.parser import Message, Snapshot
from lobreplay.queue_tracker import FillRule, QueueTracker
from lobreplay.replay import replay

BUY, SELL = Direction.BUY, Direction.SELL
N = 2   # visible levels per side


def msg(et, oid, size, price, side, t=0):
    return Message(34_200_000_000_000 + t, EventType(et), oid, size, price, side)


def snap(asks, bids=((1000, 100),)):
    return Snapshot(tuple(asks), tuple(bids))


def book_with_asks(*levels):
    """Asks seeded as pre-open liquidity; one bid at 1000."""
    book = OrderBook()
    book.seed_preopen(BUY, 1000, 100)
    for price, size in levels:
        book.seed_preopen(SELL, price, size)
    return book


def test_a_level_that_left_while_out_of_view_is_removed_and_the_new_one_adopted():
    # We remember 1030 from when it was visible; the file now shows 1040 there instead.
    book = book_with_asks((1010, 100), (1020, 100), (1030, 500))
    prev = snap([(1010, 100), (1020, 100)])
    book.apply(msg(3, 7, 100, 1010, SELL))                     # unknown id: comes off the pre-open block
    row = snap([(1020, 100), (1040, 300)])
    assert book.resync(prev, row, N) == 2
    assert book.top(N) == row
    assert sorted(book.last_adopted) == [(SELL, 1030), (SELL, 1040)]
    assert book.asks.level(1040).uncertain and not book.asks.level(1020).uncertain


def test_levels_that_stayed_in_view_are_never_touched():
    book = book_with_asks((1010, 100), (1020, 100))
    prev = snap([(1010, 100), (1020, 100)])
    wrong = snap([(1010, 100), (1020, 999)])                   # the file disagrees at a level we could see
    assert book.resync(prev, wrong, N) == 0
    assert book.top(N) != wrong                                # ...so it stays a divergence


def test_nothing_is_adopted_when_the_whole_side_was_visible():
    book = book_with_asks((1010, 100))
    prev = snap([(1010, 100)])                                 # fewer than N levels: nothing was hidden
    assert book.resync(prev, snap([(1010, 100), (1050, 5)]), N) == 0
    assert book.asks.level(1050) is None


def test_shares_that_arrived_out_of_view_go_behind_the_orders_we_know():
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1030, 200)                               # seen while 1030 was... then it slid out
    prev = snap([(1010, 100), (1020, 100)])
    book.apply(msg(3, 7, 100, 1010, SELL))
    book.resync(prev, snap([(1020, 100), (1030, 350)]), N)
    assert book.queue(SELL, 1030)[0] == (5, 200)
    (anon, extra), = book.queue(SELL, 1030)[1:]
    assert anon < PREOPEN and extra == 150


def test_shares_that_left_out_of_view_collapse_the_level_to_one_anonymous_block():
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1030, 200)
    book.add(6, SELL, 1030, 200)
    prev = snap([(1010, 100), (1020, 100)])
    book.apply(msg(3, 7, 100, 1010, SELL))
    book.resync(prev, snap([(1020, 100), (1030, 250)]), N)
    (anon, size), = book.queue(SELL, 1030)
    assert anon < PREOPEN and size == 250
    assert book.order(5) is None and book.order(6) is None
    # a later message for a forgotten order is taken from the anonymous block
    book.apply(msg(3, 6, 200, 1030, SELL))
    assert book.top(N).asks == ((1020, 100), (1030, 50))


def test_an_unknown_id_at_an_uncertain_level_falls_back_to_a_known_order():
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1030, 200)
    prev = snap([(1010, 100), (1020, 100)])
    book.apply(msg(3, 7, 100, 1010, SELL))
    book.resync(prev, snap([(1020, 100), (1030, 300)]), N)      # 100 anonymous behind order 5
    assert book.unknown_plan(SELL, 1030, 250) == [(book.queue(SELL, 1030)[1][0], 100), (5, 150)]
    book.apply(msg(3, 99, 250, 1030, SELL))                    # really an order that replaced part of 5 out of view
    assert book.top(N).asks == ((1020, 100), (1030, 50)) and book.identity_guesses == 1


def test_a_stale_record_of_a_known_order_is_tolerated_only_at_an_uncertain_level():
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1020, 200)
    with pytest.raises(BookError):
        book.apply(msg(3, 5, 150, 1020, SELL))                 # in view all along: a real inconsistency
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1030, 200)
    book.asks.level(1030).uncertain = True
    book.apply(msg(3, 5, 150, 1030, SELL))                     # it was cut to 150 out of view, then deleted
    assert book.asks.level(1030).total == 50 and book.order(5) is None and book.identity_guesses == 1


def test_replay_adopts_entering_levels_and_still_catches_a_real_divergence():
    messages = [msg(1, 1, 50, 1005, SELL), msg(3, 1, 50, 1005, SELL), msg(3, 7, 100, 1010, SELL)]
    rows = [snap([(1005, 50), (1010, 100)]), snap([(1010, 100), (1020, 100)]), snap([(1020, 100), (1040, 300)])]
    res = replay(messages, rows, N)
    assert res.ok and res.adopted_levels == 2                  # 1020 at message 2, 1040 at message 3
    bad = rows[:2] + [snap([(1020, 777), (1040, 300)])]        # 1020 was in view: it must come from messages
    assert not replay(messages, bad, N).ok


def test_tracker_keeps_its_place_when_shares_arrive_out_of_view_and_is_conservative_when_they_leave():
    book = book_with_asks((1010, 100), (1020, 100))
    book.add(5, SELL, 1030, 200)
    tracker = QueueTracker(book, FillRule.CONSERVATIVE)
    ours = tracker.post(SELL, 1030, 100, 0, 0)
    assert ours.ahead == {5: 200}
    prev = snap([(1010, 100), (1020, 100)])
    m = msg(3, 7, 100, 1010, SELL)
    tracker.observe(m, 1)
    book.apply(m)
    book.resync(prev, snap([(1020, 100), (1030, 350)]), N)
    tracker.resynced(book.last_adopted)
    assert ours.ahead == {5: 200}                              # the 150 that arrived are behind us

    # A new ask at 1015 pushes 1030 out of view; when 1015 goes, 1030 comes back smaller.
    rows = [snap([(1020, 100), (1030, 350)]), snap([(1015, 10), (1020, 100)]), snap([(1020, 100), (1030, 120)])]
    for k, m in enumerate([msg(1, 8, 10, 1015, SELL), msg(3, 8, 10, 1015, SELL)], start=2):
        tracker.observe(m, k)
        book.apply(m)
        if book.resync(rows[k - 2], rows[k - 1], N):
            tracker.resynced(book.last_adopted)
    assert book.top(N) == rows[-1]
    assert ours.ahead_shares == 120                            # all that is left is assumed to be ahead of us
