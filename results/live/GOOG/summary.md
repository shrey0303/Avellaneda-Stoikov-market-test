# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 24 (2026-10-02 to 2026-11-05)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -33516.05 [-46612.08, -22563.19] dollars (negative); 0 of 24 days positive; 3194 fills a day; 5 s markout -28.183 [-32.490, -24.144] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -33865.03 [-47015.42, -22906.64] dollars (negative); 0 of 24 days positive; 3386 fills a day; 5 s markout -27.330 [-31.558, -23.390] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -34704.46 [-48765.27, -22490.07] | negative | 0/24 | 3202 | -28.045 [-32.308, -24.016] |
| conservative | symmetric | 1 | -39894.26 [-62963.08, -20448.22] | negative | 1/24 | 3113 | -27.621 [-31.965, -23.556] |
| conservative | inventory | 2 | -33516.05 [-46612.08, -22563.19] | negative | 0/24 | 3194 | -28.183 [-32.490, -24.144] |
| conservative | symmetric | 2 | -39419.03 [-62279.02, -20185.66] | negative | 1/24 | 3068 | -27.819 [-32.147, -23.728] |
| conservative | inventory | 4 | -31858.09 [-43909.77, -22006.17] | negative | 0/24 | 3095 | -28.628 [-32.945, -24.582] |
| conservative | symmetric | 4 | -38848.83 [-61625.14, -19657.61] | negative | 1/24 | 2989 | -28.210 [-32.595, -24.024] |
| optimistic | inventory | 1 | -34957.69 [-49053.60, -22760.51] | negative | 0/24 | 3406 | -27.089 [-31.319, -23.159] |
| optimistic | symmetric | 1 | -40440.61 [-64073.11, -20656.55] | negative | 2/24 | 3303 | -26.711 [-30.964, -22.752] |
| optimistic | inventory | 2 | -33865.03 [-47015.42, -22906.64] | negative | 0/24 | 3386 | -27.330 [-31.558, -23.390] |
| optimistic | symmetric | 2 | -40191.00 [-63767.64, -20429.24] | negative | 1/24 | 3247 | -26.946 [-31.219, -22.970] |
| optimistic | inventory | 4 | -32261.04 [-44449.30, -22304.74] | negative | 0/24 | 3294 | -27.677 [-31.905, -23.712] |
| optimistic | symmetric | 4 | -39412.41 [-62463.40, -20082.71] | negative | 1/24 | 3154 | -27.354 [-31.681, -23.298] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 5189.80 [-4449.00, 17787.94] | not established |
| conservative | 2 | 5902.97 [-4823.46, 19769.22] | not established |
| conservative | 4 | 6990.74 [-4622.18, 22311.59] | not established |
| optimistic | 1 | 5482.92 [-4495.88, 18698.06] | not established |
| optimistic | 2 | 6325.97 [-4828.37, 20852.30] | not established |
| optimistic | 4 | 7151.37 [-4641.20, 22636.97] | not established |

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
| 2026-10-19 | 0.09084 | 0.0722 / 5.5 | -27282.03 | -27296.19 | 2210 | -31.606 | 100% quoted, 8489 trades |
| 2026-10-20 | 0.08560 | 0.0785 / 5.9 | -7612.79 | -7549.54 | 1130 | -29.259 | 100% quoted, 5946 trades |
| 2026-10-21 | 0.07767 | 0.0768 / 6.5 | -47241.28 | -47395.18 | 2420 | -42.704 | 100% quoted, 13763 trades |
| 2026-10-22 | 0.07724 | 0.0850 / 8.0 | -14284.81 | -14767.99 | 1900 | -20.943 | 100% quoted, 13497 trades |
| 2026-10-23 | 0.07514 | 0.0958 / 9.9 | -37735.46 | -37867.06 | 1686 | -53.034 | 100% quoted, 7250 trades |
| 2026-10-26 | 0.07559 | 0.0996 / 11.0 | -5240.29 | -5308.07 | 1040 | -19.956 | 100% quoted, 9506 trades |
| 2026-10-27 | 0.07083 | 0.1011 / 13.5 | -14483.97 | -14641.41 | 1896 | -22.055 | 100% quoted, 12353 trades |
| 2026-10-28 | 0.07165 | 0.1110 / 15.2 | -31726.94 | -31676.03 | 2827 | -37.105 | 100% quoted, 14360 trades |
| 2026-10-29 | 0.06874 | 0.1113 / 17.1 | -78447.10 | -78681.18 | 11138 | -15.240 | 100% quoted, 54450 trades |
| 2026-10-30 | 0.07053 | 0.1515 / 16.2 | -39931.14 | -40085.30 | 9481 | -14.111 | 100% quoted, 22459 trades |
| 2026-11-02 | 0.05372 | 0.1789 / 13.8 | -27436.51 | -27646.05 | 3357 | -24.125 | 100% quoted, 14707 trades |
| 2026-11-03 | 0.05796 | 0.1885 / 13.5 | -13817.08 | -13773.35 | 1798 | -26.543 | 100% quoted, 11721 trades |
| 2026-11-04 | 0.05592 | 0.1876 / 13.6 | -27997.24 | -28948.83 | 5549 | -23.177 | 100% quoted, 20045 trades |
| 2026-11-05 | 0.05309 | 0.1942 / 12.8 | -135518.99 | -136168.92 | 6852 | -44.736 | 100% quoted, 21473 trades |
