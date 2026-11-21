# AMZN: Avellaneda-Stoikov on real IEX data, day by day

- Traded days: 35 (2026-10-02 to 2026-11-20)
- Calibration-only days: 2; days without IEX data: 0

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

## Headline

Inventory strategy, risk aversion 2 ticks per lot.

- **conservative**: mean daily P&L -40943.79 [-51395.26, -31473.79] dollars (negative); 0 of 35 days positive; 4667 fills a day; 5 s markout -19.943 [-23.718, -16.932] ticks per fill (negative is against us).
- **optimistic**: mean daily P&L -41333.85 [-51834.40, -31838.46] dollars (negative); 0 of 35 days positive; 5186 fills a day; 5 s markout -18.428 [-21.841, -15.670] ticks per fill (negative is against us).

## Every setting

Mean over days, 95% bootstrap interval over days in brackets.

| rule | strategy | risk aversion (ticks) | daily P&L ($) | verdict | positive days | fills/day | 5 s markout (ticks) |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -42098.78 [-52974.40, -32173.99] | negative | 0/35 | 4730 | -19.710 [-23.443, -16.729] |
| conservative | symmetric | 1 | -44623.49 [-61796.25, -29054.96] | negative | 3/35 | 4475 | -18.349 [-21.180, -15.878] |
| conservative | inventory | 2 | -40943.79 [-51395.26, -31473.79] | negative | 0/35 | 4667 | -19.943 [-23.718, -16.932] |
| conservative | symmetric | 2 | -44144.79 [-61061.30, -28882.03] | negative | 3/35 | 4359 | -18.672 [-21.538, -16.157] |
| conservative | inventory | 4 | -38202.74 [-47645.93, -29380.93] | negative | 0/35 | 4447 | -20.401 [-24.126, -17.426] |
| conservative | symmetric | 4 | -43291.82 [-59752.48, -28495.73] | negative | 3/35 | 4153 | -19.331 [-22.317, -16.702] |
| optimistic | inventory | 1 | -42428.58 [-53470.43, -32446.84] | negative | 0/35 | 5273 | -18.155 [-21.458, -15.438] |
| optimistic | symmetric | 1 | -44167.68 [-61850.80, -28278.00] | negative | 3/35 | 5022 | -16.729 [-19.175, -14.548] |
| optimistic | inventory | 2 | -41333.85 [-51834.40, -31838.46] | negative | 0/35 | 5186 | -18.428 [-21.841, -15.670] |
| optimistic | symmetric | 2 | -43767.02 [-60979.20, -28119.25] | negative | 3/35 | 4873 | -17.136 [-19.626, -14.916] |
| optimistic | inventory | 4 | -38624.96 [-48185.32, -29714.99] | negative | 0/35 | 4921 | -18.946 [-22.457, -16.108] |
| optimistic | symmetric | 4 | -42939.82 [-59945.77, -27742.00] | negative | 3/35 | 4610 | -17.902 [-20.653, -15.518] |

## Does inventory control help?

Daily P&L of the inventory strategy minus the symmetric one, paired by day.

| rule | risk aversion (ticks) | inventory minus symmetric ($/day) | verdict |
|---|---|---|---|
| conservative | 1 | 2524.71 [-7510.93, 13014.59] | not established |
| conservative | 2 | 3201.00 [-7067.14, 14036.86] | not established |
| conservative | 4 | 5089.08 [-5728.70, 16289.57] | not established |
| optimistic | 1 | 1739.10 [-8682.76, 12665.90] | not established |
| optimistic | 2 | 2433.17 [-8289.70, 13792.59] | not established |
| optimistic | 4 | 4314.86 [-6807.91, 16050.98] | not established |

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
| 2026-10-26 | 0.04882 | 0.1436 / 23.2 | -90904.54 | -91001.72 | 3620 | -36.779 | 100% quoted, 15344 trades |
| 2026-10-27 | 0.06421 | 0.1397 / 23.8 | -2355.69 | -2845.93 | 1586 | -7.489 | 100% quoted, 14019 trades |
| 2026-10-28 | 0.06301 | 0.1374 / 25.0 | -12322.61 | -12392.73 | 2319 | -12.269 | 100% quoted, 15892 trades |
| 2026-10-29 | 0.06212 | 0.1421 / 25.5 | -33199.81 | -33256.64 | 4815 | -11.706 | 100% quoted, 31345 trades |
| 2026-10-30 | 0.05934 | 0.1436 / 24.0 | -70783.23 | -71794.47 | 11239 | -12.058 | 100% quoted, 50453 trades |
| 2026-11-02 | 0.05710 | 0.1800 / 17.5 | -65898.51 | -65656.50 | 5321 | -26.406 | 100% quoted, 31068 trades |
| 2026-11-03 | 0.04176 | 0.2007 / 17.5 | -41274.73 | -41827.52 | 5517 | -15.282 | 100% quoted, 26165 trades |
| 2026-11-04 | 0.04536 | 0.2131 / 15.7 | -75608.12 | -76012.90 | 10381 | -22.008 | 100% quoted, 56429 trades |
| 2026-11-05 | 0.04901 | 0.2505 / 14.7 | -148320.19 | -149109.64 | 12638 | -23.798 | 100% quoted, 53782 trades |
| 2026-11-06 | 0.05962 | 0.2812 / 12.8 | -61839.32 | -63085.67 | 6392 | -29.351 | 100% quoted, 25611 trades |
| 2026-11-09 | 0.06212 | 0.2605 / 13.9 | -33479.67 | -34163.90 | 6134 | -18.685 | 100% quoted, 32726 trades |
| 2026-11-10 | 0.05842 | 0.2569 / 13.4 | -28754.37 | -28954.97 | 4567 | -17.237 | 100% quoted, 27673 trades |
| 2026-11-11 | 0.05812 | 0.2615 / 13.8 | -35825.32 | -36038.86 | 5482 | -18.931 | 100% quoted, 28897 trades |
| 2026-11-12 | 0.05668 | 0.2410 / 13.6 | -26708.44 | -26973.38 | 4715 | -18.991 | 100% quoted, 27375 trades |
| 2026-11-13 | 0.04640 | 0.2102 / 15.5 | -20679.83 | -21009.53 | 3897 | -18.438 | 100% quoted, 21441 trades |
| 2026-11-16 | 0.04289 | 0.2065 / 16.5 | -41101.19 | -41588.61 | 4457 | -20.514 | 100% quoted, 29398 trades |
| 2026-11-17 | 0.05729 | 0.2034 / 17.3 | -31175.86 | -31414.33 | 5719 | -19.723 | 100% quoted, 23939 trades |
| 2026-11-18 | 0.05890 | 0.2020 / 16.7 | -30218.08 | -29697.40 | 5547 | -11.507 | 100% quoted, 23147 trades |
| 2026-11-19 | 0.06023 | 0.2004 / 16.2 | -80150.12 | -79810.19 | 8611 | -23.659 | 100% quoted, 36765 trades |
| 2026-11-20 | 0.06538 | 0.2166 / 15.6 | -88885.72 | -89943.38 | 10874 | -18.745 | 100% quoted, 42539 trades |
