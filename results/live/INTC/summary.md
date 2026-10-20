# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 11 (2026-10-02 to 2026-10-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -14278.51 [-20415.40, -8326.73] dollars (negative); 0 of 11 days positive; 2026 fills a day; 5 s markout -12.007 [-14.745, -9.129] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -14807.97 [-21139.77, -8572.94] dollars (negative); 0 of 11 days positive; 2929 fills a day; 5 s markout -9.310 [-11.799, -6.678] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -14624.74 [-20626.13, -8726.14] | negative | 0/11 | 2062 | -12.015 [-14.857, -9.030] |
| conservative | symmetric | 1 | -14300.90 [-20181.50, -8735.93] | negative | 0/11 | 1873 | -12.941 [-16.049, -9.734] |
| conservative | inventory | 2 | -14278.51 [-20415.40, -8326.73] | negative | 0/11 | 2026 | -12.007 [-14.745, -9.129] |
| conservative | symmetric | 2 | -13667.18 [-19618.48, -8095.42] | negative | 0/11 | 1754 | -13.489 [-16.648, -10.288] |
| conservative | inventory | 4 | -13603.20 [-19617.12, -7704.13] | negative | 0/11 | 1922 | -12.165 [-14.944, -9.256] |
| conservative | symmetric | 4 | -12962.07 [-18748.00, -7538.36] | negative | 0/11 | 1571 | -14.435 [-17.523, -11.172] |
| optimistic | inventory | 1 | -15213.85 [-21520.06, -9056.75] | negative | 0/11 | 3055 | -9.220 [-11.786, -6.547] |
| optimistic | symmetric | 1 | -15504.77 [-21427.26, -9629.73] | negative | 1/11 | 2822 | -9.841 [-12.542, -7.046] |
| optimistic | inventory | 2 | -14807.97 [-21139.77, -8572.94] | negative | 0/11 | 2929 | -9.310 [-11.799, -6.678] |
| optimistic | symmetric | 2 | -14860.93 [-20894.02, -8930.66] | negative | 0/11 | 2558 | -10.467 [-13.273, -7.599] |
| optimistic | inventory | 4 | -14151.44 [-20414.87, -7972.21] | negative | 0/11 | 2718 | -9.538 [-11.983, -6.955] |
| optimistic | symmetric | 4 | -14234.84 [-20110.32, -8531.85] | negative | 0/11 | 2197 | -11.482 [-14.455, -8.492] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -323.84 [-5182.35, 3484.89] | not established |
| conservative | 2 | -611.32 [-5887.85, 3385.68] | not established |
| conservative | 4 | -641.13 [-5872.07, 3277.69] | not established |
| optimistic | 1 | 290.93 [-4855.29, 4634.85] | not established |
| optimistic | 2 | 52.96 [-5209.15, 4520.22] | not established |
| optimistic | 4 | 83.41 [-5262.86, 4466.37] | not established |

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
