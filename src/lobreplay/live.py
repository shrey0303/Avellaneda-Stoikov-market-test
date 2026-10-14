"""Phase 12: the A-S strategies on real IEX data, one finished trading day at a time.

The LOBSTER study (study.py) has one day per stock. This runs the same two
strategies on every new trading day, using the IEX exchange's quotes and
trades fetched from Alpaca once the day is over (alpaca.py).

    calibrate   sigma and the fill intensity (A, k) come only from the days
                BEFORE the one being traded, so nothing is fitted on the day
                it is scored on. The first day of each stock only calibrates.
    trade       quote on IEX, one lot per side, requoted every second, in
                independent 30-minute windows (as in strategy.py)
    fill        IEX gives the best bid and ask, not the order-by-order book,
                so queue position is unknown. A quote is filled by a real IEX
                trade through its price (conservative) or at or through it
                (optimistic). The truth lies between the two.

Quotes posted at second k use the IEX quote as it stood at k and are
exposed to the trades printed in (k, k + 1]. A quote is never allowed to
cross the IEX book; it would have been a taker order. P&L is before fees
and rebates.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Callable, Iterable, Sequence

from . import as_model
from .alpaca import session_bounds_ns
from .as_model import ASParams
from .lobster_format import NS_PER_S, PRICE_SCALE, TICK_SIZE
from .strategy import ask_to_tick, bid_to_tick

S = NS_PER_S
CONSERVATIVE, OPTIMISTIC = "conservative", "optimistic"
RULES = (CONSERVATIVE, OPTIMISTIC)
STRATEGIES = (as_model.INVENTORY, as_model.SYMMETRIC)


@dataclass(frozen=True)
class LiveConfig:
    exclude_s: int = 300                 # skipped after the open and before the close
    window_s: int = 1800
    lot: int = 100
    penalty_ticks: tuple[float, ...] = (1.0, 2.0, 4.0)
    markout_s: int = 5
    sigma_horizon_s: int = 60
    probe_ticks: tuple[int, ...] = (0, 1, 2, 3, 4, 5)
    history_days: int = 5                # calibration uses at most this many earlier days
    min_sigma_samples: int = 50
    n_boot: int = 2000
    seed: int = 0


@dataclass
class Day:
    """One session on a one-second grid. bids[k], asks[k]: the IEX quote standing at open + k s,
    0 when there was no two-sided quote. trades[k]: (time_ns, price, size) printed in (open + k s, open + k s + 1 s]."""
    symbol: str
    date: str
    open_ns: int
    close_ns: int
    bids: list[int]
    asks: list[int]
    trades: list[list[tuple[int, int, int]]]
    n_quotes: int = 0
    n_trades: int = 0

    @property
    def seconds(self) -> int:
        return len(self.bids)

    def mid(self, k: int) -> float | None:
        if 0 <= k < len(self.bids) and self.bids[k]:
            return (self.bids[k] + self.asks[k]) / 2
        return None


def build_day(symbol: str, day: str, quotes: Iterable[tuple], trades: Iterable[tuple],
              bounds: tuple[int, int] | None = None) -> Day:
    """quotes: (time_ns, bid, bid_size, ask, ask_size) in time order; trades: (time_ns, price, size)."""
    open_ns, close_ns = bounds or session_bounds_ns(day)
    n = (close_ns - open_ns) // S + 1
    bids, asks = [0] * n, [0] * n
    k, cur, n_quotes = 0, (0, 0), 0
    for t, b, _, a, _ in quotes:
        n_quotes += 1
        while k < n and open_ns + k * S < t:
            bids[k], asks[k] = cur
            k += 1
        cur = (b, a) if (b > 0 and a > b) else (0, 0)
    while k < n:
        bids[k], asks[k] = cur
        k += 1
    buckets: list[list[tuple[int, int, int]]] = [[] for _ in range(n - 1)]
    n_trades = 0
    for t, p, s in trades:
        j = (t - open_ns - 1) // S
        if 0 <= j < n - 1 and s > 0:
            buckets[j].append((t, p, s))
            n_trades += 1
    return Day(symbol.upper(), day, open_ns, close_ns, bids, asks, buckets, n_quotes, n_trades)


def _bid_hit(rule: str, low: int | None, price: float) -> bool:
    return low is not None and (low < price or (rule == OPTIMISTIC and low == price))


def _ask_hit(rule: str, high: int | None, price: float) -> bool:
    return high is not None and (high > price or (rule == OPTIMISTIC and high == price))


def day_stats(day: Day, cfg: LiveConfig = LiveConfig()) -> dict:
    """What later days calibrate on: squared mid moves for sigma, and one-second probes for (A, k).

    A probe is a quote j ticks outside the mid, rounded away from it, left for one
    second. It counts as hit under a rule exactly as the strategy's quotes do.
    """
    lo_k, hi_k = cfg.exclude_s, day.seconds - 1 - cfg.exclude_s
    h = cfg.sigma_horizon_s
    sum_sq, count = 0.0, 0
    for k in range(lo_k, hi_k - h + 1, h):
        m0, m1 = day.mid(k), day.mid(k + h)
        if m0 is not None and m1 is not None:
            sum_sq += ((m1 - m0) / PRICE_SCALE) ** 2
            count += 1
    probes = {r: {j: [0, 0, 0.0] for j in cfg.probe_ticks} for r in RULES}   # probes, hits, sum of delta ($)
    quoted = spread_sum = 0
    for k in range(lo_k, hi_k):
        m = day.mid(k)
        if m is None:
            continue
        quoted += 1
        spread_sum += day.asks[k] - day.bids[k]
        prices = [p for _, p, _ in day.trades[k]]
        low, high = (min(prices), max(prices)) if prices else (None, None)
        for j in cfg.probe_ticks:
            bid = math.floor(m / TICK_SIZE) * TICK_SIZE - j * TICK_SIZE
            ask = math.ceil(m / TICK_SIZE) * TICK_SIZE + j * TICK_SIZE
            delta = ((m - bid) + (ask - m)) / PRICE_SCALE
            for r in RULES:
                row = probes[r][j]
                row[0] += 2
                row[1] += _bid_hit(r, low, bid) + _ask_hit(r, high, ask)
                row[2] += delta
    return {
        "sigma_horizon_s": h, "sum_sq": sum_sq, "increments": count,
        "probes": {r: {str(j): v for j, v in rows.items()} for r, rows in probes.items()},
        "seconds_quoted": quoted, "seconds": max(0, hi_k - lo_k),
        "mean_spread_ticks": spread_sum / quoted / TICK_SIZE if quoted else None,
    }


def fit_intensity(rows: dict[str, list]) -> dict | None:
    """Fit rate(delta) = A exp(-k delta) to pooled probes. rate = -ln(1 - hit share) per second,
    weighted least squares on ln(rate) with the hit count as weight."""
    pts = []
    for n, hits, sum_delta in rows.values():
        if n and 0 < hits < n:
            pts.append((sum_delta / n, math.log(-math.log1p(-hits / n)), hits))
    if len(pts) < 2:
        return None
    w = sum(p[2] for p in pts)
    mx = sum(p[0] * p[2] for p in pts) / w
    my = sum(p[1] * p[2] for p in pts) / w
    sxx = sum(p[2] * (p[0] - mx) ** 2 for p in pts)
    if sxx <= 0:
        return None
    slope = sum(p[2] * (p[0] - mx) * (p[1] - my) for p in pts) / sxx
    k = -slope
    if not k > 0:
        return None
    return {"A": math.exp(my + k * mx), "k": k, "points": len(pts)}


def calibrate(history: Sequence[dict], cfg: LiveConfig = LiveConfig()) -> tuple[dict | None, list[str]]:
    """Pool the stats of earlier days into sigma and (A, k) per rule. Returns (calibration, problems)."""
    if not history:
        return None, ["no earlier day to calibrate on; this day only calibrates"]
    sum_sq = sum(h["stats"]["sum_sq"] for h in history)
    count = sum(h["stats"]["increments"] for h in history)
    if count < cfg.min_sigma_samples:
        return None, [f"only {count} {cfg.sigma_horizon_s} s mid moves on the calibration days"]
    sigma = math.sqrt(sum_sq / count / cfg.sigma_horizon_s)
    intensity, problems = {}, []
    for r in RULES:
        pooled: dict[str, list] = {}
        for h in history:
            for j, (n, hits, sd) in h["stats"]["probes"][r].items():
                row = pooled.setdefault(j, [0, 0, 0.0])
                row[0] += n
                row[1] += hits
                row[2] += sd
        fit = fit_intensity(pooled)
        if fit is None:
            problems.append(f"fill intensity could not be fitted under the {r} rule")
        else:
            intensity[r] = fit
    if not sigma > 0:
        problems.append("sigma is zero on the calibration days")
        return None, problems
    cal = {"days": [h["date"] for h in history], "sigma": sigma, "intensity": intensity}
    return (cal if intensity else None), problems


def _run(day: Day, strategy: str, params: ASParams, rule: str, cfg: LiveConfig) -> dict:
    lot, tick = cfg.lot, TICK_SIZE
    start, end = cfg.exclude_s, day.seconds - 1 - cfg.exclude_s
    windows = []
    for ws in range(start, end - cfg.window_s + 1, cfg.window_s):
        we = ws + cfg.window_s
        q = 0
        cash = capture = 0.0                 # price units * shares
        fills = bought = sold = 0
        marks: list[float] = []
        last_mid = None
        for k in range(ws, we):
            m = day.mid(k)
            if m is None:
                continue
            last_mid = m
            bid_d, ask_d = as_model.quotes(strategy, m / PRICE_SCALE, q / lot, params, we - k)
            bid = min(bid_to_tick(bid_d), day.asks[k] - tick)   # never cross the IEX book
            ask = max(ask_to_tick(ask_d), day.bids[k] + tick)
            rb = ra = lot
            for _, p, s in day.trades[k]:
                sign = 0
                if rb and _bid_hit(rule, p, bid):
                    f, sign, price = min(rb, s), 1, bid
                    rb -= f
                elif ra and _ask_hit(rule, p, ask):
                    f, sign, price = min(ra, s), -1, ask
                    ra -= f
                if not sign:
                    continue
                q += sign * f
                cash -= sign * f * price
                capture += sign * f * (m - price)
                fills += 1
                bought += f if sign > 0 else 0
                sold += f if sign < 0 else 0
                after = day.mid(k + 1 + cfg.markout_s)
                if after is not None:
                    marks.append(sign * (after - m) / tick)
        close = day.mid(we)
        close = close if close is not None else last_mid
        pnl = (cash + q * close) / PRICE_SCALE if close is not None else 0.0
        windows.append({
            "start_s": ws, "end_s": we, "pnl": pnl, "spread_capture": capture / PRICE_SCALE,
            "inventory_pnl": pnl - capture / PRICE_SCALE, "fills": fills, "shares_bought": bought,
            "shares_sold": sold, "end_inventory": q, "markout_sum": sum(marks), "markout_n": len(marks),
        })
    n_marks = sum(w["markout_n"] for w in windows)
    return {
        "windows": windows,
        "day_pnl": sum(w["pnl"] for w in windows),
        "fills": sum(w["fills"] for w in windows),
        "markout_mean": sum(w["markout_sum"] for w in windows) / n_marks if n_marks else None,
        "markout_n": n_marks,
    }


def run_day(day: Day, history: Sequence[dict], cfg: LiveConfig = LiveConfig()) -> dict:
    stats = day_stats(day, cfg)
    res = {
        "symbol": day.symbol, "date": day.date, "source": "Alpaca free plan, IEX quotes and trades",
        "n_quotes": day.n_quotes, "n_trades": day.n_trades,
        "quote_coverage": stats["seconds_quoted"] / stats["seconds"] if stats["seconds"] else 0.0,
        "stats": stats, "calibration": None, "problems": [], "runs": [],
        "config": asdict(cfg),
    }
    if stats["increments"] == 0 or day.n_trades == 0:
        res["problems"].append("too little IEX data on this day to trade or calibrate")
        return res
    cal, problems = calibrate(history, cfg)
    res["calibration"], res["problems"] = cal, problems
    if cal is None:
        return res
    for rule, fit in cal["intensity"].items():
        for pt in cfg.penalty_ticks:
            gamma = as_model.gamma_for_penalty(pt * TICK_SIZE / PRICE_SCALE, cal["sigma"], cfg.window_s)
            params = ASParams(sigma=cal["sigma"], A=fit["A"], k=fit["k"], gamma=gamma)
            for strategy in STRATEGIES:
                run = _run(day, strategy, params, rule, cfg)
                res["runs"].append({"strategy": strategy, "penalty_ticks": pt, "rule": rule, "gamma": gamma, **run})
    return res


# ---- days on disk -------------------------------------------------------------------------------

def weekdays(since: str, until: str) -> list[str]:
    d, last, out = date.fromisoformat(since), date.fromisoformat(until), []
    while d <= last:
        if d.weekday() < 5:
            out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def last_finished_day(now: datetime | None = None, delay_s: int = 20 * 60) -> str:
    """The latest weekday whose close is at least delay_s old (Alpaca withholds the last 15 minutes)."""
    now = now or datetime.now(timezone.utc)
    d = now.date()
    while True:
        if d.weekday() < 5 and session_bounds_ns(d.isoformat())[1] + delay_s * S <= int(now.timestamp() * S):
            return d.isoformat()
        d -= timedelta(days=1)


def load_days(out_dir: str | Path, symbol: str) -> list[dict]:
    folder = Path(out_dir) / symbol.upper() / "days"
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(folder.glob("*.json"))]


def write_day(res: dict, out_dir: str | Path) -> Path:
    path = Path(out_dir) / res["symbol"] / "days" / f"{res['date']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(res, indent=1) + "\n", encoding="utf-8")
    return path


def process(client, symbols: Sequence[str], days: Sequence[str], out_dir: str | Path,
            cfg: LiveConfig = LiveConfig(), log: Callable[[str], None] = lambda s: None) -> list[str]:
    """Fetch, calibrate and trade every listed day not already on disk. Returns the (symbol, date)s written."""
    written = []
    for symbol in symbols:
        symbol = symbol.upper()
        done = {d["date"]: d for d in load_days(out_dir, symbol)}
        for day in days:
            if day in done:
                continue
            open_ns, close_ns = session_bounds_ns(day)
            quotes = client.quotes(symbol, open_ns - 60 * S, close_ns)
            trades = client.trades(symbol, open_ns, close_ns)
            d = build_day(symbol, day, quotes, list(trades), (open_ns, close_ns))
            if d.n_quotes == 0 and d.n_trades == 0:
                res = {"symbol": symbol, "date": day, "no_data": True}
                log(f"{symbol} {day}: no IEX data (market holiday?)")
            else:
                history = [h for h in sorted(done.values(), key=lambda h: h["date"])
                           if h["date"] < day and not h.get("no_data") and h.get("stats", {}).get("increments")]
                res = run_day(d, history[-cfg.history_days:], cfg)
                traded = "traded" if res["runs"] else "calibration only"
                log(f"{symbol} {day}: {d.n_quotes} quotes, {d.n_trades} trades, {traded}"
                    + "".join(f"; {p}" for p in res["problems"]))
            write_day(res, out_dir)
            done[day] = res
            written.append(f"{symbol} {day}")
    return written
