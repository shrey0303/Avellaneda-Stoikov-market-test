"""Extension (Q7-Q8): does the order book predict the next price move?

The A-S model assumes order flow says nothing about where the mid goes next.
This module measures how wrong that is with three standard signals, each
positive when the book or the recent flow leans towards buyers:

  queue_imbalance   (bid size - ask size) / (bid size + ask size) at the touch
  ofi               order flow imbalance at the touch over the last few seconds,
                    in lots (Cont, Kukanov and Stoikov 2014): size added at or
                    above the best bid, minus size removed from it, minus the
                    same for the ask
  trade_imbalance   buyer-initiated minus seller-initiated visible volume over
                    the last few seconds, in lots

For each signal x and horizon h, the mid change over the next h seconds (in
ticks) is regressed on x using morning samples only, and that fitted line is
then scored on the afternoon. Nothing from the afternoon enters a fit, and a
morning sample is only used if its h-second target ends before the split.

Samples sit on a one-second grid, so targets at horizons above a second
overlap and are autocorrelated. Every interval is therefore a bootstrap over
whole windows, like the rest of the study, not over samples.
"""

from __future__ import annotations

import math
from collections import deque
from dataclasses import asdict, dataclass, field
from typing import Callable, Sequence

from .book import OrderBook
from .lobster_format import NS_PER_S, PRICE_SCALE, TICK_SIZE, Direction, EventType
from .parser import LobsterFiles, Message
from .session import MarketReplay

QUEUE_IMBALANCE = "queue_imbalance"
OFI = "ofi"
TRADE_IMBALANCE = "trade_imbalance"
SIGNALS = (QUEUE_IMBALANCE, OFI, TRADE_IMBALANCE)
LOT = 100


@dataclass(frozen=True)
class SignalConfig:
    grid_s: int = 1                                      # sampling interval
    lookback_s: float = 5.0                              # window of the two flow signals
    horizons_s: tuple[int, ...] = (1, 5, 10, 30, 60)
    skew_horizon_s: int = 5                              # horizon whose fit the strategy leans on
    min_samples: int = 200


# ---------------------------------------------------------------------------
# Live signal values, kept in step with the book
# ---------------------------------------------------------------------------


def _touch(book: OrderBook) -> tuple[int | None, int, int | None, int]:
    """(best bid, its size, best ask, its size); size 0 where a side is empty."""
    b, a = book.bids.best(), book.asks.best()
    return (b, book.bids.levels[b].total if b is not None else 0,
            a, book.asks.levels[a].total if a is not None else 0)


class LiveSignals:
    """Call update(msg) after each message is applied; value(name, now_ns) reads a signal."""

    def __init__(self, book: OrderBook, lookback_s: float):
        self.book = book
        self.lookback_ns = int(lookback_s * NS_PER_S)
        self._prev = _touch(book)
        self._events: deque[tuple[int, float, float]] = deque()   # (time, ofi increment, signed trade), in lots
        self._ofi = 0.0
        self._trade = 0.0

    def update(self, msg: Message) -> None:
        pb, qb, pa, qa = self._prev
        cur = nb, nqb, na, nqa = _touch(self.book)
        self._prev = cur
        e = 0.0
        if nb is not None and pb is not None:
            e += (nqb if nb >= pb else 0) - (qb if nb <= pb else 0)
        if na is not None and pa is not None:
            e -= (nqa if na <= pa else 0) - (qa if na >= pa else 0)
        trade = 0.0
        if msg.event_type == EventType.EXEC_VISIBLE:
            # a resting SELL was hit, so the aggressor was a buyer
            trade = msg.size if msg.direction == Direction.SELL else -msg.size
        if e or trade:
            e, trade = e / LOT, trade / LOT
            self._events.append((msg.time_ns, e, trade))
            self._ofi += e
            self._trade += trade

    def value(self, name: str, now_ns: int) -> float:
        if name == QUEUE_IMBALANCE:
            _, qb, _, qa = self._prev
            return (qb - qa) / (qb + qa) if qb + qa else 0.0
        cutoff = now_ns - self.lookback_ns
        ev = self._events
        while ev and ev[0][0] <= cutoff:
            _, e, trade = ev.popleft()
            self._ofi -= e
            self._trade -= trade
        if not ev:                       # clear float drift whenever the window empties
            self._ofi = self._trade = 0.0
        if name == OFI:
            return self._ofi
        if name == TRADE_IMBALANCE:
            return self._trade
        raise ValueError(f"unknown signal {name!r}")


# ---------------------------------------------------------------------------
# Recording samples on a grid
# ---------------------------------------------------------------------------


@dataclass
class SignalSamples:
    grid_s: int
    times: list[int] = field(default_factory=list)
    mids: list[float | None] = field(default_factory=list)            # price units
    features: dict[str, list[float]] = field(default_factory=lambda: {s: [] for s in SIGNALS})


def record(files: LobsterFiles, start_ns: int, end_ns: int, cfg: SignalConfig = SignalConfig()) -> SignalSamples:
    """One pass over the day: mid and every signal at each grid time in [start_ns, end_ns).

    A sample at grid time g describes the book after the last message before g.
    """
    replay = MarketReplay(files)
    live = LiveSignals(replay.book, cfg.lookback_s)
    out = SignalSamples(cfg.grid_s)
    step = cfg.grid_s * NS_PER_S
    nxt = start_ns

    def sample_until(t_ns: int, mid: float | None) -> None:
        nonlocal nxt
        while nxt <= t_ns and nxt < end_ns:
            out.times.append(nxt)
            out.mids.append(mid)
            for name in SIGNALS:
                out.features[name].append(live.value(name, nxt))
            nxt += step

    replay.before.append(lambda k, m: sample_until(m.time_ns, replay.mid_before))
    for _, m in replay:
        live.update(m)
        if m.time_ns >= end_ns:
            break
    return out


# ---------------------------------------------------------------------------
# Fit on one period, score on another
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SignalFit:
    signal: str
    horizon_s: int
    intercept: float      # ticks
    slope: float          # ticks of mid change per unit of signal
    n: int
    corr: float           # in-sample correlation between signal and target


@dataclass(frozen=True)
class SignalScore:
    signal: str
    horizon_s: int
    n: int
    corr: float           # out-of-sample correlation, pooled over the period
    r2: float             # 1 - SSE(fitted line) / SSE(predicting no change)
    hit_rate: float       # share of non-zero moves whose direction the fitted line called
    hits_n: int
    window_corrs: list[float]


def _pairs(s: SignalSamples, name: str, horizon_s: int, lo_ns: int, hi_ns: int) -> list[tuple[int, float, float]]:
    """(time, signal, mid change in ticks over the horizon) for samples whose target lies inside [lo, hi)."""
    step = horizon_s // s.grid_s
    xs, mids, times = s.features[name], s.mids, s.times
    out = []
    for i in range(len(times) - step):
        if times[i] < lo_ns or times[i + step] >= hi_ns:
            continue
        m0, m1 = mids[i], mids[i + step]
        if m0 is not None and m1 is not None:
            out.append((times[i], xs[i], (m1 - m0) / TICK_SIZE))
    return out


def _corr(xs: Sequence[float], ys: Sequence[float]) -> float:
    n = len(xs)
    if n < 3:
        return float("nan")
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    syy = sum((y - my) ** 2 for y in ys)
    if sxx <= 0 or syy <= 0:
        return float("nan")
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / math.sqrt(sxx * syy)


def fit(s: SignalSamples, name: str, horizon_s: int, lo_ns: int, hi_ns: int, min_samples: int = 200) -> SignalFit | None:
    """Least-squares line target = intercept + slope * signal; None if there is too little to fit."""
    rows = _pairs(s, name, horizon_s, lo_ns, hi_ns)
    n = len(rows)
    if n < min_samples:
        return None
    xs, ys = [r[1] for r in rows], [r[2] for r in rows]
    mx, my = sum(xs) / n, sum(ys) / n
    sxx = sum((x - mx) ** 2 for x in xs)
    if sxx <= 0:
        return None
    slope = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sxx
    return SignalFit(name, horizon_s, my - slope * mx, slope, n, _corr(xs, ys))


def score(s: SignalSamples, f: SignalFit, windows: Sequence[tuple[int, int]]) -> SignalScore:
    """Score a fitted line on samples it has not seen, pooled and per window."""
    xs_all: list[float] = []
    ys_all: list[float] = []
    window_corrs = []
    for lo, hi in windows:
        rows = _pairs(s, f.signal, f.horizon_s, lo, hi)
        xs, ys = [r[1] for r in rows], [r[2] for r in rows]
        xs_all += xs
        ys_all += ys
        c = _corr(xs, ys)
        if not math.isnan(c):
            window_corrs.append(c)
    sse = sum((y - (f.intercept + f.slope * x)) ** 2 for x, y in zip(xs_all, ys_all))
    sst = sum(y * y for y in ys_all)
    called = [(f.slope * x > 0) == (y > 0) for x, y in zip(xs_all, ys_all) if y != 0 and f.slope * x != 0]
    return SignalScore(f.signal, f.horizon_s, len(xs_all), _corr(xs_all, ys_all),
                       1 - sse / sst if sst > 0 else float("nan"),
                       sum(called) / len(called) if called else float("nan"), len(called), window_corrs)


# ---------------------------------------------------------------------------
# Leaning quotes on a signal
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SkewModel:
    """Shift both quotes by the fitted move: slope * signal. The intercept is the
    morning's drift, which the model takes to be zero, so it is not carried over."""

    signal: str
    horizon_s: int
    lookback_s: float
    slope_dollars: float      # dollars of expected mid change per unit of signal

    def reader(self, live: LiveSignals) -> Callable[[int], float]:
        return lambda now_ns: self.slope_dollars * live.value(self.signal, now_ns)


def choose_skew(fits: Sequence[SignalFit], cfg: SignalConfig) -> SkewModel | None:
    """The signal with the strongest in-sample correlation at the skew horizon. Uses the fitting period only."""
    usable = [f for f in fits if f.horizon_s == cfg.skew_horizon_s and not math.isnan(f.corr) and f.slope != 0]
    if not usable:
        return None
    best = max(usable, key=lambda f: abs(f.corr))
    return SkewModel(best.signal, best.horizon_s, cfg.lookback_s, best.slope * TICK_SIZE / PRICE_SCALE)


@dataclass
class SignalStudy:
    fits: list[SignalFit]
    scores: list[SignalScore]
    skew: SkewModel | None
    samples_fit: int
    samples_test: int

    def to_dict(self) -> dict:
        return {"fits": [asdict(f) for f in self.fits], "skew": asdict(self.skew) if self.skew else None,
                "samples_fit": self.samples_fit, "samples_test": self.samples_test}


def analyse(files: LobsterFiles, start_ns: int, split_ns: int, end_ns: int,
            test_windows: Sequence[tuple[int, int]], cfg: SignalConfig = SignalConfig()) -> SignalStudy:
    """Fit every signal at every horizon on [start, split), score each on the test windows."""
    s = record(files, start_ns, end_ns, cfg)
    fits = [f for name in SIGNALS for h in cfg.horizons_s
            if (f := fit(s, name, h, start_ns, split_ns, cfg.min_samples)) is not None]
    scores = [score(s, f, test_windows) for f in fits]
    return SignalStudy(fits, scores, choose_skew(fits, cfg),
                       sum(1 for t in s.times if t < split_ns), sum(1 for t in s.times if t >= split_ns))
