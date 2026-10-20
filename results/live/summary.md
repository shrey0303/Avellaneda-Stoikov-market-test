# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 11 | -23200.09 [-26689.10, -19861.55] (negative) | -23646.96 [-27258.22, -20243.26] (negative) | 0/11 | -18.699 [-20.876, -16.979] | 3710.81 [-88.42, 7053.75] (not established) |
| [AMZN](AMZN/summary.md) | 11 | -26181.10 [-38232.87, -15657.40] (negative) | -26644.51 [-39002.93, -15889.42] (negative) | 0/11 | -21.295 [-32.239, -14.042] | -2046.25 [-14479.61, 8402.98] (not established) |
| [GOOG](GOOG/summary.md) | 11 | -29355.60 [-46180.82, -18125.16] (negative) | -29841.07 [-46825.19, -18572.82] (negative) | 0/11 | -27.583 [-32.715, -22.565] | 5617.34 [-2388.31, 15866.63] (not established) |
| [INTC](INTC/summary.md) | 11 | -14278.51 [-20415.40, -8326.73] (negative) | -14807.97 [-21139.77, -8572.94] (negative) | 0/11 | -12.007 [-14.745, -9.129] | -611.32 [-5887.85, 3385.68] (not established) |
| [MSFT](MSFT/summary.md) | 11 | -100731.22 [-146459.46, -66111.11] (negative) | -101043.68 [-146705.18, -66325.50] (negative) | 0/11 | -50.733 [-60.299, -41.578] | 696.67 [-9367.96, 10775.20] (not established) |
