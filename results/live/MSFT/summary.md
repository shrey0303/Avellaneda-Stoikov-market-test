# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 38 (2026-10-02 to 2026-11-25)
- Calibration-only days: 2; days without IEX data: 1

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -122038.82 [-146197.69, -98891.52] dollars (negative); 0 of 38 days positive; 5012 fills a day; 5 s markout -59.930 [-70.203, -51.191] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -122637.07 [-146813.29, -99382.22] dollars (negative); 0 of 38 days positive; 5215 fills a day; 5 s markout -58.226 [-68.248, -49.593] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -124477.69 [-149225.80, -100601.68] | negative | 0/38 | 4931 | -60.070 [-70.465, -51.128] |
| conservative | symmetric | 1 | -131337.17 [-160840.92, -104379.00] | negative | 0/38 | 4823 | -59.797 [-70.258, -50.828] |
| conservative | inventory | 2 | -122038.82 [-146197.69, -98891.52] | negative | 0/38 | 5012 | -59.930 [-70.203, -51.191] |
| conservative | symmetric | 2 | -130845.39 [-160161.53, -103959.40] | negative | 0/38 | 4786 | -60.110 [-70.578, -51.066] |
| conservative | inventory | 4 | -117417.80 [-141002.33, -94594.01] | negative | 0/38 | 5023 | -60.507 [-70.840, -51.751] |
| conservative | symmetric | 4 | -130028.30 [-159157.09, -103189.81] | negative | 0/38 | 4713 | -60.695 [-71.322, -51.584] |
| optimistic | inventory | 1 | -125352.34 [-150171.05, -101388.59] | negative | 0/38 | 5139 | -58.273 [-68.305, -49.469] |
| optimistic | symmetric | 1 | -132527.57 [-161925.91, -105516.47] | negative | 0/38 | 5032 | -57.917 [-67.973, -49.224] |
| optimistic | inventory | 2 | -122637.07 [-146813.29, -99382.22] | negative | 0/38 | 5215 | -58.226 [-68.248, -49.593] |
| optimistic | symmetric | 2 | -131985.97 [-161510.65, -105069.16] | negative | 0/38 | 4985 | -58.323 [-68.415, -49.616] |
| optimistic | inventory | 4 | -118020.96 [-141809.78, -95355.31] | negative | 0/38 | 5224 | -58.821 [-68.808, -50.110] |
| optimistic | symmetric | 4 | -131051.63 [-160167.38, -104344.77] | negative | 0/38 | 4900 | -59.073 [-69.374, -50.256] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 6859.48 [-813.28, 15674.63] | not established |
| conservative | 2 | 8806.57 [-779.12, 19872.23] | not established |
| conservative | 4 | 12610.50 [1346.72, 25678.68] | positive |
| optimistic | 1 | 7175.24 [-734.70, 16312.57] | not established |
| optimistic | 2 | 9348.90 [-480.00, 20815.39] | not established |
| optimistic | 4 | 13030.68 [1774.27, 26396.58] | positive |

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
| 2026-11-11 | 0.20065 | 0.2051 / 6.9 | -78191.47 | -82311.30 | 5271 | -52.877 | 100% quoted, 24540 trades |
| 2026-11-12 | 0.19325 | 0.1913 / 7.4 | -67288.92 | -67736.27 | 3888 | -59.738 | 100% quoted, 16796 trades |
| 2026-11-13 | 0.16619 | 0.1631 / 8.2 | -95933.41 | -97723.88 | 4896 | -49.710 | 100% quoted, 16586 trades |
| 2026-11-16 | 0.11827 | 0.1590 / 8.1 | -71541.28 | -72016.10 | 3719 | -51.176 | 100% quoted, 15418 trades |
| 2026-11-17 | 0.12350 | 0.1558 / 7.4 | -62366.93 | -62687.36 | 4524 | -41.029 | 100% quoted, 26251 trades |
| 2026-11-18 | 0.12723 | 0.1631 / 8.0 | -91434.32 | -91601.15 | 7043 | -39.604 | 100% quoted, 26258 trades |
| 2026-11-19 | 0.12489 | 0.1634 / 8.0 | -112831.21 | -113103.60 | 6100 | -65.154 | 100% quoted, 26002 trades |
| 2026-11-20 | 0.12171 | 0.1766 / 7.8 | -244874.67 | -246342.50 | 12484 | -26.832 | 100% quoted, 32978 trades |
| 2026-11-23 | 0.12337 | 0.2090 / 6.6 | -47302.43 | -47119.67 | 3582 | -44.015 | 100% quoted, 24701 trades |
| 2026-11-24 | 0.12816 | 0.2235 / 7.1 | -107431.05 | -108357.62 | 4792 | -61.749 | 100% quoted, 15317 trades |
| 2026-11-25 | 0.13731 | 0.2122 / 6.6 | -139181.94 | -140070.11 | 3715 | -116.989 | 100% quoted, 19929 trades |
| 2026-11-26 | no IEX data |  |  |  |  |  |  |
