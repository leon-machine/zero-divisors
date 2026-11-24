"""synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values: exact checks.

The antiperiodic array on M thermal periods is the product of the M arrays of twist (2j + 1)/(2M) (stored).
B_1(a) = a - 1/2, B_2(a) = a^2 - a + 1/6.  A real character modulo 2M is given by a Kronecker symbol.  Scalars only
(grade 0); GA is used for the one statement with a bivector, the unit of the characters of order four.
Everything is integer or Fraction arithmetic.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def b1(a):
    return a - F(1, 2)


def b2(a):
    return a * a - a + F(1, 6)


def jacobi(a, n):
    """Jacobi symbol (a/n), n odd and positive."""
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                out = -out
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            out = -out
        a %= n
    return out if n == 1 else 0


def kronecker(D, a):
    """Kronecker symbol (D/a) for a fundamental discriminant D and an integer a > 0."""
    if a % 2 == 0:
        if D % 2 == 0:
            return 0
        two = 1 if D % 8 in (1, 7) else -1
        return two * kronecker(D, a // 2)
    if D % 2:
        # (D/a) for odd D: quadratic reciprocity in the form (D/a) = (a/|D|) for D = 1 mod 4
        return jacobi(a, abs(D))
    # even D = 4m or 8m: (D/a) = (2/a)^e (m'/a) (-1/a)^[m' < 0]
    m, e = D, 0
    while m % 2 == 0:
        m //= 2
        e += 1
    val = jacobi(abs(m), a) if abs(m) > 1 else 1
    if m < 0 and a % 4 == 3:
        val = -val
    if e % 2 and a % 8 in (3, 5):
        val = -val
    return val


def l_value(D, f, k):
    """L(1 - k, chi) for chi = (D/.) read as a character modulo f, from the generalised Bernoulli number:
    L(1 - k, chi) = -(f^(k-1)/k) sum_{a=1}^{f} chi(a) B_k(a/f)."""
    bern = {1: b1, 2: b2}[k]
    tot = F(0)
    for a in range(1, f + 1):
        c = kronecker(D, a) if gcd(a, f) == 1 else 0
        tot += c * bern(F(a, f))
    return -F(f ** (k - 1), k) * tot


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def class_number(D):
    """Number of reduced positive definite forms a x^2 + b x y + c y^2 of discriminant D < 0."""
    h = 0
    b = D % 2
    while 3 * b * b <= -D:
        q = (b * b - D) // 4
        a = max(b, 1)
        while a * a <= q:
            if q % a == 0:
                c = q // a
                if b == 0 or a == b or a == c:
                    h += 1
                else:
                    h += 2
            a += 1
        b += 2
    return h


def sigma(n):
    return sum(d for d in range(1, n + 1) if n % d == 0)


# (discriminant D, M) with D prime to 2 or dividing 2M suitably: chi = (D/.) is a character modulo 2M
CASES = [(-4, 2), (8, 4), (-8, 4), (-3, 3), (12, 6), (5, 5), (-7, 7), (-20, 10), (-15, 15), (-23, 23), (-4, 6),
         (8, 12), (13, 13), (-11, 11)]


def check_fibre_sums_of_asymmetry_and_sea_energy_are_the_generalised_bernoulli_numbers():
    premise("synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages")
    premise("synthesis.null-ordering-of-counted-units-is-zeta-symmetric")
    premise("synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums")
    ok, count = True, 0
    seen = {}
    for D, M in CASES:
        f = 2 * M
        twists = [F(2 * j + 1, f) for j in range(M)]
        # the stored product rule: the twists are the solutions of M delta = 1/2 modulo 1, and the sea energies add
        ok = ok and all((M * d - F(1, 2)).denominator == 1 for d in twists)
        ok = ok and sum(b2(d) for d in twists) == b2(F(1, 2)) / M
        chi = [kronecker(D, 2 * j + 1) if gcd(2 * j + 1, f) == 1 else 0 for j in range(M)]
        # a character modulo 2M: multiplicative on the odd residues
        for i in range(M):
            for j in range(M):
                p = ((2 * i + 1) * (2 * j + 1)) % f
                ok = ok and chi[(p - 1) // 2] == chi[i] * chi[j]
        asym = sum(c * (1 - 2 * d) for c, d in zip(chi, twists))
        energy = sum(c * b2(d) for c, d in zip(chi, twists))
        ok = ok and asym == 2 * l_value(D, f, 1)
        ok = ok and energy == -l_value(D, f, 2) / M
        # parity: an even character sees no asymmetry, an odd one no sea energy
        if D > 0:
            ok = ok and asym == 0
        else:
            ok = ok and energy == 0
        seen[(D, M)] = (asym, energy)
        count += 1
    ok = ok and count == 14
    # the instances of clause (v)
    ok = ok and [seen[k][0] for k in ((-4, 2), (-8, 4), (-20, 10), (-3, 3), (-11, 11))] == [1, 2, 4, F(4, 3), 4]
    ok = ok and [seen[k][0] for k in ((-7, 7), (-15, 15), (-23, 23))] == [0, 0, 0]
    ok = ok and [seen[k][1] for k in ((8, 4), (12, 6), (5, 5), (13, 13))] == [F(1, 4), F(1, 3), F(6, 25), F(6, 13)]
    GA.check("14 real characters: the fibre sums are 2 L(0, chi) and -L(-1, chi)/M; parity kills one of them", ok)
    return ok


def check_the_values_agree_with_class_numbers_and_with_the_divisor_sum_formula():
    premise("synthesis.imported-hurwitz-zeta-values-and-dirichlet-l-functions-as-hurwitz-sums")
    premise("synthesis.imported-class-number-formula-at-zero-for-negative-discriminants")
    premise("synthesis.imported-zeta-of-a-real-quadratic-field-at-minus-one-as-a-divisor-sum")
    ok = True
    units = {-3: 6, -4: 4}
    # odd characters: L(0, chi_D) = 2 h(D) / w(D) at the conductor, times 1 - chi(2) when 2M has an extra factor 2
    for D, M in CASES:
        if D > 0:
            continue
        f = 2 * M
        cond = -D
        prim = l_value(D, cond, 1)
        ok = ok and prim == F(2 * class_number(D), units.get(D, 2))
        euler = F(1)
        if cond % 2 == 1:
            euler = 1 - kronecker(D, 2)
        if f % 3 == 0 and cond % 3 != 0:
            euler *= 1 - kronecker(D, 3)
        ok = ok and l_value(D, f, 1) == euler * prim
    ok = ok and [class_number(D) for D in (-3, -4, -7, -8, -11, -15, -20, -23)] == [1, 1, 1, 1, 1, 2, 2, 3]
    # even characters: zeta(-1) L(-1, chi_D) = (1/60) sum over b of sigma((D - b^2)/4), zeta(-1) = -1/12
    for D in (5, 8, 12, 13):
        tot = 0
        b = D % 2
        while b * b < D:
            tot += sigma((D - b * b) // 4) * (1 if b == 0 else 2)
            b += 2
        ok = ok and F(-1, 12) * l_value(D, D, 2) == F(tot, 60)
    ok = ok and [l_value(D, D, 2) for D in (5, 8, 12, 13)] == [F(-2, 5), F(-1), F(-2), F(-2)]
    for D, M in CASES:
        if D < 0:
            continue
        f = 2 * M
        euler = F(1)
        if D % 2 == 1:
            euler = 1 - 2 * kronecker(D, 2)
        if f % 3 == 0 and D % 3 != 0:
            euler *= 1 - 3 * kronecker(D, 3)
        ok = ok and l_value(D, f, 2) == euler * l_value(D, D, 2)
    GA.check("L(0, chi) = 2h/w for eight negative discriminants; L(-1, chi) by the divisor sum for 5, 8, 12, 13", ok)
    return ok


def check_the_two_halves_of_the_stored_array_and_the_character_of_the_quarter_turn():
    premise("synthesis.light-ray-continuum-is-the-twist-integral-of-arrays-and-window-values-are-twist-averages")
    premise("std-algebra.complex-numbers")
    ok = True
    # M = 2: the halves have twists 1/4, 3/4, sea energies B_2 = -1/48 each and asymmetries +1/2, -1/2
    ok = ok and b2(F(1, 4)) == F(-1, 48) and b2(F(3, 4)) == F(-1, 48)
    ok = ok and (1 - 2 * F(1, 4), 1 - 2 * F(3, 4)) == (F(1, 2), F(-1, 2))
    ok = ok and l_value(-4, 4, 1) == F(1, 2) and l_value(-4, 4, 2) == 0
    # the character of conductor 4 is the grade-0 part of the powers of the quarter turn J = e_1 e_2 times -J:
    # chi(a) = <-J J^a>_0 on odd a (1, -1 at a = 1, 3 modulo 4)
    sq = (1, 1)
    J = GA.mul(GA.gen(0), GA.gen(1), sq)
    mJ = GA.neg(J)
    p = GA.sc(F(1))
    vals = []
    for a in range(1, 9):
        p = GA.mul(p, J, sq)
        vals.append(GA.mul(mJ, p, sq).get((), F(0)))
    ok = ok and vals == [1, 0, -1, 0, 1, 0, -1, 0]
    ok = ok and all(vals[a - 1] == (kronecker(-4, a) if a % 2 else 0) for a in range(1, 9))
    GA.check("the halves: B_2 = -1/48, asymmetries +-1/2, sum 1 = 2 L(0, chi_4); chi_4(a) = <-J J^a>_0", ok)
    return ok
