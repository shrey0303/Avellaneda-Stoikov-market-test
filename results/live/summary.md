# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 23 | -38330.58 [-52031.93, -27767.13] (negative) | -38985.83 [-52856.78, -28253.52] (negative) | 0/23 | -21.188 [-23.566, -18.935] | -1308.73 [-5892.40, 2305.06] (not established) |
| [AMZN](AMZN/summary.md) | 23 | -35038.89 [-45306.44, -25502.67] (negative) | -35430.21 [-45782.28, -25776.67] (negative) | 0/23 | -19.931 [-25.518, -15.572] | -338.95 [-11469.79, 10839.77] (not established) |
| [GOOG](GOOG/summary.md) | 23 | -29081.14 [-39022.29, -20876.38] (negative) | -29417.03 [-39402.38, -21112.52] (negative) | 0/23 | -27.464 [-31.857, -23.494] | 6121.07 [-5214.88, 21323.77] (not established) |
| [INTC](INTC/summary.md) | 23 | -8314.05 [-12439.88, -4650.65] (negative) | -8410.59 [-12706.78, -4543.68] (negative) | 0/23 | -7.792 [-10.035, -5.623] | 228.83 [-2467.51, 2231.20] (not established) |
| [MSFT](MSFT/summary.md) | 23 | -126599.47 [-160108.78, -96733.17] (negative) | -127041.80 [-160697.20, -96956.79] (negative) | 0/23 | -56.255 [-69.490, -46.546] | 5804.59 [-3137.90, 17179.32] (not established) |
