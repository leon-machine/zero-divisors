"""synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate: exact checks.

Modes are the planes of Cl(m, m): generators e_k (square +1), f_k (square -1), parity p_k = f_k e_k. The adjoint is
the linear extension of the inverse on blades (it fixes every e_k and negates every f_k). An observable is a
self-adjoint element of square one; a state is x -> <rho x>_0 / <rho>_0 with rho a sum of terms y y^dagger.

(1) The square of the CHSH element and the certificate 8 - C^2 = (Z^dagger Z + {A1,A2}^2 + {B1,B2}^2)/2 with
    Z = [A1,A2] - [B1,B2], on rational directions of two modes and on observables that are not directions.
(2) The scalar part of x^dagger x is the sum of the squares of the coefficients; on sample states the value of C
    squared is at most the value of C^2, which is 8 minus half the three values of the certificate.
(3) The split: the directions of mode 1 and the Klein-twisted directions of mode 2 commute, the untwisted ones do
    not, and C^2 = 4 + 4 (a1 ^ a2)(b1 ^ b2) e_1 f_2.
(4) Over Q(sqrt 2) (pairs of rational elements): the idempotent P = (1 + K)/4 + sqrt 2 C/8, C P = 2 sqrt 2 P,
    P x P = 4 <P x>_0 P on all sixteen blades.
(5) A square-one element that is not self-adjoint has value above 4 on a state.
"""
from fractions import Fraction as F
from functools import reduce
from itertools import product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
NMODES_TWO, NMODES_THREE = 2, 3


def setup(m):
    sq = tuple(s for _ in range(m) for s in (1, -1))
    e = [GA.gen(2 * k) for k in range(m)]
    f = [GA.gen(2 * k + 1) for k in range(m)]
    par = [GA.mul(f[k], e[k], sq) for k in range(m)]
    return sq, e, f, par


def mul(sq, *xs):
    return reduce(lambda a, b: GA.mul(a, b, sq), xs)


def dagger(x):
    """Linear extension of the blade inverse: the reverse with a sign for every generator of square -1."""
    r = GA.reverse(x)
    return {b: (c if sum(1 for i in b if i % 2 == 1) % 2 == 0 else -c) for b, c in r.items()}


def s0(x):
    return x.get((), F(0))


def comm(sq, x, y):
    return GA.sub(mul(sq, x, y), mul(sq, y, x))


def acomm(sq, x, y):
    return GA.add(mul(sq, x, y), mul(sq, y, x))


def lin(c, x, s, y):
    return GA.add(GA.scal(F(c), x), GA.scal(F(s), y))


def chsh(sq, A1, A2, B1, B2):
    return GA.add(mul(sq, A1, GA.add(B1, B2)), mul(sq, A2, GA.sub(B1, B2)))


def is_observable(sq, x):
    return GA.eq(dagger(x), x) and GA.eq(mul(sq, x, x), ONE)


def value(sq, rho, x):
    return s0(mul(sq, rho, x)) / s0(rho)


def certificate_holds(sq, A1, A2, B1, B2):
    """C^2 = 4 - [A1,A2][B1,B2] and 8 - C^2 = (Z^dagger Z + SA^2 + SB^2)/2, exactly."""
    C = chsh(sq, A1, A2, B1, B2)
    X, Y = comm(sq, A1, A2), comm(sq, B1, B2)
    C2 = mul(sq, C, C)
    landau = GA.eq(C2, GA.sub(GA.scal(F(4), ONE), mul(sq, X, Y)))
    Z = GA.sub(X, Y)
    SA, SB = acomm(sq, A1, A2), acomm(sq, B1, B2)
    rhs = GA.scal(F(1, 2), GA.add(mul(sq, dagger(Z), Z), mul(sq, SA, SA), mul(sq, SB, SB)))
    return landau and GA.eq(GA.sub(GA.scal(F(8), ONE), C2), rhs)


# rational points of the circle x^2 + z^2 = 1
PTS = [(F(1), F(0)), (F(0), F(1)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(8, 17), F(-15, 17))]


def two_mode_settings():
    """Directions of mode 1 (span of e_1, p_1) and Klein-twisted directions of mode 2 (span of e_2 p_1, p_2)."""
    sq, e, f, par = setup(NMODES_TWO)
    E2 = mul(sq, e[1], par[0])
    return sq, e, f, par, E2


def sample_states(sq, gens):
    """States rho = y y^dagger for some rational y built from the generators."""
    ys = []
    g = gens
    ys.append(GA.add(ONE, g[0]))
    ys.append(GA.add(GA.scal(F(2), ONE), mul(sq, g[0], g[2]), GA.scal(F(-1, 3), g[1])))
    ys.append(GA.add(g[3], GA.scal(F(5, 2), mul(sq, g[0], g[1], g[2])), ONE))
    ys.append(GA.add(mul(sq, g[1], g[3]), GA.scal(F(3), mul(sq, g[0], g[3])), GA.scal(F(-2), g[2]), ONE))
    rhos = [mul(sq, y, dagger(y)) for y in ys]
    rhos.append(GA.add(rhos[0], rhos[2]))
    return rhos


# ------------------------------------------------------------------ (1)
def check_square_of_the_chsh_element_and_the_rational_certificate():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.division-gives-the-rationals")
    sq, e, f, par, E2 = two_mode_settings()
    count = 0
    ok = True
    for a1, a2, b1, b2 in product(PTS, repeat=4):
        A1, A2 = lin(a1[0], e[0], a1[1], par[0]), lin(a2[0], e[0], a2[1], par[0])
        B1, B2 = lin(b1[0], E2, b1[1], par[1]), lin(b2[0], E2, b2[1], par[1])
        ok = ok and all(is_observable(sq, x) for x in (A1, A2, B1, B2))
        ok = ok and GA.commutes(A1, B1, sq) and GA.commutes(A2, B2, sq)
        ok = ok and certificate_holds(sq, A1, A2, B1, B2)
        count += 1
    assert ok and count == 625
    # observables that are not directions: three modes, party A on modes 1 and 2, party B on mode 3 twisted
    sq, e, f, par = setup(NMODES_THREE)
    G = mul(sq, par[0], par[1])
    A1 = e[0]
    A2 = GA.add(GA.scal(F(1, 2), mul(sq, GA.add(ONE, par[1]), e[0])),
                GA.scal(F(1, 2), mul(sq, GA.sub(ONE, par[1]), par[0])))
    A3 = lin(F(3, 5), e[1], F(4, 5), par[1])
    B1, B2 = mul(sq, e[2], G), lin(F(5, 13), mul(sq, e[2], G), F(12, 13), par[2])
    assert all(is_observable(sq, x) for x in (A1, A2, A3, B1, B2))
    assert all(GA.commutes(a, b, sq) for a in (A1, A2, A3) for b in (B1, B2))
    # the anticommutator of A1 and A2 is 1 + p_2, not a scalar
    assert GA.eq(acomm(sq, A1, A2), GA.add(ONE, par[1]))
    assert certificate_holds(sq, A1, A2, B1, B2)
    assert certificate_holds(sq, A2, A3, B1, B2)
    assert certificate_holds(sq, A3, A1, B2, B1)


# ------------------------------------------------------------------ (2)
def check_scalar_part_is_positive_and_every_sample_state_obeys_the_bound():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("synthesis.division-gives-the-rationals")
    sq, e, f, par, E2 = two_mode_settings()
    blades = [{b: F(1)} for b in GA.all_blades(2 * NMODES_TWO)]
    assert len(blades) == 16
    # the adjoint of a blade is its inverse, so <x^dagger x>_0 is the sum of the squared coefficients
    assert all(GA.eq(mul(sq, dagger(b), b), ONE) for b in blades)
    x = GA.add(GA.scal(F(2), e[0]), GA.scal(F(-3), f[1]), GA.scal(F(1, 2), mul(sq, e[0], f[0], e[1])), ONE)
    assert s0(mul(sq, dagger(x), x)) == F(4) + F(9) + F(1, 4) + F(1)
    y = GA.add(par[0], GA.scal(F(7), mul(sq, e[1], f[1], f[0])))
    assert GA.eq(dagger(mul(sq, x, y)), mul(sq, dagger(y), dagger(x)))
    rhos = sample_states(sq, [e[0], f[0], e[1], f[1]])
    # a state close to the bound at the anticommuting settings: y = (14/5 + C)(1 + K)
    Cs = chsh(sq, e[0], par[0], E2, par[1])
    ynear = mul(sq, GA.add(GA.scal(F(14, 5), ONE), Cs), GA.add(ONE, mul(sq, e[0], f[1])))
    rhos.append(mul(sq, ynear, dagger(ynear)))
    assert value(sq, rhos[-1], Cs) == F(280, 99)
    settings = [(PTS[0], PTS[1], PTS[0], PTS[1]), (PTS[2], PTS[1], PTS[3], PTS[0]), (PTS[4], PTS[3], PTS[2], PTS[4])]
    worst = F(0)
    for (a1, a2, b1, b2) in settings:
        A1, A2 = lin(a1[0], e[0], a1[1], par[0]), lin(a2[0], e[0], a2[1], par[0])
        B1, B2 = lin(b1[0], E2, b1[1], par[1]), lin(b2[0], E2, b2[1], par[1])
        C = chsh(sq, A1, A2, B1, B2)
        C2 = mul(sq, C, C)
        Z = GA.sub(comm(sq, A1, A2), comm(sq, B1, B2))
        ZZ = mul(sq, dagger(Z), Z)
        SA, SB = acomm(sq, A1, A2), acomm(sq, B1, B2)
        for rho in rhos:
            assert s0(rho) > 0 and GA.eq(dagger(rho), rho)
            v, v2 = value(sq, rho, C), value(sq, rho, C2)
            parts = [value(sq, rho, ZZ), value(sq, rho, mul(sq, SA, SA)), value(sq, rho, mul(sq, SB, SB))]
            assert all(t >= 0 for t in parts)
            assert v2 == F(8) - F(1, 2) * sum(parts)
            assert v * v <= v2 <= F(8)
            worst = max(worst, v * v)
    # the largest squared value met on these samples, pinned
    assert worst == F(78400, 9801) and F(8) - worst == F(8, 9801)


# ------------------------------------------------------------------ (3)
def check_klein_twisted_directions_commute_and_the_square_is_four_plus_four_wedges_k():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("singularity.descent-parity-average")
    sq, e, f, par, E2 = two_mode_settings()
    K = mul(sq, e[0], f[1])
    assert GA.eq(dagger(K), K) and GA.eq(mul(sq, K, K), ONE)
    # untwisted: the two sub-Clifford algebras do not commute, and e_1 e_2 is not an observable
    assert GA.anticommutes(e[0], e[1], sq)
    u = mul(sq, e[0], e[1])
    assert GA.eq(mul(sq, u, u), GA.scal(F(-1), ONE)) and GA.eq(dagger(u), GA.scal(F(-1), u))
    # f_k is not self-adjoint: the self-adjoint part of a mode is spanned by 1, e_k, p_k
    assert GA.eq(dagger(f[0]), GA.scal(F(-1), f[0])) and is_observable(sq, par[0]) and is_observable(sq, e[0])
    assert GA.anticommutes(e[0], par[0], sq) and GA.anticommutes(E2, par[1], sq)
    # parity: the total parity anticommutes with e_1 and e_2 p_1 and commutes with p_1, p_2, so the parity
    # average of a direction keeps only its p-component
    G = mul(sq, par[0], par[1])
    assert GA.anticommutes(G, e[0], sq) and GA.anticommutes(G, E2, sq)
    assert GA.commutes(G, par[0], sq) and GA.commutes(G, par[1], sq)
    d = lin(F(3, 5), E2, F(4, 5), par[1])
    assert GA.eq(GA.scal(F(1, 2), GA.add(d, mul(sq, G, d, G))), GA.scal(F(4, 5), par[1]))
    count = 0
    for a1, a2, b1, b2 in product(PTS, repeat=4):
        A1, A2 = lin(a1[0], e[0], a1[1], par[0]), lin(a2[0], e[0], a2[1], par[0])
        B1, B2 = lin(b1[0], E2, b1[1], par[1]), lin(b2[0], E2, b2[1], par[1])
        wa = a1[0] * a2[1] - a1[1] * a2[0]
        wb = b1[0] * b2[1] - b1[1] * b2[0]
        da = a1[0] * a2[0] + a1[1] * a2[1]
        C = chsh(sq, A1, A2, B1, B2)
        assert GA.eq(mul(sq, C, C), GA.add(GA.scal(F(4), ONE), GA.scal(F(4) * wa * wb, K)))
        assert GA.eq(acomm(sq, A1, A2), GA.scal(F(2) * da, ONE)) and wa * wa + da * da == F(1)
        assert GA.commutes(K, C, sq)
        count += 1
    assert count == 625
    C = chsh(sq, e[0], par[0], E2, par[1])
    assert GA.eq(mul(sq, C, C), GA.add(GA.scal(F(4), ONE), GA.scal(F(4), K)))
    assert GA.eq(mul(sq, C, C, C), GA.scal(F(8), C)) and GA.eq(mul(sq, K, C), C)


# ------------------------------------------------------------------ (4)  Q(sqrt 2) as pairs (a, b) = a + b sqrt 2
def r2_mul(sq, x, y):
    return (GA.add(mul(sq, x[0], y[0]), GA.scal(F(2), mul(sq, x[1], y[1]))),
            GA.add(mul(sq, x[0], y[1]), mul(sq, x[1], y[0])))


def r2_eq(x, y):
    return GA.eq(x[0], y[0]) and GA.eq(x[1], y[1])


def check_saturating_state_is_a_pure_state_over_the_field_with_root_two():
    premise("synthesis.mode-split-of-the-clifford-algebra-and-its-klein-twist-to-the-tensor-product")
    premise("synthesis.division-gives-the-rationals")
    sq, e, f, par, E2 = two_mode_settings()
    K = mul(sq, e[0], f[1])
    C = chsh(sq, e[0], par[0], E2, par[1])
    P = (GA.scal(F(1, 4), GA.add(ONE, K)), GA.scal(F(1, 8), C))
    assert r2_eq(r2_mul(sq, P, P), P)
    assert GA.eq(dagger(P[0]), P[0]) and GA.eq(dagger(P[1]), P[1])
    # C P = 2 sqrt 2 P
    assert r2_eq(r2_mul(sq, (C, {}), P), r2_mul(sq, ({}, GA.scal(F(2), ONE)), P))
    # trace one and value 2 sqrt 2: 4 <P>_0 = 1, 4 <P C>_0 = 0 + 2 sqrt 2
    assert F(4) * s0(P[0]) == F(1) and s0(P[1]) == F(0)
    PC = r2_mul(sq, P, (C, {}))
    assert (F(4) * s0(PC[0]), F(4) * s0(PC[1])) == (F(0), F(2))
    # rank one: P x P = 4 <P x>_0 P on every blade
    n = 0
    for b in GA.all_blades(2 * NMODES_TWO):
        x = ({b: F(1)}, {})
        Px = r2_mul(sq, P, x)
        t = (GA.scal(F(4) * s0(Px[0]), ONE), GA.scal(F(4) * s0(Px[1]), ONE))
        assert r2_eq(r2_mul(sq, Px, P), r2_mul(sq, t, P))
        n += 1
    assert n == 16
    # the projection onto the blades of mode 1 is 1/4 (reduced state 1/2); the projection onto the blades of
    # mode 2 is 1/4 + sqrt 2 e_2 / 8, which is not the reduction of the twisted split (P is not even)
    on_a = [{b: c for b, c in part.items() if set(b) <= {0, 1}} for part in P]
    on_b = [{b: c for b, c in part.items() if set(b) <= {2, 3}} for part in P]
    assert GA.eq(on_a[0], GA.scal(F(1, 4), ONE)) and on_a[1] == {}
    assert GA.eq(on_b[0], GA.scal(F(1, 4), ONE)) and GA.eq(on_b[1], GA.scal(F(1, 8), e[1]))
    # P is not even: it does not commute with the total parity
    G = mul(sq, par[0], par[1])
    assert not GA.commutes(G, P[1], sq) and GA.commutes(G, P[0], sq)


# ------------------------------------------------------------------ (5)
def check_square_one_element_that_is_not_self_adjoint_exceeds_four():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    sq, e, f, par, E2 = two_mode_settings()
    A = lin(F(17, 8), e[0], F(15, 8), f[0])
    assert GA.eq(mul(sq, A, A), ONE) and not GA.eq(dagger(A), A)
    assert GA.commutes(A, par[1], sq) and is_observable(sq, par[1])
    rho = GA.scal(F(1, 4), mul(sq, GA.add(ONE, e[0]), GA.add(ONE, par[1])))
    assert GA.eq(mul(sq, rho, rho), rho) and GA.eq(dagger(rho), rho)
    C = chsh(sq, A, A, par[1], par[1])
    assert value(sq, rho, C) == F(17, 4) and F(17, 4) > F(4)
    # the identity for the square still holds: C^2 = 4, so the value of C^2 is 4 while the value of C is 17/4
    assert GA.eq(mul(sq, C, C), GA.scal(F(4), ONE))
    assert value(sq, rho, C) ** 2 > value(sq, rho, mul(sq, C, C))
