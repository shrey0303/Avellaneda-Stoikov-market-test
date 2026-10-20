# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 11 (2026-10-02 to 2026-10-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29355.60 [-46180.82, -18125.16] dollars (negative); 0 of 11 days positive; 2325 fills a day; 5 s markout -27.583 [-32.715, -22.565] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29841.07 [-46825.19, -18572.82] dollars (negative); 0 of 11 days positive; 2418 fills a day; 5 s markout -27.075 [-32.155, -22.108] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -30692.94 [-51053.47, -17491.76] | negative | 0/11 | 2315 | -27.373 [-32.500, -22.396] |
| conservative | symmetric | 1 | -35202.03 [-61538.84, -17264.40] | negative | 0/11 | 2292 | -26.525 [-31.635, -21.498] |
| conservative | inventory | 2 | -29355.60 [-46180.82, -18125.16] | negative | 0/11 | 2325 | -27.583 [-32.715, -22.565] |
| conservative | symmetric | 2 | -34972.94 [-61240.65, -17129.52] | negative | 0/11 | 2271 | -26.624 [-31.738, -21.585] |
| conservative | inventory | 4 | -27538.87 [-40778.84, -18290.12] | negative | 0/11 | 2287 | -28.065 [-33.129, -23.053] |
| conservative | symmetric | 4 | -34354.89 [-60594.98, -16555.39] | negative | 0/11 | 2235 | -26.822 [-31.906, -21.824] |
| optimistic | inventory | 1 | -30992.79 [-51485.13, -17837.16] | negative | 0/11 | 2409 | -26.878 [-32.054, -21.887] |
| optimistic | symmetric | 1 | -35475.83 [-62259.18, -17398.38] | negative | 0/11 | 2375 | -26.112 [-31.148, -21.108] |
| optimistic | inventory | 2 | -29841.07 [-46825.19, -18572.82] | negative | 0/11 | 2418 | -27.075 [-32.155, -22.108] |
| optimistic | symmetric | 2 | -35221.80 [-61837.82, -17204.61] | negative | 0/11 | 2354 | -26.191 [-31.179, -21.198] |
| optimistic | inventory | 4 | -27900.55 [-41173.91, -18620.28] | negative | 0/11 | 2382 | -27.556 [-32.541, -22.617] |
| optimistic | symmetric | 4 | -34758.31 [-61196.47, -16826.80] | negative | 0/11 | 2311 | -26.349 [-31.330, -21.377] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4509.09 [-948.52, 11296.79] | not established |
| conservative | 2 | 5617.34 [-2388.31, 15866.63] | not established |
| conservative | 4 | 6816.02 [-3499.20, 20828.24] | not established |
| optimistic | 1 | 4483.04 [-1173.65, 11584.59] | not established |
| optimistic | 2 | 5380.72 [-2843.11, 15814.06] | not established |
| optimistic | 4 | 6857.76 [-3514.03, 21024.26] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.06399 | 0.1467 / 15.3 | -11239.88 | -11388.79 | 2611 | -14.894 | 100% quoted, 6767 trades |
| 2026-10-05 | 0.06162 | 0.1095 / 12.5 | -22660.49 | -22799.99 | 2604 | -17.254 | 100% quoted, 9105 trades |
| 2026-10-06 | 0.05802 | 0.1063 / 11.7 | -15860.42 | -16278.82 | 2137 | -16.669 | 100% quoted, 5468 trades |
| 2026-10-07 | 0.05532 | 0.0954 / 10.7 | -31484.55 | -31831.84 | 2531 | -28.992 | 100% quoted, 6416 trades |
| 2026-10-08 | 0.06492 | 0.0900 / 9.8 | -100703.35 | -101842.43 | 3797 | -34.179 | 100% quoted, 7026 trades |
| 2026-10-09 | 0.07586 | 0.0759 / 6.7 | -15241.87 | -16035.32 | 2180 | -26.736 | 100% quoted, 6154 trades |
| 2026-10-12 | 0.08256 | 0.0739 / 6.1 | -26412.27 | -26445.74 | 1682 | -34.199 | 100% quoted, 4728 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.09808 | 0.0677 / 4.8 | -19385.65 | -20284.38 | 2738 | -22.659 | 100% quoted, 8865 trades |
| 2026-10-15 | 0.09592 | 0.0710 / 4.4 | -8858.35 | -9745.90 | 1481 | -31.364 | 100% quoted, 8160 trades |
| 2026-10-16 | 0.08691 | 0.0722 / 5.4 | -43782.76 | -44302.42 | 1600 | -44.858 | 100% quoted, 5455 trades |
| 2026-10-19 | 0.09084 | 0.0722 / 5.5 | -27282.03 | -27296.19 | 2210 | -31.606 | 100% quoted, 8489 trades |
