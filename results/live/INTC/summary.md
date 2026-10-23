# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 14 (2026-10-02 to 2026-10-22)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -11644.99 [-17226.91, -6384.52] dollars (negative); 0 of 14 days positive; 1913 fills a day; 5 s markout -10.315 [-12.989, -7.537] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -12003.72 [-17893.68, -6469.52] dollars (negative); 0 of 14 days positive; 2935 fills a day; 5 s markout -7.946 [-10.296, -5.571] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -11956.43 [-17460.98, -6690.63] | negative | 0/14 | 1968 | -10.305 [-13.025, -7.468] |
| conservative | symmetric | 1 | -12039.64 [-17190.77, -7396.00] | negative | 0/14 | 1804 | -11.063 [-14.073, -7.981] |
| conservative | inventory | 2 | -11644.99 [-17226.91, -6384.52] | negative | 0/14 | 1913 | -10.315 [-12.989, -7.537] |
| conservative | symmetric | 2 | -11398.39 [-16544.39, -6715.82] | negative | 0/14 | 1658 | -11.547 [-14.597, -8.410] |
| conservative | inventory | 4 | -11058.10 [-16493.93, -5916.72] | negative | 0/14 | 1775 | -10.478 [-13.151, -7.761] |
| conservative | symmetric | 4 | -10923.24 [-15907.90, -6487.73] | negative | 0/14 | 1437 | -12.399 [-15.527, -9.191] |
| optimistic | inventory | 1 | -12367.06 [-18202.50, -6876.73] | negative | 0/14 | 3114 | -7.851 [-10.254, -5.453] |
| optimistic | symmetric | 1 | -13043.26 [-18524.76, -7986.56] | negative | 2/14 | 2906 | -8.374 [-10.913, -5.816] |
| optimistic | inventory | 2 | -12003.72 [-17893.68, -6469.52] | negative | 0/14 | 2935 | -7.946 [-10.296, -5.571] |
| optimistic | symmetric | 2 | -12418.08 [-17842.21, -7447.09] | negative | 0/14 | 2569 | -8.926 [-11.564, -6.281] |
| optimistic | inventory | 4 | -11469.48 [-17188.18, -6071.79] | negative | 0/14 | 2650 | -8.152 [-10.481, -5.781] |
| optimistic | symmetric | 4 | -11835.74 [-17050.28, -7080.67] | negative | 0/14 | 2130 | -9.814 [-12.572, -7.002] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 83.21 [-3921.86, 3190.03] | not established |
| conservative | 2 | -246.60 [-4599.01, 2979.22] | not established |
| conservative | 4 | -134.86 [-4345.34, 2954.46] | not established |
| optimistic | 1 | 676.21 [-3432.26, 4361.69] | not established |
| optimistic | 2 | 414.36 [-3866.96, 4060.38] | not established |
| optimistic | 4 | 366.26 [-4002.55, 3933.64] | not established |

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
