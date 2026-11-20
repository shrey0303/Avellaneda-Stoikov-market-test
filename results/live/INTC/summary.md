# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 34 (2026-10-02 to 2026-11-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -8616.07 [-11585.07, -5982.14] dollars (negative); 0 of 34 days positive; 1835 fills a day; 5 s markout -8.173 [-9.861, -6.610] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -8667.24 [-11789.73, -5938.66] dollars (negative); 0 of 34 days positive; 2979 fills a day; 5 s markout -5.951 [-7.306, -4.732] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9031.30 [-11984.10, -6366.12] | negative | 0/34 | 1948 | -8.058 [-9.754, -6.510] |
| conservative | symmetric | 1 | -9614.96 [-13275.37, -6353.44] | negative | 3/34 | 1811 | -8.539 [-10.368, -6.880] |
| conservative | inventory | 2 | -8616.07 [-11585.07, -5982.14] | negative | 0/34 | 1835 | -8.173 [-9.861, -6.610] |
| conservative | symmetric | 2 | -9102.90 [-12713.08, -5897.92] | negative | 3/34 | 1609 | -9.147 [-11.044, -7.409] |
| conservative | inventory | 4 | -8067.40 [-10966.06, -5536.67] | negative | 0/34 | 1618 | -8.566 [-10.269, -6.957] |
| conservative | symmetric | 4 | -8639.45 [-12030.05, -5579.50] | negative | 4/34 | 1316 | -10.192 [-12.191, -8.343] |
| optimistic | inventory | 1 | -9057.10 [-12165.42, -6268.18] | negative | 0/34 | 3253 | -5.783 [-7.150, -4.576] |
| optimistic | symmetric | 1 | -10093.74 [-14045.10, -6386.14] | negative | 8/34 | 3059 | -6.147 [-7.610, -4.846] |
| optimistic | inventory | 2 | -8667.24 [-11789.73, -5938.66] | negative | 0/34 | 2979 | -5.951 [-7.306, -4.732] |
| optimistic | symmetric | 2 | -9705.73 [-13583.10, -6202.88] | negative | 4/34 | 2636 | -6.690 [-8.218, -5.325] |
| optimistic | inventory | 4 | -8167.07 [-11174.58, -5501.94] | negative | 0/34 | 2560 | -6.301 [-7.678, -5.039] |
| optimistic | symmetric | 4 | -9031.96 [-12650.08, -5784.09] | negative | 4/34 | 2072 | -7.610 [-9.269, -6.126] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 583.66 [-1682.17, 2781.08] | not established |
| conservative | 2 | 486.83 [-1870.20, 2634.95] | not established |
| conservative | 4 | 572.05 [-1742.93, 2641.12] | not established |
| optimistic | 1 | 1036.65 [-1621.08, 3578.82] | not established |
| optimistic | 2 | 1038.48 [-1529.00, 3571.58] | not established |
| optimistic | 4 | 864.89 [-1563.07, 3100.98] | not established |

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
