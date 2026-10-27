# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 16 (2026-10-02 to 2026-10-26)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27189.14 [-39559.45, -17792.67] dollars (negative); 0 of 16 days positive; 2109 fills a day; 5 s markout -29.332 [-34.823, -24.320] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -27571.23 [-40031.86, -18103.34] dollars (negative); 0 of 16 days positive; 2206 fills a day; 5 s markout -28.666 [-34.013, -23.754] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -28243.10 [-42991.51, -17586.54] | negative | 0/16 | 2096 | -29.097 [-34.543, -24.165] |
| conservative | symmetric | 1 | -31866.97 [-51182.01, -17891.32] | negative | 0/16 | 2070 | -28.498 [-33.905, -23.699] |
| conservative | inventory | 2 | -27189.14 [-39559.45, -17792.67] | negative | 0/16 | 2109 | -29.332 [-34.823, -24.320] |
| conservative | symmetric | 2 | -31616.51 [-50928.14, -17667.20] | negative | 0/16 | 2051 | -28.632 [-34.070, -23.827] |
| conservative | inventory | 4 | -25680.00 [-35566.55, -17588.29] | negative | 0/16 | 2078 | -29.831 [-35.391, -24.809] |
| conservative | symmetric | 4 | -31092.17 [-50348.18, -17376.51] | negative | 0/16 | 2013 | -28.900 [-34.373, -24.093] |
| optimistic | inventory | 1 | -28492.41 [-43319.69, -17764.92] | negative | 0/16 | 2196 | -28.351 [-33.649, -23.534] |
| optimistic | symmetric | 1 | -32122.05 [-51709.10, -17949.55] | negative | 1/16 | 2158 | -27.844 [-33.095, -23.164] |
| optimistic | inventory | 2 | -27571.23 [-40031.86, -18103.34] | negative | 0/16 | 2206 | -28.666 [-34.013, -23.754] |
| optimistic | symmetric | 2 | -31908.21 [-51420.81, -17817.28] | negative | 0/16 | 2136 | -27.991 [-33.279, -23.336] |
| optimistic | inventory | 4 | -25996.68 [-35842.57, -17940.71] | negative | 0/16 | 2178 | -29.065 [-34.475, -24.153] |
| optimistic | symmetric | 4 | -31487.98 [-50853.24, -17582.56] | negative | 0/16 | 2091 | -28.287 [-33.647, -23.544] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3623.87 [-184.76, 8500.84] | not established |
| conservative | 2 | 4427.37 [-1228.68, 11664.57] | not established |
| conservative | 4 | 5412.17 [-1726.50, 15277.13] | not established |
| optimistic | 1 | 3629.65 [-442.07, 8715.64] | not established |
| optimistic | 2 | 4336.98 [-1495.13, 11730.18] | not established |
| optimistic | 4 | 5491.30 [-1753.25, 15446.60] | not established |

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
