import json
import math
import random
from datetime import datetime, timezone

import pytest

from lobreplay import alpaca, live, live_report
from lobreplay.alpaca import AlpacaClient, parse_time_ns, session_bounds_ns
from lobreplay.as_model import INVENTORY, SYMMETRIC, ASParams
from lobreplay.cli import main
from lobreplay.live import CONSERVATIVE, OPTIMISTIC, LiveConfig, build_day

S = 10**9
CENT = 100   # one tick in price units


def test_session_bounds_follow_new_york_daylight_saving():
    o, c = session_bounds_ns("2026-10-14")             # EDT, UTC-4
    assert datetime.fromtimestamp(o / S, timezone.utc).strftime("%H:%M") == "13:30"
    assert (c - o) == 6.5 * 3600 * S
    o, _ = session_bounds_ns("2026-12-01")             # EST, UTC-5
    assert datetime.fromtimestamp(o / S, timezone.utc).strftime("%H:%M") == "14:30"
    o, _ = session_bounds_ns("2026-03-09")             # the day after DST starts
    assert datetime.fromtimestamp(o / S, timezone.utc).strftime("%H:%M") == "13:30"


def test_parse_time_keeps_nanoseconds():
    base = int(datetime(2026, 10, 14, 13, 30, tzinfo=timezone.utc).timestamp()) * S
    assert parse_time_ns("2026-10-14T13:30:00Z") == base
    assert parse_time_ns("2026-10-14T13:30:00.5Z") == base + S // 2
    assert parse_time_ns("2026-10-14T13:30:00.123456789Z") == base + 123456789
    assert alpaca.format_time(base + 7) == "2026-10-14T13:30:00.000000007Z"


def test_client_follows_pages_and_converts_prices():
    client = AlpacaClient("k", "s", sleep=lambda s: None)
    pages = {
        None: {"trades": [{"t": "2026-10-14T13:30:01Z", "p": 100.01, "s": 50}], "next_page_token": "x"},
        "x": {"trades": [{"t": "2026-10-14T13:30:02Z", "p": 100.005, "s": 10}], "next_page_token": None},
    }
    seen = []

    def fake_get(path):
        token = "x" if "page_token=x" in path else None
        seen.append(path)
        assert "feed=iex" in path
        return pages[token]

    client._get = fake_get
    o, c = session_bounds_ns("2026-10-14")
    got = list(client.trades("aapl", o, c))
    assert [p for _, p, _ in got] == [1_000_100, 1_000_050]
    assert len(seen) == 2 and seen[0].startswith("/v2/stocks/AAPL/trades?")


def test_client_retries_on_rate_limit_then_gives_up(monkeypatch):
    calls = []

    class Resp:
        status = 429

        def read(self):
            return b"slow down"

    class Conn:
        def __init__(self, *a, **k):
            pass

        def request(self, *a, **k):
            calls.append(1)

        def getresponse(self):
            return Resp()

        def close(self):
            pass

    monkeypatch.setattr(alpaca.http.client, "HTTPSConnection", Conn)
    client = AlpacaClient("k", "s", retries=3, sleep=lambda s: None)
    with pytest.raises(OSError, match="after 3 attempts"):
        client._get("/v2/stocks/AAPL/quotes")
    assert len(calls) == 3


def test_from_env_needs_keys(monkeypatch):
    monkeypatch.delenv("ALPACA_API_KEY", raising=False)
    monkeypatch.delenv("ALPACA_API_SECRET", raising=False)
    with pytest.raises(ValueError, match="ALPACA_API_KEY"):
        alpaca.from_env()


def tiny_day(quotes, trades, seconds=20):
    return build_day("TEST", "2026-10-14", quotes, trades, (0, seconds * S))


def test_grid_takes_the_quote_standing_at_each_second():
    day = tiny_day([(0, 1000_000, 1, 1000_200, 1), (2 * S + 1, 1000_100, 1, 1000_300, 1),
                    (5 * S, 0, 0, 1000_300, 1)], [(3 * S, 1000_100, 10), (4 * S + 1, 1000_200, 5)])
    assert day.bids[:3] == [1000_000, 1000_000, 1000_000]
    assert day.bids[3] == 1000_100
    assert day.mid(4) == 1000_200
    assert day.mid(5) is None            # one-sided quote: no mid
    assert day.trades[2] == [(3 * S, 1000_100, 10)]   # (2 s, 3 s]
    assert day.trades[4] == [(4 * S + 1, 1000_200, 5)]
    assert day.n_quotes == 3 and day.n_trades == 2


def flat_day(trade_price, seconds=40):
    """A quote of 100.00 / 100.04 all day; one trade at trade_price in second 10."""
    return tiny_day([(0, 1_000_000, 100, 1_000_400, 100)], [(10 * S + 5, trade_price, 500)], seconds)


def params():
    return ASParams(sigma=0.001, A=1.0, k=50.0, gamma=0.01)


@pytest.mark.parametrize("price,cons,opt", [(1_000_000, 0, 1), (999_900, 1, 1), (1_000_100, 0, 0)])
def test_fill_rules_on_the_bid(price, cons, opt):
    cfg = LiveConfig(exclude_s=0, window_s=30, markout_s=1)
    day = flat_day(price)
    # symmetric quotes around 100.02: total spread ~ (2/0.01) ln(1.0002) ~ $0.04, so bid 100.00, ask 100.04
    for rule, want in ((CONSERVATIVE, cons), (OPTIMISTIC, opt)):
        r = live._run(day, SYMMETRIC, params(), rule, cfg)
        assert r["fills"] == want, rule
        if want:
            w = r["windows"][0]
            assert w["shares_bought"] == 100 and w["end_inventory"] == 100   # one lot, not the trade's 500
            assert w["spread_capture"] == pytest.approx(100 * 0.02)


def test_quotes_never_cross_the_iex_book():
    cfg = LiveConfig(exclude_s=0, window_s=30)
    day = tiny_day([(0, 1_000_000, 100, 1_000_100, 100)], [(10 * S + 5, 1_000_100, 100)], 40)
    # a huge inventory-free k makes the A-S spread tiny, so raw quotes would sit inside a one-tick book
    tight = ASParams(sigma=0.0001, A=1.0, k=1e6, gamma=0.0001)
    r = live._run(day, SYMMETRIC, tight, OPTIMISTIC, cfg)
    # the ask may not go below bid + 1 tick = 100.01 and the bid may not reach 100.01
    assert r["windows"][0]["shares_bought"] == 0
    assert r["windows"][0]["shares_sold"] == 100


def test_intensity_fit_recovers_a_and_k():
    A, k = 0.05, 60.0
    rows = {}
    for j in range(6):
        delta = 0.005 + 0.01 * j
        n = 200_000
        hits = round(n * (1 - math.exp(-A * math.exp(-k * delta))))
        rows[str(j)] = [n, hits, delta * n]
    fit = live.fit_intensity(rows)
    assert fit["A"] == pytest.approx(A, rel=0.05)
    assert fit["k"] == pytest.approx(k, rel=0.05)
    assert live.fit_intensity({"0": [10, 0, 0.1], "1": [10, 10, 0.2]}) is None


def test_last_finished_day_waits_for_the_close():
    before = datetime(2026, 10, 14, 20, 10, tzinfo=timezone.utc)   # 16:10 New York
    after = datetime(2026, 10, 14, 20, 25, tzinfo=timezone.utc)
    sunday = datetime(2026, 10, 18, 12, 0, tzinfo=timezone.utc)
    assert live.last_finished_day(before) == "2026-10-13"
    assert live.last_finished_day(after) == "2026-10-14"
    assert live.last_finished_day(sunday) == "2026-10-16"
    assert live.weekdays("2026-10-09", "2026-10-13") == ["2026-10-09", "2026-10-12", "2026-10-13"]


class FakeClient:
    """Synthetic IEX days: a random-walk mid, a 2-4 cent spread, trades at and through the quotes."""

    def __init__(self, holidays=()):
        self.holidays, self.fetched = set(holidays), []

    def _path(self, symbol, start_ns):
        """(day, first second, one mid per second from 60 s before the open to the close), shared by both feeds."""
        day = datetime.fromtimestamp(start_ns / S + 120, timezone.utc).date().isoformat()
        o, c = session_bounds_ns(day)
        rng, mid, mids = random.Random(f"{symbol}/{day}"), 5_000_000, []
        for _ in range((c - o) // S + 61):
            mid += rng.choice((-CENT,) + (0,) * 8 + (CENT,))
            mids.append(mid)
        return day, o - 60 * S, mids

    def quotes(self, symbol, start_ns, end_ns):
        day, t0, mids = self._path(symbol, start_ns)
        self.fetched.append((symbol, day))
        if day in self.holidays:
            return
        rng = random.Random(f"{symbol}/{day}/quotes")
        for t in range(start_ns, end_ns, S):
            half = rng.choice((1, 2)) * CENT
            mid = mids[(t - t0) // S]
            yield t + 1000, mid - half, 100, mid + half, 100

    def trades(self, symbol, start_ns, end_ns):
        day, t0, mids = self._path(symbol, start_ns)
        if day in self.holidays:
            return
        rng = random.Random(f"{symbol}/{day}/trades")
        for t in range(start_ns, end_ns, S):
            if rng.random() < 0.3:
                mid = mids[(t - t0) // S]
                yield t + S // 2, mid + rng.choice((-3, -2, -1, 1, 2, 3)) * CENT, rng.choice((10, 100, 300))


FAST = LiveConfig(penalty_ticks=(2.0,), n_boot=200)


def test_process_calibrates_on_earlier_days_only_and_is_restartable(tmp_path):
    client = FakeClient(holidays={"2026-10-13"})
    days = ["2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15"]
    written = live.process(client, ["test"], days, tmp_path, FAST)
    assert written == [f"TEST {d}" for d in days]

    got = {d["date"]: d for d in live.load_days(tmp_path, "TEST")}
    assert got["2026-10-12"]["runs"] == [] and got["2026-10-12"]["calibration"] is None   # first day: calibrate only
    assert got["2026-10-13"]["no_data"] is True
    assert got["2026-10-14"]["calibration"]["days"] == ["2026-10-12"]                     # never the day itself
    assert got["2026-10-15"]["calibration"]["days"] == ["2026-10-12", "2026-10-14"]
    runs = got["2026-10-15"]["runs"]
    assert {(r["strategy"], r["rule"]) for r in runs} == {(s, r) for s in (INVENTORY, SYMMETRIC)
                                                          for r in (CONSERVATIVE, OPTIMISTIC)}
    for r in runs:
        assert len(r["windows"]) == 12           # 09:35 to 15:35 in 30-minute windows
        assert r["day_pnl"] == pytest.approx(sum(w["pnl"] for w in r["windows"]))
        for w in r["windows"]:
            assert w["pnl"] == pytest.approx(w["spread_capture"] + w["inventory_pnl"])
    cons = {r["strategy"]: r["fills"] for r in runs if r["rule"] == CONSERVATIVE}
    opt = {r["strategy"]: r["fills"] for r in runs if r["rule"] == OPTIMISTIC}
    assert all(opt[s] >= cons[s] > 0 for s in cons)

    client.fetched.clear()
    assert live.process(client, ["TEST"], days + ["2026-10-16"], tmp_path, FAST) == ["TEST 2026-10-16"]
    assert client.fetched == [("TEST", "2026-10-16")]


def test_reports_are_written(tmp_path):
    live.process(FakeClient(), ["TEST"], ["2026-10-12", "2026-10-13", "2026-10-14"], tmp_path, FAST)
    path = live_report.write_reports(tmp_path, ["TEST"], FAST)
    overview = path.read_text(encoding="utf-8")
    assert "[TEST](TEST/summary.md)" in overview
    md = (tmp_path / "TEST" / "summary.md").read_text(encoding="utf-8")
    assert "Traded days: 2 (2026-10-13 to 2026-10-14)" in md
    assert "| 2026-10-12 | calibration only |" in md
    assert (tmp_path / "TEST" / "cumulative_pnl.svg").read_text(encoding="utf-8").startswith("<svg")


def test_cli_report_only_needs_no_keys(tmp_path, monkeypatch):
    monkeypatch.delenv("ALPACA_API_KEY", raising=False)
    live.process(FakeClient(), ["TEST"], ["2026-10-12", "2026-10-13"], tmp_path, FAST)
    assert main(["live", "--report-only", "--ticker", "TEST", "--out", str(tmp_path)]) == 0
    assert json.loads((tmp_path / "TEST" / "days" / "2026-10-13.json").read_text())["runs"]
    assert main(["live", "--ticker", "TEST", "--out", str(tmp_path), "--since", "2026-10-14",
                 "--until", "2026-10-14"]) == 1    # fetching needs the keys
