# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 16 (2026-10-02 to 2026-10-26)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -101426.07 [-137503.89, -74680.44] dollars (negative); 0 of 16 days positive; 4216 fills a day; 5 s markout -48.645 [-56.797, -41.432] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -101679.59 [-137695.26, -74849.16] dollars (negative); 0 of 16 days positive; 4368 fills a day; 5 s markout -47.366 [-55.162, -40.489] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -103248.56 [-139521.14, -75370.83] | negative | 0/16 | 4162 | -48.427 [-56.464, -41.268] |
| conservative | symmetric | 1 | -105460.80 [-145097.98, -73951.46] | negative | 0/16 | 4074 | -47.955 [-56.145, -40.836] |
| conservative | inventory | 2 | -101426.07 [-137503.89, -74680.44] | negative | 0/16 | 4216 | -48.645 [-56.797, -41.432] |
| conservative | symmetric | 2 | -104979.29 [-144712.60, -73572.66] | negative | 0/16 | 4043 | -48.188 [-56.444, -41.041] |
| conservative | inventory | 4 | -97219.37 [-132387.23, -71607.71] | negative | 0/16 | 4221 | -49.579 [-57.856, -42.135] |
| conservative | symmetric | 4 | -104266.80 [-143941.25, -72642.06] | negative | 0/16 | 3981 | -48.713 [-57.016, -41.478] |
| optimistic | inventory | 1 | -103380.93 [-139760.31, -75620.67] | negative | 0/16 | 4310 | -47.102 [-55.055, -40.224] |
| optimistic | symmetric | 1 | -105803.61 [-145479.40, -74016.20] | negative | 0/16 | 4221 | -46.592 [-54.535, -39.842] |
| optimistic | inventory | 2 | -101679.59 [-137695.26, -74849.16] | negative | 0/16 | 4368 | -47.366 [-55.162, -40.489] |
| optimistic | symmetric | 2 | -105312.38 [-144919.42, -73678.73] | negative | 0/16 | 4182 | -46.940 [-54.883, -40.121] |
| optimistic | inventory | 4 | -97277.81 [-132365.05, -71714.96] | negative | 0/16 | 4373 | -48.356 [-56.324, -41.291] |
| optimistic | symmetric | 4 | -104648.42 [-144103.11, -73281.06] | negative | 0/16 | 4112 | -47.452 [-55.449, -40.525] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2212.24 [-5133.51, 8419.16] | not established |
| conservative | 2 | 3553.22 [-5419.15, 11766.73] | not established |
| conservative | 4 | 7047.43 [-3021.32, 16968.77] | not established |
| optimistic | 1 | 2422.69 [-5077.19, 9053.66] | not established |
| optimistic | 2 | 3632.79 [-5378.01, 12041.73] | not established |
| optimistic | 4 | 7370.62 [-2580.80, 17268.66] | not established |

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
