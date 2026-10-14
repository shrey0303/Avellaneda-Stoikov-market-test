# lobreplay — Avellaneda–Stoikov on real order book data

Replays NASDAQ order-by-order data (LOBSTER) to test the Avellaneda–Stoikov
(2008) market-making formula against real order flow. The formula says what
buy and sell prices a market maker should quote. This project posts those
prices on a real trading day, works out which of them would have traded, and
compares the outcome with what the formula's own assumptions predict.

## Results

One trading day (21 June 2012), five NASDAQ stocks, 2,110,860 order book
messages. Calibrated and fitted on 09:31–12:45, tested on 12:45–15:59.
Brackets are 95% bootstrap intervals over six 30-minute windows. Full tables
are in `results/<TICKER>/report.md`, which `study` writes. `results/` is in
`.gitignore`, so the chart below shows only after `study` has been run, or
if `results/` is taken out of `.gitignore` and committed.

![Signal correlation by horizon, MSFT](results/MSFT/signal_decay.svg)

**1. The model's "a fill tells you nothing" assumption fails on real fills.**
Five seconds after one of our fills the mid price had moved against us, in
every stock. The model assumes zero.

| stock | spread | markout at 5 s (ticks per share) | fills behind it |
|---|---|---|---|
| AAPL | 17 ticks | −4.5 [−6.8, −2.2] | 142 |
| AMZN | 14 ticks | −7.9 [−11.4, −4.2] | 17 |
| GOOG | 31 ticks | −4.9 [−7.1, −1.8] | 14 |
| MSFT | 1 tick | −0.8 [−1.0, −0.5] | 4 |
| INTC | 1 tick | −0.75 [−1.5, 0.0], not established | 4 |

Inventory strategy, middle risk setting, conservative fill rule. The first
four hold under the optimistic rule too.

**2. The calibrated model overstates fills and profit.** In AAPL the replay
made $148 per window [24, 260] where the model world, with the same σ, A and
k, made $710; it got 24 fills per window where the model expected 49. In the
two one-tick-spread stocks the gap is far larger: under one fill per window
against 22 expected, because the model's spread is wider than the market's
and its quotes sit behind the best price. Part of this gap is the calibration
method and not the model; see limitation 12.

Every fill is booked at its own price. The $148 values the shares still held
when a window closes at the middle price, which no one can trade at. The
report therefore gives the profit three ways (AAPL, per window):

| how leftover shares are treated | profit |
|---|---|
| Not counted: completed buy-and-sell pairs only | $110 [9, 218] |
| Valued at the middle price | $148 [24, 260] |
| Traded out against the real book at the close | $137 [15, 245] |
| The model's forecast | $710 |

About 127 shares were left at a typical close, out of 2,220 traded per
window. In AMZN and GOOG the completed pairs made $2 to $5 per window and
closing the leftover at real prices takes the total to −$13 and +$3: nothing
distinguishable from zero.

**3. Queue imbalance predicts the next move in one-tick-spread stocks, out of
sample.** A line fitted in the morning, scored in the afternoon, on the mid
change over the next 5 seconds:

| stock | correlation | direction called |
|---|---|---|
| MSFT | 0.26 [0.25, 0.28] | 73% of 1,987 moves |
| INTC | 0.23 [0.19, 0.30] | 77% of 1,264 moves |
| AAPL, AMZN, GOOG | 0.04 to 0.06 | 54% to 57% |

This matches what was written down beforehand: stronger where the spread is
one tick. Order flow imbalance and trade imbalance were weaker than expected,
0.06 to 0.12 at best.

**4. The paper's "volatility is constant" assumption was off by a quarter.**
The paper fixes σ for the whole session. Measured the same way in both
halves of the day, afternoon volatility was 24% to 32% below the morning's
in all five stocks. The study still uses the morning's σ all afternoon,
because that is the model being tested. This comparison was made with a
separate script; the `study` report prints the morning figure only.

**What did not come out.**
- Leaning the quotes on the signal (Q8) showed no measurable gain in markout
  or P&L in any stock. A null result.
- The value of queue position (Q4) is not established. In AAPL and AMZN it
  is large under the optimistic fill rule and absent under the conservative
  one, which by this study's own rule is not a conclusion. In INTC and MSFT
  the strategy traded too rarely to say anything.
- One day per stock. Nothing here shows the numbers hold on another day.

### How far the replay can be trusted

| check | result |
|---|---|
| Book rebuilt from messages against the exchange's book, after every message | zero divergences, 2,110,860 messages, 5 stocks |
| Levels taken from the orderbook file instead (see below) | 42,855, about 2% of messages |
| Real orders shadowed: did we predict the message at which each finished filling? | 71,289 of 72,615 (98.2%) |
| ...per stock | AAPL 99.4%, AMZN 99.4%, GOOG 99.7%, INTC 97.3%, MSFT 97.5% |
| ...every fill at the same message and size | 71,113 of 72,615 (97.9%) |
| Mismatches with no cause tag | 58 (AAPL 3, GOOG 1, INTC 25, MSFT 29) |

The message file leaves out events beyond the tenth price level, so a level
that rises into the top ten from outside cannot be rebuilt from messages and
is taken from the orderbook file. Levels already in view are never taken from
it. `docs/DATA_FORMAT.md` has the details.

Shadow mismatches are tagged with a cause seen in the data: mostly an order
behind us trading while others were still ahead, and levels that had been
out of view. The 58 untagged ones are cases where, with nothing ahead of the
shadowed order, an order that arrived later traded first. A tag for that
(`later_order_traded_first`) is defined in `shadow.py`, but the check that
assigns it is not in the code at present, so `shadow` ends "UNEXPLAINED
MISMATCHES" for four of the five stocks and exits non-zero. The match rates
do not depend on the tags.

## Status

| Phase | What | Code | Done-criterion met |
|---|---|---|---|
| 1 | Parse LOBSTER message/orderbook files | `parser.py`, `lobster_format.py` | yes — all five files parse, format checked against the bundled readme |
| 2 | Rebuild the book, compare after every message | `book.py`, `replay.py` | yes — zero divergences, five stocks, full day |
| 3 | Queue tracker, conservative + optimistic fill rules | `queue_tracker.py` | yes (unit tests) |
| 4 | Shadow validation against real orders' fills | `shadow.py` | partly — 98.2% predicted; 58 mismatches have no cause tag (see above) |
| 5 | Calibrate σ, A, k | `calibration.py` | yes |
| 6 | Strategy runs and model-world comparison, Q1–Q6 | `as_model.py`, `strategy.py`, `model_world.py`, `stats.py`, `study.py` | yes — Q1–Q3 answered; Q4 and Q5 not established |
| 7 | Report, plots, limitations | `study.py`, `plots.py`, this file | yes |
| 8 | Predictive signals and a signal-leaning strategy, Q7–Q8 | `signals.py`, `strategy.py`, `study.py` | yes — Q7 answered; Q8 is a null |
| 9 | Real-data run and write-up | `results/`, this file | yes — run on 8 Oct 2026, re-run on 9 Oct 2026 with identical numbers |
| 10 | Recorder, freeze and daily scoring for the track record, Q9 | `recorder.py`, `track.py` | yes (tests, and a 14-second live recording) |
| 11 | Run the track record | — | no — needs weeks of recording, not started; nothing is recorded or frozen |

156 unit tests pass. The folder is not yet a git repository.

`make-synthetic` writes placeholder files in the LOBSTER format. Their order
flow is random: **nothing measured on them says anything about markets.**
They exist to prove the pipeline runs and to test it. Queue imbalance does
predict the next move in these files, but only because a thin queue is
mechanically the next to empty; that says nothing about real order flow.

## Setup

```
python -m venv .venv
.venv\Scripts\python -m pip install -e ".[dev]"
.venv\Scripts\python -m pytest -q
```

Python 3.10 or later. No third-party packages are needed to run the study;
`pytest` is needed only for the tests.

## Reproducing the study

Download the level-10 samples from
<https://data.lobsterdata.com/info/DataSamples.php> and unzip them into
`data/lobster/` (any folder works; pass it as `--dir`). The data is not
committed: `.gitignore` excludes `data/`.

```
python -m lobreplay check    --dir data/lobster --ticker AAPL AMZN GOOG INTC MSFT
python -m lobreplay validate --dir data/lobster --ticker AAPL AMZN GOOG INTC MSFT
python -m lobreplay shadow   --dir data/lobster --ticker AAPL AMZN GOOG INTC MSFT
python -m lobreplay study    --dir data/lobster --ticker AAPL AMZN GOOG INTC MSFT --out results
```

Run them in that order. All four take about 15 minutes together.
`docs/DATA_FORMAT.md` records how the format was checked against the readme
that comes with the sample files.

| Command | Phase | Passes when | On the real sample |
|---|---|---|---|
| `check` | 1 | every row parses and the two files line up | passes |
| `validate` | 2 | zero divergences from the orderbook file | passes |
| `shadow` | 4 | every mismatch between predicted and actual fills carries a cause tag | fails for AAPL, GOOG, INTC, MSFT on the 58 untagged mismatches |
| `study` | 5–8 | calibration is usable and the strategies were traded | passes, no problems reported |

`study` writes, for each ticker, `results/<TICKER>/report.md` (a three-line
headline, then the answers to Q1–Q8 with tables, including replay profit
three ways and shares traded per window), `results.json` (every number
behind them) and five SVG plots. With more than one ticker it also writes
`results/summary.md`, the cross-stock table for Q5. The same command with
the same `--seed` gives the same numbers.

To try the pipeline without real data:

```
python -m lobreplay make-synthetic --out data/synthetic --messages 400000
python -m lobreplay shadow --dir data/synthetic --ticker FAKE
python -m lobreplay study  --dir data/synthetic --ticker FAKE --out results
```

A 400,000-message day takes about three minutes for `study`.

## Track record: one frozen signal, many later days

The LOBSTER study scores each signal on one afternoon. One afternoon can look
good by luck. The track record fits a signal once, freezes it, and scores it
untouched on every later day. It uses Binance BTCUSDT recorded live, because
that is the only free source of new days. It is Level 2 data, so only the
prediction is scored; no strategy is traded on it.

```
python -m lobreplay record                # every day; one row a second into data/crypto/BTCUSDT/<UTC date>.csv
python -m lobreplay freeze                # once, after about a week; writes frozen/BTCUSDT.json
git add frozen/BTCUSDT.json && git commit -m "Freeze signal" && git push
python -m lobreplay track                 # any time after; writes results/track/BTCUSDT/track.md
```

- `record` runs for 24 hours unless `--hours` says otherwise. Stop it with
  Ctrl+C; rows already written are kept. A failed request loses that second
  and nothing else.
- `freeze` fits the three signals on every finished day on disk, picks the
  one with the strongest correlation at the 5-second horizon, and writes it
  with a SHA-256 fingerprint. It refuses to overwrite an existing file.
- **Push the frozen file before the next day starts.** GitHub's push time is
  the evidence that the signal existed before the days it is scored on.
- `track` scores only days that start after the freeze. Fitting days, the
  freeze day and today are listed and left out, and so is any day with less
  than an hour of usable data. It refuses to run if the frozen file was
  edited.
- The pass mark is written into the frozen file: at least 20 scored days, the
  95% interval of the mean daily correlation excludes zero on the frozen
  side, and a sign test gives p < 0.05. Otherwise the report says "did not
  hold up".
- If the signal fails, that is the result. A different signal needs a new
  frozen file and a new set of days.

## How the study is run

- **Split.** σ, A and k are calibrated on 09:31–12:45. The strategies trade
  12:45–15:59. Calibration stops reading the file at 12:45. The first and last
  minute of the session are left out.
- **σ** comes from the mid price on a one-second grid, at the 60-second
  horizon by default (`--sigma-horizon`). The report shows the variance-ratio
  curve so that the choice can be judged. It is measured once, on the
  morning, and held fixed all afternoon, as the paper assumes.
- **A and k** come from probes: a hypothetical 100-share order every 5 seconds
  on each side, 0–5 ticks behind the touch, left for up to 60 seconds.
  λ(δ) = A·e^(−kδ) is fitted by Poisson maximum likelihood, separately under
  each fill rule.
- **Strategies.** Inventory (A–S reservation price) and symmetric (same
  spread, centred on the mid, blind to inventory). Three risk-aversion
  settings, chosen so that one lot of inventory moves the reservation price by
  1, 2 or 4 ticks at the start of a window. One lot per side. Requote every
  second and after each fill.
- **Queue modes.** Sticky keeps an order whose price has not changed.
  Requeue cancels and re-posts at every requote, which sends it to the back.
  The difference is Q4.
- **Sessions.** The afternoon is cut into 30-minute windows
  (`--window-minutes`). Each starts flat. Every figure is a mean over windows
  with a 95% bootstrap interval.
- **Profit.** Every fill is booked at its own price. Shares still held when
  a window closes have no trade price, so profit is reported three ways:
  completed buy-and-sell pairs only (first in, first out); leftover valued
  at the closing mid (the figure used in Q1–Q4 and Q8); and leftover traded
  out against the real book at the close, level by level.
- **Model world.** The same σ, A, k and γ in a simulator where the model's
  assumptions hold exactly, with continuous quotes. This is what the replay is
  compared against in Q1 and Q3.
- **Both fill rules, always.** Each rule is carried through calibration and
  trading on its own. Q6 lists every finding under both and marks any that
  does not hold under both as not a conclusion.
- **Signals (Q7).** Queue imbalance, order flow imbalance and trade imbalance
  are sampled once a second. For each signal and each horizon (1, 5, 10, 30,
  60 s) a straight line is fitted on the morning: mid change over the next
  *h* seconds against the signal. That line is scored on the afternoon:
  correlation, R² against predicting no change, and how often it calls the
  direction. A morning sample is dropped if its target reaches past 12:45.
  Intervals are bootstrapped over windows, because one-second samples at
  longer horizons overlap.
- **Signal strategy (Q8).** The signal with the strongest morning correlation
  at the 5-second horizon is chosen. The signal strategy is the inventory
  strategy with both quotes shifted by slope × signal. It is compared with
  the plain inventory strategy on the same windows, under both fill rules.
  With a slope of zero it reproduces the inventory strategy exactly (tested).

## Limitations

Say these before anyone asks.

1. **No market impact.** A hypothetical order never changes the replay. That
   is acceptable for one round lot and wrong for size.
2. **No latency.** Quotes react instantly.
3. **No fees or rebates.** P&L is gross.
4. **Hidden liquidity is handled by assumption.** Hidden executions neither
   shrink the queue ahead of us nor fill us.
5. **One day, five stocks, 2012, US market.** Indicative at best.
6. **Fill rules are bounds, not truth.** The conservative rule understates
   fills and the optimistic rule overstates them.
7. **An order the market moves through is filled late.** If a real order
   arrives at a price that would have traded with ours, the replay fills us
   only at the next real execution. The report counts how often a requote
   finds our order in that state ("overtaken").
8. **Tick rounding separates replay from model.** Replay quotes sit on the
   one-cent grid and the model world's do not. In a stock that trades at a
   one-tick spread, part of any gap in Q1 is this rounding and not adverse
   selection.
9. **The model itself** has a fixed horizon and constant parameters.
   The signals are the textbook ones, fitted with a straight line on one
   morning; one day cannot show that a signal is stable across days, and a
   signal that predicts the price is not a profit once fees and latency are
   counted.
10. **The track record is a different market and a coarser feed.** It is
    BTCUSDT on Binance at one snapshot a second, not NASDAQ order by order.
    It shows whether the method holds up over time; it does not confirm the
    LOBSTER numbers. Days are not fully independent, so the sign test is
    generous.
11. **Levels beyond the tenth are invisible.** The message file omits them,
    so when one rises into view its size comes from the orderbook file and
    the identity of its orders is a best guess. About 2% of messages bring
    such a level in.
12. **The probes and the strategy do not rest the same way.** A and k are
    measured from orders left at a fixed price for up to 60 seconds, which
    fill when the price comes to them. The strategy moves its quotes with
    the mid every second, so it backs away as the price approaches. The
    model's fill forecast therefore starts too high, and part of the gap in
    result 2 is this and not adverse selection. It was not re-tuned after
    seeing the results.
13. **Few fills in the one-tick-spread stocks.** INTC and MSFT gave 2 to 7
    fills per run over the afternoon. Their markouts and every strategy
    comparison in those two stocks rest on that.
14. **Volatility is measured once.** σ comes from the morning and is held
    fixed, as the paper assumes. The afternoon was 24–32% calmer. In AAPL
    this moves the quotes little (about 2 cents of the 31-cent spread comes
    from the volatility term), but the model world also runs on the
    morning's σ, and the effect of that on its forecast was not measured.
15. **Leftover shares are closed against a frozen book.** The "closed at
    real prices" profit uses the book as it stands at the instant the
    window ends and does not model the price moving while we trade out.
16. **`as_model.py` and the intensity fit were written for this
    repository.** An earlier version of the plan spoke of reusing them from
    a separate simulation project; no such code is here. What is checked
    here: the formulas against the paper's equations, and the model world
    against the paper's own table for its parameters (`tests/test_as_model.py`).

## Library use

Queue tracking is also a library API. For each message call
`tracker.observe(msg, k)`, then `book.apply(msg)`, then `tracker.settle()`;
post hypothetical orders between messages with `tracker.post(...)`.
`session.MarketReplay` runs that loop for you.
