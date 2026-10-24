# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 15 (2026-10-02 to 2026-10-23)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -10989.00 [-16501.97, -6069.80] dollars (negative); 0 of 15 days positive; 1866 fills a day; 5 s markout -9.868 [-12.663, -7.175] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -11319.20 [-17071.11, -6141.16] dollars (negative); 0 of 15 days positive; 2885 fills a day; 5 s markout -7.599 [-10.007, -5.348] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -11315.47 [-16847.79, -6430.22] | negative | 0/15 | 1925 | -9.878 [-12.718, -7.163] |
| conservative | symmetric | 1 | -11420.41 [-16551.79, -6761.78] | negative | 0/15 | 1766 | -10.606 [-13.700, -7.650] |
| conservative | inventory | 2 | -10989.00 [-16501.97, -6069.80] | negative | 0/15 | 1866 | -9.868 [-12.663, -7.175] |
| conservative | symmetric | 2 | -10845.38 [-16053.91, -6166.81] | negative | 0/15 | 1618 | -11.089 [-14.234, -8.088] |
| conservative | inventory | 4 | -10426.13 [-15766.91, -5644.53] | negative | 0/15 | 1725 | -10.048 [-12.852, -7.368] |
| conservative | symmetric | 4 | -10444.28 [-15491.73, -5979.97] | negative | 0/15 | 1395 | -11.917 [-15.111, -8.816] |
| optimistic | inventory | 1 | -11685.17 [-17451.20, -6514.30] | negative | 0/15 | 3067 | -7.510 [-9.955, -5.234] |
| optimistic | symmetric | 1 | -12265.11 [-17850.87, -7121.57] | negative | 2/15 | 2862 | -8.013 [-10.570, -5.563] |
| optimistic | inventory | 2 | -11319.20 [-17071.11, -6141.16] | negative | 0/15 | 2885 | -7.599 [-10.007, -5.348] |
| optimistic | symmetric | 2 | -11680.12 [-17144.52, -6724.26] | negative | 0/15 | 2525 | -8.551 [-11.219, -6.030] |
| optimistic | inventory | 4 | -10808.20 [-16386.49, -5807.94] | negative | 0/15 | 2592 | -7.800 [-10.177, -5.510] |
| optimistic | symmetric | 4 | -11257.80 [-16476.62, -6512.84] | negative | 0/15 | 2081 | -9.418 [-12.243, -6.739] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 104.94 [-3515.19, 3049.02] | not established |
| conservative | 2 | -143.62 [-4185.55, 2923.69] | not established |
| conservative | 4 | 18.16 [-3937.52, 3049.90] | not established |
| optimistic | 1 | 579.94 [-3296.39, 4017.43] | not established |
| optimistic | 2 | 360.91 [-3689.05, 3730.64] | not established |
| optimistic | 4 | 449.60 [-3583.14, 3798.72] | not established |

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
