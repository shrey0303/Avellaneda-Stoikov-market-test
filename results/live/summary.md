# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 18 | -27786.84 [-33318.98, -23041.02] (negative) | -28322.23 [-33865.61, -23580.82] (negative) | 0/18 | -20.945 [-23.848, -18.260] | 2323.98 [-149.14, 4701.56] (not established) |
| [AMZN](AMZN/summary.md) | 18 | -28840.56 [-40061.41, -19122.51] (negative) | -29241.48 [-40655.99, -19508.85] (negative) | 0/18 | -20.609 [-27.855, -15.324] | -2329.53 [-10247.97, 4828.53] (not established) |
| [GOOG](GOOG/summary.md) | 18 | -26735.40 [-37889.17, -18124.05] (negative) | -27080.95 [-38250.65, -18437.37] (negative) | 0/18 | -29.359 [-34.058, -24.728] | 4022.96 [-1154.45, 10308.42] (not established) |
| [INTC](INTC/summary.md) | 18 | -9570.04 [-14462.04, -5110.97] (negative) | -9801.00 [-14919.06, -5087.53] (negative) | 0/18 | -8.904 [-11.373, -6.394] | -30.14 [-3462.39, 2410.31] (not established) |
| [MSFT](MSFT/summary.md) | 18 | -98445.95 [-130311.79, -74764.84] (negative) | -98674.49 [-130597.00, -74940.50] (negative) | 0/18 | -49.404 [-56.898, -42.605] | 4079.10 [-3877.35, 11725.67] (not established) |
