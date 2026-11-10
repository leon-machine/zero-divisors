"""synthesis.number-n-free-at-fixed-d-term-level-on-the-stored-relations: exact checks.

Two models A and B of the stored rung field on the null-lift locus (lift family c_lambda: alpha = (H^2/lambda, 0),
beta = (-lambda, 0), norm N* = (H^4/lambda^2 + lambda^2)/2, m = (H^4/lambda^2 - lambda^2)/2, so N*^2 - m^2 = H^4)
with the potential V = V_D + kappa N*^2, V_D on the family = (1/2)(g^2 m^2/4 + g'^2 (m/2 - zeta)^2), xi = 2 zeta.
They share Newton's constant G = M_P^-2, the level xi, the couplings g, g', kappa, and differ in H^2 = Lambda/3:
  A: H = 48, lambda = 32;   B: H = 63, lambda = 49;   m = 2080 in both;   G = 1/1008^2, so N = M_P/H is 21 and 16.
Ambient space Cl(2,4) in GA.py, squares (e_0, e_1, e_2, e_3, e_+, e_-) = (+1, -1, -1, -1, +1, -1), n_inf = e_+ + e_-,
n_0 = (e_+ - e_-)/2, frozen point I_Lambda = n_inf + (Lambda/6) n_0 with Q(I_Lambda) = Lambda/3 (the stored chart).
(1) Both frames are critical points of V along the lift family at the SAME level xi = m (g^2 + g'^2 + 8 kappa)/g'^2
    (derivative of the rational function zero, second derivative positive), with m < N* (inside H < ... lambda < H).
(2) N differs (21 against 16) while xi G, g, g', kappa and every ratio of tree masses squared (fixed multiples of N*)
    agree; (v/M_P)^2 = 2 G N* differs, by N*_A^2 - N*_B^2 = H_A^4 - H_B^4 exactly; at N = 10^61 against 2 x 10^61
    with v/M_P = 2 x 10^-17 the relative change of (v/M_P)^4 is below 10^-176.
(3) The stored relations containing N hold in both: G Lambda = 3 N^-2; entropy coefficient S/pi = A/(4 pi G) = N^2;
    Casimir m_h^2/H^2 = (m_h/M_P)^2 N^2; G v^2 N^2 = (v/H)^2; N*^2 = m^2 + H^4; counts scale as N^2.
(4) Kinematic clause: the versor U = (37 e_+ - 5 e_-) e_+ fixes e_0..e_3 and carries I_{Lambda_A} to (16/21) I_{Lambda_B};
    for every pair of rational positive norms tried such a versor exists, so a function of the frozen point that is
    invariant under the isometries and under positive rescaling takes one value on them.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
NINF = GA.add(GA.gen(4), GA.gen(5))
N0 = GA.scal(F(1, 2), GA.sub(GA.gen(4), GA.gen(5)))
G_NEWTON = F(1, 1008 ** 2)
GC, GP, KAPPA = F(2, 3), F(1, 2), F(1, 5)
MODELS = {"A": (F(48), F(32)), "B": (F(63), F(49))}     # (H, lambda)


def I_of(lam):
    return GA.add(NINF, GA.scal(lam / 6, N0))


def frame(H, lam):
    H2 = H * H
    nstar = (H2 * H2 / (lam * lam) + lam * lam) / 2
    m = (H2 * H2 / (lam * lam) - lam * lam) / 2
    return H2, nstar, m


def level(m):
    return m * (GC * GC + GP * GP + 8 * KAPPA) / (GP * GP)


def V_family(H2, zeta):
    """V along the lift family as a rational function of lambda."""
    lam = GA.RF.var()
    c = GA.RF.const
    u2 = c(H2 * H2) / (lam * lam)
    nstar = (u2 + lam * lam) * c(F(1, 2))
    m = (u2 - lam * lam) * c(F(1, 2))
    half_m = m * c(F(1, 2))
    vd = (c(GC * GC / 4) * m * m + c(GP * GP) * (half_m - c(zeta)) * (half_m - c(zeta))) * c(F(1, 2))
    return vd + c(KAPPA) * nstar * nstar


def check_two_vacua_at_one_level_and_two_values_of_n():
    premise("synthesis.d-term-level-free-at-fixed-n")
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    xis, ns = [], []
    for H, lam in MODELS.values():
        H2, nstar, m = frame(H, lam)
        assert m == 2080 and nstar * nstar - m * m == H2 * H2 and 0 < lam < H
        xi = level(m)
        xis.append(xi)
        V = V_family(H2, xi / 2)
        d1 = V.deriv()
        assert d1.eval(lam) == 0 and d1.deriv().eval(lam) > 0
        assert d1.eval(lam + 1) != 0
        ns.append(1 / (G_NEWTON * H2))
    assert xis[0] == xis[1] == F(171808, 9)
    assert ns == [441, 256]                                  # N^2: N = 21 and N = 16
    return True


def check_dimensionless_spectrum_equal_and_weak_scale_moves_only_through_h4():
    premise("synthesis.constant-d-term-level-fixes-weak-scale-against-planck-under-promotion")
    premise("synthesis.d-term-level-free-at-fixed-n")
    spec, vmp, nst = [], [], []
    for H, lam in MODELS.values():
        H2, nstar, m = frame(H, lam)
        mw2 = GC * GC * nstar / 2
        mz2 = (GC * GC + GP * GP) * nstar / 2
        mh2 = mz2 + 4 * KAPPA * nstar
        mpm2 = mw2 + 4 * KAPPA * nstar
        spec.append((mw2 / mz2, mh2 / mz2, mpm2 / mz2, mz2 / nstar))
        vmp.append(2 * nstar * G_NEWTON)
        nst.append(nstar)
    assert spec[0] == spec[1] == (F(16, 25), F(413, 125), F(368, 125), F(25, 72))
    assert nst == [3104, 4481] and vmp[0] != vmp[1]
    assert nst[1] ** 2 - nst[0] ** 2 == 63 ** 4 - 48 ** 4     # the stored N*^2 = m*^2 + H^4, same m*
    # realistic sizes, Planck units G = 1: v^2 = 2 N*, v/M_P = 2e-17, H^2 = 1/N^2
    mstar = F(2, 10 ** 34)
    hA4, hB4 = F(1, 10 ** 244), F(1, 16 * 10 ** 244)          # N = 10^61 and 2 x 10^61
    rel = ((mstar ** 2 + hA4) - (mstar ** 2 + hB4)) / mstar ** 2   # relative change of N*^2, that is of (v/M_P)^4
    assert 0 < rel < F(1, 10 ** 176) and rel * 10 ** 177 > 2
    return True


def check_stored_relations_with_n_hold_in_both_models():
    premise("synthesis.smallness-monomials-exact-hierarchy-casimir")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    premise("synthesis.de-sitter-mode-count")
    n2s = []
    for H, lam in MODELS.values():
        H2, nstar, m = frame(H, lam)
        Lam = 3 * H2
        I = I_of(Lam)
        assert GA.dot(I, I, SQ) == H2                        # Q(I) = Lambda/3 = H^2
        n2 = 1 / (G_NEWTON * GA.dot(I, I, SQ))               # N^2 = M_P^2 / Q(I)
        assert G_NEWTON * Lam == 3 / n2
        area_over_pi = 4 / H2                                # A = 4 pi / H^2
        assert area_over_pi / (4 * G_NEWTON) == n2           # S = A/4G = pi N^2
        v2 = 2 * nstar
        assert G_NEWTON * v2 * n2 == v2 / H2
        mh2 = ((GC * GC + GP * GP) / 2 + 4 * KAPPA) * nstar
        assert mh2 / H2 == (mh2 * G_NEWTON) * n2             # Casimir -w(w+3) = (m/M_P)^2 N^2
        n2s.append(n2)
    assert n2s == [441, 256] and n2s[0] / n2s[1] == F(21, 16) ** 2   # entropy and counts scale as N^2
    return True


def check_isometry_and_rescaling_join_the_two_frozen_points():
    premise("standard-model.trichotomy-what-kind-number")
    premise("standard-model.imported-frozen-point-dictionary")
    cases = [(F(48), F(63)), (F(1), F(3)), (F(5, 7), F(2, 9))]
    for HA, HB in cases:
        mu = HA / HB
        p, q = mu.numerator, mu.denominator
        u1 = GA.gen(4)
        u2 = GA.add(GA.scal(p + q, GA.gen(4)), GA.scal(q - p, GA.gen(5)))
        U = GA.mul(u2, u1, SQ)
        n2 = GA.dot(u2, u2, SQ)
        assert n2 == 4 * p * q
        Ui = GA.scal(1 / n2, GA.mul(u1, u2, SQ))
        assert GA.eq(GA.mul(U, Ui, SQ), GA.sc(1))
        for i in range(4):
            assert GA.eq(GA.mul(GA.mul(U, GA.gen(i), SQ), Ui, SQ), GA.gen(i))
        IA, IB = I_of(3 * HA * HA), I_of(3 * HB * HB)
        img = GA.mul(GA.mul(U, IA, SQ), Ui, SQ)
        assert GA.eq(img, GA.scal(mu, IB))
        assert GA.dot(img, img, SQ) == GA.dot(IA, IA, SQ) == HA * HA
    U0 = GA.mul(GA.add(GA.scal(37, GA.gen(4)), GA.scal(-5, GA.gen(5))), GA.gen(4), SQ)
    assert GA.eq(U0, GA.add(GA.sc(37), GA.scal(5, GA.mul(GA.gen(4), GA.gen(5), SQ))))
    return True
