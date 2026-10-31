# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 20 (2026-10-02 to 2026-10-30)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -111882.42 [-143490.48, -82597.01] dollars (negative); 0 of 20 days positive; 4628 fills a day; 5 s markout -49.547 [-56.395, -43.219] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -112253.25 [-143875.72, -82906.08] dollars (negative); 0 of 20 days positive; 4777 fills a day; 5 s markout -48.406 [-54.973, -42.256] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -113175.86 [-144861.00, -83202.26] | negative | 0/20 | 4568 | -49.552 [-56.305, -43.212] |
| conservative | symmetric | 1 | -114915.91 [-147194.22, -83432.93] | negative | 0/20 | 4475 | -49.235 [-55.824, -42.853] |
| conservative | inventory | 2 | -111882.42 [-143490.48, -82597.01] | negative | 0/20 | 4628 | -49.547 [-56.395, -43.219] |
| conservative | symmetric | 2 | -114457.33 [-146799.15, -83113.25] | negative | 0/20 | 4444 | -49.454 [-56.046, -43.009] |
| conservative | inventory | 4 | -107313.26 [-138403.03, -78990.09] | negative | 0/20 | 4619 | -50.307 [-57.253, -43.947] |
| conservative | symmetric | 4 | -113745.97 [-146084.10, -82380.85] | negative | 0/20 | 4383 | -49.905 [-56.652, -43.402] |
| optimistic | inventory | 1 | -113567.79 [-145440.83, -83354.55] | negative | 0/20 | 4714 | -48.338 [-54.877, -42.219] |
| optimistic | symmetric | 1 | -115236.64 [-147912.18, -83514.85] | negative | 0/20 | 4619 | -48.046 [-54.449, -41.843] |
| optimistic | inventory | 2 | -112253.25 [-143875.72, -82906.08] | negative | 0/20 | 4777 | -48.406 [-54.973, -42.256] |
| optimistic | symmetric | 2 | -114753.91 [-147210.72, -83172.23] | negative | 0/20 | 4583 | -48.335 [-54.757, -42.140] |
| optimistic | inventory | 4 | -107496.91 [-138529.92, -79145.63] | negative | 0/20 | 4765 | -49.206 [-55.840, -42.998] |
| optimistic | symmetric | 4 | -114087.48 [-146400.16, -82865.74] | negative | 0/20 | 4514 | -48.790 [-55.286, -42.551] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1740.06 [-4333.07, 6926.77] | not established |
| conservative | 2 | 2574.91 [-4981.30, 9199.43] | not established |
| conservative | 4 | 6432.71 [-1911.92, 14170.15] | not established |
| optimistic | 1 | 1668.84 [-4752.23, 7324.67] | not established |
| optimistic | 2 | 2500.66 [-5361.27, 9415.46] | not established |
| optimistic | 4 | 6590.57 [-1854.43, 14404.45] | not established |

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
