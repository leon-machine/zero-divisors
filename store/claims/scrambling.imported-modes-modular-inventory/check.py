"""scrambling.imported-modes-modular-inventory: exact checks on the atom Cl(1,1) (GA blade engine).

e+ = e0 (square +1), e- = e1 (square -1), f = (e+ + e-)/2, f^* = (e+ - e-)/2, N = f^* f, sigma = f^* f - f f^*.
(1) sigma = e+ e- (a pure bivector), sigma^2 = 1; [sigma, f]/2 = -f and [sigma, f^*]/2 = +f^* (weights -1, +1),
    so Ad(exp(lambda sigma/2)) scales the pair by e^(-lambda), e^(lambda); sigma = P1 - P0 with P1 = f^* f,
    P0 = f f^* the occupation projectors (orthogonal idempotents summing to 1), so sigma/2 = N - 1/2.
(2) Uniqueness up to reparametrisation and orientation: Cl(1,1) has exactly one bivector blade, so every
    one-parameter rotor flow exp(t B), B a bivector, is exp(t b sigma); (b sigma)^2 = b^2 at samples.
(3) The normalisation: for the Schwarzschild function f(r) = 1 - 2M/r the surface gravity f'(r_h)/2 at the
    root r_h = 2M is 1/(4M) (exact rational functions, M = 1, 3/2, 7), so rapidity = t/(4M).
(4) The continuation U = cos(theta/2) + i sin(theta/2) sigma in the complexified atom (pairs re, im) satisfies
    U U^-1 = 1 with U^-1 = cos - i sin sigma, and U f U^-1 = (cos theta - i sin theta) f at rational points
    (cos theta = c^2 - s^2, sin theta = 2cs): the identity exactly when s = 0, so the conjugation has period
    2 pi (at theta = pi it is -1 on f) while U(2 pi) = -1. The real commutant of sigma is span{1, sigma}
    (dimension 2), and (a + b sigma)^2 = a^2 + b^2 + 2ab sigma is never -1 for real a, b, so the generator
    i sigma (square -1) lies outside the real algebra.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1)
POINTS = [(F(3, 5), F(4, 5)), (F(5, 13), F(-12, 13)), (F(0), F(1)), (F(-1), F(0)), (F(1), F(0))]
MASSES = [F(1), F(3, 2), F(7)]
BS = [F(2), F(-1, 3)]

f = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(1)))
fs = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1)))
P1 = GA.mul(fs, f, SQ)
P0 = GA.mul(f, fs, SQ)
SIG = GA.sub(P1, P0)


def com(x, y):
    return GA.sub(GA.mul(x, y, SQ), GA.mul(y, x, SQ))


def check_boost_bivector_weights_and_spectral_projectors():
    premise("hawking.modular-structure-completed-pair")
    ok = True
    ok = ok and SIG == {(0, 1): F(1)}
    ok = ok and GA.mul(SIG, SIG, SQ) == GA.sc(1)
    ok = ok and GA.scal(F(1, 2), com(SIG, f)) == GA.neg(f)
    ok = ok and GA.scal(F(1, 2), com(SIG, fs)) == fs
    ok = ok and GA.mul(P0, P0, SQ) == P0 and GA.mul(P1, P1, SQ) == P1 and GA.mul(P0, P1, SQ) == {}
    ok = ok and GA.add(P0, P1) == GA.sc(1)
    ok = ok and GA.scal(F(1, 2), SIG) == GA.sub(P1, GA.sc(F(1, 2)))
    GA.check("sigma = e+e-, sigma^2 = 1, weights -1/+1 on f, f*; sigma = P1 - P0, sigma/2 = N - 1/2", ok)
    return ok


def check_unique_flow_up_to_reparametrisation():
    premise("hawking.modular-structure-completed-pair")
    ok = True
    biv = [b for b in GA.all_blades(2) if len(b) == 2]
    ok = ok and biv == [(0, 1)]
    for b in BS:
        B = GA.scal(b, SIG)
        ok = ok and GA.mul(B, B, SQ) == GA.sc(b * b)
        ok = ok and GA.scal(F(1, 2), com(B, f)) == GA.scal(-b, f)
    GA.check("the bivector space of the atom is one-dimensional: flows differ only by speed and orientation", ok)
    return ok


def check_surface_gravity_normalisation():
    premise("singularity.computed")
    ok = True
    for M in MASSES:
        fr = GA.RF([-2 * M, F(1)], [F(0), F(1)])        # (r - 2M)/r
        rh = 2 * M
        ok = ok and fr.eval(rh) == 0
        kappa = fr.deriv().eval(rh) * F(1, 2)
        ok = ok and kappa == F(1, 4) / M
    GA.check("kappa = f'(r_h)/2 = 1/(4M) for f = 1 - 2M/r", ok)
    return ok


def cmul(x, y):
    return (GA.sub(GA.mul(x[0], y[0], SQ), GA.mul(x[1], y[1], SQ)),
            GA.add(GA.mul(x[0], y[1], SQ), GA.mul(x[1], y[0], SQ)))


def check_euclidean_continuation_period_and_reality():
    premise("singularity.euclidean-rotor-where-it-lies")
    ok = True
    for c, s in POINTS:
        U = (GA.sc(c), GA.scal(s, SIG))
        Uinv = (GA.sc(c), GA.scal(-s, SIG))
        ok = ok and cmul(U, Uinv) == (GA.sc(1), {})
        conj = cmul(cmul(U, (f, {})), Uinv)
        ok = ok and conj == (GA.scal(c * c - s * s, f), GA.scal(-2 * c * s, f))
        ok = ok and (conj == (f, {})) == (s == 0)
    U2pi = (GA.sc(-1), {})
    ok = ok and cmul(cmul(U2pi, (f, {})), U2pi) == (f, {})
    Upi = (GA.sc(0), SIG)
    ok = ok and cmul(cmul(Upi, (f, {})), (GA.sc(0), GA.neg(SIG))) == (GA.neg(f), {})
    blades = GA.all_blades(2)
    rows = [GA.basis_vector_of(com({b: F(1)}, SIG), blades) for b in blades]
    M_ = [[rows[j][i] for j in range(4)] for i in range(4)]
    ok = ok and 4 - GA.field_rank(M_) == 2
    for a in (F(0), F(1), F(-2, 3)):
        for b in (F(0), F(1, 2), F(3)):
            sqr = GA.mul(GA.add(GA.sc(a), GA.scal(b, SIG)), GA.add(GA.sc(a), GA.scal(b, SIG)), SQ)
            ok = ok and sqr.get((), F(0)) == a * a + b * b and sqr != GA.sc(-1)
    ok = ok and cmul((GA.sc(0), SIG), (GA.sc(0), SIG)) == (GA.sc(-1), {})
    GA.check("continuation: conjugation period 2 pi, U(2 pi) = -1; i sigma (square -1) is not real", ok)
    return ok
