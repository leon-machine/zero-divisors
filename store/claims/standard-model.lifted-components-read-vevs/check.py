"""standard-model.lifted-components-read-vevs: exact checks.

The second-rung components are computed, not typed in: in GA.py's (2,4) + (1,1) (indices 0..5
ground, 6, 7 = e_+', e_-'), with n_0 = (e_- - e_+)/2, n_inf = e_+ + e_-, v = n_inf/2, w = -n_0, the
lift X(x) = n_0 + x + (Q(x)/2) n_inf and the normalised reciprocal Q(x) X(x/Q(x)) of ground
vectors x; a rung component c = a v_4 + b w_4 has a = 2 c.w and b = 2 c.v. The mass forms are
computed in the five-mode module Lambda(C^5) (pair modes 0, 1, 2, rung modes 3, 4 = the text's
4, 5; species by sector under (S)) with the invariant pairing B: M_c(psi, phi) = B(psi, c phi) on
the sixteen. Magnitudes are compared through their squares. Checked, at Lambda = 1/10 (the
proof's value) and at Lambda = 3, -6/5, 0:
(1) read through the conjugate c* = b v_4 + a w_4 (real coefficients) for the up-type and
    neutrino entries and through c for the down-type and charged-lepton ones: the lift gives all
    four 1, the reciprocal's lift all four Lambda/3, their sum all four 1 + Lambda/3 (31/30 at
    Lambda = 1/10), m_u/m_d = 1;
(2) read through c itself: the lift gives m_e = m_d = 1, m_nu = m_u = Lambda/3, the reciprocal's
    lift the reverse;
(3) the unit is the lift's: the lift of any ground vector x gives all four 1 through c*, and its
    reciprocal's lift all four |Q(x)|;
(4) a vector of the ground space V (pair modes) couples only the triplet pairs QQ, QL, u^c d^c,
    u^c e^c, d^c nu^c: no Dirac mass.
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


madd, msc, comm = fock.madd, fock.msc, fock.comm


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

SQ8 = (1, 1, -1, -1, -1, -1, 1, -1)
GROUND = [(0, 1, 0, 0, 0, 0), (2, 1, 1, 0, 3, 1), (F(1, 2), 3, F(2, 3), -1, 0, F(1, 5)),
          (1, 0, 2, 0, 0, 0), (0, 1, 0, 0, 0, 1)]
DIRAC = {("L", "nu^c"), ("Q", "u^c"), ("L", "e^c"), ("Q", "d^c")}
GROUND_VECS_IN_V = [((0, 1), (0, 1)), ((1, 1), (2, -1)), ((0, 2), (3, 5))]   # (modes, (coef v, coef w))


def frozen_ground(lam):
    """A ground vector of norm Lambda/3 in the plane e_+, e_- : (t, s) with 3 t s = Lambda."""
    t, s = F(1), lam / 3
    return GA.add(GA.scal((t + s) / 2, GA.gen(1)), GA.scal((t - s) / 2, GA.gen(5)))


def gvec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c}


def Q(x):
    return GA.dot(x, x, SQ8)


N0 = GA.scal(F(1, 2), GA.sub(GA.gen(7), GA.gen(6)))
NINF = GA.add(GA.gen(6), GA.gen(7))
VV, WW = GA.scal(F(1, 2), NINF), GA.neg(N0)


def lift_component(x):
    X = GA.add(N0, x, GA.scal(Q(x) / 2, NINF))
    c = {b: v for b, v in X.items() if b[0] in (6, 7)}
    return 2 * GA.dot(c, WW, SQ8), 2 * GA.dot(c, VV, SQ8)


def recip_component(x):
    q = Q(x)
    X = GA.scal(q, GA.add(N0, GA.scal(1 / q, x), GA.scal(1 / (2 * q), NINF)))
    c = {b: v for b, v in X.items() if b[0] in (6, 7)}
    return 2 * GA.dot(c, WW, SQ8), 2 * GA.dot(c, VV, SQ8)


def op(a, b):
    return madd(msc(a, VOP[3]), msc(b, WOP[3]))


def reading_through_conjugate(a, b):
    """{species pair: |entry|^2}: up-type and neutrino from M_{c*}, the rest from M_c."""
    up = species_entries(op(b, a))
    down = species_entries(op(a, b))
    out = {}
    for key in (("L", "nu^c"), ("Q", "u^c")):
        out[key] = up.get(key)
    for key in (("L", "e^c"), ("Q", "d^c")):
        out[key] = down.get(key)
    return out


LAMS = [F(1, 10), F(3), F(-6, 5), F(0)]


def check_reading_through_the_conjugate():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.transported-frozen-point")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for lam in LAMS:
        I = frozen_ground(lam)
        ok = ok and Q(I) == lam / 3
        al, bl = lift_component(I)
        ok = ok and (al, bl) == (lam / 3, -1)
        got = reading_through_conjugate(al, bl)
        ok = ok and all(got[key] == {F(1)} for key in DIRAC)
        if lam != 0:
            ar, br = recip_component(I)
            ok = ok and (ar, br) == (1, -lam / 3)
            got = reading_through_conjugate(ar, br)
            ok = ok and all(got[key] == {(lam / 3) ** 2} for key in DIRAC)
            got = reading_through_conjugate(al + ar, bl + br)
            ok = ok and all(got[key] == {(1 + lam / 3) ** 2} for key in DIRAC)
            ok = ok and got[("Q", "u^c")] == got[("Q", "d^c")]
    ok = ok and (1 + F(1, 10) / 3) == F(31, 30)
    GA.check("through c*: lift all four 1, reciprocal all four Lambda/3, sum all four 1 + Lambda/3", ok)
    return ok


def check_reading_through_c_itself():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.transported-frozen-point")
    premise("standard-model.hyp-s-slot-statistics")
    ok = True
    for lam in LAMS:
        if lam == 0:
            continue
        I = frozen_ground(lam)
        got = species_entries(op(*lift_component(I)))
        ok = ok and got == {("L", "e^c"): {F(1)}, ("Q", "d^c"): {F(1)},
                            ("L", "nu^c"): {(lam / 3) ** 2}, ("Q", "u^c"): {(lam / 3) ** 2}}
        got = species_entries(op(*recip_component(I)))
        ok = ok and got == {("L", "nu^c"): {F(1)}, ("Q", "u^c"): {F(1)},
                            ("L", "e^c"): {(lam / 3) ** 2}, ("Q", "d^c"): {(lam / 3) ** 2}}
    GA.check("through c: the lift is H_d-type (m_e = m_d = 1, m_nu = m_u = Lambda/3), the reciprocal H_u-type", ok)
    return ok


def check_the_unit_is_the_lifts():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.transported-frozen-point")
    ok = True
    for cs in GROUND:
        x = gvec(cs)
        a, b = lift_component(x)
        ok = ok and b == -1 and a == Q(x)
        got = reading_through_conjugate(a, b)
        ok = ok and all(got[key] == {F(1)} for key in DIRAC)
        if Q(x) != 0:
            got = reading_through_conjugate(*recip_component(x))
            ok = ok and all(got[key] == {Q(x) ** 2} for key in DIRAC)
    GA.check("the lift of any ground vector gives the unit 1 through c*; its reciprocal |Q(x)|", ok)
    return ok


def check_ground_frozen_point_gives_no_dirac_mass():
    premise("standard-model.yukawa-pattern-two-rung-module")
    premise("standard-model.hyp-s-slot-statistics")
    triplet = {("Q", "Q"), ("L", "Q"), ("d^c", "u^c"), ("e^c", "u^c"), ("d^c", "nu^c")}
    ok = True
    seen = set()
    for modes, (cv, cw) in GROUND_VECS_IN_V:
        x = madd(msc(F(cv), VOP[modes[0]]), msc(F(cw), WOP[modes[1]]))
        pairs = set(species_entries(x))
        ok = ok and pairs <= triplet and not (pairs & DIRAC) and pairs
        seen |= pairs
    ok = ok and seen == triplet
    GA.check("a vector of V couples only the triplet pairs: no Dirac mass", ok)
    return ok
