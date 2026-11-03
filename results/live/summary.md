# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 21 | -30382.86 [-37379.04, -24097.07] (negative) | -30988.99 [-38099.05, -24703.19] (negative) | 0/21 | -20.755 [-23.209, -18.343] | 1014.11 [-1943.53, 3744.52] (not established) |
| [AMZN](AMZN/summary.md) | 21 | -32810.08 [-43580.99, -23210.76] (negative) | -33193.06 [-44064.53, -23516.31] (negative) | 0/21 | -20.054 [-25.998, -15.409] | 3120.59 [-6726.06, 14308.33] (not established) |
| [GOOG](GOOG/summary.md) | 21 | -29859.61 [-41090.49, -21140.49] (negative) | -30184.27 [-41423.70, -21490.42] (negative) | 0/21 | -27.711 [-32.255, -23.340] | 9569.65 [-307.46, 25511.07] (not established) |
| [INTC](INTC/summary.md) | 21 | -8742.89 [-13170.44, -4929.71] (negative) | -8903.07 [-13489.12, -4808.60] (negative) | 0/21 | -8.137 [-10.576, -5.828] | 119.51 [-2837.79, 2365.29] (not established) |
| [MSFT](MSFT/summary.md) | 21 | -116734.40 [-148176.17, -87082.67] (negative) | -117145.05 [-148788.98, -87326.09] (negative) | 0/21 | -50.439 [-57.045, -44.030] | 6736.24 [-2988.15, 17798.74] (not established) |
