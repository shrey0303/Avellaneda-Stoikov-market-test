# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 21 (2026-10-02 to 2026-11-02)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29859.61 [-41090.49, -21140.49] dollars (negative); 0 of 21 days positive; 2974 fills a day; 5 s markout -27.711 [-32.255, -23.340] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -30184.27 [-41423.70, -21490.42] dollars (negative); 0 of 21 days positive; 3155 fills a day; 5 s markout -26.895 [-31.331, -22.674] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -31308.41 [-44333.01, -21338.21] | negative | 0/21 | 2991 | -27.530 [-32.018, -23.192] |
| conservative | symmetric | 1 | -39883.22 [-64380.33, -22382.72] | negative | 0/21 | 2926 | -27.041 [-31.512, -22.682] |
| conservative | inventory | 2 | -29859.61 [-41090.49, -21140.49] | negative | 0/21 | 2974 | -27.711 [-32.255, -23.340] |
| conservative | symmetric | 2 | -39429.27 [-63571.79, -22117.86] | negative | 0/21 | 2882 | -27.226 [-31.690, -22.861] |
| conservative | inventory | 4 | -28072.77 [-37009.07, -20769.29] | negative | 0/21 | 2871 | -28.151 [-32.746, -23.800] |
| conservative | symmetric | 4 | -38824.10 [-63036.32, -21481.19] | negative | 0/21 | 2807 | -27.593 [-32.133, -23.176] |
| optimistic | inventory | 1 | -31523.37 [-44563.07, -21486.34] | negative | 0/21 | 3181 | -26.642 [-31.013, -22.447] |
| optimistic | symmetric | 1 | -40442.35 [-65421.18, -22539.07] | negative | 1/21 | 3104 | -26.208 [-30.600, -21.962] |
| optimistic | inventory | 2 | -30184.27 [-41423.70, -21490.42] | negative | 0/21 | 3155 | -26.895 [-31.331, -22.674] |
| optimistic | symmetric | 2 | -40192.46 [-65206.94, -22305.66] | negative | 0/21 | 3051 | -26.420 [-30.845, -22.165] |
| optimistic | inventory | 4 | -28411.64 [-37343.31, -21024.63] | negative | 0/21 | 3056 | -27.257 [-31.770, -23.019] |
| optimistic | symmetric | 4 | -39389.24 [-63832.86, -21859.98] | negative | 0/21 | 2962 | -26.804 [-31.257, -22.497] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 8574.81 [194.64, 23250.92] | positive |
| conservative | 2 | 9569.65 [-307.46, 25511.07] | not established |
| conservative | 4 | 10751.33 [-482.90, 27943.30] | not established |
| optimistic | 1 | 8918.98 [148.74, 24283.23] | positive |
| optimistic | 2 | 10008.20 [-307.84, 26935.36] | not established |
| optimistic | 4 | 10977.60 [-566.42, 28424.12] | not established |

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
