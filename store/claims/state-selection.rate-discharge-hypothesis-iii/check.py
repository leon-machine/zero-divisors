"""state-selection.rate-discharge-hypothesis-iii: exact checks of the finite cores of the argument.

(1) KMS forces Gibbs (Theorem singularity.kms-uniqueness-factor): on the mode factor M_2 with K = w (N - 1/2), the
    KMS condition at Boltzmann factor q = e^{-beta w} has, among all density matrices, the one-dimensional solution
    space spanned by diag(1, q); the solution is even (zero off-diagonal, (P)) and has full rank for q > 0 (the
    state is faithful, as the modular group presupposes), while the non-faithful diag(1, 0) solves it for no q > 0.
(2) One temperature for all modes (Corollary singularity.universality-temperature-under-g): for two modes with
    weights 1 and 2 (K = N1 + 2 N2) the product of per-mode Gibbs states with factors q1, q2 is KMS for the joint
    flow at one beta exactly when q2 = q1^2 (solved on the 4 x 4 diagonal), at sample pairs.
(3) The period (Proposition state-selection.euclidean-partner-curvature-selected): with J = I sigma_r in Cl(1,3),
    J^2 = -1, the rotor R = c + s J at a rational point (c, s) = (cos(theta/2), sin(theta/2)) acts on vectors as the
    identity exactly when s = 0, so the conjugation action closes at theta = 2 pi (c = -1, R = -1) and at no
    smaller angle; at s != 0 the action is a nontrivial rotation by cos(theta) = c^2 - s^2 in the plane of
    e2, e3.
(4) The calibration (Proposition singularity.plane-rate): kappa = f'(2M)/2 = 1/(4M) for f = 1 - 2M/r, so a rapidity
    period 2 pi is beta = 2 pi/kappa = 8 pi M and T = 1/(8 pi M): coefficients 8M and 1/(8M) at sample M.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QS = [F(1, 2), F(9, 16), F(4)]
PAIRS = [(F(1, 2), F(1, 4)), (F(1, 3), F(1, 9)), (F(1, 2), F(1, 3)), (F(2, 3), F(1, 2))]
CIRCLE = [(F(3, 5), F(4, 5)), (F(-1), F(0)), (F(1), F(0)), (F(-5, 13), F(12, 13)), (F(0), F(1))]
MASSES = [F(1, 2), F(3), F(7, 2)]
S13 = GA.sig(1, 3)


def kms_rows(w):
    d = len(w)
    rows = []
    for a in range(d):
        for b in range(d):
            for c in range(d):
                for e in range(d):
                    row = [F(0)] * (d * d)
                    if b == c:
                        row[d * e + a] += 1
                    if e == a:
                        row[d * b + c] -= w[a] / w[b]
                    rows.append(row)
    return rows


def check_kms_state_is_the_faithful_gibbs_state():
    premise("singularity.kms-uniqueness-factor")
    premise("singularity.p-univalence")
    ok = True
    for q in QS:
        rows = kms_rows([F(1), q])
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == 1
        rho = [x / (ker[0][0] + ker[0][3]) for x in ker[0]]
        ok = ok and rho == [1 / (1 + q), F(0), F(0), q / (1 + q)]
        ok = ok and rho[0] * rho[3] - rho[1] * rho[2] != 0
        pure = [F(1), F(0), F(0), F(0)]
        ok = ok and any(sum(r[i] * pure[i] for i in range(4)) != 0 for r in rows)
    _tp_rv = (ok); assert _tp_rv is not False, "check_kms_state_is_the_faithful_gibbs_state"; return _tp_rv


def check_one_beta_for_all_modes():
    premise("singularity.universality-temperature-under-g")
    ok = True
    hits = 0
    for q1, q2 in PAIRS:
        rho = [F(1), q1, q2, q1 * q2]                    # product state on |n1 n2>, index n1 + 2 n2
        # a joint Gibbs state is proportional to (1, x, x^2, x^3); x is read off the first ratio
        x = rho[1] / rho[0]
        G = [x ** (n1 + 2 * n2) for n2 in range(2) for n1 in range(2)]
        found = all(rho[i] * G[0] == G[i] * rho[0] for i in range(4))
        ok = ok and found == (q2 == q1 * q1)
        hits += found
    _tp_rv = (ok and hits == 2); assert _tp_rv is not False, "check_one_beta_for_all_modes"; return _tp_rv


def check_conjugation_closes_at_two_pi():
    premise("state-selection.euclidean-partner-curvature-selected")
    premise("singularity.r-regularity-fixed-locus")
    I = GA.mul(GA.mul(GA.gen(0), GA.gen(1), S13), GA.mul(GA.gen(2), GA.gen(3), S13), S13)
    J = GA.mul(I, GA.mul(GA.gen(0), GA.gen(1), S13), S13)
    ok = GA.mul(J, J, S13) == {(): F(-1)}
    identities = 0
    for c, s in CIRCLE:
        R = GA.add(GA.sc(c), GA.scal(s, J))
        Rinv = GA.sub(GA.sc(c), GA.scal(s, J))
        ok = ok and GA.mul(R, Rinv, S13) == {(): F(1)}
        trivial = all(GA.eq(GA.mul(GA.mul(R, GA.gen(i), S13), Rinv, S13), GA.gen(i)) for i in range(4))
        ok = ok and trivial == (s == 0)
        identities += trivial
        img = GA.mul(GA.mul(R, GA.gen(2), S13), Rinv, S13)
        ok = ok and img.get((2,), F(0)) == c * c - s * s
        if c == -1:
            ok = ok and R == {(): F(-1)}
    _tp_rv = (ok and identities == 2); assert _tp_rv is not False, "check_conjugation_closes_at_two_pi"; return _tp_rv


def check_calibration_beta_is_eight_pi_m():
    premise("singularity.plane-rate")
    ok = True
    for M in MASSES:
        rh = 2 * M
        kappa = (2 * M / (rh * rh)) / 2
        ok = ok and kappa == 1 / (4 * M)
        beta_over_pi = 2 / kappa
        ok = ok and beta_over_pi == 8 * M and 1 / beta_over_pi == 1 / (8 * M)
    _tp_rv = (ok); assert _tp_rv is not False, "check_calibration_beta_is_eight_pi_m"; return _tp_rv
