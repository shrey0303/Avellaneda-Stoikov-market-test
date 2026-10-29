# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 18 (2026-10-02 to 2026-10-28)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -9570.04 [-14462.04, -5110.97] dollars (negative); 0 of 18 days positive; 1785 fills a day; 5 s markout -8.904 [-11.373, -6.394] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -9801.00 [-14919.06, -5087.53] dollars (negative); 0 of 18 days positive; 2826 fills a day; 5 s markout -6.809 [-9.011, -4.664] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9875.06 [-14722.19, -5379.98] | negative | 0/18 | 1854 | -8.902 [-11.400, -6.345] |
| conservative | symmetric | 1 | -10119.63 [-14737.97, -5673.96] | negative | 0/18 | 1704 | -9.551 [-12.264, -6.755] |
| conservative | inventory | 2 | -9570.04 [-14462.04, -5110.97] | negative | 0/18 | 1785 | -8.904 [-11.373, -6.394] |
| conservative | symmetric | 2 | -9539.90 [-14085.56, -5138.48] | negative | 0/18 | 1548 | -10.017 [-12.759, -7.188] |
| conservative | inventory | 4 | -9057.56 [-13822.72, -4681.89] | negative | 0/18 | 1625 | -9.089 [-11.545, -6.577] |
| conservative | symmetric | 4 | -8947.39 [-13401.10, -4723.34] | negative | 1/18 | 1306 | -10.845 [-13.635, -7.980] |
| optimistic | inventory | 1 | -10118.74 [-15215.14, -5351.87] | negative | 0/18 | 3033 | -6.722 [-8.945, -4.540] |
| optimistic | symmetric | 1 | -10997.50 [-15700.26, -6151.05] | negative | 3/18 | 2830 | -7.192 [-9.527, -4.897] |
| optimistic | inventory | 2 | -9801.00 [-14919.06, -5087.53] | negative | 0/18 | 2826 | -6.809 [-9.011, -4.664] |
| optimistic | symmetric | 2 | -10358.02 [-15078.16, -5709.65] | negative | 0/18 | 2472 | -7.687 [-10.116, -5.314] |
| optimistic | inventory | 4 | -9337.89 [-14326.00, -4745.73] | negative | 0/18 | 2505 | -7.001 [-9.188, -4.843] |
| optimistic | symmetric | 4 | -9637.84 [-14241.22, -5141.92] | negative | 1/18 | 1999 | -8.488 [-11.005, -5.971] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 244.57 [-2918.83, 2530.07] | not established |
| conservative | 2 | -30.14 [-3462.39, 2410.31] | not established |
| conservative | 4 | -110.17 [-3418.39, 2313.01] | not established |
| optimistic | 1 | 878.76 [-2460.09, 3635.08] | not established |
| optimistic | 2 | 557.02 [-2880.15, 3243.93] | not established |
| optimistic | 4 | 299.95 [-3149.51, 2915.21] | not established |

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
