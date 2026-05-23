# CS 121 — Search engine (`m1` / `m2` / `m3`)

This folder can hold **three code snapshots** side by side: **`m1/`** (indexer), **`m2/`** (boolean search + indexer copy), **`m3/`** (weighted indexing + ranked search). They all read the same **`developer/`** and write the same **`index/`** unless you change `--output`.

---

## Folder layout

| Path | Role |
|------|------|
| **`developer/DEV/`** | Crawled JSON pages (download / unzip here; not committed if huge). |
| **`index/dev-all/`** (or `index/test/`) | Output of the indexer: `index.txt`, `lexicon.txt`, `doc_ids.txt`, `partials/`, `stats.json`. |
| **`m1/`** | **Milestone 1** — indexer only (`main.py` + helpers). |
| **`m2/`** | **Milestone 2** — boolean AND search (`search.py`) **plus** indexer modules if you want one folder for both. |
| **`m3/`** | **Milestone 3** — **weighted** indexing (`weighted_counts` in `index.py`) and **`search.py`** with **ranked** (default) or **`--boolean`** mode. See **`m3/README.md`**. |

`readme.txt` in this folder only reminds you to add **`developer`**; you still need to **run an indexer** (`m1`, `m2`, or `m3`) to create **`index/`**.

---

## Paths (important)

Defaults assume you open a terminal **inside** `m1`, `m2`, or `m3`:

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

**M3 (weighted index + ranked search):** see **`m3/README.md`**. Short version:

```powershell
cd m3
pip install -r requirements.txt
python main.py          # rebuild index (same default paths)
python search.py        # ranked by default; add --boolean for M2-style
```

**You do not need to delete `m1` or `m2` to use `m3`.** They are separate folders. All three can coexist. If everyone uses the same default **`../index/dev-all`**, running an indexer from **any** of them **overwrites** that index — use a different **`--output`** if you want to keep multiple indexes.

Use **`python search.py --index-dir ..\index\test`** (or similar) if your index is not `dev-all`.

---

## Optional test index

```powershell
cd m1
python main.py --corpus ..\analyst\ANALYST --output ..\index\test --limit 50 --docs-per-partial 8
```

```powershell
cd m2
python search.py --index-dir ..\index\test
```
