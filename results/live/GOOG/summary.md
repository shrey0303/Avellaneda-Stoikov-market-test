# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 17 (2026-10-02 to 2026-10-27)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26441.78 [-38453.66, -17541.43] dollars (negative); 0 of 17 days positive; 2097 fills a day; 5 s markout -28.904 [-33.877, -24.248] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26810.65 [-38942.37, -17905.02] dollars (negative); 0 of 17 days positive; 2200 fills a day; 5 s markout -28.188 [-33.007, -23.694] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27562.89 [-42036.01, -17477.96] | negative | 0/17 | 2082 | -28.662 [-33.609, -24.100] |
| conservative | symmetric | 1 | -31268.29 [-49953.23, -18146.50] | negative | 0/17 | 2054 | -28.113 [-33.021, -23.633] |
| conservative | inventory | 2 | -26441.78 [-38453.66, -17541.43] | negative | 0/17 | 2097 | -28.904 [-33.877, -24.248] |
| conservative | symmetric | 2 | -30980.57 [-49554.82, -17914.93] | negative | 0/17 | 2033 | -28.271 [-33.153, -23.764] |
| conservative | inventory | 4 | -24973.83 [-34394.26, -17491.21] | negative | 0/17 | 2066 | -29.399 [-34.465, -24.697] |
| conservative | symmetric | 4 | -30408.15 [-48939.45, -17385.90] | negative | 0/17 | 1993 | -28.572 [-33.507, -24.080] |
| optimistic | inventory | 1 | -27773.20 [-42170.55, -17633.62] | negative | 0/17 | 2191 | -27.874 [-32.691, -23.404] |
| optimistic | symmetric | 1 | -31544.36 [-50546.58, -18164.72] | negative | 1/17 | 2151 | -27.384 [-32.178, -22.928] |
| optimistic | inventory | 2 | -26810.65 [-38942.37, -17905.02] | negative | 0/17 | 2200 | -28.188 [-33.007, -23.694] |
| optimistic | symmetric | 2 | -31330.55 [-50261.73, -18032.47] | negative | 0/17 | 2126 | -27.562 [-32.327, -23.126] |
| optimistic | inventory | 4 | -25279.09 [-34736.88, -17745.76] | negative | 0/17 | 2173 | -28.575 [-33.531, -23.989] |
| optimistic | symmetric | 4 | -30881.60 [-49520.41, -17729.33] | negative | 0/17 | 2077 | -27.891 [-32.744, -23.427] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3705.40 [19.83, 8345.33] | positive |
| conservative | 2 | 4538.79 [-936.07, 11546.25] | not established |
| conservative | 4 | 5434.33 [-1544.60, 14779.82] | not established |
| optimistic | 1 | 3771.16 [-115.99, 8685.36] | not established |
| optimistic | 2 | 4519.90 [-1214.82, 11626.84] | not established |
| optimistic | 4 | 5602.51 [-1507.39, 15066.01] | not established |

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
