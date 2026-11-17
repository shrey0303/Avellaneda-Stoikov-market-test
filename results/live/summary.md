# Live track record: Avellaneda-Stoikov on real IEX data

Updated after every US trading day by the `live` GitHub Actions workflow. Each stock has its own page with every setting and every day.

- IEX only: Alpaca's free plan carries the IEX exchange's own quotes and trades, a few percent of US volume. The strategy is simulated as if it quoted on IEX alone.
- No queue position: IEX data has the best bid and ask, not the order-by-order book. The conservative rule fills a quote only on a trade through its price; the optimistic rule also on a trade at it. The truth lies between the two.
- Calibrated on earlier days only (up to five). The first day of each stock only calibrates.
- P&L is in dollars, one lot of 100 shares per side, 30-minute windows that each start and end flat at the mid, before fees and rebates.

Inventory strategy at 2 ticks of risk aversion. Mean over days with a 95% bootstrap interval over days.

| stock | days traded | daily P&L, conservative ($) | daily P&L, optimistic ($) | positive days (cons.) | 5 s markout (ticks, cons.) | inventory minus symmetric (cons., $/day) |
|---|---|---|---|---|---|---|
| [AAPL](AAPL/summary.md) | 31 | -43174.78 [-54468.34, -32951.96] (negative) | -43857.36 [-55295.60, -33615.69] (negative) | 0/31 | -23.774 [-26.579, -21.207] | -4794.52 [-13067.86, 1222.10] (not established) |
| [AMZN](AMZN/summary.md) | 31 | -38793.64 [-49309.88, -29390.10] (negative) | -39219.98 [-49764.10, -29727.18] (negative) | 0/31 | -20.141 [-24.313, -16.934] | 727.66 [-7860.02, 9678.49] (not established) |
| [GOOG](GOOG/summary.md) | 31 | -35304.81 [-46315.90, -26063.29] (negative) | -35634.93 [-46649.60, -26368.12] (negative) | 0/31 | -27.883 [-31.663, -24.299] | 4188.70 [-4110.51, 15120.66] (not established) |
| [INTC](INTC/summary.md) | 31 | -8765.47 [-11855.27, -5898.44] (negative) | -8811.22 [-12049.22, -5840.39] (negative) | 0/31 | -8.336 [-10.142, -6.566] | 597.61 [-1746.40, 2758.25] (not established) |
| [MSFT](MSFT/summary.md) | 31 | -123614.60 [-152805.87, -98384.95] (negative) | -124223.44 [-153538.19, -98889.94] (negative) | 0/31 | -60.709 [-72.768, -50.807] | 5048.87 [-3560.37, 13993.05] (not established) |
