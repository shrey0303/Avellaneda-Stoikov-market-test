# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 24 (2026-10-02 to 2026-11-05)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -134540.40 [-169924.05, -102792.26] dollars (negative); 0 of 24 days positive; 4985 fills a day; 5 s markout -58.430 [-71.307, -48.067] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -134998.91 [-170436.92, -103101.50] dollars (negative); 0 of 24 days positive; 5135 fills a day; 5 s markout -57.257 [-70.095, -47.017] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -136737.56 [-172708.24, -104635.67] | negative | 0/24 | 4902 | -58.609 [-71.930, -48.071] |
| conservative | symmetric | 1 | -141573.41 [-181311.21, -108069.10] | negative | 0/24 | 4784 | -58.336 [-71.961, -47.625] |
| conservative | inventory | 2 | -134540.40 [-169924.05, -102792.26] | negative | 0/24 | 4985 | -58.430 [-71.307, -48.067] |
| conservative | symmetric | 2 | -141151.58 [-180916.61, -107605.69] | negative | 0/24 | 4753 | -58.565 [-72.235, -47.888] |
| conservative | inventory | 4 | -129676.25 [-165415.09, -98948.38] | negative | 0/24 | 4993 | -59.201 [-72.126, -48.849] |
| conservative | symmetric | 4 | -140340.42 [-180176.04, -106815.14] | negative | 0/24 | 4692 | -59.032 [-72.716, -48.297] |
| optimistic | inventory | 1 | -137244.82 [-173204.60, -105047.39] | negative | 0/24 | 5055 | -57.325 [-70.523, -46.848] |
| optimistic | symmetric | 1 | -142047.85 [-181926.71, -108513.95] | negative | 0/24 | 4930 | -57.038 [-70.174, -46.470] |
| optimistic | inventory | 2 | -134998.91 [-170436.92, -103101.50] | negative | 0/24 | 5135 | -57.257 [-70.095, -47.017] |
| optimistic | symmetric | 2 | -141489.57 [-181237.36, -107922.47] | negative | 0/24 | 4893 | -57.356 [-70.620, -46.775] |
| optimistic | inventory | 4 | -130046.59 [-165826.77, -99128.55] | negative | 0/24 | 5145 | -58.029 [-70.831, -47.904] |
| optimistic | symmetric | 4 | -140764.38 [-180394.63, -107300.55] | negative | 0/24 | 4824 | -57.876 [-71.405, -47.187] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4835.85 [-1808.32, 12538.67] | not established |
| conservative | 2 | 6611.17 [-2419.67, 16860.16] | not established |
| conservative | 4 | 10664.18 [504.87, 22881.98] | positive |
| optimistic | 1 | 4803.03 [-2332.68, 12691.53] | not established |
| optimistic | 2 | 6490.66 [-2665.05, 16754.08] | not established |
| optimistic | 4 | 10717.79 [342.28, 22980.22] | positive |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.09188 | 0.1438 / 7.8 | -65274.53 | -65888.49 | 2452 | -75.700 | 100% quoted, 13763 trades |
| 2026-10-05 | 0.12604 | 0.1347 / 8.9 | -79396.69 | -80419.49 | 4148 | -41.324 | 100% quoted, 16740 trades |
| 2026-10-06 | 0.11589 | 0.1348 / 9.1 | -52361.15 | -51868.89 | 4397 | -33.239 | 100% quoted, 13695 trades |
| 2026-10-07 | 0.10694 | 0.1325 / 8.9 | -16941.47 | -17240.57 | 2370 | -29.213 | 100% quoted, 13278 trades |
| 2026-10-08 | 0.09814 | 0.1282 / 9.5 | -89481.54 | -90269.51 | 3660 | -53.834 | 100% quoted, 17122 trades |
| 2026-10-09 | 0.11259 | 0.1277 / 9.8 | -75181.24 | -75637.03 | 3752 | -44.122 | 100% quoted, 12668 trades |
| 2026-10-12 | 0.11763 | 0.1272 / 9.6 | -113648.16 | -114515.77 | 3508 | -77.494 | 100% quoted, 12123 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.13651 | 0.1311 / 8.8 | -69596.52 | -69191.59 | 4345 | -42.767 | 100% quoted, 19532 trades |
| 2026-10-15 | 0.14547 | 0.1440 / 8.5 | -129653.63 | -129815.96 | 4768 | -43.605 | 100% quoted, 13232 trades |
| 2026-10-16 | 0.14607 | 0.1387 / 7.6 | -304716.82 | -304893.28 | 6729 | -73.847 | 100% quoted, 17571 trades |
| 2026-10-19 | 0.17502 | 0.1457 / 6.6 | -111791.66 | -111739.96 | 5452 | -42.922 | 100% quoted, 13924 trades |
| 2026-10-20 | 0.16547 | 0.1530 / 6.2 | -116555.06 | -116739.68 | 4135 | -36.905 | 100% quoted, 9975 trades |
| 2026-10-21 | 0.17516 | 0.1369 / 5.5 | -44263.54 | -44228.99 | 3663 | -34.778 | 100% quoted, 10191 trades |
| 2026-10-22 | 0.17922 | 0.1220 / 4.2 | -71692.00 | -71831.55 | 5312 | -30.329 | 100% quoted, 16194 trades |
| 2026-10-23 | 0.17294 | 0.1301 / 4.3 | -170271.54 | -170360.20 | 3705 | -70.328 | 100% quoted, 11728 trades |
| 2026-10-26 | 0.15766 | 0.1219 / 4.4 | -111991.52 | -112232.53 | 5068 | -47.914 | 100% quoted, 15140 trades |
| 2026-10-27 | 0.16665 | 0.1211 / 4.1 | -71920.07 | -71868.73 | 3214 | -60.372 | 100% quoted, 12940 trades |
| 2026-10-28 | 0.16607 | 0.1255 / 5.0 | -77289.88 | -77398.54 | 4709 | -50.572 | 100% quoted, 20210 trades |
| 2026-10-29 | 0.16483 | 0.1436 / 5.9 | -228691.03 | -230438.36 | 9416 | -41.140 | 100% quoted, 26085 trades |
| 2026-10-30 | 0.16610 | 0.1508 / 5.3 | -236930.34 | -238485.83 | 7757 | -60.530 | 100% quoted, 22289 trades |
| 2026-11-02 | 0.17587 | 0.1638 / 4.8 | -213774.08 | -214981.01 | 6481 | -68.289 | 100% quoted, 21236 trades |
| 2026-11-03 | 0.17789 | 0.1685 / 4.6 | -289788.58 | -290776.71 | 4728 | -167.134 | 100% quoted, 21070 trades |
| 2026-11-04 | 0.25177 | 0.1814 / 4.9 | -170576.85 | -171138.72 | 7509 | -67.500 | 100% quoted, 36246 trades |
| 2026-11-05 | 0.25532 | 0.1943 / 4.5 | -317181.76 | -318012.39 | 8369 | -108.458 | 100% quoted, 35897 trades |
