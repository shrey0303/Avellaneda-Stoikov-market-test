# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 16 (2026-10-02 to 2026-10-26)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -10565.01 [-16077.40, -5650.72] dollars (negative); 0 of 16 days positive; 1845 fills a day; 5 s markout -9.558 [-12.180, -6.863] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -10844.22 [-16617.62, -5656.19] dollars (negative); 0 of 16 days positive; 2880 fills a day; 5 s markout -7.339 [-9.640, -5.024] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -10898.96 [-16383.81, -6042.56] | negative | 0/16 | 1907 | -9.567 [-12.215, -6.838] |
| conservative | symmetric | 1 | -11104.39 [-15967.86, -6610.72] | negative | 0/16 | 1750 | -10.274 [-13.163, -7.311] |
| conservative | inventory | 2 | -10565.01 [-16077.40, -5650.72] | negative | 0/16 | 1845 | -9.558 [-12.180, -6.863] |
| conservative | symmetric | 2 | -10529.11 [-15414.04, -6051.11] | negative | 0/16 | 1598 | -10.766 [-13.679, -7.786] |
| conservative | inventory | 4 | -10005.32 [-15408.38, -5208.09] | negative | 0/16 | 1694 | -9.761 [-12.395, -7.094] |
| conservative | symmetric | 4 | -10009.78 [-14716.64, -5790.10] | negative | 0/16 | 1365 | -11.629 [-14.664, -8.585] |
| optimistic | inventory | 1 | -11210.36 [-17022.09, -6076.09] | negative | 0/16 | 3071 | -7.247 [-9.587, -4.930] |
| optimistic | symmetric | 1 | -12068.75 [-17271.83, -7168.16] | negative | 2/16 | 2864 | -7.742 [-10.227, -5.300] |
| optimistic | inventory | 2 | -10844.22 [-16617.62, -5656.19] | negative | 0/16 | 2880 | -7.339 [-9.640, -5.024] |
| optimistic | symmetric | 2 | -11370.90 [-16431.08, -6538.23] | negative | 0/16 | 2517 | -8.269 [-10.832, -5.737] |
| optimistic | inventory | 4 | -10338.38 [-15941.60, -5305.20] | negative | 0/16 | 2573 | -7.540 [-9.836, -5.229] |
| optimistic | symmetric | 4 | -10811.86 [-15759.48, -6190.52] | negative | 0/16 | 2058 | -9.133 [-11.836, -6.428] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 205.44 [-3303.55, 2959.94] | not established |
| conservative | 2 | -35.90 [-3917.23, 2853.93] | not established |
| conservative | 4 | 4.47 [-3877.49, 2842.41] | not established |
| optimistic | 1 | 858.38 [-2821.01, 4097.77] | not established |
| optimistic | 2 | 526.69 [-3331.34, 3808.03] | not established |
| optimistic | 4 | 473.48 [-3350.16, 3691.88] | not established |

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
