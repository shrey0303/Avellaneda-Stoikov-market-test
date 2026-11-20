# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 34 (2026-10-02 to 2026-11-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -36964.02 [-47571.91, -27571.87] dollars (negative); 0 of 34 days positive; 3170 fills a day; 5 s markout -28.312 [-31.762, -24.975] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -37289.63 [-47926.72, -27865.59] dollars (negative); 0 of 34 days positive; 3358 fills a day; 5 s markout -27.421 [-30.767, -24.206] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -37970.76 [-49238.15, -28002.47] | negative | 0/34 | 3183 | -28.100 [-31.569, -24.770] |
| conservative | symmetric | 1 | -41006.81 [-58226.88, -26563.30] | negative | 1/34 | 3112 | -27.531 [-31.024, -24.200] |
| conservative | inventory | 2 | -36964.02 [-47571.91, -27571.87] | negative | 0/34 | 3170 | -28.312 [-31.762, -24.975] |
| conservative | symmetric | 2 | -40558.94 [-57647.43, -26216.15] | negative | 1/34 | 3071 | -27.740 [-31.238, -24.373] |
| conservative | inventory | 4 | -35280.24 [-45121.32, -26642.80] | negative | 0/34 | 3072 | -28.838 [-32.329, -25.509] |
| conservative | symmetric | 4 | -40038.66 [-57093.72, -25697.93] | negative | 1/34 | 2996 | -28.144 [-31.698, -24.745] |
| optimistic | inventory | 1 | -38215.76 [-49440.70, -28234.57] | negative | 0/34 | 3379 | -27.153 [-30.489, -23.947] |
| optimistic | symmetric | 1 | -41465.70 [-58947.32, -26808.79] | negative | 2/34 | 3294 | -26.616 [-30.000, -23.438] |
| optimistic | inventory | 2 | -37289.63 [-47926.72, -27865.59] | negative | 0/34 | 3358 | -27.421 [-30.767, -24.206] |
| optimistic | symmetric | 2 | -41202.76 [-58724.80, -26514.21] | negative | 1/34 | 3244 | -26.830 [-30.209, -23.638] |
| optimistic | inventory | 4 | -35624.41 [-45530.26, -26965.55] | negative | 0/34 | 3264 | -27.815 [-31.189, -24.632] |
| optimistic | symmetric | 4 | -40553.66 [-57730.58, -26119.88] | negative | 1/34 | 3156 | -27.267 [-30.701, -23.988] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3036.05 [-3701.49, 12360.77] | not established |
| conservative | 2 | 3594.92 [-3771.80, 13588.73] | not established |
| conservative | 4 | 4758.42 [-3375.71, 15745.49] | not established |
| optimistic | 1 | 3249.93 [-3751.87, 12883.00] | not established |
| optimistic | 2 | 3913.14 [-3799.28, 14527.11] | not established |
| optimistic | 4 | 4929.25 [-3376.39, 16064.72] | not established |

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
