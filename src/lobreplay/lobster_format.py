"""LOBSTER file-format constants — the ONE place format assumptions live.

Everything here was written from the LOBSTER documentation as remembered, NOT
from the readme bundled with the sample files. Before trusting any result,
check each constant against that readme (see docs/DATA_FORMAT.md, which has a
checklist). If a constant is wrong, fix it here; nothing else should hard-code
these values.
"""

from enum import IntEnum


class EventType(IntEnum):
    """Message-file column 2."""

    SUBMIT = 1          # new limit order
    CANCEL = 2          # partial cancellation (size = shares removed)
    DELETE = 3          # total deletion (size = shares removed, i.e. what was left)
    EXEC_VISIBLE = 4    # execution of a visible resting limit order
    EXEC_HIDDEN = 5     # execution of a hidden (non-displayed) order — book unchanged
    CROSS = 6           # cross trade, e.g. auction — book unchanged
    HALT = 7            # trading-halt indicator — book unchanged


class Direction(IntEnum):
    """Message-file column 6: the side of the *resting limit order*.

    For an execution (type 4/5), direction is the side of the order that was
    hit, so a SELL-side execution is a buyer-initiated trade.
    """

    SELL = -1
    BUY = 1


# Event types that change the visible book.
BOOK_EVENTS = frozenset({EventType.SUBMIT, EventType.CANCEL, EventType.DELETE, EventType.EXEC_VISIBLE})

# Halt messages (type 7) put a status code in the price column instead of a price.
HALT_PRICE_HALTED = -1
HALT_PRICE_QUOTING = 0
HALT_PRICE_RESUMED = 1
HALT_PRICE_CODES = frozenset({HALT_PRICE_HALTED, HALT_PRICE_QUOTING, HALT_PRICE_RESUMED})

# Prices are dollars * PRICE_SCALE, stored as integers. Never convert except for display.
PRICE_SCALE = 10_000

# Minimum price increment: $0.01 for NASDAQ stocks priced at $1 or more.
TICK_SIZE = 100

# Orderbook file: unused levels are filled with these dummy values.
DUMMY_ASK_PRICE = 9_999_999_999
DUMMY_BID_PRICE = -9_999_999_999
DUMMY_SIZE = 0

# Orderbook file column layout per level, repeated `levels` times:
#   ask_price, ask_size, bid_price, bid_size
ORDERBOOK_COLS_PER_LEVEL = 4

MESSAGE_COLS = 6

# Market session in seconds after midnight (Eastern time).
SESSION_START_S = 34_200   # 09:30:00
SESSION_END_S = 57_600     # 16:00:00

NS_PER_S = 1_000_000_000


def format_price(price: int) -> str:
    """Integer LOBSTER price -> '$585.33' for display only."""
    return f"${price / PRICE_SCALE:,.4f}".rstrip("0").rstrip(".")
