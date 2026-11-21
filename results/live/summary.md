# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 35 | -42082.22 [-52565.53, -32800.89] (negative) | -42703.18 [-53319.47, -33372.25] (negative) | 0/35 | -23.383 [-26.137, -20.928] | -4624.36 [-11977.55, 859.21] (not established) |
| [AMZN](AMZN/summary.md) | 35 | -40943.79 [-51395.26, -31473.79] (negative) | -41333.85 [-51834.40, -31838.46] (negative) | 0/35 | -19.943 [-23.718, -16.932] | 3201.00 [-7067.14, 14036.86] (not established) |
| [GOOG](GOOG/summary.md) | 35 | -37321.60 [-47461.61, -28609.69] (negative) | -37645.75 [-47805.26, -28901.64] (negative) | 0/35 | -28.599 [-32.062, -25.408] | 3322.40 [-3953.89, 12686.95] (not established) |
| [INTC](INTC/summary.md) | 35 | -8510.45 [-11343.52, -5972.75] (negative) | -8539.79 [-11493.10, -5892.14] (negative) | 0/35 | -8.045 [-9.735, -6.547] | 475.22 [-1852.78, 2561.58] (not established) |
| [MSFT](MSFT/summary.md) | 35 | -124101.71 [-149750.67, -97890.02] (negative) | -124704.61 [-150413.42, -98340.37] (negative) | 0/35 | -58.703 [-69.567, -49.738] | 8063.30 [-2801.16, 19697.95] (not established) |
