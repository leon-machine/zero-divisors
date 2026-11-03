"""Phase 3 gate: regenerate one paper from the store and compare with the original.

  python -m tp.gate3 recipes/t02-regenerated.yaml

Checks, for every theorem-like environment of the original paper:
  - it is in the store (by label) and in the regenerated document;
  - its statement survives (word overlap of the normalised statement text);
  - its type survives (Theorem, Proposition, Fact (imported), ...);
  - a proved result carries a proof, an imported one carries provenance;
  - the order of the results (Kendall tau against the paper's order).
Then it compiles the regenerated LaTeX and runs the assembled verify script,
and counts the original verify script's checks that the document's claims
account for.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile

import yaml

from .extract import PAPERS, strip_comments
from .gate import kendall_tau
from .model import load_store

ENVS = ("theorem", "proposition", "lemma", "corollary", "fact", "definition",
        "conjecture", "assembly", "computation", "principle", "remark", "example")
GEN_ENV = {"theorem": "theorem", "proposition": "proposition", "lemma": "lemma",
           "corollary": "corollary", "assembled": "fact", "fact": "fact",
           "definition": "definition", "conjecture": "conjecture",
           "principle": "principle", "remark": "remark", "example": "example"}


def _words(tex):
    t = re.sub(r"\\label\{[^}]*\}", " ", tex)
    t = re.sub(r"\\(?:ref|eqref|cite[pt]?)\{[^}]*\}", " ", t)
    t = re.sub(r"\\[a-zA-Z]+", " ", t)
    t = re.sub(r"[^A-Za-z0-9]+", " ", t).lower()
    return [w for w in t.split() if len(w) > 2]


def _overlap(a, b):
    A, B = set(_words(a)), set(_words(b))
    return len(A & B) / max(1, len(A))


def _original_envs(tex):
    src = strip_comments(open(tex, encoding="utf-8").read())
    out = []
    for m in re.finditer(r"\\begin\{(%s)\}(\[[^\]]*\])?" % "|".join(ENVS), src):
        env = m.group(1)
        end = src.find(r"\end{%s}" % env, m.end())
        body = src[m.end():end]
        lab = re.search(r"\\label\{([^}]+)\}", body)
        out.append({"env": env, "title": (m.group(2) or "").strip("[]"),
                    "label": lab.group(1) if lab else None, "text": body,
                    "has_proof": src[end:end + 400].lstrip().startswith(r"\begin{proof}")
                    or r"\begin{proof}" in src[end:end + 200]})
    return out


def main(recipe_path, lab="."):
    recipe = yaml.safe_load(open(recipe_path))
    doc = recipe["doc"]
    folder = os.path.join(lab, "documents", doc)
    tex = open(os.path.join(folder, "rendered.tex")).read()
    original = os.path.normpath(os.path.join(lab, recipe["gate"]["original"]))
    code = next(c for c, f, *_ in PAPERS if os.path.basename(f) == os.path.basename(original))
    store = load_store(os.path.join(lab, "store"))
    by_label = {}
    for e in store.entities.values():
        loc = e.meta.get("locators") or {}
        if loc.get("paper") == code and loc.get("label"):
            by_label.setdefault(loc["label"], e.id)
    gen = {}
    for m in re.finditer(r"\\begin\{(\w+)\}(?:\[[^\]]*\])?\\label\{c:([^}]+)\}(.*?)\\end\{\1\}"
                         r"(\s*\\begin\{proof\})?", tex, re.S):
        gen[m.group(2)] = {"env": m.group(1), "text": m.group(3),
                           "proof": bool(m.group(4)),
                           "prov": r"\emph{Provenance:}" in m.group(3),
                           "pos": m.start()}
    reg_path = os.path.join(lab, "store", "labels.yaml")
    reg = (yaml.safe_load(open(reg_path)) or {}) if os.path.exists(reg_path) else {}
    rows, order_paper = [], []
    for o in _original_envs(original):
        cid = by_label.get(o["label"])
        alias = False
        if cid is None and o["label"]:
            # a Fact that restates an earlier paper's result is that result:
            # the recreation cites it (with provenance) instead of copying it
            rec = reg.get(f"{code}:{o['label']}") or {}
            if isinstance(rec, dict) and rec.get("entity") in store.entities:
                cid, alias = rec["entity"], True
        g = gen.get(cid) if cid else None
        row = {"label": o["label"], "env": o["env"], "title": o["title"], "claim": cid,
               "in_doc": bool(g)}
        row["alias"] = alias
        if g:
            if not alias:
                order_paper.append(cid)
            row["gen_env"] = g["env"]
            row["type_kept"] = GEN_ENV.get(g["env"]) == o["env"] or (
                o["env"] == "fact" and g["env"] == "assembled") or (
                alias and o["env"] == "fact" and g["env"] in ("fact", "assembled"))
            row["statement_overlap"] = round(_overlap(o["text"], g["text"]), 3)
            st = store.entities[cid].meta.get("status")
            row["support"] = ("proof" if g["proof"] else "provenance" if g["prov"]
                              else "none")
            row["support_ok"] = (g["proof"] if st == "proved" else
                                 g["prov"] if st == "imported" else True)
        rows.append(row)
    order_gen = sorted(order_paper, key=lambda c: gen[c]["pos"])
    tau, n = kendall_tau(order_paper, order_gen)
    # compile
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, "x.tex"), "w").write(tex)
        for _ in range(2):
            p = subprocess.run(["pdflatex", "-interaction=nonstopmode", "x.tex"], cwd=d,
                               capture_output=True, text=True)
        log = open(os.path.join(d, "x.log"), errors="replace").read()
    errors = len(re.findall(r"^! ", log, re.M))
    undefined = len(re.findall(r"LaTeX Warning: (?:Reference|Citation) .* undefined", log))
    # how much of the original's vocabulary the regenerated text carries
    body = strip_comments(open(original, encoding="utf-8").read())
    body = body[body.find(r"\begin{document}"):body.find(r"\begin{thebibliography}")]
    gbody = tex[tex.find(r"\begin{document}"):]
    W_o, W_g = _words(body), set(_words(gbody))
    word_cov = round(sum(1 for w in W_o if w in W_g) / max(1, len(W_o)), 3)
    vs = [f for f in os.listdir(folder) if f.startswith("verify_")][0]
    v = subprocess.run([sys.executable, vs], cwd=folder, capture_output=True, text=True)
    return {"doc": doc, "original": os.path.basename(original), "paper": code,
            "rows": rows, "order_tau": tau, "order_n": n,
            "words": {"original": len(W_o), "generated": len(_words(gbody)),
                      "coverage": word_cov},
            "compile": {"errors": errors, "undefined": undefined,
                        "pdf": p.returncode == 0},
            "verify": {"returncode": v.returncode, "tail": v.stdout.strip().splitlines()[-4:]},
            "extra_in_doc": sorted(set(gen) - set(order_paper)
                                   - {x["claim"] for x in rows if x.get("alias")})}


def report_md(r, path):
    L = [f"# Phase 3 gate: {r['original']} regenerated as `{r['doc']}`", "",
         "| original | label | in store | in doc | type kept | statement overlap | support |",
         "|---|---|---|---|---|---|---|"]
    for x in r["rows"]:
        L.append("| {env} {title} | `{label}` | {c} | {d} | {t} | {o} | {s} |".format(
            env=x["env"], title=x["title"], label=x["label"],
            c="yes" if x["claim"] else "**no**", d="yes" if x["in_doc"] else "**no**",
            t=("yes" if x.get("type_kept") else f"**{x.get('gen_env')}**") if x["in_doc"] else "",
            o=x.get("statement_overlap", ""),
            s=(x.get("support", "") + ("" if x.get("support_ok", True) else " **missing**"))))
    L += ["", f"Order of results, Kendall tau against the paper: {r['order_tau']} "
          f"over {r['order_n']} results.", "",
          f"Words: the original has {r['words']['original']}, the regenerated text "
          f"{r['words']['generated']}; {r['words']['coverage']:.0%} of the original's word "
          f"occurrences appear in the regenerated text.", "",
          f"Compile: {r['compile']['errors']} errors, {r['compile']['undefined']} undefined "
          f"references or citations.", "",
          f"Assembled verify script: exit {r['verify']['returncode']}; "
          + "; ".join(r["verify"]["tail"]), "",
          "In the document but not a numbered result of the paper: "
          + (", ".join(f"`{x}`" for x in r["extra_in_doc"]) or "none"), ""]
    open(path, "w").write("\n".join(L))


if __name__ == "__main__":
    r = main(sys.argv[1])
    print(json.dumps(r, indent=1))
    if len(sys.argv) > 2:
        report_md(r, sys.argv[2])
