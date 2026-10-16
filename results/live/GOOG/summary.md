# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 10 (2026-10-02 to 2026-10-16)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29562.96 [-47205.85, -16586.95] dollars (negative); 0 of 10 days positive; 2336 fills a day; 5 s markout -27.180 [-33.023, -21.785] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -30095.56 [-47776.28, -17044.18] dollars (negative); 0 of 10 days positive; 2435 fills a day; 5 s markout -26.663 [-32.475, -21.300] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -30931.70 [-51952.35, -15963.60] | negative | 0/10 | 2333 | -27.019 [-32.897, -21.646] |
| conservative | symmetric | 1 | -35504.37 [-64475.40, -15342.22] | negative | 0/10 | 2320 | -26.223 [-32.034, -20.826] |
| conservative | inventory | 2 | -29562.96 [-47205.85, -16586.95] | negative | 0/10 | 2336 | -27.180 [-33.023, -21.785] |
| conservative | symmetric | 2 | -35264.70 [-64189.74, -15229.52] | negative | 0/10 | 2298 | -26.322 [-32.137, -20.927] |
| conservative | inventory | 4 | -27691.13 [-41687.87, -17087.66] | negative | 0/10 | 2291 | -27.619 [-33.413, -22.189] |
| conservative | symmetric | 4 | -34636.31 [-63433.62, -14670.10] | negative | 0/10 | 2261 | -26.502 [-32.357, -21.139] |
| optimistic | inventory | 1 | -31256.75 [-52393.17, -16273.98] | negative | 0/10 | 2432 | -26.524 [-32.345, -21.110] |
| optimistic | symmetric | 1 | -35823.42 [-65159.57, -15281.21] | negative | 0/10 | 2406 | -25.781 [-31.509, -20.456] |
| optimistic | inventory | 2 | -30095.56 [-47776.28, -17044.18] | negative | 0/10 | 2435 | -26.663 [-32.475, -21.300] |
| optimistic | symmetric | 2 | -35553.77 [-64719.24, -15106.48] | negative | 0/10 | 2386 | -25.855 [-31.551, -20.540] |
| optimistic | inventory | 4 | -28058.33 [-42163.58, -17440.35] | negative | 0/10 | 2391 | -27.093 [-32.715, -21.719] |
| optimistic | symmetric | 4 | -35049.13 [-64029.87, -14771.90] | negative | 0/10 | 2341 | -26.028 [-31.704, -20.718] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4572.68 [-1530.69, 12144.04] | not established |
| conservative | 2 | 5701.74 [-3232.61, 17006.94] | not established |
| conservative | 4 | 6945.18 [-4336.84, 22386.77] | not established |
| optimistic | 1 | 4566.67 [-1915.53, 12505.13] | not established |
| optimistic | 2 | 5458.21 [-3730.42, 17079.65] | not established |
| optimistic | 4 | 6990.80 [-4492.90, 22517.49] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.06399 | 0.1467 / 15.3 | -11239.88 | -11388.79 | 2611 | -14.894 | 100% quoted, 6767 trades |
| 2026-10-05 | 0.06162 | 0.1095 / 12.5 | -22660.49 | -22799.99 | 2604 | -17.254 | 100% quoted, 9105 trades |
| 2026-10-06 | 0.05802 | 0.1063 / 11.7 | -15860.42 | -16278.82 | 2137 | -16.669 | 100% quoted, 5468 trades |
| 2026-10-07 | 0.05532 | 0.0954 / 10.7 | -31484.55 | -31831.84 | 2531 | -28.992 | 100% quoted, 6416 trades |
| 2026-10-08 | 0.06492 | 0.0900 / 9.8 | -100703.35 | -101842.43 | 3797 | -34.179 | 100% quoted, 7026 trades |
| 2026-10-09 | 0.07586 | 0.0759 / 6.7 | -15241.87 | -16035.32 | 2180 | -26.736 | 100% quoted, 6154 trades |
| 2026-10-12 | 0.08256 | 0.0739 / 6.1 | -26412.27 | -26445.74 | 1682 | -34.199 | 100% quoted, 4728 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.09808 | 0.0677 / 4.8 | -19385.65 | -20284.38 | 2738 | -22.659 | 100% quoted, 8865 trades |
| 2026-10-15 | 0.09592 | 0.0710 / 4.4 | -8858.35 | -9745.90 | 1481 | -31.364 | 100% quoted, 8160 trades |
| 2026-10-16 | 0.08691 | 0.0722 / 5.4 | -43782.76 | -44302.42 | 1600 | -44.858 | 100% quoted, 5455 trades |
