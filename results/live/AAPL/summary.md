# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 22 (2026-10-02 to 2026-11-03)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -34688.69 [-46360.32, -25511.42] dollars (negative); 0 of 22 days positive; 5091 fills a day; 5 s markout -20.744 [-23.291, -18.449] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -35286.29 [-46951.68, -26031.68] dollars (negative); 0 of 22 days positive; 5808 fills a day; 5 s markout -18.856 [-21.178, -16.720] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -35560.70 [-47437.23, -26296.30] | negative | 0/22 | 5082 | -20.765 [-23.292, -18.480] |
| conservative | symmetric | 1 | -35428.29 [-45612.54, -27391.44] | negative | 0/22 | 4788 | -21.210 [-23.846, -18.778] |
| conservative | inventory | 2 | -34688.69 [-46360.32, -25511.42] | negative | 0/22 | 5091 | -20.744 [-23.291, -18.449] |
| conservative | symmetric | 2 | -34965.88 [-45135.57, -26983.61] | negative | 0/22 | 4668 | -21.593 [-24.245, -19.153] |
| conservative | inventory | 4 | -33169.74 [-44232.33, -24457.11] | negative | 0/22 | 4984 | -20.926 [-23.527, -18.616] |
| conservative | symmetric | 4 | -33868.23 [-43502.02, -26254.01] | negative | 0/22 | 4442 | -22.351 [-25.043, -19.905] |
| optimistic | inventory | 1 | -36063.96 [-47858.40, -26700.03] | negative | 0/22 | 5828 | -18.826 [-21.083, -16.677] |
| optimistic | symmetric | 1 | -36616.13 [-47070.59, -28574.62] | negative | 0/22 | 5512 | -19.157 [-21.539, -16.937] |
| optimistic | inventory | 2 | -35286.29 [-46951.68, -26031.68] | negative | 0/22 | 5808 | -18.856 [-21.178, -16.720] |
| optimistic | symmetric | 2 | -36155.08 [-46471.11, -28146.40] | negative | 0/22 | 5336 | -19.640 [-22.095, -17.375] |
| optimistic | inventory | 4 | -33846.36 [-45064.67, -25030.88] | negative | 0/22 | 5639 | -19.150 [-21.501, -16.983] |
| optimistic | symmetric | 4 | -34986.24 [-44996.84, -27118.58] | negative | 0/22 | 5038 | -20.412 [-22.914, -18.074] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -132.41 [-3367.59, 2990.49] | not established |
| conservative | 2 | 277.18 [-2907.10, 3313.47] | not established |
| conservative | 4 | 698.49 [-2233.25, 3437.60] | not established |
| optimistic | 1 | 552.16 [-2637.09, 3702.90] | not established |
| optimistic | 2 | 868.79 [-2337.03, 4091.43] | not established |
| optimistic | 4 | 1139.87 [-1622.62, 3920.86] | not established |

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
| 2026-10-29 | 0.05757 | 0.1600 / 18.0 | -11580.52 | -11787.24 | 2538 | -16.161 | 100% quoted, 22448 trades |
| 2026-10-30 | 0.05669 | 0.1551 / 20.6 | -64029.90 | -65720.71 | 9404 | -20.676 | 100% quoted, 40818 trades |
| 2026-11-02 | 0.05117 | 0.1819 / 20.2 | -62266.35 | -63460.68 | 9692 | -22.000 | 100% quoted, 39739 trades |
| 2026-11-03 | 0.04913 | 0.2006 / 19.3 | -125111.33 | -125529.76 | 12054 | -20.532 | 100% quoted, 37510 trades |
