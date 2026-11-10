# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 26 (2026-10-02 to 2026-11-09)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -9102.95 [-12627.81, -5846.17] dollars (negative); 0 of 26 days positive; 2000 fills a day; 5 s markout -8.060 [-10.196, -6.087] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -9159.57 [-12873.66, -5756.88] dollars (negative); 0 of 26 days positive; 3163 fills a day; 5 s markout -6.076 [-7.798, -4.460] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9560.01 [-13104.77, -6310.59] | negative | 0/26 | 2117 | -8.003 [-10.164, -6.011] |
| conservative | symmetric | 1 | -10603.36 [-14455.32, -7081.14] | negative | 0/26 | 1971 | -8.521 [-10.803, -6.369] |
| conservative | inventory | 2 | -9102.95 [-12627.81, -5846.17] | negative | 0/26 | 2000 | -8.060 [-10.196, -6.087] |
| conservative | symmetric | 2 | -10094.29 [-13888.62, -6529.23] | negative | 0/26 | 1761 | -9.024 [-11.436, -6.819] |
| conservative | inventory | 4 | -8484.45 [-11957.05, -5320.59] | negative | 0/26 | 1770 | -8.341 [-10.541, -6.358] |
| conservative | symmetric | 4 | -9430.77 [-13114.78, -6015.20] | negative | 1/26 | 1451 | -9.877 [-12.386, -7.557] |
| optimistic | inventory | 1 | -9609.59 [-13353.05, -6217.61] | negative | 0/26 | 3441 | -5.949 [-7.685, -4.324] |
| optimistic | symmetric | 1 | -11358.61 [-15312.22, -7638.56] | negative | 3/26 | 3238 | -6.347 [-8.195, -4.609] |
| optimistic | inventory | 2 | -9159.57 [-12873.66, -5756.88] | negative | 0/26 | 3163 | -6.076 [-7.798, -4.460] |
| optimistic | symmetric | 2 | -10819.67 [-14769.36, -7115.72] | negative | 0/26 | 2807 | -6.845 [-8.773, -5.041] |
| optimistic | inventory | 4 | -8611.59 [-12240.79, -5335.71] | negative | 0/26 | 2744 | -6.320 [-8.070, -4.697] |
| optimistic | symmetric | 4 | -9978.30 [-13683.29, -6431.37] | negative | 1/26 | 2227 | -7.650 [-9.725, -5.708] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1043.35 [-1146.89, 2941.15] | not established |
| conservative | 2 | 991.33 [-1455.77, 3080.75] | not established |
| conservative | 4 | 946.32 [-1530.91, 3072.83] | not established |
| optimistic | 1 | 1749.03 [-697.05, 3910.06] | not established |
| optimistic | 2 | 1660.09 [-827.14, 3836.61] | not established |
| optimistic | 4 | 1366.71 [-1027.67, 3563.48] | not established |

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
