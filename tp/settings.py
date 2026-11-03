"""The running text of the papers, as setting notes.

    python -m tp.settings --suite .. --store store [--papers T01] [--dry-run]

A paper is more than its numbered results: between them runs the text that
introduces notation, motivates the next step and places the work. A recreated
paper without it uses symbols it never introduces. This module stores that
text as notes with status `setting`: one note per run of prose between two
environments (results, proofs, remarks, figures) inside one section or
subsection. A setting note comments on the result it sets up (the next result
in its section; failing that the previous one; failing that the results it
refers to, or the nearest result of the paper). The abstract is stored too,
as a setting note titled "Abstract".

Like every note, a setting asserts nothing the graph relies on: nothing may
use it. Existing notes are never overwritten (a setting is found again by its
paper and line).
"""
from __future__ import annotations

from .credit import for_paper as credit_for_paper
import argparse
import os
import re
import sys

import yaml

from .extract import PAPERS, SYNTHETIC, ENV_KIND, Paper, read_labels, balanced, slug, REF_RE, LABEL_RE
from .model import load_store
from .notes import (store_index, house_words, rewrite_refs, _section_title, _clean_title,
                    paper_files)

REMOVE_ENVS = sorted(set(k for k in ENV_KIND if k != "algorithm") | {
    "remark", "example", "proof", "figure", "figure*", "tikzpicture", "abstract",
    "thebibliography", "keyresult", "godeeper", "titlepage", "wrapfigure"})
HEADING = re.compile(r"\\(section|subsection|subsubsection|paragraph)(\*?)\{")
DROP_LINE = re.compile(r"^\s*\\(maketitle|newpage|clearpage|tableofcontents|appendix|"
                       r"bigskip|medskip|smallskip|vfill|centering|noindent|FloatBarrier|"
                       r"addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}|phantomsection)\s*$", re.M)
MIN_WORDS = 12


def _spans(body, names):
    """Spans of every \\begin{name}...\\end{name}, outermost only."""
    out = []
    pat = re.compile(r"\\begin\{(" + "|".join(re.escape(n) for n in names) + r")\}")
    pos = 0
    while True:
        m = pat.search(body, pos)
        if not m:
            break
        env = m.group(1)
        depth, j = 1, m.end()
        opener, closer = "\\begin{" + env + "}", "\\end{" + env + "}"
        while depth:
            a, b = body.find(opener, j), body.find(closer, j)
            if b < 0:
                b = len(body)
                depth = 0
                break
            if 0 <= a < b:
                depth += 1
                j = a + len(opener)
            else:
                depth -= 1
                j = b + len(closer)
        out.append((m.start(), j, env))
        pos = j
    return out


def _clean(text):
    t = LABEL_RE.sub("", text)
    t = re.sub(r"\\href\{[^}]*\}\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\url\{[^}]*\}", "", t)
    t = re.sub(r"\\verb\*?(.)(.*?)\1", lambda m: "\\texttt{" + re.sub(r"([_&%$#{}])", r"\\\1", m.group(2)) + "}", t)
    t = re.sub(r",?\s*on page~?\s*\\pageref\{[^}]*\}", "", t)
    t = re.sub(r"\bpage~?\s*\\pageref\{([^}]*)\}", r"\\ref{\1}", t)
    t = re.sub(r"\\pageref\{([^}]*)\}", r"\\ref{\1}", t)
    t = DROP_LINE.sub("", t)
    t = re.sub(r"\\(?:vspace|hspace)\*?\{[^}]*\}", "", t)
    t = re.sub(r"\\setlength\{[^}]*\}\{[^}]*\}|\\(?:begingroup|endgroup|normalsize|small|"
               r"footnotesize|large|Large|raggedright|raggedbottom|par)\b\s*", " ", t)
    t = re.sub(r"\\paragraph\*?\{([^}]*)\}", r"\\textbf{\1}", t)
    # tables: keep the tabular, the caption becomes a line of its own
    t = re.sub(r"\\begin\{table\*?\}(\[[^\]]*\])?|\\end\{table\*?\}", "", t)
    t = re.sub(r"\\caption\{", r"\n\n\\emph{", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def _words(t):
    return len(re.findall(r"[A-Za-z]{2,}", re.sub(r"\$[^$]*\$", " ", t)))


def scan(suite, code, tex, labels_dir, by_label, by_line):
    base = os.path.splitext(os.path.basename(tex))[0]
    labels = read_labels(os.path.join(labels_dir, base + ".labels.txt"))
    p = Paper(code, os.path.join(suite, tex), "", labels)
    body = p.body
    line_of = lambda pos: body[:pos].count("\n") + p.preamble.count("\n") + 1
    results = [r for r in by_line.get(code, []) if r[2] != "object"]

    out = []
    # the abstract
    ab = re.search(r"\\begin\{abstract\}(.*?)\\end\{abstract\}", body, re.S)
    if ab:
        out.append({"kind": "abstract", "title": "Abstract", "section": "Abstract",
                    "text": _clean(ab.group(1)), "line": line_of(ab.start()),
                    "start": ab.start(), "end": ab.end()})
    first = HEADING.search(body)
    if not first:
        return out
    stop = min([i for i in (body.find("\\begin{thebibliography}"),
                            body.find("\\end{document}")) if i >= 0] or [len(body)])
    region = (first.start(), stop)
    cut = sorted(s for s in _spans(body, REMOVE_ENVS) if s[1] > region[0] and s[0] < region[1])
    # text the extractor already made an entity of (T01's algorithm section)
    for lab, title, start_marker, end_marker in SYNTHETIC.get(code, []):
        i = body.find(start_marker)
        if i >= 0:
            j = body.find(end_marker, i)
            cut = sorted(cut + [(i + len(start_marker), j if j > 0 else i, "synthetic")])
    heads = [(m.start(), balanced(body, m.end() - 1, "{", "}"), m.group(1), m.group(2))
             for m in HEADING.finditer(body, region[0], region[1])]
    # walk the region, cutting at environments and headings
    bounds = sorted([(s, e, "env") for s, e, _ in cut] + [(s, e, "head") for s, e, _, _ in heads])
    sec, subsec = "", ""
    pos = region[0]
    k = 0

    def flush(a, b):
        nonlocal k
        if b <= a:
            return
        raw = body[a:b]
        text = _clean(raw)
        if _words(text) < MIN_WORDS:
            return
        k += 1
        out.append({"kind": "setting", "section": sec, "subsection": subsec,
                    "title": subsec or sec, "text": text, "line": line_of(a + len(raw) - len(raw.lstrip())),
                    "start": a, "end": b})
    for s, e, what in bounds:
        if s < pos:
            pos = max(pos, e)
            continue
        flush(pos, s)
        if what == "head":
            m = HEADING.match(body, s)
            title = _section_title(body[m.end():e - 1])
            if m.group(1) == "section":
                sec, subsec = title, ""
            elif m.group(1) in ("subsection", "subsubsection"):
                subsec = title
            # \paragraph{X} stays as text
            if m.group(1) == "paragraph":
                pos = s
                continue
        pos = e
    flush(pos, region[1])

    # targets
    head_lines = [line_of(s) for s, e, lvl, _ in heads if lvl in ("section", "subsection")]
    for n in out:
        n["comments_on"] = _targets(n, results, by_label, code, head_lines)
    return out


def _targets(n, results, by_label, code, head_lines):
    after = [r for r in results if r[0] > n["line"]]
    before = [r for r in results if r[0] <= n["line"]]
    refs = []
    for m in REF_RE.finditer(n["text"]):
        for l in m.group(1).split(","):
            t = by_label.get((code, l.strip()))
            if t and t not in refs and not t.startswith("note."):
                refs.append(t)
    if n["kind"] == "abstract":
        return [after[0][1]] if after else refs[:1]
    nxt_head = min([h for h in head_lines if h > n["line"]] or [10 ** 9])
    prv_head = max([h for h in head_lines if h <= n["line"]] or [0])
    out = []
    if after and after[0][0] < nxt_head:          # sets up the next result of its section
        out.append(after[0][1])
    elif before and before[-1][0] >= prv_head:     # or closes its section's last result
        out.append(before[-1][1])
    for r in refs:
        if r not in out:
            out.append(r)
    if not out:
        out = [after[0][1]] if after else ([before[-1][1]] if before else [])
    return out[:4]


def note_id(code, n, used):
    region = next((r for c, t, r, s in PAPERS if c == code), code.lower())
    base = "abstract" if n["kind"] == "abstract" else \
        "setting-" + (slug(_clean_title(n["title"]), maxwords=5) or "text")
    eid = f"note.{region}.{base}"
    i = 2
    while eid in used:
        eid = f"note.{region}.{base}-{i}"
        i += 1
    used.add(eid)
    return eid


def write(store_dir, eid, code, n, subject, session):
    folder = os.path.join(store_dir, "notes", eid)
    if os.path.exists(folder):
        return False
    os.makedirs(folder)
    meta = {"id": eid, "kind": "note", "version": 1,
            "title": n["title"] or "Setting", "status": "setting", "subject": subject,
            "proposed_by": {"kind": "extraction", "session": session},
            "ai_involved": "yes", "credit": credit_for_paper(code),
            "comments_on": n["comments_on"],
            "locators": {"paper": code,
                         "number": "Abstract" if n["kind"] == "abstract" else "Setting",
                         "section": n["section"], "line": n["line"]}}
    if n.get("subsection"):
        meta["locators"]["subsection"] = n["subsection"]
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    open(os.path.join(folder, "entity.md"), "w", encoding="utf-8").write(
        f"---\n{fm}---\n\n## formal\n{n['text']}\n\n## technical\npending\n\n"
        f"## lay\npending\n\n## one-liner\npending\n")
    return True


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="..")
    ap.add_argument("--store", default="store")
    ap.add_argument("--labels-dir", default="seed/aux_labels")
    ap.add_argument("--papers", default="")
    ap.add_argument("--session", default="settings-2026-10-21")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    store = load_store(a.store)
    by_label, by_line = store_index(store)
    used = set(store.entities)
    want = set(filter(None, a.papers.split(",")))
    made = kept = words = 0
    untargeted = []
    for code, tex, region, script in paper_files(a.suite):
        if want and code not in want:
            continue
        have = {int((e.meta.get("locators") or {}).get("line") or 0)
                for e in store.entities.values()
                if e.kind == "note" and e.status == "setting"
                and (e.meta.get("locators") or {}).get("paper") == code}
        for n in scan(a.suite, code, tex, a.labels_dir, by_label, by_line):
            if n["line"] in have:
                kept += 1
                continue
            if not n["comments_on"]:
                # a paper whose results carry no line (T17's table rows): the
                # setting comments on the paper's results it names, else its first
                own = sorted(eid for eid, e in store.entities.items() if e.kind != "note"
                             and (e.meta.get("locators") or {}).get("paper") == code)
                named = [x for x in own if x.split(".")[-1][:12] in n["text"]]
                n["comments_on"] = (named or own)[:1]
            if not n["comments_on"]:
                untargeted.append((code, n["line"]))
                continue
            n["title"], n["text"] = house_words(n["title"]), house_words(n["text"])
            n["text"] = rewrite_refs(n["text"], code, by_label)
            words += _words(n["text"])
            eid = note_id(code, n, used)
            subject = store.entities[n["comments_on"][0]].meta.get("subject")
            if a.dry_run or write(a.store, eid, code, n, subject, a.session):
                made += 1
    print(f"settings written {made}, already present {kept}, without a target "
          f"{len(untargeted)}, words {words}")
    for u in untargeted[:10]:
        print("  no target:", u)
    return 0


if __name__ == "__main__":
    sys.exit(main())
