# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 17 (2026-10-02 to 2026-10-27)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28348.28 [-34221.15, -23359.35] dollars (negative); 0 of 17 days positive; 4435 fills a day; 5 s markout -20.833 [-23.841, -18.142] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28871.07 [-34646.61, -23853.19] dollars (negative); 0 of 17 days positive; 5139 fills a day; 5 s markout -18.879 [-21.657, -16.397] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29220.77 [-35223.64, -24196.73] | negative | 0/17 | 4425 | -20.828 [-23.815, -18.140] |
| conservative | symmetric | 1 | -31280.97 [-36911.53, -26478.27] | negative | 0/17 | 4168 | -21.458 [-24.565, -18.566] |
| conservative | inventory | 2 | -28348.28 [-34221.15, -23359.35] | negative | 0/17 | 4435 | -20.833 [-23.841, -18.142] |
| conservative | symmetric | 2 | -30884.66 [-36547.71, -26038.26] | negative | 0/17 | 4056 | -21.842 [-24.985, -18.934] |
| conservative | inventory | 4 | -27189.01 [-32776.72, -22237.50] | negative | 0/17 | 4352 | -21.003 [-24.032, -18.274] |
| conservative | symmetric | 4 | -30057.93 [-35532.32, -25394.02] | negative | 0/17 | 3841 | -22.618 [-25.855, -19.644] |
| optimistic | inventory | 1 | -29655.80 [-35638.99, -24461.45] | negative | 0/17 | 5149 | -18.843 [-21.534, -16.375] |
| optimistic | symmetric | 1 | -32400.93 [-38276.19, -27394.46] | negative | 0/17 | 4851 | -19.343 [-22.176, -16.719] |
| optimistic | inventory | 2 | -28871.07 [-34646.61, -23853.19] | negative | 0/17 | 5139 | -18.879 [-21.657, -16.397] |
| optimistic | symmetric | 2 | -31970.78 [-37837.92, -26951.42] | negative | 0/17 | 4682 | -19.854 [-22.756, -17.175] |
| optimistic | inventory | 4 | -27760.65 [-33292.02, -22820.66] | negative | 0/17 | 4990 | -19.158 [-21.973, -16.657] |
| optimistic | symmetric | 4 | -30896.51 [-36554.82, -26032.92] | negative | 0/17 | 4396 | -20.656 [-23.639, -17.901] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2060.20 [-731.13, 4983.55] | not established |
| conservative | 2 | 2536.38 [-71.79, 5237.82] | not established |
| conservative | 4 | 2868.92 [560.74, 5216.02] | positive |
| optimistic | 1 | 2745.13 [-243.93, 5761.57] | not established |
| optimistic | 2 | 3099.70 [211.81, 6038.67] | positive |
| optimistic | 4 | 3135.86 [500.56, 5761.93] | positive |

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
