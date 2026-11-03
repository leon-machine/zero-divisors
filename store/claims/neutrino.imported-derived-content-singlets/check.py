"""neutrino.imported-derived-content-singlets: exact checks.

Exact U(2) x U(3) characters, peeled into irreducibles against Schur characters; the abelian weight is
q = 3|lam| - 2|mu| (the action (lambda^3 a, lambda^-2 b)) and Y = q/6.
(1) Fermion content: on the five-mode module of Hypothesis (S) the doublets are (j, k) = (1,1) = (2,3)_{1/6}
    and (1,3) = (2,1)_{-1/2} on the even half (the other doublets, (1,0) and (1,2), are their conjugates
    on the odd half).
(2) The sector of a single conformal spinor, the row j = 0: grade k is Lambda^k C^3 = 1, 3, 3b, 1 with
    weight -2k and Y = -k/3 = 0, -1/3, -2/3, -1. Listed by the handedness that keeps the even grades and
    conjugates the odd ones: (1)_0 + (3b)_{-2/3} + (3b)_{+1/3} + (1)_{+1}, the hypercharge-zero singlet at
    grade zero.
(3) The four anomaly sums vanish on Q, L and these singlets; and given the content, Y_Q = 1/6 and a fourth
    singlet at Y = 0 or none, the conditions force Y_L = -1/2, Y_e = 1, and Y_u + Y_d = -1/3,
    Y_u Y_d = -2/9, so {Y_u, Y_d} = {-2/3, 1/3} as an unordered pair (the roots of t^2 + t/3 - 2/9).
(4) The Z_6 lattice: every representation of the derived content satisfies 2t + 3 delta + q = 0 mod 6
    (t the triality, delta = 1 on doublets), computed from its weights; a fractionally charged colour
    singlet such as (1,1)_{1/6} is off the lattice.
"""
from collections import Counter
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Exact characters of U(2) x U(3): a representation is a Counter of weights
# ((a1, a2), (b1, b2, b3)); irreducibles are products of Schur characters,
# computed by enumerating semistandard tableaux. Decomposition peels the
# lexicographically largest weight, which is always a highest weight.
# ---------------------------------------------------------------------------


def ssyt(shape, n):
    """Content vectors of the semistandard tableaux of the given shape with entries 0..n-1."""
    cells = [(r, c) for r, row in enumerate(shape) for c in range(row)]
    out = Counter()

    def fill(i, T):
        if i == len(cells):
            cont = [0] * n
            for v in T.values():
                cont[v] += 1
            out[tuple(cont)] += 1
            return
        r, c = cells[i]
        lo = 0
        if c > 0:
            lo = max(lo, T[(r, c - 1)])
        if r > 0:
            lo = max(lo, T[(r - 1, c)] + 1)
        for v in range(lo, n):
            T[(r, c)] = v
            fill(i + 1, T)
            del T[(r, c)]

    fill(0, {})
    return out


def schur(hw, n):
    """Character of the U(n) irreducible with highest weight hw (entries may be negative)."""
    m = min(hw)
    shape = [h - m for h in hw]
    ch = ssyt([s for s in shape if s > 0], n)
    return Counter({tuple(x + m for x in w): c for w, c in ch.items()})


def irr_char(lam, mu):
    a, b = schur(lam, 2), schur(mu, 3)
    return Counter({(wa, wb): ca * cb for wa, ca in a.items() for wb, cb in b.items()})


def decompose(ch):
    """List of ((lam, mu), multiplicity) for a U(2) x U(3) character."""
    ch = Counter({k: v for k, v in ch.items() if v})
    out = []
    while ch:
        top = max(ch)
        m = ch[top]
        if m < 0:
            return None
        out.append((top, m))
        ch.subtract(Counter({k: m * v for k, v in irr_char(*top).items()}))
        ch = Counter({k: v for k, v in ch.items() if v})
    return out


SU3_NAME = {(0, 0): "1", (1, 0): "3", (0, 1): "3b", (2, 0): "6", (0, 2): "6b", (1, 1): "8",
            (3, 0): "10", (0, 3): "10b"}


def label(lam, mu):
    """(SU(2) dimension, SU(3) name, abelian weight q = 3|lam| - 2|mu|)."""
    return (lam[0] - lam[1] + 1, SU3_NAME[(mu[0] - mu[1], mu[1] - mu[2])], 3 * sum(lam) - 2 * sum(mu))


def cell_ledger(k):
    """Character of Lambda^k(C^2 (x) C^3): cells (i, a), weight = (row counts, column counts)."""
    cells = [(i, a) for i in range(2) for a in range(3)]
    ch = Counter()
    for S in combinations(cells, k):
        u2 = tuple(sum(1 for (i, a) in S if i == r) for r in range(2))
        u3 = tuple(sum(1 for (i, a) in S if a == c) for c in range(3))
        ch[(u2, u3)] += 1
    return ch


def five_mode(j, k):
    """Character of Lambda^j C^2 (x) Lambda^k C^3 (j slots, k pairs)."""
    ch = Counter()
    for S in combinations(range(2), j):
        for T in combinations(range(3), k):
            ch[(tuple(1 if r in S else 0 for r in range(2)), tuple(1 if c in T else 0 for c in range(3)))] += 1
    return ch


CONJ = {"1": "1", "3": "3b", "3b": "3", "6": "6b", "6b": "6", "8": "8"}
NCOL = {"1": 1, "3": 3, "3b": 3, "6": 6, "6b": 6, "8": 8}


def conj(sp):
    d2, col, y = sp
    return (d2, CONJ[col], -y)


def anomaly_sums(species):
    """The four sums of the imported anomaly Fact over left-handed species (d2, colour, Y):
    [SU(3)]^2 U(1) over colour (anti)triplets weighted by SU(2) multiplicity, [SU(2)]^2 U(1) over
    doublets weighted by colour multiplicity, U(1)^3, gravitational."""
    su3 = sum((d2 * y for d2, col, y in species if col in ("3", "3b")), F(0))
    su2 = sum((NCOL[col] * y for d2, col, y in species if d2 == 2), F(0))
    cub = sum((d2 * NCOL[col] * y ** 3 for d2, col, y in species), F(0))
    grav = sum((d2 * NCOL[col] * y for d2, col, y in species), F(0))
    return (su3, su2, cub, grav)


def five_mode_species():
    """(j, k) -> (SU(2) dim, colour, Y) of the five-mode module, read from its characters."""
    out = {}
    for j in range(3):
        for k in range(4):
            dec = decompose(five_mode(j, k))
            (lam, mu), m = dec[0]
            d2, col, q = label(lam, mu)
            out[(j, k)] = (d2, col, F(q, 6)) if len(dec) == 1 and m == 1 else None
    return out


def solve_generation(yQ):
    """Solve the four anomaly conditions for (Y_L, Y_e, s = Y_u + Y_d, p = Y_u Y_d) given Y_Q and the
    content Q (2,3), L (2,1), u^c, d^c (1,3b), e^c (1,1), and nu^c (1,1) at Y = 0 or absent (the two
    give the same equations, nu^c contributing 0 to every sum)."""
    yL = -3 * yQ                                   # [SU(2)]^2 U(1): 3 Y_Q + Y_L = 0
    s = -2 * yQ                                    # [SU(3)]^2 U(1): 2 Y_Q + Y_u + Y_d = 0
    ye = -(6 * yQ + 2 * yL + 3 * s)                # gravitational (the nu^c term is 0 either way)
    rest = 6 * yQ ** 3 + 2 * yL ** 3 + ye ** 3     # U(1)^3: rest + 3 (Y_u^3 + Y_d^3) = 0
    cubes = -rest / 3                              # Y_u^3 + Y_d^3 = s^3 - 3 s p
    p = (s ** 3 - cubes) / (3 * s)
    return yL, ye, s, p


def triality(col):
    return {"1": 0, "3": 1, "3b": 2, "6": 2, "6b": 1, "8": 0}[col]


# sample representations off the Z_6 lattice: a fractionally charged colour singlet (1,1)_{1/6} and a
# doublet triplet at the wrong hypercharge (2,3)_{-1/3}
OFF_LATTICE = ((1, "1", F(1, 6)), (2, "3", F(-1, 3)))
# the (SU(2) dimension, colour) cases over which the index of the lattice is checked
LATTICE_CASES = tuple((d2, col) for d2 in (1, 2) for col in ("1", "3", "3b"))


def on_lattice(sp):
    d2, col, y = sp
    q = 6 * y
    return q.denominator == 1 and (2 * triality(col) + 3 * (1 if d2 == 2 else 0) + q.numerator) % 6 == 0


def singlet_listing():
    sp = five_mode_species()
    return [sp[(0, k)] if k % 2 == 0 else conj(sp[(0, k)]) for k in range(4)]


def check_doublet_content():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.raw-representation-content-state-space")
    sp = five_mode_species()
    ok = None not in sp.values()
    even_doublets = sorted(((j, k), v) for (j, k), v in sp.items() if v[0] == 2 and (j + k) % 2 == 0)
    ok = ok and even_doublets == [((1, 1), (2, "3", F(1, 6))), ((1, 3), (2, "1", F(-1, 2)))]
    odd_doublets = sorted(v for (j, k), v in sp.items() if v[0] == 2 and (j + k) % 2 == 1)
    ok = ok and odd_doublets == sorted(conj(v) for _, v in even_doublets)
    GA.check("the content is (2,3) + (2,1), the doublets of the five-mode module", ok)
    return ok


def check_single_spinor_singlets():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    sp = five_mode_species()
    row = [sp[(0, k)] for k in range(4)]
    ok = row == [(1, "1", F(0)), (1, "3", F(-1, 3)), (1, "3b", F(-2, 3)), (1, "1", F(-1))]
    ok = ok and all(row[k][2] == F(-k, 3) for k in range(4))
    listing = singlet_listing()
    ok = ok and listing == [(1, "1", F(0)), (1, "3b", F(1, 3)), (1, "3b", F(-2, 3)), (1, "1", F(1))]
    ok = ok and listing[0][2] == 0
    GA.check("single-spinor singlets: Y = -k/3; even-grade listing nu^c, u^c, d^c, e^c", ok)
    return ok


def check_anomaly_conditions_hold_and_determine():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    sp = five_mode_species()
    content = [sp[(1, 1)], sp[(1, 3)]] + singlet_listing()
    ok = anomaly_sums(content) == (0, 0, 0, 0)
    ok = ok and anomaly_sums([s for s in content if s != (1, "1", F(0))]) == (0, 0, 0, 0)
    yL, ye, s, p = solve_generation(F(1, 6))
    ok = ok and yL == F(-1, 2) and ye == 1 and s == F(-1, 3) and p == F(-2, 9)
    # the quadratic t^2 - s t + p has exactly the roots -2/3 and 1/3
    roots = [F(-2, 3), F(1, 3)]
    ok = ok and roots[0] + roots[1] == s and roots[0] * roots[1] == p
    ok = ok and all(t * t - s * t + p == 0 for t in roots)
    GA.check("the anomaly conditions hold and fix the singlet spectrum up to u^c <-> d^c", ok)
    return ok


def check_z6_lattice():
    premise("standard-model.global-form-quotient-determined")
    sp = five_mode_species()
    ok = all(on_lattice(v) for v in sp.values())
    ok = ok and len(sp) == 12
    ok = ok and not any(on_lattice(r) for r in OFF_LATTICE)
    # the condition cuts out an index-6 lattice: for each SU(2) dimension and colour (triality 0, 1, 2),
    # exactly one q = 6Y in each period of six is allowed
    ok = ok and all(sum(on_lattice((d2, col, F(q, 6))) for q in range(6)) == 1 for d2, col in LATTICE_CASES)
    GA.check("the representations of the derived content lie on the Z_6 lattice", ok)
    return ok
