import os
from collections import Counter
from nltk.stem import PorterStemmer
from parse_document import Parse
from postings import Postings

stemmer = PorterStemmer()

# Save RAM to disk
def writePartialFile(index, partialsFolder, partialNum, paths):
    if len(index) == 0:
        return index, partialNum, paths

    # zfill(4) pads the number( 0 -> "0000")
    fileNum = str(partialNum).zfill(4)
    path = os.path.join(partialsFolder, "partial_" + fileNum + ".txt")
    with open(path, "w", encoding="utf-8") as f:
        for term in sorted(index.keys()):
            posts = index[term]
            line = term + "\t" + ",".join(str(p.docid) + ":" + str(p.frequency) for p in posts)
            f.write(line + "\n")

    paths.append(path)
    return {}, partialNum + 1, paths

def buildIndex(documents):
    index = {}
    docNum = -1

    for document in documents:
        docNum = docNum + 1
        tokens = Parse(document)
        stemmedTokens = [stemmer.stem(t.lower()) for t in tokens] 

        counts = Counter(stemmedTokens)
        for token, freq in counts.items():
            tempPost = Postings(docNum, freq)

            if token not in index:
                index[token] = [tempPost]
            else:
                index[token].append(tempPost)
    return index

def buildPartialIndex(documents, partialsFolder, docsPerPartial=5000):
    os.makedirs(partialsFolder, exist_ok=True)

    index = {}
    nDocs = 0
    partialNum = 0
    paths = []
    docNum = -1

    for document in documents:
        docNum = docNum + 1
        tokens = Parse(document)
        stemmedTokens = [stemmer.stem(t.lower()) for t in tokens]
        counts = Counter(stemmedTokens)

        for token, freq in counts.items():
            tempPost = Postings(docNum, freq)
            if token not in index:
                index[token] = [tempPost]
            else:
                index[token].append(tempPost)

        nDocs = nDocs + 1
        if nDocs >= docsPerPartial:
            index, partialNum, paths = writePartialFile(index, partialsFolder, partialNum, paths)
            nDocs = 0

        if docsPerPartial > 0 and docNum > 0 and (docNum + 1) % docsPerPartial == 0:
            print("  ... indexed", docNum + 1, "documents (partial files so far:", len(paths), ")")

    index, partialNum, paths = writePartialFile(index, partialsFolder, partialNum, paths)
    return paths
