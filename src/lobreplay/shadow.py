"""Phase 4: shadow validation (approach document §5.3).

Real orders that rested and then filled are a free answer key. For each one we
post a hypothetical order at the same price, at the same moment, behind the
same queue, and ask the queue tracker when it fills. Then we compare with when
the real order actually filled.

Two passes over the message file:
  1. pick the real orders: submitted in the file, never cancelled or deleted,
     executed in full by visible executions;
  2. replay, posting each shadow just BEFORE its real order's SUBMIT message,
     so the queue snapshot is exactly what the real order joined behind. The
     real order then arrives "behind" the shadow, and its executions are the
     fills the tracker should hand to us.

A mismatch is not automatically a tracker bug. Each one is tagged with what
could explain it; anything left untagged is "unexplained" and needs a look.
"""

from __future__ import annotations

import random
from collections import Counter
from dataclasses import dataclass, field

from .lobster_format import Direction, EventType
from .parser import LobsterFiles, Message, format_time_ns, iter_messages
from .queue_tracker import FillRule, HypotheticalOrder, QuoteError
from .session import MarketReplay


@dataclass
class RealOrder:
    order_id: int
    side: Direction
    price: int
    size: int
    submit_index: int
    submit_ns: int
    execs: list[tuple[int, int]] = field(default_factory=list)  # (message index, size)
    exec_ns: int = 0          # time of the last execution
    modified: bool = False    # partially cancelled or deleted

    @property
    def executed(self) -> int:
        return sum(size for _, size in self.execs)


def select_orders(messages, max_orders: int | None = None, seed: int = 0) -> list[RealOrder]:
    """Real orders that were fully executed and never modified, in submit order."""
    seen: dict[int, RealOrder] = {}
    for k, m in enumerate(messages, start=1):
        et = m.event_type
        if et == EventType.SUBMIT:
            seen[m.order_id] = RealOrder(m.order_id, m.direction, m.price, m.size, k, m.time_ns)
            continue
        o = seen.get(m.order_id)
        if o is None:
            continue  # pre-open order, or a non-book event with order id 0
        if et == EventType.EXEC_VISIBLE:
            o.execs.append((k, m.size))
            o.exec_ns = m.time_ns
        elif et in (EventType.CANCEL, EventType.DELETE):
            o.modified = True
    picked = [o for o in seen.values() if not o.modified and o.executed == o.size]
    if max_orders is not None and len(picked) > max_orders:
        picked = sorted(random.Random(seed).sample(picked, max_orders), key=lambda o: o.submit_index)
    return picked


# Outcome of one shadow under one rule.
EXACT = "exact"          # every fill at the same message, same size
EARLY = "early"          # we predicted completion before the real order completed
LATE = "late"            # ...after
NEVER = "never"          # we never completed
PARTIAL = "partial_differs"  # completed at the same message, but the partial fills differ
REJECTED = "rejected"    # could not be posted (would lock or cross)

# Possible explanations for a mismatch.
TAG_UNSEEN = "unseen_level"            # level was beyond the visible depth at the open: queue ahead unknown
TAG_ANOMALY = "priority_anomaly"       # an order behind us traded while orders were ahead (not strict FIFO)
TAG_HIDDEN = "hidden_at_price"         # a hidden execution printed at our price while we rested
TAG_SAME_TIME = "same_timestamp"       # predicted and actual completion share a timestamp
TAG_TRADE_THROUGH = "trade_through"    # we were filled by a trade at a worse price than ours
TAG_VACATED = "vacated_rule"           # filled by the optimistic vacated-level rule
TAG_OLDER = "older_order_joined"       # an order with a lower ID (entered earlier, e.g. released at the open)
#                                        appeared at our price after us; it has time priority over us
TAG_LEFT_VIEW = "level_left_view"      # our level was outside the top N at some point: who rests there is a guess
TAG_LATER_FIRST = "later_order_traded_first"  # with nothing ahead of us, an order that arrived after the real one
#                                        traded at our price before the real one was done: the exchange did not
#                                        follow visible first-in-first-out (e.g. a reserve order's refreshed part)
UNEXPLAINED = "unexplained"


@dataclass
class ShadowOutcome:
    real: RealOrder
    rule: FillRule
    outcome: str
    predicted: list[tuple[int, int]]
    tags: tuple[str, ...] = ()

    def describe(self) -> str:
        r = self.real
        return (
            f"order {r.order_id} {r.side.name} {r.size}@{r.price} submitted at message {r.submit_index} "
            f"(t={format_time_ns(r.submit_ns)}): {self.outcome} [{', '.join(self.tags) or '-'}] "
            f"actual={r.execs} predicted={self.predicted}"
        )


@dataclass
class ShadowReport:
    candidates: int
    outcomes: dict[FillRule, list[ShadowOutcome]]

    def counts(self, rule: FillRule) -> Counter:
        return Counter(o.outcome for o in self.outcomes[rule])

    def match_rate(self, rule: FillRule) -> float:
        """Share of shadows whose completion message was predicted exactly."""
        outs = [o for o in self.outcomes[rule] if o.outcome != REJECTED]
        if not outs:
            return float("nan")
        return sum(o.outcome in (EXACT, PARTIAL) for o in outs) / len(outs)

    def mismatches(self, rule: FillRule) -> list[ShadowOutcome]:
        return [o for o in self.outcomes[rule] if o.outcome != EXACT]

    def unexplained(self, rule: FillRule) -> list[ShadowOutcome]:
        return [o for o in self.mismatches(rule) if UNEXPLAINED in o.tags]

    @property
    def ok(self) -> bool:
        """Phase 4 done-criterion: every mismatch has an explanation, under both rules."""
        return self.candidates > 0 and not any(self.unexplained(rule) for rule in FillRule)

    def summary(self, show: int = 10) -> str:
        lines = [f"real orders shadowed: {self.candidates}"]
        for rule in FillRule:
            c = self.counts(rule)
            lines.append(f"{rule.value}:")
            lines.append(f"  completion message predicted: {self.match_rate(rule):.2%}")
            lines.append("  outcomes: " + ", ".join(f"{name}={n}" for name, n in sorted(c.items())))
            tags = Counter(t for o in self.mismatches(rule) for t in o.tags)
            if tags:
                lines.append("  mismatch explanations: " + ", ".join(f"{t}={n}" for t, n in sorted(tags.items())))
            for o in self.unexplained(rule)[:show]:
                lines.append("    " + o.describe())
        if not self.candidates:
            lines.append("RESULT: NOTHING TO SHADOW")
        else:
            lines.append("RESULT: ALL MISMATCHES EXPLAINED" if self.ok else "RESULT: UNEXPLAINED MISMATCHES")
        return "\n".join(lines)


def shadow_validate(files: LobsterFiles, max_orders: int | None = None, seed: int = 0) -> ShadowReport:
    picked = select_orders(iter_messages(files.message_path), max_orders, seed)
    by_submit = {o.submit_index: o for o in picked}

    replay = MarketReplay(files)
    trackers = {rule: replay.tracker(rule) for rule in FillRule}
    shadows: dict[int, dict[FillRule, HypotheticalOrder | None]] = {}
    unseen: set[int] = set()
    resting: dict[tuple[Direction, int], set[int]] = {}   # (side, price) -> real order ids being shadowed
    hidden: set[int] = set()
    older: set[int] = set()
    left_view: set[int] = set()

    def post_shadow(k: int, m: Message) -> None:
        real = by_submit.get(k)
        if real is None:
            return
        if replay.book.side(real.side).is_unseen(real.price):
            unseen.add(real.order_id)
        level = replay.book.side(real.side).level(real.price)
        if level is not None and level.uncertain:
            left_view.add(real.order_id)
        posted: dict[FillRule, HypotheticalOrder | None] = {}
        for rule, tr in trackers.items():
            try:
                posted[rule] = tr.post(real.side, real.price, real.size, k - 1, m.time_ns)
            except QuoteError:
                posted[rule] = None
        shadows[real.order_id] = posted
        resting.setdefault((real.side, real.price), set()).add(real.order_id)

    replay.before.append(post_shadow)
    by_id = {o.order_id: o for o in picked}
    for k, m in replay:
        for key in replay.book.last_adopted:
            left_view.update(resting.get(key, ()))
        if m.event_type == EventType.EXEC_HIDDEN:
            hidden.update(resting.get((m.direction, m.price), ()))
        elif m.event_type == EventType.SUBMIT:
            older.update(i for i in resting.get((m.direction, m.price), ()) if i > m.order_id)
        elif m.event_type == EventType.EXEC_VISIBLE:
            real = by_id.get(m.order_id)
            if real is not None and k == real.execs[-1][0]:
                resting[(real.side, real.price)].discard(real.order_id)  # the real order is done

    outcomes: dict[FillRule, list[ShadowOutcome]] = {rule: [] for rule in FillRule}
    for real in picked:
        for rule in FillRule:
            extra = [tag for tag, ids in ((TAG_OLDER, older), (TAG_LEFT_VIEW, left_view)) if real.order_id in ids]
            outcomes[rule].append(_judge(real, rule, shadows[real.order_id][rule], real.order_id in unseen,
                                         real.order_id in hidden, extra))
    return ShadowReport(len(picked), outcomes)


def _judge(real: RealOrder, rule: FillRule, shadow: HypotheticalOrder | None, unseen: bool, hidden: bool,
           extra: list[str] = ()) -> ShadowOutcome:
    if shadow is None:
        return ShadowOutcome(real, rule, REJECTED, [], (UNEXPLAINED,))
    predicted = [(f.index, f.size) for f in shadow.fills]
    if predicted == real.execs:
        return ShadowOutcome(real, rule, EXACT, predicted)

    actual_done = real.execs[-1][0]
    if shadow.remaining:
        outcome = NEVER
    elif predicted[-1][0] == actual_done:
        outcome = PARTIAL
    else:
        outcome = EARLY if predicted[-1][0] < actual_done else LATE

    tags = list(extra)
    if unseen:
        tags.append(TAG_UNSEEN)
    if shadow.anomalies:
        tags.append(TAG_ANOMALY)
    if hidden:
        tags.append(TAG_HIDDEN)
    reasons = {f.reason.value for f in shadow.fills}
    if "trade_through" in reasons:
        tags.append(TAG_TRADE_THROUGH)
    if "vacated" in reasons:
        tags.append(TAG_VACATED)
    if shadow.fills and shadow.fills[-1].time_ns == real.exec_ns and not shadow.remaining:
        tags.append(TAG_SAME_TIME)
    return ShadowOutcome(real, rule, outcome, predicted, tuple(tags) or (UNEXPLAINED,))
