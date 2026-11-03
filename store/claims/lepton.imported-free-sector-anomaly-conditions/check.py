"""lepton.imported-free-sector-anomaly-conditions: exact checks.

(1) The sector of a single conformal spinor, Sp = Lambda W, W = C^3, with the pair-slot factor acting as
    Lambda(lambda^-2 b): its grade-k character (U(3) weights, peeled into irreducibles against Schur
    characters) is one irreducible, 1, 3, 3b, 1 for k = 0..3, and the U(1) factor acts by lambda^(-2k):
    weight -2k, Y = -2k/6, giving (1)_0, (3)_{-1/3}, (3b)_{-2/3}, (1)_{-1}.
(2) The anomaly clause: the four sums of the imported Fact are computed by one routine; the rule that a
    fermion of the opposite handedness enters as its conjugate (conjugate representation, opposite
    hypercharge) is tested through its consequence that a vectorlike pair (a species together with the
    same species of the opposite handedness, entered as its conjugate) contributes zero to all four sums,
    for every species of (1) and for the doublets (2,3)_{1/6}, (2,1)_{-1/2}; a species entered twice in one
    handedness does not cancel. The anomaly conditions themselves are imported definitions.
The -external textbook entity is a restatement of the same Fact; no premise() call for it.
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


def grade_species(k):
    ch = Counter({((0, 0), tuple(1 if a in S else 0 for a in range(3))): 1 for S in combinations(range(3), k)})
    dec = decompose(ch)
    if len(dec) != 1 or dec[0][1] != 1:
        return None
    (lam, mu), m = dec[0]
    d2, col, q = label(lam, mu)
    weight = -2 * sum(mu)          # lambda^-2 on each occupied pair mode
    return (d2, col, F(weight, 6))


def check_free_sector_content():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    got = [grade_species(k) for k in range(4)]
    want = [(1, "1", F(0)), (1, "3", F(-1, 3)), (1, "3b", F(-2, 3)), (1, "1", F(-1))]
    ok = got == want
    ok = ok and [F(-2 * k, 6) for k in range(4)] == [y for d, c, y in want]
    GA.check("the free sector is (1)_0 + (3)_{-1/3} + (3b)_{-2/3} + (1)_{-1}, weight -2k at grade k", ok)
    return ok


def check_opposite_handedness_enters_conjugated():
    premise("standard-model.imported-anomaly-coefficients")
    species = [grade_species(k) for k in range(4)] + [(2, "3", F(1, 6)), (2, "1", F(-1, 2))]
    ok = all(anomaly_sums([sp, conj(sp)]) == (0, 0, 0, 0) for sp in species)
    # without conjugation (the same species twice in one handedness) the sums do not cancel
    ok = ok and anomaly_sums([species[1], species[1]]) == (F(-2, 3), 0, F(-2, 9), F(-2))
    ok = ok and anomaly_sums([species[5], species[5]]) == (0, -1, F(-1, 2), -2)
    GA.check("a fermion of opposite handedness enters as its conjugate: vectorlike pairs cancel", ok)
    return ok
