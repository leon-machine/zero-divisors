"""Make proofs cite the premises their derivations list.

    python -m tp.citepremises [--store store] [--dry-run]

A derivation's `uses` says which results a proof relies on; the proof text
should name each with \\claimref, so a reader (or an AI) can see where it is
used. Many proofs refer to premises in the paper's own way: a \\ref, a
citation with a locator ("\\cite[Prop.~7.21]{ButlerT5}"), or a number
("Theorem 4.13"). This pass turns those into \\claimref where they point at a
listed premise, and gives a restatement of earlier results (an "Imported:"
Fact) a closing sentence naming what it restates. What it cannot place is
left for review (`premises still uncited`). An edited proof's original is
kept as orig-proof-NAME.tex and the entity's version is bumped.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import sys

import yaml

from .model import load_store

TYPE = (r"(?:Theorems?|Thms?\.?|Propositions?|Props?\.?|Lemmas?|Lems?\.?|Corollar(?:y|ies)|"
        r"Cors?\.?|Facts?|Definitions?|Defs?\.?|Premises?|Observations?|Obs\.?|Principles?|"
        r"Conjectures?|Conj\.?)")


def paper_of_key(key):
    m = re.fullmatch(r"ButlerT(\d+)([a-z]?)", key)
    if not m:
        return None
    return f"T{int(m.group(1)):02d}{m.group(2)}"


def number_of(e):
    loc = e.meta.get("locators") or {}
    if isinstance(loc, list):
        loc = loc[0] if loc else {}
    num = str(loc.get("number") or "").split(" ")[-1]
    return loc.get("paper"), (num if re.fullmatch(r"[A-Z]?\d+(?:\.\d+)*", num) else None)


def cited(text):
    return set(re.findall(r"\\claimref\{([^}]+)\}", text))


def fix_text(text, code, premises, store, reg):
    """-> (new text, set of premises now cited)."""
    done = set()

    # 1. \ref / \eqref / \cref whose label is carried by a premise
    def ref_sub(m):
        labs = [l.strip() for l in m.group(2).split(",")]
        out = []
        for lab in labs:
            t = (reg.get(f"{code}:{lab}") or {}).get("entity")
            if t in premises:
                done.add(t)
                out.append(r"\claimref{%s}" % t)
            else:
                out.append(m.group(1) + "{" + lab + "}")
        return ", ".join(out)
    text = re.sub(r"(\\(?:ref|eqref|cref|Cref))\{([^}]+)\}", ref_sub, text)

    # 2. a series citation with a locator: \cite[Prop.~7.21(1)]{ButlerT5}
    def cite_sub(m):
        loc, keys = m.group(1) or "", [k.strip() for k in m.group(2).split(",")]
        add = []
        for p in premises:
            if p in done:
                continue
            pp, num = number_of(store.entities[p])
            if not num or pp is None:
                continue
            if any(paper_of_key(k) == pp for k in keys) and \
                    re.search(r"(?<![\d.])" + re.escape(num) + r"(?![\d])", loc):
                add.append(p)
        for p in add:
            done.add(p)
        if not add:
            return m.group(0)
        return m.group(0) + " (" + ", ".join(r"\claimref{%s}" % p for p in add) + ")"
    text = re.sub(r"\\cite[pt]?\[([^\]]*)\]\{([^}]+)\}", cite_sub, text)

    # 2b. "Theorem 4.13 of \cite{ButlerT1}", "T1's Theorem 4.13", "(T1, Thm 4.13)"
    for p in premises:
        if p in done:
            continue
        pp, num = number_of(store.entities[p])
        if not num or pp is None:
            continue
        short = "T" + str(int(pp[1:3])) + pp[3:] if re.fullmatch(r"T\d\d[a-z]?", pp) else pp
        pats = [re.compile(r"(" + TYPE + r")(~|\s+)" + re.escape(num) + r"(?![\d.]\d)"
                           r"(?=[^.;]{0,40}\\cite[pt]?(?:\[[^\]]*\])?\{[^}]*Butler" + re.escape(short) + r"\b)"),
                re.compile(r"(?<=\b" + re.escape(short) + r"[\s,])(" + TYPE + r")(~|\s+)"
                           + re.escape(num) + r"(?![\d.]\d)"),
                re.compile(r"(?<=\b" + re.escape(short) + r"'s )(" + TYPE + r")(~|\s+)"
                           + re.escape(num) + r"(?![\d.]\d)")]
        for pat in pats:
            if pat.search(text):
                text = pat.sub(lambda m: m.group(1) + m.group(2) + r"\claimref{%s}" % p, text)
                done.add(p)
                break

    # 3. a number of the same paper after a type word: "Theorem~4.13", "Lemma 2.1(ii)"
    for p in premises:
        if p in done:
            continue
        pp, num = number_of(store.entities[p])
        if not num or pp != code:
            continue
        pat = re.compile(r"(" + TYPE + r")(~|\s+)" + re.escape(num) + r"(?![\d.]\d)")
        if pat.search(text):
            text = pat.sub(lambda m: m.group(1) + m.group(2) + r"\claimref{%s}" % p, text, count=0)
            done.add(p)
    return text, done


def postulate_patterns(title):
    """Ways a proof names a postulate, from its title ("Hypothesis (S): ...",
    "P1: ...", "Premise U: ...", "(L$_E$): ...", "Tameness")."""
    head = title.split(":")[0].strip()
    pats = []
    m = re.search(r"\(([^)]+)\)", head)
    if m:
        lab = re.escape(m.group(1))
        pats += [r"(?:Hypothesis|Premise|Postulate)~?\s*\(" + lab + r"\)", r"\(" + lab + r"\)"]
    elif re.fullmatch(r"(?:Premise |Joint )?[A-Z]{1,2}\d?", head):
        lab = head.split()[-1]
        pats += [r"(?:Premise|Hypothesis|Joint)~?\s*\(?" + re.escape(lab) + r"\)?(?![\w])",
                 r"\(" + re.escape(lab) + r"\)"]
        if re.fullmatch(r"[A-Z]\d", lab):
            pats.append(r"(?<![\w\\])" + re.escape(lab) + r"(?![\w])")
    else:
        word = head.split()[0].lower().rstrip(",")
        if len(word) > 5:
            stem = word[:-4] if word.endswith("ness") else word[:-2]
            pats.append(r"\b" + re.escape(stem) + r"\w*")
    return [re.compile(x, re.I if not m else 0) for x in pats]


def cite_postulates(store, dry=False):
    """Name each assumed postulate where the proof mentions it by its label."""
    n = 0
    changed = set()
    for eid, e in sorted(store.entities.items()):
        for d in e.derivations():
            if not isinstance(d, dict) or not d.get("proof"):
                continue
            name = d.get("name")
            text = e.proofs.get(name, "")
            if not text.strip():
                continue
            new = text
            for ref in d.get("assumes") or []:
                pid = ref.split("@")[0]
                if pid in cited(new) or pid not in store.entities:
                    continue
                for pat in postulate_patterns(store.entities[pid].title):
                    m = pat.search(new)
                    if m:
                        tok = m.group(0)
                        rep = (tok[:-1] + r", \claimref{%s})" % pid) if tok.startswith("(") and tok.endswith(")") \
                            else tok + r" (\claimref{%s})" % pid
                        new = new[:m.start()] + rep + new[m.end():]
                        n += 1
                        break
            if new != text and not dry:
                fname = d.get("proof")
                path = os.path.join(e.path, fname)
                orig = os.path.join(e.path, "orig-" + fname)
                if not os.path.exists(orig):
                    shutil.copyfile(path, orig)
                open(path, "w", encoding="utf-8").write(new)
                changed.add(eid)
    for eid in changed:
        p = os.path.join(store.entities[eid].path, "entity.md")
        t = open(p, encoding="utf-8").read()
        t = re.sub(r"^version: (\d+)$", lambda m: f"version: {int(m.group(1)) + 1}", t,
                   count=1, flags=re.M)
        open(p, "w", encoding="utf-8").write(t)
    return n, len(changed)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--store", default="store")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--report", default="seed/uncited_premises_remaining.yaml")
    ap.add_argument("--assumes", action="store_true",
                    help="cite assumed postulates where the proof names them by label")
    a = ap.parse_args(argv)
    store = load_store(a.store)
    if a.assumes:
        n, k = cite_postulates(store, a.dry_run)
        print(f"postulates cited by label: {n} in {k} entities")
        return 0
    reg = yaml.safe_load(open(os.path.join(a.store, "labels.yaml"))) or {}
    fixed = restated = 0
    remaining = {}
    changed_entities = set()
    for eid, e in sorted(store.entities.items()):
        code = (e.meta.get("locators") or {}).get("paper")
        for d in e.derivations():
            if not isinstance(d, dict) or not d.get("proof"):
                continue
            name = d.get("name")
            text = e.proofs.get(name, "")
            if not text.strip():
                continue
            premises = {p.split("@")[0] for p in (d.get("uses") or [])}
            todo = premises - cited(text)
            if not todo:
                continue
            new, done = fix_text(text, code, todo, store, reg)
            todo -= done
            fixed += len(done)
            # a restatement of earlier results: say what it restates
            if todo and e.title.lower().startswith("imported") and e.status == "proved":
                names = ", ".join(r"\claimref{%s}" % p for p in sorted(todo))
                new = new.rstrip() + "\n\nThis restates " + names + "."
                restated += len(todo)
                todo = set()
            if todo:
                remaining.setdefault(eid, {})[name] = sorted(todo)
            if new != text and not a.dry_run:
                fname = d.get("proof")
                path = os.path.join(e.path, fname)
                orig = os.path.join(e.path, "orig-" + fname)
                if not os.path.exists(orig):
                    shutil.copyfile(path, orig)
                open(path, "w", encoding="utf-8").write(new if new.endswith("\n") else new + "\n")
                changed_entities.add(eid)
    if not a.dry_run:
        for eid in changed_entities:
            p = os.path.join(store.entities[eid].path, "entity.md")
            t = open(p, encoding="utf-8").read()
            t = re.sub(r"^version: (\d+)$", lambda m: f"version: {int(m.group(1)) + 1}", t,
                       count=1, flags=re.M)
            open(p, "w", encoding="utf-8").write(t)
        with open(a.report, "w", encoding="utf-8") as fh:
            yaml.safe_dump(remaining, fh, sort_keys=True, width=120)
    print(f"cited by reference, citation or number: {fixed}; restatements named: {restated}; "
          f"entities edited: {len(changed_entities)}; premises still uncited: "
          f"{sum(len(v) for x in remaining.values() for v in x.values())} in {len(remaining)} entities")
    return 0


if __name__ == "__main__":
    sys.exit(main())
