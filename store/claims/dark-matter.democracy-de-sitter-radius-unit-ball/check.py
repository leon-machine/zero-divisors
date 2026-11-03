"""dark-matter.democracy-de-sitter-radius-unit-ball: exact checks.

Numbers of Q(pi) are Laurent polynomials in pi, {k: c} for sum c pi^k (pi transcendental); the
unit-ball volumes come from V_0 = 1, V_1 = 2, V_D = (2 pi / D) V_(D-2) and the unit-sphere areas
from |S^(n-1)| = n V_n.

Checked:
(1) Under D a tower of spacetime dimension n has density M/(|S^n| l^n) on its sphere; read through
    a thickness l (n = 5) or with sheets l apart (n = 3) it is a density per unit of our
    four-measure, and the share against ours, M/(|S^4| l^4), is |S^4|/|S^n|: M and l cancel
    (checked at two sample values of each) for n = 3, 4, 5.
(2) The sphere form equals the ball form: |S^n| = 2 pi V_(n-1) (hat-box identity, n = 1..7), so
    |S^4|/|S^n| = V_3/V_(n-1): 4/3 at n = 3 and 8/(3 pi) at n = 5.
(3) The total over the dark towers (n = 4 once, n = 3 and n = 5 twice each) is the unit-ball
    rule's 11/3 + 16/(3 pi).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = [F(1), F(17, 3)]          # sample total masses M_tot (D: common to all towers)
LENGTHS = [F(1), F(5, 2)]          # sample de Sitter radii l
DARK_N = [4, 3, 3, 5, 5]           # mirror, two three-dimensional, two five-dimensional towers


def lp(c, k=0):
    return {k: F(c)} if c != 0 else {}


def ladd(*xs):
    out = {}
    for x in xs:
        for k, c in x.items():
            out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}


def lmul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1 + k2] = new.get(k1 + k2, F(0)) + c1 * c2
        out = {k: c for k, c in new.items() if c != 0}
    return out


def linv(a):
    assert len(a) == 1
    (k, c), = a.items()
    return {-k: 1 / c}


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def sphere(k):
    """|S^k|, the area of the unit sphere in R^(k+1)"""
    return lmul(lp(k + 1), ball(k + 1))


def share(n, M, l):
    dens = lmul(lp(M / l ** n), linv(sphere(n)))           # D: density on the tower's sphere
    per_ours = lmul(dens, lp(l ** (n - 4)))                  # R3 at the unit l
    ours = lmul(lp(M / l ** 4), linv(sphere(4)))
    return lmul(per_ours, linv(ours))


def check_shares_are_sphere_ratios():
    premise("dark-matter.d-democracy-total-mass")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    for M in MASSES:
        for l in LENGTHS:
            for n in (3, 4, 5):
                assert share(n, M, l) == lmul(sphere(4), linv(sphere(n)))
    assert sphere(4) == {2: F(8, 3)} and sphere(3) == {2: F(2)} and sphere(5) == {3: F(1)}
    return True


def check_sphere_form_is_ball_form():
    for n in range(1, 8):
        assert sphere(n) == lmul(lp(2, 1), ball(n - 1))
    assert lmul(sphere(4), linv(sphere(3))) == {0: F(4, 3)}
    assert lmul(sphere(4), linv(sphere(5))) == {-1: F(8, 3)}
    assert lmul(sphere(4), linv(sphere(3))) == lmul(ball(3), linv(ball(2)))
    assert lmul(sphere(4), linv(sphere(5))) == lmul(ball(3), linv(ball(4)))
    return True


def check_total_is_unit_ball_rule():
    premise("dark-matter.d-democracy-total-mass")
    premise("dark-matter.r3-one-cell-per-unshared-direction")
    total = ladd(*[share(n, MASSES[1], LENGTHS[1]) for n in DARK_N])
    assert total == {0: F(11, 3), -1: F(16, 3)}
    return True
