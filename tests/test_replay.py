import pytest

from lobreplay.book import PREOPEN
from lobreplay.lobster_format import Direction, EventType
from lobreplay.parser import Message, Snapshot, find_files
from lobreplay.replay import replay, replay_files, seed_book
from lobreplay.synthetic import SyntheticConfig, generate

BUY, SELL = Direction.BUY, Direction.SELL


@pytest.mark.parametrize("seed,levels", [(0, 10), (1, 5), (2, 1), (3, 10)])
def test_synthetic_replays_with_zero_divergences(tmp_path, seed, levels):
    files = generate(SyntheticConfig(n_messages=5000, levels=levels, seed=seed), tmp_path)
    res = replay_files(files)
    assert res.ok, res.summary()
    assert res.messages == 5000
    assert res.crossed_states == 0
    assert res.event_counts[EventType.EXEC_VISIBLE] > 0


def _corrupt_line(path, index, fn):
    lines = path.read_text().splitlines()
    lines[index] = fn(lines[index])
    path.write_text("\n".join(lines) + "\n")


def test_corrupted_orderbook_row_is_caught_at_that_row(tmp_path):
    files = generate(SyntheticConfig(n_messages=2000, levels=5, seed=4), tmp_path)

    def bump_best_bid_size(line):
        cells = line.split(",")
        cells[3] = str(int(cells[3]) + 1)
        return ",".join(cells)

    _corrupt_line(files.orderbook_path, 1234, bump_best_bid_size)
    res = replay_files(files)
    assert not res.ok
    assert res.divergences[0].index == 1235
    assert "mismatch" in res.divergences[0].reason


def test_flipped_direction_is_caught(tmp_path):
    files = generate(SyntheticConfig(n_messages=2000, levels=5, seed=5), tmp_path)
    lines = files.message_path.read_text().splitlines()
    target = next(i for i, ln in enumerate(lines) if i > 500 and ln.split(",")[1] == "1")

    def flip(line):
        cells = line.split(",")
        cells[5] = str(-int(cells[5]))
        return ",".join(cells)

    _corrupt_line(files.message_path, target, flip)
    res = replay_files(files)
    assert not res.ok
    assert res.divergences[0].index == target + 1


def test_max_divergences_continues_past_first(tmp_path):
    files = generate(SyntheticConfig(n_messages=1000, levels=5, seed=6), tmp_path)

    def bump_best_ask_size(line):
        cells = line.split(",")
        cells[1] = str(int(cells[1]) + 7)
        return ",".join(cells)

    for idx in (100, 600):
        _corrupt_line(files.orderbook_path, idx, bump_best_ask_size)
    res = replay_files(files, max_divergences=10)
    assert [d.index for d in res.divergences] == [101, 601]


def test_length_mismatch_reported(tmp_path):
    files = generate(SyntheticConfig(n_messages=300, levels=5, seed=7), tmp_path)
    lines = files.orderbook_path.read_text().splitlines()
    files.orderbook_path.write_text("\n".join(lines[:-1]) + "\n")
    res = replay_files(find_files(tmp_path, "FAKE", 5))
    assert not res.ok
    assert "different lengths" in res.divergences[0].reason


# -- seeding: undoing message 1 ------------------------------------------------

ROW_AFTER = Snapshot(asks=((1010, 100), (1020, 200)), bids=((1000, 300), (990, 400)))


def test_seed_undoes_first_submit():
    first = Message(0, EventType.SUBMIT, 50, 100, 1000, BUY)
    book = seed_book(first, ROW_AFTER, levels=2)
    assert book.queue(BUY, 1000) == [(PREOPEN, 200)]
    book.apply(first)
    assert book.top(2) == ROW_AFTER


def test_seed_undoes_first_submit_that_created_a_level():
    first = Message(0, EventType.SUBMIT, 50, 300, 1000, BUY)
    book = seed_book(first, ROW_AFTER, levels=2)
    assert book.top(2).bids == ((990, 400),)
    # Row was full, so whatever sat below 990 before message 1 is unseen.
    assert book.bids.unseen_beyond == 990
    book.apply(first)
    assert book.top(2) == ROW_AFTER


def test_seed_undoes_first_delete_of_whole_level():
    first = Message(0, EventType.DELETE, 77, 50, 1005, SELL)
    book = seed_book(first, ROW_AFTER, levels=2)
    assert book.top(3).asks == ((1005, 50), (1010, 100), (1020, 200))
    book.apply(first)
    assert book.top(2) == ROW_AFTER


def test_seed_ignores_first_event_beyond_visible_depth():
    first = Message(0, EventType.CANCEL, 77, 50, 1100, SELL)
    book = seed_book(first, ROW_AFTER, levels=2)
    book.apply(first)
    assert book.unseen_reductions == 1
    assert book.top(2) == ROW_AFTER


def test_replay_accepts_in_memory_sequences():
    msgs = [
        Message(1, EventType.CROSS, 0, 100, 1000, BUY),
        Message(2, EventType.SUBMIT, 1, 100, 1005, BUY),
        Message(3, EventType.EXEC_VISIBLE, 1, 100, 1005, BUY),
    ]
    row0 = Snapshot(asks=((1010, 100),), bids=((1000, 100),))
    row1 = Snapshot(asks=((1010, 100),), bids=((1005, 100), (1000, 100)))
    res = replay(msgs, [row0, row1, row0], levels=2)
    assert res.ok, res.summary()
