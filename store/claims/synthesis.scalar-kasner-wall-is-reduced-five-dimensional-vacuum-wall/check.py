"""synthesis.scalar-kasner-wall-is-reduced-five-dimensional-vacuum-wall: exact checks.

Diagonal metrics whose components depend on one coordinate T only, with T = s^N so that every power is a
Laurent monomial in s (GA.RF). Curvature by the formula of the stored plane-wave check
(Gamma^a_bc = 1/2 g^ad (...), R^a_bcd = d_c Gamma^a_db - ..., Ric_bd = R^a_bad), derivatives along T only.

  check_five_dimensional_vacuum: G = dT^2 - sum_{a=1..4} T^{2 P_a} dx_a^2 is Ricci-flat at three rational points
                     of the five-dimensional Kasner sphere (sum P = 1 = sum P^2), and not at a point off it.
  check_reduction:   g = T^{P_4} (dT^2 - sum_{i=1..3} T^{2 P_i} dx_i^2): the only nonzero Ricci component is, in the
                     store sign (Ric_store = -Ric_formula, as calibrated in the stored plane-wave check),
                     Ric_TT = -(3/2) P_4^2 / T^2 = -8 pi G (d_T phi)^2 for 8 pi G phi_T^2 = (3/2) P_4^2 / T^2, and
                     the wave operator of phi = log T vanishes: d_T(sqrt|g| g^TT d_T log T) = 0.
  check_exponents:   proper time tau = T^{1 + P_4/2}/(1 + P_4/2); g = dtau^2 - sum c_i tau^{2 p_i} dx_i^2 with
                     p_i = (P_i + P_4/2)/(1 + P_4/2); sum p = 1 and sum p^2 + c^2 = 1, c^2 = 8 pi G q^2 =
                     (3/2) P_4^2/(1 + P_4/2)^2, phi = q log tau; the inverse map recovers P.
  check_completed_residue: in Cl(1,4) (e0^2 = 1, e1..e3^2 = -1, e4^2 = -3/2 so that the scalar slot carries the
                     dilaton normalisation without square roots), B = sum p_i e0 e_i + (P_4/(1 + P_4/2)) e0 e4 squares
                     to 1; with e4^2 = -1 the five-dimensional residue B5 = sum_a P_a e0 e_a squares to 1, and
                     (1 + P_4/2) B_w = B5^(3) + (P_4/2) sum_i e0 e_i, B5^(3) the part of B5 along e1, e2, e3.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

SPHERE = [(F(1, 2), F(1, 2), F(1, 2), F(-1, 2)),
          (F(-2, 5), F(4, 5), F(1, 5), F(2, 5)),
          (F(2, 3), F(-1, 3), F(0), F(2, 3))]
OFF = (F(1, 2), F(1, 2), F(1, 4), F(-1, 4))     # sum 1, sum of squares 5/8


def lcm(a, b):
    x, y = a, b
    while y:
        x, y = y, x % y
    return a * b // x


def common_N(vals):
    n = 1
    for v in vals:
        n = lcm(n, F(v).denominator)
    return n


def mono(c, e):
    """c * s^e for integer e, as an RF."""
    e = int(e)
    if e >= 0:
        return RF([F(0)] * e + [F(c)])
    return RF([F(c)], [F(0)] * (-e) + [F(1)])


def diag_ricci(gd, dTds):
    """gd: list of RF (diagonal metric, coordinate 0 = T). Derivatives along coordinate 0 only."""
    n = len(gd)
    zero = RF.const(0)

    def d0(f):
        return f.deriv() / dTds
    gi = [RF.const(1) / x for x in gd]
    dg = [d0(x) for x in gd]
    half = RF.const(F(1, 2))
    Gam = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = zero
                # Gamma^a_bc = 1/2 g^aa (d_b g_ac + d_c g_ab - d_a g_bc), only d_0 nonzero, g diagonal
                if b == 0 and a == c:
                    s = s + dg[a]
                if c == 0 and a == b:
                    s = s + dg[a]
                if a == 0 and b == c:
                    s = s - dg[b]
                Gam[(a, b, c)] = gi[a] * s * half
    Ric = [[zero] * n for _ in range(n)]
    for b in range(n):
        for d in range(n):
            s = zero
            for a in range(n):
                # R^a_bad = d_a Gamma^a_db - d_d Gamma^a_ab + Gamma^a_ae Gamma^e_db - Gamma^a_de Gamma^e_ab
                if a == 0:
                    s = s + d0(Gam[(a, d, b)])
                if d == 0:
                    s = s - d0(Gam[(a, a, b)])
                for e in range(n):
                    s = s + Gam[(a, a, e)] * Gam[(e, d, b)] - Gam[(a, d, e)] * Gam[(e, a, b)]
            Ric[b][d] = s
    return Ric


def kasner5(P):
    N = common_N(list(P))
    s = RF.var()
    T = mono(1, N)
    dTds = mono(N, N - 1)
    gd = [RF.const(1)] + [-mono(1, 2 * N * Pa) for Pa in P]
    return gd, T, dTds


def check_five_dimensional_vacuum():
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    for P in SPHERE:
        assert sum(P) == 1 and sum(x * x for x in P) == 1
        gd, T, dTds = kasner5(P)
        Ric = diag_ricci(gd, dTds)
        assert all(Ric[i][j].is_zero() for i in range(5) for j in range(5))
    gd, T, dTds = kasner5(OFF)
    Ric = diag_ricci(gd, dTds)
    assert not Ric[0][0].is_zero()
    return True


def reduced(P):
    P4 = P[3]
    N = common_N([P4, 2 * P[0], 2 * P[1], 2 * P[2]])
    T = mono(1, N)
    dTds = mono(N, N - 1)
    gd = [mono(1, N * P4)] + [-mono(1, N * (P4 + 2 * P[i])) for i in range(3)]
    return gd, T, dTds, N


def check_reduction():
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    for P in SPHERE:
        P4 = P[3]
        gd, T, dTds, N = reduced(P)
        Ric = diag_ricci(gd, dTds)
        for i in range(4):
            for j in range(4):
                if (i, j) != (0, 0):
                    assert Ric[i][j].is_zero()
        # store sign (Ric_store = -Ric_formula, Ric_store = Lambda g on de Sitter): Ric_store_TT = -8 pi G phi_T^2
        target = RF.const(-F(3, 2) * P4 * P4) / (T * T)
        assert (-Ric[0][0]).eqrf(target)
        # wave operator on phi = log T: sqrt|g| g^TT d_T phi = T^{1 + P4} T^{-P4} T^{-1} = 1
        sqrtg_N = N * (2 * P4 + 1 - P4)          # exponent of s in sqrt|g| (with sum P_i = 1 - P4)
        assert sum(P[:3]) == 1 - P4
        flux = mono(1, sqrtg_N) * (RF.const(1) / gd[0]) * (RF.const(1) / T)
        assert flux.eqrf(RF.const(1))
    # control off the sphere: P = (1/2, 1/2, 1/4, -1/4) has sum 1 but sum of squares 5/8, and Ric_TT is not
    # -8 pi G phi_T^2 there
    gd, T, dTds, N = reduced(OFF)
    Ric = diag_ricci(gd, dTds)
    assert not (-Ric[0][0]).eqrf(RF.const(-F(3, 2) * OFF[3] * OFF[3]) / (T * T))
    return True


def exponents(P):
    P4 = P[3]
    k = 1 + P4 / 2
    p = [(P[i] + P4 / 2) / k for i in range(3)]
    c2 = F(3, 2) * P4 * P4 / (k * k)
    return p, c2, k


def check_exponents():
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    for P in SPHERE:
        P4 = P[3]
        p, c2, k = exponents(P)
        # g_ii = -T^{P4 + 2 P_i} = -(k tau)^{2 p_i}: exponent identity P4 + 2 P_i = 2 p_i k
        for i in range(3):
            assert P4 + 2 * P[i] == 2 * p[i] * k
        # dtau = T^{P4/2} dT, tau = T^k / k
        assert k - 1 == P4 / 2
        assert sum(p) == 1
        assert sum(x * x for x in p) + c2 == 1
        # 8 pi G q^2 with phi = q log tau = q k log T and 8 pi G phi_T^2 T^2 = (3/2) P4^2
        q2_8piG = F(3, 2) * P4 * P4 / (k * k)
        assert q2_8piG == c2
        # inverse map from (p, c) with c = sqrt(3/2) P4 / k: P4 = c/(sqrt(3/2) - c/2); checked on c^2
        # via P4 / k = 2 P4 / (2 + P4), and P_i = p_i k - P4/2
        for i in range(3):
            assert p[i] * k - P4 / 2 == P[i]
    # the identity sum p^2 + 8 pi G q^2 = 1 + (S2 - 1)/k^2 for sum P = 1, also off the sphere
    for P in SPHERE + [OFF]:
        p, c2, k = exponents(P)
        S2 = sum(x * x for x in P)
        assert sum(P) == 1
        assert sum(x * x for x in p) + c2 == 1 + (S2 - 1) / (k * k)
    p, c2, k = exponents(OFF)
    assert sum(x * x for x in p) + c2 != 1
    # the quiescent point: all p positive
    p, c2, k = exponents(SPHERE[0])
    assert p == [F(1, 3)] * 3 and c2 == F(2, 3)
    p, c2, k = exponents(SPHERE[1])
    assert p == [F(-1, 6), F(5, 6), F(1, 3)] and c2 == F(1, 6)
    return True


def blade_sum(terms):
    out = {}
    for blade, c in terms:
        out[blade] = out.get(blade, F(0)) + c
    return {b: c for b, c in out.items() if c != 0}


def check_completed_residue():
    premise("synthesis.unit-boost-residue-needs-nonpositive-exponent")
    premise("dark-energy.frozen-point-datum-kasner-wall")
    sq_dil = [F(1), F(-1), F(-1), F(-1), F(-3, 2)]
    sq_5 = [F(1), F(-1), F(-1), F(-1), F(-1)]
    for P in SPHERE:
        P4 = P[3]
        p, c2, k = exponents(P)
        e = [GA.gen(i) for i in range(5)]

        def biv(i, j, sq):
            return GA.mul(e[i], e[j], sq)
        B = GA.add(*[GA.scal(p[i], biv(0, i + 1, sq_dil)) for i in range(3)],
                   GA.scal(P4 / k, biv(0, 4, sq_dil)))
        assert GA.eq(GA.mul(B, B, sq_dil), GA.sc(1))
        Bw = GA.add(*[GA.scal(p[i], biv(0, i + 1, sq_dil)) for i in range(3)])
        assert GA.eq(GA.mul(Bw, Bw, sq_dil), GA.sc(1 - c2))
        B5 = GA.add(*[GA.scal(P[a], biv(0, a + 1, sq_5)) for a in range(4)])
        assert GA.eq(GA.mul(B5, B5, sq_5), GA.sc(1))
        B53 = GA.add(*[GA.scal(P[i], biv(0, i + 1, sq_5)) for i in range(3)])
        Biso = GA.add(*[biv(0, i + 1, sq_5) for i in range(3)])
        Bw5 = GA.add(*[GA.scal(p[i], biv(0, i + 1, sq_5)) for i in range(3)])
        assert GA.eq(GA.scal(k, Bw5), GA.add(B53, GA.scal(P4 / 2, Biso)))
    return True
