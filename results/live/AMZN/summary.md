# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 16 (2026-10-02 to 2026-10-26)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -31528.24 [-43757.22, -21327.06] dollars (negative); 0 of 16 days positive; 2696 fills a day; 5 s markout -21.950 [-28.738, -16.284] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -31944.25 [-44159.46, -21568.14] dollars (negative); 0 of 16 days positive; 3091 fills a day; 5 s markout -19.937 [-26.013, -14.798] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -32060.73 [-44222.20, -21859.49] | negative | 0/16 | 2730 | -21.690 [-28.433, -16.099] |
| conservative | symmetric | 1 | -28927.13 [-40372.77, -19504.32] | negative | 0/16 | 2526 | -19.303 [-24.263, -14.925] |
| conservative | inventory | 2 | -31528.24 [-43757.22, -21327.06] | negative | 0/16 | 2696 | -21.950 [-28.738, -16.284] |
| conservative | symmetric | 2 | -28783.21 [-40100.41, -19476.86] | negative | 0/16 | 2434 | -19.763 [-24.826, -15.301] |
| conservative | inventory | 4 | -30138.77 [-42016.09, -19911.89] | negative | 0/16 | 2569 | -22.366 [-29.067, -16.685] |
| conservative | symmetric | 4 | -28187.09 [-39466.73, -19016.26] | negative | 0/16 | 2279 | -20.655 [-25.956, -15.932] |
| optimistic | inventory | 1 | -32368.12 [-44615.22, -22115.87] | negative | 0/16 | 3145 | -19.626 [-25.597, -14.584] |
| optimistic | symmetric | 1 | -28550.20 [-39883.65, -18937.33] | negative | 0/16 | 2975 | -17.089 [-21.320, -13.341] |
| optimistic | inventory | 2 | -31944.25 [-44159.46, -21568.14] | negative | 0/16 | 3091 | -19.937 [-26.013, -14.798] |
| optimistic | symmetric | 2 | -28305.36 [-39733.39, -18730.68] | negative | 0/16 | 2850 | -17.622 [-21.964, -13.775] |
| optimistic | inventory | 4 | -30549.29 [-42581.72, -20169.65] | negative | 0/16 | 2921 | -20.501 [-26.758, -15.176] |
| optimistic | symmetric | 4 | -28063.28 [-39464.02, -18547.16] | negative | 0/16 | 2638 | -18.699 [-23.455, -14.445] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -3133.60 [-11412.89, 4612.76] | not established |
| conservative | 2 | -2745.03 [-11419.36, 5206.80] | not established |
| conservative | 4 | -1951.68 [-11436.84, 6403.29] | not established |
| optimistic | 1 | -3817.92 [-12649.35, 4522.78] | not established |
| optimistic | 2 | -3638.90 [-13211.21, 5304.53] | not established |
| optimistic | 4 | -2486.01 [-12827.17, 6553.31] | not established |

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
