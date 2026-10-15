# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 8 (2026-10-02 to 2026-10-14)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -70235.16 [-88003.32, -51391.58] dollars (negative); 0 of 8 days positive; 3579 fills a day; 5 s markout -49.712 [-62.213, -38.916] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -70628.92 [-88530.45, -51871.03] dollars (negative); 0 of 8 days positive; 3793 fills a day; 5 s markout -47.503 [-59.226, -37.256] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -69968.30 [-87106.25, -50756.37] | negative | 0/8 | 3547 | -49.243 [-60.999, -39.041] |
| conservative | symmetric | 1 | -66388.31 [-85667.49, -46213.45] | negative | 0/8 | 3486 | -48.510 [-59.326, -39.065] |
| conservative | inventory | 2 | -70235.16 [-88003.32, -51391.58] | negative | 0/8 | 3579 | -49.712 [-62.213, -38.916] |
| conservative | symmetric | 2 | -65828.24 [-84969.00, -45667.39] | negative | 0/8 | 3448 | -48.855 [-59.749, -39.358] |
| conservative | inventory | 4 | -68590.51 [-86787.97, -50092.79] | negative | 0/8 | 3596 | -50.593 [-63.856, -39.341] |
| conservative | symmetric | 4 | -65330.37 [-84923.48, -45174.96] | negative | 0/8 | 3364 | -49.739 [-61.048, -39.948] |
| optimistic | inventory | 1 | -70191.73 [-87843.11, -51153.18] | negative | 0/8 | 3758 | -47.019 [-58.015, -37.299] |
| optimistic | symmetric | 1 | -66792.89 [-86475.73, -46396.93] | negative | 0/8 | 3703 | -46.179 [-56.165, -37.228] |
| optimistic | inventory | 2 | -70628.92 [-88530.45, -51871.03] | negative | 0/8 | 3793 | -47.503 [-59.226, -37.256] |
| optimistic | symmetric | 2 | -66466.59 [-86289.50, -46242.58] | negative | 0/8 | 3651 | -46.729 [-56.899, -37.639] |
| optimistic | inventory | 4 | -68807.23 [-87141.35, -50168.14] | negative | 0/8 | 3809 | -48.496 [-60.942, -37.760] |
| optimistic | symmetric | 4 | -66059.41 [-85631.11, -45848.72] | negative | 0/8 | 3558 | -47.521 [-57.915, -38.237] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -3579.99 [-14719.64, 6268.72] | not established |
| conservative | 2 | -4406.92 [-16904.97, 7414.65] | not established |
| conservative | 4 | -3260.13 [-15939.45, 10166.07] | not established |
| optimistic | 1 | -3398.84 [-15024.38, 7754.21] | not established |
| optimistic | 2 | -4162.33 [-17179.28, 8721.63] | not established |
| optimistic | 4 | -2747.82 [-15054.23, 10957.38] | not established |

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
