# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 28 (2026-10-02 to 2026-11-11)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -34097.12 [-45434.47, -24866.28] dollars (negative); 0 of 28 days positive; 3217 fills a day; 5 s markout -27.824 [-31.893, -24.004] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -34403.59 [-45817.60, -25142.58] dollars (negative); 0 of 28 days positive; 3411 fills a day; 5 s markout -26.934 [-30.925, -23.207] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -35358.68 [-47750.77, -24974.06] | negative | 0/28 | 3229 | -27.676 [-31.835, -23.793] |
| conservative | symmetric | 1 | -39663.12 [-59471.94, -23619.32] | negative | 1/28 | 3140 | -27.288 [-31.431, -23.427] |
| conservative | inventory | 2 | -34097.12 [-45434.47, -24866.28] | negative | 0/28 | 3217 | -27.824 [-31.893, -24.004] |
| conservative | symmetric | 2 | -39197.89 [-58804.28, -23316.36] | negative | 1/28 | 3096 | -27.491 [-31.670, -23.576] |
| conservative | inventory | 4 | -32388.70 [-42788.52, -24057.25] | negative | 0/28 | 3112 | -28.283 [-32.376, -24.489] |
| conservative | symmetric | 4 | -38663.26 [-58288.86, -22831.33] | negative | 1/28 | 3016 | -27.876 [-32.087, -23.928] |
| optimistic | inventory | 1 | -35596.14 [-47915.75, -25184.16] | negative | 0/28 | 3434 | -26.706 [-30.678, -23.021] |
| optimistic | symmetric | 1 | -40194.31 [-60488.24, -23797.01] | negative | 2/28 | 3328 | -26.348 [-30.360, -22.665] |
| optimistic | inventory | 2 | -34403.59 [-45817.60, -25142.58] | negative | 0/28 | 3411 | -26.934 [-30.925, -23.207] |
| optimistic | symmetric | 2 | -39910.16 [-60248.34, -23539.16] | negative | 1/28 | 3275 | -26.575 [-30.609, -22.875] |
| optimistic | inventory | 4 | -32769.09 [-43219.43, -24382.55] | negative | 0/28 | 3310 | -27.302 [-31.283, -23.569] |
| optimistic | symmetric | 4 | -39150.27 [-59022.72, -23190.95] | negative | 1/28 | 3181 | -27.008 [-31.162, -23.210] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4304.45 [-4200.53, 15865.30] | not established |
| conservative | 2 | 5100.77 [-4459.84, 17745.10] | not established |
| conservative | 4 | 6274.55 [-4092.41, 19815.76] | not established |
| optimistic | 1 | 4598.17 [-4226.52, 16605.50] | not established |
| optimistic | 2 | 5506.57 [-4469.61, 18810.54] | not established |
| optimistic | 4 | 6381.18 [-4157.93, 20052.57] | not established |

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
| 2026-10-21 | 0.07767 | 0.0768 / 6.5 | -47241.28 | -47395.18 | 2420 | -42.704 | 100% quoted, 13763 trades |
| 2026-10-22 | 0.07724 | 0.0850 / 8.0 | -14284.81 | -14767.99 | 1900 | -20.943 | 100% quoted, 13497 trades |
| 2026-10-23 | 0.07514 | 0.0958 / 9.9 | -37735.46 | -37867.06 | 1686 | -53.034 | 100% quoted, 7250 trades |
| 2026-10-26 | 0.07559 | 0.0996 / 11.0 | -5240.29 | -5308.07 | 1040 | -19.956 | 100% quoted, 9506 trades |
| 2026-10-27 | 0.07083 | 0.1011 / 13.5 | -14483.97 | -14641.41 | 1896 | -22.055 | 100% quoted, 12353 trades |
| 2026-10-28 | 0.07165 | 0.1110 / 15.2 | -31726.94 | -31676.03 | 2827 | -37.105 | 100% quoted, 14360 trades |
| 2026-10-29 | 0.06874 | 0.1113 / 17.1 | -78447.10 | -78681.18 | 11138 | -15.240 | 100% quoted, 54450 trades |
| 2026-10-30 | 0.07053 | 0.1515 / 16.2 | -39931.14 | -40085.30 | 9481 | -14.111 | 100% quoted, 22459 trades |
| 2026-11-02 | 0.05372 | 0.1789 / 13.8 | -27436.51 | -27646.05 | 3357 | -24.125 | 100% quoted, 14707 trades |
| 2026-11-03 | 0.05796 | 0.1885 / 13.5 | -13817.08 | -13773.35 | 1798 | -26.543 | 100% quoted, 11721 trades |
| 2026-11-04 | 0.05592 | 0.1876 / 13.6 | -27997.24 | -28948.83 | 5549 | -23.177 | 100% quoted, 20045 trades |
| 2026-11-05 | 0.05309 | 0.1942 / 12.8 | -135518.99 | -136168.92 | 6852 | -44.736 | 100% quoted, 21473 trades |
| 2026-11-06 | 0.06552 | 0.1636 / 11.2 | -53632.78 | -53471.79 | 2571 | -45.366 | 100% quoted, 10795 trades |
| 2026-11-09 | 0.07127 | 0.1425 / 13.2 | -34997.31 | -35127.24 | 3776 | -17.760 | 100% quoted, 14482 trades |
| 2026-11-10 | 0.07227 | 0.1397 / 11.9 | -39429.17 | -39506.73 | 4476 | -22.864 | 100% quoted, 11153 trades |
| 2026-11-11 | 0.07838 | 0.1387 / 9.4 | -22274.87 | -22434.01 | 2598 | -16.683 | 100% quoted, 14215 trades |
