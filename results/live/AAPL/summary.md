# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 14 (2026-10-02 to 2026-10-22)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -25730.56 [-31741.16, -21028.26] dollars (negative); 0 of 14 days positive; 4402 fills a day; 5 s markout -19.126 [-22.038, -16.560] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26121.36 [-32060.45, -21440.95] dollars (negative); 0 of 14 days positive; 5133 fills a day; 5 s markout -17.254 [-19.927, -14.945] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -26621.48 [-32805.24, -21815.68] | negative | 0/14 | 4404 | -19.102 [-22.011, -16.538] |
| conservative | symmetric | 1 | -28677.95 [-34560.89, -24005.71] | negative | 0/14 | 4172 | -19.536 [-22.540, -16.823] |
| conservative | inventory | 2 | -25730.56 [-31741.16, -21028.26] | negative | 0/14 | 4402 | -19.126 [-22.038, -16.560] |
| conservative | symmetric | 2 | -28180.53 [-34121.95, -23546.03] | negative | 0/14 | 4050 | -19.947 [-23.008, -17.182] |
| conservative | inventory | 4 | -24485.41 [-30258.67, -19987.17] | negative | 0/14 | 4300 | -19.311 [-22.316, -16.691] |
| conservative | symmetric | 4 | -27399.26 [-33191.29, -22852.88] | negative | 0/14 | 3821 | -20.736 [-23.921, -17.842] |
| optimistic | inventory | 1 | -26981.93 [-33143.87, -22089.06] | negative | 0/14 | 5160 | -17.170 [-19.761, -14.897] |
| optimistic | symmetric | 1 | -29707.80 [-35757.10, -24869.58] | negative | 0/14 | 4874 | -17.577 [-20.297, -15.162] |
| optimistic | inventory | 2 | -26121.36 [-32060.45, -21440.95] | negative | 0/14 | 5133 | -17.254 [-19.927, -14.945] |
| optimistic | symmetric | 2 | -29268.12 [-35353.21, -24441.48] | negative | 0/14 | 4695 | -18.059 [-20.865, -15.536] |
| optimistic | inventory | 4 | -24970.03 [-30611.19, -20516.81] | negative | 0/14 | 4956 | -17.569 [-20.318, -15.213] |
| optimistic | symmetric | 4 | -28197.82 [-34133.61, -23478.10] | negative | 0/14 | 4397 | -18.832 [-21.741, -16.224] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2056.46 [-1105.44, 5276.68] | not established |
| conservative | 2 | 2449.97 [-560.44, 5502.04] | not established |
| conservative | 4 | 2913.85 [249.36, 5530.34] | positive |
| optimistic | 1 | 2725.87 [-668.15, 6137.43] | not established |
| optimistic | 2 | 3146.76 [-87.24, 6451.60] | not established |
| optimistic | 4 | 3227.79 [334.55, 6134.57] | positive |

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
