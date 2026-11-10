# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 26 (2026-10-02 to 2026-11-09)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -45191.50 [-59198.97, -32935.51] dollars (negative); 0 of 26 days positive; 5815 fills a day; 5 s markout -22.844 [-25.964, -20.124] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -45902.83 [-60042.65, -33508.59] dollars (negative); 0 of 26 days positive; 6525 fills a day; 5 s markout -21.024 [-24.140, -18.423] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -46160.93 [-60408.31, -33748.04] | negative | 0/26 | 5778 | -22.937 [-26.150, -20.163] |
| conservative | symmetric | 1 | -39117.42 [-49037.15, -30362.61] | negative | 0/26 | 5420 | -23.397 [-26.712, -20.519] |
| conservative | inventory | 2 | -45191.50 [-59198.97, -32935.51] | negative | 0/26 | 5815 | -22.844 [-25.964, -20.124] |
| conservative | symmetric | 2 | -38758.49 [-48727.04, -29944.46] | negative | 0/26 | 5298 | -23.780 [-27.087, -20.889] |
| conservative | inventory | 4 | -43309.81 [-56690.66, -31660.07] | negative | 0/26 | 5725 | -22.961 [-26.073, -20.249] |
| conservative | symmetric | 4 | -37656.89 [-47192.48, -29148.59] | negative | 0/26 | 5069 | -24.524 [-27.840, -21.571] |
| optimistic | inventory | 1 | -46789.25 [-61107.80, -34201.25] | negative | 0/26 | 6517 | -21.056 [-24.230, -18.405] |
| optimistic | symmetric | 1 | -39985.08 [-49767.36, -31101.09] | negative | 1/26 | 6140 | -21.387 [-24.564, -18.644] |
| optimistic | inventory | 2 | -45902.83 [-60042.65, -33508.59] | negative | 0/26 | 6525 | -21.024 [-24.140, -18.423] |
| optimistic | symmetric | 2 | -39502.83 [-49259.54, -30701.44] | negative | 1/26 | 5968 | -21.852 [-25.041, -19.062] |
| optimistic | inventory | 4 | -44052.70 [-57555.06, -32333.70] | negative | 0/26 | 6375 | -21.258 [-24.287, -18.663] |
| optimistic | symmetric | 4 | -38516.17 [-48240.69, -29871.66] | negative | 0/26 | 5667 | -22.627 [-25.840, -19.814] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -7043.51 [-17242.19, 230.57] | not established |
| conservative | 2 | -6433.01 [-15913.13, 553.46] | not established |
| conservative | 4 | -5652.92 [-14348.61, 877.41] | not established |
| optimistic | 1 | -6804.17 [-17448.13, 858.72] | not established |
| optimistic | 2 | -6400.00 [-16679.16, 1141.38] | not established |
| optimistic | 4 | -5536.53 [-14696.36, 1271.55] | not established |

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
| 2026-11-04 | 0.05612 | 0.2090 / 15.4 | -118452.16 | -120375.69 | 11492 | -30.935 | 100% quoted, 46835 trades |
| 2026-11-05 | 0.06740 | 0.2421 / 14.1 | -110660.16 | -112827.90 | 14483 | -25.187 | 100% quoted, 64164 trades |
| 2026-11-06 | 0.07151 | 0.2904 / 12.5 | -101595.87 | -101959.44 | 7821 | -36.925 | 100% quoted, 27562 trades |
| 2026-11-09 | 0.07380 | 0.2740 / 11.4 | -81119.60 | -82012.08 | 5400 | -44.521 | 100% quoted, 25966 trades |
