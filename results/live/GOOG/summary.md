# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 20 (2026-10-02 to 2026-10-30)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29980.77 [-41019.73, -20988.07] dollars (negative); 0 of 20 days positive; 2954 fills a day; 5 s markout -27.891 [-32.471, -23.459] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -30311.18 [-41482.50, -21285.04] dollars (negative); 0 of 20 days positive; 3130 fills a day; 5 s markout -27.086 [-31.496, -22.782] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -31482.64 [-44871.35, -20923.75] | negative | 0/20 | 2976 | -27.677 [-32.208, -23.297] |
| conservative | symmetric | 1 | -40415.94 [-64430.83, -22177.10] | negative | 0/20 | 2924 | -27.183 [-31.740, -22.786] |
| conservative | inventory | 2 | -29980.77 [-41019.73, -20988.07] | negative | 0/20 | 2954 | -27.891 [-32.471, -23.459] |
| conservative | symmetric | 2 | -39981.62 [-63748.98, -21846.44] | negative | 0/20 | 2881 | -27.365 [-31.947, -22.950] |
| conservative | inventory | 4 | -28139.73 [-37165.96, -20615.66] | negative | 0/20 | 2847 | -28.347 [-32.989, -23.886] |
| conservative | symmetric | 4 | -39373.85 [-63062.81, -21248.95] | negative | 0/20 | 2806 | -27.721 [-32.392, -23.270] |
| optimistic | inventory | 1 | -31689.12 [-44929.18, -21178.98] | negative | 0/20 | 3160 | -26.820 [-31.215, -22.539] |
| optimistic | symmetric | 1 | -40935.81 [-65532.22, -22329.85] | negative | 1/20 | 3096 | -26.359 [-30.751, -22.116] |
| optimistic | inventory | 2 | -30311.18 [-41482.50, -21285.04] | negative | 0/20 | 3130 | -27.086 [-31.496, -22.782] |
| optimistic | symmetric | 2 | -40709.85 [-65304.42, -22094.92] | negative | 0/20 | 3045 | -26.569 [-31.000, -22.323] |
| optimistic | inventory | 4 | -28473.17 [-37563.37, -20897.09] | negative | 0/20 | 3028 | -27.468 [-31.887, -23.088] |
| optimistic | symmetric | 4 | -39916.95 [-63881.63, -21621.32] | negative | 0/20 | 2957 | -26.957 [-31.470, -22.615] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 8933.29 [-32.80, 22427.97] | not established |
| conservative | 2 | 10000.85 [-342.29, 24702.31] | not established |
| conservative | 4 | 11234.12 [-697.28, 27753.44] | not established |
| optimistic | 1 | 9246.69 [-96.48, 23318.67] | not established |
| optimistic | 2 | 10398.67 [-474.11, 25913.63] | not established |
| optimistic | 4 | 11443.77 [-634.86, 28287.87] | not established |

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
