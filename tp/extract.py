"""Seed the store from the series' LaTeX sources (Phase 1 extraction).

For each paper: theorem-like environments become entities, \\ref and
cross-paper \\cite[locator]{ButlerTn} become draft edges, Fact (imported)
blocks become imported claims (or aliases of the series claim they restate),
verify-script check labels become legacy evidence, and the preamble's macros
become the notation registry.  Everything extracted is marked review: draft;
the typing pass decides which draft edges are real premises.

Usage:  python -m tp.extract SUITE_DIR LABELS_DIR STORE_DIR
"""
from __future__ import annotations

from .credit import for_paper as credit_for_paper
import json
import os
import re
import shutil
import sys
from collections import Counter, defaultdict

import yaml

from .evidence import label_keys
from .model import dump_entity

PAPERS = [
    # code, tex file, region, verify script
    ("T01", "T01_transport_principle.tex", "transport", "verify_T01.py"),
    ("T02", "T02_projective_to_conformal.tex", "conformal", "verify_T02.py"),
    ("T03", "T03_tower_car.tex", "tower", "verify_T03.py"),
    ("T04", "T04_clifford_sheaves.tex", "sheaf", "verify_T04.py"),
    ("T05", "T05_gravitational_singularity.tex", "singularity", "verify_T05.py"),
    ("T06", "T06_blackhole_interior.tex", "interior", "verify_T06.py"),
    ("T07", "T07_hawking_radiation.tex", "hawking", "verify_T07.py"),
    # added after the pilot: the rest of the series and its companion notes
    ("T00", "T00_ga_primer.tex", "primer", "verify_T00.py"),
    # T0a, the primer's companion note (T0's former Section 14), deposited on 2026-11-20; its
    # results were stored by the runs of 7 to 17 November, under synthesis ids, before it was a paper
    ("T00a", "T00a_geometry_first.tex", "geometry-first", "verify_T00a.py"),
    ("T05-pairing", "T05_pairing_generator_note.tex", "pairing", "verify_T05_pairing.py"),
    ("T05-angle", "T05_angle_note.tex", "angle", "verify_T05_angle.py"),
    ("T05-descent-lift", "T05_descent_lift_note.tex", "descent-lift", "verify_T05_dilation.py"),
    ("T05-state-selection", "T05_state_selection_note.tex", "state-selection", "verify_state_selection.py"),
    ("T05-three-routes", "T05_three_routes_note.tex", "three-routes", "verify_three_routes.py"),
    ("T08", "T08_entropy_scrambling.tex", "scrambling", "verify_T08.py"),
    ("T09", "T09_twistor_correspondence.tex", "correspondence", "verify_T09.py"),
    ("T10", "T10_dark_energy.tex", "dark-energy", "verify_T10.py"),
    ("T11", "T11_origin_of_mass.tex", "mass", "verify_T11.py"),
    ("T12", "T12_standard_model.tex", "standard-model", "verify_T12.py"),
    ("T12-lepton", "T12_lepton_note.tex", "lepton", "verify_T12_lepton.py"),
    ("T12-rungs", "T12_rungs_note.tex", "rungs", "verify_T12_rungs.py"),
    ("T13", "T13_quark_lepton_families.tex", "families", "verify_T13.py"),
    ("T14", "T14_dark_matter.tex", "dark-matter", "verify_T14.py"),
    ("T14a", "T14a_odd_extensions.tex", "odd-extensions", "verify_T14a.py"),
    ("T14b", "T14b_simulations.tex", "simulations", "verify_T14b.py"),
    ("T15", "T15_neutrino_masses.tex", "neutrino", "verify_T15.py"),
    ("T16", "T16_qm_gr_one_relation.tex", "one-relation", "verify_T16.py"),
    ("T17", "T17_transport_programme.tex", "programme", "verify_T17.py"),
    ("T17-rule2", "T17_rule2_note.tex", "rule2", "verify_T17_rule2.py"),
    # working notes added after the build (21 October 2026); they live beside their runs
    # T14c, deposited on 2026-11-20, moved to the suite root with T14c_supplement/ that day
    ("T14c", "T14c_dark_tower_matter.tex", "dark-tower-matter", "verify_T14c.py"),
    ("FT", "Claude outputs/ga_field_theory_note_2026-10-16/FT_one_complex_unit.tex",
     "field-theory", "Claude outputs/ga_field_theory_note_2026-10-16/verify_FT.py"),
]
# Sections that are cited as results: (paper, section number) -> label of a
# synthetic entity built from the section's text.
SECTION_TARGETS = {("T01", "8.1"): "sec:algorithm", ("T01", "8"): "sec:algorithm"}
SYNTHETIC = {"T01": [("sec:algorithm", "The transport algorithm",
                      "\\subsection{The transport algorithm}\\label{sec:algorithm}",
                      "\\begin{table")]}

ENV_KIND = {
    "theorem": ("claim", "proved", "Thm"), "proposition": ("claim", "proved", "Prop"),
    "lemma": ("claim", "proved", "Lem"), "corollary": ("claim", "proved", "Cor"),
    "principle": ("claim", "proved", "Principle"),
    "conjecture": ("claim", "conjectured", "Conj"),
    "definition": ("object", "defined", "Def"),
    "fact": ("claim", "imported", "Fact"),
    "axiom": ("claim", "postulate", "Axiom"), "premise": ("claim", "postulate", "Premise"),
    "hypothesis": ("claim", "postulate", "Hyp"),
    "question": ("question", "open", "Question"),
    "assembly": ("claim", "proved", "Asm"),
    "computation": ("claim", "proved", "Comp"),
    "observation": ("claim", "conjectured", "Obs"),
    "record": ("prediction", "live", "Rec"),
    "algorithm": ("claim", "proved", "Sec"),
}
ENV_RE = re.compile(r"\\begin\{(" + "|".join(k for k in ENV_KIND if k != "algorithm") + r")\}")
NO_PROOF_ENVS = {"definition", "axiom", "premise", "hypothesis", "question", "record"}
PROOF_RE = re.compile(r"\\begin\{proof\}")
REF_RE = re.compile(r"\\(?:ref|cref|Cref|autoref)\{([^}]+)\}")
EQREF_RE = re.compile(r"\\eqref\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite[pt]?(?:\[([^\]]*)\])?\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
NEWLABEL_RE = re.compile(r"\\newlabel\{([^}]+)\}\{\{([^}]*)\}\{[^}]*\}\{(.*?)\}\{([^}]*)\}")
SERIES_RE = re.compile(r"^ButlerT(\d+)([a-z]?)$")
TYPE_WORD = re.compile(r"(Thms?|Theorems?|Props?|Propositions?|Lems?|Lemmas?|Cors?|"
                       r"Corollar(?:y|ies)|Defs?|Definitions?|Facts?|Prems?|Premises?|"
                       r"Conjs?|Conjectures?|Ax(?:ioms?)?|Principles?|Hyps?|Hypothes[ie]s)\b")
NUM_RE = re.compile(r"(?<![\w.])([A-Z]?\d+\.\d+)(?![\d])")
THEOREM_COUNTERS = ("assembly", "computation", "observation", "record", "theorem", "proposition", "lemma", "corollary", "definition",
                    "fact", "conjecture", "axiom", "premise", "principle",
                    "hypothesis", "question", "remark", "example")


def strip_comments(s: str) -> str:
    return re.sub(r"(?<!\\)%.*", "", s)


def balanced(s: str, i: int, open_c: str, close_c: str):
    """s[i] == open_c; return index just past the matching close_c."""
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == open_c:
            depth += 1
        elif c == close_c:
            depth -= 1
            if depth == 0:
                return j + 1
        j += 1
    return len(s)


def slug(text: str, maxwords=6) -> str:
    t = re.sub(r"\\cite[pt]?(\[[^\]]*\])?\{[^}]*\}", " ", text)
    t = re.sub(r"\b(Theorem|Lemma|Proposition|Corollary|Definition|Fact|Section|Thm|Lem|Prop|Cor)"
               r"\.?~?\s*[A-Z]?\d+(\.\d+)*", " ", t)
    t = re.sub(r"\$[^$]*\$", " ", t)
    t = re.sub(r"\\[a-zA-Z]+\*?(\{[^}]*\})?", " ", t)
    t = t.replace("'", "")
    words = re.findall(r"[A-Za-z0-9]+", t.lower())
    stop = {"the", "a", "an", "of", "and", "in", "on", "for", "to", "is", "its", "at",
            "as", "by", "with", "from", "that", "this"}
    words = [w for w in words if w not in stop] or words
    return "-".join(words[:maxwords]) or "untitled"


def read_labels(path: str):
    """aux \\newlabel lines -> {label: (number, title, counter)}."""
    out = {}
    if not os.path.exists(path):
        return out
    for line in open(path, encoding="utf-8", errors="replace"):
        m = NEWLABEL_RE.match(line.strip())
        if m:
            lab, num, title, anchor = m.groups()
            counter = anchor.split(".")[0] if anchor else ""
            out[lab] = (num, title, counter)
    return out


def parse_macros(preamble: str):
    out = {}
    for m in re.finditer(r"\\(?:re)?newcommand\*?\{?\\([A-Za-z]+)\}?(\[\d\])?\{", preamble):
        end = balanced(preamble, m.end() - 1, "{", "}")
        out[m.group(1)] = preamble[m.end():end - 1]
    for m in re.finditer(r"\\DeclareMathOperator\*?\{\\([A-Za-z]+)\}\{", preamble):
        end = balanced(preamble, m.end() - 1, "{", "}")
        out[m.group(1)] = r"\operatorname{" + preamble[m.end():end - 1] + "}"
    for m in re.finditer(r"\\def\\([A-Za-z]+)\{", preamble):
        end = balanced(preamble, m.end() - 1, "{", "}")
        out[m.group(1)] = preamble[m.end():end - 1]
    return out


def parse_bib(body: str):
    out = {}
    m = re.search(r"\\begin\{thebibliography\}.*?\n(.*?)\\end\{thebibliography\}", body, re.S)
    if not m:
        return out
    items = re.split(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", m.group(1))
    for k, txt in zip(items[1::2], items[2::2]):
        clean = re.sub(r"\\emph\{([^}]*)\}", r"\1", txt)
        clean = re.sub(r"\\[a-zA-Z]+\{([^}]*)\}", r"\1", clean)
        clean = clean.replace("~", " ").replace("\\&", "&")
        clean = re.sub(r"[{}\\]", "", clean)
        clean = re.sub(r"\s+", " ", clean).strip()
        doi = re.search(r"10\.\d{4,9}/[^\s,}]+", txt)
        out[k] = {"citation": clean, "doi": doi.group(0).rstrip(".") if doi else None,
                  "latex": txt.strip()}
    return out


def locator_numbers(loc: str):
    """'Thms.~7.3 and 7.6, Prop.~7.18, Eq. (3.1)' -> ['7.3', '7.6', '7.18']."""
    nums, current = [], None
    for item in re.split(r"[,;]", loc or ""):
        tw = TYPE_WORD.search(item)
        if tw:
            current = tw.group(1)
        elif re.search(r"\b(Eqs?|Sec|Secs|App|Fig|Table|eq)\b|\\S|§", item):
            current = None
        if current:
            nums += NUM_RE.findall(item)
    return nums


class Paper:
    def __init__(self, code, tex_path, region, labels):
        self.code, self.region, self.labels = code, region, labels
        raw = open(tex_path, encoding="utf-8").read()
        self.source = strip_comments(raw)
        i = self.source.find("\\begin{document}")
        self.preamble, self.body = self.source[:i], self.source[i:]
        self.macros = parse_macros(self.preamble)
        self.bib = parse_bib(self.body)
        self.by_number = {}
        for lab, (num, title, counter) in labels.items():
            if counter in THEOREM_COUNTERS:
                self.by_number.setdefault(num, lab)
        self.envs = self._envs()

    def _envs(self):
        envs = []
        for m in ENV_RE.finditer(self.body):
            env = m.group(1)
            j = m.end()
            title = None
            k = j
            while k < len(self.body) and self.body[k] in " \t":
                k += 1
            if k < len(self.body) and self.body[k] == "[":
                e = balanced(self.body, k, "[", "]")
                title = self.body[k + 1:e - 1]
                j = e
            end = self.body.find("\\end{" + env + "}", j)
            stmt = self.body[j:end]
            lab = LABEL_RE.search(stmt)
            envs.append({"env": env, "title": title, "start": m.start(),
                         "end": end + len("\\end{" + env + "}"),
                         "label": lab.group(1) if lab else None,
                         "statement": LABEL_RE.sub("", stmt).strip(),
                         "line": self.body[:m.start()].count("\n")
                         + self.preamble.count("\n") + 1,
                         "proofs": []})
        # proofs: explicit "Proof of X \ref{lbl}" wins; else the nearest
        # preceding environment with no other theorem-like env in between
        for m in PROOF_RE.finditer(self.body):
            j = m.end()
            arg = None
            if self.body[j:j + 1] == "[":
                e = balanced(self.body, j, "[", "]")
                arg = self.body[j + 1:e - 1]
                j = e
            end = self.body.find("\\end{proof}", j)
            text = self.body[j:end].strip()
            target = None
            if arg:
                r = REF_RE.search(arg)
                if r:
                    target = next((x for x in envs if x["label"] == r.group(1)), None)
            if target is None:
                # premises, definitions and questions carry no proof: a proof
                # after one of them belongs to the last provable result before it
                prev = [x for x in envs if x["end"] <= m.start()
                        and x["env"] not in NO_PROOF_ENVS]
                if prev:
                    target = prev[-1]
            if target is not None:
                target["proofs"].append(text)
        for lab, title, start, end in SYNTHETIC.get(self.code, []):
            i = self.body.find(start)
            if i < 0:
                continue
            j = self.body.find(end, i)
            stmt = self.body[i + len(start):j].strip()
            envs.append({"env": "algorithm", "title": title, "start": i, "end": j,
                         "label": lab, "statement": stmt,
                         "line": self.body[:i].count("\n") + self.preamble.count("\n") + 1,
                         "proofs": ["Each step names the result that licenses it; the "
                                    "derivation is those results.\n\n" + stmt]})
        return envs

    def number_of(self, label):
        return self.labels.get(label, ("?",))[0]


ABBREV = re.compile(r"(?:Props?|Thms?|Lems?|Cors?|Defs?|Secs?|Eqs?|App|Figs?|cf|e\.g|i\.e|Prems?|Rem|Conj|Ax|Hyp|resp|vs|al)\.$")


def trailing_window(text, end):
    """The locator text that follows a citation: up to the next \\cite, a
    newline, or a sentence end that is not an abbreviation; at most 160 chars."""
    w = text[end:end + 160]
    stop = len(w)
    m = re.search(r"\\cite|\n", w)
    if m:
        stop = m.start()
    for m in re.finditer(r"\.\s+(?=[A-Z\\])", w[:stop]):
        if not ABBREV.search(w[:m.start() + 1]):
            stop = m.start()
            break
    return w[:stop]


def series_cites(papers, text):
    """All series citations in text, with locators inside the brackets and in
    the text that follows: -> (resolved [(code, label)], unlocated [key])."""
    found, unlocated = [], []
    for m in CITE_RE.finditer(text):
        loc = (m.group(1) or "") + " , " + trailing_window(text, m.end())
        for key in [k.strip() for k in m.group(2).split(",")]:
            r = resolve_series_cite(papers, key, loc)
            if isinstance(r, list):
                if r:
                    found += r
                else:
                    unlocated.append(key)
            elif isinstance(r, tuple):
                unlocated.append(key)
    return found, unlocated


def resolve_series_cite(papers, key, loc):
    """\\cite[loc]{ButlerTn} -> list of (paper code, label)."""
    m = SERIES_RE.match(key)
    if not m:
        return None
    code = f"T{int(m.group(1)):02d}{m.group(2)}"
    if code not in papers:
        return ("outside", code)
    p = papers[code]
    out = []
    for n in locator_numbers(loc):
        lab = p.by_number.get(n)
        if lab:
            out.append((code, lab))
    for sec in re.findall(r"(?:\\S|§|Section)\s*~?(\d+(?:\.\d+)?)", loc or ""):
        lab = SECTION_TARGETS.get((code, sec))
        if lab and (code, lab) not in out:
            out.append((code, lab))
    return out


LAYOUT_MACROS = {"section", "subsection", "topfraction", "bottomfraction",
                 "textfraction", "floatpagefraction", "cone", "file"}


def extract(suite: str, labels_dir: str, store: str, session="pilot-2026-10-20",
            force=False):
    papers = {}
    for code, tex, region, _ in PAPERS:
        base = os.path.splitext(os.path.basename(tex))[0]
        labels = read_labels(os.path.join(labels_dir, base + ".labels.txt"))
        papers[code] = Paper(code, os.path.join(suite, tex), region, labels)

    # ---- assign ids ---------------------------------------------------------
    ent_of = {}            # (code, label or synthetic) -> record
    used_ids = set()
    records = []
    for code, p in papers.items():
        for k, env in enumerate(p.envs):
            kind, status, short = ENV_KIND[env["env"]]
            base = slug(env["title"]) if env["title"] else \
                (slug(env["label"].split(":", 1)[-1]) if env["label"] else f"{short.lower()}-{k}")
            prefix = "obj." + p.region if kind == "object" else \
                ("q." + p.region if kind == "question" else p.region)
            eid = f"{prefix}.{base}"
            n = 2
            while eid in used_ids:
                eid = f"{prefix}.{base}-{n}"
                n += 1
            used_ids.add(eid)
            num = p.number_of(env["label"]) if env["label"] else "?"
            rec = {"code": code, "paper": p, "env": env, "kind": kind, "status": status,
                   "id": eid, "locator": f"{short} {num}", "alias_of": None}
            records.append(rec)
            ent_of[(code, env["label"] or f"#{k}")] = rec

    def lookup(code, label):
        return ent_of.get((code, label))

    # ---- facts: alias, assembled, or imported ---------------------------------
    stats = Counter()
    extra = []
    for rec in records:
        if rec["env"]["env"] != "fact":
            continue
        p = rec["paper"]
        text = rec["env"]["statement"]
        series_targets, external, outside = [], [], []
        for m in CITE_RE.finditer(text):
            loc, keys = m.group(1) or "", [k.strip() for k in m.group(2).split(",")]
            loc_ext = loc + " , " + trailing_window(text, m.end())
            for key in keys:
                r = resolve_series_cite(papers, key, loc_ext)
                if r is None:
                    external.append((key, loc))
                elif isinstance(r, tuple):
                    outside.append((key, loc, r[1]))
                else:
                    series_targets += [lookup(c, l) for c, l in r if lookup(c, l)]
        series_targets = [t for t in dict.fromkeys(id(t) for t in series_targets)]
        targets = [r for r in records if id(r) in series_targets]
        rec["fact_external"], rec["fact_outside"], rec["fact_series"] = external, outside, targets
        if not external and not outside and len(targets) == 1 \
                and targets[0]["kind"] != "object":
            rec["alias_of"] = targets[0]
            stats["fact-alias"] += 1
        elif not external and not outside and targets:
            rec["status"] = "proved"
            rec["assembled"] = True
            stats["fact-assembled-from-series"] += 1
        elif targets:
            # mixed: series results plus outside literature.  The series part
            # is a real logical dependency, so the fact becomes a proved claim
            # assembled from the series results and one companion imported
            # claim that carries the external citations.
            rec["status"] = "proved"
            rec["assembled"] = True
            cid = rec["id"] + "-external"
            comp = {"code": rec["code"], "paper": p,
                    "env": dict(rec["env"], label=None, proofs=[],
                                title=(rec["env"]["title"] or "") + " (external ingredients)"),
                    "kind": "claim", "status": "imported", "id": cid,
                    "locator": rec["locator"], "alias_of": None,
                    "fact_external": external, "fact_outside": outside, "fact_series": [],
                    "companion_of": rec["id"]}
            used_ids.add(cid)
            rec["companion"] = comp
            extra.append(comp)
            stats["fact-mixed-split"] += 1
        else:
            stats["fact-imported"] += 1
    records += extra

    def final(rec):
        seen = set()
        while rec["alias_of"] is not None and id(rec) not in seen:
            seen.add(id(rec))
            rec = rec["alias_of"]
        return rec

    # ---- edges -------------------------------------------------------------
    def refs_in(code, text):
        """-> list of target records, unresolved labels, eqref count, outside cites."""
        targets, unresolved, outside = [], [], []
        for m in REF_RE.finditer(text):
            for lab in m.group(1).split(","):
                lab = lab.strip()
                r = lookup(code, lab)
                if r:
                    targets.append(final(r))
                elif not re.match(r"(sec|subsec|ssec|app|fig|tab|eq|item|part|step|ch)[:.]",
                                  lab):
                    unresolved.append(lab)
        found, unlocated = series_cites(papers, text)
        targets += [final(lookup(c, l)) for c, l in found if lookup(c, l)]
        outside += unlocated
        return targets, unresolved, len(EQREF_RE.findall(text)), outside

    def rewrite(code, text):
        def sub(m):
            labs = [l.strip() for l in m.group(1).split(",")]
            outs = []
            for lab in labs:
                r = lookup(code, lab)
                outs.append("\\claimref{" + final(r)["id"] + "}" if r else m.group(0))
            return ", ".join(outs)
        return REF_RE.sub(sub, text)

    # ---- verify scripts -> legacy evidence ------------------------------------
    legacy = {}
    unattributed = Counter()
    for code, tex, region, script in PAPERS:
        path = os.path.join(suite, script)
        if not os.path.exists(path):
            continue
        src = open(path, encoding="utf-8").read()
        p = papers[code]
        labels_found = re.findall(r"check\(\s*f?(\"(?:[^\"\\]|\\.)*\"|'(?:[^'\\]|\\.)*')", src)
        for raw in labels_found:
            lab = raw[1:-1]
            keys = label_keys(lab)
            hit = False
            for key in keys:
                kind, val = key.split(":", 1)
                label = p.by_number.get(val) if kind == "num" else val
                r = lookup(code, label) if label else None
                if r:
                    r = final(r)
                    legacy.setdefault(r["id"], (script, set()))[1].add(key)
                    hit = True
            if not hit:
                unattributed[code] += 1

    # ---- write ---------------------------------------------------------------
    if os.path.exists(store):
        if not force:
            raise SystemExit(f"{store} exists: extraction seeds an empty store only. "
                             "The store is now the source of truth; pass --force to "
                             "discard it and re-seed.")
        shutil.rmtree(store)
    dirs = {"claim": "claims", "object": "objects", "question": "questions",
            "prediction": "predictions"}
    notation, conflicts = {}, defaultdict(set)
    for code, p in papers.items():
        for mac, d in p.macros.items():
            if mac in LAYOUT_MACROS or "\\begin{scope}" in d or "\\old" in d:
                continue   # page layout and drawing helpers are not notation
            if mac in notation and notation[mac] != d:
                conflicts[mac].update({notation[mac], d})
            notation.setdefault(mac, d)
    flags_all = Counter()
    for rec in records:
        if rec["alias_of"] is not None:
            continue
        p, env, code = rec["paper"], rec["env"], rec["code"]
        s_targets, s_unres, s_eq, s_out = refs_in(code, env["statement"])
        proof = "\n\n".join(env["proofs"])
        p_targets, p_unres, p_eq, p_out = refs_in(code, proof)
        me = rec["id"]
        about = sorted({t["id"] for t in s_targets + p_targets
                        if t["kind"] == "object" and t["id"] != me})
        assumes = sorted({t["id"] for t in s_targets + p_targets
                          if t["status"] == "postulate" and t["id"] != me})
        uses = sorted({t["id"] for t in p_targets
                       if t["kind"] == "claim" and t["status"] != "postulate"
                       and t["id"] != me})
        context = sorted({t["id"] for t in s_targets
                          if t["kind"] == "claim" and t["status"] != "postulate"
                          and t["id"] != me} - set(uses))
        flags = []
        meta = {"id": me, "kind": rec["kind"], "version": 1,
                "title": _title(env, rec), "status": rec["status"],
                "region": p.region,
                "proposed_by": {"kind": "extraction", "session": session},
                # the series' authorship disclosure: drafted with Claude (tp/credit.py)
                "ai_involved": "yes", "credit": credit_for_paper(code), "review": "draft"}
        if about:
            meta["about"] = about
        if rec["kind"] == "claim" and rec["status"] in ("proved",):
            if rec.get("assembled"):
                fs = [final(t) for t in rec["fact_series"]]
                uses = sorted(set(uses) | {t["id"] for t in fs if t["kind"] == "claim"
                                           and t["status"] != "postulate"})
                assumes = sorted(set(assumes) | {t["id"] for t in fs
                                                 if t["status"] == "postulate"})
                if rec.get("companion"):
                    uses = sorted(set(uses) | {rec["companion"]["id"]})
                obj = {t["id"] for t in fs if t["kind"] == "object"}
                if obj:
                    meta["about"] = sorted(set(meta.get("about", [])) | obj)
                proof = proof or env["statement"]
                flags.append("fact restating several series results: derived from them")
            if env["env"] == "principle":
                uses = sorted(set(uses) | set(context))
                context = []
                proof = proof or env["statement"]
                flags.append("summary principle: derivation is its cited theorems")
            if not proof:
                flags.append("no proof environment found")
            d = {"name": "main"}
            if uses:
                d["uses"] = [u + "@1" for u in uses]
            if assumes:
                d["assumes"] = [a + "@1" for a in assumes]
            d["proof"] = "proof-main.tex"
            meta["derivations"] = [d]
            if me in legacy:
                script, keys = legacy[me]
                meta["checked_by"] = [{"kind": "legacy", "script": script,
                                       "tags": sorted(keys)}]
            else:
                meta["checked_by"] = [{"kind": "proof", "derivation": "main"}]
        elif rec["kind"] == "prediction":
            basis = sorted(set(uses) | set(context))
            d = {"name": "basis"}
            if basis:
                d["uses"] = [u + "@1" for u in basis]
            if assumes:
                d["assumes"] = [a + "@1" for a in assumes]
            meta["derivations"] = [d]
            flags.append("registered record: kill condition to be filled from the source")
        elif rec["status"] == "conjectured":
            mot = sorted(set(context) | set(uses))
            if mot:
                meta["lineage"] = {"motivated_by": mot}
            else:
                flags.append("conjecture with no referenced motivation")
        elif rec["status"] == "imported":
            imp = []
            for key, loc in rec.get("fact_external", []):
                b = p.bib.get(key, {})
                item = {"citation": b.get("citation") or key, "key": key}
                if loc:
                    item["locator"] = loc
                if b.get("doi"):
                    item["doi"] = b["doi"]
                imp.append(item)
            for key, loc, ocode in rec.get("fact_outside", []):
                b = p.bib.get(key, {})
                imp.append({"citation": b.get("citation") or key, "key": key,
                            "locator": loc, "series": True})
            if not imp:
                prov = re.search(r"\\emph\{Provenance:\}\s*(.+?)(?:\.\s|\.$)", env["statement"], re.S)
                if prov:
                    imp = [{"citation": re.sub(r"[~\\{}]", " ", prov.group(1)).strip()}]
                    flags.append("citation taken from inline provenance (no \\cite)")
                else:
                    imp = [{"citation": "unattributed in source"}]
                    flags.append("imported fact with no citation")
            meta["imported_from"] = _dedupe(imp)
            series = [t["id"] for t in rec.get("fact_series", [])]
            if series:
                meta["lineage"] = {"derived_from": sorted(set(series))}
            if rec.get("companion_of"):
                flags.append("external ingredients of " + rec["companion_of"])
        if assumes and rec["status"] != "proved" and rec["kind"] == "claim" \
                and rec["status"] not in ("postulate",):
            flags.append("statement names postulates: " + ", ".join(assumes))
        meta["locators"] = {"paper": code, "number": rec["locator"],
                            "label": env["label"] or "", "line": env["line"]}
        ex = {"env": env["env"]}
        if context:
            ex["context_refs"] = context
        unres = sorted(set(s_unres + p_unres))
        if unres:
            ex["unresolved_refs"] = unres
        if s_eq + p_eq:
            ex["eqrefs"] = s_eq + p_eq
        outs = sorted(set(s_out + p_out))
        if outs:
            ex["outside_pilot_cites"] = outs
        if flags:
            ex["flags"] = flags
            flags_all.update(f.split(":")[0] for f in flags)
        meta["extraction"] = ex
        formal = rewrite(code, env["statement"])
        if rec.get("companion_of"):
            cits = "; ".join(i["citation"] + (", " + i["locator"] if i.get("locator") else "")
                             for i in meta.get("imported_from", []))
            formal = ("The results from outside the series on which \\claimref{"
                      + rec["companion_of"] + "} draws, as cited there: " + cits + ".")
        title = meta["title"]
        levels = {"formal": formal, "technical": "pending", "lay": "pending",
                  "one-liner": title}
        folder = os.path.join(store, dirs[rec["kind"]], me)
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "entity.md"), "w", encoding="utf-8") as fh:
            fh.write(dump_entity(meta, levels))
        if "derivations" in meta:
            with open(os.path.join(folder, "proof-main.tex"), "w", encoding="utf-8") as fh:
                fh.write(rewrite(code, proof) + "\n")
        stats[f"{rec['kind']}:{rec['status']}"] += 1

    aliases = {f"{r['code']}:{r['env']['label']}": final(r)["id"]
               for r in records if r["alias_of"] is not None}
    label_map = {f"{r['code']}:{r['env']['label']}": final(r)["id"]
                 for r in records if r["env"]["label"]}
    roots = [label_map[k] for k in ("T01:pri:transport", "T01:thm:totality",
                                    "T01:thm:minimality", "T01:thm:chartmin")
             if k in label_map]
    config = {
        "transport_roots": roots,
        "legacy_scripts_dir": "../..",
        "house_style": {"banned_words": ["honest", "honestly"]},
        "governance": {"maintainers": ["leon"], "core_regions": ["transport"]},
        "ai_judge": {"enabled": False},
    }
    with open(os.path.join(store, "config.yaml"), "w") as fh:
        yaml.safe_dump(config, fh, sort_keys=False)
    with open(os.path.join(store, "notation.yaml"), "w") as fh:
        yaml.safe_dump(dict(sorted(notation.items())), fh, allow_unicode=True)
    with open(os.path.join(store, "tombstones.yaml"), "w") as fh:
        fh.write("[]\n")
    seed = {"stats": dict(stats), "flags": dict(flags_all),
            "aliases": aliases, "label_map": label_map,
            "notation_conflicts": {k: sorted(v) for k, v in conflicts.items()},
            "unattributed_checks": dict(unattributed),
            "legacy_mapped_entities": len(legacy)}
    with open(os.path.join(store, "..", "seed", "extraction_report.json"), "w") as fh:
        json.dump(seed, fh, indent=1)
    return seed


def _title(env, rec):
    t = env["title"]
    if t:
        t = re.sub(r"\\cite[pt]?(\[[^\]]*\])?\{[^}]*\}", "", t)
        t = re.sub(r"[;,]?\s*(\{\})?\s*[;,]?\s*(\{\})?\s*$", "", t)
        t = re.sub(r"\\(?:emph|textit|textbf)\{([^}]*)\}", r"\1", t)
        return re.sub(r"\s+", " ", t).strip()
    return f"{rec['code']} {rec['locator']}"


def _dedupe(items):
    seen, out = set(), []
    for it in items:
        k = (it.get("key"), it.get("locator"))
        if k not in seen:
            seen.add(k)
            out.append(it)
    return out


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if a != "--force"]
    print(json.dumps(extract(*args[:3], force="--force" in sys.argv), indent=1)[:3000])
