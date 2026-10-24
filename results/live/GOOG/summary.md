# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 15 (2026-10-02 to 2026-10-23)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28652.40 [-40912.08, -18941.90] dollars (negative); 0 of 15 days positive; 2180 fills a day; 5 s markout -29.957 [-35.280, -24.803] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29055.44 [-41487.45, -19333.63] dollars (negative); 0 of 15 days positive; 2276 fills a day; 5 s markout -29.305 [-34.441, -24.310] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29900.20 [-44658.73, -18700.57] | negative | 0/15 | 2168 | -29.695 [-35.031, -24.531] |
| conservative | symmetric | 1 | -33971.32 [-53424.19, -19534.43] | negative | 0/15 | 2141 | -29.029 [-34.471, -24.095] |
| conservative | inventory | 2 | -28652.40 [-40912.08, -18941.90] | negative | 0/15 | 2180 | -29.957 [-35.280, -24.803] |
| conservative | symmetric | 2 | -33703.02 [-53062.76, -19299.45] | negative | 0/15 | 2122 | -29.146 [-34.619, -24.211] |
| conservative | inventory | 4 | -26994.38 [-36862.64, -18964.20] | negative | 0/15 | 2150 | -30.457 [-35.784, -25.278] |
| conservative | symmetric | 4 | -33148.49 [-52437.75, -18785.30] | negative | 0/15 | 2085 | -29.388 [-34.953, -24.437] |
| optimistic | inventory | 1 | -30139.58 [-44942.71, -18923.40] | negative | 0/15 | 2266 | -28.979 [-34.118, -23.953] |
| optimistic | symmetric | 1 | -34267.46 [-53712.81, -19691.38] | negative | 0/15 | 2228 | -28.405 [-33.669, -23.561] |
| optimistic | inventory | 2 | -29055.44 [-41487.45, -19333.63] | negative | 0/15 | 2276 | -29.305 [-34.441, -24.310] |
| optimistic | symmetric | 2 | -34033.12 [-53517.84, -19477.17] | negative | 0/15 | 2206 | -28.536 [-33.787, -23.699] |
| optimistic | inventory | 4 | -27309.02 [-37181.93, -19251.66] | negative | 0/15 | 2247 | -29.759 [-34.906, -24.784] |
| optimistic | symmetric | 4 | -33576.92 [-52817.39, -19140.30] | negative | 0/15 | 2162 | -28.811 [-34.230, -23.904] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4071.12 [7.11, 9007.24] | positive |
| conservative | 2 | 5050.63 [-886.88, 12441.74] | not established |
| conservative | 4 | 6154.11 [-1401.51, 16185.15] | not established |
| optimistic | 1 | 4127.88 [-156.07, 9303.79] | not established |
| optimistic | 2 | 4977.68 [-1168.33, 12488.48] | not established |
| optimistic | 4 | 6267.89 [-1429.36, 16367.48] | not established |

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
