# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 19 (2026-10-02 to 2026-10-29)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -105300.95 [-136866.28, -78917.15] dollars (negative); 0 of 19 days positive; 4463 fills a day; 5 s markout -48.969 [-56.264, -42.365] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -105609.43 [-137218.50, -79216.39] dollars (negative); 0 of 19 days positive; 4612 fills a day; 5 s markout -47.800 [-54.858, -41.365] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -106715.87 [-138460.32, -79857.28] | negative | 0/19 | 4402 | -48.858 [-56.081, -42.242] |
| conservative | symmetric | 1 | -108422.65 [-142648.75, -79654.98] | negative | 0/19 | 4297 | -48.446 [-55.495, -41.868] |
| conservative | inventory | 2 | -105300.95 [-136866.28, -78917.15] | negative | 0/19 | 4463 | -48.969 [-56.264, -42.365] |
| conservative | symmetric | 2 | -107944.40 [-142145.52, -79239.04] | negative | 0/19 | 4266 | -48.661 [-55.718, -42.099] |
| conservative | inventory | 4 | -100882.88 [-131707.04, -75599.34] | negative | 0/19 | 4465 | -49.732 [-57.006, -43.039] |
| conservative | symmetric | 4 | -107256.94 [-141520.46, -78418.37] | negative | 0/19 | 4205 | -49.139 [-56.263, -42.447] |
| optimistic | inventory | 1 | -106990.58 [-138898.68, -80094.63] | negative | 0/19 | 4547 | -47.654 [-54.773, -41.145] |
| optimistic | symmetric | 1 | -108602.69 [-142720.20, -79728.13] | negative | 0/19 | 4439 | -47.207 [-53.937, -40.896] |
| optimistic | inventory | 2 | -105609.43 [-137218.50, -79216.39] | negative | 0/19 | 4612 | -47.800 [-54.858, -41.365] |
| optimistic | symmetric | 2 | -108165.99 [-142334.19, -79332.07] | negative | 0/19 | 4402 | -47.527 [-54.318, -41.185] |
| optimistic | inventory | 4 | -101003.80 [-131872.89, -75780.97] | negative | 0/19 | 4611 | -48.616 [-55.662, -42.097] |
| optimistic | symmetric | 4 | -107540.25 [-141620.89, -78772.97] | negative | 0/19 | 4334 | -47.996 [-54.912, -41.586] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1706.78 [-4586.54, 7571.01] | not established |
| conservative | 2 | 2643.44 [-5479.30, 10484.12] | not established |
| conservative | 4 | 6374.06 [-2377.06, 15566.85] | not established |
| optimistic | 1 | 1612.11 [-4961.83, 8009.30] | not established |
| optimistic | 2 | 2556.56 [-5667.52, 10723.72] | not established |
| optimistic | 4 | 6536.45 [-2088.65, 15741.39] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.09188 | 0.1438 / 7.8 | -65274.53 | -65888.49 | 2452 | -75.700 | 100% quoted, 13763 trades |
| 2026-10-05 | 0.12604 | 0.1347 / 8.9 | -79396.69 | -80419.49 | 4148 | -41.324 | 100% quoted, 16740 trades |
| 2026-10-06 | 0.11589 | 0.1348 / 9.1 | -52361.15 | -51868.89 | 4397 | -33.239 | 100% quoted, 13695 trades |
| 2026-10-07 | 0.10694 | 0.1325 / 8.9 | -16941.47 | -17240.57 | 2370 | -29.213 | 100% quoted, 13278 trades |
| 2026-10-08 | 0.09814 | 0.1282 / 9.5 | -89481.54 | -90269.51 | 3660 | -53.834 | 100% quoted, 17122 trades |
| 2026-10-09 | 0.11259 | 0.1277 / 9.8 | -75181.24 | -75637.03 | 3752 | -44.122 | 100% quoted, 12668 trades |
| 2026-10-12 | 0.11763 | 0.1272 / 9.6 | -113648.16 | -114515.77 | 3508 | -77.494 | 100% quoted, 12123 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.13651 | 0.1311 / 8.8 | -69596.52 | -69191.59 | 4345 | -42.767 | 100% quoted, 19532 trades |
| 2026-10-15 | 0.14547 | 0.1440 / 8.5 | -129653.63 | -129815.96 | 4768 | -43.605 | 100% quoted, 13232 trades |
| 2026-10-16 | 0.14607 | 0.1387 / 7.6 | -304716.82 | -304893.28 | 6729 | -73.847 | 100% quoted, 17571 trades |
| 2026-10-19 | 0.17502 | 0.1457 / 6.6 | -111791.66 | -111739.96 | 5452 | -42.922 | 100% quoted, 13924 trades |
| 2026-10-20 | 0.16547 | 0.1530 / 6.2 | -116555.06 | -116739.68 | 4135 | -36.905 | 100% quoted, 9975 trades |
| 2026-10-21 | 0.17516 | 0.1369 / 5.5 | -44263.54 | -44228.99 | 3663 | -34.778 | 100% quoted, 10191 trades |
| 2026-10-22 | 0.17922 | 0.1220 / 4.2 | -71692.00 | -71831.55 | 5312 | -30.329 | 100% quoted, 16194 trades |
| 2026-10-23 | 0.17294 | 0.1301 / 4.3 | -170271.54 | -170360.20 | 3705 | -70.328 | 100% quoted, 11728 trades |
| 2026-10-26 | 0.15766 | 0.1219 / 4.4 | -111991.52 | -112232.53 | 5068 | -47.914 | 100% quoted, 15140 trades |
| 2026-10-27 | 0.16665 | 0.1211 / 4.1 | -71920.07 | -71868.73 | 3214 | -60.372 | 100% quoted, 12940 trades |
| 2026-10-28 | 0.16607 | 0.1255 / 5.0 | -77289.88 | -77398.54 | 4709 | -50.572 | 100% quoted, 20210 trades |
| 2026-10-29 | 0.16483 | 0.1436 / 5.9 | -228691.03 | -230438.36 | 9416 | -41.140 | 100% quoted, 26085 trades |
