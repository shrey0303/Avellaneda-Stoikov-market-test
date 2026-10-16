# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 10 | -22276.98 [-25658.36, -18829.78] (negative) | -22655.78 [-26083.05, -19151.57] (negative) | 0/10 | -18.260 [-20.409, -16.529] | 5071.55 [2442.47, 7907.30] (positive) |
| [AMZN](AMZN/summary.md) | 10 | -25190.13 [-37291.84, -14205.65] (negative) | -25615.40 [-38130.24, -14428.19] (negative) | 0/10 | -21.154 [-32.536, -13.227] | -1948.68 [-14925.18, 9351.18] (not established) |
| [GOOG](GOOG/summary.md) | 10 | -29562.96 [-47205.85, -16586.95] (negative) | -30095.56 [-47776.28, -17044.18] (negative) | 0/10 | -27.180 [-33.023, -21.785] | 5701.74 [-3232.61, 17006.94] (not established) |
| [INTC](INTC/summary.md) | 10 | -15374.38 [-21950.52, -8768.65] (negative) | -15974.67 [-22819.20, -9143.91] (negative) | 0/10 | -12.685 [-15.404, -9.690] | -736.25 [-6826.76, 3622.53] (not established) |
| [MSFT](MSFT/summary.md) | 10 | -99625.18 [-153046.22, -62948.32] (negative) | -99974.06 [-153409.08, -63208.15] (negative) | 0/10 | -51.515 [-62.556, -41.593] | 237.46 [-11390.83, 11646.27] (not established) |
