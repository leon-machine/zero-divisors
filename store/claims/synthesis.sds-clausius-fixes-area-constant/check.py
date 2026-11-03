"""synthesis.schwarzschild-de-sitter-clausius-fixes-area-constant: exact checks.

pi is a formal symbol: an entropy is recorded by its coefficient of pi (S = pi * s).
Units G = hbar = 1, L2 = ell^2 = 3/Lambda rational. Along the family at fixed L2 the mass is
read as a function of a horizon radius, M(r) = r (1 - r^2/L2)/2, a rational function of r.
"""
from fractions import Fraction as F
import GA
from GA import RF, add, sub, scal, gen, mul
from tp_premise import premise

# horizon pairs (r_b, r_c), 0 < r_b < r_c, both rational; L2 = r_b^2 + r_b r_c + r_c^2
PAIRS = [(F(1), F(2)), (F(1, 3), F(5)), (F(2, 7), F(3, 2)), (F(1, 10), F(1)), (F(4, 5), F(9, 10))]


def f_val(M, L2, r):
    return 1 - 2 * M / r - r * r / L2


def fprime(M, L2, r):
    return 2 * M / (r * r) - 2 * r / L2


def dot6(a, b, sq):
    return add(mul(a, b, sq), mul(b, a, sq)).get((), F(0)) / 2


def check_sds_clausius():
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.quarter-from-temperature")
    premise("synthesis.de-sitter-temperature-frozen-point-norm")
    premise("standard-model.imported-frozen-point-dictionary")
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    r = RF.var()
    for rb, rc in PAIRS:
        L2 = rb * rb + rb * rc + rc * rc
        M = rb * rc * (rb + rc) / (2 * L2)
        # both are horizons, ordered, and bracket the Nariai radius^2 = L2/3; r_c < ell
        assert f_val(M, L2, rb) == 0 and f_val(M, L2, rc) == 0
        assert 3 * rb * rb < L2 < 3 * rc * rc and rc * rc < L2
        # the third root is -(r_b + r_c) < 0: r f(r) L2 = -(r - rb)(r - rc)(r + rb + rc)
        for t in (F(1, 2), F(3), F(7, 3)):
            assert t * f_val(M, L2, t) * L2 == -(t - rb) * (t - rc) * (t + rb + rc)
        # mass along the family at fixed L2, as a function of either horizon radius
        Mr = r * (RF.const(1) - r * r / RF.const(L2)) / RF.const(2)
        assert Mr.eval(rb) == M and Mr.eval(rc) == M
        dM = Mr.deriv()
        # Clausius on each horizon: T_h = |f'(r_h)|/(4 pi), dS_h/dr_h = 2 pi r_h (coefficient of pi: 2 r_h)
        # black hole: f' > 0 and dM = T_b dS_b ; cosmological: f' < 0 and dM = -T_c dS_c
        assert fprime(M, L2, rb) > 0 and fprime(M, L2, rc) < 0
        Tb_4pi = fprime(M, L2, rb)          # 4 pi T_b
        Tc_4pi = -fprime(M, L2, rc)         # 4 pi T_c
        assert dM.eval(rb) == Tb_4pi / 4 * (2 * rb)      # (4 pi T / 4 pi) * (2 pi r) = T dS/dr
        assert dM.eval(rc) == -Tc_4pi / 4 * (2 * rc)
        # the general identity: dM/dr = r f'(r)/2 on the horizon locus, i.e. (1 - 3 r^2/L2)/2
        assert dM.eval(rb) == (1 - 3 * rb * rb / L2) / 2
        # so S_h / pi = r_h^2 + c_h / pi: the antiderivative of 2 r is r^2, unique up to a constant
        # MacDowell-Mansouri constant c = -pi L2: both horizons negative, the hole by at least 2 L2/3
        assert rb * rb - L2 < -2 * L2 / 3
        assert rc * rc - L2 < 0
        # total of the two horizons under the MM constant: r_b^2 + r_c^2 - 2 L2 < 0
        assert rb * rb + rc * rc - 2 * L2 < 0
    # the Nariai merger: r_b = r_c = r_N gives L2 = 3 r_N^2 and M_N = r_N / 3, equal areas
    for rN in (F(1), F(2, 3), F(5)):
        L2 = 3 * rN * rN
        MN = rN * rN * (2 * rN) / (2 * L2)
        assert MN == rN / 3
        assert f_val(MN, L2, rN) == 0 and fprime(MN, L2, rN) == 0       # double root
    # the M -> 0 ends: black hole r_b -> 0 (area -> 0), cosmological r_c -> ell
    sq = (1, -1, -1, -1, 1, -1)
    n0 = scal(F(1, 2), add(gen(4), gen(5)))
    ninf = sub(gen(4), gen(5))
    for ell in (F(1), F(2), F(3, 2), F(5, 7)):
        L2 = ell * ell
        assert f_val(F(0), L2, ell) == 0                               # pure de Sitter horizon at r = ell
        # 4 pi T_c = -f'(ell) = 2/ell, so (2 pi T_c)^2 = (-f'(ell)/2)^2 = 1/L2 = <I, I>
        Lam = 3 / L2
        I = add(ninf, scal(Lam / 6, n0))
        assert dot6(I, I, sq) == 1 / L2
        assert (-fprime(F(0), L2, ell) / 2) ** 2 == dot6(I, I, sq)
        # the M -> 0 limit of the family's cosmological radius: r_b = 0 in L2 = r_b^2 + r_b r_c + r_c^2
        rb0, rc0 = F(0), ell
        assert rb0 * rb0 + rb0 * rc0 + rc0 * rc0 == L2
        # with c_c = c_b = 0: S_c(M=0)/pi = ell^2 = N^2 in Planck units (N^2 = M_P^2/<I,I>, M_P = 1)
        assert rc0 * rc0 == 1 / dot6(I, I, sq)
    # Lambda -> 0: Schwarzschild, f'(2M) = 1/(2M) = 2 kappa with kappa = 1/(4M); quarter recovered
    for M in (F(1), F(3, 2), F(7)):
        fp = 2 * M / ((2 * M) ** 2)
        assert fp == 2 * (1 / (4 * M))
        assert ((2 * M) ** 2) == 4 * M * M             # S/pi = r_b^2 = 4 M^2, S = 4 pi M^2 = A/4
    return True




