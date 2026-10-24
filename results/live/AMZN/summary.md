# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 15 (2026-10-02 to 2026-10-23)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -27569.82 [-36672.49, -19526.27] dollars (negative); 0 of 15 days positive; 2634 fills a day; 5 s markout -20.962 [-28.422, -15.567] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28007.09 [-37356.35, -19799.93] dollars (negative); 0 of 15 days positive; 3030 fills a day; 5 s markout -19.026 [-25.895, -14.122] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -27942.97 [-36728.63, -20237.65] | negative | 0/15 | 2672 | -20.695 [-28.055, -15.342] |
| conservative | symmetric | 1 | -25193.22 [-33965.78, -17921.49] | negative | 0/15 | 2497 | -18.132 [-23.098, -14.214] |
| conservative | inventory | 2 | -27569.82 [-36672.49, -19526.27] | negative | 0/15 | 2634 | -20.962 [-28.422, -15.567] |
| conservative | symmetric | 2 | -25081.97 [-33778.67, -17952.08] | negative | 0/15 | 2406 | -18.565 [-23.660, -14.559] |
| conservative | inventory | 4 | -26635.41 [-36485.66, -18225.35] | negative | 0/15 | 2508 | -21.367 [-28.797, -15.995] |
| conservative | symmetric | 4 | -24486.81 [-32946.24, -17490.81] | negative | 0/15 | 2252 | -19.378 [-24.758, -15.146] |
| optimistic | inventory | 1 | -28235.01 [-37173.40, -20332.92] | negative | 0/15 | 3089 | -18.692 [-25.388, -13.897] |
| optimistic | symmetric | 1 | -24948.30 [-34043.11, -17528.61] | negative | 0/15 | 2947 | -16.026 [-20.189, -12.689] |
| optimistic | inventory | 2 | -28007.09 [-37356.35, -19799.93] | negative | 0/15 | 3030 | -19.026 [-25.895, -14.122] |
| optimistic | symmetric | 2 | -24664.94 [-33805.58, -17269.27] | negative | 0/15 | 2821 | -16.544 [-20.822, -13.101] |
| optimistic | inventory | 4 | -27019.67 [-37042.27, -18475.81] | negative | 0/15 | 2862 | -19.546 [-26.507, -14.540] |
| optimistic | symmetric | 4 | -24338.83 [-33311.56, -17129.27] | negative | 0/15 | 2612 | -17.533 [-22.229, -13.720] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -2749.75 [-11156.03, 5435.06] | not established |
| conservative | 2 | -2487.85 [-11146.81, 6217.57] | not established |
| conservative | 4 | -2148.60 [-11661.45, 6754.96] | not established |
| optimistic | 1 | -3286.71 [-12487.20, 5552.39] | not established |
| optimistic | 2 | -3342.15 [-13113.06, 6134.37] | not established |
| optimistic | 4 | -2680.84 [-12837.48, 6866.38] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.05668 | 0.1233 / 27.9 | -30045.81 | -30079.37 | 2367 | -29.095 | 100% quoted, 13756 trades |
| 2026-10-05 | 0.04825 | 0.1181 / 27.1 | -20339.61 | -20764.35 | 3271 | -13.002 | 100% quoted, 15058 trades |
| 2026-10-06 | 0.04333 | 0.1204 / 23.8 | -9806.57 | -9785.46 | 1742 | -12.999 | 100% quoted, 15857 trades |
| 2026-10-07 | 0.04001 | 0.1208 / 25.4 | -10714.98 | -10932.95 | 2557 | -11.542 | 100% quoted, 13432 trades |
| 2026-10-08 | 0.03757 | 0.1203 / 24.6 | -57570.03 | -58213.54 | 3770 | -25.776 | 100% quoted, 18135 trades |
| 2026-10-09 | 0.04527 | 0.1247 / 23.0 | -18458.69 | -18608.94 | 2452 | -14.765 | 100% quoted, 12249 trades |
| 2026-10-12 | 0.04566 | 0.1223 / 21.8 | -11862.88 | -12733.79 | 1762 | -15.701 | 100% quoted, 11529 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.04917 | 0.1128 / 21.9 | -67220.40 | -69167.13 | 2365 | -66.562 | 100% quoted, 14568 trades |
| 2026-10-15 | 0.06091 | 0.1144 / 22.8 | -10732.59 | -10506.59 | 1935 | -10.823 | 100% quoted, 15912 trades |
| 2026-10-16 | 0.05059 | 0.1108 / 24.4 | -15149.75 | -15361.85 | 2753 | -11.274 | 100% quoted, 19489 trades |
| 2026-10-19 | 0.04950 | 0.1238 / 25.8 | -36090.78 | -36935.65 | 3890 | -22.708 | 100% quoted, 20463 trades |
| 2026-10-20 | 0.05308 | 0.1344 / 24.0 | -24917.59 | -25198.38 | 2796 | -16.793 | 100% quoted, 20750 trades |
| 2026-10-21 | 0.04994 | 0.1445 / 24.0 | -18910.46 | -19371.50 | 2459 | -15.609 | 100% quoted, 13131 trades |
| 2026-10-22 | 0.03676 | 0.1408 / 23.5 | -47417.76 | -47814.34 | 3312 | -20.338 | 100% quoted, 24341 trades |
| 2026-10-23 | 0.04230 | 0.1550 / 23.2 | -34309.42 | -34632.51 | 2085 | -27.441 | 100% quoted, 12733 trades |
