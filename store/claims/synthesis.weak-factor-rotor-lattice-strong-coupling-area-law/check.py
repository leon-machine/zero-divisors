"""synthesis.weak-factor-rotor-lattice-strong-coupling-area-law: exact checks.

The weak factor su(2) as the bivectors B1 = g2g3, B2 = g3g1, B3 = g1g2 of Cl(3,0); link variables are
rotors U = u0 + u1 B1 + u2 B2 + u3 B3 with U rev(U) = 1, and <.>_0 is the scalar part. Products of rotors
are computed by a four-component product that is first checked against GA.mul on every pair of basis
elements. Haar averages on SU(2) = the unit three-sphere use the exact moment formula
E[u^alpha] = prod (alpha_i - 1)!! / (4 * 6 * ... * (2 + |alpha|)) (zero if any alpha_i is odd); the
24 Hurwitz units (the binary tetrahedral group) and the 8 units of the quaternion group are used as exact
finite averages, after checking that they reproduce every Haar moment up to degree 5 and 3 respectively
(every integrand below has degree at most 2 in each link). Compact U(1) uses rotors a + b B3 and the
group {1, B3, -1, -B3}.
Clauses: (i) the bivectors close to su(2) with a negative-definite trace form; (ii) the averages;
(iii) the gluing rule and the vanishing of gauge-variant averages, on every basis pair (complete by
bilinearity); (iv) gauge invariance of closed loops under rational vertex rotors; (v) the leading
strong-coupling coefficients of the 1x1, 1x2 and 2x2 Wilson loops, SU(2) and U(1); (vi) the scalar part
of exp(B) to sixth order.
"""
from fractions import Fraction as F
from itertools import product

import GA
from GA import mul, sc, gen, eq, add, scal
from tp_premise import premise

S3 = (1, 1, 1)
BASIS = [sc(1), mul(gen(1), gen(2), S3), mul(gen(2), gen(0), S3), mul(gen(0), gen(1), S3)]


def to_ga(q):
    return add(*[scal(q[i], BASIS[i]) for i in range(4)])


def qmul(p, q):
    a0, a1, a2, a3 = p
    b0, b1, b2, b3 = q
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2,
            a0 * b2 + a1 * b3 + a2 * b0 - a3 * b1,
            a0 * b3 - a1 * b2 + a2 * b1 + a3 * b0)


def rev(q):
    return (q[0], -q[1], -q[2], -q[3])


def s0(q):
    return q[0]


def unit(i):
    return tuple(F(1) if j == i else F(0) for j in range(4))


ONE = (1, 0, 0, 0)
Q8 = [tuple(s if j == i else 0 for j in range(4)) for i in range(4) for s in (1, -1)]
HURWITZ = Q8 + [tuple(F(x, 2) for x in signs) for signs in product((1, -1), repeat=4)]
Z4 = [ONE, (0, 0, 0, 1), (-1, 0, 0, 0), (0, 0, 0, -1)]


def dfact(n):
    r = 1
    while n > 1:
        r *= n
        n -= 2
    return r


def haar_moment(alpha):
    if any(a % 2 for a in alpha):
        return F(0)
    num = 1
    for a in alpha:
        num *= dfact(a - 1)
    den = 1
    for j in range(sum(alpha) // 2):
        den *= 4 + 2 * j
    return F(num, den)


def average(group, fn):
    return sum((fn(u) for u in group), F(0)) / len(group)


def check_bivectors_close_to_su2_and_product_matches_ga():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    for i in range(4):
        for j in range(4):
            assert eq(to_ga(qmul(unit(i), unit(j))), mul(BASIS[i], BASIS[j], S3))
    b1, b2, b3 = BASIS[1], BASIS[2], BASIS[3]

    def comm(x, y):
        return add(mul(x, y, S3), scal(-1, mul(y, x, S3)))
    assert eq(comm(b1, b2), scal(-2, b3)) and eq(comm(b2, b3), scal(-2, b1)) and eq(comm(b3, b1), scal(-2, b2))
    for b in (b1, b2, b3):
        assert mul(b, b, S3) == sc(-1)
    # three generators, trace form <B B'>_0 = -delta: compact, dimension 3
    gram = [[mul(x, y, S3).get((), F(0)) for y in (b1, b2, b3)] for x in (b1, b2, b3)]
    assert gram == [[-1, 0, 0], [0, -1, 0], [0, 0, -1]]


def check_finite_groups_reproduce_haar_moments():
    for g in HURWITZ:
        assert sum(x * x for x in g) == 1
    assert len(HURWITZ) == 24 and len(Q8) == 8
    assert haar_moment((2, 0, 0, 0)) == F(1, 4)
    assert haar_moment((4, 0, 0, 0)) == F(1, 8) and haar_moment((2, 2, 0, 0)) == F(1, 24)
    for deg in range(0, 6):
        for alpha in product(range(deg + 1), repeat=4):
            if sum(alpha) != deg:
                continue

            def mono(u, alpha=alpha):
                r = F(1)
                for x, a in zip(u, alpha):
                    r *= x ** a
                return r
            h = haar_moment(alpha)
            assert average(HURWITZ, mono) == h
            if deg <= 3:
                assert average(Q8, mono) == h
    # Q8 is not a 4-design: E[u0^4] = 1/4 there against 1/8
    assert average(Q8, lambda u: u[0] ** 4) == F(1, 4)


def check_gluing_rule_and_gauge_variant_averages_vanish():
    basis = [unit(k) for k in range(len(BASIS))]
    second = [haar_moment(tuple(2 if m == k else 0 for m in range(len(basis)))) for k in range(len(basis))]
    assert second == [F(1, 4)] * 4
    pairs = 0
    for X in basis:
        assert average(HURWITZ, lambda U: s0(qmul(X, U))) == 0
        for Y in basis:
            lhs = average(HURWITZ, lambda U: s0(qmul(X, U)) * s0(qmul(rev(U), Y)))
            by_moments = sum(second[k] * s0(qmul(X, e)) * s0(qmul(rev(e), Y)) for k, e in enumerate(basis))
            assert lhs == by_moments == F(1, 4) * s0(qmul(X, Y))
            pairs += 1
    assert pairs == 16
    # U(1): the gluing coefficient is 1/2 on span{1, B3}
    for X in (ONE, unit(3)):
        for Y in (ONE, unit(3)):
            assert average(Z4, lambda U: s0(qmul(X, U)) * s0(qmul(rev(U), Y))) == F(1, 2) * s0(qmul(X, Y))


# ---------------------------------------------------------------- lattice patches
def patch(R, T):
    sites = [(x, y) for x in range(R + 1) for y in range(T + 1)]
    links = [((x, y), (x + 1, y)) for x in range(R) for y in range(T + 1)]
    links += [((x, y), (x, y + 1)) for x in range(R + 1) for y in range(T)]
    plaqs = [[((x, y), (x + 1, y)), ((x + 1, y), (x + 1, y + 1)),
              ((x, y + 1), (x + 1, y + 1)), ((x, y), (x, y + 1))] for x in range(R) for y in range(T)]
    return sites, links, plaqs


def path_product(U, corners):
    r = ONE
    for a, b in zip(corners, corners[1:]):
        r = qmul(r, U[(a, b)] if (a, b) in U else rev(U[(b, a)]))
    return r


def boundary(R, T):
    c = [(x, 0) for x in range(R + 1)] + [(R, y) for y in range(1, T + 1)]
    c += [(x, T) for x in range(R - 1, -1, -1)] + [(0, y) for y in range(T - 1, -1, -1)]
    return c


def plaq_corners(x, y):
    return [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1), (x, y)]


def tree_gauge_average(R, T, group):
    # maximal tree: all vertical links on x = 0 and all horizontal links; free links: vertical x > 0
    sites, links, plaqs = patch(R, T)
    free = [((x, y), (x, y + 1)) for x in range(1, R + 1) for y in range(T)]
    total = F(0)
    for vals in product(group, repeat=len(free)):
        U = {l: ONE for l in links}
        U.update(dict(zip(free, vals)))
        val = s0(path_product(U, boundary(R, T)))
        for x in range(R):
            for y in range(T):
                val *= s0(path_product(U, plaq_corners(x, y)))
        total += val
    return total / len(group) ** len(free)


def check_closed_loops_gauge_invariant():
    sites, links, plaqs = patch(2, 2)
    vals = [(F(3, 5), F(4, 5), F(0), F(0)), (F(1, 2), F(1, 2), F(1, 2), F(-1, 2)),
            (F(2, 3), F(1, 3), F(2, 3), F(0)), (F(0), F(3, 5), F(0), F(4, 5))]
    U = {l: vals[k % 4] for k, l in enumerate(links)}
    g = {s: vals[(k + 1) % 4] for k, s in enumerate(sites)}
    V = {(a, b): qmul(qmul(g[a], U[(a, b)]), rev(g[b])) for (a, b) in links}
    for corners in (boundary(2, 2), boundary(1, 1), plaq_corners(1, 1), boundary(2, 1)):
        assert s0(path_product(U, corners)) == s0(path_product(V, corners))
    open_line = [(0, 0), (1, 0), (2, 0)]
    assert s0(path_product(U, open_line)) != s0(path_product(V, open_line))


def check_strong_coupling_area_law_leading_coefficients():
    # 1x1 without gauge fixing, all four links averaged over Q8
    sites, links, plaqs = patch(1, 1)
    full = F(0)
    for vals in product(Q8, repeat=4):
        U = dict(zip(links, vals))
        full += s0(path_product(U, boundary(1, 1))) * s0(path_product(U, plaq_corners(0, 0)))
    assert full / 8 ** 4 == F(1, 4)
    assert tree_gauge_average(1, 1, HURWITZ) == F(1, 4)
    assert tree_gauge_average(2, 1, HURWITZ) == F(1, 16)
    assert tree_gauge_average(2, 2, Q8) == F(1, 256)


def check_compact_u1_has_the_same_strong_coupling_area_law():
    # compact U(1) links a + b B3: (beta/2)^A
    assert tree_gauge_average(1, 1, Z4) == F(1, 2)
    assert tree_gauge_average(2, 1, Z4) == F(1, 4)
    assert tree_gauge_average(2, 2, Z4) == F(1, 16)


def check_scalar_part_of_exponential_is_cosine_series():
    for B in ((F(1, 3), F(2, 3), F(2, 3)), (F(3, 7), F(0), F(-2, 5))):
        b = (F(0),) + B
        n2 = sum(x * x for x in B)
        assert qmul(b, b) == (-n2, F(0), F(0), F(0))
        p = unit(0)
        series = F(0)
        fact = 1
        for n in range(7):
            if n > 0:
                p = qmul(p, b)
                fact *= n
            series += s0(p) * F(1, fact)
        assert series == 1 - n2 / 2 + n2 ** 2 / 24 - n2 ** 3 / 720
