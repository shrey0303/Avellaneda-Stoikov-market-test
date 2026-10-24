# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 15 | -26291.44 [-32091.17, -21704.25] (negative) | -26708.26 [-32399.03, -22130.58] (negative) | 0/15 | -19.487 [-22.354, -16.988] | 2391.78 [-438.83, 5283.25] (not established) |
| [AMZN](AMZN/summary.md) | 15 | -27569.82 [-36672.49, -19526.27] (negative) | -28007.09 [-37356.35, -19799.93] (negative) | 0/15 | -20.962 [-28.422, -15.567] | -2487.85 [-11146.81, 6217.57] (not established) |
| [GOOG](GOOG/summary.md) | 15 | -28652.40 [-40912.08, -18941.90] (negative) | -29055.44 [-41487.45, -19333.63] (negative) | 0/15 | -29.957 [-35.280, -24.803] | 5050.63 [-886.88, 12441.74] (not established) |
| [INTC](INTC/summary.md) | 15 | -10989.00 [-16501.97, -6069.80] (negative) | -11319.20 [-17071.11, -6141.16] (negative) | 0/15 | -9.868 [-12.663, -7.175] | -143.62 [-4185.55, 2923.69] (not established) |
| [MSFT](MSFT/summary.md) | 15 | -100721.70 [-136790.88, -72119.07] (negative) | -100976.06 [-136901.80, -72285.92] (negative) | 0/15 | -48.694 [-56.979, -40.667] | 3097.40 [-6196.09, 12064.94] (not established) |
