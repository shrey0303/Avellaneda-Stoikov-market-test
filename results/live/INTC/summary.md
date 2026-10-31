# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 20 (2026-10-02 to 2026-10-30)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -9083.96 [-13816.60, -5103.01] dollars (negative); 0 of 20 days positive; 1915 fills a day; 5 s markout -8.386 [-10.820, -6.082] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -9250.64 [-14236.38, -5128.87] dollars (negative); 0 of 20 days positive; 3034 fills a day; 5 s markout -6.403 [-8.512, -4.428] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9394.80 [-14175.56, -5477.33] | negative | 0/20 | 2008 | -8.375 [-10.867, -6.031] |
| conservative | symmetric | 1 | -9747.88 [-14014.79, -5832.83] | negative | 0/20 | 1855 | -8.991 [-11.689, -6.443] |
| conservative | inventory | 2 | -9083.96 [-13816.60, -5103.01] | negative | 0/20 | 1915 | -8.386 [-10.820, -6.082] |
| conservative | symmetric | 2 | -9258.27 [-13534.77, -5364.35] | negative | 0/20 | 1673 | -9.433 [-12.183, -6.856] |
| conservative | inventory | 4 | -8559.96 [-13256.74, -4708.57] | negative | 0/20 | 1721 | -8.577 [-11.018, -6.290] |
| conservative | symmetric | 4 | -8704.43 [-12915.68, -4888.22] | negative | 1/20 | 1393 | -10.211 [-13.049, -7.544] |
| optimistic | inventory | 1 | -9576.77 [-14622.60, -5409.74] | negative | 0/20 | 3281 | -6.311 [-8.465, -4.300] |
| optimistic | symmetric | 1 | -10606.73 [-15172.85, -6349.82] | negative | 3/20 | 3073 | -6.760 [-9.035, -4.666] |
| optimistic | inventory | 2 | -9250.64 [-14236.38, -5128.87] | negative | 0/20 | 3034 | -6.403 [-8.512, -4.428] |
| optimistic | symmetric | 2 | -10032.97 [-14507.73, -5873.92] | negative | 0/20 | 2674 | -7.236 [-9.575, -5.067] |
| optimistic | inventory | 4 | -8787.01 [-13636.92, -4752.33] | negative | 0/20 | 2664 | -6.591 [-8.668, -4.601] |
| optimistic | symmetric | 4 | -9476.96 [-13893.88, -5451.23] | negative | 1/20 | 2143 | -7.999 [-10.450, -5.702] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 353.08 [-2571.18, 2552.08] | not established |
| conservative | 2 | 174.31 [-3045.22, 2432.80] | not established |
| conservative | 4 | 144.47 [-3068.86, 2489.25] | not established |
| optimistic | 1 | 1029.96 [-2057.33, 3614.40] | not established |
| optimistic | 2 | 782.33 [-2395.19, 3295.31] | not established |
| optimistic | 4 | 689.95 [-2587.25, 3254.76] | not established |

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
