import json
import random
from datetime import datetime, timedelta, timezone

import pytest

from lobreplay import recorder, track
from lobreplay.cli import main
from lobreplay.signals import OFI, QUEUE_IMBALANCE, TRADE_IMBALANCE, fit
from lobreplay.track import BEFORE_FREEZE, FIT_DAY, SCORED, TOO_LITTLE, UNFINISHED, TrackConfig

S = 10**9
SYMBOL = "TESTUSDT"


def utc(day: str, hour: int = 0) -> datetime:
    return datetime.strptime(day, "%Y-%m-%d").replace(tzinfo=timezone.utc) + timedelta(hours=hour)


def write_rows(root, day, rows):
    """rows: (seconds after midnight, bid, bid_qty, ask, ask_qty, buy, sell)."""
    path = root / SYMBOL / f"{day}.csv"
    path.parent.mkdir(parents=True, exist_ok=True)
    t0 = int(utc(day).timestamp()) * S
    with open(path, "w", newline="") as fh:
        fh.write(",".join(recorder.COLUMNS) + "\n")
        for sec, *rest in rows:
            fh.write(",".join([str(t0 + int(sec * S))] + [str(x) for x in rest]) + "\n")
    return path


def write_day(root, day, seconds, strength, seed):
    """A day where the mid tends to move, a second later, towards the bigger queue."""
    rng = random.Random(f"{day}/{seed}")
    rows, mid_ticks, x_prev = [], 5_000_000, 0.0
    for i in range(seconds):
        mid_ticks += round(2 * strength * x_prev + rng.gauss(0, 0.5))
        x = rng.uniform(-1, 1)
        bid = mid_ticks / 100
        rows.append((i + 0.2, f"{bid:.2f}", f"{5 * (1 + x):.5f}", f"{bid + 0.01:.2f}", f"{5 * (1 - x):.5f}",
                     f"{rng.random():.5f}", f"{rng.random():.5f}"))
        x_prev = x
    return write_rows(root, day, rows)


def load(paths, lookback_s=5.0):
    return track.load_days(paths, 1, lookback_s, 2.0)


# -- recorded rows -> samples ---------------------------------------------------------

def test_samples_describe_the_last_row_at_or_before_each_second(tmp_path):
    p = write_rows(tmp_path, "2026-09-01", [
        (0.2, "100.00", 3, "100.01", 1, 0, 0),
        (1.2, "100.00", 3, "100.01", 1, 2.0, 0.5),     # same book, trades only
        (2.2, "100.00", 5, "100.01", 1, 0, 0),         # 2 added at the bid
        (3.0, "100.01", 4, "100.02", 6, 0, 1.0),       # stamped exactly on the second
    ])
    s = load([p])
    t0 = int(utc("2026-09-01").timestamp()) * S
    assert s.times == [t0 + 1 * S, t0 + 2 * S, t0 + 3 * S]
    assert s.mids == [1_000_050.0, 1_000_050.0, 1_000_150.0]
    assert s.features[QUEUE_IMBALANCE] == pytest.approx([0.5, 0.5, -0.2])
    assert s.features[TRADE_IMBALANCE] == pytest.approx([0.0, 1.5, 0.5])
    # second 3: +2 at the bid, then the bid steps up (+4) and the ask steps away (+1 removed from the ask)
    assert s.features[OFI] == pytest.approx([0.0, 0.0, 2.0 + 4.0 + 1.0])


def test_a_gap_has_no_mid_and_restarts_the_flow_signals(tmp_path):
    p = write_rows(tmp_path, "2026-09-01", [
        (0.2, "100.00", 3, "100.01", 1, 0, 0),
        (1.2, "100.00", 3, "100.01", 1, 4.0, 0),
        (9.2, "100.05", 3, "100.06", 1, 50.0, 0),      # eight seconds of trades arrive at once
        (10.2, "100.05", 3, "100.06", 1, 1.0, 0),
        (11.2, "100.05", 3, "100.06", 1, 0, 0),
    ])
    s = load([p], lookback_s=30.0)
    # seconds 1-3 are covered (a row may be up to 2 s old), 4-9 are not, 10-11 are again
    assert s.mids == [1_000_050.0, 1_000_050.0, 1_000_050.0] + [None] * 6 + [1_000_550.0, 1_000_550.0]
    assert s.features[TRADE_IMBALANCE] == pytest.approx([0, 4, 4] + [0] * 6 + [0, 1])
    assert s.features[OFI] == pytest.approx([0.0] * 11)


def test_no_price_change_is_measured_across_days_or_gaps(tmp_path):
    a = write_day(tmp_path, "2026-09-01", 400, 1.0, 0)
    b = write_day(tmp_path, "2026-09-02", 400, 1.0, 0)
    s = load([a, b])
    for h in (1, 5, 60):
        f = fit(s, QUEUE_IMBALANCE, h, s.times[0], s.times[-1] + 1)
        # day 1 covers 401 seconds (its last row serves 2 s more), day 2 covers 399; the last h of each have no target
        assert f.n == (401 - h) + (399 - h)


# -- freeze ---------------------------------------------------------------------------

FIT_DAYS = ["2026-09-01", "2026-09-02", "2026-09-03"]
CFG = TrackConfig(min_day_samples=1000, min_days=20)


def history(root, strength_after, n_test=22, seconds=1500):
    for d in FIT_DAYS:
        write_day(root, d, seconds, 1.0, 0)
    write_day(root, "2026-09-04", seconds, 1.0, 0)                 # the day the freeze is made
    test_days = [(utc("2026-09-05") + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(n_test)]
    for d in test_days:
        write_day(root, d, seconds, strength_after, 0)
    return test_days


def frozen_at(root, when=("2026-09-04", 12)):
    path = root / "frozen" / f"{SYMBOL}.json"
    return path, track.freeze(root, SYMBOL, path, cfg=CFG, now=utc(*when))


def test_freeze_fits_finished_days_only_and_picks_the_strongest_signal(tmp_path):
    history(tmp_path, 1.0, n_test=0)
    path, body = frozen_at(tmp_path)
    assert body["fit_days"] == FIT_DAYS                              # not the unfinished 4th
    assert body["signal"]["signal"] == QUEUE_IMBALANCE and body["signal"]["horizon_s"] == 5
    assert body["signal"]["slope"] > 0 and body["created_utc"] == "2026-09-04T12:00:00Z"
    assert len(body["candidates"]) == 3 * 5
    assert track.load_frozen(path)[0] == body


def test_a_frozen_file_is_never_overwritten_and_edits_are_detected(tmp_path):
    history(tmp_path, 1.0, n_test=0)
    path, _ = frozen_at(tmp_path)
    with pytest.raises(FileExistsError):
        track.freeze(tmp_path, SYMBOL, path, cfg=CFG, now=utc("2026-09-04", 13))
    doc = json.loads(path.read_text(encoding="utf-8"))
    doc["frozen"]["signal"]["slope"] *= 1.01
    path.write_text(json.dumps(doc), encoding="utf-8")
    with pytest.raises(ValueError, match="changed after it was frozen"):
        track.run_track(tmp_path, path, now=utc("2026-09-30"))


def test_freeze_needs_data(tmp_path):
    with pytest.raises(ValueError):
        track.freeze(tmp_path, SYMBOL, tmp_path / "f.json", cfg=CFG, now=utc("2026-09-04"))


# -- scoring --------------------------------------------------------------------------

def test_only_days_after_the_freeze_are_scored_and_every_day_is_listed(tmp_path):
    test_days = history(tmp_path, 1.0)
    write_day(tmp_path, test_days[3], 300, 1.0, 0)                   # overwrite one day with five minutes of data
    path, _ = frozen_at(tmp_path)
    today = (utc(test_days[-1])).replace(hour=9)                     # the last test day is still being recorded
    res = track.run_track(tmp_path, path, now=today)
    status = {d["day"]: d["status"] for d in res["days"]}
    assert [status[d] for d in FIT_DAYS] == [FIT_DAY] * 3
    assert status["2026-09-04"] == BEFORE_FREEZE
    assert status[test_days[3]] == TOO_LITTLE and status[test_days[-1]] == UNFINISHED
    scored = [d for d in res["days"] if d["status"] == SCORED]
    assert [d["day"] for d in scored] == [d for d in test_days[:-1] if d != test_days[3]]
    sm = res["summary"]
    assert sm["days_scored"] == 20 and sm["days_right_sign"] == 20
    assert sm["mean_daily_corr"]["lo"] > 0 and sm["sign_test_p"] == pytest.approx(0.5 ** 20)
    assert sm["verdict"] == "held up"


def test_a_signal_that_stops_working_is_reported_as_such(tmp_path):
    history(tmp_path, 0.0)                                           # after the freeze the mid ignores the book
    path, _ = frozen_at(tmp_path)
    res = track.run_track(tmp_path, path, now=utc("2026-10-15"))
    sm = res["summary"]
    assert sm["days_scored"] == 22 and sm["verdict"] == "did not hold up"
    assert abs(sm["mean_daily_corr"]["mean"]) < 0.05


def test_no_verdict_before_enough_days(tmp_path):
    history(tmp_path, 1.0, n_test=5)
    path, _ = frozen_at(tmp_path)
    res = track.run_track(tmp_path, path, now=utc("2026-10-15"))
    assert res["summary"]["verdict"] == "too few days for a verdict: 5 scored, 20 needed"
    out = track.write_track(res, tmp_path / "out")
    report = (out / "track.md").read_text(encoding="utf-8")
    assert "5 of 5 days" in report and "left out: fit day" in report and (out / "track.svg").exists()
    assert json.loads((out / "track.json").read_text(encoding="utf-8"))["sha256"] == res["sha256"]


def test_sign_test():
    assert track.sign_test_p(5, 5) == pytest.approx(1 / 32)
    assert track.sign_test_p(0, 7) == 1.0
    assert track.sign_test_p(22, 25) == pytest.approx(sum([2300, 300, 25, 1]) / 2 ** 25)


def test_cli_freeze_and_track(tmp_path, capsys):
    history(tmp_path, 1.0, n_test=2)
    frozen = tmp_path / "frozen.json"
    assert main(["freeze", "--dir", str(tmp_path), "--symbol", SYMBOL, "--frozen", str(frozen)]) == 0
    assert "Commit and push" in capsys.readouterr().out
    assert main(["freeze", "--dir", str(tmp_path), "--symbol", SYMBOL, "--frozen", str(frozen)]) == 1
    assert main(["track", "--dir", str(tmp_path), "--frozen", str(frozen), "--out", str(tmp_path / "out")]) == 0
    assert "too few days" in capsys.readouterr().out      # every file predates the real freeze time


# -- recorder -------------------------------------------------------------------------

class Clock:
    def __init__(self, start: datetime):
        self.now = int(start.timestamp() * S)

    def __call__(self) -> int:
        self.now += 1_000_000          # every look at the clock costs a millisecond
        return self.now

    def sleep(self, seconds: float) -> None:
        self.now += int(seconds * S)


class FakeFeed:
    def __init__(self, fail_on=()):
        self.calls, self.polls, self.fail_on, self.resets = [], 0, set(fail_on), 0

    def trades(self):
        self.polls += 1
        self.calls.append("trades")
        if self.polls in self.fail_on:
            raise OSError("network down")
        return 0.25, 0.5

    def book(self):
        self.calls.append("book")
        return "100.00", "3.0", "100.01", "1.0"

    def reset(self):
        self.resets += 1


def test_recorder_writes_one_row_a_second_and_splits_files_at_utc_midnight(tmp_path):
    clock = Clock(utc("2026-10-07", 23) + timedelta(minutes=59, seconds=56.5))
    feed = FakeFeed(fail_on={2})
    rows, errors = recorder.record(feed, tmp_path, "btcusdt", 6.0, clock=clock, sleep=clock.sleep)
    assert (rows, errors, feed.resets) == (5, 1, 1)
    assert feed.calls[:2] == ["trades", "book"]            # trades first: nothing in a row is later than its book
    first = (tmp_path / "BTCUSDT" / "2026-10-07.csv").read_text().splitlines()
    second = (tmp_path / "BTCUSDT" / "2026-10-08.csv").read_text().splitlines()
    assert first[0] == second[0] == ",".join(recorder.COLUMNS)
    assert len(first) == 1 + 2 and len(second) == 1 + 3    # 23:59:57, (58 failed), 59 | 00:00:00, 01, 02
    assert first[1].split(",")[1:] == ["100.00", "3.0", "100.01", "1.0", "0.25000000", "0.50000000"]
    s = track.load_days(list(track.day_files(tmp_path, "BTCUSDT").values()), 1, 5.0, 2.0)
    assert len(s.times) == 5 and None not in s.mids       # the recorder's files are what track.py reads
