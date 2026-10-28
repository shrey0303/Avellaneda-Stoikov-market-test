# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 17 | -28348.28 [-34221.15, -23359.35] (negative) | -28871.07 [-34646.61, -23853.19] (negative) | 0/17 | -20.833 [-23.841, -18.142] | 2536.38 [-71.79, 5237.82] (not established) |
| [AMZN](AMZN/summary.md) | 17 | -29812.21 [-41355.28, -19485.72] (negative) | -30232.59 [-41906.17, -19800.10] (negative) | 0/17 | -21.100 [-27.864, -15.336] | -2945.38 [-11325.63, 5058.32] (not established) |
| [GOOG](GOOG/summary.md) | 17 | -26441.78 [-38453.66, -17541.43] (negative) | -26810.65 [-38942.37, -17905.02] (negative) | 0/17 | -28.904 [-33.877, -24.248] | 4538.79 [-936.07, 11546.25] (not established) |
| [INTC](INTC/summary.md) | 17 | -10038.28 [-15261.99, -5405.81] (negative) | -10289.94 [-15771.81, -5416.20] (negative) | 0/17 | -9.203 [-11.866, -6.625] | -102.12 [-3767.77, 2469.48] (not established) |
| [MSFT](MSFT/summary.md) | 17 | -99690.42 [-132064.60, -74159.17] (negative) | -99926.01 [-132326.85, -74385.92] (negative) | 0/17 | -49.335 [-57.201, -42.096] | 3930.26 [-4290.31, 11413.24] (not established) |
