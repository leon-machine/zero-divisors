"""rungs.imported-results-t12-used-registration: exact checks.

Exact U(2) x U(3) characters peeled into irreducibles (Schur characters); abelian weight q = 3|lam| - 2|mu|,
Y = q/6; species of the derived generation at (j, k) (j slots, k pairs): nu^c (0,0), u^c (0,2), Q (1,1),
L (1,3), e^c (2,0), d^c (2,2).
(1) The slot factor Lambda^2 C^2 of the mass bracket is (1,1)_1; the five-mode component (2,0) is the same.
(2) Given the content, Y_Q = 1/6 and a fourth singlet at 0 or absent, the anomaly conditions fix the
    spectrum ({Y_u, Y_d} = {-2/3, 1/3}); with a free fourth singlet Y + t (B - L) is anomaly-free for every t
    (a cubic in t vanishing at 5 points).
(3) sin^2 theta_W = tr T_3^2 / tr Q^2 is 3/8 over the derived generation and 9/26 over the quark doublet and
    singlets, computed state by state. With the inputs of the spectrum run (alpha_em^-1 = 128,
    sin^2 = 0.2312, alpha_s = 0.118 = 59/500, b = (41/10, -19/6, -7)) the three pairwise meeting points
    x_ij = (a_i - a_j)/(b_i - b_j) are three different rationals, and the unification condition predicts
    sin^2 theta_W = 78761/379488, not 0.2312: the desert does not meet.
(4) Untwisted, the generator alpha j + beta k has [SU(3)]^2 U(1), [SU(2)]^2 U(1), gravitational sums
    2(2a + 3b), 2(2a + 3b), 8(2a + 3b) (zero only on the hypercharge line (3, -2)); twisted by det^-1/2
    (charge alpha j + beta k - (2 alpha + 3 beta)/2) all four sums and the mixed Y^2 X, Y X^2 vanish
    identically (linear forms at 3 points, the binary quadratic and cubic forms at 4 and 5 pairwise
    non-proportional points). X = j + k - 5/2 is the twisted total mode number; on one mode
    n - 1/2 = (1/2)(v + w)(w - v), a Majorana bilinear, so X lies in so(10): U(1)_X. The Majorana term
    nu^c nu^c has X = -5 and Y = 0, so it breaks U(1)_X and keeps hypercharge (the breaking of Pati-Salam
    to the determinant-one part is Proposition standard-model.majorana-element, checked there).
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

SPECIES_AT = {"nuc": (0, 0), "uc": (0, 2), "Q": (1, 1), "L": (1, 3), "ec": (2, 0), "dc": (2, 2)}
SAMPLES_AB = [(F(1), F(0)), (F(0), F(1)), (F(1), F(1)), (F(2), F(-5)), (F(-3, 2), F(7, 3))]
T_SAMPLES = (F(1), F(-2), F(1, 3), F(5, 7), F(-11, 4))


def generation():
    sp = five_mode_species()
    return {n: sp[jk] for n, jk in SPECIES_AT.items()}


def traces(names, gen):
    t3, q2 = F(0), F(0)
    for n in names:
        d2, col, y = gen[n]
        for m in range(d2):
            T3 = F(d2 - 1, 2) - m
            t3 += NCOL[col] * T3 * T3
            q2 += NCOL[col] * (T3 + y) ** 2
    return t3, q2


def sums_for(charge):
    """Four anomaly sums of the derived generation for a charge function of (j, k)."""
    gen = generation()
    return anomaly_sums([(d, c, charge(*SPECIES_AT[n])) for n, (d, c, y) in gen.items()])


def check_mass_bracket_slot_factor():
    premise("standard-model.mass-bracket-charged-singlet")
    premise("standard-model.hyp-s-slot-statistics")
    dec = decompose(Counter({((1, 1), (0, 0, 0)): 1}))
    lab = label(*dec[0][0])
    ok = len(dec) == 1 and (lab[0], lab[1], F(lab[2], 6)) == (1, "1", F(1))
    ok = ok and five_mode_species()[(2, 0)] == (1, "1", F(1))
    GA.check("the mass bracket's slot factor is (1,1)_1, the five-mode state at (2,0)", ok)
    return ok


def check_hypercharge_unique_and_family():
    premise("standard-model.hypercharge-global-form-pair-counting-consistency")
    yL, ye, s, p = solve_generation(F(1, 6))
    ok = (yL, ye, s, p) == (F(-1, 2), F(1), F(-1, 3), F(-2, 9))
    ok = ok and all(t * t - s * t + p == 0 for t in (F(-2, 3), F(1, 3)))
    gen = generation()
    bl = {n: 1 - F(2, 3) * SPECIES_AT[n][1] for n in gen}
    ok = ok and bl == {"nuc": 1, "uc": F(-1, 3), "Q": F(1, 3), "L": -1, "ec": 1, "dc": F(-1, 3)}
    for t in T_SAMPLES:
        ok = ok and anomaly_sums([(d, c, y + t * bl[n]) for n, (d, c, y) in gen.items()]) == (0, 0, 0, 0)
    GA.check("unique hypercharges given the fourth singlet; Y + t(B - L) when it is free", ok)
    return ok


def check_weak_angle_and_desert():
    premise("standard-model.weak-angle-over-derived-generation")
    premise("standard-model.spectrum-run")
    gen = generation()
    t3, q2 = traces(list(gen), gen)
    ok = t3 / q2 == F(3, 8)
    t3b, q2b = traces(["Q", "uc", "dc", "ec", "nuc"], gen)
    ok = ok and t3b / q2b == F(9, 26)
    A, s2, a3 = F(128), F(2312, 10000), F(500, 59)
    a2 = s2 * A
    a1 = F(3, 5) * (A - a2)
    a = (a1, a2, a3)
    b = (F(41, 10), F(-19, 6), F(-7))
    x = {(i, j): (a[i] - a[j]) / (b[i] - b[j]) for i in range(3) for j in range(i + 1, 3)}
    ok = ok and len(set(x.values())) == 3 and all(v > 0 for v in x.values())
    r0 = (b[0] - b[1]) / (b[1] - b[2])
    a2u = (F(3, 5) * A + r0 * a3) / (F(8, 5) + r0)
    ok = ok and a2u / A == F(78761, 379488) and a2u / A != s2 and s2 - a2u / A > F(2, 100)
    GA.check("sin^2 = 3/8 over the generation (9/26 without L); the desert run does not meet", ok)
    return ok


def check_abelian_generators_twisted_and_untwisted():
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.majorana-element")
    ok = True
    for al, be in SAMPLES_AB:
        su3, su2, cub, grav = sums_for(lambda j, k: al * j + be * k)
        L = 2 * al + 3 * be
        ok = ok and (su3, su2, grav) == (2 * L, 2 * L, 8 * L)
    ok = ok and sums_for(lambda j, k: F(j + k)) == (10, 10, 400, 40)
    ok = ok and sums_for(lambda j, k: F(j - k)) == (-2, -2, -32, -8)
    ok = ok and sums_for(lambda j, k: F(3 * j - 2 * k, 6)) == (0, 0, 0, 0)
    gen = generation()
    for al, be in SAMPLES_AB:
        tw = lambda j, k: al * j + be * k - (2 * al + 3 * be) / 2
        ok = ok and sums_for(tw) == (0, 0, 0, 0)
        mixed1 = sum((d * NCOL[c] * y * y * tw(*SPECIES_AT[n]) for n, (d, c, y) in gen.items()), F(0))
        mixed2 = sum((d * NCOL[c] * y * tw(*SPECIES_AT[n]) ** 2 for n, (d, c, y) in gen.items()), F(0))
        ok = ok and mixed1 == 0 and mixed2 == 0
    # X = j + k - 5/2 is the twisted total mode number; one mode: n - 1/2 = (1/2)(v + w)(w - v)
    X = {n: F(sum(SPECIES_AT[n]), 1) - F(5, 2) for n in gen}
    ok = ok and X == {"nuc": F(-5, 2), "uc": F(-1, 2), "Q": F(-1, 2), "L": F(3, 2), "ec": F(-1, 2), "dc": F(3, 2)}
    v, w = [[0, 0], [1, 0]], [[0, 1], [0, 0]]
    vw = [[v[i][j] + w[i][j] for j in range(2)] for i in range(2)]
    wv = [[w[i][j] - v[i][j] for j in range(2)] for i in range(2)]
    prod = [[F(sum(vw[i][k] * wv[k][j] for k in range(2)), 2) for j in range(2)] for i in range(2)]
    ok = ok and prod == [[F(-1, 2), 0], [0, F(1, 2)]]
    # the Majorana bilinear nu^c nu^c: X = -5 (broken) while Y = 0 (kept)
    ok = ok and 2 * X["nuc"] == -5 and 2 * gen["nuc"][2] == 0
    GA.check("untwisted: only hypercharge passes the linear conditions; twisted: all anomaly-free; U(1)_X", ok)
    return ok
