"""mass.weight-polynomial-two-series: exact checks of the algebra of -w(w+3), ported from legacy
verify_T11.py (cor:series) and widened (polynomial identities with GA's exact polynomials, a dense
rational grid for the sign, general n for the conformally coupled weight, an exact remainder for nu).

Polynomials are GA coefficient lists (lowest degree first). m^2/H^2 = p(w) := -w(w+3) (the n = 4
dictionary, H^2 = Lambda/3 = Q(I)).
  (1) p = -(w)(w+3) has exactly the roots 0 and -3 (p is divided by w and by w+3 with zero remainder,
      quotient -1); the shadow map w -> -3-w preserves p (polynomial identity); with Delta = -w,
      p = Delta(3 - Delta), the de Sitter mass formula.
  (2) w = 1 - n/2 gives -w(w+n-1) = n(n-2)/4 as a polynomial identity in n (and n = 2..10); n = 4: 2.
  (3) p = 9/4 - (w + 3/2)^2 (identity); on 54 rational w in [-5, 9/4), p >= 0 exactly on [-3, 0],
      p <= 9/4 with equality only at -3/2, and p < 0 outside [-3, 0].
  (4) w = -3/2 +- i nu gives p = 9/4 + nu^2 in Q(i); sqrt(1 - (9/4) eps^2) = 1 - (9/8) eps^2 - ...
      (eps = H/m) by GA's power series, and the remainder of nu - (x - 9/(8x)), x = m/H, is exact:
      a^2 - nu^2 = 81/(64 x^2) for a = x - 9/(8x), so nu = x - (9/8)/x + O(x^-3).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

GRID = sorted({F(k, 4) for k in range(-20, 10)} | {F(k, 7) for k in range(-27, 0)})
NUS = [F(1), F(2), F(7, 3), F(100)]
XS = [F(2), F(5, 3), F(10), F(1000)]


def poly_p():
    """-w(w+3) built as a product of linear factors."""
    return GA.pmul([F(0), F(-1)], [F(3), F(1)])


def check_massless_pair_and_shadow_symmetry():
    premise("mass.mass-weight-dictionary")
    premise("mass.imported-unitary-representations-de-sitter-group")
    p = poly_p()
    ok = GA.ptrim(p) == [F(0), F(-3), F(-1)]
    qw, rw = GA.pdivmod(p, [F(0), F(1)])
    q3, r3 = GA.pdivmod(qw, [F(3), F(1)])
    ok = ok and GA.ptrim(rw) == []
    ok = ok and all(c == 0 for c in r3) and GA.ptrim(q3) == [F(-1)]
    ok = ok and GA.peval(p, F(0)) == 0 and GA.peval(p, F(-3)) == 0
    # shadow: p(-3 - w) as a polynomial in w equals p(w)
    shadow = GA.padd(GA.pmul([F(-3), F(-1)], [F(-3), F(-1)]), GA.pmul([F(3)], [F(-3), F(-1)]))
    shadow = GA.pneg(shadow)
    ok = ok and GA.ptrim(shadow) == GA.ptrim(p)
    # Delta = -w: Delta(3 - Delta) at Delta = -w is p
    dd = GA.pmul([F(0), F(-1)], [F(3), F(1)])
    ok = ok and GA.ptrim(dd) == GA.ptrim(p)
    roots = {w for w in GRID if GA.peval(p, w) == 0}
    ok = ok and sorted(roots) == [F(-3), F(0)]
    GA.check("m = 0 exactly at w = 0, -3; shadow symmetry; p = Delta(3 - Delta)", ok)
    assert ok


def check_conformally_coupled_weight():
    premise("mass.mass-weight-dictionary")
    ok = True
    # -w(w+n-1) at w = 1 - n/2, as a polynomial in n: (n/2 - 1)(n/2) = n(n-2)/4
    w_of_n = [F(1), F(-1, 2)]
    val = GA.pneg(GA.pmul(w_of_n, GA.padd(w_of_n, [F(-1), F(1)])))
    ok = ok and GA.ptrim(val) == GA.ptrim([F(0), F(-1, 2), F(1, 4)])
    for n in range(2, 11):
        w = 1 - F(n, 2)
        ok = ok and -w * (w + n - 1) == F(n * (n - 2), 4)
    ok = ok and GA.peval(poly_p(), F(-1)) == 2
    GA.check("w = 1 - n/2 gives m^2 = n(n-2)/4 Q(I); n = 4: m^2 = 2 H^2", ok)
    assert ok


def check_real_weights_complementary_series():
    premise("mass.mass-weight-dictionary")
    premise("mass.imported-unitary-representations-de-sitter-group")
    p = poly_p()
    sq = GA.pneg(GA.pmul([F(3, 2), F(1)], [F(3, 2), F(1)]))
    ok = GA.ptrim(GA.padd([F(9, 4)], sq)) == GA.ptrim(p)
    for w in GRID:
        m2 = GA.peval(p, w)
        ok = ok and ((m2 >= 0) == (F(-3) <= w <= 0))
        ok = ok and m2 <= F(9, 4) and ((m2 == F(9, 4)) == (w == F(-3, 2)))
    ok = ok and GA.peval(p, F(1)) == -4 and GA.peval(p, F(-3, 2)) == F(9, 4)
    GA.check("real w: m^2 = 9/4 - (w+3/2)^2, nonnegative exactly on [-3, 0]", ok)
    assert ok


def check_principal_series_and_expansion():
    premise("mass.imported-unitary-representations-de-sitter-group")
    ok = True
    for nu in NUS:
        for sgn in (1, -1):
            w = GA.qi(F(-3, 2), sgn * nu)
            ok = ok and -(w * (w + GA.qi(3))) == GA.qi(F(9, 4) + nu * nu)
    root = GA.ps_pow_rat(GA.ps_trunc([F(1), F(0), F(-9, 4)], 6), F(1, 2), 6)
    ok = ok and root[:5] == [F(1), F(0), F(-9, 8), F(0), F(-81, 128)]
    for x in XS:
        nu2 = x * x - F(9, 4)
        a = x - F(9, 8) / x
        ok = ok and (a * a - nu2) * x * x == F(81, 64) and nu2 > 0
    GA.check("m > 3H/2: w = -3/2 +- i nu, nu = m/H - (9/8) H/m + O((H/m)^3)", ok)
    assert ok
