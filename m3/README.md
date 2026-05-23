# M3 — weighted index + ranked search

This folder is a **later milestone** snapshot: same overall pipeline as **`m1`/`m2`**, but indexing uses **weighted token counts** (important HTML zones), and **`search.py`** can run **tf-idf-style ranked** results (default) or plain **boolean** top 5 (`--boolean`).

Paths match **`root`**: from **`m3/`**, defaults are **`../developer/DEV`** and **`../index/dev-all`**.

---

## How to run

**1. Build or rebuild the index** (indexer only — plain `python main.py`):

```powershell
cd m3
pip install -r requirements.txt

python main.py
```

Optional (same flags as `m1`):

```powershell
python main.py --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
python main.py --corpus ..\analyst\ANALYST --output ..\index\test --limit 50 --docs-per-partial 8
```

**2. Search** (needs an existing index):

```powershell
cd m3
python search.py
```

- **`--index-dir ..\index\test`** — use another index folder.
- **`--boolean`** — M2-style first five AND hits (no score column); omit it for **ranked** output with scores and timing.

**Quit:** `quit`, `exit`, or `q`.

---

## Same `index/` as `m1` / `m2`?

By default, **yes** — all use **`../index/dev-all`**. Building from **`m3`** **overwrites** that folder’s index files unless you pass a different **`--output`**.

You do **not** have to delete **`m1`** or **`m2`**; they are separate code copies. Remove them only if you want less duplication.
