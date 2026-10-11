# INTC 2012-06-21: Avellaneda-Stoikov replay study

- Calibrated on 09:31:00 to 12:45:00; traded on 12:45:00 to 15:59:00.
- Windows of 1800 s, each an independent session. Requote every 1 s and after each fill. One lot = 100 shares per side.
- Figures are means over windows with a 95% bootstrap interval in brackets. A difference whose interval contains zero is not claimed.
- P&L is in dollars per window, before fees and rebates. Markouts are in ticks per share.

## Headline

Middle settings only; every setting is in the tables below.

- **Adverse selection.** 5 s after a fill, the mid had moved by conservative -0.750 ticks [-1.500, 0.000]; optimistic -0.750 ticks [-1.500, 0.000] per share (negative is against us). Across fill rules: not established under both rules: not a conclusion.
- **Model against replay.** conservative: replay -0.496 [-3.913, 2.000] against the model's 25.241 [23.595, 26.832] dollars per window (replay below model); optimistic: replay -0.496 [-3.913, 2.000] against the model's 25.284 [23.652, 26.856] dollars per window (replay below model).
- **Prediction.** `queue_imbalance` had an out-of-sample correlation of 0.234 [0.185, 0.296] with the mid change over the next 5 s (positive). Leaning quotes on it changed the 5 s markout by conservative 0.250 ticks [0.000, 0.750]; optimistic 0.250 ticks [0.000, 0.750]. Across fill rules: not established under both rules: not a conclusion.

## Calibration

sigma = 0.00277269 dollars per sqrt(second), taken at the 60 s horizon.

![Variance ratio](variance_ratio.svg)

| horizon (s) | sigma ($/sqrt s) | increments | variance ratio vs longest |
|---|---|---|---|
| 1 | 0.002601 | 11639 | 0.855 |
| 2 | 0.002539 | 5819 | 0.815 |
| 5 | 0.002516 | 2327 | 0.800 |
| 10 | 0.002461 | 1163 | 0.766 |
| 30 | 0.002584 | 387 | 0.844 |
| 60 | 0.002773 | 193 | 0.972 |
| 120 | 0.002351 | 96 | 0.699 |
| 300 | 0.002813 | 38 | 1.000 |

### Fill intensity, conservative rule

A = 0.020795 per second, k = 89.934 per dollar, from 4656 probes, 768 filled, 252153 s of exposure.

![Fill intensity, conservative](intensity_conservative.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 422 | 29537 | 0.0051 | 0.01429 | 0.01322 |
| 1 | 773 | 181 | 40585 | 0.0151 | 0.00446 | 0.00537 |
| 2 | 760 | 84 | 43591 | 0.0250 | 0.00193 | 0.00219 |
| 3 | 796 | 50 | 46492 | 0.0351 | 0.00108 | 0.00089 |
| 4 | 740 | 25 | 43604 | 0.0451 | 0.00057 | 0.00036 |
| 5 | 811 | 6 | 48345 | 0.0550 | 0.00012 | 0.00015 |

### Fill intensity, optimistic rule

A = 0.020928 per second, k = 90.044 per dollar, from 4656 probes, 771 filled, 252066 s of exposure.

![Fill intensity, optimistic](intensity_optimistic.svg)

| ticks behind touch | probes | fills | exposure (s) | mean delta ($) | empirical rate (/s) | fitted rate (/s) |
|---|---|---|---|---|---|---|
| 0 | 776 | 424 | 29484 | 0.0051 | 0.01438 | 0.01330 |
| 1 | 773 | 181 | 40585 | 0.0151 | 0.00446 | 0.00539 |
| 2 | 760 | 85 | 43557 | 0.0250 | 0.00195 | 0.00220 |
| 3 | 796 | 50 | 46492 | 0.0351 | 0.00108 | 0.00089 |
| 4 | 740 | 25 | 43604 | 0.0451 | 0.00057 | 0.00036 |
| 5 | 811 | 6 | 48345 | 0.0550 | 0.00012 | 0.00015 |

## Q1. Does the calibrated model predict replay P&L?

| fill rule | strategy | penalty (ticks) | replay P&L | model P&L | replay fills | model fills | verdict |
|---|---|---|---|---|---|---|---|
| conservative | inventory | 1 | -1.079 [-6.917, 3.921] | 28.309 [26.257, 30.270] | 1.167 [0.667, 1.667] | 24.535 [23.895, 25.155] | replay below model |
| conservative | symmetric | 1 | -1.079 [-6.917, 3.921] | 33.350 [27.811, 38.769] | 1.167 [0.667, 1.667] | 22.305 [21.690, 22.905] | replay below model |
| conservative | inventory | 2 | -0.496 [-3.913, 2.000] | 25.241 [23.595, 26.832] | 0.667 [0.333, 1.000] | 22.405 [21.735, 23.070] | replay below model |
| conservative | symmetric | 2 | -0.662 [-6.663, 4.250] | 30.730 [26.387, 35.025] | 1.000 [0.333, 1.667] | 18.630 [18.030, 19.220] | replay below model |
| conservative | inventory | 4 | 1.000 [0.000, 2.500] | 19.150 [17.928, 20.421] | 0.333 [0.000, 0.667] | 17.445 [16.790, 18.115] | replay below model |
| conservative | symmetric | 4 | 1.000 [0.000, 2.500] | 25.041 [21.441, 28.545] | 0.333 [0.000, 0.667] | 13.240 [12.740, 13.725] | replay below model |
| optimistic | inventory | 1 | -1.079 [-6.917, 3.921] | 28.392 [26.316, 30.336] | 1.167 [0.667, 1.667] | 24.795 [24.155, 25.420] | replay below model |
| optimistic | symmetric | 1 | -1.079 [-6.917, 3.921] | 33.496 [27.973, 38.904] | 1.167 [0.667, 1.667] | 22.455 [21.835, 23.050] | replay below model |
| optimistic | inventory | 2 | -0.496 [-3.913, 2.000] | 25.284 [23.652, 26.856] | 0.667 [0.333, 1.000] | 22.525 [21.855, 23.185] | replay below model |
| optimistic | symmetric | 2 | -0.662 [-6.663, 4.250] | 30.658 [26.313, 34.877] | 1.000 [0.333, 1.667] | 18.710 [18.115, 19.290] | replay below model |
| optimistic | inventory | 4 | 1.000 [0.000, 2.500] | 19.369 [18.154, 20.633] | 0.333 [0.000, 0.667] | 17.545 [16.890, 18.210] | replay below model |
| optimistic | symmetric | 4 | 1.000 [0.000, 2.500] | 25.150 [21.444, 28.714] | 0.333 [0.000, 0.667] | 13.330 [12.825, 13.815] | replay below model |

### Replay profit three ways

Every fill is booked at its own price. Shares still held when a window closes have no trade price, so the profit depends on how they are valued. Realised counts completed buy-and-sell pairs only (first in, first out). The middle column is the replay P&L used everywhere else in this report. The last column trades the leftover out against the real book at the close, level by level, which is what closing would have cost. Sticky quotes.

| run | realised | leftover valued at the mid | leftover closed at real prices | shares left at the close | shares traded per window |
|---|---|---|---|---|---|
| inventory/1t/sticky/conservative | 0.000 [0.000, 0.000] | -1.079 [-6.917, 3.921] | -1.597 [-7.667, 3.237] | 104 | 104 |
| symmetric/1t/sticky/conservative | 0.000 [0.000, 0.000] | -1.079 [-6.917, 3.921] | -1.597 [-7.667, 3.237] | 104 | 104 |
| inventory/2t/sticky/conservative | 0.000 [0.000, 0.000] | -0.496 [-3.913, 2.000] | -0.763 [-4.263, 1.667] | 54 | 54 |
| symmetric/2t/sticky/conservative | 0.000 [0.000, 0.000] | -0.662 [-6.663, 4.250] | -1.097 [-7.263, 3.667] | 87 | 87 |
| inventory/4t/sticky/conservative | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |
| symmetric/4t/sticky/conservative | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |
| inventory/1t/sticky/optimistic | 0.000 [0.000, 0.000] | -1.079 [-6.917, 3.921] | -1.597 [-7.667, 3.237] | 104 | 104 |
| symmetric/1t/sticky/optimistic | 0.000 [0.000, 0.000] | -1.079 [-6.917, 3.921] | -1.597 [-7.667, 3.237] | 104 | 104 |
| inventory/2t/sticky/optimistic | 0.000 [0.000, 0.000] | -0.496 [-3.913, 2.000] | -0.763 [-4.263, 1.667] | 54 | 54 |
| symmetric/2t/sticky/optimistic | 0.000 [0.000, 0.000] | -0.662 [-6.663, 4.250] | -1.097 [-7.263, 3.667] | 87 | 87 |
| inventory/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |
| symmetric/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |
| signal/1t/sticky/conservative | 0.333 [0.000, 1.000] | -0.579 [-3.996, 1.917] | -0.930 [-4.360, 1.570] | 70 | 104 |
| signal/2t/sticky/conservative | 0.000 [0.000, 0.000] | -0.329 [-3.913, 2.500] | -0.597 [-4.263, 2.167] | 54 | 54 |
| signal/4t/sticky/conservative | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |
| signal/1t/sticky/optimistic | 0.333 [0.000, 1.000] | -0.579 [-3.996, 1.917] | -0.930 [-4.360, 1.570] | 70 | 104 |
| signal/2t/sticky/optimistic | 0.000 [0.000, 0.000] | -0.329 [-3.913, 2.500] | -0.597 [-4.263, 2.167] | 54 | 54 |
| signal/4t/sticky/optimistic | 0.000 [0.000, 0.000] | 1.000 [0.000, 2.500] | 0.833 [0.000, 2.167] | 33 | 33 |

## Q2. Adverse selection: markouts on replay fills

Negative means the mid moved against us after the fill. In the model world the expected markout is zero.

![Markouts](markouts.svg)

| fill rule | strategy | penalty (ticks) | horizon (s) | markout (ticks) | fills | verdict |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 1 | -0.400 [-0.700, -0.100] | 7 | negative |
| conservative | inventory | 1 | 5 | -0.500 [-1.100, 0.000] | 7 | inside the interval: no claim |
| conservative | inventory | 1 | 30 | -1.200 [-2.600, 0.000] | 7 | inside the interval: no claim |
| conservative | symmetric | 1 | 1 | -0.400 [-0.700, -0.100] | 7 | negative |
| conservative | symmetric | 1 | 5 | -0.500 [-1.100, 0.000] | 7 | inside the interval: no claim |
| conservative | symmetric | 1 | 30 | -1.200 [-2.600, 0.000] | 7 | inside the interval: no claim |
| conservative | inventory | 2 | 1 | -0.500 [-1.000, 0.000] | 4 | inside the interval: no claim |
| conservative | inventory | 2 | 5 | -0.750 [-1.500, 0.000] | 4 | inside the interval: no claim |
| conservative | inventory | 2 | 30 | -2.000 [-4.000, 0.000] | 4 | inside the interval: no claim |
| conservative | symmetric | 2 | 1 | -0.250 [-0.500, 0.000] | 6 | inside the interval: no claim |
| conservative | symmetric | 2 | 5 | -0.625 [-1.250, 0.000] | 6 | inside the interval: no claim |
| conservative | symmetric | 2 | 30 | -1.500 [-3.000, 0.000] | 6 | inside the interval: no claim |
| conservative | inventory | 4 | 1 | 0.000 [0.000, 0.000] | 2 | inside the interval: no claim |
| conservative | inventory | 4 | 5 | -0.500 [-1.000, 0.000] | 2 | inside the interval: no claim |
| conservative | inventory | 4 | 30 | -1.500 [-3.000, 0.000] | 2 | inside the interval: no claim |
| conservative | symmetric | 4 | 1 | 0.000 [0.000, 0.000] | 2 | inside the interval: no claim |
| conservative | symmetric | 4 | 5 | -0.500 [-1.000, 0.000] | 2 | inside the interval: no claim |
| conservative | symmetric | 4 | 30 | -1.500 [-3.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | inventory | 1 | 1 | -0.400 [-0.700, -0.100] | 7 | negative |
| optimistic | inventory | 1 | 5 | -0.500 [-1.100, 0.000] | 7 | inside the interval: no claim |
| optimistic | inventory | 1 | 30 | -1.200 [-2.600, 0.000] | 7 | inside the interval: no claim |
| optimistic | symmetric | 1 | 1 | -0.400 [-0.700, -0.100] | 7 | negative |
| optimistic | symmetric | 1 | 5 | -0.500 [-1.100, 0.000] | 7 | inside the interval: no claim |
| optimistic | symmetric | 1 | 30 | -1.200 [-2.600, 0.000] | 7 | inside the interval: no claim |
| optimistic | inventory | 2 | 1 | -0.500 [-1.000, 0.000] | 4 | inside the interval: no claim |
| optimistic | inventory | 2 | 5 | -0.750 [-1.500, 0.000] | 4 | inside the interval: no claim |
| optimistic | inventory | 2 | 30 | -2.000 [-4.000, 0.000] | 4 | inside the interval: no claim |
| optimistic | symmetric | 2 | 1 | -0.250 [-0.500, 0.000] | 6 | inside the interval: no claim |
| optimistic | symmetric | 2 | 5 | -0.625 [-1.250, 0.000] | 6 | inside the interval: no claim |
| optimistic | symmetric | 2 | 30 | -1.500 [-3.000, 0.000] | 6 | inside the interval: no claim |
| optimistic | inventory | 4 | 1 | 0.000 [0.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | inventory | 4 | 5 | -0.500 [-1.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | inventory | 4 | 30 | -1.500 [-3.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | symmetric | 4 | 1 | 0.000 [0.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | symmetric | 4 | 5 | -0.500 [-1.000, 0.000] | 2 | inside the interval: no claim |
| optimistic | symmetric | 4 | 30 | -1.500 [-3.000, 0.000] | 2 | inside the interval: no claim |

## Q3. Where the gap comes from: spread capture and inventory P&L

| fill rule | strategy | penalty (ticks) | replay spread capture | model spread capture | replay inventory P&L | model inventory P&L |
|---|---|---|---|---|---|---|
| conservative | inventory | 1 | 0.517 [0.202, 0.833] | 27.895 [27.171, 28.599] | -1.597 [-7.667, 3.237] | 0.414 [-1.529, 2.231] |
| conservative | symmetric | 1 | 0.517 [0.202, 0.833] | 29.947 [29.104, 30.785] | -1.597 [-7.667, 3.237] | 3.403 [-2.045, 8.900] |
| conservative | inventory | 2 | 0.268 [0.070, 0.434] | 25.521 [24.768, 26.267] | -0.763 [-4.263, 1.667] | -0.281 [-1.652, 1.062] |
| conservative | symmetric | 2 | 0.434 [0.070, 0.768] | 28.665 [27.710, 29.622] | -1.097 [-7.263, 3.667] | 2.065 [-2.216, 6.336] |
| conservative | inventory | 4 | 0.167 [0.000, 0.333] | 19.933 [19.205, 20.683] | 0.833 [0.000, 2.167] | -0.783 [-1.793, 0.184] |
| conservative | symmetric | 4 | 0.167 [0.000, 0.333] | 24.163 [23.155, 25.119] | 0.833 [0.000, 2.167] | 0.878 [-2.557, 4.380] |
| optimistic | inventory | 1 | 0.517 [0.202, 0.833] | 28.151 [27.433, 28.855] | -1.597 [-7.667, 3.237] | 0.241 [-1.670, 2.043] |
| optimistic | symmetric | 1 | 0.517 [0.202, 0.833] | 30.117 [29.276, 30.937] | -1.597 [-7.667, 3.237] | 3.379 [-2.104, 8.936] |
| optimistic | inventory | 2 | 0.268 [0.070, 0.434] | 25.624 [24.867, 26.360] | -0.763 [-4.263, 1.667] | -0.341 [-1.713, 0.998] |
| optimistic | symmetric | 2 | 0.434 [0.070, 0.768] | 28.758 [27.807, 29.703] | -1.097 [-7.263, 3.667] | 1.901 [-2.374, 6.079] |
| optimistic | inventory | 4 | 0.167 [0.000, 0.333] | 20.020 [19.296, 20.770] | 0.833 [0.000, 2.167] | -0.651 [-1.646, 0.327] |
| optimistic | symmetric | 4 | 0.167 [0.000, 0.333] | 24.312 [23.310, 25.257] | 0.833 [0.000, 2.167] | 0.838 [-2.643, 4.226] |

## Q4. What queue position is worth: sticky minus always-requeue

| fill rule | strategy | penalty (ticks) | P&L difference | fills difference | verdict |
|---|---|---|---|---|---|
| conservative | inventory | 1 | -0.029 [-0.350, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | symmetric | 1 | -0.029 [-0.350, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | inventory | 2 | 0.088 [0.000, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | symmetric | 2 | 0.088 [0.000, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| conservative | inventory | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | symmetric | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | inventory | 1 | -0.029 [-0.350, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| optimistic | symmetric | 1 | -0.029 [-0.350, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| optimistic | inventory | 2 | 0.088 [0.000, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| optimistic | symmetric | 2 | 0.088 [0.000, 0.263] | 0.167 [0.000, 0.500] | inside the interval: no claim |
| optimistic | inventory | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | symmetric | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Q5. Tick size

In the calibration window the spread was one tick 98.8% of the time (mean 1.01 ticks), which puts this stock in the **large-tick** group. Compare Q4 across stocks in the two groups; one stock cannot answer Q5.

## Inventory strategy against symmetric

| fill rule | penalty (ticks) | P&L difference | |end inventory| difference (shares) | verdict |
|---|---|---|---|---|
| conservative | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 2 | 0.167 [-2.250, 2.750] | -33.333 [-66.667, 0.000] | inside the interval: no claim |
| conservative | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 2 | 0.167 [-2.250, 2.750] | -33.333 [-66.667, 0.000] | inside the interval: no claim |
| optimistic | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Q6. Do the findings survive the choice of fill rule?

| finding | conservative | optimistic | verdict |
|---|---|---|---|
| markout 1s, inventory, 1 ticks | -0.400 [-0.700, -0.100] | -0.400 [-0.700, -0.100] | holds under both rules |
| markout 5s, inventory, 1 ticks | -0.500 [-1.100, 0.000] | -0.500 [-1.100, 0.000] | not established under both rules: not a conclusion |
| markout 30s, inventory, 1 ticks | -1.200 [-2.600, 0.000] | -1.200 [-2.600, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 1 ticks | -0.029 [-0.350, 0.263] | -0.029 [-0.350, 0.263] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 1 ticks | -0.400 [-0.700, -0.100] | -0.400 [-0.700, -0.100] | holds under both rules |
| markout 5s, symmetric, 1 ticks | -0.500 [-1.100, 0.000] | -0.500 [-1.100, 0.000] | not established under both rules: not a conclusion |
| markout 30s, symmetric, 1 ticks | -1.200 [-2.600, 0.000] | -1.200 [-2.600, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 1 ticks | -0.029 [-0.350, 0.263] | -0.029 [-0.350, 0.263] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 1 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 1 ticks | 0.500 [-1.917, 2.833] | 0.500 [-1.917, 2.833] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 1 ticks | -0.167 [-0.400, 0.067] | -0.167 [-0.400, 0.067] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 1 ticks | -0.167 [-0.367, 0.000] | -0.167 [-0.367, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 1 ticks | -0.533 [-1.033, -0.100] | -0.533 [-1.033, -0.100] | holds under both rules |
| markout 1s, inventory, 2 ticks | -0.500 [-1.000, 0.000] | -0.500 [-1.000, 0.000] | not established under both rules: not a conclusion |
| markout 5s, inventory, 2 ticks | -0.750 [-1.500, 0.000] | -0.750 [-1.500, 0.000] | not established under both rules: not a conclusion |
| markout 30s, inventory, 2 ticks | -2.000 [-4.000, 0.000] | -2.000 [-4.000, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 2 ticks | 0.088 [0.000, 0.263] | 0.088 [0.000, 0.263] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 2 ticks | -0.250 [-0.500, 0.000] | -0.250 [-0.500, 0.000] | not established under both rules: not a conclusion |
| markout 5s, symmetric, 2 ticks | -0.625 [-1.250, 0.000] | -0.625 [-1.250, 0.000] | not established under both rules: not a conclusion |
| markout 30s, symmetric, 2 ticks | -1.500 [-3.000, 0.000] | -1.500 [-3.000, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 2 ticks | 0.088 [0.000, 0.263] | 0.088 [0.000, 0.263] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 2 ticks | 0.167 [-2.250, 2.750] | 0.167 [-2.250, 2.750] | not established under both rules: not a conclusion |
| signal - inventory P&L, 2 ticks | 0.167 [0.000, 0.500] | 0.167 [0.000, 0.500] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 2 ticks | 0.250 [0.000, 0.750] | 0.250 [0.000, 0.750] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 2 ticks | 0.250 [0.000, 0.750] | 0.250 [0.000, 0.750] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 2 ticks | 0.250 [0.000, 0.750] | 0.250 [0.000, 0.750] | not established under both rules: not a conclusion |
| markout 1s, inventory, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 5s, inventory, 4 ticks | -0.500 [-1.000, 0.000] | -0.500 [-1.000, 0.000] | not established under both rules: not a conclusion |
| markout 30s, inventory, 4 ticks | -1.500 [-3.000, 0.000] | -1.500 [-3.000, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), inventory, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 1s, symmetric, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| markout 5s, symmetric, 4 ticks | -0.500 [-1.000, 0.000] | -0.500 [-1.000, 0.000] | not established under both rules: not a conclusion |
| markout 30s, symmetric, 4 ticks | -1.500 [-3.000, 0.000] | -1.500 [-3.000, 0.000] | not established under both rules: not a conclusion |
| queue value (sticky - requeue P&L), symmetric, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| inventory - symmetric P&L, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory P&L, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 1s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 5s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |
| signal - inventory markout 30s, 4 ticks | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | not established under both rules: not a conclusion |

## Q7. Does the order book predict the next price move?

Beyond the approach document's six questions. Each signal is positive when the book or the recent flow leans towards buyers. A line was fitted on the calibration window and scored on the test window, 11640 and 11640 one-second samples. The correlation is the mean over windows, with its interval; R² is measured against predicting no change.

![Signal correlation by horizon](signal_decay.svg)

| signal | horizon (s) | fitted slope (ticks per unit) | correlation, fit window | correlation, test windows | R², test | direction called | verdict |
|---|---|---|---|---|---|---|---|
| queue_imbalance | 1 | 0.1156 | 0.167 | 0.161 [0.136, 0.197] | 0.0169 | 80.8% of 307 moves | positive |
| queue_imbalance | 5 | 0.3501 | 0.234 | 0.234 [0.185, 0.296] | 0.0431 | 76.8% of 1264 moves | positive |
| queue_imbalance | 10 | 0.4802 | 0.230 | 0.250 [0.180, 0.325] | 0.0544 | 72.8% of 2240 moves | positive |
| queue_imbalance | 30 | 0.6859 | 0.186 | 0.208 [0.112, 0.295] | 0.0396 | 65.6% of 4800 moves | positive |
| queue_imbalance | 60 | 0.6609 | 0.125 | 0.132 [0.020, 0.237] | 0.0151 | 60.6% of 6735 moves | positive |
| ofi | 1 | 0.0001 | 0.040 | 0.060 [0.037, 0.082] | 0.0039 | 68.4% of 307 moves | positive |
| ofi | 5 | 0.0001 | 0.039 | 0.064 [0.044, 0.086] | 0.0047 | 66.6% of 1263 moves | positive |
| ofi | 10 | 0.0002 | 0.043 | 0.081 [0.051, 0.108] | 0.0048 | 65.1% of 2240 moves | positive |
| ofi | 30 | 0.0004 | 0.047 | 0.109 [0.095, 0.125] | 0.0083 | 58.6% of 4792 moves | positive |
| ofi | 60 | 0.0004 | 0.037 | 0.072 [0.049, 0.101] | 0.0012 | 55.7% of 6713 moves | positive |
| trade_imbalance | 1 | 0.0002 | 0.030 | 0.070 [0.045, 0.099] | 0.0057 | 64.7% of 289 moves | positive |
| trade_imbalance | 5 | 0.0008 | 0.050 | 0.072 [0.044, 0.100] | 0.0055 | 62.0% of 1183 moves | positive |
| trade_imbalance | 10 | 0.0012 | 0.052 | 0.085 [0.048, 0.120] | 0.0037 | 61.2% of 2083 moves | positive |
| trade_imbalance | 30 | 0.0018 | 0.044 | 0.112 [0.081, 0.143] | 0.0083 | 58.4% of 4383 moves | positive |
| trade_imbalance | 60 | 0.0018 | 0.030 | 0.072 [0.054, 0.095] | 0.0004 | 56.0% of 6196 moves | positive |

## Q8. Does leaning quotes on the signal reduce adverse selection?

The signal strategy is the inventory strategy with both quotes shifted by the fitted move: `queue_imbalance` at the 5 s horizon, 0.003501 dollars per unit. It was chosen for the strongest correlation in the calibration window. Differences are signal minus inventory, paired by window; a positive markout difference means less adverse selection.

| fill rule | penalty (ticks) | P&L difference | fills difference | requotes where the skew moved a quote by a tick or more | verdict |
|---|---|---|---|---|---|
| conservative | 1 | 0.500 [-1.917, 2.833] | 0.000 [-0.667, 0.833] | 3636 | inside the interval: no claim |
| conservative | 2 | 0.167 [0.000, 0.500] | 0.000 [0.000, 0.000] | 2117 | inside the interval: no claim |
| conservative | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 2152 | inside the interval: no claim |
| optimistic | 1 | 0.500 [-1.917, 2.833] | 0.000 [-0.667, 0.833] | 3627 | inside the interval: no claim |
| optimistic | 2 | 0.167 [0.000, 0.500] | 0.000 [0.000, 0.000] | 2114 | inside the interval: no claim |
| optimistic | 4 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 2149 | inside the interval: no claim |

| fill rule | penalty (ticks) | horizon (s) | markout, signal | markout, inventory | difference | verdict |
|---|---|---|---|---|---|---|
| conservative | 1 | 1 | -0.567 [-0.967, -0.167] | -0.400 [-0.700, -0.100] | -0.167 [-0.400, 0.067] | inside the interval: no claim |
| conservative | 1 | 5 | -0.667 [-1.400, -0.067] | -0.500 [-1.100, 0.000] | -0.167 [-0.367, 0.000] | inside the interval: no claim |
| conservative | 1 | 30 | -1.733 [-3.333, -0.133] | -1.200 [-2.600, 0.000] | -0.533 [-1.033, -0.100] | negative |
| conservative | 2 | 1 | -0.250 [-0.750, 0.000] | -0.500 [-1.000, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| conservative | 2 | 5 | -0.500 [-1.000, 0.000] | -0.750 [-1.500, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| conservative | 2 | 30 | -1.750 [-3.750, 0.000] | -2.000 [-4.000, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| conservative | 4 | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 4 | 5 | -0.500 [-1.000, 0.000] | -0.500 [-1.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| conservative | 4 | 30 | -1.500 [-3.000, 0.000] | -1.500 [-3.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 1 | 1 | -0.567 [-0.967, -0.167] | -0.400 [-0.700, -0.100] | -0.167 [-0.400, 0.067] | inside the interval: no claim |
| optimistic | 1 | 5 | -0.667 [-1.400, -0.067] | -0.500 [-1.100, 0.000] | -0.167 [-0.367, 0.000] | inside the interval: no claim |
| optimistic | 1 | 30 | -1.733 [-3.333, -0.133] | -1.200 [-2.600, 0.000] | -0.533 [-1.033, -0.100] | negative |
| optimistic | 2 | 1 | -0.250 [-0.750, 0.000] | -0.500 [-1.000, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| optimistic | 2 | 5 | -0.500 [-1.000, 0.000] | -0.750 [-1.500, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| optimistic | 2 | 30 | -1.750 [-3.750, 0.000] | -2.000 [-4.000, 0.000] | 0.250 [0.000, 0.750] | inside the interval: no claim |
| optimistic | 4 | 1 | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 5 | -0.500 [-1.000, 0.000] | -0.500 [-1.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |
| optimistic | 4 | 30 | -1.500 [-3.000, 0.000] | -1.500 [-3.000, 0.000] | 0.000 [0.000, 0.000] | inside the interval: no claim |

## Diagnostics

| run | fills | orders posted | requotes that found our order overtaken |
|---|---|---|---|
| inventory/1t/sticky/conservative | 7 | 612 | 0 |
| inventory/1t/requeue/conservative | 6 | 19916 | 0 |
| symmetric/1t/sticky/conservative | 7 | 611 | 0 |
| symmetric/1t/requeue/conservative | 6 | 19916 | 0 |
| inventory/2t/sticky/conservative | 4 | 611 | 0 |
| inventory/2t/requeue/conservative | 3 | 19910 | 0 |
| symmetric/2t/sticky/conservative | 6 | 609 | 0 |
| symmetric/2t/requeue/conservative | 5 | 19914 | 0 |
| inventory/4t/sticky/conservative | 2 | 622 | 0 |
| inventory/4t/requeue/conservative | 2 | 19908 | 0 |
| symmetric/4t/sticky/conservative | 2 | 621 | 0 |
| symmetric/4t/requeue/conservative | 2 | 19908 | 0 |
| inventory/1t/sticky/optimistic | 7 | 613 | 0 |
| inventory/1t/requeue/optimistic | 6 | 19916 | 0 |
| symmetric/1t/sticky/optimistic | 7 | 611 | 0 |
| symmetric/1t/requeue/optimistic | 6 | 19916 | 0 |
| inventory/2t/sticky/optimistic | 4 | 611 | 0 |
| inventory/2t/requeue/optimistic | 3 | 19910 | 0 |
| symmetric/2t/sticky/optimistic | 6 | 609 | 0 |
| symmetric/2t/requeue/optimistic | 5 | 19914 | 0 |
| inventory/4t/sticky/optimistic | 2 | 622 | 0 |
| inventory/4t/requeue/optimistic | 2 | 19908 | 0 |
| symmetric/4t/sticky/optimistic | 2 | 621 | 0 |
| symmetric/4t/requeue/optimistic | 2 | 19908 | 0 |
| signal/1t/sticky/conservative | 7 | 1007 | 0 |
| signal/2t/sticky/conservative | 4 | 845 | 0 |
| signal/4t/sticky/conservative | 2 | 865 | 0 |
| signal/1t/sticky/optimistic | 7 | 1015 | 0 |
| signal/2t/sticky/optimistic | 4 | 846 | 0 |
| signal/4t/sticky/optimistic | 2 | 859 | 0 |

An overtaken order is one the real book moved through between requotes. In reality it would have traded; the replay only fills it at the next real execution (see README, limitations).
