"""The model's own world: the benchmark the replay is compared against (Q1).

Here the A-S assumptions hold exactly. The mid is a driftless Brownian motion
with the calibrated sigma, and a quote resting delta from the mid is filled at
Poisson rate A * exp(-k * delta), independently of where the mid goes next. So
by construction a fill carries no information: expected markout is zero.

Quotes are continuous (never rounded to ticks), one lot per fill, and each
path is one session of the same length as a replay window.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass

from .as_model import INVENTORY, SYMMETRIC, ASParams, total_spread


@dataclass(frozen=True)
class ModelPath:
    pnl: float              # dollars
    spread_capture: float   # dollars
    inventory_pnl: float    # dollars
    fills: int
    end_inventory: int      # shares


def simulate(
    strategy: str,
    p: ASParams,
    horizon_s: float,
    n_paths: int = 200,
    dt: float = 0.5,
    lot: int = 100,
    seed: int = 0,
    start_price: float = 100.0,
) -> list[ModelPath]:
    if strategy not in (INVENTORY, SYMMETRIC):
        raise ValueError(f"unknown strategy {strategy!r}")
    rng = random.Random(seed)
    steps = max(1, round(horizon_s / dt))
    step_sd = p.sigma * math.sqrt(dt)
    skew = p.gamma * p.sigma**2 if strategy == INVENTORY else 0.0   # reservation shift per lot per second left
    paths = []
    for _ in range(n_paths):
        s, q, cash, capture, fills = start_price, 0, 0.0, 0.0, 0
        for i in range(steps):
            tau = horizon_s - i * dt
            centre = s - q * skew * tau
            half = total_spread(p, tau) / 2
            bid, ask = centre - half, centre + half
            # At most one fill per side per step; dt must keep A * dt well below 1.
            # The exponent is capped so a quote skewed far through the mid cannot overflow.
            if rng.random() < -math.expm1(-p.A * math.exp(min(p.k * (bid - s), 50.0)) * dt):
                q += 1
                cash -= bid
                capture += s - bid
                fills += 1
            if rng.random() < -math.expm1(-p.A * math.exp(min(p.k * (s - ask), 50.0)) * dt):
                q -= 1
                cash += ask
                capture += ask - s
                fills += 1
            s += step_sd * rng.gauss(0.0, 1.0)
        pnl = cash + q * s
        paths.append(ModelPath(pnl * lot, capture * lot, (pnl - capture) * lot, fills, q * lot))
    return paths
