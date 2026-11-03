"""pairing.stabiliser-parabolic-algebra-null-direction: exact checks.

Conventions: C^4 with orthonormal e0 (+1), e1, e2, e3 (-1), complex-bilinear <,>; l = e0 + e1, n = e0 - e1,
m = e2 + i e3, mb = e2 - i e3, W = span(l, m); bivectors act by B.v = (1/2)[B, v], computed in the Clifford
algebra Cl(1,3) with Gaussian-rational coefficients; pv(B) = <B.l, m>.
(1) W is maximal isotropic; pv on the basis: e01, e23 -> 0, e02 -> 1, e03 -> i, e12 -> -1, e13 -> -i;
    pv(n e2) = 2, pv(n e3) = 2i.
(2) B.W in W iff pv(B) = 0: the stabiliser conditions (<B.w, w'> = 0 for w, w' in W) have rank one and
    the same kernel as pv, of complex dimension five; on twelve sample complex bivectors B.l and B.m lie in W
    exactly when pv(B) = 0 (both outcomes occur). The mb-component of B.l is -pv(B)/2 (<mb, m> = -2).
(3) Real points: the real bivectors with Re pv = Im pv = 0 form a space of real dimension 4 (the two real
    equations have rank 2), spanned by e01, e23, l e2, l e3, each with pv = 0 and linearly independent.
(4) Spin action: in the two-mode Fock model of Cl(1,3)_C the vacuum of W (joint kernel of c(l), c(m)) is a
    line, and the bivectors fixing its ray form exactly the kernel of pv (dimension five).
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
import gtg
from tp_premise import premise

QI = GA.QI
ZERO, ONE, IU = QI(0), QI(1), QI(0, 1)
SQ4 = (1, -1, -1, -1)
PAIRS = list(combinations(range(4), 2))   # e01, e02, e03, e12, e13, e23


def cvec(*c):
    return {(a,): (v if isinstance(v, QI) else QI(v)) for a, v in enumerate(c) if v != 0}


def cmul(x, y):
    return GA.mul(x, y, SQ4)


def cscal(c, x):
    c = c if isinstance(c, QI) else QI(c)
    return {b: c * v for b, v in x.items() if c * v != 0}


def cadd(*xs):
    out = {}
    for x in xs:
        for b, v in x.items():
            out[b] = out.get(b, ZERO) + v
    return {b: v for b, v in out.items() if v != 0}


def act(B, v):
    return gtg.comm(B, v, SQ4)                # (Bv - vB)/2


def ipc(u, v):
    return sum((SQ4[a] * u.get((a,), ZERO) * v.get((a,), ZERO) for a in range(4)), ZERO)


ELL, ENN = cvec(1, 1, 0, 0), cvec(1, -1, 0, 0)
EM, EMB = cvec(0, 0, 1, IU), cvec(0, 0, 1, -IU)
BAS = {p: cmul(cvec(*[1 if k == p[0] else 0 for k in range(4)]), cvec(*[1 if k == p[1] else 0 for k in range(4)]))
       for p in PAIRS}
SAMPLE_COEFFS = [(1, 0, 0, 0, 0, 0), (0, 1, 0, 0, 0, 0), (1, 2, 3, 4, 5, 6), (QI(1, 1), 0, 2, QI(0, -1), 1, 3),
                 (0, 1, 0, 1, 0, 0), (0, 0, 1, 0, 1, 0), (2, 1, QI(0, 1), 1, QI(0, -1), -1), (0, 0, 0, 0, 0, 1),
                 (1, 1, 1, 1, 1, 1), (0, 1, QI(0, -1), 0, 0, 0), (3, QI(2, 1), 1, QI(2, 1), -1, 7), (0, 0, 1, 0, -1, 0)]


def bivector(coeffs):
    return cadd(*[cscal(c, BAS[p]) for c, p in zip(coeffs, PAIRS) if c != 0])


def pv(B):
    return ipc(act(B, ELL), EM)


def vcoords(v):
    return [v.get((a,), ZERO) for a in range(4)]


def in_W(v):
    return GA.field_rank([vcoords(ELL), vcoords(EM), vcoords(v)]) == 2


def check_values_on_the_basis_and_null_rotations():
    ok = True
    ok = ok and ipc(ELL, ELL) == ZERO and ipc(EM, EM) == ZERO and ipc(ELL, EM) == ZERO
    ok = ok and ipc(EMB, EM) == QI(-2) and ipc(ENN, ELL) == QI(2)
    expect = {(0, 1): ZERO, (2, 3): ZERO, (0, 2): ONE, (0, 3): IU, (1, 2): -ONE, (1, 3): -IU}
    ok = ok and all(pv(BAS[p]) == v for p, v in expect.items())
    ok = ok and pv(cmul(ENN, cvec(0, 0, 1, 0))) == QI(2) and pv(cmul(ENN, cvec(0, 0, 0, 1))) == QI(0, 2)
    _tp_rv = (ok); assert _tp_rv is not False, "check_values_on_the_basis_and_null_rotations"; return _tp_rv


def check_stabiliser_is_the_kernel_of_one_functional():
    premise("pairing.imported-two-readings-capacities-vacuum-null")
    ok = True
    Wb = [ELL, EM]
    rows = [[ipc(act(BAS[p], w), w2) for p in PAIRS] for w in Wb for w2 in Wb]
    pvrow = [pv(BAS[p]) for p in PAIRS]
    ok = ok and GA.field_rank(rows) == 1 and GA.field_rank(rows + [pvrow]) == 1
    ok = ok and len(GA.field_kernel(rows)) == 5
    zero_seen = nonzero_seen = 0
    for c in SAMPLE_COEFFS:
        B = bivector(c)
        p = pv(B)
        stab = in_W(act(B, ELL)) and in_W(act(B, EM))
        ok = ok and stab == (p == ZERO)
        # mb-component of B.l: B.l = al l + an n + am m + amb mb with amb = <B.l, m>/<mb, m>
        Bl = act(B, ELL)
        sol = GA.field_solve([[vcoords(v)[r] for v in (ELL, ENN, EM, EMB)] for r in range(4)], vcoords(Bl))
        ok = ok and sol[3] == p * QI(F(-1, 2)) and sol[1] == ZERO
        zero_seen += 1 if p == ZERO else 0
        nonzero_seen += 1 if p != ZERO else 0
    ok = ok and zero_seen == 5 and nonzero_seen == 7
    _tp_rv = (ok); assert _tp_rv is not False, "check_stabiliser_is_the_kernel_of_one_functional"; return _tp_rv


def check_real_points_are_the_parabolic_algebra():
    ok = True
    vals = [pv(BAS[p]) for p in PAIRS]
    real_rows = [[v.re for v in vals], [v.im for v in vals]]
    ok = ok and GA.mat_rank(real_rows) == 2 and len(GA.field_kernel(real_rows)) == 4
    para = [BAS[(0, 1)], BAS[(2, 3)], cmul(ELL, cvec(0, 0, 1, 0)), cmul(ELL, cvec(0, 0, 0, 1))]
    ok = ok and all(pv(B) == ZERO for B in para)
    blades = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    rows = [[B.get(b, ZERO).re for b in blades] for B in para]
    ok = ok and all(B.get(b, ZERO).im == 0 for B in para for b in blades) and GA.mat_rank(rows) == 4
    ok = ok and all(not B.get((), ZERO) for B in para)
    _tp_rv = (ok); assert _tp_rv is not False, "check_real_points_are_the_parabolic_algebra"; return _tp_rv


# two-mode Fock model of Cl(1,3)_C: (e0, e1) -> mode 0, (e2, e3) -> mode 1
def op(i, create):
    """a_i^dag (create) or a_i on two Jordan-Wigner modes, dense over GA.QI (LSB bitmask basis)."""
    return fock.to_dense(fock.msc(ONE, fock.cre(i, 2) if create else fock.ann(i, 2)), 4, ZERO)


def lin(*terms):
    return [[sum((c * M[r][k] for c, M in terms), ZERO) for k in range(4)] for r in range(4)]


mm = GA.field_mat_mul


W0, W0P, W1, W1P = op(0, True), op(0, False), op(1, True), op(1, False)
GEN = [lin((ONE, W0), (ONE, W0P)), lin((ONE, W0), (-ONE, W0P)), lin((ONE, W1), (-ONE, W1P)),
       lin((-IU, W1), (-IU, W1P))]


def cop(v):
    return lin(*[(v.get((a,), ZERO), GEN[a]) for a in range(4)])


def check_spin_action_fixes_vacuum_ray_iff_pv_vanishes():
    premise("pairing.imported-two-readings-capacities-vacuum-null")
    ok = True
    ok = ok and all(lin((ONE, mm(GEN[a], GEN[b])), (ONE, mm(GEN[b], GEN[a]))) ==
                    [[QI(2 * SQ4[a]) if (a == b and r == k) else ZERO for k in range(4)] for r in range(4)]
                    for a in range(4) for b in range(4))
    vac = GA.field_kernel(cop(ELL) + cop(EM))
    ok = ok and len(vac) == 1
    u = vac[0]
    imgs = []
    for p in PAIRS:
        X = mm(GEN[p[0]], GEN[p[1]])
        imgs.append([sum((X[r][k] * u[k] for k in range(4)), ZERO) for r in range(4)])
    M = [[imgs[k][r] for k in range(6)] + [-u[r]] for r in range(4)]
    ker = GA.field_kernel(M)
    ok = ok and len(ker) == 5
    pvrow = [pv(BAS[p]) for p in PAIRS]
    ok = ok and all(sum((pvrow[i] * k[i] for i in range(6)), ZERO) == ZERO for k in ker)
    _tp_rv = (ok); assert _tp_rv is not False, "check_spin_action_fixes_vacuum_ray_iff_pv_vanishes"; return _tp_rv
