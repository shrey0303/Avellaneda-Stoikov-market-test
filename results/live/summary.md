# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 12 | -26151.97 [-33286.95, -20861.14] (negative) | -26509.53 [-33454.66, -21236.05] (negative) | 0/12 | -19.941 [-23.135, -17.314] | 3231.66 [-304.41, 6343.97] (not established) |
| [AMZN](AMZN/summary.md) | 12 | -26075.81 [-37550.61, -16367.79] (negative) | -26524.00 [-38333.97, -16554.01] (negative) | 0/12 | -20.920 [-30.357, -14.222] | -546.86 [-11900.49, 9150.69] (not established) |
| [GOOG](GOOG/summary.md) | 12 | -27543.70 [-44573.17, -16518.48] (negative) | -27983.45 [-45196.61, -16924.14] (negative) | 0/12 | -27.722 [-32.566, -22.963] | 5207.47 [-2034.96, 15786.45] (not established) |
| [INTC](INTC/summary.md) | 12 | -13246.79 [-19115.88, -7320.57] (negative) | -13686.61 [-19751.58, -7465.25] (negative) | 0/12 | -11.318 [-14.129, -8.372] | -683.15 [-5546.64, 3002.80] (not established) |
| [MSFT](MSFT/summary.md) | 12 | -102049.87 [-145661.38, -70530.05] (negative) | -102351.68 [-145772.84, -70883.37] (negative) | 0/12 | -49.581 [-59.419, -41.121] | 3430.28 [-7371.05, 13856.95] (not established) |
