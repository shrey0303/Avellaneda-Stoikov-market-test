# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 9 (2026-10-02 to 2026-10-15)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26305.73 [-40121.38, -14383.76] dollars (negative); 0 of 9 days positive; 2469 fills a day; 5 s markout -22.251 [-34.568, -13.818] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26754.68 [-40879.17, -14641.23] dollars (negative); 0 of 9 days positive; 2856 fills a day; 5 s markout -20.063 [-31.024, -12.428] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -26868.38 [-40408.32, -15067.15] | negative | 0/9 | 2494 | -21.980 [-34.037, -13.677] |
| conservative | symmetric | 1 | -24971.00 [-37985.78, -14099.48] | negative | 0/9 | 2294 | -19.136 [-26.666, -13.476] |
| conservative | inventory | 2 | -26305.73 [-40121.38, -14383.76] | negative | 0/9 | 2469 | -22.251 [-34.568, -13.818] |
| conservative | symmetric | 2 | -24864.02 [-38002.74, -14238.94] | negative | 0/9 | 2213 | -19.661 [-27.460, -13.801] |
| conservative | inventory | 4 | -25613.03 [-40698.29, -13175.02] | negative | 0/9 | 2358 | -22.531 [-34.635, -14.133] |
| conservative | symmetric | 4 | -24205.47 [-36950.32, -13712.63] | negative | 0/9 | 2075 | -20.589 [-29.017, -14.470] |
| optimistic | inventory | 1 | -27117.37 [-40870.78, -15104.58] | negative | 0/9 | 2900 | -19.747 [-30.400, -12.303] |
| optimistic | symmetric | 1 | -25221.91 [-38443.09, -14033.37] | negative | 0/9 | 2712 | -16.667 [-22.852, -11.919] |
| optimistic | inventory | 2 | -26754.68 [-40879.17, -14641.23] | negative | 0/9 | 2856 | -20.063 [-31.024, -12.428] |
| optimistic | symmetric | 2 | -24842.74 [-38094.00, -13703.56] | negative | 0/9 | 2600 | -17.255 [-23.611, -12.363] |
| optimistic | inventory | 4 | -26007.84 [-41549.06, -13396.42] | negative | 0/9 | 2700 | -20.702 [-31.987, -12.847] |
| optimistic | symmetric | 4 | -24321.48 [-37360.29, -13649.71] | negative | 0/9 | 2415 | -18.363 [-25.622, -12.966] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -1897.38 [-15826.85, 9990.91] | not established |
| conservative | 2 | -1441.71 [-16034.89, 11099.17] | not established |
| conservative | 4 | -1407.56 [-17712.53, 11765.84] | not established |
| optimistic | 1 | -1895.46 [-15928.41, 10870.47] | not established |
| optimistic | 2 | -1911.94 [-17490.79, 11698.12] | not established |
| optimistic | 4 | -1686.35 [-19187.85, 12606.24] | not established |

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
