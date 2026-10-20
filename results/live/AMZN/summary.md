# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 11 (2026-10-02 to 2026-10-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26181.10 [-38232.87, -15657.40] dollars (negative); 0 of 11 days positive; 2624 fills a day; 5 s markout -21.295 [-32.239, -14.042] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26644.51 [-39002.93, -15889.42] dollars (negative); 0 of 11 days positive; 3028 fills a day; 5 s markout -19.243 [-28.982, -12.679] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -26570.40 [-38028.42, -16211.89] | negative | 0/11 | 2655 | -21.032 [-31.780, -13.904] |
| conservative | symmetric | 1 | -24264.01 [-36419.86, -14756.35] | negative | 0/11 | 2475 | -18.198 [-24.952, -13.338] |
| conservative | inventory | 2 | -26181.10 [-38232.87, -15657.40] | negative | 0/11 | 2624 | -21.295 [-32.239, -14.042] |
| conservative | symmetric | 2 | -24134.85 [-36186.41, -14711.33] | negative | 0/11 | 2386 | -18.705 [-25.714, -13.717] |
| conservative | inventory | 4 | -25388.73 [-38376.39, -14556.44] | negative | 0/11 | 2506 | -21.551 [-32.256, -14.399] |
| conservative | symmetric | 4 | -23517.73 [-35194.23, -14282.00] | negative | 0/11 | 2235 | -19.571 [-27.090, -14.335] |
| optimistic | inventory | 1 | -26821.37 [-38454.00, -16350.55] | negative | 0/11 | 3084 | -18.903 [-28.453, -12.490] |
| optimistic | symmetric | 1 | -24517.85 [-37115.07, -14725.24] | negative | 0/11 | 2916 | -15.942 [-21.414, -11.869] |
| optimistic | inventory | 2 | -26644.51 [-39002.93, -15889.42] | negative | 0/11 | 3028 | -19.243 [-28.982, -12.679] |
| optimistic | symmetric | 2 | -23981.70 [-36391.83, -14270.78] | negative | 0/11 | 2795 | -16.477 [-22.085, -12.241] |
| optimistic | inventory | 4 | -25751.13 [-39059.08, -14727.57] | negative | 0/11 | 2862 | -19.787 [-29.832, -13.012] |
| optimistic | symmetric | 4 | -23464.58 [-35580.78, -14062.38] | negative | 0/11 | 2594 | -17.490 [-23.953, -12.848] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2306.39 [-14161.47, 7632.68] | not established |
| conservative | 2 | -2046.25 [-14479.61, 8402.98] | not established |
| conservative | 4 | -1871.00 [-15680.45, 8939.87] | not established |
| optimistic | 1 | -2303.53 [-14155.11, 8157.68] | not established |
| optimistic | 2 | -2662.81 [-15658.87, 8671.02] | not established |
| optimistic | 4 | -2286.55 [-16976.84, 9552.83] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.05668 | 0.1233 / 27.9 | -30045.81 | -30079.37 | 2367 | -29.095 | 100% quoted, 13756 trades |
| 2026-10-05 | 0.04825 | 0.1181 / 27.1 | -20339.61 | -20764.35 | 3271 | -13.002 | 100% quoted, 15058 trades |
| 2026-10-06 | 0.04333 | 0.1204 / 23.8 | -9806.57 | -9785.46 | 1742 | -12.999 | 100% quoted, 15857 trades |
| 2026-10-07 | 0.04001 | 0.1208 / 25.4 | -10714.98 | -10932.95 | 2557 | -11.542 | 100% quoted, 13432 trades |
| 2026-10-08 | 0.03757 | 0.1203 / 24.6 | -57570.03 | -58213.54 | 3770 | -25.776 | 100% quoted, 18135 trades |
| 2026-10-09 | 0.04527 | 0.1247 / 23.0 | -18458.69 | -18608.94 | 2452 | -14.765 | 100% quoted, 12249 trades |
| 2026-10-12 | 0.04566 | 0.1223 / 21.8 | -11862.88 | -12733.79 | 1762 | -15.701 | 100% quoted, 11529 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.04917 | 0.1128 / 21.9 | -67220.40 | -69167.13 | 2365 | -66.562 | 100% quoted, 14568 trades |
| 2026-10-15 | 0.06091 | 0.1144 / 22.8 | -10732.59 | -10506.59 | 1935 | -10.823 | 100% quoted, 15912 trades |
| 2026-10-16 | 0.05059 | 0.1108 / 24.4 | -15149.75 | -15361.85 | 2753 | -11.274 | 100% quoted, 19489 trades |
| 2026-10-19 | 0.04950 | 0.1238 / 25.8 | -36090.78 | -36935.65 | 3890 | -22.708 | 100% quoted, 20463 trades |
