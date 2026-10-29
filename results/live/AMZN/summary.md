# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 18 (2026-10-02 to 2026-10-28)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28840.56 [-40061.41, -19122.51] dollars (negative); 0 of 18 days positive; 2613 fills a day; 5 s markout -20.609 [-27.855, -15.324] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29241.48 [-40655.99, -19508.85] dollars (negative); 0 of 18 days positive; 3015 fills a day; 5 s markout -18.702 [-25.239, -13.873] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29291.38 [-40521.91, -19506.23] | negative | 0/18 | 2655 | -20.344 [-27.428, -15.139] |
| conservative | symmetric | 1 | -26645.45 [-37219.70, -17259.29] | negative | 1/18 | 2463 | -18.196 [-23.455, -13.994] |
| conservative | inventory | 2 | -28840.56 [-40061.41, -19122.51] | negative | 0/18 | 2613 | -20.609 [-27.855, -15.324] |
| conservative | symmetric | 2 | -26511.03 [-36993.58, -17287.54] | negative | 1/18 | 2372 | -18.635 [-24.003, -14.330] |
| conservative | inventory | 4 | -27577.14 [-38410.62, -18041.15] | negative | 0/18 | 2481 | -21.022 [-28.162, -15.734] |
| conservative | symmetric | 4 | -25867.57 [-36244.31, -16719.95] | negative | 1/18 | 2217 | -19.459 [-25.242, -14.898] |
| optimistic | inventory | 1 | -29583.95 [-40922.07, -19692.53] | negative | 0/18 | 3078 | -18.401 [-24.841, -13.661] |
| optimistic | symmetric | 1 | -25983.64 [-36515.68, -16386.14] | negative | 1/18 | 2915 | -16.099 [-20.532, -12.464] |
| optimistic | inventory | 2 | -29241.48 [-40655.99, -19508.85] | negative | 0/18 | 3015 | -18.702 [-25.239, -13.873] |
| optimistic | symmetric | 2 | -25840.21 [-36381.41, -16370.19] | negative | 1/18 | 2790 | -16.614 [-21.164, -12.904] |
| optimistic | inventory | 4 | -27956.22 [-38975.98, -18380.45] | negative | 0/18 | 2839 | -19.238 [-25.947, -14.288] |
| optimistic | symmetric | 4 | -25685.83 [-36236.70, -16271.94] | negative | 1/18 | 2577 | -17.623 [-22.745, -13.498] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2645.93 [-10427.42, 4296.90] | not established |
| conservative | 2 | -2329.53 [-10247.97, 4828.53] | not established |
| conservative | 4 | -1709.57 [-10373.29, 5679.76] | not established |
| optimistic | 1 | -3600.31 [-11632.24, 3749.70] | not established |
| optimistic | 2 | -3401.28 [-12015.35, 4434.32] | not established |
| optimistic | 4 | -2270.38 [-11604.16, 5563.63] | not established |

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
