"""synthesis.null-vacuum-singularity-under-reparametrisation-and-dilation: exact checks.

Copied from the check functions (1) and (2) of synthesis.collapsing-hole-flux-from-ground-state-on-the-
ingoing-sheet, where these lemmas were first stated.
(1) Reparametrisation: for a polynomial xi with rational coefficients and a base point U0, the squared
    ratio of the weight-1/2 null-vacuum kernels in xi and in U, xi'(U0+x) xi'(U0) x^2/(xi(U0+x)-xi(U0))^2,
    is an exact rational function of x whose Taylor coefficients at 0 are 1, 0, S_xi(U0)/6 (Schwarzian);
    tabulated at three xi and three U0. The same coefficient S/6 is the diagonal value of the difference of
    the weight-1 field's own kernels (U - U')^{-2}. Covariance-weight controls: the kernel 1/(U - U')
    carried with weight 0 or 1 gives a constant term != 1 or a linear term != 0; xi = U^3 at U0 = 0 gives
    ratio 0.
(2) Dilation: with eps a formal variable, eps/(eps U - eps U') = 1/(U - U') exactly (weight 1/2), while
    weights 0 and 1 are not invariant; eps R(eps U, eps U') for a polynomial R has no eps^0 term; a
    remainder homogeneous of degree -1 is unchanged.
Exact arithmetic only (Fractions, rational functions).
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise


def _shift(p, U0):
    """p(U0 + x) as a polynomial in x (coefficient lists over Fraction)."""
    out = []
    for i, c in enumerate(p):
        term = [F(1)]
        for _ in range(i):
            term = GA.pmul(term, [F(U0), F(1)])
        out = GA.padd(out, [c * t for t in term])
    return out


def _ratio_sq(xi, U0, twice_weight):
    """(xi'(U0+x) xi'(U0))^{2w} x^2 / (xi(U0+x) - xi(U0))^2 as an RF in x; 2w = twice_weight."""
    xs = _shift(xi, U0)
    d = GA.pderiv(xi)
    ds = _shift(d, U0)
    d0 = GA.peval(d, U0)
    diff = GA.padd(xs, GA.pneg([GA.peval(xi, U0)]))
    q, r = GA.pdivmod(diff, [F(0), F(1)])
    GA.check("xi(U0 + x) - xi(U0) is divisible by x", not r)
    num = [F(1)]
    for _ in range(twice_weight):
        num = GA.pmul(num, GA.pmul(ds, [d0]))
    return RF(num, GA.pmul(q, q))


def _taylor(rf, n):
    num = GA.ps_trunc(rf.num, n)
    den = GA.ps_trunc(rf.den, n)
    return GA.ps_mul(num, GA.ps_inv(den, n), n)


def check_regular_reparametrisation_keeps_the_ground_state_singularity():
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    xis = ([F(0), F(1), F(1, 3)],
           [F(2), F(3), F(-1, 2), F(1, 5)],
           [F(0), F(1), F(0), F(1, 7)])
    base = (F(0), F(1, 2), F(-3, 4))
    # tabulated S_xi(U0)/6 for the nine cases, row by xi
    want = ((F(-1, 9), F(-1, 16), F(-4, 9)),
            (F(7, 180), F(196, 2809), F(-544, 106929)),
            (F(1, 7), F(88, 961), F(928, 19321)))
    for i, xi in enumerate(xis):
        d1, d2, d3 = GA.pderiv(xi), GA.pderiv(GA.pderiv(xi)), GA.pderiv(GA.pderiv(GA.pderiv(xi)))
        for j, U0 in enumerate(base):
            a, b2, c6 = GA.peval(d1, U0), GA.peval(d2, U0), GA.peval(d3, U0)
            GA.check("xi' > 0 at the base point", a > 0)
            S6 = (c6 / a - F(3, 2) * (b2 / a) ** 2) / 6
            co = _taylor(_ratio_sq(xi, U0, 1), 3)
            GA.check("weight 1/2: squared ratio = 1 + 0 x + (S/6) x^2", co[0] == 1 and co[1] == 0 and co[2] == S6)
            GA.check("tabulated S/6", S6 == want[i][j])
            # the weight-1 field's own kernels (U - U')^{-2}: their difference is (squared ratio - 1)/x^2,
            # whose value on the diagonal is the x^2 coefficient S/6: continuous, nonzero
            GA.check("weight-1 own-kernel difference on the diagonal is S/6", co[2] == want[i][j] and (co[2] != 0))
            c0 = _taylor(_ratio_sq(xi, U0, 0), 1)
            c1 = _taylor(_ratio_sq(xi, U0, 2), 1)
            GA.check("covariance-weight control 0 on the kernel 1/(U - U'): constant term 1/xi'^2", c0[0] == 1 / (a * a))
            GA.check("covariance-weight control 1 on the kernel 1/(U - U'): constant xi'^2, linear xi' xi''", c1[0] == a * a and c1[1] == a * b2)
            if not (a == 1 and b2 == 0):
                GA.check("the kernel 1/(U - U') is not covariant with weight 0 or 1 off xi' = 1, xi'' = 0",
                         not (c0[0] == 1 and c0[1] == 0) or not (c1[0] == 1 and c1[1] == 0))
    # the Schwarzian of a Moebius-type polynomial truncation is not zero: a generic nonzero value
    GA.check("S/6 of xi = U + U^2/3 at 0 is -1/9", want[0][0] == F(-1, 9))
    # singular reparametrisation: xi'(0) = 0 kills the ratio
    GA.check("xi = U^3 at U0 = 0: ratio vanishes", _ratio_sq([F(0), F(0), F(0), F(1)], F(0), 1).eval(F(0)) == 0)


def check_scaling_limit_is_the_ground_state():
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("hawking.imported-quasi-free-kms-reduces-two")
    e = RF.var()
    # polynomial remainder R = 3 - 2U + (5/2)U' + 7UU' - (1/3)U^2; tabulated: 1/(U - U'), the eps^2
    # coefficient of eps R(eps U, eps U') (= -2U + (5/2)U'), and the degree -1 kernel 1/(U + 2U')
    R = {(0, 0): F(3), (1, 0): F(-2), (0, 1): F(5, 2), (1, 1): F(7), (2, 0): F(-1, 3)}
    pts = ((F(2, 3), F(-5, 7), F(21, 29), F(-131, 42), F(-21, 16)),
           (F(-1), F(3, 2), F(-2, 5), F(23, 4), F(1, 2)),
           (F(1, 4), F(-1, 3), F(12, 7), F(-4, 3), F(-12, 5)))
    for U, Up, inv, c2, hom in pts:
        sing = RF.const(1) / (e * RF.const(U) - e * RF.const(Up))
        GA.check("tabulated 1/(U - U')", 1 / (U - Up) == inv)
        GA.check("weight 1/2: eps/(eps U - eps U') = 1/(U - U')", (e * sing).eqrf(RF.const(inv)))
        GA.check("control weight 0: not invariant", not sing.eqrf(RF.const(inv)))
        GA.check("control weight 1: not invariant", not (e * e * sing).eqrf(RF.const(inv)))
        scaled = RF.const(0)
        for (j, k), c in R.items():
            scaled = scaled + RF.const(c * U ** j * Up ** k) * RF([F(0)] * (j + k) + [F(1)])
        scaled = e * scaled
        co = _taylor(scaled, 2)
        GA.check("eps R(eps U, eps U') has no eps^0 term", co[0] == 0)
        GA.check("its eps^1 coefficient is R(0,0) = 3", co[1] == 3)
        GA.check("tabulated eps^2 coefficient -2U + (5/2)U'", co[2] == c2)
        GA.check("control: without the half-density factor the eps^0 term is R(0,0)",
                 (scaled / e).eval(F(0)) == 3)
        Rh = RF.const(1) / (e * RF.const(U) + RF.const(2) * e * RF.const(Up))
        GA.check("tabulated 1/(U + 2U')", 1 / (U + 2 * Up) == hom)
        GA.check("degree -1 remainder: eps R_h(eps U, eps U') = R_h(U, U')", (e * Rh).eqrf(RF.const(hom)))
