# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 18 (2026-10-02 to 2026-10-28)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27786.84 [-33318.98, -23041.02] dollars (negative); 0 of 18 days positive; 4350 fills a day; 5 s markout -20.945 [-23.848, -18.260] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28322.23 [-33865.61, -23580.82] dollars (negative); 0 of 18 days positive; 5045 fills a day; 5 s markout -18.966 [-21.695, -16.494] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -28638.10 [-34227.88, -23867.72] | negative | 0/18 | 4336 | -20.965 [-23.900, -18.318] |
| conservative | symmetric | 1 | -30511.92 [-35981.16, -25897.14] | negative | 0/18 | 4088 | -21.563 [-24.602, -18.681] |
| conservative | inventory | 2 | -27786.84 [-33318.98, -23041.02] | negative | 0/18 | 4350 | -20.945 [-23.848, -18.260] |
| conservative | symmetric | 2 | -30110.83 [-35537.30, -25486.69] | negative | 0/18 | 3978 | -21.952 [-25.045, -19.033] |
| conservative | inventory | 4 | -26655.04 [-32049.67, -22074.35] | negative | 0/18 | 4273 | -21.107 [-24.068, -18.419] |
| conservative | symmetric | 4 | -29284.68 [-34537.55, -24832.89] | negative | 0/18 | 3768 | -22.741 [-25.896, -19.773] |
| optimistic | inventory | 1 | -29090.92 [-34737.25, -24201.25] | negative | 0/18 | 5053 | -18.932 [-21.647, -16.485] |
| optimistic | symmetric | 1 | -31647.38 [-37368.90, -26901.99] | negative | 0/18 | 4765 | -19.417 [-22.237, -16.830] |
| optimistic | inventory | 2 | -28322.23 [-33865.61, -23580.82] | negative | 0/18 | 5045 | -18.966 [-21.695, -16.494] |
| optimistic | symmetric | 2 | -31241.81 [-36869.03, -26470.70] | negative | 0/18 | 4598 | -19.933 [-22.812, -17.291] |
| optimistic | inventory | 4 | -27228.39 [-32652.24, -22588.85] | negative | 0/18 | 4902 | -19.231 [-21.960, -16.769] |
| optimistic | symmetric | 4 | -30180.47 [-35636.14, -25532.09] | negative | 0/18 | 4316 | -20.745 [-23.677, -18.014] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1873.82 [-721.11, 4396.33] | not established |
| conservative | 2 | 2323.98 [-149.14, 4701.56] | not established |
| conservative | 4 | 2629.64 [481.02, 4767.21] | positive |
| optimistic | 1 | 2556.45 [-179.54, 5265.07] | not established |
| optimistic | 2 | 2919.58 [280.82, 5620.28] | positive |
| optimistic | 4 | 2952.08 [572.72, 5382.74] | positive |

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
| 2026-10-20 | 0.04106 | 0.1818 / 19.7 | -58622.64 | -57997.89 | 4256 | -33.597 | 100% quoted, 19216 trades |
| 2026-10-21 | 0.05390 | 0.1790 / 20.8 | -23484.60 | -23720.65 | 4470 | -16.976 | 100% quoted, 19414 trades |
| 2026-10-22 | 0.05449 | 0.1601 / 19.4 | -22919.69 | -23863.97 | 5135 | -11.504 | 100% quoted, 21118 trades |
| 2026-10-23 | 0.05418 | 0.1687 / 17.7 | -34143.81 | -34924.81 | 4547 | -24.544 | 100% quoted, 19025 trades |
| 2026-10-26 | 0.06266 | 0.1529 / 17.0 | -49956.47 | -51251.85 | 5340 | -30.478 | 100% quoted, 22165 trades |
| 2026-10-27 | 0.06605 | 0.1548 / 16.5 | -37592.69 | -38932.58 | 3871 | -31.369 | 100% quoted, 23909 trades |
| 2026-10-28 | 0.05709 | 0.1607 / 17.1 | -18242.35 | -18991.81 | 2915 | -22.848 | 100% quoted, 19597 trades |
