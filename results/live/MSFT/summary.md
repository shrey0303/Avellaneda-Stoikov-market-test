# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 18 (2026-10-02 to 2026-10-28)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -98445.95 [-130311.79, -74764.84] dollars (negative); 0 of 18 days positive; 4188 fills a day; 5 s markout -49.404 [-56.898, -42.605] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -98674.49 [-130597.00, -74940.50] dollars (negative); 0 of 18 days positive; 4332 fills a day; 5 s markout -48.189 [-55.280, -41.689] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -100250.23 [-132903.74, -75905.69] | negative | 0/18 | 4124 | -49.282 [-56.650, -42.478] |
| conservative | symmetric | 1 | -102953.50 [-139156.61, -76497.05] | negative | 0/18 | 4023 | -48.951 [-56.186, -42.210] |
| conservative | inventory | 2 | -98445.95 [-130311.79, -74764.84] | negative | 0/18 | 4188 | -49.404 [-56.898, -42.605] |
| conservative | symmetric | 2 | -102525.05 [-138609.01, -76170.17] | negative | 0/18 | 3994 | -49.174 [-56.422, -42.402] |
| conservative | inventory | 4 | -94292.97 [-124806.26, -71546.42] | negative | 0/18 | 4197 | -50.190 [-57.829, -43.265] |
| conservative | symmetric | 4 | -101857.81 [-138005.34, -75398.60] | negative | 0/18 | 3936 | -49.664 [-57.117, -42.773] |
| optimistic | inventory | 1 | -100398.81 [-132970.61, -75939.00] | negative | 0/18 | 4266 | -48.026 [-55.197, -41.423] |
| optimistic | symmetric | 1 | -103295.07 [-139851.71, -76872.35] | negative | 0/18 | 4161 | -47.652 [-54.550, -41.236] |
| optimistic | inventory | 2 | -98674.49 [-130597.00, -74940.50] | negative | 0/18 | 4332 | -48.189 [-55.280, -41.689] |
| optimistic | symmetric | 2 | -102827.26 [-139287.90, -76312.16] | negative | 0/18 | 4125 | -47.983 [-54.948, -41.516] |
| optimistic | inventory | 4 | -94351.29 [-124720.58, -71724.42] | negative | 0/18 | 4343 | -49.022 [-56.343, -42.392] |
| optimistic | symmetric | 4 | -102176.62 [-138258.51, -75801.51] | negative | 0/18 | 4059 | -48.471 [-55.550, -41.900] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2703.28 [-3547.88, 8577.10] | not established |
| conservative | 2 | 4079.10 [-3877.35, 11725.67] | not established |
| conservative | 4 | 7564.84 [-1397.82, 16879.72] | not established |
| optimistic | 1 | 2896.25 [-3525.03, 9282.51] | not established |
| optimistic | 2 | 4152.77 [-3907.42, 12166.61] | not established |
| optimistic | 4 | 7825.33 [-1075.47, 17020.31] | not established |

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
