# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 14 (2026-10-02 to 2026-10-22)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -95753.86 [-134698.72, -68451.98] dollars (negative); 0 of 14 days positive; 4192 fills a day; 5 s markout -47.149 [-56.422, -39.332] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -96020.05 [-135084.02, -68766.45] dollars (negative); 0 of 14 days positive; 4356 fills a day; 5 s markout -45.725 [-54.445, -38.309] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -97534.17 [-137406.11, -68824.61] | negative | 0/14 | 4131 | -46.911 [-55.913, -39.179] |
| conservative | symmetric | 1 | -100175.50 [-143533.14, -68612.02] | negative | 0/14 | 4039 | -46.454 [-55.003, -38.996] |
| conservative | inventory | 2 | -95753.86 [-134698.72, -68451.98] | negative | 0/14 | 4192 | -47.149 [-56.422, -39.332] |
| conservative | symmetric | 2 | -99676.92 [-143156.35, -68065.12] | negative | 0/14 | 4006 | -46.706 [-55.355, -39.171] |
| conservative | inventory | 4 | -91896.11 [-129601.30, -65715.79] | negative | 0/14 | 4216 | -47.800 [-57.149, -39.866] |
| conservative | symmetric | 4 | -98991.58 [-142263.48, -67240.20] | negative | 0/14 | 3937 | -47.271 [-56.164, -39.558] |
| optimistic | inventory | 1 | -97722.32 [-137571.63, -69065.11] | negative | 0/14 | 4294 | -45.438 [-54.072, -38.029] |
| optimistic | symmetric | 1 | -100585.06 [-144060.32, -68619.74] | negative | 0/14 | 4200 | -44.937 [-52.926, -37.935] |
| optimistic | inventory | 2 | -96020.05 [-135084.02, -68766.45] | negative | 0/14 | 4356 | -45.725 [-54.445, -38.309] |
| optimistic | symmetric | 2 | -100085.66 [-143544.86, -68264.12] | negative | 0/14 | 4158 | -45.319 [-53.420, -38.261] |
| optimistic | inventory | 4 | -92023.72 [-129630.95, -65833.93] | negative | 0/14 | 4379 | -46.418 [-55.307, -38.881] |
| optimistic | symmetric | 4 | -99455.42 [-142544.25, -67862.95] | negative | 0/14 | 4083 | -45.864 [-54.122, -38.543] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2641.33 [-4975.31, 9744.23] | not established |
| conservative | 2 | 3923.06 [-5710.61, 13084.11] | not established |
| conservative | 4 | 7095.47 [-3659.29, 18142.53] | not established |
| optimistic | 1 | 2862.74 [-5005.15, 10336.65] | not established |
| optimistic | 2 | 4065.61 [-5793.04, 13457.77] | not established |
| optimistic | 4 | 7431.71 [-3316.64, 18628.51] | not established |

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
