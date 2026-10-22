# Lab 1 hints

Read one hint at a time.

<details>
<summary>Hint 1: where is the problem?</summary>

The current code works in **two steps**: it reads the balance, waits, then charges. While it waits, the other click reads the *same* balance. Both see "1 credit", so both charge.

</details>

<details>
<summary>Hint 2: what to change</summary>

Instead of "read, then decide, then write", ask the database to do the check **and** the charge in one statement:

```sql
UPDATE users SET credits = credits - 1 WHERE id = ? AND credits >= 1
```

The database guarantees that only one of the two statements can succeed when there is one credit.

</details>

<details>
<summary>Hint 3: how do you know it worked?</summary>

`c.execute(...)` returns a cursor. Its `rowcount` tells you how many rows the statement changed: `1` means the charge happened (start the analysis), `0` means there was no credit left. Keep the delay *after* a successful charge: that is when the analysis actually starts.

</details>
