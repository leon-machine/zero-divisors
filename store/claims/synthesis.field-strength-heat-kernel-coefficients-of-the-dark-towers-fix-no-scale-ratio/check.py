"""synthesis.field-strength-heat-kernel-coefficients-of-the-dark-towers-fix-no-scale-ratio: exact checks.

(1) Spin weights s = 4 Re tr M(F)^2 / X, X = -2 <F^2>_0, of the vector and spinor representations in the algebras of
    the towers: Cl(2,1), Cl(1,2) (three dimensions), Cl(1,3), Cl(3,1) (four), Cl(4,1), Cl(1,4) (five), on generic
    rational bivectors. The spinor trace is taken on a left ideal A P as the trace of y -> x y P over the algebra.
(2) The stored rule (1/3) sigma w (n + 6 s): vector with ghosts (d - 26)/6, a spinor of n_c complex components
    n_c/3, and the power of the proper time that the coefficient multiplies.
(3) The table by tower on the stored content, and the four-dimensional reading of the five-dimensional content.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(1)
# signature, idempotent factors (pairs of generator indices whose product squares to +1), complex components
TOWER_ALGEBRAS = (
    ((2, 1), ((0, 2),), 2),
    ((1, 2), ((0, 1),), 2),
    ((1, 3), ((0, 3),), 4),
    ((3, 1), ((0, 3),), 4),
    ((4, 1), ((0, 4), (0, 3, 4)), 4),
    ((1, 4), ((0, 1), (2, 3, 4)), 4),
)
COEFFS = (F(3), F(-2), F(1, 2), F(5, 3), F(-7, 4), F(2, 5), F(1), F(-4, 3), F(3, 7), F(-1, 6))


def blade(idx, SQ):
    x = ONE
    for i in idx:
        x = GA.mul(x, GA.gen(i), SQ)
    return x


def generic_bivector(d, SQ):
    terms = []
    for j, (a, b) in enumerate(combinations(range(d), 2)):
        terms.append(GA.scal(COEFFS[j], blade((a, b), SQ)))
    return GA.add(*terms)


def vector_trace_of_square(Fb, d, SQ):
    """trace over vectors of (a -> a.F)^2, a.F = (aF - Fa)/2."""
    def act(a):
        return GA.scal(F(1, 2), GA.sub(GA.mul(a, Fb, SQ), GA.mul(Fb, a, SQ)))
    total = F(0)
    for mu in range(d):
        image = act(act(GA.gen(mu)))
        total += image.get((mu,), F(0))
    return total


def ideal_trace(x, P, d, SQ):
    """real trace of left multiplication by x on the left ideal A P: sum over blades b of <b^-1 x b P>_0."""
    total = F(0)
    for r in range(d + 1):
        for idx in combinations(range(d), r):
            b = blade(idx, SQ)
            b2 = GA.mul(b, b, SQ).get((), F(0))
            binv = GA.scal(1 / b2, b)
            total += GA.mul(GA.mul(GA.mul(binv, x, SQ), b, SQ), P, SQ).get((), F(0))
    return total


def check_spin_weights_are_the_same_in_three_four_and_five_dimensions():
    premise("synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces")
    for (p, q), factors, n_c in TOWER_ALGEBRAS:
        SQ = GA.sig(p, q)
        d = p + q
        Fb = generic_bivector(d, SQ)
        F2 = GA.mul(Fb, Fb, SQ)
        X = -2 * F2.get((), F(0))
        GA.check("X is not zero on the generic bivector", X != 0)
        GA.check("vector spin weight is -4", 4 * vector_trace_of_square(Fb, d, SQ) / X == -4)
        P = ONE
        for idx in factors:
            u = blade(idx, SQ)
            GA.check("idempotent factor squares to one", GA.eq(GA.mul(u, u, SQ), ONE))
            P = GA.scal(F(1, 2), GA.mul(P, GA.add(ONE, u), SQ))
        GA.check("P is idempotent", GA.eq({k: v for k, v in GA.mul(P, P, SQ).items() if v != 0},
                                          {k: v for k, v in P.items() if v != 0}))
        if (p, q) == (2, 1):
            I3 = blade(range(d), SQ)
            w = GA.mul(I3, P, SQ)
            GA.check("in Cl(2,1) the commutant element w = I P squares to +P", GA.eq(
                {k: v for k, v in GA.mul(w, w, SQ).items() if v != 0}, {k: v for k, v in P.items() if v != 0}))
            GA.check("and P A P is spanned by P and w", GA.rank_of_vectors(
                [[GA.mul(GA.mul(P, blade(idx, SQ), SQ), P, SQ).get(b, F(0)) for b in GA.all_blades(d)]
                 for r in range(d + 1) for idx in combinations(range(d), r)]) == 2)
        real_dim = ideal_trace(ONE, P, d, SQ)
        GA.check("the ideal has n_c complex components", real_dim == 2 * n_c)
        quarter = GA.scal(F(1, 4), F2)
        complex_trace = ideal_trace(quarter, P, d, SQ) / 2
        GA.check("spinor spin weight is -n_c/2", 4 * complex_trace / X == F(-n_c, 2))
    return True


def rule(sigma, w, n, s):
    return F(1, 3) * sigma * w * (n + 6 * s)


def vector_with_ghosts(d):
    return rule(1, F(1, 2), d, -4) + rule(-1, 1, 1, 0)


def spinor(n_c):
    return rule(-1, F(1, 2), n_c, F(-n_c, 2))


def check_rule_gives_d_minus_26_over_6_and_a_logarithm_only_in_four_dimensions():
    premise("synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces")
    premise("synthesis.imported-heat-kernel-coefficients-and-background-field-gauge")
    GA.check("stored values at d = 4", vector_with_ghosts(4) == F(-11, 3) and spinor(2) == F(2, 3)
             and spinor(4) == F(4, 3) and rule(1, 1, 1, 0) == F(1, 3))
    for d in range(2, 30):
        GA.check("vector with ghosts", vector_with_ghosts(d) == F(d - 26, 6))
        GA.check("its sign", (vector_with_ghosts(d) < 0) == (d < 26))
    GA.check("d = 3 and d = 5", vector_with_ghosts(3) == F(-23, 6) and vector_with_ghosts(5) == F(-7, 2))
    for n_c in range(1, 9):
        GA.check("spinor of n_c components", spinor(n_c) == F(n_c, 3))
    # the coefficient is a_k with k = 4 and multiplies t^((k - d)/2): t^0 (a logarithm) only at d = 4
    powers = dict((d, F(4 - d, 2)) for d in (3, 4, 5))
    GA.check("powers of the proper time", powers == {3: F(1, 2), 4: F(0), 5: F(-1, 2)})
    GA.check("mass dimension of the squared coupling", [4 - d for d in (3, 4, 5)] == [1, 0, -1])
    return True


def check_table_by_tower_on_the_stored_content():
    premise("synthesis.gauge-algebra-by-tower")
    premise("dark-tower-matter.three-dimensional-content")
    premise("dark-tower-matter.five-dimensional-content")
    premise("dark-tower-matter.three-dimensional-phases")
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-matter.no-coupling-rule-odd-towers-follows")
    premise("dark-tower-matter.r1-has-no-mechanism-odd-towers")
    premise("dark-tower-matter.five-dimensional-towers")
    premise("synthesis.one-loop-running-coefficients-from-spacetime-algebra-spin-traces")
    C2_SU3, T_TRIPLET = 3, F(1, 2)
    # three-dimensional towers: each so(2) factor, one unit-charge two-component fermion, no self-coupling
    GA.check("d = 3, each abelian factor", 0 * vector_with_ghosts(3) + spinor(2) * 1 ** 2 == F(2, 3))
    # five-dimensional towers under (S): (name, colour dimension, Y), four-component Dirac species
    species = (("U", 3, F(2, 3)), ("D", 3, F(-1, 3)), ("E", 1, F(-1)), ("N", 1, F(0)))
    triplets = sum(1 for (_, dim, _) in species if dim == 3)
    sumY2 = sum(dim * Y * Y for (_, dim, Y) in species)
    GA.check("two triplets and sum of dim Y^2 = 8/3", triplets == 2 and sumY2 == F(8, 3))
    GA.check("d = 5 colour under (S)", C2_SU3 * vector_with_ghosts(5) + triplets * spinor(4) * T_TRIPLET == F(-55, 6))
    GA.check("d = 5 colour without (S)", C2_SU3 * vector_with_ghosts(5) + spinor(4) * T_TRIPLET == F(-59, 6))
    GA.check("d = 5 abelian under (S)", spinor(4) * sumY2 == F(32, 9))
    GA.check("d = 5 abelian without (S)", spinor(4) * 3 * F(2, 3) ** 2 == F(16, 9))
    # four-dimensional reading of the same content, against the stored visible colour coefficient
    b_S = C2_SU3 * vector_with_ghosts(4) + triplets * spinor(4) * T_TRIPLET
    b_noS = C2_SU3 * vector_with_ghosts(4) + spinor(4) * T_TRIPLET
    b_vis = -11 + F(4 * 3, 3)
    GA.check("four-dimensional reading", (b_S, b_noS, b_vis) == (F(-29, 3), F(-31, 3), -7))
    GA.check("one copy of the (S) content is one generation's colour content", b_S == -11 + F(4, 3))
    GA.check("equal to the visible coefficient exactly at three copies", -11 + 3 * F(4, 3) == b_vis)
    GA.check("the exponent's coefficient 1/7 - 3/29", F(1, 7) - F(3, 29) == F(8, 203))
    return True
