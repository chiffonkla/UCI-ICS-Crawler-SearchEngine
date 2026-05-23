import argparse
import os
import sys

from corpus_io import collect_pages, write_doc_ids
from index import buildPartialIndex
from merge_report import finishIndex

# Defaults when you run: python main.py
TEAM_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CORPUS = os.path.normpath(os.path.join(TEAM_DIR, "..", "developer", "DEV"))
DEFAULT_OUTPUT = os.path.normpath(os.path.join(TEAM_DIR, "..", "index", "dev-all"))


def run_indexer(args):
    print("Corpus:", args.corpus)
    print("Output:", args.output)

    # Load pages as [(doc_id, {"url", "content"}), ...]
    print("Reading corpus...")
    pages = collect_pages(args.corpus, limit=args.limit)
    if len(pages) == 0:
        print("No pages found. Check --corpus path.")
        sys.exit(1)

    # Write doc_ids.txt (one line per page: doc_id + tab + url)
    write_doc_ids(args.output, pages)
    print("Loaded", len(pages), "documents.")
    print("Wrote", os.path.join(args.output, "doc_ids.txt"))

    documents = [page for (doc_id, page) in pages]

    partialsFolder = os.path.join(args.output, "partials")
    print("Building partial index files in:", partialsFolder)
    print("(one partial file every", args.docs_per_partial, "pages)")
    partialPaths, sumlengths = buildPartialIndex(
        documents,
        partialsFolder,
        docsPerPartial=args.docs_per_partial,
    )
    print("Wrote", len(partialPaths), "partial index file(s).")
    if len(partialPaths) < 3 and args.limit is None:
        print(
            "Developer spec wants >= 3 partial files on full corpus.",
            "Use a smaller --docs-per-partial if you only see 1 or 2 files.",
        )

    n_pages = len(pages)
    avglength = 0.0
    if n_pages > 0:
        avglength = sumlengths / n_pages

    finishIndex(
        args.output,
        nDocuments=n_pages,
        corpus=os.path.normpath(args.corpus),
        partialsFolder=partialsFolder,
        avglength=avglength,
    )


def cli_main():
    parser = argparse.ArgumentParser(description="team2: search (default) or index")
    sub = parser.add_subparsers(dest="command")

    idx = sub.add_parser("index", help="Run M1 indexer (build inverted index on disk)")
    idx.add_argument(
        "--corpus",
        default=DEFAULT_CORPUS,
        help="Folder with JSON pages (default: ../developer/DEV)",
    )
    idx.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="Output folder (default: ../index/dev-all)",
    )
    idx.add_argument("--limit", type=int, default=None, help="Only load this many pages (testing)")
    idx.add_argument(
        "--docs-per-partial",
        type=int,
        default=5000,
        help="Write one partial index file after every N pages (default 5000).",
    )

    args = parser.parse_args()

    if args.command == "index":
        run_indexer(args)
    else:
        from search import main as search_main

        search_main()


if __name__ == "__main__":
    cli_main()
