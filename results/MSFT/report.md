# MSFT 2012-06-21: Avellaneda-Stoikov replay study

- Calibrated on 09:31:00 to 12:45:00; traded on 12:45:00 to 15:59:00.
- Windows of 1800 s, each an independent session. Requote every 1 s and after each fill. One lot = 100 shares per side.
- Figures are means over windows with a 95% bootstrap interval in brackets. A difference whose interval contains zero is not claimed.
- P&L is in dollars per window, before fees and rebates. Markouts are in ticks per share.

## Headline

Middle settings only; every setting is in the tables below.

- **Adverse selection.** 5 s after a fill, the mid had moved by conservative -0.833 ticks [-1.000, -0.500]; optimistic -0.833 ticks [-1.000, -0.500] per share (negative is against us). Across fill rules: holds under both rules.
- **Model against replay.** conservative: replay -0.833 [-2.500, 0.250] against the model's 31.868 [30.067, 33.615] dollars per window (replay below model); optimistic: replay -0.833 [-2.500, 0.250] against the model's 32.202 [30.372, 33.984] dollars per window (replay below model).
- **Prediction.** `queue_imbalance` had an out-of-sample correlation of 0.264 [0.246, 0.281] with the mid change over the next 5 s (positive). Leaning quotes on it changed the 5 s markout by conservative 0.000 ticks [0.000, 0.000]; optimistic 0.000 ticks [0.000, 0.000]. Across fill rules: not established under both rules: not a conclusion.

## Calibration

sigma = 0.00288488 dollars per sqrt(second), taken at the 60 s horizon.

![Variance ratio](variance_ratio.svg)

| horizon (s) | sigma ($/sqrt s) | increments | variance ratio vs longest |
|---|---|---|---|
| 1 | 0.002918 | 11639 | 0.676 |
| 2 | 0.002935 | 5819 | 0.684 |
| 5 | 0.002874 | 2327 | 0.655 |
| 10 | 0.002970 | 1163 | 0.700 |
| 30 | 0.002863 | 387 | 0.651 |
| 60 | 0.002885 | 193 | 0.661 |
| 120 | 0.002896 | 96 | 0.666 |
| 300 | 0.003549 | 38 | 1.000 |

### Fill intensity, conservative rule

A = 0.020303 per second, k = 71.8 per dollar, from 4656 probes, 946 filled, 246860 s of exposure.

![Fill intensity, conservative](intensity_conservative.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 428 | 29122 | 0.0051 | 0.01470 | 0.01413 |
| 1 | 773 | 253 | 38310 | 0.0150 | 0.00660 | 0.00691 |
| 2 | 760 | 133 | 41898 | 0.0250 | 0.00317 | 0.00336 |
| 3 | 796 | 70 | 46043 | 0.0351 | 0.00152 | 0.00164 |
| 4 | 740 | 37 | 43490 | 0.0451 | 0.00085 | 0.00080 |
| 5 | 811 | 25 | 47999 | 0.0550 | 0.00052 | 0.00039 |

### Fill intensity, optimistic rule

A = 0.020543 per second, k = 71.957 per dollar, from 4656 probes, 951 filled, 246475 s of exposure.

![Fill intensity, optimistic](intensity_optimistic.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 431 | 28925 | 0.0051 | 0.01490 | 0.01429 |
| 1 | 773 | 254 | 38169 | 0.0150 | 0.00665 | 0.00697 |
| 2 | 760 | 133 | 41896 | 0.0250 | 0.00317 | 0.00339 |
| 3 | 796 | 70 | 46043 | 0.0351 | 0.00152 | 0.00165 |
| 4 | 740 | 37 | 43490 | 0.0451 | 0.00085 | 0.00080 |
| 5 | 811 | 26 | 47953 | 0.0550 | 0.00054 | 0.00039 |

## Q1. Does the calibrated model predict replay P&L?

| fill rule | strategy | penalty (ticks) | replay P&L | model P&L | replay fills | model fills | verdict |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -0.917 [-2.583, 0.167] | 35.117 [32.759, 37.330] | 0.833 [0.333, 1.333] | 24.540 [23.895, 25.170] | replay below model |
| conservative | symmetric | 1 | -0.917 [-2.583, 0.167] | 40.426 [34.481, 46.361] | 0.833 [0.333, 1.333] | 22.790 [22.175, 23.385] | replay below model |
| conservative | inventory | 2 | -0.833 [-2.500, 0.250] | 31.868 [30.067, 33.615] | 0.667 [0.167, 1.333] | 22.710 [22.070, 23.350] | replay below model |
| conservative | symmetric | 2 | 0.083 [-0.167, 0.333] | 37.549 [32.544, 42.377] | 0.500 [0.167, 0.833] | 19.545 [18.965, 20.150] | replay below model |
| conservative | inventory | 4 | -0.917 [-2.583, 0.000] | 26.890 [25.351, 28.444] | 0.500 [0.000, 1.167] | 19.070 [18.410, 19.750] | replay below model |
| conservative | symmetric | 4 | 0.000 [-0.250, 0.250] | 32.933 [28.745, 36.995] | 0.333 [0.000, 0.667] | 14.780 [14.260, 15.295] | replay below model |
| optimistic | inventory | 1 | -0.917 [-2.583, 0.167] | 35.296 [32.923, 37.487] | 0.833 [0.333, 1.333] | 24.780 [24.125, 25.420] | replay below model |
| optimistic | symmetric | 1 | -0.917 [-2.583, 0.167] | 40.643 [34.693, 46.485] | 0.833 [0.333, 1.333] | 23.000 [22.385, 23.605] | replay below model |
| optimistic | inventory | 2 | -0.833 [-2.500, 0.250] | 32.202 [30.372, 33.984] | 0.667 [0.167, 1.333] | 22.950 [22.290, 23.605] | replay below model |
| optimistic | symmetric | 2 | 0.083 [-0.167, 0.333] | 37.528 [32.374, 42.277] | 0.500 [0.167, 0.833] | 19.700 [19.110, 20.305] | replay below model |
| optimistic | inventory | 4 | -0.917 [-2.583, 0.000] | 27.014 [25.462, 28.571] | 0.500 [0.000, 1.167] | 19.275 [18.605, 19.965] | replay below model |
| optimistic | symmetric | 4 | 0.000 [-0.250, 0.250] | 33.263 [29.176, 37.338] | 0.333 [0.000, 0.667] | 14.965 [14.430, 15.485] | replay below model |

### Replay profit three ways

Every fill is booked at its own price. Shares still held when a window closes have no trade price, so the profit depends on how they are valued. Realised counts completed buy-and-sell pairs only (first in, first out). The middle column is the replay P&L used everywhere else in this report. The last column trades the leftover out against the real book at the close, level by level, which is what closing would have cost. Sticky quotes.

| run | realised | leftover valued at the mid | leftover closed at real prices | shares left at the close | shares traded per window |
|---|---|---|---|---|---|
| inventory/1t/sticky/conservative | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.167] | -1.167 [-2.667, -0.167] | 50 | 83 |
| symmetric/1t/sticky/conservative | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.167] | -1.167 [-2.667, -0.167] | 50 | 83 |
| inventory/2t/sticky/conservative | -0.833 [-2.500, 0.000] | -0.833 [-2.500, 0.250] | -1.000 [-2.667, 0.000] | 33 | 67 |
| symmetric/2t/sticky/conservative | 0.000 [0.000, 0.000] | 0.083 [-0.167, 0.333] | -0.167 [-0.500, 0.000] | 50 | 50 |
| inventory/4t/sticky/conservative | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.000] | -1.000 [-2.667, 0.000] | 17 | 50 |
| symmetric/4t/sticky/conservative | 0.000 [0.000, 0.000] | 0.000 [-0.250, 0.250] | -0.167 [-0.500, 0.000] | 33 | 33 |
| inventory/1t/sticky/optimistic | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.167] | -1.167 [-2.667, -0.167] | 50 | 83 |
| symmetric/1t/sticky/optimistic | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.167] | -1.167 [-2.667, -0.167] | 50 | 83 |
| inventory/2t/sticky/optimistic | -0.833 [-2.500, 0.000] | -0.833 [-2.500, 0.250] | -1.000 [-2.667, 0.000] | 33 | 67 |
| symmetric/2t/sticky/optimistic | 0.000 [0.000, 0.000] | 0.083 [-0.167, 0.333] | -0.167 [-0.500, 0.000] | 50 | 50 |
| inventory/4t/sticky/optimistic | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.000] | -1.000 [-2.667, 0.000] | 17 | 50 |
| symmetric/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 0.000 [-0.250, 0.250] | -0.167 [-0.500, 0.000] | 33 | 33 |
| signal/1t/sticky/conservative | -0.833 [-2.500, 0.000] | -1.417 [-3.167, 0.083] | -1.667 [-3.333, -0.167] | 50 | 83 |
| signal/2t/sticky/conservative | -0.833 [-2.500, 0.000] | -1.417 [-3.167, 0.083] | -1.667 [-3.333, -0.167] | 50 | 83 |
| signal/4t/sticky/conservative | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.000] | -1.000 [-2.667, 0.000] | 17 | 50 |
| signal/1t/sticky/optimistic | -0.833 [-2.500, 0.000] | -1.417 [-3.167, 0.083] | -1.667 [-3.333, -0.167] | 50 | 83 |
| signal/2t/sticky/optimistic | -0.833 [-2.500, 0.000] | -1.417 [-3.167, 0.083] | -1.667 [-3.333, -0.167] | 50 | 83 |
| signal/4t/sticky/optimistic | -0.833 [-2.500, 0.000] | -0.917 [-2.583, 0.000] | -1.000 [-2.667, 0.000] | 17 | 50 |

## Q2. Adverse selection: markouts on replay fills

Negative means the mid moved against us after the fill. In the model world the expected markout is zero.

![Markouts](markouts.svg)

| fill rule | strategy | penalty (ticks) | horizon (s) | markout (ticks) | fills | verdict |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 1 | -1.000 [-1.000, -1.000] | 5 | negative |
| conservative | inventory | 1 | 5 | -1.375 [-2.500, -0.625] | 5 | negative |
| conservative | inventory | 1 | 30 | -1.125 [-1.875, -0.375] | 5 | negative |
| conservative | symmetric | 1 | 1 | -1.000 [-1.000, -1.000] | 5 | negative |
| conservative | symmetric | 1 | 5 | -1.375 [-2.500, -0.625] | 5 | negative |
| conservative | symmetric | 1 | 30 | -1.125 [-1.875, -0.375] | 5 | negative |
| conservative | inventory | 2 | 1 | -1.000 [-1.000, -1.000] | 4 | negative |
| conservative | inventory | 2 | 5 | -0.833 [-1.000, -0.500] | 4 | negative |
| conservative | inventory | 2 | 30 | -0.833 [-1.500, 0.000] | 4 | inside the interval: no claim |
| conservative | symmetric | 2 | 1 | -1.000 [-1.000, -1.000] | 3 | negative |
| conservative | symmetric | 2 | 5 | -1.000 [-1.000, -1.000] | 3 | negative |
| conservative | symmetric | 2 | 30 | -1.333 [-3.000, 0.000] | 3 | inside the interval: no claim |
| conservative | inventory | 4 | 1 | -1.000 [-1.000, -1.000] | 3 | negative |
| conservative | inventory | 4 | 5 | -0.750 [-1.000, -0.500] | 3 | negative |
| conservative | inventory | 4 | 30 | -1.250 [-1.500, -1.000] | 3 | negative |
| conservative | symmetric | 4 | 1 | -1.000 [-1.000, -1.000] | 2 | negative |
| conservative | symmetric | 4 | 5 | -1.000 [-1.000, -1.000] | 2 | negative |
| conservative | symmetric | 4 | 30 | -2.000 [-3.000, -1.000] | 2 | negative |
| optimistic | inventory | 1 | 1 | -1.000 [-1.000, -1.000] | 5 | negative |
| optimistic | inventory | 1 | 5 | -1.375 [-2.500, -0.625] | 5 | negative |
| optimistic | inventory | 1 | 30 | -1.125 [-1.875, -0.375] | 5 | negative |
| optimistic | symmetric | 1 | 1 | -1.000 [-1.000, -1.000] | 5 | negative |
| optimistic | symmetric | 1 | 5 | -1.375 [-2.500, -0.625] | 5 | negative |
| optimistic | symmetric | 1 | 30 | -1.125 [-1.875, -0.375] | 5 | negative |
| optimistic | inventory | 2 | 1 | -1.000 [-1.000, -1.000] | 4 | negative |
| optimistic | inventory | 2 | 5 | -0.833 [-1.000, -0.500] | 4 | negative |
| optimistic | inventory | 2 | 30 | -0.833 [-1.500, 0.000] | 4 | inside the interval: no claim |
| optimistic | symmetric | 2 | 1 | -1.000 [-1.000, -1.000] | 3 | negative |
| optimistic | symmetric | 2 | 5 | -1.000 [-1.000, -1.000] | 3 | negative |
| optimistic | symmetric | 2 | 30 | -1.333 [-3.000, 0.000] | 3 | inside the interval: no claim |
| optimistic | inventory | 4 | 1 | -1.000 [-1.000, -1.000] | 3 | negative |
| optimistic | inventory | 4 | 5 | -0.750 [-1.000, -0.500] | 3 | negative |
| optimistic | inventory | 4 | 30 | -1.250 [-1.500, -1.000] | 3 | negative |
| optimistic | symmetric | 4 | 1 | -1.000 [-1.000, -1.000] | 2 | negative |
| optimistic | symmetric | 4 | 5 | -1.000 [-1.000, -1.000] | 2 | negative |
| optimistic | symmetric | 4 | 30 | -2.000 [-3.000, -1.000] | 2 | negative |

## Q3. Where the gap comes from: spread capture and inventory P&L

| fill rule | strategy | penalty (ticks) | replay spread capture | model spread capture | replay inventory P&L | model inventory P&L |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 0.417 [0.167, 0.667] | 34.886 [33.976, 35.804] | -1.333 [-3.167, -0.167] | 0.231 [-1.979, 2.368] |
| conservative | symmetric | 1 | 0.417 [0.167, 0.667] | 37.034 [36.009, 38.022] | -1.333 [-3.167, -0.167] | 3.392 [-2.456, 9.221] |
| conservative | inventory | 2 | 0.333 [0.083, 0.667] | 32.310 [31.415, 33.220] | -1.167 [-3.167, 0.000] | -0.442 [-1.979, 1.143] |
| conservative | symmetric | 2 | 0.250 [0.083, 0.417] | 35.717 [34.620, 36.836] | -0.167 [-0.500, 0.000] | 1.832 [-3.062, 6.616] |
| conservative | inventory | 4 | 0.250 [0.000, 0.583] | 27.169 [26.235, 28.127] | -1.167 [-3.167, 0.000] | -0.279 [-1.461, 0.908] |
| conservative | symmetric | 4 | 0.167 [0.000, 0.333] | 31.784 [30.561, 32.966] | -0.167 [-0.500, 0.000] | 1.149 [-2.730, 5.001] |
| optimistic | inventory | 1 | 0.417 [0.167, 0.667] | 35.146 [34.228, 36.050] | -1.333 [-3.167, -0.167] | 0.150 [-2.023, 2.260] |
| optimistic | symmetric | 1 | 0.417 [0.167, 0.667] | 37.308 [36.282, 38.305] | -1.333 [-3.167, -0.167] | 3.335 [-2.498, 9.096] |
| optimistic | inventory | 2 | 0.333 [0.083, 0.667] | 32.570 [31.623, 33.490] | -1.167 [-3.167, 0.000] | -0.368 [-1.892, 1.184] |
| optimistic | symmetric | 2 | 0.250 [0.083, 0.417] | 35.946 [34.871, 37.100] | -0.167 [-0.500, 0.000] | 1.582 [-3.372, 6.362] |
| optimistic | inventory | 4 | 0.250 [0.000, 0.583] | 27.401 [26.454, 28.358] | -1.167 [-3.167, 0.000] | -0.386 [-1.597, 0.803] |
| optimistic | symmetric | 4 | 0.167 [0.000, 0.333] | 32.116 [30.883, 33.335] | -0.167 [-0.500, 0.000] | 1.146 [-2.716, 4.996] |

## Q4. What queue position is worth: sticky minus always-requeue

| fill rule | strategy | penalty (ticks) | P&L difference | fills difference | verdict |
|---|---|---|---|---|---|
| conservative | inventory | 1 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 1 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 2 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 2 | -0.026 [-0.078, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | inventory | 4 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 4 | -0.026 [-0.078, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 1 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 1 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 2 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 2 | -0.026 [-0.078, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 4 | -0.072 [-0.163, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 4 | -0.026 [-0.078, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Q5. Tick size

In the calibration window the spread was one tick 99.0% of the time (mean 1.01 ticks), which puts this stock in the **large-tick** group. Compare Q4 across stocks in the two groups; one stock cannot answer Q5.

## Inventory strategy against symmetric

| fill rule | penalty (ticks) | P&L difference | |end inventory| difference (shares) | verdict |
|---|---|---|---|---|
| conservative | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 2 | -0.917 [-2.750, 0.000] | -16.667 [-50.000, 0.000] | inside the interval: no claim |
| conservative | 4 | -0.917 [-2.750, 0.000] | -16.667 [-50.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | -0.917 [-2.750, 0.000] | -16.667 [-50.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | -0.917 [-2.750, 0.000] | -16.667 [-50.000, 0.000] | inside the interval: no claim |

## Q6. Do the findings survive the choice of fill rule?

| finding | conservative | optimistic | verdict |
|---|---|---|---|
| markout 1s, inventory, 1 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, inventory, 1 ticks | -1.375 [-2.500, -0.625] | -1.375 [-2.500, -0.625] | holds under both rules |
| markout 30s, inventory, 1 ticks | -1.125 [-1.875, -0.375] | -1.125 [-1.875, -0.375] | holds under both rules |
| queue value (sticky - requeue P&L), inventory, 1 ticks | -0.072 [-0.163, 0.000] | -0.072 [-0.163, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 1 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, symmetric, 1 ticks | -1.375 [-2.500, -0.625] | -1.375 [-2.500, -0.625] | holds under both rules |
| markout 30s, symmetric, 1 ticks | -1.125 [-1.875, -0.375] | -1.125 [-1.875, -0.375] | holds under both rules |
| queue value (sticky - requeue P&L), symmetric, 1 ticks | -0.072 [-0.163, 0.000] | -0.072 [-0.163, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 1 ticks | -0.500 [-1.750, 0.250] | -0.500 [-1.750, 0.250] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, inventory, 2 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, inventory, 2 ticks | -0.833 [-1.000, -0.500] | -0.833 [-1.000, -0.500] | holds under both rules |
| markout 30s, inventory, 2 ticks | -0.833 [-1.500, 0.000] | -0.833 [-1.500, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 2 ticks | -0.072 [-0.163, 0.000] | -0.072 [-0.163, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 2 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, symmetric, 2 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 30s, symmetric, 2 ticks | -1.333 [-3.000, 0.000] | -1.333 [-3.000, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 2 ticks | -0.026 [-0.078, 0.000] | -0.026 [-0.078, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 2 ticks | -0.917 [-2.750, 0.000] | -0.917 [-2.750, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 2 ticks | -0.583 [-1.750, 0.000] | -0.583 [-1.750, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 2 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 2 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 2 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, inventory, 4 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, inventory, 4 ticks | -0.750 [-1.000, -0.500] | -0.750 [-1.000, -0.500] | holds under both rules |
| markout 30s, inventory, 4 ticks | -1.250 [-1.500, -1.000] | -1.250 [-1.500, -1.000] | holds under both rules |
| queue value (sticky - requeue P&L), inventory, 4 ticks | -0.072 [-0.163, 0.000] | -0.072 [-0.163, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 4 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 5s, symmetric, 4 ticks | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | holds under both rules |
| markout 30s, symmetric, 4 ticks | -2.000 [-3.000, -1.000] | -2.000 [-3.000, -1.000] | holds under both rules |
| queue value (sticky - requeue P&L), symmetric, 4 ticks | -0.026 [-0.078, 0.000] | -0.026 [-0.078, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 4 ticks | -0.917 [-2.750, 0.000] | -0.917 [-2.750, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |

## Q7. Does the order book predict the next price move?

Beyond the approach document's six questions. Each signal is positive when the book or the recent flow leans towards buyers. A line was fitted on the calibration window and scored on the test window, 11640 and 11640 one-second samples. The correlation is the mean over windows, with its interval; R² is measured against predicting no change.

![Signal correlation by horizon](signal_decay.svg)

| signal | horizon (s) | fitted slope (ticks per unit) | correlation, fit window | correlation, test windows | R², test | direction called | verdict |
|---|---|---|---|---|---|---|---|
| queue_imbalance | 1 | 0.1342 | 0.179 | 0.182 [0.162, 0.203] | 0.0274 | 82.0% of 478 moves | positive |
| queue_imbalance | 5 | 0.4152 | 0.251 | 0.264 [0.246, 0.281] | 0.0544 | 73.1% of 1987 moves | positive |
| queue_imbalance | 10 | 0.5367 | 0.226 | 0.258 [0.231, 0.289] | 0.0503 | 67.7% of 3375 moves | positive |
| queue_imbalance | 30 | 0.6859 | 0.162 | 0.205 [0.151, 0.261] | 0.0289 | 60.3% of 6089 moves | positive |
| queue_imbalance | 60 | 0.5258 | 0.087 | 0.154 [0.099, 0.210] | 0.0172 | 58.3% of 7288 moves | positive |
| ofi | 1 | 0.0000 | 0.021 | 0.060 [0.041, 0.077] | 0.0027 | 72.1% of 476 moves | positive |
| ofi | 5 | 0.0002 | 0.056 | 0.077 [0.050, 0.107] | 0.0080 | 66.2% of 1978 moves | positive |
| ofi | 10 | 0.0002 | 0.040 | 0.072 [0.037, 0.112] | 0.0067 | 63.0% of 3354 moves | positive |
| ofi | 30 | 0.0004 | 0.052 | 0.021 [-0.010, 0.042] | 0.0026 | 56.2% of 6035 moves | inside the interval: no claim |
| ofi | 60 | 0.0006 | 0.052 | -0.012 [-0.054, 0.023] | -0.0055 | 54.1% of 7205 moves | inside the interval: no claim |
| trade_imbalance | 1 | 0.0000 | 0.006 | 0.036 [0.020, 0.052] | 0.0006 | 61.3% of 439 moves | positive |
| trade_imbalance | 5 | 0.0003 | 0.019 | 0.037 [0.011, 0.063] | 0.0023 | 59.2% of 1776 moves | positive |
| trade_imbalance | 10 | -0.0001 | -0.004 | 0.025 [-0.015, 0.060] | 0.0010 | 41.8% of 2984 moves | inside the interval: no claim |
| trade_imbalance | 30 | 0.0005 | 0.011 | 0.006 [-0.036, 0.048] | 0.0042 | 51.3% of 5246 moves | inside the interval: no claim |
| trade_imbalance | 60 | 0.0011 | 0.019 | -0.004 [-0.034, 0.026] | 0.0046 | 51.1% of 6183 moves | inside the interval: no claim |

## Q8. Does leaning quotes on the signal reduce adverse selection?

The signal strategy is the inventory strategy with both quotes shifted by the fitted move: `queue_imbalance` at the 5 s horizon, 0.004152 dollars per unit. It was chosen for the strongest correlation in the calibration window. Differences are signal minus inventory, paired by window; a positive markout difference means less adverse selection.

| fill rule | penalty (ticks) | P&L difference | fills difference | requotes where the skew moved a quote by a tick or more | verdict |
|---|---|---|---|---|---|
| conservative | 1 | -0.500 [-1.750, 0.250] | 0.000 [-0.500, 0.500] | 3786 | inside the interval: no claim |
| conservative | 2 | -0.583 [-1.750, 0.000] | 0.167 [0.000, 0.500] | 2153 | inside the interval: no claim |
| conservative | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 2655 | inside the interval: no claim |
| optimistic | 1 | -0.500 [-1.750, 0.250] | 0.000 [-0.500, 0.500] | 3815 | inside the interval: no claim |
| optimistic | 2 | -0.583 [-1.750, 0.000] | 0.167 [0.000, 0.500] | 2140 | inside the interval: no claim |
| optimistic | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 2657 | inside the interval: no claim |

| fill rule | penalty (ticks) | horizon (s) | markout, signal | markout, inventory | difference | verdict |
|---|---|---|---|---|---|---|
| conservative | 1 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 1 | 5 | -0.833 [-1.000, -0.500] | -0.833 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 1 | 30 | -0.833 [-1.500, 0.000] | -0.833 [-1.500, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 2 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 2 | 5 | -0.833 [-1.000, -0.500] | -0.833 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 2 | 30 | -0.833 [-1.500, 0.000] | -0.833 [-1.500, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 4 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 4 | 5 | -0.750 [-1.000, -0.500] | -0.750 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 4 | 30 | -1.250 [-1.500, -1.000] | -1.250 [-1.500, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 5 | -0.833 [-1.000, -0.500] | -0.833 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 30 | -0.833 [-1.500, 0.000] | -0.833 [-1.500, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 5 | -0.833 [-1.000, -0.500] | -0.833 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 30 | -0.833 [-1.500, 0.000] | -0.833 [-1.500, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 1 | -1.000 [-1.000, -1.000] | -1.000 [-1.000, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 5 | -0.750 [-1.000, -0.500] | -0.750 [-1.000, -0.500] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 30 | -1.250 [-1.500, -1.000] | -1.250 [-1.500, -1.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Diagnostics

| run | fills | orders posted | requotes that found our order overtaken |
|---|---|---|---|
| inventory/1t/sticky/conservative | 5 | 943 | 0 |
| inventory/1t/requeue/conservative | 5 | 19684 | 0 |
| symmetric/1t/sticky/conservative | 5 | 943 | 0 |
| symmetric/1t/requeue/conservative | 5 | 19684 | 0 |
| inventory/2t/sticky/conservative | 4 | 942 | 0 |
| inventory/2t/requeue/conservative | 4 | 19682 | 0 |
| symmetric/2t/sticky/conservative | 3 | 941 | 0 |
| symmetric/2t/requeue/conservative | 3 | 19680 | 0 |
| inventory/4t/sticky/conservative | 3 | 951 | 0 |
| inventory/4t/requeue/conservative | 3 | 19680 | 0 |
| symmetric/4t/sticky/conservative | 2 | 951 | 0 |
| symmetric/4t/requeue/conservative | 2 | 19678 | 0 |
| inventory/1t/sticky/optimistic | 5 | 940 | 0 |
| inventory/1t/requeue/optimistic | 5 | 19684 | 0 |
| symmetric/1t/sticky/optimistic | 5 | 940 | 0 |
| symmetric/1t/requeue/optimistic | 5 | 19684 | 0 |
| inventory/2t/sticky/optimistic | 4 | 942 | 0 |
| inventory/2t/requeue/optimistic | 4 | 19682 | 0 |
| symmetric/2t/sticky/optimistic | 3 | 941 | 0 |
| symmetric/2t/requeue/optimistic | 3 | 19680 | 0 |
| inventory/4t/sticky/optimistic | 3 | 951 | 0 |
| inventory/4t/requeue/optimistic | 3 | 19680 | 0 |
| symmetric/4t/sticky/optimistic | 2 | 951 | 0 |
| symmetric/4t/requeue/optimistic | 2 | 19678 | 0 |
| signal/1t/sticky/conservative | 5 | 1535 | 0 |
| signal/2t/sticky/conservative | 5 | 1367 | 0 |
| signal/4t/sticky/conservative | 3 | 1357 | 0 |
| signal/1t/sticky/optimistic | 5 | 1552 | 0 |
| signal/2t/sticky/optimistic | 5 | 1361 | 0 |
| signal/4t/sticky/optimistic | 3 | 1346 | 0 |

An overtaken order is one the real book moved through between requotes. In reality it would have traded; the replay only fills it at the next real execution (see README, limitations).
