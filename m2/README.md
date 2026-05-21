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

# Console search (point at the folder that contains index.txt, lexicon.txt, doc_ids.txt)
python search.py --index-dir ..\index\dev-all
```

If you omit `--index-dir`, it defaults to `..\index\dev-all` relative to `m2`.

Type queries at the `>` prompt; type `quit` when done.

The **index** must already exist (build it with the indexer first). From the **m1** folder, for example:

```powershell
cd m1
pip install -r requirements.txt

python main.py --corpus ..\developer\DEV --output ..\index\dev-all --docs-per-partial 5000
```

The output folder is created automatically. The corpus folder must already exist (your crawled JSON).
