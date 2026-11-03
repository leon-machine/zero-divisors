"""Apply tag assignments to the store.

    python -m tp.tags apply seed/tag_assignment_*.yaml [--store store]
    python -m tp.tags report [--store store]

Tags are a controlled vocabulary (store/tags.yaml): cross-cutting themes, so a
result can belong to several besides its one subject. They are cosmetic in
the version sense (no bump): they describe a result, they do not change what
it says. `apply` writes each assignment into the entity's front matter as
`tags: [...]`, replacing any earlier tags; it refuses unknown tags and ids.
`report` prints the vocabulary with counts, and the results with no tag.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter

import yaml

from .model import load_store, ENTITY_FILE

FM = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def apply(paths, store_root):
    store = load_store(store_root)
    vocab = {t["id"] for t in store.tags}
    assign = {}
    for p in paths:
        for k, v in (yaml.safe_load(open(p)) or {}).items():
            assign[k] = list(dict.fromkeys(v or []))
    bad_ids = [k for k in assign if k not in store.entities]
    bad_tags = sorted({t for v in assign.values() for t in v if t not in vocab})
    if bad_ids or bad_tags:
        raise SystemExit(f"refused: unknown ids {bad_ids[:10]}, unknown tags {bad_tags[:10]}")
    n = 0
    for eid, tags in assign.items():
        e = store.entities[eid]
        path = f"{e.path}/{ENTITY_FILE}"
        text = open(path, encoding="utf-8").read()
        m = FM.match(text)
        head = m.group(1)
        head = re.sub(r"^tags:.*\n(?:- .*\n)*", "", head + "\n", flags=re.M).rstrip("\n")
        if tags:
            line = "tags: [" + ", ".join(tags) + "]"
            if re.search(r"^subject: .*$", head, re.M):
                head = re.sub(r"^(subject: .*)$", r"\1\n" + line.replace("\\", r"\\"),
                              head, count=1, flags=re.M)
            else:
                head += "\n" + line
        new = "---\n" + head + "\n---\n" + text[m.end():]
        if new != text:
            open(path, "w", encoding="utf-8").write(new)
            n += 1
    print(f"tagged {n} entities from {len(assign)} assignments")


def report(store_root):
    store = load_store(store_root)
    c = Counter(t for e in store.entities.values() for t in (e.meta.get("tags") or []))
    for t in store.tags:
        print(f"{c.get(t['id'], 0):4d}  {t['group']:<11} {t['id']}")
    untagged = [k for k, e in store.entities.items()
                if e.kind != "note" and not e.meta.get("tags")]
    print(f"{len(untagged)} results carry no tag")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=("apply", "report"))
    ap.add_argument("files", nargs="*")
    ap.add_argument("--store", default="store")
    a = ap.parse_args(argv)
    if a.cmd == "apply":
        apply(a.files, a.store)
    else:
        report(a.store)
    return 0


if __name__ == "__main__":
    sys.exit(main())
