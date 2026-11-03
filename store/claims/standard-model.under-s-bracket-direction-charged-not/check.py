"""standard-model.under-s-bracket-direction-charged-not: exact checks.

The five-mode module Lambda(C^5) (pair modes 0, 1, 2 = W, rung modes 3, 4 = R_2), exact, with
6Y = 3 N_R - 2 N_W, 2T_3 = n_3 - n_4, the colour Cartan n_0, n_1, n_2, and the invariant pairing
B (a state paired only with its complement). Checked:
(1) the two-mode states Lambda^2(R_2 + W): sectors (2,0) x 1, (1,1) x 6, (0,2) x 3 with Y = 1, 1/6,
    -2/3; their T_3 values {0}, {+-1/2} and colour weights (singlet, triplet e_i, antitriplet
    -e_i mod the trace): (1,1)_1 + (2,3)_{1/6} + (1,3bar)_{-2/3}, the 10 of SU(5) as
    e^c + Q + u^c; the slot bivector state is the e^c direction with T_3 = 0, Y = 1, charge 1;
    (a) it is not neutral: a condensate there breaks electromagnetism.
(2) (b) under U(5) (raising operators E_ab, a < b, acting on the ten mode vectors v_a -> weight
    e_a, w_a -> -e_a, extended to exterior powers), the number of highest-weight vectors of the
    weight of the 10 of SU(5) (e_1 + e_2 modulo the trace) is 0 in 10_v = Lambda^1, 1 in
    120 = Lambda^3 and 1 in Lambda^5 = 126 + 126bar (one of the two halves; which half is the
    convention of Fact standard-model.imported-spinor-bilinears and is not recomputed).
(3) (b) the couplings through the pairing on the sixteen: the 10_v and Lambda^5 couplings
    B(psi, x phi) are symmetric, the Lambda^3 (120) couplings antisymmetric, so they vanish on one
    generation (psi = phi); the 120 coupling in the bracket direction (w_0 w_1 w_2, the e^c weight
    modulo the trace) is nonzero and joins L with L, antisymmetrically. (c) follows: no one-generation mass operator from the bracket
    direction.
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

LAMBDA2_SAMPLE_MODES = list(combinations(range(NM), 2))


def colour_weight(s):
    n = [s >> m & 1 for m in PAIRS]
    t = sum(n)
    return tuple(3 * x - t for x in n)      # 3 x (colour weight minus its mean)


def check_two_mode_states_are_the_ten():
    premise("standard-model.under-s-composites-state-space-spinor")
    premise("standard-model.hyp-s-slot-statistics")
    two = [s for s in range(DIM) if bin(s).count("1") == 2]
    by = {}
    for s in two:
        y = YOP6.get((s, s), 0)
        t3 = T3OP2.get((s, s), 0)
        get_or_set(by, sector(s), []).append((y, t3, colour_weight(s)))
    ok = sorted((k, len(v)) for k, v in by.items()) == [((0, 2), 3), ((1, 1), 6), ((2, 0), 1)]
    ok = ok and {y for y, _t, _c in by[(2, 0)]} == {6} and {y for y, _t, _c in by[(1, 1)]} == {1}
    ok = ok and {y for y, _t, _c in by[(0, 2)]} == {-4}
    ok = ok and sorted(t for _y, t, _c in by[(1, 1)]) == [-1, -1, -1, 1, 1, 1]
    ok = ok and sorted({c for _y, _t, c in by[(1, 1)]}) == [(-1, -1, 2), (-1, 2, -1), (2, -1, -1)]
    ok = ok and sorted({c for _y, _t, c in by[(0, 2)]}) == [(-2, 1, 1), (1, -2, 1), (1, 1, -2)]
    ok = ok and by[(2, 0)] == [(6, 0, (0, 0, 0))]
    # (a) charge Q = T_3 + Y of the bracket direction: 6Q = 3 (2T_3) + 6Y
    s = (1 << 3) | (1 << 4)
    ok = ok and SPECIES[sector(s)] == "e^c" and 3 * T3OP2.get((s, s), 0) + YOP6.get((s, s), 0) == 6
    GA.check("Lambda^2(R_2 + W) = (1,1)_1 + (2,3)_{1/6} + (1,3bar)_{-2/3}; the bracket direction has charge 1", ok)
    return ok


# ---- U(5) on the ten mode vectors: index a < 5 is v_a (weight e_a), 5 + a is w_a (weight -e_a)

def weight_of(mon):
    w = [0] * 5
    for i in mon:
        if i < 5:
            w[i] += 1
        else:
            w[i - 5] -= 1
    return tuple(w)


def raise_vec(a, b, i):
    """E_ab on the basis vector i: v_b -> v_a, w_a -> -w_b."""
    if i == b:
        return [(a, 1)]
    if i == 5 + a:
        return [(5 + b, -1)]
    return []


def raise_mon(a, b, mon):
    out = {}
    for pos, i in enumerate(mon):
        for j, c in raise_vec(a, b, i):
            new = list(mon)
            new[pos] = j
            if len(set(new)) < len(new):
                continue
            perm = sorted(range(len(new)), key=lambda t: new[t])
            sgn = 1
            seen = list(perm)
            for x in range(len(seen)):
                for y in range(x + 1, len(seen)):
                    if seen[x] > seen[y]:
                        sgn = -sgn
            key = tuple(sorted(new))
            out[key] = out.get(key, 0) + sgn * c
    return {k: v for k, v in out.items() if v}


def highest_weight_count(r, lam):
    """Number of independent vectors of Lambda^r(C^10) whose weight is lam modulo (1,1,1,1,1)
    and which are killed by every raising operator E_ab, a < b."""
    def equiv(w):
        d = [w[i] - lam[i] for i in range(5)]
        return all(x == d[0] for x in d)
    space = [m for m in combinations(range(10), r) if equiv(weight_of(m))]
    if not space:
        return 0
    rows = {}
    for col, m in enumerate(space):
        for a in range(5):
            for b in range(a + 1, 5):
                for key, v in raise_mon(a, b, m).items():
                    get_or_set(rows, (a, b, key), [F(0)] * len(space))[col] += v
    if not rows:
        return len(space)
    return len(space) - GA.rank_of_vectors(list(rows.values()))


def check_the_ten_occurs_in_120_and_126_not_in_10v():
    premise("standard-model.imported-spinor-bilinears")
    lam = (1, 1, 0, 0, 0)
    got = [highest_weight_count(r, lam) for r in (1, 3, 5)]
    # control: the 5 (weight e_1) occurs once in 10_v, and Lambda^2 5 = 10 has its vector v_0 ^ v_1
    ok = got == [0, 1, 1] and highest_weight_count(1, (1, 0, 0, 0, 0)) == 1
    ok = ok and highest_weight_count(2, lam) == 1
    GA.check("the 10 of SU(5): absent from 10_v, once in 120 = Lambda^3, once in Lambda^5 = 126 + 126bar", ok)
    return ok


def coupling_symmetry(x):
    """(+1 symmetric, -1 antisymmetric, 0 neither or zero) for B(S, x T) on the sixteen."""
    M = mass_form(x)
    if not M:
        return 0
    if all(M.get((T, S), 0) == v for (S, T), v in M.items()):
        return 1
    if all(M.get((T, S), 0) == -v for (S, T), v in M.items()):
        return -1
    return 0


def check_120_couplings_antisymmetric_vanish_on_one_generation():
    premise("standard-model.imported-spinor-bilinears")
    premise("standard-model.mass-bracket-charged-singlet")
    ops = VOP + WOP
    sym1 = {coupling_symmetry(x) for x in ops}
    sym3 = {coupling_symmetry(mm(*[ops[i] for i in idx])) for idx in combinations(range(10), 3)
            if not any(i + 5 in idx for i in idx)}
    sym5 = {coupling_symmetry(mm(*[ops[i] for i in idx])) for idx in combinations(range(10), 5)
            if not any(i + 5 in idx for i in idx)}
    ok = sym1 == {1} and sym3 <= {-1, 0} and -1 in sym3 and sym5 <= {1, 0} and 1 in sym5
    br = mm(WOP[0], WOP[1], WOP[2])
    M = mass_form(br)
    ok = ok and coupling_symmetry(br) == -1 and bool(M)
    ok = ok and all(M.get((S, S), 0) == 0 for S in EVEN)
    pairs = {tuple(sorted([SPECIES[sector(S)], SPECIES[sector(T)]])) for (S, T) in M}
    # it joins L with L, the SU(2)-antisymmetric pair
    ok = ok and pairs == {("L", "L")}
    GA.check("10_v and Lambda^5 couplings symmetric, 120 couplings antisymmetric (zero on one generation)", ok)
    return ok
