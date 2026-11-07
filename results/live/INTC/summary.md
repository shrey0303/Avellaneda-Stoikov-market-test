# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 25 (2026-10-02 to 2026-11-06)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -8704.10 [-12405.52, -5459.71] dollars (negative); 0 of 25 days positive; 2023 fills a day; 5 s markout -7.665 [-9.758, -5.800] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -8762.11 [-12625.18, -5339.94] dollars (negative); 0 of 25 days positive; 3199 fills a day; 5 s markout -5.837 [-7.597, -4.310] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9181.56 [-12939.80, -5918.15] | negative | 0/25 | 2142 | -7.624 [-9.750, -5.735] |
| conservative | symmetric | 1 | -10070.93 [-13992.29, -6600.63] | negative | 0/25 | 1994 | -8.164 [-10.490, -6.097] |
| conservative | inventory | 2 | -8704.10 [-12405.52, -5459.71] | negative | 0/25 | 2023 | -7.665 [-9.758, -5.800] |
| conservative | symmetric | 2 | -9559.22 [-13573.25, -6091.94] | negative | 0/25 | 1783 | -8.602 [-10.980, -6.477] |
| conservative | inventory | 4 | -8082.30 [-11693.80, -4916.45] | negative | 0/25 | 1790 | -7.901 [-9.993, -6.025] |
| conservative | symmetric | 4 | -8949.15 [-12812.41, -5618.29] | negative | 1/25 | 1467 | -9.371 [-11.823, -7.157] |
| optimistic | inventory | 1 | -9231.92 [-13161.39, -5789.72] | negative | 0/25 | 3480 | -5.737 [-7.502, -4.170] |
| optimistic | symmetric | 1 | -10835.29 [-14891.25, -6997.89] | negative | 3/25 | 3279 | -6.124 [-8.032, -4.463] |
| optimistic | inventory | 2 | -8762.11 [-12625.18, -5339.94] | negative | 0/25 | 3199 | -5.837 [-7.597, -4.310] |
| optimistic | symmetric | 2 | -10295.88 [-14305.50, -6630.13] | negative | 0/25 | 2844 | -6.581 [-8.569, -4.834] |
| optimistic | inventory | 4 | -8209.95 [-11936.42, -4870.13] | negative | 0/25 | 2775 | -6.047 [-7.819, -4.508] |
| optimistic | symmetric | 4 | -9478.35 [-13373.20, -6050.32] | negative | 1/25 | 2255 | -7.321 [-9.463, -5.482] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 889.37 [-1340.12, 2812.04] | not established |
| conservative | 2 | 855.13 [-1652.72, 2941.27] | not established |
| conservative | 4 | 866.85 [-1663.49, 3035.04] | not established |
| optimistic | 1 | 1603.37 [-816.15, 3902.04] | not established |
| optimistic | 2 | 1533.77 [-1034.50, 3811.34] | not established |
| optimistic | 4 | 1268.40 [-1184.29, 3433.00] | not established |

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
| 2026-11-04 | 0.01610 | 0.2286 / 78.3 | -5783.48 | -4897.26 | 2543 | -4.088 | 100% quoted, 54552 trades |
| 2026-11-05 | 0.01619 | 0.2514 / 76.2 | -14416.90 | -13728.45 | 4820 | -5.340 | 100% quoted, 64980 trades |
| 2026-11-06 | 0.01775 | 0.2829 / 67.4 | -11962.36 | -11880.82 | 2222 | -7.070 | 100% quoted, 38853 trades |
