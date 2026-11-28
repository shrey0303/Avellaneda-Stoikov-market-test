# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 39 (2026-10-02 to 2026-11-27)
- Calibration-only days: 2; days without IEX data: 1

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -121727.82 [-145920.37, -99054.63] dollars (negative); 0 of 39 days positive; 4942 fills a day; 5 s markout -62.040 [-73.508, -52.568] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -122332.13 [-146566.40, -99588.61] dollars (negative); 0 of 39 days positive; 5143 fills a day; 5 s markout -60.249 [-71.455, -50.951] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -124161.25 [-149166.62, -100808.34] | negative | 0/39 | 4862 | -62.237 [-74.022, -52.586] |
| conservative | symmetric | 1 | -131026.75 [-159424.97, -103743.24] | negative | 0/39 | 4756 | -62.016 [-73.838, -52.287] |
| conservative | inventory | 2 | -121727.82 [-145920.37, -99054.63] | negative | 0/39 | 4942 | -62.040 [-73.508, -52.568] |
| conservative | symmetric | 2 | -130548.83 [-158807.63, -103388.88] | negative | 0/39 | 4720 | -62.345 [-74.248, -52.569] |
| conservative | inventory | 4 | -117180.40 [-140476.39, -95212.08] | negative | 0/39 | 4953 | -62.584 [-73.998, -53.092] |
| conservative | symmetric | 4 | -129734.04 [-158027.74, -102820.93] | negative | 0/39 | 4647 | -62.973 [-75.031, -53.088] |
| optimistic | inventory | 1 | -125035.45 [-150157.13, -101684.01] | negative | 0/39 | 5068 | -60.302 [-71.581, -50.984] |
| optimistic | symmetric | 1 | -132226.21 [-160993.75, -104829.79] | negative | 0/39 | 4963 | -59.977 [-71.264, -50.529] |
| optimistic | inventory | 2 | -122332.13 [-146566.40, -99588.61] | negative | 0/39 | 5143 | -60.249 [-71.455, -50.951] |
| optimistic | symmetric | 2 | -131698.72 [-160472.18, -104415.94] | negative | 0/39 | 4916 | -60.408 [-71.850, -50.910] |
| optimistic | inventory | 4 | -117792.19 [-141146.35, -95682.11] | negative | 0/39 | 5152 | -60.809 [-71.922, -51.532] |
| optimistic | symmetric | 4 | -130755.11 [-159132.72, -103817.34] | negative | 0/39 | 4832 | -61.223 [-72.899, -51.658] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 6865.50 [-768.28, 15788.72] | not established |
| conservative | 2 | 8821.01 [-760.67, 19657.69] | not established |
| conservative | 4 | 12553.64 [1535.32, 25021.76] | positive |
| optimistic | 1 | 7190.76 [-685.67, 16402.58] | not established |
| optimistic | 2 | 9366.59 [-680.42, 20533.00] | not established |
| optimistic | 4 | 12962.92 [1899.26, 25647.00] | positive |

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
| 2026-11-27 | 0.19502 | 0.2120 / 6.7 | -109909.88 | -110744.24 | 2285 | -142.188 | 100% quoted, 6651 trades |
