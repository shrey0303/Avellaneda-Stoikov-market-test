# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 27 (2026-10-02 to 2026-11-10)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -130336.95 [-164010.06, -100262.25] dollars (negative); 0 of 27 days positive; 4832 fills a day; 5 s markout -61.796 [-75.277, -50.685] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -130782.93 [-164598.89, -100609.23] dollars (negative); 0 of 27 days positive; 4990 fills a day; 5 s markout -60.411 [-73.857, -49.403] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -132239.08 [-166346.83, -101667.57] | negative | 0/27 | 4748 | -61.933 [-75.930, -50.515] |
| conservative | symmetric | 1 | -137142.87 [-173187.83, -104377.56] | negative | 0/27 | 4637 | -61.571 [-75.652, -50.314] |
| conservative | inventory | 2 | -130336.95 [-164010.06, -100262.25] | negative | 0/27 | 4832 | -61.796 [-75.277, -50.685] |
| conservative | symmetric | 2 | -136722.48 [-172750.39, -103941.63] | negative | 0/27 | 4605 | -61.832 [-75.918, -50.507] |
| conservative | inventory | 4 | -126104.43 [-159769.26, -96447.83] | negative | 0/27 | 4845 | -62.515 [-76.027, -51.466] |
| conservative | symmetric | 4 | -136009.77 [-172042.02, -103515.59] | negative | 0/27 | 4543 | -62.380 [-76.495, -50.942] |
| optimistic | inventory | 1 | -132731.51 [-166962.14, -102049.04] | negative | 0/27 | 4910 | -60.416 [-74.084, -49.274] |
| optimistic | symmetric | 1 | -137535.83 [-173596.50, -104657.73] | negative | 0/27 | 4793 | -59.970 [-73.669, -48.838] |
| optimistic | inventory | 2 | -130782.93 [-164598.89, -100609.23] | negative | 0/27 | 4990 | -60.411 [-73.857, -49.403] |
| optimistic | symmetric | 2 | -137011.96 [-173021.13, -104235.56] | negative | 0/27 | 4757 | -60.321 [-74.153, -49.136] |
| optimistic | inventory | 4 | -126572.54 [-160396.00, -96830.71] | negative | 0/27 | 5006 | -61.096 [-74.502, -50.283] |
| optimistic | symmetric | 4 | -136359.25 [-172285.67, -103821.10] | negative | 0/27 | 4686 | -60.980 [-75.013, -49.662] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4903.79 [-1461.46, 12283.42] | not established |
| conservative | 2 | 6385.53 [-2016.48, 16182.05] | not established |
| conservative | 4 | 9905.34 [-182.65, 21678.19] | not established |
| optimistic | 1 | 4804.33 [-1945.29, 12423.39] | not established |
| optimistic | 2 | 6229.03 [-2469.95, 16133.44] | not established |
| optimistic | 4 | 9786.71 [-414.30, 21396.06] | not established |

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
| 2026-11-04 | 0.25177 | 0.1814 / 4.9 | -170576.85 | -171138.72 | 7509 | -67.500 | 100% quoted, 36246 trades |
| 2026-11-05 | 0.25532 | 0.1943 / 4.5 | -317181.76 | -318012.39 | 8369 | -108.458 | 100% quoted, 35897 trades |
| 2026-11-06 | 0.27693 | 0.2128 / 5.1 | -168076.57 | -169699.00 | 3973 | -158.776 | 100% quoted, 20695 trades |
| 2026-11-09 | 0.28227 | 0.2084 / 5.8 | -44599.32 | -44083.31 | 2182 | -57.656 | 100% quoted, 19217 trades |
| 2026-11-10 | 0.27299 | 0.2066 / 7.1 | -77452.08 | -77383.12 | 4656 | -49.732 | 100% quoted, 22631 trades |
