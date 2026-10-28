# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 17 (2026-10-02 to 2026-10-27)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -99690.42 [-132064.60, -74159.17] dollars (negative); 0 of 17 days positive; 4158 fills a day; 5 s markout -49.335 [-57.201, -42.096] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -99926.01 [-132326.85, -74385.92] dollars (negative); 0 of 17 days positive; 4303 fills a day; 5 s markout -48.090 [-55.646, -41.167] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -101573.22 [-134473.59, -75029.14] | negative | 0/17 | 4099 | -49.163 [-57.031, -42.030] |
| conservative | symmetric | 1 | -104061.21 [-141056.06, -75274.83] | negative | 0/17 | 4009 | -48.674 [-56.470, -41.618] |
| conservative | inventory | 2 | -99690.42 [-132064.60, -74159.17] | negative | 0/17 | 4158 | -49.335 [-57.201, -42.096] |
| conservative | symmetric | 2 | -103620.68 [-140547.36, -74806.39] | negative | 0/17 | 3980 | -48.901 [-56.698, -41.881] |
| conservative | inventory | 4 | -95432.52 [-127135.25, -70626.18] | negative | 0/17 | 4167 | -50.178 [-57.932, -42.862] |
| conservative | symmetric | 4 | -102921.57 [-139754.82, -73925.99] | negative | 0/17 | 3920 | -49.404 [-57.282, -42.325] |
| optimistic | inventory | 1 | -101710.43 [-134527.95, -75328.02] | negative | 0/17 | 4242 | -47.894 [-55.573, -40.967] |
| optimistic | symmetric | 1 | -104412.98 [-141661.83, -75513.82] | negative | 0/17 | 4150 | -47.347 [-54.785, -40.555] |
| optimistic | inventory | 2 | -99926.01 [-132326.85, -74385.92] | negative | 0/17 | 4303 | -48.090 [-55.646, -41.167] |
| optimistic | symmetric | 2 | -103924.14 [-140999.65, -75186.26] | negative | 0/17 | 4113 | -47.684 [-55.229, -40.770] |
| optimistic | inventory | 4 | -95485.46 [-127065.84, -70664.80] | negative | 0/17 | 4315 | -48.998 [-56.583, -41.895] |
| optimistic | symmetric | 4 | -103262.19 [-140162.43, -74579.96] | negative | 0/17 | 4046 | -48.180 [-55.858, -41.169] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2488.00 [-4217.40, 8428.27] | not established |
| conservative | 2 | 3930.26 [-4290.31, 11413.24] | not established |
| conservative | 4 | 7489.05 [-2089.35, 16398.46] | not established |
| optimistic | 1 | 2702.55 [-4268.36, 9014.23] | not established |
| optimistic | 2 | 3998.13 [-4343.78, 11617.00] | not established |
| optimistic | 4 | 7776.73 [-1719.57, 16715.39] | not established |

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
