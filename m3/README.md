# M3 — weighted index + ranked search

This folder is a **later milestone** snapshot: same overall pipeline as **`m1`/`m2`**, but indexing uses **weighted token counts** (important HTML zones), and **`search.py`** can run **tf-idf-style ranked** results (default) or plain **boolean** top 5 (`--boolean`).

Paths match **`root`**: from **`m3/`**, defaults are **`../developer/DEV`** and **`../index/dev-all`**.

## What Milestone 3 is about

**Goal:** Same **inverted index on disk** as M1/M2, but indexing uses **weighted term counts** (extra weight for **title**, **h1–h3**, **b/strong**). Search still uses **Boolean AND** over stemmed terms, then **ranks** the matching documents and prints the **top 5 URLs with scores**.

**Indexer:** Build `index.txt`, `lexicon.txt`, `doc_ids.txt`, partials, and `stats.json` from the developer (or test) corpus.

## How to Run
From the **`m3`** folder:

```powershell
cd m3
pip install -r requirements.txt

# Full developer index path (default inside search.py: ..\index\dev-all)
python search.py

# Use a specific index (recommended after an M3 rebuild, e.g. dev-m3)
python search.py --index-dir ..\index\dev-m3

# Or override index path explicitly
python search.py --index-dir ..\index\dev-all
```

Type queries at the `>` prompt; type `quit` when done.

The **index** folder must already exist (`index.txt`, `lexicon.txt`, `doc_ids.txt`). For M3 you should build it with **`m3`** so postings match **weighted** indexing. **`stats.json`** should be present for correct IDF scaling on the full corpus.

**From `m3`:** `python main.py index …` runs the indexer. Plain `python main.py` with no `index` starts **search** (same as `python search.py`).

### Build the index from `m3`

```powershell
cd m3
pip install -r requirements.txt

# Full developer run (defaults: ../developer/DEV -> ../index/dev-all)
python main.py index

# Safer while iterating: separate output folder
python main.py index --output ..\index\dev-m3

# Small test
python main.py index --corpus ..\analyst\ANALYST --output ..\index\test --limit 50 --docs-per-partial 8

# Or override paths explicitly
python main.py index --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
```

The output folder is created automatically. The corpus folder must already exist (your crawled JSON).

### Build the index from `m1` or `m2`

You can still use **`m1`** or **`m2`** to build an index, but that index will **not** include M3 **field weights** in the postings. For M3 demos and reports, build from **`m3`** above.

---


## How to Run (Easy Instructions)

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
