# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 10 (2026-10-02 to 2026-10-16)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -99625.18 [-153046.22, -62948.32] dollars (negative); 0 of 10 days positive; 4013 fills a day; 5 s markout -51.515 [-62.556, -41.593] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -99974.06 [-153409.08, -63208.15] dollars (negative); 0 of 10 days positive; 4218 fills a day; 5 s markout -49.601 [-60.404, -40.069] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -100493.02 [-154907.41, -62783.28] | negative | 0/10 | 3976 | -51.387 [-62.338, -41.745] |
| conservative | symmetric | 1 | -100366.00 [-159943.84, -58362.39] | negative | 0/10 | 3906 | -50.954 [-61.129, -41.854] |
| conservative | inventory | 2 | -99625.18 [-153046.22, -62948.32] | negative | 0/10 | 4013 | -51.515 [-62.556, -41.593] |
| conservative | symmetric | 2 | -99862.64 [-159497.51, -57855.97] | negative | 0/10 | 3870 | -51.262 [-61.603, -42.162] |
| conservative | inventory | 4 | -96883.98 [-149004.71, -61524.06] | negative | 0/10 | 4032 | -52.126 [-63.646, -42.095] |
| conservative | symmetric | 4 | -99285.04 [-158619.37, -57246.63] | negative | 0/10 | 3788 | -52.049 [-62.487, -42.744] |
| optimistic | inventory | 1 | -100741.55 [-155458.46, -63118.75] | negative | 0/10 | 4178 | -49.408 [-59.979, -40.047] |
| optimistic | symmetric | 1 | -100908.37 [-160690.46, -58528.98] | negative | 0/10 | 4112 | -48.879 [-58.622, -40.263] |
| optimistic | inventory | 2 | -99974.06 [-153409.08, -63208.15] | negative | 0/10 | 4218 | -49.601 [-60.404, -40.069] |
| optimistic | symmetric | 2 | -100422.32 [-159778.45, -58222.71] | negative | 0/10 | 4059 | -49.386 [-59.244, -40.607] |
| optimistic | inventory | 4 | -97034.39 [-148941.79, -61766.99] | negative | 0/10 | 4236 | -50.262 [-61.252, -40.577] |
| optimistic | symmetric | 4 | -99901.40 [-159006.44, -58007.91] | negative | 0/10 | 3971 | -50.123 [-60.086, -41.191] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -127.02 [-9886.54, 9220.50] | not established |
| conservative | 2 | 237.46 [-11390.83, 11646.27] | not established |
| conservative | 4 | 2401.06 [-10047.47, 15450.43] | not established |
| optimistic | 1 | 166.82 [-9936.83, 10185.05] | not established |
| optimistic | 2 | 448.27 [-11577.47, 12472.55] | not established |
| optimistic | 4 | 2867.01 [-9491.28, 15993.74] | not established |

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
