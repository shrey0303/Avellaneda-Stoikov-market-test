# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 20 (2026-10-02 to 2026-10-30)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -31155.66 [-42168.01, -21306.25] dollars (negative); 0 of 20 days positive; 3155 fills a day; 5 s markout -19.736 [-26.550, -14.969] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -31569.89 [-42710.59, -21602.13] dollars (negative); 0 of 20 days positive; 3590 fills a day; 5 s markout -17.937 [-24.020, -13.592] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -31808.92 [-42900.05, -22151.49] | negative | 0/20 | 3226 | -19.452 [-26.181, -14.727] |
| conservative | symmetric | 1 | -35447.37 [-51926.11, -22738.29] | negative | 1/20 | 3043 | -17.411 [-22.195, -13.749] |
| conservative | inventory | 2 | -31155.66 [-42168.01, -21306.25] | negative | 0/20 | 3155 | -19.736 [-26.550, -14.969] |
| conservative | symmetric | 2 | -35170.15 [-51451.53, -22619.69] | negative | 1/20 | 2944 | -17.816 [-22.725, -14.066] |
| conservative | inventory | 4 | -29429.54 [-40292.67, -20012.18] | negative | 0/20 | 2980 | -20.137 [-26.791, -15.400] |
| conservative | symmetric | 4 | -34467.77 [-50688.34, -22039.62] | negative | 1/20 | 2772 | -18.594 [-23.840, -14.605] |
| optimistic | inventory | 1 | -32115.07 [-43449.32, -22271.23] | negative | 0/20 | 3681 | -17.632 [-23.597, -13.390] |
| optimistic | symmetric | 1 | -35055.29 [-51914.07, -22052.81] | negative | 1/20 | 3526 | -15.458 [-19.497, -12.280] |
| optimistic | inventory | 2 | -31569.89 [-42710.59, -21602.13] | negative | 0/20 | 3590 | -17.937 [-24.020, -13.592] |
| optimistic | symmetric | 2 | -34742.91 [-51535.13, -21838.58] | negative | 1/20 | 3391 | -15.938 [-20.105, -12.668] |
| optimistic | inventory | 4 | -29856.97 [-40833.77, -20287.30] | negative | 0/20 | 3376 | -18.458 [-24.693, -14.036] |
| optimistic | symmetric | 4 | -34333.10 [-50637.14, -21745.74] | negative | 1/20 | 3164 | -16.878 [-21.569, -13.270] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3638.45 [-6644.19, 14416.50] | not established |
| conservative | 2 | 4014.49 [-6547.69, 14983.48] | not established |
| conservative | 4 | 5038.23 [-6263.48, 16764.19] | not established |
| optimistic | 1 | 2940.22 [-7445.79, 14343.93] | not established |
| optimistic | 2 | 3173.02 [-8007.02, 14943.44] | not established |
| optimistic | 4 | 4476.14 [-7205.93, 16662.29] | not established |

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
