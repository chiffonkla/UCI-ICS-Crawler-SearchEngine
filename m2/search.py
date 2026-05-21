import os
import sys

from corpus_io import get_url, read_urls
from index_reader import line_for_term, read_lexicon
from parse_document import stem_query
from postings import parse_line
from query import intersect


def run_query(lex, index_path, urls, text):
    stems = stem_query(text)
    if len(stems) == 0:
        print("No terms.")
        return

    lists = []
    for s in stems:
        raw = line_for_term(lex, index_path, s)
        if raw is None:
            print("No results.")
            return
        _, posts = parse_line(raw)
        if len(posts) == 0:
            print("No results.")
            return
        lists.append(posts)

    cur = lists[0]
    for k in range(1, len(lists)):
        cur = intersect(cur, lists[k])

    if len(cur) == 0:
        print("No results.")
        return

    print("Found", len(cur), "doc(s). Top 5:")
    for j in range(min(5, len(cur))):
        u = get_url(urls, cur[j].docid)
        if u is None:
            u = "(no url)"
        print(" ", j + 1, u)


def main():
    index_dir = os.path.join("..", "index", "dev-all")
    if "--index-dir" in sys.argv:
        i = sys.argv.index("--index-dir")
        if i + 1 < len(sys.argv):
            index_dir = sys.argv[i + 1]

    index_path = os.path.join(str(index_dir), "index.txt")
    if not os.path.isfile(index_path):
        print("Missing:", index_path)
        print("Usage: python search.py [--index-dir path\\to\\index]")
        sys.exit(1)

    print("Loading...")
    lex = read_lexicon(index_dir)
    urls = read_urls(index_dir)
    print("Ready (quit to exit).\n")

    while True:
        try:
            line = input("> ").strip()
        except EOFError:
            print()
            break
        if line == "":
            continue
        if line.lower() in ("quit", "exit", "q"):
            break
        run_query(lex, index_path, urls, line)


if __name__ == "__main__":
    main()
