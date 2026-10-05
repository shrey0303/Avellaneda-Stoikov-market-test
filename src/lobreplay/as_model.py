"""Avellaneda-Stoikov (2008) quoting formulas.

Units used throughout Phases 5-6:
    price, delta   dollars
    time           seconds
    sigma          dollars per sqrt(second)
    A              fills per second at delta = 0
    k              1 / dollars
    q              inventory in lots (one lot = one quote size)
    gamma          1 / dollars

    reservation price   r      = s - q * gamma * sigma^2 * (T - t)
    total spread        spread = gamma * sigma^2 * (T - t) + (2 / gamma) * ln(1 + gamma / k)
    quotes              bid = r - spread / 2,   ask = r + spread / 2

The symmetric strategy quotes the same spread centred on the mid. It must not
see inventory anywhere, including in how quotes are rounded to ticks.
"""

from __future__ import annotations

import math
from dataclasses import dataclass

INVENTORY = "inventory"
SYMMETRIC = "symmetric"
STRATEGIES = (INVENTORY, SYMMETRIC)


@dataclass(frozen=True)
class ASParams:
    sigma: float
    A: float
    k: float
    gamma: float

    def __post_init__(self) -> None:
        if not (self.sigma > 0 and self.k > 0 and self.gamma > 0 and self.A > 0):
            raise ValueError(f"A-S parameters must all be positive: {self}")


def reservation_price(mid: float, q: float, p: ASParams, tau: float) -> float:
    return mid - q * p.gamma * p.sigma**2 * tau


def total_spread(p: ASParams, tau: float) -> float:
    return p.gamma * p.sigma**2 * tau + (2 / p.gamma) * math.log1p(p.gamma / p.k)


def quotes(strategy: str, mid: float, q: float, p: ASParams, tau: float) -> tuple[float, float]:
    """Continuous (bid, ask) in dollars. `tau` is seconds left in the session."""
    half = total_spread(p, tau) / 2
    if strategy == INVENTORY:
        centre = reservation_price(mid, q, p, tau)
    elif strategy == SYMMETRIC:
        centre = mid  # q is deliberately unused
    else:
        raise ValueError(f"unknown strategy {strategy!r}")
    return centre - half, centre + half


def gamma_for_penalty(penalty: float, sigma: float, horizon: float) -> float:
    """Risk aversion at which one lot of inventory shifts the reservation price by
    `penalty` dollars at the start of a session of `horizon` seconds."""
    return penalty / (sigma**2 * horizon)


def intensity(delta: float, A: float, k: float) -> float:
    """Fill rate (per second) of a quote resting `delta` dollars from the mid."""
    return A * math.exp(-k * delta)
