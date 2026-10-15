# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 9 (2026-10-02 to 2026-10-15)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27982.98 [-47614.97, -15484.94] dollars (negative); 0 of 9 days positive; 2418 fills a day; 5 s markout -25.216 [-30.008, -20.522] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28517.02 [-48257.04, -16031.04] dollars (negative); 0 of 9 days positive; 2521 fills a day; 5 s markout -24.723 [-29.454, -20.026] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29364.95 [-52895.73, -14487.72] | negative | 0/9 | 2419 | -25.045 [-29.824, -20.355] |
| conservative | symmetric | 1 | -34063.80 [-65241.21, -13166.82] | negative | 0/9 | 2409 | -24.240 [-28.880, -19.565] |
| conservative | inventory | 2 | -27982.98 [-47614.97, -15484.94] | negative | 0/9 | 2418 | -25.216 [-30.008, -20.522] |
| conservative | symmetric | 2 | -33829.34 [-64895.96, -13031.67] | negative | 0/9 | 2386 | -24.335 [-28.950, -19.622] |
| conservative | inventory | 4 | -26037.41 [-41240.17, -16029.43] | negative | 0/9 | 2361 | -25.709 [-30.537, -20.996] |
| conservative | symmetric | 4 | -33217.36 [-64332.59, -12474.69] | negative | 0/9 | 2346 | -24.516 [-29.091, -19.898] |
| optimistic | inventory | 1 | -29712.25 [-53302.60, -14827.23] | negative | 0/9 | 2523 | -24.562 [-29.406, -19.821] |
| optimistic | symmetric | 1 | -34401.43 [-65932.93, -13140.61] | negative | 0/9 | 2497 | -23.829 [-28.464, -19.255] |
| optimistic | inventory | 2 | -28517.02 [-48257.04, -16031.04] | negative | 0/9 | 2521 | -24.723 [-29.454, -20.026] |
| optimistic | symmetric | 2 | -34079.45 [-65449.09, -13006.78] | negative | 0/9 | 2474 | -23.926 [-28.545, -19.317] |
| optimistic | inventory | 4 | -26413.41 [-41582.87, -16328.24] | negative | 0/9 | 2466 | -25.253 [-30.068, -20.527] |
| optimistic | symmetric | 4 | -33510.71 [-64719.62, -12719.82] | negative | 0/9 | 2429 | -24.095 [-28.693, -19.484] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4698.86 [-2195.57, 12789.45] | not established |
| conservative | 2 | 5846.36 [-4004.13, 18034.36] | not established |
| conservative | 4 | 7179.95 [-5543.62, 23942.97] | not established |
| optimistic | 1 | 4689.18 [-2578.61, 13163.09] | not established |
| optimistic | 2 | 5562.43 [-4714.01, 17998.69] | not established |
| optimistic | 4 | 7097.30 [-5700.70, 23916.36] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.06399 | 0.1467 / 15.3 | -11239.88 | -11388.79 | 2611 | -14.894 | 100% quoted, 6767 trades |
| 2026-10-05 | 0.06162 | 0.1095 / 12.5 | -22660.49 | -22799.99 | 2604 | -17.254 | 100% quoted, 9105 trades |
| 2026-10-06 | 0.05802 | 0.1063 / 11.7 | -15860.42 | -16278.82 | 2137 | -16.669 | 100% quoted, 5468 trades |
| 2026-10-07 | 0.05532 | 0.0954 / 10.7 | -31484.55 | -31831.84 | 2531 | -28.992 | 100% quoted, 6416 trades |
| 2026-10-08 | 0.06492 | 0.0900 / 9.8 | -100703.35 | -101842.43 | 3797 | -34.179 | 100% quoted, 7026 trades |
| 2026-10-09 | 0.07586 | 0.0759 / 6.7 | -15241.87 | -16035.32 | 2180 | -26.736 | 100% quoted, 6154 trades |
| 2026-10-12 | 0.08256 | 0.0739 / 6.1 | -26412.27 | -26445.74 | 1682 | -34.199 | 100% quoted, 4728 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.09808 | 0.0677 / 4.8 | -19385.65 | -20284.38 | 2738 | -22.659 | 100% quoted, 8865 trades |
| 2026-10-15 | 0.09592 | 0.0710 / 4.4 | -8858.35 | -9745.90 | 1481 | -31.364 | 100% quoted, 8160 trades |
