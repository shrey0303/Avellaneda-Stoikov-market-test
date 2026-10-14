"""Phase 12: fetch one finished trading day of IEX quotes and trades from Alpaca.

Alpaca's free market-data plan serves the IEX exchange's own best bid and ask
and every IEX trade, tick by tick, for any past day. Only the most recent 15
minutes are withheld, so a day can be fetched once the close is 15 minutes
old. The account is free and needs no deposit; a paper-trading key is enough.

    ALPACA_API_KEY, ALPACA_API_SECRET    read from the environment

Nothing is written to disk here. live.py turns the two streams into one day.
"""

from __future__ import annotations

import http.client
import json
import os
import time
from datetime import date, datetime, timedelta, timezone
from typing import Callable, Iterator
from urllib.parse import urlencode

from .lobster_format import NS_PER_S, PRICE_SCALE

HOST = "data.alpaca.markets"
PAGE_LIMIT = 10_000
_RETRY_STATUS = {429, 500, 502, 503, 504}


def _first_sunday(year: int, month: int) -> date:
    d = date(year, month, 1)
    return d + timedelta(days=(6 - d.weekday()) % 7)


def new_york_utc_offset_h(day: date) -> int:
    """-4 in US daylight saving time (second Sunday of March to first Sunday of November), else -5."""
    dst_start = _first_sunday(day.year, 3) + timedelta(days=7)
    dst_end = _first_sunday(day.year, 11)
    return -4 if dst_start <= day < dst_end else -5


def session_bounds_ns(day: str) -> tuple[int, int]:
    """(09:30, 16:00) New York time on `day` (YYYY-MM-DD), as UTC nanoseconds."""
    d = date.fromisoformat(day)
    midnight = datetime(d.year, d.month, d.day, tzinfo=timezone.utc) - timedelta(hours=new_york_utc_offset_h(d))
    t0 = int(midnight.timestamp()) * NS_PER_S
    return t0 + (9 * 3600 + 1800) * NS_PER_S, t0 + 16 * 3600 * NS_PER_S


def parse_time_ns(stamp: str) -> int:
    """RFC 3339 UTC time with up to nine fractional digits, e.g. 2026-10-14T13:30:00.123456789Z."""
    s = stamp.rstrip("Z")
    if s.endswith("+00:00"):
        s = s[:-6]
    whole, _, frac = s.partition(".")
    secs = int(datetime.fromisoformat(whole).replace(tzinfo=timezone.utc).timestamp())
    return secs * NS_PER_S + int((frac + "000000000")[:9])


def format_time(time_ns: int) -> str:
    secs, ns = divmod(time_ns, NS_PER_S)
    return datetime.fromtimestamp(secs, timezone.utc).strftime("%Y-%m-%dT%H:%M:%S") + f".{ns:09d}Z"


def to_units(dollars: float) -> int:
    return round(dollars * PRICE_SCALE)


class AlpacaClient:
    def __init__(self, key: str, secret: str, host: str = HOST, timeout_s: float = 30.0,
                 retries: int = 6, sleep: Callable[[float], None] = time.sleep):
        self.headers = {"APCA-API-KEY-ID": key, "APCA-API-SECRET-KEY": secret, "Accept": "application/json"}
        self.host, self.timeout_s, self.retries, self.sleep = host, timeout_s, retries, sleep
        self.requests = 0

    def _get(self, path: str) -> dict:
        for attempt in range(self.retries):
            try:
                conn = http.client.HTTPSConnection(self.host, timeout=self.timeout_s)
                try:
                    conn.request("GET", path, headers=self.headers)
                    resp = conn.getresponse()
                    body = resp.read()
                finally:
                    conn.close()
            except (OSError, http.client.HTTPException) as e:
                err = f"{type(e).__name__}: {e}"
            else:
                self.requests += 1
                if resp.status == 200:
                    return json.loads(body)
                if resp.status not in _RETRY_STATUS:
                    raise OSError(f"HTTP {resp.status} for {path.split('?')[0]}: {body[:300]!r}")
                err = f"HTTP {resp.status}"
            if attempt + 1 < self.retries:
                self.sleep(min(60.0, 2.0 ** attempt))
        raise OSError(f"giving up on {path.split('?')[0]} after {self.retries} attempts ({err})")

    def _pages(self, kind: str, symbol: str, start_ns: int, end_ns: int) -> Iterator[dict]:
        query = {"start": format_time(start_ns), "end": format_time(end_ns), "limit": PAGE_LIMIT,
                 "feed": "iex", "sort": "asc"}
        token = None
        while True:
            q = dict(query, page_token=token) if token else query
            page = self._get(f"/v2/stocks/{symbol.upper()}/{kind}?{urlencode(q)}")
            yield from page.get(kind) or ()
            token = page.get("next_page_token")
            if not token:
                return

    def quotes(self, symbol: str, start_ns: int, end_ns: int) -> Iterator[tuple[int, int, int, int, int]]:
        """(time_ns, bid, bid_size, ask, ask_size), prices in PRICE_SCALE units; a missing side is 0."""
        for q in self._pages("quotes", symbol, start_ns, end_ns):
            yield (parse_time_ns(q["t"]), to_units(q.get("bp") or 0.0), int(q.get("bs") or 0),
                   to_units(q.get("ap") or 0.0), int(q.get("as") or 0))

    def trades(self, symbol: str, start_ns: int, end_ns: int) -> Iterator[tuple[int, int, int]]:
        """(time_ns, price, size), price in PRICE_SCALE units."""
        for t in self._pages("trades", symbol, start_ns, end_ns):
            yield parse_time_ns(t["t"]), to_units(t["p"]), int(t["s"])


def from_env() -> AlpacaClient:
    key, secret = os.environ.get("ALPACA_API_KEY"), os.environ.get("ALPACA_API_SECRET")
    if not key or not secret:
        raise ValueError("set ALPACA_API_KEY and ALPACA_API_SECRET (a free Alpaca paper-trading key is enough)")
    return AlpacaClient(key, secret)
