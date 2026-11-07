# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 25 | -43754.38 [-58089.87, -31653.03] (negative) | -44458.46 [-59049.39, -32342.53] (negative) | 0/25 | -21.977 [-24.461, -19.509] | -5929.54 [-16544.45, 1105.05] (not established) |
| [AMZN](AMZN/summary.md) | 25 | -40642.16 [-55339.70, -28829.54] (negative) | -41083.60 [-55918.46, -29232.83] (negative) | 0/25 | -20.463 [-25.329, -16.417] | -80.63 [-9734.12, 10336.31] (not established) |
| [GOOG](GOOG/summary.md) | 25 | -34320.72 [-47861.47, -23565.99] (negative) | -34649.30 [-48233.76, -23913.64] (negative) | 0/25 | -28.871 [-33.145, -24.757] | 5620.83 [-4825.89, 18957.03] (not established) |
| [INTC](INTC/summary.md) | 25 | -8704.10 [-12405.52, -5459.71] (negative) | -8762.11 [-12625.18, -5339.94] (negative) | 0/25 | -7.665 [-9.758, -5.800] | 855.13 [-1652.72, 2941.27] (not established) |
| [MSFT](MSFT/summary.md) | 25 | -135881.85 [-170598.16, -104538.70] (negative) | -136386.91 [-171252.81, -104957.43] (negative) | 0/25 | -62.444 [-77.505, -50.079] | 5535.78 [-4056.69, 15336.14] (not established) |
