# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 20 (2026-10-02 to 2026-10-30)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28788.68 [-35622.69, -23386.28] dollars (negative); 0 of 20 days positive; 4512 fills a day; 5 s markout -20.692 [-23.346, -18.273] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29365.40 [-36372.54, -23889.73] dollars (negative); 0 of 20 days positive; 5227 fills a day; 5 s markout -18.721 [-21.168, -16.507] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29596.25 [-36512.14, -24141.88] | negative | 0/20 | 4496 | -20.708 [-23.333, -18.296] |
| conservative | symmetric | 1 | -30292.02 [-36016.39, -25141.34] | negative | 0/20 | 4229 | -21.244 [-24.026, -18.655] |
| conservative | inventory | 2 | -28788.68 [-35622.69, -23386.28] | negative | 0/20 | 4512 | -20.692 [-23.346, -18.273] |
| conservative | symmetric | 2 | -29859.90 [-35638.16, -24737.79] | negative | 0/20 | 4112 | -21.647 [-24.468, -19.050] |
| conservative | inventory | 4 | -27546.29 [-34119.89, -22367.93] | negative | 0/20 | 4426 | -20.871 [-23.627, -18.408] |
| conservative | symmetric | 4 | -28968.59 [-34528.23, -24049.22] | negative | 0/20 | 3892 | -22.437 [-25.300, -19.769] |
| optimistic | inventory | 1 | -30120.63 [-37116.86, -24508.03] | negative | 0/20 | 5238 | -18.691 [-21.124, -16.480] |
| optimistic | symmetric | 1 | -31470.40 [-37274.14, -26304.81] | negative | 0/20 | 4942 | -19.092 [-21.642, -16.776] |
| optimistic | inventory | 2 | -29365.40 [-36372.54, -23889.73] | negative | 0/20 | 5227 | -18.721 [-21.168, -16.507] |
| optimistic | symmetric | 2 | -31063.57 [-36881.96, -25828.79] | negative | 0/20 | 4769 | -19.602 [-22.202, -17.219] |
| optimistic | inventory | 4 | -28168.09 [-34923.68, -22906.75] | negative | 0/20 | 5079 | -19.007 [-21.498, -16.758] |
| optimistic | symmetric | 4 | -29966.21 [-35723.35, -24800.63] | negative | 0/20 | 4476 | -20.409 [-23.076, -17.935] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 695.77 [-2551.25, 3739.50] | not established |
| conservative | 2 | 1071.22 [-2207.13, 3975.75] | not established |
| conservative | 4 | 1422.30 [-1564.71, 4008.33] | not established |
| optimistic | 1 | 1349.77 [-1992.68, 4429.07] | not established |
| optimistic | 2 | 1698.17 [-1590.51, 4754.81] | not established |
| optimistic | 4 | 1798.12 [-1130.15, 4520.91] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.03590 | 0.1627 / 21.8 | -20422.65 | -20056.01 | 2805 | -21.307 | 100% quoted, 18831 trades |
| 2026-10-05 | 0.03352 | 0.1556 / 24.5 | -23657.69 | -23811.35 | 4159 | -17.189 | 100% quoted, 21277 trades |
| 2026-10-06 | 0.03492 | 0.1547 / 23.4 | -16586.88 | -16698.85 | 3883 | -16.620 | 100% quoted, 17706 trades |
| 2026-10-07 | 0.03494 | 0.1521 / 22.9 | -19191.59 | -19890.24 | 4187 | -16.319 | 100% quoted, 22360 trades |
| 2026-10-08 | 0.03494 | 0.1561 / 22.6 | -22937.02 | -23554.55 | 4768 | -18.093 | 100% quoted, 21964 trades |
| 2026-10-09 | 0.03552 | 0.1602 / 22.4 | -30969.88 | -31701.81 | 5736 | -17.518 | 100% quoted, 30585 trades |
| 2026-10-12 | 0.03760 | 0.1646 / 20.4 | -27309.15 | -27596.35 | 3327 | -26.526 | 100% quoted, 16325 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.04355 | 0.1628 / 18.8 | -19274.68 | -20392.63 | 5006 | -14.498 | 100% quoted, 32766 trades |
| 2026-10-15 | 0.04310 | 0.1754 / 19.3 | -13261.23 | -13383.33 | 2902 | -18.648 | 100% quoted, 21362 trades |
| 2026-10-16 | 0.04253 | 0.1672 / 19.7 | -29159.03 | -29472.61 | 6166 | -15.879 | 100% quoted, 29380 trades |
| 2026-10-19 | 0.04269 | 0.1770 / 19.8 | -32431.15 | -33558.76 | 4833 | -23.095 | 100% quoted, 21058 trades |
| 2026-10-20 | 0.04106 | 0.1818 / 19.7 | -58622.64 | -57997.89 | 4256 | -33.597 | 100% quoted, 19216 trades |
| 2026-10-21 | 0.05390 | 0.1790 / 20.8 | -23484.60 | -23720.65 | 4470 | -16.976 | 100% quoted, 19414 trades |
| 2026-10-22 | 0.05449 | 0.1601 / 19.4 | -22919.69 | -23863.97 | 5135 | -11.504 | 100% quoted, 21118 trades |
| 2026-10-23 | 0.05418 | 0.1687 / 17.7 | -34143.81 | -34924.81 | 4547 | -24.544 | 100% quoted, 19025 trades |
| 2026-10-26 | 0.06266 | 0.1529 / 17.0 | -49956.47 | -51251.85 | 5340 | -30.478 | 100% quoted, 22165 trades |
| 2026-10-27 | 0.06605 | 0.1548 / 16.5 | -37592.69 | -38932.58 | 3871 | -31.369 | 100% quoted, 23909 trades |
| 2026-10-28 | 0.05709 | 0.1607 / 17.1 | -18242.35 | -18991.81 | 2915 | -22.848 | 100% quoted, 19597 trades |
| 2026-10-29 | 0.05757 | 0.1600 / 18.0 | -11580.52 | -11787.24 | 2538 | -16.161 | 100% quoted, 22448 trades |
| 2026-10-30 | 0.05669 | 0.1551 / 20.6 | -64029.90 | -65720.71 | 9404 | -20.676 | 100% quoted, 40818 trades |
