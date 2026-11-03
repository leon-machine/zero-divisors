"""Phase 1 gate: compare a generated document with G00's hand-written sections.

  python -m tp.gate recipes/falling-in.yaml ../G00_transport_papers_guide.tex
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile

import yaml

from .extract import PAPERS, locator_numbers, read_labels

LOC_RE = re.compile(r"\\loc\{(T\d+)\}\{([^}]*)\}\{")
TYPE_OF_ENV = {"theorem": "Thm", "proposition": "Prop", "lemma": "Lem",
               "corollary": "Cor", "fact": "Fact", "premise": "Prem",
               "definition": "Def", "axiom": "Ax"}


def _env_of(lab, cid):
    if not cid:
        return None
    for sub in ("claims", "objects"):
        p = os.path.join(lab, "store", sub, cid, "entity.md")
        if os.path.exists(p):
            m = re.search(r"\n  env: (\w+)", open(p).read())
            return m.group(1) if m else None
    return None


def kendall_tau(a, b):
    common = [x for x in a if x in b]
    pos = {x: i for i, x in enumerate(b)}
    n = len(common)
    if n < 2:
        return None, n
    conc = disc = 0
    for i in range(n):
        for j in range(i + 1, n):
            if pos[common[i]] < pos[common[j]]:
                conc += 1
            else:
                disc += 1
    return (conc - disc) / (conc + disc), n


def main(recipe_path, g00_path, lab="."):
    recipe = yaml.safe_load(open(recipe_path))
    a, b = recipe["gate"]["g00_lines"]
    g00 = open(g00_path, encoding="utf-8").read().splitlines()[a - 1:b]
    text = "\n".join(g00)
    seed = json.load(open(os.path.join(lab, "seed", "extraction_report.json")))
    label_map = seed["label_map"]
    labels = {}
    for code, tex, _, _ in PAPERS:
        labels[code] = read_labels(os.path.join(lab, "seed", "aux_labels",
                                                tex[:-4] + ".labels.txt"))
    cited, outside, mismatches = [], [], []
    for m in LOC_RE.finditer(text):
        code = f"T{int(m.group(1)[1:]):02d}"
        if code not in labels:
            outside.append(f"{m.group(1)} {m.group(2)}")
            continue
        for item in re.split(r",\s*", m.group(2)):
            tw = re.match(r"\s*([A-Za-z]+)\.?~?", item)
            for n in locator_numbers(item):
                lab_ = next((l for l, (num, t, c) in labels[code].items()
                             if num == n and c in TYPE_OF_ENV), None)
                if not lab_:
                    outside.append(f"{m.group(1)} {item} (number not found)")
                    continue
                cid = label_map.get(f"{code}:{lab_}")
                env = _env_of(lab, cid)
                if tw and TYPE_OF_ENV.get(env) and not tw.group(1).startswith(
                        TYPE_OF_ENV[env][:3]):
                    mismatches.append(f"{m.group(1)} {item.strip()}: G00 says "
                                      f"{tw.group(1)}, the paper has a {env}")
                if cid and cid not in cited:
                    cited.append(cid)
    folder = os.path.join(lab, "documents", recipe["doc"])
    blocks = json.load(open(os.path.join(folder, "blocks.json")))
    audit = json.load(open(os.path.join(folder, "audit.json")))
    shown = [b["claim"].split("@")[0] for b in blocks if b["type"] == "theorem"]
    facts = [b["claim"].split("@")[0] for b in blocks if b["type"] == "fact"]
    posts = [b["claim"].split("@")[0] for b in blocks if b["type"] == "postulate"]
    tau, n = kendall_tau(cited, shown)
    extra = [c for c in shown if c not in cited]
    gaps = [b["id"] for b in blocks if b.get("gap")]
    prose = [b for b in blocks if b["type"] in ("transition", "framing", "abstract")]
    loc_lines = sum(1 for line in g00 if "\\loc{" in line)
    narrative = sum(1 for line in g00 if line.strip() and not line.startswith("%")
                    and "\\loc{" not in line and not line.lstrip().startswith("\\"))
    figures = text.count("\\begin{tikzpicture}")
    boxes = len(re.findall(r"\\begin\{(godeeper|keyresult)\}", text))
    # compile the generated LaTeX
    with tempfile.TemporaryDirectory() as tmp:
        tex = os.path.join(tmp, "doc.tex")
        open(tex, "w").write(open(os.path.join(folder, "rendered.tex")).read())
        cp = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                             "doc.tex"], cwd=tmp, capture_output=True, text=True, timeout=180)
        cp = subprocess.run(["pdflatex", "-interaction=nonstopmode", "doc.tex"],
                            cwd=tmp, capture_output=True, text=True, timeout=180)
        ok = os.path.exists(os.path.join(tmp, "doc.pdf"))
        errs = [l for l in cp.stdout.splitlines() if l.startswith("!")]
        undefined = len(re.findall(r"Reference `[^']+' on page \d+ undefined", cp.stdout))
        pages = re.search(r"Output written on doc.pdf \((\d+) pages", cp.stdout)
        if ok:
            os.makedirs(os.path.join(folder, "build"), exist_ok=True)
            import shutil
            shutil.copy(os.path.join(tmp, "doc.pdf"),
                        os.path.join(folder, "build", recipe["doc"] + ".pdf"))
    proofs_eq = proofs_unres = 0
    store = os.path.join(lab, "store", "claims")
    for c in shown:
        ent = open(os.path.join(store, c, "entity.md")).read()
        m = re.search(r"eqrefs: (\d+)", ent)
        proofs_eq += int(m.group(1)) if m else 0
        proofs_unres += ent.count("unresolved_refs")
    from collections import Counter
    codes = Counter(f["code"] for f in audit)
    r = {
        "g00_cited_in_pilot": len(cited), "g00_cited_outside_pilot": outside,
        "locator_type_mismatches": mismatches,
        "generated_shown": len(shown), "generated_cited_facts": len(facts),
        "generated_postulates": posts,
        "extra_prerequisites_not_in_g00": extra,
        "order_agreement_kendall_tau": tau, "order_pairs_compared": n,
        "pending_level_gaps": gaps, "prose_blocks": len(prose),
        "g00_lines_with_locators": loc_lines, "g00_narrative_lines": narrative,
        "g00_figures": figures, "g00_boxes": boxes,
        "latex_compiles": ok, "latex_errors": errs[:5],
        "latex_undefined_refs": undefined,
        "pdf_pages": int(pages.group(1)) if pages else None,
        "shown_claims_with_equation_refs": proofs_eq,
        "shown_claims_with_unresolved_refs": proofs_unres,
        "audit_codes": dict(codes),
    }
    json.dump(r, open(os.path.join(folder, "gate.json"), "w"), indent=1)
    return r


if __name__ == "__main__":
    print(json.dumps(main(*sys.argv[1:3]), indent=1))


def report_md(r_full, r_guide, path):
    def row(k, a, b):
        return f"| {k} | {a} | {b} |"
    lines = ["# Phase 1 gate: regenerating G00's black-hole sections", "",
             "Recipes: recipes/falling-in.yaml (technical guide, prerequisites shown) and "
             "recipes/falling-in-guide.yaml (G00 length: spine shown, the rest cited).", "",
             "| Measure | Full | Guide length |", "| --- | --- | --- |",
             row("G00 results in the pilot (spine)", r_full["g00_cited_in_pilot"], r_guide["g00_cited_in_pilot"]),
             row("Claims shown with proof or rests-on", r_full["generated_shown"], r_guide["generated_shown"]),
             row("Results cited as facts", r_full["generated_cited_facts"], r_guide["generated_cited_facts"]),
             row("Postulates surfaced", len(r_full["generated_postulates"]), len(r_guide["generated_postulates"])),
             row("Order agreement with G00 (Kendall tau)", f"{r_full['order_agreement_kendall_tau']:.2f}",
                 f"{r_guide['order_agreement_kendall_tau']:.2f}"),
             row("Claim blocks with pending text", len(r_full["pending_level_gaps"]), len(r_guide["pending_level_gaps"])),
             row("LaTeX compiles / pages", f"{r_full['latex_compiles']} / {r_full['pdf_pages']}",
                 f"{r_guide['latex_compiles']} / {r_guide['pdf_pages']}"),
             row("LaTeX errors", len(r_full["latex_errors"]), len(r_guide["latex_errors"])),
             row("Audit findings", r_full["audit_codes"], r_guide["audit_codes"]), ""]
    return lines
