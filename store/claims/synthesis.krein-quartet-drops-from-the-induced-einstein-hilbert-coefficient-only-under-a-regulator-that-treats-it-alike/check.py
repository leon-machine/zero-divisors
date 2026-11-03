"""The Krein quartet in the induced Einstein-Hilbert coefficient: exact checks.

Weights are contributions to the induced Einstein-Hilbert coefficient in units of one minimally coupled real
scalar, read from the t^-1 coefficient of a heat trace (four dimensions) or from the zero-point sum on the
Einstein static field. Checks:
(1) GA curvature: on the Einstein static field R x S^3 (unit radius) Ric = (0, 2, 2, 2), R = 6; on the unit
    four-sphere Ric = 3, R = 12; the Feynman-gauge vector density tr(E + R/6), E = -Ric, is -2 scalar units on
    both, so with two ghosts the vector weight is -4.
(2) Einstein static field, energy cut-off, Feynman gauge: the time component (scalar harmonics), the
    longitudinal component (exact one-forms, l >= 1) and the ghost and antighost (scalar harmonics, fermionic)
    all have omega^2 = l(l + 2); their signed multiplicities cancel at every l >= 1 and leave one mode of zero
    energy at l = 0. The coexact one-forms (omega = l + 1, multiplicity 2l(l + 2)) are the attachment's helicity
    +-1 modules. The S^3 spectra reproduce the heat-kernel densities (sqrt(pi) units).
(3) The gauge-fixed operator P_alpha = Q(k) - (1 - 1/alpha) k (k . ) in momentum space (GA): transverse
    eigenvalue Q(k), longitudinal Q(k)/alpha.
(4) Unit four-sphere: scalar and coexact one-form spectra reproduce the heat-kernel densities exactly (volume and
    tr(E + R/6), with Ric from GA).
(5) Heat-kernel cut-off on the gauge-fixed operators: vector weight alpha - 5 (transverse -3, longitudinal alpha,
    ghosts -2); Lambda^4 weight 1 + alpha^2; the gauge-invariant reading det_T^-1/2 det_0^1/2 gives -4.
(6) The series' content: B = N_W - 4 N_V + 8(1 - 6 xi_R) + N_V (alpha - 1) chi, chi = 1 for the heat-kernel
    cut-off on the gauge-fixed operators and 0 for the energy cut-off.
Exact arithmetic only (Fractions; polynomials in the heat-kernel time).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SAKHAROV = "synthesis.imported-sakharov-induced-gravity-coefficients"
STORED = "synthesis.attachment-modules-give-sakharov-weights-cancelling-at-three-separate-generations"


# ------------------------------------------------------------------ helpers (no asserted values here)
def ricci_map(n, curved, kappa):
    """Euclidean Cl(n,0), curvature R(e_i ^ e_j) = kappa e_i ^ e_j for i, j in `curved`, else 0.
    Returns the list Ric(e_a) = sum_b e_b . R(e_b ^ e_a) (grade-one part of e_b R(e_b ^ e_a))."""
    sq = GA.sig(n, 0)
    out = []
    for a in range(n):
        acc = {}
        for b in range(n):
            if b == a or a not in curved or b not in curved:
                continue
            Rb = GA.scal(kappa, GA.mul(GA.gen(b), GA.gen(a), sq))
            prod = GA.mul(GA.gen(b), Rb, sq)
            acc = GA.add(acc, {kk: v for kk, v in prod.items() if len(kk) == 1})
        out.append(acc)
    return out


def diag(vecs):
    return [vecs[a].get((a,), F(0)) for a in range(len(vecs))]


def binom(n, r):
    if r < 0 or n < r:
        return 0
    num, den = 1, 1
    for i in range(r):
        num *= n - i
        den *= i + 1
    return num // den


def harmonic_count(dim_ambient, l):
    """Dimension of the harmonic homogeneous polynomials of degree l on R^dim_ambient."""
    return binom(l + dim_ambient - 1, dim_ambient - 1) - binom(l + dim_ambient - 3, dim_ambient - 1)


def fact(j):
    out = 1
    for i in range(2, j + 1):
        out *= i
    return out


def polar_halfgrid(p, c):
    """Polar part {-j: coef} at t = 0 of sum over nu in 1/2 + Z>=0 of p(nu) exp(-t(nu^2 - c)), p an odd
    polynomial {power: coef}. The polar part is that of the integral over (0, oo) (midpoint Euler-Maclaurin;
    the endpoint corrections are odd derivatives at 0, polynomial in t): int nu^(2j+1) e^{-t nu^2} = j!/(2 t^(j+1))."""
    base = {}
    for pw, co in p.items():
        j = (pw - 1) // 2
        base[-(j + 1)] = base.get(-(j + 1), F(0)) + F(co) * F(fact(j), 2)
    out = {}
    for e, co in base.items():
        m = 0
        while e + m < 0:
            out[e + m] = out.get(e + m, F(0)) + co * F(c) ** m / fact(m)
            m += 1
    return out


def polar_intgrid_even(p, c):
    """Polar part, in units of sqrt(pi), of sum over k in Z>=0 of p(k) exp(-t(k^2 - c)), p an even polynomial:
    int_0^oo k^(2j) e^{-t k^2} dk = Gamma(j + 1/2)/(2 t^(j + 1/2)), Gamma(j + 1/2) = sqrt(pi) (2j)!/(4^j j!).
    Keys are half-integers (the power of t)."""
    base = {}
    for pw, co in p.items():
        j = pw // 2
        g = F(fact(2 * j), 4 ** j * fact(j))
        key = -F(2 * j + 1, 2)
        base[key] = base.get(key, F(0)) + F(co) * g / 2
    out = {}
    for e, co in base.items():
        m = 0
        while e + m < 0:
            out[e + m] = out.get(e + m, F(0)) + co * F(c) ** m / fact(m)
            m += 1
    return out


def addp(*ps):
    out = {}
    for p in ps:
        for kk, v in p.items():
            out[kk] = out.get(kk, F(0)) + v
    return {kk: v for kk, v in out.items() if v != 0}


def scalp(c, p):
    return {kk: F(c) * v for kk, v in p.items()}


def s4_scalar():
    # lambda = l(l + 3) = nu^2 - 9/4, nu = l + 3/2; multiplicity (l+1)(l+2)(2l+3)/6 = nu(nu^2 - 1/4)/3
    return polar_halfgrid({3: F(1, 3), 1: F(-1, 12)}, F(9, 4))


def s4_coexact():
    # lambda = (l+1)(l+2) = nu^2 - 1/4; multiplicity l(l+3)(2l+3)/2 = nu(nu^2 - 9/4), l >= 1 (zero at l = 0)
    return polar_halfgrid({3: F(1), 1: F(-9, 4)}, F(1, 4))


def vector_weights(alpha):
    """(t^-1 weight, t^-2 weight) of one gauge vector with its two ghosts under a heat-kernel cut-off on the
    gauge-fixed operators, in units of one minimal scalar. Longitudinal sector: scalar spectrum over alpha."""
    sc, co = s4_scalar(), s4_coexact()
    w1 = (co[-1] + alpha * sc[-1] - 2 * sc[-1]) / sc[-1]
    w2 = (co[-2] + alpha ** 2 * sc[-2] - 2 * sc[-2]) / sc[-2]
    return w1, w2


# ------------------------------------------------------------------ checks
def check_einstein_static_and_sphere_curvature_and_vector_density():
    premise(SAKHAROV)
    premise("synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres")  # coexact one-form spectrum on S^3
    esu = ricci_map(4, {1, 2, 3}, F(1))
    s4 = ricci_map(4, {0, 1, 2, 3}, F(1))
    R_esu, R_s4 = sum(diag(esu)), sum(diag(s4))
    ok = diag(esu) == [0, 2, 2, 2] and R_esu == 6 and diag(s4) == [3, 3, 3, 3] and R_s4 == 12
    for ric, R in ((esu, R_esu), (s4, R_s4)):
        unit = R / 6                                  # minimal scalar: tr(E + R/6) = R/6
        vec = sum(-x for x in diag(ric)) + 4 * R / 6  # E = -Ric on four components
        ghosts = -2 * unit
        ok = ok and vec / unit == -2 and (vec + ghosts) / unit == -4
        # Weyl fermion: Lichnerowicz E = (1/2) sum_{a<b} e_a e_b R(e_a ^ e_b), two components, fermion sign
    sq = GA.sig(4, 0)
    for ric_planes, R in (({1, 2, 3}, R_esu), ({0, 1, 2, 3}, R_s4)):
        E = {}
        for a in range(4):
            for b in range(a + 1, 4):
                if a in ric_planes and b in ric_planes:
                    eab = GA.mul(GA.gen(a), GA.gen(b), sq)
                    E = GA.add(E, GA.scal(F(1, 2), GA.mul(eab, eab, sq)))
        lich = E.get((), F(0))
        weyl = -2 * (lich + R / 6) / (R / 6)
        ok = ok and lich == -R / 4 and weyl == 1
    assert ok
    return ok


def check_quartet_cancels_level_by_level_on_the_einstein_static_field():
    premise(SAKHAROV)
    premise(STORED)
    premise("synthesis.krein-form-premise-indefinite-inner-product-for-gauge-fields")  # (K1): zero-point sign of the negative-norm time component
    premise("synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres")
    ok = True
    for l in range(0, 40):
        scalar_mult = harmonic_count(4, l)            # scalar harmonics on S^3, eigenvalue l(l + 2)
        ok = ok and scalar_mult == (l + 1) ** 2
        exact_mult = scalar_mult if l >= 1 else 0     # d of a nonconstant harmonic, same eigenvalue
        time_comp = scalar_mult                       # A_0: Ric(e_0) = 0, minimal scalar on R x S^3
        signed = time_comp + exact_mult - 2 * scalar_mult
        ok = ok and signed == (-1 if l == 0 else 0)
        # physical modes: coexact one-forms, omega = l + 1, multiplicity 2 l (l + 2) = 2 (k^2 - 1), k = l + 1:
        # the helicity +-1 modules, n = k - 2, multiplicity (n + 1)(n + 3)
        if l >= 1:
            n = l - 1
            ok = ok and 2 * l * (l + 2) == 2 * (n + 1) * (n + 3)
    # zero-point energy of the quartet: only l = 0 survives, at omega^2 = 0 * (0 + 2) = 0
    ok = ok and 0 * (0 + 2) == 0
    # the S^3 spectra reproduce the heat-kernel densities: (sqrt(pi)/4) t^-3/2 (rank + t tr(E + R/6))
    esu = ricci_map(4, {1, 2, 3}, F(1))
    ric3 = diag(esu)[1:]
    R3 = sum(ric3)
    scal = polar_intgrid_even({2: 1}, 1)                     # sum k^2 e^{-t(k^2 - 1)}, k = l + 1
    coex = polar_intgrid_even({2: 2, 0: -2}, 0)              # sum 2(k^2 - 1) e^{-t k^2}
    total1 = addp(coex, scal)                                # one-forms: coexact + exact (exact = scalar, l >= 1)
    q = F(1, 4)
    ok = ok and scal == {F(-3, 2): q, F(-1, 2): q * (R3 / 6)}
    tr1 = sum(-x for x in ric3) + 3 * R3 / 6
    ok = ok and total1 == {F(-3, 2): 3 * q, F(-1, 2): q * tr1}
    assert ok
    return ok


def check_gauge_fixed_operator_has_longitudinal_eigenvalue_over_alpha():
    sq = GA.sig(4, 0)
    k = GA.add(GA.scal(2, GA.gen(0)), GA.scal(-1, GA.gen(1)), GA.scal(3, GA.gen(3)))
    Qk = GA.mul(k, k, sq)[()]
    trans = [GA.add(GA.scal(1, GA.gen(0)), GA.scal(2, GA.gen(1))), GA.gen(2),
             GA.add(GA.scal(3, GA.gen(1)), GA.scal(1, GA.gen(3)))]
    ok = Qk == 14 and all(GA.dot(k, t, sq) == 0 for t in trans)
    for alpha in (F(1, 3), F(1), F(5, 2)):
        def P(a):
            return GA.sub(GA.scal(Qk, a), GA.scal((1 - 1 / alpha) * GA.dot(k, a, sq), k))
        ok = ok and GA.eq(P(k), GA.scal(Qk / alpha, k))
        ok = ok and all(GA.eq(P(t), GA.scal(Qk, t)) for t in trans)
    assert ok
    return ok


def check_four_sphere_spectra_reproduce_heat_kernel_densities():
    premise(SAKHAROV)
    premise("synthesis.imported-ikeda-taniguchi-spectra-of-the-hodge-laplacian-on-spheres")  # scalar and coexact one-form spectra on S^4
    ok = all(harmonic_count(5, l) * 6 == (l + 1) * (l + 2) * (2 * l + 3) for l in range(30))
    s4 = ricci_map(4, {0, 1, 2, 3}, F(1))
    R = sum(diag(s4))
    vol = F(1, 6)                     # Vol(S^4)/(4 pi)^2 = (8 pi^2 / 3)/(16 pi^2)
    sc, co = s4_scalar(), s4_coexact()
    ok = ok and sc == {-2: vol, -1: vol * R / 6}
    tr1 = sum(-x for x in diag(s4)) + 4 * R / 6
    one_forms = addp(co, sc)          # exact one-forms carry the nonzero scalar spectrum
    ok = ok and one_forms == {-2: 4 * vol, -1: vol * tr1}
    assert ok
    return ok


def check_vector_weight_is_alpha_minus_five():
    premise(SAKHAROV)
    premise(STORED)
    ok = True
    for alpha in (F(0), F(1, 2), F(1), F(2), F(3)):
        w1, w2 = vector_weights(alpha)
        ok = ok and w1 == alpha - 5 and w2 == 1 + alpha ** 2
    sc, co = s4_scalar(), s4_coexact()
    ok = ok and (co[-1] - sc[-1]) / sc[-1] == -4      # det_T^-1/2 det_0^+1/2, one cut-off
    ok = ok and (co[-2] - sc[-2]) / sc[-2] == 2       # two helicities in the volume term
    ok = ok and vector_weights(F(1))[0] == -4
    assert ok
    return ok


def check_series_content_induced_coefficient():
    premise(SAKHAROV)
    premise(STORED)
    premise("standard-model.connection-forced")
    premise("synthesis.slot-module-light-ray-arrays-are-weyl-components")
    premise("synthesis.linear-rung-field-has-a-neutral-normal-pair-in-the-scalon-sum")
    NV = (3 * 3 - 1) + (2 * 2 - 1) + 1
    NW = 16 * 3
    NS = 2 * 4                                         # two doublets, four real components each

    def B(alpha, xi, chi):
        w1 = vector_weights(alpha)[0] if chi else F(-4)
        return NW + NV * w1 + NS * (1 - 6 * xi)
    ok = NV == 12 and NS == 8
    ok = ok and B(F(1), F(1, 6), 1) == 0 and B(F(7), F(1, 6), 0) == 0
    ok = ok and B(F(0), F(1, 6), 1) == -12 and B(F(0), F(0), 1) == -4
    ok = ok and B(F(1), F(0), 1) == 8 and B(F(1), F(0), 0) == 8
    for alpha in (F(0), F(1, 2), F(2)):
        for xi in (F(0), F(1, 6), F(1, 4)):
            ok = ok and B(alpha, xi, 1) == 12 * (alpha - 1) + 8 * (1 - 6 * xi)
            ok = ok and B(alpha, xi, 0) == 8 * (1 - 6 * xi)
    # the stored cancellation survives the heat-kernel cut-off only on the line 12 (alpha - 1) = -8 (1 - 6 xi)
    ok = ok and B(F(1, 3), F(0), 1) == 0
    assert ok
    return ok
