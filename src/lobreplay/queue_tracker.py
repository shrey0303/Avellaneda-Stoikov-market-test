"""Phase 3: track a hypothetical order's place in the real queue.

A hypothetical order never enters the book; history can't react to it. We only
ask: *if* it had been resting here, behind these real orders, when would it
have filled? (approach document §5.2)

  1. On post, snapshot the real orders resting at our price on our side. All of
     them are ahead of us. Orders arriving later are behind us and ignored.
  2. As those ahead orders execute, partially cancel or are deleted, shrink the
     "ahead" set by exactly that size.
  3. Decide fills under one of two rules (run both, report both):

     CONSERVATIVE  ahead is empty AND a real visible execution happens at our
                   price on our side (we take the fill an order behind us got),
                   OR the market trades through our price.
     OPTIMISTIC    as conservative, plus: once our price level has emptied
                   while we still rest, the next visible execution against our
                   side at ANY price fills all we have left.

  Hidden executions (EXEC_HIDDEN) neither shrink the queue nor fill us.
  Cancelling and re-posting puts us at the back: post a new order.

Usage, per message, for each tracker:  tracker.observe(msg, k); book.apply(msg);
tracker.settle(). observe() must see the book *before* the message is applied,
because that is how an unknown order ID (pre-open liquidity) is recognised.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass, field
from enum import Enum

from .book import PREOPEN, OrderBook
from .lobster_format import Direction, EventType
from .parser import Message


class FillRule(Enum):
    CONSERVATIVE = "conservative"
    OPTIMISTIC = "optimistic"


class FillReason(Enum):
    QUEUE = "queue"                  # front of queue, real execution at our price
    TRADE_THROUGH = "trade_through"  # market traded at a worse price than ours
    VACATED = "vacated"              # optimistic only: level emptied, next execution against our side


@dataclass(frozen=True)
class Fill:
    index: int        # 1-based message number that produced the fill
    time_ns: int
    price: int
    size: int
    reason: FillReason
    order_id: int = 0  # the hypothetical order that was filled


@dataclass
class HypotheticalOrder:
    order_id: int
    side: Direction
    price: int
    size: int
    posted_index: int
    posted_ns: int
    ahead: dict[int, int]                        # real order_id -> shares still ahead of us (PREOPEN included)
    remaining: int = 0
    fills: list[Fill] = field(default_factory=list)
    level_seen: bool = False      # real orders have rested at our price while we were there
    level_vacated: bool = False   # ...and then all of them left
    cancelled: bool = False
    anomalies: int = 0            # priority anomalies seen by this order

    def __post_init__(self) -> None:
        self.remaining = self.size

    @property
    def ahead_shares(self) -> int:
        return sum(self.ahead.values())

    @property
    def filled(self) -> int:
        return self.size - self.remaining

    @property
    def active(self) -> bool:
        return self.remaining > 0 and not self.cancelled

    def is_worse(self, price: int) -> bool:
        """True if `price` is beyond ours from the market's side: below our bid, above our ask."""
        return price < self.price if self.side == Direction.BUY else price > self.price


class QuoteError(ValueError):
    """A hypothetical quote that would lock or cross the real book."""


class QueueTracker:
    def __init__(self, book: OrderBook, rule: FillRule):
        self.book = book
        self.rule = rule
        self.orders: list[HypotheticalOrder] = []
        self._live: list[HypotheticalOrder] = []  # superset of the active orders; pruned lazily
        self._ids = itertools.count(1)
        self.last_fills: list[Fill] = []  # fills produced by the most recent observe()
        # Executions at our price of an order NOT ahead of us while shares are still
        # ahead: impossible under strict FIFO, so it means our picture of the queue
        # was wrong (hidden priority, odd lots, ...). Counted, never filled.
        self.priority_anomalies = 0

    # -- strategy side ----------------------------------------------------

    def post(self, side: Direction, price: int, size: int, index: int, time_ns: int) -> HypotheticalOrder:
        """Rest a hypothetical order behind everything currently at `price`.

        Call between messages: after message `index` has been applied.
        """
        if size <= 0:
            raise ValueError(f"size must be positive, got {size}")
        opposite = self.book.asks if side == Direction.BUY else self.book.bids
        best_opp = opposite.best()
        if best_opp is not None and (price >= best_opp if side == Direction.BUY else price <= best_opp):
            raise QuoteError(f"{side.name} at {price} would lock or cross the opposite best {best_opp}")
        ahead = dict(self.book.queue(side, price))
        order = HypotheticalOrder(next(self._ids), side, price, size, index, time_ns, ahead)
        order.level_seen = bool(ahead)
        self.orders.append(order)
        self._live = [o for o in self._live if o.active]
        self._live.append(order)
        return order

    def cancel(self, order: HypotheticalOrder) -> None:
        order.cancelled = True

    def active_orders(self) -> list[HypotheticalOrder]:
        return [o for o in self._live if o.active]

    # -- per-message hooks ------------------------------------------------

    def observe(self, msg: Message, index: int) -> list[Fill]:
        """Update every active order for message `index`. Call BEFORE book.apply(msg)."""
        et = msg.event_type
        new_fills: list[Fill] = []
        self.last_fills = new_fills
        if et not in (EventType.CANCEL, EventType.DELETE, EventType.EXEC_VISIBLE):
            return new_fills  # submits are behind us; hidden/cross/halt don't touch the visible queue
        # An unknown ID is taken from anonymous liquidity; ask the book which blocks it will use.
        plan = () if self.book.order(msg.order_id) else self.book.unknown_plan(msg.direction, msg.price, msg.size)
        for o in self._live:
            if msg.direction != o.side or not o.active:
                continue
            fill = self._observe_one(o, msg, index, plan)
            if fill:
                o.fills.append(fill)
                o.remaining -= fill.size
                new_fills.append(fill)
        return new_fills

    def resynced(self, changed: list[tuple[Direction, int]]) -> None:
        """The book took these (side, price) levels from the orderbook file; bring `ahead` back in line.

        Entries that are gone from the level are dropped. If the level was
        collapsed into one anonymous block, we assume the shares that left were
        behind us, which keeps as much ahead of us as can still be there.
        """
        for o in self._live:
            if not o.active or (o.side, o.price) not in changed:
                continue
            queue = dict(self.book.queue(o.side, o.price))
            before = o.ahead_shares
            o.ahead = {key: min(size, queue[key]) for key, size in o.ahead.items() if key in queue}
            if before > o.ahead_shares and len(queue) == 1:
                (key, size), = queue.items()
                if key not in o.ahead:
                    o.ahead[key] = min(before, size)

    def settle(self) -> None:
        """Record levels that emptied under us. Call AFTER book.apply(msg).

        A level we posted into while it was empty only counts as vacated once
        real orders have joined it and then all left.
        """
        for o in self._live:
            if o.level_vacated or not o.active:
                continue
            if self.book.side(o.side).level(o.price) is not None:
                o.level_seen = True
            elif o.level_seen:
                o.level_vacated = True

    # -- rules -------------------------------------------------------------

    def _observe_one(self, o: HypotheticalOrder, msg: Message, index: int, plan) -> Fill | None:
        is_exec = msg.event_type == EventType.EXEC_VISIBLE

        if msg.price == o.price:
            if msg.order_id in o.ahead:
                hits = [(msg.order_id, msg.size)]
            else:
                hits = [(key, take) for key, take in plan if key in o.ahead]
            if hits:
                for key, take in hits:
                    left = o.ahead[key] - take
                    if left > 0:
                        o.ahead[key] = left
                    else:
                        del o.ahead[key]
                return None
            if not is_exec:
                return None  # a cancel behind us changes nothing
            if o.ahead_shares:
                self.priority_anomalies += 1
                o.anomalies += 1
                return None
            return Fill(index, msg.time_ns, o.price, min(msg.size, o.remaining), FillReason.QUEUE, o.order_id)

        if not is_exec:
            return None
        if o.is_worse(msg.price):
            return Fill(index, msg.time_ns, o.price, o.remaining, FillReason.TRADE_THROUGH, o.order_id)
        if self.rule == FillRule.OPTIMISTIC and o.level_vacated:
            return Fill(index, msg.time_ns, o.price, o.remaining, FillReason.VACATED, o.order_id)
        return None
