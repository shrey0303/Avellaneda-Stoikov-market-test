import pytest

from lobreplay.lobster_format import Direction, EventType
from lobreplay.parser import LobsterFiles, Message, format_time_ns, iter_messages
from lobreplay.queue_tracker import FillRule
from lobreplay.shadow import EXACT, LATE, TAG_ANOMALY, select_orders, shadow_validate
from lobreplay.synthetic import SyntheticConfig, generate

BUY, SELL = Direction.BUY, Direction.SELL
CONS, OPT = FillRule.CONSERVATIVE, FillRule.OPTIMISTIC


def msg(et, oid, size, price, side, t=0):
    return Message(t, EventType(et), oid, size, price, side)


def write_files(tmp_path, messages, levels=2) -> LobsterFiles:
    """Message file plus a one-row orderbook file (only row 1 is read, to seed the book)."""
    mp = tmp_path / "X_2012-06-21_34200000_57600000_message_2.csv"
    op = tmp_path / "X_2012-06-21_34200000_57600000_orderbook_2.csv"
    with open(mp, "w", newline="") as fh:
        for i, m in enumerate(messages):
            t = m.time_ns or 34_200_000_000_000 + i
            fh.write(f"{format_time_ns(t)},{int(m.event_type)},{m.order_id},{m.size},{m.price},{int(m.direction)}\n")
    # Pre-open book: 100 on each side at 1000/1010, before the opening cross in message 1.
    op.write_text("1010,100,1000,100,9999999999,0,-9999999999,0\n")
    return LobsterFiles("X", "2012-06-21", levels, mp, op)


CROSS = msg(6, 0, 100, 1005, BUY)


def test_select_keeps_only_unmodified_fully_executed_orders():
    messages = [
        msg(1, 1, 100, 1000, BUY), msg(4, 1, 100, 1000, BUY),                          # filled in one go
        msg(1, 2, 300, 1000, BUY), msg(4, 2, 100, 1000, BUY), msg(4, 2, 200, 1000, BUY),  # filled in two
        msg(1, 3, 100, 1000, BUY), msg(2, 3, 40, 1000, BUY), msg(4, 3, 60, 1000, BUY),  # partially cancelled
        msg(1, 4, 100, 1000, BUY), msg(4, 4, 50, 1000, BUY),                           # never completed
        msg(1, 5, 100, 1000, BUY), msg(3, 5, 100, 1000, BUY),                          # deleted
        msg(4, 99, 100, 1000, BUY),                                                    # pre-open order
    ]
    picked = select_orders(messages)
    assert [o.order_id for o in picked] == [1, 2]
    assert picked[1].execs == [(4, 100), (5, 200)]


def test_shadow_behind_preopen_and_real_queue_is_exact(tmp_path):
    files = write_files(tmp_path, [
        CROSS,
        msg(1, 1, 200, 1000, BUY),      # ahead of the order we shadow
        msg(1, 2, 300, 1000, BUY),      # <- shadowed
        msg(1, 3, 100, 1000, BUY),      # behind it
        msg(4, 77, 100, 1000, BUY),     # pre-open liquidity trades
        msg(4, 1, 200, 1000, BUY),
        msg(4, 2, 120, 1000, BUY),      # partial fill of the real order
        msg(4, 2, 180, 1000, BUY),      # completion
        msg(4, 3, 100, 1000, BUY),
    ])
    rep = shadow_validate(files)
    by_id = {o.real.order_id: o for o in rep.outcomes[CONS]}
    assert by_id[2].outcome == EXACT and by_id[2].predicted == [(7, 120), (8, 180)]
    assert all(o.outcome == EXACT for rule in FillRule for o in rep.outcomes[rule])
    assert rep.ok and rep.match_rate(CONS) == 1.0


def test_queue_jump_is_reported_late_and_tagged(tmp_path):
    files = write_files(tmp_path, [
        CROSS,
        msg(1, 1, 200, 1000, BUY),      # ahead, and it never trades
        msg(1, 2, 100, 1000, BUY),      # <- shadowed; fills while order 1 still rests
        msg(4, 2, 100, 1000, BUY),
        msg(4, 77, 100, 1000, BUY),
    ])
    rep = shadow_validate(files)
    (o,) = [o for o in rep.outcomes[CONS] if o.real.order_id == 2]
    assert o.outcome != EXACT and TAG_ANOMALY in o.tags
    assert rep.ok                       # explained, so not a failure
    assert rep.match_rate(CONS) < 1.0


def test_late_prediction_without_a_cause_is_unexplained(tmp_path, monkeypatch):
    files = write_files(tmp_path, [CROSS, msg(1, 2, 100, 1000, BUY), msg(4, 77, 100, 1000, BUY), msg(4, 2, 100, 1000, BUY)])
    import lobreplay.shadow as shadow

    real_select = shadow.select_orders

    def lying_select(messages, max_orders=None, seed=0):
        picked = real_select(messages, max_orders, seed)
        picked[0].execs = [(3, 100)]    # pretend the real order filled a message earlier than it did
        picked[0].exec_ns -= 1
        return picked

    monkeypatch.setattr(shadow, "select_orders", lying_select)
    rep = shadow.shadow_validate(files)
    assert rep.outcomes[CONS][0].outcome == LATE
    assert not rep.ok and rep.unexplained(CONS)


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_synthetic_fifo_data_is_predicted_exactly(tmp_path, seed):
    files = generate(SyntheticConfig(n_messages=6000, levels=10, seed=seed), tmp_path)
    rep = shadow_validate(files)
    assert rep.candidates > 100
    for rule in FillRule:
        assert rep.counts(rule) == {EXACT: rep.candidates}
    assert rep.ok


def test_max_orders_samples_reproducibly(tmp_path):
    files = generate(SyntheticConfig(n_messages=3000, levels=10, seed=3), tmp_path)
    a = select_orders(iter_messages(files.message_path), max_orders=25, seed=1)
    b = select_orders(iter_messages(files.message_path), max_orders=25, seed=1)
    assert len(a) == 25 and [o.order_id for o in a] == [o.order_id for o in b]
    assert [o.submit_index for o in a] == sorted(o.submit_index for o in a)
