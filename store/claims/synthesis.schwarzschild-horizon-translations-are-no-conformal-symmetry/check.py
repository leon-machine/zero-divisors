"""Conformal symmetries of the Schwarzschild field and the horizon's affine translations: exact checks.

Gauge Theory Gravity on flat spacetime, store sign (lib/gtg.py), Kerr-Schild gauge
hb^{-1}(a) = a - H (a.k) k, H = M/r, k = e_0 + x/r (null), at background points (0, 0, 0, z), so r = z; M = 1/2
(2M = 1, horizon at r = 1, kappa = 1/(4M) = 1/2). Jets of order 2 about each point; sqrt(r) rational at the
sampled radii.
(1) The field is Ricci-flat and I = 2<R(a^b) R(d_b^d_a)> = 48 M^2/r^6 at r = 1/4, 1, 9/4, 4, 9 (inside, on and
    outside the horizon; tabulated).
(2) Weight -4: for g' = Omega^2 g with Omega = (2M/r)^(3/2) and Omega = 2M/r the Weyl square of g' is
    Omega^-4 I (tabulated); for Omega = (2M/r)^(3/2) it is the constant 48 M^2/(2M)^6 = 12.
(3) The scalar curvature of g_hat = (2M/r)^3 g is (27 M - 9 r/2)/(2M)^3 at the five radii (tabulated), affine in r
    with slope -9/2 /(2M)^3, nonzero.
(4) The background time translation e_0 is a symmetry of the field (the coframe does not depend on t); its
    physical vector K = hb^{-1}(e_0) is null at r = 2M and (K.D)K = -kappa K there (store's D) with kappa = 1/2,
    timelike outside and spacelike inside, where (K.D)K is not along K.
(5) Control: a de Sitter instant (Friedmann a = 1, da/dt = d2a/dt2 = 1) has Weyl square 0, so g_hat is undefined
    there, as it must be for a field whose horizon translations are conformal symmetries.
"""
from fractions import Fraction as F
import GA
import gtg
from tp_premise import premise

J = gtg.Jet
E = [GA.gen(i) for i in range(4)]
M = F(1, 2)
RADII = [F(1, 4), F(1), F(9, 4), F(4), F(9)]


def _ks(z, pw=None):
    X = [J.var(i, F(v), 4, 2) for i, v in enumerate((0, 0, 0, z))]
    r = (X[1] * X[1] + X[2] * X[2] + X[3] * X[3]).sqrt()
    ri = r.inv()
    H = M * ri
    k = [J.const(1, 4), X[1] * ri, X[2] * ri, X[3] * ri]
    sgn = [1, -1, -1, -1]
    TH = [[None] * 4 for _ in range(4)]
    for mu in range(4):
        for a in range(4):
            TH[a][mu] = (J.const(1, 4) if a == mu else J.const(0, 4)) - H * (sgn[mu] * k[mu]) * k[a]
    if pw is not None:
        Om = (2 * M * ri).pw(pw)
        TH = [[Om * TH[a][mu] for mu in range(4)] for a in range(4)]
    return gtg.Field(TH)


def _weyl_sq(R):
    return gtg.kretschmann(gtg.weyl_op(R))


def check_weyl_square_of_the_schwarzschild_field():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    table = {F(1, 4): F(49152), F(1): F(12), F(9, 4): F(16384, 177147), F(4): F(3, 1024), F(9): F(4, 177147)}
    ok = True
    for z in RADII:
        R = _ks(z).curvature()
        ok = ok and gtg.ricci_flat(R) and gtg.kretschmann(R) == table[z] and _weyl_sq(R) == table[z]
        ok = ok and table[z] == 48 * M * M / z ** 6
    GA.check("Schwarzschild: Ricci-flat, Weyl square 48 M^2/r^6 inside, on and outside the horizon", ok)
    return ok


def check_weyl_square_has_conformal_weight_minus_four():
    premise("synthesis.imported-gtg-dictionary")
    # tabulated Weyl squares of Omega^2 g: (r, Omega exponent) -> value
    table = {(F(1, 4), F(3, 2)): F(12), (F(4), F(3, 2)): F(12), (F(9), F(3, 2)): F(12),
             (F(4), F(1)): F(3, 4), (F(9), F(1)): F(4, 27)}
    ok = True
    for (z, p), val in table.items():
        Wsq = _weyl_sq(_ks(z, p).curvature())
        ok = ok and Wsq == val
        # weight: Weyl square of Omega^2 g = Omega^-4 * 48 M^2 / r^6
        ok = ok and val == 48 * M * M / z ** 6 * (z / (2 * M)) ** int(4 * p)
    GA.check("Weyl square of Omega^2 g is Omega^-4 times that of g; constant 12 for Omega = (2M/r)^(3/2)", ok)
    return ok


def check_scalar_curvature_of_the_invariant_metric_separates_radii():
    premise("synthesis.imported-gtg-dictionary")
    table = {F(1, 4): F(99, 8), F(1): F(9), F(9, 4): F(27, 8), F(4): F(-9, 2), F(9): F(-27)}
    ok = True
    for z in RADII:
        Rh = gtg.ricci_scalar(_ks(z, F(3, 2)).curvature())
        ok = ok and Rh == table[z] and Rh == (27 * M - F(9, 2) * z) / (2 * M) ** 3
    # affine in r with nonzero slope
    zs = sorted(table)
    slopes = set((table[b] - table[a]) / (b - a) for a, b in zip(zs, zs[1:]))
    ok = ok and slopes == {F(-9, 2)}
    GA.check("g_hat = (2M/r)^3 g has scalar curvature (27M - 9r/2)/(2M)^3: affine, slope -9/2 at 2M = 1", ok)
    return ok


def check_killing_time_on_the_horizon_is_a_dilation():
    premise("synthesis.positive-null-energy-gives-r-premises")
    premise("synthesis.imported-gtg-dictionary")
    ok = True
    for z, sign in [(F(1), 0), (F(4), 1), (F(1, 4), -1)]:
        f = _ks(z)
        Kj = f.g[0]
        K = gtg.m_val(Kj)
        q = gtg.vdot(K, K)
        ok = ok and ((q > 0) - (q < 0)) == sign
        # the coframe is t-independent: d_0 of every coframe jet vanishes
        ok = ok and all(not f.TH[a][mu].d(0) for a in range(4) for mu in range(4))
        if sign == 0:
            # (K.D) K = D_{e_0} K = -kappa K in the store's D (left-action Omega), kappa = 1/(4M) = 1/2:
            # K is tangent to the generator, null, and not affinely parametrised, inaffinity kappa
            DK = f.cov(0, Kj)
            ok = ok and gtg.m_sub(DK, gtg.m_scal(F(-1, 2), K)) == {} and K != {}
        else:
            # off the horizon (K.D)K is not along K (tabulated r = 4: -(1/256) e_0 + (7/256) e_3, K = (7 e_0 - e_3)/8)
            DK = f.cov(0, Kj)
            ok = ok and gtg.vdot(DK, DK) * gtg.vdot(K, K) != gtg.vdot(DK, K) ** 2
    GA.check("Killing time: null on r = 2M with (K.D)K = -K/2, timelike outside, spacelike inside", ok)
    return ok


def check_de_sitter_control_has_no_invariant_metric():
    premise("synthesis.de-sitter-horizon-translation-is-conformal-null-rotation")
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    at = J.from_taylor(0, [F(1), F(1), F(1, 2)], 4)
    TH = [[J.const(0, 4) for _ in range(4)] for _ in range(4)]
    TH[0][0] = J.const(1, 4)
    for i in (1, 2, 3):
        TH[i][i] = at
    R = gtg.Field(TH).curvature()
    ok = _weyl_sq(R) == 0 and all(R[(a, b)] == {(a, b): F(1)} for a in range(4) for b in range(a + 1, 4))
    # whereas the Schwarzschild field at r = 4 has Weyl square 3/1024, nonzero
    ok = ok and _weyl_sq(_ks(F(4)).curvature()) == F(3, 1024)
    GA.check("de Sitter: Weyl square 0 (no invariant metric); Schwarzschild: nonzero", ok)
    return ok
