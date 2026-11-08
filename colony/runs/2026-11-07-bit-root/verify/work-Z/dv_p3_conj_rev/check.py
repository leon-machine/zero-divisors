"""synthesis.division-gives-the-rationals: exact checks.

Cl_R(p,q) for a subring R of Q is the R-span of the blades e_S with the blade product
e_S e_T = (-1)^f(S,T) e_{S xor T}, f(S,T) = #{(i,j) in S x T : i > j} + |S cap T cap N|.
GA.py multiplies with Fraction coefficients; integer inputs stay integral, so the products
computed here are products in Cl_Z(p,q) (and in Cl_Q(p,q)).
(0) The blade product of GA.py is the rule above (structure constants +-1, closure over Z), the
    twisting function is bilinear over F2 (so the ring is associative), and v^2 = Q(v) for integer
    vectors, in every signature with n <= 4.
(1) Inverses: for integer vectors v with Q(v) != 0 in a box, in four signatures, v (v/Q(v)) = 1 and
    v/Q(v) has coefficients in Z[1/P] exactly when Q(v) is a unit of Z[1/P], for five prime sets P;
    hand-computed inverses of 3e1 + 4e2 in Cl(2,0) and 2e1 + e2 in Cl(1,1).
(2) The smallest ring: e1 (m e1)^{-1} = 1/m for m = 1..30, so every prime up to 29 must be inverted;
    every rational a/m is the scalar e1 (a e1)(m e1)^{-1} ... built from integer blades and inverses.
(3) What division leaves: nonzero null vectors exist exactly for p, q >= 1; zero divisors exist exactly
    for (p,q) outside {(0,0),(0,1),(0,2)}, exhibited with integer coefficients for every (p,q) with
    n <= 5; in Cl(0,1) and Cl(0,2) x xbar is the sum of the squares of the coefficients.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise


def blades(n):
    return [S for k in range(n + 1) for S in combinations(range(n), k)]


def f_twist(S, T, p):
    return sum(1 for i in S for j in T if i > j) + sum(1 for i in S if i in T and i >= p)


def vec(coeffs):
    return {(i,): F(a) for i, a in enumerate(coeffs) if a != 0}


def qval(coeffs, p):
    return sum(a * a for a in coeffs[:p]) - sum(a * a for a in coeffs[p:])


def primes_of(m):
    m, out, d = abs(m), set(), 2
    while d * d <= m:
        while m % d == 0:
            out.add(d)
            m //= d
        d += 1
    if m > 1:
        out.add(m)
    return out


def in_ZP(x, P):
    """x in Z[1/P]: the primes of the reduced denominator lie in P."""
    return primes_of(F(x).denominator) <= set(P)


def is_unit_ZP(m, P):
    return m != 0 and primes_of(m) <= set(P)


def conj(x):
    """Clifford conjugation: grade involution composed with reversion."""
    return GA.reverse(x)


def check_blade_product_is_the_twisted_rule():
    premise("std-algebra.orthogonal-anticommute")
    count = 0
    for n in range(1, 5):
        for p in range(n + 1):
            sq = GA.sig(p, n - p)
            B = blades(n)
            for S in B:
                for T in B:
                    prod_ = GA.mul({S: F(1)}, {T: F(1)}, sq)
                    X = tuple(sorted(set(S) ^ set(T)))
                    assert prod_ == {X: F((-1) ** f_twist(S, T, p))}
                    count += 1
            # bilinearity of f over F2 in each slot (hence associativity)
            for S, T, U in product(B, repeat=3):
                ST = tuple(sorted(set(S) ^ set(T)))
                TU = tuple(sorted(set(T) ^ set(U)))
                assert (f_twist(ST, U, p) - f_twist(S, U, p) - f_twist(T, U, p)) % 2 == 0
                assert (f_twist(S, TU, p) - f_twist(S, T, p) - f_twist(S, U, p)) % 2 == 0
            # v^2 = Q(v) for integer vectors
            for coeffs in product((-2, 0, 1, 3), repeat=n):
                v = vec(coeffs)
                assert GA.mul(v, v, sq) == GA.sc(qval(coeffs, p))
    # sum over n of (n + 1) signatures times 4^n ordered pairs of blades
    assert count == 2 * 4 + 3 * 16 + 4 * 64 + 5 * 256
    return True


def check_vector_invertible_exactly_when_its_square_is_a_unit():
    premise("std-algebra.inverse-of-vector")
    Psets = [(), (2,), (3,), (2, 3), (2, 5)]
    tally = {}
    for (p, q) in ((2, 0), (1, 1), (0, 3), (1, 2)):
        n = p + q
        sq = GA.sig(p, q)
        for coeffs in product(range(-3, 4), repeat=n):
            m = qval(coeffs, p)
            if m == 0:
                continue
            v = vec(coeffs)
            u = GA.scal(F(1, m), v)
            assert GA.mul(v, u, sq) == GA.sc(1) and GA.mul(u, v, sq) == GA.sc(1)
            for P in Psets:
                coeffs_ok = all(in_ZP(c, P) for c in u.values())
                assert coeffs_ok == is_unit_ZP(m, P)
                tally[P] = tally.get(P, 0) + (1 if coeffs_ok else 0)
    # hand-computed inverses
    s20 = GA.sig(2, 0)
    v = vec((3, 4))
    assert GA.mul(v, GA.scal(F(1, 25), v), s20) == GA.sc(1)
    s11 = GA.sig(1, 1)
    w = vec((2, 1))
    assert qval((2, 1), 1) == 3
    assert GA.mul(w, {(0,): F(2, 3), (1,): F(1, 3)}, s11) == GA.sc(1)
    # over Z only the vectors of square +-1 are invertible: +-e1, +-e2 in (2,0) and in (1,1)
    # (a^2 - b^2 = (a - b)(a + b) = +-1), +-e_i in (0,3); in (1,2), a^2 - b^2 - c^2 = 1 has the
    # 2 + 8 solutions (+-1,0,0), (+-3,+-2,+-2) in the box and = -1 has 4 + 8 + 16 + 16 (a = 0,1,2,3)
    assert tally[()] == 4 + 4 + 6 + (2 + 8) + (4 + 8 + 16 + 16)
    return True


def check_the_smallest_ring_of_division_is_the_rationals():
    premise("std-algebra.inverse-of-vector")
    needed = set()
    for (p, q) in ((1, 0), (0, 1), (1, 1)):
        sq = GA.sig(p, q)
        e1 = GA.gen(0)
        for m in range(1, 31):
            v = GA.scal(m, e1)
            Qv = qval((m,) + (0,) * (q + p - 1), p)
            assert Qv == (m * m if p >= 1 else -m * m)
            vinv = GA.scal(F(1, Qv), v)
            assert GA.mul(v, vinv, sq) == GA.sc(1)
            # e1 (m e1)^{-1} is the scalar 1/m
            assert GA.mul(e1, vinv, sq) == GA.sc(F(1, m))
            needed |= primes_of(m)
            # a/m = (a e1)(m e1)^{-1}
            for a in (1, -2, 7):
                assert GA.mul(GA.scal(a, e1), vinv, sq) == GA.sc(F(a, m))
    assert sorted(needed) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    # the grade-0 part of a product of rational elements is a rational multiple of 1
    sq = GA.sig(1, 2)
    x = GA.add(GA.sc(F(1, 2)), GA.scal(F(2, 3), GA.gen(0)), {(1, 2): F(-5, 7)})
    y = GA.add(GA.sc(3), GA.scal(F(1, 5), GA.gen(1)), {(0, 1, 2): F(1, 4)})
    xy = GA.mul(x, y, sq)
    assert xy[()] == F(3, 2)
    return True


def check_null_vectors_and_zero_divisors_survive_division():
    division = []
    for n in range(0, 6):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p, q)
            # nonzero null vectors exist exactly when p, q >= 1
            has_null = any(qval(c, p) == 0 for c in product(range(-2, 3), repeat=n) if any(c))
            assert has_null == (p >= 1 and q >= 1)
            if p >= 1 and q >= 1:
                nv = GA.add(GA.gen(0), GA.gen(p))
                assert GA.mul(nv, nv, sq) == {} and nv != {}
            zd = None
            if p >= 1:
                a, b = GA.add(GA.sc(1), GA.gen(0)), GA.sub(GA.sc(1), GA.gen(0))
                zd = (a, b)
            elif q >= 3:
                w = {(0, 1, 2): F(1)}
                assert GA.mul(w, w, sq) == GA.sc(1)
                zd = (GA.add(GA.sc(1), w), GA.sub(GA.sc(1), w))
            if zd:
                assert zd[0] and zd[1] and GA.mul(zd[0], zd[1], sq) == {}
            else:
                division.append((p, q))
                # x xbar = sum of squares of the coefficients: a division ring over Q
                for cs in product((-2, 1, 3), repeat=2 ** n):
                    x = {S: F(c) for S, c in zip(blades(n), cs)}
                    assert GA.mul(x, conj(x), sq) == GA.sc(sum(c * c for c in cs))
                    assert GA.mul(conj(x), x, sq) == GA.sc(sum(c * c for c in cs))
    assert division == [(0, 0), (0, 1), (0, 2)]
    return True
