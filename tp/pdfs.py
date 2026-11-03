"""Compile the stored documents to PDF for the page (site/pdf/<doc>.pdf).

  python -m tp.pdfs [--docs documents] [--out site/pdf] [--only a,b]

Each document's rendered.tex (written by tp doc / tp regen in the series' paper form) is
compiled twice with pdflatex in a temporary folder. Trails are walks, not papers, and are
skipped. The PDFs are build output: site/pdf is not committed, and tp.site lists whatever
is there for the publish call.
"""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import tempfile

import yaml


def is_paper(folder):
    rp = os.path.join(folder, "recipe.yaml")
    if not os.path.exists(rp) or not os.path.exists(os.path.join(folder, "rendered.tex")):
        return False
    rec = yaml.safe_load(open(rp)) or {}
    name = os.path.basename(folder)
    return not rec.get("trail") and name != "tour" and not name.startswith("trail-")


def compile_one(tex_path, out_pdf):
    with tempfile.TemporaryDirectory() as tmp:
        shutil.copy(tex_path, os.path.join(tmp, "doc.tex"))
        for _ in range(2):
            subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "doc.tex"],
                           cwd=tmp, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=300)
        pdf = os.path.join(tmp, "doc.pdf")
        if not os.path.exists(pdf):
            log = open(os.path.join(tmp, "doc.log"), errors="replace").read()
            err = [ln for ln in log.splitlines() if ln.startswith("! ")][:3]
            return False, "; ".join(err) or "no PDF produced"
        shutil.copy(pdf, out_pdf)
        return True, ""


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--docs", default="documents")
    ap.add_argument("--out", default=os.path.join("site", "pdf"))
    ap.add_argument("--only", default="")
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True)
    only = {x for x in a.only.split(",") if x}
    bad = 0
    for d in sorted(os.listdir(a.docs)):
        f = os.path.join(a.docs, d)
        if (only and d not in only) or not is_paper(f):
            continue
        ok, why = compile_one(os.path.join(f, "rendered.tex"), os.path.join(a.out, d + ".pdf"))
        print(("ok    " if ok else "FAIL  ") + d + ("" if ok else ": " + why))
        bad += not ok
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
