# AAPL: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 10 (2026-10-02 to 2026-10-16)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -22276.98 [-25658.36, -18829.78] dollars (negative); 0 of 10 days positive; 4294 fills a day; 5 s markout -18.260 [-20.409, -16.529] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -22655.78 [-26083.05, -19151.57] dollars (negative); 0 of 10 days positive; 5048 fills a day; 5 s markout -16.358 [-18.249, -14.870] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -23000.04 [-26349.45, -19607.54] | negative | 0/10 | 4288 | -18.238 [-20.398, -16.544] |
| conservative | symmetric | 1 | -27948.88 [-32925.33, -23893.80] | negative | 0/10 | 4064 | -18.757 [-20.943, -16.932] |
| conservative | inventory | 2 | -22276.98 [-25658.36, -18829.78] | negative | 0/10 | 4294 | -18.260 [-20.409, -16.529] |
| conservative | symmetric | 2 | -27348.53 [-32230.59, -23311.47] | negative | 0/10 | 3935 | -19.195 [-21.478, -17.303] |
| conservative | inventory | 4 | -21339.76 [-24594.50, -17959.77] | negative | 0/10 | 4189 | -18.431 [-20.718, -16.605] |
| conservative | symmetric | 4 | -26445.72 [-31087.61, -22359.62] | negative | 0/10 | 3703 | -20.046 [-22.483, -17.983] |
| optimistic | inventory | 1 | -23319.90 [-26961.05, -19758.04] | negative | 0/10 | 5079 | -16.292 [-18.085, -14.849] |
| optimistic | symmetric | 1 | -28911.70 [-34386.58, -24632.30] | negative | 0/10 | 4801 | -16.743 [-18.577, -15.186] |
| optimistic | inventory | 2 | -22655.78 [-26083.05, -19151.57] | negative | 0/10 | 5048 | -16.358 [-18.249, -14.870] |
| optimistic | symmetric | 2 | -28508.93 [-34016.32, -24210.57] | negative | 0/10 | 4613 | -17.237 [-19.152, -15.582] |
| optimistic | inventory | 4 | -21817.86 [-25066.08, -18514.64] | negative | 0/10 | 4873 | -16.654 [-18.607, -15.073] |
| optimistic | symmetric | 4 | -27367.20 [-32412.77, -23287.10] | negative | 0/10 | 4301 | -18.021 [-20.104, -16.235] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4948.84 [2347.54, 7916.80] | positive |
| conservative | 2 | 5071.55 [2442.47, 7907.30] | positive |
| conservative | 4 | 5105.96 [2878.94, 7589.25] | positive |
| optimistic | 1 | 5591.80 [2771.76, 8770.55] | positive |
| optimistic | 2 | 5853.15 [3176.62, 9196.41] | positive |
| optimistic | 4 | 5549.34 [3139.71, 8443.67] | positive |

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
