# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 32 (2026-10-02 to 2026-11-17)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -34883.02 [-44924.93, -26285.12] dollars (negative); 0 of 32 days positive; 3207 fills a day; 5 s markout -27.855 [-31.523, -24.329] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -35216.88 [-45335.17, -26605.19] dollars (negative); 0 of 32 days positive; 3398 fills a day; 5 s markout -26.984 [-30.505, -23.603] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -35895.90 [-47101.01, -26456.10] | negative | 0/32 | 3220 | -27.661 [-31.319, -24.207] |
| conservative | symmetric | 1 | -39263.26 [-57937.89, -25495.55] | negative | 1/32 | 3145 | -27.135 [-30.847, -23.669] |
| conservative | inventory | 2 | -34883.02 [-44924.93, -26285.12] | negative | 0/32 | 3207 | -27.855 [-31.523, -24.329] |
| conservative | symmetric | 2 | -38814.42 [-57383.04, -25225.18] | negative | 1/32 | 3102 | -27.330 [-31.049, -23.835] |
| conservative | inventory | 4 | -33290.57 [-42871.32, -25274.17] | negative | 0/32 | 3105 | -28.377 [-32.075, -24.838] |
| conservative | symmetric | 4 | -38270.24 [-56882.38, -24673.81] | negative | 1/32 | 3027 | -27.705 [-31.513, -24.170] |
| optimistic | inventory | 1 | -36151.46 [-47346.36, -26725.56] | negative | 0/32 | 3418 | -26.753 [-30.293, -23.429] |
| optimistic | symmetric | 1 | -39740.16 [-58878.95, -25668.09] | negative | 2/32 | 3329 | -26.247 [-29.808, -22.907] |
| optimistic | inventory | 2 | -35216.88 [-45335.17, -26605.19] | negative | 0/32 | 3398 | -26.984 [-30.505, -23.603] |
| optimistic | symmetric | 2 | -39454.82 [-58595.51, -25475.20] | negative | 1/32 | 3278 | -26.454 [-30.044, -23.101] |
| optimistic | inventory | 4 | -33648.21 [-43278.69, -25579.77] | negative | 0/32 | 3299 | -27.393 [-30.935, -23.932] |
| optimistic | symmetric | 4 | -38770.56 [-57445.40, -25188.52] | negative | 1/32 | 3188 | -26.867 [-30.554, -23.431] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3367.36 [-3789.83, 13694.48] | not established |
| conservative | 2 | 3931.39 [-3955.29, 15085.60] | not established |
| conservative | 4 | 4979.67 [-3648.41, 17270.99] | not established |
| optimistic | 1 | 3588.70 [-3826.23, 14348.80] | not established |
| optimistic | 2 | 4237.94 [-4000.74, 16044.51] | not established |
| optimistic | 4 | 5122.35 [-3642.32, 17655.38] | not established |

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
| 2026-11-12 | 0.07707 | 0.1302 / 9.4 | -31153.76 | -31172.15 | 4227 | -20.975 | 100% quoted, 15450 trades |
| 2026-11-13 | 0.06975 | 0.1167 / 8.6 | -43874.19 | -45419.14 | 3613 | -24.181 | 100% quoted, 11223 trades |
| 2026-11-16 | 0.07074 | 0.1158 / 7.3 | -64701.93 | -64791.04 | 2621 | -40.152 | 100% quoted, 11213 trades |
| 2026-11-17 | 0.08289 | 0.1090 / 6.8 | -21807.49 | -22257.33 | 2082 | -26.996 | 100% quoted, 13248 trades |
