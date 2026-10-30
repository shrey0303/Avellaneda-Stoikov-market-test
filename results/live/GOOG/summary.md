# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 19 (2026-10-02 to 2026-10-29)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -29457.07 [-40751.56, -19872.46] dollars (negative); 0 of 19 days positive; 2611 fills a day; 5 s markout -28.616 [-33.491, -24.111] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -29796.75 [-41233.24, -20180.88] dollars (negative); 0 of 19 days positive; 2772 fills a day; 5 s markout -27.791 [-32.487, -23.401] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -30947.71 [-44336.87, -19663.11] | negative | 0/19 | 2615 | -28.395 [-33.185, -23.915] |
| conservative | symmetric | 1 | -40646.65 [-65974.42, -20865.92] | negative | 0/19 | 2568 | -27.944 [-32.734, -23.452] |
| conservative | inventory | 2 | -29457.07 [-40751.56, -19872.46] | negative | 0/19 | 2611 | -28.616 [-33.491, -24.111] |
| conservative | symmetric | 2 | -40245.92 [-65446.35, -20675.70] | negative | 0/19 | 2530 | -28.132 [-32.932, -23.664] |
| conservative | inventory | 4 | -27657.98 [-36820.08, -19558.90] | negative | 0/19 | 2528 | -29.076 [-34.007, -24.567] |
| conservative | symmetric | 4 | -39696.04 [-64896.85, -20251.90] | negative | 0/19 | 2462 | -28.503 [-33.389, -23.942] |
| optimistic | inventory | 1 | -31148.27 [-44554.13, -19837.99] | negative | 0/19 | 2787 | -27.508 [-32.149, -23.160] |
| optimistic | symmetric | 1 | -41172.61 [-67104.42, -21041.28] | negative | 1/19 | 2727 | -27.092 [-31.766, -22.797] |
| optimistic | inventory | 2 | -29796.75 [-41233.24, -20180.88] | negative | 0/19 | 2772 | -27.791 [-32.487, -23.401] |
| optimistic | symmetric | 2 | -40975.84 [-67065.64, -20884.65] | negative | 0/19 | 2680 | -27.306 [-31.971, -22.993] |
| optimistic | inventory | 4 | -27974.69 [-37135.62, -19785.23] | negative | 0/19 | 2695 | -28.168 [-32.884, -23.761] |
| optimistic | symmetric | 4 | -40229.06 [-65654.14, -20573.24] | negative | 0/19 | 2600 | -27.709 [-32.465, -23.294] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 9698.94 [399.57, 24326.09] | positive |
| conservative | 2 | 10788.86 [-57.95, 26949.63] | not established |
| conservative | 4 | 12038.06 [-464.23, 30269.27] | not established |
| optimistic | 1 | 10024.33 [241.15, 25287.81] | positive |
| optimistic | 2 | 11179.09 [-258.35, 28240.60] | not established |
| optimistic | 4 | 12254.37 [-532.31, 30626.87] | not established |

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
