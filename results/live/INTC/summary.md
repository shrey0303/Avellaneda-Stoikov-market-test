# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 39 (2026-10-02 to 2026-11-27)
- Calibration-only days: 2; days without IEX data: 1

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -7916.29 [-10580.66, -5501.92] dollars (negative); 0 of 39 days positive; 1844 fills a day; 5 s markout -7.654 [-9.221, -6.202] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -7915.57 [-10711.66, -5435.98] dollars (negative); 0 of 39 days positive; 3032 fills a day; 5 s markout -5.575 [-6.828, -4.428] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -8317.95 [-10963.53, -5926.18] | negative | 0/39 | 1971 | -7.533 [-9.101, -6.074] |
| conservative | symmetric | 1 | -9015.45 [-12114.22, -6090.44] | negative | 3/39 | 1846 | -7.982 [-9.671, -6.436] |
| conservative | inventory | 2 | -7916.29 [-10580.66, -5501.92] | negative | 0/39 | 1844 | -7.654 [-9.221, -6.202] |
| conservative | symmetric | 2 | -8532.53 [-11535.93, -5633.71] | negative | 3/39 | 1625 | -8.558 [-10.292, -6.952] |
| conservative | inventory | 4 | -7388.53 [-9975.15, -5079.74] | negative | 0/39 | 1610 | -8.030 [-9.579, -6.550] |
| conservative | symmetric | 4 | -8036.93 [-10904.70, -5227.99] | negative | 5/39 | 1315 | -9.537 [-11.382, -7.795] |
| optimistic | inventory | 1 | -8280.31 [-11096.88, -5723.04] | negative | 0/39 | 3322 | -5.421 [-6.653, -4.289] |
| optimistic | symmetric | 1 | -9505.43 [-12880.42, -6302.71] | negative | 8/39 | 3136 | -5.760 [-7.077, -4.549] |
| optimistic | inventory | 2 | -7915.57 [-10711.66, -5435.98] | negative | 0/39 | 3032 | -5.575 [-6.828, -4.428] |
| optimistic | symmetric | 2 | -9131.02 [-12411.60, -6026.26] | negative | 5/39 | 2694 | -6.275 [-7.665, -5.005] |
| optimistic | inventory | 4 | -7446.86 [-10140.11, -5055.05] | negative | 0/39 | 2584 | -5.904 [-7.162, -4.728] |
| optimistic | symmetric | 4 | -8376.10 [-11393.63, -5408.81] | negative | 4/39 | 2101 | -7.143 [-8.638, -5.766] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 697.50 [-1282.20, 2553.00] | not established |
| conservative | 2 | 616.24 [-1400.94, 2508.84] | not established |
| conservative | 4 | 648.40 [-1352.77, 2451.17] | not established |
| optimistic | 1 | 1225.11 [-1054.83, 3405.73] | not established |
| optimistic | 2 | 1215.45 [-1067.84, 3381.52] | not established |
| optimistic | 4 | 929.24 [-1117.03, 2916.15] | not established |

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
| 2026-11-09 | 0.01771 | 0.2366 / 64.1 | -19074.41 | -19096.07 | 1426 | -17.939 | 100% quoted, 34942 trades |
| 2026-11-10 | 0.01974 | 0.2204 / 60.4 | -12935.55 | -13002.14 | 1172 | -11.930 | 100% quoted, 18547 trades |
| 2026-11-11 | 0.02133 | 0.2121 / 57.2 | -2454.87 | -2333.88 | 878 | -5.879 | 100% quoted, 31105 trades |
| 2026-11-12 | 0.02052 | 0.1898 / 56.7 | -4658.20 | -4385.59 | 778 | -9.005 | 100% quoted, 20404 trades |
| 2026-11-13 | 0.01928 | 0.1499 / 61.6 | -8514.15 | -8562.43 | 1055 | -12.647 | 100% quoted, 21216 trades |
| 2026-11-16 | 0.01955 | 0.1365 / 66.2 | -6490.01 | -6714.84 | 996 | -9.377 | 100% quoted, 23554 trades |
| 2026-11-17 | 0.01759 | 0.1291 / 68.1 | -3020.47 | -3196.08 | 1252 | -4.986 | 100% quoted, 31244 trades |
| 2026-11-18 | 0.01658 | 0.1449 / 74.3 | -6952.31 | -7020.16 | 1509 | -8.021 | 100% quoted, 25446 trades |
| 2026-11-19 | 0.01748 | 0.1481 / 72.7 | -11244.09 | -11322.24 | 2757 | -6.462 | 100% quoted, 40883 trades |
| 2026-11-20 | 0.01903 | 0.1711 / 69.1 | -4919.38 | -4206.42 | 3496 | -3.692 | 100% quoted, 63095 trades |
| 2026-11-23 | 0.01891 | 0.2224 / 70.2 | -3040.89 | -2860.51 | 1889 | -3.987 | 100% quoted, 37736 trades |
| 2026-11-24 | 0.01949 | 0.2447 / 71.8 | -3841.78 | -3335.34 | 1782 | -4.570 | 100% quoted, 31162 trades |
| 2026-11-25 | 0.01978 | 0.2472 / 70.6 | -2420.99 | -2110.24 | 1575 | -3.656 | 100% quoted, 31092 trades |
| 2026-11-26 | no IEX data |  |  |  |  |  |  |
| 2026-11-27 | 0.01965 | 0.2604 / 73.0 | -1566.00 | -1508.44 | 763 | -4.730 | 100% quoted, 15558 trades |
