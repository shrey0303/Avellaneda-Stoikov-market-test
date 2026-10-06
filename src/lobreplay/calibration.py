"""Phase 5: calibrate sigma, A and k on real data (approach document §5.4).

Everything here reads one time window and nothing after it, so a strategy run
on a later window has no look-ahead.

  sigma   from the mid price sampled on a 1-second grid, at several horizons.
          The variance-ratio curve shows how much short-horizon estimates are
          inflated by microstructure noise; the horizon used is a stated choice.
  A, k    from probes: hypothetical single orders posted a random number of
          ticks behind the touch, each recorded as (distance from mid, seconds
          resting, filled?). lambda(delta) = A * exp(-k * delta) is fitted by
          Poisson maximum likelihood, once per fill rule.
  spread  time-weighted distribution of the quoted spread in ticks, used to
          sort stocks into large-tick and small-tick groups (§5.6).
"""

from __future__ import annotations

import math
import random
from bisect import bisect_right
from collections import Counter, deque
from dataclasses import dataclass, field
from typing import Sequence

from .as_model import intensity
from .lobster_format import NS_PER_S, PRICE_SCALE, TICK_SIZE, Direction
from .parser import LobsterFiles
from .queue_tracker import FillRule, HypotheticalOrder, QuoteError
from .session import MarketReplay, mid_units

# ---------------------------------------------------------------------------
# Mid price and sigma
# ---------------------------------------------------------------------------


class MidSeries:
    """Mid price (price units) after each message; `at(t)` is the last value at or before t."""

    def __init__(self) -> None:
        self.times: list[int] = []
        self.mids: list[float] = []

    def add(self, time_ns: int, mid: float | None) -> None:
        if mid is not None:
            self.times.append(time_ns)
            self.mids.append(mid)

    def at(self, time_ns: int) -> float | None:
        i = bisect_right(self.times, time_ns)
        return self.mids[i - 1] if i else None

    def covers(self, time_ns: int) -> bool:
        return bool(self.times) and time_ns <= self.times[-1]


@dataclass(frozen=True)
class VRPoint:
    horizon_s: int
    sigma: float       # dollars per sqrt(second)
    n: int             # non-overlapping increments used
    ratio: float       # sigma^2 at this horizon / sigma^2 at the longest horizon


def variance_ratio(series: MidSeries, start_ns: int, end_ns: int, horizons: Sequence[int]) -> list[VRPoint]:
    """Per-second variance of the mid at each horizon, from non-overlapping increments.

    Zero drift is assumed (as in the model), so variance is the mean squared
    increment. A ratio above 1 at short horizons means extra short-term noise;
    below 1 means short-term moves that later continue.
    """
    grid: list[float] = []
    t = start_ns
    while t < end_ns:
        m = series.at(t)
        if m is not None:
            grid.append(m / PRICE_SCALE)
        t += NS_PER_S
    raw = []
    for h in sorted(horizons):
        incs = [grid[i + h] - grid[i] for i in range(0, len(grid) - h, h)]
        if len(incs) >= 2:
            raw.append((h, sum(d * d for d in incs) / (len(incs) * h), len(incs)))
    if not raw:
        return []
    ref = raw[-1][1]
    return [VRPoint(h, math.sqrt(v), n, v / ref if ref > 0 else float("nan")) for h, v, n in raw]


# ---------------------------------------------------------------------------
# Fill intensity
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class IntensityFit:
    A: float            # fills per second at delta = 0
    k: float            # 1 / dollars
    n_obs: int
    n_fills: int
    exposure_s: float
    interior: bool      # False: the likelihood has no interior maximum (see fit_intensity)

    @property
    def usable(self) -> bool:
        return self.interior and self.A > 0 and self.k > 0


def fit_intensity(deltas: Sequence[float], exposures: Sequence[float], filled: Sequence[bool]) -> IntensityFit:
    """Poisson maximum likelihood for lambda(delta) = A * exp(-k * delta).

    Each observation is a quote resting `exposure` seconds at distance `delta`
    that ended in a fill or was censored. The log-likelihood is

        sum_fills (ln A - k * delta_i)  -  A * sum_all T_i * exp(-k * delta_i)

    For fixed k the best A is fills / sum T_i exp(-k delta_i). Substituting,
    the k that maximises the likelihood is where the exposure-weighted mean
    delta (weights T_i exp(-k delta_i)) equals the mean delta of the fills.
    That weighted mean falls as k rises, so bisection finds it.

    No interior maximum exists when fills are, on average, no closer to the mid
    than the exposure was (fill rate does not fall with distance: k = 0 is
    returned) or when every fill sits at the smallest delta (k is unbounded).
    """
    n = len(deltas)
    if not (n == len(exposures) == len(filled)):
        raise ValueError("deltas, exposures and filled must have the same length")
    n_fills = sum(1 for f in filled if f)
    exposure = sum(exposures)
    if n_fills == 0 or exposure <= 0:
        return IntensityFit(0.0, 0.0, n, n_fills, exposure, False)

    d0 = min(deltas)
    target = sum(d for d, f in zip(deltas, filled) if f) / n_fills

    def weighted(k: float) -> tuple[float, float]:
        """(sum of weights, weighted mean delta), weights T * exp(-k (delta - d0))."""
        s = sd = 0.0
        for d, t in zip(deltas, exposures):
            w = t * math.exp(-k * (d - d0))
            s += w
            sd += w * d
        return s, sd / s

    if target >= weighted(0.0)[1]:
        return IntensityFit(n_fills / exposure, 0.0, n, n_fills, exposure, False)
    unbounded = IntensityFit(float("inf"), float("inf"), n, n_fills, exposure, False)
    if target <= d0:            # every fill at the smallest delta
        return unbounded
    spread = max(deltas) - d0
    lo, hi = 0.0, 1.0 / spread
    while weighted(hi)[1] > target:
        hi *= 2
        if hi * spread > 700:   # exp underflow before the bracket closed
            return unbounded
    for _ in range(100):
        mid = (lo + hi) / 2
        if weighted(mid)[1] > target:
            lo = mid
        else:
            hi = mid
    k = (lo + hi) / 2
    s, _ = weighted(k)
    return IntensityFit(n_fills / s * math.exp(k * d0), k, n, n_fills, exposure, True)


@dataclass
class Probe:
    side: Direction
    depth_ticks: int        # ticks behind the best quote on its own side
    delta: float            # dollars from the mid when posted
    posted_ns: int
    rest_s: float = 0.0     # seconds until the first fill, or until it was withdrawn
    filled: bool = False


@dataclass(frozen=True)
class RateRow:
    depth_ticks: int
    probes: int
    fills: int
    exposure_s: float
    mean_delta: float
    empirical: float        # fills per second of exposure
    fitted: float           # exposure-weighted mean of the fitted lambda over this row's probes


def rate_table(probes: Sequence[Probe], fit: IntensityFit) -> list[RateRow]:
    """Fitted curve against empirical fill rates, one row per posting depth."""
    rows = []
    for depth in sorted({p.depth_ticks for p in probes}):
        group = [p for p in probes if p.depth_ticks == depth]
        exposure = sum(p.rest_s for p in group)
        fills = sum(p.filled for p in group)
        fitted = float("nan")
        if fit.usable and exposure > 0:
            fitted = sum(p.rest_s * intensity(p.delta, fit.A, fit.k) for p in group) / exposure
        rows.append(RateRow(depth, len(group), fills, exposure, sum(p.delta for p in group) / len(group),
                            fills / exposure if exposure > 0 else float("nan"), fitted))
    return rows


# ---------------------------------------------------------------------------
# Spread profile
# ---------------------------------------------------------------------------


@dataclass
class SpreadProfile:
    ns_by_ticks: Counter = field(default_factory=Counter)   # spread in ticks -> nanoseconds quoted

    @property
    def total_ns(self) -> int:
        return sum(self.ns_by_ticks.values())

    def share(self, ticks: int) -> float:
        total = self.total_ns
        return self.ns_by_ticks.get(ticks, 0) / total if total else float("nan")

    @property
    def mean_ticks(self) -> float:
        total = self.total_ns
        return sum(t * ns for t, ns in self.ns_by_ticks.items()) / total if total else float("nan")

    def tick_group(self, threshold: float = 0.5) -> str:
        """'large-tick' if the spread is one tick at least `threshold` of the time."""
        return "large-tick" if self.share(1) >= threshold else "small-tick"


# ---------------------------------------------------------------------------
# One calibration pass
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class CalibrationConfig:
    horizons_s: tuple[int, ...] = (1, 2, 5, 10, 30, 60, 120, 300)
    sigma_horizon_s: int = 60
    probe_every_s: float = 5.0
    probe_max_depth: int = 5        # probes go 0..max_depth ticks behind the touch
    probe_max_rest_s: float = 60.0
    probe_size: int = 100
    seed: int = 0


@dataclass
class Calibration:
    start_ns: int
    end_ns: int
    sigma: float | None
    sigma_horizon_s: int
    variance_ratio: list[VRPoint]
    fits: dict[FillRule, IntensityFit]
    probes: dict[FillRule, list[Probe]]
    spread: SpreadProfile
    messages: int


def calibrate(files: LobsterFiles, start_ns: int, end_ns: int, cfg: CalibrationConfig = CalibrationConfig()) -> Calibration:
    """Calibrate on [start_ns, end_ns). Stops reading at the first message at or after end_ns."""
    replay = MarketReplay(files)
    trackers = {rule: replay.tracker(rule) for rule in FillRule}
    rng = random.Random(cfg.seed)
    series, spread = MidSeries(), SpreadProfile()
    probes: dict[FillRule, list[Probe]] = {rule: [] for rule in FillRule}
    live: dict[FillRule, dict[int, tuple[Probe, HypotheticalOrder]]] = {rule: {} for rule in FillRule}
    expiries: deque[tuple[int, dict[FillRule, int]]] = deque()   # (expire_ns, order id per rule), in time order
    every_ns = int(cfg.probe_every_s * NS_PER_S)
    max_rest_ns = int(cfg.probe_max_rest_s * NS_PER_S)
    next_probe_ns = start_ns

    def withdraw(up_to_ns: int, cap_ns: int | None = None) -> None:
        while expiries and expiries[0][0] <= up_to_ns:
            expire_ns, ids = expiries.popleft()
            for rule, oid in ids.items():
                entry = live[rule].pop(oid, None)
                if entry:
                    probe, order = entry
                    probe.rest_s = (min(expire_ns, cap_ns or expire_ns) - probe.posted_ns) / NS_PER_S
                    trackers[rule].cancel(order)

    def post_probes(k: int, t_ns: int) -> None:
        mid = mid_units(replay.book)
        if mid is None:
            return
        for side in (Direction.BUY, Direction.SELL):
            depth = rng.randint(0, cfg.probe_max_depth)
            best = replay.book.side(side).best()
            price = best - depth * TICK_SIZE if side == Direction.BUY else best + depth * TICK_SIZE
            if price <= 0:
                continue
            ids = {}
            for rule, tr in trackers.items():
                try:
                    order = tr.post(side, price, cfg.probe_size, k - 1, t_ns)
                except QuoteError:   # only possible while the real book is itself crossed
                    break
                probe = Probe(side, depth, abs(mid - price) / PRICE_SCALE, t_ns)
                probes[rule].append(probe)
                live[rule][order.order_id] = (probe, order)
                ids[rule] = order.order_id
            if ids:
                expiries.append((min(t_ns + max_rest_ns, end_ns), ids))

    def before(k: int, m) -> None:
        nonlocal next_probe_ns
        withdraw(m.time_ns)
        while next_probe_ns <= m.time_ns and next_probe_ns < end_ns:
            post_probes(k, next_probe_ns)
            next_probe_ns += every_ns

    replay.before.append(before)
    last_ns, reached_end = start_ns, False
    prev: tuple[int, float | None] | None = None
    for k, m in replay:
        t = m.time_ns
        if prev is not None and prev[1] is not None:
            a, b = max(prev[0], start_ns), min(t, end_ns)
            if b > a:
                spread.ns_by_ticks[round(prev[1] / TICK_SIZE)] += b - a
        if t >= end_ns:
            reached_end = True
            break
        last_ns = t
        for rule, tr in trackers.items():
            for f in tr.last_fills:
                entry = live[rule].pop(f.order_id, None)
                if entry:   # first fill ends the probe; any remainder is withdrawn
                    probe, order = entry
                    probe.filled, probe.rest_s = True, (t - probe.posted_ns) / NS_PER_S
                    tr.cancel(order)
        series.add(t, mid_units(replay.book))
        b, a = replay.book.bids.best(), replay.book.asks.best()
        prev = (t, a - b if a is not None and b is not None else None)
    withdraw(end_ns, cap_ns=None if reached_end else last_ns)   # the file may stop before the window does

    vr = variance_ratio(series, start_ns, end_ns, cfg.horizons_s)
    sigma = next((p.sigma for p in vr if p.horizon_s == cfg.sigma_horizon_s), None)
    fits = {
        rule: fit_intensity([p.delta for p in ps], [p.rest_s for p in ps], [p.filled for p in ps])
        for rule, ps in probes.items()
    }
    return Calibration(start_ns, end_ns, sigma, cfg.sigma_horizon_s, vr, fits, probes, spread, replay.k)
