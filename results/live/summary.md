# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 13 | -25946.78 [-32924.86, -20874.82] (negative) | -26295.00 [-33130.06, -21223.65] (negative) | 0/13 | -19.713 [-22.701, -17.341] | 2865.31 [-373.70, 5915.71] (not established) |
| [AMZN](AMZN/summary.md) | 13 | -25524.63 [-36244.30, -16911.19] (negative) | -25973.81 [-36967.15, -17150.74] (negative) | 0/13 | -20.511 [-29.450, -14.586] | -603.12 [-11061.76, 8286.44] (not established) |
| [GOOG](GOOG/summary.md) | 13 | -29058.90 [-43971.46, -18454.44] (negative) | -29476.66 [-44566.14, -18873.75] (negative) | 0/13 | -28.875 [-33.859, -23.779] | 5491.66 [-1426.32, 14374.50] (not established) |
| [INTC](INTC/summary.md) | 13 | -12459.50 [-18512.53, -6936.54] (negative) | -12864.85 [-19115.10, -7057.04] (negative) | 0/13 | -10.851 [-13.591, -7.969] | -347.49 [-4912.22, 3179.42] (not established) |
| [MSFT](MSFT/summary.md) | 13 | -97604.77 [-137825.02, -67617.72] (negative) | -97880.71 [-138080.06, -68173.25] (negative) | 0/13 | -48.442 [-57.375, -40.314] | 3019.46 [-6743.38, 12912.83] (not established) |
