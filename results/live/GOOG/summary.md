# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 27 (2026-10-02 to 2026-11-10)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -34534.98 [-46080.68, -24831.43] dollars (negative); 0 of 27 days positive; 3240 fills a day; 5 s markout -28.237 [-32.460, -24.271] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -34846.91 [-46474.33, -25132.83] dollars (negative); 0 of 27 days positive; 3436 fills a day; 5 s markout -27.330 [-31.453, -23.472] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -35754.29 [-48337.40, -25102.05] | negative | 0/27 | 3252 | -28.087 [-32.327, -24.085] |
| conservative | symmetric | 1 | -39997.81 [-59249.17, -23098.62] | negative | 1/27 | 3163 | -27.680 [-31.962, -23.696] |
| conservative | inventory | 2 | -34534.98 [-46080.68, -24831.43] | negative | 0/27 | 3240 | -28.237 [-32.460, -24.271] |
| conservative | symmetric | 2 | -39539.53 [-58536.63, -22800.90] | negative | 1/27 | 3118 | -27.881 [-32.188, -23.886] |
| conservative | inventory | 4 | -32858.00 [-43645.30, -24220.51] | negative | 0/27 | 3137 | -28.712 [-32.925, -24.702] |
| conservative | symmetric | 4 | -39027.73 [-58005.47, -22279.06] | negative | 1/27 | 3039 | -28.273 [-32.611, -24.230] |
| optimistic | inventory | 1 | -35990.24 [-48569.08, -25408.14] | negative | 0/27 | 3459 | -27.093 [-31.218, -23.234] |
| optimistic | symmetric | 1 | -40499.23 [-60249.19, -23254.53] | negative | 2/27 | 3354 | -26.725 [-30.811, -22.932] |
| optimistic | inventory | 2 | -34846.91 [-46474.33, -25132.83] | negative | 0/27 | 3436 | -27.330 [-31.453, -23.472] |
| optimistic | symmetric | 2 | -40221.18 [-60235.14, -23057.71] | negative | 1/27 | 3300 | -26.955 [-31.084, -23.131] |
| optimistic | inventory | 4 | -33244.62 [-44107.03, -24535.41] | negative | 0/27 | 3335 | -27.719 [-31.847, -23.879] |
| optimistic | symmetric | 4 | -39494.73 [-58915.47, -22643.39] | negative | 1/27 | 3206 | -27.393 [-31.617, -23.460] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4243.52 [-4406.35, 15033.30] | not established |
| conservative | 2 | 5004.55 [-4562.74, 16654.01] | not established |
| conservative | 4 | 6169.73 [-4142.76, 18823.03] | not established |
| optimistic | 1 | 4508.99 [-4523.59, 15813.81] | not established |
| optimistic | 2 | 5374.27 [-4554.97, 17568.89] | not established |
| optimistic | 4 | 6250.11 [-4295.53, 18988.34] | not established |

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
