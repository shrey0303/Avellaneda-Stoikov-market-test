# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 14 | -25730.56 [-31741.16, -21028.26] (negative) | -26121.36 [-32060.45, -21440.95] (negative) | 0/14 | -19.126 [-22.038, -16.560] | 2449.97 [-560.44, 5502.04] (not established) |
| [AMZN](AMZN/summary.md) | 14 | -27088.42 [-37232.84, -18781.20] (negative) | -27533.85 [-38016.14, -19048.20] (negative) | 0/14 | -20.499 [-28.831, -14.882] | -2323.99 [-12749.45, 6620.27] (not established) |
| [GOOG](GOOG/summary.md) | 14 | -28003.61 [-42114.44, -17695.33] (negative) | -28426.04 [-42643.28, -18088.69] (negative) | 0/14 | -28.308 [-33.080, -23.531] | 5505.93 [-833.97, 14020.47] (not established) |
| [INTC](INTC/summary.md) | 14 | -11644.99 [-17226.91, -6384.52] (negative) | -12003.72 [-17893.68, -6469.52] (negative) | 0/14 | -10.315 [-12.989, -7.537] | -246.60 [-4599.01, 2979.22] (not established) |
| [MSFT](MSFT/summary.md) | 14 | -95753.86 [-134698.72, -68451.98] (negative) | -96020.05 [-135084.02, -68766.45] (negative) | 0/14 | -47.149 [-56.422, -39.332] | 3923.06 [-5710.61, 13084.11] (not established) |
