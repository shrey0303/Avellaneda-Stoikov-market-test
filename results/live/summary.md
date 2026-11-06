# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 24 | -41344.32 [-54943.30, -29875.15] (negative) | -42062.59 [-55836.05, -30442.75] (negative) | 0/24 | -21.354 [-23.659, -19.140] | -5663.65 [-16844.95, 1511.76] (not established) |
| [AMZN](AMZN/summary.md) | 24 | -39758.95 [-53354.54, -27820.12] (negative) | -40166.85 [-53746.37, -28129.34] (negative) | 0/24 | -20.093 [-25.362, -15.868] | 1090.47 [-9857.83, 12108.14] (not established) |
| [GOOG](GOOG/summary.md) | 24 | -33516.05 [-46612.08, -22563.19] (negative) | -33865.03 [-47015.42, -22906.64] (negative) | 0/24 | -28.183 [-32.490, -24.144] | 5902.97 [-4823.46, 19769.22] (not established) |
| [INTC](INTC/summary.md) | 24 | -8568.33 [-12481.80, -5188.05] (negative) | -8632.17 [-12690.36, -5130.46] (negative) | 0/24 | -7.690 [-9.835, -5.764] | 751.69 [-2000.65, 2914.47] (not established) |
| [MSFT](MSFT/summary.md) | 24 | -134540.40 [-169924.05, -102792.26] (negative) | -134998.91 [-170436.92, -103101.50] (negative) | 0/24 | -58.430 [-71.307, -48.067] | 6611.17 [-2419.67, 16860.16] (not established) |
