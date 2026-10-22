# MSFT: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 13 (2026-10-02 to 2026-10-21)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -97604.77 [-137825.02, -67617.72] dollars (negative); 0 of 13 days positive; 4106 fills a day; 5 s markout -48.442 [-57.375, -40.314] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -97880.71 [-138080.06, -68173.25] dollars (negative); 0 of 13 days positive; 4278 fills a day; 5 s markout -46.925 [-55.333, -39.212] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -99232.90 [-141030.91, -68128.16] | negative | 0/13 | 4053 | -48.298 [-56.924, -40.360] |
| conservative | symmetric | 1 | -101092.23 [-147182.35, -65950.20] | negative | 0/13 | 3970 | -47.805 [-56.321, -39.968] |
| conservative | inventory | 2 | -97604.77 [-137825.02, -67617.72] | negative | 0/13 | 4106 | -48.442 [-57.375, -40.314] |
| conservative | symmetric | 2 | -100624.23 [-146602.30, -65501.34] | negative | 0/13 | 3937 | -48.074 [-56.664, -40.281] |
| conservative | inventory | 4 | -93847.68 [-132512.05, -64947.42] | negative | 0/13 | 4130 | -49.061 [-58.134, -40.897] |
| conservative | symmetric | 4 | -99933.20 [-146003.05, -64733.93] | negative | 0/13 | 3865 | -48.680 [-57.459, -40.779] |
| optimistic | inventory | 1 | -99429.43 [-141303.11, -68122.02] | negative | 0/13 | 4223 | -46.700 [-54.906, -39.045] |
| optimistic | symmetric | 1 | -101516.83 [-147707.50, -66088.48] | negative | 0/13 | 4141 | -46.159 [-54.178, -38.715] |
| optimistic | inventory | 2 | -97880.71 [-138080.06, -68173.25] | negative | 0/13 | 4278 | -46.925 [-55.333, -39.212] |
| optimistic | symmetric | 2 | -101033.41 [-147252.64, -65704.61] | negative | 0/13 | 4097 | -46.572 [-54.693, -38.988] |
| optimistic | inventory | 4 | -93996.11 [-132657.61, -65115.02] | negative | 0/13 | 4302 | -47.595 [-56.299, -39.693] |
| optimistic | symmetric | 4 | -100422.25 [-146332.61, -65242.34] | negative | 0/13 | 4019 | -47.164 [-55.432, -39.481] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 1859.34 [-6276.22, 9387.26] | not established |
| conservative | 2 | 3019.46 [-6743.38, 12912.83] | not established |
| conservative | 4 | 6085.52 [-5158.20, 18436.43] | not established |
| optimistic | 1 | 2087.40 [-6221.74, 10128.70] | not established |
| optimistic | 2 | 3152.71 [-6863.60, 13391.56] | not established |
| optimistic | 4 | 6426.14 [-4721.58, 18912.05] | not established |

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
