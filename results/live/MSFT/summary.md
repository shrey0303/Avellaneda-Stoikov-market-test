# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 15 (2026-10-02 to 2026-10-23)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -100721.70 [-136790.88, -72119.07] dollars (negative); 0 of 15 days positive; 4160 fills a day; 5 s markout -48.694 [-56.979, -40.667] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -100976.06 [-136901.80, -72285.92] dollars (negative); 0 of 15 days positive; 4315 fills a day; 5 s markout -47.364 [-55.432, -39.638] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -102415.28 [-138137.28, -72722.09] | negative | 0/15 | 4101 | -48.502 [-56.696, -40.642] |
| conservative | symmetric | 1 | -104307.62 [-141921.50, -72507.02] | negative | 0/15 | 4009 | -48.123 [-56.238, -40.445] |
| conservative | inventory | 2 | -100721.70 [-136790.88, -72119.07] | negative | 0/15 | 4160 | -48.694 [-56.979, -40.667] |
| conservative | symmetric | 2 | -103819.10 [-141533.94, -72069.36] | negative | 0/15 | 3978 | -48.371 [-56.505, -40.664] |
| conservative | inventory | 4 | -96858.23 [-132190.51, -68996.49] | negative | 0/15 | 4181 | -49.501 [-58.086, -41.293] |
| conservative | symmetric | 4 | -103129.73 [-140918.87, -71423.50] | negative | 0/15 | 3913 | -48.917 [-57.137, -41.094] |
| optimistic | inventory | 1 | -102585.67 [-138719.22, -72767.31] | negative | 0/15 | 4254 | -47.116 [-55.103, -39.526] |
| optimistic | symmetric | 1 | -104667.78 [-142431.21, -72685.37] | negative | 0/15 | 4162 | -46.694 [-54.361, -39.302] |
| optimistic | inventory | 2 | -100976.06 [-136901.80, -72285.92] | negative | 0/15 | 4315 | -47.364 [-55.432, -39.638] |
| optimistic | symmetric | 2 | -104177.25 [-142044.75, -72356.75] | negative | 0/15 | 4122 | -47.059 [-54.874, -39.626] |
| optimistic | inventory | 4 | -96944.95 [-132144.14, -69163.34] | negative | 0/15 | 4337 | -48.208 [-56.485, -40.256] |
| optimistic | symmetric | 4 | -103536.63 [-141301.73, -72123.09] | negative | 0/15 | 4049 | -47.597 [-55.488, -40.053] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1892.33 [-5808.03, 8700.35] | not established |
| conservative | 2 | 3097.40 [-6196.09, 12064.94] | not established |
| conservative | 4 | 6271.50 [-4247.35, 16896.05] | not established |
| optimistic | 1 | 2082.11 [-5932.87, 9287.71] | not established |
| optimistic | 2 | 3201.19 [-6308.54, 12457.96] | not established |
| optimistic | 4 | 6591.68 [-3801.49, 17161.21] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.09188 | 0.1438 / 7.8 | -65274.53 | -65888.49 | 2452 | -75.700 | 100% quoted, 13763 trades |
| 2026-10-05 | 0.12604 | 0.1347 / 8.9 | -79396.69 | -80419.49 | 4148 | -41.324 | 100% quoted, 16740 trades |
| 2026-10-06 | 0.11589 | 0.1348 / 9.1 | -52361.15 | -51868.89 | 4397 | -33.239 | 100% quoted, 13695 trades |
| 2026-10-07 | 0.10694 | 0.1325 / 8.9 | -16941.47 | -17240.57 | 2370 | -29.213 | 100% quoted, 13278 trades |
| 2026-10-08 | 0.09814 | 0.1282 / 9.5 | -89481.54 | -90269.51 | 3660 | -53.834 | 100% quoted, 17122 trades |
| 2026-10-09 | 0.11259 | 0.1277 / 9.8 | -75181.24 | -75637.03 | 3752 | -44.122 | 100% quoted, 12668 trades |
| 2026-10-12 | 0.11763 | 0.1272 / 9.6 | -113648.16 | -114515.77 | 3508 | -77.494 | 100% quoted, 12123 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.13651 | 0.1311 / 8.8 | -69596.52 | -69191.59 | 4345 | -42.767 | 100% quoted, 19532 trades |
| 2026-10-15 | 0.14547 | 0.1440 / 8.5 | -129653.63 | -129815.96 | 4768 | -43.605 | 100% quoted, 13232 trades |
| 2026-10-16 | 0.14607 | 0.1387 / 7.6 | -304716.82 | -304893.28 | 6729 | -73.847 | 100% quoted, 17571 trades |
| 2026-10-19 | 0.17502 | 0.1457 / 6.6 | -111791.66 | -111739.96 | 5452 | -42.922 | 100% quoted, 13924 trades |
| 2026-10-20 | 0.16547 | 0.1530 / 6.2 | -116555.06 | -116739.68 | 4135 | -36.905 | 100% quoted, 9975 trades |
| 2026-10-21 | 0.17516 | 0.1369 / 5.5 | -44263.54 | -44228.99 | 3663 | -34.778 | 100% quoted, 10191 trades |
| 2026-10-22 | 0.17922 | 0.1220 / 4.2 | -71692.00 | -71831.55 | 5312 | -30.329 | 100% quoted, 16194 trades |
| 2026-10-23 | 0.17294 | 0.1301 / 4.3 | -170271.54 | -170360.20 | 3705 | -70.328 | 100% quoted, 11728 trades |
