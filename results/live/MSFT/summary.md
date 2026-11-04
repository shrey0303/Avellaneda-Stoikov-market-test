# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 22 (2026-10-02 to 2026-11-03)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -124600.50 [-159432.73, -93365.76] dollars (negative); 0 of 22 days positive; 4717 fills a day; 5 s markout -55.744 [-69.921, -45.550] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -125037.39 [-159923.12, -93784.22] dollars (negative); 0 of 22 days positive; 4861 fills a day; 5 s markout -54.617 [-68.628, -44.601] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -126398.02 [-161395.70, -94609.14] | negative | 0/22 | 4637 | -55.862 [-70.307, -45.435] |
| conservative | symmetric | 1 | -130229.52 [-167270.02, -96245.57] | negative | 0/22 | 4530 | -55.524 [-70.159, -44.888] |
| conservative | inventory | 2 | -124600.50 [-159432.73, -93365.76] | negative | 0/22 | 4717 | -55.744 [-69.921, -45.550] |
| conservative | symmetric | 2 | -129781.84 [-166827.87, -95769.52] | negative | 0/22 | 4500 | -55.742 [-70.381, -45.060] |
| conservative | inventory | 4 | -119747.16 [-154681.96, -89155.13] | negative | 0/22 | 4726 | -56.542 [-70.470, -46.226] |
| conservative | symmetric | 4 | -129070.00 [-165954.21, -95141.81] | negative | 0/22 | 4442 | -56.192 [-70.912, -45.406] |
| optimistic | inventory | 1 | -126925.10 [-162407.77, -94944.08] | negative | 0/22 | 4780 | -54.622 [-68.793, -44.453] |
| optimistic | symmetric | 1 | -130580.11 [-167796.43, -96576.82] | negative | 0/22 | 4670 | -54.262 [-68.541, -43.903] |
| optimistic | inventory | 2 | -125037.39 [-159923.12, -93784.22] | negative | 0/22 | 4861 | -54.617 [-68.628, -44.601] |
| optimistic | symmetric | 2 | -130046.67 [-167155.32, -95971.59] | negative | 0/22 | 4635 | -54.562 [-68.887, -44.224] |
| optimistic | inventory | 4 | -120079.45 [-154916.35, -89322.77] | negative | 0/22 | 4869 | -55.435 [-69.241, -45.329] |
| optimistic | symmetric | 4 | -129394.84 [-166252.65, -95545.59] | negative | 0/22 | 4570 | -55.049 [-69.523, -44.512] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3831.50 [-3602.71, 12109.34] | not established |
| conservative | 2 | 5181.34 [-4610.06, 16508.73] | not established |
| conservative | 4 | 9322.83 [-2588.07, 23189.33] | not established |
| optimistic | 1 | 3655.01 [-4188.03, 12336.10] | not established |
| optimistic | 2 | 5009.28 [-5027.39, 16653.14] | not established |
| optimistic | 4 | 9315.39 [-2674.85, 23379.13] | not established |

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
| 2026-10-30 | 0.16610 | 0.1508 / 5.3 | -236930.34 | -238485.83 | 7757 | -60.530 | 100% quoted, 22289 trades |
| 2026-11-02 | 0.17587 | 0.1638 / 4.8 | -213774.08 | -214981.01 | 6481 | -68.289 | 100% quoted, 21236 trades |
| 2026-11-03 | 0.17789 | 0.1685 / 4.6 | -289788.58 | -290776.71 | 4728 | -167.134 | 100% quoted, 21070 trades |
