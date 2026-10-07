"""Phase 6: run the A-S strategies against the replay (approach document §5.5).

Each run is one (strategy, risk aversion, queue mode, fill rule) combination
with its own queue tracker, so many runs share a single pass over the day.

A run quotes one lot per side. It requotes on a fixed interval and after each
of its fills. In sticky mode an order whose desired price has not changed is
left alone and keeps its place in the queue; in requeue mode it is cancelled
and re-posted at every requote, which sends it to the back (the Q4 ablation).

The day is cut into fixed windows. Each window is an independent session:
inventory starts at zero, the A-S horizon T is the window's end, and whatever
inventory is left is marked at the mid when the window closes.

    window P&L      = cash + inventory * closing mid
    spread capture  = sum over fills of (mid just before the fill - price), signed so
                      that buying below the mid and selling above it are positive
    inventory P&L   = window P&L - spread capture   (what the mid did while we held)

Every fill is booked at its own price. Only the shares left at the close have
no trade price, so the window's profit is reported three ways:

    realised P&L    completed buy-and-sell pairs only, matched first in, first out
    window P&L      realised + leftover valued at the closing mid (the figure above)
    closed P&L      realised + leftover traded out against the real book at the close:
                    sold into the bids or bought from the asks, level by level
"""

from __future__ import annotations

import math
from collections import deque
from dataclasses import dataclass, field

from . import as_model
from .as_model import ASParams
from .book import OrderBook
from .calibration import MidSeries
from .lobster_format import NS_PER_S, PRICE_SCALE, TICK_SIZE, Direction
from .parser import LobsterFiles
from .queue_tracker import Fill, FillRule, HypotheticalOrder, QueueTracker
from .session import MarketReplay, mid_units
from .signals import LiveSignals, SkewModel

BUY, SELL = Direction.BUY, Direction.SELL
# The inventory strategy with both quotes shifted by a signal's fitted price move (signals.py).
# It is not an A-S strategy, so it has no model-world counterpart.
SIGNAL = "signal"
_TIE = 1e-6  # price units; a quote within this of a tick is treated as on it, whatever the inventory


def bid_to_tick(dollars: float) -> int:
    """Round a continuous bid DOWN to the tick grid. Takes no inventory argument on purpose."""
    return math.floor((dollars * PRICE_SCALE + _TIE) / TICK_SIZE) * TICK_SIZE


def ask_to_tick(dollars: float) -> int:
    """Round a continuous ask UP to the tick grid."""
    return math.ceil((dollars * PRICE_SCALE - _TIE) / TICK_SIZE) * TICK_SIZE


@dataclass(frozen=True)
class RunSpec:
    strategy: str           # as_model.INVENTORY, as_model.SYMMETRIC or SIGNAL
    penalty_ticks: float    # risk-aversion setting, see as_model.gamma_for_penalty
    sticky: bool
    rule: FillRule

    @property
    def label(self) -> str:
        queue = "sticky" if self.sticky else "requeue"
        return f"{self.strategy}/{self.penalty_ticks:g}t/{queue}/{self.rule.value}"


@dataclass(frozen=True)
class StrategyConfig:
    window_s: float = 1800.0
    requote_s: float = 1.0
    lot: int = 100


@dataclass(frozen=True)
class FillRecord:
    window: int
    time_ns: int
    sign: int               # +1 we bought, -1 we sold
    price: int
    size: int
    mid_before: float       # price units


@dataclass
class WindowResult:
    index: int
    start_ns: int
    end_ns: int
    pnl: float = 0.0             # dollars; leftover shares valued at the closing mid
    realised_pnl: float = 0.0    # dollars; completed buy-and-sell pairs only
    closed_pnl: float = 0.0      # dollars; leftover shares traded out against the real book at the close
    spread_capture: float = 0.0  # dollars
    inventory_pnl: float = 0.0   # dollars
    fills: int = 0
    shares_bought: int = 0
    shares_sold: int = 0
    end_inventory: int = 0       # shares
    posts: int = 0               # hypothetical orders posted
    overtaken: int = 0           # requotes that found our resting order locked or crossed by the real book
    skew_moved: int = 0          # SIGNAL only: requotes where the skew changed a quote by at least a tick


@dataclass
class RunResult:
    spec: RunSpec
    params: ASParams
    windows: list[WindowResult] = field(default_factory=list)
    fills: list[FillRecord] = field(default_factory=list)


class QuotingRun:
    def __init__(self, spec: RunSpec, params: ASParams, tracker: QueueTracker, book: OrderBook, cfg: StrategyConfig,
                 skew=None):
        self.spec, self.params, self.tracker, self.book, self.cfg = spec, params, tracker, book, cfg
        self.skew = skew       # time_ns -> expected mid move in dollars; used by SIGNAL runs only
        self.result = RunResult(spec, params)
        self.window: WindowResult | None = None
        self.orders: dict[Direction, HypotheticalOrder | None] = {BUY: None, SELL: None}
        self.shares = 0
        self.cash = 0          # price units * shares, exact
        self.capture = 0.0     # price units * shares
        self.realised = 0      # price units * shares, exact
        self.lots: deque[list[int]] = deque()   # open [signed shares, price], oldest first

    def open_window(self, index: int, start_ns: int, end_ns: int) -> None:
        self.window = WindowResult(index, start_ns, end_ns)
        self.shares, self.cash, self.capture, self.realised = 0, 0, 0.0, 0
        self.lots.clear()

    def _match(self, sign: int, price: int, size: int) -> None:
        """Close the oldest opposite lots with this fill; whatever is left opens a new lot."""
        lots = self.lots
        while size and lots and lots[0][0] * sign < 0:
            lot = lots[0]
            n = min(size, abs(lot[0]))
            self.realised += n * (price - lot[1]) * (1 if lot[0] > 0 else -1)   # sell price minus buy price
            lot[0] += sign * n
            size -= n
            if lot[0] == 0:
                lots.popleft()
        if size:
            lots.append([sign * size, price])

    def _closing_cash(self, mark: float) -> float:
        """Cash from trading the leftover shares out against the book as it stands, walking down the levels.

        Shares beyond the levels we hold go at the last price reached; with an empty side, at the mid.
        """
        left = abs(self.shares)
        if not left:
            return 0.0
        side = self.book.bids if self.shares > 0 else self.book.asks   # long: sell into bids; short: buy from asks
        sign = 1 if self.shares > 0 else -1
        cash, price = 0.0, mark
        for price in side.best_prices(len(side.levels)):
            n = min(left, side.levels[price].total)
            cash += sign * n * price
            left -= n
            if not left:
                return cash
        return cash + sign * left * price

    def close_window(self, mid: float | None) -> None:
        w = self.window
        if w is None:
            return
        for side in (BUY, SELL):
            self._cancel(side)
        mark = mid if mid is not None else 0.0   # no mid ever seen: nothing can have traded either
        w.pnl = (self.cash + self.shares * mark) / PRICE_SCALE
        w.realised_pnl = self.realised / PRICE_SCALE
        w.closed_pnl = (self.cash + self._closing_cash(mark)) / PRICE_SCALE
        w.spread_capture = self.capture / PRICE_SCALE
        w.inventory_pnl = w.pnl - w.spread_capture
        w.end_inventory = self.shares
        self.result.windows.append(w)
        self.window = None

    def requote(self, index: int, time_ns: int) -> None:
        """Bring both quotes to their desired prices given the book as it stands now."""
        w = self.window
        mid = mid_units(self.book)
        if w is None or mid is None:
            return
        tau = max(w.end_ns - time_ns, 0) / NS_PER_S
        leaning = self.spec.strategy == SIGNAL
        base = as_model.INVENTORY if leaning else self.spec.strategy
        bid_d, ask_d = as_model.quotes(base, mid / PRICE_SCALE, self.shares / self.cfg.lot, self.params, tau)
        if leaning and self.skew is not None:
            shift = self.skew(time_ns)
            if (bid_to_tick(bid_d + shift), ask_to_tick(ask_d + shift)) != (bid_to_tick(bid_d), ask_to_tick(ask_d)):
                w.skew_moved += 1
            bid_d, ask_d = bid_d + shift, ask_d + shift
        best_bid, best_ask = self.book.bids.best(), self.book.asks.best()
        # Never lock or cross the real book. The clamp looks only at the book, so it is inventory-blind.
        bid = min(bid_to_tick(bid_d), best_ask - TICK_SIZE)
        ask = max(ask_to_tick(ask_d), best_bid + TICK_SIZE)
        if bid >= ask or bid <= 0:
            return
        self._place(BUY, bid, best_ask, index, time_ns)
        self._place(SELL, ask, best_bid, index, time_ns)

    def _place(self, side: Direction, price: int, best_opposite: int, index: int, time_ns: int) -> None:
        current = self.orders[side]
        if current is not None and current.active:
            if current.price >= best_opposite if side == BUY else current.price <= best_opposite:
                self.window.overtaken += 1
            if self.spec.sticky and current.price == price:
                return
            self.tracker.cancel(current)
        self.orders[side] = self.tracker.post(side, price, self.cfg.lot, index, time_ns)
        self.window.posts += 1

    def _cancel(self, side: Direction) -> None:
        current = self.orders[side]
        if current is not None and current.active:
            self.tracker.cancel(current)
        self.orders[side] = None

    def take_fills(self, fills: list[Fill], mid_before: float | None) -> None:
        w = self.window
        bid = self.orders[BUY]
        for f in fills:
            sign = 1 if bid is not None and f.order_id == bid.order_id else -1
            mid = mid_before if mid_before is not None else float(f.price)
            self.shares += sign * f.size
            self.cash -= sign * f.price * f.size
            self._match(sign, f.price, f.size)
            self.capture += sign * (mid - f.price) * f.size
            w.fills += 1
            if sign > 0:
                w.shares_bought += f.size
            else:
                w.shares_sold += f.size
            self.result.fills.append(FillRecord(w.index, f.time_ns, sign, f.price, f.size, mid))


def windows_between(start_ns: int, end_ns: int, window_s: float) -> list[tuple[int, int]]:
    """Whole windows that fit in [start_ns, end_ns)."""
    size = int(window_s * NS_PER_S)
    return [(s, s + size) for s in range(start_ns, end_ns - size + 1, size)]


def run_strategies(
    files: LobsterFiles,
    runs: list[tuple[RunSpec, ASParams]],
    start_ns: int,
    end_ns: int,
    cfg: StrategyConfig = StrategyConfig(),
    record_after_s: float = 0.0,
    skew: SkewModel | None = None,
) -> tuple[list[RunResult], MidSeries]:
    """Trade whole windows inside [start_ns, end_ns); returns each run's results and the mid series.

    The mid series runs on for `record_after_s` past the last window so that
    markouts of late fills can be measured. That part is measurement only; no
    order is live by then.

    `skew` is what SIGNAL runs lean on. It must have been fitted on data before
    start_ns; the signal itself is read live and sees only messages already applied.
    """
    replay = MarketReplay(files)
    signals = LiveSignals(replay.book, skew.lookback_s) if skew else None
    reader = skew.reader(signals) if skew else None
    live = [QuotingRun(spec, params, replay.tracker(spec.rule), replay.book, cfg, reader) for spec, params in runs]
    windows = windows_between(start_ns, end_ns, cfg.window_s)
    requote_ns = int(cfg.requote_s * NS_PER_S)
    series = MidSeries()
    state = {"w": 0, "open": False, "next": 0, "last_mid": None}

    def before(k: int, m) -> None:
        t = m.time_ns
        if replay.mid_before is not None:
            state["last_mid"] = replay.mid_before
        while state["w"] < len(windows) and t >= windows[state["w"]][1]:
            if state["open"]:
                for run in live:
                    run.close_window(state["last_mid"])
            state["w"] += 1
            state["open"] = False
        if state["w"] == len(windows):
            return
        w_start, w_end = windows[state["w"]]
        if t < w_start:
            return
        if not state["open"]:
            state["open"], state["next"] = True, w_start
            for run in live:
                run.open_window(state["w"], w_start, w_end)
        if state["next"] <= t:
            # Several requote times may have passed with no message; the book is the same for all, so act once.
            due = state["next"] + (t - state["next"]) // requote_ns * requote_ns
            for run in live:
                run.requote(k - 1, due)
            state["next"] = due + requote_ns

    replay.before.append(before)
    stop_ns = (windows[-1][1] if windows else start_ns) + int(record_after_s * NS_PER_S)
    for k, m in replay:
        t = m.time_ns
        if signals is not None:
            signals.update(m)
        if t >= start_ns:
            series.add(t, mid_units(replay.book))
        if state["open"]:
            for run in live:
                fills = run.tracker.last_fills
                if fills:
                    run.take_fills(fills, replay.mid_before)
                    run.requote(k, t)
        if t >= stop_ns:
            break
    if state["open"]:   # the file ended inside a window
        last = mid_units(replay.book) or state["last_mid"]
        for run in live:
            run.close_window(last)
    return [run.result for run in live], series


def markouts(result: RunResult, series: MidSeries, horizons_s: tuple[float, ...]) -> dict[float, dict[int, list[float]]]:
    """horizon -> window -> markouts in dollars per share: sign * (mid(t + h) - mid just before the fill).

    Negative means the price moved against us after we were filled. Fills too
    close to the end of the data for mid(t + h) to exist are left out.
    """
    out: dict[float, dict[int, list[float]]] = {h: {} for h in horizons_s}
    for f in result.fills:
        for h in horizons_s:
            at = f.time_ns + int(h * NS_PER_S)
            if series.covers(at):
                out[h].setdefault(f.window, []).append(f.sign * (series.at(at) - f.mid_before) / PRICE_SCALE)
    return out
