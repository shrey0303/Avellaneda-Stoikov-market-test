"""Streaming parsers for LOBSTER message and orderbook files.

Both files are read lazily: a full day of a liquid stock is hundreds of
thousands of rows and the orderbook file has 4*levels integers per row, so
holding it all as Python ints would cost hundreds of MB.

All values stay integers: time in nanoseconds after midnight, prices in
dollars * 10_000, sizes in shares.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator, NamedTuple

from .lobster_format import (
    BOOK_EVENTS,
    DUMMY_ASK_PRICE,
    DUMMY_BID_PRICE,
    DUMMY_SIZE,
    HALT_PRICE_CODES,
    MESSAGE_COLS,
    NS_PER_S,
    ORDERBOOK_COLS_PER_LEVEL,
    Direction,
    EventType,
)


class ParseError(ValueError):
    """A row that does not match the expected LOBSTER format."""


class Message(NamedTuple):
    time_ns: int
    event_type: EventType
    order_id: int
    size: int
    price: int
    direction: Direction


class Snapshot(NamedTuple):
    """Top-N book: (price, size) pairs, best first, dummy levels dropped."""

    asks: tuple[tuple[int, int], ...]
    bids: tuple[tuple[int, int], ...]


# ---------------------------------------------------------------------------
# Field parsing
# ---------------------------------------------------------------------------

def parse_time_ns(text: str) -> int:
    """'34200.004241176' -> 34200004241176. Parsed from text, never via float.

    The real sample files print some times with more than nine decimals
    ('36754.716797047004'); the extra digits are rounded to the nearest nanosecond.
    """
    text = text.strip()
    whole, _, frac = text.partition(".")
    if not whole.isdigit() or (frac and not frac.isdigit()):
        raise ParseError(f"bad timestamp {text!r}")
    ns = int(whole) * NS_PER_S + int(frac[:9].ljust(9, "0") or 0)
    return ns + 1 if len(frac) > 9 and frac[9] >= "5" else ns


def format_time_ns(time_ns: int) -> str:
    """Inverse of parse_time_ns, always 9 decimals."""
    return f"{time_ns // NS_PER_S}.{time_ns % NS_PER_S:09d}"


def parse_message_row(row: list[str], line_no: int) -> Message:
    if len(row) != MESSAGE_COLS:
        raise ParseError(f"line {line_no}: expected {MESSAGE_COLS} columns, got {len(row)}")
    try:
        time_ns = parse_time_ns(row[0])
        event_type = EventType(int(row[1]))
        order_id, size, price = int(row[2]), int(row[3]), int(row[4])
        direction = Direction(int(row[5]))
    except ValueError as exc:  # includes ParseError and bad enum values
        raise ParseError(f"line {line_no}: {exc}") from exc
    return Message(time_ns, event_type, order_id, size, price, direction)


def parse_orderbook_row(row: list[str], levels: int, line_no: int) -> Snapshot:
    expected = levels * ORDERBOOK_COLS_PER_LEVEL
    if len(row) != expected:
        raise ParseError(f"line {line_no}: expected {expected} columns for {levels} levels, got {len(row)}")
    try:
        vals = [int(v) for v in row]
    except ValueError as exc:
        raise ParseError(f"line {line_no}: {exc}") from exc

    asks: list[tuple[int, int]] = []
    bids: list[tuple[int, int]] = []
    for i in range(0, expected, ORDERBOOK_COLS_PER_LEVEL):
        ask_p, ask_s, bid_p, bid_s = vals[i : i + 4]
        _append_level(asks, ask_p, ask_s, DUMMY_ASK_PRICE, line_no, "ask")
        _append_level(bids, bid_p, bid_s, DUMMY_BID_PRICE, line_no, "bid")
    return Snapshot(_strip_dummies(asks), _strip_dummies(bids))


def _append_level(out: list, price: int, size: int, dummy: int, line_no: int, side: str) -> None:
    if price == dummy:
        if size != DUMMY_SIZE:
            raise ParseError(f"line {line_no}: dummy {side} price with size {size}")
        out.append(None)  # placeholder; real levels may not follow a dummy
        return
    if out and out[-1] is None:
        raise ParseError(f"line {line_no}: real {side} level after an empty one")
    if price <= 0 or size <= 0:
        raise ParseError(f"line {line_no}: non-positive {side} level ({price}, {size})")
    out.append((price, size))


def _strip_dummies(levels: list) -> tuple:
    return tuple(lv for lv in levels if lv is not None)


# ---------------------------------------------------------------------------
# File iteration
# ---------------------------------------------------------------------------

def iter_messages(path: str | Path) -> Iterator[Message]:
    with open(path, newline="") as fh:
        for line_no, row in enumerate(csv.reader(fh), start=1):
            if row:
                yield parse_message_row(row, line_no)


def iter_orderbook(path: str | Path, levels: int) -> Iterator[Snapshot]:
    with open(path, newline="") as fh:
        for line_no, row in enumerate(csv.reader(fh), start=1):
            if row:
                yield parse_orderbook_row(row, levels, line_no)


# ---------------------------------------------------------------------------
# Locating files
# ---------------------------------------------------------------------------

# e.g. AAPL_2012-06-21_34200000_57600000_message_10.csv
_FILE_RE = re.compile(
    r"^(?P<ticker>[A-Z.]+)_(?P<date>\d{4}-\d{2}-\d{2})_(?P<start>\d+)_(?P<end>\d+)_"
    r"(?P<kind>message|orderbook)_(?P<levels>\d+)\.csv$"
)


@dataclass(frozen=True)
class LobsterFiles:
    ticker: str
    date: str
    levels: int
    message_path: Path
    orderbook_path: Path


def find_files(directory: str | Path, ticker: str, levels: int) -> LobsterFiles:
    """Find the message/orderbook pair for one ticker and depth in a directory."""
    directory = Path(directory)
    found: dict[str, tuple[Path, str]] = {}
    for p in directory.iterdir():
        m = _FILE_RE.match(p.name)
        if m and m["ticker"] == ticker and int(m["levels"]) == levels:
            if m["kind"] in found:
                raise FileNotFoundError(f"multiple {m['kind']} files for {ticker} level {levels} in {directory}")
            found[m["kind"]] = (p, m["date"])
    missing = {"message", "orderbook"} - found.keys()
    if missing:
        raise FileNotFoundError(f"no {', '.join(sorted(missing))} file for {ticker} level {levels} in {directory}")
    return LobsterFiles(ticker, found["message"][1], levels, found["message"][0], found["orderbook"][0])


# ---------------------------------------------------------------------------
# Sanity checks (Phase 1 done-criterion)
# ---------------------------------------------------------------------------

@dataclass
class SanityReport:
    message_rows: int = 0
    orderbook_rows: int = 0
    event_counts: Counter = field(default_factory=Counter)
    first_time_ns: int | None = None
    last_time_ns: int | None = None
    problems: list[str] = field(default_factory=list)

    MAX_PROBLEMS = 50

    def add_problem(self, text: str) -> None:
        if len(self.problems) < self.MAX_PROBLEMS:
            self.problems.append(text)

    @property
    def ok(self) -> bool:
        return not self.problems

    def summary(self) -> str:
        lines = [
            f"message rows:   {self.message_rows}",
            f"orderbook rows: {self.orderbook_rows}",
        ]
        if self.first_time_ns is not None:
            lines.append(f"time range:     {format_time_ns(self.first_time_ns)} .. {format_time_ns(self.last_time_ns)}")
        lines.append("event counts:")
        for et in EventType:
            lines.append(f"  {et.value} {et.name:<13} {self.event_counts.get(et, 0)}")
        unseen = [et.name for et in EventType if self.event_counts.get(et, 0) == 0]
        if unseen:
            lines.append(f"never seen:     {', '.join(unseen)}  (fine for halts/crosses; check the rest)")
        lines.append("OK" if self.ok else f"PROBLEMS ({len(self.problems)} shown):")
        lines.extend(f"  - {p}" for p in self.problems)
        return "\n".join(lines)


def check_files(files: LobsterFiles) -> SanityReport:
    """Parse both files fully and check row-level invariants.

    Book consistency (does the orderbook row follow from the messages?) is
    Phase 2's job — see replay.py. This only checks each file on its own terms
    plus that they line up row-for-row.
    """
    rep = SanityReport()
    prev_time = None
    try:
        for i, msg in enumerate(iter_messages(files.message_path), start=1):
            rep.message_rows = i
            rep.event_counts[msg.event_type] += 1
            if rep.first_time_ns is None:
                rep.first_time_ns = msg.time_ns
            if prev_time is not None and msg.time_ns < prev_time:
                rep.add_problem(f"message {i}: time goes backwards")
            prev_time = rep.last_time_ns = msg.time_ns
            _check_message_values(msg, i, rep)
    except ParseError as exc:
        rep.add_problem(f"message file: {exc}")

    try:
        for j, _ in enumerate(iter_orderbook(files.orderbook_path, files.levels), start=1):
            rep.orderbook_rows = j
    except ParseError as exc:
        rep.add_problem(f"orderbook file: {exc}")

    if rep.message_rows != rep.orderbook_rows:
        rep.add_problem(f"row count mismatch: {rep.message_rows} messages vs {rep.orderbook_rows} orderbook rows")
    return rep


def _check_message_values(msg: Message, i: int, rep: SanityReport) -> None:
    et = msg.event_type
    if et == EventType.HALT:
        if msg.price not in HALT_PRICE_CODES:
            rep.add_problem(f"message {i}: halt with unknown status code {msg.price}")
        return
    if msg.size <= 0:
        rep.add_problem(f"message {i}: non-positive size {msg.size}")
    if msg.price <= 0:
        rep.add_problem(f"message {i}: non-positive price {msg.price}")
    if et in BOOK_EVENTS and msg.order_id <= 0:
        rep.add_problem(f"message {i}: book event with order id {msg.order_id}")
