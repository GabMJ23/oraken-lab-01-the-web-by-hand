"""Checks that REPORT.md is filled in. It does not grade your reasoning: it makes sure nothing is left blank."""
import pathlib
import re

REPORT = pathlib.Path(__file__).resolve().parent.parent / "REPORT.md"


def section(text, start, end=None):
    i = text.index(start)
    j = text.index(end, i) if end else len(text)
    return text[i:j]


def test_report_exists():
    assert REPORT.exists(), "REPORT.md is missing."


def test_required_answers_filled():
    text = REPORT.read_text(encoding="utf-8")
    required = section(text, "## Part A", "**Going further")
    left = required.count("TODO")
    assert left == 0, f"{left} required answer(s) still say TODO in REPORT.md (Parts A and B)."


def test_a4_mentions_the_status_code():
    text = REPORT.read_text(encoding="utf-8")
    a4 = section(text, "**A4.**", "## Part B")
    assert re.search(r"\b404\b", a4), "A4: which status code did the wrong path return?"


def test_b2_explanation_is_substantial():
    text = REPORT.read_text(encoding="utf-8")
    b2 = section(text, "**B2.**", "**B3.**")
    words = len(re.findall(r"\w+", b2))
    assert words >= 40, "B2: explain the double charge in about five lines (40 words or more)."
