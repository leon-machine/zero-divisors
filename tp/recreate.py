"""Recreate every paper of the series from the store, and measure how close
each comes to its original.

    python -m tp.recreate [--papers T01,T02] [--no-verify]

For each paper a recipe recipes/<code>-regenerated.yaml is written (unless
one exists): its spine is every result of the paper in the paper's order,
shown at formal level with the paper's remarks and examples attached. The
document is generated (or regenerated) and the Phase 3 gate compares it with
the original: which numbered results and notes are present, whether their
type is kept, word overlap of statements, order (Kendall tau), how much of the
original's wording survives, whether it compiles with every reference
resolved, and whether the assembled verify script passes.

The prose (abstract, introductions, transitions) is the template writer's
unless documents/<doc>/prose.json supplies it; the measure of the store is
the results, proofs and notes, not the prose.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import yaml

from . import docgen, gate3
from .extract import PAPERS
from .model import load_store


def paper_title(suite, tex):
    import re
    src = open(os.path.join(suite, tex), encoding="utf-8").read()
    m = re.search(r"\\title\{(.*?)\}\s*\n", src, re.S)
    t = m.group(1) if m else os.path.basename(tex)
    t = re.sub(r"\\\\(\[[^\]]*\])?", ": ", t)
    t = re.sub(r"\\(?:bfseries|large|Large|itshape|normalsize|small)\b", "", t)
    t = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+\s*", "", t)          # font switches such as \upshape
    t = re.sub(r"[{}]", "", t)
    t = re.sub(r"\s+", " ", t).strip(" :")
    return t.replace(": :", ":").replace("::", ":")


def recipe_for(store, code, tex, suite):
    ents = []
    for eid, e in store.entities.items():
        loc = e.meta.get("locators") or {}
        if isinstance(loc, list):
            loc = loc[0] if loc else {}
        if loc.get("paper") == code and e.kind != "note" and e.status != "postulate":
            ents.append((int(loc.get("line") or 0), eid))
    spine = [eid for _, eid in sorted(ents)]
    # the paper's Facts that are aliases of earlier results: cited, not derived
    from . import labels as labelreg
    reg = labelreg.load(store.root)
    cite = []
    for k, rec in reg.items():
        if k.startswith(code + ":fact:") and isinstance(rec, dict):
            t = rec.get("entity")
            if t in store.entities and t not in spine and t not in cite:
                cite.append(t)
    doc = code.lower() + "-regenerated"
    return {"doc": doc,
            "title": paper_title(suite, tex) + " (regenerated from the store)",
            "author": "Leon Butler", "level": "formal", "spine": spine,
            "show": "spine-only", "paper": code, "sections": "paper", "cite": cite,
            "include": {"assumptions": "always", "refutations": "in-cone",
                        "predictions": "in-cone", "notes": "attached",
                        "settings": "attached"},
            "prose": "paper",
            "on_refuted": "keep-as-refutation", "format": "latex-series",
            "budget": {"abstract_words": [150, 250]},
            "gate": {"phase": 3, "original": os.path.join("..", tex),
                     "note": f"Recreate {code} from the store"}}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--papers", default="")
    ap.add_argument("--store", default="store")
    ap.add_argument("--report", default="seed/RECREATION_REPORT.md")
    a = ap.parse_args(argv)
    want = [x for x in a.papers.split(",") if x]
    store = load_store(a.store)
    suite = ".."             # the papers sit beside the lab folder
    rows = []
    for code, tex, region, script in PAPERS:
        if want and code not in want:
            continue
        if not os.path.exists(os.path.join(suite, tex)):
            continue
        rpath = os.path.join("recipes", code.lower() + "-regenerated.yaml")
        r = recipe_for(store, code, tex, suite)
        if os.path.exists(rpath):
            old = yaml.safe_load(open(rpath))
            if old.get("cite") != r["cite"]:
                old["cite"] = r["cite"]          # keep the rest of a hand-kept recipe
                yaml.safe_dump(old, open(rpath, "w"), sort_keys=False, allow_unicode=True,
                               width=100)
        else:
            if not r["spine"]:
                continue
            yaml.safe_dump(r, open(rpath, "w"), sort_keys=False, allow_unicode=True, width=100)
        try:
            docgen.generate(a.store, rpath)
            g = gate3.main(rpath)
            gate3.report_md(g, os.path.join("documents", code.lower() + "-regenerated",
                                            "GATE3.md"))
        except Exception as exc:          # one paper's failure must not stop the rest
            rows.append({"paper": code, "error": f"{type(exc).__name__}: {exc}"[:300]})
            print(code, "ERROR", exc, file=sys.stderr)
            continue
        rs = g["rows"]
        res = [x for x in rs if x["env"] not in ("remark", "example")]
        notes = [x for x in rs if x["env"] in ("remark", "example")]
        row = {"paper": code,
               "results": len(res), "results_in_doc": sum(x["in_doc"] for x in res),
               "notes": len(notes), "notes_in_doc": sum(x["in_doc"] for x in notes),
               "type_kept": sum(1 for x in res if x.get("type_kept")),
               "overlap_min": min([x.get("statement_overlap", 1) for x in rs
                                   if x["in_doc"] and not x.get("alias")] or [1]),
               "aliases": sum(1 for x in rs if x.get("alias")),
               "tau": g["order_tau"], "words": g["words"], "compile": g["compile"],
               "verify": g["verify"]["returncode"]}
        rows.append(row)
        print(json.dumps(row))
    write_report(rows, a.report)
    return 0


def write_report(rows, path):
    L = ["# Recreating the papers from the store", "",
         "Each paper regenerated at formal level from the store (results in the paper's",
         "order, proofs, imports with provenance, remarks and examples attached) and",
         "compared with its original by the Phase 3 gate. Prose is the template",
         "writer's except where a prose file exists. A Fact of the paper that restates",
         "an earlier paper's result counts as present when the recreation cites that",
         "result (with its provenance); its statement overlap is not counted, since the",
         "recreation quotes the earlier paper's statement.", "",
         "| paper | results present | type kept | notes present | lowest statement overlap "
         "| order (tau) | words of original kept | compile errors | undefined refs | verify |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        if "error" in r:
            L.append(f"| {r['paper']} | error: {r['error']} |||||||||")
            continue
        L.append("| {p} | {a}/{b} | {t}/{b} | {na}/{nb} | {o:.2f} | {tau:.3f} | {w:.0%} | {ce} | {u} | {v} |"
                 .format(p=r["paper"], a=r["results_in_doc"], b=r["results"], t=r["type_kept"],
                         na=r["notes_in_doc"], nb=r["notes"], o=r["overlap_min"],
                         tau=r["tau"] if r["tau"] is not None else 0,
                         w=r["words"]["coverage"], ce=r["compile"]["errors"],
                         u=r["compile"]["undefined"],
                         v="pass" if r["verify"] == 0 else f"exit {r['verify']}"))
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    sys.exit(main())
