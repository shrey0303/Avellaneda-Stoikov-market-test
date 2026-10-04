"""One pass over a LOBSTER day: a seeded book with queue trackers kept in step.

Phases 4-6 all need the same loop (observe, apply, settle), so it lives here
once. A `before` hook for message k sees the book as it stood after message
k-1. It is handed message k so it knows what time it is acting at; a strategy
hook must use nothing else from it (shadow validation, which is not a
strategy, also reads which order is about to arrive).
"""

from __future__ import annotations

import itertools
from typing import Callable, Iterator

from .book import OrderBook
from .lobster_format import PRICE_SCALE, SESSION_END_S, SESSION_START_S, NS_PER_S
from .parser import LobsterFiles, Message, iter_messages, iter_orderbook
from .queue_tracker import FillRule, QueueTracker
from .replay import seed_book

SESSION_START_NS = SESSION_START_S * NS_PER_S
SESSION_END_NS = SESSION_END_S * NS_PER_S


def mid_units(book: OrderBook) -> float | None:
    """Mid price in LOBSTER price units (may end in .5), None if a side is empty."""
    b, a = book.bids.best(), book.asks.best()
    if b is None or a is None:
        return None
    return (a + b) / 2


def to_dollars(units: float) -> float:
    return units / PRICE_SCALE


class MarketReplay:
    """Iterating yields (k, msg) AFTER message k is applied and trackers have settled.

    `before` hooks run just before message k is observed: use them for anything
    that must act on the pre-message book (posting, timed requotes, closing a
    window). `mid_before` is the mid at that same moment.
    """

    def __init__(self, files: LobsterFiles):
        self.files = files
        msgs = iter_messages(files.message_path)
        rows = iter_orderbook(files.orderbook_path, files.levels)
        first, row = next(msgs), next(rows)
        self.book = seed_book(first, row, files.levels)
        self._msgs = itertools.chain([first], msgs)
        self._rows = itertools.chain([row], rows)   # needed for levels that enter the view (OrderBook.resync)
        self.trackers: list[QueueTracker] = []
        self.before: list[Callable[[int, Message], None]] = []
        self.k = 0
        self.mid_before: float | None = None

    def tracker(self, rule: FillRule) -> QueueTracker:
        tr = QueueTracker(self.book, rule)
        self.trackers.append(tr)
        return tr

    def __iter__(self) -> Iterator[tuple[int, Message]]:
        book, trackers, levels = self.book, self.trackers, self.files.levels
        prev = None
        # A file with fewer rows than messages (hand-built tests) is replayed from messages alone.
        for k, (m, row) in enumerate(zip(self._msgs, itertools.chain(self._rows, itertools.repeat(None))), start=1):
            self.mid_before = mid_units(book)
            for hook in self.before:
                hook(k, m)
            for tr in trackers:
                tr.observe(m, k)
            book.apply(m)
            if prev is not None and row is not None and book.resync(prev, row, levels):
                for tr in trackers:
                    tr.resynced(book.last_adopted)
            prev = row
            for tr in trackers:
                tr.settle()
            self.k = k
            yield k, m
