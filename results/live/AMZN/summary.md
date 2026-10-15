# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 8 (2026-10-02 to 2026-10-14)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28252.37 [-44714.78, -15384.17] dollars (negative); 0 of 8 days positive; 2536 fills a day; 5 s markout -23.680 [-37.109, -14.608] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28785.69 [-45471.58, -15705.21] dollars (negative); 0 of 8 days positive; 2922 fills a day; 5 s markout -21.386 [-33.346, -13.167] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -28531.27 [-44330.51, -15798.13] | negative | 0/8 | 2560 | -23.384 [-36.596, -14.429] |
| conservative | symmetric | 1 | -22696.31 [-37564.34, -12131.65] | negative | 0/8 | 2340 | -20.123 [-28.352, -13.921] |
| conservative | inventory | 2 | -28252.37 [-44714.78, -15384.17] | negative | 0/8 | 2536 | -23.680 [-37.109, -14.608] |
| conservative | symmetric | 2 | -22799.15 [-37726.62, -12160.80] | negative | 0/8 | 2260 | -20.666 [-29.111, -14.356] |
| conservative | inventory | 4 | -27712.34 [-44878.12, -14397.85] | negative | 0/8 | 2428 | -24.016 [-37.124, -15.063] |
| conservative | symmetric | 4 | -22290.94 [-36771.23, -11790.28] | negative | 0/8 | 2124 | -21.641 [-30.736, -14.936] |
| optimistic | inventory | 1 | -28853.31 [-44976.88, -15881.57] | negative | 0/8 | 2961 | -21.015 [-32.702, -12.961] |
| optimistic | symmetric | 1 | -22633.65 [-37550.72, -11993.75] | negative | 0/8 | 2751 | -17.521 [-24.230, -12.437] |
| optimistic | inventory | 2 | -28785.69 [-45471.58, -15705.21] | negative | 0/8 | 2922 | -21.386 [-33.346, -13.167] |
| optimistic | symmetric | 2 | -22384.29 [-37444.81, -11642.74] | negative | 0/8 | 2641 | -18.129 [-24.997, -12.862] |
| optimistic | inventory | 4 | -28156.23 [-45705.96, -14630.02] | negative | 0/8 | 2762 | -22.086 [-34.309, -13.662] |
| optimistic | symmetric | 4 | -22006.65 [-36819.66, -11702.30] | negative | 0/8 | 2456 | -19.317 [-27.265, -13.394] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -5834.96 [-19896.18, 3525.89] | not established |
| conservative | 2 | -5453.22 [-20289.87, 4599.38] | not established |
| conservative | 4 | -5421.40 [-21790.02, 5586.13] | not established |
| optimistic | 1 | -6219.66 [-19911.70, 2993.72] | not established |
| optimistic | 2 | -6401.40 [-21762.93, 3863.38] | not established |
| optimistic | 4 | -6149.58 [-23516.87, 5179.74] | not established |

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
