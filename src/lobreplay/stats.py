"""Bootstrap confidence intervals over sessions (approach document §5.7).

One day per stock is little data, so every figure is a mean over fixed
windows with a percentile-bootstrap interval, and a difference only counts if
its interval excludes zero.
"""

from __future__ import annotations

import random
from dataclasses import asdict, dataclass
from statistics import fmean
from typing import Sequence


@dataclass(frozen=True)
class Estimate:
    mean: float
    lo: float
    hi: float
    n: int

    @property
    def excludes_zero(self) -> bool:
        return self.n > 1 and (self.lo > 0 or self.hi < 0)

    def to_dict(self) -> dict:
        return {**asdict(self), "excludes_zero": self.excludes_zero}


def bootstrap_mean(values: Sequence[float], n_boot: int = 2000, alpha: float = 0.05, seed: int = 0) -> Estimate:
    """Mean with a percentile bootstrap (1 - alpha) interval. Resamples whole values (windows)."""
    n = len(values)
    if n == 0:
        return Estimate(float("nan"), float("nan"), float("nan"), 0)
    mean = fmean(values)
    if n == 1:
        return Estimate(mean, mean, mean, 1)
    rng = random.Random(seed)
    means = sorted(fmean(rng.choices(values, k=n)) for _ in range(n_boot))
    lo = means[int((alpha / 2) * (n_boot - 1))]
    hi = means[int((1 - alpha / 2) * (n_boot - 1))]
    return Estimate(mean, lo, hi, n)


def paired_difference(a: Sequence[float], b: Sequence[float], **kw) -> Estimate:
    """Bootstrap of mean(a - b) with a and b paired by window."""
    if len(a) != len(b):
        raise ValueError(f"paired samples differ in length: {len(a)} vs {len(b)}")
    return bootstrap_mean([x - y for x, y in zip(a, b)], **kw)
