# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 8 | -22543.69 [-25881.10, -19608.40] (negative) | -22962.73 [-26325.94, -20053.60] (negative) | 0/8 | -18.509 [-21.216, -16.389] | 5878.74 [3135.05, 8901.84] (positive) |
| [AMZN](AMZN/summary.md) | 8 | -28252.37 [-44714.78, -15384.17] (negative) | -28785.69 [-45471.58, -15705.21] (negative) | 0/8 | -23.680 [-37.109, -14.608] | -5453.22 [-20289.87, 4599.38] (not established) |
| [GOOG](GOOG/summary.md) | 8 | -30373.56 [-51854.99, -17041.08] (negative) | -30863.41 [-52457.32, -17423.23] (negative) | 0/8 | -24.448 [-29.497, -19.524] | 5685.55 [-5209.46, 20170.82] (not established) |
| [INTC](INTC/summary.md) | 8 | -17496.22 [-24557.61, -9989.98] (negative) | -18239.56 [-25502.21, -10453.84] (negative) | 0/8 | -14.414 [-16.264, -12.244] | -1606.28 [-8437.45, 3500.76] (not established) |
| [MSFT](MSFT/summary.md) | 8 | -70235.16 [-88003.32, -51391.58] (negative) | -70628.92 [-88530.45, -51871.03] (negative) | 0/8 | -49.712 [-62.213, -38.916] | -4406.92 [-16904.97, 7414.65] (not established) |
