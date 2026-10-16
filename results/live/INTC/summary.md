# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 10 (2026-10-02 to 2026-10-16)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -15374.38 [-21950.52, -8768.65] dollars (negative); 0 of 10 days positive; 2096 fills a day; 5 s markout -12.685 [-15.404, -9.690] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -15974.67 [-22819.20, -9143.91] dollars (negative); 0 of 10 days positive; 2977 fills a day; 5 s markout -9.886 [-12.466, -7.155] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -15723.83 [-22129.67, -9162.41] | negative | 0/10 | 2126 | -12.701 [-15.531, -9.608] |
| conservative | symmetric | 1 | -15245.46 [-21217.66, -8789.50] | negative | 0/10 | 1926 | -13.682 [-16.747, -10.300] |
| conservative | inventory | 2 | -15374.38 [-21950.52, -8768.65] | negative | 0/10 | 2096 | -12.685 [-15.404, -9.690] |
| conservative | symmetric | 2 | -14638.13 [-20608.74, -8290.49] | negative | 0/10 | 1812 | -14.222 [-17.273, -10.833] |
| conservative | inventory | 4 | -14686.65 [-21061.65, -8340.67] | negative | 0/10 | 2000 | -12.845 [-15.557, -9.863] |
| conservative | symmetric | 4 | -13992.16 [-19783.32, -7878.53] | negative | 0/10 | 1639 | -15.171 [-18.300, -11.740] |
| optimistic | inventory | 1 | -16384.08 [-23222.97, -9462.54] | negative | 0/10 | 3080 | -9.818 [-12.481, -7.032] |
| optimistic | symmetric | 1 | -16116.98 [-22319.28, -9086.69] | negative | 1/10 | 2845 | -10.462 [-13.254, -7.532] |
| optimistic | inventory | 2 | -15974.67 [-22819.20, -9143.91] | negative | 0/10 | 2977 | -9.886 [-12.466, -7.155] |
| optimistic | symmetric | 2 | -15725.20 [-21849.07, -8786.83] | negative | 0/10 | 2600 | -11.096 [-13.978, -8.057] |
| optimistic | inventory | 4 | -15280.02 [-21982.99, -8692.41] | negative | 0/10 | 2786 | -10.106 [-12.626, -7.410] |
| optimistic | symmetric | 4 | -15100.74 [-21101.18, -8454.84] | negative | 0/10 | 2256 | -12.146 [-15.099, -8.992] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -478.37 [-6001.64, 3696.70] | not established |
| conservative | 2 | -736.25 [-6826.76, 3622.53] | not established |
| conservative | 4 | -694.49 [-6724.96, 3579.78] | not established |
| optimistic | 1 | -267.10 [-5977.84, 4691.35] | not established |
| optimistic | 2 | -249.46 [-6299.17, 4765.29] | not established |
| optimistic | 4 | -179.29 [-6252.02, 4671.64] | not established |

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
| 2026-10-15 | 0.02192 | 0.1576 / 52.1 | -11353.03 | -11755.31 | 2895 | -7.699 | 100% quoted, 36726 trades |
| 2026-10-16 | 0.01975 | 0.1645 / 58.1 | -2421.01 | -2074.86 | 1261 | -3.846 | 100% quoted, 29908 trades |
