# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 21 (2026-10-02 to 2026-11-02)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -116734.40 [-148176.17, -87082.67] dollars (negative); 0 of 21 days positive; 4716 fills a day; 5 s markout -50.439 [-57.045, -44.030] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -117145.05 [-148788.98, -87326.09] dollars (negative); 0 of 21 days positive; 4863 fills a day; 5 s markout -49.331 [-55.570, -43.101] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -119125.19 [-151444.61, -88460.37] | negative | 0/21 | 4650 | -50.339 [-56.859, -44.007] |
| conservative | symmetric | 1 | -123925.79 [-160651.84, -89430.21] | negative | 0/21 | 4547 | -49.956 [-56.254, -43.658] |
| conservative | inventory | 2 | -116734.40 [-148176.17, -87082.67] | negative | 0/21 | 4716 | -50.439 [-57.045, -44.030] |
| conservative | symmetric | 2 | -123470.64 [-160240.68, -89027.36] | negative | 0/21 | 4517 | -50.169 [-56.476, -43.907] |
| conservative | inventory | 4 | -111346.40 [-141514.92, -82887.70] | negative | 0/21 | 4714 | -51.262 [-57.953, -44.735] |
| conservative | symmetric | 4 | -122704.42 [-159242.78, -88303.92] | negative | 0/21 | 4457 | -50.590 [-57.059, -44.262] |
| optimistic | inventory | 1 | -119622.23 [-152599.57, -88843.02] | negative | 0/21 | 4794 | -49.169 [-55.483, -42.928] |
| optimistic | symmetric | 1 | -124364.38 [-161142.84, -89740.27] | negative | 0/21 | 4690 | -48.802 [-54.888, -42.648] |
| optimistic | inventory | 2 | -117145.05 [-148788.98, -87326.09] | negative | 0/21 | 4863 | -49.331 [-55.570, -43.101] |
| optimistic | symmetric | 2 | -123788.92 [-160444.56, -89306.37] | negative | 0/21 | 4654 | -49.090 [-55.239, -42.926] |
| optimistic | inventory | 4 | -111602.80 [-141738.05, -83151.40] | negative | 0/21 | 4860 | -50.185 [-56.705, -43.936] |
| optimistic | symmetric | 4 | -123107.00 [-159678.42, -88874.86] | negative | 0/21 | 4587 | -49.522 [-55.706, -43.317] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4800.61 [-2662.20, 13212.65] | not established |
| conservative | 2 | 6736.24 [-2988.15, 17798.74] | not established |
| conservative | 4 | 11358.02 [353.44, 24410.80] | positive |
| optimistic | 1 | 4742.15 [-3094.21, 13377.56] | not established |
| optimistic | 2 | 6643.88 [-3294.15, 17690.71] | not established |
| optimistic | 4 | 11504.19 [538.17, 24508.19] | positive |

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
