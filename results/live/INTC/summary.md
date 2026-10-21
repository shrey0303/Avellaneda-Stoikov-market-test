# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 12 (2026-10-02 to 2026-10-20)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -13246.79 [-19115.88, -7320.57] dollars (negative); 0 of 12 days positive; 1990 fills a day; 5 s markout -11.318 [-14.129, -8.372] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -13686.61 [-19751.58, -7465.25] dollars (negative); 0 of 12 days positive; 2936 fills a day; 5 s markout -8.780 [-11.283, -6.216] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -13577.21 [-19443.11, -7683.70] | negative | 0/12 | 2034 | -11.326 [-14.203, -8.301] |
| conservative | symmetric | 1 | -13168.64 [-18863.85, -7588.56] | negative | 0/12 | 1852 | -12.194 [-15.379, -8.932] |
| conservative | inventory | 2 | -13246.79 [-19115.88, -7320.57] | negative | 0/12 | 1990 | -11.318 [-14.129, -8.372] |
| conservative | symmetric | 2 | -12563.64 [-18225.34, -7102.26] | negative | 0/12 | 1724 | -12.703 [-15.928, -9.384] |
| conservative | inventory | 4 | -12598.85 [-18281.68, -6808.32] | negative | 0/12 | 1870 | -11.475 [-14.247, -8.523] |
| conservative | symmetric | 4 | -12090.54 [-17595.08, -6814.64] | negative | 0/12 | 1525 | -13.604 [-16.877, -10.177] |
| optimistic | inventory | 1 | -14090.42 [-20140.49, -7882.77] | negative | 0/12 | 3081 | -8.686 [-11.226, -6.083] |
| optimistic | symmetric | 1 | -14167.01 [-20142.99, -8142.14] | negative | 2/12 | 2861 | -9.274 [-12.041, -6.520] |
| optimistic | inventory | 2 | -13686.61 [-19751.58, -7465.25] | negative | 0/12 | 2936 | -8.780 [-11.283, -6.216] |
| optimistic | symmetric | 2 | -13677.19 [-19694.31, -7716.34] | negative | 0/12 | 2569 | -9.863 [-12.722, -7.020] |
| optimistic | inventory | 4 | -13081.35 [-18947.31, -7014.39] | negative | 0/12 | 2691 | -8.997 [-11.517, -6.457] |
| optimistic | symmetric | 4 | -13145.02 [-18797.48, -7465.70] | negative | 0/12 | 2176 | -10.831 [-13.856, -7.861] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -408.57 [-4793.92, 3118.62] | not established |
| conservative | 2 | -683.15 [-5546.64, 3002.80] | not established |
| conservative | 4 | -508.31 [-5251.36, 3040.89] | not established |
| optimistic | 1 | 76.60 [-4723.49, 4282.63] | not established |
| optimistic | 2 | -9.42 [-4926.69, 4156.10] | not established |
| optimistic | 4 | 63.67 [-4886.64, 4154.80] | not established |

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
