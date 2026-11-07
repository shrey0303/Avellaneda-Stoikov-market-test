# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 25 (2026-10-02 to 2026-11-06)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -40642.16 [-55339.70, -28829.54] dollars (negative); 0 of 25 days positive; 4134 fills a day; 5 s markout -20.463 [-25.329, -16.417] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -41083.60 [-55918.46, -29232.83] dollars (negative); 0 of 25 days positive; 4626 fills a day; 5 s markout -18.749 [-23.123, -15.079] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -41590.03 [-57079.09, -29442.54] | negative | 0/25 | 4190 | -20.227 [-25.029, -16.172] |
| conservative | symmetric | 1 | -41012.40 [-60823.59, -26091.40] | negative | 1/25 | 3944 | -18.452 [-21.986, -15.155] |
| conservative | inventory | 2 | -40642.16 [-55339.70, -28829.54] | negative | 0/25 | 4134 | -20.463 [-25.329, -16.417] |
| conservative | symmetric | 2 | -40561.53 [-59813.73, -26035.97] | negative | 1/25 | 3838 | -18.811 [-22.437, -15.442] |
| conservative | inventory | 4 | -38156.57 [-51417.12, -27070.26] | negative | 0/25 | 3936 | -20.888 [-25.686, -16.868] |
| conservative | symmetric | 4 | -39608.48 [-58483.37, -25475.32] | negative | 1/25 | 3645 | -19.524 [-23.356, -15.995] |
| optimistic | inventory | 1 | -42056.01 [-57800.18, -29772.62] | negative | 0/25 | 4708 | -18.488 [-22.804, -14.848] |
| optimistic | symmetric | 1 | -40779.63 [-60918.64, -25971.87] | negative | 1/25 | 4475 | -16.605 [-19.672, -13.608] |
| optimistic | inventory | 2 | -41083.60 [-55918.46, -29232.83] | negative | 0/25 | 4626 | -18.749 [-23.123, -15.079] |
| optimistic | symmetric | 2 | -40407.49 [-60390.15, -25524.81] | negative | 1/25 | 4332 | -17.066 [-20.188, -14.012] |
| optimistic | inventory | 4 | -38630.42 [-52065.71, -27459.40] | negative | 0/25 | 4385 | -19.268 [-23.785, -15.518] |
| optimistic | symmetric | 4 | -39620.81 [-58949.82, -25047.39] | negative | 1/25 | 4084 | -17.927 [-21.354, -14.728] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -577.63 [-10233.49, 9732.50] | not established |
| conservative | 2 | -80.63 [-9734.12, 10336.31] | not established |
| conservative | 4 | 1451.91 [-8690.44, 12744.69] | not established |
| optimistic | 1 | -1276.38 [-11206.18, 9358.46] | not established |
| optimistic | 2 | -676.12 [-10725.28, 10450.67] | not established |
| optimistic | 4 | 990.39 [-9455.42, 12661.66] | not established |

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
| 2026-10-30 | 0.05934 | 0.1436 / 24.0 | -70783.23 | -71794.47 | 11239 | -12.058 | 100% quoted, 50453 trades |
| 2026-11-02 | 0.05710 | 0.1800 / 17.5 | -65898.51 | -65656.50 | 5321 | -26.406 | 100% quoted, 31068 trades |
| 2026-11-03 | 0.04176 | 0.2007 / 17.5 | -41274.73 | -41827.52 | 5517 | -15.282 | 100% quoted, 26165 trades |
| 2026-11-04 | 0.04536 | 0.2131 / 15.7 | -75608.12 | -76012.90 | 10381 | -22.008 | 100% quoted, 56429 trades |
| 2026-11-05 | 0.04901 | 0.2505 / 14.7 | -148320.19 | -149109.64 | 12638 | -23.798 | 100% quoted, 53782 trades |
| 2026-11-06 | 0.05962 | 0.2812 / 12.8 | -61839.32 | -63085.67 | 6392 | -29.351 | 100% quoted, 25611 trades |
