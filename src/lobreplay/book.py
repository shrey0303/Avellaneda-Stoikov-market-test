"""Order-by-order limit order book driven by LOBSTER messages.

No matching happens here. LOBSTER messages are the exchange's matching
*output*: an aggressive order shows up as one EXEC_VISIBLE per resting order it
hit, then a SUBMIT for any unfilled remainder. So the book only adds, reduces
and removes orders by ID.

Each price level keeps its orders in arrival (time-priority) order, because
Phase 3's queue tracker needs to know exactly who is ahead of whom. A partial
cancel keeps an order's place, as on NASDAQ.

Orders resting before the file starts never appear as SUBMIT messages, so
their IDs are unknown. They are represented by one PREOPEN pseudo-order at the
front of each initially visible level (pre-open orders have time priority over
anything submitted later). Messages that reference an unknown ID reduce that
block. Levels beyond the initially visible depth were never seen at all;
unknown-ID reductions there are counted and ignored.

The message file only carries events inside the visible depth (the top N
levels at that moment). A level that slides out of view can change with no
message, and a level can appear from beyond the depth without ever having been
announced. So whenever a level enters the view from outside, resync() takes its
size from the orderbook file. Shares that arrived out of view become an
anonymous block at the back of the level; if shares left, we cannot know whose,
and the whole level becomes one anonymous block. Such a level is marked
uncertain: its total is right, the identity of its orders is a best guess.
Levels that have stayed in view are never touched by resync().
"""

from __future__ import annotations

import itertools
from bisect import bisect_left, bisect_right, insort
from dataclasses import dataclass, field

from .lobster_format import Direction, EventType
from .parser import Message, Snapshot

PREOPEN = -1  # pseudo order id for liquidity resting before the first message


class BookError(RuntimeError):
    """A message that is inconsistent with the current book state."""


@dataclass
class Level:
    price: int
    orders: dict[int, int] = field(default_factory=dict)  # order_id -> remaining size, FIFO; anonymous blocks have id < 0
    total: int = 0
    uncertain: bool = False   # has been out of view: the total is right, who holds it is a guess


class BookSide:
    def __init__(self, direction: Direction):
        self.direction = direction
        self.is_bid = direction == Direction.BUY
        self._prices: list[int] = []  # ascending
        self.levels: dict[int, Level] = {}
        # Prices strictly worse than this were beyond the visible depth when the
        # book was seeded; None means the whole side was visible.
        self.unseen_beyond: int | None = None

    def level(self, price: int) -> Level | None:
        return self.levels.get(price)

    def get_or_create(self, price: int) -> Level:
        lv = self.levels.get(price)
        if lv is None:
            lv = self.levels[price] = Level(price)
            insort(self._prices, price)
        return lv

    def remove_level(self, price: int) -> None:
        del self.levels[price]
        del self._prices[bisect_left(self._prices, price)]

    def best_prices(self, n: int) -> list[int]:
        if self.is_bid:
            return self._prices[: -n - 1 : -1] if n else []
        return self._prices[:n]

    def best(self) -> int | None:
        if not self._prices:
            return None
        return self._prices[-1] if self.is_bid else self._prices[0]

    def is_worse(self, price: int, ref: int) -> bool:
        """True if `price` is further from the market than `ref` on this side."""
        return price < ref if self.is_bid else price > ref

    def prices_worse_than(self, ref: int) -> list[int]:
        """Our level prices beyond `ref`, nearest first."""
        if self.is_bid:
            return self._prices[: bisect_left(self._prices, ref)][::-1]
        return self._prices[bisect_right(self._prices, ref):]

    def is_unseen(self, price: int) -> bool:
        if self.unseen_beyond is None:
            return False
        return self.is_worse(price, self.unseen_beyond)

    def top(self, n: int) -> tuple[tuple[int, int], ...]:
        return tuple((p, self.levels[p].total) for p in self.best_prices(n))


class OrderBook:
    def __init__(self) -> None:
        self.bids = BookSide(Direction.BUY)
        self.asks = BookSide(Direction.SELL)
        self._orders: dict[int, tuple[Direction, int]] = {}  # order_id -> (side, price)
        self.unseen_reductions = 0  # unknown-ID reductions beyond the seeded depth
        self._anon = itertools.count(PREOPEN - 1, -1)  # ids for anonymous blocks created by resync
        self.adopted_levels = 0     # levels whose size was taken from the orderbook file on entering the view
        self.identity_guesses = 0   # messages at an uncertain level that did not fit our record of its orders
        self.last_adopted: list[tuple[Direction, int]] = []  # (side, price) changed by the latest resync

    # -- levels entering the view --------------------------------------------

    def resync(self, prev: Snapshot, row: Snapshot, levels: int) -> int:
        """Take from the orderbook file every level that was out of view after the previous message.

        `prev` and `row` are the file's rows before and after the message just
        applied. Only prices beyond the worst level of `prev` are touched, and
        only when that side filled all `levels` (otherwise the whole side was
        visible and nothing can be unknown). Returns the number of levels changed.
        """
        if self.last_adopted:
            self.last_adopted = []
        for side, before, now in ((self.asks, prev.asks, row.asks), (self.bids, prev.bids, row.bids)):
            if len(before) < levels:
                continue
            edge = before[-1][0]
            limit = now[-1][0] if len(now) == levels else None   # None: the whole side is visible now
            if limit is not None and not side.is_worse(limit, edge):
                continue
            shown = {p: s for p, s in now if side.is_worse(p, edge)}
            for p in side.prices_worse_than(edge):
                if limit is not None and side.is_worse(p, limit):
                    break
                if p not in shown:
                    self._adopt(side, p, 0)   # it left while out of view
            for p, s in shown.items():
                self._adopt(side, p, s)
        return len(self.last_adopted)

    def _adopt(self, side: BookSide, price: int, size: int) -> None:
        lv = side.level(price)
        have = lv.total if lv else 0
        if lv:
            lv.uncertain = True
        if have == size:
            return
        if size < have:   # shares left out of view and we cannot know whose: forget who was there
            for oid in lv.orders:
                self._orders.pop(oid, None)
            side.remove_level(price)
            have = 0
        if size > have:   # whatever arrived out of view arrived after everything we know about
            lv = side.get_or_create(price)
            lv.uncertain = True
            lv.orders[next(self._anon)] = size - have
            lv.total = size
        self.adopted_levels += 1
        self.last_adopted.append((side.direction, price))

    # -- seeding -----------------------------------------------------------

    def side(self, direction: Direction) -> BookSide:
        return self.bids if direction == Direction.BUY else self.asks

    def seed_preopen(self, direction: Direction, price: int, size: int) -> None:
        if size <= 0:
            raise BookError(f"pre-open seed with size {size} at {price}")
        lv = self.side(direction).get_or_create(price)
        if lv.orders:
            raise BookError(f"pre-open seed at {price} on a non-empty level")
        lv.orders[PREOPEN] = size
        lv.total = size

    def set_unseen_beyond(self, direction: Direction, price: int | None) -> None:
        self.side(direction).unseen_beyond = price

    # -- message handling --------------------------------------------------

    def apply(self, msg: Message) -> None:
        et = msg.event_type
        if et == EventType.SUBMIT:
            self.add(msg.order_id, msg.direction, msg.price, msg.size)
        elif et == EventType.CANCEL or et == EventType.EXEC_VISIBLE:
            self.reduce(msg.order_id, msg.direction, msg.price, msg.size, full_delete=False)
        elif et == EventType.DELETE:
            self.reduce(msg.order_id, msg.direction, msg.price, msg.size, full_delete=True)
        # EXEC_HIDDEN, CROSS, HALT: visible book unchanged.

    def add(self, order_id: int, direction: Direction, price: int, size: int) -> None:
        if order_id in self._orders:
            raise BookError(f"order {order_id} submitted twice")
        if size <= 0:
            raise BookError(f"order {order_id} submitted with size {size}")
        lv = self.side(direction).get_or_create(price)
        lv.orders[order_id] = size
        lv.total += size
        self._orders[order_id] = (direction, price)

    def reduce(self, order_id: int, direction: Direction, price: int, size: int, *, full_delete: bool) -> None:
        side = self.side(direction)
        known = self._orders.get(order_id)

        if known is None:
            self._reduce_unknown(order_id, side, price, size)
            return

        if known != (direction, price):
            raise BookError(
                f"order {order_id} is resting at {known[1]} side {known[0].name}, "
                f"message says {price} side {direction.name}"
            )
        lv = side.levels[price]
        remaining = lv.orders[order_id]
        if size > remaining or (full_delete and size != remaining):
            if not lv.uncertain:
                if size > remaining:
                    raise BookError(f"order {order_id}: reduce by {size} but only {remaining} left")
                raise BookError(
                    f"order {order_id}: delete of {size} but {remaining} left "
                    "(check DELETE size semantics in docs/DATA_FORMAT.md)"
                )
            # The order changed while its level was out of view. Drop our stale record of it
            # and keep the level's total moving by exactly what the message says.
            self.identity_guesses += 1
            self._take(side, lv, order_id, remaining)
            del self._orders[order_id]
            if size > remaining:
                self._reduce_unknown(order_id, side, price, size - remaining)
            else:
                lv = side.get_or_create(price)
                lv.uncertain = True
                lv.orders[next(self._anon)] = remaining - size
                lv.total += remaining - size
            return
        self._take(side, lv, order_id, size)
        if order_id not in lv.orders:
            del self._orders[order_id]

    def unknown_plan(self, direction: Direction, price: int, size: int) -> list[tuple[int, int]]:
        """Which resting entries a reduction by an unknown order ID is taken from: (id, shares).

        Anonymous blocks first, oldest first. At an uncertain level, known
        orders after that, front first: one of them must be a stale record.
        """
        lv = self.side(direction).level(price)
        if lv is None:
            return []
        plan, left = [], size
        for anonymous in (True, False) if lv.uncertain else (True,):
            for oid, have in lv.orders.items():
                if not left:
                    return plan
                if (oid < 0) == anonymous:
                    take = min(have, left)
                    plan.append((oid, take))
                    left -= take
        return plan

    def _reduce_unknown(self, order_id: int, side: BookSide, price: int, size: int) -> None:
        plan = self.unknown_plan(side.direction, price, size)
        got = sum(take for _, take in plan)
        if got < size:
            if side.is_unseen(price):
                self.unseen_reductions += 1
                return
            raise BookError(
                f"unknown order {order_id} reduces {size} at {price} side {side.direction.name}, "
                f"but only {got} shares there can be anyone's but a known order's"
            )
        lv = side.levels[price]
        for oid, take in plan:
            self._take(side, lv, oid, take)
            if oid >= 0:
                self.identity_guesses += 1
                if oid not in lv.orders:
                    del self._orders[oid]

    @staticmethod
    def _take(side: BookSide, lv: Level, key: int, size: int) -> None:
        left = lv.orders[key] - size
        if left:
            lv.orders[key] = left
        else:
            del lv.orders[key]
        lv.total -= size
        if lv.total == 0:
            side.remove_level(lv.price)

    # -- queries -----------------------------------------------------------

    def top(self, n: int) -> Snapshot:
        return Snapshot(self.asks.top(n), self.bids.top(n))

    def is_crossed(self) -> bool:
        b, a = self.bids.best(), self.asks.best()
        return b is not None and a is not None and b >= a

    def queue(self, direction: Direction, price: int) -> list[tuple[int, int]]:
        """(order_id, remaining) at a level in time priority; PREOPEN first if present."""
        lv = self.side(direction).level(price)
        return list(lv.orders.items()) if lv else []

    def order(self, order_id: int) -> tuple[Direction, int, int] | None:
        """(side, price, remaining) for a resting known order, else None."""
        known = self._orders.get(order_id)
        if known is None:
            return None
        direction, price = known
        return direction, price, self.side(direction).levels[price].orders[order_id]

    def __len__(self) -> int:
        return len(self._orders)
