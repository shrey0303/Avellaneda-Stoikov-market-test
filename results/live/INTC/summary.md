# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 17 (2026-10-02 to 2026-10-27)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -10038.28 [-15261.99, -5405.81] dollars (negative); 0 of 17 days positive; 1807 fills a day; 5 s markout -9.203 [-11.866, -6.625] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -10289.94 [-15771.81, -5416.20] dollars (negative); 0 of 17 days positive; 2841 fills a day; 5 s markout -7.047 [-9.405, -4.804] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -10359.38 [-15557.80, -5746.58] | negative | 0/17 | 1871 | -9.203 [-11.908, -6.566] |
| conservative | symmetric | 1 | -10470.47 [-15254.41, -6239.52] | negative | 0/17 | 1720 | -9.882 [-12.848, -7.030] |
| conservative | inventory | 2 | -10038.28 [-15261.99, -5405.81] | negative | 0/17 | 1807 | -9.203 [-11.866, -6.625] |
| conservative | symmetric | 2 | -9936.16 [-14601.25, -5671.54] | negative | 0/17 | 1566 | -10.362 [-13.349, -7.476] |
| conservative | inventory | 4 | -9501.37 [-14573.53, -4940.30] | negative | 0/17 | 1653 | -9.390 [-12.021, -6.793] |
| conservative | symmetric | 4 | -9418.64 [-14008.51, -5256.99] | negative | 1/17 | 1330 | -11.209 [-14.251, -8.258] |
| optimistic | inventory | 1 | -10636.52 [-16121.10, -5749.08] | negative | 0/17 | 3040 | -6.957 [-9.358, -4.709] |
| optimistic | symmetric | 1 | -11328.97 [-16471.59, -6557.69] | negative | 3/17 | 2835 | -7.441 [-9.947, -5.076] |
| optimistic | inventory | 2 | -10289.94 [-15771.81, -5416.20] | negative | 0/17 | 2841 | -7.047 [-9.405, -4.804] |
| optimistic | symmetric | 2 | -10713.45 [-15833.02, -6129.17] | negative | 0/17 | 2484 | -7.951 [-10.551, -5.483] |
| optimistic | inventory | 4 | -9806.79 [-15082.61, -5037.18] | negative | 0/17 | 2528 | -7.251 [-9.589, -5.018] |
| optimistic | symmetric | 4 | -10067.24 [-14996.57, -5531.59] | negative | 1/17 | 2022 | -8.780 [-11.485, -6.203] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 111.09 [-3243.20, 2607.17] | not established |
| conservative | 2 | -102.12 [-3767.77, 2469.48] | not established |
| conservative | 4 | -82.73 [-3712.57, 2479.73] | not established |
| optimistic | 1 | 692.45 [-2913.14, 3636.72] | not established |
| optimistic | 2 | 423.51 [-3317.74, 3291.74] | not established |
| optimistic | 4 | 260.45 [-3450.55, 3141.38] | not established |

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
