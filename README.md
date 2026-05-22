# CS 121 — Search engine (M1 + M2 layout)

This folder matches a simple **two-folder** layout: **`m1/`** = build the index, **`m2/`** = search it. Put the crawled corpus next to this tree (see **Paths** below).

---

## Folder layout

| Path | Role |
|------|------|
| **`developer/DEV/`** | Crawled JSON pages (download / unzip here; not committed if huge). |
| **`index/dev-all/`** (or `index/test/`) | Output of the indexer: `index.txt`, `lexicon.txt`, `doc_ids.txt`, `partials/`, `stats.json`. |
| **`m1/`** | **Milestone 1** — indexer only (`main.py` + helpers). |
| **`m2/`** | **Milestone 2** — console search (`search.py`) **plus copies** of the same indexer modules so everything runs from one place if you want. |

`readme.txt` in this folder only reminds you to add **`developer`**; you still need to **run the indexer** once to create **`index/`**.

---

## Paths (important)

Defaults assume you open a terminal **inside** `m1` or `m2`:

- Corpus: **`../developer/DEV`**
- Index: **`../index/dev-all`**

So from repo root you typically:

```powershell
cd m1
python main.py
```

```powershell
cd m2
python search.py
```

Use **`python search.py --index-dir ..\index\test`** (or similar) if your index is not `dev-all`.

---

## Should you delete `m1/`?

**Not required.** Here is the tradeoff:

| Keep **`m1/`** | Delete **`m1/`** (only use **`m2/`**) |
|----------------|----------------------------------------|
| Matches “M1 vs M2” milestones and easy zip layout. | One folder to maintain; **`m2/`** already includes **`main.py`**, **`merge_report.py`**, **`index.py`**, etc., so you can **index and search** from **`m2/`** only (`python main.py` then `python search.py`). |
| Two copies of merge code — they must stay in sync (same bug would have hurt both until fixed). | Fewer duplicates; less risk of editing one folder and forgetting the other. |

**Recommendation:** Keep **`m1/`** if your team expects a separate M1 folder. **Otherwise** you can work only in **`m2/`** and ignore or remove **`m1/`** — functionally **`m2`** already has the indexer code.

### If you removed `m1/` — one folder for everything

Always use **`m2/`**: **`main.py`** rebuilds the index; **`search.py`** runs queries.

```powershell
cd m2
pip install -r requirements.txt

# Rebuild full developer index (long)
python main.py

# Then search
python search.py
```

Same optional flags as before, e.g.  
`python main.py --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000`.

---

## Quick commands

**Install (from `m1` or `m2`):**

```powershell
cd m1
pip install -r requirements.txt
```

**Full developer index (long run):**

```powershell
cd m1
python main.py
```

**Search:**

```powershell
cd m2
pip install -r requirements.txt
python search.py
```

**Quit search:** type `quit`, `exit`, or `q`.

---

## Optional test index

```powershell
cd cs-121\m1
python main.py --corpus ..\analyst\ANALYST --output ..\index\test --limit 50 --docs-per-partial 8
```

```powershell
cd cs-121\m2
python search.py --index-dir ..\index\test
```
