import json
import xml.etree.ElementTree as ET

import pytest

from lobreplay.calibration import CalibrationConfig
from lobreplay.cli import main
from lobreplay.plots import Series, line_chart
from lobreplay.stats import Estimate
from lobreplay.strategy import StrategyConfig
from lobreplay.study import StudyConfig, _across_rules, render_report, render_summary, run_study, write_outputs
from lobreplay.synthetic import SyntheticConfig, generate

FAST = StudyConfig(
    penalty_ticks=(1.0, 2.0),
    calibration=CalibrationConfig(probe_every_s=10.0),
    strategy=StrategyConfig(requote_s=5.0),
    model_paths=20,
    model_dt=5.0,
    n_boot=200,
)


@pytest.fixture(scope="module")
def study(tmp_path_factory):
    files = generate(SyntheticConfig(n_messages=12_000, levels=10, seed=11), tmp_path_factory.mktemp("study"))
    return files, run_study(files, FAST)


def test_study_answers_every_question_under_both_rules(study):
    _, res = study
    assert res["problems"] == [] and res["synthetic"]
    q = res["questions"]
    assert set(q) == {"Q1_model_vs_replay_pnl", "Q2_markouts", "Q3_pnl_decomposition", "Q4_queue_value",
                      "Q5_tick_size", "Q6_fill_rule_sensitivity", "inventory_vs_symmetric",
                      "Q7_signal_prediction", "Q8_signal_skew"}
    for name in ("Q1_model_vs_replay_pnl", "Q3_pnl_decomposition", "Q4_queue_value"):
        assert {r["rule"] for r in q[name]} == {"conservative", "optimistic"}
        assert len(q[name]) == 2 * 2 * 2          # rules x strategies x penalties
    assert len(q["Q2_markouts"]) == 2 * 2 * 2 * 3  # ... x horizons
    assert all({"conservative", "optimistic", "verdict"} <= set(r) for r in q["Q6_fill_rule_sensitivity"])
    assert len(res["runs"]) == 2 * 2 * 2 * 2 + 2 * 2   # ... x sticky/requeue, plus the signal runs (rules x penalties)


def test_signal_section_is_fitted_before_trading_and_scored_after(study):
    _, res = study
    sg, q = res["signal"], res["questions"]
    assert sg["skew"] is not None and sg["skew"]["horizon_s"] == 5
    assert {(s["signal"], s["horizon_s"]) for s in q["Q7_signal_prediction"]} == \
        {(n, h) for n in ("queue_imbalance", "ofi", "trade_imbalance") for h in (1, 5, 10, 30, 60)}
    assert all(f["n"] <= sg["samples_fit"] for f in sg["fits"])
    # the synthetic mid keeps moving all afternoon, so every score is a real number
    assert all(s["hits_n"] > 0 and s["test_corr"] is not None and s["window_corr"]["n"] >= 2
               for s in q["Q7_signal_prediction"])
    assert {r["rule"] for r in q["Q8_signal_skew"]["pnl"]} == {"conservative", "optimistic"}
    assert len(q["Q8_signal_skew"]["pnl"]) == 2 * 2           # rules x penalties
    assert len(q["Q8_signal_skew"]["markouts"]) == 2 * 2 * 3  # ... x horizons
    assert any(r["claim"].startswith("signal - inventory") for r in q["Q6_fill_rule_sensitivity"])


def test_calibration_window_ends_where_trading_starts(study):
    _, res = study
    c = res["config"]
    assert c["calibration_window"] == ["09:31:00", "12:45:00"]
    assert c["test_window"] == ["12:45:00", "15:59:00"]
    for run in res["runs"]:
        assert all(w["start_ns"] >= 45_900 * 10**9 for w in run["windows"])


def test_study_is_reproducible(study):
    files, res = study
    again = run_study(files, FAST)
    assert json.dumps(again, default=str) == json.dumps(res, default=str)


def test_outputs_are_written_and_well_formed(study, tmp_path):
    _, res = study
    out = write_outputs(res, tmp_path)
    assert json.loads((out / "results.json").read_text(encoding="utf-8"))["ticker"] == "FAKE"
    report = (out / "report.md").read_text(encoding="utf-8")
    assert "synthetic placeholder data" in report
    for heading in ("## Headline", "## Calibration", "## Q1.", "## Q2.", "## Q3.", "## Q4.", "## Q5.", "## Q6.",
                    "## Q7.", "## Q8."):
        assert heading in report
    svgs = sorted(p.name for p in out.glob("*.svg"))
    assert svgs == ["intensity_conservative.svg", "intensity_optimistic.svg", "markouts.svg", "signal_decay.svg",
                    "variance_ratio.svg"]
    for name in svgs:
        ET.parse(out / name)                       # valid XML
        assert f"({name})" in report               # and referenced by the report
    assert "FAKE" in render_summary([res, res])


def test_unusable_calibration_is_reported_not_traded(tmp_path):
    files = generate(SyntheticConfig(n_messages=300, levels=10, seed=1), tmp_path)   # a few minutes of data at most
    res = run_study(files, FAST)
    assert res["problems"] and res["questions"] == {}
    assert "## Problems" in render_report(res)


def test_cli_study_and_shadow(tmp_path, capsys):
    generate(SyntheticConfig(n_messages=12_000, levels=10, seed=11), tmp_path / "data")
    assert main(["shadow", "--dir", str(tmp_path / "data"), "--ticker", "FAKE", "--max-orders", "200"]) == 0
    assert "ALL MISMATCHES EXPLAINED" in capsys.readouterr().out
    assert main(["study", "--dir", str(tmp_path / "data"), "--ticker", "FAKE", "--out", str(tmp_path / "out"),
                 "--model-paths", "5"]) == 0
    assert (tmp_path / "out" / "FAKE" / "report.md").exists()


def test_fill_rule_verdicts():
    pos, neg, none = Estimate(1.0, 0.5, 1.5, 6), Estimate(-1.0, -1.5, -0.5, 6), Estimate(0.1, -0.5, 0.7, 6)
    assert _across_rules({"conservative": pos, "optimistic": pos}) == "holds under both rules"
    assert _across_rules({"conservative": pos, "optimistic": neg}).startswith("FLIPS")
    assert _across_rules({"conservative": pos, "optimistic": none}).startswith("not established")
    assert _across_rules({"conservative": pos}) == "only one rule available"


def test_chart_handles_empty_and_degenerate_input():
    ET.fromstring(line_chart("t", "s", "x", []))
    ET.fromstring(line_chart("t", "s", "x", [Series("a", [(1.0, 0.0)])], log_x=True, reference_y=0.0))
    svg = line_chart("t", "s", "x", [Series("a & b", [(1, 1.0), (2, 2.0)]), Series("c", [(1, 2.0), (2, float("nan"))])])
    ET.fromstring(svg)
    assert "a &amp; b" in svg
