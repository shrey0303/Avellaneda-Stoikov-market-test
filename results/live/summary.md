# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 34 | -42102.47 [-52526.52, -32475.38] (negative) | -42757.28 [-53296.70, -33035.78] (negative) | 0/34 | -23.535 [-26.058, -21.026] | -4232.27 [-12014.50, 1267.05] (not established) |
| [AMZN](AMZN/summary.md) | 34 | -39533.73 [-49878.28, -30507.48] (negative) | -39904.15 [-50298.90, -30816.55] (negative) | 0/34 | -19.978 [-23.860, -16.968] | 1639.71 [-8180.97, 12222.29] (not established) |
| [GOOG](GOOG/summary.md) | 34 | -36964.02 [-47571.91, -27571.87] (negative) | -37289.63 [-47926.72, -27865.59] (negative) | 0/34 | -28.312 [-31.762, -24.975] | 3594.92 [-3771.80, 13588.73] (not established) |
| [INTC](INTC/summary.md) | 34 | -8616.07 [-11585.07, -5982.14] (negative) | -8667.24 [-11789.73, -5938.66] (negative) | 0/34 | -8.173 [-9.861, -6.610] | 486.83 [-1870.20, 2634.95] (not established) |
| [MSFT](MSFT/summary.md) | 34 | -120549.56 [-147457.64, -94979.83] (negative) | -121127.03 [-148289.33, -95457.95] (negative) | 0/34 | -59.640 [-70.470, -50.362] | 4197.42 [-3957.89, 12831.82] (not established) |
