# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 22 | -34688.69 [-46360.32, -25511.42] (negative) | -35286.29 [-46951.68, -26031.68] (negative) | 0/22 | -20.744 [-23.291, -18.449] | 277.18 [-2907.10, 3313.47] (not established) |
| [AMZN](AMZN/summary.md) | 22 | -33194.84 [-43356.48, -23952.57] (negative) | -33585.54 [-43795.42, -24194.68] (negative) | 0/22 | -19.837 [-25.820, -15.354] | 2119.08 [-7788.71, 12642.67] (not established) |
| [GOOG](GOOG/summary.md) | 22 | -29130.41 [-39987.25, -20509.96] (negative) | -29438.32 [-40364.95, -20723.73] (negative) | 0/22 | -27.658 [-32.199, -23.328] | 8981.26 [-319.17, 22393.18] (not established) |
| [INTC](INTC/summary.md) | 22 | -8429.08 [-12776.94, -4823.32] (negative) | -8570.29 [-13143.53, -4758.88] (negative) | 0/22 | -7.961 [-10.310, -5.757] | 182.16 [-2556.95, 2258.85] (not established) |
| [MSFT](MSFT/summary.md) | 22 | -124600.50 [-159432.73, -93365.76] (negative) | -125037.39 [-159923.12, -93784.22] (negative) | 0/22 | -55.744 [-69.921, -45.550] | 5181.34 [-4610.06, 16508.73] (not established) |
