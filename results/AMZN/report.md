# AMZN 2012-06-21: Avellaneda-Stoikov replay study

- Calibrated on 09:31:00 to 12:45:00; traded on 12:45:00 to 15:59:00.
- Windows of 1800 s, each an independent session. Requote every 1 s and after each fill. One lot = 100 shares per side.
- Figures are means over windows with a 95% bootstrap interval in brackets. A difference whose interval contains zero is not claimed.
- P&L is in dollars per window, before fees and rebates. Markouts are in ticks per share.

## Headline

Middle settings only; every setting is in the tables below.

- **Adverse selection.** 5 s after a fill, the mid had moved by conservative -7.866 ticks [-11.375, -4.194]; optimistic -7.770 ticks [-9.300, -5.783] per share (negative is against us). Across fill rules: holds under both rules.
- **Model against replay.** conservative: replay -5.786 [-70.619, 48.747] against the model's 365.416 [328.324, 402.467] dollars per window (replay below model); optimistic: replay 136.990 [67.480, 200.250] against the model's 1116.039 [1066.742, 1163.138] dollars per window (replay below model).
- **Prediction.** `trade_imbalance` had an out-of-sample correlation of 0.101 [0.064, 0.141] with the mid change over the next 5 s (positive). Leaning quotes on it changed the 5 s markout by conservative -1.769 ticks [-4.869, 0.500]; optimistic -0.795 ticks [-2.883, 1.343]. Across fill rules: not established under both rules: not a conclusion.

## Calibration

sigma = 0.0245602 dollars per sqrt(second), taken at the 60 s horizon.

![Variance ratio](variance_ratio.svg)

| horizon (s) | sigma ($/sqrt s) | increments | variance ratio vs longest |
|---|---|---|---|
| 1 | 0.022575 | 11639 | 0.758 |
| 2 | 0.022583 | 5819 | 0.758 |
| 5 | 0.022763 | 2327 | 0.770 |
| 10 | 0.023288 | 1163 | 0.806 |
| 30 | 0.024128 | 387 | 0.865 |
| 60 | 0.024560 | 193 | 0.897 |
| 120 | 0.026756 | 96 | 1.064 |
| 300 | 0.025935 | 38 | 1.000 |

### Fill intensity, conservative rule

A = 0.01698 per second, k = 6.4978 per dollar, from 4656 probes, 1918 filled, 210741 s of exposure.

![Fill intensity, conservative](intensity_conservative.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 361 | 32735 | 0.0735 | 0.01103 | 0.01053 |
| 1 | 773 | 366 | 33129 | 0.0809 | 0.01105 | 0.01012 |
| 2 | 760 | 318 | 34241 | 0.0924 | 0.00929 | 0.00940 |
| 3 | 796 | 310 | 36831 | 0.1011 | 0.00842 | 0.00889 |
| 4 | 740 | 286 | 34287 | 0.1131 | 0.00834 | 0.00828 |
| 5 | 811 | 277 | 39518 | 0.1238 | 0.00701 | 0.00772 |

### Fill intensity, optimistic rule

A = 0.032214 per second, k = 3.8799 per dollar, from 4656 probes, 3443 filled, 156378 s of exposure.

![Fill intensity, optimistic](intensity_optimistic.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 556 | 25207 | 0.0735 | 0.02206 | 0.02404 |
| 1 | 773 | 594 | 24387 | 0.0809 | 0.02436 | 0.02355 |
| 2 | 760 | 567 | 25164 | 0.0924 | 0.02253 | 0.02249 |
| 3 | 796 | 600 | 26942 | 0.1011 | 0.02227 | 0.02172 |
| 4 | 740 | 543 | 25454 | 0.1131 | 0.02133 | 0.02073 |
| 5 | 811 | 583 | 29225 | 0.1238 | 0.01995 | 0.01998 |

## Q1. Does the calibrated model predict replay P&L?

| fill rule | strategy | penalty (ticks) | replay P&L | model P&L | replay fills | model fills | verdict |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 9.110 [-79.816, 87.724] | 372.655 [330.520, 416.939] | 3.833 [1.833, 6.833] | 22.300 [21.695, 22.890] | replay below model |
| conservative | symmetric | 1 | -18.910 [-117.577, 67.588] | 376.082 [323.901, 426.998] | 4.167 [2.000, 7.000] | 22.105 [21.505, 22.710] | replay below model |
| conservative | inventory | 2 | -5.786 [-70.619, 48.747] | 365.416 [328.324, 402.467] | 2.833 [1.167, 5.333] | 22.000 [21.370, 22.610] | replay below model |
| conservative | symmetric | 2 | -20.021 [-94.467, 54.425] | 374.644 [323.856, 425.309] | 3.500 [1.500, 6.500] | 21.780 [21.175, 22.390] | replay below model |
| conservative | inventory | 4 | 20.761 [-25.129, 60.558] | 350.226 [322.199, 378.010] | 2.500 [0.833, 5.167] | 21.695 [21.080, 22.315] | replay below model |
| conservative | symmetric | 4 | -12.807 [-83.217, 53.821] | 372.501 [320.881, 422.732] | 2.833 [1.000, 5.000] | 21.200 [20.610, 21.795] | replay below model |
| optimistic | inventory | 1 | 132.833 [81.750, 180.417] | 1130.220 [1076.539, 1181.957] | 4.667 [2.167, 8.167] | 42.455 [41.595, 43.290] | replay below model |
| optimistic | symmetric | 1 | 139.167 [107.667, 167.500] | 1145.869 [1079.621, 1210.252] | 3.833 [2.500, 5.667] | 42.425 [41.600, 43.225] | replay below model |
| optimistic | inventory | 2 | 136.990 [67.480, 200.250] | 1116.039 [1066.742, 1163.138] | 4.500 [2.000, 7.833] | 42.230 [41.380, 43.060] | replay below model |
| optimistic | symmetric | 2 | 125.688 [66.958, 175.688] | 1147.172 [1081.033, 1210.059] | 4.333 [1.833, 7.333] | 42.075 [41.260, 42.900] | replay below model |
| optimistic | inventory | 4 | 125.333 [65.000, 188.500] | 1091.802 [1052.836, 1131.471] | 5.167 [2.500, 8.167] | 41.710 [40.830, 42.570] | replay below model |
| optimistic | symmetric | 4 | 44.521 [-39.167, 129.562] | 1146.900 [1082.516, 1211.413] | 3.833 [2.000, 6.500] | 41.355 [40.530, 42.180] | replay below model |

### Replay profit three ways

Every fill is booked at its own price. Shares still held when a window closes have no trade price, so the profit depends on how they are valued. Realised counts completed buy-and-sell pairs only (first in, first out). The middle column is the replay P&L used everywhere else in this report. The last column trades the leftover out against the real book at the close, level by level, which is what closing would have cost. Sticky quotes.

| run | realised | leftover valued at the mid | leftover closed at real prices | shares left at the close | shares traded per window |
|---|---|---|---|---|---|
| inventory/1t/sticky/conservative | 5.497 [0.000, 11.163] | 9.110 [-79.816, 87.724] | -2.190 [-93.582, 76.537] | 189 | 228 |
| symmetric/1t/sticky/conservative | 2.663 [0.000, 7.990] | -18.910 [-117.577, 67.588] | -35.945 [-149.203, 58.237] | 245 | 250 |
| inventory/2t/sticky/conservative | 4.675 [0.000, 14.025] | -5.786 [-70.619, 48.747] | -13.232 [-80.755, 39.920] | 134 | 200 |
| symmetric/2t/sticky/conservative | 0.000 [0.000, 0.000] | -20.021 [-94.467, 54.425] | -34.157 [-114.270, 41.267] | 224 | 224 |
| inventory/4t/sticky/conservative | 14.357 [0.000, 43.070] | 20.761 [-25.129, 60.558] | 17.312 [-28.625, 57.340] | 68 | 174 |
| symmetric/4t/sticky/conservative | 0.000 [0.000, 0.000] | -12.807 [-83.217, 53.821] | -23.023 [-98.543, 47.665] | 186 | 186 |
| inventory/1t/sticky/optimistic | 56.667 [5.667, 126.000] | 132.833 [81.750, 180.417] | 121.353 [68.020, 169.853] | 167 | 467 |
| symmetric/1t/sticky/optimistic | 27.333 [0.000, 66.333] | 139.167 [107.667, 167.500] | 122.893 [92.487, 149.227] | 217 | 383 |
| inventory/2t/sticky/optimistic | 84.440 [19.273, 159.047] | 136.990 [67.480, 200.250] | 129.105 [60.333, 193.772] | 122 | 444 |
| symmetric/2t/sticky/optimistic | 55.333 [15.667, 104.833] | 125.688 [66.958, 175.688] | 114.657 [58.990, 160.323] | 154 | 421 |
| inventory/4t/sticky/optimistic | 76.667 [20.500, 134.500] | 125.333 [65.000, 188.500] | 120.260 [58.760, 183.853] | 83 | 517 |
| symmetric/4t/sticky/optimistic | 20.875 [-34.333, 87.792] | 44.521 [-39.167, 129.562] | 38.802 [-44.147, 124.292] | 96 | 371 |
| signal/1t/sticky/conservative | 13.833 [-6.000, 47.500] | -16.418 [-88.335, 49.727] | -23.405 [-99.928, 47.027] | 131 | 198 |
| signal/2t/sticky/conservative | 15.928 [0.000, 47.595] | -9.923 [-77.539, 48.968] | -15.528 [-88.585, 46.813] | 106 | 179 |
| signal/4t/sticky/conservative | 1.577 [0.000, 4.730] | -3.072 [-50.176, 38.437] | -7.193 [-56.868, 34.937] | 80 | 120 |
| signal/1t/sticky/optimistic | 45.000 [-5.667, 101.000] | 96.250 [34.333, 151.917] | 89.593 [28.333, 143.520] | 117 | 450 |
| signal/2t/sticky/optimistic | 29.250 [-19.333, 74.167] | 79.042 [9.375, 140.542] | 74.710 [7.710, 132.667] | 82 | 418 |
| signal/4t/sticky/optimistic | 75.583 [20.667, 147.917] | 114.708 [48.000, 190.625] | 111.117 [45.000, 187.017] | 65 | 468 |

## Q2. Adverse selection: markouts on replay fills

Negative means the mid moved against us after the fill. In the model world the expected markout is zero.

![Markouts](markouts.svg)

| fill rule | strategy | penalty (ticks) | horizon (s) | markout (ticks) | fills | verdict |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 1 | -7.995 [-11.216, -4.208] | 23 | negative |
| conservative | inventory | 1 | 5 | -8.714 [-12.136, -4.792] | 23 | negative |
| conservative | inventory | 1 | 30 | -5.744 [-14.598, 2.292] | 23 | inside the interval: no claim |
| conservative | symmetric | 1 | 1 | -8.132 [-11.879, -4.417] | 25 | negative |
| conservative | symmetric | 1 | 5 | -8.667 [-11.734, -4.896] | 25 | negative |
| conservative | symmetric | 1 | 30 | -5.555 [-14.617, 2.390] | 25 | inside the interval: no claim |
| conservative | inventory | 2 | 1 | -6.588 [-9.921, -3.333] | 17 | negative |
| conservative | inventory | 2 | 5 | -7.866 [-11.375, -4.194] | 17 | negative |
| conservative | inventory | 2 | 30 | -7.616 [-18.833, 2.593] | 17 | inside the interval: no claim |
| conservative | symmetric | 2 | 1 | -6.933 [-10.867, -3.667] | 21 | negative |
| conservative | symmetric | 2 | 5 | -8.167 [-11.208, -4.625] | 21 | negative |
| conservative | symmetric | 2 | 30 | -7.596 [-19.000, 2.433] | 21 | inside the interval: no claim |
| conservative | inventory | 4 | 1 | -6.650 [-9.800, -3.400] | 15 | negative |
| conservative | inventory | 4 | 5 | -7.067 [-11.100, -3.400] | 15 | negative |
| conservative | inventory | 4 | 30 | -5.294 [-17.894, 3.850] | 15 | inside the interval: no claim |
| conservative | symmetric | 4 | 1 | -7.229 [-10.950, -3.400] | 17 | negative |
| conservative | symmetric | 4 | 5 | -7.612 [-11.500, -3.700] | 17 | negative |
| conservative | symmetric | 4 | 30 | -4.688 [-17.400, 5.075] | 17 | inside the interval: no claim |
| optimistic | inventory | 1 | 1 | -6.177 [-8.566, -3.212] | 28 | negative |
| optimistic | inventory | 1 | 5 | -6.112 [-8.778, -3.458] | 28 | negative |
| optimistic | inventory | 1 | 30 | -1.292 [-5.720, 3.328] | 28 | inside the interval: no claim |
| optimistic | symmetric | 1 | 1 | -7.142 [-10.448, -3.389] | 23 | negative |
| optimistic | symmetric | 1 | 5 | -6.979 [-10.458, -3.542] | 23 | negative |
| optimistic | symmetric | 1 | 30 | -1.899 [-4.708, 0.611] | 23 | inside the interval: no claim |
| optimistic | inventory | 2 | 1 | -6.265 [-8.473, -4.490] | 27 | negative |
| optimistic | inventory | 2 | 5 | -7.770 [-9.300, -5.783] | 27 | negative |
| optimistic | inventory | 2 | 30 | -3.367 [-6.375, -0.192] | 27 | negative |
| optimistic | symmetric | 2 | 1 | -5.836 [-8.338, -3.193] | 26 | negative |
| optimistic | symmetric | 2 | 5 | -6.495 [-9.506, -3.483] | 26 | negative |
| optimistic | symmetric | 2 | 30 | -2.509 [-4.840, -0.091] | 26 | negative |
| optimistic | inventory | 4 | 1 | -4.304 [-6.625, -1.917] | 31 | negative |
| optimistic | inventory | 4 | 5 | -4.648 [-8.148, -1.981] | 31 | negative |
| optimistic | inventory | 4 | 30 | -2.098 [-4.292, 0.644] | 31 | inside the interval: no claim |
| optimistic | symmetric | 4 | 1 | -4.462 [-6.439, -2.729] | 23 | negative |
| optimistic | symmetric | 4 | 5 | -4.901 [-7.450, -2.660] | 23 | negative |
| optimistic | symmetric | 4 | 30 | -2.397 [-5.958, 0.756] | 23 | inside the interval: no claim |

## Q3. Where the gap comes from: spread capture and inventory P&L

| fill rule | strategy | penalty (ticks) | replay spread capture | model spread capture | replay inventory P&L | model inventory P&L |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 17.790 [7.407, 27.629] | 346.745 [337.195, 356.257] | -8.680 [-100.848, 73.734] | 25.910 [-15.431, 69.151] |
| conservative | symmetric | 1 | 21.979 [6.018, 42.980] | 345.548 [336.184, 355.005] | -40.889 [-157.775, 55.812] | 30.534 [-20.446, 81.865] |
| conservative | inventory | 2 | 16.298 [6.747, 27.258] | 343.772 [333.907, 353.716] | -22.084 [-87.907, 33.748] | 21.644 [-13.773, 58.009] |
| conservative | symmetric | 2 | 19.955 [6.104, 36.167] | 345.684 [336.050, 355.428] | -39.976 [-124.658, 38.132] | 28.960 [-21.306, 78.757] |
| conservative | inventory | 4 | 12.036 [4.233, 24.128] | 339.917 [330.156, 349.730] | 8.725 [-30.400, 42.833] | 10.309 [-16.378, 37.972] |
| conservative | symmetric | 4 | 17.638 [7.063, 30.359] | 346.502 [336.839, 356.267] | -30.446 [-109.258, 44.100] | 25.998 [-24.471, 74.572] |
| optimistic | inventory | 1 | 106.333 [53.917, 176.167] | 1099.244 [1076.790, 1120.488] | 26.500 [-11.167, 65.417] | 30.976 [-18.010, 78.129] |
| optimistic | symmetric | 1 | 91.250 [61.250, 129.833] | 1102.853 [1081.423, 1123.618] | 47.917 [2.083, 83.750] | 43.016 [-18.296, 104.621] |
| optimistic | inventory | 2 | 100.707 [44.957, 169.997] | 1094.795 [1072.892, 1116.512] | 36.283 [-6.383, 86.583] | 21.243 [-21.274, 62.582] |
| optimistic | symmetric | 2 | 101.167 [46.167, 163.333] | 1103.007 [1081.615, 1124.581] | 24.521 [-25.458, 65.750] | 44.165 [-16.699, 104.343] |
| optimistic | inventory | 4 | 111.750 [60.583, 168.833] | 1081.317 [1058.734, 1103.828] | 13.583 [-44.000, 63.583] | 10.485 [-21.900, 42.510] |
| optimistic | symmetric | 4 | 86.083 [45.583, 145.250] | 1102.082 [1080.131, 1123.948] | -41.562 [-114.500, 25.521] | 44.818 [-16.066, 106.412] |

## Q4. What queue position is worth: sticky minus always-requeue

| fill rule | strategy | penalty (ticks) | P&L difference | fills difference | verdict |
|---|---|---|---|---|---|
| conservative | inventory | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 1 | 3.983 [0.000, 11.948] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 2 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 2 | 3.983 [0.000, 11.948] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 1 | 7.333 [-6.500, 19.417] | 0.500 [0.167, 0.833] | inside the interval: no claim |
| optimistic | symmetric | 1 | 15.500 [5.833, 24.083] | 0.667 [0.333, 1.000] | positive |
| optimistic | inventory | 2 | 15.667 [2.083, 33.167] | 0.667 [0.167, 1.333] | positive |
| optimistic | symmetric | 2 | 25.833 [7.667, 49.250] | 0.833 [0.333, 1.333] | positive |
| optimistic | inventory | 4 | 32.917 [3.917, 71.583] | 1.167 [0.167, 2.500] | positive |
| optimistic | symmetric | 4 | 20.833 [0.000, 47.000] | 0.500 [0.000, 0.833] | inside the interval: no claim |

## Q5. Tick size

In the calibration window the spread was one tick 0.1% of the time (mean 14.43 ticks), which puts this stock in the **small-tick** group. Compare Q4 across stocks in the two groups; one stock cannot answer Q5.

## Inventory strategy against symmetric

| fill rule | penalty (ticks) | P&L difference | |end inventory| difference (shares) | verdict |
|---|---|---|---|---|
| conservative | 1 | 28.020 [-16.327, 88.413] | -55.833 [-232.333, 65.167] | inside the interval: no claim |
| conservative | 2 | 14.235 [-19.455, 64.720] | -89.833 [-240.333, 21.000] | inside the interval: no claim |
| conservative | 4 | 33.568 [-18.110, 102.890] | -118.167 [-254.333, -15.667] | inside the interval: no claim |
| optimistic | 1 | -6.333 [-49.417, 45.083] | -50.000 [-150.000, 33.333] | inside the interval: no claim |
| optimistic | 2 | 11.303 [-47.197, 72.740] | -31.833 [-126.167, 72.333] | inside the interval: no claim |
| optimistic | 4 | 80.812 [25.833, 148.812] | -12.500 [-66.667, 41.667] | positive |

## Q6. Do the findings survive the choice of fill rule?

| finding | conservative | optimistic | verdict |
|---|---|---|---|
| markout 1s, inventory, 1 ticks | -7.995 [-11.216, -4.208] | -6.177 [-8.566, -3.212] | holds under both rules |
| markout 5s, inventory, 1 ticks | -8.714 [-12.136, -4.792] | -6.112 [-8.778, -3.458] | holds under both rules |
| markout 30s, inventory, 1 ticks | -5.744 [-14.598, 2.292] | -1.292 [-5.720, 3.328] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 1 ticks | 0.000 [0.000, 0.000] | 7.333 [-6.500, 19.417] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 1 ticks | -8.132 [-11.879, -4.417] | -7.142 [-10.448, -3.389] | holds under both rules |
| markout 5s, symmetric, 1 ticks | -8.667 [-11.734, -4.896] | -6.979 [-10.458, -3.542] | holds under both rules |
| markout 30s, symmetric, 1 ticks | -5.555 [-14.617, 2.390] | -1.899 [-4.708, 0.611] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 1 ticks | 3.983 [0.000, 11.948] | 15.500 [5.833, 24.083] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 1 ticks | 28.020 [-16.327, 88.413] | -6.333 [-49.417, 45.083] | not established under both rules: not a conclusion |
| signal - inventory P&L, 1 ticks | -25.528 [-65.347, 7.778] | -36.583 [-90.583, 5.417] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 1 ticks | -1.872 [-4.650, 0.614] | 0.484 [-0.718, 1.787] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 1 ticks | -1.371 [-4.330, 0.937] | -0.509 [-3.048, 1.653] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 1 ticks | -1.730 [-4.681, 0.680] | -1.204 [-5.524, 1.993] | not established under both rules: not a conclusion |
| markout 1s, inventory, 2 ticks | -6.588 [-9.921, -3.333] | -6.265 [-8.473, -4.490] | holds under both rules |
| markout 5s, inventory, 2 ticks | -7.866 [-11.375, -4.194] | -7.770 [-9.300, -5.783] | holds under both rules |
| markout 30s, inventory, 2 ticks | -7.616 [-18.833, 2.593] | -3.367 [-6.375, -0.192] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 2 ticks | 0.000 [0.000, 0.000] | 15.667 [2.083, 33.167] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 2 ticks | -6.933 [-10.867, -3.667] | -5.836 [-8.338, -3.193] | holds under both rules |
| markout 5s, symmetric, 2 ticks | -8.167 [-11.208, -4.625] | -6.495 [-9.506, -3.483] | holds under both rules |
| markout 30s, symmetric, 2 ticks | -7.596 [-19.000, 2.433] | -2.509 [-4.840, -0.091] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 2 ticks | 3.983 [0.000, 11.948] | 25.833 [7.667, 49.250] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 2 ticks | 14.235 [-19.455, 64.720] | 11.303 [-47.197, 72.740] | not established under both rules: not a conclusion |
| signal - inventory P&L, 2 ticks | -4.137 [-40.471, 39.750] | -57.948 [-119.262, -5.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 2 ticks | -1.007 [-3.450, 1.043] | -0.235 [-2.503, 1.755] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 2 ticks | -1.769 [-4.869, 0.500] | -0.795 [-2.883, 1.343] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 2 ticks | 1.164 [-5.294, 10.014] | -4.023 [-6.627, -1.980] | not established under both rules: not a conclusion |
| markout 1s, inventory, 4 ticks | -6.650 [-9.800, -3.400] | -4.304 [-6.625, -1.917] | holds under both rules |
| markout 5s, inventory, 4 ticks | -7.067 [-11.100, -3.400] | -4.648 [-8.148, -1.981] | holds under both rules |
| markout 30s, inventory, 4 ticks | -5.294 [-17.894, 3.850] | -2.098 [-4.292, 0.644] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 4 ticks | 0.000 [0.000, 0.000] | 32.917 [3.917, 71.583] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 4 ticks | -7.229 [-10.950, -3.400] | -4.462 [-6.439, -2.729] | holds under both rules |
| markout 5s, symmetric, 4 ticks | -7.612 [-11.500, -3.700] | -4.901 [-7.450, -2.660] | holds under both rules |
| markout 30s, symmetric, 4 ticks | -4.688 [-17.400, 5.075] | -2.397 [-5.958, 0.756] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 4 ticks | 0.000 [0.000, 0.000] | 20.833 [0.000, 47.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 4 ticks | 33.568 [-18.110, 102.890] | 80.812 [25.833, 148.812] | not established under both rules: not a conclusion |
| signal - inventory P&L, 4 ticks | -23.832 [-60.023, 0.308] | -10.625 [-29.167, 6.875] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 4 ticks | -2.152 [-4.562, -0.125] | 1.220 [-0.097, 2.870] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 4 ticks | -2.765 [-6.062, -0.125] | 0.545 [-1.153, 2.944] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 4 ticks | -2.257 [-6.062, -0.125] | -1.023 [-3.324, 0.679] | not established under both rules: not a conclusion |

## Q7. Does the order book predict the next price move?

Beyond the approach document's six questions. Each signal is positive when the book or the recent flow leans towards buyers. A line was fitted on the calibration window and scored on the test window, 11640 and 11640 one-second samples. The correlation is the mean over windows, with its interval; R² is measured against predicting no change.

![Signal correlation by horizon](signal_decay.svg)

| signal | horizon (s) | fitted slope (ticks per unit) | correlation, fit window | correlation, test windows | R², test | direction called | verdict |
|---|---|---|---|---|---|---|---|
| queue_imbalance | 1 | 0.1200 | 0.031 | 0.056 [0.042, 0.074] | 0.0032 | 58.1% of 2640 moves | positive |
| queue_imbalance | 5 | 0.1324 | 0.015 | 0.061 [0.050, 0.073] | 0.0024 | 56.8% of 6366 moves | positive |
| queue_imbalance | 10 | 0.0629 | 0.005 | 0.049 [0.034, 0.065] | 0.0012 | 54.8% of 7905 moves | positive |
| queue_imbalance | 30 | -0.2970 | -0.013 | 0.006 [-0.041, 0.041] | 0.0006 | 48.2% of 9207 moves | inside the interval: no claim |
| queue_imbalance | 60 | -1.2450 | -0.038 | 0.004 [-0.070, 0.077] | -0.0026 | 47.2% of 9205 moves | inside the interval: no claim |
| ofi | 1 | 0.0063 | 0.032 | 0.068 [0.041, 0.098] | 0.0024 | 57.4% of 2614 moves | positive |
| ofi | 5 | 0.0227 | 0.050 | 0.071 [0.018, 0.122] | 0.0008 | 55.9% of 5989 moves | positive |
| ofi | 10 | 0.0408 | 0.063 | 0.081 [0.026, 0.134] | 0.0015 | 55.6% of 7241 moves | positive |
| ofi | 30 | 0.0507 | 0.044 | 0.056 [0.014, 0.087] | 0.0017 | 52.7% of 8262 moves | positive |
| ofi | 60 | 0.0516 | 0.031 | 0.011 [-0.026, 0.042] | 0.0028 | 51.9% of 8227 moves | inside the interval: no claim |
| trade_imbalance | 1 | 0.0507 | 0.068 | 0.095 [0.070, 0.125] | 0.0103 | 61.0% of 1803 moves | positive |
| trade_imbalance | 5 | 0.1722 | 0.101 | 0.101 [0.064, 0.141] | 0.0086 | 59.1% of 3942 moves | positive |
| trade_imbalance | 10 | 0.2331 | 0.095 | 0.100 [0.042, 0.159] | 0.0082 | 57.2% of 4654 moves | positive |
| trade_imbalance | 30 | 0.4425 | 0.101 | 0.063 [0.007, 0.111] | -0.0018 | 54.3% of 5233 moves | positive |
| trade_imbalance | 60 | 0.7017 | 0.113 | 0.024 [-0.038, 0.081] | -0.0124 | 53.9% of 5165 moves | inside the interval: no claim |

## Q8. Does leaning quotes on the signal reduce adverse selection?

The signal strategy is the inventory strategy with both quotes shifted by the fitted move: `trade_imbalance` at the 5 s horizon, 0.001722 dollars per unit. It was chosen for the strongest correlation in the calibration window. Differences are signal minus inventory, paired by window; a positive markout difference means less adverse selection.

| fill rule | penalty (ticks) | P&L difference | fills difference | requotes where the skew moved a quote by a tick or more | verdict |
|---|---|---|---|---|---|
| conservative | 1 | -25.528 [-65.347, 7.778] | -1.333 [-2.500, -0.333] | 1679 | inside the interval: no claim |
| conservative | 2 | -4.137 [-40.471, 39.750] | -0.333 [-0.833, 0.333] | 1706 | inside the interval: no claim |
| conservative | 4 | -23.832 [-60.023, 0.308] | -0.667 [-1.333, -0.167] | 1676 | inside the interval: no claim |
| optimistic | 1 | -36.583 [-90.583, 5.417] | -0.167 [-0.500, 0.000] | 1718 | inside the interval: no claim |
| optimistic | 2 | -57.948 [-119.262, -5.000] | -0.167 [-1.167, 0.833] | 1672 | negative |
| optimistic | 4 | -10.625 [-29.167, 6.875] | -0.333 [-1.167, 0.500] | 1726 | inside the interval: no claim |

| fill rule | penalty (ticks) | horizon (s) | markout, signal | markout, inventory | difference | verdict |
|---|---|---|---|---|---|---|
| conservative | 1 | 1 | -9.867 [-15.137, -4.492] | -7.995 [-11.216, -4.208] | -1.872 [-4.650, 0.614] | inside the interval: no claim |
| conservative | 1 | 5 | -10.085 [-16.173, -4.333] | -8.714 [-12.136, -4.792] | -1.371 [-4.330, 0.937] | inside the interval: no claim |
| conservative | 1 | 30 | -7.474 [-16.833, 1.194] | -5.744 [-14.598, 2.292] | -1.730 [-4.681, 0.680] | inside the interval: no claim |
| conservative | 2 | 1 | -8.113 [-14.312, -2.600] | -7.106 [-10.906, -3.400] | -1.007 [-3.450, 1.043] | inside the interval: no claim |
| conservative | 2 | 5 | -9.208 [-16.325, -3.217] | -7.439 [-11.639, -3.467] | -1.769 [-4.869, 0.500] | inside the interval: no claim |
| conservative | 2 | 30 | -3.875 [-10.350, 2.375] | -5.039 [-17.550, 4.222] | 1.164 [-5.294, 10.014] | inside the interval: no claim |
| conservative | 4 | 1 | -9.214 [-15.375, -3.500] | -7.062 [-10.812, -3.000] | -2.152 [-4.562, -0.125] | negative |
| conservative | 4 | 5 | -9.848 [-18.188, -3.125] | -7.083 [-12.125, -2.708] | -2.765 [-6.062, -0.125] | negative |
| conservative | 4 | 30 | -1.375 [-9.750, 5.875] | 0.882 [-3.681, 6.062] | -2.257 [-6.062, -0.125] | negative |
| optimistic | 1 | 1 | -5.693 [-8.344, -2.659] | -6.177 [-8.566, -3.212] | 0.484 [-0.718, 1.787] | inside the interval: no claim |
| optimistic | 1 | 5 | -6.621 [-9.046, -4.278] | -6.112 [-8.778, -3.458] | -0.509 [-3.048, 1.653] | inside the interval: no claim |
| optimistic | 1 | 30 | -2.496 [-7.159, 2.667] | -1.292 [-5.720, 3.328] | -1.204 [-5.524, 1.993] | inside the interval: no claim |
| optimistic | 2 | 1 | -6.500 [-8.190, -4.850] | -6.265 [-8.473, -4.490] | -0.235 [-2.503, 1.755] | inside the interval: no claim |
| optimistic | 2 | 5 | -8.565 [-11.120, -5.665] | -7.770 [-9.300, -5.783] | -0.795 [-2.883, 1.343] | inside the interval: no claim |
| optimistic | 2 | 30 | -7.390 [-9.100, -5.100] | -3.367 [-6.375, -0.192] | -4.023 [-6.627, -1.980] | negative |
| optimistic | 4 | 1 | -3.085 [-4.196, -1.681] | -4.304 [-6.625, -1.917] | 1.220 [-0.097, 2.870] | inside the interval: no claim |
| optimistic | 4 | 5 | -4.103 [-5.533, -2.403] | -4.648 [-8.148, -1.981] | 0.545 [-1.153, 2.944] | inside the interval: no claim |
| optimistic | 4 | 30 | -3.121 [-4.847, -1.633] | -2.098 [-4.292, 0.644] | -1.023 [-3.324, 0.679] | inside the interval: no claim |

## Diagnostics

| run | fills | orders posted | requotes that found our order overtaken |
|---|---|---|---|
| inventory/1t/sticky/conservative | 23 | 4994 | 0 |
| inventory/1t/requeue/conservative | 23 | 17190 | 0 |
| symmetric/1t/sticky/conservative | 25 | 4996 | 0 |
| symmetric/1t/requeue/conservative | 25 | 17194 | 0 |
| inventory/2t/sticky/conservative | 17 | 4978 | 0 |
| inventory/2t/requeue/conservative | 17 | 17178 | 0 |
| symmetric/2t/sticky/conservative | 21 | 4991 | 0 |
| symmetric/2t/requeue/conservative | 21 | 17186 | 0 |
| inventory/4t/sticky/conservative | 15 | 5002 | 0 |
| inventory/4t/requeue/conservative | 15 | 17174 | 0 |
| symmetric/4t/sticky/conservative | 17 | 4996 | 0 |
| symmetric/4t/requeue/conservative | 17 | 17178 | 0 |
| inventory/1t/sticky/optimistic | 28 | 5009 | 0 |
| inventory/1t/requeue/optimistic | 25 | 17194 | 0 |
| symmetric/1t/sticky/optimistic | 23 | 4980 | 0 |
| symmetric/1t/requeue/optimistic | 19 | 17182 | 0 |
| inventory/2t/sticky/optimistic | 27 | 4962 | 0 |
| inventory/2t/requeue/optimistic | 23 | 17190 | 0 |
| symmetric/2t/sticky/optimistic | 26 | 4985 | 0 |
| symmetric/2t/requeue/optimistic | 21 | 17186 | 0 |
| inventory/4t/sticky/optimistic | 31 | 5017 | 0 |
| inventory/4t/requeue/optimistic | 24 | 17192 | 0 |
| symmetric/4t/sticky/optimistic | 23 | 4997 | 0 |
| symmetric/4t/requeue/optimistic | 20 | 17184 | 0 |
| signal/1t/sticky/conservative | 15 | 5424 | 0 |
| signal/2t/sticky/conservative | 15 | 5380 | 0 |
| signal/4t/sticky/conservative | 11 | 5384 | 0 |
| signal/1t/sticky/optimistic | 27 | 5403 | 0 |
| signal/2t/sticky/optimistic | 26 | 5413 | 0 |
| signal/4t/sticky/optimistic | 29 | 5430 | 0 |

An overtaken order is one the real book moved through between requotes. In reality it would have traded; the replay only fills it at the next real execution (see README, limitations).
