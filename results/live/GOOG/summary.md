# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 38 (2026-10-02 to 2026-11-25)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -37795.99 [-47325.58, -29217.83] dollars (negative); 0 of 38 days positive; 3236 fills a day; 5 s markout -28.545 [-31.736, -25.336] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -38114.53 [-47710.31, -29499.24] dollars (negative); 0 of 38 days positive; 3430 fills a day; 5 s markout -27.604 [-30.666, -24.479] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -38756.18 [-49367.73, -29740.08] | negative | 0/38 | 3247 | -28.326 [-31.478, -25.142] |
| conservative | symmetric | 1 | -43436.42 [-58148.26, -30199.66] | negative | 1/38 | 3178 | -27.725 [-30.875, -24.553] |
| conservative | inventory | 2 | -37795.99 [-47325.58, -29217.83] | negative | 0/38 | 3236 | -28.545 [-31.736, -25.336] |
| conservative | symmetric | 2 | -42931.03 [-57494.30, -29863.28] | negative | 1/38 | 3136 | -27.945 [-31.136, -24.753] |
| conservative | inventory | 4 | -36189.94 [-45472.50, -28393.76] | negative | 0/38 | 3143 | -29.035 [-32.227, -25.830] |
| conservative | symmetric | 4 | -42359.59 [-56988.30, -29374.50] | negative | 1/38 | 3059 | -28.357 [-31.591, -25.151] |
| optimistic | inventory | 1 | -38984.75 [-49583.47, -29960.79] | negative | 0/38 | 3449 | -27.349 [-30.416, -24.235] |
| optimistic | symmetric | 1 | -43778.60 [-58819.42, -30444.99] | negative | 2/38 | 3365 | -26.793 [-29.833, -23.700] |
| optimistic | inventory | 2 | -38114.53 [-47710.31, -29499.24] | negative | 0/38 | 3430 | -27.604 [-30.666, -24.479] |
| optimistic | symmetric | 2 | -43528.68 [-58494.03, -30131.66] | negative | 1/38 | 3314 | -27.013 [-30.057, -23.936] |
| optimistic | inventory | 4 | -36542.83 [-45846.62, -28705.64] | negative | 0/38 | 3341 | -28.000 [-31.064, -24.885] |
| optimistic | symmetric | 4 | -42918.14 [-57583.22, -29762.79] | negative | 1/38 | 3224 | -27.457 [-30.596, -24.296] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4680.24 [-2344.37, 12620.27] | not established |
| conservative | 2 | 5135.04 [-2400.44, 13825.28] | not established |
| conservative | 4 | 6169.65 [-1768.89, 15645.45] | not established |
| optimistic | 1 | 4793.84 [-2466.81, 13136.72] | not established |
| optimistic | 2 | 5414.16 [-2389.18, 14474.72] | not established |
| optimistic | 4 | 6375.31 [-1646.18, 15883.97] | not established |

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
