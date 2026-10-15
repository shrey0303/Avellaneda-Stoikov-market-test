# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 9 (2026-10-02 to 2026-10-15)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -76837.22 [-97368.01, -55697.26] dollars (negative); 0 of 9 days positive; 3711 fills a day; 5 s markout -49.033 [-59.693, -39.415] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -77205.26 [-97741.43, -55896.44] dollars (negative); 0 of 9 days positive; 3915 fills a day; 5 s markout -47.036 [-57.112, -37.927] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -77136.56 [-98649.51, -56047.10] | negative | 0/9 | 3686 | -48.647 [-58.652, -39.579] |
| conservative | symmetric | 1 | -74806.61 [-99771.20, -51229.14] | negative | 0/9 | 3638 | -48.103 [-57.611, -39.627] |
| conservative | inventory | 2 | -76837.22 [-97368.01, -55697.26] | negative | 0/9 | 3711 | -49.033 [-59.693, -39.415] |
| conservative | symmetric | 2 | -74266.10 [-99263.42, -50955.18] | negative | 0/9 | 3602 | -48.425 [-58.020, -39.889] |
| conservative | inventory | 4 | -74599.01 [-94113.71, -54269.07] | negative | 0/9 | 3716 | -49.925 [-60.916, -39.758] |
| conservative | symmetric | 4 | -73674.76 [-98604.23, -50525.80] | negative | 0/9 | 3518 | -49.231 [-59.148, -40.495] |
| optimistic | inventory | 1 | -77397.90 [-99180.64, -56020.87] | negative | 0/9 | 3887 | -46.619 [-56.181, -38.037] |
| optimistic | symmetric | 1 | -75259.03 [-100634.69, -51247.30] | negative | 0/9 | 3844 | -45.964 [-54.699, -38.161] |
| optimistic | inventory | 2 | -77205.26 [-97741.43, -55896.44] | negative | 0/9 | 3915 | -47.036 [-57.112, -37.927] |
| optimistic | symmetric | 2 | -74805.18 [-100013.55, -50995.50] | negative | 0/9 | 3793 | -46.485 [-55.399, -38.509] |
| optimistic | inventory | 4 | -74824.76 [-94378.40, -54287.65] | negative | 0/9 | 3922 | -47.964 [-58.440, -38.327] |
| optimistic | symmetric | 4 | -74402.41 [-99368.07, -50967.63] | negative | 0/9 | 3705 | -47.242 [-56.347, -39.070] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2329.95 [-12822.78, 6468.08] | not established |
| conservative | 2 | -2571.12 [-14665.74, 8100.07] | not established |
| conservative | 4 | -924.25 [-13450.14, 11410.46] | not established |
| optimistic | 1 | -2138.88 [-13100.52, 7586.80] | not established |
| optimistic | 2 | -2400.07 [-14825.66, 8901.31] | not established |
| optimistic | 4 | -422.35 [-12753.24, 12071.98] | not established |

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
