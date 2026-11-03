"""standard-model.reduction: exact checks of clauses (1) to (3) and of the freedom in (4).

The five-mode module Lambda(C^5) (pair modes 0, 1, 2, rung modes 3, 4), exact; species by sector
(j, k) = (rung number, pair number) under (S); Gaussian-rational two-spinors for the slot
components' spinor parts, with the grip momentum of Theorem standard-model.grip-mass-two-rung-module
(one null momentum pi pi-bar per slot component, m^2 = 2 det of the sum). Checked:
(1) in the six-number order (nu^c, u^c, Q, L, e^c, d^c) of Proposition
    standard-model.invariant-operators-module the number of slot components is (1, 1, 2, 2, 1, 1),
    read off the module; the mass form is exactly zero on the four slot singlets for every spinor
    sample and the area 2 |[pi^1 pi^2]|^2 on Q and L, taking different values on different states
    (state-dependent, a form and not a number); it is invariant under unitary slot mixing of the
    components (|det A| = 1), while no nonzero vector of V_C has zero weight under the pair mixing
    u(3) (Proposition standard-model.frozen-point-pair-mixing), so the frozen point is not pair
    invariant;
(2) over all sectors the mass is supported exactly on the slot doublets j = 1, the inverse of the
    demanded split for every multiplet cut along the slot/pair line;
(3) the bracket direction, the slot bivector state, has charge T_3 + Y = 1 and transforms by
    det(A) under the slot mixing; its only coupling of two sixteens through the pairing B (the 120
    direction w_0 w_1 w_2 of its weight) is antisymmetric, so it vanishes on one generation;
(4) the six species projectors commute with s(u(2) + u(3)) on the sixteen and are independent:
    six free numbers, which (1) to (3) leave undetermined except as computed above.
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
# ---------------------------------------------------------------------------
# Two-component spinors over Q(i) (GA.QI): the momentum of a single conformal spinor is
# p_{AA'} = pi_A conj(pi_A'), a 2x2 Hermitian matrix with p^2 = 2 det p (the convention of the
# grip Fact); the slot bracket [pi^1 pi^2] = det(pi^i_A).
# ---------------------------------------------------------------------------
QI = GA.QI


def momentum(pi):
    return [[pi[a] * pi[b].conj() for b in range(2)] for a in range(2)]


def msum(ps):
    out = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for p in ps:
        out = [[out[a][b] + p[a][b] for b in range(2)] for a in range(2)]
    return out


def mass2(ps):
    """m^2 = 2 det(sum p), a real number (a Fraction) for Hermitian momenta."""
    P = msum(ps)
    m = 2 * (P[0][0] * P[1][1] - P[0][1] * P[1][0])
    assert m.im == 0
    return m.re


def bracket(p1, p2):
    return p1[0] * p2[1] - p1[1] * p2[0]


def absq(z):
    return z * z.conj()


def mix(A, pis):
    """Slot mixing of the components: pi'_a = sum_b A_ab pi_b."""
    return [[sum((A[a][b] * pis[b][i] for b in range(len(pis))), QI(0)) for i in range(2)]
            for a in range(len(pis))]

ORDER = ["nu^c", "u^c", "Q", "L", "e^c", "d^c"]
SPINORS = [[QI(1, 0), QI(0, 1)], [QI(2, -1), QI(1, 1)], [QI(0, 3), QI(-1, 2)],
           [QI(F(1, 2), 0), QI(F(3, 2), -1)], [QI(-1, 1), QI(4, 0)]]
UNITARY = [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]]


def sector_of(name):
    return next(sec for sec, nm in SPECIES.items() if nm == name)


def n_components(sec):
    return len({s >> 3 for s in range(DIM) if sector(s) == sec})


def masses(ncomp):
    return [mass2([momentum(SPINORS[i]) for i in idx]) for idx in combinations(range(len(SPINORS)), ncomp)]


def check_six_numbers_zero_on_singlets_area_on_doublets():
    premise("standard-model.grip-mass-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    premise("standard-model.moment-map-grip-mass-are-insensitive")
    premise("standard-model.imported-grip-area-casimir-form")
    counts = [n_components(sector_of(nm)) for nm in ORDER]
    ok = counts == [1, 1, 2, 2, 1, 1]
    ok = ok and (len(ORDER) == len(counts) and all(set(masses(c)) == {F(0)} for nm, c in zip(ORDER, counts) if c == 1))
    dbl = masses(2)
    ok = ok and all(m > 0 for m in dbl) and len(set(dbl)) > 1
    for a, b in combinations(SPINORS, 2):
        ok = ok and mass2([momentum(a), momentum(b)]) == 2 * absq(bracket(a, b))
        a2, b2 = mix(UNITARY, [a, b])
        ok = ok and mass2([momentum(a2), momentum(b2)]) == mass2([momentum(a), momentum(b)])
        ok = ok and msum([momentum(a2), momentum(b2)]) == msum([momentum(a), momentum(b)])
    GA.check("(1) the six numbers (0, 0, m_Q, m_L, 0, 0): exact zeros, area forms on Q and L, slot-mixing invariant", ok)
    return ok


def check_frozen_point_not_pair_invariant():
    premise("standard-model.frozen-point-pair-mixing")
    cartan = [NUM[0], NUM[1], NUM[2]]
    wts = sorted(tuple(ad_weight(H, x) for H in cartan) for x in VOP[:3] + WOP[:3])
    ok = wts == sorted([(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)])
    GA.check("(1) the pair vectors have nonzero u(3) weights: no frozen point in V is pair invariant", ok)
    return ok


def check_inverse_split_on_every_multiplet():
    premise("standard-model.under-s-frozen-points-split-inverse")
    premise("standard-model.grip-mass-two-rung-module")
    secs = sorted({sector(s) for s in range(DIM)})
    massive = [sec for sec in secs if any(m != 0 for m in masses(n_components(sec)))]
    ok = len(secs) == 12 and massive == [(1, 0), (1, 1), (1, 2), (1, 3)]
    GA.check("(2) the frozen-point mass is supported exactly on the slot doublets in every multiplet", ok)
    return ok


def check_bracket_charged_and_no_one_generation_operator():
    premise("standard-model.under-s-bracket-direction-charged-not")
    premise("standard-model.mass-bracket-charged-singlet")
    s = (1 << 3) | (1 << 4)
    ok = SPECIES[sector(s)] == "e^c" and 3 * T3OP2.get((s, s), 0) + YOP6.get((s, s), 0) == 6
    # under the slot mixing the bivector v_3 v_4 goes to det(A) v_3 v_4
    A = UNITARY
    vp = [madd(msc(A[0][a], VOP[3]), msc(A[1][a], VOP[4])) for a in range(2)]
    det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    ok = ok and mm(vp[0], vp[1]) == msc(det, mm(VOP[3], VOP[4])) and det * det.conj() == QI(1)
    M = mass_form(mm(WOP[0], WOP[1], WOP[2]))
    ok = ok and bool(M) and all(M.get((T, S), 0) == -v for (S, T), v in M.items())
    ok = ok and all(M.get((S, S), 0) == 0 for S in EVEN)
    GA.check("(3) the bracket direction has charge 1, transforms by det, couples antisymmetrically", ok)
    return ok


def check_six_free_numbers():
    premise("standard-model.invariant-operators-module")
    gens = [mm(VOP[a], WOP[b]) for a in SLOTS for b in SLOTS] + [mm(VOP[a], WOP[b]) for a in PAIRS for b in PAIRS]
    proj = {}
    for s in EVEN:
        get_or_set(proj, SPECIES[sector(s)], {})[(s, s)] = F(1)
    ev = set(EVEN)
    ok = sorted(proj) == sorted(ORDER)
    for P in proj.values():
        for X in gens:
            Xe = {k: v for k, v in X.items() if k[0] in ev and k[1] in ev}
            ok = ok and not comm(Xe, P)
    flat = [[P.get((s, s), F(0)) for s in EVEN] for P in proj.values()]
    ok = ok and GA.rank_of_vectors(flat) == 6
    GA.check("(4) six independent invariant operators on the sixteen: the six numbers are free", ok)
    return ok
