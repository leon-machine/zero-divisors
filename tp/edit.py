"""Structured edits of entity.md (roadmap item 1). `tp sign` is retired: human sign-off is
recorded through reviews sealed by ORCID (tp/reviews.py, docs/REVIEWS.md).

  tp bump       <id> --note "<sentence>" [--by maintainer-YYYY-MM-DD]
  tp note       <id> "<text>"                     [--by ...]
  tp wire-check <id>
  tp restate    <id> --level formal|technical|lay|one-liner|title --from FILE --note "<why>"

Every command also takes --store (default store) and --date YYYY-MM-DD (default today).

The bump rule (the store's rule for maintainer edits): one version bump per session between
locks. An entity whose version is above the one recorded for it in store/.tp-lock.json (the
accepted state `tp lock` writes) has already been bumped: the version is kept and the sentence
is appended to today's maintainer note, or to a new one. Otherwise the version goes up by one
and the note records "Version n -> n+1.". An entity with no lock entry falls back to a date
rule: already bumped if its `extraction` block holds a note dated today that records a change
(any dated entry, unless it only says "Version kept at n"). Either way, a sign-off of the
current version forces a new version for any further change. New notes are `maintainer_pass`,
else `maintainer_pass_2`, ...

Edits are made on the text of the front matter, line by line, so everything not changed
(comments, quoting, key order, the level sections) stays byte for byte as it was. After
each edit the file is parsed again, compared with the intended result, validated against
tp.schema.ENTITY and the store's layer-1 rules for that entity, and restored on failure.
"""
from __future__ import annotations

import argparse
import ast
import copy
import json
import datetime
import os
import re
import sys

import yaml

from .model import (ENTITY_DIRS, ENTITY_FILE, LEVELS, SECTION_RE, Entity, Store,
                    load_entity, parse_entity_text)
from .schema import ENTITY

TRUST_ORDER = ("ai-proposed", "ai-refereed", "human-read", "human-checked", "published")
SIGNED_LEVELS = ("human-read", "human-checked")
# a version bump voids sign-offs of the old version; a human trust level they supported
# drops to the floor until someone signs the new version (validator rule E120)
TRUST_FLOOR = "ai-proposed"
TOP_KEY_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_-]*):(?:[ \t]|$)")
SUB_KEY_RE = re.compile(r"^( *)([A-Za-z0-9_][A-Za-z0-9_.-]*):(?:[ \t]|$)")
PLAIN_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._@-]*$")


class Refused(Exception):
    pass


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def sq(s) -> str:
    """A single-line, single-quoted YAML scalar."""
    s = " ".join(str(s).split())
    return "'" + s.replace("'", "''") + "'"


def scalar(s) -> str:
    """Plain if that reads back as the same string, else single-quoted."""
    s = str(s)
    if "\n" not in s and s == s.strip() and s:
        try:
            if yaml.safe_load(f"k: {s}") == {"k": s} and "#" not in s:
                return s
        except yaml.YAMLError:
            pass
    return sq(s)


def _indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _blank(line: str) -> bool:
    return not line.strip()


def find_folder(store: str, eid: str) -> str:
    for sub in ENTITY_DIRS.values():
        p = os.path.join(store, sub, eid)
        if os.path.isfile(os.path.join(p, ENTITY_FILE)):
            return p
    raise Refused(f"no entity {eid!r} in {store}")


def split_doc(text: str):
    """entity.md text -> (head lines, tail). The head is the front matter between the
    opening `---` line and the closing one; tail starts with the closing `---`."""
    if not text.startswith("---\n"):
        raise Refused("entity.md does not start with a front matter line")
    k = text.find("\n---", 3)
    if k < 0:
        raise Refused("unterminated front matter")
    return text[4:k + 1].splitlines(True), text[k + 1:]


def join_doc(lines, tail) -> str:
    return "---\n" + "".join(lines) + tail


def top_spans(lines):
    """[(key, start, end)] of the top-level keys; end is exclusive, trailing blank lines
    are left out."""
    starts = [(i, TOP_KEY_RE.match(ln).group(1)) for i, ln in enumerate(lines)
              if TOP_KEY_RE.match(ln)]
    out = []
    for n, (i, key) in enumerate(starts):
        j = i + 1
        limit = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        while j < limit:
            ln = lines[j]
            if not _blank(ln) and ln[0] not in " -\t":
                break       # a column-0 comment or anything else ends the value
            j += 1
        while j > i + 1 and _blank(lines[j - 1]):
            j -= 1
        out.append((key, i, j))
    return out


def top_span(lines, key):
    for k, i, j in top_spans(lines):
        if k == key:
            return i, j
    return None


def _inline_value(line: str) -> str:
    """What follows `key:` on its own line, comments dropped."""
    v = line.split(":", 1)[1].strip()
    return "" if v.startswith("#") else v


def child_spans(lines, i, j):
    """Children of the block mapping in lines[i+1:j] -> (indent, [(key, start, end)])."""
    body = [n for n in range(i + 1, j) if not _blank(lines[n])
            and not lines[n].lstrip().startswith("#")]
    if not body:
        return None, []
    ind = _indent(lines[body[0]])
    starts = []
    for n in range(i + 1, j):
        m = SUB_KEY_RE.match(lines[n])
        if m and len(m.group(1)) == ind:
            starts.append((n, m.group(2)))
    out = []
    for k, (n, key) in enumerate(starts):
        e = starts[k + 1][0] if k + 1 < len(starts) else j
        while e > n + 1 and _blank(lines[e - 1]):
            e -= 1
        out.append((key, n, e))
    return ind, out


def _parse_meta(text):
    meta, levels, errs = parse_entity_text(text)
    if errs:
        raise Refused("; ".join(errs))
    return meta, levels


def today_str(a) -> str:
    if getattr(a, "date", None):
        try:
            datetime.date.fromisoformat(a.date)
        except ValueError:
            raise Refused(f"--date {a.date!r} is not YYYY-MM-DD")
        return a.date
    return datetime.date.today().isoformat()


def _house_style(text: str, store: str):
    if "—" in text:
        raise Refused("note text: em dash; use a comma, colon or brackets")
    cfg = {}
    p = os.path.join(store, "config.yaml")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as fh:
            cfg = yaml.safe_load(fh) or {}
    for w in (cfg.get("house_style") or {}).get("banned_words", []) or []:
        if re.search(r"\b" + re.escape(w) + r"\b", text, re.I):
            raise Refused(f"note text: banned word {w!r}")


# ---------------------------------------------------------------------------
# validation and the guarded write
# ---------------------------------------------------------------------------

def _layer1_findings(folder: str, store: str):
    """Layer-1 findings of this one entity, with the store's config and notation."""
    try:
        from . import validate as V
    except ImportError:          # no jsonschema: the schema check below is skipped too
        return set()
    def _y(name, default):
        p = os.path.join(store, name)
        if not os.path.exists(p):
            return default
        with open(p, encoding="utf-8") as fh:
            return yaml.safe_load(fh) or default
    ent = load_entity(folder)
    st = Store(root=store, entities={ent.id or "?": ent}, config=_y("config.yaml", {}),
               tombstones=set(), notation=_y("notation.yaml", {}), lock={}, duplicates=[])
    rep = V.Report()
    V.layer1(st, rep)
    return {(f.code, f.message) for f in rep.errors()}


def _schema_errors(meta):
    try:
        import jsonschema
    except ImportError:
        miss = [k for k in ENTITY["required"] if k not in meta]
        extra = [k for k in meta if k not in ENTITY["properties"]]
        return [f"missing {k}" for k in miss] + [f"unknown field {k}" for k in extra]
    v = jsonschema.Draft7Validator(ENTITY)
    return [f"{'/'.join(map(str, e.absolute_path)) or 'front matter'}: {e.message}"
            for e in v.iter_errors(meta)]


def commit(folder, store, eid, old_text, new_text, expect_meta, expect_levels):
    """Write new_text, then check it parses to exactly the intended meta and levels, meets
    the schema and adds no layer-1 error; restore old_text otherwise."""
    path = os.path.join(folder, ENTITY_FILE)
    before = _layer1_findings(folder, store)
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(new_text)
    try:
        meta, levels = _parse_meta(new_text)
        probs = []
        if meta != expect_meta:
            diff = sorted(k for k in set(meta) | set(expect_meta)
                          if meta.get(k) != expect_meta.get(k))
            probs.append("the edited front matter does not read back as intended "
                         f"(fields {', '.join(diff)}); nothing changed")
        if levels != expect_levels:
            probs.append("the level sections do not read back as intended; nothing changed")
        probs += [f"schema: {m}" for m in _schema_errors(meta)]
        if not probs:
            new = _layer1_findings(folder, store) - before
            probs += [f"{c} {m}" for c, m in sorted(new)]
    except Refused as exc:
        probs = [str(exc)]
    except Exception as exc:     # never leave a broken file behind
        probs = [f"{type(exc).__name__}: {exc}"]
    if probs:
        with open(path, "w", encoding="utf-8", newline="") as fh:
            fh.write(old_text)
        raise Refused("; ".join(probs))


# ---------------------------------------------------------------------------
# the maintainer note and the bump rule
# ---------------------------------------------------------------------------

def _is_maint(key, d):
    return key.startswith("maintainer") or str(d.get("by", "")).startswith("maintainer")


def _records_change(d, v):
    note = str(d.get("note", ""))
    return f"-> {v}" in note or "version kept" not in note.lower()


def locked_version(store, eid):
    """The version recorded for eid in the store's lock (store/.tp-lock.json, the accepted
    state tp lock writes), or None when the entity has no lock entry."""
    p = os.path.join(store, ".tp-lock.json")
    if not os.path.exists(p):
        return None
    try:
        with open(p, encoding="utf-8") as fh:
            entry = (json.load(fh) or {}).get(eid)
        return int(entry["version"]) if isinstance(entry, dict) else None
    except (ValueError, KeyError, TypeError):
        return None


def apply_note(lines, meta, sentence, *, today, by, bump, locked=None):
    """Apply the bump rule (bump=True) or add a note without a version change.
    `locked` is the entity's version in the lock: the entity counts as already bumped when
    its version is above it (one bump per session between locks); with no lock entry the
    date rule decides. Returns (lines, meta, message); meta is the intended parsed result."""
    meta = copy.deepcopy(meta)
    lines = list(lines)
    v = int(meta.get("version") or 1)
    ext = meta.get("extraction")
    if ext is not None and not isinstance(ext, dict):
        raise Refused("extraction is not a mapping")
    ext = ext or {}
    dated = [(k, d) for k, d in ext.items()
             if isinstance(d, dict) and str(d.get("date", "")) == today]
    if locked is not None:
        changed_today = v > locked
        since = f"since the lock (version {locked})"
    else:
        changed_today = any(_records_change(d, v) for _, d in dated)
        since = "today"
    if bump and any(isinstance(so, dict) and so.get("version") == v
                    for so in meta.get("signoffs") or []):
        # someone signed this version: a further change needs a new version regardless
        changed_today = False
    mine = [(k, d) for k, d in dated if _is_maint(k, d)]
    sentence = " ".join(sentence.split())
    if sentence and sentence[-1] not in ".!?":
        sentence += "."
    new_v = v + 1 if bump and not changed_today else v
    span = top_span(lines, "extraction")
    target = None
    if mine:
        # today's maintainer note, preferring the one that recorded a change
        target = max(mine, key=lambda kd: (_records_change(kd[1], v), "note" in kd[1]))
    trust_from = None
    if new_v != v and meta.get("trust") in SIGNED_LEVELS:
        signed = [so.get("level") for so in meta.get("signoffs") or []
                  if isinstance(so, dict) and so.get("version") == new_v]
        if meta["trust"] not in signed and not (meta["trust"] == "human-read"
                                                and "human-checked" in signed):
            trust_from = meta["trust"]
    if new_v != v:
        text = f"{sentence} Version {v} -> {new_v}."
        if trust_from:
            text += (f" Trust lowered from {trust_from} to {TRUST_FLOOR}: the sign-offs are"
                     f" for version {v}.")
    elif not bump and not changed_today and not (
            target and "version kept" in str(target[1].get("note", "")).lower()):
        text = f"{sentence} Version kept at {v}."
    else:
        text = sentence
    if target:
        key, d = target
        old = str(d.get("note", "")).strip()
        newnote = f"{old} {text}" if old else text
        lines = _set_child_note(lines, span, key, newnote)
        meta["extraction"][key]["note"] = " ".join(newnote.split())
        where = f"note appended to extraction.{key}"
    else:
        taken = set(ext)
        key = "maintainer_pass"
        n = 2
        while key in taken:
            key, n = f"maintainer_pass_{n}", n + 1
        lines = _add_child(lines, span, key, by, today, text)
        new_ext = {key: {"by": by, "date": today, "note": " ".join(text.split())}}
        new_ext.update(meta.get("extraction") or {})
        meta["extraction"] = new_ext
        where = f"new note extraction.{key}"
    if new_v != v:
        lines = _set_version(lines, new_v)
        meta["version"] = new_v
        vmsg = f"version {v} -> {new_v}"
        if trust_from:
            lines = _set_top_scalar(lines, "trust", TRUST_FLOOR)
            meta["trust"] = TRUST_FLOOR
            vmsg += f", trust {trust_from} -> {TRUST_FLOOR}"
    else:
        vmsg = f"version {v} kept" + (f" (already changed {since})" if bump else "")
    return lines, meta, f"{vmsg}; {where}"


def _set_version(lines, new_v):
    span = top_span(lines, "version")
    if not span:
        raise Refused("no version line")
    i, j = span
    if j != i + 1:
        raise Refused("version is not on one line")
    lines[i] = re.sub(r"^version:(\s*)\d+", lambda m: f"version:{m.group(1)}{new_v}", lines[i])
    return lines


def _child_lines(ind, key, by, today, note):
    p, q = " " * ind, " " * (ind + 2)
    return [f"{p}{key}:\n", f"{q}by: {scalar(by)}\n", f"{q}date: '{today}'\n",
            f"{q}note: {sq(note)}\n"]


def _add_child(lines, span, key, by, today, note):
    if span is None:
        while lines and _blank(lines[-1]):
            lines.pop()
        return lines + ["extraction:\n"] + _child_lines(2, key, by, today, note)
    i, j = span
    if _inline_value(lines[i]) not in ("", "{}", "null", "~"):
        raise Refused("extraction is written in flow style; edit it by hand once")
    ind, kids = child_spans(lines, i, j)
    ind = ind or 2
    if _inline_value(lines[i]):
        lines[i] = "extraction:\n"
    return lines[:i + 1] + _child_lines(ind, key, by, today, note) + lines[i + 1:]


def _set_child_note(lines, span, key, note):
    i, j = span
    ind, kids = child_spans(lines, i, j)
    for k, a, b in kids:
        if k != key:
            continue
        if _inline_value(lines[a]):
            raise Refused(f"extraction.{key} is written in flow style; edit it by hand once")
        sub = [n for n in range(a + 1, b) if not _blank(lines[n])]
        sind = _indent(lines[sub[0]]) if sub else ind + 2
        for n in range(a + 1, b):
            m = SUB_KEY_RE.match(lines[n])
            if m and len(m.group(1)) == sind and m.group(2) == "note":
                e = n + 1
                while e < b and (_blank(lines[e]) or _indent(lines[e]) > sind):
                    e += 1
                while e > n + 1 and _blank(lines[e - 1]):
                    e -= 1
                return lines[:n] + [f"{' ' * sind}note: {sq(note)}\n"] + lines[e:]
        return lines[:b] + [f"{' ' * sind}note: {sq(note)}\n"] + lines[b:]
    raise Refused(f"extraction.{key} not found in the text")


# ---------------------------------------------------------------------------
# checked_by
# ---------------------------------------------------------------------------

CHECK_PREFIXES = ("check_", "test_")


def check_functions(path):
    """Top-level check_/test_ functions of a check file, in source order. One that another
    check function calls is a helper and is left out (a run() or __main__ block that calls
    the checks does not count)."""
    with open(path, encoding="utf-8") as fh:
        tree = ast.parse(fh.read(), filename=path)
    tops = [n for n in tree.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
    cands = [n.name for n in tops if n.name.startswith(CHECK_PREFIXES)]
    called = set()
    for n in tops:
        if n.name.startswith(CHECK_PREFIXES):
            called |= {x.id for x in ast.walk(n) if isinstance(x, ast.Name) and x.id != n.name}
    return [f for f in cands if f not in called]


def _is_own_check(e):
    return isinstance(e, dict) and e.get("kind") == "check" \
        and str(e.get("ref", "")).startswith("check.py::")


def set_checked_by(lines, old_list, fns):
    """Rewrite checked_by so its check.py entries are exactly fns, in order, after the
    other entries. Returns (lines, new_list)."""
    own = [e["ref"].split("::", 1)[1] for e in old_list if _is_own_check(e)]
    if own == list(fns):
        # already in step: other entries may sit between the checks; that is left alone
        return lines, old_list
    keep = [e for e in old_list if not _is_own_check(e)]
    have = {}
    for e in old_list:
        if _is_own_check(e):
            have.setdefault(e["ref"].split("::", 1)[1], e)
    new_list = keep + [have.get(f, {"kind": "check", "ref": f"check.py::{f}"}) for f in fns]
    span = top_span(lines, "checked_by")
    if span is None:
        if not new_list:
            return lines, new_list
        block = ["checked_by:\n"] + _ev_lines(0, new_list)
        at = None
        sp = top_span(lines, "derivations")
        if sp:
            at = sp[1]
        else:
            for k in ("locators", "extraction"):
                sp = top_span(lines, k)
                if sp:
                    at = sp[0]
                    break
        if at is None:
            while lines and _blank(lines[-1]):
                lines.pop()
            at = len(lines)
        return lines[:at] + block + lines[at:], new_list
    i, j = span
    if not new_list:
        return lines[:i] + ["checked_by: []\n"] + lines[j:], new_list
    if _inline_value(lines[i]):
        # flow style: written fresh in block style
        return lines[:i] + ["checked_by:\n"] + _ev_lines(0, new_list) + lines[j:], new_list
    items = [n for n in range(i + 1, j) if lines[n].lstrip(" ").startswith("-")
             and not lines[n].lstrip(" ").startswith("--")]
    if not items:
        return lines[:i] + ["checked_by:\n"] + _ev_lines(0, new_list) + lines[j:], new_list
    d = _indent(lines[items[0]])
    starts = [n for n in items if _indent(lines[n]) == d]
    pre = lines[i + 1:starts[0]]
    chunks = []
    for k, s in enumerate(starts):
        e = starts[k + 1] if k + 1 < len(starts) else j
        txt = "".join(lines[s:e])
        parsed = yaml.safe_load(txt)
        if not (isinstance(parsed, list) and len(parsed) == 1):
            raise Refused("checked_by has an entry the editor cannot read")
        chunks.append((parsed[0], lines[s:e]))
    out_keep = [c for p, c in chunks if not _is_own_check(p)]
    by_fn = {}
    for p, c in chunks:
        if _is_own_check(p):
            by_fn.setdefault(p["ref"].split("::", 1)[1], c)
    body = [ln for c in out_keep for ln in c]
    for f in fns:
        body += by_fn.get(f) or _ev_lines(d, [{"kind": "check", "ref": f"check.py::{f}"}])
    if body and not body[-1].endswith("\n"):
        body[-1] += "\n"
    return lines[:i + 1] + pre + body + lines[j:], new_list


def _ev_lines(d, entries):
    out = []
    p = " " * d
    for e in entries:
        first = True
        for k, val in e.items():
            lead = f"{p}- " if first else f"{p}  "
            if isinstance(val, list):
                out.append(f"{lead}{k}:\n")
                out += [f"{p}  - {scalar(x)}\n" for x in val]
            else:
                out.append(f"{lead}{k}: {scalar(val)}\n")
            first = False
    return out


# ---------------------------------------------------------------------------
# levels, title, trust
# ---------------------------------------------------------------------------

def set_level(tail, level, text):
    """tail starts with the closing '---' line; replace one ## section's text."""
    head, body = tail.split("\n", 1) if "\n" in tail else (tail, "")
    marks = list(SECTION_RE.finditer(body))
    for k, m in enumerate(marks):
        if m.group(1) != level:
            continue
        end = marks[k + 1].start() if k + 1 < len(marks) else len(body)
        region = body[m.end():end]
        lead = re.match(r"\n*", region).group(0) or "\n"
        trail = re.search(r"\n*$", region).group(0)
        if k + 1 < len(marks):
            trail = trail if len(trail) >= 2 else "\n\n"
        else:
            trail = trail or "\n"
        return head + "\n" + body[:m.end()] + lead + text + trail + body[end:]
    # absent: insert before the next level in order, else at the end
    after = LEVELS[LEVELS.index(level) + 1:]
    for m in marks:
        if m.group(1) in after:
            at = m.start()
            return head + "\n" + body[:at] + f"## {level}\n{text}\n\n" + body[at:]
    sep = "" if body.endswith("\n\n") or not body else ("\n" if body.endswith("\n") else "\n\n")
    return head + "\n" + body + sep + f"## {level}\n{text}\n"


def _set_top_scalar(lines, key, value, after=("review", "ai_involved")):
    span = top_span(lines, key)
    line = f"{key}: {scalar(value)}\n"
    if span:
        i, j = span
        return lines[:i] + [line] + lines[j:]
    for k in after:
        sp = top_span(lines, k)
        if sp:
            return lines[:sp[1]] + [line] + lines[sp[1]:]
    while lines and _blank(lines[-1]):
        lines.pop()
    return lines + [line]


def _load(a):
    folder = find_folder(a.store, a.id)
    path = os.path.join(folder, ENTITY_FILE)
    with open(path, encoding="utf-8", newline="") as fh:
        text = fh.read()
    meta, levels = _parse_meta(text)
    if meta.get("id") != a.id:
        raise Refused(f"{path} carries id {meta.get('id')!r}")
    lines, tail = split_doc(text)
    return folder, text, meta, levels, lines, tail


def _lint_before_bump(store, folder):
    """A version bump records a finished change: refuse it while the entity's check is broken
    (tp lint's evidence errors: a check that fails, does not parse, asserts nothing, uses floats,
    touches an undeclared premise, or a payload clause that is not True). Text errors are left to
    tp lint and tp check."""
    if not os.path.exists(os.path.join(folder, "check.py")):
        return
    from . import lint
    ctx = lint.store_context(store)
    _, findings, _ = lint.lint_entity(ctx, folder, run=True)
    errs = [f for f in findings if f.severity == "error" and f.code[:2] in ("E4", "L5")
            and not f.message.startswith("legacy")]      # the paper's scripts are not this edit
    if errs:
        raise Refused("tp lint finds " + "; ".join(f"{f.code} {f.message}" for f in errs[:3])
                      + " (fix it first, or pass --no-lint)")


def cmd_bump(a, bump=True):
    today = today_str(a)
    kind = getattr(a, "kind", None)
    if kind and not re.match(r"^(Correction|Change|Wording):", a.note.strip(), re.I):
        a.note = kind.capitalize() + ": " + a.note.strip()
    _house_style(a.note, a.store)
    folder, text, meta, levels, lines, tail = _load(a)
    if bump and not getattr(a, "no_lint", False):
        _lint_before_bump(a.store, folder)
    by = a.by or f"maintainer-{today}"
    lines, expect, msg = apply_note(lines, meta, a.note, today=today, by=by, bump=bump,
                                  locked=locked_version(a.store, a.id))
    commit(folder, a.store, a.id, text, join_doc(lines, tail), expect, levels)
    return f"{a.cmd} {a.id}: {msg}"


def cmd_wire(a):
    today = today_str(a)
    folder, text, meta, levels, lines, tail = _load(a)
    cp = os.path.join(folder, "check.py")
    if not os.path.exists(cp):
        raise Refused(f"{a.id} has no check.py")
    try:
        fns = check_functions(cp)
    except SyntaxError as exc:
        raise Refused(f"check.py does not parse: {exc}")
    old = list(meta.get("checked_by") or [])
    lines, new = set_checked_by(lines, old, fns)
    if new == old:
        return f"wire-check {a.id}: checked_by already matches check.py ({len(fns)} check(s)); no change"
    old_fns = [e["ref"].split("::", 1)[1] for e in old if _is_own_check(e)]
    added = [f for f in fns if f not in old_fns]
    removed = [f for f in old_fns if f not in fns]
    note = f"Check entries synced with check.py: +{len(added)}, -{len(removed)}"
    detail = []
    if added:
        detail.append("added " + ", ".join(added))
    if removed:
        detail.append("removed " + ", ".join(dict.fromkeys(removed)))
    if not added and not removed:
        detail.append("reordered to source order")
    note += " (" + "; ".join(detail) + ")."
    expect = copy.deepcopy(meta)
    expect["checked_by"] = new
    lines, expect2, msg = apply_note(lines, expect, note, today=today,
                                     locked=locked_version(a.store, a.id), by=a.by or f"maintainer-{today}", bump=True)
    commit(folder, a.store, a.id, text, join_doc(lines, tail), expect2, levels)
    return f"wire-check {a.id}: +{len(added)} -{len(removed)} check entries; {msg}"


def cmd_restate(a):
    today = today_str(a)
    _house_style(a.note, a.store)
    with open(a.source, encoding="utf-8") as fh:
        new = fh.read().strip("\n").rstrip()
    if not new.strip():
        raise Refused(f"{a.source} is empty")
    folder, text, meta, levels, lines, tail = _load(a)
    expect = copy.deepcopy(meta)
    exp_levels = dict(levels)
    if a.level == "title":
        if "\n" in new:
            raise Refused("a title is one line")
        if new == meta.get("title"):
            return f"restate {a.id}: title unchanged; no change"
        lines = _set_top_scalar(lines, "title", new)
        expect["title"] = new
    else:
        if SECTION_RE.search(new) or re.search(r"^---", new, re.M):
            raise Refused(f"{a.source} contains a section heading or a '---' line")
        if levels.get(a.level, "").strip("\n") == new:
            return f"restate {a.id}: {a.level} level unchanged; no change"
        tail = set_level(tail, a.level, new)
        exp_levels[a.level] = new
    what = "Title" if a.level == "title" else f"The {a.level} level"
    why = a.note.strip()
    note = f"{what} restated: {why}"
    lines, expect, msg = apply_note(lines, expect, note, today=today,
                                    locked=locked_version(a.store, a.id), by=a.by or f"maintainer-{today}", bump=True)
    commit(folder, a.store, a.id, text, join_doc(lines, tail), expect, exp_levels)
    return f"restate {a.id}: {a.level} replaced; {msg}"


def _parser(cmd):
    ap = argparse.ArgumentParser(prog=f"tp {cmd}")
    ap.add_argument("id")
    ap.add_argument("--store", default="store")
    ap.add_argument("--date", default=None, help="YYYY-MM-DD (default today)")
    if cmd == "bump":
        ap.add_argument("--note", required=True)
        ap.add_argument("--kind", choices=("correction", "change", "wording"), default=None,
                        help="what the edit is to a reader of the deposited paper; recorded as the "
                             "note's first word, which tp.deposits reads to class the revision")
        ap.add_argument("--by", default=None)
        ap.add_argument("--no-lint", action="store_true",
                        help="bump even if tp lint finds an error")
    elif cmd == "note":
        ap.add_argument("note")
        ap.add_argument("--by", default=None)
    elif cmd == "wire-check":
        ap.add_argument("--by", default=None)
    elif cmd == "restate":
        ap.add_argument("--level", required=True,
                        choices=list(LEVELS) + ["title"])
        ap.add_argument("--from", dest="source", required=True)
        ap.add_argument("--note", required=True)
        ap.add_argument("--by", default=None)
    return ap


def main(argv):
    cmd = argv[0]
    a = _parser(cmd).parse_args(argv[1:])
    a.cmd = cmd
    try:
        if cmd == "bump":
            out = cmd_bump(a, bump=True)
        elif cmd == "note":
            out = cmd_bump(a, bump=False)
        elif cmd == "wire-check":
            out = cmd_wire(a)
        elif cmd == "restate":
            out = cmd_restate(a)
        else:
            print(f"tp: unknown edit command {cmd!r}")
            return 1
    except Refused as exc:
        print(f"{cmd} {getattr(a, 'id', '')}: refused: {exc}")
        return 1
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
