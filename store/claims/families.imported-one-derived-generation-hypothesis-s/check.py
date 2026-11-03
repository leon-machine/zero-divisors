"""families.imported-one-derived-generation-hypothesis-s: exact checks.

Exact U(2) x U(3) characters, peeled into irreducibles against Schur characters; abelian weight
q = 3|lam| - 2|mu|, Y = q/6.
(1) Unconditional: the pair-level generators (the cells of C^2 (x) C^3) are (2,3) with q = 1, Y = 1/6. The
    single-spinor singlets (grades k = 0..3 of Lambda C^3, weight -2k) listed in one handedness (even grades
    kept, odd conjugated) carry Y = 0, -2/3, 1/3, 1.
(2) Only under (S): the tensor ledger Lambda(C^2 (x) C^3) has no (2,1) at all, while the five-mode module of
    (S) has the lepton doublet (2,1)_{-1/2} at (j, k) = (1,3).
(3) Given the content, Y_Q = 1/6 and a fourth singlet at Y = 0 or none, the four anomaly conditions force
    Y_L = -1/2, Y_e = 1 and {Y_u, Y_d} = {-2/3, 1/3}. Both hypotheses are necessary: with a free fourth
    singlet the shifted charges Y + t (B - L) satisfy all four conditions identically in t (a cubic in t
    vanishing at 5 points), and with the doublets in the opposite handedness from the singlets the
    [SU(3)]^2 U(1) and cubic sums are -2/3 and 4/9.
(4) Chirality is the parity grading: the even and odd halves of the five-mode module carry inequivalent
    content (the odd half is the conjugate of the even one and differs from it).
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

BL = {"Q": F(1, 3), "L": F(-1), "uc": F(-1, 3), "dc": F(-1, 3), "ec": F(1), "nuc": F(1)}


def generation():
    sp = five_mode_species()
    return {"Q": sp[(1, 1)], "L": sp[(1, 3)], "uc": sp[(0, 2)], "dc": sp[(2, 2)], "ec": sp[(2, 0)],
            "nuc": sp[(0, 0)]}


def check_unconditional_content():
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    dec = decompose(cell_ledger(1))
    ok = len(dec) == 1 and label(*dec[0][0]) == (2, "3", 1) and F(label(*dec[0][0])[2], 6) == F(1, 6)
    sp = five_mode_species()
    listing = [sp[(0, k)] if k % 2 == 0 else conj(sp[(0, k)]) for k in range(4)]
    ok = ok and [y for d, c, y in listing] == [F(0), F(1, 3), F(-2, 3), F(1)]
    ok = ok and sorted(y for d, c, y in listing) == [F(-2, 3), F(0), F(1, 3), F(1)]
    GA.check("pair-level generators (2,3)_{1/6}; single-spinor singlets 0, -2/3, 1/3, 1", ok)
    return ok


def check_lepton_doublet_only_under_s():
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.quarks-leptons-two-level-fermion-content")
    ledger = [label(lam, mu) for k in range(7) for (lam, mu), m in decompose(cell_ledger(k))]
    ok = not any(d == 2 and c == "1" for d, c, q in ledger)
    sp = five_mode_species()
    ok = ok and sp[(1, 3)] == (2, "1", F(-1, 2))
    ok = ok and [jk for jk, v in sp.items() if v[:2] == (2, "1")] == [(1, 0), (1, 3)]
    GA.check("the lepton doublet exists in the five-mode module of (S) and not in the tensor ledger", ok)
    return ok


def check_uniqueness_and_necessity():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    yL, ye, s, p = solve_generation(F(1, 6))
    ok = yL == F(-1, 2) and ye == 1 and s == F(-1, 3) and p == F(-2, 9)
    ok = ok and all(t * t - s * t + p == 0 for t in (F(-2, 3), F(1, 3)))
    gen = generation()
    ok = ok and anomaly_sums(list(gen.values())) == (0, 0, 0, 0)
    # free fourth singlet: Y + t (B - L) is anomaly-free for every t (cubic in t, zero at 5 points)
    for t in (F(1), F(-2), F(1, 3), F(5, 7), F(-11, 4)):
        shifted = [(d, c, y + t * BL[n]) for n, (d, c, y) in gen.items()]
        ok = ok and anomaly_sums(shifted) == (0, 0, 0, 0)
    ok = ok and gen["nuc"][2] + F(1) * BL["nuc"] == 1
    # doublets in the opposite handedness from the singlets
    flipped = [conj(gen["Q"]), conj(gen["L"])] + [gen[n] for n in ("uc", "dc", "ec", "nuc")]
    su3, su2, cub, grav = anomaly_sums(flipped)
    ok = ok and su3 == F(-2, 3) and cub == F(4, 9)
    GA.check("the spectrum is unique given the content, Y_Q = 1/6 and the fourth singlet; both hypotheses needed", ok)
    return ok


def check_chirality_halves_inequivalent():
    premise("standard-model.chirality-two-halves-spinor-module-conjugation")
    sp = five_mode_species()
    even = Counter(v for (j, k), v in sp.items() if (j + k) % 2 == 0)
    odd = Counter(v for (j, k), v in sp.items() if (j + k) % 2 == 1)
    ok = sum(even.values()) == 6 and sum(odd.values()) == 6
    ok = ok and odd == Counter(conj(v) for v in even.elements()) and odd != even
    # already the single-spinor sector: even grades (1)_0 + (3b)_{-2/3}, odd (3)_{-1/3} + (1)_{-1}
    ok = ok and sorted([sp[(0, 0)], sp[(0, 2)]]) == [(1, "1", F(0)), (1, "3b", F(-2, 3))]
    ok = ok and sorted([sp[(0, 1)], sp[(0, 3)]]) == [(1, "1", F(-1)), (1, "3", F(-1, 3))]
    GA.check("the two chirality halves carry inequivalent (mutually conjugate) content", ok)
    return ok
