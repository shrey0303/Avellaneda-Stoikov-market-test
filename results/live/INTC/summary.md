# INTC: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 13 (2026-10-02 to 2026-10-21)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -12459.50 [-18512.53, -6936.54] dollars (negative); 0 of 13 days positive; 1944 fills a day; 5 s markout -10.851 [-13.591, -7.969] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -12864.85 [-19115.10, -7057.04] dollars (negative); 0 of 13 days positive; 2909 fills a day; 5 s markout -8.376 [-10.851, -5.887] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -12807.57 [-18772.71, -7320.55] | negative | 0/13 | 1993 | -10.851 [-13.645, -7.900] |
| conservative | symmetric | 1 | -12735.08 [-18507.11, -7750.94] | negative | 0/13 | 1821 | -11.659 [-14.706, -8.441] |
| conservative | inventory | 2 | -12459.50 [-18512.53, -6936.54] | negative | 0/13 | 1944 | -10.851 [-13.591, -7.969] |
| conservative | symmetric | 2 | -12112.00 [-17908.54, -7109.58] | negative | 0/13 | 1687 | -12.161 [-15.269, -8.909] |
| conservative | inventory | 4 | -11836.33 [-17730.65, -6446.86] | negative | 0/13 | 1813 | -11.027 [-13.770, -8.164] |
| conservative | symmetric | 4 | -11666.88 [-17161.98, -6911.53] | negative | 0/13 | 1477 | -13.062 [-16.186, -9.713] |
| optimistic | inventory | 1 | -13247.35 [-19539.79, -7460.50] | negative | 0/13 | 3066 | -8.276 [-10.811, -5.709] |
| optimistic | symmetric | 1 | -13793.19 [-19638.17, -8392.30] | negative | 2/13 | 2858 | -8.833 [-11.482, -6.135] |
| optimistic | inventory | 2 | -12864.85 [-19115.10, -7057.04] | negative | 0/13 | 2909 | -8.376 [-10.851, -5.887] |
| optimistic | symmetric | 2 | -13174.71 [-19100.70, -7898.19] | negative | 0/13 | 2551 | -9.407 [-12.144, -6.588] |
| optimistic | inventory | 4 | -12284.52 [-18329.38, -6674.12] | negative | 0/13 | 2650 | -8.593 [-11.002, -6.133] |
| optimistic | symmetric | 4 | -12664.99 [-18313.28, -7691.53] | negative | 0/13 | 2140 | -10.342 [-13.195, -7.398] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | -72.49 [-4184.00, 3255.56] | not established |
| conservative | 2 | -347.49 [-4912.22, 3179.42] | not established |
| conservative | 4 | -169.45 [-4754.25, 3206.81] | not established |
| optimistic | 1 | 545.84 [-3785.06, 4408.64] | not established |
| optimistic | 2 | 309.86 [-4164.44, 4128.64] | not established |
| optimistic | 4 | 380.47 [-4164.39, 4101.81] | not established |

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
| 2026-10-19 | 0.01801 | 0.1773 / 63.7 | -3319.80 | -3140.96 | 1329 | -5.225 | 100% quoted, 29649 trades |
| 2026-10-20 | 0.01869 | 0.1856 / 64.1 | -1897.85 | -1351.64 | 1595 | -3.741 | 100% quoted, 32079 trades |
| 2026-10-21 | 0.01889 | 0.1903 / 66.1 | -3012.00 | -3003.82 | 1399 | -5.246 | 100% quoted, 31948 trades |
