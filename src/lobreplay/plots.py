"""Small dependency-free SVG line charts for the study report.

Each chart is a standalone .svg that follows the viewer's light/dark setting.
Series colours are assigned in a fixed order (blue, then orange); text always
uses the ink colours, never a series colour. Hovering a marker shows its value.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from html import escape
from typing import Sequence

_STYLE = """
.surface{fill:#fcfcfb}.title{fill:#0b0b0b;font-weight:600;font-size:14px}
.sub,.legend{fill:#52514e;font-size:12px}.tick{fill:#898781;font-size:11px;font-variant-numeric:tabular-nums}
.grid{stroke:#e1e0d9;stroke-width:1}.axis{stroke:#c3c2b7;stroke-width:1}.ref{stroke:#898781;stroke-width:1}
.s1{stroke:#2a78d6}.s2{stroke:#eb6834}.f1{fill:#2a78d6}.f2{fill:#eb6834}
.line{fill:none;stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.dot{stroke:#fcfcfb;stroke-width:2}
text{font-family:system-ui,-apple-system,"Segoe UI",sans-serif}
@media (prefers-color-scheme: dark){
.surface{fill:#1a1a19}.title{fill:#ffffff}.sub,.legend{fill:#c3c2b7}
.grid{stroke:#2c2c2a}.axis{stroke:#383835}.dot{stroke:#1a1a19}
.s1{stroke:#3987e5}.s2{stroke:#d95926}.f1{fill:#3987e5}.f2{fill:#d95926}}
"""

W, H = 640, 360
LEFT, RIGHT, TOP, BOTTOM = 64, 24, 76, 48


@dataclass(frozen=True)
class Series:
    name: str
    points: Sequence[tuple[float, float]]
    line: bool = True       # join the points
    markers: bool = True


def _nice_ticks(lo: float, hi: float, n: int = 5) -> list[float]:
    if hi <= lo:
        hi = lo + (abs(lo) or 1.0)
    raw = (hi - lo) / n
    mag = 10 ** math.floor(math.log10(raw))
    step = next(m * mag for m in (1, 2, 5, 10) if m * mag >= raw)
    first = math.floor(lo / step) * step
    ticks = []
    v = first
    while v <= hi + step * 0.999:
        ticks.append(round(v, 12))
        v += step
    return ticks


def _fmt(v: float) -> str:
    if v == 0:
        return "0"
    a = abs(v)
    if a >= 100:
        return f"{v:,.0f}"
    if a >= 1:
        return f"{v:.2f}".rstrip("0").rstrip(".")
    return f"{v:.3g}"


def line_chart(
    title: str,
    subtitle: str,
    x_label: str,
    series: Sequence[Series],
    log_x: bool = False,
    reference_y: float | None = None,
    x_ticks: Sequence[float] | None = None,
) -> str:
    """At most two series. `reference_y` draws a labelled-by-subtitle horizontal rule."""
    series = [s for s in series if s.points][:2]
    xs = [p[0] for s in series for p in s.points]
    ys = [p[1] for s in series for p in s.points if math.isfinite(p[1])]
    if not xs or not ys:
        return _frame(title, "no data", "")
    if reference_y is not None:
        ys.append(reference_y)
    fx = (lambda v: math.log10(v)) if log_x else (lambda v: v)
    x_lo, x_hi = fx(min(xs)), fx(max(xs))
    if x_hi == x_lo:
        x_lo, x_hi = x_lo - 1, x_hi + 1
    y_ticks = _nice_ticks(min(ys), max(ys))
    y_lo, y_hi = y_ticks[0], y_ticks[-1]
    pw, ph = W - LEFT - RIGHT, H - TOP - BOTTOM

    def px(v: float) -> float:
        return LEFT + (fx(v) - x_lo) / (x_hi - x_lo) * pw

    def py(v: float) -> float:
        return TOP + (1 - (v - y_lo) / (y_hi - y_lo)) * ph

    out = []
    for t in y_ticks:
        out.append(f'<line class="grid" x1="{LEFT}" x2="{W - RIGHT}" y1="{py(t):.1f}" y2="{py(t):.1f}"/>')
        out.append(f'<text class="tick" x="{LEFT - 8}" y="{py(t) + 4:.1f}" text-anchor="end">{_fmt(t)}</text>')
    out.append(f'<line class="axis" x1="{LEFT}" x2="{W - RIGHT}" y1="{TOP + ph}" y2="{TOP + ph}"/>')
    for t in (x_ticks if x_ticks is not None else sorted(set(xs))):
        out.append(f'<text class="tick" x="{px(t):.1f}" y="{TOP + ph + 18}" text-anchor="middle">{_fmt(t)}</text>')
    out.append(f'<text class="sub" x="{LEFT + pw / 2}" y="{H - 10}" text-anchor="middle">{escape(x_label)}</text>')
    if reference_y is not None:
        out.append(f'<line class="ref" x1="{LEFT}" x2="{W - RIGHT}" y1="{py(reference_y):.1f}" y2="{py(reference_y):.1f}"/>')

    # Drawn last-to-first, with the later series' markers larger, so that two
    # series lying on top of each other are both still visible.
    for i, s in reversed(list(enumerate(series, start=1))):
        r = 3 + 2 * i
        pts = [(x, y) for x, y in s.points if math.isfinite(y)]
        if s.line and len(pts) > 1:
            path = " ".join(f"{px(x):.1f},{py(y):.1f}" for x, y in pts)
            out.append(f'<polyline class="line s{i}" points="{path}"/>')
        if s.markers:
            for x, y in pts:
                tip = escape(f"{s.name}: {_fmt(y)} at {x_label} {_fmt(x)}")
                out.append(f'<circle class="dot f{i}" cx="{px(x):.1f}" cy="{py(y):.1f}" r="{r}"><title>{tip}</title></circle>')

    if len(series) > 1:   # a single series is named by the title
        x = LEFT
        for i, s in enumerate(series, start=1):
            out.append(f'<circle class="f{i}" cx="{x + 5}" cy="{TOP - 16}" r="5"/>')
            out.append(f'<text class="legend" x="{x + 16}" y="{TOP - 12}">{escape(s.name)}</text>')
            x += 28 + 7 * len(s.name)
    return _frame(title, subtitle, "\n".join(out))


def _frame(title: str, subtitle: str, body: str) -> str:
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
        f'aria-label="{escape(title)}">\n<style>{_STYLE}</style>\n'
        f'<rect class="surface" width="{W}" height="{H}" rx="8"/>\n'
        f'<text class="title" x="{LEFT}" y="26">{escape(title)}</text>\n'
        f'<text class="sub" x="{LEFT}" y="44">{escape(subtitle)}</text>\n{body}\n</svg>\n'
    )
