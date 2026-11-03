"""dark-matter.nesting: exact checks.

(i)   In GA.py: in Cl(1,4) the generators e_0..e_3 square to (+1, -1, -1, -1) and anticommute
      pairwise (a Cl(1,3)); in Cl(1,3), e_0, e_1, e_2 give a Cl(1,2); mirror chain: in Cl(4,1) the
      slice e_0, e_1, e_2, e_4 gives a Cl(3,1), and in Cl(3,1) the slice e_0, e_1, e_3 a Cl(2,1).
      Control: the relations fail for a non-slice choice (e_0..e_3 of Cl(1,4) do not give a Cl(3,1)).
(ii)  Balls: on a rational grid G^4 (G = {0, +-1/2, +-1, +-3/2}) the points of B^4 with x_4 = 0 are
      exactly the points of B^3 (with a zero appended), counted (33); likewise B^3 with x_3 = 0 is B^2
      (13 points). The 56 grid points of B^4 with x_4 != 0 lie off the hyperplane.
(iii) Spheres: on rational points of S^5 (from Pythagorean data) with x_6 = 0 the points are points
      of S^4, and conversely; same for S^4 and S^3. The measures are linked by the hat-box identity
      |S^(D+1)| = 2 pi V_D, checked as an identity in pi (Laurent polynomials in pi, V_D from the
      recursion V_D = (2 pi / D) V_(D-2), |S^(n-1)| = n V_n) for D = 2, 3, 4: the balls carry D and
      the spheres n = D + 1.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

GRID = [F(0), F(1, 2), F(-1, 2), F(1), F(-1), F(3, 2), F(-3, 2)]
# rational points on unit spheres, from 3^2 + 4^2 = 5^2 and 2^2 + 3^2 + 6^2 = 7^2
SPHERE_PTS6 = [
    [F(3, 5), F(4, 5), F(0), F(0), F(0), F(0)],
    [F(2, 7), F(0), F(3, 7), F(0), F(6, 7), F(0)],
    [F(0), F(0), F(0), F(0), F(3, 5), F(4, 5)],
    [F(1, 2), F(1, 2), F(1, 2), F(1, 2), F(0), F(0)],
    [F(2, 7), F(3, 7), F(0), F(0), F(0), F(6, 7)],
]


def relations_hold(gens, sq, target):
    for g, t in zip(gens, target):
        if not GA.eq(GA.mul(GA.gen(g), GA.gen(g), sq), GA.sc(t)):
            return False
    for a in range(len(gens)):
        for b in range(a + 1, len(gens)):
            x, y = GA.gen(gens[a]), GA.gen(gens[b])
            if not GA.is_zero(GA.add(GA.mul(x, y, sq), GA.mul(y, x, sq))):
                return False
    return True


def norm2(x):
    return sum(c * c for c in x)


def lp(c, k=0):
    return {k: F(c)}


def lmul(a, b):
    out = {}
    for k1, c1 in a.items():
        for k2, c2 in b.items():
            out[k1 + k2] = out.get(k1 + k2, F(0)) + c1 * c2
    return {k: c for k, c in out.items() if c != 0}


def ball(D):
    V = {0: lp(1), 1: lp(2)}
    for n in range(2, D + 1):
        V[n] = lmul(lp(F(2, n), 1), V[n - 2])
    return V[D]


def check_slices_are_subalgebras():
    assert relations_hold([0, 1, 2, 3], GA.sig(1, 4), [1, -1, -1, -1])
    assert relations_hold([0, 1, 2], GA.sig(1, 3), [1, -1, -1])
    assert relations_hold([0, 1, 2, 4], GA.sig(4, 1), [1, 1, 1, -1])
    assert relations_hold([0, 1, 3], GA.sig(3, 1), [1, 1, -1])
    assert not relations_hold([0, 1, 2, 3], GA.sig(1, 4), [1, 1, 1, -1])
    return True


def check_ball_sections():
    in4 = [x for x in product(GRID, repeat=4) if norm2(x) <= 1]
    sec4 = sorted(x[:3] for x in in4 if x[3] == 0)
    in3 = sorted(x for x in product(GRID, repeat=3) if norm2(x) <= 1)
    assert sec4 == in3 and len(in3) == 33
    sec3 = sorted(x[:2] for x in in3 if x[2] == 0)
    in2 = sorted(x for x in product(GRID, repeat=2) if norm2(x) <= 1)
    assert sec3 == in2 and len(in2) == 13
    assert len([x for x in in4 if x[3] != 0]) == 56
    return True


def check_sphere_sections_and_measures():
    for x in SPHERE_PTS6:
        assert norm2(x) == 1
        on5 = x[5] == 0
        assert on5 == (norm2(x[:5]) == 1)
        if on5:
            assert (x[4] == 0) == (norm2(x[:4]) == 1)
    assert sum(1 for x in SPHERE_PTS6 if x[5] == 0) == 3
    assert sum(1 for x in SPHERE_PTS6 if x[5] == 0 and x[4] == 0) == 2
    for D in (2, 3, 4):
        n = D + 1
        sphere_n = lmul(lp(n + 1), ball(n + 1))          # |S^n| = (n + 1) V_(n+1)
        assert sphere_n == lmul(lp(2, 1), ball(D))
    assert lmul(lp(5), ball(5)) == {2: F(8, 3)}           # |S^4| = 8 pi^2 / 3
    return True
