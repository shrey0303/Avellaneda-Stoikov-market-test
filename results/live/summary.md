# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 27 | -45202.53 [-58514.96, -33533.48] (negative) | -45893.53 [-59242.50, -34164.93] (negative) | 0/27 | -23.516 [-26.666, -20.583] | -5892.32 [-15465.65, 796.32] (not established) |
| [AMZN](AMZN/summary.md) | 27 | -39936.60 [-52283.87, -28998.22] (negative) | -40378.11 [-52748.13, -29430.26] (negative) | 0/27 | -20.278 [-25.200, -16.639] | 400.52 [-9407.67, 9721.40] (not established) |
| [GOOG](GOOG/summary.md) | 27 | -34534.98 [-46080.68, -24831.43] (negative) | -34846.91 [-46474.33, -25132.83] (negative) | 0/27 | -28.237 [-32.460, -24.271] | 5004.55 [-4562.74, 16654.01] (not established) |
| [INTC](INTC/summary.md) | 27 | -9244.90 [-12726.98, -6122.03] (negative) | -9301.89 [-12910.42, -6065.33] (negative) | 0/27 | -8.204 [-10.260, -6.358] | 1511.51 [-1116.74, 3888.90] (not established) |
| [MSFT](MSFT/summary.md) | 27 | -130336.95 [-164010.06, -100262.25] (negative) | -130782.93 [-164598.89, -100609.23] (negative) | 0/27 | -61.796 [-75.277, -50.685] | 6385.53 [-2016.48, 16182.05] (not established) |
