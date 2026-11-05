# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 23 (2026-10-02 to 2026-11-04)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -35038.89 [-45306.44, -25502.67] dollars (negative); 0 of 23 days positive; 3666 fills a day; 5 s markout -19.931 [-25.518, -15.572] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -35430.21 [-45782.28, -25776.67] dollars (negative); 0 of 23 days positive; 4142 fills a day; 5 s markout -18.158 [-23.188, -14.149] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -35772.84 [-45949.39, -26200.81] | negative | 0/23 | 3735 | -19.679 [-25.195, -15.360] |
| conservative | symmetric | 1 | -34966.56 [-48754.28, -23218.47] | negative | 1/23 | 3526 | -17.897 [-21.823, -14.266] |
| conservative | inventory | 2 | -35038.89 [-45306.44, -25502.67] | negative | 0/23 | 3666 | -19.931 [-25.518, -15.572] |
| conservative | symmetric | 2 | -34699.94 [-48417.71, -23045.97] | negative | 1/23 | 3423 | -18.268 [-22.297, -14.561] |
| conservative | inventory | 4 | -33010.55 [-43023.03, -23889.58] | negative | 0/23 | 3480 | -20.352 [-25.876, -15.981] |
| conservative | symmetric | 4 | -33943.11 [-47664.91, -22267.83] | negative | 1/23 | 3239 | -18.998 [-23.284, -15.107] |
| optimistic | inventory | 1 | -36122.23 [-46365.05, -26481.45] | negative | 0/23 | 4234 | -17.878 [-22.771, -13.943] |
| optimistic | symmetric | 1 | -34706.77 [-48802.35, -22681.40] | negative | 1/23 | 4038 | -16.004 [-19.364, -12.843] |
| optimistic | inventory | 2 | -35430.21 [-45782.28, -25776.67] | negative | 0/23 | 4142 | -18.158 [-23.188, -14.149] |
| optimistic | symmetric | 2 | -34319.48 [-48261.47, -22295.56] | negative | 1/23 | 3897 | -16.474 [-19.897, -13.208] |
| optimistic | inventory | 4 | -33440.18 [-43565.09, -24196.49] | negative | 0/23 | 3913 | -18.679 [-23.878, -14.578] |
| optimistic | symmetric | 4 | -33750.08 [-47480.59, -22118.91] | negative | 1/23 | 3659 | -17.363 [-21.180, -13.829] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -806.28 [-12003.98, 10232.45] | not established |
| conservative | 2 | -338.95 [-11469.79, 10839.77] | not established |
| conservative | 4 | 932.56 [-10795.42, 12681.36] | not established |
| optimistic | 1 | -1415.46 [-12712.32, 10041.49] | not established |
| optimistic | 2 | -1110.73 [-12519.90, 10653.93] | not established |
| optimistic | 4 | 309.90 [-11737.19, 12070.68] | not established |

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
