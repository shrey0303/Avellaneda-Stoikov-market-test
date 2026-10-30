# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 19 (2026-10-02 to 2026-10-29)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -9180.85 [-13743.63, -4957.69] dollars (negative); 0 of 19 days positive; 1755 fills a day; 5 s markout -8.624 [-11.097, -6.157] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -9383.99 [-14201.34, -4961.15] dollars (negative); 0 of 19 days positive; 2801 fills a day; 5 s markout -6.583 [-8.678, -4.532] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -9492.34 [-14105.43, -5276.90] | negative | 0/19 | 1828 | -8.622 [-11.126, -6.141] |
| conservative | symmetric | 1 | -9700.24 [-13952.79, -5466.31] | negative | 0/19 | 1682 | -9.254 [-11.980, -6.579] |
| conservative | inventory | 2 | -9180.85 [-13743.63, -4957.69] | negative | 0/19 | 1755 | -8.624 [-11.097, -6.157] |
| conservative | symmetric | 2 | -9127.75 [-13375.48, -4915.29] | negative | 0/19 | 1523 | -9.703 [-12.464, -6.958] |
| conservative | inventory | 4 | -8667.78 [-13166.97, -4589.58] | negative | 0/19 | 1592 | -8.815 [-11.310, -6.400] |
| conservative | symmetric | 4 | -8480.00 [-12671.87, -4313.26] | negative | 1/19 | 1279 | -10.498 [-13.403, -7.650] |
| optimistic | inventory | 1 | -9705.11 [-14526.44, -5243.82] | negative | 0/19 | 3019 | -6.496 [-8.603, -4.435] |
| optimistic | symmetric | 1 | -10666.85 [-15226.72, -6149.20] | negative | 3/19 | 2816 | -6.952 [-9.182, -4.788] |
| optimistic | inventory | 2 | -9383.99 [-14201.34, -4961.15] | negative | 0/19 | 2801 | -6.583 [-8.678, -4.532] |
| optimistic | symmetric | 2 | -9999.38 [-14466.01, -5560.68] | negative | 0/19 | 2451 | -7.440 [-9.766, -5.197] |
| optimistic | inventory | 4 | -8930.96 [-13613.76, -4659.08] | negative | 0/19 | 2473 | -6.769 [-8.857, -4.721] |
| optimistic | symmetric | 4 | -9259.46 [-13578.27, -4996.33] | negative | 1/19 | 1972 | -8.218 [-10.680, -5.825] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 207.90 [-2883.35, 2455.24] | not established |
| conservative | 2 | -53.10 [-3373.11, 2300.32] | not established |
| conservative | 4 | -187.78 [-3438.89, 2112.57] | not established |
| optimistic | 1 | 961.74 [-2431.84, 3603.91] | not established |
| optimistic | 2 | 615.39 [-2883.30, 3175.55] | not established |
| optimistic | 4 | 328.50 [-3101.57, 2852.30] | not established |

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
