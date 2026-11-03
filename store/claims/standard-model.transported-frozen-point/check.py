"""standard-model.transported-frozen-point: exact checks.

The quadratic space (2,4) + (1,1) + (1,1) in GA.py: indices 0..5 the ground R^{2,4} with squares
(+,+,-,-,-,-), 6, 7 the second rung's e_+', e_-', 8, 9 the third rung's e_+'', e_-''. T1's null
pair n_0 = (e_- - e_+)/2, n_inf = e_+ + e_- (n_0 . n_inf = -1), the lift
X(x) = n_0 + x + (Q(x)/2) n_inf of Fact transport.totality, and the mode vectors v = n_inf/2,
w = -n_0. The frozen point is sampled as several ground vectors I (not only in one plane), with
Lambda := 3 Q(I) (Fact standard-model.imported-frozen-point-grip-thirteenth-refutation), positive,
negative and zero. Checked: v, w null with v . w = 1/2 and v^* = w for the conjugation fixing e_+
and negating e_-; (i) X(I) null with rung component -w_4 + (Lambda/3) v_4 of norm -Lambda/3;
(ii) Q(I) X(I/Q(I)) = (Lambda/3) n_0' + I + n_inf'/2, null, rung component v_4 - (Lambda/3) w_4 of
norm -Lambda/3, and at Lambda = 0 the ideal point I + n_inf'/2 with rung component exactly v_4;
(iii) lifting X(I) to the third rung adds -w_5 and nothing else; the coefficient one of -w_4 (of
v_4) for every x (every invertible x), the admixture scaling as lambda^2 under I -> lambda I, and
the two rung components being conjugate null directions (the conjugation sends one to minus the
other). The hypercharges -1/2 of w_4, w_5 and +1/2 of v_4 are read in the five-mode module as the
ad-eigenvalues of 6Y = 3 N_R - 2 N_W (that labelling is the module's, Proposition
standard-model.under-s-composites-state-space-spinor, which this derivation does not list, so that
function calls no premise).
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

SQ10 = (1, 1, -1, -1, -1, -1, 1, -1, 1, -1)
# ground vectors (coordinates on e_0..e_5); Lambda = 3 Q(I)
GROUND = [(0, 1, 0, 0, 0, 0), (0, F(5, 4), 0, 0, 0, F(3, 4)), (2, 1, 1, 0, 3, 1), (1, 0, 0, 1, 0, 0),
          (0, 1, 0, 0, 0, 1), (F(1, 2), 3, F(2, 3), -1, 0, F(1, 5)), (1, 0, 2, 0, 0, 0)]
SCALES = [2, F(-1, 3), F(5, 7)]


def gvec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c}


def Q(x):
    return GA.dot(x, x, SQ10)


def rung(a, b):
    """(n_0, n_inf, v, w) of the rung with generators a (+1), b (-1)."""
    ep, em = GA.gen(a), GA.gen(b)
    n0 = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(ep, em)
    return n0, ninf, GA.scal(F(1, 2), ninf), GA.neg(n0)


def lift(x, n0, ninf):
    return GA.add(n0, x, GA.scal(Q(x) / 2, ninf))


def part(x, idx):
    return {b: c for b, c in x.items() if len(b) == 1 and b[0] in idx}


def star(x):
    """The conjugation on vectors: fixes the +1 generators, negates the -1 generators."""
    return {b: (c if SQ10[b[0]] > 0 else -c) for b, c in x.items()}


R2 = rung(6, 7)
R3 = rung(8, 9)


def check_mode_vectors():
    premise("transport.totality")
    ok = True
    for n0, ninf, v, w in (R2, R3):
        ok = ok and Q(n0) == 0 and Q(ninf) == 0 and GA.dot(n0, ninf, SQ10) == -1
        ok = ok and Q(v) == 0 and Q(w) == 0 and GA.dot(v, w, SQ10) == F(1, 2)
        ok = ok and GA.eq(GA.add(GA.mul(v, w, SQ10), GA.mul(w, v, SQ10)), GA.sc(1))
        ok = ok and GA.eq(star(v), w) and GA.eq(star(w), v)
    GA.check("v = n_inf/2, w = -n_0: null, v . w = 1/2, vw + wv = 1, v* = w", ok)
    return ok


def check_lift_and_its_rung_component():
    premise("transport.totality")
    premise("standard-model.imported-frozen-point-grip-thirteenth-refutation")
    n0, ninf, v, w = R2
    ok = True
    lams = set()
    for cs in GROUND:
        I = gvec(cs)
        lam = 3 * Q(I)
        lams.add((lam > 0) - (lam < 0))
        X = lift(I, n0, ninf)
        c = part(X, (6, 7))
        ok = ok and Q(X) == 0
        ok = ok and GA.eq(c, GA.add(n0, GA.scal(lam / 6, ninf)))
        ok = ok and GA.eq(c, GA.add(GA.neg(w), GA.scal(lam / 3, v)))
        ok = ok and Q(c) == -lam / 3 and GA.eq(part(X, range(6)), I)
    ok = ok and lams == {-1, 0, 1}
    GA.check("(i) X(I) null with rung component -w_4 + (Lambda/3) v_4 of norm -Lambda/3", ok)
    return ok


def check_reciprocal_lift():
    premise("transport.totality")
    premise("standard-model.imported-frozen-point-grip-thirteenth-refutation")
    n0, ninf, v, w = R2
    ok = True
    for cs in GROUND:
        I = gvec(cs)
        lam = 3 * Q(I)
        if lam == 0:
            ideal = GA.add(I, GA.scal(F(1, 2), ninf))
            ok = ok and Q(ideal) == 0 and GA.eq(part(ideal, (6, 7)), v)
            continue
        R = GA.scal(Q(I), lift(GA.scal(1 / Q(I), I), n0, ninf))
        ok = ok and Q(R) == 0
        ok = ok and GA.eq(R, GA.add(GA.scal(lam / 3, n0), I, GA.scal(F(1, 2), ninf)))
        c = part(R, (6, 7))
        ok = ok and GA.eq(c, GA.sub(v, GA.scal(lam / 3, w))) and Q(c) == -lam / 3
    GA.check("(ii) the normalised reciprocal's lift has rung component v_4 - (Lambda/3) w_4; at Lambda = 0, v_4", ok)
    return ok


def check_third_rung_adds_minus_w5():
    premise("transport.totality")
    n0, ninf, v, w = R2
    n0b, ninfb, vb, wb = R3
    ok = True
    for cs in GROUND:
        I = gvec(cs)
        lam = 3 * Q(I)
        X = lift(I, n0, ninf)
        XX = lift(X, n0b, ninfb)
        ok = ok and Q(XX) == 0
        ok = ok and GA.eq(GA.sub(XX, X), GA.neg(wb))
        ok = ok and GA.eq(part(XX, (6, 7)), GA.add(GA.neg(w), GA.scal(lam / 3, v)))
    GA.check("(iii) lifting the null X(I) adds n_0'' = -w_5 only", ok)
    return ok


def check_normalisation_scaling_and_conjugate_directions():
    premise("transport.totality")
    premise("standard-model.imported-frozen-point-grip-thirteenth-refutation")
    n0, ninf, v, w = R2
    ok = True
    for cs in GROUND:
        x = gvec(cs)
        c = part(lift(x, n0, ninf), (6, 7))
        # coefficient of -w is one whatever x is: c + w is a multiple of v
        ok = ok and GA.dot(GA.add(c, w), v, SQ10) == 0 and GA.dot(c, v, SQ10) == F(-1, 2)
        if Q(x) != 0:
            r = part(GA.scal(Q(x), lift(GA.scal(1 / Q(x), x), n0, ninf)), (6, 7))
            ok = ok and GA.dot(r, w, SQ10) == F(1, 2) and GA.dot(GA.sub(r, v), w, SQ10) == 0
            # conjugate null directions: the conjugation sends the lift's component to minus the
            # reciprocal's
            ok = ok and GA.eq(star(c), GA.neg(r))
        for lm in SCALES:
            cl = part(lift(GA.scal(lm, x), n0, ninf), (6, 7))
            ok = ok and GA.eq(GA.add(cl, w), GA.scal(lm * lm, GA.add(c, w)))
    GA.check("coefficient one for every x, admixture scaling lambda^2, conjugate null directions", ok)
    return ok


def check_hypercharges_of_the_components():
    # the module's hypercharge (Proposition standard-model.under-s-composites-state-space-spinor) is
    # not among this claim's premises; the labelling is checked without a premise() call
    got = [ad_weight(YOP6, x) for x in (VOP[3], VOP[4], WOP[3], WOP[4])]
    got2 = [ad_weight(T3OP2, x) for x in (VOP[3], VOP[4], WOP[3], WOP[4])]
    ok = got == [3, 3, -3, -3] and got2 == [1, -1, -1, 1]
    GA.check("v_4, v_5 have Y = +1/2 and w_4, w_5 have Y = -1/2: conjugate doublets", ok)
    return ok
