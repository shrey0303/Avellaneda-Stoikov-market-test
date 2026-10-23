# GOOG: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 14 (2026-10-02 to 2026-10-22)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -28003.61 [-42114.44, -17695.33] dollars (negative); 0 of 14 days positive; 2216 fills a day; 5 s markout -28.308 [-33.080, -23.531] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -28426.04 [-42643.28, -18088.69] dollars (negative); 0 of 14 days positive; 2312 fills a day; 5 s markout -27.748 [-32.409, -23.028] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -29344.36 [-46179.95, -17553.82] | negative | 0/14 | 2205 | -28.031 [-32.735, -23.376] |
| conservative | symmetric | 1 | -33771.17 [-56210.25, -18245.17] | negative | 0/14 | 2178 | -27.315 [-31.836, -22.808] |
| conservative | inventory | 2 | -28003.61 [-42114.44, -17695.33] | negative | 0/14 | 2216 | -28.308 [-33.080, -23.531] |
| conservative | symmetric | 2 | -33509.53 [-55890.15, -18037.86] | negative | 0/14 | 2159 | -27.416 [-31.933, -22.911] |
| conservative | inventory | 4 | -26258.68 [-37481.78, -17660.56] | negative | 0/14 | 2182 | -28.796 [-33.705, -23.980] |
| conservative | symmetric | 4 | -32949.80 [-55336.21, -17619.87] | negative | 0/14 | 2122 | -27.608 [-32.073, -23.151] |
| optimistic | inventory | 1 | -29581.81 [-46493.13, -17684.97] | negative | 0/14 | 2302 | -27.439 [-32.113, -22.792] |
| optimistic | symmetric | 1 | -34073.72 [-56813.02, -18508.04] | negative | 0/14 | 2267 | -26.755 [-31.133, -22.238] |
| optimistic | inventory | 2 | -28426.04 [-42643.28, -18088.69] | negative | 0/14 | 2312 | -27.748 [-32.409, -23.028] |
| optimistic | symmetric | 2 | -33829.78 [-56443.86, -18253.94] | negative | 0/14 | 2245 | -26.870 [-31.235, -22.371] |
| optimistic | inventory | 4 | -26577.02 [-37805.02, -17898.44] | negative | 0/14 | 2279 | -28.187 [-32.881, -23.459] |
| optimistic | symmetric | 4 | -33363.98 [-55703.25, -17909.80] | negative | 0/14 | 2200 | -27.079 [-31.511, -22.629] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 4426.81 [76.19, 10039.48] | positive |
| conservative | 2 | 5505.93 [-833.97, 14020.47] | not established |
| conservative | 4 | 6691.12 [-1445.65, 18296.54] | not established |
| optimistic | 1 | 4491.91 [-138.22, 10370.28] | not established |
| optimistic | 2 | 5403.74 [-1114.42, 14045.99] | not established |
| optimistic | 4 | 6786.96 [-1425.31, 18487.45] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.06399 | 0.1467 / 15.3 | -11239.88 | -11388.79 | 2611 | -14.894 | 100% quoted, 6767 trades |
| 2026-10-05 | 0.06162 | 0.1095 / 12.5 | -22660.49 | -22799.99 | 2604 | -17.254 | 100% quoted, 9105 trades |
| 2026-10-06 | 0.05802 | 0.1063 / 11.7 | -15860.42 | -16278.82 | 2137 | -16.669 | 100% quoted, 5468 trades |
| 2026-10-07 | 0.05532 | 0.0954 / 10.7 | -31484.55 | -31831.84 | 2531 | -28.992 | 100% quoted, 6416 trades |
| 2026-10-08 | 0.06492 | 0.0900 / 9.8 | -100703.35 | -101842.43 | 3797 | -34.179 | 100% quoted, 7026 trades |
| 2026-10-09 | 0.07586 | 0.0759 / 6.7 | -15241.87 | -16035.32 | 2180 | -26.736 | 100% quoted, 6154 trades |
| 2026-10-12 | 0.08256 | 0.0739 / 6.1 | -26412.27 | -26445.74 | 1682 | -34.199 | 100% quoted, 4728 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.09808 | 0.0677 / 4.8 | -19385.65 | -20284.38 | 2738 | -22.659 | 100% quoted, 8865 trades |
| 2026-10-15 | 0.09592 | 0.0710 / 4.4 | -8858.35 | -9745.90 | 1481 | -31.364 | 100% quoted, 8160 trades |
| 2026-10-16 | 0.08691 | 0.0722 / 5.4 | -43782.76 | -44302.42 | 1600 | -44.858 | 100% quoted, 5455 trades |
| 2026-10-19 | 0.09084 | 0.0722 / 5.5 | -27282.03 | -27296.19 | 2210 | -31.606 | 100% quoted, 8489 trades |
| 2026-10-20 | 0.08560 | 0.0785 / 5.9 | -7612.79 | -7549.54 | 1130 | -29.259 | 100% quoted, 5946 trades |
| 2026-10-21 | 0.07767 | 0.0768 / 6.5 | -47241.28 | -47395.18 | 2420 | -42.704 | 100% quoted, 13763 trades |
| 2026-10-22 | 0.07724 | 0.0850 / 8.0 | -14284.81 | -14767.99 | 1900 | -20.943 | 100% quoted, 13497 trades |
