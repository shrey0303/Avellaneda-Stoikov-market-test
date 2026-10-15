# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 8 (2026-10-02 to 2026-10-14)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -17496.22 [-24557.61, -9989.98] dollars (negative); 0 of 8 days positive; 2100 fills a day; 5 s markout -14.414 [-16.264, -12.244] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -18239.56 [-25502.21, -10453.84] dollars (negative); 0 of 8 days positive; 2838 fills a day; 5 s markout -11.322 [-13.280, -8.965] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -17713.98 [-24628.12, -10216.92] | negative | 0/8 | 2094 | -14.457 [-16.436, -12.088] |
| conservative | symmetric | 1 | -16277.80 [-22732.08, -9612.41] | negative | 0/8 | 1877 | -15.607 [-17.788, -13.074] |
| conservative | inventory | 2 | -17496.22 [-24557.61, -9989.98] | negative | 0/8 | 2100 | -14.414 [-16.264, -12.244] |
| conservative | symmetric | 2 | -15889.94 [-22400.85, -9278.84] | negative | 0/8 | 1798 | -16.170 [-18.333, -13.666] |
| conservative | inventory | 4 | -16870.99 [-23720.54, -9572.43] | negative | 0/8 | 2042 | -14.531 [-16.430, -12.347] |
| conservative | symmetric | 4 | -15389.61 [-21725.10, -9039.26] | negative | 0/8 | 1672 | -17.173 [-19.323, -14.733] |
| optimistic | inventory | 1 | -18506.62 [-25696.17, -10639.30] | negative | 0/8 | 2887 | -11.255 [-13.317, -8.817] |
| optimistic | symmetric | 1 | -16810.94 [-23299.63, -9842.14] | negative | 1/8 | 2604 | -12.015 [-14.164, -9.471] |
| optimistic | inventory | 2 | -18239.56 [-25502.21, -10453.84] | negative | 0/8 | 2838 | -11.322 [-13.280, -8.965] |
| optimistic | symmetric | 2 | -16590.29 [-23087.62, -9798.34] | negative | 0/8 | 2431 | -12.697 [-14.903, -10.098] |
| optimistic | inventory | 4 | -17610.01 [-24628.07, -10052.35] | negative | 0/8 | 2715 | -11.517 [-13.467, -9.194] |
| optimistic | symmetric | 4 | -16081.31 [-22429.55, -9559.65] | negative | 0/8 | 2171 | -13.833 [-16.116, -11.170] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -1436.18 [-7522.29, 3413.92] | not established |
| conservative | 2 | -1606.28 [-8437.45, 3500.76] | not established |
| conservative | 4 | -1481.37 [-8301.15, 3609.48] | not established |
| optimistic | 1 | -1695.67 [-7553.30, 3329.47] | not established |
| optimistic | 2 | -1649.27 [-8138.24, 3540.44] | not established |
| optimistic | 4 | -1528.70 [-8054.22, 3527.91] | not established |

## Day by day

Inventory strategy at 2 ticks.

![Cumulative P&L](cumulative_pnl.svg)

| date | sigma ($/sqrt s) | A / k (conservative) | P&L conservative ($) | P&L optimistic ($) | fills (cons.) | 5 s markout (ticks, cons.) | IEX data |
|---|---|---|---|---|---|---|---|
| 2026-10-01 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-02 | 0.03676 | 0.2096 / 37.8 | -28953.32 | -29533.70 | 3512 | -14.048 | 100% quoted, 20263 trades |
| 2026-10-05 | 0.03458 | 0.1827 / 31.7 | -17982.03 | -18514.21 | 1813 | -16.001 | 100% quoted, 20854 trades |
| 2026-10-06 | 0.03036 | 0.1596 / 32.3 | -27199.84 | -28277.24 | 3107 | -16.738 | 100% quoted, 22050 trades |
| 2026-10-07 | 0.03001 | 0.1545 / 29.8 | -27924.08 | -29077.36 | 2894 | -16.887 | 100% quoted, 17100 trades |
| 2026-10-08 | 0.02992 | 0.1466 / 28.0 | -23440.90 | -24950.76 | 3028 | -15.149 | 100% quoted, 31296 trades |
| 2026-10-09 | 0.02858 | 0.1431 / 27.1 | -7686.91 | -8454.60 | 955 | -17.342 | 100% quoted, 26508 trades |
| 2026-10-12 | 0.02711 | 0.1370 / 30.3 | -1917.16 | -2162.12 | 416 | -10.779 | 100% quoted, 23043 trades |
| 2026-10-13 | calibration only |  |  |  |  |  | no earlier day to calibrate on; this day only calibrates |
| 2026-10-14 | 0.02428 | 0.1408 / 41.0 | -4865.53 | -4946.51 | 1074 | -8.365 | 100% quoted, 29449 trades |
