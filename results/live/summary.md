# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 20 | -28788.68 [-35622.69, -23386.28] (negative) | -29365.40 [-36372.54, -23889.73] (negative) | 0/20 | -20.692 [-23.346, -18.273] | 1071.22 [-2207.13, 3975.75] (not established) |
| [AMZN](AMZN/summary.md) | 20 | -31155.66 [-42168.01, -21306.25] (negative) | -31569.89 [-42710.59, -21602.13] (negative) | 0/20 | -19.736 [-26.550, -14.969] | 4014.49 [-6547.69, 14983.48] (not established) |
| [GOOG](GOOG/summary.md) | 20 | -29980.77 [-41019.73, -20988.07] (negative) | -30311.18 [-41482.50, -21285.04] (negative) | 0/20 | -27.891 [-32.471, -23.459] | 10000.85 [-342.29, 24702.31] (not established) |
| [INTC](INTC/summary.md) | 20 | -9083.96 [-13816.60, -5103.01] (negative) | -9250.64 [-14236.38, -5128.87] (negative) | 0/20 | -8.386 [-10.820, -6.082] | 174.31 [-3045.22, 2432.80] (not established) |
| [MSFT](MSFT/summary.md) | 20 | -111882.42 [-143490.48, -82597.01] (negative) | -112253.25 [-143875.72, -82906.08] (negative) | 0/20 | -49.547 [-56.395, -43.219] | 2574.91 [-4981.30, 9199.43] (not established) |
