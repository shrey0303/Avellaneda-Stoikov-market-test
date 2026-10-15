# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 9 (2026-10-02 to 2026-10-15)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -21512.31 [-24950.50, -18516.01] dollars (negative); 0 of 9 days positive; 4086 fills a day; 5 s markout -18.524 [-20.886, -16.689] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -21898.35 [-25472.12, -18798.78] dollars (negative); 0 of 9 days positive; 4818 fills a day; 5 s markout -16.553 [-18.648, -14.967] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -22260.66 [-25708.00, -19311.92] | negative | 0/9 | 4073 | -18.514 [-20.850, -16.742] |
| conservative | symmetric | 1 | -27852.55 [-33748.21, -23709.03] | negative | 0/9 | 3873 | -19.051 [-21.439, -17.107] |
| conservative | inventory | 2 | -21512.31 [-24950.50, -18516.01] | negative | 0/9 | 4086 | -18.524 [-20.886, -16.689] |
| conservative | symmetric | 2 | -27319.06 [-33062.25, -23255.40] | negative | 0/9 | 3746 | -19.505 [-22.038, -17.481] |
| conservative | inventory | 4 | -20697.11 [-24128.33, -17668.81] | negative | 0/9 | 3986 | -18.701 [-21.224, -16.776] |
| conservative | symmetric | 4 | -26391.74 [-31772.07, -22307.39] | negative | 0/9 | 3521 | -20.392 [-23.104, -18.194] |
| optimistic | inventory | 1 | -22479.50 [-26220.75, -19366.70] | negative | 0/9 | 4845 | -16.492 [-18.468, -14.952] |
| optimistic | symmetric | 1 | -28636.31 [-34924.43, -24194.14] | negative | 0/9 | 4588 | -16.988 [-19.010, -15.324] |
| optimistic | inventory | 2 | -21898.35 [-25472.12, -18798.78] | negative | 0/9 | 4818 | -16.553 [-18.648, -14.967] |
| optimistic | symmetric | 2 | -28254.37 [-34702.66, -23764.65] | negative | 0/9 | 4400 | -17.511 [-19.651, -15.776] |
| optimistic | inventory | 4 | -21213.17 [-24655.41, -18149.63] | negative | 0/9 | 4648 | -16.880 [-19.044, -15.206] |
| optimistic | symmetric | 4 | -27243.51 [-33169.64, -23082.53] | negative | 0/9 | 4096 | -18.330 [-20.633, -16.467] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 5591.89 [2969.21, 8624.05] | positive |
| conservative | 2 | 5806.75 [3414.02, 8636.04] | positive |
| conservative | 4 | 5694.63 [3566.29, 8202.62] | positive |
| optimistic | 1 | 6156.81 [3326.44, 9370.39] | positive |
| optimistic | 2 | 6356.02 [3518.80, 9859.31] | positive |
| optimistic | 4 | 6030.35 [3517.83, 9059.31] | positive |

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
