# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 8 (2026-10-02 to 2026-10-14)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -22543.69 [-25881.10, -19608.40] dollars (negative); 0 of 8 days positive; 4234 fills a day; 5 s markout -18.509 [-21.216, -16.389] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -22962.73 [-26325.94, -20053.60] dollars (negative); 0 of 8 days positive; 4972 fills a day; 5 s markout -16.523 [-18.909, -14.715] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -23191.92 [-26636.66, -20126.64] | negative | 0/8 | 4216 | -18.503 [-21.183, -16.456] |
| conservative | symmetric | 1 | -28971.06 [-34637.76, -24524.67] | negative | 0/8 | 4000 | -19.076 [-21.814, -16.819] |
| conservative | inventory | 2 | -22543.69 [-25881.10, -19608.40] | negative | 0/8 | 4234 | -18.509 [-21.216, -16.389] |
| conservative | symmetric | 2 | -28422.43 [-33990.61, -24108.49] | negative | 0/8 | 3870 | -19.539 [-22.425, -17.206] |
| conservative | inventory | 4 | -21758.04 [-25009.11, -18862.62] | negative | 0/8 | 4135 | -18.661 [-21.572, -16.464] |
| conservative | symmetric | 4 | -27632.79 [-32777.54, -23601.34] | negative | 0/8 | 3641 | -20.398 [-23.443, -17.901] |
| optimistic | inventory | 1 | -23458.46 [-27156.54, -20340.88] | negative | 0/8 | 4999 | -16.477 [-18.712, -14.740] |
| optimistic | symmetric | 1 | -29692.88 [-35940.65, -25085.98] | negative | 0/8 | 4716 | -17.017 [-19.311, -15.138] |
| optimistic | inventory | 2 | -22962.73 [-26325.94, -20053.60] | negative | 0/8 | 4972 | -16.523 [-18.909, -14.715] |
| optimistic | symmetric | 2 | -29309.76 [-35668.02, -24685.32] | negative | 0/8 | 4523 | -17.547 [-19.979, -15.586] |
| optimistic | inventory | 4 | -22293.14 [-25512.64, -19504.28] | negative | 0/8 | 4798 | -16.870 [-19.365, -14.954] |
| optimistic | symmetric | 4 | -28369.73 [-34125.41, -23947.21] | negative | 0/8 | 4218 | -18.361 [-20.980, -16.239] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 5779.14 [2767.33, 8906.12] | positive |
| conservative | 2 | 5878.74 [3135.05, 8901.84] | positive |
| conservative | 4 | 5874.76 [3458.84, 8505.09] | positive |
| optimistic | 1 | 6234.42 [2929.97, 9743.13] | positive |
| optimistic | 2 | 6347.03 [3144.89, 10115.59] | positive |
| optimistic | 4 | 6076.59 [3165.24, 9324.90] | positive |

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
