# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 30 | -43725.17 [-55384.84, -33290.95] (negative) | -44419.28 [-56219.98, -33966.78] (negative) | 0/30 | -23.684 [-26.693, -21.119] | -5147.21 [-13811.42, 911.90] (not established) |
| [AMZN](AMZN/summary.md) | 30 | -38716.72 [-49797.69, -28979.85] (negative) | -39141.02 [-50312.77, -29347.31] (negative) | 0/30 | -20.128 [-24.451, -16.741] | 818.11 [-8725.50, 10011.21] (not established) |
| [GOOG](GOOG/summary.md) | 30 | -34324.91 [-45626.19, -25680.64] (negative) | -34663.06 [-46037.41, -25937.89] (negative) | 0/30 | -27.474 [-31.182, -23.796] | 4112.07 [-4499.27, 15747.24] (not established) |
| [INTC](INTC/summary.md) | 30 | -8841.32 [-12055.78, -5869.58] (negative) | -8881.10 [-12254.69, -5763.48] (negative) | 0/30 | -8.301 [-10.169, -6.563] | 955.28 [-1305.24, 2987.95] (not established) |
| [MSFT](MSFT/summary.md) | 30 | -125350.38 [-155566.42, -97277.64] (negative) | -125963.69 [-156319.08, -97803.67] (negative) | 0/30 | -61.027 [-72.980, -51.129] | 5154.69 [-3696.31, 14589.62] (not established) |
