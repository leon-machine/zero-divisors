"""Loading the store: entity folders on disk -> Entity objects.

An entity is a folder holding `entity.md`: YAML front matter between `---`
lines, then level sections introduced by `## formal`, `## technical`,
`## lay`, `## one-liner`.  Derivation proof text lives in sibling files named
in the front matter (`proof: proof-main.tex`).

Nothing derived is ever read from disk: see DERIVED_FIELDS.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from dataclasses import dataclass, field
from typing import Any

import yaml

ENTITY_FILE = "entity.md"
LEVELS = ("formal", "technical", "lay", "one-liner")
KINDS = ("claim", "object", "prediction", "question", "note", "quantity")
ENTITY_DIRS = {"claim": "claims", "object": "objects",
               "prediction": "predictions", "question": "questions",
               "note": "notes", "quantity": "quantities"}

# Fields computed by the build.  A file that contains any of them is rejected
# (layer 1), because hand-written copies of derived state drift.
DERIVED_FIELDS = ("reverse_edges", "effective_status", "ledger_computed",
                  "stale", "past_cone", "future_cone", "impact",
                  "weakest_link", "check_result")

# Substantive fields: changing any of these requires a version bump.
SUBSTANTIVE_FIELDS = ("status", "derivations", "about", "checked_by",
                      "specialises", "equivalent_to", "contradicts",
                      "supports", "tests", "kills", "fitted_to",
                      "imported_from", "kill_condition", "reading_of", "refuted_by",
                      "comments_on")
LATE_SUBSTANTIVE = ("comments_on",)

PIN_RE = re.compile(r"^(?P<id>[a-z][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+)@(?P<v>[1-9][0-9]*)$")
ID_RE = re.compile(r"^[a-z][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+$")


def parse_pin(s: str):
    """'a.b@3' -> ('a.b', 3); returns None if malformed."""
    m = PIN_RE.match(s) if isinstance(s, str) else None
    return (m.group("id"), int(m.group("v"))) if m else None


@dataclass
class Entity:
    id: str
    kind: str
    meta: dict
    levels: dict
    path: str                      # folder
    proofs: dict = field(default_factory=dict)   # derivation name -> text
    parse_errors: list = field(default_factory=list)

    @property
    def version(self) -> int:
        return int(self.meta.get("version", 0) or 0)

    @property
    def status(self) -> str:
        return self.meta.get("status", "")

    @property
    def title(self) -> str:
        return self.meta.get("title", self.id)

    def derivations(self) -> list:
        return self.meta.get("derivations") or []

    def pins(self, key: str) -> list:
        """Pinned references in a top-level list field."""
        return list(self.meta.get(key) or [])

    def substantive_hash(self) -> str:
        sub = {k: self.meta.get(k) for k in SUBSTANTIVE_FIELDS}
        # fields added to the list later must not change the hash of an
        # entity that does not use them
        for k in LATE_SUBSTANTIVE:
            if sub.get(k) is None:
                sub.pop(k)
        sub["formal"] = (self.levels.get("formal") or "").strip()
        sub["proofs"] = {k: v.strip() for k, v in sorted(self.proofs.items())}
        # the evidence itself: the content of every check file the entity names
        checks = {}
        for ev in self.meta.get("checked_by") or []:
            ref = str((ev or {}).get("ref") or "")
            fname = ref.split("::")[0]
            if fname and re.fullmatch(r"[A-Za-z0-9_.-]+\.py", fname) and self.path:
                fp = os.path.join(self.path, fname)
                if os.path.exists(fp):
                    with open(fp, "rb") as fh:
                        checks[fname] = hashlib.sha256(fh.read()).hexdigest()
        sub["check_files"] = checks
        blob = json.dumps(sub, sort_keys=True, default=str)
        # moving a pin to a premise's new version is a review act, not a change of
        # content: pins are left out, the ids they point at are kept
        blob = re.sub(r'"([a-z][a-z0-9-]*(?:\.[a-z0-9][a-z0-9-]*)+)@[1-9][0-9]*"', r'"\1"', blob)
        return hashlib.sha256(blob.encode()).hexdigest()[:16]


SECTION_RE = re.compile(r"^## (formal|technical|lay|one-liner)\s*$", re.M)


def parse_entity_text(text: str):
    """Split entity.md into (meta dict, levels dict, errors)."""
    errors = []
    if not text.startswith("---"):
        return {}, {}, ["E101 missing YAML front matter"]
    parts = text.split("\n---", 1)
    if len(parts) < 2:
        return {}, {}, ["E101 unterminated YAML front matter"]
    head = parts[0][3:]
    body = parts[1].lstrip("-").lstrip("\n")
    try:
        meta = yaml.safe_load(head) or {}
        if not isinstance(meta, dict):
            errors.append("E101 front matter is not a mapping")
            meta = {}
    except yaml.YAMLError as exc:
        return {}, {}, [f"E101 YAML parse error: {exc}"]
    levels = {}
    marks = list(SECTION_RE.finditer(body))
    for i, m in enumerate(marks):
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        levels[m.group(1)] = body[m.end():end].strip("\n")
    return meta, levels, errors


def load_entity(folder: str) -> Entity:
    with open(os.path.join(folder, ENTITY_FILE), encoding="utf-8") as fh:
        meta, levels, errors = parse_entity_text(fh.read())
    ent = Entity(id=str(meta.get("id", "")), kind=str(meta.get("kind", "")),
                 meta=meta, levels=levels, path=folder, parse_errors=errors)
    for d in ent.derivations():
        if isinstance(d, dict) and d.get("proof"):
            p = os.path.join(folder, str(d["proof"]))
            if os.path.exists(p):
                with open(p, encoding="utf-8") as fh:
                    text = fh.read()
                if text.strip():
                    ent.proofs[str(d.get("name", ""))] = text
    return ent


@dataclass
class Store:
    root: str
    entities: dict                 # id -> Entity
    config: dict
    tombstones: set
    notation: dict                 # macro -> definition
    lock: dict                     # id -> {"version": n, "hash": h}
    duplicates: list               # ids defined more than once
    subjects: list = field(default_factory=list)   # [{id, title, side, about}] in map order
    tags: list = field(default_factory=list)       # [{id, title, group, about}]: the tag vocabulary
    replaced_by: dict = field(default_factory=dict)  # retired id -> the id that replaced it
    open_problems: list = field(default_factory=list)  # store/open_problems.yaml: problems to attack

    def get(self, ref: str):
        p = parse_pin(ref)
        return self.entities.get(p[0] if p else ref)


def _read_yaml(path: str, default):
    if not os.path.exists(path):
        return default
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh) or default


def _tombstones(root):
    """tombstones.yaml lists retired ids, as bare strings or as records
    {id, replaced_by, date, reason}. -> (set of ids, {id: replaced_by})."""
    ids, repl = set(), {}
    for t in _read_yaml(os.path.join(root, "tombstones.yaml"), []) or []:
        if isinstance(t, dict) and t.get("id"):
            ids.add(t["id"])
            if t.get("replaced_by"):
                repl[t["id"]] = t["replaced_by"]
        elif isinstance(t, str):
            ids.add(t)
    return ids, repl


def load_store(root: str) -> Store:
    entities, dups = {}, []
    for kind, sub in ENTITY_DIRS.items():
        base = os.path.join(root, sub)
        if not os.path.isdir(base):
            continue
        for name in sorted(os.listdir(base)):
            folder = os.path.join(base, name)
            if os.path.isfile(os.path.join(folder, ENTITY_FILE)):
                ent = load_entity(folder)
                key = ent.id or f"<unnamed:{folder}>"
                if key in entities:
                    dups.append(key)
                entities[key] = ent
    lock_path = os.path.join(root, ".tp-lock.json")
    lock = {}
    if os.path.exists(lock_path):
        with open(lock_path, encoding="utf-8") as fh:
            lock = json.load(fh)
    tomb, repl = _tombstones(root)
    config = _read_yaml(os.path.join(root, "config.yaml"), {})
    # The series' verify scripts live beside the papers, not in the lab. A clone of the
    # lab outside TP_Papers_Suite points at them with TP_LEGACY_DIR (an absolute path).
    if os.environ.get("TP_LEGACY_DIR"):
        config = dict(config, legacy_scripts_dir=os.path.abspath(os.environ["TP_LEGACY_DIR"]))
    return Store(root=root, entities=entities, replaced_by=repl,
                 config=config,
                 tombstones=tomb,
                 notation=_read_yaml(os.path.join(root, "notation.yaml"), {}),
                 lock=lock, duplicates=dups,
                 subjects=_read_yaml(os.path.join(root, "subjects.yaml"), []),
                 tags=_read_yaml(os.path.join(root, "tags.yaml"), []),
                 open_problems=_read_yaml(os.path.join(root, "open_problems.yaml"), []))


def lock_entry(e: Entity) -> dict:
    assumes = sorted({a for d in e.derivations() if isinstance(d, dict)
                      for a in (d.get("assumes") or [])})
    return {"version": e.version, "hash": e.substantive_hash(),
            "status": e.status, "assumes": assumes,
            "ledger": e.meta.get("ledger"),
            # who did what, kept so that an amendment can be checked to keep every earlier credit
            "credit": [[str(c.get("name", "")), str(c.get("role", "")), c.get("version")]
                       for c in (e.meta.get("credit") or []) if isinstance(c, dict)]}


def write_lock(store: Store) -> None:
    lock = {eid: lock_entry(e) for eid, e in sorted(store.entities.items())}
    with open(os.path.join(store.root, ".tp-lock.json"), "w", encoding="utf-8") as fh:
        json.dump(lock, fh, indent=1, sort_keys=True)


def dump_entity(meta: dict, levels: dict) -> str:
    """Serialise front matter and levels back to entity.md text."""
    head = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, width=100)
    out = ["---", head.rstrip("\n"), "---", ""]
    for lv in LEVELS:
        if lv in levels:
            out += [f"## {lv}", levels[lv].rstrip("\n"), ""]
    return "\n".join(out)
