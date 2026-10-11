# GOOG 2012-06-21: Avellaneda-Stoikov replay study

- Calibrated on 09:31:00 to 12:45:00; traded on 12:45:00 to 15:59:00.
- Windows of 1800 s, each an independent session. Requote every 1 s and after each fill. One lot = 100 shares per side.
- Figures are means over windows with a 95% bootstrap interval in brackets. A difference whose interval contains zero is not claimed.
- P&L is in dollars per window, before fees and rebates. Markouts are in ticks per share.

## Headline

Middle settings only; every setting is in the tables below.

- **Adverse selection.** 5 s after a fill, the mid had moved by conservative -4.917 ticks [-7.100, -1.817]; optimistic -9.250 ticks [-14.000, -5.500] per share (negative is against us). Across fill rules: holds under both rules.
- **Model against replay.** conservative: replay 19.141 [-10.000, 51.113] against the model's 605.629 [536.930, 676.060] dollars per window (replay below model); optimistic: replay 77.167 [11.167, 158.167] against the model's 1800.544 [1710.749, 1886.118] dollars per window (replay below model).
- **Prediction.** `trade_imbalance` had an out-of-sample correlation of 0.103 [0.082, 0.129] with the mid change over the next 5 s (positive). Leaning quotes on it changed the 5 s markout by conservative -0.130 ticks [-0.650, 0.260]; optimistic -2.333 ticks [-7.000, 0.000]. Across fill rules: not established under both rules: not a conclusion.

## Calibration

sigma = 0.0406195 dollars per sqrt(second), taken at the 60 s horizon.

![Variance ratio](variance_ratio.svg)

| horizon (s) | sigma ($/sqrt s) | increments | variance ratio vs longest |
|---|---|---|---|
| 1 | 0.045982 | 11639 | 1.476 |
| 2 | 0.043897 | 5819 | 1.345 |
| 5 | 0.042158 | 2327 | 1.241 |
| 10 | 0.040274 | 1163 | 1.132 |
| 30 | 0.038309 | 387 | 1.025 |
| 60 | 0.040620 | 193 | 1.152 |
| 120 | 0.035398 | 96 | 0.875 |
| 300 | 0.037847 | 38 | 1.000 |

### Fill intensity, conservative rule

A = 0.015941 per second, k = 3.6708 per dollar, from 4656 probes, 1790 filled, 215904 s of exposure.

![Fill intensity, conservative](intensity_conservative.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 362 | 32344 | 0.1594 | 0.01119 | 0.00897 |
| 1 | 773 | 311 | 35420 | 0.1680 | 0.00878 | 0.00875 |
| 2 | 760 | 313 | 34716 | 0.1793 | 0.00902 | 0.00842 |
| 3 | 796 | 281 | 37849 | 0.1849 | 0.00742 | 0.00819 |
| 4 | 740 | 250 | 35925 | 0.1969 | 0.00696 | 0.00801 |
| 5 | 811 | 273 | 39651 | 0.2093 | 0.00689 | 0.00756 |

### Fill intensity, optimistic rule

A = 0.022915 per second, k = 1.7268 per dollar, from 4656 probes, 2968 filled, 177621 s of exposure.

![Fill intensity, optimistic](intensity_optimistic.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 571 | 24838 | 0.1594 | 0.02299 | 0.01739 |
| 1 | 773 | 510 | 29045 | 0.1680 | 0.01756 | 0.01720 |
| 2 | 760 | 515 | 27727 | 0.1793 | 0.01857 | 0.01681 |
| 3 | 796 | 468 | 32123 | 0.1849 | 0.01457 | 0.01666 |
| 4 | 740 | 424 | 30579 | 0.1969 | 0.01387 | 0.01642 |
| 5 | 811 | 480 | 33309 | 0.2093 | 0.01441 | 0.01601 |

## Q1. Does the calibrated model predict replay P&L?

| fill rule | strategy | penalty (ticks) | replay P&L | model P&L | replay fills | model fills | verdict |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 14.724 [-15.667, 47.899] | 617.454 [541.756, 693.031] | 2.667 [1.333, 3.833] | 21.060 [20.475, 21.660] | replay below model |
| conservative | symmetric | 1 | 4.152 [-53.345, 59.050] | 621.749 [536.620, 703.003] | 2.667 [1.167, 4.000] | 21.080 [20.500, 21.680] | replay below model |
| conservative | inventory | 2 | 19.141 [-10.000, 51.113] | 605.629 [536.930, 676.060] | 2.333 [1.167, 3.333] | 21.040 [20.435, 21.650] | replay below model |
| conservative | symmetric | 2 | 25.238 [-9.787, 67.992] | 619.349 [534.858, 700.778] | 2.333 [1.167, 3.333] | 20.900 [20.315, 21.505] | replay below model |
| conservative | inventory | 4 | 40.139 [-0.165, 80.865] | 597.108 [539.321, 652.958] | 2.667 [1.000, 4.500] | 20.785 [20.175, 21.370] | replay below model |
| conservative | symmetric | 4 | 25.017 [-8.500, 67.517] | 616.694 [531.678, 697.521] | 2.167 [1.000, 3.167] | 20.620 [20.030, 21.215] | replay below model |
| optimistic | inventory | 1 | 55.083 [0.000, 132.667] | 1795.411 [1697.319, 1887.856] | 0.833 [0.000, 1.500] | 30.200 [29.495, 30.905] | replay below model |
| optimistic | symmetric | 1 | 54.917 [0.000, 132.167] | 1799.905 [1696.597, 1899.969] | 0.833 [0.000, 1.500] | 30.175 [29.460, 30.895] | replay below model |
| optimistic | inventory | 2 | 77.167 [11.167, 158.167] | 1800.544 [1710.749, 1886.118] | 1.000 [0.333, 1.667] | 30.175 [29.470, 30.875] | replay below model |
| optimistic | symmetric | 2 | 90.167 [11.167, 178.333] | 1805.119 [1701.012, 1904.504] | 0.833 [0.167, 1.500] | 30.090 [29.380, 30.785] | replay below model |
| optimistic | inventory | 4 | 30.583 [0.000, 69.417] | 1796.586 [1715.377, 1874.535] | 0.500 [0.000, 1.167] | 30.165 [29.455, 30.865] | replay below model |
| optimistic | symmetric | 4 | 30.583 [0.000, 69.417] | 1802.883 [1702.975, 1899.599] | 0.500 [0.000, 1.167] | 29.855 [29.160, 30.565] | replay below model |

### Replay profit three ways

Every fill is booked at its own price. Shares still held when a window closes have no trade price, so the profit depends on how they are valued. Realised counts completed buy-and-sell pairs only (first in, first out). The middle column is the replay P&L used everywhere else in this report. The last column trades the leftover out against the real book at the close, level by level, which is what closing would have cost. Sticky quotes.

| run | realised | leftover valued at the mid | leftover closed at real prices | shares left at the close | shares traded per window |
|---|---|---|---|---|---|
| inventory/1t/sticky/conservative | 10.138 [-0.085, 30.500] | 14.724 [-15.667, 47.899] | -10.428 [-60.358, 34.407] | 136 | 202 |
| symmetric/1t/sticky/conservative | 15.500 [0.000, 36.333] | 4.152 [-53.345, 59.050] | -31.128 [-114.685, 42.108] | 166 | 233 |
| inventory/2t/sticky/conservative | 1.972 [-0.085, 6.000] | 19.141 [-10.000, 51.113] | 3.068 [-38.915, 42.073] | 102 | 169 |
| symmetric/2t/sticky/conservative | 7.500 [0.000, 18.167] | 25.238 [-9.787, 67.992] | 3.117 [-53.723, 55.027] | 120 | 186 |
| inventory/4t/sticky/conservative | 12.938 [2.000, 25.087] | 40.139 [-0.165, 80.865] | 30.215 [-5.108, 67.443] | 84 | 220 |
| symmetric/4t/sticky/conservative | 8.000 [0.000, 19.333] | 25.017 [-8.500, 67.517] | 3.068 [-53.158, 55.433] | 119 | 186 |
| inventory/1t/sticky/optimistic | 0.000 [0.000, 0.000] | 55.083 [0.000, 132.667] | 37.848 [0.000, 105.822] | 83 | 83 |
| symmetric/1t/sticky/optimistic | 0.000 [0.000, 0.000] | 54.917 [0.000, 132.167] | 37.682 [0.000, 105.322] | 83 | 83 |
| inventory/2t/sticky/optimistic | 25.500 [0.000, 76.500] | 77.167 [11.167, 158.167] | 62.365 [2.387, 131.322] | 67 | 100 |
| symmetric/2t/sticky/optimistic | 0.000 [0.000, 0.000] | 90.167 [11.167, 178.333] | 74.365 [2.387, 150.000] | 83 | 83 |
| inventory/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 30.583 [0.000, 69.417] | 20.553 [0.000, 56.887] | 50 | 50 |
| symmetric/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 30.583 [0.000, 69.417] | 20.553 [0.000, 56.887] | 50 | 50 |
| signal/1t/sticky/conservative | 10.138 [-0.085, 30.500] | 23.373 [-29.667, 85.315] | -11.090 [-78.885, 56.705] | 167 | 234 |
| signal/2t/sticky/conservative | 7.472 [-0.057, 18.500] | 34.253 [-1.066, 67.620] | 18.353 [-7.923, 44.630] | 102 | 202 |
| signal/4t/sticky/conservative | 7.318 [-0.030, 17.667] | 28.176 [-12.128, 71.000] | 9.912 [-28.817, 52.412] | 116 | 186 |
| signal/1t/sticky/optimistic | 0.000 [0.000, 0.000] | 90.167 [11.167, 178.333] | 74.365 [2.387, 150.000] | 83 | 83 |
| signal/2t/sticky/optimistic | 0.000 [0.000, 0.000] | 90.167 [11.167, 178.333] | 74.365 [2.387, 150.000] | 83 | 83 |
| signal/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 30.583 [0.000, 69.417] | 20.553 [0.000, 56.887] | 50 | 50 |

## Q2. Adverse selection: markouts on replay fills

Negative means the mid moved against us after the fill. In the model world the expected markout is zero.

![Markouts](markouts.svg)

| fill rule | strategy | penalty (ticks) | horizon (s) | markout (ticks) | fills | verdict |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 1 | -2.950 [-5.300, -0.050] | 16 | negative |
| conservative | inventory | 1 | 5 | -4.408 [-6.717, -1.175] | 16 | negative |
| conservative | inventory | 1 | 30 | -4.758 [-11.417, 4.675] | 16 | inside the interval: no claim |
| conservative | symmetric | 1 | 1 | -3.495 [-5.700, -0.465] | 16 | negative |
| conservative | symmetric | 1 | 5 | -5.487 [-7.827, -2.000] | 16 | negative |
| conservative | symmetric | 1 | 30 | -5.030 [-11.667, 4.483] | 16 | inside the interval: no claim |
| conservative | inventory | 2 | 1 | -3.467 [-5.500, -0.600] | 14 | negative |
| conservative | inventory | 2 | 5 | -4.917 [-7.100, -1.817] | 14 | negative |
| conservative | inventory | 2 | 30 | -5.450 [-12.500, 5.183] | 14 | inside the interval: no claim |
| conservative | symmetric | 2 | 1 | -3.675 [-5.700, -0.825] | 14 | negative |
| conservative | symmetric | 2 | 5 | -5.133 [-7.100, -1.900] | 14 | negative |
| conservative | symmetric | 2 | 30 | -5.617 [-12.500, 4.317] | 14 | inside the interval: no claim |
| conservative | inventory | 4 | 1 | -4.200 [-5.900, -2.100] | 16 | negative |
| conservative | inventory | 4 | 5 | -6.036 [-7.783, -3.757] | 16 | negative |
| conservative | inventory | 4 | 30 | -7.576 [-13.233, -0.262] | 16 | negative |
| conservative | symmetric | 4 | 1 | -3.550 [-5.700, -0.450] | 13 | negative |
| conservative | symmetric | 4 | 5 | -5.225 [-7.683, -1.525] | 13 | negative |
| conservative | symmetric | 4 | 30 | -5.858 [-13.233, 4.692] | 13 | inside the interval: no claim |
| optimistic | inventory | 1 | 1 | -8.000 [-9.500, -7.000] | 5 | negative |
| optimistic | inventory | 1 | 5 | -8.750 [-12.500, -5.500] | 5 | negative |
| optimistic | inventory | 1 | 30 | -10.583 [-20.500, 3.250] | 5 | inside the interval: no claim |
| optimistic | symmetric | 1 | 1 | -8.000 [-9.500, -7.000] | 5 | negative |
| optimistic | symmetric | 1 | 5 | -8.750 [-12.500, -5.500] | 5 | negative |
| optimistic | symmetric | 1 | 30 | -10.583 [-20.500, 3.250] | 5 | inside the interval: no claim |
| optimistic | inventory | 2 | 1 | -6.250 [-7.500, -4.250] | 6 | negative |
| optimistic | inventory | 2 | 5 | -9.250 [-14.000, -5.500] | 6 | negative |
| optimistic | inventory | 2 | 30 | -6.000 [-14.500, 3.250] | 6 | inside the interval: no claim |
| optimistic | symmetric | 2 | 1 | -10.833 [-18.000, -7.000] | 5 | negative |
| optimistic | symmetric | 2 | 5 | -11.583 [-21.000, -5.500] | 5 | negative |
| optimistic | symmetric | 2 | 30 | -4.583 [-14.500, 3.250] | 5 | inside the interval: no claim |
| optimistic | inventory | 4 | 1 | -3.750 [-7.000, -0.500] | 3 | negative |
| optimistic | inventory | 4 | 5 | -4.375 [-8.250, -0.500] | 3 | negative |
| optimistic | inventory | 4 | 30 | -2.750 [-14.500, 9.000] | 3 | inside the interval: no claim |
| optimistic | symmetric | 4 | 1 | -3.750 [-7.000, -0.500] | 3 | negative |
| optimistic | symmetric | 4 | 5 | -4.375 [-8.250, -0.500] | 3 | negative |
| optimistic | symmetric | 4 | 30 | -2.750 [-14.500, 9.000] | 3 | inside the interval: no claim |

## Q3. Where the gap comes from: spread capture and inventory P&L

| fill rule | strategy | penalty (ticks) | replay spread capture | model spread capture | replay inventory P&L | model inventory P&L |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 26.918 [13.275, 38.896] | 577.829 [561.637, 594.155] | -12.194 [-43.550, 19.343] | 39.626 [-32.174, 112.141] |
| conservative | symmetric | 1 | 32.861 [14.054, 52.753] | 579.337 [563.409, 595.858] | -28.709 [-104.069, 29.692] | 42.413 [-41.033, 122.710] |
| conservative | inventory | 2 | 21.335 [10.501, 32.729] | 579.961 [563.223, 597.300] | -2.194 [-26.817, 22.583] | 25.668 [-41.235, 93.512] |
| conservative | symmetric | 2 | 24.418 [11.805, 35.417] | 579.392 [563.236, 596.298] | 0.821 [-31.250, 35.921] | 39.957 [-44.058, 118.693] |
| conservative | inventory | 4 | 28.838 [11.530, 45.502] | 575.494 [558.646, 591.775] | 11.302 [-16.958, 39.367] | 21.614 [-32.771, 75.751] |
| conservative | symmetric | 4 | 24.892 [11.755, 36.947] | 581.400 [564.856, 598.477] | 0.125 [-30.483, 33.242] | 35.294 [-45.340, 112.850] |
| optimistic | inventory | 1 | 45.083 [0.000, 80.750] | 1753.755 [1712.903, 1794.765] | 10.000 [-25.833, 61.917] | 41.656 [-45.982, 127.215] |
| optimistic | symmetric | 1 | 44.917 [0.000, 80.250] | 1753.333 [1711.760, 1795.109] | 10.000 [-25.833, 61.917] | 46.572 [-47.968, 144.311] |
| optimistic | inventory | 2 | 53.583 [17.250, 91.167] | 1755.075 [1713.923, 1795.766] | 23.583 [-12.167, 75.000] | 45.469 [-35.759, 124.911] |
| optimistic | symmetric | 2 | 44.250 [9.167, 80.417] | 1754.283 [1712.828, 1794.937] | 45.917 [-12.167, 111.250] | 50.837 [-43.163, 146.983] |
| optimistic | inventory | 4 | 26.917 [0.000, 61.417] | 1757.346 [1715.566, 1798.510] | 3.667 [-18.250, 29.250] | 39.240 [-33.325, 110.395] |
| optimistic | symmetric | 4 | 26.917 [0.000, 61.417] | 1752.176 [1711.280, 1793.853] | 3.667 [-18.250, 29.250] | 50.707 [-41.855, 143.249] |

## Q4. What queue position is worth: sticky minus always-requeue

| fill rule | strategy | penalty (ticks) | P&L difference | fills difference | verdict |
|---|---|---|---|---|---|
| conservative | inventory | 1 | 11.423 [0.000, 34.270] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | symmetric | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 2 | 11.423 [0.000, 34.270] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | symmetric | 2 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 2 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 2 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Q5. Tick size

In the calibration window the spread was one tick 0.0% of the time (mean 31.48 ticks), which puts this stock in the **small-tick** group. Compare Q4 across stocks in the two groups; one stock cannot answer Q5.

## Inventory strategy against symmetric

| fill rule | penalty (ticks) | P&L difference | |end inventory| difference (shares) | verdict |
|---|---|---|---|---|
| conservative | 1 | 10.572 [-17.126, 48.677] | -30.500 [-90.500, 0.000] | inside the interval: no claim |
| conservative | 2 | -6.097 [-17.626, -0.167] | -17.167 [-50.500, 0.000] | negative |
| conservative | 4 | 15.122 [-1.833, 47.532] | -34.833 [-104.500, 0.000] | inside the interval: no claim |
| optimistic | 1 | 0.167 [0.000, 0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | -13.000 [-39.000, 0.000] | -16.667 [-50.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Q6. Do the findings survive the choice of fill rule?

| finding | conservative | optimistic | verdict |
|---|---|---|---|
| markout 1s, inventory, 1 ticks | -2.950 [-5.300, -0.050] | -8.000 [-9.500, -7.000] | holds under both rules |
| markout 5s, inventory, 1 ticks | -4.408 [-6.717, -1.175] | -8.750 [-12.500, -5.500] | holds under both rules |
| markout 30s, inventory, 1 ticks | -4.758 [-11.417, 4.675] | -10.583 [-20.500, 3.250] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 1 ticks | 11.423 [0.000, 34.270] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 1 ticks | -3.495 [-5.700, -0.465] | -8.000 [-9.500, -7.000] | holds under both rules |
| markout 5s, symmetric, 1 ticks | -5.487 [-7.827, -2.000] | -8.750 [-12.500, -5.500] | holds under both rules |
| markout 30s, symmetric, 1 ticks | -5.030 [-11.667, 4.483] | -10.583 [-20.500, 3.250] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 1 ticks | 10.572 [-17.126, 48.677] | 0.167 [0.000, 0.500] | not established under both rules: not a conclusion |
| signal - inventory P&L, 1 ticks | 8.649 [-20.390, 45.837] | 35.083 [-10.250, 115.500] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 1 ticks | 0.500 [0.000, 1.500] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 1 ticks | 0.500 [0.000, 1.500] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 1 ticks | 0.500 [0.000, 1.500] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, inventory, 2 ticks | -3.467 [-5.500, -0.600] | -6.250 [-7.500, -4.250] | holds under both rules |
| markout 5s, inventory, 2 ticks | -4.917 [-7.100, -1.817] | -9.250 [-14.000, -5.500] | holds under both rules |
| markout 30s, inventory, 2 ticks | -5.450 [-12.500, 5.183] | -6.000 [-14.500, 3.250] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 2 ticks | 11.423 [0.000, 34.270] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 2 ticks | -3.675 [-5.700, -0.825] | -10.833 [-18.000, -7.000] | holds under both rules |
| markout 5s, symmetric, 2 ticks | -5.133 [-7.100, -1.900] | -11.583 [-21.000, -5.500] | holds under both rules |
| markout 30s, symmetric, 2 ticks | -5.617 [-12.500, 4.317] | -4.583 [-14.500, 3.250] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 2 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 2 ticks | -6.097 [-17.626, -0.167] | -13.000 [-39.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 2 ticks | 15.112 [-3.663, 49.000] | 13.000 [0.000, 39.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 2 ticks | 0.027 [0.000, 0.080] | -4.583 [-13.750, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 2 ticks | -0.130 [-0.650, 0.260] | -2.333 [-7.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 2 ticks | -0.967 [-2.167, 0.000] | 1.417 [0.000, 4.250] | not established under both rules: not a conclusion |
| markout 1s, inventory, 4 ticks | -4.200 [-5.900, -2.100] | -3.750 [-7.000, -0.500] | holds under both rules |
| markout 5s, inventory, 4 ticks | -6.036 [-7.783, -3.757] | -4.375 [-8.250, -0.500] | holds under both rules |
| markout 30s, inventory, 4 ticks | -7.576 [-13.233, -0.262] | -2.750 [-14.500, 9.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 4 ticks | -3.550 [-5.700, -0.450] | -3.750 [-7.000, -0.500] | holds under both rules |
| markout 5s, symmetric, 4 ticks | -5.225 [-7.683, -1.525] | -4.375 [-8.250, -0.500] | holds under both rules |
| markout 30s, symmetric, 4 ticks | -5.858 [-13.233, 4.692] | -2.750 [-14.500, 9.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 4 ticks | 15.122 [-1.833, 47.532] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 4 ticks | -11.963 [-27.187, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 4 ticks | 0.767 [0.000, 2.100] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 4 ticks | 0.602 [-0.193, 2.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 4 ticks | 0.385 [-0.846, 2.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |

## Q7. Does the order book predict the next price move?

Beyond the approach document's six questions. Each signal is positive when the book or the recent flow leans towards buyers. A line was fitted on the calibration window and scored on the test window, 11640 and 11640 one-second samples. The correlation is the mean over windows, with its interval; R² is measured against predicting no change.

![Signal correlation by horizon](signal_decay.svg)

| signal | horizon (s) | fitted slope (ticks per unit) | correlation, fit window | correlation, test windows | R², test | direction called | verdict |
|---|---|---|---|---|---|---|---|
| queue_imbalance | 1 | 0.2291 | 0.028 | 0.049 [0.035, 0.062] | 0.0023 | 58.1% of 2389 moves | positive |
| queue_imbalance | 5 | 0.4377 | 0.026 | 0.045 [0.017, 0.077] | 0.0021 | 54.9% of 6569 moves | positive |
| queue_imbalance | 10 | 0.2798 | 0.012 | 0.030 [-0.011, 0.070] | 0.0013 | 54.0% of 8072 moves | inside the interval: no claim |
| queue_imbalance | 30 | 0.2515 | 0.007 | 0.026 [-0.010, 0.059] | 0.0029 | 53.1% of 9225 moves | inside the interval: no claim |
| queue_imbalance | 60 | 0.3515 | 0.007 | -0.016 [-0.062, 0.024] | 0.0029 | 53.6% of 9195 moves | inside the interval: no claim |
| ofi | 1 | 0.0062 | 0.009 | 0.085 [0.072, 0.098] | 0.0015 | 61.0% of 2419 moves | positive |
| ofi | 5 | -0.0128 | -0.009 | 0.117 [0.099, 0.136] | -0.0017 | 40.6% of 6490 moves | positive |
| ofi | 10 | -0.0430 | -0.022 | 0.099 [0.081, 0.116] | -0.0033 | 43.4% of 7823 moves | positive |
| ofi | 30 | -0.0888 | -0.027 | 0.069 [0.026, 0.105] | -0.0011 | 45.0% of 8781 moves | positive |
| ofi | 60 | -0.0937 | -0.021 | 0.003 [-0.038, 0.050] | 0.0024 | 48.3% of 8728 moves | inside the interval: no claim |
| trade_imbalance | 1 | 0.0753 | 0.032 | 0.081 [0.069, 0.096] | 0.0063 | 61.7% of 1712 moves | positive |
| trade_imbalance | 5 | 0.1932 | 0.040 | 0.103 [0.082, 0.129] | 0.0103 | 59.0% of 4482 moves | positive |
| trade_imbalance | 10 | 0.2376 | 0.036 | 0.082 [0.065, 0.106] | 0.0078 | 57.8% of 5299 moves | positive |
| trade_imbalance | 30 | 0.4226 | 0.039 | 0.042 [0.025, 0.058] | 0.0055 | 56.7% of 5864 moves | positive |
| trade_imbalance | 60 | 0.3543 | 0.024 | 0.006 [-0.041, 0.045] | 0.0039 | 55.2% of 5834 moves | inside the interval: no claim |

## Q8. Does leaning quotes on the signal reduce adverse selection?

The signal strategy is the inventory strategy with both quotes shifted by the fitted move: `trade_imbalance` at the 5 s horizon, 0.001932 dollars per unit. It was chosen for the strongest correlation in the calibration window. Differences are signal minus inventory, paired by window; a positive markout difference means less adverse selection.

| fill rule | penalty (ticks) | P&L difference | fills difference | requotes where the skew moved a quote by a tick or more | verdict |
|---|---|---|---|---|---|
| conservative | 1 | 8.649 [-20.390, 45.837] | 0.000 [0.000, 0.000] | 1670 | inside the interval: no claim |
| conservative | 2 | 15.112 [-3.663, 49.000] | 0.167 [-0.500, 1.000] | 1781 | inside the interval: no claim |
| conservative | 4 | -11.963 [-27.187, 0.000] | -0.500 [-1.500, 0.000] | 1730 | inside the interval: no claim |
| optimistic | 1 | 35.083 [-10.250, 115.500] | 0.000 [-0.500, 0.500] | 1728 | inside the interval: no claim |
| optimistic | 2 | 13.000 [0.000, 39.000] | -0.167 [-0.500, 0.000] | 1746 | inside the interval: no claim |
| optimistic | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 1738 | inside the interval: no claim |

| fill rule | penalty (ticks) | horizon (s) | markout, signal | markout, inventory | difference | verdict |
|---|---|---|---|---|---|---|
| conservative | 1 | 1 | -2.450 [-5.100, 0.500] | -2.950 [-5.300, -0.050] | 0.500 [0.000, 1.500] | inside the interval: no claim |
| conservative | 1 | 5 | -3.908 [-6.517, -0.875] | -4.408 [-6.717, -1.175] | 0.500 [0.000, 1.500] | inside the interval: no claim |
| conservative | 1 | 30 | -4.258 [-11.017, 4.775] | -4.758 [-11.417, 4.675] | 0.500 [0.000, 1.500] | inside the interval: no claim |
| conservative | 2 | 1 | -3.440 [-5.500, -0.520] | -3.467 [-5.500, -0.600] | 0.027 [0.000, 0.080] | inside the interval: no claim |
| conservative | 2 | 5 | -5.047 [-7.533, -1.557] | -4.917 [-7.100, -1.817] | -0.130 [-0.650, 0.260] | inside the interval: no claim |
| conservative | 2 | 30 | -6.417 [-13.233, 3.383] | -5.450 [-12.500, 5.183] | -0.967 [-2.167, 0.000] | inside the interval: no claim |
| conservative | 4 | 1 | -3.433 [-5.600, -1.167] | -4.200 [-5.900, -2.100] | 0.767 [0.000, 2.100] | inside the interval: no claim |
| conservative | 4 | 5 | -5.433 [-7.333, -3.350] | -6.036 [-7.783, -3.757] | 0.602 [-0.193, 2.000] | inside the interval: no claim |
| conservative | 4 | 30 | -7.192 [-12.400, -0.942] | -7.576 [-13.233, -0.262] | 0.385 [-0.846, 2.000] | inside the interval: no claim |
| optimistic | 1 | 1 | -7.250 [-7.500, -7.000] | -7.250 [-7.500, -7.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 5 | -6.875 [-8.250, -5.500] | -6.875 [-8.250, -5.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 30 | -5.625 [-14.500, 3.250] | -5.625 [-14.500, 3.250] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 1 | -10.833 [-18.000, -7.000] | -6.250 [-7.500, -4.250] | -4.583 [-13.750, 0.000] | inside the interval: no claim |
| optimistic | 2 | 5 | -11.583 [-21.000, -5.500] | -9.250 [-14.000, -5.500] | -2.333 [-7.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 30 | -4.583 [-14.500, 3.250] | -6.000 [-14.500, 3.250] | 1.417 [0.000, 4.250] | inside the interval: no claim |
| optimistic | 4 | 1 | -3.750 [-7.000, -0.500] | -3.750 [-7.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 5 | -4.375 [-8.250, -0.500] | -4.375 [-8.250, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 30 | -2.750 [-14.500, 9.000] | -2.750 [-14.500, 9.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Diagnostics

| run | fills | orders posted | requotes that found our order overtaken |
|---|---|---|---|
| inventory/1t/sticky/conservative | 16 | 4876 | 0 |
| inventory/1t/requeue/conservative | 15 | 14700 | 0 |
| symmetric/1t/sticky/conservative | 16 | 4871 | 0 |
| symmetric/1t/requeue/conservative | 16 | 14702 | 0 |
| inventory/2t/sticky/conservative | 14 | 4888 | 0 |
| inventory/2t/requeue/conservative | 13 | 14696 | 0 |
| symmetric/2t/sticky/conservative | 14 | 4870 | 0 |
| symmetric/2t/requeue/conservative | 14 | 14698 | 0 |
| inventory/4t/sticky/conservative | 16 | 4886 | 0 |
| inventory/4t/requeue/conservative | 16 | 14702 | 0 |
| symmetric/4t/sticky/conservative | 13 | 4872 | 0 |
| symmetric/4t/requeue/conservative | 13 | 14696 | 0 |
| inventory/1t/sticky/optimistic | 5 | 4851 | 0 |
| inventory/1t/requeue/optimistic | 5 | 14680 | 0 |
| symmetric/1t/sticky/optimistic | 5 | 4848 | 0 |
| symmetric/1t/requeue/optimistic | 5 | 14680 | 0 |
| inventory/2t/sticky/optimistic | 6 | 4860 | 0 |
| inventory/2t/requeue/optimistic | 6 | 14682 | 0 |
| symmetric/2t/sticky/optimistic | 5 | 4851 | 0 |
| symmetric/2t/requeue/optimistic | 5 | 14680 | 0 |
| inventory/4t/sticky/optimistic | 3 | 4866 | 0 |
| inventory/4t/requeue/optimistic | 3 | 14676 | 0 |
| symmetric/4t/sticky/optimistic | 3 | 4864 | 0 |
| symmetric/4t/requeue/optimistic | 3 | 14676 | 0 |
| signal/1t/sticky/conservative | 16 | 5322 | 0 |
| signal/2t/sticky/conservative | 15 | 5347 | 0 |
| signal/4t/sticky/conservative | 13 | 5313 | 0 |
| signal/1t/sticky/optimistic | 5 | 5300 | 0 |
| signal/2t/sticky/optimistic | 5 | 5295 | 0 |
| signal/4t/sticky/optimistic | 3 | 5314 | 0 |

An overtaken order is one the real book moved through between requotes. In reality it would have traded; the replay only fills it at the next real execution (see README, limitations).
