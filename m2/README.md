# ICS Search Engine

We are on the **developer** track (full `developer/DEV` corpus, index on disk, partial files + merge).


## What Milestone 2 is about

**Goal:** Query an **existing** inverted index from disk and print **Boolean AND** results as **URLs** (top 5 per query).

The indexer already maps each stemmed word → list of postings (doc id + term frequency). Search **does not** rebuild the index. It stems the query, looks up each term in `lexicon.txt` / `index.txt`, intersects the posting lists (AND), and maps doc ids to URLs with `doc_ids.txt`. **Tf-idf ranking is optional for this milestone** (required later for the final search engine).


## How to Run

From the **`m2`** folder:

```powershell
cd m2
pip install -r requirements.txt

# Full developer index (defaults: ../index/dev-all)
# Console search
python search.py

# Small test (use the small index you built with m1, e.g. ../index/test)
python search.py --index-dir ..\index\test

# Or override index path explicitly
python search.py --index-dir ..\index\dev-all
```
If you omit `--index-dir`, it defaults to `..\index\dev-all` relative to `m2`.

Type queries at the `>` prompt; type `quit` when done.

## Index Q/A
The **index** folder must already exist (`index.txt`, `lexicon.txt`, `doc_ids.txt`). Build it with **m1** first (indexer) or from **m2** — same corpus/output paths; only the command differs.

**From `team` (m1):** `python main.py` runs the indexer.

**From `team2` (m2):** `python main.py index …` runs the same indexer (`index` tells this `main.py` not to start the search UI). Plain `python main.py` with no `index` starts **search** instead..

### Build the index from **`m1`** folder

```powershell
cd m1
pip install -r requirements.txt

# Full developer run (defaults: ../developer/DEV -> ../index/dev-all)
python main.py

# Or override paths explicitly
python main.py --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
```

### Build the index from **`m2`** folder

```powershell
cd m2
pip install -r requirements.txt

# Full developer run (defaults: ../developer/DEV -> ../index/dev-all)
python main.py index

# Or override paths explicitly
python main.py index --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
```

The **output** folder is created automatically. The **corpus** folder must already exist (your crawled JSON).
