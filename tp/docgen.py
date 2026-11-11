"""Document generation and regeneration from stored versions.

generate(store, recipe)  -> builds a document from a recipe and stores it in
                            store/../documents/<doc>/ as version 1 (or the next
                            version if it exists, via regenerate).
regenerate(store, doc)   -> updates the stored document: unchanged blocks are
                            copied byte for byte, only blocks touched by claim
                            changes are rebuilt, human overrides are kept or
                            raised as conflicts, and a changelog and redline
                            are written.

Prose (transitions and framing) comes from a pluggable writer.  The default
TemplateWriter is deterministic and plain; an AI writer fills the same slots
through prose.json.  Every prose sentence carries a tag: [[c:<id>]] when it
restates a claim, [[t]] when it is a pure transition with no new facts.
"""
from __future__ import annotations

import copy
import datetime as dt
import difflib
import hashlib
import json
import os
import re
from collections import defaultdict

import yaml

from . import derive
from . import labels as labelreg
from .model import load_store, parse_pin
from .validate import validate

BLOCK_TYPE = {"proved": "theorem", "imported": "fact", "postulate": "postulate",
              "conjectured": "conjecture", "refuted": "refutation",
              "defined": "definition"}
TAG_RE = re.compile(r"\[\[(c:[a-z0-9.\-]+|t)\]\]")
SENT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\\$])")
NUM_TOKEN = re.compile(r"(?<![A-Za-z_\\])\d+(?:[./]\d+)*")
DASH_RE = re.compile(r"\u2014|(?<![-!])---(?!-)")


def _h(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()[:12]


def docs_root(store_root: str) -> str:
    return os.path.join(os.path.dirname(os.path.abspath(store_root)), "documents")


# ---------------------------------------------------------------------------
# selection
# ---------------------------------------------------------------------------

def _premises(d):
    out = []
    for r in (d.get("uses") or []) + (d.get("assumes") or []):
        p = parse_pin(r)
        if p:
            out.append(p[0])
    return out


def choose_derivation(store, eid, level, ledger_roots, ledger):
    e = store.entities[eid]
    ds = [d for d in e.derivations() if isinstance(d, dict)]
    if not ds:
        return None
    if level == "lay":
        return min(ds, key=lambda d: (len(_premises(d)), d.get("name", "")))

    def essential(d):
        return any(p in ledger_roots or ledger.get(p) == "essential" for p in _premises(d))
    return sorted(ds, key=lambda d: (not essential(d), d.get("name", "")))[0]


def select(store, recipe, ledger):
    missing = [x for x in recipe.get("spine") or [] if x not in store.entities]
    if missing:
        raise ValueError("the recipe's spine names entities not in the store: "
                         + ", ".join(missing) + " (retired ids are listed in "
                         "tombstones.yaml; replace them in the recipe)")
    roots = set(store.config.get("transport_roots") or [])
    level = recipe.get("level", "technical")
    frontier_ids = set(recipe.get("frontier") or [])
    frontier_regions = set(recipe.get("frontier_regions") or [])
    frontier_subjects = set(recipe.get("frontier_subjects") or [])
    shown, cited, assumed, chosen = [], set(), set(), {}
    seen = set()

    def is_frontier(eid):
        e = store.entities[eid]
        return (eid in frontier_ids or e.meta.get("region") in frontier_regions
                or e.meta.get("subject") in frontier_subjects
                or (e.meta.get("programme") == "standard"
                    and recipe.get("programme") != "standard"))

    def visit(eid):
        if eid in seen or eid not in store.entities:
            return
        seen.add(eid)
        e = store.entities[eid]
        if e.status == "postulate":
            assumed.add(eid)
            return
        spine_only = recipe.get("show") == "spine-only"
        in_spine = eid in recipe["spine"]
        if (e.status == "imported" and not in_spine) or (
                (is_frontier(eid) or spine_only) and not in_spine):
            # an imported result named in the spine is shown, with its provenance
            cited.add(eid)
            return
        d = choose_derivation(store, eid, level, roots, ledger)
        chosen[eid] = d
        if d:
            for p in _premises(d):
                visit(p)
        shown.append(eid)       # post-order: premises first

    for s in recipe["spine"]:
        visit(s)
    # results the document cites without deriving (a paper's imported Facts
    # that restate results of earlier papers)
    for c in recipe.get("cite") or []:
        if c in store.entities and c not in shown and store.entities[c].status != "postulate":
            cited.add(c)
    inc = recipe.get("include") or {}
    refutations, predictions = [], []
    sel = set(shown) | cited
    for eid, e in store.entities.items():
        if inc.get("refutations") == "in-cone" and e.status == "refuted":
            if set(e.meta.get("refuted_by") or []) & sel:
                refutations.append(eid)
        if inc.get("predictions") == "in-cone" and e.kind == "prediction":
            if any(p in sel for d in e.derivations() if isinstance(d, dict)
                   for p in _premises(d)):
                predictions.append(eid)
    # notes (remarks and examples) follow the shown results they comment on
    notes = defaultdict(list)
    if inc.get("notes") in ("attached", "all"):
        shown_set = set(shown)
        for eid, e in store.entities.items():
            if e.kind != "note" or e.status == "setting":
                continue
            on = [t for t in e.meta.get("comments_on") or [] if t in shown_set]
            if on and (inc.get("notes") == "all" or on[0] == (e.meta.get("comments_on") or [None])[0]):
                # after the last of the results it discusses
                notes[max(on, key=shown.index)].append(eid)
        line = lambda x: int(((store.entities[x].meta.get("locators") or {}).get("line")) or 0)
        for k in notes:
            notes[k].sort(key=line)
    # the running text of the paper a recreation follows (setting notes)
    settings = []
    if inc.get("settings") in ("attached", "all") and recipe.get("paper"):
        for eid, e in store.entities.items():
            loc = e.meta.get("locators") or {}
            if e.kind == "note" and e.status == "setting" and loc.get("paper") == recipe["paper"]:
                settings.append(eid)
        settings.sort(key=lambda x: int((store.entities[x].meta.get("locators") or {})
                                        .get("line") or 0))
    return {"order": shown, "cited": sorted(cited), "assumed": sorted(assumed),
            "derivation": {k: (v or {}).get("name") for k, v in chosen.items()},
            "refutations": sorted(refutations), "predictions": sorted(predictions),
            "notes": dict(notes), "settings": settings}


# ---------------------------------------------------------------------------
# ordering into sections
# ---------------------------------------------------------------------------

def section_key(store, eid):
    e = store.entities[eid]
    return e.meta.get("subject") or e.meta.get("region") or "general"


def paper_sections(store, sel, recipe):
    """A recreation of a paper follows the paper's own sections: each result
    goes in the top-level section of its paper that contains it, sections in
    the paper's order, results in the paper's order inside them."""
    code = recipe.get("paper")
    outline = [x for x in (_REG.get(f"{code}#outline") or []) if x.get("level") == "section"]
    def where(c):
        loc = store.entities[c].meta.get("locators") or {}
        if loc.get("paper") != code or not loc.get("line"):
            return None, 10 ** 9
        line = int(loc["line"])
        sec = [x for x in outline if x["line"] <= line]
        return (sec[-1] if sec else None), line
    groups, first, named = {}, {}, {}
    members = list(sel["order"])
    inline = [n for ns in (sel.get("notes") or {}).values() for n in ns]
    inline += [n for n in sel.get("settings") or []
               if (store.entities[n].meta.get("locators") or {}).get("number") != "Abstract"]
    if inline:
        sel["inline_notes"] = True
        members += [n for n in inline if n not in members]
    for c in members:
        sec, line = where(c)
        key = (f"paper-{sec['number'] or sec['line']}" if sec else
               section_key(store, c))
        groups.setdefault(key, []).append((line, c))
        first[key] = min(first.get(key, 10 ** 9), sec["line"] if sec else 10 ** 9)
        if sec:
            named[key] = sec["title"]
    titles = {x["id"]: x["title"] for x in store.subjects}
    titles.update(named)
    titles.update(recipe.get("section_titles") or {})
    out = []
    for key in sorted(groups, key=lambda k: first[k]):
        out.append({"key": key, "title": titles.get(key, key.replace("-", " ").title()),
                    "claims": [c for _, c in sorted(groups[key], key=lambda x: x[0])]})
    return out


def order_sections(store, sel, recipe):
    """Cluster by section key, order sections by dependency (merging mutual
    dependence), keep the post-order (premise just before first use) inside."""
    if recipe.get("sections") == "paper" and recipe.get("paper"):
        return paper_sections(store, sel, recipe)
    order = sel["order"]
    pos = {c: i for i, c in enumerate(order)}
    key = {c: section_key(store, c) for c in order}
    keys = list(dict.fromkeys(key[c] for c in order))
    dep = defaultdict(set)
    for c in order:
        d = (store.entities[c].derivations() or [None])
        dname = sel["derivation"].get(c)
        for der in store.entities[c].derivations():
            if isinstance(der, dict) and der.get("name") == dname:
                for p in _premises(der):
                    if p in key and key[p] != key[c]:
                        dep[key[c]].add(key[p])
    cyc = derive.find_cycles(dep)
    merged = {}
    for comp in cyc:
        head = min(comp, key=keys.index)
        for k in comp:
            merged[k] = head
    mk = lambda k: merged.get(k, k)
    skeys = list(dict.fromkeys(mk(k) for k in keys))
    sdep = defaultdict(set)
    for a, bs in dep.items():
        for b in bs:
            if mk(a) != mk(b):
                sdep[mk(a)].add(mk(b))
    # topological order of sections, ties by first appearance
    done, out = set(), []
    while len(out) < len(skeys):
        for k in skeys:
            if k not in done and sdep[k] <= done:
                out.append(k)
                done.add(k)
                break
        else:                      # should not happen after merging
            out += [k for k in skeys if k not in done]
            break
    sections = []
    titles = {x["id"]: x["title"] for x in store.subjects}
    titles.update(recipe.get("section_titles") or {})
    for k in out:
        members = sorted([c for c in order if mk(key[c]) == k], key=pos.get)
        sections.append({"key": k, "title": titles.get(k, k.replace("-", " ").title()),
                         "claims": members})
    return sections


# ---------------------------------------------------------------------------
# prose writers
# ---------------------------------------------------------------------------

class TemplateWriter:
    """Deterministic, plain prose.  Each sentence is tagged."""

    def __init__(self, store, level):
        self.store, self.level = store, level

    def one(self, eid):
        e = self.store.entities[eid]
        t = (e.levels.get("one-liner") or e.title).strip()
        return t if t.endswith(".") else t + "."

    def transition(self, prev, nxt, uses_prev):
        if prev is None:
            return f"We begin here. [[t]]"
        if uses_prev:
            return f"The next result builds directly on the one just stated. [[t]]"
        return f"We turn to a further ingredient. [[t]]"

    def section_intro(self, section):
        t = section["title"]
        t = t[0].lower() + t[1:] if t[:2].istitle() and not t.split()[0].isupper() \
            and t.split()[0] not in ("Clifford", "Einstein", "Witt") else t
        return f"This section gathers the results on {t}. [[t]]"

    def abstract(self, doc):
        sp = doc["spine"]
        parts = [f"{self.one(s)} [[c:{s}]]" for s in sp[:4]]
        return " ".join(parts)

    def introduction(self, doc):
        return ("Every result below is drawn from the Physics Graph; each is "
                "shown with its derivation or cited with its provenance. [[t]]")

    def conclusion(self, doc):
        return f"{self.one(doc['spine'][-1])} [[c:{doc['spine'][-1]}]]"


class FileWriter(TemplateWriter):
    """Prose supplied in documents/<doc>/prose.json, keyed by slot id; any slot
    missing there falls back to the template."""

    def __init__(self, store, level, prose: dict):
        super().__init__(store, level)
        self.prose = prose

    def get(self, slot, fallback):
        return self.prose.get(slot, fallback)


# ---------------------------------------------------------------------------
# block tree
# ---------------------------------------------------------------------------

_REG = {}      # the label registry of the store being rendered (set by _context)


def _paper_of(e):
    loc = e.meta.get("locators") or {}
    if isinstance(loc, list):
        loc = loc[0] if loc else {}
    return loc.get("paper")


def resolve_refs(store, eid, text):
    """The paper's own \\ref and \\eqref, rewritten for a reader without it."""
    return labelreg.resolve(text, _paper_of(store.entities[eid]), _REG,
                            entities=set(store.entities))


def claim_text(store, eid, level):
    e = store.entities[eid]
    lv = "formal" if level == "formal" else level
    text = (e.levels.get(lv) or "").strip()
    gap = (not text) or text == "pending"
    if lv == "formal" and text.rstrip(". ") == e.title.rstrip(". "):
        # some table-row entities carry only their title formally
        tech = (e.levels.get("technical") or "").strip()
        if tech and tech != "pending":
            text = tech
    if not gap:
        text = resolve_refs(store, eid, text)
    return (f"[pending: {lv} text]" if gap else text), gap


def claim_block(store, eid, btype, level, derivation=None):
    e = store.entities[eid]
    text, gap = claim_text(store, eid, level)
    b = {"id": f"c:{eid}", "type": btype, "claim": f"{eid}@{e.version}",
         "title": e.title, "text": text, "gap": gap, "level": level}
    if btype == "theorem" and derivation:
        b["derivation"] = derivation
        if level == "formal":
            b["proof"] = resolve_refs(store, eid, e.proofs.get(derivation, ""))
        else:
            prem = []
            for d in e.derivations():
                if isinstance(d, dict) and d.get("name") == derivation:
                    prem = _premises(d)
            b["rests_on"] = prem
    if btype == "fact":
        imp = e.meta.get("imported_from") or []
        loc = e.meta.get("locators") or {}
        if imp:
            b["provenance"] = "; ".join(
                i["citation"] + (f", {i['locator']}" if i.get("locator") else "")
                for i in imp)
        else:
            b["provenance"] = (f"Physics Graph result {eid}, version {e.version}"
                               + (f" ({loc.get('paper')} {loc.get('number')})"
                                  if loc.get("paper") else ""))
    if btype == "refutation":
        b["refuted_by"] = e.meta.get("refuted_by") or []
    if btype == "prediction":
        b["kill_condition"] = e.meta.get("kill_condition") or {}
    b["hash"] = _h(json.dumps({k: b.get(k) for k in ("text", "proof", "provenance",
                                                      "title", "claim", "rests_on",
                                                      "derivation", "type")},
                              sort_keys=True))
    return b


_EFF = {}       # effective status of the store being rendered (set by _context)


def _shown_type(store, eid):
    """The environment a shown entity takes: what it is, not where it sits."""
    e = store.entities[eid]
    if e.kind == "object":
        return "definition"
    if e.kind == "note":
        return "note"
    if e.kind == "prediction":
        return "prediction"
    if e.status == "proved" and _EFF.get(eid) in ("conjectured", "unsupported"):
        return "conjecture"     # declared proved, but it rests on something unproved
    return {"imported": "fact", "conjectured": "conjecture",
            "refuted": "refutation"}.get(e.status, "theorem")


def build_blocks(store, recipe, sel, sections, writer):
    level = recipe.get("level", "technical")
    doc = {"spine": recipe["spine"]}
    W = writer
    get = getattr(W, "get", lambda slot, fb: fb)
    paper_prose = recipe.get("prose") == "paper"
    if paper_prose:
        # the paper's own text carries the document: its abstract, and no
        # generated framing or transitions between its running text
        ab = next((n for n in sel.get("settings") or []
                   if (store.entities[n].meta.get("locators") or {}).get("number") == "Abstract"),
                  None)
        ab_text = (resolve_refs(store, ab, store.entities[ab].levels.get("formal") or "")
                   if ab else get("abstract", W.abstract(doc)))
        blocks = [{"id": "abstract", "type": "abstract", "text": ab_text, "verbatim": bool(ab)}]
        get = lambda slot, fb: ""
    else:
        blocks = [{"id": "abstract", "type": "abstract",
                   "text": get("abstract", W.abstract(doc))},
                  {"id": "introduction", "type": "framing",
                   "text": get("introduction", W.introduction(doc))}]
    if sel["assumed"]:
        blocks.append({"id": "s:assumptions", "type": "section",
                       "title": "What we assume"})
        for a in sel["assumed"]:
            blocks.append(claim_block(store, a, "postulate", level))
    prev = None
    shown_premises = {}
    for c in sel["order"]:
        for d in store.entities[c].derivations():
            if isinstance(d, dict) and d.get("name") == sel["derivation"].get(c):
                shown_premises[c] = set(_premises(d))
    for s in sections:
        blocks.append({"id": f"s:{s['key']}", "type": "section", "title": s["title"]})
        blocks.append({"id": f"i:{s['key']}", "type": "framing",
                       "text": get(f"i:{s['key']}", W.section_intro(s))})
        for c in s["claims"]:
            if store.entities[c].kind == "note":
                if sel.get("inline_notes"):
                    blocks.append(claim_block(store, c, "note", level))
                continue
            slot = f"t:{prev or '^'}>{c}"
            blocks.append({"id": slot, "type": "transition",
                           "between": [prev, c],
                           "text": get(slot, W.transition(prev, c,
                                                          prev in shown_premises.get(c, ())))})
            blocks.append(claim_block(store, c, _shown_type(store, c), level,
                                      sel["derivation"].get(c)))
            if not sel.get("inline_notes"):
                for n in (sel.get("notes") or {}).get(c, []):
                    blocks.append(claim_block(store, n, "note", level))
            prev = c
    if sel["cited"]:
        blocks.append({"id": "s:cited", "type": "section",
                       "title": "Results cited, not shown"})
        for c in sel["cited"]:
            st = store.entities[c].status
            blocks.append(claim_block(store, c, "conjecture" if st == "conjectured"
                                      else "fact", level))
    placed = {b["id"] for b in blocks}
    for r in sel["refutations"]:
        if f"c:{r}" not in placed:
            blocks.append(claim_block(store, r, "refutation", level))
    for p in sel["predictions"]:
        if f"c:{p}" not in placed:
            blocks.append(claim_block(store, p, "prediction", level))
    blocks.append({"id": "conclusion", "type": "framing",
                   "text": get("conclusion", W.conclusion(doc))})
    for b in blocks:
        if "hash" not in b:
            b["hash"] = _h(b.get("text", "") + b.get("title", ""))
    return blocks


def number_blocks(blocks):
    n = 0
    for b in blocks:
        if b["type"] in ("theorem", "fact", "postulate", "conjecture", "refutation",
                         "prediction", "definition"):
            n += 1
            b["number"] = n
    return blocks


# ---------------------------------------------------------------------------
# audit
# ---------------------------------------------------------------------------

def split_sentences(text):
    """Sentences, each ending at its tag.  A chunk is cut after every tag;
    any sentence inside a chunk that ends before the chunk's tag is returned
    on its own, untagged, so it fails the audit."""
    out = []
    for chunk in re.split(r"(?<=\]\])\s+", text.strip()):
        parts = [p.strip() for p in SENT_RE.split(chunk) if p.strip()]
        # re-attach a tag that the sentence splitter separated from its sentence
        merged = []
        for p in parts:
            if merged and TAG_RE.fullmatch(p):
                merged[-1] += " " + p
            else:
                merged.append(p)
        out += merged
    return out


def audit(store, recipe, blocks, graph_checks):
    findings = []
    for b in blocks:
        if b.get("conflict"):
            findings.append(("D112", b["id"], "your edit to this block is kept, but the "
                             "result under it changed ("
                             + str(b["conflict"].get("claim_change")) + "); resolve it with "
                             "set_override, or remove the override to take the new text"))
    eff = derive.effective_status(store)
    for b in blocks:
        cid = (b.get("claim") or "").split("@")[0]
        e = store.entities.get(cid)
        if e is not None and e.status == "proved" and eff.get(cid) != "proved" \
                and b["type"] != "refutation":
            findings.append(("D111", b["id"], f"{cid} is declared proved but rests on "
                             f"something weaker (effective: {eff.get(cid)}); it is shown "
                             "as a conjecture until its premises are settled"))
    ids_in_doc = {b["claim"].split("@")[0] for b in blocks if b.get("claim")}
    banned = [w.lower() for w in (store.config.get("house_style") or {}).get(
        "banned_words", [])]
    for b in blocks:
        if b["type"] not in ("transition", "framing", "abstract") or b.get("verbatim"):
            continue
        for s in split_sentences(b["text"]):
            tags = TAG_RE.findall(s)
            body = TAG_RE.sub("", s)
            if not tags:
                findings.append(("D101", b["id"], f"untagged sentence: {body[:80]}"))
                continue
            claims = [t[2:] for t in tags if t.startswith("c:")]
            for c in claims:
                if c not in ids_in_doc:
                    findings.append(("D102", b["id"], f"cites {c}, which is not in "
                                     "this document"))
            nums = set(NUM_TOKEN.findall(re.sub(r"\[\[.*?\]\]", "", body)))
            if tags == ["t"]:
                if nums or "$" in body:
                    findings.append(("D103", b["id"], "a transition carries content "
                                     f"(numbers or maths): {body[:80]}"))
            elif nums:
                pool = " ".join((store.entities[c].levels.get(lv) or "")
                                for c in claims if c in store.entities
                                for lv in ("formal", "technical", "lay", "one-liner"))
                pool_nums = set(NUM_TOKEN.findall(pool))
                missing = [n for n in nums if n not in pool_nums]
                if missing:
                    findings.append(("D104", b["id"], f"number(s) {missing} appear in "
                                     f"no cited claim: {body[:80]}"))
    for b in blocks:
        txt = " ".join(str(b.get(k, "")) for k in ("text", "title", "proof"))
        if DASH_RE.search(re.sub(r"(?<!\\)%.*", "", txt)):
            findings.append(("D105", b["id"], "em dash"))
        for w in banned:
            if re.search(r"\b" + re.escape(w) + r"\b", txt, re.I):
                findings.append(("D106", b["id"], f"banned word '{w}'"))
        if b.get("gap"):
            findings.append(("D107", b["id"], f"{b['level']} text is pending for "
                             f"{b['claim']}"))
        if b.get("claim"):
            cid = b["claim"].split("@")[0]
            if graph_checks.get(cid) == "fail":
                findings.append(("D108", b["id"], f"check for {cid} is red"))
    ab = next((b for b in blocks if b["type"] == "abstract"), None)
    lo, hi = (recipe.get("budget") or {}).get("abstract_words", [0, 10 ** 6])
    if ab:
        n = len(TAG_RE.sub("", ab["text"]).split())
        if not lo <= n <= hi:
            findings.append(("D109", "abstract", f"abstract has {n} words; budget "
                             f"{lo} to {hi}"))
    findings.append(("D110", "document", "AI judge not configured: entailment of "
                     "tagged sentences by their claims was not checked"))
    return [{"code": c, "block": b, "message": m} for c, b, m in findings]


# ---------------------------------------------------------------------------
# rendering
# ---------------------------------------------------------------------------

PROVED_ENVS = {"Prop": "proposition", "Proposition": "proposition",
               "Lemma": "lemma", "Lem": "lemma", "Cor": "corollary",
               "Corollary": "corollary", "Thm": "theorem", "Theorem": "theorem",
               "Fact": "assembled", "Principle": "principle"}

ENV_NAME = {"theorem": "theorem", "fact": "fact", "postulate": "postulate",
            "conjecture": "conjecture", "refutation": "refutation",
            "prediction": "prediction", "definition": "definition"}


def _strip_tags(text):
    return re.sub(r"\s*\[\[(?:c:[a-z0-9.\-]+|t)\]\]", "", text)


_IN_DOC = set()
_TITLES = {}


_SHORT_SRC = {}


def _claimrefs_tex(text):
    def sub(m):
        cid = m.group(1)
        if cid in _IN_DOC:
            return r"\ref{c:" + cid + "}"
        where = _SHORT_SRC.get(cid)
        return r"\emph{" + _tex_title(_TITLES.get(cid, cid)) + "}" + (" [" + _tex_title(where) + "]" if where else "")
    return re.sub(r"\\claimref\{([^}]+)\}", sub, text)


_LAST_SUB = [None]

# ---- the series' deposited papers (store/references.yaml: ButlerT<n>, with a Zenodo DOI)
_PAPER_RE = re.compile(r"^T0*(\d+)([a-c]?)$")
ZENODO_COMMUNITY = "https://zenodo.org/communities/transport-papers"
AUTHOR = {"name": "Leon Butler", "email": "lbutler.math@gmail.com", "orcid": "0009-0006-4449-5617"}


def _refs(store):
    try:
        import yaml
        return yaml.safe_load(open(os.path.join(store.root, "references.yaml"))) or {}
    except Exception:
        return {}


def paper_key(code):
    """'T07' or 'T7' -> 'ButlerT7'; 'T14a' -> 'ButlerT14a'; anything else -> None."""
    m = _PAPER_RE.match(str(code or ""))
    return f"ButlerT{int(m.group(1))}{m.group(2)}" if m else None


def paper_meta(store, code, refs=None):
    """Short name, title, subtitle and DOI of a deposited paper, from its reference entry."""
    key = paper_key(code)
    ent = (refs if refs is not None else _refs(store)).get(key) if key else None
    if not ent:
        return None
    cit = str(ent.get("citation") or "")
    m = re.match(r"L\. Butler, (.*?), Transport Papers (T\d+[a-c]?)", cit, re.S)
    full = re.sub(r"\s+", " ", m.group(1)) if m else ""
    title, _, sub = full.partition(": ")
    return {"short": m.group(2) if m else code, "title": title, "subtitle": sub,
            "doi": ent.get("doi")}


def _doi_tex(doi):
    return r"\href{https://doi.org/%s}{doi:%s}" % (doi, doi) if doi else ""


def source_line(store, eid, refs=None):
    """'T5, Thm 4.2 (doi:...)' for a result extracted from a deposited paper, else ''."""
    e = store.entities[eid]
    loc = e.meta.get("locators") or {}
    code, num = loc.get("paper"), loc.get("number")
    if e.meta.get("programme") == "standard" and not code:
        srcs = loc.get("sources") or []
        txt = "the algebra core of the Physics Graph, proved there with an exact check"
        if srcs:
            r = (refs if refs is not None else _refs(store)).get(srcs[0].get("key"), {})
            cit = str(r.get("citation") or srcs[0].get("key", ""))
            txt += "; standard, see " + cit.rstrip(".") + (", " + srcs[0]["locator"] if srcs[0].get("locator") else "")
        return txt
    if not code:
        return ""
    meta = paper_meta(store, str(code).split("-")[0], refs)
    name = meta["short"] if meta else str(code)
    if "-" in str(code):
        name += " (" + str(code).split("-", 1)[1].replace("-", " ") + " note)"
    out = name + (", " + str(num) if num else "")
    if meta and meta.get("doi"):
        out += " (" + _doi_tex(meta["doi"]) + ")"
    return out


def render_latex(store, recipe, blocks):
    _LAST_SUB[0] = None
    _IN_DOC.clear()
    _IN_DOC.update(b["claim"].split("@")[0] for b in blocks if b.get("claim"))
    _TITLES.clear()
    _TITLES.update({k: e.title for k, e in store.entities.items()})
    _SHORT_SRC.clear()
    for k, e in store.entities.items():
        loc = e.meta.get("locators") or {}
        if loc.get("paper") and loc.get("number"):
            pc = str(loc["paper"])
            m = _PAPER_RE.match(pc.split("-")[0])
            _SHORT_SRC[k] = (f"T{int(m.group(1))}{m.group(2)}" if m else pc) + ", " + str(loc["number"])
        elif e.meta.get("programme") == "standard":
            _SHORT_SRC[k] = "algebra core"
    notation = store.notation or {}
    macros = "\n".join(r"\providecommand{\%s}{}\renewcommand{\%s}{%s}" % (k, k, v)
                       for k, v in sorted(notation.items()) if "#" not in v)
    argmacros = "\n".join(r"\providecommand{\%s}{}\renewcommand{\%s}[%d]{%s}" % (
        k, k, max(int(n) for n in re.findall(r"#(\d)", v)), v)
        for k, v in sorted(notation.items()) if "#" in v)
    disclaimer = (store.config.get("house_style") or {}).get("disclaimer", "")
    refs = _refs(store)
    code = recipe.get("paper")
    meta = paper_meta(store, code, refs) if code and "-" not in str(code) else None
    title = re.sub(r"\s*\((regenerated|recreated)[^)]*\)\s*$", "", recipe.get("title", recipe["doc"]))
    subtitle = recipe.get("subtitle") or ""
    if meta and meta["title"]:
        title, subtitle = meta["title"], subtitle or meta["subtitle"]
    series = (r" \textperiodcentered{} Transport Papers, " + meta["short"]) if meta else ""
    chg = None
    if meta and meta.get("doi"):
        from . import deposits
        try:
            chg = deposits.compare(store, store.root, str(code), blocks)
        except Exception:                      # a missing or unreadable deposit: no marks
            chg = None
    marked = {}                                # block id -> (environment word, claim id)
    today = dt.date.today()
    gen_date = f"{today.day} {today.strftime('%B %Y')}"
    if meta and meta.get("doi"):
        footer = (r"Generated by the Physics Graph, not the version of record. Official version: "
                  r"\href{https://doi.org/" + meta["doi"] + "}{doi:" + meta["doi"] + "}")
    else:
        footer = (r"Generated by the Physics Graph from approved parts of its store; not a deposited paper. "
                  r"Papers of record: \href{" + ZENODO_COMMUNITY + "}{Zenodo, Transport Papers}")
    out = [r"\documentclass[11pt]{article}",
           r"\usepackage[margin=1.1in]{geometry}",
           r"\usepackage{amsmath,amssymb,amsthm,mathtools,booktabs,array,tabularx,longtable}",
           r"\usepackage[dvipsnames]{xcolor}",
           r"\usepackage[colorlinks=true,linkcolor=MidnightBlue,citecolor=MidnightBlue,urlcolor=MidnightBlue]{hyperref}",
           r"\usepackage{fancyhdr}",
           r"\pagestyle{fancy}\fancyhf{}\renewcommand{\headrulewidth}{0pt}",
           r"\fancyfoot[R]{\thepage}",
           r"\fancyfoot[L]{\scriptsize\color{gray}" + footer + "}",
           r"\fancypagestyle{plain}{\fancyhf{}\fancyfoot[R]{\thepage}\fancyfoot[L]{\scriptsize\color{gray}"
           + footer + r"}\renewcommand{\headrulewidth}{0pt}}",
           r"\newtheorem{theorem}{Theorem}[section]",
           r"\newtheorem{proposition}[theorem]{Proposition}",
           r"\newtheorem{lemma}[theorem]{Lemma}",
           r"\newtheorem{corollary}[theorem]{Corollary}",
           r"\newtheorem{conjecture}[theorem]{Conjecture}",
           r"\newtheorem{refutation}[theorem]{Refutation}",
           r"\newtheorem{prediction}[theorem]{Prediction}",
           r"\newtheorem{principle}[theorem]{Principle}",
           r"\newtheorem{observation}[theorem]{Observation}",
           r"\newtheorem{axiom}[theorem]{Axiom}",
           r"\theoremstyle{definition}",
           r"\newtheorem{definition}[theorem]{Definition}",
           r"\newtheorem{fact}[theorem]{Fact}",
           r"\newtheorem{assembled}[theorem]{Assembly}",
           r"\newtheorem{postulate}[theorem]{Postulate}",
           r"\newtheorem{premise}[theorem]{Premise}",
           r"\newtheorem{hypothesis}[theorem]{Hypothesis}",
           r"\newtheorem{remark}[theorem]{Remark}",
           r"\newtheorem{example}[theorem]{Example}",
           r"\theoremstyle{plain}",
           r"\setlength{\marginparwidth}{0.8in}",
           r"\newcommand{\changedmark}[2]{\marginpar{\raggedright\scriptsize\color{#1}#2}}",
           macros, argmacros,
           r"\title{\bfseries " + title + (r"\\[4pt]\large\itshape " + subtitle if subtitle else "") + "}",
           r"\author{" + AUTHOR["name"] + r"\\ \normalsize\href{mailto:" + AUTHOR["email"] + r"}{\texttt{"
           + AUTHOR["email"] + r"}}\\ \normalsize ORCID: \href{https://orcid.org/" + AUTHOR["orcid"]
           + "}{" + AUTHOR["orcid"] + "}}",
           r"\date{Generated by the Physics Graph, " + gen_date + series
           + (r"\\[3pt]\small Official version: \href{https://doi.org/" + meta["doi"] + "}{doi:"
              + meta["doi"] + "}" if meta and meta.get("doi") else "") + "}",
           r"\begin{document}", r"\maketitle"]
    if meta and meta.get("doi"):
        about = (r"\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{\textbf{This is not the "
                 r"version of record.} The official version of this paper is the one deposited on Zenodo, "
                 + _doi_tex(meta["doi"]) + r". This PDF was generated by the Physics Graph on " + gen_date
                 + r" and assembled from approved parts of its store: the results, proofs and text of "
                 r"the paper as the store holds them, each result with its premises and machine checks. "
                 r"It is regenerated when a result it contains is corrected, so it may differ from the "
                 r"deposited paper. " + _changes_notice(chg) + "}}")
    else:
        about = (r"\noindent\fbox{\parbox{\dimexpr\linewidth-2\fboxsep-2\fboxrule}{\textbf{This is not a "
                 r"deposited paper.} It was generated by the Physics Graph on " + gen_date + r" and "
                 r"assembled from approved parts of its store. It follows results across several papers "
                 r"of the series; each is stated with its proof and credited to the paper that first "
                 r"proved it. The official versions of those papers are on Zenodo, in the Transport "
                 r"Papers community, \url{" + ZENODO_COMMUNITY + "}.}}")
    paper_form = recipe.get("sections") == "paper"
    held = []            # paper recreations: the assumptions come after the Introduction
    seen_sections = [0]
    section = [None]
    for b in blocks:
        t = b["type"]
        if b.get("conflict"):
            out.append(r"\noindent\fbox{\parbox{\linewidth}{\textbf{Edit conflict.} The "
                       r"passage below is a human edit; the result under it has changed "
                       r"since. See the changelog.}}")
        if t == "abstract":
            out += [r"\begin{abstract}", r"\normalsize", _claimrefs_tex(_strip_tags(b["text"])),
                    r"\end{abstract}"]
            if recipe.get("msc") or recipe.get("keywords"):
                out.append(r"\medskip")
                if recipe.get("msc"):
                    out.append(r"\noindent\textbf{MSC 2020.} " + recipe["msc"] + r"\\")
                if recipe.get("keywords"):
                    out.append(r"\textbf{Keywords.} " + recipe["keywords"])
            out += [r"\newpage", r"\noindent " + disclaimer if disclaimer else "", "",
                    about, r"\newpage"]
        elif t == "section":
            section[0] = b["id"]
            if paper_form and b["id"] == "s:assumptions":
                continue
            if paper_form and b["id"] != "s:assumptions" and held and seen_sections[0] == 1:
                out.append(r"\section*{What we assume}")
                out.append(r"The results below are taken as given in this paper; each result that "
                           r"rests on one says so.")
                out += held
                held.clear()
            seen_sections[0] += 1
            if b["id"] == "s:cited":
                out.append(r"\section{Results used from elsewhere}")
                out.append(r"The proofs above use the following results of the series, stated "
                           r"briefly; each is proved in the paper named.")
            else:
                out.append(r"\section{" + _tex_title(b["title"]) + "}")
        elif t in ("framing", "transition"):
            txt = _claimrefs_tex(_tex_title(_strip_tags(b["text"])))
            if not txt.strip():
                continue
            if b["id"] == "conclusion":
                out.append(r"\section*{Conclusion}")
            elif b["id"] == "introduction":
                out.append(r"\section*{Introduction}")
            out.append(txt)
        else:
            env = ENV_NAME.get(t, "theorem")
            cid = b["claim"].split("@")[0]
            if t == "note" and store.entities[cid].status == "setting":
                e = store.entities[cid]
                sub = (e.meta.get("locators") or {}).get("subsection")
                if sub and sub != _LAST_SUB[0]:
                    out.append(r"\subsection*{" + _tex_title(sub) + "}")
                _LAST_SUB[0] = sub
                out.append(r"\phantomsection\label{c:%s}" % cid)
                out.append(_claimrefs_tex(b["text"]))
                out.append("")
                continue
            if t == "note":
                env = store.entities[cid].status       # remark or example
            if env == "theorem":
                # keep the source's own name for a proved result (Proposition, Lemma, ...)
                num = str(((store.entities[cid].meta.get("locators") or {}).get("number")) or "")
                env = PROVED_ENVS.get(num.split(" ")[0], "theorem")
            chunk = []
            if t == "note" and re.match(r"(Remark|Example) on ", b["title"]):
                chunk.append(r"\begin{%s}\label{c:%s}" % (env, cid))
            else:
                chunk.append(r"\begin{%s}[%s]\label{c:%s}" % (env, _tex_title(b["title"]), cid))
            text = b["text"]
            if section[0] == "s:cited":
                ol = (store.entities[cid].levels.get("one-liner") or "").strip()
                if ol and ol != "pending":
                    text = resolve_refs(store, cid, ol)
            mk = (chg or {}).get("blocks", {}).get(b["id"])
            if mk and (mk["kind"] == "revised" or (mk["kind"] == "added" and not mk["cited"])):
                colour, word = (("MidnightBlue", "added since the deposit") if mk["kind"] == "added"
                                else _MARK[mk["class"]])
                chunk.append(r"\changedmark{" + colour + "}{" + word + "}")
                marked[b["id"]] = (env, cid)
            chunk.append(_claimrefs_tex(text))
            src = source_line(store, cid, refs)
            prov = b.get("provenance") or ""
            if prov.startswith(("Physics Graph result", "Transport Lab claim")):   # the old wording in stored documents
                prov = src or prov
            if t in ("theorem", "conjecture") and src and (
                    not code or str((store.entities[cid].meta.get("locators") or {}).get("paper"))
                    .split("-")[0] != str(code).split("-")[0]):
                chunk.append(r"\emph{First proved in} " + src + ".")
            elif prov:
                chunk.append(r"\emph{Source:} " + _tex_title(prov) + ".")
            if paper_form and section[0] == "s:assumptions":
                held += chunk + [r"\end{%s}" % env, ""]
                continue
            out += chunk
            if b.get("kill_condition"):
                kc = b["kill_condition"]
                out.append(r"\emph{Kill condition:} " + kc.get("threshold", "") + ".")
            out.append(r"\end{%s}" % env)
            if b.get("proof"):
                out += [r"\begin{proof}", _claimrefs_tex(b["proof"]), r"\end{proof}"]
            elif b.get("rests_on"):
                rest = ", ".join(r"\ref{c:%s}" % p if f"c:{p}" in {x["id"] for x in blocks}
                                 else store.entities[p].title for p in b["rests_on"]
                                 if p in store.entities)
                out.append(r"\noindent\emph{Rests on:} " + rest + ".")
        out.append("")
    if held:
        out.append(r"\section*{What we assume}")
        out += held
    out += _changes_section(chg, marked)
    out += _bibliography(store, "\n".join(out))
    out.append(r"\end{document}")
    return "\n".join(out)


def _changes_notice(chg):
    """The sentence of the notice box that says how this PDF differs from the deposit."""
    if chg is None:
        return r"Where it does, the store records why."
    from .deposits import summary_sentence
    s = summary_sentence(chg)
    if not (chg["summary"]["revised"] or chg["summary"]["added"] or chg["summary"]["removed"]):
        return _plain_tex(s)
    return (_plain_tex(s) + r" Each revised or added result is marked in the margin "
            r"(\textcolor{BrickRed}{corrected}, \textcolor{BurntOrange}{changed}, "
            r"\textcolor{gray}{reworded}), and the last section, \emph{Changes since the deposited "
            r"version}, lists them with the reason for each.")


_NOTE_KEEP = 3


def _clip(t, n=360):
    """A note cut at a word boundary near n characters."""
    t = " ".join((t or "").split())
    if len(t) <= n:
        return t
    return t[:n].rsplit(" ", 1)[0].rstrip(",;:") + " [...]"


def _plain_tex(t):
    """Plain text for LaTeX: maths between dollar signs kept, everything else escaped."""
    parts = re.split(r"(\$[^$]*\$)", t or "") if (t or "").count("$") % 2 == 0 else [t or ""]
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) > 1:
            out.append(p)
            continue
        p = p.replace("\\", "\x00")
        for a, b in (("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_"), ("{", r"\{"),
                     ("}", r"\}"), ("$", r"\$"), ("^", r"\^{}"), ("~", r"\~{}")):
            p = p.replace(a, b)
        out.append(p.replace("\x00", r"\textbackslash{}"))
    return "".join(out)


_MARK = {"corrected": ("BrickRed", "corrected since the deposit"),
         "changed": ("BurntOrange", "changed since the deposit"),
         "reworded": ("gray", "reworded")}
_HEADINGS = (("corrected", "Corrected", "The deposited version was wrong or claimed too much here."),
             ("changed", "Changed", "The content changed by a later decision, not because the "
              "deposited version was wrong."),
             ("reworded", "Reworded", "Wording, notation, terminology or citations only; the "
              "mathematics and the claim are as deposited."))


def _changes_section(chg, marked):
    """The closing section of a regenerated paper: every result revised or added since the
    deposited version, with the store's notes on it, and the deposited results withdrawn."""
    if chg is None:
        return []
    from .deposits import summary_sentence
    s = chg["summary"]
    out = [r"\section*{Changes since the deposited version}",
           r"\addcontentsline{toc}{section}{Changes since the deposited version}",
           _plain_tex(summary_sentence(chg)) + r" The comparison is with the source of version "
           + _plain_tex(chg["version"]) + r" on Zenodo, " + _doi_tex(chg["doi"]) + r". A result counts as "
           r"revised when the words or mathematics of its statement or proof differ from that "
           r"source; a citation added in a parenthesis does not count. A result the paper cites "
           r"from elsewhere is compared with the deposit of the paper that proves it. Each "
           r"revision is classed as corrected, changed or reworded; the classes were assigned "
           r"by a review of each difference and the store's record of why it was made, and a "
           r"revision not yet reviewed is counted as changed."]
    rows = [(bid, x) for bid, x in chg["blocks"].items() if bid in marked]

    def head(bid, x):
        env, cid = marked[bid]
        h = env.capitalize() + r"~\ref{c:" + cid + r"} (\emph{" + _tex_title(x["title"]) + "})"
        if x.get("deposited_number"):
            h += ", " + _plain_tex(x["deposited_number"]) + " in the deposit"
        return h

    for cls, heading, gloss in _HEADINGS:
        items = [(bid, x) for bid, x in rows if x["kind"] == "revised" and x["class"] == cls]
        if not items:
            continue
        out += [r"\subsection*{" + heading + "}", gloss, r"\begin{itemize}\setlength{\itemsep}{2pt}"]
        for bid, x in items:
            h = head(bid, x) + ": " + x["what"] + "."
            if x.get("why") and x.get("reviewed"):
                h += " " + _plain_tex(x["why"])
            if cls != "reworded":
                notes = x["notes"][-2:]
                if notes:
                    h += r" \emph{Store notes.} " + " ".join(r"\emph{" + n["date"] + r":} "
                                                            + _plain_tex(_clip(n["note"])) for n in notes)
            out.append(r"\item " + h)
        out.append(r"\end{itemize}")
    items = [(bid, x) for bid, x in rows if x["kind"] == "added"]
    if items:
        out += [r"\subsection*{Added}", r"Results stated here that the deposited paper did not state.",
                r"\begin{itemize}\setlength{\itemsep}{2pt}"]
        for bid, x in items:
            notes = x["notes"][-1:]
            out.append(r"\item " + head(bid, x) + "." + ("" if not notes else " " + _plain_tex(_clip(notes[0]["note"]))))
        out.append(r"\end{itemize}")
    extra = []
    if s["added_cited"]:
        extra.append(f"{s['added_cited']} result{'s' if s['added_cited'] != 1 else ''} from elsewhere in "
                     r"the series or the algebra core are stated here that the deposited paper cited "
                     r"or used without stating")
    if s["citations"]:
        extra.append(f"{s['citations']} result{'s' if s['citations'] != 1 else ''} gained citations only")
    if extra:
        out.append(r"\noindent In addition, " + "; ".join(extra) + ". These are not marked.")
    if chg["removed"]:
        out += [r"\subsection*{Withdrawn}", r"\begin{itemize}"]
        for x in chg["removed"]:
            out.append(r"\item " + _plain_tex(x["deposited_number"]) + r" (\emph{" + _tex_title(x["title"])
                       + "}): " + _plain_tex(x["why"]) + ".")
        out.append(r"\end{itemize}")
    return out


def _tex_title(t):
    """A title as LaTeX: maths in $...$ kept, stray _ ^ & % # outside it escaped
    (some extracted titles lost their dollar signs)."""
    parts = re.split(r"(\$[^$]*\$)", t or "")
    out = []
    for i, p in enumerate(parts):
        if i % 2:
            out.append(p)
        else:
            p = re.sub(r"(?<!\\)_", r"\\_", p)
            p = re.sub(r"(?<!\\)\^", r"\\^{}", p)
            p = re.sub(r"(?<!\\)([&%#])", r"\\\1", p)
            p = re.sub(r"\\(mathrm|mathfrak|mathbb|mathcal)\{([^}]*)\}", r"$\\\1{\2}$", p)
            out.append(p)
    return "".join(out)


def _bibliography(store, tex):
    """The cited entries, printed from the store's reference registry."""
    keys = []
    for m in re.finditer(r"\\cite[pt]?\*?(?:\[[^\]]*\])*\{([^}]+)\}", tex):
        for k in m.group(1).split(","):
            k = k.strip()
            if k and k not in keys:
                keys.append(k)
    if not keys:
        return []
    path = os.path.join(store.root, "references.yaml")
    refs = yaml.safe_load(open(path)) if os.path.exists(path) else {}
    out = [r"\begin{thebibliography}{99}"]
    for k in keys:
        txt = (refs.get(k) or {}).get("latex") or (r"\emph{Reference %s is not in the "
                                                    r"store's registry.}" % k)
        out.append(r"\bibitem{%s} %s" % (k, txt))
    out.append(r"\end{thebibliography}")
    return out


def render_markdown(store, recipe, blocks):
    out = [f"# {recipe.get('title', recipe['doc'])}", ""]
    for b in blocks:
        t = b["type"]
        if b.get("conflict"):
            out += ["> **Edit conflict.** The passage below is a human edit; the result "
                    "under it has changed since. See the changelog.", ""]
        if t == "abstract":
            out += ["**Abstract.** " + _strip_tags(b["text"]), ""]
        elif t == "section":
            out += [f"## {b['title']}", ""]
        elif t in ("framing", "transition"):
            out += [_strip_tags(b["text"]), ""]
        else:
            if t == "note":
                t = store.entities[b["claim"].split("@")[0]].status
            label = {"theorem": "Theorem", "fact": "Fact (imported)", "remark": "Remark",
                     "example": "Example",
                     "postulate": "Postulate", "conjecture": "Conjecture",
                     "refutation": "Refutation", "prediction": "Prediction",
                     "definition": "Definition"}.get(t, t)
            out += [f"**{label} {b.get('number', '')} ({b['title']}).** {b['text']}", ""]
            if b.get("provenance"):
                out += [f"*Provenance:* {b['provenance']}.", ""]
            if b.get("proof"):
                out += ["*Proof.* " + b["proof"], ""]
            if b.get("rests_on"):
                out += ["*Rests on:* " + ", ".join(b["rests_on"]), ""]
    return "\n".join(out)


def verify_script(store, blocks):
    """Assemble the document's verify script from its claims' evidence."""
    legacy = defaultdict(set)
    checks = []
    for b in blocks:
        if not b.get("claim"):
            continue
        cid = b["claim"].split("@")[0]
        e = store.entities[cid]
        for ev in e.meta.get("checked_by") or []:
            if ev.get("kind") == "legacy":
                legacy[ev["script"]].update(ev.get("tags") or [])
            elif ev.get("kind") == "check":
                checks.append((cid, os.path.relpath(e.path, store.root), ev["ref"]))
    lines = ['"""Verify script assembled from the claims in this document.',
             "Runs each claim's own check and the tagged checks of the series verify",
             'scripts it relies on.  Exact arithmetic throughout (GA.py)."""',
             "import os, sys", "HERE = os.path.dirname(os.path.abspath(__file__))",
             "LAB = os.path.abspath(os.path.join(HERE, '..', '..'))",
             "sys.path[:0] = [os.path.join(LAB, 'lib'), LAB]",
             "import GA", "from tp import evidence",
             "from tp.model import load_store",
             "from tp.validate import legacy_path",
             f"STORE = os.path.join(LAB, {os.path.basename(store.root)!r})",
             f"LEGACY_DIR = os.path.normpath(os.path.join(STORE, "
             f"{store.config.get('legacy_scripts_dir', '.')!r}))",
             "LEGACY = " + json.dumps({k: sorted(v) for k, v in sorted(legacy.items())},
                                      indent=1),
             f"CHECKS = {checks!r}", "",
             "def main():",
             "    global _STORE, _LDIR",
             "    _STORE = load_store(STORE)",
             "    _LDIR = _STORE.config.get('legacy_scripts_dir')",
             "    ok = True",
             "    for script, tags in LEGACY.items():",
             "        res = evidence.run_legacy(legacy_path(_STORE, _LDIR, script),",
             "                                  os.path.join(STORE, '.tp-cache'))",
             "        hits = [(l, r) for l, r in res if evidence.label_keys(l) & set(tags)]",
             "        bad = [l for l, r in hits if not r]",
             "        GA.check(f'{script}: {len(hits)} tagged checks', bool(hits) and not bad)",
             "        ok &= bool(hits) and not bad",
             "    for cid, folder, ref in CHECKS:",
             "        fname, func = ref.split('::')",
             "        path = os.path.join(STORE, folder)",
             "        src = open(os.path.join(path, fname)).read()",
             "        r = evidence.run_check(STORE, path, src, func)",
             "        GA.check(f'{cid}: {ref}', r['ok'])",
             "        ok &= r['ok']",
             "    print(('ALL PASS' if ok else 'FAILURES: ' + str(len(GA.FAILURES))))",
             "    return 0 if ok else 1", "",
             "if __name__ == '__main__':", "    sys.exit(main())", ""]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# store a version
# ---------------------------------------------------------------------------

def _write_version(store, recipe, folder, blocks, version, changelog, overrides,
                   audit_findings, old_md=None):
    os.makedirs(folder, exist_ok=True)
    claims = sorted({b["claim"] for b in blocks if b.get("claim")})
    manifest = {"doc": recipe["doc"], "version": version, "claims": claims,
                "recipe_hash": _h(yaml.safe_dump(recipe, sort_keys=True)),
                "generated": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                "spine": recipe["spine"]}
    md = render_markdown(store, recipe, blocks)
    tex = render_latex(store, recipe, blocks)
    files = {"recipe.yaml": yaml.safe_dump(recipe, sort_keys=False),
             "blocks.json": json.dumps(blocks, indent=1),
             "manifest.json": json.dumps(manifest, indent=1),
             "rendered.md": md, "rendered.tex": tex,
             "audit.json": json.dumps(audit_findings, indent=1),
             "overrides.json": json.dumps(overrides, indent=1),
             f"verify_{recipe['doc'].replace('-', '_')}.py": verify_script(store, blocks)}
    for name, text in files.items():
        with open(os.path.join(folder, name), "w", encoding="utf-8") as fh:
            fh.write(text)
    snap = os.path.join(folder, "versions", f"v{version}")
    os.makedirs(snap, exist_ok=True)
    for name in ("blocks.json", "manifest.json", "rendered.md", "rendered.tex", "audit.json"):
        with open(os.path.join(snap, name), "w", encoding="utf-8") as fh:
            fh.write(files[name])
    log_path = os.path.join(folder, "changelog.md")
    entry = [f"## v{version} ({manifest['generated']})", ""] + \
        [f"- {c}" for c in changelog] + [""]
    prev = f"# Changelog: {recipe['doc']}\n\n"
    if os.path.exists(log_path):
        with open(log_path, encoding="utf-8") as fh:
            prev = fh.read()
    head, _, rest = prev.partition("\n\n")
    with open(log_path, "w", encoding="utf-8") as fh:
        fh.write(head + "\n\n" + "\n".join(entry) + "\n" + rest)
    if old_md is not None:
        diff = difflib.unified_diff(old_md.splitlines(), md.splitlines(),
                                    f"v{version - 1}", f"v{version}", lineterm="")
        with open(os.path.join(snap, "redline.diff"), "w", encoding="utf-8") as fh:
            fh.write("\n".join(diff))
        html = difflib.HtmlDiff(wrapcolumn=90).make_file(
            old_md.splitlines(), md.splitlines(), f"v{version - 1}", f"v{version}",
            context=True, numlines=2)
        with open(os.path.join(snap, "redline.html"), "w", encoding="utf-8") as fh:
            fh.write(html)
    return manifest


def _context(store_root):
    store = load_store(store_root)
    rep = validate(store, layers=(1, 2, 3), keep_going=True)
    _EFF.clear()
    _EFF.update(getattr(rep, "eff", {}) or {})
    _REG.clear()
    _REG.update(labelreg.load(store_root))
    return store, rep


def _checks(store_root):
    p = os.path.join(os.path.dirname(os.path.abspath(store_root)), "build", "graph.json")
    if os.path.exists(p):
        return {n["id"]: n["check"] for n in json.load(open(p))["nodes"]}
    return {}


def _writer(store, recipe, folder):
    prose_path = os.path.join(folder, "prose.json")
    if os.path.exists(prose_path):
        return FileWriter(store, recipe.get("level"), json.load(open(prose_path)))
    return TemplateWriter(store, recipe.get("level"))


def generate(store_root, recipe_path):
    recipe = yaml.safe_load(open(recipe_path))
    check_doc_id(recipe.get("doc"))
    folder = os.path.join(docs_root(store_root), recipe["doc"])
    if os.path.exists(os.path.join(folder, "manifest.json")):
        return regenerate(store_root, recipe["doc"], recipe=recipe)
    store, rep = _context(store_root)
    sel = select(store, recipe, rep.ledger)
    sections = order_sections(store, sel, recipe)
    blocks = number_blocks(build_blocks(store, recipe, sel, sections,
                                       _writer(store, recipe, folder)))
    findings = audit(store, recipe, blocks, _checks(store_root))
    m = _write_version(store, recipe, folder, blocks, 1,
                       [f"first generation: {sum(1 for b in blocks if b.get('claim'))} "
                        "claim blocks"], {}, findings)
    return {"doc_id": recipe["doc"], "version": 1, "folder": folder, "bump": "new",
            "changelog": [], "selection": sel, "audit": findings, "manifest": m}


# ---------------------------------------------------------------------------
# regeneration from the stored version
# ---------------------------------------------------------------------------

DOC_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,80}$")


def check_doc_id(doc_id):
    """Document ids become folder names: lowercase letters, digits and hyphens only."""
    if not isinstance(doc_id, str) or not DOC_ID_RE.fullmatch(doc_id):
        raise ValueError(f"document id {doc_id!r} must be lowercase letters, digits "
                         "and hyphens")
    return doc_id


def b_type(b):
    return b.get("type")


def regenerate(store_root, doc_id, recipe=None):
    check_doc_id(doc_id)
    folder = os.path.join(docs_root(store_root), doc_id)
    old_blocks = json.load(open(os.path.join(folder, "blocks.json")))
    old_man = json.load(open(os.path.join(folder, "manifest.json")))
    overrides = json.load(open(os.path.join(folder, "overrides.json")))
    old_md = open(os.path.join(folder, "rendered.md"), encoding="utf-8").read()
    recipe = recipe or yaml.safe_load(open(os.path.join(folder, "recipe.yaml")))
    store, rep = _context(store_root)
    graph_checks = _checks(store_root)
    st = derive.staleness(store, {k for k, v in graph_checks.items() if v == "fail"},
                          rep.graph)
    sel = select(store, recipe, rep.ledger)
    sections = order_sections(store, sel, recipe)
    fresh = number_blocks(build_blocks(store, recipe, sel, sections,
                                       _writer(store, recipe, folder)))
    fresh_by = {b["id"]: b for b in fresh}
    old_by = {b["id"]: b for b in old_blocks}

    # 1. classify claims
    old_claims = {c.split("@")[0]: int(c.split("@")[1]) for c in old_man["claims"]}
    new_claims = {b["claim"].split("@")[0]: int(b["claim"].split("@")[1])
                  for b in fresh if b.get("claim")}
    cls = {}
    for c in set(old_claims) | set(new_claims):
        if c not in new_claims:
            cls[c] = "removed"
        elif c not in old_claims:
            cls[c] = "added"
        elif new_claims[c] > old_claims[c]:
            cls[c] = "revised-substantive"
        else:
            ob, nb = old_by.get(f"c:{c}"), fresh_by.get(f"c:{c}")
            cls[c] = ("revised-cosmetic" if ob and nb and ob["hash"] != nb["hash"]
                      else "unchanged")
        ob = old_by.get(f"c:{c}")
        if c in store.entities and store.entities[c].status == "refuted" \
                and cls[c] != "removed" and not (ob and ob["type"] == "refutation"):
            cls[c] = "refuted"
        if c in st["stale"] and cls[c] == "unchanged":
            cls[c] = "stale"
    changed = {c for c, k in cls.items() if k != "unchanged"}

    # 2. which blocks are affected
    def affected(b):
        if b.get("claim"):
            return b["claim"].split("@")[0] in changed
        ob = old_by.get(b["id"])
        if ob is not None and ob.get("hash") != b.get("hash") and \
                b["type"] in ("transition", "framing", "abstract"):
            return True                 # its prose source changed
        if b["type"] == "transition":
            return any(x in changed for x in b.get("between") or [] if x)
        if b["id"] in ("abstract", "conclusion", "introduction"):
            spine_changed = any(cls.get(s) in ("revised-substantive", "refuted")
                                for s in recipe["spine"])
            return spine_changed or any(k in ("added", "removed") for k in cls.values())
        if b["type"] == "framing" and b["id"].startswith("i:"):
            key = b["id"][2:]
            return any(section_key(store, c) == key and c in changed
                       for c in new_claims if c in store.entities)
        return False

    # 3. placement: keep the old sequence, insert new blocks where the fresh
    #    sequence puts them relative to their nearest surviving predecessor
    out, used = [], set()
    old_ids = [b["id"] for b in old_blocks]
    fresh_ids = [b["id"] for b in fresh]
    def section_of(blocks):
        cur, out_ = None, {}
        for b in blocks:
            if b["type"] == "section":
                cur = b["id"]
            out_[b["id"]] = cur
        return out_
    old_sec, fresh_sec = section_of(old_blocks), section_of(fresh)
    # a block whose section changed (say a cited fact now shown) is placed afresh
    moved = {i for i in old_ids if i in fresh_by and b_type(fresh_by[i]) != "section"
             and old_sec.get(i) != fresh_sec.get(i)}
    survivors = [i for i in old_ids if i in fresh_by and i not in moved]
    inserts = defaultdict(list)          # anchor id -> new ids after it
    inserts_seen = set()
    for k, fid in enumerate(fresh_ids):
        if fid in old_by and fid not in moved:
            continue
        anchor = next((fresh_ids[j] for j in range(k - 1, -1, -1)
                       if fresh_ids[j] in old_by and fresh_ids[j] not in moved
                       or fresh_ids[j] in inserts_seen), None)
        inserts_seen.add(fid)
        inserts[anchor].append(fid)
    seq = []

    def place(i):
        seq.append(i)
        for j in inserts.get(i, []):
            place(j)
    for j in inserts.get(None, []):
        place(j)
    for i in survivors:
        place(i)
    # removed claims: drop, or keep as refutation per recipe
    on_ref = recipe.get("on_refuted", "keep-as-refutation")
    changelog, conflicts = [], []
    for c, k in sorted(cls.items()):
        if k != "unchanged":
            changelog.append(f"{c}: {k}")
    for i in sorted(moved):
        changelog.append(f"{i}: moved to {fresh_sec.get(i)}")
    for i in seq:
        nb, ob = fresh_by[i], old_by.get(i)
        cid = nb["claim"].split("@")[0] if nb.get("claim") else None
        if ob is not None and not affected(nb):
            b = copy.deepcopy(ob)                         # frozen: byte for byte
            if "number" in nb:
                b["number"] = nb["number"]
        else:
            b = copy.deepcopy(nb)
            if cid and cls.get(cid) == "refuted":
                if on_ref == "remove":
                    changelog.append(f"{cid}: refuted, removed from the document")
                    continue
                b["type"] = "refutation"
                b["refuted_by"] = store.entities[cid].meta.get("refuted_by") or []
        ov = overrides.get(i)
        if ov:
            if ob is not None and not affected(nb):
                b["text"] = ov["text"]
            else:
                b["conflict"] = {"override": ov["text"], "generated": nb.get("text"),
                                 "claim_change": cls.get(cid, "context changed")}
                b["text"] = ov["text"]
                conflicts.append(i)
                changelog.append(f"CONFLICT in {i}: your edit kept; its inputs changed "
                                 f"({cls.get(cid, 'neighbouring claims changed')})")
        out.append(b)
    for c, k in cls.items():
        if k == "removed":
            changelog.append(f"{c}: left the document's dependency cone, removed")
    old_num = {b["id"]: b.get("number") for b in old_blocks if b.get("number")}
    number_blocks(out)
    for b in out:
        if b.get("number") and old_num.get(b["id"]) and old_num[b["id"]] != b["number"]:
            changelog.append(f"renumbered {b['id']}: {old_num[b['id']]} -> {b['number']}")

    # 4. version bump
    spine_sub = any(cls.get(s) in ("revised-substantive", "refuted") for s in recipe["spine"])
    if spine_sub or any(k == "removed" for k in cls.values()):
        bump = "major"
    elif any(k in ("added", "revised-substantive") for k in cls.values()) or conflicts:
        bump = "minor"          # a shown result changed in substance, or an edit conflicts
    elif changed or conflicts or any(
            affected(fresh_by[i]) for i in seq if i in old_by):
        bump = "patch"
    else:
        bump = "none"
    if bump == "none":
        new_tex = render_latex(store, recipe, out)
        old_tex = open(os.path.join(folder, "rendered.tex"), encoding="utf-8").read()
        if new_tex != old_tex:
            bump = "patch"
            changelog.append("rendering changed (house style or template); no claim changed")
    if bump == "none":
        return {"doc_id": doc_id, "version": old_man["version"], "folder": folder,
                "bump": "none", "changelog": [], "classes": cls}
    findings = audit(store, recipe, out, graph_checks)
    version = old_man["version"] + 1
    _write_version(store, recipe, folder, out, version,
                   [f"bump: {bump}"] + changelog, overrides, findings, old_md)
    frozen = sum(1 for b in out if b["id"] in old_by and not affected(fresh_by.get(b["id"], b)))
    return {"doc_id": doc_id, "version": version, "folder": folder, "bump": bump,
            "changelog": changelog, "classes": cls, "conflicts": conflicts,
            "frozen_blocks": frozen, "total_blocks": len(out), "audit": findings}


def reaudit(store_root, doc_id):
    """Re-run the audit on the stored current version without a new version."""
    check_doc_id(doc_id)
    folder = os.path.join(docs_root(store_root), doc_id)
    store = load_store(store_root)
    recipe = yaml.safe_load(open(os.path.join(folder, "recipe.yaml")))
    blocks = json.load(open(os.path.join(folder, "blocks.json")))
    findings = audit(store, recipe, blocks, _checks(store_root))
    with open(os.path.join(folder, "audit.json"), "w", encoding="utf-8") as fh:
        json.dump(findings, fh, indent=1)
    return findings


def set_override(store_root, doc_id, block_id, text):
    """Record a human edit to one block; it survives regeneration."""
    check_doc_id(doc_id)
    folder = os.path.join(docs_root(store_root), doc_id)
    blocks = json.load(open(os.path.join(folder, "blocks.json")))
    b = next(x for x in blocks if x["id"] == block_id)
    ovp = os.path.join(folder, "overrides.json")
    ov = json.load(open(ovp))
    ov[block_id] = {"text": text, "base_hash": b["hash"]}
    b["text"] = text
    json.dump(ov, open(ovp, "w"), indent=1)
    json.dump(blocks, open(os.path.join(folder, "blocks.json"), "w"), indent=1)
