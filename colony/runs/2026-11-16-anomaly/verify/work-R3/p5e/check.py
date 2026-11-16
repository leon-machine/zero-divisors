"""The order-four structure on real projective walls, and the signed count of the sixteen modulo sixteen.

(1) In Cl(p,q), p + q = 2m, the pseudoscalar anticommutes with every vector (it lifts the map -1) and its
    square is (-1)^(m+q). Moving one direction from the positive to the negative side changes the sign of the
    square. In Cl(6,2) the product of the pseudoscalar of six positive directions and that of a negative plane
    is the pseudoscalar, of square +1, and equals, up to sign, the pseudoscalar of Cl(5,1) times that of a
    hyperbolic plane, which anticommutes with the plane's two vectors.
(2) Stiefel-Whitney classes on real projective space with the tautological line, in Z_2[x]/(x^(n+1)):
    w(k gamma) = (1 + x)^k. For p + q = 2m the class w_2(p gamma) + w_2(q gamma) is (m + q) x^2, the exponent of
    (1). w_1(RP^n) = 0 and w_2(RP^n) = x^2 exactly for n = 1 mod 4; w_1 = w_2 = 0 exactly for n = 3 mod 4. On
    the quarter-turn lens spaces, from the stored cell model, x^2 = 6u = 0 and w = (1 + u)^(k+1), so
    L^5(4) is neither spin nor carries the order-four structure; the same route at order two reproduces (2).
(3) The sixteen: every element of the maximal torus of the Standard Model group whose square is 1 on the
    sixteen reverses 0 or 8 states (sixteen sign patterns, one trivial) and fixes the neutral singlet. So the signed count of omega times such
    an element is 0 modulo 16 on sixteen components and one fixed odd class on fifteen, and 16 is the gcd of
    the differences; fifteen-component generations give 0 modulo 16 only in multiples of sixteen. The sums of
    X = 5 - 2N and of its cube vanish on sixteen and are -5, -125 on fifteen (-10 with the full state).
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise


def pseudoscalar(n):
    return {tuple(range(n)): F(1)}


def check_pseudoscalar_lifts_of_the_antipodal_map_square_to_a_sign_set_by_the_signature():
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    ok = True
    table = {}
    for m in (1, 2, 3, 4):
        for q in range(2 * m + 1):
            p = 2 * m - q
            sq = GA.sig(p, q)
            J = pseudoscalar(2 * m)
            J2 = GA.mul(J, J, sq)
            ok = ok and J2 == GA.sc((-1) ** (m + q))
            ok = ok and all(GA.anticommutes(J, GA.gen(i), sq) for i in range(2 * m))
            table[(p, q)] = J2[()]
    ok = ok and [pq for pq, v in sorted(table.items()) if sum(pq) == 6 and v == -1] == [(0, 6), (2, 4), (4, 2), (6, 0)]
    ok = ok and [pq for pq, v in sorted(table.items()) if sum(pq) == 4 and v == -1] == [(1, 3), (3, 1)]
    ok = ok and table[(0, 2)] == -1 and table[(1, 1)] == 1 and table[(2, 0)] == -1
    # the ten Majoranas
    s10 = GA.sig(10, 0)
    w = pseudoscalar(10)
    ok = ok and GA.mul(w, w, s10) == GA.sc(-1) and all(GA.anticommutes(w, GA.gen(i), s10) for i in range(10))
    # Cl(6,2): generators 0..5 positive, 6, 7 negative
    s62 = GA.sig(6, 2)
    J6 = pseudoscalar(6)
    j = {(6, 7): F(1)}
    P = GA.mul(J6, j, s62)
    ok = ok and GA.mul(J6, J6, s62) == GA.sc(-1) and GA.mul(j, j, s62) == GA.sc(-1)
    ok = ok and P == pseudoscalar(8) and GA.mul(P, P, s62) == GA.sc(1) and GA.commutes(J6, j, s62)
    # far side Cl(5,1): directions 0..4 and 6; hyperbolic plane: 5 (positive) and 7 (negative)
    Jfar = {(0, 1, 2, 3, 4, 6): F(1)}
    E = {(5, 7): F(1)}
    ok = ok and GA.mul(Jfar, Jfar, s62) == GA.sc(1) and GA.mul(E, E, s62) == GA.sc(1)
    ok = ok and GA.mul(Jfar, E, s62) == GA.scal(-1, P)
    ok = ok and GA.anticommutes(E, GA.gen(5), s62) and GA.anticommutes(E, GA.gen(7), s62)
    ok = ok and all(GA.commutes(E, GA.gen(i), s62) for i in (0, 1, 2, 3, 4, 6))
    GA.check("pseudoscalar of Cl(p,q), p+q = 2m: lifts -1, square (-1)^(m+q); pair (J, j) is the far side's lift", ok)
    return ok


def power_of_one_plus_x(k, n):
    """(1 + x)^k in Z_2[x]/(x^(n+1)) as a coefficient list."""
    out = [1] + [0] * n
    for _ in range(k):
        out = [(out[i] + (out[i - 1] if i else 0)) % 2 for i in range(n + 1)]
    return out


def check_classes_of_real_projective_and_lens_walls():
    premise("synthesis.imported-whitney-product-formula-and-projective-space")
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    ok = True
    spin, order_four = [], []
    for n in range(1, 14):
        w = power_of_one_plus_x(n + 1, n)
        w1 = w[1]
        w2 = w[2] if n >= 2 else 0
        x2 = 1 if n >= 2 else 0                      # x^2 != 0 exactly for n >= 2
        if w1 == 0 and w2 == 0:
            spin.append(n)
        if w1 == 0 and w2 == x2 and x2 == 1:
            order_four.append(n)
        # with the doubled dying line: w(T + 2 gamma) = (1 + x)^(n + 3)
        w_ext = power_of_one_plus_x(n + 3, n)
        ext2 = w_ext[2] if n >= 2 else 0
        ok = ok and (w_ext[1] == w1) and ((ext2 + w2) % 2 == x2)
    ok = ok and spin == [1, 3, 7, 11] and order_four == [5, 9, 13]
    # sides of signature (p, q) on RP^(2m-1): w_2(p gamma) + w_2(q gamma) = (m + q) x^2
    for m in range(1, 7):
        n = 2 * m - 1
        for q in range(2 * m + 1):
            p = 2 * m - q
            a, b = power_of_one_plus_x(p, max(n, 2)), power_of_one_plus_x(q, max(n, 2))
            ok = ok and (a[2] + b[2]) % 2 == (m + q) % 2
            ok = ok and a[1] == b[1] == p % 2
    # definite physical side (2m, 0) and its far side (2m - 1, 1): exactly one has the class x^2
    ok = ok and [(m % 2, (m + 1) % 2) for m in (2, 3)] == [(0, 1), (1, 0)]
    # quotients of S^(2k+1) by the cyclic group of order d acting by the d-th turn in every plane, from the
    # stored cell model: for two odd cells the diagonal has one term for each pair 0 <= r < j <= d - 1, so
    # x^2 = (number of such pairs) u; and T + R = (k + 1) eta with w(eta) = 1 + u, so w = (1 + u)^(k+1) in
    # Z_2[u]/(u^(k+1)). For d = 4 these are the quarter-turn lens spaces, for d = 2 real projective space.
    def square_of_x(d):
        return len([(r, j) for r in range(d) for j in range(d) if r < j]) % 2

    def w2_coefficient(k):
        poly = [1] + [0] * k                       # powers of u up to u^k
        for _ in range(k):
            poly = [(poly[i] + (poly[i - 1] if i else 0)) % 2 for i in range(k + 1)]
        return poly[1]

    ok = ok and square_of_x(4) == 0 and square_of_x(2) == 1 and square_of_x(8) == 0
    lens = {}
    for k in range(1, 7):
        w2 = w2_coefficient(k)                     # coefficient of u in w_2
        squares = {0, square_of_x(4)}              # a^2 / u for the two classes a = 0, x of H^1
        lens[k] = (w2 == 0, any(w2 == a2 for a2 in squares))
    # (spin, order-four structure with some flat line): L^5(4) (k = 2) has neither
    ok = ok and lens[2] == (False, False) and lens[1] == (True, True) and lens[3] == (True, True)
    ok = ok and [k for k in lens if not lens[k][1]] == [2, 4, 6]
    # control: the same route at d = 2 (u = x^2) reproduces the Whitney classes of projective space
    for k in range(1, 7):
        n = 2 * k + 1
        ok = ok and w2_coefficient(k) == power_of_one_plus_x(n + 1, n)[2]
        ok = ok and ((w2_coefficient(k) == square_of_x(2)) == (n in order_four))
    GA.check("RP^n: w_1 = 0, w_2 = x^2 iff n = 1 mod 4; sides: (m + q) x^2; lens L^5(4): w_2 = u, x^2 = 0", ok)
    return ok


MODES = (1, 2, 3, 4, 5)
PAIR, SLOT = (1, 2, 3), (4, 5)
EVEN = [frozenset(c) for r in (0, 2, 4) for c in combinations(MODES, r)]


def weights(S):
    """(6Y, 2T_3, lambda_3, lambda_8') of an occupation state: integers."""
    j, k = len(S & set(SLOT)), len(S & set(PAIR))
    six_y = 3 * (j - 1) + 3 - 2 * k
    return six_y, (4 in S) - (5 in S), (1 in S) - (2 in S), (2 in S) - (3 in S)


def check_signed_count_of_the_order_four_element_is_defined_modulo_sixteen():
    premise("synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element")
    premise("synthesis.neutral-singlet-bit-decided-by-gauge-algebra-leaving-u5")
    premise("standard-model.imported-anomaly-coefficients")
    ok = len(EVEN) == 16
    ok = ok and sorted(weights(S)[0] for S in EVEN) == [-4, -4, -4, -3, -3, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 6]
    empty = frozenset()
    patterns = set()
    # torus elements exp(2 pi (a 6Y/12 + b 2T_3/4 + c lambda_3/4 + d lambda_8'/4)): all with square 1 on the sixteen
    for a, b, c, d in product(range(12), range(4), range(4), range(4)):
        phase = {S: F(a * weights(S)[0], 12) + F(b * weights(S)[1] + c * weights(S)[2] + d * weights(S)[3], 4)
                 for S in EVEN}
        if all((2 * ph).denominator == 1 for ph in phase.values()):
            patterns.add(tuple(int(2 * phase[S]) % 2 for S in EVEN))
    flipped = sorted(sum(pt) for pt in patterns)
    ok = ok and len(patterns) == 16 and set(flipped) == {0, 8} and flipped.count(0) == 1
    ok = ok and all(pt[EVEN.index(empty)] == 0 for pt in patterns)
    # omega acts by one unit on all sixteen (count -16 in the stored orientation); omega g reverses the flipped states
    counts16 = sorted(-16 + 2 * sum(pt) for pt in patterns)
    counts15 = sorted(-15 + 2 * sum(pt) for pt in patterns)
    ok = ok and set(counts16) == {-16, 0} and set(counts15) == {-15, 1}
    ok = ok and all(c % 16 == 0 for c in counts16) and all(c % 16 == 1 for c in counts15)
    # 16 is the largest modulus for which the count is a function of the class: gcd of the differences
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return abs(a)
    g16 = g15 = 0
    for a in counts16:
        g16 = gcd(g16, a - counts16[0])
    for a in counts15:
        g15 = gcd(g15, a - counts15[0])
    ok = ok and g16 == 16 and g15 == 16
    # the abelian charge X = 5 - 2N of which omega is the quarter turn: the linear and cubic sums of the
    # imported anomaly conditions, on sixteen, on fifteen, and on fifteen with the full state as the singlet
    X = {S: 5 - 2 * len(S) for S in EVEN}
    ok = ok and all(x % 4 == 1 for x in X.values())
    ok = ok and sum(X.values()) == 0 and sum(x ** 3 for x in X.values()) == 0
    fifteen = [X[S] for S in EVEN if S != empty]
    ok = ok and sum(fifteen) == -5 and sum(x ** 3 for x in fifteen) == -125
    swapped = fifteen + [5 - 2 * 5]
    ok = ok and sum(swapped) == -10 and swapped[-1] % 4 == 3
    # generations
    ok = ok and all((16 * g) % 16 == 0 for g in range(1, 40))
    ok = ok and [g for g in range(1, 40) if (-15 * g) % 16 == 0] == [16, 32]
    ok = ok and (-15 * 3) % 16 == 3 and (-16 * 3) % 16 == 0 and (1 * 3) % 16 == 3
    GA.check("sixteen: torus involutions reverse 0 or 8 states, fix the singlet; count 0 mod 16, fifteen: 1 mod 16", ok)
    return ok
