# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 8 (2026-10-02 to 2026-10-14)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -30373.56 [-51854.99, -17041.08] dollars (negative); 0 of 8 days positive; 2535 fills a day; 5 s markout -24.448 [-29.497, -19.524] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -30863.41 [-52457.32, -17423.23] dollars (negative); 0 of 8 days positive; 2642 fills a day; 5 s markout -23.957 [-29.014, -19.039] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -31714.60 [-58110.37, -15504.28] | negative | 0/8 | 2539 | -24.256 [-29.269, -19.317] |
| conservative | symmetric | 1 | -36296.31 [-72002.81, -13048.62] | negative | 0/8 | 2524 | -23.460 [-28.487, -18.667] |
| conservative | inventory | 2 | -30373.56 [-51854.99, -17041.08] | negative | 0/8 | 2535 | -24.448 [-29.497, -19.524] |
| conservative | symmetric | 2 | -36059.11 [-71653.14, -12952.65] | negative | 0/8 | 2498 | -23.550 [-28.600, -18.725] |
| conservative | inventory | 4 | -28065.57 [-44747.41, -17528.65] | negative | 0/8 | 2473 | -24.838 [-29.897, -19.926] |
| conservative | symmetric | 4 | -35363.13 [-70937.12, -12271.02] | negative | 0/8 | 2457 | -23.713 [-28.718, -18.878] |
| optimistic | inventory | 1 | -32052.85 [-58427.13, -15776.08] | negative | 0/8 | 2648 | -23.752 [-28.883, -18.789] |
| optimistic | symmetric | 1 | -36675.72 [-72938.13, -13007.34] | negative | 0/8 | 2617 | -23.105 [-28.148, -18.326] |
| optimistic | inventory | 2 | -30863.41 [-52457.32, -17423.23] | negative | 0/8 | 2642 | -23.957 [-29.014, -19.039] |
| optimistic | symmetric | 2 | -36323.89 [-72437.51, -12796.70] | negative | 0/8 | 2593 | -23.196 [-28.239, -18.422] |
| optimistic | inventory | 4 | -28429.10 [-45181.28, -17832.88] | negative | 0/8 | 2581 | -24.424 [-29.488, -19.450] |
| optimistic | symmetric | 4 | -35698.15 [-71380.90, -12520.92] | negative | 0/8 | 2543 | -23.361 [-28.356, -18.596] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4581.72 [-2885.22, 14164.99] | not established |
| conservative | 2 | 5685.55 [-5209.46, 20170.82] | not established |
| conservative | 4 | 7297.56 [-6897.42, 26940.07] | not established |
| optimistic | 1 | 4622.87 [-3302.56, 14712.09] | not established |
| optimistic | 2 | 5460.48 [-5673.95, 20341.53] | not established |
| optimistic | 4 | 7269.05 [-7048.84, 27045.35] | not established |

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
