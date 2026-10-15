# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 9 | -21512.31 [-24950.50, -18516.01] (negative) | -21898.35 [-25472.12, -18798.78] (negative) | 0/9 | -18.524 [-20.886, -16.689] | 5806.75 [3414.02, 8636.04] (positive) |
| [AMZN](AMZN/summary.md) | 9 | -26305.73 [-40121.38, -14383.76] (negative) | -26754.68 [-40879.17, -14641.23] (negative) | 0/9 | -22.251 [-34.568, -13.818] | -1441.71 [-16034.89, 11099.17] (not established) |
| [GOOG](GOOG/summary.md) | 9 | -27982.98 [-47614.97, -15484.94] (negative) | -28517.02 [-48257.04, -16031.04] (negative) | 0/9 | -25.216 [-30.008, -20.522] | 5846.36 [-4004.13, 18034.36] (not established) |
| [INTC](INTC/summary.md) | 9 | -16813.64 [-23289.56, -10142.00] (negative) | -17519.09 [-24238.58, -10701.35] (negative) | 0/9 | -13.667 [-15.839, -11.171] | -654.14 [-7249.62, 4146.93] (not established) |
| [MSFT](MSFT/summary.md) | 9 | -76837.22 [-97368.01, -55697.26] (negative) | -77205.26 [-97741.43, -55896.44] (negative) | 0/9 | -49.033 [-59.693, -39.415] | -2571.12 [-14665.74, 8100.07] (not established) |
