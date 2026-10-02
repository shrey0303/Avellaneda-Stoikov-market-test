import pytest

from lobreplay.lobster_format import DUMMY_ASK_PRICE, DUMMY_BID_PRICE, Direction, EventType
from lobreplay.parser import (
    ParseError,
    check_files,
    find_files,
    format_time_ns,
    parse_message_row,
    parse_orderbook_row,
    parse_time_ns,
)
from lobreplay.synthetic import SyntheticConfig, generate


def test_time_parsed_exactly_without_float():
    assert parse_time_ns("34200.004241176") == 34_200_004_241_176
    assert parse_time_ns("34200.5") == 34_200_500_000_000
    assert parse_time_ns("34200") == 34_200_000_000_000
    assert format_time_ns(34_200_004_241_176) == "34200.004241176"


def test_times_with_more_than_nine_decimals_round_to_the_nanosecond():
    # both forms occur in the real sample files
    assert parse_time_ns("36754.716797047004") == 36_754_716_797_047
    assert parse_time_ns("34397.878728270996") == 34_397_878_728_271
    assert parse_time_ns("34200.9999999995") == 34_201_000_000_000


@pytest.mark.parametrize("bad", ["", "-1.0", "3a.0", "1.2.3"])
def test_bad_time_rejected(bad):
    with pytest.raises(ParseError):
        parse_time_ns(bad)


def test_message_row():
    m = parse_message_row(["34200.017459617", "1", "16113575", "18", "5853300", "1"], 1)
    assert m.event_type is EventType.SUBMIT
    assert m.direction is Direction.BUY
    assert (m.order_id, m.size, m.price) == (16113575, 18, 5853300)


@pytest.mark.parametrize(
    "row",
    [
        ["34200.0", "9", "1", "1", "1", "1"],       # unknown event type
        ["34200.0", "1", "1", "1", "1", "0"],       # bad direction
        ["34200.0", "1", "1", "1", "1"],            # too few columns
        ["34200.0", "1", "1", "1.5", "1", "1"],     # non-integer size
    ],
)
def test_bad_message_rows(row):
    with pytest.raises(ParseError):
        parse_message_row(row, 7)


def test_orderbook_row_drops_dummy_levels():
    row = [5860000, 100, 5850000, 200, DUMMY_ASK_PRICE, 0, 5849900, 300]
    snap = parse_orderbook_row([str(v) for v in row], levels=2, line_no=1)
    assert snap.asks == ((5860000, 100),)
    assert snap.bids == ((5850000, 200), (5849900, 300))


def test_orderbook_row_rejects_level_after_gap():
    row = [DUMMY_ASK_PRICE, 0, DUMMY_BID_PRICE, 0, 5860000, 100, 5850000, 200]
    with pytest.raises(ParseError):
        parse_orderbook_row([str(v) for v in row], levels=2, line_no=1)


def test_sanity_check_on_synthetic(tmp_path):
    files = generate(SyntheticConfig(n_messages=3000, levels=5, seed=3), tmp_path)
    assert find_files(tmp_path, "FAKE", 5) == files
    rep = check_files(files)
    assert rep.ok, rep.summary()
    assert rep.message_rows == rep.orderbook_rows == 3000
    for et in EventType:
        assert rep.event_counts[et] > 0, et


def test_sanity_check_catches_backwards_time_and_row_mismatch(tmp_path):
    files = generate(SyntheticConfig(n_messages=200, levels=5, seed=1), tmp_path)
    lines = files.message_path.read_text().splitlines()
    lines[10], lines[11] = lines[11], lines[10]
    files.message_path.write_text("\n".join(lines) + "\n")
    ob = files.orderbook_path.read_text().splitlines()
    files.orderbook_path.write_text("\n".join(ob[:-1]) + "\n")

    rep = check_files(files)
    text = "\n".join(rep.problems)
    assert "time goes backwards" in text or lines[10].split(",")[0] == lines[11].split(",")[0]
    assert "row count mismatch" in text
