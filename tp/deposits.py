"""What has changed in a paper since the version deposited on Zenodo.

    python -m tp.deposits report <doc> [--store store]      the changes, as text
    python -m tp.deposits summary [--store store]            one line per deposited paper
    python -m tp.deposits record <code> --tex FILE --doi DOI --version V [--note ...]
                                                             a new deposit replaces the baseline

The baseline of a paper is the LaTeX source of its deposited version, kept in deposits/
with a manifest (deposits/deposits.yaml: DOI, printed version, file, sha256). A result is
compared with the deposit of the paper that states it (its locators.paper), so a Fact a
paper imports is compared with the deposit of the paper that proves it.

The comparison is textual, after a normalisation that undoes what extraction does to a
source: cross-references (\\ref, \\cite, \\claimref) and labels are dropped, layout
commands (\\small, \\setlength, \\centering, ...) and font commands are dropped, braces and
whitespace are dropped. A statement or proof is unchanged when what remains occurs in
the deposited source as it stands. So any change to the words or the mathematics counts,
including a change of notation or terminology; a change only to the premises cited, the
checks attached or the store's metadata does not.

For one document the result is:
  per result shown: "statement", "proof" (or both) when revised since its deposit,
                    "added" when the deposited paper did not contain it,
                    nothing when unchanged or when it has no deposited source to compare;
  removed:          results of the deposited paper the document no longer shows, with the
                    reason the store gives (refuted, merged into another result, ...).
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import re
import shutil
import sys
from functools import lru_cache

import yaml

DEPOSITS = "deposits"

_REF = re.compile(r"\\(?:claimref|ref|eqref|cref|Cref|autoref|label|cite[pt]?|url|href)\*?"
                  r"(?:\[[^\]]*\])?\{[^}]*\}")
_LAYOUT = re.compile(r"\\(?:setlength\{[^}]*\}\{[^}]*\}|[vh]space\*?\{[^}]*\}|small|footnotesize"
                     r"|scriptsize|normalsize|smallskip|medskip|bigskip|noindent|par|centering"
                     r"|raggedright|begingroup|endgroup|arraybackslash)(?![A-Za-z])")
_FONT = re.compile(r"\\(?:caption|emph|textbf|textit|texttt|textrm|textsf|paragraph|text)"
                   r"(?![A-Za-z])\*?")
_FLOAT = re.compile(r"\\(?:begin|end)\{(?:table|figure)\}(?:\[[^\]]*\])?")
_SYNTH_PROOF = re.compile(r"^\s*(Follows from|Assembled from|By)\b.{0,400}$", re.S)


_PAREN_REF = re.compile(r"\((?:[^()]|\([^()]*\))*?\\(?:claimref|ref|eqref|cref|Cref|autoref|cite[pt]?)"
                        r"(?:[^()]|\([^()]*\))*?\)")


def normalise(s, drop_cited=False):
    """The comparable residue of a passage. With drop_cited, a parenthesis that cites
    something is dropped whole, so that a citation added in a parenthesis (the grounding
    passes add them) does not count as a change of wording."""
    s = re.sub(r"(?<!\\)%[^\n]*", "", s or "")
    if drop_cited:
        s = _PAREN_REF.sub("", s)
    s = _REF.sub("", s)
    for _ in range(3):                         # what a removed reference leaves behind
        s = re.sub(r"\(\s*(?:[,;]|and|see|cf\.?)?\s*\)", "", s)
        s = re.sub(r"[,;]\s*(?:and\s*)?\)", ")", s)
        s = re.sub(r"\(\s*[,;]\s*", "(", s)
    s = _FLOAT.sub("", s)
    s = _LAYOUT.sub("", s)
    s = re.sub(r"\\verb\|([^|]*)\|", r"\1", s)
    s = s.replace("\\_", "_").replace("~", " ")
    s = _FONT.sub("", s)
    return re.sub(r"[{}\s]", "", s)


def _root(store_root):
    return os.path.join(os.path.dirname(os.path.abspath(store_root)), DEPOSITS)


def manifest(store_root):
    p = os.path.join(_root(store_root), "deposits.yaml")
    return (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}


class Baseline:
    """The deposited source of one paper."""

    def __init__(self, store_root, code, entry):
        from .extract import Paper, strip_comments
        self.code, self.entry = code, entry
        path = os.path.join(_root(store_root), entry["file"])
        src = open(path, encoding="utf-8").read()
        self.sha256 = hashlib.sha256(src.encode("utf-8")).hexdigest()
        body = strip_comments(src)
        body = body[body.find("\\begin{document}"):]
        self.body = normalise(body)
        self.body_uncited = normalise(body, drop_cited=True)
        try:
            self.envs = {e["label"]: e for e in Paper(code, path, "x", {}).envs if e["label"]}
        except Exception:                     # a source the extractor cannot parse: text only
            self.envs = {}

    def contains(self, text):
        """True when the passage stands in the deposit as written, "cited" when it does once
        parentheses that cite are set aside on both sides, else False."""
        n = normalise(text)
        if not n or n in self.body:
            return True
        n2 = normalise(text, drop_cited=True)
        return "cited" if (not n2 or n2 in self.body_uncited) else False


@lru_cache(maxsize=None)
def _baselines(store_root):
    out = {}
    for code, entry in manifest(store_root).items():
        if os.path.exists(os.path.join(_root(store_root), entry.get("file", ""))):
            out[code] = Baseline(store_root, code, entry)
    return out


@lru_cache(maxsize=None)
def _labels(store_root):
    p = os.path.join(store_root, "labels.yaml")
    return (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}


def deposited_entities(store, store_root, code):
    """entity id -> the deposited paper's number for it ("Prop 2.5"), for every result the
    deposited paper states: its labelled environments (a Fact the paper imports included)
    and its untitled passages (setting notes, located by line)."""
    out = {}
    for k, v in _labels(store_root).items():
        if isinstance(v, dict) and v.get("entity") and k.split(":", 1)[0] == code:
            out.setdefault(v["entity"], _number(store, v["entity"], code, v, k))
    for cid, e in store.entities.items():
        loc = e.meta.get("locators") or {}
        if str(loc.get("paper") or "") == code and (loc.get("line") or loc.get("label")):
            out.setdefault(cid, str(loc.get("number") or ""))
    return out


_PREFIX = {"fact": "Fact", "prop": "Prop", "thm": "Thm", "lem": "Lem", "cor": "Cor", "def": "Def",
           "rem": "Rem", "ex": "Example", "conj": "Conj", "prem": "Premise", "ax": "Axiom",
           "hyp": "Hyp", "prin": "Principle", "q": "Question", "obs": "Obs", "comp": "Comp",
           "asm": "Assembly"}


def _number(store, cid, code, lab, key=""):
    e = store.entities.get(cid)
    loc = (e.meta.get("locators") or {}) if e else {}
    if str(loc.get("paper") or "") == code and loc.get("number"):
        return str(loc["number"])
    pre = key.split(":", 2)[1] if key.count(":") >= 2 else ""
    kind = _PREFIX.get(pre) or str(lab.get("kind") or "").capitalize()
    return (kind + " " + str(lab.get("number") or "")).strip()


def entity_change(store, store_root, cid):
    """("statement"|"proof"|"statement and proof"|None, deposited text or None) for a result
    compared with the deposit of the paper that states it; (None, None) when there is no
    deposited source to compare (a result first made in the Lab, or an undeposited paper)."""
    e = store.entities.get(cid)
    if e is None:
        return None, None
    loc = e.meta.get("locators") or {}
    base = _baselines(store_root).get(str(loc.get("paper") or ""))
    if base is None or not (loc.get("line") or loc.get("label")) or cid.endswith("-external") \
            or e.kind == "prediction":
        return None, None
    env = base.envs.get(loc.get("label")) if loc.get("label") else None
    sc = base.contains(e.levels.get("formal") or "")
    st, cited = sc is False, sc == "cited"
    pr = False
    for text in e.proofs.values():
        if env is not None and not env["proofs"] and _SYNTH_PROOF.match(text.strip()):
            continue                          # the Lab's own one-line proof of an assembly
        pc = base.contains(text)
        pr = pr or pc is False
        cited = cited or pc == "cited"
    what = "statement and proof" if st and pr else ("statement" if st else ("proof" if pr else None))
    if what is None and cited:
        what = "citations"                    # only citations added, in parentheses
    dep = None
    if env is not None:
        code = base.code
        dep = {"statement": _resolve(store_root, code, env["statement"].strip()),
               "proof": _resolve(store_root, code, "\n\n".join(env["proofs"]).strip())}
    return what, dep


def _resolve(store_root, code, text):
    """A deposited passage made readable on its own: \\ref and \\eqref become the deposited
    numbers, a citation becomes its key and locator in brackets."""
    labels = _labels(store_root)

    def num(m):
        v = labels.get(f"{code}:{m.group(2)}") or {}
        n = str(v.get("number") or "?")
        return f"({n})" if m.group(1) == "eqref" else n

    text = re.sub(r"\\(ref|eqref|cref|Cref|autoref)\{([^}]*)\}", num, text)
    text = re.sub(r"\\cite[pt]?(?:\[([^\]]*)\])?\{([^}]*)\}",
                  lambda m: "[" + m.group(2) + (", " + m.group(1) if m.group(1) else "") + "]", text)
    return text


_QUIET_NOTE = re.compile(r"^(Own exact check|Check entries synced|Own check|Exact check)", re.I)


def change_notes(e):
    """The store's dated notes on a result, oldest first, without those that only record a
    check: what a reader comparing it with the deposit wants to know."""
    out = []
    for k, d in (e.meta.get("extraction") or {}).items():
        if isinstance(d, dict) and d.get("note") and d.get("date"):
            note = " ".join(str(d["note"]).split())
            if _QUIET_NOTE.match(note) or "tests" in k:
                continue
            note = re.sub(r"\s*Version \d+ -> \d+\.?", "", note).strip()
            out.append({"date": str(d["date"]), "note": note})
    return sorted(out, key=lambda x: x["date"])


# ---------------------------------------------------------------------------
# how much a revision matters: corrected, changed, or reworded
# ---------------------------------------------------------------------------
#
# A revised result is in one of three classes:
#   corrected  the deposited version was wrong or over-claimed, and the edit fixes it;
#   changed    the content changed, but not because the deposit was wrong (a scope or a
#              clause added by decision, a new proof route, a premise restated, a merge);
#   reworded   only wording, notation, terminology or citations (Q(v) for the square of a
#              vector, conformal spinor for twistor, the Gauge Theory Gravity wording, a
#              citation added).
# The class of each revision is a judgement, recorded once in deposits/classification.yaml
# with a one-line reason, for the entity version it was made on (a review pass, or a
# maintainer through `python -m tp.deposits set`). A later edit returns the result to the
# rules below until it is classified again. The rules never say "corrected": they say
# "reworded" only when every recorded edit is a wording pass (or a bump note that starts
# "Wording:") or, with nothing on record, when every difference from the deposit is a
# citation or a word or two with no mathematics; otherwise "changed". A bump note that
# starts "Correction:" or "Change:" names its class.

CLASSES = ("corrected", "changed", "reworded")
_EDGE_KEYS = {"cite_pass", "connect_pass", "typing", "maintainer_pass_tests", "check_lost",
              "check_restored", "maintainer_pass_refines", "cite", "typing_pass"}
_WORD_KEYS = {"notation_pass", "ga_conversion", "i4_conversion", "maintainer_pass_2",
              "maintainer_pass_gtg", "maintainer_pass_gtg_l0"}
_WORD_NOTE = re.compile(
    r"^(Wording:|Grounding pass|Squares of vectors|Renamed|Gauge Theory Gravity wording pass)"
    r"|no change of content|wording only", re.I)
_CORR_NOTE = re.compile(r"^Correction:", re.I)
_CHANGE_NOTE = re.compile(r"^Change:", re.I)


def _passes(e):
    """(key, note) for every recorded edit of a result since extraction."""
    out = []
    for k, d in (e.meta.get("extraction") or {}).items():
        if isinstance(d, dict) and (d.get("date") or d.get("note")) and k not in (
                "context_refs", "eqrefs", "env", "sources"):
            out.append((k, " ".join(str(d.get("note") or "").split())))
    return out


_CITE_TOKEN = "\x01"


def _tokens(s):
    s = re.sub(r"\\(?:claimref|ref|eqref|cref|Cref|autoref|cite[pt]?)\*?(?:\[[^\]]*\])?\{[^}]*\}",
               " " + _CITE_TOKEN + " ", s or "")
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = _LAYOUT.sub(" ", s).replace("~", " ")
    return s.split()


def _small_or_cited(dep_text, cur_text):
    """True when every difference between the deposited and current text is a citation
    (with at most a few connecting words) or a change of one or two words with no
    mathematics: the text-only evidence for "reworded"."""
    import difflib
    a, b = _tokens(dep_text), _tokens(cur_text)
    for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if op == "equal":
            continue
        old, new = a[i1:i2], b[j1:j2]
        if any("$" in t or "\\" in t for t in old + new if t != _CITE_TOKEN):
            if not (_CITE_TOKEN in new and len([t for t in new if t != _CITE_TOKEN]) <= 6
                    and not any("$" in t for t in old)):
                return False
        cited = _CITE_TOKEN in new
        words = [t for t in new if t != _CITE_TOKEN]
        if cited and len(old) <= 2 and len(words) <= 25:
            continue
        if not cited and len(old) <= 2 and len(new) <= 2:
            continue
        return False
    return True


@lru_cache(maxsize=None)
def _overrides(store_root):
    p = os.path.join(_root(store_root), "classification.yaml")
    return (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}


def classify(store_root, e, deposited):
    """(class, reason, reviewed) for a revised result; see the comment above."""
    ov = _overrides(store_root).get(e.id)
    if isinstance(ov, dict) and ov.get("class") in CLASSES and int(ov.get("version") or 0) == e.version:
        return ov["class"], ov.get("reason") or "", True
    corr, chg, word = [], [], []
    for k, n in _passes(e):
        if k in _EDGE_KEYS or k.endswith("_tests"):
            continue
        if _CORR_NOTE.match(n):
            corr.append(n)
        elif _CHANGE_NOTE.match(n):
            chg.append(n)
        elif k in _WORD_KEYS or _WORD_NOTE.search(n):
            word.append(n or k)
        else:
            chg.append(n or k)
    if corr:
        return "corrected", corr[-1], False
    if chg:
        return "changed", "not yet classified by review", False
    if word:
        return "reworded", "wording, notation or terminology pass", False
    if deposited is not None:
        cur = (e.levels.get("formal") or "") + "\n" + "\n".join(e.proofs.values())
        dep = deposited["statement"] + "\n" + deposited["proof"]
        if _small_or_cited(dep, cur):
            return "reworded", "citations or a word or two added", False
    return "changed", "not yet classified by review", False


def compare(store, store_root, code, blocks):
    """The changes of one document since the deposit of paper `code` (see the module doc).
    Returns None when the paper has no deposit on record."""
    entry = manifest(store_root).get(code)
    if entry is None:
        return None
    dep = deposited_entities(store, store_root, code)
    shown = {}
    for b in blocks:
        if b.get("claim"):
            shown.setdefault(b["claim"].split("@")[0], b)
    per = {}
    for cid, b in shown.items():
        e = store.entities.get(cid)
        if e is None:
            continue
        if cid not in dep:
            kind = "added"
            what, depo = None, None
        else:
            what, depo = entity_change(store, store_root, cid)
            if what is None:
                continue
            kind = "cited" if what == "citations" else "revised"
        cls, why, rev_ok = classify(store_root, e, depo) if kind == "revised" else (None, None, None)
        per[b["id"]] = {"claim": cid, "kind": kind, "what": what, "number": b.get("number"),
                        "class": cls, "why": why, "reviewed": rev_ok,
                        "type": b.get("type"), "title": b.get("title") or e.title,
                        "deposited_number": dep.get(cid),
                        # brought in from elsewhere (a cited result, a premise of another
                        # paper, a refutation or prediction of the series) rather than new here
                        "cited": b.get("type") in ("fact", "postulate", "refutation", "prediction")
                        or str((e.meta.get("locators") or {}).get("paper") or code).split("-")[0] != code,
                        "deposited": depo, "notes": change_notes(e)}
    tomb = {}
    tp = os.path.join(store_root, "tombstones.yaml")
    if os.path.exists(tp):
        for t in yaml.safe_load(open(tp, encoding="utf-8")) or []:
            if isinstance(t, dict) and t.get("id"):
                tomb[t["id"]] = t
    removed = []
    for cid, num in sorted(dep.items(), key=lambda kv: kv[1]):
        if cid in shown:
            continue
        e = store.entities.get(cid)
        if e is not None and e.kind == "note" and e.status == "setting":
            continue                          # the deposited paper's prose; not a result
        if e is not None and e.status != "refuted":
            continue                          # still in the store, left out by the recipe
        why = ("refuted" if e is not None else
               ("merged into " + str(tomb[cid].get("merged_into") or tomb[cid].get("into"))
                if cid in tomb and (tomb[cid].get("merged_into") or tomb[cid].get("into"))
                else "withdrawn from the store"))
        removed.append({"claim": cid, "deposited_number": num,
                        "title": e.title if e is not None else cid, "why": why})
    rev = [x for x in per.values() if x["kind"] == "revised"]
    summary = {
        "statements": sum(1 for x in rev if "statement" in x["what"]),
        "proofs_only": sum(1 for x in rev if x["what"] == "proof"),
        "revised": len(rev),
        "corrected": sum(1 for x in rev if x["class"] == "corrected"),
        "changed": sum(1 for x in rev if x["class"] == "changed"),
        "reworded": sum(1 for x in rev if x["class"] == "reworded"),
        "added": sum(1 for x in per.values() if x["kind"] == "added" and not x["cited"]),
        "added_cited": sum(1 for x in per.values() if x["kind"] == "added" and x["cited"]),
        "removed": len(removed),
        "citations": sum(1 for x in per.values() if x["kind"] == "cited"),
        "compared": sum(1 for c in shown if c in dep),
    }
    return {"code": code, "doi": entry.get("doi"), "version": str(entry.get("version") or ""),
            "file": entry.get("file"), "blocks": per, "removed": removed, "summary": summary}


def summary_sentence(ch):
    """One sentence for a notice: how the generated paper differs from the deposit."""
    if ch is None:
        return ""
    s = ch["summary"]
    parts = []
    pl = lambda n, w: f"{n} {w}{'s' if n != 1 else ''}"
    if s.get("corrected"):
        parts.append(pl(s["corrected"], "result") + " corrected")
    if s.get("changed"):
        parts.append((pl(s["changed"], "result") if not parts else str(s["changed"])) + " changed")
    if s.get("reworded"):
        parts.append((pl(s["reworded"], "result") if not parts else str(s["reworded"]))
                     + " reworded (wording, notation or citations only)")
    if s["added"]:
        parts.append(f"{s['added']} result{'s' if s['added'] != 1 else ''} added")
    if s["added_cited"]:
        parts.append(f"{s['added_cited']} cited result{'s' if s['added_cited'] != 1 else ''} added")
    if s["removed"]:
        parts.append(f"{s['removed']} deposited result{'s' if s['removed'] != 1 else ''} withdrawn")
    if not parts:
        return (f"No result differs from the deposited version {ch['version']}.")
    tail = ", ".join(parts[:-1]) + (" and " if len(parts) > 1 else "") + parts[-1]
    return f"Since the deposited version {ch['version']}: {tail}."


# ---------------------------------------------------------------------------
# command line
# ---------------------------------------------------------------------------

def _doc_compare(store_root, doc):
    import json
    from .model import load_store
    folder = os.path.join(os.path.dirname(os.path.abspath(store_root)), "documents", doc)
    rec = yaml.safe_load(open(os.path.join(folder, "recipe.yaml"), encoding="utf-8"))
    blocks = json.load(open(os.path.join(folder, "blocks.json"), encoding="utf-8"))
    store = load_store(store_root)
    return compare(store, store_root, str(rec.get("paper") or ""), blocks)


def main(argv=None):
    ap = argparse.ArgumentParser(prog="tp.deposits")
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("report")
    r.add_argument("doc")
    r.add_argument("--store", default="store")
    s = sub.add_parser("summary")
    s.add_argument("--store", default="store")
    o = sub.add_parser("set", help="set the class of one revised result by hand")
    o.add_argument("entity")
    o.add_argument("--class", dest="cls", required=True, choices=CLASSES)
    o.add_argument("--by", required=True)
    o.add_argument("--reason", default="")
    o.add_argument("--store", default="store")
    n = sub.add_parser("record")
    n.add_argument("code")
    n.add_argument("--tex", required=True)
    n.add_argument("--doi", required=True)
    n.add_argument("--version", required=True)
    n.add_argument("--note", default="")
    n.add_argument("--store", default="store")
    a = ap.parse_args(argv)
    if a.cmd == "set":
        from .model import load_store
        e = load_store(a.store).entities.get(a.entity)
        if e is None:
            print(f"no entity {a.entity}")
            return 1
        p = os.path.join(_root(a.store), "classification.yaml")
        cur = (yaml.safe_load(open(p, encoding="utf-8")) or {}) if os.path.exists(p) else {}
        cur[a.entity] = {"class": a.cls, "version": e.version, "by": a.by,
                         "date": dt.date.today().isoformat(), "reason": a.reason}
        with open(p, "w", encoding="utf-8") as fh:
            fh.write("# Classes set by hand for results revised since their deposit (tp.deposits set).\n"
                     "# Each holds for the entity version named; a later edit returns it to the rules.\n"
                     + yaml.safe_dump(cur, sort_keys=True, allow_unicode=True))
        print(f"{a.entity} version {e.version}: {a.cls}")
        return 0
    if a.cmd == "record":
        root = _root(a.store)
        os.makedirs(root, exist_ok=True)
        name = os.path.basename(a.tex)
        shutil.copy(a.tex, os.path.join(root, name))
        man = manifest(a.store)
        sha = hashlib.sha256(open(os.path.join(root, name), "rb").read()).hexdigest()
        man[a.code] = {"doi": a.doi, "version": a.version, "file": name, "sha256": sha,
                       "recorded": dt.date.today().isoformat(), "note": a.note}
        with open(os.path.join(root, "deposits.yaml"), "w", encoding="utf-8") as fh:
            fh.write(_HEADER + yaml.safe_dump(man, sort_keys=True, allow_unicode=True))
        print(f"recorded {a.code} version {a.version} ({a.doi}); documents of {a.code} now "
              f"compare against it: regenerate them (tp regen) and rebuild the PDFs")
        return 0
    if a.cmd == "report":
        ch = _doc_compare(a.store, a.doc)
        if ch is None:
            print(f"{a.doc}: its paper has no deposit on record")
            return 0
        print(f"{a.doc} against {ch['code']} version {ch['version']} ({ch['doi']})")
        print(summary_sentence(ch))
        for b in ch["blocks"].values():
            tag = ((b["class"] + ": " + b["what"]) if b["kind"] == "revised" else b["what"] if b["kind"] == "cited"
                   else ("cited, added" if b["cited"] else "added"))
            print(f"  {b['number'] or '-':>6}  {tag:22s} {b['title'][:70]}")
        for x in ch["removed"]:
            print(f"  {'':>6}  withdrawn ({x['why']}) {x['deposited_number']} {x['title'][:60]}")
        return 0
    docs = os.path.join(os.path.dirname(os.path.abspath(a.store)), "documents")
    for d in sorted(os.listdir(docs)):
        rp = os.path.join(docs, d, "recipe.yaml")
        if not os.path.exists(rp) or d.startswith("trail") or d == "tour":
            continue
        ch = _doc_compare(a.store, d)
        if ch is not None:
            s = ch["summary"]
            print(f"{d:28s} compared {s['compared']:4d}  corrected {s['corrected']:3d}  changed {s['changed']:3d}  "
                  f"reworded {s['reworded']:3d}  citations {s['citations']:3d}  added {s['added']:3d} (+{s['added_cited']} cited)  withdrawn {s['removed']}")
    return 0


_HEADER = ("# The deposited versions of the Transport Papers: the baseline against which the Lab\n"
           "# marks what has changed in a generated paper. One entry per paper; the .tex beside\n"
           "# this file is the source of the version on Zenodo. When a new version is deposited,\n"
           "# replace it with: python -m tp.deposits record <code> --tex FILE --doi DOI --version V\n")


if __name__ == "__main__":
    sys.exit(main())
