"""dark-matter.imported-derived-generation-flag: exact checks.

Computable parts of an imported Fact that restates several series results.
(1) Witt decomposition of the complexified conformal ambient, in GA Cl(2,4) (e_0, e_1 square +1, e_2..e_5
    square -1) with Q(i) coefficients (GA.QI): v_1, w_1 = (e_0 + e_2)/2, (e_0 - e_2)/2 and v_2, w_2 =
    (e_1 + e_3)/2, (e_1 - e_3)/2 are real null pairs (v.v = w.w = 0, v.w = 1/2) spanning two real
    hyperbolic planes; their orthogonal complement span(e_4, e_5) has Gram signature (0, 2, 0) (congruence),
    so it contains no real null vector, and the real Witt index of R^{2,4} is min(2, 4) = 2 (Gram signature
    (2, 4, 0)): no third real pair exists. Over C, v_3 = (e_4 + i e_5)/2, w_3 = -(e_4 - i e_5)/2 is a null
    pair with v_3.w_3 = 1/2, and the three pairs are mutually orthogonal and span V_C (rank 6 over Q(i)).
(2) The listing choice: the derived generation (five-mode module, even total mode number) and the opposite
    listing (odd half) are each other's conjugates, so choosing one handedness is choosing the
    particle-antiparticle orientation; species read from exact characters with Y = (3j - 2k)/6.
The condensate alignment (a citation of T13) and the reading of the listing choice as the descent's flag
(a definition of this paper) have no computable content here.
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

QI = GA.QI
S24 = GA.sig(2, 4)


def vec(coeffs):
    return {(i,): QI(c) if not isinstance(c, QI) else c for i, c in coeffs.items() if c}


def dot(x, y):
    return GA.dot(x, y, S24)


def check_witt_decomposition_two_real_one_complex():
    premise("correspondence.twistors-are-states-three-ladder-pairs")
    premise("correspondence.fock-model-complexified-ascended-algebra")
    h = F(1, 2)
    pairs = [(vec({0: h, 2: h}), vec({0: h, 2: -h})), (vec({1: h, 3: h}), vec({1: h, 3: -h})),
             (vec({4: QI(h), 5: QI(0, h)}), vec({4: QI(-h), 5: QI(0, h)}))]
    ok = True
    for a, (v, w) in enumerate(pairs):
        ok = ok and dot(v, v) == 0 and dot(w, w) == 0 and dot(v, w) == h
        for b, (v2, w2) in enumerate(pairs):
            if a != b:
                ok = ok and all(dot(x, y) == 0 for x in (v, w) for y in (v2, w2))
    # the first two pairs are real
    ok = ok and all(c.im == 0 for v, w in pairs[:2] for x in (v, w) for c in x.values())
    ok = ok and any(c.im != 0 for c in pairs[2][0].values())
    rows = [[x.get((i,), QI(0)) for i in range(6)] for v, w in pairs for x in (v, w)]
    ok = ok and GA.field_rank(rows) == 6
    gram = [[GA.dot(GA.gen(i), GA.gen(j), S24) for j in range(6)] for i in range(6)]
    ok = ok and GA.congruence_signature(gram) == (2, 4, 0)
    comp = [[GA.dot(GA.gen(i), GA.gen(j), S24) for j in (4, 5)] for i in (4, 5)]
    ok = ok and GA.congruence_signature(comp) == (0, 2, 0)
    # the complement is orthogonal to both real planes
    ok = ok and all(dot(vec({c: 1}), x) == 0 for c in (4, 5) for v, w in pairs[:2] for x in (v, w))
    GA.check("three Witt pairs of V_C: two real hyperbolic planes of R^{2,4}, the third only complex", ok)
    return ok


def check_listing_choice_is_particle_antiparticle():
    premise("standard-model.chirality-two-halves-spinor-module-conjugation")
    premise("standard-model.hyp-s-slot-statistics")
    sp = five_mode_species()
    even = Counter(v for (j, k), v in sp.items() if (j + k) % 2 == 0)
    odd = Counter(v for (j, k), v in sp.items() if (j + k) % 2 == 1)
    gen = Counter([(2, "3", F(1, 6)), (2, "1", F(-1, 2)), (1, "3b", F(-2, 3)), (1, "3b", F(1, 3)),
                   (1, "1", F(1)), (1, "1", F(0))])
    ok = even == gen and odd == Counter(conj(v) for v in gen.elements()) and odd != even
    GA.check("the two listings are the generation and its conjugate: the particle-antiparticle choice", ok)
    return ok
