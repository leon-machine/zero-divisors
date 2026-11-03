"""synthesis.de-sitter-entropy-pi-n-squared: exact checks.

pi and ln 2 are kept as formal symbols: a quantity a + b pi is the pair (a, b), and the count
in the capacity convention is (pi / ln 2) N^2, recorded by its coefficient. The horizon's
areal radius is read from the conformal model, the entropy from the area, and N from the
Planck mass and the frozen point's norm.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen
from tp_premise import premise

HS = [F(1, 2), F(1), F(3), F(2, 7), F(5, 3)]
MPS = [F(10), F(7, 2), F(1000)]


def dot(a, b, sq):
    return add(mul(a, b, sq), mul(b, a, sq)).get((), F(0)) / 2


def check_de_sitter_entropy():
    premise("synthesis.imported-gibbons-hawking-entropy")
    premise("standard-model.imported-frozen-point-dictionary")
    premise("synthesis.de-sitter-static-boost-frozen-point")
    premise("synthesis.cosmological-horizon-completed-pair")
    sq = (1, -1, -1, -1, 1, -1)
    n0 = scal(F(1, 2), add(gen(4), gen(5)))
    ninf = sub(gen(4), gen(5))
    for h in HS:
        L = 3 * h * h
        I = add(ninf, scal(L / 6, n0))
        assert dot(I, I, sq) == h * h                    # <I,I> = H^2
        # the bifurcation sphere: r = 2/h on the slice x0 = 0; sigma = 1 - L Q / 12 = 2;
        # areal radius R = r / sigma = 1/h
        r = 2 / h
        X = add(add(n0, scal(r, gen(1))), scal(r * r / 2, ninf))
        sigma = dot(X, I, sq)
        assert sigma == 2
        R = r / sigma
        assert R == 1 / h
        for MP in MPS:
            N = MP / h
            assert N * N == MP * MP / dot(I, I, sq)      # N^2 = M_P^2 / <I,I>
            area_over_pi = 4 * R * R * MP * MP           # A / pi in Planck units (A = 4 pi R^2 / l_P^2)
            S_over_pi = area_over_pi / 4                 # S = A / 4G
            assert S_over_pi == N * N                    # S = pi N^2
            assert area_over_pi == 4 * N * N             # A = 4 pi N^2
            # the weight reading: m^2 = -w(w+3) H^2 with w = -3/2 + i nu; on complex pairs (re, im)
            # -w(w+3) = 9/4 + nu^2, so M_P^2 = (9/4 + N_w^2) H^2 and S / pi = N_w^2 + 9/4
            for nu in (F(0), F(1, 2), F(7, 3)):
                w = (F(-3, 2), nu)
                w3 = (w[0] + 3, w[1])
                prod = (w[0] * w3[0] - w[1] * w3[1], w[0] * w3[1] + w[1] * w3[0])
                assert (-prod[0], -prod[1]) == (F(9, 4) + nu * nu, F(0))
            Nw2 = MP * MP / (h * h) - F(9, 4)          # the nu with (9/4 + nu^2) H^2 = M_P^2
            assert (F(9, 4) + Nw2) * h * h == MP * MP and S_over_pi == Nw2 + F(9, 4)
    return True
