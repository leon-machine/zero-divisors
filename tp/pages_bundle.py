"""Assemble the folder a static host serves (Cloudflare Pages for zerodivisors.org) from a built site/.

    python -m tp.pdfs                     # the papers' PDFs, into site/pdf (needs pdflatex)
    python -m tp.site                     # the page and the pages that need no JavaScript
    python -m tp.pages_bundle [--site site] [--out build/pages]
    npx wrangler pages deploy build/pages --project-name zero-divisors --branch main

Run it from the release tag (RELEASING.md, step 5). It copies site/ without the files that only
feed the build (the page templates, the artifact's file list, the recorded check runs, the guides
list), then checks the folder against the host's limits and against what the public site needs:
index.html in standards mode, a 404.html, the PDFs, and the sitemap. It exits non-zero on a
problem, so nothing broken is deployed.

Cloudflare's dashboard upload takes at most 1,000 files, and the site has several thousand, so
deploy with wrangler (docs/HOSTING.md), which takes up to 20,000.
"""
import argparse
import fnmatch
import os
import shutil
import sys

# what only the build reads: never served
EXCLUDE = ("*.template.html", "publish_files.json", "check_runs.json", "guides.yaml")
MAX_FILES = 20000                 # Cloudflare Pages, per deployment (free plan)
MAX_FILE_BYTES = 25 * 1024 * 1024  # Cloudflare Pages, per file


def _skip(rel):
    return "/" not in rel and any(fnmatch.fnmatch(rel, p) for p in EXCLUDE)


def bundle(site="site", out=os.path.join("build", "pages")):
    """Copy site/ into out/ (replacing it) and return (files, problems, notes)."""
    if os.path.abspath(out).startswith(os.path.abspath(site) + os.sep):
        raise SystemExit("--out must not be inside --site")
    shutil.rmtree(out, ignore_errors=True)
    files, big = 0, []
    for root, dirs, names in os.walk(site):
        dirs.sort()
        for n in sorted(names):
            src = os.path.join(root, n)
            rel = os.path.relpath(src, site).replace(os.sep, "/")
            if _skip(rel):
                continue
            dst = os.path.join(out, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
            files += 1
            if os.path.getsize(src) > MAX_FILE_BYTES:
                big.append(rel)
    problems, notes = [], []
    if files > MAX_FILES:
        problems.append(f"{files} files: over the host's limit of {MAX_FILES}")
    for rel in big:
        problems.append(f"{rel} is over 25 MiB, the host's limit per file")
    idx = os.path.join(out, "index.html")
    if not os.path.exists(idx):
        problems.append("no index.html: run python -m tp.site first")
    elif not open(idx, encoding="utf-8").read(64).lstrip().lower().startswith("<!doctype html>"):
        problems.append("index.html does not start with <!DOCTYPE html> (browsers would use quirks mode)")
    if not os.path.exists(os.path.join(out, "404.html")):
        problems.append("no 404.html: unknown addresses would be served the home page")
    if not os.path.exists(os.path.join(out, "sitemap.xml")):
        problems.append("no sitemap.xml: set site_url in store/config.yaml and rebuild")
    pdfs = os.path.join(out, "pdf")
    if not (os.path.isdir(pdfs) and any(f.endswith(".pdf") for f in os.listdir(pdfs))):
        notes.append("no PDFs in site/pdf: the documents will show no PDF link (python -m tp.pdfs, then rebuild)")
    return files, problems, notes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--site", default="site")
    ap.add_argument("--out", default=os.path.join("build", "pages"))
    a = ap.parse_args(argv)
    files, problems, notes = bundle(a.site, a.out)
    size = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(a.out) for f in fs)
    print(f"{a.out}: {files} files, {size / 1e6:.1f} MB")
    for n in notes:
        print("note:", n)
    for p in problems:
        print("problem:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
