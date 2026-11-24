# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 36 | -41522.49 [-52132.27, -32300.85] (negative) | -42121.45 [-52808.59, -32812.24] (negative) | 0/36 | -23.192 [-25.527, -20.870] | -4762.69 [-11904.53, 693.80] (not established) |
| [AMZN](AMZN/summary.md) | 36 | -41030.83 [-51495.18, -31863.25] (negative) | -41406.18 [-51871.36, -32193.96] (negative) | 0/36 | -19.965 [-23.875, -17.002] | 2538.29 [-7368.96, 13565.92] (not established) |
| [GOOG](GOOG/summary.md) | 36 | -37232.33 [-47794.49, -28719.66] (negative) | -37555.66 [-48167.78, -29013.54] (negative) | 0/36 | -28.396 [-31.864, -25.235] | 4408.71 [-3330.60, 13549.84] (not established) |
| [INTC](INTC/summary.md) | 36 | -8358.52 [-10933.12, -5854.63] (negative) | -8382.03 [-11084.95, -5767.73] (negative) | 0/36 | -7.932 [-9.518, -6.388] | 454.66 [-1711.79, 2499.04] (not established) |
| [MSFT](MSFT/summary.md) | 36 | -121968.40 [-147817.46, -97610.80] (negative) | -122549.47 [-148397.99, -98077.73] (negative) | 0/36 | -58.295 [-68.517, -49.033] | 8649.80 [-1713.85, 20325.88] (not established) |
