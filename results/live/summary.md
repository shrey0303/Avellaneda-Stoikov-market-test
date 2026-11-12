# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 28 | -44878.63 [-57243.41, -33939.14] (negative) | -45557.22 [-58150.40, -34575.52] (negative) | 0/28 | -23.556 [-26.727, -20.694] | -5509.52 [-14081.46, 1333.09] (not established) |
| [AMZN](AMZN/summary.md) | 28 | -39789.76 [-51316.97, -28846.62] (negative) | -40223.14 [-51769.20, -29280.60] (negative) | 0/28 | -20.229 [-24.572, -16.552] | 1365.70 [-7578.86, 10481.67] (not established) |
| [GOOG](GOOG/summary.md) | 28 | -34097.12 [-45434.47, -24866.28] (negative) | -34403.59 [-45817.60, -25142.58] (negative) | 0/28 | -27.824 [-31.893, -24.004] | 5100.77 [-4459.84, 17745.10] (not established) |
| [INTC](INTC/summary.md) | 28 | -9002.40 [-12318.50, -5818.04] (negative) | -9053.03 [-12476.43, -5780.99] (negative) | 0/28 | -8.121 [-10.053, -6.321] | 1195.07 [-1247.99, 3408.48] (not established) |
| [MSFT](MSFT/summary.md) | 28 | -128474.61 [-160256.82, -99686.28] (negative) | -129051.80 [-160974.23, -100161.40] (negative) | 0/28 | -61.477 [-74.893, -50.525] | 4329.17 [-5090.67, 14205.32] (not established) |
