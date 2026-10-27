# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 16 | -27770.51 [-33741.38, -22870.77] (negative) | -28242.23 [-34187.20, -23306.18] (negative) | 0/16 | -20.174 [-23.291, -17.495] | 2220.86 [-397.80, 4957.41] (not established) |
| [AMZN](AMZN/summary.md) | 16 | -31528.24 [-43757.22, -21327.06] (negative) | -31944.25 [-44159.46, -21568.14] (negative) | 0/16 | -21.950 [-28.738, -16.284] | -2745.03 [-11419.36, 5206.80] (not established) |
| [GOOG](GOOG/summary.md) | 16 | -27189.14 [-39559.45, -17792.67] (negative) | -27571.23 [-40031.86, -18103.34] (negative) | 0/16 | -29.332 [-34.823, -24.320] | 4427.37 [-1228.68, 11664.57] (not established) |
| [INTC](INTC/summary.md) | 16 | -10565.01 [-16077.40, -5650.72] (negative) | -10844.22 [-16617.62, -5656.19] (negative) | 0/16 | -9.558 [-12.180, -6.863] | -35.90 [-3917.23, 2853.93] (not established) |
| [MSFT](MSFT/summary.md) | 16 | -101426.07 [-137503.89, -74680.44] (negative) | -101679.59 [-137695.26, -74849.16] (negative) | 0/16 | -48.645 [-56.797, -41.432] | 3553.22 [-5419.15, 11766.73] (not established) |
