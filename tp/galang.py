"""The language of the Physics Graph is geometric algebra.

Statements, proofs and checks are written in real geometric algebra: checks import GA.py (E403),
and the formal and technical statements and the proofs avoid the usual stand-ins for what the
algebra already provides. Where geometric algebra is not the right language, the entity says so:

  outside_ga:
    kind: imported | complex-analysis | bridge | other
    why: <the reason, in a sentence>

  - imported: a result taken from elsewhere, stated in its source's language;
  - complex-analysis: analytic continuation, contour arguments, Hilbert-space structure (the
    conventions' "imaginary units" section lists where a bare i stays);
  - bridge: a result whose point is to connect geometric algebra with the standard formalism;
  - other: anything else, with the reason judged in review.

scan(entity) finds the stand-ins in the formal and technical levels and the proofs. It looks only
for unambiguous signs: Pauli or Dirac (gamma) matrices named as such, a cross product, the complex
field or sqrt(-1). It does not flag a matrix as such (the Gram matrix of a form, a mass matrix),
components such as F_{mu nu} or a structure constant epsilon_{ijk}, which geometric algebra uses
too, nor a bare i; and it does not judge whether a declared reason is good. Ordinary scalar
mathematics is geometric algebra already (grade 0) and needs no declaration.

  python -m tp ga-report [--store store]   list the entities that use such notation and do not
                                           declare outside_ga (to translate, or to declare)
"""
import argparse
import re

KINDS = ("imported", "complex-analysis", "bridge", "other")
KIND_WORDS = {"imported": "an imported result, stated in its source's language",
              "complex-analysis": "complex analysis or Hilbert-space structure",
              "bridge": "a bridge to the standard formalism", "other": "see the reason"}

PATTERNS = [
    ("Pauli matrices", re.compile(r"Pauli\s+(?:spin\s+)?matri", re.I)),
    ("Dirac matrices", re.compile(r"(?<!Fermi-)(?<!Fermi )Dirac\s+(?:gamma\s+)?matrices|gamma[\s-]+matri", re.I)),
    ("a cross product", re.compile(r"cross\s+product|\\(?:vec|mathbf|boldsymbol)\{[^}]*\}\s*\\times\s*\\(?:vec|mathbf|boldsymbol)", re.I)),
    ("the complex field", re.compile(r"\\mathbb\{C\}|\\sqrt\{-1\}")),
]


def scan(e):
    """The stand-ins for geometric algebra in an entity's formal and technical levels and proofs:
    a sorted list of what was found."""
    texts = [e.levels.get("formal") or "", e.levels.get("technical") or ""]
    texts += list((e.proofs or {}).values())
    blob = "\n".join(texts)
    return sorted({label for label, rx in PATTERNS if rx.search(blob)})


def declared(e):
    d = e.meta.get("outside_ga")
    return d if isinstance(d, dict) and d.get("kind") in KINDS and d.get("why") else None


def report(store):
    rows = []
    for eid, e in sorted(store.entities.items()):
        hits = scan(e)
        if hits and not declared(e):
            rows.append((eid, hits))
    return rows


def main(argv=None):
    from .model import load_store
    ap = argparse.ArgumentParser(prog="tp ga-report")
    ap.add_argument("cmd")
    ap.add_argument("--store", default="store")
    a = ap.parse_args(argv)
    st = load_store(a.store)
    rows = report(st)
    for eid, hits in rows:
        print(f"{eid}: {', '.join(hits)}")
    print(f"\n{len(rows)} entit{'y' if len(rows) == 1 else 'ies'} use notation outside geometric algebra "
          "without declaring outside_ga (translate them, or declare the reason)")
    return 0
