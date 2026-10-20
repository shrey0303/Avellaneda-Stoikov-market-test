# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 11 (2026-10-02 to 2026-10-19)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -23200.09 [-26689.10, -19861.55] dollars (negative); 0 of 11 days positive; 4343 fills a day; 5 s markout -18.699 [-20.876, -16.979] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -23646.96 [-27258.22, -20243.26] dollars (negative); 0 of 11 days positive; 5080 fills a day; 5 s markout -16.820 [-18.771, -15.256] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -23969.86 [-27474.96, -20615.60] | negative | 0/11 | 4331 | -18.702 [-20.891, -16.959] |
| conservative | symmetric | 1 | -27496.99 [-32119.48, -23961.92] | negative | 0/11 | 4075 | -19.264 [-21.533, -17.409] |
| conservative | inventory | 2 | -23200.09 [-26689.10, -19861.55] | negative | 0/11 | 4343 | -18.699 [-20.876, -16.979] |
| conservative | symmetric | 2 | -26910.89 [-31320.13, -23489.22] | negative | 0/11 | 3951 | -19.691 [-22.051, -17.785] |
| conservative | inventory | 4 | -22239.69 [-25606.45, -18967.54] | negative | 0/11 | 4252 | -18.821 [-21.067, -17.025] |
| conservative | symmetric | 4 | -26092.41 [-30374.47, -22705.89] | negative | 0/11 | 3727 | -20.521 [-22.949, -18.503] |
| optimistic | inventory | 1 | -24321.63 [-28106.73, -20782.85] | negative | 0/11 | 5096 | -16.787 [-18.711, -15.215] |
| optimistic | symmetric | 1 | -28327.63 [-33213.55, -24462.17] | negative | 0/11 | 4784 | -17.263 [-19.260, -15.591] |
| optimistic | inventory | 2 | -23646.96 [-27258.22, -20243.26] | negative | 0/11 | 5080 | -16.820 [-18.771, -15.256] |
| optimistic | symmetric | 2 | -27998.77 [-33010.69, -24213.59] | negative | 0/11 | 4602 | -17.763 [-19.839, -16.029] |
| optimistic | inventory | 4 | -22780.28 [-26178.32, -19524.39] | negative | 0/11 | 4915 | -17.095 [-19.109, -15.479] |
| optimistic | symmetric | 4 | -26961.11 [-31607.18, -23436.88] | negative | 0/11 | 4300 | -18.552 [-20.783, -16.715] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 3527.14 [-439.36, 6960.84] | not established |
| conservative | 2 | 3710.81 [-88.42, 7053.75] | not established |
| conservative | 4 | 3852.72 [413.33, 6831.27] | positive |
| optimistic | 1 | 4006.00 [-366.77, 7816.80] | not established |
| optimistic | 2 | 4351.81 [155.63, 8157.19] | positive |
| optimistic | 4 | 4180.83 [411.36, 7567.32] | positive |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.03590 | 0.1627 / 21.8 | -20422.65 | -20056.01 | 2805 | -21.307 | 100% quoted, 18831 trades |
| 2026-10-05 | 0.03352 | 0.1556 / 24.5 | -23657.69 | -23811.35 | 4159 | -17.189 | 100% quoted, 21277 trades |
| 2026-10-06 | 0.03492 | 0.1547 / 23.4 | -16586.88 | -16698.85 | 3883 | -16.620 | 100% quoted, 17706 trades |
| 2026-10-07 | 0.03494 | 0.1521 / 22.9 | -19191.59 | -19890.24 | 4187 | -16.319 | 100% quoted, 22360 trades |
| 2026-10-08 | 0.03494 | 0.1561 / 22.6 | -22937.02 | -23554.55 | 4768 | -18.093 | 100% quoted, 21964 trades |
| 2026-10-09 | 0.03552 | 0.1602 / 22.4 | -30969.88 | -31701.81 | 5736 | -17.518 | 100% quoted, 30585 trades |
| 2026-10-12 | 0.03760 | 0.1646 / 20.4 | -27309.15 | -27596.35 | 3327 | -26.526 | 100% quoted, 16325 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.04355 | 0.1628 / 18.8 | -19274.68 | -20392.63 | 5006 | -14.498 | 100% quoted, 32766 trades |
| 2026-10-15 | 0.04310 | 0.1754 / 19.3 | -13261.23 | -13383.33 | 2902 | -18.648 | 100% quoted, 21362 trades |
| 2026-10-16 | 0.04253 | 0.1672 / 19.7 | -29159.03 | -29472.61 | 6166 | -15.879 | 100% quoted, 29380 trades |
| 2026-10-19 | 0.04269 | 0.1770 / 19.8 | -32431.15 | -33558.76 | 4833 | -23.095 | 100% quoted, 21058 trades |
