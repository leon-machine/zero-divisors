"""synthesis.smallness-monomials-exact-hierarchy-casimir: exact checks.

The frozen point I_Lambda = n_inf + (Lambda/6) n_0 is built in Cl(2,4) and its norm read off
(<I,I> = H^2 = Lambda/3). The two gravitational monomials are then checked as identities in
rationals; the hierarchy entry is checked through the weight's Casimir -w(w+3), computed on
complex pairs (re, im), and the gap between Im w and m/H is bracketed by exact squared
inequalities, so no square root is ever taken.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen
from tp_premise import premise

HS = [F(1, 2), F(1), F(3), F(2, 7), F(5, 3)]
MPS = [F(10), F(7, 2), F(1000)]
XS = [F(8, 5), F(2), F(5, 2), F(7), F(100), F(10 ** 6)]


def dot(a, b, sq):
    return add(mul(a, b, sq), mul(b, a, sq)).get((), F(0)) / 2


def casimir(w):
    """-w(w+3) for w = (re, im)."""
    w3 = (w[0] + 3, w[1])
    pr = (w[0] * w3[0] - w[1] * w3[1], w[0] * w3[1] + w[1] * w3[0])
    return (-pr[0], -pr[1])


def check_gravitational_monomials():
    premise("standard-model.imported-frozen-point-dictionary")
    sq = (1, -1, -1, -1, 1, -1)
    n0 = scal(F(1, 2), add(gen(4), gen(5)))       # the dictionary's chart: n_0.n_inf = +1
    ninf = sub(gen(4), gen(5))
    assert dot(n0, ninf, sq) == 1 and dot(n0, n0, sq) == 0 and dot(ninf, ninf, sq) == 0
    for h in HS:
        L = 3 * h * h
        I = add(ninf, scal(L / 6, n0))            # I_Lambda = n_inf + (Lambda/6) n_0
        nI = dot(I, I, sq)
        assert nI == L / 3 == h * h               # <I,I> = Lambda/3 = H^2
        for MP in MPS:
            G = 1 / (MP * MP)
            N = MP / h
            assert G * L == 3 / (N * N)           # G Lambda = 3 N^-2
            assert G * nI == 1 / (N * N)          # (H/M_P)^2 = N^-2
            assert G * L != 1 / (N * N)
    return True


def check_hierarchy_entry():
    premise("standard-model.imported-frozen-point-dictionary")
    for nu in (F(0), F(1, 3), F(5, 2), F(40)):
        assert casimir((F(-3, 2), nu)) == (F(9, 4) + nu * nu, F(0))
        assert casimir((F(-3, 2), -nu)) == (F(9, 4) + nu * nu, F(0))
    # real weights on [-3, 0] give 0 <= m^2/H^2 <= 9/4, maximal at w = -3/2
    for w in (F(0), F(-1), F(-3, 2), F(-2), F(-3)):
        c = casimir((w, F(0)))[0]
        assert 0 <= c <= F(9, 4)
    assert casimir((F(-3, 2), F(0)))[0] == F(9, 4)
    for h in HS:
        for MP in MPS:
            N = MP / h
            for x in XS:                          # x = m/H > 3/2
                m = x * h
                nu2 = x * x - F(9, 4)             # Im w(m)^2 from the dictionary
                assert casimir((F(-3, 2), F(0)))[0] + nu2 == (m / MP) ** 2 * N ** 2   # exact monomial
                assert nu2 < x * x                # Im w(m) < (m/M_P) N strictly
                lo = x - F(9, 4) / x              # Im w >= x - 9/(4x)
                hi = x - F(9, 8) / x              # Im w <= x - 9/(8x)
                assert lo >= 0 and lo * lo <= nu2 <= hi * hi
                assert not (hi * hi < nu2)
            Nw2 = N * N - F(9, 4)                 # N_w = Im w(M_P)
            assert Nw2 + F(9, 4) == (MP / h) ** 2
    return True
