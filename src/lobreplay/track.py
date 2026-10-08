"""Phases 10-11: freeze one signal, then score it on every later day (approach document §5.9, Q9).

    fit, once      the three signals of signals.py, on the days recorded so far
    freeze         the strongest one at the freeze horizon is written to a file
                   with a SHA-256 fingerprint; the file is never overwritten
    score          every day that starts after the freeze is scored with that
                   fixed line; nothing is refitted

The input is the recorder's one-row-a-second files (recorder.py). It is Level
2 data, so only the prediction is scored here. No strategy is traded and no
queue position is modelled.

A grid second is usable only if a row arrived within max_stale_s before it.
A second without one has no mid, so no price change is measured across a gap,
and the flow signals start again from zero after it.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
from collections import deque
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Sequence

from .lobster_format import NS_PER_S, PRICE_SCALE
from .plots import Series, line_chart
from .signals import OFI, QUEUE_IMBALANCE, SIGNALS, TRADE_IMBALANCE, SignalFit, SignalSamples, fit, score
from .stats import bootstrap_mean

FIT_DAY, BEFORE_FREEZE, UNFINISHED, TOO_LITTLE, SCORED = (
    "fit day", "not after the freeze", "unfinished day", "too little data", "scored")


@dataclass(frozen=True)
class TrackConfig:
    grid_s: int = 1
    lookback_s: float = 5.0
    horizons_s: tuple[int, ...] = (1, 5, 10, 30, 60)
    freeze_horizon_s: int = 5
    max_stale_s: float = 2.0         # a row older than this does not describe the current second
    min_day_samples: int = 3600      # a day needs an hour of usable samples to be scored
    min_days: int = 20               # scored days needed before any verdict
    alpha: float = 0.05


# ---------------------------------------------------------------------------
# Recorded rows -> samples on a one-second grid
# ---------------------------------------------------------------------------


def day_files(data_dir: str | Path, symbol: str) -> dict[str, Path]:
    """UTC date -> that day's file, in date order."""
    return {p.stem: p for p in sorted((Path(data_dir) / symbol.upper()).glob("????-??-??.csv"))}


def _rows(paths: Sequence[Path]):
    for path in paths:
        with open(path, newline="") as fh:
            for r in csv.DictReader(fh):
                yield (int(r["recv_ns"]), round(float(r["bid"]) * PRICE_SCALE), float(r["bid_qty"]),
                       round(float(r["ask"]) * PRICE_SCALE), float(r["ask_qty"]),
                       float(r["buy_qty"]), float(r["sell_qty"]))


def load_days(paths: Sequence[Path], grid_s: int, lookback_s: float, max_stale_s: float) -> SignalSamples:
    """Mid and the three signals at every grid second from the first row to the last.

    The sample at second g describes the last row at or before g. Flow signals
    are in units of the traded asset, summed over the lookback.
    """
    out = SignalSamples(grid_s)
    step, lookback, stale = grid_s * NS_PER_S, int(lookback_s * NS_PER_S), int(max_stale_s * NS_PER_S)
    events: deque[tuple[int, float, float]] = deque()   # (time, ofi increment, signed trade volume)
    prev = None
    g = None

    def emit_until(t_ns: int) -> None:
        """Samples for every grid second before t_ns, from the rows seen so far."""
        nonlocal g
        while g < t_ns:
            fresh = prev is not None and g - prev[0] <= stale
            while events and events[0][0] <= g - lookback:
                events.popleft()
            out.times.append(g)
            out.mids.append((prev[1] + prev[3]) / 2 if fresh else None)
            qb, qa = (prev[2], prev[4]) if fresh else (0.0, 0.0)
            out.features[QUEUE_IMBALANCE].append((qb - qa) / (qb + qa) if qb + qa else 0.0)
            out.features[OFI].append(sum(e[1] for e in events) if fresh else 0.0)
            out.features[TRADE_IMBALANCE].append(sum(e[2] for e in events) if fresh else 0.0)
            g += step

    for row in sorted(_rows(paths)):
        t, bid, qb, ask, qa, buy, sell = row
        if g is None:
            g = -(-t // step) * step
        emit_until(t)   # a row stamped exactly on a grid second belongs to that second
        if prev is None or t - prev[0] > stale:
            events.clear()   # after a gap the flow since the last row is unknown
        else:
            _, pb, pqb, pa, pqa, _, _ = prev
            e = (qb if bid >= pb else 0.0) - (pqb if bid <= pb else 0.0)
            e -= (qa if ask <= pa else 0.0) - (pqa if ask >= pa else 0.0)
            events.append((t, e, buy - sell))
        prev = row
    if prev is not None:
        emit_until(prev[0] + 1)
    return out


# ---------------------------------------------------------------------------
# Freeze
# ---------------------------------------------------------------------------


def _fingerprint(body: dict) -> str:
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def _utc(now: datetime | None) -> datetime:
    return now if now is not None else datetime.now(timezone.utc)


def freeze(data_dir: str | Path, symbol: str, out_path: str | Path, days: Sequence[str] | None = None,
           cfg: TrackConfig = TrackConfig(), now: datetime | None = None) -> dict:
    """Fit on `days` (default: every finished day on disk), choose one signal, write it once."""
    out_path, now = Path(out_path), _utc(now)
    if out_path.exists():
        raise FileExistsError(f"{out_path} already exists. A frozen signal is never overwritten; "
                              "a new signal needs a new file and a new set of test days.")
    files = day_files(data_dir, symbol)
    today = now.strftime("%Y-%m-%d")
    days = sorted(days) if days else [d for d in files if d < today]
    missing = [d for d in days if d not in files]
    if missing or not days:
        raise ValueError(f"no recorded file for {missing}" if missing else "no finished recorded day to fit on")
    s = load_days([files[d] for d in days], cfg.grid_s, cfg.lookback_s, cfg.max_stale_s)
    lo, hi = s.times[0], s.times[-1] + 1
    fits = [f for name in SIGNALS for h in cfg.horizons_s if (f := fit(s, name, h, lo, hi)) is not None]
    usable = [f for f in fits if f.horizon_s == cfg.freeze_horizon_s and not math.isnan(f.corr) and f.slope != 0]
    if not usable:
        raise ValueError(f"nothing could be fitted at the {cfg.freeze_horizon_s} s horizon on {days}")
    best = max(usable, key=lambda f: abs(f.corr))
    body = {
        "symbol": symbol.upper(),
        "created_utc": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "fit_days": days,
        "signal": asdict(best),
        "grid_s": cfg.grid_s, "lookback_s": cfg.lookback_s, "max_stale_s": cfg.max_stale_s,
        "min_day_samples": cfg.min_day_samples,
        "pass_mark": {"min_days": cfg.min_days, "alpha": cfg.alpha,
                      "rule": "the interval of the mean daily correlation excludes zero on the frozen side "
                              "and the sign test p-value is below alpha"},
        "candidates": [asdict(f) for f in fits],   # everything that was looked at, not only the winner
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps({"frozen": body, "sha256": _fingerprint(body)}, indent=2), encoding="utf-8")
    return body


def load_frozen(path: str | Path) -> tuple[dict, str]:
    """The frozen body and its fingerprint; refuses a file that was edited after the freeze."""
    doc = json.loads(Path(path).read_text(encoding="utf-8"))
    if _fingerprint(doc["frozen"]) != doc["sha256"]:
        raise ValueError(f"{path} does not match its fingerprint: it was changed after it was frozen")
    return doc["frozen"], doc["sha256"]


# ---------------------------------------------------------------------------
# Score every later day
# ---------------------------------------------------------------------------


def sign_test_p(k: int, n: int) -> float:
    """Chance of k or more right-signed days out of n if each day were a fair coin."""
    return sum(math.comb(n, i) for i in range(k, n + 1)) / 2 ** n if n else float("nan")


def run_track(data_dir: str | Path, frozen_path: str | Path, now: datetime | None = None,
              n_boot: int = 2000, seed: int = 0) -> dict:
    frozen, sha = load_frozen(frozen_path)
    f = SignalFit(**frozen["signal"])
    today, frozen_day = _utc(now).strftime("%Y-%m-%d"), frozen["created_utc"][:10]
    side = 1 if f.slope > 0 else -1
    days = []
    for day, path in day_files(data_dir, frozen["symbol"]).items():
        row = {"day": day, "status": SCORED, "n": 0, "corr": None, "r2": None, "hit_rate": None, "hits_n": 0}
        if day in frozen["fit_days"]:
            row["status"] = FIT_DAY
        elif day <= frozen_day:
            row["status"] = BEFORE_FREEZE
        elif day >= today:
            row["status"] = UNFINISHED
        else:
            s = load_days([path], frozen["grid_s"], frozen["lookback_s"], frozen["max_stale_s"])
            sc = score(s, f, [(s.times[0], s.times[-1] + 1)]) if s.times else None
            if sc is None or sc.n < frozen["min_day_samples"] or math.isnan(sc.corr):
                row.update(status=TOO_LITTLE, n=sc.n if sc else 0)
            else:
                row.update(n=sc.n, corr=sc.corr, r2=sc.r2, hits_n=sc.hits_n,
                           hit_rate=None if math.isnan(sc.hit_rate) else sc.hit_rate)
        days.append(row)

    corrs = [d["corr"] for d in days if d["status"] == SCORED]
    n, right = len(corrs), sum(1 for c in corrs if c * side > 0)
    est = bootstrap_mean(corrs, n_boot=n_boot, alpha=frozen["pass_mark"]["alpha"], seed=seed)
    p = sign_test_p(right, n)
    need = frozen["pass_mark"]["min_days"]
    if n < need:
        verdict = f"too few days for a verdict: {n} scored, {need} needed"
    elif est.excludes_zero and est.mean * side > 0 and p < frozen["pass_mark"]["alpha"]:
        verdict = "held up"
    else:
        verdict = "did not hold up"
    return {"frozen": frozen, "sha256": sha, "days": days,
            "summary": {"days_scored": n, "days_right_sign": right, "frozen_side": "positive" if side > 0 else "negative",
                        "mean_daily_corr": est.to_dict() if n else None, "sign_test_p": p if n else None,
                        "verdict": verdict}}


def render_track(res: dict) -> str:
    fr, sm, sig = res["frozen"], res["summary"], res["frozen"]["signal"]
    L = [f"# {fr['symbol']}: out-of-sample track record of one frozen signal", "",
         f"- Frozen at {fr['created_utc']}, fitted on {fr['fit_days'][0]} to {fr['fit_days'][-1]} "
         f"({len(fr['fit_days'])} days, {sig['n']} samples).",
         f"- Signal: `{sig['signal']}`, predicting the mid change over the next {sig['horizon_s']} s. "
         f"Slope {sig['slope']:.6g} ticks per unit, correlation {sig['corr']:.3f} on the fitting days.",
         f"- Fingerprint (SHA-256): `{res['sha256']}`. It matches the frozen file, so nothing was changed after the freeze.",
         "- Proof that the freeze came before the test days is the push time of the commit that added the frozen file.",
         "- Only days that start after the freeze are scored. Nothing is refitted. Every recorded day is listed.", "",
         "## Result", ""]
    if sm["days_scored"]:
        e = sm["mean_daily_corr"]
        L += [f"- **{sm['days_right_sign']} of {sm['days_scored']} days** had a {sm['frozen_side']} correlation, "
              "the side the signal was frozen on.",
              f"- Mean daily correlation {e['mean']:.3f} [{e['lo']:.3f}, {e['hi']:.3f}], bootstrap over days.",
              f"- Sign test p = {sm['sign_test_p']:.4f} (days treated as independent, which is generous)."]
    L += [f"- **Verdict against the pass mark stated at the freeze: {sm['verdict']}.**", ""]
    if sm["days_scored"]:
        L += ["![Daily correlation](track.svg)", ""]
    L += ["## Every day", "", "| day (UTC) | status | samples | correlation | R² vs no change | direction called |",
          "|---|---|---|---|---|---|"]
    for d in res["days"]:
        if d["status"] == SCORED:
            hit = f"{d['hit_rate']:.1%} of {d['hits_n']} moves" if d["hit_rate"] is not None else "n/a"
            L.append(f"| {d['day']} | scored | {d['n']} | {d['corr']:.3f} | {d['r2']:.4f} | {hit} |")
        else:
            L.append(f"| {d['day']} | left out: {d['status']} | {d['n'] or ''} | | | |")
    L += ["", "## Limits", "",
          "- One snapshot a second of the best bid and ask. Book changes between snapshots are missed.",
          "- A different market from the LOBSTER study. This shows whether the method holds up over time; "
          "it does not confirm the NASDAQ numbers.",
          "- A prediction is not a profit: no fees, latency or fills are modelled here.", ""]
    return "\n".join(L)


def write_track(res: dict, out_dir: str | Path) -> Path:
    out = Path(out_dir) / res["frozen"]["symbol"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "track.json").write_text(json.dumps(res, indent=2), encoding="utf-8")
    (out / "track.md").write_text(render_track(res), encoding="utf-8")
    scored = [d for d in res["days"] if d["status"] == SCORED]
    if scored:
        (out / "track.svg").write_text(line_chart(
            "Daily out-of-sample correlation of the frozen signal",
            "One point per scored day after the freeze, in date order. The rule marks zero.",
            "scored day", [Series("correlation", [(i + 1, d["corr"]) for i, d in enumerate(scored)])],
            reference_y=0.0), encoding="utf-8")
    return out
