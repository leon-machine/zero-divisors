"""synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three: exact checks.

Cl(3,0) with e_1, e_2, e_3 of square +1.  Its even subalgebra holds x = x_0 + x_1 B_1 + x_2 B_2 + x_3 B_3 with
B_1 = e_3 e_2, B_2 = e_1 e_3, B_3 = e_2 e_1 (B_1 B_2 = B_3, B_k^2 = -1).  N(x) = x x~ is the scalar
x_0^2 + x_1^2 + x_2^2 + x_3^2.  Everything is integer or Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

SQ3 = (1, 1, 1)
ONE = GA.sc(F(1))
B = [GA.mul(GA.gen(2), GA.gen(1), SQ3), GA.mul(GA.gen(0), GA.gen(2), SQ3), GA.mul(GA.gen(1), GA.gen(0), SQ3)]


def even(x):
    out = GA.sc(F(x[0]))
    for k in range(3):
        out = GA.add(out, GA.scal(F(x[k + 1]), B[k]))
    return out


def coeffs(X):
    """Components (x_0, x_1, x_2, x_3) of an even element in the basis 1, B_1, B_2, B_3."""
    out = []
    for basis in [ONE] + B:
        (blade, c), = basis.items()
        out.append(X.get(blade, F(0)) / c)
    return tuple(out)


def norm(X):
    n = GA.mul(X, GA.reverse(X), SQ3)
    assert set(n) <= {()}
    return n.get((), F(0))


def four_squares(n):
    """One representation of the integer n >= 0 as a sum of four squares, by search (largest term first)."""
    a = 0
    while (a + 1) * (a + 1) <= n:
        a += 1
    while a >= 0:
        r1 = n - a * a
        b = min(a, int_sqrt(r1))
        while b >= 0:
            r2 = r1 - b * b
            c = min(b, int_sqrt(r2))
            while c >= 0:
                r3 = r2 - c * c
                d = int_sqrt(r3)
                if d * d == r3 and d <= c:
                    return (a, b, c, d)
                c -= 1
            b -= 1
        a -= 1
    return None


def int_sqrt(n):
    if n < 0:
        return -1
    x = 0
    while (x + 1) * (x + 1) <= n:
        x += 1
    return x


def primes_up_to(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int_sqrt(p) + 1))]


def check_norm_of_the_even_subalgebra_is_a_sum_of_four_squares_and_multiplicative():
    premise("std-algebra.quaternions")
    ok = True
    ok = ok and GA.eq(GA.mul(B[0], B[1], SQ3), B[2]) and all(GA.eq(GA.mul(b, b, SQ3), GA.sc(F(-1))) for b in B)
    samples = [(1, 2, 3, 4), (2, -1, 0, 5), (F(1, 2), F(1, 3), -2, 1), (0, 1, 1, 1), (3, 0, 0, 0),
               (F(2, 7), 3, F(-1, 5), 0), (1, 1, 1, 2), (5, -3, 2, F(1, 4))]
    count = 0
    for x in samples:
        X = even(x)
        ok = ok and coeffs(X) == tuple(F(c) for c in x)
        ok = ok and norm(X) == sum(F(c) * F(c) for c in x)
        for y in samples:
            Y = even(y)
            XY = GA.mul(X, Y, SQ3)
            ok = ok and all(len(b) % 2 == 0 for b in XY)
            ok = ok and norm(XY) == norm(X) * norm(Y)
            count += 1
    ok = ok and count == 64
    GA.check("x x~ is the sum of the four squared components and N(xy) = N(x) N(y) on 64 pairs of even elements", ok)
    return ok


def check_descent_writes_every_odd_prime_below_two_hundred_as_a_square_of_an_integer_even_element():
    premise("std-algebra.quaternions")
    ok, done = True, 0
    for p in primes_up_to(199):
        if p == 2:
            continue
        half = (p - 1) // 2
        # step (3) of the proof: a^2 + b^2 + 1 = 0 modulo p with 0 <= a, b <= (p-1)/2
        sols = [(a, b) for a in range(half + 1) for b in range(half + 1) if (a * a + b * b + 1) % p == 0]
        ok = ok and len(sols) > 0
        a, b = sols[0]
        x = (a, b, 1, 0)
        m = (a * a + b * b + 1) // p
        ok = ok and 0 < m < p
        steps = 0
        while m > 1:
            if m % 2 == 0:
                # pair components of equal parity; the half sums and differences have norm m p / 2
                ev = sorted(x, key=lambda c: c % 2)
                ok = ok and (ev[0] - ev[1]) % 2 == 0 and (ev[2] - ev[3]) % 2 == 0
                x = ((ev[0] + ev[1]) // 2, (ev[0] - ev[1]) // 2, (ev[2] + ev[3]) // 2, (ev[2] - ev[3]) // 2)
                ok = ok and sum(c * c for c in x) == (m // 2) * p
                m = m // 2
            else:
                y = tuple(((c + (m - 1) // 2) % m) - (m - 1) // 2 for c in x)   # residues in (-m/2, m/2)
                ok = ok and all((c - d) % m == 0 and 2 * abs(d) < m for c, d in zip(x, y))
                ny = sum(c * c for c in y)
                ok = ok and ny % m == 0 and 0 < ny < m * m
                m2 = ny // m
                Z = GA.mul(even(x), even(y), SQ3)
                z = coeffs(Z)
                ok = ok and all(c.denominator == 1 and c.numerator % m == 0 for c in z)
                x = tuple(c.numerator // m for c in z)
                ok = ok and sum(c * c for c in x) == m2 * p and m2 < m
                m = m2
            steps += 1
            if steps > 60:
                ok = False
                break
        ok = ok and sum(c * c for c in x) == p
        done += 1
    ok = ok and done == 45
    GA.check("for the 45 odd primes below 200 the descent ends at an integer even element of square p", ok)
    return ok


def check_integers_to_three_thousand_are_sums_of_four_squares_and_three_fail_exactly_on_the_sevens():
    ok = True
    three = set()
    lim = 3000
    r = int_sqrt(lim)
    for a, b, c in product(range(r + 1), repeat=3):
        s = a * a + b * b + c * c
        if s <= lim:
            three.add(s)
    for n in range(1, lim + 1):
        q = four_squares(n)
        ok = ok and q is not None and sum(c * c for c in q) == n
        m = n
        while m % 4 == 0:
            m //= 4
        ok = ok and ((n in three) == (m % 8 != 7))
    GA.check("1..3000 are sums of four squares; exactly the 4^a(8b+7) are not sums of three", ok)
    return ok


def check_seven_times_a_square_is_never_a_sum_of_three_squares():
    ok = True
    sq8 = sorted({(a * a) % 8 for a in range(8)})
    ok = ok and sq8 == [0, 1, 4]
    # an odd d: 7 d^2 = 7 modulo 8, and no three squares sum to 7 modulo 8
    ok = ok and all((7 * d * d) % 8 == 7 for d in (1, 3, 5, 7))
    ok = ok and all((a + b + c) % 8 != 7 for a in sq8 for b in sq8 for c in sq8)
    # an even d: the sum is 0 modulo 4, which forces a, b, c all even (then divide all four by 2)
    ok = ok and all(((a * a + b * b + c * c) % 4 != 0) or (a % 2 == 0 and b % 2 == 0 and c % 2 == 0)
                    for a in range(4) for b in range(4) for c in range(4))
    # no solution of a^2 + b^2 + c^2 = 7 d^2 with 1 <= d <= 40
    r = set()
    for a in range(0, 107):
        for b in range(a, 107):
            r.add(a * a + b * b)
    hit = False
    for d in range(1, 41):
        t = 7 * d * d
        for c in range(0, int_sqrt(t) + 1):
            if (t - c * c) in r:
                hit = True
    ok = ok and not hit
    GA.check("a^2 + b^2 + c^2 = 7 d^2 has no solution: the tables modulo 8 and 4, and none with d <= 40", ok)
    return ok


def check_positive_rationals_are_squares_and_positive_semidefinite_matrices_are_sums_of_squares():
    premise("synthesis.division-gives-the-rationals")
    ok = True
    for t in [F(7), F(7, 9), F(3, 5), F(22, 7), F(1, 28), F(15), F(23, 2), F(60, 11)]:
        q = four_squares(t.numerator * t.denominator)
        x = tuple(F(c, t.denominator) for c in q)
        ok = ok and norm(even(x)) == t
    # a positive semidefinite rational matrix is a sum of at most 4n matrices x x^T
    A = [[F(2), F(1), F(0)], [F(1), F(5), F(3)], [F(0), F(3), F(7)]]
    n = 3
    L = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    D = [F(0)] * n
    W = [row[:] for row in A]
    for j in range(n):
        D[j] = W[j][j]
        ok = ok and D[j] > 0
        for i in range(j + 1, n):
            L[i][j] = W[i][j] / D[j]
        for i in range(j + 1, n):
            for k in range(j + 1, n):
                W[i][k] -= L[i][j] * L[k][j] * D[j]
    S = [[F(0)] * n for _ in range(n)]
    terms = 0
    for j in range(n):
        q = four_squares(D[j].numerator * D[j].denominator)
        for c in q:
            if c == 0:
                continue
            col = [F(c, D[j].denominator) * L[i][j] for i in range(n)]
            for i in range(n):
                for k in range(n):
                    S[i][k] += col[i] * col[k]
            terms += 1
    ok = ok and S == A and terms <= 4 * n
    GA.check("eight positive rationals are squares x x~; a 3 by 3 positive matrix is a sum of at most 12 squares", ok)
    return ok
