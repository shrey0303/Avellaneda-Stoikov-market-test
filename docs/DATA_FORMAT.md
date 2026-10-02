# LOBSTER data format — checked against the real sample

Every format assumption in the code lives in `src/lobreplay/lobster_format.py`.
On 8 Oct 2026 each one was checked against `LOBSTER_SampleFiles_ReadMe.txt`
(version of 01 Sept 2013, shipped with the sample) and against the five sample
files themselves: AAPL, AMZN, GOOG, INTC and MSFT for 21 June 2012, 10 levels.

## Files

`TICKER_YYYY-MM-DD_34200000_57600000_message_N.csv` and
`TICKER_YYYY-MM-DD_34200000_57600000_orderbook_N.csv`, same number of rows;
orderbook row *k* is the book **after** message *k*.

## Checklist

"Readme" means the readme states it. "Data" means the files confirm it:
`check` parses every row, and `validate` reproduces the orderbook file from
the messages, which fails at the first wrong assumption.

- [x] Message file has 6 columns: time, event type, order ID, size, price, direction. *Readme, data.*
- [x] Time is seconds after midnight, parsed to integer nanoseconds. *Readme, data.*
- [x] Event types: 1 submit, 2 partial cancel, 3 delete, 4 visible execution,
      5 hidden execution, 7 trading halt. *Readme.* The readme lists no type 6
      (cross trade) and the sample has none; the parser still accepts it.
- [x] Direction: 1 = buy limit order, −1 = sell limit order. For executions it is
      the side of the **resting** order (−1 execution = buyer-initiated trade). *Readme, data.*
- [x] Type 2 size = shares cancelled; type 3 size = shares remaining at deletion. *Data*
      (the readme does not say; a wrong reading would diverge at once).
- [x] Type 7 price column: −1 halted, 0 quoting, 1 resumed; direction −1. *Readme.*
      The sample has no halt.
- [x] Prices are dollars × 10,000. *Readme, data.*
- [x] Orderbook columns per level: ask price, ask size, bid price, bid size. *Readme, data.*
- [x] Empty levels: ask price 9999999999, bid price −9999999999, size 0. *Readme.*
- [x] Hidden executions (type 5) do not change the orderbook file. *Data.*
- [x] Orders resting before 09:30 have no submit message (handled as PREOPEN). *Data.*
- [x] Tick size is $0.01 (`TICK_SIZE = 100`) for every stock used. *Data:* all five trade above $1.
- [x] The session runs 09:30:00–16:00:00. *Readme (file names), data.*

## What the real files do that was not expected

1. **Some timestamps have more than nine decimals** (`36754.716797047004`,
   `34397.878728270996`) in AMZN, INTC and MSFT. They are a nanosecond value
   printed with floating-point noise. The parser rounds to the nearest
   nanosecond.

2. **The message file only carries events inside the top N levels.** The
   readme says so: the message file holds events "causing an update of the
   limit order book in the requested price range". A level that slides out of
   the top 10 can change or vanish with no message, and a level can rise into
   the top 10 without ever having been announced. No replay can rebuild those
   levels from the messages.

   So when a level **enters the top 10 from outside**, its size is taken from
   the orderbook file (`OrderBook.resync`). Every level that was already in
   view must still come out of the messages alone, and `validate` reports a
   divergence if it does not. `validate` prints how many levels were adopted
   this way. For such a level the total is exact but who holds it is a best
   guess; see `book.py`.

3. **Orders entered before the open appear in the book just after 09:30 with
   their old, lower order IDs**, behind orders that the file showed first, and
   trade ahead of them. Visible arrival order is therefore not time priority
   in the first moments of the session. The study leaves out the first minute.

4. **The exchange does not always follow visible first-in-first-out.** A few
   hundred times a day in INTC and MSFT, an order that arrived later trades
   before an untouched order that was already resting at the same price
   (probably reserve orders, whose refreshed part loses priority). Shadow
   validation counts these.
