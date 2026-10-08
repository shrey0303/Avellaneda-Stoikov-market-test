"""Phases 5-7 end to end for one stock: calibrate, trade, benchmark, write up.

    morning    calibrate sigma, A, k                       (calibration.py)
    afternoon  run every strategy variant on the replay    (strategy.py)
    model      same parameters in the model's own world    (model_world.py)
    report     Q1-Q6 under both fill rules, with bootstrap intervals over windows

The morning window ends where the afternoon window starts, and calibration
stops reading at that point, so nothing traded on was used to calibrate.

Each fill rule is carried through the whole pipeline on its own: A and k are
fitted from probes filled under that rule, and the strategies then trade
under that rule. Q6 compares the two pipelines.
"""

from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass, field
from pathlib import Path
from statistics import fmean
from typing import Callable

from . import as_model, model_world, signals
from .as_model import ASParams
from .calibration import Calibration, CalibrationConfig, calibrate, rate_table
from .lobster_format import NS_PER_S, PRICE_SCALE, TICK_SIZE
from .parser import LobsterFiles
from .plots import Series, line_chart
from .queue_tracker import FillRule
from .session import SESSION_END_NS, SESSION_START_NS
from .signals import SignalConfig, SignalStudy
from .stats import Estimate, bootstrap_mean, paired_difference
from .strategy import SIGNAL, RunResult, RunSpec, StrategyConfig, markouts, run_strategies, windows_between
from .synthetic import SyntheticConfig

TICK_DOLLARS = TICK_SIZE / PRICE_SCALE
RULES = (FillRule.CONSERVATIVE, FillRule.OPTIMISTIC)


@dataclass(frozen=True)
class StudyConfig:
    exclude_s: float = 60.0              # skipped at the open and at the close
    split_s: float = 45_900.0            # 12:45:00 - calibrate before, trade after
    penalty_ticks: tuple[float, ...] = (1.0, 2.0, 4.0)
    markout_horizons_s: tuple[float, ...] = (1.0, 5.0, 30.0)
    calibration: CalibrationConfig = field(default_factory=CalibrationConfig)
    strategy: StrategyConfig = field(default_factory=StrategyConfig)
    signals: SignalConfig = field(default_factory=SignalConfig)
    model_paths: int = 200
    model_dt: float = 0.5
    n_boot: int = 2000
    seed: int = 0


def run_study(files: LobsterFiles, cfg: StudyConfig = StudyConfig(), log: Callable[[str], None] = lambda s: None) -> dict:
    start_ns = SESSION_START_NS + int(cfg.exclude_s * NS_PER_S)
    split_ns = int(cfg.split_s * NS_PER_S)
    end_ns = SESSION_END_NS - int(cfg.exclude_s * NS_PER_S)

    def est(values) -> Estimate:
        return bootstrap_mean(list(values), n_boot=cfg.n_boot, seed=cfg.seed)

    def diff(a, b) -> Estimate:
        return paired_difference(list(a), list(b), n_boot=cfg.n_boot, seed=cfg.seed)

    log(f"calibrating on {_clock(start_ns)} .. {_clock(split_ns)}")
    cal = calibrate(files, start_ns, split_ns, cfg.calibration)
    result: dict = {
        "ticker": files.ticker,
        "date": files.date,
        "synthetic": files.ticker == SyntheticConfig().ticker,
        "config": _config_dict(cfg, start_ns, split_ns, end_ns),
        "calibration": _calibration_dict(cal),
        "signal": None,
        "runs": [],
        "model": [],
        "questions": {},
        "problems": [],
    }
    if cal.sigma is None or cal.sigma <= 0:
        result["problems"].append(
            f"no sigma at the {cal.sigma_horizon_s}s horizon: too little mid-price data in the calibration window"
        )
        return result

    log("measuring order-book signals: fit on the morning, score on the afternoon")
    test_windows = windows_between(split_ns, end_ns, cfg.strategy.window_s)
    sg = signals.analyse(files, start_ns, split_ns, end_ns, test_windows, cfg.signals)
    result["signal"] = _signal_dict(sg, est)
    if sg.skew is None:
        result["problems"].append("no signal could be fitted at the skew horizon; the signal strategy was not traded")

    horizon = cfg.strategy.window_s
    params: dict[tuple[FillRule, float], ASParams] = {}
    for rule in RULES:
        fit = cal.fits[rule]
        if not fit.usable:
            result["problems"].append(
                f"{rule.value}: intensity fit unusable (fills={fit.n_fills}, k={fit.k:g}); this rule was not traded"
            )
            continue
        for pt in cfg.penalty_ticks:
            gamma = as_model.gamma_for_penalty(pt * TICK_DOLLARS, cal.sigma, horizon)
            params[(rule, pt)] = ASParams(cal.sigma, fit.A, fit.k, gamma)
    if not params:
        return result

    specs = [
        (RunSpec(strategy, pt, sticky, rule), p)
        for (rule, pt), p in params.items()
        for strategy in as_model.STRATEGIES
        for sticky in (True, False)
    ]
    if sg.skew is not None:
        specs += [(RunSpec(SIGNAL, pt, True, rule), p) for (rule, pt), p in params.items()]
    log(f"trading {len(specs)} strategy variants on {_clock(split_ns)} .. {_clock(end_ns)}")
    results, series = run_strategies(files, specs, split_ns, end_ns, cfg.strategy,
                                     record_after_s=max(cfg.markout_horizons_s), skew=sg.skew)
    by_spec = {r.spec: r for r in results}

    for r in results:
        result["runs"].append(_run_dict(r, markouts(r, series, cfg.markout_horizons_s), est))

    log(f"simulating the model world ({cfg.model_paths} paths per variant)")
    model: dict[tuple[FillRule, str, float], list[model_world.ModelPath]] = {}
    for (rule, pt), p in params.items():
        for strategy in as_model.STRATEGIES:
            paths = model_world.simulate(strategy, p, horizon, cfg.model_paths, cfg.model_dt, cfg.strategy.lot, cfg.seed)
            model[(rule, strategy, pt)] = paths
            result["model"].append({
                "rule": rule.value, "strategy": strategy, "penalty_ticks": pt,
                "pnl": est(x.pnl for x in paths).to_dict(),
                "spread_capture": est(x.spread_capture for x in paths).to_dict(),
                "inventory_pnl": est(x.inventory_pnl for x in paths).to_dict(),
                "fills": est(x.fills for x in paths).to_dict(),
                "abs_end_inventory": est(abs(x.end_inventory) for x in paths).to_dict(),
            })

    result["questions"] = _questions(cfg, cal, params, by_spec, model, series, est, diff)
    result["questions"]["Q7_signal_prediction"] = result["signal"]["scores"]
    return result


# ---------------------------------------------------------------------------
# Assembling the result
# ---------------------------------------------------------------------------


def _config_dict(cfg: StudyConfig, start_ns: int, split_ns: int, end_ns: int) -> dict:
    d = asdict(cfg)
    d["calibration_window"] = [_clock(start_ns), _clock(split_ns)]
    d["test_window"] = [_clock(split_ns), _clock(end_ns)]
    return d


def _clock(time_ns: int) -> str:
    s = time_ns // NS_PER_S
    return f"{s // 3600:02d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def _calibration_dict(cal: Calibration) -> dict:
    intensity = {}
    for rule in RULES:
        fit, probes = cal.fits[rule], cal.probes[rule]
        intensity[rule.value] = {**asdict(fit), "usable": fit.usable,
                                 "table": [asdict(row) for row in rate_table(probes, fit)]}
    sp = cal.spread
    return {
        "messages_read": cal.messages,
        "sigma": cal.sigma,
        "sigma_horizon_s": cal.sigma_horizon_s,
        "variance_ratio": [asdict(p) for p in cal.variance_ratio],
        "intensity": intensity,
        "spread": {
            "share_one_tick": sp.share(1),
            "mean_ticks": sp.mean_ticks,
            "tick_group": sp.tick_group() if sp.total_ns else None,
            "seconds_by_ticks": {str(t): ns / NS_PER_S for t, ns in sorted(sp.ns_by_ticks.items())},
        },
    }


def _signal_dict(sg: SignalStudy, est) -> dict:
    """Morning fit beside afternoon score for every signal and horizon."""
    fits = {(f.signal, f.horizon_s): f for f in sg.fits}

    def num(x: float) -> float | None:   # NaN is not valid JSON
        return None if math.isnan(x) else x

    scores = []
    for s in sg.scores:
        f = fits[(s.signal, s.horizon_s)]
        e = est(s.window_corrs)
        scores.append({
            "signal": s.signal, "horizon_s": s.horizon_s,
            "fit_n": f.n, "fit_corr": num(f.corr), "slope_ticks": f.slope,
            "test_n": s.n, "test_corr": num(s.corr), "window_corr": e.to_dict(),
            "r2": num(s.r2), "hit_rate": num(s.hit_rate), "hits_n": s.hits_n,
            "verdict": _verdict(e) if s.hits_n else "the mid did not move in the test window",
        })
    return {**sg.to_dict(), "scores": scores}


def _window_markouts(per_window: dict[int, list[float]]) -> list[float]:
    """One number per window that had fills: that window's mean markout, in ticks."""
    return [fmean(v) / TICK_DOLLARS for _, v in sorted(per_window.items())]


def _run_dict(r: RunResult, marks: dict, est) -> dict:
    w = r.windows
    return {
        "label": r.spec.label,
        "strategy": r.spec.strategy,
        "penalty_ticks": r.spec.penalty_ticks,
        "sticky": r.spec.sticky,
        "rule": r.spec.rule.value,
        "gamma": r.params.gamma,
        "windows": [asdict(x) for x in w],
        "pnl": est(x.pnl for x in w).to_dict(),
        "spread_capture": est(x.spread_capture for x in w).to_dict(),
        "inventory_pnl": est(x.inventory_pnl for x in w).to_dict(),
        "fills": est(x.fills for x in w).to_dict(),
        "abs_end_inventory": est(abs(x.end_inventory) for x in w).to_dict(),
        "realised_pnl": est(x.realised_pnl for x in w).to_dict(),
        "closed_pnl": est(x.closed_pnl for x in w).to_dict(),
        "shares_traded": est(x.shares_bought + x.shares_sold for x in w).to_dict(),
        "total_fills": sum(x.fills for x in w),
        "total_posts": sum(x.posts for x in w),
        "total_overtaken": sum(x.overtaken for x in w),
        "total_skew_moved": sum(x.skew_moved for x in w),
        "markout_ticks": {
            f"{h:g}": {**est(_window_markouts(per_window)).to_dict(), "fills": sum(len(v) for v in per_window.values())}
            for h, per_window in marks.items()
        },
    }


def _verdict(e: Estimate) -> str:
    if e.n < 2:
        return "too few windows"
    if not e.excludes_zero:
        return "inside the interval: no claim"
    return "positive" if e.mean > 0 else "negative"


def _across_rules(by_rule: dict[str, Estimate]) -> str:
    """Q6: does a finding survive the choice of fill rule?"""
    if len(by_rule) < len(RULES):
        return "only one rule available"
    signs = {(_verdict(e)) for e in by_rule.values()}
    if signs == {"positive"} or signs == {"negative"}:
        return "holds under both rules"
    if signs == {"positive", "negative"}:
        return "FLIPS between rules: not a conclusion"
    return "not established under both rules: not a conclusion"


def _questions(cfg, cal, params, by_spec, model, series, est, diff) -> dict:
    rules = [rule for rule in RULES if any(r == rule for r, _ in params)]
    q1, q2, q3, q4, compare = [], [], [], [], []
    q8_pnl, q8_marks = [], []
    claims: dict[str, dict[str, Estimate]] = {}

    for rule in rules:
        for pt in cfg.penalty_ticks:
            for strategy in as_model.STRATEGIES:
                run = by_spec[RunSpec(strategy, pt, True, rule)]
                requeue = by_spec[RunSpec(strategy, pt, False, rule)]
                paths = model[(rule, strategy, pt)]
                key = {"rule": rule.value, "strategy": strategy, "penalty_ticks": pt}
                pnl = [w.pnl for w in run.windows]

                replay_pnl, model_pnl = est(pnl), est(p.pnl for p in paths)
                overlap = replay_pnl.lo <= model_pnl.hi and model_pnl.lo <= replay_pnl.hi
                q1.append({**key, "replay_pnl": replay_pnl.to_dict(), "model_pnl": model_pnl.to_dict(),
                           "replay_fills": est(w.fills for w in run.windows).to_dict(),
                           "model_fills": est(p.fills for p in paths).to_dict(),
                           "verdict": "intervals overlap: no claim" if overlap else
                                      ("replay below model" if replay_pnl.mean < model_pnl.mean else "replay above model")})

                marks = markouts(run, series, cfg.markout_horizons_s)
                for h, per_window in marks.items():
                    e = est(_window_markouts(per_window))
                    q2.append({**key, "horizon_s": h, "markout_ticks": e.to_dict(),
                               "fills": sum(len(v) for v in per_window.values()), "verdict": _verdict(e)})
                    claims.setdefault(f"markout {h:g}s, {strategy}, {pt:g} ticks", {})[rule.value] = e

                q3.append({**key,
                           "replay_spread_capture": est(w.spread_capture for w in run.windows).to_dict(),
                           "replay_inventory_pnl": est(w.inventory_pnl for w in run.windows).to_dict(),
                           "model_spread_capture": est(p.spread_capture for p in paths).to_dict(),
                           "model_inventory_pnl": est(p.inventory_pnl for p in paths).to_dict()})

                d = diff(pnl, [w.pnl for w in requeue.windows])
                q4.append({**key, "pnl_sticky_minus_requeue": d.to_dict(),
                           "fills_sticky_minus_requeue": diff([w.fills for w in run.windows],
                                                              [w.fills for w in requeue.windows]).to_dict(),
                           "verdict": _verdict(d)})
                claims.setdefault(f"queue value (sticky - requeue P&L), {strategy}, {pt:g} ticks", {})[rule.value] = d

            inv = by_spec[RunSpec(as_model.INVENTORY, pt, True, rule)].windows
            sym = by_spec[RunSpec(as_model.SYMMETRIC, pt, True, rule)].windows
            d = diff([w.pnl for w in inv], [w.pnl for w in sym])
            compare.append({"rule": rule.value, "penalty_ticks": pt, "pnl_inventory_minus_symmetric": d.to_dict(),
                            "abs_inventory_inventory_minus_symmetric": diff(
                                [abs(w.end_inventory) for w in inv], [abs(w.end_inventory) for w in sym]).to_dict(),
                            "verdict": _verdict(d)})
            claims.setdefault(f"inventory - symmetric P&L, {pt:g} ticks", {})[rule.value] = d

            lean = by_spec.get(RunSpec(SIGNAL, pt, True, rule))
            if lean is None:
                continue
            plain = by_spec[RunSpec(as_model.INVENTORY, pt, True, rule)]
            d = diff([w.pnl for w in lean.windows], [w.pnl for w in inv])
            q8_pnl.append({"rule": rule.value, "penalty_ticks": pt, "pnl_signal_minus_inventory": d.to_dict(),
                           "fills_signal_minus_inventory": diff([w.fills for w in lean.windows],
                                                                [w.fills for w in inv]).to_dict(),
                           "requotes_moved_by_skew": sum(w.skew_moved for w in lean.windows),
                           "verdict": _verdict(d)})
            claims.setdefault(f"signal - inventory P&L, {pt:g} ticks", {})[rule.value] = d
            m_lean = markouts(lean, series, cfg.markout_horizons_s)
            m_plain = markouts(plain, series, cfg.markout_horizons_s)
            for h in cfg.markout_horizons_s:
                # pair the two runs on windows where both had fills
                both = sorted(set(m_lean[h]) & set(m_plain[h]))
                a = [fmean(m_lean[h][w]) / TICK_DOLLARS for w in both]
                b = [fmean(m_plain[h][w]) / TICK_DOLLARS for w in both]
                d = diff(a, b)
                q8_marks.append({"rule": rule.value, "penalty_ticks": pt, "horizon_s": h,
                                 "markout_signal": est(a).to_dict(), "markout_inventory": est(b).to_dict(),
                                 "markout_signal_minus_inventory": d.to_dict(), "verdict": _verdict(d)})
                claims.setdefault(f"signal - inventory markout {h:g}s, {pt:g} ticks", {})[rule.value] = d

    sp = cal.spread
    q6 = [{"claim": name, **{rule: e.to_dict() for rule, e in by_rule.items()}, "verdict": _across_rules(by_rule)}
          for name, by_rule in claims.items()]
    return {
        "Q1_model_vs_replay_pnl": q1,
        "Q2_markouts": q2,
        "Q3_pnl_decomposition": q3,
        "Q4_queue_value": q4,
        "Q5_tick_size": {"share_one_tick": sp.share(1), "mean_spread_ticks": sp.mean_ticks,
                         "tick_group": sp.tick_group() if sp.total_ns else None,
                         "note": "Compare Q4 across stocks in the two groups; one stock cannot answer Q5."},
        "Q6_fill_rule_sensitivity": q6,
        "Q8_signal_skew": {"pnl": q8_pnl, "markouts": q8_marks},
        "inventory_vs_symmetric": compare,
    }


# ---------------------------------------------------------------------------
# Writing it up
# ---------------------------------------------------------------------------

SYNTHETIC_WARNING = (
    "> **This run used synthetic placeholder data.** The order flow is random, so every number "
    "below only shows that the pipeline runs. None of it says anything about markets."
)


def _e(d: dict, unit: str = "") -> str:
    if d["n"] == 0:
        return "n/a"
    return f"{d['mean']:.3f}{unit} [{d['lo']:.3f}, {d['hi']:.3f}]"


def _n(x: float | None, spec: str) -> str:
    return "n/a" if x is None else format(x, spec)


def _table(header: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)]
    out += ["| " + " | ".join(str(c) for c in row) + " |" for row in rows]
    return out + [""]


def _headline(res: dict) -> list[str]:
    """The study's three main findings as plain sentences, each with its interval and verdict.

    Uses the middle risk-aversion setting and the middle markout horizon.
    """
    q, c = res["questions"], res["config"]
    pt = c["penalty_ticks"][len(c["penalty_ticks"]) // 2]
    h = c["markout_horizons_s"][len(c["markout_horizons_s"]) // 2]
    by_claim = {r["claim"]: r for r in q["Q6_fill_rule_sensitivity"]}

    def both(r: dict, unit: str) -> str:
        return "; ".join(f"{rule} {_e(r[rule], unit)}" for rule in ("conservative", "optimistic") if rule in r)

    out = []
    r = by_claim.get(f"markout {h:g}s, {as_model.INVENTORY}, {pt:g} ticks")
    if r:
        out.append(f"- **Adverse selection.** {h:g} s after a fill, the mid had moved by {both(r, ' ticks')} "
                   f"per share (negative is against us). Across fill rules: {r['verdict']}.")
    rows = [x for x in q["Q1_model_vs_replay_pnl"] if x["strategy"] == as_model.INVENTORY and x["penalty_ticks"] == pt]
    if rows:
        out.append("- **Model against replay.** " + "; ".join(
            f"{x['rule']}: replay {_e(x['replay_pnl'])} against the model's {_e(x['model_pnl'])} dollars per window "
            f"({x['verdict']})" for x in rows) + ".")
    skew = (res["signal"] or {}).get("skew")
    if skew:
        s = next(x for x in res["signal"]["scores"]
                 if x["signal"] == skew["signal"] and x["horizon_s"] == skew["horizon_s"])
        text = (f"- **Prediction.** `{s['signal']}` had an out-of-sample correlation of {_e(s['window_corr'])} with "
                f"the mid change over the next {s['horizon_s']} s ({s['verdict']}).")
        r = by_claim.get(f"signal - inventory markout {h:g}s, {pt:g} ticks")
        if r:
            text += (f" Leaning quotes on it changed the {h:g} s markout by {both(r, ' ticks')}. "
                     f"Across fill rules: {r['verdict']}.")
        out.append(text)
    return out


def render_report(res: dict) -> str:
    c, cal, q = res["config"], res["calibration"], res["questions"]
    L = [f"# {res['ticker']} {res['date']}: Avellaneda-Stoikov replay study", ""]
    if res["synthetic"]:
        L += [SYNTHETIC_WARNING, ""]
    L += [
        f"- Calibrated on {c['calibration_window'][0]} to {c['calibration_window'][1]}; "
        f"traded on {c['test_window'][0]} to {c['test_window'][1]}.",
        f"- Windows of {c['strategy']['window_s']:g} s, each an independent session. Requote every "
        f"{c['strategy']['requote_s']:g} s and after each fill. One lot = {c['strategy']['lot']} shares per side.",
        "- Figures are means over windows with a 95% bootstrap interval in brackets. "
        "A difference whose interval contains zero is not claimed.",
        "- P&L is in dollars per window, before fees and rebates. Markouts are in ticks per share.",
        "",
    ]
    if q:
        L += ["## Headline", "", "Middle settings only; every setting is in the tables below.", ""] + _headline(res) + [""]
    if res["problems"]:
        L += ["## Problems", ""] + [f"- {p}" for p in res["problems"]] + [""]

    L += ["## Calibration", "", f"sigma = {cal['sigma']:.6g} dollars per sqrt(second), taken at the "
          f"{cal['sigma_horizon_s']} s horizon." if cal["sigma"] else "sigma could not be estimated.", "",
          "![Variance ratio](variance_ratio.svg)", ""]
    L += _table(["horizon (s)", "sigma ($/sqrt s)", "increments", "variance ratio vs longest"],
                [[p["horizon_s"], f"{p['sigma']:.6f}", p["n"], f"{p['ratio']:.3f}"] for p in cal["variance_ratio"]])
    for rule, fit in cal["intensity"].items():
        L += [f"### Fill intensity, {rule} rule", "",
              f"A = {fit['A']:.5g} per second, k = {fit['k']:.5g} per dollar, from {fit['n_obs']} probes, "
              f"{fit['n_fills']} filled, {fit['exposure_s']:.0f} s of exposure."
              + ("" if fit["usable"] else " **Not usable: the likelihood has no interior maximum.**"), "",
              f"![Fill intensity, {rule}](intensity_{rule}.svg)", ""]
        L += _table(["ticks behind touch", "probes", "fills", "exposure (s)", "mean delta ($)", "empirical rate (/s)", "fitted rate (/s)"],
                    [[r["depth_ticks"], r["probes"], r["fills"], f"{r['exposure_s']:.0f}", f"{r['mean_delta']:.4f}",
                      f"{r['empirical']:.5f}", f"{r['fitted']:.5f}"] for r in fit["table"]])
    if not q:
        return "\n".join(L)

    def key(r):
        return [r["rule"], r["strategy"], f"{r['penalty_ticks']:g}"]

    head = ["fill rule", "strategy", "penalty (ticks)"]
    L += ["## Q1. Does the calibrated model predict replay P&L?", ""]
    L += _table(head + ["replay P&L", "model P&L", "replay fills", "model fills", "verdict"],
                [key(r) + [_e(r["replay_pnl"]), _e(r["model_pnl"]), _e(r["replay_fills"]), _e(r["model_fills"]), r["verdict"]]
                 for r in q["Q1_model_vs_replay_pnl"]])
    L += ["### Replay profit three ways", "",
          "Every fill is booked at its own price. Shares still held when a window closes have no trade price, so "
          "the profit depends on how they are valued. Realised counts completed buy-and-sell pairs only (first in, "
          "first out). The middle column is the replay P&L used everywhere else in this report. The last column "
          "trades the leftover out against the real book at the close, level by level, which is what closing would "
          "have cost. Sticky quotes.", ""]
    L += _table(["run", "realised", "leftover valued at the mid", "leftover closed at real prices",
                 "shares left at the close", "shares traded per window"],
                [[r["label"], _e(r["realised_pnl"]), _e(r["pnl"]), _e(r["closed_pnl"]),
                  f"{r['abs_end_inventory']['mean']:.0f}", f"{r['shares_traded']['mean']:.0f}"]
                 for r in res["runs"] if r["sticky"]])
    L += ["## Q2. Adverse selection: markouts on replay fills", "",
          "Negative means the mid moved against us after the fill. In the model world the expected markout is zero.", "",
          "![Markouts](markouts.svg)", ""]
    L += _table(head + ["horizon (s)", "markout (ticks)", "fills", "verdict"],
                [key(r) + [f"{r['horizon_s']:g}", _e(r["markout_ticks"]), r["fills"], r["verdict"]] for r in q["Q2_markouts"]])
    L += ["## Q3. Where the gap comes from: spread capture and inventory P&L", ""]
    L += _table(head + ["replay spread capture", "model spread capture", "replay inventory P&L", "model inventory P&L"],
                [key(r) + [_e(r["replay_spread_capture"]), _e(r["model_spread_capture"]),
                           _e(r["replay_inventory_pnl"]), _e(r["model_inventory_pnl"])] for r in q["Q3_pnl_decomposition"]])
    L += ["## Q4. What queue position is worth: sticky minus always-requeue", ""]
    L += _table(head + ["P&L difference", "fills difference", "verdict"],
                [key(r) + [_e(r["pnl_sticky_minus_requeue"]), _e(r["fills_sticky_minus_requeue"]), r["verdict"]]
                 for r in q["Q4_queue_value"]])
    q5 = q["Q5_tick_size"]
    L += ["## Q5. Tick size", "",
          f"In the calibration window the spread was one tick {q5['share_one_tick']:.1%} of the time "
          f"(mean {q5['mean_spread_ticks']:.2f} ticks), which puts this stock in the **{q5['tick_group']}** group. "
          f"{q5['note']}", ""]
    L += ["## Inventory strategy against symmetric", ""]
    L += _table(["fill rule", "penalty (ticks)", "P&L difference", "|end inventory| difference (shares)", "verdict"],
                [[r["rule"], f"{r['penalty_ticks']:g}", _e(r["pnl_inventory_minus_symmetric"]),
                  _e(r["abs_inventory_inventory_minus_symmetric"]), r["verdict"]] for r in q["inventory_vs_symmetric"]])
    L += ["## Q6. Do the findings survive the choice of fill rule?", ""]
    L += _table(["finding", "conservative", "optimistic", "verdict"],
                [[r["claim"], _e(r["conservative"]) if "conservative" in r else "n/a",
                  _e(r["optimistic"]) if "optimistic" in r else "n/a", r["verdict"]] for r in q["Q6_fill_rule_sensitivity"]])
    sig = res["signal"]
    L += ["## Q7. Does the order book predict the next price move?", "",
          "Beyond the approach document's six questions. Each signal is positive when the book or the recent flow "
          "leans towards buyers. A line was fitted on the calibration window and scored on the test window, "
          f"{sig['samples_fit']} and {sig['samples_test']} one-second samples. The correlation is the mean over "
          "windows, with its interval; R² is measured against predicting no change.", "",
          "![Signal correlation by horizon](signal_decay.svg)", ""]
    L += _table(["signal", "horizon (s)", "fitted slope (ticks per unit)", "correlation, fit window",
                 "correlation, test windows", "R², test", "direction called", "verdict"],
                [[r["signal"], r["horizon_s"], f"{r['slope_ticks']:.4f}", _n(r["fit_corr"], ".3f"), _e(r["window_corr"]),
                  _n(r["r2"], ".4f"),
                  f"{r['hit_rate']:.1%} of {r['hits_n']} moves" if r["hit_rate"] is not None else "n/a", r["verdict"]]
                 for r in q["Q7_signal_prediction"]])
    q8 = q["Q8_signal_skew"]
    L += ["## Q8. Does leaning quotes on the signal reduce adverse selection?", ""]
    if sig["skew"] and q8["pnl"]:
        k = sig["skew"]
        L += [f"The signal strategy is the inventory strategy with both quotes shifted by the fitted move: "
              f"`{k['signal']}` at the {k['horizon_s']} s horizon, {k['slope_dollars']:.6f} dollars per unit. It was "
              "chosen for the strongest correlation in the calibration window. Differences are signal minus "
              "inventory, paired by window; a positive markout difference means less adverse selection.", ""]
        L += _table(["fill rule", "penalty (ticks)", "P&L difference", "fills difference",
                     "requotes where the skew moved a quote by a tick or more", "verdict"],
                    [[r["rule"], f"{r['penalty_ticks']:g}", _e(r["pnl_signal_minus_inventory"]),
                      _e(r["fills_signal_minus_inventory"]), r["requotes_moved_by_skew"],
                      r["verdict"]] for r in q8["pnl"]])
        L += _table(["fill rule", "penalty (ticks)", "horizon (s)", "markout, signal", "markout, inventory",
                     "difference", "verdict"],
                    [[r["rule"], f"{r['penalty_ticks']:g}", f"{r['horizon_s']:g}", _e(r["markout_signal"]),
                      _e(r["markout_inventory"]), _e(r["markout_signal_minus_inventory"]), r["verdict"]]
                     for r in q8["markouts"]])
    else:
        L += ["The signal strategy was not traded (see Problems).", ""]
    L += ["## Diagnostics", ""]
    L += _table(["run", "fills", "orders posted", "requotes that found our order overtaken"],
                [[r["label"], r["total_fills"], r["total_posts"], r["total_overtaken"]] for r in res["runs"]])
    L += ["An overtaken order is one the real book moved through between requotes. In reality it would have "
          "traded; the replay only fills it at the next real execution (see README, limitations).", ""]
    return "\n".join(L)


def render_plots(res: dict) -> dict[str, str]:
    cal, q = res["calibration"], res["questions"]
    plots = {"variance_ratio.svg": line_chart(
        "Variance ratio of the mid price",
        "Per-second variance at each horizon, relative to the longest. The rule marks 1.",
        "horizon (s)", [Series("variance ratio", [(p["horizon_s"], p["ratio"]) for p in cal["variance_ratio"]])],
        log_x=True, reference_y=1.0)}
    for rule, fit in cal["intensity"].items():
        rows = [r for r in fit["table"] if r["exposure_s"] > 0]
        plots[f"intensity_{rule}.svg"] = line_chart(
            f"Fill rate by distance behind the touch, {rule} rule",
            "Fills per second of resting time.",
            "ticks behind the touch",
            [Series("empirical", [(r["depth_ticks"], r["empirical"]) for r in rows], line=False),
             Series("fitted", [(r["depth_ticks"], r["fitted"]) for r in rows])])
    if q:
        pts = res["config"]["penalty_ticks"]
        mid_pt = pts[len(pts) // 2]
        series = []
        for rule in RULES:
            rows = [r for r in q["Q2_markouts"] if r["rule"] == rule.value and r["strategy"] == as_model.INVENTORY
                    and r["penalty_ticks"] == mid_pt and r["markout_ticks"]["n"]]
            series.append(Series(rule.value, [(r["horizon_s"], r["markout_ticks"]["mean"]) for r in rows]))
        plots["markouts.svg"] = line_chart(
            "Markout after a fill, by horizon",
            f"Inventory strategy, {mid_pt:g}-tick penalty, sticky quotes. Ticks per share; below 0 is adverse.",
            "seconds after the fill", series, reference_y=0.0)
        scores = res["signal"]["scores"]
        plots["signal_decay.svg"] = line_chart(
            "Signal correlation with the next mid change, by horizon",
            "Out of sample: fitted on the calibration window, mean correlation over test windows.",
            "horizon (s)",
            [Series(name, [(r["horizon_s"], r["window_corr"]["mean"]) for r in scores
                           if r["signal"] == name and r["window_corr"]["n"]]) for name in signals.SIGNALS],
            log_x=True, reference_y=0.0)
    return plots


def write_outputs(res: dict, out_dir: str | Path) -> Path:
    """Write results.json, report.md and the plots into out_dir/<ticker>/; returns that directory."""
    out = Path(out_dir) / res["ticker"]
    out.mkdir(parents=True, exist_ok=True)
    (out / "results.json").write_text(json.dumps(res, indent=1, default=str), encoding="utf-8")
    (out / "report.md").write_text(render_report(res), encoding="utf-8")
    for name, svg in render_plots(res).items():
        (out / name).write_text(svg, encoding="utf-8")
    return out


def render_summary(results: list[dict]) -> str:
    """Cross-stock view for Q5: is queue position worth more in large-tick stocks?"""
    L = ["# Cross-stock summary", ""]
    if any(r["synthetic"] for r in results):
        L += [SYNTHETIC_WARNING, ""]
    rows = []
    for r in results:
        q5 = r["questions"].get("Q5_tick_size")
        if not q5:
            rows.append([r["ticker"], "n/a", "n/a", "not traded: " + "; ".join(r["problems"]), "", ""])
            continue
        for row in r["questions"]["Q4_queue_value"]:
            rows.append([r["ticker"], f"{q5['share_one_tick']:.1%}", q5["tick_group"],
                         f"{row['rule']} / {row['strategy']} / {row['penalty_ticks']:g}t",
                         _e(row["pnl_sticky_minus_requeue"]), row["verdict"]])
    L += _table(["stock", "time at one-tick spread", "group", "run", "sticky minus requeue P&L ($/window)", "verdict"], rows)
    L += ["Stated in advance (approach document §5.6): the queue effect should be much stronger in the "
          "large-tick group. With one day per stock this is a comparison of a few stocks, not a test.", ""]
    return "\n".join(L)
