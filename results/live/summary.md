# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 19 | -26933.88 [-32644.27, -22164.93] (negative) | -27451.96 [-33095.67, -22577.34] (negative) | 0/19 | -20.693 [-23.518, -18.137] | 2060.51 [-489.76, 4461.33] (not established) |
| [AMZN](AMZN/summary.md) | 19 | -29070.00 [-39767.11, -19690.19] (negative) | -29452.81 [-40150.96, -20000.96] (negative) | 0/19 | -20.140 [-27.029, -15.031] | 1619.74 [-8891.03, 12368.42] (not established) |
| [GOOG](GOOG/summary.md) | 19 | -29457.07 [-40751.56, -19872.46] (negative) | -29796.75 [-41233.24, -20180.88] (negative) | 0/19 | -28.616 [-33.491, -24.111] | 10788.86 [-57.95, 26949.63] (not established) |
| [INTC](INTC/summary.md) | 19 | -9180.85 [-13743.63, -4957.69] (negative) | -9383.99 [-14201.34, -4961.15] (negative) | 0/19 | -8.624 [-11.097, -6.157] | -53.10 [-3373.11, 2300.32] (not established) |
| [MSFT](MSFT/summary.md) | 19 | -105300.95 [-136866.28, -78917.15] (negative) | -105609.43 [-137218.50, -79216.39] (negative) | 0/19 | -48.969 [-56.264, -42.365] | 2643.44 [-5479.30, 10484.12] (not established) |
