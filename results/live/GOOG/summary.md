# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 12 (2026-10-02 to 2026-10-20)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27543.70 [-44573.17, -16518.48] dollars (negative); 0 of 12 days positive; 2225 fills a day; 5 s markout -27.722 [-32.566, -22.963] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -27983.45 [-45196.61, -16924.14] dollars (negative); 0 of 12 days positive; 2315 fills a day; 5 s markout -27.228 [-31.983, -22.514] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -28775.67 [-49518.37, -15894.41] | negative | 0/12 | 2216 | -27.537 [-32.382, -22.772] |
| conservative | symmetric | 1 | -32971.35 [-60626.68, -15681.12] | negative | 0/12 | 2194 | -26.800 [-31.623, -22.053] |
| conservative | inventory | 2 | -27543.70 [-44573.17, -16518.48] | negative | 0/12 | 2225 | -27.722 [-32.566, -22.963] |
| conservative | symmetric | 2 | -32751.17 [-60272.46, -15497.99] | negative | 0/12 | 2174 | -26.907 [-31.741, -22.168] |
| conservative | inventory | 4 | -25892.57 [-39514.65, -16887.28] | negative | 0/12 | 2190 | -28.154 [-32.948, -23.388] |
| conservative | symmetric | 4 | -32190.75 [-59710.62, -15096.26] | negative | 0/12 | 2138 | -27.131 [-31.934, -22.414] |
| optimistic | inventory | 1 | -29011.81 [-49764.71, -16124.48] | negative | 0/12 | 2308 | -27.001 [-31.903, -22.232] |
| optimistic | symmetric | 1 | -33189.46 [-61230.48, -15695.09] | negative | 0/12 | 2274 | -26.355 [-31.127, -21.672] |
| optimistic | inventory | 2 | -27983.45 [-45196.61, -16924.14] | negative | 0/12 | 2315 | -27.228 [-31.983, -22.514] |
| optimistic | symmetric | 2 | -32950.79 [-60972.86, -15531.01] | negative | 0/12 | 2254 | -26.440 [-31.187, -21.767] |
| optimistic | inventory | 4 | -26248.24 [-39851.10, -17234.94] | negative | 0/12 | 2282 | -27.656 [-32.355, -22.941] |
| optimistic | symmetric | 4 | -32538.11 [-60401.03, -15283.91] | negative | 0/12 | 2213 | -26.621 [-31.355, -21.953] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4195.69 [-796.33, 11283.22] | not established |
| conservative | 2 | 5207.47 [-2034.96, 15786.45] | not established |
| conservative | 4 | 6298.18 [-2907.55, 20505.21] | not established |
| optimistic | 1 | 4177.65 [-1065.64, 11598.41] | not established |
| optimistic | 2 | 4967.34 [-2551.16, 15795.35] | not established |
| optimistic | 4 | 6289.87 [-3052.05, 20720.84] | not established |

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
| 2026-10-20 | 0.08560 | 0.0785 / 5.9 | -7612.79 | -7549.54 | 1130 | -29.259 | 100% quoted, 5946 trades |
