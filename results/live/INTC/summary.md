# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 29 (2026-10-02 to 2026-11-12)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -8852.60 [-12347.40, -5880.25] dollars (negative); 0 of 29 days positive; 1891 fills a day; 5 s markout -8.151 [-10.149, -6.401] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -8892.09 [-12532.99, -5804.13] dollars (negative); 0 of 29 days positive; 3011 fills a day; 5 s markout -6.069 [-7.706, -4.633] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9284.48 [-12730.11, -6246.91] | negative | 0/29 | 2001 | -8.068 [-10.050, -6.288] |
| conservative | symmetric | 1 | -10462.04 [-14069.98, -6883.48] | negative | 1/29 | 1864 | -8.595 [-10.712, -6.687] |
| conservative | inventory | 2 | -8852.60 [-12347.40, -5880.25] | negative | 0/29 | 1891 | -8.151 [-10.149, -6.401] |
| conservative | symmetric | 2 | -9982.47 [-13552.61, -6460.29] | negative | 1/29 | 1663 | -9.154 [-11.349, -7.188] |
| conservative | inventory | 4 | -8260.55 [-11643.94, -5386.37] | negative | 0/29 | 1672 | -8.500 [-10.484, -6.700] |
| conservative | symmetric | 4 | -9456.21 [-12974.22, -5993.32] | negative | 2/29 | 1369 | -10.091 [-12.381, -7.993] |
| optimistic | inventory | 1 | -9323.88 [-12993.07, -6147.17] | negative | 0/29 | 3279 | -5.912 [-7.557, -4.482] |
| optimistic | symmetric | 1 | -11149.16 [-15007.33, -7329.98] | negative | 4/29 | 3084 | -6.311 [-8.033, -4.779] |
| optimistic | inventory | 2 | -8892.09 [-12532.99, -5804.13] | negative | 0/29 | 3011 | -6.069 [-7.706, -4.633] |
| optimistic | symmetric | 2 | -10718.32 [-14446.38, -7045.24] | negative | 1/29 | 2668 | -6.843 [-8.651, -5.260] |
| optimistic | inventory | 4 | -8380.36 [-11905.14, -5351.81] | negative | 0/29 | 2605 | -6.372 [-8.029, -4.929] |
| optimistic | symmetric | 4 | -9968.90 [-13492.32, -6427.59] | negative | 2/29 | 2112 | -7.711 [-9.616, -5.997] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1177.56 [-1160.40, 3382.50] | not established |
| conservative | 2 | 1129.87 [-1332.22, 3377.70] | not established |
| conservative | 4 | 1195.66 [-1308.20, 3475.21] | not established |
| optimistic | 1 | 1825.27 [-689.53, 4262.02] | not established |
| optimistic | 2 | 1826.24 [-675.62, 4234.34] | not established |
| optimistic | 4 | 1588.55 [-910.56, 3920.22] | not established |

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
