# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 19 (2026-10-02 to 2026-10-29)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29070.00 [-39767.11, -19690.19] dollars (negative); 0 of 19 days positive; 2729 fills a day; 5 s markout -20.140 [-27.029, -15.031] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29452.81 [-40150.96, -20000.96] dollars (negative); 0 of 19 days positive; 3146 fills a day; 5 s markout -18.279 [-24.450, -13.644] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29658.88 [-40516.08, -20152.36] | negative | 0/19 | 2778 | -19.871 [-26.666, -14.832] |
| conservative | symmetric | 1 | -30870.04 [-44691.13, -19359.28] | negative | 1/19 | 2575 | -17.782 [-22.632, -13.781] |
| conservative | inventory | 2 | -29070.00 [-39767.11, -19690.19] | negative | 0/19 | 2729 | -20.140 [-27.029, -15.031] |
| conservative | symmetric | 2 | -30689.74 [-44411.56, -19314.12] | negative | 1/19 | 2481 | -18.206 [-23.185, -14.120] |
| conservative | inventory | 4 | -27587.11 [-38190.87, -18507.81] | negative | 0/19 | 2586 | -20.538 [-27.327, -15.456] |
| conservative | symmetric | 4 | -29995.59 [-43560.40, -18741.80] | negative | 1/19 | 2320 | -19.010 [-24.255, -14.668] |
| optimistic | inventory | 1 | -29938.41 [-40852.49, -20398.73] | negative | 0/19 | 3214 | -17.983 [-24.039, -13.429] |
| optimistic | symmetric | 1 | -30431.40 [-44421.77, -18419.84] | negative | 1/19 | 3041 | -15.751 [-19.995, -12.304] |
| optimistic | inventory | 2 | -29452.81 [-40150.96, -20000.96] | negative | 0/19 | 3146 | -18.279 [-24.450, -13.644] |
| optimistic | symmetric | 2 | -30155.65 [-43938.57, -18293.20] | negative | 1/19 | 2912 | -16.248 [-20.600, -12.709] |
| optimistic | inventory | 4 | -27980.40 [-38764.62, -18775.20] | negative | 0/19 | 2959 | -18.804 [-25.174, -14.051] |
| optimistic | symmetric | 4 | -29875.00 [-43622.71, -18293.19] | negative | 1/19 | 2694 | -17.225 [-21.977, -13.332] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1211.16 [-9002.57, 11701.93] | not established |
| conservative | 2 | 1619.74 [-8891.03, 12368.42] | not established |
| conservative | 4 | 2408.47 [-8660.66, 13525.86] | not established |
| optimistic | 1 | 493.00 [-10231.84, 11549.14] | not established |
| optimistic | 2 | 702.85 [-10536.79, 11793.95] | not established |
| optimistic | 4 | 1894.61 [-9564.61, 13197.93] | not established |

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
| 2026-10-20 | 0.05308 | 0.1344 / 24.0 | -24917.59 | -25198.38 | 2796 | -16.793 | 100% quoted, 20750 trades |
| 2026-10-21 | 0.04994 | 0.1445 / 24.0 | -18910.46 | -19371.50 | 2459 | -15.609 | 100% quoted, 13131 trades |
| 2026-10-22 | 0.03676 | 0.1408 / 23.5 | -47417.76 | -47814.34 | 3312 | -20.338 | 100% quoted, 24341 trades |
| 2026-10-23 | 0.04230 | 0.1550 / 23.2 | -34309.42 | -34632.51 | 2085 | -27.441 | 100% quoted, 12733 trades |
| 2026-10-26 | 0.04882 | 0.1436 / 23.2 | -90904.54 | -91001.72 | 3620 | -36.779 | 100% quoted, 15344 trades |
| 2026-10-27 | 0.06421 | 0.1397 / 23.8 | -2355.69 | -2845.93 | 1586 | -7.489 | 100% quoted, 14019 trades |
| 2026-10-28 | 0.06301 | 0.1374 / 25.0 | -12322.61 | -12392.73 | 2319 | -12.269 | 100% quoted, 15892 trades |
| 2026-10-29 | 0.06212 | 0.1421 / 25.5 | -33199.81 | -33256.64 | 4815 | -11.706 | 100% quoted, 31345 trades |
