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
field or sqrt(-1), and a bare imaginary unit i in mathematics (a number or a complex structure, not
an index letter: since 7 November 2026 the unit is written as the pseudoscalar it stands for, I_4,
the right unit x I_4, right multiplication by I_6, or a plane's unit bivector). It does not flag a
matrix as such (the Gram matrix of a form, a mass matrix), components such as F_{mu nu} or a
structure constant epsilon_{ijk}, which geometric algebra uses too, nor i as an index (e_i, sum_i,
x^i, i = 1, ..., n, clause labels (i)); and it does not judge whether a declared reason is good. Ordinary scalar
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


# --- a bare imaginary unit, inside mathematics only ($...$, \[...\], equation environments)
_MATH = re.compile(
    r"\$\$(.+?)\$\$|\$(.+?)\$|\\\[(.+?)\\\]|\\\((.+?)\\\)"
    r"|\\begin\{(equation\*?|align\*?|gather\*?|multline\*?|eqnarray\*?)\}(.+?)\\end\{\5\}", re.S)
# a standalone letter i, not part of a word or macro, not a sub/superscript index
_TOKEN = re.compile(r"(?<![A-Za-z\\_^@])i(?![A-Za-z_'])")
_INDEX_AFTER = re.compile(r"\s*(=|\\in\b|\\ne(q)?\b|<|>|\\le(q)?\b|\\ge(q)?\b|\\to\b|,\s*[jklmn]\b|\\dots|\\ldots|"
                          r"\\cdots|\+\s*1\b|-\s*1\b\s*([,}\)]|$))")
_INDEX_AFTER2 = re.compile(r"\s*(\\notin\b|\\leftrightarrow\b|\\\}|:|/\s*[0-9]|\^\{?([-+0]|\\[mp][pm])\}?|\s*(\\,|\\;)?\s*[a-z]\s*\})")
_INDEX_BEFORE = re.compile(r"(\\setminus|\\\{|\\ket\{|\\bra\{|\\ne(q)?|\\mathbf\{|[_^]?\{[0-9]|^\s*0)\s*$"
                           r"|\\(mu|nu|alpha|beta|rho|sigma)\s*=\s*$")
# a numeral times the unit times a capital or a matrix, 3iI_2, 2iJ; the Gaussian field Q(i)
_UNIT_EXTRA = re.compile(r"(?<![A-Za-z\\_^{])[0-9]+\s*i(?=[A-Z]|\\mathbb|\\mathsf)|(\\mathbb\{Q\}|(?<![A-Za-z\\])Q)\(\s*i\s*\)")
# an i followed by a letter where it can only be the unit: e^{it}, \Delta^{is}, \exp(it ...), \alpha_{i\beta}
_UNIT_BEFORE_LETTER = re.compile(
    r"\^\{\s*-?\s*[0-9]*\s*(\\pi)?\s*i\s*[a-zA-Z\\(]|\\exp\s*(\\left|\\bigl|\\Bigl)?\(\s*-?\s*[0-9]*\s*(\\pi)?\s*i\s*[a-zA-Z\\(]"
    r"|_\{i\\beta\}|(?<=[+=-])\s*i[a-zA-Z](?![A-Za-z])|(?<=[+=-] )i[a-zA-Z](?![A-Za-z])|(?<![A-Za-z\\_^])i(\\beta|\\lambda|\\theta|\\omega|\\pi|\\hbar|\\partial|\\epsilon|\\varepsilon|\\tau|"
    r"\\varphi|\\phi|\\alpha|\\kappa|\\delta|\\chi|\\psi)(?![A-Za-z])")


def bare_unit_hits(text):
    """Short contexts where a bare imaginary unit is used as a number or a complex structure."""
    out = []
    for m in _MATH.finditer(text or ""):
        seg = next(g for g in (m.group(1), m.group(2), m.group(3), m.group(4), m.group(6)) if g is not None)
        if seg.strip() in ("i", "i,", "i, j", "i,j"):
            continue
        if re.search(r"\(\s*i\s*[-+]\s*1\s*\)", seg):
            continue                                      # i is an index throughout: (i+1)(d-1-i)
        for u in _UNIT_EXTRA.finditer(seg):
            out.append(seg[max(0, u.start() - 12):u.end() + 8])
        if re.fullmatch(r"\s*-?\s*i[a-hopq-z]\s*", seg):
            out.append(seg)                               # a unit times a letter alone: $iq$
        for u in _UNIT_BEFORE_LETTER.finditer(seg):
            ctx_before = seg[max(0, u.start() - 12):u.start()]
            if not u.group(0).startswith("_{i\\beta") and re.search(r"_\{\s*$", ctx_before):
                continue                                  # a subscript index such as Z_{i\alpha}
            if re.match(r"\^\{\s*i\s*(\\,)?\s*[jklmna0-9]\s*[\\}]", seg[u.start():u.start() + 12]):
                continue                                  # an index pair such as B^{il}, g^{ij}
            out.append(seg[max(0, u.start() - 12):u.end() + 8])
        for t in _TOKEN.finditer(seg):
            a, b = t.start(), t.end()
            before, after = seg[max(0, a - 16):a], seg[b:b + 24]
            if re.search(r"[_^]\{\s*$", before) and re.match(r"\s*[},]", after):
                continue
            if re.search(r"[_^]\{[^{}]*$", before) and not re.search(r"\^\{[^{}]*$", before):
                continue
            if re.search(r"\^\{[0-9j]*$", before) and re.match(r"[0-9j]+\}", after):
                continue
            if re.search(r"\(\s*$", before) and re.match(r"\s*\)", after):
                continue
            if _INDEX_AFTER.match(after) or _INDEX_AFTER2.match(after) or _INDEX_BEFORE.search(before):
                continue
            if re.search(r"(?<![A-Za-z\\])[nmdjklNM0-9]\s*[-+]\s*$", before) and re.match(r"\s*([)\]},]|$)", after):
                continue                                  # index arithmetic such as n - i, d-1-i
            if re.search(r"[\(\[]\s*$", before) and re.match(r"\s*,", after):
                continue                                  # a pair label such as (i, A)
            if re.search(r",\s*$", before) and re.match(r"\s*\}", after):
                continue                                  # a trailing subscript index such as _{sig,i}
            if re.search(r"[_^]\{[^{}]*$", before) and re.match(r"\s*[-+]\s*[0-9a-z]", after):
                continue                                  # index arithmetic in a sub/superscript, ^{i+j}
            if re.search(r"(\\sum|\\prod|\\bigoplus|\\bigotimes|\\max|\\min)_?\{?\s*$", before):
                continue
            if re.match(r"\s*=\s*e_", after) or re.search(r"\\mathrm\{\s*$", before) and re.match(r"\}\s*=\s*e_", after):
                continue                                  # a named unit defined as a blade, i = e_1
            out.append(before + "i" + after)
    return out


def scan(e):
    """The stand-ins for geometric algebra in an entity's formal and technical levels and proofs:
    a sorted list of what was found."""
    texts = [e.levels.get("formal") or "", e.levels.get("technical") or ""]
    texts += list((e.proofs or {}).values())
    blob = "\n".join(texts)
    found = {label for label, rx in PATTERNS if rx.search(blob)}
    if bare_unit_hits(blob):
        found.add("a bare imaginary unit")
    return sorted(found)


UNIT = "a bare imaginary unit"


def unexcused(e):
    """The stand-ins that count against an entity: everything scan finds, unless outside_ga is declared;
    a bare imaginary unit counts even then (Leon's rule of 7 November 2026: the unit is always written as
    the pseudoscalar it stands for, by the unit principle of the conventions)."""
    hits = scan(e)
    if declared(e):
        hits = [h for h in hits if h == UNIT]
    return hits


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
