# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 16 (2026-10-02 to 2026-10-26)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27770.51 [-33741.38, -22870.77] dollars (negative); 0 of 16 days positive; 4470 fills a day; 5 s markout -20.174 [-23.291, -17.495] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28242.23 [-34187.20, -23306.18] dollars (negative); 0 of 16 days positive; 5176 fills a day; 5 s markout -18.312 [-21.166, -15.862] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -28620.29 [-34685.91, -23718.32] | negative | 0/16 | 4457 | -20.184 [-23.282, -17.527] |
| conservative | symmetric | 1 | -30359.11 [-36044.22, -25480.53] | negative | 0/16 | 4206 | -20.698 [-23.869, -17.834] |
| conservative | inventory | 2 | -27770.51 [-33741.38, -22870.77] | negative | 0/16 | 4470 | -20.174 [-23.291, -17.495] |
| conservative | symmetric | 2 | -29991.37 [-35811.12, -25073.76] | negative | 0/16 | 4090 | -21.087 [-24.309, -18.178] |
| conservative | inventory | 4 | -26588.43 [-32355.68, -21839.63] | negative | 0/16 | 4384 | -20.362 [-23.536, -17.644] |
| conservative | symmetric | 4 | -29233.46 [-34851.70, -24493.93] | negative | 0/16 | 3870 | -21.853 [-25.132, -18.847] |
| optimistic | inventory | 1 | -29005.16 [-35098.04, -24013.73] | negative | 0/16 | 5188 | -18.257 [-21.089, -15.839] |
| optimistic | symmetric | 1 | -31429.61 [-37363.19, -26411.64] | negative | 0/16 | 4892 | -18.696 [-21.575, -16.133] |
| optimistic | inventory | 2 | -28242.23 [-34187.20, -23306.18] | negative | 0/16 | 5176 | -18.312 [-21.166, -15.862] |
| optimistic | symmetric | 2 | -31007.09 [-37024.17, -26013.33] | negative | 0/16 | 4721 | -19.183 [-22.135, -16.538] |
| optimistic | inventory | 4 | -27120.96 [-32870.18, -22406.37] | negative | 0/16 | 5024 | -18.575 [-21.499, -16.098] |
| optimistic | symmetric | 4 | -29987.91 [-35816.07, -25006.36] | negative | 0/16 | 4431 | -19.956 [-22.977, -17.206] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1738.82 [-1076.44, 4625.03] | not established |
| conservative | 2 | 2220.86 [-397.80, 4957.41] | not established |
| conservative | 4 | 2645.04 [292.85, 5011.44] | positive |
| optimistic | 1 | 2424.45 [-626.40, 5410.28] | not established |
| optimistic | 2 | 2764.86 [-137.68, 5760.13] | not established |
| optimistic | 4 | 2866.96 [255.33, 5514.18] | positive |

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
