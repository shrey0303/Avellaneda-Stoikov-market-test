# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 11 (2026-10-02 to 2026-10-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -100731.22 [-146459.46, -66111.11] dollars (negative); 0 of 11 days positive; 4144 fills a day; 5 s markout -50.733 [-60.299, -41.578] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -101043.68 [-146705.18, -66325.50] dollars (negative); 0 of 11 days positive; 4339 fills a day; 5 s markout -48.955 [-58.075, -40.143] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -101794.50 [-148944.00, -66404.03] | negative | 0/11 | 4091 | -50.651 [-60.062, -41.694] |
| conservative | symmetric | 1 | -101915.72 [-153370.61, -63337.84] | negative | 0/11 | 4011 | -50.216 [-59.244, -41.510] |
| conservative | inventory | 2 | -100731.22 [-146459.46, -66111.11] | negative | 0/11 | 4144 | -50.733 [-60.299, -41.578] |
| conservative | symmetric | 2 | -101427.89 [-153027.49, -62842.55] | negative | 0/11 | 3976 | -50.514 [-59.547, -41.771] |
| conservative | inventory | 4 | -97626.45 [-142141.30, -64226.05] | negative | 0/11 | 4172 | -51.307 [-61.215, -42.102] |
| conservative | symmetric | 4 | -100871.45 [-152233.41, -62222.92] | negative | 0/11 | 3897 | -51.233 [-60.482, -42.404] |
| optimistic | inventory | 1 | -102016.76 [-148837.40, -66524.05] | negative | 0/11 | 4284 | -48.791 [-57.905, -40.147] |
| optimistic | symmetric | 1 | -102384.02 [-154139.80, -63423.26] | negative | 0/11 | 4207 | -48.308 [-56.809, -40.014] |
| optimistic | inventory | 2 | -101043.68 [-146705.18, -66325.50] | negative | 0/11 | 4339 | -48.955 [-58.075, -40.143] |
| optimistic | symmetric | 2 | -101905.66 [-153488.61, -63215.24] | negative | 0/11 | 4157 | -48.782 [-57.411, -40.436] |
| optimistic | inventory | 4 | -97802.01 [-142235.61, -64409.17] | negative | 0/11 | 4366 | -49.573 [-59.033, -40.579] |
| optimistic | symmetric | 4 | -101361.85 [-152471.02, -62728.71] | negative | 0/11 | 4072 | -49.448 [-58.217, -40.987] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 121.21 [-8455.32, 8234.15] | not established |
| conservative | 2 | 696.67 [-9367.96, 10775.20] | not established |
| conservative | 4 | 3245.00 [-7993.36, 14572.35] | not established |
| optimistic | 1 | 367.26 [-8489.71, 9176.22] | not established |
| optimistic | 2 | 861.98 [-9493.10, 11350.71] | not established |
| optimistic | 4 | 3559.84 [-7468.14, 14980.22] | not established |

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
