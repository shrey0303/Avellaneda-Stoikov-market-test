# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 18 (2026-10-02 to 2026-10-28)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26735.40 [-37889.17, -18124.05] dollars (negative); 0 of 18 days positive; 2137 fills a day; 5 s markout -29.359 [-34.058, -24.728] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -27080.95 [-38250.65, -18437.37] dollars (negative); 0 of 18 days positive; 2251 fills a day; 5 s markout -28.534 [-33.045, -24.014] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27741.56 [-40889.43, -17807.65] | negative | 0/18 | 2120 | -29.136 [-33.794, -24.483] |
| conservative | symmetric | 1 | -31018.66 [-48092.85, -18554.80] | negative | 0/18 | 2087 | -28.658 [-33.304, -24.032] |
| conservative | inventory | 2 | -26735.40 [-37889.17, -18124.05] | negative | 0/18 | 2137 | -29.359 [-34.058, -24.728] |
| conservative | symmetric | 2 | -30758.36 [-47773.90, -18335.94] | negative | 0/18 | 2064 | -28.846 [-33.499, -24.232] |
| conservative | inventory | 4 | -25396.92 [-34291.70, -17980.65] | negative | 0/18 | 2109 | -29.809 [-34.546, -25.134] |
| conservative | symmetric | 4 | -30213.36 [-47178.38, -17776.67] | negative | 0/18 | 2019 | -29.218 [-33.895, -24.636] |
| optimistic | inventory | 1 | -27959.97 [-41103.71, -17984.37] | negative | 0/18 | 2239 | -28.245 [-32.680, -23.706] |
| optimistic | symmetric | 1 | -31279.48 [-48571.24, -18603.54] | negative | 1/18 | 2194 | -27.806 [-32.312, -23.329] |
| optimistic | inventory | 2 | -27080.95 [-38250.65, -18437.37] | negative | 0/18 | 2251 | -28.534 [-33.045, -24.014] |
| optimistic | symmetric | 2 | -31044.94 [-48250.96, -18421.69] | negative | 0/18 | 2166 | -28.016 [-32.541, -23.552] |
| optimistic | inventory | 4 | -25708.75 [-34627.88, -18298.16] | negative | 0/18 | 2226 | -28.898 [-33.445, -24.376] |
| optimistic | symmetric | 4 | -30614.89 [-47652.84, -18065.84] | negative | 0/18 | 2111 | -28.419 [-33.058, -23.839] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3277.10 [-192.53, 7476.79] | not established |
| conservative | 2 | 4022.96 [-1154.45, 10308.42] | not established |
| conservative | 4 | 4816.44 [-1754.75, 13392.75] | not established |
| optimistic | 1 | 3319.51 [-278.48, 7701.12] | not established |
| optimistic | 2 | 3963.99 [-1369.60, 10334.48] | not established |
| optimistic | 4 | 4906.14 [-1759.89, 13489.89] | not established |

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
