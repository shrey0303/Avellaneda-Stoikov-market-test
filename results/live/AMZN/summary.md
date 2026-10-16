# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 10 (2026-10-02 to 2026-10-16)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -25190.13 [-37291.84, -14205.65] dollars (negative); 0 of 10 days positive; 2497 fills a day; 5 s markout -21.154 [-32.536, -13.227] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -25615.40 [-38130.24, -14428.19] dollars (negative); 0 of 10 days positive; 2901 fills a day; 5 s markout -19.074 [-29.213, -11.936] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -25684.31 [-37477.35, -14938.03] | negative | 0/10 | 2523 | -20.907 [-32.120, -13.147] |
| conservative | symmetric | 1 | -23353.01 [-35460.71, -13184.22] | negative | 0/10 | 2332 | -18.298 [-25.381, -13.056] |
| conservative | inventory | 2 | -25190.13 [-37291.84, -14205.65] | negative | 0/10 | 2497 | -21.154 [-32.536, -13.227] |
| conservative | symmetric | 2 | -23241.45 [-35328.66, -13193.61] | negative | 0/10 | 2247 | -18.805 [-26.138, -13.380] |
| conservative | inventory | 4 | -24452.11 [-37875.59, -13191.59] | negative | 0/10 | 2383 | -21.424 [-32.605, -13.630] |
| conservative | symmetric | 4 | -22671.07 [-34344.37, -12868.23] | negative | 0/10 | 2102 | -19.693 [-27.635, -13.923] |
| optimistic | inventory | 1 | -25949.55 [-38025.99, -15047.33] | negative | 0/10 | 2952 | -18.750 [-28.677, -11.792] |
| optimistic | symmetric | 1 | -23617.41 [-36123.31, -13271.97] | negative | 0/10 | 2768 | -15.956 [-21.838, -11.569] |
| optimistic | inventory | 2 | -25615.40 [-38130.24, -14428.19] | negative | 0/10 | 2901 | -19.074 [-29.213, -11.936] |
| optimistic | symmetric | 2 | -23134.27 [-35542.26, -12705.03] | negative | 0/10 | 2650 | -16.516 [-22.544, -11.970] |
| optimistic | inventory | 4 | -24829.54 [-38596.02, -13339.02] | negative | 0/10 | 2736 | -19.669 [-30.070, -12.336] |
| optimistic | symmetric | 4 | -22629.71 [-34844.02, -12556.74] | negative | 0/10 | 2454 | -17.561 [-24.480, -12.496] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2331.29 [-14520.01, 8439.36] | not established |
| conservative | 2 | -1948.68 [-14925.18, 9351.18] | not established |
| conservative | 4 | -1781.04 [-15906.52, 9926.96] | not established |
| optimistic | 1 | -2332.14 [-14431.69, 8835.25] | not established |
| optimistic | 2 | -2481.13 [-16036.46, 9673.25] | not established |
| optimistic | 4 | -2199.84 [-17371.88, 10370.48] | not established |

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
