# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 39 | -43813.68 [-54314.25, -34526.43] (negative) | -44333.82 [-54913.18, -35060.70] (negative) | 0/39 | -23.885 [-26.283, -21.610] | -3741.52 [-10636.48, 1381.38] (not established) |
| [AMZN](AMZN/summary.md) | 39 | -40958.27 [-50600.20, -32347.52] (negative) | -41288.93 [-50983.50, -32661.79] (negative) | 0/39 | -20.168 [-23.581, -17.452] | 3108.05 [-6392.08, 13133.87] (not established) |
| [GOOG](GOOG/summary.md) | 39 | -37275.79 [-47008.39, -28490.70] (negative) | -37583.27 [-47291.27, -28793.04] (negative) | 0/39 | -28.376 [-31.452, -25.210] | 4989.93 [-2212.69, 13992.25] (not established) |
| [INTC](INTC/summary.md) | 39 | -7916.29 [-10580.66, -5501.92] (negative) | -7915.57 [-10711.66, -5435.98] (negative) | 0/39 | -7.654 [-9.221, -6.202] | 616.24 [-1400.94, 2508.84] (not established) |
| [MSFT](MSFT/summary.md) | 39 | -121727.82 [-145920.37, -99054.63] (negative) | -122332.13 [-146566.40, -99588.61] (negative) | 0/39 | -62.040 [-73.508, -52.568] | 8821.01 [-760.67, 19657.69] (not established) |
