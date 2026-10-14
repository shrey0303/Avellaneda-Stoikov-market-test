"""Phase 12 reports: how the A-S strategies did on each real IEX day, and across days.

Every figure is per day. A mean over days carries a 95% bootstrap interval
over days, and a difference is only claimed when its interval excludes zero,
as in the LOBSTER study.
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

from . import as_model
from .live import CONSERVATIVE, OPTIMISTIC, RULES, LiveConfig, load_days
from .plots import Series, line_chart
from .stats import Estimate, bootstrap_mean, paired_difference

HEADLINE_PT = 2.0
INV, SYM = as_model.INVENTORY, as_model.SYMMETRIC

CAVEATS = [
    "IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. "
    "The strategy is simulated as if it quoted on IEX alone.",
    "No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule "
    "fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies "
    "between the two.",
    "Calibrated on earlier days only (up to five). The first day of each stock only calibrates.",
    "P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, "
    "before fees and rebates.",
]


def _run(day: dict, strategy: str, pt: float, rule: str) -> dict | None:
    for r in day.get("runs", ()):
        if r["strategy"] == strategy and r["penalty_ticks"] == pt and r["rule"] == rule:
            return r
    return None


def _e(e: Estimate, spec: str = ".2f") -> str:
    if e.n == 0:
        return "n/a"
    if e.n == 1:
        return f"{e.mean:{spec}} (one day)"
    return f"{e.mean:{spec}} [{e.lo:{spec}}, {e.hi:{spec}}]"


def _verdict(e: Estimate) -> str:
    if e.n < 2:
        return "too few days"
    if e.excludes_zero:
        return "positive" if e.mean > 0 else "negative"
    return "not established"


def _table(header: list[str], rows: list[list]) -> list[str]:
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header),
            *["| " + " | ".join(str(c) for c in row) + " |" for row in rows], ""]


def _f(x, spec: str) -> str:
    return "n/a" if x is None else f"{x:{spec}}"


def symbol_summary(days: Sequence[dict], cfg: LiveConfig = LiveConfig()) -> dict:
    traded = [d for d in days if d.get("runs")]
    out = {"symbol": days[0]["symbol"] if days else "", "days_traded": len(traded),
           "days_calibration_only": sum(1 for d in days if not d.get("no_data") and not d.get("runs")),
           "days_no_data": sum(1 for d in days if d.get("no_data")),
           "first": traded[0]["date"] if traded else None, "last": traded[-1]["date"] if traded else None,
           "runs": [], "compare": []}
    for rule in RULES:
        for pt in cfg.penalty_ticks:
            per = {}
            for strategy in (INV, SYM):
                pnl = [r["day_pnl"] for d in traded if (r := _run(d, strategy, pt, rule))]
                marks = [r["markout_mean"] for d in traded
                         if (r := _run(d, strategy, pt, rule)) and r["markout_mean"] is not None]
                fills = [r["fills"] for d in traded if (r := _run(d, strategy, pt, rule))]
                per[strategy] = pnl
                out["runs"].append({
                    "rule": rule, "strategy": strategy, "penalty_ticks": pt,
                    "pnl": bootstrap_mean(pnl, n_boot=cfg.n_boot, seed=cfg.seed),
                    "positive_days": sum(1 for x in pnl if x > 0), "days": len(pnl),
                    "fills_per_day": sum(fills) / len(fills) if fills else None,
                    "markout": bootstrap_mean(marks, n_boot=cfg.n_boot, seed=cfg.seed),
                })
            if per[INV] and len(per[INV]) == len(per[SYM]):
                out["compare"].append({"rule": rule, "penalty_ticks": pt,
                                       "diff": paired_difference(per[INV], per[SYM], n_boot=cfg.n_boot, seed=cfg.seed)})
    return out


def _headline(s: dict, rule: str) -> dict | None:
    return next((r for r in s["runs"] if r["rule"] == rule and r["strategy"] == INV
                 and r["penalty_ticks"] == HEADLINE_PT), None)


def render_symbol(days: Sequence[dict], cfg: LiveConfig = LiveConfig()) -> tuple[str, str]:
    """(summary.md, cumulative P&L svg) for one stock."""
    s = symbol_summary(days, cfg)
    sym = s["symbol"]
    L = [f"# {sym}: Avellaneda-Stoikov on real IEX data, day by day", ""]
    L += [f"- Traded days: {s['days_traded']}" + (f" ({s['first']} to {s['last']})" if s["first"] else ""),
          f"- Calibration-only days: {s['days_calibration_only']}; days without IEX data: {s['days_no_data']}", ""]
    L += [f"- {c}" for c in CAVEATS] + [""]
    if not s["days_traded"]:
        L += ["No day has been traded yet.", ""]
        return "\n".join(L), ""

    L += ["## Headline", "", f"Inventory strategy, risk aversion {HEADLINE_PT:g} ticks per lot.", ""]
    for rule in RULES:
        h = _headline(s, rule)
        if h:
            L.append(f"- **{rule}**: mean daily P&L {_e(h['pnl'])} dollars ({_verdict(h['pnl'])}); "
                     f"{h['positive_days']} of {h['days']} days positive; "
                     f"{_f(h['fills_per_day'], '.0f')} fills a day; "
                     f"5 s markout {_e(h['markout'], '.3f')} ticks per fill (negative is against us).")
    L.append("")

    L += ["## Every setting", "", "Mean over days, 95% bootstrap interval over days in brackets.", ""]
    L += _table(["rule", "strategy", "risk aversion (ticks)", "daily P&L ($)", "verdict", "positive days",
                 "fills/day", "5 s markout (ticks)"],
                [[r["rule"], r["strategy"], f"{r['penalty_ticks']:g}", _e(r["pnl"]), _verdict(r["pnl"]),
                  f"{r['positive_days']}/{r['days']}", _f(r["fills_per_day"], ".0f"), _e(r["markout"], ".3f")]
                 for r in s["runs"]])

    L += ["## Does inventory control help?", "",
          "Daily P&L of the inventory strategy minus the symmetric one, paired by day.", ""]
    L += _table(["rule", "risk aversion (ticks)", "inventory minus symmetric ($/day)", "verdict"],
                [[c["rule"], f"{c['penalty_ticks']:g}", _e(c["diff"]), _verdict(c["diff"])] for c in s["compare"]])

    L += ["## Day by day", "", f"Inventory strategy at {HEADLINE_PT:g} ticks.", ""]
    L.append("![Cumulative P&L](cumulative_pnl.svg)")
    L.append("")
    rows = []
    for d in days:
        if d.get("no_data"):
            rows.append([d["date"], "no IEX data", "", "", "", "", "", ""])
            continue
        cal = d.get("calibration")
        if not d.get("runs"):
            rows.append([d["date"], "calibration only", "", "", "", "", "", "; ".join(d.get("problems", []))])
            continue
        con, opt = _run(d, INV, HEADLINE_PT, CONSERVATIVE), _run(d, INV, HEADLINE_PT, OPTIMISTIC)
        fit = cal["intensity"].get(CONSERVATIVE)
        rows.append([d["date"], f"{cal['sigma']:.5f}",
                     f"{fit['A']:.4f} / {fit['k']:.1f}" if fit else "n/a",
                     _f(con and con["day_pnl"], ".2f"), _f(opt and opt["day_pnl"], ".2f"),
                     _f(con and con["fills"], "d"), _f(con and con["markout_mean"], ".3f"),
                     f"{d['quote_coverage']:.0%} quoted, {d['n_trades']} trades"])
    L += _table(["date", "sigma ($/sqrt s)", "A / k (conservative)", "P&L conservative ($)", "P&L optimistic ($)",
                 "fills (cons.)", "5 s markout (ticks, cons.)", "IEX data"], rows)

    chart = _cumulative_chart(days, sym)
    return "\n".join(L), chart


def _cumulative_chart(days: Sequence[dict], sym: str) -> str:
    series = []
    for strategy, name in ((INV, "inventory"), (SYM, "symmetric")):
        total, pts = 0.0, []
        for i, d in enumerate([d for d in days if d.get("runs")], start=1):
            r = _run(d, strategy, HEADLINE_PT, CONSERVATIVE)
            if r:
                total += r["day_pnl"]
                pts.append((i, total))
        series.append(Series(name, pts))
    n = max((len(s.points) for s in series), default=0)
    ticks = list(range(1, n + 1)) if n <= 12 else None
    return line_chart(f"{sym}: cumulative P&L on real IEX days",
                      f"dollars, conservative fills, {HEADLINE_PT:g} ticks risk aversion",
                      "traded day", series, reference_y=0.0, x_ticks=ticks)


def render_overview(summaries: Sequence[dict]) -> str:
    L = ["# Live track record: Avellaneda-Stoikov on real IEX data", "",
         "Updated after every US trading day by the `live` GitHub Actions workflow. "
         "Each stock has its own page with every setting and every day.", ""]
    L += [f"- {c}" for c in CAVEATS] + [""]
    rows = []
    for s in summaries:
        con = next((r for r in s["runs"] if r["rule"] == CONSERVATIVE and r["strategy"] == INV
                    and r["penalty_ticks"] == HEADLINE_PT), None)
        opt = next((r for r in s["runs"] if r["rule"] == OPTIMISTIC and r["strategy"] == INV
                    and r["penalty_ticks"] == HEADLINE_PT), None)
        diff = next((c for c in s["compare"] if c["rule"] == CONSERVATIVE and c["penalty_ticks"] == HEADLINE_PT), None)
        if not con or not con["days"]:
            rows.append([f"[{s['symbol']}]({s['symbol']}/summary.md)", s["days_traded"], "n/a", "n/a", "", "", ""])
            continue
        rows.append([f"[{s['symbol']}]({s['symbol']}/summary.md)", s["days_traded"],
                     f"{_e(con['pnl'])} ({_verdict(con['pnl'])})", f"{_e(opt['pnl'])} ({_verdict(opt['pnl'])})",
                     f"{con['positive_days']}/{con['days']}", _e(con["markout"], ".3f"),
                     f"{_e(diff['diff'])} ({_verdict(diff['diff'])})" if diff else "n/a"])
    L += [f"Inventory strategy at {HEADLINE_PT:g} ticks of risk aversion. Mean over days with a 95% bootstrap "
          "interval over days.", ""]
    L += _table(["stock", "days traded", "daily P&L, conservative ($)", "daily P&L, optimistic ($)",
                 "positive days (cons.)", "5 s markout (ticks, cons.)", "inventory minus symmetric (cons., $/day)"],
                rows)
    return "\n".join(L)


def write_reports(out_dir: str | Path, symbols: Sequence[str], cfg: LiveConfig = LiveConfig()) -> Path:
    out = Path(out_dir)
    summaries = []
    for sym in symbols:
        days = load_days(out, sym)
        if not days:
            continue
        md, svg = render_symbol(days, cfg)
        folder = out / sym.upper()
        (folder / "summary.md").write_text(md, encoding="utf-8")
        if svg:
            (folder / "cumulative_pnl.svg").write_text(svg, encoding="utf-8")
        summaries.append(symbol_summary(days, cfg))
    path = out / "summary.md"
    out.mkdir(parents=True, exist_ok=True)
    path.write_text(render_overview(summaries), encoding="utf-8")
    return path
