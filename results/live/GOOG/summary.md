# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 39 (2026-10-02 to 2026-11-27)
- Calibration-only days: 2; days without IEX data: 1

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -37275.79 [-47008.39, -28490.70] dollars (negative); 0 of 39 days positive; 3211 fills a day; 5 s markout -28.376 [-31.452, -25.210] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -37583.27 [-47291.27, -28793.04] dollars (negative); 0 of 39 days positive; 3403 fills a day; 5 s markout -27.446 [-30.437, -24.366] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -38188.35 [-48484.52, -28978.54] | negative | 0/39 | 3222 | -28.164 [-31.220, -24.996] |
| conservative | symmetric | 1 | -42758.15 [-58394.48, -29466.27] | negative | 1/39 | 3152 | -27.572 [-30.623, -24.397] |
| conservative | inventory | 2 | -37275.79 [-47008.39, -28490.70] | negative | 0/39 | 3211 | -28.376 [-31.452, -25.210] |
| conservative | symmetric | 2 | -42265.72 [-57679.82, -29049.08] | negative | 1/39 | 3110 | -27.788 [-30.873, -24.598] |
| conservative | inventory | 4 | -35703.27 [-44929.21, -27583.03] | negative | 0/39 | 3120 | -28.850 [-31.980, -25.674] |
| conservative | symmetric | 4 | -41714.56 [-57227.89, -28524.22] | negative | 1/39 | 3034 | -28.198 [-31.330, -24.953] |
| optimistic | inventory | 1 | -38400.97 [-48739.78, -29222.53] | negative | 0/39 | 3422 | -27.198 [-30.142, -24.137] |
| optimistic | symmetric | 1 | -43079.64 [-58883.96, -29649.29] | negative | 2/39 | 3335 | -26.655 [-29.599, -23.618] |
| optimistic | inventory | 2 | -37583.27 [-47291.27, -28793.04] | negative | 0/39 | 3403 | -27.446 [-30.437, -24.366] |
| optimistic | symmetric | 2 | -42854.96 [-58665.78, -29467.96] | negative | 1/39 | 3285 | -26.875 [-29.828, -23.816] |
| optimistic | inventory | 4 | -36048.09 [-45309.98, -27879.03] | negative | 0/39 | 3315 | -27.825 [-30.839, -24.738] |
| optimistic | symmetric | 4 | -42254.72 [-57860.98, -29078.79] | negative | 1/39 | 3196 | -27.311 [-30.346, -24.176] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4569.79 [-2053.79, 12758.46] | not established |
| conservative | 2 | 4989.93 [-2212.69, 13992.25] | not established |
| conservative | 4 | 6011.28 [-1838.66, 15790.10] | not established |
| optimistic | 1 | 4678.67 [-2194.98, 13201.49] | not established |
| optimistic | 2 | 5271.69 [-2200.16, 14610.11] | not established |
| optimistic | 4 | 6206.63 [-1767.94, 16157.60] | not established |

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
| 2026-11-18 | 0.08424 | 0.1098 / 7.8 | -20776.91 | -20798.03 | 1366 | -34.399 | 100% quoted, 15007 trades |
| 2026-11-19 | 0.08468 | 0.1090 / 8.5 | -119742.99 | -120109.10 | 3816 | -36.841 | 100% quoted, 11809 trades |
| 2026-11-20 | 0.10467 | 0.1077 / 8.3 | -49479.42 | -49753.96 | 3880 | -38.365 | 100% quoted, 24000 trades |
| 2026-11-23 | 0.10575 | 0.1254 / 9.9 | -34107.93 | -34402.36 | 3976 | -21.278 | 100% quoted, 14024 trades |
| 2026-11-24 | 0.09854 | 0.1343 / 10.1 | -24105.85 | -24463.36 | 2661 | -19.500 | 100% quoted, 13760 trades |
| 2026-11-25 | 0.09429 | 0.1368 / 10.5 | -71777.83 | -71885.01 | 4644 | -42.938 | 100% quoted, 16590 trades |
| 2026-11-26 | no IEX data |  |  |  |  |  |  |
| 2026-11-27 | 0.11373 | 0.1474 / 9.2 | -17508.30 | -17395.63 | 2289 | -21.976 | 100% quoted, 7560 trades |
