"""dark-matter.reduced-response-gravity-needs-supporting-stress: exact checks.

(0) Setting, in GA (Cl(1,3), (+,-,-,-)): the conformal-Newtonian field hb^{-1}(e_tau) = a(1 + psi) gamma0,
    hb^{-1}(e_i) = a(1 - phi) gamma_i of the premise Fact has derived metric g = hb^{-1} . hb^{-1} whose part
    linear in the potentials is a^2 (2 psi d tau^2 + 2 phi dx^2), i.e. a^2 [(1 + 2 psi) d tau^2 -
    (1 - 2 phi) dx^2] at linear order, minus the source's line element in (-,+,+,+) (linear parts
    extracted exactly from the quadratic dependence on the potentials).
(1) With the Fact's momentum equation theta' = -H theta + k^2 psi - k^2 sigma, the reduced response
    theta' = -H theta + g k^2 psi holds for all theta exactly when sigma = (1 - g) psi: the equation is
    linear in sigma with coefficient -k^2 != 0, checked at rational samples with the solution unique.
(2) With the traceless equation k^2 (phi - psi) = c [rho sigma + Sigma], c = 12 pi G a^2 treated as a
    rational parameter (the identity is polynomial in c), the stated psi satisfies it exactly at rational
    samples, and at g = 1 it reduces to psi = phi - c Sigma/k^2 (no stress from the component).
(3) A tower whose sheets are held fixed responds to the projection of the gradient force onto the sheets:
    with GA rejection k_perp = (k ^ n) n^{-1}, g = k . k_perp / k^2 = k_perp^2/k^2 = 1 - (k . n)^2/(k^2 n^2)
    = sin^2(theta) at rational sample vectors, and its orientation average (1/2) int_{-1}^{1} (1 - u^2) du
    = 2/3 exactly.
The physical conclusion (no medium in the series, so g = 1) is an argument about the series' content, not a
computation.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
S3 = GA.sig(3, 0)
SAMPLES = [(F(3), F(1, 5), F(2, 3)), (F(1, 2), F(-4, 7), F(1, 3)), (F(5, 2), F(3, 11), F(0))]   # (k, psi, g)
PARAMS = [(F(2), F(1, 7), F(3, 5), F(1, 9), F(2, 3), F(5, 4)), (F(1, 3), F(-2, 5), F(4), F(-1, 2), F(1, 4), F(7))]
VECS = [((1, 2, 2), (0, 0, 1)), ((2, 3, 6), (1, 0, 0)), ((1, 4, 8), (2, -1, 2)), ((3, 0, 4), (0, 1, 0))]
HUBBLE, THETAS, DELTA = F(2, 7), (F(1), F(-3)), F(1, 10)
POTS = [(F(1, 3), F(2, 5), F(3, 2)), (F(-1, 7), F(1, 4), F(2))]                                 # (psi, phi, a)


def metric(psi, phi, a):
    g0 = GA.scal(a * (1 + psi), GA.gen(0))
    g1 = GA.scal(a * (1 - phi), GA.gen(1))
    return GA.dot(g0, g0, S13), GA.dot(g1, g1, S13)


def check_setting_derived_metric_linear_order():
    premise("dark-matter.imported-linear-momentum-equation-traceless-field")
    ok = True
    for psi, phi, a in POTS:
        gp, gm = metric(psi, phi, a), metric(-psi, -phi, a)
        g0 = metric(F(0), F(0), a)
        lin_tt, lin_xx = (gp[0] - gm[0]) / 2, (gp[1] - gm[1]) / 2
        ok = ok and g0 == (a * a, -a * a) and lin_tt == 2 * a * a * psi and lin_xx == 2 * a * a * phi
    _tp_rv = (ok); assert _tp_rv is not False, "check_setting_derived_metric_linear_order"; return _tp_rv


def check_unique_stress_for_reduced_response():
    premise("dark-matter.imported-linear-momentum-equation-traceless-field")
    ok = True
    sigmas = []
    for k, psi, g in SAMPLES:
        def residual(sigma, theta, H=HUBBLE):
            full = -H * theta + k * k * psi - k * k * sigma
            reduced = -H * theta + g * k * k * psi
            return full - reduced
        # residual is affine in sigma: residual = coef sigma + const, independent of theta
        th1, th2 = THETAS
        const, coef = residual(F(0), th1), residual(F(1), th1) - residual(F(0), th1)
        ok = ok and residual(F(0), th2) == const and coef == -k * k and coef != 0
        sigma = -const / coef
        ok = ok and residual(sigma, th2) == 0 and residual(sigma + DELTA, th2) != 0
        sigmas.append(sigma)
    _tp_rv = (ok and sigmas == [F(1, 15), F(-8, 21), F(3, 11)]); assert _tp_rv is not False, "check_unique_stress_for_reduced_response"; return _tp_rv


def check_potential_with_the_stress():
    premise("dark-matter.imported-linear-momentum-equation-traceless-field")
    ok = True
    for c, phi, k, Sig, rho, g in PARAMS:
        psi = (phi - c * Sig / (k * k)) / (1 + c * rho * (1 - g) / (k * k))
        sigma = (1 - g) * psi
        ok = ok and k * k * (phi - psi) == c * (rho * sigma + Sig)
        psi1 = (phi - c * Sig / (k * k)) / (1 + c * rho * (1 - 1) / (k * k))
        ok = ok and psi1 == phi - c * Sig / (k * k) and k * k * (phi - psi1) == c * Sig
    _tp_rv = (ok); assert _tp_rv is not False, "check_potential_with_the_stress"; return _tp_rv


def check_projected_response_and_orientation_average():
    ok = True
    for kv, nv in VECS:
        k = GA.add(*[GA.scal(x, GA.gen(i)) for i, x in enumerate(kv)])
        n = GA.add(*[GA.scal(x, GA.gen(i)) for i, x in enumerate(nv)])
        nn = GA.dot(n, n, S3)
        kperp = {b: c for b, c in GA.scal(1 / nn, GA.mul(GA.scal(F(1, 2), GA.sub(GA.mul(k, n, S3), GA.mul(n, k, S3))), n, S3)).items() if len(b) == 1}
        kk = GA.dot(k, k, S3)
        g = GA.dot(k, kperp, S3) / kk
        ok = ok and g == GA.dot(kperp, kperp, S3) / kk == 1 - GA.dot(k, n, S3) ** 2 / (kk * nn)
        ok = ok and GA.dot(kperp, n, S3) == 0
    anti = GA.ps_int([F(1), F(0), F(-1)])
    avg = (GA.peval(anti, F(1)) - GA.peval(anti, F(-1))) / 2
    _tp_rv = (ok and avg == F(2, 3)); assert _tp_rv is not False, "check_projected_response_and_orientation_average"; return _tp_rv
