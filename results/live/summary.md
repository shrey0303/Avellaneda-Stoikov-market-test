# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 38 | -44050.85 [-54771.27, -34596.73] (negative) | -44584.75 [-55378.45, -35078.07] (negative) | 0/38 | -23.703 [-26.194, -21.367] | -3890.17 [-11428.36, 1586.55] (not established) |
| [AMZN](AMZN/summary.md) | 38 | -40538.68 [-50290.92, -31712.53] (negative) | -40888.71 [-50674.77, -32058.65] (negative) | 0/38 | -19.929 [-23.422, -17.176] | 3013.82 [-6123.16, 12869.68] (not established) |
| [GOOG](GOOG/summary.md) | 38 | -37795.99 [-47325.58, -29217.83] (negative) | -38114.53 [-47710.31, -29499.24] (negative) | 0/38 | -28.545 [-31.736, -25.336] | 5135.04 [-2400.44, 13825.28] (not established) |
| [INTC](INTC/summary.md) | 38 | -8083.41 [-10638.61, -5881.17] (negative) | -8084.18 [-10779.40, -5768.08] (negative) | 0/38 | -7.731 [-9.359, -6.343] | 640.59 [-1460.37, 2588.74] (not established) |
| [MSFT](MSFT/summary.md) | 38 | -122038.82 [-146197.69, -98891.52] (negative) | -122637.07 [-146813.29, -99382.22] (negative) | 0/38 | -59.930 [-70.203, -51.191] | 8806.57 [-779.12, 19872.23] (not established) |
