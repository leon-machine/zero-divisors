"""Quantities (roadmap item 10) and the contradiction scan (item 9).

A quantity entity (store/quantities/<id>/entity.md, kind `quantity`) holds one record
value: symbol, an exact decimal value, its uncertainty, units, dimension and source.

    tp quantity list                 every quantity: symbol, value, units, status
    tp quantity show <id>            one quantity in full, with the entities that use it
    tp quantity users <id> [--json]  entities that pin it, and entities whose text or check
                                     carries its value as a literal (not yet pinned)
    tp quantity check                every quantity validates (layer 1), its value and
                                     uncertainty parse exactly, uncertainty < |value|, and
                                     its dimension agrees with its units

The scan helpers here (`numbers`, `symbol_hits`, `literal_users`, `contradictions`) are
used by layer 5 of the validator (W510 / I510).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from fractions import Fraction

from .model import LEVELS, Store, load_store

# ---------------------------------------------------------------------------
# units and dimensions
# ---------------------------------------------------------------------------

# base dimensions: (mass, length, time, temperature); scale is the SI value of one unit
EV = Fraction("1.602176634e-19")            # J, exact (SI 2019)
BASE_UNITS = {
    "kg": (Fraction(1), (1, 0, 0, 0)),
    "g": (Fraction(1, 1000), (1, 0, 0, 0)),
    "m": (Fraction(1), (0, 1, 0, 0)),
    "km": (Fraction(1000), (0, 1, 0, 0)),
    "cm": (Fraction(1, 100), (0, 1, 0, 0)),
    "fm": (Fraction(1, 10 ** 15), (0, 1, 0, 0)),
    # IAU 2015: 1 pc = 648000/pi au; an exact decimal is not available, the store's value
    # (quantity.megaparsec) is used, and only its dimension matters here
    "Mpc": (Fraction("3.0856775814913673e22"), (0, 1, 0, 0)),
    "pc": (Fraction("3.0856775814913673e16"), (0, 1, 0, 0)),
    "s": (Fraction(1), (0, 0, 1, 0)),
    "yr": (Fraction(31557600), (0, 0, 1, 0)),          # Julian year
    "Gyr": (Fraction(31557600) * 10 ** 9, (0, 0, 1, 0)),
    "K": (Fraction(1), (0, 0, 0, 1)),
    "J": (Fraction(1), (1, 2, -2, 0)),
    "meV": (EV / 1000, (1, 2, -2, 0)),
    "eV": (EV, (1, 2, -2, 0)),
    "keV": (EV * 10 ** 3, (1, 2, -2, 0)),
    "MeV": (EV * 10 ** 6, (1, 2, -2, 0)),
    "GeV": (EV * 10 ** 9, (1, 2, -2, 0)),
    "TeV": (EV * 10 ** 12, (1, 2, -2, 0)),
    "1": (Fraction(1), (0, 0, 0, 0)),
}

DIMENSIONS = {
    "dimensionless": (0, 0, 0, 0),
    "mass": (1, 0, 0, 0),
    "length": (0, 1, 0, 0),
    "time": (0, 0, 1, 0),
    "temperature": (0, 0, 0, 1),
    "energy": (1, 2, -2, 0),
    "action": (1, 2, -1, 0),
    "velocity": (0, 1, -1, 0),
    "inverse time": (0, 0, -1, 0),
    "inverse area": (0, -2, 0, 0),
    "energy per temperature": (1, 2, -2, -1),
    "energy times length": (1, 3, -2, 0),
}
ENERGY = DIMENSIONS["energy"]

UNIT_TOKEN_RE = re.compile(r"([A-Za-z]+|1)(?:\^\{?([+-]?\d+)\}?)?$")


def parse_units(text: str):
    """'km/s/Mpc', 'GeV s', 'm^-2', 'MeV fm', '1', 'dimensionless' -> (scale, dims).
    Raises ValueError on an unknown unit."""
    s = str(text).strip()
    if s in ("", "1", "dimensionless"):
        return Fraction(1), (0, 0, 0, 0)
    scale, dims = Fraction(1), [0, 0, 0, 0]
    parts = re.split(r"\s*(/)\s*", s)
    sign = 1
    for part in parts:
        if part == "/":
            sign = -1
            continue
        for tok in part.replace("*", " ").replace("\\,", " ").split():
            m = UNIT_TOKEN_RE.match(tok)
            if not m or m.group(1) not in BASE_UNITS:
                raise ValueError(f"unknown unit {tok!r} in {text!r}")
            u_scale, u_dims = BASE_UNITS[m.group(1)]
            p = sign * int(m.group(2) or 1)
            scale *= u_scale ** p
            for i in range(4):
                dims[i] += p * u_dims[i]
        # a slash applies to the one token group after it only
        sign = 1
    return scale, tuple(dims)


def dimension_agrees(units: str, dimension: str):
    """-> (ok, message). Mass quoted in an energy unit (GeV for a particle mass) is
    accepted: the store works in natural units, c = 1."""
    try:
        _, ud = parse_units(units)
    except ValueError as exc:
        return False, str(exc)
    want = DIMENSIONS.get(str(dimension).strip())
    if want is None:
        return False, (f"unknown dimension {dimension!r} (use one of "
                       + ", ".join(sorted(DIMENSIONS)) + ")")
    if ud == want or (want == DIMENSIONS["mass"] and ud == ENERGY):
        return True, ""
    return False, f"units {units!r} do not have dimension {dimension!r}"


def convert(value: Fraction, from_units: str, to_units: str):
    """value in from_units -> value in to_units, or None if the dimensions differ or a
    unit is unknown."""
    try:
        fs, fd = parse_units(from_units)
        ts, td = parse_units(to_units)
    except ValueError:
        return None
    if fd != td:
        return None
    return value * fs / ts


# ---------------------------------------------------------------------------
# quantity entities
# ---------------------------------------------------------------------------

def exact_value(text):
    from .validate import exact_value as ev
    return ev(text)


def quantities(store: Store) -> dict:
    return {eid: e for eid, e in sorted(store.entities.items()) if e.kind == "quantity"}


def block(e) -> dict:
    q = e.meta.get("quantity")
    return q if isinstance(q, dict) else {}


def value_of(e):
    try:
        return exact_value(block(e).get("value"))
    except (ValueError, TypeError):
        return None


def uncertainty_of(e) -> Fraction:
    try:
        return exact_value(block(e)["uncertainty"]) if "uncertainty" in block(e) else Fraction(0)
    except (ValueError, TypeError):
        return Fraction(0)


def check_entity(store: Store, e, layer1_findings=()) -> list:
    """-> [(severity, message)] for one quantity entity."""
    out = [("error", f"{f.code} {f.message}") for f in layer1_findings]
    q = block(e)
    if not q:
        return out + [("error", "no quantity block")]
    v = u = None
    try:
        v = exact_value(q.get("value"))
    except (ValueError, TypeError) as exc:
        out.append(("error", f"value: {exc}"))
    if "uncertainty" in q:
        try:
            u = exact_value(q["uncertainty"])
        except (ValueError, TypeError) as exc:
            out.append(("error", f"uncertainty: {exc}"))
    if v is not None and u is not None:
        if u < 0:
            out.append(("error", "uncertainty is negative"))
        elif v != 0 and u >= abs(v):
            out.append(("error", f"uncertainty {q['uncertainty']} is not below |value| "
                        f"{q['value']}"))
    if q.get("exact"):
        if u:
            out.append(("error", "an exact value carries no uncertainty"))
        if e.status == "measured":
            out.append(("error", "a measured value is not exact"))
    elif e.status == "measured" and "uncertainty" not in q:
        out.append(("warning", "a measured value without an uncertainty"))
    units = q.get("units")
    try:
        parse_units(units)
    except ValueError as exc:
        out.append(("error", f"units: {exc}"))
    else:
        if q.get("dimension"):
            ok, msg = dimension_agrees(units, q["dimension"])
            if not ok:
                out.append(("error", f"dimension: {msg}"))
    src = q.get("source") or {}
    if not (src.get("doi") or src.get("url") or src.get("locator")):
        out.append(("warning", "source has no doi, url or locator"))
    return out


# ---------------------------------------------------------------------------
# numbers in LaTeX and in check source
# ---------------------------------------------------------------------------

NUM_RE = re.compile(
    r"(?<![\w.\\{])(?P<sign>[-\u2212])?(?P<mant>\d+(?:\.\d+)?)"
    r"(?:\s*(?:\\times|\\cdot|x|\u00d7)\s*10\^\{?(?P<exp1>[-\u2212+]?\d+)\}?"
    r"|[eE](?P<exp2>[-+]?\d+))?"
    r"(?P<dots>\s*(?:\\ldots|\\dots|\.\.\.))?(?![\w.])")
UNC_RE = re.compile(r"\s*(?:\\pm|\+-|\+/-|\u00b1)\s*(\d+(?:\.\d+)?)")
UNIT_AFTER_RE = re.compile(
    r"\s*(?:\\,|\\ |~|\$|\\mathrm\{|\\text\{|\{)*\s*"
    r"(?P<u>meV|keV|MeV|GeV|TeV|eV|km\s*/\s*s\s*/\s*Mpc|km\s*s\^\{?-1\}?\s*Mpc\^\{?-1\}?|"
    r"m\^\{?-2\}?|K|kg|fm|Mpc|km|cm|Gyr|s)(?![A-Za-z])")


class Number:
    __slots__ = ("value", "ulp", "sig", "digits", "start", "end", "text", "dots", "exp",
                 "bare_int")

    def __init__(self, m):
        mant = m.group("mant")
        exp = m.group("exp1") or m.group("exp2") or "0"
        exp = int(exp.replace("\u2212", "-"))
        neg = bool(m.group("sign"))
        val = Fraction(mant) * Fraction(10) ** exp
        self.value = -val if neg else val
        dec = len(mant.split(".")[1]) if "." in mant else 0
        self.ulp = Fraction(10) ** (exp - dec)
        self.digits = mant.replace(".", "").lstrip("0") or "0"
        self.sig = len(self.digits)
        self.start, self.end = m.start(), m.end()
        self.text = m.group(0).strip()
        self.dots = bool(m.group("dots"))
        self.exp = exp
        self.bare_int = "." not in mant and not (m.group("exp1") or m.group("exp2"))


def numbers(text: str):
    for m in NUM_RE.finditer(text):
        yield Number(m)


PY_FRACTION_RE = re.compile(
    r"\b(?:F|Fraction|Q|q)\(\s*(?P<p>\d+)\s*,\s*(?:10\s*\*\*\s*(?P<k>\d+)|(?P<d>10+))\s*\)")


class _PyNumber(Number):
    def __init__(self, m):
        p = m.group("p")
        k = int(m.group("k")) if m.group("k") else len(m.group("d")) - 1
        self.value = Fraction(int(p), 10 ** k)
        self.ulp = Fraction(1, 10 ** k)
        self.digits = p.lstrip("0") or "0"
        self.sig = len(self.digits)
        self.start, self.end = m.start(), m.end()
        self.text = m.group(0)
        self.dots = False
        self.exp = 0
        self.bare_int = False


def py_fractions(text: str):
    """F(938272, 1000), Fraction(12209, 10 ** 4): decimals spelled as fractions in checks."""
    for m in PY_FRACTION_RE.finditer(text):
        yield _PyNumber(m)


def plain(text: str) -> str:
    """LaTeX -> a comparable plain string: macros like \\mathrm and braces dropped,
    backslashes removed (\\tau -> tau, m_{\\tau} -> m_tau). A space survives only
    between two word characters (the boundary of a token), and as ' '."""
    t = re.sub(r"\\(?:mathrm|text|rm|mathit|boldsymbol|bm)\b", "", text)
    t = re.sub(r"\\[,;:! ]", " ", t)
    t = t.replace("$", " ").replace("{", "").replace("}", "")
    t = t.replace("\\", "")
    t = re.sub(r"(?<=[^\w\s])\s+|\s+(?=[^\w\s])", "", t)
    return re.sub(r"\s+", " ", t).strip()


# extra spellings of a symbol beyond its LaTeX form in the quantity block
SYMBOL_VARIANTS = {
    "quantity.planck-mass": ("M_Pl", "M_P", "m_P", "M_Planck"),
    "quantity.reduced-planck-mass": ("M_P", "M_Pl", "barM_P", "M_bar"),
    "quantity.weak-mixing-angle-mz": ("sin^2theta_W", "sin^2theta_WM_Z", "s^2_W",
                                      "sin^2theta_W(M_Z)"),
    "quantity.strong-coupling-mz": ("alpha_s", "alpha_s(M_Z)", "alpha_3"),
    "quantity.inverse-fine-structure-mz": ("alpha^-1_em", "alpha_em^-1",
                                           "alpha_em^-1(M_Z)", "alpha^-1_em(M_Z)"),
    "quantity.hubble-constant": ("H_0", "H0"),
    "quantity.dark-energy-density-parameter": ("Omega_Lambda", "Omega_L"),
    "quantity.baryon-density": ("Omega_bh^2",),
    "quantity.cold-dark-matter-density": ("Omega_ch^2", "Omega_cdmh^2"),
    "quantity.cmb-temperature": ("T_0", "T_CMB", "T_gamma0"),
    "quantity.effective-neutrino-number": ("N_eff", "Neff"),
    "quantity.top-quark-mass": ("m_t",),
    "quantity.bottom-quark-mass": ("m_b",),
    "quantity.z-boson-mass": ("M_Z", "m_Z"),
    "quantity.tau-mass": ("m_tau",),
    "quantity.muon-mass": ("m_mu",),
    "quantity.electron-mass": ("m_e",),
    "quantity.proton-mass": ("m_p",),
}


def symbol_forms(e) -> set:
    forms = {plain(str(block(e).get("symbol") or ""))}
    forms |= set(SYMBOL_VARIANTS.get(e.id, ()))
    return {f for f in forms if f}


REL_RE = re.compile(r"(=|\\approx|\\simeq|\\equiv|\u2248)\s*$")


CHECK_WRAP_RE = re.compile(r"(?:\b(?:F|Fraction|Q|q)\(\s*)?[\"']?$")


def symbol_before(text: str, num: Number, width=48):
    """If the number follows `<symbol> = ` (or \\approx; in a check also
    `NAME = F("`), -> the plain text before the relation, else None."""
    pre = text[max(0, num.start - width):num.start]
    pre = pre[:CHECK_WRAP_RE.search(pre).start()]
    m = REL_RE.search(pre)
    if not m:
        return None
    return plain(pre[:m.start()])


def matches_symbol(before: str, forms, ignore_case=False) -> bool:
    """`before` ends with one of the symbol forms, starting a token (not m_tau inside
    xm_tau); spaces inside the symbol are ignored (Omega_b h^2 = Omega_bh^2). With
    ignore_case (check source: OMEGA_L), case is ignored; never in LaTeX, where m_p and
    M_P differ. A trailing argument like (M_Z) is allowed."""
    if before is None:
        return False
    low = before.lower() if ignore_case else before
    tight = low.replace(" ", "")
    # position in `low` of each character of `tight`
    pos = [i for i, ch in enumerate(low) if ch != " "]
    for f in forms:
        f = (f.lower() if ignore_case else f).replace(" ", "")
        for m in re.finditer(re.escape(f) + r"(?:\([^()]{0,12}\))?$", tight):
            k = m.start()
            if k == 0:
                return True
            i = pos[k]
            if not low[i - 1].isalnum() or low[i - 1] == " ":
                return True
    return False


def unit_after(text: str, num: Number):
    m = UNIT_AFTER_RE.match(text, num.end)
    if not m:
        return None
    u = re.sub(r"\s+", "", m.group("u"))
    if u.startswith("km") and "Mpc" in u:
        return "km/s/Mpc"
    if u.startswith("m^"):
        return "m^-2"
    return u


def uncertainty_after(text: str, num: Number):
    m = UNC_RE.match(text, num.end)
    return Fraction(m.group(1)) * Fraction(10) ** num.exp if m else None


# ---------------------------------------------------------------------------
# literal users: where a record value is written into text or a check
# ---------------------------------------------------------------------------

def _digit_match(num: Number, val: Fraction) -> bool:
    """The displayed digits of num are val's (rounded or truncated to those digits), up to
    a power of 1000 (a unit prefix: GeV -> eV, km -> m)."""
    if val == 0 or num.value == 0:
        return False
    # long literals (5 or more digits) may carry any power of ten: F(12209, 10 ** 4) * 10 ** 19
    ks = [Fraction(10) ** k for k in range(-40, 41)] if num.sig >= 5 \
        else [Fraction(1000) ** k for k in range(-5, 6)]
    for scale in ks:
        target = abs(val) * scale
        if abs(abs(num.value) - target) <= num.ulp:
            # rounding or truncation to the shown digits
            if abs(abs(num.value) - target) * 2 <= num.ulp or \
                    (abs(num.value) <= target < abs(num.value) + num.ulp):
                return True
    return False


def _sig_digits(v: Fraction) -> str:
    """The significant digits of an exact decimal, trailing zeros dropped ('1.220890e19'
    -> '12209'); '' if v is not a terminating decimal."""
    v = abs(v)
    for _ in range(80):
        if v.denominator == 1:
            return str(v.numerator).rstrip("0")
        v *= 10
    return ""


def _sources(e):
    """(where, text) pairs scanned for literals: formal and technical levels, proofs, and
    the entity's own Python files."""
    out = [(f"level {lv}", e.levels.get(lv) or "") for lv in ("formal", "technical")]
    out += [(f"proof {k}", v) for k, v in e.proofs.items()]
    if e.path and os.path.isdir(e.path):
        for fn in sorted(os.listdir(e.path)):
            if fn.endswith(".py"):
                with open(os.path.join(e.path, fn), encoding="utf-8", errors="replace") as fh:
                    out.append((fn, fh.read()))
    return out


def literal_users(store: Store, qids=None, detail=False) -> dict:
    """-> {qid: {eid: sorted literals}}: entities whose text or check carries the
    quantity's value. A literal of 4 or more significant digits counts on its own; a
    shorter one only right after the quantity's symbol and a relation. With detail=True
    -> {qid: {eid: {"check": [...], "text": [...]}}} (check: the entity's Python files;
    text: its formal and technical levels and proofs)."""
    qs = quantities(store)
    if qids is not None:
        qs = {k: v for k, v in qs.items() if k in qids}
    targets = []
    for qid, q in qs.items():
        v = value_of(q)
        if v is None or v == 0:
            continue
        targets.append((qid, v, symbol_forms(q), q.meta.get("quantity", {}).get("exact")))
    out = {qid: {} for qid in qs}
    for eid, e in store.entities.items():
        if e.kind == "quantity":
            continue
        for where, text in _sources(e):
            nums = list(numbers(text))
            if where.endswith(".py"):
                nums += list(py_fractions(text))
            for num in nums:
                if num.sig < 2:
                    continue
                before = None
                for qid, v, forms, exact in targets:
                    if not _digit_match(num, v):
                        continue
                    if num.bare_int:
                        # a bare integer counts only when it carries every significant
                        # digit of a long value (299792458); F(938272, 1000) is read as
                        # the decimal it spells, by PY_FRACTION_RE
                        if len(num.digits.rstrip("0")) < 6 or num.digits.rstrip("0") != _sig_digits(v) \
                                or text[num.end:num.end + 2].lstrip().startswith(","):
                            continue
                    ok = num.sig >= 4 and not (exact and num.sig < 6 and v.denominator == 1)
                    if not ok:
                        if before is None:
                            before = symbol_before(text, num) or ""
                        ok = matches_symbol(before, forms, ignore_case=where.endswith(".py"))
                    if ok:
                        kind = "check" if where.endswith(".py") else "text"
                        out[qid].setdefault(eid, set()).add((kind, num.text))
    if detail:
        return {qid: {eid: {k: sorted(t for kk, t in lits if kk == k)
                            for k in ("check", "text") if any(kk == k for kk, _ in lits)}
                      for eid, lits in sorted(users.items())}
                for qid, users in out.items()}
    return {qid: {eid: sorted({t for _, t in lits}) for eid, lits in sorted(users.items())}
            for qid, users in out.items()}


def pinned_users(store: Store, qid: str) -> list:
    from .model import parse_pin
    res = []
    for eid, e in sorted(store.entities.items()):
        for ref in e.meta.get("quantities") or []:
            p = parse_pin(ref)
            if p and p[0] == qid:
                res.append((eid, ref))
    return res


# ---------------------------------------------------------------------------
# contradictions (layer 5, W510)
# ---------------------------------------------------------------------------

# C10 of docs/gtg-dictionary.md: the store displays the connection
# Omega in the GTG sign, D_a M = a.nabla M + Omega(a) x M. A displayed connection value
# in the Cartan sign (no minus) is the drift these patterns catch. Cartan one-forms
# omega^{i}{}_{0} = H_i theta^i remain allowed (they are forms, not bivector values).
_SUB_I = r"_\{?(?:i|[1-3])\}?"
SIGN_PATTERNS = [
    ("C10 Omega(e_i) = +sigma_i B_i",
     re.compile(r"\\Omega\s*\(\s*(?:\\hb\()?\s*e" + _SUB_I + r"\s*\)?\s*\)\s*=\s*\+?\s*"
                r"\\sigma" + _SUB_I + r"\s*\\?,?\s*B" + _SUB_I)),
    ("C10 connection value +H_i e_0 ^ e_i",
     re.compile(r"\\(?:Omega|omega)\s*\(\s*(?:e|\\gamma)" + _SUB_I + r"\s*\)\s*=\s*\+?\s*"
                r"H" + _SUB_I + r"\s*\\?,?\s*\(?\s*(?:e|\\gamma)_\{?0\}?\s*\\wedge")),
    ("C10 Omega = +H_i B_i (bivector form, no minus)",
     re.compile(r"\\Omega\s*\(\s*e" + _SUB_I + r"\s*\)\s*=\s*\+?\s*H" + _SUB_I
                + r"\s*\\?,?\s*B" + _SUB_I)),
    # the patterns below match the positive form anywhere; a match right after a minus
    # sign is the GTG display and is skipped (see _after_minus)
    ("C10 Hubble-normalised Kasner connection +sum_i p_i B_i (x) theta^i",
     re.compile(r"\\sum_\{?i\}?\s*p_\{?i\}?\s*\\?,?\s*B_\{?i\}?\s*\\?,?\s*\\otimes\s*"
                r"(?:\\hat\s*\\?|\\widehat\{\\?)?theta")),
    ("C10 boundary value +sum_i p_i B_i (x) nu^i",
     re.compile(r"boundary value is\s*(?:the weight one-form\s*,?\s*)?\$?\s*\\sum_\{?i\}?\s*"
                r"p_\{?i\}?\s*\\?,?\s*B_\{?i\}?\s*\\?,?\s*\\otimes")),
    ("C10 model generator H(s) = +sum_i u^i p_i B_i",
     re.compile(r"H\s*\(s\)\s*=\s*\+?\s*\\sum_\{?i\}?\s*u\^\{?i\}?\s*\(s\)\s*\\?,?\s*"
                r"p_\{?i\}?\s*\\?,?\s*B_\{?i\}?")),
    ("C10 limiting connection +B_w",
     re.compile(r"\\(?:Omega|omega)[^$]{0,60}?(?:\\to|\\rightarrow|\\longrightarrow)\s*\+?\s*"
                r"B_\{?(?:w|\\mathrm\{w\})\}?(?![\w^])")),
]

FRACTION_RE = re.compile(
    r"(?<![\w.^_{])(?:\\[dt]?frac\{(?P<p1>\d+)\}\{(?P<q1>\d+)\}|(?P<p2>\d+)\s*/\s*(?P<q2>\d+))"
    r"\s*(?P<rel>=|\\approx|\\simeq)\s*(?=\d)")


def _after_minus(text: str, i: int) -> bool:
    """A minus sign right before position i (spaces, $, { and \\left( skipped)."""
    pre = re.sub(r"(?:\s|\$|\{|\\left\(|\()+$", "", text[max(0, i - 20):i])
    return pre.endswith("-") or pre.endswith("\u2212")


def _level_texts(e):
    return [(lv, e.levels.get(lv) or "") for lv in ("formal", "technical")]


# a value inside a prediction, a fit, a running mass or a hypothetical is not a record
# value: the sentence up to the number (and a little after) is searched for these cues
NOT_RECORD_RE = re.compile(
    r"\b(?:predict\w*|fit|fits|fitted|fitting|running|runs|run to|would|model\w*|"
    r"hypothetical\w*|suppose\w*|if|at the scale|at the unification|toy|sample|"
    r"for example|e\.g\.)\b", re.I)


def _not_record(text: str, num: Number) -> bool:
    start = max(text.rfind(". ", 0, num.start), text.rfind("\n\n", 0, num.start), 0)
    return bool(NOT_RECORD_RE.search(text[start:num.end + 40]))


def scan_occurrences(store: Store, qs=None, with_exempt=False):
    """-> [(eid, level, qid, Number, unit, unc)] for every `<symbol> = number` in formal and
    technical texts whose symbol is a quantity's (claims, predictions, objects, questions;
    notes are commentary and are left out). Values in a sentence that reads as a
    prediction, fit or hypothetical (NOT_RECORD_RE) are left out; with_exempt=True
    -> (kept, left_out)."""
    qs = quantities(store) if qs is None else qs
    forms = {qid: symbol_forms(q) for qid, q in qs.items()}
    out, left = [], []
    for eid, e in sorted(store.entities.items()):
        if e.kind in ("quantity", "note"):
            continue
        for lv, text in _level_texts(e):
            if not text or text.strip() == "pending":
                continue
            for num in numbers(text):
                before = symbol_before(text, num)
                if not before:
                    continue
                for qid, fs in forms.items():
                    if matches_symbol(before, fs):
                        row = (eid, lv, qid, num, unit_after(text, num),
                               uncertainty_after(text, num))
                        (left if _not_record(text, num) else out).append(row)
    return (out, left) if with_exempt else out


def _in_units(num: Number, unit, q):
    """num's value in the quantity's units; None if its unit has another dimension."""
    qu = str(block(q).get("units") or "1")
    if unit is None:
        return num.value, num.ulp
    c = convert(Fraction(1), unit, qu)
    if c is None:
        return None
    return num.value * c, num.ulp * c


DRIFT_WINDOW = Fraction(5, 100)     # a different value within 5 %: drift, not another quantity


def contradictions(store: Store):
    """-> (findings, stats): findings are (eid, message) pairs for W510, stats a dict for
    the I510 summary."""
    qs = quantities(store)
    finds, stats = [], {"quantities": len(qs), "occurrences": 0, "drift": 0,
                        "disagree": 0, "decimal": 0, "sign": 0, "sign_hits": {}}
    occ, left = scan_occurrences(store, qs, with_exempt=True)
    stats["occurrences"] = len(occ)
    stats["not_record"] = len(left)
    ok_occ = []
    # (a) drift from the quantity entity's value
    by_num = {}
    for eid, lv, qid, num, unit, unc in occ:
        by_num.setdefault((eid, lv, num.start), []).append((qid, num, unit, unc))
    for (eid, lv, _), cands in sorted(by_num.items()):
        agree, near = [], []
        for qid, num, unit, unc in cands:
            q = qs[qid]
            v = value_of(q)
            conv = _in_units(num, unit, q)
            if v is None or conv is None:
                continue
            x, ulp = conv
            gap = abs(x - v)
            if gap <= uncertainty_of(q) + ulp:
                agree.append((qid, x, ulp, num))
            elif v != 0 and gap / abs(v) <= DRIFT_WINDOW:
                near.append((qid, x, ulp, num, gap))
        if agree:
            ok_occ.extend((eid, lv, a[0], a[1], a[2], a[3]) for a in agree)
        elif near:
            qid, x, ulp, num, gap = near[0]
            q = qs[qid]
            qb = block(q)
            unc = f" +- {qb['uncertainty']}" if qb.get("uncertainty") else ""
            units = str(qb.get("units") or "")
            units = "" if units in ("", "1", "dimensionless") else " " + units
            finds.append((eid, f"quantity drift ({lv}): {num.text}"
                          f" for {qb.get('symbol')}, but {qid} is {qb.get('value')}{unc}"
                          f"{units}; the gap {float(gap):.3g} exceeds the "
                          "uncertainty and the displayed precision"))
            stats["drift"] += 1
    # (b) two statements disagreeing with each other at their displayed precision
    seen = set()
    by_q = {}
    for eid, lv, qid, x, ulp, num in ok_occ:
        by_q.setdefault(qid, []).append((eid, lv, x, ulp, num))
    for qid, rows in sorted(by_q.items()):
        for i, (e1, l1, x1, u1, n1) in enumerate(rows):
            for e2, l2, x2, u2, n2 in rows[i + 1:]:
                if e1 == e2 or abs(x1 - x2) <= u1 + u2:
                    continue
                key = (qid, min(e1, e2), max(e1, e2))
                if key in seen:
                    continue
                seen.add(key)
                sym = block(qs[qid]).get("symbol")
                finds.append((e1, f"same-quantity disagreement: {sym} = {n1.text} here "
                              f"({l1}) but {n2.text} in {e2} ({l2}); incompatible at the "
                              f"displayed precision ({qid})"))
                stats["disagree"] += 1
    # (d) an exact fraction shown with a decimal that is neither its rounding nor, under
    # \ldots, its truncation
    for eid, e in sorted(store.entities.items()):
        if e.kind == "quantity":
            continue
        for lv, text in _level_texts(e):
            for m in FRACTION_RE.finditer(text):
                p = int(m.group("p1") or m.group("p2"))
                q = int(m.group("q1") or m.group("q2"))
                if q == 0:
                    continue
                nm = NUM_RE.match(text, m.end())
                if not nm:
                    continue
                num = Number(nm)
                if num.exp != 0 or "." not in nm.group("mant"):
                    continue          # an integer or a power of ten: not a decimal display
                exact = Fraction(p, q)
                x, ulp = abs(num.value), num.ulp      # the fraction carries no sign here
                trunc_ok = x <= exact < x + ulp
                round_ok = abs(exact - x) * 2 <= ulp
                bad = (not trunc_ok) if num.dots else not (trunc_ok or round_ok)
                if bad:
                    shown = f"{m.group(0).strip()} {num.text}"
                    want = _decimal(exact, len(nm.group("mant").split(".")[1]) + 2)
                    how = "a truncation (\\ldots)" if num.dots else "a rounding or truncation"
                    finds.append((eid, f"decimal drift ({lv}): {shown} is not {how} of "
                                  f"{p}/{q} = {want}..."))
                    stats["decimal"] += 1
    # (c) sign conventions
    for eid, e in sorted(store.entities.items()):
        if e.kind == "quantity":
            continue
        texts = _level_texts(e) + [(f"proof {k}", v) for k, v in e.proofs.items()]
        for lv, text in texts:
            for name, rx in SIGN_PATTERNS:
                for m in rx.finditer(text):
                    if _after_minus(text, m.start()):
                        continue
                    snippet = re.sub(r"\s+", " ", text[m.start():m.end()])
                    finds.append((eid, f"sign convention ({lv}): '{snippet}' shows a "
                                  f"connection value in the Cartan sign; the store displays "
                                  f"Omega in the GTG sign (DICTIONARY C10) [{name}]"))
                    stats["sign"] += 1
                    stats["sign_hits"][name] = stats["sign_hits"].get(name, 0) + 1
    return finds, stats


def _decimal(x: Fraction, places: int) -> str:
    neg = x < 0
    x = abs(x)
    ip = x.numerator // x.denominator
    frac = x - ip
    digs = []
    for _ in range(places):
        frac *= 10
        d = frac.numerator // frac.denominator
        digs.append(str(d))
        frac -= d
    return ("-" if neg else "") + str(ip) + ("." + "".join(digs) if places else "")


# ---------------------------------------------------------------------------
# command line
# ---------------------------------------------------------------------------

def _fmt(e) -> str:
    q = block(e)
    unc = f" +- {q['uncertainty']}" if q.get("uncertainty") else ""
    ex = " (exact)" if q.get("exact") else ""
    return f"{q.get('value')}{unc} {q.get('units', '')}{ex}".strip()


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="tp quantity", description=__doc__.split("\n\n")[0])
    ap.add_argument("action", choices=("list", "show", "users", "check"))
    ap.add_argument("id", nargs="?")
    ap.add_argument("--store", default="store")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args(argv[1:])
    if not os.path.isdir(a.store):
        print(f"tp quantity: no store at {a.store}", file=sys.stderr)
        return 2
    store = load_store(a.store)
    qs = quantities(store)
    if a.action in ("show", "users"):
        if not a.id:
            print(f"tp quantity {a.action}: give a quantity id", file=sys.stderr)
            return 2
        if a.id not in qs:
            print(f"tp quantity: {a.id} is not a quantity of this store", file=sys.stderr)
            return 2
    if a.action == "list":
        rows = [(qid, str(block(q).get("symbol", "")), _fmt(q), q.status)
                for qid, q in qs.items()]
        if a.json:
            json.dump([dict(zip(("id", "symbol", "value", "status"), r)) for r in rows],
                      sys.stdout, indent=1)
            print()
            return 0
        w = max((len(r[0]) for r in rows), default=0)
        for r in rows:
            print(f"{r[0]:<{w}}  {r[3]:<8}  {r[1]} = {r[2]}")
        print(f"{len(rows)} quantities")
        return 0
    if a.action == "show":
        q = qs[a.id]
        b = block(q)
        print(f"{a.id}  (version {q.version}, {q.status})")
        print(f"  {q.title}")
        print(f"  {b.get('symbol')} = {_fmt(q)}")
        if b.get("dimension"):
            print(f"  dimension: {b['dimension']}")
        src = b.get("source") or {}
        print(f"  source: {src.get('citation', '')}"
              + (f", {src['locator']}" if src.get("locator") else "")
              + (f", doi {src['doi']}" if src.get("doi") else "")
              + (f", {src['url']}" if src.get("url") else ""))
        if b.get("date"):
            print(f"  date: {b['date']}")
        if b.get("note"):
            print(f"  note: {b['note']}")
        print()
        print((q.levels.get("formal") or "").strip())
        _print_users(store, a.id)
        return 0
    if a.action == "users":
        if a.json:
            lit = literal_users(store, {a.id})[a.id]
            json.dump({"pinned": [r for _, r in pinned_users(store, a.id)],
                       "pinned_by": [eid for eid, _ in pinned_users(store, a.id)],
                       "literal": lit}, sys.stdout, indent=1)
            print()
            return 0
        _print_users(store, a.id)
        return 0
    # check
    from .validate import Report, layer1
    rep = Report()
    layer1(store, rep)
    by = {}
    for f in rep.findings:
        if f.entity in qs and f.severity == "error":
            by.setdefault(f.entity, []).append(f)
    n_err = n_warn = 0
    for qid, q in qs.items():
        res = check_entity(store, q, by.get(qid, ()))
        for sev, msg in res:
            print(f"{'E' if sev == 'error' else 'W'}  {qid}: {msg}")
        n_err += sum(s == "error" for s, _ in res)
        n_warn += sum(s == "warning" for s, _ in res)
    print(f"tp quantity check: {len(qs)} quantities, {n_err} error(s), {n_warn} warning(s)")
    return 1 if n_err else 0


def _print_users(store, qid):
    pins = pinned_users(store, qid)
    lit = literal_users(store, {qid})[qid]
    print(f"\npinned by {len(pins)} entit{'y' if len(pins) == 1 else 'ies'}:")
    for eid, ref in pins:
        print(f"  {eid}  ({ref})")
    unpinned = {k: v for k, v in lit.items() if k not in {e for e, _ in pins}}
    print(f"value written as a literal in {len(lit)} entit{'y' if len(lit) == 1 else 'ies'}"
          f" ({len(unpinned)} not pinning it):")
    for eid, lits in lit.items():
        mark = "" if eid in unpinned else "  [pinned]"
        print(f"  {eid}: {', '.join(lits)}{mark}")


if __name__ == "__main__":
    sys.exit(main(["quantity"] + sys.argv[1:]))
