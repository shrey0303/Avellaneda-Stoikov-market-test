# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 23 (2026-10-02 to 2026-11-04)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -126599.47 [-160108.78, -96733.17] dollars (negative); 0 of 23 days positive; 4838 fills a day; 5 s markout -56.255 [-69.490, -46.546] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -127041.80 [-160697.20, -96956.79] dollars (negative); 0 of 23 days positive; 4986 fills a day; 5 s markout -55.128 [-68.246, -45.553] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -128439.62 [-162102.74, -98482.72] | negative | 0/23 | 4759 | -56.370 [-70.038, -46.407] |
| conservative | symmetric | 1 | -132838.79 [-169270.59, -100001.90] | negative | 0/23 | 4650 | -56.026 [-69.830, -46.049] |
| conservative | inventory | 2 | -126599.47 [-160108.78, -96733.17] | negative | 0/23 | 4838 | -56.255 [-69.490, -46.546] |
| conservative | symmetric | 2 | -132404.06 [-168915.12, -99670.85] | negative | 0/23 | 4620 | -56.240 [-69.996, -46.289] |
| conservative | inventory | 4 | -121833.32 [-154979.29, -92594.40] | negative | 0/23 | 4845 | -57.070 [-70.414, -47.296] |
| conservative | symmetric | 4 | -131636.43 [-167944.63, -98895.19] | negative | 0/23 | 4561 | -56.693 [-70.651, -46.646] |
| optimistic | inventory | 1 | -128981.77 [-162949.76, -98867.95] | negative | 0/23 | 4909 | -55.108 [-68.668, -45.394] |
| optimistic | symmetric | 1 | -133314.35 [-169703.06, -100587.58] | negative | 0/23 | 4794 | -54.753 [-68.216, -45.029] |
| optimistic | inventory | 2 | -127041.80 [-160697.20, -96956.79] | negative | 0/23 | 4986 | -55.128 [-68.246, -45.553] |
| optimistic | symmetric | 2 | -132685.30 [-169007.82, -99856.35] | negative | 0/23 | 4758 | -55.059 [-68.532, -45.335] |
| optimistic | inventory | 4 | -122199.20 [-155561.47, -92809.74] | negative | 0/23 | 4994 | -55.934 [-69.111, -46.333] |
| optimistic | symmetric | 4 | -132010.97 [-168233.70, -99304.12] | negative | 0/23 | 4692 | -55.552 [-69.206, -45.718] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4399.16 [-2465.09, 12757.01] | not established |
| conservative | 2 | 5804.59 [-3137.90, 17179.32] | not established |
| conservative | 4 | 9803.11 [-952.64, 23584.47] | not established |
| optimistic | 1 | 4332.58 [-2841.70, 13043.56] | not established |
| optimistic | 2 | 5643.50 [-3523.29, 17137.13] | not established |
| optimistic | 4 | 9811.77 [-1056.33, 23483.42] | not established |

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
