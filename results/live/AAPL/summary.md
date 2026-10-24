# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 15 (2026-10-02 to 2026-10-23)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -26291.44 [-32091.17, -21704.25] dollars (negative); 0 of 15 days positive; 4412 fills a day; 5 s markout -19.487 [-22.354, -16.988] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26708.26 [-32399.03, -22130.58] dollars (negative); 0 of 15 days positive; 5131 fills a day; 5 s markout -17.621 [-20.296, -15.358] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27174.46 [-33164.01, -22502.62] | negative | 0/15 | 4411 | -19.481 [-22.329, -17.013] |
| conservative | symmetric | 1 | -29069.83 [-34509.28, -24756.36] | negative | 0/15 | 4179 | -19.948 [-22.799, -17.332] |
| conservative | inventory | 2 | -26291.44 [-32091.17, -21704.25] | negative | 0/15 | 4412 | -19.487 [-22.354, -16.988] |
| conservative | symmetric | 2 | -28683.23 [-34210.18, -24268.26] | negative | 0/15 | 4059 | -20.353 [-23.263, -17.711] |
| conservative | inventory | 4 | -25061.91 [-30519.13, -20674.48] | negative | 0/15 | 4313 | -19.695 [-22.698, -17.111] |
| conservative | symmetric | 4 | -27937.51 [-33312.26, -23623.72] | negative | 0/15 | 3834 | -21.138 [-24.116, -18.358] |
| optimistic | inventory | 1 | -27544.42 [-33585.92, -22790.11] | negative | 0/15 | 5154 | -17.549 [-20.147, -15.328] |
| optimistic | symmetric | 1 | -30142.99 [-35872.03, -25758.58] | negative | 0/15 | 4871 | -17.995 [-20.680, -15.634] |
| optimistic | inventory | 2 | -26708.26 [-32399.03, -22130.58] | negative | 0/15 | 5131 | -17.621 [-20.296, -15.358] |
| optimistic | symmetric | 2 | -29712.41 [-35474.11, -25314.47] | negative | 0/15 | 4695 | -18.479 [-21.218, -16.050] |
| optimistic | inventory | 4 | -25546.91 [-30897.12, -21237.97] | negative | 0/15 | 4962 | -17.929 [-20.660, -15.588] |
| optimistic | symmetric | 4 | -28673.83 [-34259.96, -24277.30] | negative | 0/15 | 4400 | -19.240 [-22.001, -16.724] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1895.37 [-1141.38, 5014.27] | not established |
| conservative | 2 | 2391.78 [-438.83, 5283.25] | not established |
| conservative | 4 | 2875.60 [413.02, 5322.22] | positive |
| optimistic | 1 | 2598.57 [-638.38, 5896.99] | not established |
| optimistic | 2 | 3004.15 [-64.49, 6281.68] | not established |
| optimistic | 4 | 3126.91 [433.45, 5888.74] | positive |

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
