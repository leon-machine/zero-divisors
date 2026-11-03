"""standard-model.transported-frozen-point-doublet-datum-not: exact checks (DRAFT, not wired).

Written against the corrected clause (ii) proposed in the T09 report: a nonzero real rung vector
c = alpha . v + beta . w breaks the slot mixing U(2) to a U(1) exactly when beta is a multiple of
conj(alpha) (for real c: alpha and beta parallel, or one of them zero), as for the frozen point's
lift (alpha, beta) = (Lambda/3, -1) along one rung, and breaks it completely otherwise (for
example c = v_4 + w_5).

The five-mode module Lambda(C^5) (pair modes 0, 1, 2 = W, rung modes 3, 4 = the text's 4, 5),
exact. Checked:
(ii) the rung vectors carry 6Y = +3 (v) and -3 (w), 2T_3 = +-1, commute with the colour u(3); the
     su(2) raising operator v_4 w_5 carries v_5 to v_4 and w_4 to -w_5: R_2 + conj(R_2) =
     (2,1)_{1/2} + (2,1)_{-1/2}; the u(2) stabiliser of real rung vectors (real-linear algebra
     over Q(i)) has dimension 1 for the parallel samples and 0 for the others;
(iii) the 24 mixed bivectors x_W y_R change the rung and the pair number by one each, have no
     matrix element within a sector, and on the sixteen join Q to nu^c, u^c, e^c, d^c and L to u^c,
     d^c only; their expectation vanishes on every rung-sector component of sample states; through
     the bilinear pairing B the rung vectors join exactly the Yukawa pairs L nu^c, Q u^c (v) and
     L e^c, Q d^c (w).
Clause (i) (parallel sections of a flat trivial summand are the constants) has no finite content
beyond the definition and is not checked.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from pyutil import get_or_set
import fock
from tp_premise import premise

# ---------------------------------------------------------------------------
# The five-mode module Lambda(W + R_2) = Lambda(C^5), exact. States are bitmasks 0..31, mode m
# occupied when bit m is set; modes 0, 1, 2 are the pair modes (W), modes 3, 4 the rung (slot)
# modes, the text's v_4, v_5. Operators are sparse matrices {(row, col): number}; creation has the
# Jordan-Wigner sign (-1)^(occupied modes below m). Sector of a state: (j, k) = (rung number,
# pair number); 6Y = 3j - 2k. The invariant pairing B(psi, phi) pairs a state only with its
# complement.
# ---------------------------------------------------------------------------
NM, DIM, FULL = 5, 32, 31
PAIRS, SLOTS = (0, 1, 2), (3, 4)
SPECIES = {(0, 0): "nu^c", (0, 2): "u^c", (1, 1): "Q", (1, 3): "L", (2, 0): "e^c", (2, 2): "d^c"}


def nr(s):
    return sum(1 for m in SLOTS if s >> m & 1)


def nw(s):
    return sum(1 for m in PAIRS if s >> m & 1)


def sector(s):
    return (nr(s), nw(s))


mm, madd, msc, comm = fock.mm, fock.madd, fock.msc, fock.comm


ONE = fock.eye(DIM)
VOP = [fock.cre(m, NM) for m in range(NM)]  # v_m, creation
WOP = [fock.ann(m, NM) for m in range(NM)]  # w_m, annihilation
NUM = [fock.num(m, NM) for m in range(NM)]
YOP6 = madd(msc(3, madd(NUM[3], NUM[4])), msc(-2, madd(NUM[0], NUM[1], NUM[2])))   # 6Y
T3OP2 = madd(NUM[3], msc(-1, NUM[4]))                                               # 2 T_3
EVEN = [s for s in range(DIM) if (nr(s) + nw(s)) % 2 == 0]


def ad_weight(H, x):
    """The eigenvalue of ad(H) on the operator x (None if x is not an eigenvector)."""
    c = comm(H, x)
    key, v = next(iter(x.items()))
    lam = c.get(key, 0) / v
    return lam if not madd(c, msc(-lam, x)) else None


def wedge_sign(S, T):
    sgn = 1
    for i in range(NM):
        if T >> i & 1:
            sgn *= (-1) ** bin(S >> (i + 1)).count("1")
    return sgn


def bpair(S, T):
    """B on basis states: nonzero only for T the complement of S."""
    if T != FULL ^ S:
        return 0
    k = bin(S).count("1")
    return wedge_sign(S, T) * (-1) ** (k * (k - 1) // 2)


def mass_form(c):
    """M_c(S, T) = B(S, c T) on the sixteen (even states): {(S, T): value}."""
    out = {}
    for (r, t), x in c.items():
        if t in EVEN:
            S = FULL ^ r
            if S in EVEN:
                val = bpair(S, r) * x
                if val:
                    out[(S, t)] = out.get((S, t), 0) + val
    return {key: v for key, v in out.items() if v}


def species_entries(c):
    """{(species, species) sorted: set of |entry|^2} of the mass form of c."""
    out = {}
    for (S, T), val in mass_form(c).items():
        key = tuple(sorted([SPECIES[sector(S)], SPECIES[sector(T)]]))
        mag2 = val * val if not hasattr(val, "conj") else (val * val.conj()).re
        get_or_set(out, key, set()).add(mag2)
    return out

QI = GA.QI
PARALLEL = [(1, 1, 0, 0), (F(1, 30), -1, 0, 0), (0, 0, 1, 0), (2, 3, 4, 6), (0, 1, 0, 0)]
GENERIC = [(1, 0, 0, 1), (1, 2, 3, 1), (0, 1, 1, 0)]          # (alpha_4, beta_4, alpha_5, beta_5)


def rung_vector(c):
    a4, b4, a5, b5 = [F(x) for x in c]
    return madd(msc(a4, VOP[3]), msc(b4, WOP[3]), msc(a5, VOP[4]), msc(b5, WOP[4]))


def qsc(c, A):
    return {k: c * v for k, v in A.items() if c * v}


U2 = [qsc(QI(0, 1), mm(VOP[3], WOP[3])), qsc(QI(0, 1), mm(VOP[4], WOP[4])),
      madd(mm(VOP[3], WOP[4]), msc(-1, mm(VOP[4], WOP[3]))),
      qsc(QI(0, 1), madd(mm(VOP[3], WOP[4]), mm(VOP[4], WOP[3])))]


def stabiliser_dim(c):
    cols = [comm(X, c) for X in U2]
    keys = sorted({k for cm in cols for k in cm})
    rows = []
    for k in keys:
        rows.append([QI(cm.get(k, 0)).re for cm in cols])
        rows.append([QI(cm.get(k, 0)).im for cm in cols])
    return len(U2) - GA.rank_of_vectors(rows)


def check_rung_plane_is_two_conjugate_doublets():
    premise("standard-model.under-s-composites-state-space-spinor")
    ok = [ad_weight(YOP6, x) for x in (VOP[3], VOP[4], WOP[3], WOP[4])] == [3, 3, -3, -3]
    ok = ok and [ad_weight(T3OP2, x) for x in (VOP[3], VOP[4], WOP[3], WOP[4])] == [1, -1, -1, 1]
    su3 = [mm(VOP[a], WOP[b]) for a in PAIRS for b in PAIRS]
    ok = ok and all(not comm(E, x) for E in su3 for x in (VOP[3], VOP[4], WOP[3], WOP[4]))
    E45 = mm(VOP[3], WOP[4])
    ok = ok and comm(E45, VOP[4]) == VOP[3] and comm(E45, WOP[3]) == msc(-1, WOP[4])
    ok = ok and not comm(E45, VOP[3]) and not comm(E45, WOP[4])
    GA.check("R_2 + conj(R_2) = (2,1)_{1/2} + (2,1)_{-1/2}, colour singlets", ok)
    return ok


def check_real_rung_vector_stabiliser():
    premise("standard-model.under-s-composites-state-space-spinor")
    ok = all(stabiliser_dim(rung_vector(c)) == 1 for c in PARALLEL)
    ok = ok and all(stabiliser_dim(rung_vector(c)) == 0 for c in GENERIC)
    GA.check("a real rung vector leaves a U(1) iff beta is parallel to alpha; otherwise nothing", ok)
    return ok


def check_mixed_bivectors_join_sectors_off_diagonal():
    premise("standard-model.grip-mass-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    pair_vecs = VOP[:3] + WOP[:3]
    rung_vecs = [VOP[3], VOP[4], WOP[3], WOP[4]]
    mixed = [mm(x, y) for x in pair_vecs for y in rung_vecs]
    ok = len(mixed) == 24
    links = set()
    for X in mixed:
        for (r, c) in X:
            (jr, kr), (jc, kc) = sector(r), sector(c)
            ok = ok and abs(jr - jc) == 1 and abs(kr - kc) == 1
            if (jr + kr) % 2 == 0:
                links.add(tuple(sorted([SPECIES[(jr, kr)], SPECIES[(jc, kc)]])))
    want = {("Q", "nu^c"), ("Q", "u^c"), ("Q", "e^c"), ("Q", "d^c"), ("L", "u^c"), ("L", "d^c")}
    ok = ok and links == {tuple(sorted(p)) for p in want}
    for seed in (6, 7):
        psi = [QI(F((seed * (s + 3)) % 7 - 3, 2), F((seed * (s + 5)) % 5 - 2, 3)) for s in range(DIM)]
        for j in range(3):
            pj = [psi[s] if nr(s) == j else QI(0) for s in range(DIM)]
            for X in mixed:
                val = QI(0)
                for (r, c), x in X.items():
                    val = val + pj[r].conj() * pj[c] * x
                ok = ok and val == QI(0)
    GA.check("(iii) mixed bivectors change (j, k) by one each; links Q-singlets and L-u^c, d^c only", ok)
    return ok


def check_bilinear_pairing_joins_yukawa_pairs():
    premise("standard-model.hyp-s-slot-statistics")
    up = set().union(*[set(species_entries(x)) for x in (VOP[3], VOP[4])])
    down = set().union(*[set(species_entries(x)) for x in (WOP[3], WOP[4])])
    ok = up == {("L", "nu^c"), ("Q", "u^c")} and down == {("L", "e^c"), ("Q", "d^c")}
    GA.check("through the pairing the rung vectors join exactly the Yukawa pairs", ok)
    return ok
