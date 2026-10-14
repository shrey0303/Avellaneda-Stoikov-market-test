"""Command line: python -m lobreplay {make-synthetic,check,validate,shadow,study,record,freeze,track,live} ..."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import alpaca, live, live_report, recorder, track
from .calibration import CalibrationConfig
from .parser import check_files, find_files
from .replay import replay_files
from .shadow import shadow_validate
from .strategy import StrategyConfig
from .study import StudyConfig, render_summary, run_study, write_outputs
from .synthetic import SyntheticConfig, generate

LIVE_TICKERS = ("AAPL", "AMZN", "GOOG", "INTC", "MSFT")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="lobreplay", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    syn = sub.add_parser("make-synthetic", help="write placeholder LOBSTER-format files")
    syn.add_argument("--out", default="data/synthetic")
    syn.add_argument("--ticker", default="FAKE")
    syn.add_argument("--levels", type=int, default=10)
    syn.add_argument("--messages", type=int, default=20_000)
    syn.add_argument("--seed", type=int, default=0)

    for name, help_text in (
        ("check", "Phase 1: parse both files and check row-level invariants"),
        ("validate", "Phase 2: replay messages and compare against the orderbook file"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--dir", required=True, help="directory holding the LOBSTER csv files")
        p.add_argument("--ticker", required=True, nargs="+", help="one or more tickers")
        p.add_argument("--levels", type=int, default=10)
        if name == "validate":
            p.add_argument("--max-divergences", type=int, default=1,
                           help="keep going after a top-of-book mismatch, up to this many (default: stop at first)")

    for name, help_text in (
        ("shadow", "Phase 4: shadow real orders and compare predicted fills with actual fills"),
        ("study", "Phases 5-7: calibrate on the morning, trade the afternoon, write the report"),
    ):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("--dir", required=True, help="directory holding the LOBSTER csv files")
        p.add_argument("--ticker", required=True, nargs="+", help="one or more tickers")
        p.add_argument("--levels", type=int, default=10)
        p.add_argument("--seed", type=int, default=0)
        if name == "shadow":
            p.add_argument("--max-orders", type=int, default=None,
                           help="shadow a random sample of this many orders (default: all of them)")
        else:
            p.add_argument("--out", default="results", help="output directory (one sub-directory per ticker)")
            p.add_argument("--window-minutes", type=float, default=30.0)
            p.add_argument("--sigma-horizon", type=int, default=60, help="horizon in seconds at which sigma is taken")
            p.add_argument("--model-paths", type=int, default=200)

    rec = sub.add_parser("record", help="Phase 10: record the live Binance best bid/ask and trades, one row a second")
    rec.add_argument("--out", default="data/crypto")
    rec.add_argument("--symbol", default="BTCUSDT")
    rec.add_argument("--hours", type=float, default=24.0, help="how long to record before stopping")

    frz = sub.add_parser("freeze", help="Phase 11: fit on the recorded days, choose one signal, write it once")
    frz.add_argument("--dir", default="data/crypto")
    frz.add_argument("--symbol", default="BTCUSDT")
    frz.add_argument("--frozen", default=None, help="file to write (default: frozen/<SYMBOL>.json)")
    frz.add_argument("--days", nargs="*", default=None, help="UTC dates to fit on (default: every finished day)")

    trk = sub.add_parser("track", help="Phase 11: score the frozen signal on every day after the freeze")
    trk.add_argument("--dir", default="data/crypto")
    trk.add_argument("--frozen", default="frozen/BTCUSDT.json")
    trk.add_argument("--out", default="results/track")

    lv = sub.add_parser("live", help="Phase 12: fetch finished IEX days from Alpaca, trade them, update the live reports")
    lv.add_argument("--ticker", nargs="+", default=list(LIVE_TICKERS))
    lv.add_argument("--since", default=None, help="first day to trade, YYYY-MM-DD (default: the last finished day)")
    lv.add_argument("--until", default=None, help="last day (default: the last day whose close is 20 minutes old)")
    lv.add_argument("--out", default="results/live")
    lv.add_argument("--report-only", action="store_true", help="rebuild the reports from the days on disk")

    args = ap.parse_args(argv)

    if args.cmd == "live":
        return _live(args)

    if args.cmd in ("record", "freeze", "track"):
        return _track(args)

    if args.cmd == "make-synthetic":
        cfg = SyntheticConfig(ticker=args.ticker, levels=args.levels, n_messages=args.messages, seed=args.seed)
        files = generate(cfg, args.out)
        print(f"wrote {files.message_path}\nwrote {files.orderbook_path}")
        return 0

    if args.cmd == "study":
        return _study(args)

    all_ok = True
    for ticker in args.ticker:
        files = find_files(args.dir, ticker, args.levels)
        print(f"=== {ticker} {files.date} levels={files.levels} ===")
        if args.cmd == "check":
            rep = check_files(files)
        elif args.cmd == "shadow":
            rep = shadow_validate(files, max_orders=args.max_orders, seed=args.seed)
        else:
            rep = replay_files(files, max_divergences=args.max_divergences)
        print(rep.summary(), end="\n\n")
        all_ok &= rep.ok
    return 0 if all_ok else 1


def _track(args: argparse.Namespace) -> int:
    if args.cmd == "record":
        print(f"recording {args.symbol} for {args.hours:g} h into {args.out} (Ctrl+C stops it; rows already written are kept)")
        try:
            rows, errors = recorder.record(recorder.BinanceFeed(args.symbol), args.out, args.symbol,
                                           args.hours * 3600, log=print)
        except KeyboardInterrupt:
            print("stopped")
            return 0
        print(f"wrote {rows} rows, {errors} failed polls")
        return 0 if rows else 1
    try:
        if args.cmd == "freeze":
            path = args.frozen or f"frozen/{args.symbol.upper()}.json"
            body = track.freeze(args.dir, args.symbol, path, args.days)
            sig = body["signal"]
            print(f"froze {sig['signal']} at {sig['horizon_s']} s (fit correlation {sig['corr']:.3f}, "
                  f"{sig['n']} samples, {len(body['fit_days'])} days) into {path}")
            print("Commit and push this file now, before the next day is recorded. Days are scored only if they "
                  "start after the freeze.")
            return 0
        res = track.run_track(args.dir, args.frozen)
    except (FileExistsError, FileNotFoundError, ValueError) as e:
        print(f"ERROR: {e}")
        return 1
    out = track.write_track(res, args.out)
    s = res["summary"]
    print(f"{s['days_right_sign']} of {s['days_scored']} scored days on the frozen side; verdict: {s['verdict']}")
    print(f"wrote {out / 'track.md'}")
    return 0


def _live(args: argparse.Namespace) -> int:
    if not args.report_only:
        until = args.until or live.last_finished_day()
        days = live.weekdays(args.since or until, until)
        try:
            client = alpaca.from_env()
            written = live.process(client, args.ticker, days, args.out, log=print)
        except (OSError, ValueError) as e:
            print(f"ERROR: {e}")
            return 1
        print(f"{len(written)} new stock-days, {client.requests} requests")
    path = live_report.write_reports(args.out, args.ticker)
    print(f"wrote {path}")
    return 0


def _study(args: argparse.Namespace) -> int:
    cfg = StudyConfig(
        calibration=CalibrationConfig(sigma_horizon_s=args.sigma_horizon, seed=args.seed),
        strategy=StrategyConfig(window_s=args.window_minutes * 60),
        model_paths=args.model_paths,
        seed=args.seed,
    )
    results = []
    for ticker in args.ticker:
        files = find_files(args.dir, ticker, args.levels)
        print(f"=== {ticker} {files.date} levels={files.levels} ===")
        res = run_study(files, cfg, log=print)
        out = write_outputs(res, args.out)
        for problem in res["problems"]:
            print(f"PROBLEM: {problem}")
        print(f"wrote {out / 'report.md'}\n")
        results.append(res)
    if len(results) > 1:
        summary = Path(args.out) / "summary.md"
        summary.write_text(render_summary(results), encoding="utf-8")
        print(f"wrote {summary}")
    return 0 if all(r["questions"] for r in results) else 1


if __name__ == "__main__":
    sys.exit(main())
