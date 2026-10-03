"""Placeholder data: synthetic message/orderbook files in LOBSTER format.

Used until the real LOBSTER sample is downloaded, and in tests. It keeps its
own deliberately simple book (independent of book.py), so a zero-divergence
replay of this data is a real cross-check, not code agreeing with itself.

It mimics the awkward parts of real data that matter for reconstruction:
  * orders resting before the first message (no SUBMIT, IDs never announced),
  * sweeps that hit several resting orders at one timestamp,
  * partial cancels, odd lots, hidden executions, a cross and a halt.

It does NOT mimic real order flow statistically. Nothing measured on this
data means anything about markets.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from pathlib import Path

from .lobster_format import (
    DUMMY_ASK_PRICE,
    DUMMY_BID_PRICE,
    DUMMY_SIZE,
    HALT_PRICE_HALTED,
    HALT_PRICE_QUOTING,
    HALT_PRICE_RESUMED,
    NS_PER_S,
    SESSION_END_S,
    SESSION_START_S,
    Direction,
    EventType,
)
from .parser import LobsterFiles, format_time_ns

BUY, SELL = Direction.BUY, Direction.SELL
ROUND_LOTS = (100, 100, 100, 200, 200, 300, 500, 1000)


@dataclass
class SyntheticConfig:
    ticker: str = "FAKE"
    date: str = "2012-06-21"
    levels: int = 10
    n_messages: int = 20_000
    seed: int = 0
    start_price: int = 5_850_000   # $585.00
    tick: int = 100                # $0.01
    preopen_levels: int | None = None  # price levels per side resting before the first message; default = levels
    p_submit: float = 0.46
    p_cancel: float = 0.12
    p_delete: float = 0.25
    p_market: float = 0.12
    p_hidden: float = 0.05
    # Submissions outnumber removals, so without a cap the queues at the touch grow all day
    # until no market order can clear them and the mid stops moving.
    max_resting_orders: int = 120


class _SimpleBook:
    """Price -> FIFO list of [order_id, size]. Intentionally naive."""

    def __init__(self) -> None:
        self.levels = {BUY: {}, SELL: {}}
        self.where: dict[int, tuple[Direction, int]] = {}
        self._live: list[int] = []          # for O(1) random choice
        self._live_pos: dict[int, int] = {}

    def add(self, oid: int, side: Direction, price: int, size: int) -> None:
        self.levels[side].setdefault(price, []).append([oid, size])
        self.where[oid] = (side, price)
        self._live_pos[oid] = len(self._live)
        self._live.append(oid)

    def random_order(self, rng: random.Random) -> int | None:
        return rng.choice(self._live) if self._live else None

    def _forget(self, oid: int) -> None:
        del self.where[oid]
        i = self._live_pos.pop(oid)
        last = self._live.pop()
        if last != oid:
            self._live[i] = last
            self._live_pos[last] = i

    def reduce(self, oid: int, size: int) -> None:
        side, price = self.where[oid]
        queue = self.levels[side][price]
        for entry in queue:
            if entry[0] == oid:
                entry[1] -= size
                if entry[1] == 0:
                    queue.remove(entry)
                    self._forget(oid)
                break
        if not queue:
            del self.levels[side][price]

    def best(self, side: Direction) -> int | None:
        lv = self.levels[side]
        if not lv:
            return None
        return max(lv) if side == BUY else min(lv)

    def top(self, side: Direction, n: int) -> list[tuple[int, int]]:
        prices = sorted(self.levels[side], reverse=(side == BUY))[:n]
        return [(p, sum(s for _, s in self.levels[side][p])) for p in prices]


def generate(cfg: SyntheticConfig, out_dir: str | Path) -> LobsterFiles:
    rng = random.Random(cfg.seed)
    book = _SimpleBook()
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = f"{cfg.ticker}_{cfg.date}_{SESSION_START_S * 1000}_{SESSION_END_S * 1000}"
    msg_path = out_dir / f"{stem}_message_{cfg.levels}.csv"
    ob_path = out_dir / f"{stem}_orderbook_{cfg.levels}.csv"

    # Pre-open book: IDs 1.. are never announced in the message file.
    next_preopen_id = 1
    for side, sign in ((BUY, -1), (SELL, 1)):
        for k in range(1, (cfg.preopen_levels or cfg.levels) + 1):
            for _ in range(rng.randint(1, 4)):
                book.add(next_preopen_id, side, cfg.start_price + sign * k * cfg.tick, rng.choice(ROUND_LOTS))
                next_preopen_id += 1

    next_id = 10_000_000
    t = SESSION_START_S * NS_PER_S
    mean_gap = (SESSION_END_S - SESSION_START_S) * NS_PER_S / max(cfg.n_messages, 1)
    halt_at = cfg.n_messages // 2
    halted = False
    written = 0

    with open(msg_path, "w", newline="") as mf, open(ob_path, "w", newline="") as of:

        def emit(et: EventType, oid: int, size: int, price: int, side: Direction) -> None:
            nonlocal written
            mf.write(f"{format_time_ns(t)},{int(et)},{oid},{size},{price},{int(side)}\n")
            of.write(_orderbook_row(book, cfg.levels) + "\n")
            written += 1

        # Opening cross first: book unchanged, so row 1 shows the pre-open book exactly.
        emit(EventType.CROSS, 0, rng.choice(ROUND_LOTS), cfg.start_price, BUY)

        while written < cfg.n_messages:
            t += max(1, int(rng.expovariate(1 / mean_gap)))

            if written >= halt_at and not halted:  # a sweep may jump past halt_at
                halted = True
                for code in (HALT_PRICE_HALTED, HALT_PRICE_QUOTING, HALT_PRICE_RESUMED):
                    if written < cfg.n_messages:
                        emit(EventType.HALT, 0, 0, code, SELL)
                continue

            r = rng.random()
            if r < cfg.p_submit and len(book.where) >= cfg.max_resting_orders:
                r = cfg.p_submit + cfg.p_cancel   # book is full: delete a resting order instead
            if r < cfg.p_submit:
                side = rng.choice((BUY, SELL))
                price = _submit_price(rng, book, side, cfg)
                size = rng.choice(ROUND_LOTS) if rng.random() > 0.05 else rng.randint(1, 99)
                book.add(next_id, side, price, size)
                emit(EventType.SUBMIT, next_id, size, price, side)
                next_id += 1
            elif r < cfg.p_submit + cfg.p_cancel + cfg.p_delete:
                oid = book.random_order(rng)
                if oid is None:
                    continue
                side, price = book.where[oid]
                remaining = next(s for o, s in book.levels[side][price] if o == oid)
                if r < cfg.p_submit + cfg.p_cancel and remaining > 1:
                    size = rng.randint(1, remaining - 1)
                    book.reduce(oid, size)
                    emit(EventType.CANCEL, oid, size, price, side)
                else:
                    book.reduce(oid, remaining)
                    emit(EventType.DELETE, oid, remaining, price, side)
            elif r < cfg.p_submit + cfg.p_cancel + cfg.p_delete + cfg.p_market:
                # Market order: resting side is the opposite of the aggressor; one
                # EXEC_VISIBLE per resting order hit, all at the same timestamp.
                resting = rng.choice((BUY, SELL))
                want = rng.choice(ROUND_LOTS)
                while want and written < cfg.n_messages:
                    best = book.best(resting)
                    if best is None:
                        break
                    oid, size = book.levels[resting][best][0]
                    fill = min(size, want)
                    book.reduce(oid, fill)
                    emit(EventType.EXEC_VISIBLE, oid, fill, best, resting)
                    want -= fill
            else:
                mid = _mid(book, cfg)
                emit(EventType.EXEC_HIDDEN, 0, rng.choice(ROUND_LOTS), mid - mid % cfg.tick, rng.choice((BUY, SELL)))

    return LobsterFiles(cfg.ticker, cfg.date, cfg.levels, msg_path, ob_path)


def _mid(book: _SimpleBook, cfg: SyntheticConfig) -> int:
    b, a = book.best(BUY), book.best(SELL)
    if b is None and a is None:
        return cfg.start_price
    if b is None:
        return a - cfg.tick
    if a is None:
        return b + cfg.tick
    return (a + b) // 2


def _submit_price(rng: random.Random, book: _SimpleBook, side: Direction, cfg: SyntheticConfig) -> int:
    """Passive price: never crosses the opposite best; mostly near the touch."""
    depth = min(int(rng.expovariate(0.4)), 3 * cfg.levels)
    if side == BUY:
        ask = book.best(SELL)
        limit = (ask if ask is not None else _mid(book, cfg) + cfg.tick) - cfg.tick
        return max(cfg.tick, limit - depth * cfg.tick)
    bid = book.best(BUY)
    limit = (bid if bid is not None else _mid(book, cfg) - cfg.tick) + cfg.tick
    return limit + depth * cfg.tick


def _orderbook_row(book: _SimpleBook, levels: int) -> str:
    asks = book.top(SELL, levels)
    bids = book.top(BUY, levels)
    cells: list[str] = []
    for i in range(levels):
        ap, az = asks[i] if i < len(asks) else (DUMMY_ASK_PRICE, DUMMY_SIZE)
        bp, bz = bids[i] if i < len(bids) else (DUMMY_BID_PRICE, DUMMY_SIZE)
        cells += (str(ap), str(az), str(bp), str(bz))
    return ",".join(cells)
