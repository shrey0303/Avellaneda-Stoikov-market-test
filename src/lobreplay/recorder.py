"""Phase 10: record a live Level 2 feed for the track record (approach document §5.9).

Once a second the recorder asks Binance's public market-data API for the
trades since the last request and then for the best bid and ask, and appends
one row to <out>/<SYMBOL>/<UTC date>.csv:

    recv_ns, bid, bid_qty, ask, ask_qty, buy_qty, sell_qty

recv_ns is this machine's clock just after the book arrived. buy_qty and
sell_qty are the volumes of buyer- and seller-initiated trades since the
previous row. Trades are fetched BEFORE the book, so nothing in a row is
later than its bid and ask; track.py relies on that for no look-ahead.

A failed request costs that second's row and nothing else. track.py sees the
gap from the timestamps and measures nothing across it.
"""

from __future__ import annotations

import http.client
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

HOST = "data-api.binance.vision"   # public market data only; no account or key
COLUMNS = ("recv_ns", "bid", "bid_qty", "ask", "ask_qty", "buy_qty", "sell_qty")
NS_PER_S = 1_000_000_000
_FEED_ERRORS = (OSError, http.client.HTTPException, ValueError, KeyError, IndexError)


class BinanceFeed:
    def __init__(self, symbol: str, host: str = HOST, timeout_s: float = 5.0):
        self.symbol, self.host, self.timeout_s = symbol.upper(), host, timeout_s
        self._conn: http.client.HTTPSConnection | None = None
        self._last_trade_id: int | None = None

    def reset(self) -> None:
        if self._conn is not None:
            self._conn.close()
        self._conn = None

    def _get(self, path: str):
        if self._conn is None:
            self._conn = http.client.HTTPSConnection(self.host, timeout=self.timeout_s)
        self._conn.request("GET", path)
        resp = self._conn.getresponse()
        body = resp.read()
        if resp.status != 200:
            raise OSError(f"HTTP {resp.status} for {path}: {body[:200]!r}")
        return json.loads(body)

    def trades(self) -> tuple[float, float]:
        """(buyer-initiated, seller-initiated) volume since the previous call; (0, 0) on the first."""
        base = f"/api/v3/aggTrades?symbol={self.symbol}"
        if self._last_trade_id is None:
            self._last_trade_id = self._get(base + "&limit=1")[-1]["a"]
            return 0.0, 0.0
        buy = sell = 0.0
        for _ in range(10):   # a busy second can hold more than one page
            page = self._get(f"{base}&fromId={self._last_trade_id + 1}&limit=1000")
            for t in page:
                if t["m"]:    # the buyer was resting, so the seller crossed
                    sell += float(t["q"])
                else:
                    buy += float(t["q"])
            if page:
                self._last_trade_id = page[-1]["a"]
            if len(page) < 1000:
                break
        return buy, sell

    def book(self) -> tuple[str, str, str, str]:
        """(bid, bid_qty, ask, ask_qty) as the exchange printed them."""
        b = self._get(f"/api/v3/ticker/bookTicker?symbol={self.symbol}")
        return b["bidPrice"], b["bidQty"], b["askPrice"], b["askQty"]


def day_path(out_dir: str | Path, symbol: str, time_ns: int) -> Path:
    day = datetime.fromtimestamp(time_ns / NS_PER_S, timezone.utc).strftime("%Y-%m-%d")
    return Path(out_dir) / symbol.upper() / f"{day}.csv"


def record(
    feed,
    out_dir: str | Path,
    symbol: str,
    duration_s: float,
    interval_s: float = 1.0,
    clock: Callable[[], int] = time.time_ns,
    sleep: Callable[[float], None] = time.sleep,
    log: Callable[[str], None] = lambda s: None,
) -> tuple[int, int]:
    """Record for duration_s; returns (rows written, failed polls)."""
    step = int(interval_s * NS_PER_S)
    end = clock() + int(duration_s * NS_PER_S)
    rows = errors = 0
    path, fh = None, None
    try:
        while True:
            now = clock()
            due = (now // step + 1) * step
            if due >= end:
                break
            sleep((due - now) / NS_PER_S)
            try:
                buy, sell = feed.trades()
                bid, bid_qty, ask, ask_qty = feed.book()
            except _FEED_ERRORS as e:
                errors += 1
                if errors <= 5 or errors % 60 == 0:
                    log(f"poll failed ({errors} so far): {e}")
                feed.reset()
                continue
            t = clock()
            p = day_path(out_dir, symbol, t)
            if p != path:
                if fh is not None:
                    fh.close()
                p.parent.mkdir(parents=True, exist_ok=True)
                new = not p.exists()
                path, fh = p, open(p, "a", newline="")
                if new:
                    fh.write(",".join(COLUMNS) + "\n")
                log(f"writing {p}")
            fh.write(f"{t},{bid},{bid_qty},{ask},{ask_qty},{buy:.8f},{sell:.8f}\n")
            fh.flush()
            rows += 1
    finally:
        if fh is not None:
            fh.close()
    return rows, errors
