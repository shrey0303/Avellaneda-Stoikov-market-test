# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 17 (2026-10-02 to 2026-10-27)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29812.21 [-41355.28, -19485.72] dollars (negative); 0 of 17 days positive; 2631 fills a day; 5 s markout -21.100 [-27.864, -15.336] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -30232.59 [-41906.17, -19800.10] dollars (negative); 0 of 17 days positive; 3029 fills a day; 5 s markout -19.150 [-25.236, -13.891] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -30260.22 [-41882.49, -19938.96] | negative | 0/17 | 2668 | -20.851 [-27.560, -15.208] |
| conservative | symmetric | 1 | -26981.51 [-38240.95, -17184.71] | negative | 1/17 | 2476 | -18.580 [-23.669, -14.070] |
| conservative | inventory | 2 | -29812.21 [-41355.28, -19485.72] | negative | 0/17 | 2631 | -21.100 [-27.864, -15.336] |
| conservative | symmetric | 2 | -26866.83 [-38169.61, -17161.44] | negative | 1/17 | 2384 | -19.020 [-24.194, -14.397] |
| conservative | inventory | 4 | -28511.92 [-39736.04, -18420.04] | negative | 0/17 | 2501 | -21.502 [-28.213, -15.771] |
| conservative | symmetric | 4 | -26228.93 [-37286.78, -16662.26] | negative | 1/17 | 2230 | -19.873 [-25.262, -15.011] |
| optimistic | inventory | 1 | -30579.13 [-42259.39, -20134.75] | negative | 0/17 | 3087 | -18.851 [-24.872, -13.743] |
| optimistic | symmetric | 1 | -26405.54 [-37511.71, -16421.96] | negative | 1/17 | 2926 | -16.435 [-20.815, -12.496] |
| optimistic | inventory | 2 | -30232.59 [-41906.17, -19800.10] | negative | 0/17 | 3029 | -19.150 [-25.236, -13.891] |
| optimistic | symmetric | 2 | -26243.08 [-37480.36, -16354.22] | negative | 1/17 | 2801 | -16.954 [-21.452, -12.920] |
| optimistic | inventory | 4 | -28907.14 [-40293.42, -18669.07] | negative | 0/17 | 2855 | -19.689 [-25.988, -14.296] |
| optimistic | symmetric | 4 | -26084.86 [-37345.80, -16253.33] | negative | 1/17 | 2589 | -17.990 [-22.893, -13.571] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -3278.72 [-11192.07, 4370.81] | not established |
| conservative | 2 | -2945.38 [-11325.63, 5058.32] | not established |
| conservative | 4 | -2282.99 [-11161.29, 5811.47] | not established |
| optimistic | 1 | -4173.59 [-12438.55, 4021.55] | not established |
| optimistic | 2 | -3989.50 [-12903.56, 4706.54] | not established |
| optimistic | 4 | -2822.28 [-12164.91, 6043.26] | not established |

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
