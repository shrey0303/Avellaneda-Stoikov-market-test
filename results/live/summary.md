# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 29 | -44195.13 [-56748.45, -33079.12] (negative) | -44874.13 [-57555.96, -33625.92] (negative) | 0/29 | -23.696 [-26.672, -20.898] | -5402.89 [-14210.66, 1031.07] (not established) |
| [AMZN](AMZN/summary.md) | 29 | -39338.68 [-50904.25, -29154.32] (negative) | -39766.25 [-51379.08, -29475.90] (negative) | 0/29 | -20.187 [-24.461, -16.565] | 1725.87 [-7467.11, 11034.20] (not established) |
| [GOOG](GOOG/summary.md) | 29 | -33995.62 [-44417.03, -24914.10] (negative) | -34292.16 [-44740.45, -25233.15] (negative) | 0/29 | -27.588 [-31.714, -23.794] | 4407.66 [-4688.87, 15832.58] (not established) |
| [INTC](INTC/summary.md) | 29 | -8852.60 [-12347.40, -5880.25] (negative) | -8892.09 [-12532.99, -5804.13] (negative) | 0/29 | -8.151 [-10.149, -6.401] | 1129.87 [-1332.22, 3377.70] (not established) |
| [MSFT](MSFT/summary.md) | 29 | -126364.76 [-156773.16, -98396.25] (negative) | -126937.47 [-157612.72, -98896.15] (negative) | 0/29 | -61.417 [-74.000, -51.064] | 4283.02 [-4937.65, 14021.07] (not established) |
