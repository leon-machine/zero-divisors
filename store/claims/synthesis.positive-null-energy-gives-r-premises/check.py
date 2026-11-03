"""Positive null energy gives the thermal premises: exact checks.

(1) The strip: on a horizon generator with affine parameter u, the positive-energy two-point functions of a
    chiral fermion are W-(x) = (i/2pi)/(x + i0) and W+(x) = (-i/2pi)/(x - i0), x = u - v. Continued in the
    dilation parameter, F(lambda) = e^{w lambda} W-(e^{lambda} u - v); with z = e^{i theta} on the unit
    circle (rational points z = (1 - t^2 + 2 i t)/(1 + t^2), theta = 2 arctan t) the denominator z q u - v
    (q = e^{Re lambda}) has no zero for 0 < theta < 2 pi when u, v > 0, approaches the real axis from above
    at theta -> 0+ and from below at theta -> 2 pi-; the weight 1/2, the only one preserving the CAR, gives
    the factor e^{i pi} that turns W-'s coefficient into W+'s. Controls: a point on the other side of the
    edge (u < 0) puts a zero at theta = pi; theta = pi is not a return; the negative-energy prescription
    reverses the boundary signs.
(2) The symbol: the Mellin symbol m = (i/2)(cot(pi s) - i), s = 1/2 + i omega, written with the positive
    rational q = e^{pi omega} (cos pi s = -i sinh pi omega, sin pi s = cosh pi omega), equals
    (1 + e^{beta h})^{-1} with h = -omega at beta = 2 pi and at no other tested beta, and satisfies the
    two-point KMS identity 1 - m = e^{beta h} m.
(3) The horizons: in ingoing Eddington-Finkelstein form the horizon generator d_v has non-affinity
    Gamma^v_vv = f'(r_h)/2, equal to 1/(4M) on Schwarzschild and -H on de Sitter (|kappa| = H); the affine
    parameter V = e^{kappa v}/kappa obeys V'' = kappa V' (exact truncated series); the future cosmological horizon,
    in the outgoing chart, has Gamma^u_uu = +H (the ingoing chart's -H is the past horizon); the Killing field is
    xi^V = kappa V, a dilation of V at rate kappa; the local boost rotor scales every null generator of the
    local Rindler plane about its edge point, u -> r^2 u, at unit rate in rapidity, fixing the edge.
(4) The pair: in the conformal model Cl(2,4) the null translation T = 1 + (alpha/2) l n_inf moves the
    generator, and the boost and the dilation (both unit bivectors) each conjugate it to the translation by
    r^2 alpha: the ax+b relation of Borchers' theorem; boost and dilation agree on the generator and differ
    off it.
(5) Positivity: for every rational p in the closed forward cone and every rational future null l,
    <l, p> >= 0, with equality only for p on the ray of l; a spacelike direction takes both signs.
Exact arithmetic only (Fractions, Gaussian rationals); pi is never evaluated.
"""
from fractions import Fraction as F
import GA
from GA import RF, QI
from tp_premise import premise

SQ4 = (1, -1, -1, -1)                 # store signature (+,-,-,-): e0, e1, e2, e3
SQ6 = (1, -1, -1, -1, 1, -1)          # Cl(2,4): e0, e1, e2, e3, e+, e-


def _m(sq, *xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, sq)
    return out


def _unit_circle(t):
    """z = e^{i theta} with t = tan(theta/2): exact Gaussian rational."""
    d = 1 + t * t
    return QI(F(1 - t * t) / d, F(2 * t) / d)


def _sign(x):
    return (x > 0) - (x < 0)


def check_half_generator_strip_is_kms_at_two_pi():
    premise("synthesis.n-plus-null-ground-state")
    premise("hawking.imported-quasi-free-kms-reduces-two")
    premise("hawking.i-state-continuum")
    # coefficients of the two orderings, in units of 1/(2 pi), and their i0 directions
    c_minus, s_minus = QI(0, 1), +1      # omega(psi*(v) psi(u)) = (i/2pi)/(u - v + i0)
    c_plus, s_plus = QI(0, -1), -1       # omega(psi(u) psi*(v)) = (-i/2pi)/(u - v - i0)
    GA.check("CAR: the two coefficients add to zero off the diagonal", c_minus + c_plus == 0)
    ts_pos = [F(1, 50), F(1, 7), F(1, 2), F(1), F(3), F(40)]
    ts = ts_pos + [-t for t in ts_pos]
    samples = [(F(1), F(1), F(1)), (F(2), F(3), F(1, 2)), (F(5, 3), F(7, 4), F(9, 5)), (F(1, 9), F(4), F(3))]
    for (u, v, q) in samples:
        for t in ts:
            D = _unit_circle(t) * (q * u) - v
            GA.check("no zero of z q u - v in the open strip (u, v > 0)", bool(D))
            GA.check("Im(z q u - v) has the sign of t: + on (0, pi), - on (pi, 2 pi)", _sign(D.im) == _sign(t))
            GA.check("theta in (0, 2 pi) is not a return: z q u - v != q u - v", D != QI(q * u - v))
        Dpi = QI(-1) * (q * u) - v
        GA.check("theta = pi: the reflected point, still no zero", bool(Dpi) and Dpi.re < 0)
        # boundary approach: theta -> 0+ is t -> 0+, theta -> 2 pi- is t -> 0-
        GA.check("theta -> 0+: approach from above, the +i0 of W-", _sign(_unit_circle(F(1, 10 ** 6)).im) == s_minus)
        GA.check("theta -> 2 pi-: approach from below, the -i0 of W+", _sign(_unit_circle(F(-1, 10 ** 6)).im) == s_plus)
    # tabulated denominators z q u - v at hand-computed points (t, u, v, q) -> value
    table = [((F(1), F(2), F(3), F(1, 2)), QI(-3, 1)),          # z = i
             ((F(-1), F(2), F(3), F(1, 2)), QI(-3, -1)),        # z = -i
             ((F(1, 2), F(1), F(1), F(1)), QI(F(-2, 5), F(4, 5))),  # z = (3 + 4i)/5
             ((F(2), F(5, 3), F(7, 4), F(9, 5)), QI(F(-71, 20), F(12, 5)))]  # z = (-3 + 4i)/5
    for (t, u, v, q), want in table:
        GA.check("tabulated: z q u - v", _unit_circle(t) * (q * u) - v == want)
    # control: a point on the other side of the edge gives a zero inside the strip, at theta = pi
    for (u, v) in [(F(-1), F(1)), (F(-2), F(3)), (F(-5, 3), F(7, 4))]:
        q = v / (-u)
        GA.check("control: u < 0 < v puts a zero of z q u - v at theta = pi", not bool(QI(-1) * (q * u) - v))
    # the weight is forced by the anticommutator: e^{lambda w} psi(e^lambda u) preserves {psi, psi*} = delta
    # iff e^{2 lambda w} e^{-lambda} = 1; at e^{lambda/2} = rho this is rho^{4w} rho^{-2} = 1 (w = k/4: rho^{k-2})
    forced = [F(k, 4) for k in range(8) if all(rho ** (k - 2) == 1 for rho in (F(3, 2), F(1, 5)))]
    GA.check("only w = 1/2 preserves the CAR among quarter weights", forced == [F(1, 2)])
    # its factor at 2 pi is e^{i pi} = -1 (i^2), carrying c_- to c_+; an integer weight (i^0 or i^4) would not
    GA.check("e^{i pi} c_- = c_+", QI(0, 1) * QI(0, 1) * c_minus == c_plus)
    GA.check("control: e^{2 pi i} c_- != c_+", QI(1) * c_minus != c_plus)
    # control: the negative-energy prescription swaps the i0 directions; the forward strip then mismatches
    GA.check("control: with -i0 for W- the boundary at theta -> 0+ does not match",
             _sign(_unit_circle(F(1, 10 ** 6)).im) != -s_minus)
    return True


def check_past_half_is_kms_for_the_future_boost():
    premise("hawking.imported-quasi-free-kms-reduces-two")
    premise("hawking.i-state-continuum")
    # past half u, v < 0, future-directed boost there: u -> e^{-lambda} u, weight e^{-lambda/2}.
    # F(lambda) = e^{-lambda/2} (i/2pi)/(e^{-lambda} u - v + i0); continue lambda -> lambda + i theta:
    # denominator conj(z) q' u - v with q' = e^{-Re lambda}, conj(z) = e^{-i theta}.
    ts_pos = [F(1, 50), F(1, 7), F(1, 2), F(1), F(3), F(40)]
    ts = ts_pos + [-t for t in ts_pos]
    for (u, v, qp) in [(F(-1), F(-1), F(1)), (F(-2), F(-3), F(1, 2)), (F(-5, 3), F(-7, 4), F(9, 5))]:
        for t in ts:
            D = _unit_circle(t).conj() * (qp * u) - v
            GA.check("past half: no zero in the open strip", bool(D))
            GA.check("past half: Im has the sign of t (u < 0)", _sign(D.im) == _sign(t))
    # weight factor e^{-i theta/2} at theta = 2 pi is e^{-i pi} = -1: maps i to -i, as for the future half
    GA.check("past half: e^{-i pi} * i = -i", QI(-1) * QI(0, 1) == QI(0, -1))
    # tabulated: t = 1 (theta = pi/2), u = -2, v = -3, q' = 1/2: conj(i)(-1) + 3 = 3 + i
    GA.check("tabulated past-half denominator", _unit_circle(F(1)).conj() * (F(1, 2) * F(-2)) - F(-3) == QI(3, 1))
    # control: the past-directed boost on the past half (u -> e^{lambda} u) has Im of sign -t: KMS at -2 pi
    for t in ts_pos:
        D = _unit_circle(t) * (F(1) * F(-2)) - F(-3)
        GA.check("control: wrong orientation on the past half reverses the sign", _sign(D.im) == -1)
    # Mellin: under u -> -u the past-half kernel is the complex conjugate of the future-half one, so its
    # symbol on u^{-1/2 + i w} is m(-w) = (1 + e^{2 pi w})^{-1}, the I-state for the reversed generator +w
    for q in [F(2), F(1, 3), F(7, 5)]:
        m_plus = lambda qq: 1 / (1 + (1 / qq) ** 2)          # m(w) with qq = e^{pi w}
        GA.check("m(-w) = (1 + e^{2 pi w})^{-1}", m_plus(1 / q) == 1 / (1 + q * q))
        GA.check("m(w) + m(-w) = 1", m_plus(q) + m_plus(1 / q) == 1)
    return True


def check_mellin_symbol_is_the_i_state_at_two_pi():
    premise("synthesis.n-plus-null-ground-state")
    premise("hawking.i-state-continuum")
    premise("hawking.imported-ideal-fermi-gas-uniqueness")
    for q in [F(2), F(1, 3), F(7, 5), F(11), F(1)]:
        # q = e^{pi omega}; cos(pi s) = -i sinh(pi omega), sin(pi s) = cosh(pi omega)
        sinh = (q - 1 / q) / 2
        cosh = (q + 1 / q) / 2
        cot = QI(0, -1) * sinh / cosh
        m = QI(0, 1) / 2 * (cot - QI(0, 1))
        GA.check("symbol is real", m.im == 0)
        ebh = {k: (1 / q) ** k for k in (1, 2, 4)}   # e^{beta h} with h = -omega, beta = k pi
        GA.check("m = (1 + e^{2 pi h})^{-1}", m == QI(1 / (1 + ebh[2])))
        if q != 1:
            GA.check("m != (1 + e^{pi h})^{-1}", m != QI(1 / (1 + ebh[1])))
            GA.check("m != (1 + e^{4 pi h})^{-1}", m != QI(1 / (1 + ebh[4])))
        GA.check("two-point KMS identity 1 - m = e^{2 pi h} m", QI(1) - m == m * ebh[2])
        GA.check("0 < m < 1", 0 < m.re < 1)
    return True


def check_horizon_boosts_dilate_affine_generators():
    premise("singularity.euclidean-section-period")
    premise("synthesis.de-sitter-static-boost-frozen-point")
    premise("synthesis.local-boost-temperature-is-local-regularity")
    r = RF.var()

    def nonaffinity(f, rh):
        # ingoing EF in (v, r): g = [[f, -1], [-1, 0]]; Gamma^v_vv = (1/2) g^{va}(2 d_v g_av - d_a g_vv) = -(1/2) g^{vr} f'
        g = [[f, RF.const(-1)], [RF.const(-1), RF.const(0)]]
        gi = GA.rf_mat_inverse(g)
        GA.check("inverse metric g^{vv} = 0, g^{vr} = -1", gi[0][0].is_zero() and gi[0][1].eqrf(RF.const(-1)))
        gam_v = RF.const(F(-1, 2)) * gi[0][1] * f.deriv()
        gam_r = RF.const(F(-1, 2)) * gi[1][1] * f.deriv()
        GA.check("Gamma^r_vv vanishes on the horizon (the generator stays at r_h)", gam_r.eval(rh) == 0)
        return gam_v.eval(rh)

    def nonaffinity_out(f, rh):
        # outgoing EF in (u, r): g = [[f, 1], [1, 0]]; Gamma^u_uu = (1/2) g^{ur}(2 d_u g_ru - d_r g_uu) = -(1/2) g^{ur} f'
        g = [[f, RF.const(1)], [RF.const(1), RF.const(0)]]
        gi = GA.rf_mat_inverse(g)
        GA.check("outgoing: g^{uu} = 0, g^{ur} = 1", gi[0][0].is_zero() and gi[0][1].eqrf(RF.const(1)))
        gam_r = RF.const(F(1, 2)) * gi[1][1] * f.deriv() * RF.const(-1)
        GA.check("outgoing: Gamma^r_uu vanishes on the horizon", gam_r.eval(rh) == 0)
        return (RF.const(F(-1, 2)) * gi[0][1] * f.deriv()).eval(rh)

    for M in [F(1), F(5, 3), F(500)]:
        f = RF.const(1) - RF.const(2 * M) / r
        kap = nonaffinity(f, 2 * M)
        GA.check("Schwarzschild: non-affinity of d_v on r = 2M is 1/(4M)", kap == 1 / (4 * M))
    for H in [F(1), F(1, 3), F(2, 7)]:
        f = RF.const(1) - RF.const(H * H) * r * r
        kap = nonaffinity(f, 1 / H)
        GA.check("de Sitter, ingoing chart (past horizon): non-affinity -H", kap == -H)
        GA.check("de Sitter, outgoing chart (future horizon): non-affinity +H", nonaffinity_out(f, 1 / H) == H)
    # tabulated surface gravities: Schwarzschild M -> kappa, de Sitter H -> Gamma^v_vv
    for M, want in [(F(2), F(1, 8)), (F(7, 3), F(3, 28)), (F(250), F(1, 1000))]:
        GA.check("tabulated Schwarzschild kappa", nonaffinity(RF.const(1) - RF.const(2 * M) / r, 2 * M) == want)
    for H, want in [(F(3), F(-3)), (F(5, 4), F(-5, 4))]:
        GA.check("tabulated de Sitter Gamma^v_vv (ingoing, past horizon)", nonaffinity(RF.const(1) - RF.const(H * H) * r * r, 1 / H) == want)
    for H, want in [(F(3), F(3)), (F(2, 7), F(2, 7))]:
        GA.check("tabulated de Sitter Gamma^u_uu (outgoing, future horizon)", nonaffinity_out(RF.const(1) - RF.const(H * H) * r * r, 1 / H) == want)
    GA.check("control: outgoing chart on Schwarzschild gives -1/(4M) (past horizon)",
             nonaffinity_out(RF.const(1) - RF.const(4) / r, F(4)) == F(-1, 8))
    # affine parameter V = e^{kappa v}/kappa: truncated series, V'' = kappa V' coefficientwise
    N = 12
    for kap in [F(1, 4), F(1, 3), F(1)]:
        fact = [1]
        for n in range(1, N + 2):
            fact.append(fact[-1] * n)
        V = [F(0)] + [kap ** (n - 1) / fact[n] for n in range(1, N + 1)]
        V1 = [V[n + 1] * (n + 1) for n in range(N)]
        V2 = [V1[n + 1] * (n + 1) for n in range(N - 1)]
        GA.check("V'' = kappa V' (affine reparametrisation)", all(V2[n] == kap * V1[n] for n in range(N - 1)))
        # the Killing field d_v reads xi^V = dV/dv = kappa V + 1: a dilation of V about V = -1/kappa
        GA.check("xi^V = kappa V + 1 coefficientwise", all(V1[n] == (kap * V[n] + (1 if n == 0 else 0)) for n in range(N)))
        Vv = RF.var()
        xi = RF.const(kap) * Vv
        GA.check("xi^V = kappa V has non-affinity kappa: xi dxi/dV = kappa xi", (xi * xi.deriv()).eqrf(RF.const(kap) * xi))
    # local Rindler: the boost rotor dilates every null generator about its edge point at unit rate
    e = [GA.gen(i) for i in range(4)]
    l = GA.add(e[0], e[1])
    n = GA.sub(e[0], e[1])
    for rr in [F(3, 2), F(1, 5), F(7)]:
        c, s = (rr + 1 / rr) / 2, (rr - 1 / rr) / 2
        B = GA.add(GA.sc(c), GA.scal(s, _m(SQ4, e[1], e[0])))
        act = lambda x: _m(SQ4, B, x, GA.reverse(B))
        GA.check("B is a rotor", GA.eq(_m(SQ4, B, GA.reverse(B)), GA.sc(1)))
        GA.check("generator dilated: B l B~ = r^2 l", GA.eq(act(l), GA.scal(rr * rr, l)))
        GA.check("other null direction: B n B~ = r^-2 n", GA.eq(act(n), GA.scal(1 / (rr * rr), n)))
        for y in (e[2], e[3], GA.add(e[2], GA.scal(F(2, 3), e[3]))):
            GA.check("edge point fixed: transverse y", GA.eq(act(y), y))
            u = F(5, 4)
            GA.check("null plane: u l + y -> r^2 u l + y", GA.eq(act(GA.add(GA.scal(u, l), y)), GA.add(GA.scal(rr * rr * u, l), y)))
    # tabulated: r = 3/2 sends 2 l to 9/2 l; r = 1/5 sends 5 l to 1/5 l
    for rr, u, want in [(F(3, 2), F(2), F(9, 2)), (F(1, 5), F(5), F(1, 5))]:
        c, s = (rr + 1 / rr) / 2, (rr - 1 / rr) / 2
        B = GA.add(GA.sc(c), GA.scal(s, _m(SQ4, e[1], e[0])))
        GA.check("tabulated generator dilation", GA.eq(_m(SQ4, B, GA.scal(u, l), GA.reverse(B)), GA.scal(want, l)))
    return True


def check_boost_and_dilation_conjugate_null_translations():
    premise("angle.imported-theorems-deliver-their-hypotheses")
    premise("mass.chart-form-spin-isomorphism")
    e = [GA.gen(i) for i in range(6)]
    ninf = GA.add(e[4], e[5])
    n0 = GA.scal(F(1, 2), GA.sub(e[4], e[5]))
    Q = lambda x: GA.dot(x, x, SQ6)
    X = lambda x: GA.add(n0, x, GA.scal(-F(1, 2) * Q(x), ninf))
    GA.check("<n0, n_inf> = 1, both null", GA.dot(n0, ninf, SQ6) == 1 and Q(n0) == 0 and Q(ninf) == 0)
    l = GA.add(e[0], e[1])
    T = lambda al: GA.add(GA.sc(1), GA.scal(al / 2, _m(SQ6, l, ninf)))
    sand = lambda R, x: _m(SQ6, R, x, GA.reverse(R))
    for al in [F(5, 7), F(-2), F(3)]:
        for u in [F(0), F(1, 3), F(-4)]:
            GA.check("T moves the generator: T X(u l) T~ = X((u + alpha) l)",
                     GA.eq(sand(T(al), X(GA.scal(u, l))), X(GA.scal(u + al, l))))
    for rr in [F(3, 2), F(2, 5)]:
        c, s = (rr + 1 / rr) / 2, (rr - 1 / rr) / 2
        B = GA.add(GA.sc(c), GA.scal(s, _m(SQ6, e[1], e[0])))
        Dl = GA.add(GA.sc(c), GA.scal(s, _m(SQ6, e[5], e[4])))
        GA.check("boost and dilation bivectors are unit boosts",
                 GA.eq(_m(SQ6, e[1], e[0], e[1], e[0]), GA.sc(1)) and GA.eq(_m(SQ6, e[5], e[4], e[5], e[4]), GA.sc(1)))
        for u in [F(1), F(-3, 4)]:
            x = GA.scal(u, l)
            GA.check("boost on the generator: X(u l) -> X(r^2 u l)", GA.eq(sand(B, X(x)), X(GA.scal(rr * rr, x))))
            GA.check("dilation on the generator: X(u l) -> r^-2 X(r^2 u l)",
                     GA.eq(sand(Dl, X(x)), GA.scal(1 / (rr * rr), X(GA.scal(rr * rr, x)))))
        y = e[2]
        GA.check("off the generator they differ: boost fixes X(e2), dilation does not",
                 GA.eq(sand(B, X(y)), X(y)) and not GA.eq(sand(Dl, X(y)), GA.scal(1 / (rr * rr), X(y))))
        for al in [F(5, 7), F(3)]:
            GA.check("ax+b: B T_alpha B~ = T_{r^2 alpha}", GA.eq(sand(B, T(al)), T(rr * rr * al)))
            GA.check("ax+b: D T_alpha D~ = T_{r^2 alpha}", GA.eq(sand(Dl, T(al)), T(rr * rr * al)))
            GA.check("control: not T_alpha (the conjugation rescales)", not GA.eq(sand(B, T(al)), T(al)))
    # hand-computed values of r^2 alpha: (3/2, 5/7) -> 45/28, (3/2, 3) -> 27/4, (2/5, 5/7) -> 4/35, (2/5, 3) -> 12/25
    expect = {(F(3, 2), F(5, 7)): F(45, 28), (F(3, 2), F(3)): F(27, 4), (F(2, 5), F(5, 7)): F(4, 35), (F(2, 5), F(3)): F(12, 25)}
    for (rr, al), want in expect.items():
        c, s = (rr + 1 / rr) / 2, (rr - 1 / rr) / 2
        B = GA.add(GA.sc(c), GA.scal(s, _m(SQ6, e[1], e[0])))
        Dl = GA.add(GA.sc(c), GA.scal(s, _m(SQ6, e[5], e[4])))
        GA.check("tabulated: B T_alpha B~ = T_want", GA.eq(sand(B, T(al)), T(want)))
        GA.check("tabulated: D T_alpha D~ = T_want", GA.eq(sand(Dl, T(al)), T(want)))
    # tabulated translations of the generator: u + alpha
    for (u, al, want) in [(F(1, 3), F(5, 7), F(22, 21)), (F(-4), F(3), F(-1)), (F(0), F(-2), F(-2))]:
        GA.check("tabulated: T X(u l) T~ = X(want l)", GA.eq(sand(T(al), X(GA.scal(u, l))), X(GA.scal(want, l))))
    return True


def check_point_spectrum_carries_no_dilated_translation():
    premise("synthesis.point-spectrum-boost-admits-no-half-sided-translations")
    # on a window the boost generator is K = diag(k_j) with real weights; solve [K, P] = i c P for the n x n
    # matrix P over Q(i): the linear map P -> (K P - P K) - i c P is diagonal on matrix units with entries
    # (k_j - k_l) - i c, so its kernel is spanned by the units with k_j - k_l = i c.
    def kernel_dim(ks, c):
        n = len(ks)
        M = []
        for j in range(n):
            for l in range(n):
                row = [QI(0)] * (n * n)
                row[j * n + l] = QI(ks[j] - ks[l]) - QI(0, c)
                M.append(row)
        return n * n - GA.field_rank(M)
    distinct = [F(0), F(1, 4), F(-3, 2), F(5)]
    repeated = [F(0), F(1, 4), F(1, 4), F(5)]
    GA.check("c = 0: commutant of distinct weights has dimension 4", kernel_dim(distinct, F(0)) == 4)
    GA.check("c = 0: a repeated weight enlarges the commutant to 6", kernel_dim(repeated, F(0)) == 6)
    for c in [F(1), F(-2, 3), F(1, 4)]:
        GA.check("c != 0: no nonzero P with [K, P] = i c P (distinct)", kernel_dim(distinct, c) == 0)
        GA.check("c != 0: no nonzero P with [K, P] = i c P (repeated)", kernel_dim(repeated, c) == 0)
    # contrast: a real (non-unitary) scaling equation [K, P] = c P does have solutions when c is a weight gap
    def real_kernel_dim(ks, c):
        n = len(ks)
        M = []
        for j in range(n):
            for l in range(n):
                row = [QI(0)] * (n * n)
                row[j * n + l] = QI(ks[j] - ks[l] - c)
                M.append(row)
        return n * n - GA.field_rank(M)
    GA.check("contrast: [K, P] = c P with c = k_2 - k_1 = 1/4 has a solution", real_kernel_dim(distinct, F(1, 4)) == 1)
    return True


def check_spectrum_condition_gives_positive_null_generators():
    premise("angle.imported-theorems-deliver-their-hypotheses")
    # rational unit 3-vectors from Pythagorean quadruples
    dirs = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(-1), F(0), F(0)), (F(2, 3), F(2, 3), F(1, 3)),
            (F(-2, 7), F(3, 7), F(-6, 7)), (F(1, 9), F(-4, 9), F(8, 9)), (F(3, 5), F(-4, 5), F(0))]
    nulls = [GA.add(GA.sc(0), GA.gen(0), *[GA.scal(c, GA.gen(i + 1)) for i, c in enumerate(d)]) for d in dirs]
    for lv in nulls:
        GA.check("l is null", GA.dot(lv, lv, SQ4) == 0)
    ps = []
    for p0 in [F(1), F(5, 2), F(13)]:
        for d in dirs:
            for frac in [F(0), F(1, 2), F(1)]:
                ps.append(GA.add(GA.scal(p0, GA.gen(0)), *[GA.scal(p0 * frac * c, GA.gen(i + 1)) for i, c in enumerate(d)]))
    ps.append(GA.add(GA.scal(F(7), GA.gen(0)), GA.scal(F(2), GA.gen(1)), GA.scal(F(-3), GA.gen(2)), GA.scal(F(6), GA.gen(3))))
    for p in ps:
        GA.check("p in the closed forward cone", GA.dot(p, p, SQ4) >= 0 and p.get((0,), F(0)) > 0)
        for lv in nulls:
            lp = GA.dot(lv, p, SQ4)
            GA.check("<l, p> >= 0", lp >= 0)
            if lp == 0:
                # equality only on the ray of l: p - (p0/l0) l = 0
                GA.check("equality only for p on the ray of l", GA.eq(p, GA.scal(p.get((0,), F(0)), lv)))
    sp = GA.gen(1)
    vals = {_sign(GA.dot(sp, p, SQ4)) for p in ps}
    GA.check("control: a spacelike translation takes both signs", 1 in vals and -1 in vals)
    return True
