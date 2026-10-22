"""Lab 1, Part B: the double charge.

Two "clicks" arrive at the same moment. The user has a single credit.
Each click tries to start one analysis and charge one credit.

Run it:   python credits.py
Test it:  pytest -q

Your job: fix send() so that the balance can never go below zero,
whatever the number of simultaneous clicks. Do not remove the delay:
it simulates the real time it takes to start an analysis.
"""
import sqlite3
import threading
import time

DB = "credits.db"
USER_ID = 42
ANALYSIS_DELAY = 0.1  # seconds: the time it takes to start an analysis


def setup(db=DB, credits=1, user_id=USER_ID):
    """Create a fresh database with one user and a given number of credits."""
    con = sqlite3.connect(db)
    con.execute("DROP TABLE IF EXISTS users")
    con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, credits INTEGER)")
    con.execute("INSERT INTO users VALUES (?, ?)", (user_id, credits))
    con.commit()
    con.close()


def send(db=DB, user_id=USER_ID):
    """Start one analysis if the user has a credit.

    Returns True if an analysis was started (and one credit charged), False otherwise.
    """
    c = sqlite3.connect(db, timeout=10)
    try:
        # 1. check the balance
        (credits,) = c.execute("SELECT credits FROM users WHERE id = ?", (user_id,)).fetchone()
        time.sleep(ANALYSIS_DELAY)  # the time it takes to start the analysis
        # 2. charge
        if credits >= 1:
            c.execute("UPDATE users SET credits = credits - 1 WHERE id = ?", (user_id,))
            c.commit()
            return True
        return False
    finally:
        c.close()


def balance(db=DB, user_id=USER_ID):
    con = sqlite3.connect(db)
    try:
        return con.execute("SELECT credits FROM users WHERE id = ?", (user_id,)).fetchone()[0]
    finally:
        con.close()


def simulate(clicks=2, credits=1, db=DB):
    """Fire `clicks` simultaneous clicks. Returns (analyses_started, credits_left)."""
    setup(db, credits)
    results = []
    lock = threading.Lock()

    def click():
        started = send(db)
        with lock:
            results.append(started)

    threads = [threading.Thread(target=click) for _ in range(clicks)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return sum(results), balance(db)


if __name__ == "__main__":
    started, left = simulate(clicks=2, credits=1)
    print("analyses started:", started)
    print("credits left:   ", left)
