# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 13 (2026-10-02 to 2026-10-21)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -25946.78 [-32924.86, -20874.82] dollars (negative); 0 of 13 days positive; 4346 fills a day; 5 s markout -19.713 [-22.701, -17.341] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -26295.00 [-33130.06, -21223.65] dollars (negative); 0 of 13 days positive; 5064 fills a day; 5 s markout -17.767 [-20.522, -15.595] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -26839.81 [-33992.55, -21654.85] | negative | 0/13 | 4329 | -19.693 [-22.661, -17.370] |
| conservative | symmetric | 1 | -29311.10 [-35224.05, -24311.46] | negative | 0/13 | 4074 | -20.204 [-23.127, -17.805] |
| conservative | inventory | 2 | -25946.78 [-32924.86, -20874.82] | negative | 0/13 | 4346 | -19.713 [-22.701, -17.341] |
| conservative | symmetric | 2 | -28812.10 [-34787.53, -23765.72] | negative | 0/13 | 3954 | -20.629 [-23.605, -18.184] |
| conservative | inventory | 4 | -24762.94 [-31236.98, -19890.96] | negative | 0/13 | 4262 | -19.876 [-22.973, -17.420] |
| conservative | symmetric | 4 | -27941.81 [-33795.60, -23084.96] | negative | 0/13 | 3735 | -21.459 [-24.525, -18.905] |
| optimistic | inventory | 1 | -27111.80 [-34471.53, -21812.41] | negative | 0/13 | 5078 | -17.689 [-20.366, -15.595] |
| optimistic | symmetric | 1 | -30171.58 [-36339.52, -24947.38] | negative | 0/13 | 4765 | -18.153 [-20.902, -15.932] |
| optimistic | inventory | 2 | -26295.00 [-33130.06, -21223.65] | negative | 0/13 | 5064 | -17.767 [-20.522, -15.595] |
| optimistic | symmetric | 2 | -29815.70 [-36008.15, -24616.46] | negative | 0/13 | 4589 | -18.663 [-21.478, -16.399] |
| optimistic | inventory | 4 | -25225.76 [-31536.17, -20397.09] | negative | 0/13 | 4909 | -18.080 [-20.920, -15.849] |
| optimistic | symmetric | 4 | -28810.83 [-34818.54, -23757.07] | negative | 0/13 | 4294 | -19.465 [-22.301, -17.140] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2471.29 [-1002.34, 5772.25] | not established |
| conservative | 2 | 2865.31 [-373.70, 5915.71] | not established |
| conservative | 4 | 3178.87 [325.92, 5840.30] | positive |
| optimistic | 1 | 3059.78 [-582.30, 6575.66] | not established |
| optimistic | 2 | 3520.70 [52.07, 6948.52] | positive |
| optimistic | 4 | 3585.08 [513.69, 6555.18] | positive |

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
