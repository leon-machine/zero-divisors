"""The validator: six layers, cheapest first.

`validate(store)` returns a Report.  Layers run in order and the run stops
after the first layer that produced an error (unless keep_going=True, which
the build uses to report everything at once).
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from fractions import Fraction

import jsonschema

from . import derive, evidence, latexcheck
from .model import DERIVED_FIELDS, LEVELS, Store, lock_entry, parse_pin
from .schema import ENTITY, STATUSES

LAYER_NAMES = {1: "shape", 2: "references", 3: "whole store", 4: "evidence",
               5: "meaning", 6: "people"}


@dataclass
class Finding:
    code: str
    entity: str
    message: str
    fix: str = ""

    @property
    def severity(self) -> str:
        return {"E": "error", "W": "warning", "I": "info"}[self.code[0]]

    @property
    def layer(self) -> int:
        return int(self.code[1])

    def render(self) -> str:
        out = f"{self.code}  {self.entity}\n      {self.message}"
        if self.fix:
            out += f"\n      fix:   {self.fix}"
        return out


@dataclass
class Report:
    findings: list = field(default_factory=list)
    layers_run: list = field(default_factory=list)
    eff: dict = field(default_factory=dict)
    ledger: dict = field(default_factory=dict)
    graph: dict = field(default_factory=dict)
    check_results: dict = field(default_factory=dict)   # id -> "pass"/"fail"/...
    check_failed: set = field(default_factory=set)
    impact: dict = field(default_factory=dict)
    past: dict = field(default_factory=dict)
    future: dict = field(default_factory=dict)

    def add(self, code, entity, message, fix=""):
        self.findings.append(Finding(code, entity, message, fix))

    def errors(self):
        return [f for f in self.findings if f.severity == "error"]

    def by_code(self):
        return Counter(f.code for f in self.findings)


# ---------------------------------------------------------------------------
# layer 1: shape
# ---------------------------------------------------------------------------

_validator = jsonschema.Draft7Validator(ENTITY)


TITLE_MAX = 90   # a title names the result; the statement belongs in the levels


def _schema_code(err) -> str:
    path = list(err.absolute_path)
    if err.validator == "required":
        return "E102"
    if path[:1] == ["id"]:
        return "E103"
    if path[:1] == ["kind"]:
        return "E104"
    if err.validator == "pattern" and "@" in str(err.schema.get("pattern", "")):
        return "E115"
    return "E116"


def _texts(e):
    """(where, text) pairs subject to LaTeX and house-style checks."""
    out = [("title", str(e.meta.get("title") or ""))]
    out += [(f"level {lv}", e.levels.get(lv) or "") for lv in LEVELS]
    out += [(f"proof {k}", v) for k, v in e.proofs.items()]
    return out


def _note_texts(e):
    """(where, text) pairs for the free-text notes in the front matter (maintainer, review and
    decision notes): plain text, so only the house-style rules apply to them, not LaTeX."""
    out = []

    def walk(x, path):
        if isinstance(x, dict):
            for k, v in x.items():
                if k in ("note", "notes", "reason") and isinstance(v, str):
                    out.append((f"note {path}/{k}".replace(" /", " "), v))
                else:
                    walk(v, f"{path}/{k}")
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{path}[{i}]")

    walk(e.meta, "")
    return out


DASH_RE = re.compile(r"—|(?<![-!])---(?!-)")


def layer1(store: Store, rep: Report):
    banned = [w.lower() for w in
              (store.config.get("house_style") or {}).get("banned_words", [])]
    banned_re = re.compile(r"\b(" + "|".join(map(re.escape, banned)) + r")\b", re.I) \
        if banned else None
    for eid, e in store.entities.items():
        for msg in e.parse_errors:
            rep.add(msg[:4], eid, msg[5:])
        if e.parse_errors:
            continue
        for err in _validator.iter_errors(e.meta):
            loc = "/".join(map(str, err.absolute_path)) or "front matter"
            fix = ("YAML reads a bare yes, no, on or off as true or false: write 'yes' or 'no' in quotes"
                   if isinstance(err.instance, bool) else "")
            rep.add(_schema_code(err), eid, f"{loc}: {err.message}", fix)
        tl = len(str(e.meta.get("title") or ""))
        if tl > TITLE_MAX:
            rep.add("E124", eid, f"title is {tl} characters, over {TITLE_MAX}: it states the result instead of naming it",
                    "write a short name, as a theorem is named in a paper; the claim itself goes in the one-liner and formal levels")
        if e.kind in STATUSES and e.status not in STATUSES[e.kind]:
            rep.add("E105", eid, f"status '{e.status}' is not allowed for a {e.kind}",
                    f"use one of {', '.join(STATUSES[e.kind])}")
        for f in DERIVED_FIELDS:
            if f in e.meta:
                rep.add("E106", eid, f"derived field '{f}' is hand-written",
                        "delete it; the build computes it")
        ds = [d for d in e.derivations() if isinstance(d, dict)]
        with_proof = [d for d in ds if e.proofs.get(str(d.get("name")))]
        ev = e.meta.get("checked_by") or []
        if e.kind == "claim":
            if e.status == "proved":
                if not with_proof:
                    rep.add("E107", eid, "a proved claim needs a derivation with proof text")
                if not ev:
                    rep.add("E107", eid, "a proved claim needs checked_by "
                            "(a check, a legacy script, a Lean proof, or kind: proof)")
            elif e.status == "imported":
                if not e.meta.get("imported_from"):
                    rep.add("E107", eid, "an imported claim needs imported_from")
                if ds:
                    rep.add("E108", eid, "an imported claim must not carry derivations",
                            "its proof lives in the source it is imported from")
            elif e.status == "conjectured":
                lin = e.meta.get("lineage") or {}
                if not lin.get("motivated_by"):
                    rep.add("E107", eid, "a conjecture needs lineage.motivated_by "
                            "(the claim or Question that prompted it)")
                if with_proof:
                    rep.add("E108", eid, "a conjecture must not carry proof text")
            elif e.status == "refuted":
                if not e.meta.get("refuted_by"):
                    rep.add("E107", eid, "a refuted claim needs refuted_by")
            elif e.status == "postulate":
                if ds:
                    rep.add("E108", eid, "a postulate is taken as given: no derivations")
        if e.kind == "prediction":
            kc = e.meta.get("kill_condition") or {}
            missing = [k for k in ("threshold", "data_source", "registered") if not kc.get(k)]
            if missing:
                rep.add("E109", eid, f"kill condition lacks {', '.join(missing)}")
        for lv in LEVELS:
            if lv not in e.levels or not e.levels[lv].strip():
                rep.add("E114", eid, f"level '{lv}' is missing",
                        "write it, or put the single word: pending")
        if (e.levels.get("formal") or "").strip() == "pending" and e.kind != "question":
            rep.add("E114", eid, "the formal level cannot be pending")
        for where, text in _texts(e):
            if not text or text.strip() == "pending":
                continue
            for msg in latexcheck.structural_errors(text):
                rep.add("E110", eid, f"{where}: {msg[5:]}")
            bad = latexcheck.forbidden_macros(text)
            if bad:
                rep.add("E111", eid, f"{where}: macro(s) not allowed in store text: "
                        + ", ".join("\\" + m for m in bad),
                        "remove them; file access, links and catcode changes are refused")
            unk = latexcheck.unknown_macros(text, store.notation)
            if unk:
                rep.add("E111", eid, f"{where}: undeclared macro(s) "
                        + ", ".join("\\" + m for m in unk),
                        "declare them in notation.yaml")
            body = latexcheck.strip_comments(text)
            if DASH_RE.search(body):
                rep.add("E112", eid, f"{where}: em dash", "use a comma, colon or brackets")
            if banned_re:
                m = banned_re.search(body)
                if m:
                    rep.add("E113", eid, f"{where}: banned word '{m.group(0)}'")
        for where, text in _note_texts(e):
            if "—" in text:
                rep.add("E112", eid, f"{where}: em dash", "use a comma, colon or brackets")
            if banned_re:
                m = banned_re.search(text)
                if m:
                    rep.add("E113", eid, f"{where}: banned word '{m.group(0)}'")
        quantity_checks(e, rep)
        trust_checks(e, rep)
    coverage_checks(store, rep)


# ---- quantities (roadmap item 10) -----------------------------------------

EXACT_RE = re.compile(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?|[+-]?\d+/[1-9]\d*")


def exact_value(text):
    """An exact decimal or fraction string -> Fraction; anything else raises ValueError.
    (lib/tp_premise.exact_value is the same rule, on the check side.)"""
    if isinstance(text, bool) or not isinstance(text, (str, int)):
        raise ValueError(f"{text!r} is a {type(text).__name__}, not a string")
    if not EXACT_RE.fullmatch(str(text).strip()):
        raise ValueError(f"{text!r} is not an exact decimal or fraction")
    return Fraction(str(text).strip())


def quantity_checks(e, rep):
    """E117: a quantity entity carries its quantity block (and only quantities do);
    E118: its value and uncertainty are exact decimals or fractions."""
    eid, q = e.id, e.meta.get("quantity")
    if e.kind != "quantity":
        if q is not None:
            rep.add("E117", eid, f"a {e.kind} cannot carry a quantity block",
                    "make it a quantity entity, or cite one under quantities")
        return
    if not isinstance(q, dict):
        rep.add("E117", eid, "a quantity entity needs a quantity block "
                "{symbol, value, units, source}")
        return
    for k in ("value", "uncertainty"):
        if k in q:
            try:
                exact_value(q[k])
            except ValueError as exc:
                rep.add("E118", eid, f"quantity.{k}: {exc}",
                        "write it as a quoted exact decimal ('0.51099895') or fraction")


# ---- trust and sign-offs (roadmap item 8) ----------------------------------

TRUST_SIGNED = {"human-read": 1, "human-checked": 2}


def trust_checks(e, rep):
    """E119: a sign-off names a version the entity has not reached; E120: trust claims
    a human level no sign-off of the current version supports; I121: a sign-off is for
    an older version."""
    eid, cur = e.id, e.version
    best = 0
    for so in e.meta.get("signoffs") or []:
        if not isinstance(so, dict) or not isinstance(so.get("version"), int):
            continue                       # layer-1 schema reports the shape
        v = so["version"]
        if v > cur:
            rep.add("E119", eid, f"sign-off by {so.get('by')} is for version {v}, "
                    f"but the entity is at version {cur}")
        elif v < cur:
            rep.add("I121", eid, f"sign-off by {so.get('by')} ({so.get('level')}) is for "
                    f"version {v}; the entity is at version {cur}",
                    "re-read the current version and sign again (tp sign)")
        else:
            best = max(best, TRUST_SIGNED.get(so.get("level"), 0))
    trust = e.meta.get("trust")
    need = TRUST_SIGNED.get(trust, 0)
    if need > best:
        have = {0: "none", 1: "human-read", 2: "human-checked"}[best]
        rep.add("E120", eid, f"trust '{trust}' but the highest sign-off for version {cur} "
                f"is {have}", "record the sign-off with tp sign, or lower trust")


# ---- coverage records (roadmap item 7) -------------------------------------

COVERAGE_FILE = "coverage.yaml"
COVERAGE_KINDS = ("exact", "complete", "sampled", "partial")
JUDGE_VERDICTS = ("agrees", "overclaims", "misstated")


def load_coverage(e):
    """-> (data or None, error message or None) for the entity's coverage.yaml."""
    if not e.path:
        return None, None
    p = os.path.join(e.path, COVERAGE_FILE)
    if not os.path.exists(p):
        return None, None
    import yaml
    try:
        with open(p, encoding="utf-8") as fh:
            data = yaml.safe_load(fh)
    except (OSError, yaml.YAMLError) as exc:
        return None, f"does not parse: {str(exc)[:200]}"
    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, "must be a mapping with functions, judge, untouched_premises"
    return data, None


def check_functions(e):
    """-> ([(file, function)] named by checked_by kind: check, {file: set of defs})."""
    refs, defs = [], {}
    for ev in e.meta.get("checked_by") or []:
        if not isinstance(ev, dict) or ev.get("kind") != "check":
            continue
        ref = str(ev.get("ref") or "")
        if "::" in ref:
            refs.append(tuple(ref.split("::", 1)))
    files = {f for f, _ in refs} | {"check.py"}
    for f in sorted(files):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+\.py", f) or not e.path:
            continue
        fp = os.path.join(e.path, f)
        if os.path.exists(fp):
            with open(fp, encoding="utf-8") as fh:
                defs[f] = evidence.function_names(fh.read())
    return refs, defs


def coverage_shape(data):
    """Shape problems of a parsed coverage.yaml, as messages."""
    probs = []
    extra = sorted(set(data) - {"functions", "judge", "untouched_premises"})
    if extra:
        probs.append(f"unknown key(s) {', '.join(map(str, extra))}")
    fns = data.get("functions")
    if fns is not None and not isinstance(fns, dict):
        probs.append("functions must map function names to records")
    for name, rec in (fns or {}).items() if isinstance(fns, dict) else ():
        if not isinstance(rec, dict):
            probs.append(f"functions.{name} must be a mapping {{kind, clauses, omits}}")
            continue
        bad = sorted(set(rec) - {"kind", "clauses", "omits"})
        if bad:
            probs.append(f"functions.{name}: unknown key(s) {', '.join(map(str, bad))}")
        if rec.get("kind") not in COVERAGE_KINDS:
            probs.append(f"functions.{name}.kind {rec.get('kind')!r} is not one of "
                         + ", ".join(COVERAGE_KINDS))
        cl = rec.get("clauses")
        if cl is not None and not (isinstance(cl, list) and all(isinstance(c, str) for c in cl)):
            probs.append(f"functions.{name}.clauses must be a list of strings")
        if rec.get("omits") is not None and not isinstance(rec.get("omits"), str):
            probs.append(f"functions.{name}.omits must be one line of text")
    j = data.get("judge")
    if j is not None:
        if not isinstance(j, dict):
            probs.append("judge must be a mapping {by, date, verdict, note}")
        else:
            bad = sorted(set(j) - {"by", "date", "verdict", "note"})
            if bad:
                probs.append(f"judge: unknown key(s) {', '.join(map(str, bad))}")
            for k in ("by", "date", "verdict"):
                if not j.get(k):
                    probs.append(f"judge has no {k}")
            if j.get("verdict") and j["verdict"] not in JUDGE_VERDICTS:
                probs.append(f"judge.verdict {j['verdict']!r} is not one of "
                             + ", ".join(JUDGE_VERDICTS))
    up = data.get("untouched_premises")
    if up is not None and not (isinstance(up, dict) and
                               all(isinstance(k, str) and (v is None or isinstance(v, str))
                                   for k, v in up.items())):
        probs.append("untouched_premises must map premise ids to a one-line reason")
    return probs


def coverage_checks(store: Store, rep: Report):
    """E122 shape, E123 a recorded function that does not exist, W124 a check function
    with no record, W125 the judge found the statement overclaims or is misstated,
    W127 an untouched_premises entry naming no declared premise or giving no reason,
    I126 store-wide counts."""
    kinds, n_files, n_missing = Counter(), 0, 0
    for eid, e in store.entities.items():
        data, err = load_coverage(e)
        if err:
            rep.add("E122", eid, f"{COVERAGE_FILE} {err}")
            continue
        if data is None:
            continue
        n_files += 1
        probs = coverage_shape(data)
        for msg in probs:
            rep.add("E122", eid, f"{COVERAGE_FILE}: {msg}")
        fns = data.get("functions") if isinstance(data.get("functions"), dict) else {}
        refs, defs = check_functions(e)
        known = set().union(*defs.values()) if defs else set()
        for name in sorted(fns):
            if str(name) not in known:
                rep.add("E123", eid, f"{COVERAGE_FILE} records {name}, which is not a "
                        "function of the entity's check file(s)",
                        "correct the name, or delete the record")
            elif isinstance(fns[name], dict) and fns[name].get("kind") in COVERAGE_KINDS:
                kinds[fns[name]["kind"]] += 1
        missing = sorted({f for _, f in refs} - set(map(str, fns)))
        if missing:
            n_missing += len(missing)
            rep.add("W124", eid, f"{COVERAGE_FILE} has no record for "
                    + ", ".join(missing), "add {kind, clauses, omits} for each")
        j = data.get("judge")
        if isinstance(j, dict) and j.get("verdict") in ("overclaims", "misstated"):
            rep.add("W125", eid, f"the statement-versus-check judge ({j.get('by')}, "
                    f"{j.get('date')}) found the statement {j['verdict']}: "
                    f"{j.get('note') or 'no note'}",
                    "restate the result or strengthen the check, then judge again")
        up = data.get("untouched_premises")
        if isinstance(up, dict):
            declared = _declared(e)
            for pid in sorted(map(str, up)):
                if pid not in declared:
                    rep.add("W127", eid, f"untouched_premises names {pid}, which no "
                            "derivation declares", "delete the entry")
                elif not isinstance(up[pid], str) or not up[pid].strip():
                    rep.add("W127", eid, f"untouched_premises gives no reason for {pid}",
                            "say in one line why the check need not touch it")
    if n_files:
        total = sum(kinds.values())
        rep.add("I126", "store", f"coverage records: {total} check function(s) in "
                f"{n_files} entities ("
                + ", ".join(f"{k} {kinds[k]}" for k in COVERAGE_KINDS)
                + f"); {n_missing} check function(s) in those entities have no record")


def _declared(e):
    return {parse_pin(r)[0] for d in e.derivations() if isinstance(d, dict)
            for r in (d.get("uses") or []) + (d.get("assumes") or []) if parse_pin(r)}


# ---------------------------------------------------------------------------
# layer 2: references
# ---------------------------------------------------------------------------

ALLOWED = {
    # edge kind: (allowed source kinds, allowed target kinds)
    "uses": ({"claim", "prediction"}, {"claim", "object", "prediction"}),
    "assumes": ({"claim", "prediction"}, {"claim"}),
    "about": (None, {"object"}),
    "specialises": ({"claim", "prediction"}, {"claim", "prediction"}),
    "equivalent_to": ({"claim", "prediction"}, {"claim", "prediction"}),
    "contradicts": ({"claim", "prediction"}, {"claim", "prediction"}),
    "supports": ({"claim", "prediction"}, {"claim", "prediction"}),
    "tests": ({"prediction"}, {"claim"}),
    "kills": ({"prediction"}, {"claim"}),
    "settled_by": ({"question"}, {"claim", "prediction"}),
    "refuted_by": ({"claim"}, {"claim", "prediction"}),
    "comments_on": ({"note"}, {"claim", "object", "prediction", "question"}),
}


def legacy_path(store, legacy_dir, script):
    """A legacy script is named, never given as a path. It is looked for in the
    legacy folder, then in the subfolders that store/config.yaml lists under
    legacy_extra_dirs (relative, inside the legacy folder: the working notes
    keep their scripts beside their runs)."""
    base = os.path.join(store.root, legacy_dir or "")
    first = os.path.join(base, script)
    if os.path.exists(first):
        return first
    for sub in store.config.get("legacy_extra_dirs") or []:
        sub = str(sub)
        if os.path.isabs(sub) or ".." in sub.replace("\\", "/").split("/"):
            continue
        p = os.path.join(base, sub, script)
        if os.path.exists(p):
            return p
    return first


def _weakest(store, eff, e):
    """Explain an effective status: the best derivation and its weakest premise."""
    best = None
    for d in e.derivations():
        if not isinstance(d, dict):
            continue
        prem = [parse_pin(r) for r in (d.get("uses") or []) + (d.get("assumes") or [])]
        prem = [p for p in prem if p]
        worst = min(prem, key=lambda p: derive.RANK.get(eff.get(p[0], "unsupported"), 0),
                    default=None)
        score = derive.RANK.get(eff.get(worst[0], "unsupported"), 0) if worst else 3
        if best is None or score > best[0]:
            best = (score, d.get("name"), worst)
    return best


OP_KINDS = ("research", "consistency", "housekeeping")
OP_DIFFICULTY = ("tractable", "substantial", "frontier")
OP_STATUS = ("open", "partial", "reformulated", "settled")
OP_REQUIRED = ("id", "title", "area", "kind", "difficulty", "status", "statement", "entities")


def open_problem_checks(store: Store, rep: Report):
    """store/open_problems.yaml: every problem well formed, every link to an entity real."""
    subjects = {s["id"] for s in store.subjects}
    seen = set()
    for i, op in enumerate(store.open_problems or []):
        oid = op.get("id") if isinstance(op, dict) else None
        where = oid or f"open_problems.yaml[{i}]"
        if not isinstance(op, dict):
            rep.add("E217", where, "an open problem must be a mapping")
            continue
        for k in OP_REQUIRED:
            if not op.get(k):
                rep.add("E217", where, f"open problem has no '{k}'")
        if oid and not re.fullmatch(r"op\.[a-z0-9]+(-[a-z0-9]+)*", oid):
            rep.add("E217", where, "open problem ids are op.<kebab-slug>")
        if oid in seen:
            rep.add("E217", where, "open problem id used twice")
        seen.add(oid)
        for k, allowed in (("kind", OP_KINDS), ("difficulty", OP_DIFFICULTY), ("status", OP_STATUS)):
            if op.get(k) and op[k] not in allowed:
                rep.add("E217", where, f"{k} '{op[k]}' is not one of {', '.join(allowed)}")
        if op.get("area") and subjects and op["area"] not in subjects:
            rep.add("E217", where, f"area '{op['area']}' is not a subject")
        for eid in op.get("entities") or []:
            if eid not in store.entities:
                rep.add("E216", where, f"names no entity: {eid}",
                        "correct the id" + (f" (merged into {store.replaced_by[eid]})"
                                            if eid in store.replaced_by else ""))
        text = " ".join(str(op.get(k) or "") for k in ("statement", "why", "known", "success")) + \
            " ".join(str(a) for a in (op.get("attack") or []))
        for ref in sorted(set(re.findall(r"\\claimref\{([^}]+)\}", text))):
            if ref not in store.entities:
                rep.add("E216", where, f"\\claimref{{{ref}}} names no entity")


def layer2(store: Store, rep: Report):
    for dup in store.duplicates:
        rep.add("E207", dup, "this id is defined by more than one folder")
    for eid, e in store.entities.items():
        if eid in store.tombstones:
            rep.add("E205", eid, "this id is retired and can never be reused")
        # every premise a derivation lists should be named in its proof text
        for d in e.derivations():
            if not isinstance(d, dict):
                continue
            text = e.proofs.get(str(d.get("name")), "")
            if not text.strip():
                continue
            named = set(re.findall(r"\\claimref\{([^}]+)\}", text))
            missing = [p.split("@")[0] for p in (d.get("uses") or []) + (d.get("assumes") or [])
                       if p.split("@")[0] not in named]
            if missing:
                rep.add("W215", eid, f"proof {d.get('name')} never cites premise(s) "
                        + ", ".join(missing),
                        "name each with \\claimref where it is used (seed/CITE_PASS.md)")
        # a \claimref in any text must name an entity that exists
        for where, text in [(lv, e.levels.get(lv) or "") for lv in LEVELS] + \
                [("proof " + k, v) for k, v in e.proofs.items()]:
            for ref in sorted(set(re.findall(r"\\claimref\{([^}]+)\}", text))):
                if ref not in store.entities:
                    hint = (f"it was merged into {store.replaced_by[ref]}; cite that"
                            if ref in store.replaced_by else
                            "correct the id (see tombstones.yaml for retired ones)")
                    rep.add("E214", eid, f"{where}: \\claimref{{{ref}}} names no entity", hint)
    open_problem_checks(store, rep)
    for ed in derive.edges(store):
        src = store.entities[ed.src]
        tgt = store.entities.get(ed.dst)
        if ed.dst in store.tombstones:
            rep.add("E205", ed.src, f"{ed.kind} -> {ed.dst}: target id is retired")
            continue
        if tgt is None:
            rep.add("E201", ed.src, f"{ed.kind} -> {ed.dst}: no such entity")
            continue
        if ed.pin is not None and ed.pin > tgt.version:
            rep.add("E202", ed.src, f"{ed.kind} -> {ed.dst}@{ed.pin}: current version "
                    f"is {tgt.version}")
        rule = ALLOWED.get(ed.kind)
        if rule:
            srcs, tgts = rule
            if srcs is not None and src.kind not in srcs:
                rep.add("E203", ed.src, f"a {src.kind} cannot have a '{ed.kind}' edge")
            elif tgt.kind not in tgts:
                rep.add("E203", ed.src, f"{ed.kind} -> {ed.dst}: a {tgt.kind} is not a "
                        f"valid target")
            elif ed.kind == "assumes" and tgt.status != "postulate":
                rep.add("E203", ed.src, f"assumes -> {ed.dst}: target is not a postulate",
                        "use 'uses' for a proved premise")
            elif ed.kind == "uses" and tgt.status == "postulate":
                rep.add("E203", ed.src, f"uses -> {ed.dst}: a postulate is taken via "
                        "'assumes'", "move it to the derivation's assumes list")
            elif ed.kind == "uses" and tgt.kind == "object":
                rep.add("W209", ed.src, f"uses -> {ed.dst}: an object belongs in 'about'")
    subject_ids = {x.get("id") for x in store.subjects}
    if subject_ids:
        for eid, e in store.entities.items():
            sub = e.meta.get("subject")
            if not sub:
                rep.add("W210", eid, "no subject: the map and documents cannot place it",
                        "set subject to one of the ids in subjects.yaml")
            elif sub not in subject_ids:
                rep.add("E208", eid, f"subject '{sub}' is not in subjects.yaml")
    programme_checks(store, rep)
    quantity_pins(store, rep)
    tag_ids = {x.get("id") for x in store.tags}
    used_tags = set()
    for eid, e in store.entities.items():
        for t in e.meta.get("tags") or []:
            used_tags.add(t)
            if t not in tag_ids:
                rep.add("E211", eid, f"tag '{t}' is not in tags.yaml",
                        "use a tag from the vocabulary, or add it there first")
    for t in sorted(tag_ids - used_tags):
        rep.add("W212", "store", f"tag '{t}' is in tags.yaml but no entity carries it")
    rep.graph = derive.logical_graph(store)
    rep.eff = derive.effective_status(store)
    for eid, e in store.entities.items():
        if e.kind == "claim" and e.status == "proved" and rep.eff[eid] != "proved":
            why = _weakest(store, rep.eff, e)
            cause = ""
            if why and why[2]:
                p = why[2]
                cause = (f"derivation '{why[1]}' uses {p[0]}@{p[1]} "
                         f"({rep.eff.get(p[0], 'missing')})")
            elif not e.derivations():
                cause = "no derivations"
            rep.add("E204", f"{eid}@{e.version}",
                    f"declared status 'proved' exceeds effective status "
                    f"'{rep.eff[eid]}'" + (f"\n      cause: {cause}" if cause else ""),
                    "lower status, prove the premise, or name the condition as a "
                    "postulate and assume it")
        old = store.lock.get(eid)
        if old:
            if e.version < old["version"]:
                rep.add("E206", eid, f"version went backwards ({old['version']} -> {e.version})")
            elif e.version == old["version"] and e.substantive_hash() != old["hash"]:
                rep.add("E206", eid, "substantive fields changed without a version bump",
                        f"set version: {e.version + 1}")
            if "credit" in old:
                from .credit import compare, describe
                removed, unclaimed = compare(old["credit"], e.meta.get("credit"), old["version"], e.version)
                for r in removed:
                    rep.add("W220", eid, f"a credit entry of the accepted version is missing or changed: {describe(r)}",
                            "keep every earlier credit entry; an amendment adds its own")
                if unclaimed:
                    rep.add("W221", eid, f"version {e.version} has no credit entry of its own",
                            f"add to credit: {{name: <who>, role: <what was done>, version: {e.version}}}")
        # the language is geometric algebra: a new or changed entity that leaves it says why
        if store.lock and (old is None or e.substantive_hash() != old["hash"]):
            from .galang import scan, declared
            hits = [] if declared(e) else scan(e)
            if hits:
                rep.add("W222", eid, f"written outside geometric algebra ({', '.join(hits)}) without saying why",
                        "translate it, or declare outside_ga: {kind: imported | complex-analysis | bridge | other, why: ...}")


def programmes(store):
    """-> {id: {title, about}} from store/config.yaml `programmes`, or None if the store
    registers no programmes (then the programme rules are off)."""
    reg = store.config.get("programmes")
    return reg if reg is not None else None


def programme_of(store, e):
    """The entity's programme: its own field, else config default_programme."""
    return e.meta.get("programme") or store.config.get("default_programme")


def programme_checks(store: Store, rep: Report):
    """E218: with programmes registered in config.yaml, every entity's programme (its
    own, or default_programme), the default itself and every subject's programme must
    be registered."""
    reg = programmes(store)
    if reg is None:
        return
    if not isinstance(reg, dict) or not all(
            isinstance(k, str) and re.fullmatch(r"[a-z][a-z0-9-]*", k) and isinstance(v, dict)
            and v.get("title") for k, v in reg.items()):
        rep.add("E218", "store", "config.yaml programmes must map ids ([a-z][a-z0-9-]*) to "
                "{title, about}")
        return
    known = ", ".join(sorted(reg))
    dflt = store.config.get("default_programme")
    if dflt and dflt not in reg:
        rep.add("E218", "store", f"default_programme '{dflt}' is not registered",
                f"use one of {known}")
    for sub in store.subjects:
        if isinstance(sub, dict) and sub.get("programme") and sub["programme"] not in reg:
            rep.add("E218", f"subject {sub.get('id')}", f"programme '{sub['programme']}' is "
                    "not registered in config.yaml", f"use one of {known}")
    for eid, e in store.entities.items():
        prog = programme_of(store, e)
        if not prog:
            rep.add("E218", eid, "no programme, and config.yaml sets no default_programme")
        elif prog not in reg:
            rep.add("E218", eid, f"programme '{prog}' is not registered in config.yaml",
                    f"use one of {known}")


def quantity_pins(store: Store, rep: Report):
    """E219: every `quantities` pin names a quantity entity at or below its version."""
    for eid, e in store.entities.items():
        for ref in e.meta.get("quantities") or []:
            p = parse_pin(ref)
            if not p:
                continue                       # layer 1 reports a malformed pin
            tgt = store.entities.get(p[0])
            if tgt is None:
                rep.add("E219", eid, f"quantities -> {p[0]}: no such entity")
            elif tgt.kind != "quantity":
                rep.add("E219", eid, f"quantities -> {p[0]}: a {tgt.kind} is not a quantity")
            elif p[1] > tgt.version:
                rep.add("E219", eid, f"quantities -> {ref}: current version is {tgt.version}")


# ---------------------------------------------------------------------------
# layer 3: whole store
# ---------------------------------------------------------------------------

def subject_fit(store, graph):
    """-> {id: (share, n, majority subject)} for results whose logical
    neighbours (premises and dependants) mostly sit in another subject."""
    nb = defaultdict(set)
    for a, bs in graph.items():
        for b in bs:
            if a in store.entities and b in store.entities:
                nb[a].add(b)
                nb[b].add(a)
    out = {}
    for eid, ns in nb.items():
        sub = store.entities[eid].meta.get("subject")
        if len(ns) < 3 or not sub:
            continue
        subs = [store.entities[x].meta.get("subject") for x in ns]
        share = sum(1 for x in subs if x == sub) / len(subs)
        if share < 0.25:
            maj = min(set(subs), key=lambda x: (-subs.count(x), str(x)))   # ties: alphabetical
            out[eid] = (share, len(ns), maj)
    return out


def layer3(store: Store, rep: Report):
    for eid, (share, n, maj) in sorted(subject_fit(store, rep.graph).items()):
        rep.add("I213", eid, f"only {share:.0%} of its {n} logical neighbours share its "
                f"subject; most are in '{maj}'",
                "check the subject; a bridging result may rightly stay where it is "
                "and carry a tag for the other side")
    for cyc in derive.find_cycles(rep.graph):
        rep.add("E301", cyc[0], "circular reasoning: " + " -> ".join(cyc + [cyc[0]]))
    past, future = derive.cones(rep.graph, store.entities.keys())
    rep.past, rep.future = past, future
    for eid, e in store.entities.items():
        if e.kind != "prediction":
            continue
        ds = (e.meta.get("kill_condition") or {}).get("data_source")
        if not ds:
            continue
        for c in sorted(past[eid] | {eid}):
            if ds in (store.entities[c].meta.get("fitted_to") or []):
                rep.add("E302", eid, f"postdiction: {c} was fitted to '{ds}', the "
                        "dataset this prediction claims to predict")
    for ed in derive.edges(store):
        if ed.kind == "contradicts" and ed.dst in store.entities:
            a, b = store.entities[ed.src], store.entities[ed.dst]
            if "postulate" in (a.status, b.status):
                # two incompatible hypotheses (or a result against a hypothesis):
                # the store is consistent, but nothing may rest on both sides
                for eid in sorted(store.entities):
                    side = past.get(eid, set()) | {eid}
                    if ed.src in side and ed.dst in side:
                        rep.add("E307", eid, f"rests on both {ed.src} and {ed.dst}, which "
                                "contradict each other", "drop one premise, or narrow one "
                                "so they no longer conflict")
                continue
            if derive.RANK.get(rep.eff.get(ed.src), 0) == 3 and \
                    derive.RANK.get(rep.eff.get(ed.dst), 0) == 3:
                rep.add("E303", ed.src, f"contradicts {ed.dst}, and both are proved: "
                        "the store is inconsistent")
    # a killed prediction refutes the structure it rests on: flag that structure
    for eid, e in store.entities.items():
        if e.kind == "prediction" and e.status == "killed":
            basis = sorted(c for c in past.get(eid, ())
                           if store.entities[c].status in ("proved", "postulate"))
            for c in basis:
                rep.add("W306", c, f"the prediction {eid} was killed, and this rests "
                        "under it", "review it: at least one result in the killed "
                        "prediction's past cone is false")
    rep.ledger = derive.ledger(store, rep.graph)
    for eid, e in store.entities.items():
        declared = e.meta.get("ledger")
        if declared and rep.ledger.get(eid) and declared != rep.ledger[eid]:
            rep.add("E304", eid, f"declared ledger '{declared}' but computed "
                    f"'{rep.ledger[eid]}'", "delete the declared value or fix the derivations")
    changed = {eid for eid, e in store.entities.items()
               if eid not in store.lock or store.lock[eid]["hash"] != e.substantive_hash()}
    hit = set()
    for c in changed:
        hit |= future.get(c, set())
    hit -= changed
    docs = _documents_using(store, changed | hit)
    rep.impact = {"changed": sorted(changed), "affected_claims": sorted(hit),
                  "documents": docs}
    if changed and store.lock:
        rep.add("I305", "store", f"this change touches {len(changed)} entities; "
                f"{len(hit)} claims and {len(docs)} documents depend on them and need "
                "re-confirmation (the build marks a claim stale only when every "
                "derivation of it is broken)")


def _documents_using(store, ids):
    import json
    out = []
    base = os.path.join(os.path.dirname(os.path.abspath(store.root)), "documents")
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base)):
        man = os.path.join(base, name, "manifest.json")
        if os.path.exists(man):
            with open(man, encoding="utf-8") as fh:
                used = {k.split("@")[0] for k in json.load(fh).get("claims", [])}
            if used & ids:
                out.append(name)
    return out


# ---------------------------------------------------------------------------
# layer 4: evidence
# ---------------------------------------------------------------------------

L4_CACHE_FILE = ".tp-layer4.json"
L4_FORMAT = 2          # bump when the shape of a cached record changes


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def _file_sha(path: str) -> str:
    try:
        with open(path, "rb") as fh:
            return _sha(fh.read())
    except OSError:
        return "missing"


# lib modules every check depends on: the sandbox driver imports both
DRIVER_LIBS = ("GA", "tp_premise")


def _l4_toolchain() -> str:
    """Everything layer 4's outcome depends on besides the store and the optional
    lib modules (gtg, fock, series, ...), which go into each entity's own key."""
    import inspect
    import sys
    here = os.path.dirname(os.path.abspath(__file__))
    parts = [_file_sha(os.path.join(here, "evidence.py"))]
    parts += [_file_sha(os.path.join(evidence.LIB, m + ".py")) for m in DRIVER_LIBS]
    parts += [_sha((inspect.getsource(_layer4_entity) + inspect.getsource(_run_new_check)
                    ).encode()), "py%d.%d" % sys.version_info[:2], f"fmt{L4_FORMAT}"]
    return _sha("|".join(parts).encode())


def _check_file_shas(e) -> dict:
    out = {}
    for ev in e.meta.get("checked_by") or []:
        ref = str((ev or {}).get("ref") or "")
        fname = ref.split("::")[0]
        if fname and re.fullmatch(r"[A-Za-z0-9_.-]+\.py", fname) and e.path:
            out[fname] = _file_sha(os.path.join(e.path, fname))
    return out


def _check_paths(e, with_premise_file=False) -> list:
    """The check files layer 4 executes for e: those named in checked_by, and, for a
    premise, the check.py that premise() runs."""
    names = set(_check_file_shas(e))
    if with_premise_file:
        names.add("check.py")
    return [os.path.join(e.path, n) for n in sorted(names) if e.path]


class _LibIndex:
    """Which lib modules a file pulls in, transitively, and their content hashes."""

    def __init__(self):
        self.mods = evidence.lib_modules()
        self.file_memo, self.closure_memo = {}, {}
        self.text_memo = {}

    def _src(self, path):
        if path not in self.text_memo:
            try:
                with open(path, encoding="utf-8") as fh:
                    self.text_memo[path] = fh.read()
            except OSError:
                self.text_memo[path] = ""
        return self.text_memo[path]

    def imports(self, path):
        if path not in self.file_memo:
            self.file_memo[path] = evidence.lib_imports(self._src(path), self.mods)
        return self.file_memo[path]

    def closure(self, names):
        out, todo = set(), list(names)
        while todo:
            m = todo.pop()
            if m in out:
                continue
            out.add(m)
            todo += sorted(self.imports(os.path.join(evidence.LIB, m + ".py")) - out)
        return out

    def mentions_quantity(self, path):
        return "quantity" in self._src(path)


def _quantity_digest(store) -> str:
    vals = {eid: str((e.meta.get("quantity") or {}).get("value"))
            for eid, e in sorted(store.entities.items()) if e.kind == "quantity"}
    return _sha(json.dumps(vals, sort_keys=True).encode())


def _l4_key(store, e, eid, toolchain, legacy_dir, run_mutants, cone_memo,
            libs=None, qdigest=None) -> str:
    """A check reaches other entities only through premise(), which executes the
    premise's check.py (and, through its EXPORTS, possibly that premise's premises),
    and through quantity(), which reads a quantity entity's value.
    So the outcome depends on: the entity's own substantive content (formal, proofs,
    derivations without pins, checked_by, check files), the check files of its whole
    past cone, the lib modules those files import (closed under lib's own imports),
    the quantity values if any of them reads one, the legacy scripts it names, the
    toolchain and the mutation flag."""
    def cone(i, seen):
        for d in (store.entities[i].derivations() if i in store.entities else []):
            if not isinstance(d, dict):
                continue
            for r in (d.get("uses") or []) + (d.get("assumes") or []):
                pp = parse_pin(r)
                pid = pp[0] if pp else str(r).split("@")[0]
                if pid not in seen:
                    seen.add(pid)
                    cone(pid, seen)
        return seen
    if eid not in cone_memo:
        deps = sorted(cone(eid, set()) - {eid})
        cone_memo[eid] = deps
    deps = cone_memo[eid]
    dep_checks = {}
    paths = _check_paths(e)
    for d in deps:
        de = store.entities.get(d)
        if de is None:
            dep_checks[d] = "absent"
            continue
        shas = _check_file_shas(de)
        if de.path and "check.py" not in shas:
            shas["check.py"] = _file_sha(os.path.join(de.path, "check.py"))
        dep_checks[d] = shas
        paths += _check_paths(de, with_premise_file=True)
    legacy = {}
    for ev in e.meta.get("checked_by") or []:
        if (ev or {}).get("kind") == "legacy":
            sc = str(ev.get("script", ""))
            legacy[sc] = (_file_sha(legacy_path(store, legacy_dir, sc))
                          if re.fullmatch(r"[A-Za-z0-9_.-]+\.py", sc) else "bad")
    libs = libs or _LibIndex()
    used = set()
    for p in paths:
        used |= libs.imports(p)
    used = libs.closure(used) - set(DRIVER_LIBS)
    lib_shas = {m: _file_sha(os.path.join(evidence.LIB, m + ".py")) for m in sorted(used)}
    blob = {"self": e.substantive_hash(), "deps": dep_checks, "legacy": legacy,
            "tool": toolchain, "mutants": bool(run_mutants), "lib": lib_shas}
    if any(libs.mentions_quantity(p) for p in paths):
        blob["quantities"] = qdigest if qdigest is not None else _quantity_digest(store)
    return _sha(json.dumps(blob, sort_keys=True).encode())


def l4_jobs() -> int:
    """Worker processes for layer 4: TP_JOBS, else the CPU count."""
    try:
        n = int(os.environ.get("TP_JOBS") or 0)
    except ValueError:
        n = 0
    return max(1, n or os.cpu_count() or 1)


# the worker context: set in the parent before the pool forks, so workers inherit the
# loaded store instead of unpickling it per job
_JOB = {}


def _job_init(root, legacy_dir, cache, run_mutants):
    """Initialiser for start methods that do not fork: load the store afresh."""
    from .model import load_store
    _JOB.update(store=load_store(root), legacy_dir=legacy_dir, cache=cache,
                run_mutants=run_mutants)


def _legacy_job(path):
    try:
        return path, evidence.run_legacy(path, _JOB["cache"])
    except Exception as exc:          # no output, crash or timeout
        return path, ("__error__", type(exc).__name__, str(exc))


def _entity_job(arg):
    eid, legacy_results = arg
    store = _JOB["store"]
    sub = Report()
    runs = []
    _layer4_entity(store, sub, eid, store.entities[eid], _JOB["legacy_dir"], _JOB["cache"],
                   legacy_results, _JOB["run_mutants"], runs=runs)
    return eid, {"findings": [[f.code, f.entity, f.message, f.fix] for f in sub.findings],
                 "result": sub.check_results.get(eid), "failed": eid in sub.check_failed,
                 "runs": runs}


def _pool_map(fn, items, jobs, ctx):
    """map fn over items in order, in `jobs` processes (in this process if jobs == 1)."""
    items = list(items)
    if jobs <= 1 or len(items) <= 1:
        _JOB.update(ctx)
        return [fn(x) for x in items]
    import concurrent.futures as cf
    import multiprocessing as mp
    _JOB.update(ctx)
    if "fork" in mp.get_all_start_methods():
        pool = cf.ProcessPoolExecutor(max_workers=min(jobs, len(items)),
                                      mp_context=mp.get_context("fork"))
    else:
        pool = cf.ProcessPoolExecutor(
            max_workers=min(jobs, len(items)), initializer=_job_init,
            initargs=(ctx["store"].root, ctx["legacy_dir"], ctx["cache"], ctx["run_mutants"]))
    with pool:
        return list(pool.map(fn, items, chunksize=1))


def _legacy_paths(store, e, legacy_dir):
    out = []
    for ev in e.meta.get("checked_by") or []:
        if (ev or {}).get("kind") == "legacy":
            sc = str(ev.get("script", "") or "")
            if re.fullmatch(r"[A-Za-z0-9_.-]+\.py", sc):
                p = legacy_path(store, legacy_dir, sc)
                if os.path.exists(p):
                    out.append(p)
    return out


def layer4(store: Store, rep: Report, run_mutants=True, incremental=None, jobs=None):
    """Run every entity's evidence. With incremental (the default unless TP_FULL is
    set), an entity whose layer-4 inputs are unchanged since the last run replays the
    recorded findings instead of running again; see _l4_key for what counts as an
    input. Entities with errors other than E401 are never cached.

    Entities run in `jobs` worker processes (default l4_jobs()); the findings are
    gathered in store order, so the output is the same as a serial run. The premise
    comparison (W405 / I405) and the quantity comparison (W414) are made afresh from
    the recorded touched sets, so coverage.yaml and `quantities` edits need no rerun."""
    if incremental is None:
        incremental = not os.environ.get("TP_FULL")
    jobs = l4_jobs() if jobs is None else max(1, int(jobs))
    legacy_dir = store.config.get("legacy_scripts_dir")
    cache = os.environ.get("TP_CACHE_DIR") or os.path.join(store.root, ".tp-cache")
    cache_path = os.environ.get("TP_L4_CACHE") or os.path.join(store.root, L4_CACHE_FILE)
    old = {}
    if incremental and os.path.exists(cache_path):
        try:
            with open(cache_path, encoding="utf-8") as fh:
                old = json.load(fh)
        except (OSError, ValueError):
            old = {}
    toolchain = _l4_toolchain()
    libs, qdigest = _LibIndex(), _quantity_digest(store)
    new, cone_memo, keys, records, todo = {}, {}, {}, {}, []
    rep.l4_stats = {"replayed": 0, "ran": 0, "jobs": jobs}
    for eid, e in store.entities.items():
        key = _l4_key(store, e, eid, toolchain, legacy_dir, run_mutants, cone_memo,
                      libs=libs, qdigest=qdigest)
        keys[eid] = key
        hit = old.get(eid)
        if incremental and hit and hit.get("key") == key:
            records[eid] = hit
            rep.l4_stats["replayed"] += 1
        else:
            todo.append(eid)
    ctx = {"store": store, "legacy_dir": legacy_dir, "cache": cache,
           "run_mutants": run_mutants}
    # series scripts first, once each: several entities may share one
    lpaths = sorted({p for eid in todo for p in _legacy_paths(store, store.entities[eid],
                                                             legacy_dir)})
    legacy_results = {}
    for path, res in _pool_map(_legacy_job, lpaths, jobs, ctx):
        if isinstance(res, tuple) and res and res[0] == "__error__":
            res = type(res[1], (Exception,), {})(res[2])
        legacy_results[path] = res
    args = [(eid, {p: legacy_results[p] for p in _legacy_paths(store, store.entities[eid],
                                                               legacy_dir)
                   if p in legacy_results}) for eid in todo]
    for eid, rec in _pool_map(_entity_job, args, jobs, ctx):
        records[eid] = rec
        rep.l4_stats["ran"] += 1
        if not any(c.startswith("E") and c != "E401" for c, *_ in rec["findings"]):
            new[eid] = dict(rec, key=keys[eid])
    for eid, e in store.entities.items():
        rec = records.get(eid) or {}
        if eid in records and eid not in new and rec.get("key") == keys[eid]:
            new[eid] = rec                     # a replayed record stays cached
        for code, ent, msg, fix in rec.get("findings") or []:
            rep.add(code, ent, msg, fix)
        if rec.get("result") is not None:
            rep.check_results[eid] = rec["result"]
        if rec.get("failed"):
            rep.check_failed.add(eid)
        premise_findings(store, rep, e, rec.get("runs") or [])
    try:
        with open(cache_path, "w", encoding="utf-8") as fh:
            json.dump(new, fh, indent=0, sort_keys=True)
    except OSError:
        pass


def _layer4_entity(store, rep, eid, e, legacy_dir, cache, legacy_results, run_mutants,
                   runs=None):
    """Run e's evidence into rep. With `runs` (a list), each check's touched premises
    and quantities are appended to it instead of being compared here: layer4 compares
    them across all the entity's checks (premise_findings)."""
    declared = _declared(e)
    results = []
    for ev in e.meta.get("checked_by") or []:
        kind = ev.get("kind")
        if kind == "check":
            info = None
            if runs is not None:
                info = {"func": str(ev.get("ref", "")).split("::")[-1],
                        "derivation": ev.get("derivation"), "ok": False,
                        "touched": [], "quantities": []}
                runs.append(info)
            results.append(_run_new_check(store, rep, e, ev, declared, run_mutants,
                                          run_info=info))
        elif kind == "legacy":
            script = ev.get("script", "")
            if not re.fullmatch(r"[A-Za-z0-9_.-]+\.py", str(script or "")):
                rep.add("E401", eid, f"legacy script must be a file name in the "
                        f"legacy folder, not a path: {script!r}")
                results.append("fail")
                continue
            path = legacy_path(store, legacy_dir, script)
            if not os.path.exists(path):
                rep.add("E401", eid, f"legacy script not found: {script}")
                results.append("fail")
                continue
            if path not in legacy_results:
                try:
                    legacy_results[path] = evidence.run_legacy(path, cache)
                except Exception as exc:      # no output, crash or timeout
                    legacy_results[path] = exc
            if isinstance(legacy_results[path], Exception):
                rep.add("E409", eid, f"legacy script {script} did not run: "
                        f"{type(legacy_results[path]).__name__}: "
                        f"{str(legacy_results[path])[:200]}")
                results.append("fail")
                continue
            tags = set(ev.get("tags") or [])
            hits = [(lab, ok) for lab, ok in legacy_results[path]
                    if evidence.label_keys(lab) & tags]
            if not hits:
                rep.add("E412", eid, f"no check in {script} carries tags {sorted(tags)}")
                results.append("fail")
            elif not all(ok for _, ok in hits):
                bad = [lab for lab, ok in hits if not ok]
                rep.add("E406", eid, f"{len(bad)} of {len(hits)} legacy checks fail: "
                        + "; ".join(bad[:3]))
                results.append("fail")
            else:
                rep.add("I410", eid, f"{len(hits)} legacy checks pass in {script} "
                        "(premises untracked, no mutation test)")
                results.append("pass-legacy")
        elif kind == "lean":
            rep.add("W411", eid, "Lean evidence declared; no Lean toolchain here")
            results.append("unverified")
        elif kind == "proof":
            results.append("proof-only")
    if results:
        if "fail" in results:
            rep.check_results[eid] = "fail"
            rep.check_failed.add(eid)
        elif "pass" in results:
            rep.check_results[eid] = "pass"
        elif "pass-legacy" in results:
            rep.check_results[eid] = "pass-legacy"
        else:
            rep.check_results[eid] = results[0]
    else:
        rep.check_results[eid] = "none"


def _run_new_check(store, rep, e, ev, declared, run_mutants, run_info=None):
    """Run one check-kind evidence item. Without run_info it compares the declared
    premises with this check's touched set itself (W405 per check, the old rule);
    with run_info (a dict) it records ok / touched / quantities there instead."""
    eid = e.id
    ref = ev.get("ref", "")
    if "::" not in ref:
        rep.add("E401", eid, f"check ref '{ref}' must be file.py::function")
        return "fail"
    fname, func = ref.split("::", 1)
    path = os.path.join(e.path, fname)
    if not os.path.exists(path):
        rep.add("E401", eid, f"check file not found: {fname}")
        return "fail"
    with open(path, encoding="utf-8") as fh:
        src = fh.read()
    bad = False
    static = evidence.static_problems(src)
    for code, msg in static:
        rep.add(code, eid, msg)
        bad = True
    if any(code == "E401" for code, _ in static):
        return "fail"                    # it does not parse: nothing further can run
    if f"def {func}(" not in src:
        rep.add("E401", eid, f"function {func} not found in {fname}")
        return "fail"
    if not evidence.has_assertion(src, func):
        rep.add("E408", eid, f"{func} asserts nothing")
        bad = True
    r1 = evidence.run_check(store.root, e.path, src, func)
    if r1.get("timeout"):
        rep.add("E409", eid, r1["error"])
        return "fail"
    if r1.get("error") and "sandbox" in r1["error"]:
        rep.add("E409", eid, r1["error"])
        return "fail"
    if not r1["ok"]:
        rep.add("E406", eid, f"check {func} fails: {r1.get('error')}")
        return "fail"
    r2 = evidence.run_check(store.root, e.path, src, func)
    if r2["ok"] != r1["ok"] or r2.get("touched") != r1.get("touched"):
        rep.add("E407", eid, "check gives different results on two runs")
        bad = True
    touched = set(r1.get("touched") or [])
    for p in sorted(touched - declared):
        rep.add("E404", eid, f"check touches {p} but no derivation declares it",
                f"add {p}@<version> to a derivation's uses, or stop touching it")
    if run_info is not None:
        run_info.update(ok=True, touched=sorted(touched),
                        quantities=sorted(r1.get("quantities") or []))
    else:
        for p in sorted(declared - touched):
            rep.add("W405", eid, f"{p} is declared but the check never touches it")
    if run_mutants:
        n = evidence.int_literal_count(src, func)
        if n == 0:
            rep.add("W408", eid, f"{func} has no integer literal to perturb; "
                    "mutation test skipped")
        else:
            ks = sorted({round(i * (n - 1) / 7) for i in range(8)}) if n > 8 else range(n)
            survived = 0
            for k in ks:
                mut = evidence.mutate(src, func, k)
                if mut is None:
                    continue
                if evidence.run_check(store.root, e.path, mut, func)["ok"]:
                    survived += 1
            tried = len(list(ks))
            if survived == tried:
                rep.add("E408", eid, f"every perturbation of {func}'s literals still "
                        "passes: the check tests nothing")
                bad = True
            elif survived * 2 > tried:
                rep.add("W413", eid, f"{survived} of {tried} perturbations of {func}'s "
                        "literals still pass: the check is weak")
    return "fail" if bad else "pass"


# ---- declared versus touched premises and quantities -----------------------

def _primary_derivation(e):
    names = [str(d.get("name")) for d in e.derivations() if isinstance(d, dict)]
    return "main" if "main" in names else (names[0] if names else None)


def _ids(refs):
    out = set()
    for r in refs or []:
        p = parse_pin(r)
        out.add(p[0] if p else str(r).split("@")[0])
    return out


def _restates(store, e, pid):
    """Why pid is a restatement of e (equivalent_to either way, or pid derives from
    e), or None."""
    tgt = store.entities.get(pid)
    if pid in _ids(e.meta.get("equivalent_to")):
        return f"{pid} is listed as equivalent_to this result"
    if tgt is None:
        return None
    if e.id in _ids(tgt.meta.get("equivalent_to")):
        return f"{pid} lists this result as equivalent_to"
    for d in tgt.derivations():
        if isinstance(d, dict) and e.id in _ids((d.get("uses") or []) + (d.get("assumes") or [])):
            return f"{pid} itself derives from this result (derivation {d.get('name')})"
    return None


def untouched_reason(store, e, pid, checked_derivations, coverage=None):
    """Why a declared premise that no check touched is expected to stay untouched, or
    None (then it is a W405). The rules, in order:
      1. a literature `-external` entry: cited for the record, nothing to run;
      2. a restatement: equivalent_to either way, or the premise derives from e;
      3. declared only in a derivation that no check belongs to (a standard route);
      4. coverage.yaml untouched_premises lists it with a reason (any declared premise:
         proved, imported or postulate; the coverage judge's reason is recorded)."""
    if pid.endswith("-external"):
        return "a literature -external entry: cited for the record, nothing to compute"
    why = _restates(store, e, pid)
    if why:
        return "a restatement: " + why
    homes = sorted(str(d.get("name")) for d in e.derivations() if isinstance(d, dict)
                   and pid in _ids((d.get("uses") or []) + (d.get("assumes") or [])))
    if homes and not set(homes) & checked_derivations:
        return (f"declared only in derivation {', '.join(homes)}, which no check belongs "
                f"to (the checks belong to {', '.join(sorted(checked_derivations))})")
    up = (coverage or {}).get("untouched_premises")
    if isinstance(up, dict) and isinstance(up.get(pid), str) and up[pid].strip():
        return f"coverage.yaml: {up[pid].strip()}"
    return None


def premise_findings(store, rep, e, runs):
    """W405 / I405 from the checks' touched sets, compared once per entity: a premise
    any check of the entity touches is covered. W414 for quantities read but not
    listed. Skipped when a check did not complete (its error is already reported)."""
    if not runs or not all(r.get("ok") for r in runs):
        return
    eid = e.id
    touched = set().union(*(set(r.get("touched") or []) for r in runs))
    primary = _primary_derivation(e)
    checked = {r.get("derivation") or primary for r in runs} - {None}
    cov = None
    data, _ = load_coverage(e)
    if isinstance(data, dict):
        cov = data
    for pid in sorted(_declared(e) - touched):
        why = untouched_reason(store, e, pid, checked, cov)
        if why:
            rep.add("I405", eid, f"{pid} is declared and untouched, as expected: {why}")
            continue
        n = len(runs)
        rep.add("W405", eid, f"{pid} is declared but none of the entity's {n} check "
                "function(s) touches it",
                "touch it with premise() where the check uses it, drop it from the "
                "derivation, or excuse it in coverage.yaml untouched_premises")
    if any(x.kind == "quantity" for x in store.entities.values()):
        listed = _ids(e.meta.get("quantities"))
        read = set().union(*(set(r.get("quantities") or []) for r in runs))
        for q in sorted(read - listed):
            ver = store.entities[q].version if q in store.entities else None
            rep.add("W414", eid, f"the check reads quantity {q} but the entity does not "
                    "list it under quantities",
                    f"add {q}@{ver} to quantities" if ver else
                    f"{q} is not a quantity entity of this store")


# ---------------------------------------------------------------------------
# layer 5: meaning
# ---------------------------------------------------------------------------

TOKEN_RE = re.compile(r"[A-Za-z]{3,}")


CONDITION_IN_FORMAL = re.compile(
    r"\b(?:[Uu]nder (?:Hypothesis|Premise|the hypothesis|the premise|\(|[A-Z]\d)|[Aa]ssume\b|"
    r"[Cc]onditional(?:ly)?\b(?! expectation)|at leading order|observation level|record level|"
    r"[Gg]iven (?:Hypothesis|Premise|\())")
CONDITION_WORDS = re.compile(
    r"\b(?:under|assum\w*|if|given|provided|conditional\w*|hypothes\w*|premise\w*|"
    r"postulat\w*|leading order|approximately|observation|record level|unless|"
    r"suppos\w*|reading|holds only|only when|only if|working)\b", re.I)


def plain_levels_keep_conditions(store: Store, rep: Report):
    """W503: a result that holds only under something must say so at every level."""
    for eid, e in store.entities.items():
        if e.kind not in ("claim", "prediction") or e.status in ("postulate", "refuted"):
            continue
        assumes = [a for d in e.derivations() if isinstance(d, dict)
                   for a in (d.get("assumes") or [])]
        if not assumes and not CONDITION_IN_FORMAL.search(e.levels.get("formal") or ""):
            continue
        for lv in ("technical", "lay", "one-liner"):
            text = (e.levels.get(lv) or "").strip()
            if text and text != "pending" and not CONDITION_WORDS.search(text):
                rep.add("W503", eid, f"the {lv} level does not state the condition the "
                        "result holds under", "name the hypothesis or premise "
                        "(\"under (S)\", \"if\", \"assuming\") as the formal statement does")


def contradiction_checks(store: Store, rep: Report):
    """W510 (roadmap item 9): a record value that drifted from its quantity entity, two
    statements giving one quantity incompatible values, an exact fraction shown with a
    wrong decimal, or a connection value displayed in the Cartan sign (DICTIONARY C10).
    I510 summarises the scan. The scan itself is tp.quantity.contradictions."""
    from . import quantity
    finds, st = quantity.contradictions(store)
    for eid, msg in finds:
        if msg.startswith("sign convention"):
            fix = "display Omega in the GTG sign (Omega(e_i) = -sigma_i B_i, -sum_i p_i B_i)"
        elif msg.startswith("decimal drift"):
            fix = "show the truncated digits before \\ldots, or the rounded value with \\approx"
        else:
            fix = "use the quantity entity's value (and list it under quantities), or say " \
                  "why this value differs"
        rep.add("W510", eid, msg, fix)
    hits = ", ".join(f"{k}: {v}" for k, v in sorted(st["sign_hits"].items())) or "none"
    rep.add("I510", "store", f"contradiction scan: {st['quantities']} quantities, "
            f"{st['occurrences']} symbol = value occurrences compared "
            f"({st.get('not_record', 0)} left out as predictions, fits or hypotheticals); "
            f"{st['drift']} drift, {st['disagree']} disagreement(s), {st['decimal']} decimal, "
            f"{st['sign']} sign ({len(quantity.SIGN_PATTERNS)} C10 patterns; hits {hits})")


def layer5(store: Store, rep: Report, threshold=0.92):
    plain_levels_keep_conditions(store, rep)
    contradiction_checks(store, rep)
    docs = {}
    for eid, e in store.entities.items():
        toks = [t.lower() for t in TOKEN_RE.findall(e.levels.get("formal") or "")]
        if len(toks) >= 12:
            docs[eid] = Counter(toks)
    df = Counter(t for c in docs.values() for t in c)
    N = max(len(docs), 1)
    vec = {}
    for eid, c in docs.items():
        v = {t: n * math.log(1 + N / df[t]) for t, n in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[eid] = {t: x / norm for t, x in v.items()}
    ids = sorted(vec)
    linked = {(ed.src, ed.dst) for ed in derive.edges(store)
              if ed.kind in ("equivalent_to", "specialises")}
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            va, vb = vec[a], vec[b]
            s = sum(x * vb.get(t, 0) for t, x in va.items())
            if s >= threshold and (a, b) not in linked and (b, a) not in linked:
                rep.add("W501", a, f"possible duplicate of {b} (similarity {s:.2f})",
                        "merge, or link with equivalent_to")
    judge = (store.config.get("ai_judge") or {}).get("enabled")
    if not judge:
        rep.add("I502", "store", "AI judge not configured: statement-vs-check, "
                "level overclaiming and citation checks were skipped")


# ---------------------------------------------------------------------------
# layer 6: people
# ---------------------------------------------------------------------------

def layer6(store: Store, rep: Report, author: str | None):
    gov = store.config.get("governance") or {}
    # store names and the code host's logins (CI passes the login as the author)
    maintainers = set(gov.get("maintainers") or []) | set(gov.get("github_logins") or [])
    core = set(gov.get("core_regions") or [])
    if author is None:
        rep.add("E602", "store", "the people checks need an author",
                "pass --author NAME or set TP_AUTHOR")
        return
    if author in maintainers:
        return
    for eid, e in store.entities.items():
        old = store.lock.get(eid)
        new = lock_entry(e)
        if old is None:
            # a new entity is held to the same rules as a change to an old one
            if new["status"] in ("imported", "postulate"):
                rep.add("E601", eid, f"only a maintainer may add a {new['status']} entity")
            if new["status"] == "proved" and e.meta.get("region") in core:
                rep.add("E601", eid, "only a maintainer may add a proved claim to a "
                        "core region")
            if e.meta.get("ledger"):
                rep.add("E601", eid, "only a maintainer may declare a ledger class")
            if new["assumes"]:
                rep.add("E601", eid, "only a maintainer may add a postulate dependency "
                        "(assumes)")
            from .galang import scan, declared
            hits = [] if declared(e) else scan(e)
            if hits:
                rep.add("E609", eid, f"written outside geometric algebra ({', '.join(hits)}) without saying why",
                        "translate it, or declare outside_ga: {kind: imported | complex-analysis | bridge | other, why: ...}")
            continue
        if (new["status"] == "proved" and old.get("status") != "proved"
                and e.meta.get("region") in core):
            rep.add("E601", eid, "only a maintainer may promote a core claim to proved")
        if new["status"] in ("imported", "postulate") and old.get("status") != new["status"]:
            rep.add("E601", eid, f"only a maintainer may change a status to {new['status']}")
        if set(new["assumes"]) - set(old.get("assumes") or []):
            rep.add("E601", eid, "only a maintainer may add an assumes edge")
        if set(old.get("assumes") or []) - set(new["assumes"]):
            rep.add("E601", eid, "only a maintainer may remove an assumes edge")
        if new.get("ledger") != old.get("ledger"):
            rep.add("E601", eid, "only a maintainer may change a declared ledger class")
        if "credit" in old:
            from .credit import compare, describe
            removed, unclaimed = compare(old["credit"], new["credit"], old.get("version"), new["version"])
            for r in removed:
                rep.add("E603", eid, f"only a maintainer may remove or change a credit entry: {describe(r)}",
                        "keep every earlier credit entry as it was")
            if unclaimed:
                rep.add("E604", eid, f"an amendment must credit itself: version {new['version']} has no "
                        "credit entry of its own",
                        f"add to credit: {{name: <your name>, role: <what you changed>, version: {new['version']}}}, "
                        "and one for the AI model that drafted it")
        # the language is geometric algebra: a changed entity that leaves it says why
        if e.substantive_hash() != old["hash"]:
            from .galang import scan, declared
            hits = [] if declared(e) else scan(e)
            if hits:
                rep.add("E609", eid, f"written outside geometric algebra ({', '.join(hits)}) without saying why",
                        "translate it, or declare outside_ga: {kind: imported | complex-analysis | bridge | other, why: ...}")
        # an amendment says what it fixes, and its kind matches what changed (tp/amend.py)
        from .amend import findings as amendment_findings
        for code, msg, fix in amendment_findings(old, e):
            if code == "E605":
                rep.add("E605", eid, msg, fix)
            elif code == "E606":
                rep.add("E606", eid, msg, fix)
            elif code == "E607":
                rep.add("E607", eid, msg, fix)
            else:
                rep.add("E608", eid, msg, fix)
    for gone in sorted(set(store.lock) - set(store.entities)):
        if gone not in store.tombstones:
            rep.add("E601", gone, "entity removed without being retired to tombstones.yaml")


# ---------------------------------------------------------------------------

def validate(store: Store, layers=(1, 2, 3, 4, 5, 6), keep_going=False,
             author=None, run_mutants=True) -> Report:
    rep = Report()
    for n in layers:
        before = len(rep.errors())
        if n == 1:
            layer1(store, rep)
        elif n == 2:
            layer2(store, rep)
        elif n == 3:
            if not rep.graph:
                rep.graph = derive.logical_graph(store)
                rep.eff = derive.effective_status(store)
            layer3(store, rep)
        elif n == 4:
            layer4(store, rep, run_mutants)
        elif n == 5:
            layer5(store, rep)
        elif n == 6:
            layer6(store, rep, author)
        rep.layers_run.append(n)
        if len(rep.errors()) > before and not keep_going:
            break
    return rep


# ---------------------------------------------------------------------------
# the ranked summary printed at the end of `tp check`
# ---------------------------------------------------------------------------

# warnings, most important first: a weak or untestable check outranks a quiet premise
WARNING_ORDER = ("W413", "W408", "W125", "W510", "W414", "W306", "W411", "W503", "W124", "W127",
                 "W405", "W215", "W501", "W209", "W210", "W212", "W220", "W221", "W222")

CODE_TITLES = {
    "W220": "a credit entry of the accepted version is missing or changed",
    "W221": "an amendment with no credit entry of its own",
    "W222": "written outside geometric algebra without saying why",
    "W413": "weak check: most literal perturbations still pass",
    "W408": "check has no integer literal to perturb",
    "W125": "judge: statement overclaims or is misstated",
    "W414": "check reads a quantity the entity does not list",
    "W306": "rests under a killed prediction",
    "W411": "Lean evidence not run here",
    "W503": "a plain level drops the condition",
    "W124": "check function without a coverage record",
    "W127": "untouched_premises entry cannot apply",
    "W405": "declared premise no check touches",
    "W215": "proof never cites a premise",
    "W501": "possible duplicate",
    "W209": "uses an object",
    "W210": "no subject",
    "W212": "unused tag",
    "I405": "untouched premise, expected (suppressed W405)",
    "I126": "coverage records, store-wide",
    "I121": "sign-off is for an older version",
}


def _rank(code):
    sev = {"E": 0, "W": 1, "I": 2}[code[0]]
    if sev == 1:
        pos = WARNING_ORDER.index(code) if code in WARNING_ORDER else len(WARNING_ORDER)
        return (sev, pos, code)
    return (sev, 0, code)


def summarise(rep: Report, top: int = 3) -> str:
    """Counts per code, errors first, then warnings in WARNING_ORDER, then information;
    with the entities that carry each code most often."""
    by = defaultdict(Counter)
    for f in rep.findings:
        by[f.code][f.entity] += 1
    n = Counter(f.severity for f in rep.findings)
    lines = [f"summary: {n['error']} error(s), {n['warning']} warning(s), "
             f"{n['info']} information finding(s)"]
    for code in sorted(by, key=_rank):
        ents = by[code]
        tops = sorted(ents.items(), key=lambda kv: (-kv[1], kv[0]))[:top]
        who = ", ".join(f"{k} ({v})" if v > 1 else k for k, v in tops)
        more = f", +{len(ents) - top} more" if len(ents) > top else ""
        title = CODE_TITLES.get(code, "")
        lines.append(f"  {code} {sum(ents.values()):6d}  {title}"
                     + (f"\n               {who}{more}" if who else ""))
    return "\n".join(lines)
