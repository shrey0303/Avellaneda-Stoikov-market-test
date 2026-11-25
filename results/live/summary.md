# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 37 | -42674.24 [-53168.75, -33375.45] (negative) | -43229.14 [-53753.42, -33920.19] (negative) | 0/37 | -23.515 [-25.882, -21.021] | -4602.90 [-11723.03, 727.47] (not established) |
| [AMZN](AMZN/summary.md) | 37 | -40388.47 [-50366.11, -31543.65] (negative) | -40753.98 [-50780.12, -31862.41] (negative) | 0/37 | -19.952 [-23.488, -17.158] | 2917.53 [-7113.09, 13420.22] (not established) |
| [GOOG](GOOG/summary.md) | 37 | -36877.56 [-46706.93, -28312.60] (negative) | -37201.81 [-47003.59, -28582.79] (negative) | 0/37 | -28.156 [-31.482, -25.160] | 4540.51 [-2719.13, 13312.98] (not established) |
| [INTC](INTC/summary.md) | 37 | -8236.45 [-10800.41, -5829.58] (negative) | -8245.64 [-10950.70, -5713.04] (negative) | 0/37 | -7.841 [-9.377, -6.347] | 581.20 [-1647.55, 2609.96] (not established) |
| [MSFT](MSFT/summary.md) | 37 | -121575.50 [-149305.98, -97550.34] (negative) | -122165.91 [-149976.84, -98169.28] (negative) | 0/37 | -58.388 [-68.964, -49.664] | 8699.84 [-1288.01, 20472.74] (not established) |
