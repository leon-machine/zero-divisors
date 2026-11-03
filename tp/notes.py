"""Remarks and examples as notes, and the label registry.

    python -m tp.notes --suite .. --store store [--papers T01,T02] [--dry-run]

A note is commentary: a paper's remark or worked example. It comments on the
results it discusses (``comments_on``) and nothing may use it, so it never
changes what the graph proves. Notes are written to store/notes/<id>/ and an
existing note is never overwritten.

The label registry (store/labels.yaml) records, for every \\label in every
paper, what now carries it: an entity of the store, a section (by title), a
table, or an equation stated in the running text (with its LaTeX). The site
and the document generator use it to resolve \\ref and \\eqref that the store
text still carries.
"""
from __future__ import annotations

from .credit import for_paper as credit_for_paper
import argparse
import os
import re
import sys
from collections import defaultdict

import yaml

from .extract import (PAPERS, Paper, read_labels, strip_comments, balanced, slug,
                      REF_RE, EQREF_RE, LABEL_RE)
from .model import load_store

NOTE_ENVS = ("remark", "example")
NOTE_RE = re.compile(r"\\begin\{(remark|example)\}")
LABEL_POS = re.compile(r"\\label\{([^}]+)\}")
SECTION_RE = re.compile(r"\\(section|subsection|subsubsection)\*?\{")
DISPLAY_ENVS = ("equation", "equation*", "align", "align*", "gather", "gather*",
                "multline", "multline*")


def paper_files(suite, extra=()):
    out = list(PAPERS) + list(extra)
    return [(c, t, r, s) for c, t, r, s in out if os.path.exists(os.path.join(suite, t))]


def store_index(store):
    by_label, by_line = {}, defaultdict(list)
    for eid, e in store.entities.items():
        loc = e.meta.get("locators") or {}
        if isinstance(loc, list):
            loc = loc[0] if loc else {}
        code, lab, line = loc.get("paper"), loc.get("label"), loc.get("line")
        if not code:
            continue
        if lab:
            by_label[(code, lab)] = eid
        if line and e.kind != "note":
            by_line[code].append((int(line), eid, e.kind))
    for v in by_line.values():
        v.sort()
    return by_label, by_line


def _envs_with_spans(body, names):
    """-> [(env, start, end, title)] for \\begin{name}..\\end{name}."""
    out = []
    pat = re.compile(r"\\begin\{(" + "|".join(re.escape(n) for n in names) + r")\}")
    for m in pat.finditer(body):
        env = m.group(1)
        j = m.end()
        title = None
        k = j
        while k < len(body) and body[k] in " \t":
            k += 1
        if k < len(body) and body[k] == "[":
            e = balanced(body, k, "[", "]")
            title, j = body[k + 1:e - 1], e
        end = body.find("\\end{" + env + "}", j)
        if end < 0:
            continue
        out.append((env, m.start(), end + len("\\end{" + env + "}"), title, j, end))
    return out


def _line(p, pos):
    return p.body[:pos].count("\n") + p.preamble.count("\n") + 1


def _section_title(t):
    """A section title kept as LaTeX (its maths intact), for the registry."""
    t = re.sub(r"\\label\{[^}]*\}", "", t or "")
    t = re.sub(r"\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{(?:[^{}]|\{[^{}]*\})*\}", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def _clean_title(t):
    t = re.sub(r"\\(Cl|Mat|End|GL|SO|SU|Spin|Pin)\b", r"\1", t or "")
    t = re.sub(r"\\(?:emph|textit|textbf)\{([^}]*)\}", r"\1", t)
    t = re.sub(r"\\[a-zA-Z]+\*?", "", t)
    t = re.sub(r"[{}$]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def scan(suite, code, tex, labels_dir, by_label, by_line):
    """-> (notes, registry entries) for one paper."""
    base = os.path.splitext(os.path.basename(tex))[0]
    labels = read_labels(os.path.join(labels_dir, base + ".labels.txt"))
    p = Paper(code, os.path.join(suite, tex), "", labels)
    body = p.body
    results = by_line.get(code, [])

    def preceding(line):
        prev = [r for r in results if r[0] <= line and r[2] != "object"]
        return prev[-1][1] if prev else None

    def following(line):
        nxt = [r for r in results if r[0] > line and r[2] != "object"]
        return nxt[0][1] if nxt else None

    # sections, for "the section on ..." and for scoping a note to its section
    sections = []
    outline, counters = [], [0, 0]
    for m in SECTION_RE.finditer(body):
        e = balanced(body, m.end() - 1, "{", "}")
        sections.append((m.start(), body[m.end():e - 1]))
        level = m.group(1)
        starred = body[m.start():m.end()].endswith("*{")
        if level == "section":
            if not starred:
                counters = [counters[0] + 1, 0]
            num = "" if starred else str(counters[0])
        elif level == "subsection":
            if not starred:
                counters[1] += 1
            num = "" if starred else f"{counters[0]}.{counters[1]}"
        else:
            continue
        outline.append({"line": _line(p, m.start()), "level": level, "number": num,
                        "title": _section_title(body[m.end():e - 1])})

    def section_start(pos):
        prev = [s for s, _ in sections if s <= pos]
        return prev[-1] if prev else 0

    notes = []
    spans = _envs_with_spans(body, NOTE_ENVS)
    for k, (env, start, end, title, j, jend) in enumerate(spans):
        text = body[j:jend]
        lab = LABEL_RE.search(text)
        label = lab.group(1) if lab else None
        line = _line(p, start)
        targets = []
        for m in REF_RE.finditer(text):
            for l in m.group(1).split(","):
                t = by_label.get((code, l.strip()))
                if t and t not in targets:
                    targets.append(t)
        # the result the note follows, if it is in the same section
        prev = preceding(line)
        if prev:
            pl = next(r[0] for r in results if r[1] == prev)
            if _line(p, section_start(start)) <= pl:
                targets.insert(0, prev) if prev not in targets else None
        if not targets:
            nxt = following(line)
            if nxt:
                targets.append(nxt)
        num = labels.get(label, ("?",))[0] if label else "?"
        notes.append({"code": code, "env": env, "label": label, "number": num,
                      "title": title, "line": line, "text": LABEL_RE.sub("", text).strip(),
                      "comments_on": targets[:4], "start": start, "end": end})

    # registry: every \label in the body
    note_spans = [(n["start"], n["end"], n) for n in notes]
    env_spans = [(x["start"], x["end"], x) for x in p.envs]
    proof_spans = []
    for m in re.finditer(r"\\begin\{proof\}", body):
        end = body.find("\\end{proof}", m.end())
        proof_spans.append((m.start(), end))
    disp = _envs_with_spans(body, DISPLAY_ENVS)
    reg = {}
    for m in LABEL_POS.finditer(body):
        lab, pos = m.group(1), m.start()
        num, ltitle, counter = labels.get(lab, ("?", "", ""))
        rec = {"number": num}
        owner = by_label.get((code, lab))
        if owner:
            rec["entity"] = owner
        elif lab.startswith(("sec:", "subsec:", "ssec:", "app:")) or counter in (
                "section", "subsection", "subsubsection", "appendix"):
            st = [t for s, t in sections if s <= pos]
            rec["section"] = _section_title(st[-1]) if st else _section_title(ltitle)
        else:
            inside = next((x for s, e, x in env_spans if s <= pos < e), None)
            innote = next((n for s, e, n in note_spans if s <= pos < e), None)
            inproof = next(((s, e) for s, e in proof_spans if s <= pos < e), None)
            if inside is not None and by_label.get((code, inside.get("label"))):
                rec["entity"] = by_label[(code, inside["label"])]
            elif innote is not None:
                rec["note"] = (code, innote["label"] or "#%d" % innote["start"])
            elif inproof is not None:
                owner = preceding(_line(p, inproof[0]))
                if owner:
                    rec["entity"] = owner
                    rec["in"] = "proof"
            if counter in ("table",) or lab.startswith("tab:"):
                rec["table"] = _clean_title(ltitle) or lab
                rec["near"] = preceding(_line(p, pos)) or following(_line(p, pos))
            if "entity" not in rec and "note" not in rec:
                d = next((x for x in disp if x[1] <= pos < x[2]), None)
                if d is not None:
                    tex_eq = LABEL_RE.sub("", body[d[4]:d[5]]).strip()
                    rec["display"] = re.sub(r"\s+", " ", tex_eq)
                    rec["near"] = preceding(_line(p, pos)) or following(_line(p, pos))
        rec["kind"] = (counter or lab.split(":", 1)[0])
        reg[f"{code}:{lab}"] = rec
    # the paper's outline, for documents that follow the paper's sections
    reg[f"{code}#outline"] = outline
    return notes, reg


def house_words(t):
    """The house style bans some words that the papers use; notes carry the
    substitute (the paper keeps the original)."""
    if not t:
        return t
    t = re.sub(r"\bHonestly\b", "Plainly", t)
    t = re.sub(r"\bhonestly\b", "plainly", t)
    t = re.sub(r"\bHonest\b", "True", t)
    return re.sub(r"\bhonest\b", "true", t)


def note_id(n, used):
    region = next((r for c, t, r, s in PAPERS if c == n["code"]), n["code"].lower())
    if n["title"]:
        base = slug(_clean_title(n["title"]))
    elif n["label"]:
        base = slug(n["label"].split(":", 1)[-1])
    else:
        base = "%s-%s" % (n["env"], n["line"])
    base = base or n["env"]
    eid = f"note.{region}.{base}"
    i = 2
    while eid in used:
        eid = f"note.{region}.{base}-{i}"
        i += 1
    used.add(eid)
    return eid


def rewrite_refs(text, code, by_label):
    def sub(m):
        outs = []
        for lab in [l.strip() for l in m.group(1).split(",")]:
            t = by_label.get((code, lab))
            outs.append("\\claimref{" + t + "}" if t else "\\ref{" + lab + "}")
        return ", ".join(outs)
    return REF_RE.sub(sub, text)


def write_note(store_dir, eid, n, version_pins, session):
    folder = os.path.join(store_dir, "notes", eid)
    if os.path.exists(folder):
        return False
    os.makedirs(folder)
    title = re.sub(r"\s+", " ", n["title"]).strip() if n["title"] else (
        ("Example" if n["env"] == "example" else "Remark") + " on " + version_pins["title"])
    meta = {
        "id": eid, "kind": "note", "version": 1, "title": title,
        "status": n["env"], "subject": version_pins["subject"],
        "proposed_by": {"kind": "extraction", "session": session},
        "ai_involved": "yes", "credit": credit_for_paper(n["code"]),
        "comments_on": n["comments_on"],
        "locators": {"paper": n["code"], "number": f"{'Ex' if n['env'] == 'example' else 'Rem'} {n['number']}",
                     "label": n["label"], "line": n["line"]},
    }
    if not n["label"]:
        meta["locators"].pop("label")
    fm = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    body = (f"---\n{fm}---\n\n## formal\n{n['text_rewritten']}\n\n## technical\npending\n\n"
            f"## lay\npending\n\n## one-liner\npending\n")
    open(os.path.join(folder, "entity.md"), "w", encoding="utf-8").write(body)
    return True


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite", default="..")
    ap.add_argument("--store", default="store")
    ap.add_argument("--labels-dir", default="seed/aux_labels")
    ap.add_argument("--papers", default="")
    ap.add_argument("--extra", default="", help="code=tex=region=script;... papers not in PAPERS")
    ap.add_argument("--session", default="notes-2026-10-21")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    extra = [tuple(x.split("=")) for x in a.extra.split(";") if x]
    store = load_store(a.store)
    by_label, by_line = store_index(store)
    want = set(filter(None, a.papers.split(",")))
    used = set(store.entities)
    registry_path = os.path.join(a.store, "labels.yaml")
    registry = yaml.safe_load(open(registry_path)) if os.path.exists(registry_path) else {}
    registry = registry or {}
    made, skipped, untargeted = 0, 0, []
    for code, tex, region, script in paper_files(a.suite, extra):
        if want and code not in want:
            continue
        notes, reg = scan(a.suite, code, tex, a.labels_dir, by_label, by_line)
        note_ids = {}
        note_at = {}
        for eid, e in store.entities.items():
            loc = e.meta.get("locators") or {}
            if e.kind == "note" and loc.get("paper") == code:
                note_at[int(loc.get("line") or 0)] = eid
        for n in notes:
            n["title"], n["text"] = house_words(n["title"]), house_words(n["text"])
            existing = (by_label.get((code, n["label"])) if n["label"] else None) \
                or note_at.get(n["line"])
            eid = existing or note_id(n, used)
            note_ids[(code, n["label"] or "#%d" % n["start"])] = eid
            if n["label"]:
                by_label[(code, n["label"])] = eid
        for n in notes:
            eid = note_ids[(code, n["label"] or "#%d" % n["start"])]
            n["text_rewritten"] = rewrite_refs(n["text"], code, by_label)
            if not n["comments_on"]:
                untargeted.append(eid)
                continue
            first = store.entities[n["comments_on"][0]]
            info = {"title": first.title, "subject": first.meta.get("subject")}
            if a.dry_run:
                made += 1
                continue
            if write_note(a.store, eid, n, info, a.session):
                made += 1
            else:
                skipped += 1
        for k, rec in reg.items():
            if isinstance(rec, dict) and "note" in rec:
                rec["entity"] = note_ids.get(tuple(rec.pop("note")))
                if rec["entity"] is None:
                    rec.pop("entity")
            registry[k] = rec
    # labels the extractor resolved to another entity (a Fact that restates
    # a result of an earlier paper is an alias of it, not an entity of its own)
    lm_path = os.path.join(os.path.dirname(a.labels_dir.rstrip("/")), "extraction_report.json")
    if os.path.exists(lm_path):
        import json
        lm = json.load(open(lm_path)).get("label_map") or {}
        tomb_path = os.path.join(a.store, "tombstones.yaml")
        tomb = {t["id"]: t.get("replaced_by") for t in
                (yaml.safe_load(open(tomb_path)) or []) if isinstance(t, dict)} \
            if os.path.exists(tomb_path) else {}
        for k, v in lm.items():
            v = tomb.get(v, v)
            rec = registry.get(k)
            if v in store.entities and (rec is None or (
                    isinstance(rec, dict) and not ({"entity", "section"} & set(rec)))):
                registry.setdefault(k, {})["entity"] = v
    if not a.dry_run:
        with open(registry_path, "w", encoding="utf-8") as f:
            f.write("# Generated by tp.notes: every \\label of the series and what carries it.\n")
            yaml.safe_dump(registry, f, sort_keys=True, allow_unicode=True, width=120)
    print(f"notes written {made}, already present {skipped}, with no target {len(untargeted)}")
    for u in untargeted[:20]:
        print("  no target:", u)
    kinds = defaultdict(int)
    for rec in registry.values():
        if not isinstance(rec, dict):
            continue
        kinds["entity" if "entity" in rec else "section" if "section" in rec else
              "display" if "display" in rec else "table" if "table" in rec else "other"] += 1
    print("registry:", dict(kinds))
    return 0


if __name__ == "__main__":
    sys.exit(main())
