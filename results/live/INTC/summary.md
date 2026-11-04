# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 22 (2026-10-02 to 2026-11-03)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -8429.08 [-12776.94, -4823.32] dollars (negative); 0 of 22 days positive; 1863 fills a day; 5 s markout -7.961 [-10.310, -5.757] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -8570.29 [-13143.53, -4758.88] dollars (negative); 0 of 22 days positive; 2973 fills a day; 5 s markout -6.074 [-8.019, -4.250] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -8737.10 [-13084.66, -5082.82] | negative | 0/22 | 1959 | -7.946 [-10.319, -5.714] |
| conservative | symmetric | 1 | -9059.66 [-12952.65, -5587.92] | negative | 0/22 | 1810 | -8.500 [-11.083, -6.046] |
| conservative | inventory | 2 | -8429.08 [-12776.94, -4823.32] | negative | 0/22 | 1863 | -7.961 [-10.310, -5.757] |
| conservative | symmetric | 2 | -8611.23 [-12400.51, -5149.78] | negative | 0/22 | 1622 | -8.934 [-11.579, -6.465] |
| conservative | inventory | 4 | -7916.05 [-12183.34, -4394.55] | negative | 0/22 | 1661 | -8.165 [-10.481, -5.975] |
| conservative | symmetric | 4 | -8085.57 [-11853.04, -4758.37] | negative | 1/22 | 1339 | -9.689 [-12.388, -7.153] |
| optimistic | inventory | 1 | -8886.24 [-13521.82, -5005.95] | negative | 0/22 | 3223 | -5.980 [-7.951, -4.143] |
| optimistic | symmetric | 1 | -9839.76 [-14050.86, -6046.52] | negative | 3/22 | 3020 | -6.384 [-8.489, -4.431] |
| optimistic | inventory | 2 | -8570.29 [-13143.53, -4758.88] | negative | 0/22 | 2973 | -6.074 [-8.019, -4.250] |
| optimistic | symmetric | 2 | -9329.33 [-13419.73, -5646.01] | negative | 0/22 | 2614 | -6.843 [-9.020, -4.809] |
| optimistic | inventory | 4 | -8120.53 [-12615.90, -4416.44] | negative | 0/22 | 2589 | -6.260 [-8.196, -4.437] |
| optimistic | symmetric | 4 | -8809.78 [-12824.96, -5258.27] | negative | 1/22 | 2079 | -7.581 [-9.913, -5.417] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 322.56 [-2167.34, 2323.55] | not established |
| conservative | 2 | 182.16 [-2556.95, 2258.85] | not established |
| conservative | 4 | 169.52 [-2547.46, 2319.75] | not established |
| optimistic | 1 | 953.53 [-1726.27, 3373.43] | not established |
| optimistic | 2 | 759.05 [-1978.53, 3125.81] | not established |
| optimistic | 4 | 689.24 [-2016.05, 3112.48] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.03676 | 0.2096 / 37.8 | -28953.32 | -29533.70 | 3512 | -14.048 | 100% quoted, 20263 trades |
| 2026-10-05 | 0.03458 | 0.1827 / 31.7 | -17982.03 | -18514.21 | 1813 | -16.001 | 100% quoted, 20854 trades |
| 2026-10-06 | 0.03036 | 0.1596 / 32.3 | -27199.84 | -28277.24 | 3107 | -16.738 | 100% quoted, 22050 trades |
| 2026-10-07 | 0.03001 | 0.1545 / 29.8 | -27924.08 | -29077.36 | 2894 | -16.887 | 100% quoted, 17100 trades |
| 2026-10-08 | 0.02992 | 0.1466 / 28.0 | -23440.90 | -24950.76 | 3028 | -15.149 | 100% quoted, 31296 trades |
| 2026-10-09 | 0.02858 | 0.1431 / 27.1 | -7686.91 | -8454.60 | 955 | -17.342 | 100% quoted, 26508 trades |
| 2026-10-12 | 0.02711 | 0.1370 / 30.3 | -1917.16 | -2162.12 | 416 | -10.779 | 100% quoted, 23043 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.02428 | 0.1408 / 41.0 | -4865.53 | -4946.51 | 1074 | -8.365 | 100% quoted, 29449 trades |
| 2026-10-15 | 0.02192 | 0.1576 / 52.1 | -11353.03 | -11755.31 | 2895 | -7.699 | 100% quoted, 36726 trades |
| 2026-10-16 | 0.01975 | 0.1645 / 58.1 | -2421.01 | -2074.86 | 1261 | -3.846 | 100% quoted, 29908 trades |
| 2026-10-19 | 0.01801 | 0.1773 / 63.7 | -3319.80 | -3140.96 | 1329 | -5.225 | 100% quoted, 29649 trades |
| 2026-10-20 | 0.01869 | 0.1856 / 64.1 | -1897.85 | -1351.64 | 1595 | -3.741 | 100% quoted, 32079 trades |
| 2026-10-21 | 0.01889 | 0.1903 / 66.1 | -3012.00 | -3003.82 | 1399 | -5.246 | 100% quoted, 31948 trades |
| 2026-10-22 | 0.01853 | 0.1862 / 67.3 | -1056.44 | -808.99 | 1498 | -3.340 | 100% quoted, 43100 trades |
| 2026-10-23 | 0.01691 | 0.1965 / 80.5 | -1805.13 | -1736.00 | 1219 | -3.620 | 100% quoted, 19398 trades |
| 2026-10-26 | 0.01655 | 0.1805 / 79.5 | -4205.08 | -3719.41 | 1527 | -4.902 | 100% quoted, 27865 trades |
| 2026-10-27 | 0.01603 | 0.1811 / 80.2 | -1610.63 | -1421.46 | 1201 | -3.529 | 100% quoted, 29939 trades |
| 2026-10-28 | 0.01554 | 0.1746 / 81.5 | -1609.92 | -1489.04 | 1402 | -3.809 | 100% quoted, 25497 trades |
| 2026-10-29 | 0.01587 | 0.1719 / 83.1 | -2175.55 | -1877.81 | 1219 | -3.584 | 100% quoted, 25844 trades |
| 2026-10-30 | 0.01603 | 0.1566 / 82.0 | -7243.08 | -6716.97 | 4953 | -3.866 | 100% quoted, 124834 trades |
| 2026-11-02 | 0.01702 | 0.2122 / 75.7 | -1921.44 | -1951.75 | 1723 | -3.155 | 100% quoted, 66803 trades |
| 2026-11-03 | 0.01661 | 0.2270 / 77.3 | -1838.92 | -1581.84 | 969 | -4.262 | 100% quoted, 36165 trades |
