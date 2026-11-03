"""The reference registry: every bibliography entry in the series, by key.

    python -m tp.references [--suite ..] [--store store]

Writes store/references.yaml.  The first paper (in series order) that defines
a key wins; entries whose text differs between papers are listed in the
report so a maintainer can reconcile them.  Generated documents print the
entries they cite from this registry.
"""
from __future__ import annotations

import argparse
import os
import re

import yaml

from .extract import PAPERS, parse_bib, strip_comments


def build(suite: str, store: str):
    refs, conflicts = {}, {}
    for code, tex, *_ in PAPERS:
        path = os.path.join(suite, tex)
        if not os.path.exists(path):
            continue
        body = strip_comments(open(path, encoding="utf-8").read())
        for k, v in parse_bib(body).items():
            norm = re.sub(r"\s+", " ", v["citation"])
            if k in refs and k.startswith("Butler"):
                # the series' own papers: the latest paper's entry is the current one
                refs[k].update(latex=v["latex"], citation=v["citation"], doi=v["doi"],
                               current_in=code)
                continue
            if k in refs:
                if re.sub(r"\s+", " ", refs[k]["citation"]) != norm:
                    conflicts.setdefault(k, sorted({refs[k]["first_in"], code}))
                continue
            refs[k] = {"latex": v["latex"], "citation": v["citation"],
                       "doi": v["doi"], "first_in": code}
    # keep entries added for results that come from no paper (first_in: synthesis)
    path = os.path.join(store, "references.yaml")
    if os.path.exists(path):
        for k, v in (yaml.safe_load(open(path, encoding="utf-8")) or {}).items():
            if k not in refs and isinstance(v, dict) and v.get("first_in") == "synthesis":
                refs[k] = v
    with open(path, "w") as fh:
        yaml.safe_dump(dict(sorted(refs.items())), fh, allow_unicode=True, width=100)
    return refs, conflicts


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="..")
    ap.add_argument("--store", default="store")
    a = ap.parse_args()
    refs, conflicts = build(a.suite, a.store)
    print(f"{len(refs)} references; {len(conflicts)} keys whose text differs between papers")
    for k, v in sorted(conflicts.items()):
        print(f"  {k}: {', '.join(v)}")
