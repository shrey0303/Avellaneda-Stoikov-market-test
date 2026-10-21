# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 12 (2026-10-02 to 2026-10-20)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26151.97 [-33286.95, -20861.14] dollars (negative); 0 of 12 days positive; 4336 fills a day; 5 s markout -19.941 [-23.135, -17.314] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26509.53 [-33454.66, -21236.05] dollars (negative); 0 of 12 days positive; 5060 fills a day; 5 s markout -17.965 [-20.843, -15.573] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27037.46 [-34372.48, -21625.61] | negative | 0/12 | 4320 | -19.920 [-23.054, -17.323] |
| conservative | symmetric | 1 | -29904.38 [-36162.46, -24463.03] | negative | 0/12 | 4061 | -20.442 [-23.542, -17.792] |
| conservative | inventory | 2 | -26151.97 [-33286.95, -20861.14] | negative | 0/12 | 4336 | -19.941 [-23.135, -17.314] |
| conservative | symmetric | 2 | -29383.62 [-35783.42, -23905.10] | negative | 0/12 | 3940 | -20.879 [-24.023, -18.157] |
| conservative | inventory | 4 | -24984.46 [-31603.31, -19981.08] | negative | 0/12 | 4251 | -20.117 [-23.435, -17.369] |
| conservative | symmetric | 4 | -28490.22 [-34590.95, -23190.84] | negative | 0/12 | 3718 | -21.730 [-24.928, -18.917] |
| optimistic | inventory | 1 | -27348.47 [-34789.10, -21807.17] | negative | 0/12 | 5072 | -17.885 [-20.691, -15.552] |
| optimistic | symmetric | 1 | -30762.53 [-37145.47, -25090.54] | negative | 0/12 | 4755 | -18.373 [-21.279, -15.946] |
| optimistic | inventory | 2 | -26509.53 [-33454.66, -21236.05] | negative | 0/12 | 5060 | -17.965 [-20.843, -15.573] |
| optimistic | symmetric | 2 | -30420.49 [-36856.00, -24819.37] | negative | 0/12 | 4577 | -18.893 [-21.870, -16.381] |
| optimistic | inventory | 4 | -25457.65 [-31939.89, -20514.53] | negative | 0/12 | 4905 | -18.285 [-21.335, -15.801] |
| optimistic | symmetric | 4 | -29409.14 [-35689.76, -23949.52] | negative | 0/12 | 4283 | -19.682 [-22.673, -17.103] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2866.92 [-844.32, 6260.55] | not established |
| conservative | 2 | 3231.66 [-304.41, 6343.97] | not established |
| conservative | 4 | 3505.76 [419.42, 6225.15] | positive |
| optimistic | 1 | 3414.06 [-576.99, 6972.03] | not established |
| optimistic | 2 | 3910.95 [171.14, 7352.52] | positive |
| optimistic | 4 | 3951.50 [602.96, 6953.51] | positive |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.03590 | 0.1627 / 21.8 | -20422.65 | -20056.01 | 2805 | -21.307 | 100% quoted, 18831 trades |
| 2026-10-05 | 0.03352 | 0.1556 / 24.5 | -23657.69 | -23811.35 | 4159 | -17.189 | 100% quoted, 21277 trades |
| 2026-10-06 | 0.03492 | 0.1547 / 23.4 | -16586.88 | -16698.85 | 3883 | -16.620 | 100% quoted, 17706 trades |
| 2026-10-07 | 0.03494 | 0.1521 / 22.9 | -19191.59 | -19890.24 | 4187 | -16.319 | 100% quoted, 22360 trades |
| 2026-10-08 | 0.03494 | 0.1561 / 22.6 | -22937.02 | -23554.55 | 4768 | -18.093 | 100% quoted, 21964 trades |
| 2026-10-09 | 0.03552 | 0.1602 / 22.4 | -30969.88 | -31701.81 | 5736 | -17.518 | 100% quoted, 30585 trades |
| 2026-10-12 | 0.03760 | 0.1646 / 20.4 | -27309.15 | -27596.35 | 3327 | -26.526 | 100% quoted, 16325 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.04355 | 0.1628 / 18.8 | -19274.68 | -20392.63 | 5006 | -14.498 | 100% quoted, 32766 trades |
| 2026-10-15 | 0.04310 | 0.1754 / 19.3 | -13261.23 | -13383.33 | 2902 | -18.648 | 100% quoted, 21362 trades |
| 2026-10-16 | 0.04253 | 0.1672 / 19.7 | -29159.03 | -29472.61 | 6166 | -15.879 | 100% quoted, 29380 trades |
| 2026-10-19 | 0.04269 | 0.1770 / 19.8 | -32431.15 | -33558.76 | 4833 | -23.095 | 100% quoted, 21058 trades |
| 2026-10-20 | 0.04106 | 0.1818 / 19.7 | -58622.64 | -57997.89 | 4256 | -33.597 | 100% quoted, 19216 trades |
