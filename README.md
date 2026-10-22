# Lab 1: The web by hand, and the double charge

**Part 1 · Lessons 1 and 2 · about 2 hours · automatically checked**

## Goals

- Read a real HTTP request, its headers and its JSON response.
- Trigger a race condition, then fix it with a single indivisible operation.

## Before you start

You need Python 3.12 and Git. Create your own copy of this lab (**Use this template** on GitHub), clone it, then:

```bash
python -m venv .venv
# macOS / Linux: source .venv/bin/activate      Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q          # most checks fail at first: that is expected
```

Rules for every lab: one Git repository, one commit per step, your answers in `REPORT.md`, and no secret in Git.

## Part A: Observe the web

1. Open **https://lebaveux.com**, a production AI assistant used as a case study in this course. Open the developer tools (F12), **Network** tab, and reload. For the first request, note the method, the status code and three response headers.
2. Find the `strict-transport-security` header. What does it do? (Hint: lesson 2, section 2.1.)
3. In a terminal, call a public US government API, the Federal Register:
   ```bash
   curl -i "https://www.federalregister.gov/api/v1/documents.json?per_page=2"
   ```
   Find the status code and the content type. In the JSON, find an object, a list and a key/value pair.
4. Do the same on a path that does not exist: `.../api/v1/documentz.json`. What code do you get, and what does it mean?

> Tip: if you add square brackets to a URL in curl (for example `fields[]=title`), add the `-g` option. Otherwise curl treats the brackets as a pattern and sends nothing.

Write your answers in `REPORT.md`.

## Part B: Trigger the double charge

`credits.py` simulates two clicks arriving at the same moment for a user who has **one** credit.

1. Run it: `python credits.py`. How many analyses start? How many credits are left? Explain why, with the timeline table from lesson 2.
2. Fix `send()`: use **one single statement** that checks and charges at the same time (`... WHERE id = ? AND credits >= 1`), then use the cursor's `rowcount` to know whether the charge happened.
3. Run `pytest -q` until every check passes. The tests fire 2 clicks on 1 credit five times, and 10 clicks on 3 credits three times.

Do not remove the delay in `send()`. It simulates real life: fix the logic, not the timing.

## Deliverable and success criteria

- `credits.py` fixed, and `REPORT.md` completed.
- **Success:** `pytest -q` is all green. The balance never goes below zero, whatever the number of simultaneous clicks.
- Each time you push, GitHub runs the same checks (the **Actions** tab shows a green or red mark).

**Going further:** with 10 simultaneous clicks and 3 credits, how many analyses should start? Check it with `simulate(10, 3)`.

Stuck? Open `HINTS.md`: three hints, from gentle to almost the answer.
