# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 26 | -45191.50 [-59198.97, -32935.51] (negative) | -45902.83 [-60042.65, -33508.59] (negative) | 0/26 | -22.844 [-25.964, -20.124] | -6433.01 [-15913.13, 553.46] (not established) |
| [AMZN](AMZN/summary.md) | 26 | -40366.68 [-53531.26, -28610.61] (negative) | -40817.46 [-54053.42, -29028.57] (negative) | 0/26 | -20.394 [-25.465, -16.471] | 48.18 [-10003.18, 10440.16] (not established) |
| [GOOG](GOOG/summary.md) | 26 | -34346.74 [-45753.34, -24453.17] (negative) | -34667.68 [-46157.38, -24708.37] (negative) | 0/26 | -28.443 [-32.743, -24.504] | 5111.52 [-4548.44, 17891.99] (not established) |
| [INTC](INTC/summary.md) | 26 | -9102.95 [-12627.81, -5846.17] (negative) | -9159.57 [-12873.66, -5756.88] (negative) | 0/26 | -8.060 [-10.196, -6.087] | 991.33 [-1455.77, 3080.75] (not established) |
| [MSFT](MSFT/summary.md) | 26 | -132370.98 [-166977.13, -100861.56] (negative) | -132836.77 [-167660.72, -101181.79] (negative) | 0/26 | -62.260 [-76.469, -50.469] | 5403.77 [-3503.57, 14615.20] (not established) |
