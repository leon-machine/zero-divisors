"""singularity.euclidean-rotor-where-it-lies: exact checks.

Half-angles are Pythagorean: (c, s) = (cos(theta/2), sin(theta/2)) rational with c^2 + s^2 = 1; theta = 2 pi is
(c, s) = (-1, 0) and theta = 4 pi is (1, 0). Complex multivectors are pairs (re, im) of GA multivectors.
(1) In Cl(1,3) the hyperbolic atom v = (e0 + e1)/2, v* = (e0 - e1)/2 satisfies the CAR and
    sigma = v* v - v v* = e0 e1 with sigma^2 = +1; (i sigma)^2 = -1; R_{i theta} = c + i sigma s satisfies the
    composition law R(c1,s1) R(c2,s2) = R(c1c2 - s1s2, s1c2 + c1s2) and R R* = 1 (the atom's adjoint, under
    which v* is the adjoint of v and sigma* = sigma, with complex conjugation); R_{2 pi i} = -1,
    R_{4 pi i} = +1.
(2) On the two-dimensional module (v = [[0,1],[0,0]], v* its transpose): sigma = diag(-1, 1) and
    R_{i theta} = diag(c - i s, c + i s) = diag(e^{-i theta/2}, e^{i theta/2}) at 4 angles; at theta = 2 pi it is
    -1 on spinors while its conjugation fixes all four matrix units; at theta = pi it does not: there it is
    the parity alpha = Ad_sigma, whose average (x + sigma x sigma)/2 is the descent E (the diagonal part).
(3) i sigma is not real: no real element a + b sigma of the radial plane's even algebra squares to -1
    ((a + b sigma)^2 = a^2 + b^2 + 2ab sigma), and in span(sigma, I sigma) the real elements with square -1 are
    exactly +-I sigma ((a sigma + b I sigma)^2 = a^2 - b^2 + 2ab I). I sigma = e0e1e2e3 e0e1 = e2e3; its rotor
    (Pythagorean angles) fixes e0, e1, sigma and rotates e2 into e3. Every real rotor preserving the radial
    plane acts on it by a matrix L with L^T eta L = eta, eta = diag(1, -1), so |trace L| >= 2 (computed
    from the general solution on rational samples); the Euclidean rotation matrices fail L^T eta L = eta.
    The complexified rotor R_{i theta} rotates the Wick-rotated pair (e0, i e1), both of square +1:
    e0 -> cos(theta) e0 - sin(theta) (i e1).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S = GA.sig(1, 3)
E0, E1, E2, E3 = (GA.gen(i) for i in range(4))
SIG = GA.mul(E0, E1, S)
I4 = {(0, 1, 2, 3): F(1)}
ANGLES = [(F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(8, 17), F(-15, 17)), (F(0), F(1))]


def cmul(x, y):
    a, b = x
    c, d = y
    return (GA.sub(GA.mul(a, c, S), GA.mul(b, d, S)), GA.add(GA.mul(a, d, S), GA.mul(b, c, S)))


def ceq(x, y):
    return GA.eq(x[0], y[0]) and GA.eq(x[1], y[1])


def R(c, s):
    return (GA.sc(c), GA.scal(s, SIG))          # c + i s sigma


def star_real(x):
    """The atom's adjoint on Cl(1,3): anti-automorphism with e0* = e0, e_k* = -e_k (k >= 1), so that
    v* = (e0 - e1)/2 is the adjoint of v = (e0 + e1)/2."""
    out = {}
    for b, c in GA.reverse(x).items():
        out[b] = c * (-1) ** sum(1 for i in b if i != 0)
    return out


def cdag(x):
    return (star_real(x[0]), GA.neg(star_real(x[1])))


def check_complexified_rotor_period_four_pi():
    v = GA.scal(F(1, 2), GA.add(E0, E1))
    vs = GA.scal(F(1, 2), GA.sub(E0, E1))
    ok = GA.is_zero(GA.mul(v, v, S)) and GA.is_zero(GA.mul(vs, vs, S))
    ok = ok and GA.eq(GA.add(GA.mul(v, vs, S), GA.mul(vs, v, S)), GA.sc(1))
    ok = ok and GA.eq(GA.sub(GA.mul(vs, v, S), GA.mul(v, vs, S)), SIG)
    ok = ok and GA.eq(GA.mul(SIG, SIG, S), GA.sc(1))
    ok = ok and GA.eq(star_real(v), vs) and GA.eq(star_real(SIG), SIG)
    isig = ({}, SIG)
    ok = ok and ceq(cmul(isig, isig), (GA.sc(-1), {}))
    for (c1, s1) in ANGLES:
        ok = ok and c1 * c1 + s1 * s1 == 1
        ok = ok and ceq(cmul(R(c1, s1), cdag(R(c1, s1))), (GA.sc(1), {}))
        for (c2, s2) in ANGLES:
            ok = ok and ceq(cmul(R(c1, s1), R(c2, s2)), R(c1 * c2 - s1 * s2, s1 * c2 + c1 * s2))
    half = R(F(0), F(1))                          # theta = pi
    two_pi = cmul(half, half)
    ok = ok and ceq(two_pi, R(F(-1), F(0))) and ceq(two_pi, (GA.sc(-1), {}))
    ok = ok and ceq(cmul(two_pi, two_pi), (GA.sc(1), {}))
    _tp_rv = (ok); assert _tp_rv is not False, "check_complexified_rotor_period_four_pi"; return _tp_rv


QI = GA.QI


def qmm(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]


def check_module_form_and_conjugation_period():
    premise("singularity.descent-parity-average")
    v = [[QI(0), QI(1)], [QI(0), QI(0)]]
    vs = [[QI(0), QI(0)], [QI(1), QI(0)]]
    sig = [[a - b for a, b in zip(r1, r2)] for r1, r2 in zip(qmm(vs, v), qmm(v, vs))]
    ok = sig == [[QI(-1), QI(0)], [QI(0), QI(1)]]
    units = [[[QI(1) if (i, j) == (a, b) else QI(0) for j in range(2)] for i in range(2)]
             for a in range(2) for b in range(2)]
    for (c, s) in ANGLES + [(F(-1), F(0))]:
        Rm = [[QI(c) + QI(0, s) * sig[i][j] if i == j else QI(0, s) * sig[i][j] for j in range(2)]
              for i in range(2)]
        ok = ok and Rm == [[QI(c, -s), QI(0)], [QI(0), QI(c, s)]]
    Rpi = [[QI(0, -1), QI(0)], [QI(0), QI(0, 1)]]
    R2pi = qmm(Rpi, Rpi)
    ok = ok and R2pi == [[QI(-1), QI(0)], [QI(0), QI(-1)]]
    R2inv = [[QI(-1), QI(0)], [QI(0), QI(-1)]]
    Rpiinv = [[QI(0, 1), QI(0)], [QI(0), QI(0, -1)]]
    ok = ok and all(qmm(qmm(R2pi, U), R2inv) == U for U in units)
    ok = ok and any(qmm(qmm(Rpi, U), Rpiinv) != U for U in units)
    # the half-period conjugation is the parity alpha = Ad_sigma, whose average is the descent E
    for U in units:
        par = qmm(qmm(sig, U), sig)
        ok = ok and qmm(qmm(Rpi, U), Rpiinv) == par
        Ex = [[(U[i][j] + par[i][j]) * QI(F(1, 2)) for j in range(2)] for i in range(2)]
        ok = ok and Ex == [[U[i][j] if i == j else QI(0) for j in range(2)] for i in range(2)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_module_form_and_conjugation_period"; return _tp_rv


def check_euclidean_rotation_is_no_real_rotor():
    Isig = GA.mul(I4, SIG, S)
    ok = GA.eq(Isig, GA.mul(E2, E3, S)) and GA.eq(GA.mul(Isig, Isig, S), GA.sc(-1))
    for a, b in [(F(1), F(0)), (F(0), F(1)), (F(2), F(-3)), (F(1, 2), F(1, 3))]:
        x = GA.add(GA.sc(a), GA.scal(b, SIG))
        ok = ok and GA.eq(GA.mul(x, x, S), GA.add(GA.sc(a * a + b * b), GA.scal(2 * a * b, SIG)))
        y = GA.add(GA.scal(a, SIG), GA.scal(b, Isig))
        ok = ok and GA.eq(GA.mul(y, y, S), GA.add(GA.sc(a * a - b * b), GA.scal(2 * a * b, I4)))
        ok = ok and (GA.eq(GA.mul(y, y, S), GA.sc(-1)) == (a == 0 and b * b == 1))
    for (c, s) in ANGLES:
        Rr = GA.add(GA.sc(c), GA.scal(s, Isig))
        Rt = GA.reverse(Rr)
        ok = ok and GA.eq(GA.mul(Rr, Rt, S), GA.sc(1))
        for x in (E0, E1, SIG):
            ok = ok and GA.eq(GA.mul(GA.mul(Rr, x, S), Rt, S), x)
        img = GA.mul(GA.mul(Rr, E2, S), Rt, S)
        ok = ok and GA.eq(img, GA.add(GA.scal(c * c - s * s, E2), GA.scal(2 * c * s, E3)))
    # isometries of the radial plane: L^T eta L = eta; boosts [[a, b], [b, a]], a^2 - b^2 = 1
    eta = [[1, 0], [0, -1]]

    def preserves(L):
        LT = [[L[j][i] for j in range(2)] for i in range(2)]
        return GA.mat_mul(GA.mat_mul(LT, eta), L) == [[F(x) for x in r] for r in eta]
    for t in (F(1, 2), F(1, 3), F(-2, 5)):
        a, b = (1 + t * t) / (1 - t * t), 2 * t / (1 - t * t)
        L = [[a, b], [b, a]]
        ok = ok and preserves(L) and (2 * a) ** 2 > 4
    for (c, s) in ANGLES[:3]:
        cc, ss = c * c - s * s, 2 * c * s
        ok = ok and not preserves([[cc, -ss], [ss, cc]])
    # complexified: R e0 R^{-1} = cos(theta) e0 - sin(theta) (i e1), with (i e1)^2 = +1
    ie1 = ({}, E1)
    ok = ok and ceq(cmul(ie1, ie1), (GA.sc(1), {}))
    for (c, s) in ANGLES:
        Rc = R(c, s)
        Rinv = R(c, -s)
        ok = ok and ceq(cmul(Rc, Rinv), (GA.sc(1), {}))
        img = cmul(cmul(Rc, (E0, {})), Rinv)
        cos_t, sin_t = c * c - s * s, 2 * s * c
        ok = ok and ceq(img, (GA.scal(cos_t, E0), GA.scal(-sin_t, E1)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_euclidean_rotation_is_no_real_rotor"; return _tp_rv
