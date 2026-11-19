# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 33 | -42218.55 [-52224.16, -32336.49] (negative) | -42914.86 [-52935.68, -32929.41] (negative) | 0/33 | -23.605 [-26.293, -21.158] | -4906.34 [-12658.95, 683.48] (not established) |
| [AMZN](AMZN/summary.md) | 33 | -38302.93 [-49040.35, -29706.15] (negative) | -38694.88 [-49525.74, -30057.42] (negative) | 0/33 | -19.867 [-23.726, -16.840] | -1322.24 [-10290.84, 7827.37] (not established) |
| [GOOG](GOOG/summary.md) | 33 | -34455.56 [-44540.98, -26259.97] (negative) | -34779.95 [-44932.11, -26602.31] (negative) | 0/33 | -28.054 [-31.496, -24.726] | 3979.75 [-3838.66, 13693.89] (not established) |
| [INTC](INTC/summary.md) | 33 | -8536.43 [-11576.10, -5901.32] (negative) | -8586.79 [-11759.17, -5830.18] (negative) | 0/33 | -8.225 [-9.998, -6.627] | 188.61 [-2195.57, 2316.80] (not established) |
| [MSFT](MSFT/summary.md) | 33 | -120783.45 [-147810.08, -96209.20] (negative) | -121370.16 [-148542.50, -96627.30] (negative) | 0/33 | -59.473 [-70.234, -49.946] | 5308.75 [-3122.25, 14202.02] (not established) |
