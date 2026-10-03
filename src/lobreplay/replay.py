"""Replay a LOBSTER message file and validate against the orderbook file.

Phase 2 done-criterion: after EVERY message, our top-N book equals the
corresponding orderbook row, for the full day, for every stock used.

One exception, forced by the data: the message file omits events beyond the
top N levels, so a level that enters the view from outside is taken from the
orderbook file (OrderBook.resync) and counted. Every level that was already in
view must still be reproduced from the messages alone, or it is a divergence.

Seeding: the orderbook file gives the book *after* message 1, and orders
resting before the file starts have no SUBMIT message. So the initial book is
orderbook row 1 with message 1 undone, loaded as anonymous PREOPEN liquidity.
"""

from __future__ import annotations

import time
from collections import Counter
from dataclasses import dataclass, field
from itertools import zip_longest
from typing import Iterable

from .book import BookError, OrderBook
from .lobster_format import BOOK_EVENTS, Direction, EventType, format_price
from .parser import LobsterFiles, Message, Snapshot, format_time_ns, iter_messages, iter_orderbook


@dataclass
class Divergence:
    index: int          # 1-based message number == orderbook row number
    message: Message | None
    expected: Snapshot | None
    actual: Snapshot | None
    reason: str

    def describe(self) -> str:
        lines = [f"divergence at message {self.index}: {self.reason}"]
        if self.message is not None:
            m = self.message
            lines.append(
                f"  message: t={format_time_ns(m.time_ns)} type={m.event_type.name} id={m.order_id} "
                f"size={m.size} price={m.price} ({format_price(m.price)}) dir={m.direction.name}"
            )
        if self.expected is not None and self.actual is not None:
            lines.append(_side_by_side(self.expected, self.actual))
        return "\n".join(lines)


def _side_by_side(expected: Snapshot, actual: Snapshot) -> str:
    rows = ["  side lvl   expected (price x size)      ours (price x size)"]
    for name, exp, act in (("ask", expected.asks, actual.asks), ("bid", expected.bids, actual.bids)):
        for i, (e, a) in enumerate(zip_longest(exp, act), start=1):
            mark = "  " if e == a else "<>"
            rows.append(f"{mark}{name} {i:>3}   {_fmt_level(e):<26}   {_fmt_level(a)}")
    return "\n".join(rows)


def _fmt_level(lv: tuple[int, int] | None) -> str:
    return "-" if lv is None else f"{lv[0]} x {lv[1]}"


@dataclass
class ReplayResult:
    levels: int
    messages: int = 0
    event_counts: Counter = field(default_factory=Counter)
    divergences: list[Divergence] = field(default_factory=list)
    unseen_reductions: int = 0
    adopted_levels: int = 0
    identity_guesses: int = 0
    crossed_states: int = 0
    elapsed_s: float = 0.0

    @property
    def ok(self) -> bool:
        return not self.divergences

    def summary(self) -> str:
        lines = [
            f"messages replayed:  {self.messages}",
            f"levels compared:    {self.levels}",
            f"divergences:        {len(self.divergences)}",
            f"unseen reductions:  {self.unseen_reductions}  (unknown-ID events beyond the initial visible depth)",
            f"levels adopted:     {self.adopted_levels}  (entered the top {self.levels} from outside; size taken from the "
            "orderbook file, because the message file omits events out there)",
            f"identity guesses:   {self.identity_guesses}  (messages at such a level that did not fit our record of its orders)",
            f"crossed states:     {self.crossed_states}",
            f"elapsed:            {self.elapsed_s:.1f}s",
            "event counts:       " + ", ".join(f"{et.name}={self.event_counts.get(et, 0)}" for et in EventType),
            "RESULT: ZERO DIVERGENCES" if self.ok else "RESULT: DIVERGED",
        ]
        lines.extend(d.describe() for d in self.divergences)
        return "\n".join(lines)


def seed_book(first_msg: Message, first_row: Snapshot, levels: int) -> OrderBook:
    """Book state *before* message 1, from orderbook row 1 with message 1 undone."""
    sides = {Direction.SELL: dict(first_row.asks), Direction.BUY: dict(first_row.bids)}
    full = {Direction.SELL: len(first_row.asks) == levels, Direction.BUY: len(first_row.bids) == levels}

    if first_msg.event_type in BOOK_EVENTS:
        d = first_msg.direction
        state, price, size = sides[d], first_msg.price, first_msg.size
        beyond_view = full[d] and _worse(d, price, _worst(d, state))
        if not beyond_view:  # an event deeper than the visible depth leaves the visible state alone
            if first_msg.event_type == EventType.SUBMIT:
                before = state.get(price, 0) - size
                if before < 0:
                    raise BookError(f"message 1 adds {size} at {price} but row 1 shows only {state.get(price, 0)}")
                if before:
                    state[price] = before
                else:
                    del state[price]
            else:
                state[price] = state.get(price, 0) + size

    book = OrderBook()
    for d, state in sides.items():
        for price, size in state.items():
            book.seed_preopen(d, price, size)
        book.set_unseen_beyond(d, _worst(d, state) if full[d] and state else None)
    return book


def _worst(d: Direction, state: dict[int, int]) -> int:
    return min(state) if d == Direction.BUY else max(state)


def _worse(d: Direction, price: int, ref: int) -> bool:
    return price < ref if d == Direction.BUY else price > ref


def replay(
    messages: Iterable[Message],
    rows: Iterable[Snapshot],
    levels: int,
    max_divergences: int = 1,
) -> ReplayResult:
    """Replay messages, comparing top-`levels` after each against `rows`.

    Stops after `max_divergences` top-N mismatches, or immediately on a
    BookError (the book state is no longer meaningful after one).
    """
    res = ReplayResult(levels=levels)
    start = time.perf_counter()
    book: OrderBook | None = None
    prev: Snapshot | None = None

    for i, (msg, row) in enumerate(zip_longest(messages, rows), start=1):
        if msg is None or row is None:
            res.divergences.append(Divergence(i, msg, row, None, "message and orderbook files have different lengths"))
            break
        if book is None:
            try:
                book = seed_book(msg, row, levels)
            except BookError as exc:
                res.divergences.append(Divergence(i, msg, row, None, f"cannot seed initial book: {exc}"))
                break

        res.messages = i
        res.event_counts[msg.event_type] += 1
        try:
            book.apply(msg)
        except BookError as exc:
            res.divergences.append(Divergence(i, msg, row, book.top(levels), f"book error: {exc}"))
            break
        if prev is not None:
            book.resync(prev, row, levels)   # only levels that were out of view; see book.py
        prev = row

        if book.is_crossed():
            res.crossed_states += 1
        ours = book.top(levels)
        if ours != row:
            res.divergences.append(Divergence(i, msg, row, ours, "top-of-book mismatch"))
            if len(res.divergences) >= max_divergences:
                break

    if book is not None:
        res.unseen_reductions = book.unseen_reductions
        res.adopted_levels = book.adopted_levels
        res.identity_guesses = book.identity_guesses
    res.elapsed_s = time.perf_counter() - start
    return res


def replay_files(files: LobsterFiles, max_divergences: int = 1) -> ReplayResult:
    return replay(
        iter_messages(files.message_path),
        iter_orderbook(files.orderbook_path, files.levels),
        files.levels,
        max_divergences=max_divergences,
    )
