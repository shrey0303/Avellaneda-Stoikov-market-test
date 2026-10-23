# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 14 (2026-10-02 to 2026-10-22)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27088.42 [-37232.84, -18781.20] dollars (negative); 0 of 14 days positive; 2674 fills a day; 5 s markout -20.499 [-28.831, -14.882] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -27533.85 [-38016.14, -19048.20] dollars (negative); 0 of 14 days positive; 3083 fills a day; 5 s markout -18.527 [-25.940, -13.448] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27447.75 [-37244.34, -19430.12] | negative | 0/14 | 2712 | -20.220 [-28.315, -14.703] |
| conservative | symmetric | 1 | -24838.46 [-34261.45, -16902.47] | negative | 0/14 | 2547 | -17.323 [-22.546, -13.548] |
| conservative | inventory | 2 | -27088.42 [-37232.84, -18781.20] | negative | 0/14 | 2674 | -20.499 [-28.831, -14.882] |
| conservative | symmetric | 2 | -24764.43 [-34200.02, -16962.16] | negative | 0/14 | 2454 | -17.764 [-23.126, -13.876] |
| conservative | inventory | 4 | -26312.72 [-37394.69, -17531.02] | negative | 0/14 | 2546 | -20.871 [-29.122, -15.307] |
| conservative | symmetric | 4 | -24179.46 [-33344.92, -16578.61] | negative | 0/14 | 2294 | -18.577 [-24.376, -14.481] |
| optimistic | inventory | 1 | -27717.84 [-37674.76, -19672.43] | negative | 0/14 | 3142 | -18.213 [-25.443, -13.254] |
| optimistic | symmetric | 1 | -24541.04 [-34123.64, -16500.79] | negative | 0/14 | 3013 | -15.266 [-19.588, -12.141] |
| optimistic | inventory | 2 | -27533.85 [-38016.14, -19048.20] | negative | 0/14 | 3083 | -18.527 [-25.940, -13.448] |
| optimistic | symmetric | 2 | -24258.02 [-33880.05, -16179.98] | negative | 0/14 | 2883 | -15.768 [-20.202, -12.541] |
| optimistic | inventory | 4 | -26700.78 [-37967.91, -17783.20] | negative | 0/14 | 2912 | -19.085 [-26.758, -13.868] |
| optimistic | symmetric | 4 | -23935.23 [-33323.80, -16067.25] | negative | 0/14 | 2668 | -16.719 [-21.766, -13.140] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2609.29 [-12585.78, 6011.69] | not established |
| conservative | 2 | -2323.99 [-12749.45, 6620.27] | not established |
| conservative | 4 | -2133.27 [-13449.08, 7314.13] | not established |
| optimistic | 1 | -3176.80 [-13535.56, 5998.22] | not established |
| optimistic | 2 | -3275.82 [-14610.51, 6437.44] | not established |
| optimistic | 4 | -2765.55 [-14790.33, 7322.34] | not established |

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
