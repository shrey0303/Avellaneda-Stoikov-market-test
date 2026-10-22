# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 13 (2026-10-02 to 2026-10-21)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -25524.63 [-36244.30, -16911.19] dollars (negative); 0 of 13 days positive; 2625 fills a day; 5 s markout -20.511 [-29.450, -14.586] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -25973.81 [-36967.15, -17150.74] dollars (negative); 0 of 13 days positive; 3020 fills a day; 5 s markout -18.571 [-26.545, -13.188] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -25941.20 [-36323.84, -17745.80] | negative | 0/13 | 2651 | -20.290 [-29.132, -14.473] |
| conservative | symmetric | 1 | -25085.43 [-35554.74, -16133.51] | negative | 0/13 | 2460 | -17.638 [-23.381, -13.703] |
| conservative | inventory | 2 | -25524.63 [-36244.30, -16911.19] | negative | 0/13 | 2625 | -20.511 [-29.450, -14.586] |
| conservative | symmetric | 2 | -24921.51 [-35460.14, -16064.86] | negative | 0/13 | 2372 | -18.099 [-23.968, -14.047] |
| conservative | inventory | 4 | -24683.38 [-35991.94, -15641.92] | negative | 0/13 | 2507 | -20.824 [-29.553, -14.975] |
| conservative | symmetric | 4 | -24317.15 [-34540.10, -15683.78] | negative | 0/13 | 2223 | -18.915 [-25.151, -14.653] |
| optimistic | inventory | 1 | -26229.66 [-36805.35, -17815.92] | negative | 0/13 | 3068 | -18.293 [-26.067, -13.058] |
| optimistic | symmetric | 1 | -25350.20 [-35967.93, -16283.50] | negative | 0/13 | 2896 | -15.527 [-20.197, -12.215] |
| optimistic | inventory | 2 | -25973.81 [-36967.15, -17150.74] | negative | 0/13 | 3020 | -18.571 [-26.545, -13.188] |
| optimistic | symmetric | 2 | -24976.40 [-35546.73, -15837.30] | negative | 0/13 | 2776 | -16.046 [-20.863, -12.638] |
| optimistic | inventory | 4 | -25092.43 [-36652.39, -15865.73] | negative | 0/13 | 2861 | -19.091 [-27.290, -13.627] |
| optimistic | symmetric | 4 | -24370.34 [-34766.64, -15424.10] | negative | 0/13 | 2572 | -17.016 [-22.538, -13.249] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -855.78 [-10908.29, 7786.57] | not established |
| conservative | 2 | -603.12 [-11061.76, 8286.44] | not established |
| conservative | 4 | -366.24 [-11974.21, 9020.83] | not established |
| optimistic | 1 | -879.46 [-11112.92, 8137.79] | not established |
| optimistic | 2 | -997.41 [-12229.83, 8761.55] | not established |
| optimistic | 4 | -722.10 [-13194.99, 9438.33] | not established |

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
