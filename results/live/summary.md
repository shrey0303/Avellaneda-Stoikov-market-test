# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 32 | -42498.02 [-53503.80, -32343.19] (negative) | -43181.67 [-54342.13, -32953.87] (negative) | 0/32 | -23.592 [-26.388, -21.064] | -5214.02 [-13384.05, 725.31] (not established) |
| [AMZN](AMZN/summary.md) | 32 | -38555.59 [-49059.96, -29652.29] (negative) | -38976.05 [-49621.93, -30072.84] (negative) | 0/32 | -20.128 [-24.162, -16.921] | 373.00 [-8161.07, 8948.74] (not established) |
| [GOOG](GOOG/summary.md) | 32 | -34883.02 [-44924.93, -26285.12] (negative) | -35216.88 [-45335.17, -26605.19] (negative) | 0/32 | -27.855 [-31.523, -24.329] | 3931.39 [-3955.29, 15085.60] (not established) |
| [INTC](INTC/summary.md) | 32 | -8585.94 [-11644.87, -5956.28] (negative) | -8635.75 [-11832.33, -5875.22] (negative) | 0/32 | -8.231 [-9.980, -6.597] | 490.71 [-1732.33, 2627.29] (not established) |
| [MSFT](MSFT/summary.md) | 32 | -121700.61 [-149725.93, -95398.18] (negative) | -122300.44 [-150413.21, -96106.92] (negative) | 0/32 | -60.094 [-71.934, -50.311] | 4252.07 [-4175.56, 13386.55] (not established) |
