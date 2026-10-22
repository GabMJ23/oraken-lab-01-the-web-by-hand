"""Automated checks for Lab 1, Part B. Run with: pytest -q"""
import credits


def run(tmp_path, clicks, start_credits, name="t.db"):
    return credits.simulate(clicks=clicks, credits=start_credits, db=str(tmp_path / name))


def test_one_click_one_credit(tmp_path):
    started, left = run(tmp_path, clicks=1, start_credits=1)
    assert (started, left) == (1, 0)


def test_no_credit_no_analysis(tmp_path):
    started, left = run(tmp_path, clicks=1, start_credits=0)
    assert (started, left) == (0, 0), "With 0 credits, nothing should start and the balance stays at 0."


def test_two_simultaneous_clicks_one_credit(tmp_path):
    for i in range(5):
        started, left = run(tmp_path, clicks=2, start_credits=1, name=f"two-{i}.db")
        assert left >= 0, f"The balance went negative ({left}): the double charge is still there."
        assert started == 1, f"{started} analyses started with a single credit; exactly 1 should start."
        assert left == 0


def test_ten_clicks_three_credits(tmp_path):
    for i in range(3):
        started, left = run(tmp_path, clicks=10, start_credits=3, name=f"ten-{i}.db")
        assert left >= 0, f"The balance went negative ({left})."
        assert started == 3, f"{started} analyses started with 3 credits; exactly 3 should start."
        assert left == 0


def test_delay_is_still_there():
    assert credits.ANALYSIS_DELAY >= 0.1, "Keep the delay: it simulates real life. Fix the logic, not the timing."
