"""synthesis.additive-weights-on-the-rational-projectors-of-two-or-more-modes-are-linear: exact checks.

Three algebras are used.  Cl(3,3) of three modes: e_j (square +1, index 2j), f_j (square -1, index 2j+1); the
dagger sends a blade to its inverse; the eight elements s_S span a minimal left ideal.  Cl(3,0): its even
subalgebra holds the rational rotors x = x_0 + x_1 B_1 + x_2 B_2 + x_3 B_3 with B_1 = e_3 e_2, B_2 = e_1 e_3,
B_3 = e_2 e_1.  Cl(5,0): the reflection in a vector m is x -> -m x m^-1.  Everything is integer or Fraction
arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
SQ3 = (1, 1, 1)
SAMPLES = [(1, 1, 1, 1, 1), (1, 2, 3, 4, 5), (1, 1, 1, 1, 1, 1, 1, 1), (3, -1, 2, 5, 1, 1, -2, 7),
           (1, 2, 3, 4, 5, 6), (2, 1, 1, 1, 1, 1, 3)]


# ---------------------------------------------------------------- small exact helpers
def dot(a, b):
    return sum(F(x) * F(y) for x, y in zip(a, b))


def rank(rows):
    return GA.mat_rank([list(r) for r in rows])


def in_span(rows, target):
    return rank(list(rows) + [list(target)]) == rank(rows)


def prod(sq, *xs):
    out = ONE
    for x in xs:
        out = GA.mul(out, x, sq)
    return out


def dagger(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b)
        s = F(-1) ** (g * (g - 1) // 2)
        for k in b:
            s *= sq[k]
        out[b] = s * c
    return out


# ---------------------------------------------------------------- rotors (even subalgebra of Cl(3,0))
def rotor(r):
    b1 = GA.mul(GA.gen(1), GA.gen(2), SQ3)
    b2 = GA.mul(GA.gen(0), GA.gen(2), SQ3)
    b3 = GA.mul(GA.gen(1), GA.gen(0), SQ3)
    return GA.add(GA.sc(F(r[0])), GA.scal(F(r[1]), b1), GA.scal(F(r[2]), b2), GA.scal(F(r[3]), b3))


def coords(x):
    return (x.get((), F(0)), -x.get((1, 2), F(0)), x.get((0, 2), F(0)), -x.get((0, 1), F(0)))


def rmul(r, s):
    return coords(GA.mul(rotor(r), rotor(s), SQ3))


def rrev(r):
    return (F(r[0]), -F(r[1]), -F(r[2]), -F(r[3]))


def rinv(r):
    n = dot(r, r)
    return tuple(c / n for c in rrev(r))


def prime_factors(n):
    out = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def rotor_of_prime(p, memo):
    """A rational rotor of norm p, by the induction of clause (ii)."""
    if p in memo:
        return memo[p]
    if p == 2:
        memo[p] = (F(1), F(1), F(0), F(0))
        return memo[p]
    h = (p - 1) // 2
    squares = {(a * a) % p: a for a in range(h + 1)}
    assert len(squares) == h + 1                      # the squares of 0..h are distinct modulo p
    b = next(b for b in range(h + 1) if (-1 - b * b) % p in squares)
    a = squares[(-1 - b * b) % p]
    m = (a * a + b * b + 1) // p
    assert m * p == a * a + b * b + 1 and 1 <= m < p
    q = rmul((a, b, 1, 0), rinv(rotor_of_integer(m, memo)))
    assert dot(q, q) == p
    memo[p] = q
    return q


def rotor_of_integer(n, memo):
    q = (F(1), F(0), F(0), F(0))
    for p in prime_factors(n):
        q = rmul(q, rotor_of_prime(p, memo))
    return q


def rotor_of_rational(x, memo):
    x = F(x)
    q = rotor_of_integer(x.numerator * x.denominator, memo)
    return tuple(c / x.denominator for c in q)


# ---------------------------------------------------------------- the reflection of clause (iii)
def reflect(m, x):
    c = 2 * dot(m, x) / dot(m, m)
    return tuple(F(xi) - c * F(mi) for xi, mi in zip(x, m))


def standard_four_space_through(r, memo):
    """s in the first four coordinates with s.s = r.r, and the images of e_0..e_3 under the reflection in r - s."""
    n = len(r)
    s = tuple(rotor_of_rational(dot(r, r), memo)) + (F(0),) * (n - 4)
    m = tuple(F(a) - b for a, b in zip(r, s))
    basis = []
    for i in range(4):
        e = tuple(F(1) if j == i else F(0) for j in range(n))
        basis.append(reflect(m, e) if any(m) else e)
    return s, m, basis


def quad_eval(c):
    """The ten monomials c_a c_b: the evaluation at c as a functional on the quadratic forms of a four-space."""
    return [c[a] * c[b] for a in range(4) for b in range(a, 4)]


def hyperplane_data(r, memo):
    n = len(r)
    s, m, w = standard_four_space_through(r, memo)
    forms = [tuple(w[i][k] for i in range(4)) for k in range(n)]      # x_k restricted to W, in the basis w
    classes = []
    for f in forms:
        if not any(rank([f, g]) == 1 for g in classes):
            classes.append(f)
    evs = []
    for f in classes:
        ker = [tuple(F(x) for x in v) for v in GA.field_kernel([list(f)])]
        vecs = ker + [tuple(a + b for a, b in zip(ker[i], ker[j])) for i, j in combinations(range(len(ker)), 2)]
        evs.append([quad_eval(c) for c in vecs])
    return s, w, forms, classes, evs


# ---------------------------------------------------------------- checks
def check_three_modes_are_the_rational_matrices_of_size_eight_and_even_elements_are_two_blocks():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    modes = 3
    sq = tuple([1, -1] * modes)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(modes)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * j), GA.gen(2 * j + 1))) for j in range(modes)]
    for j in range(modes):
        assert GA.eq(dagger(v[j], sq), w[j]) and GA.is_zero(prod(sq, v[j], v[j]))
        assert GA.eq(GA.add(prod(sq, v[j], w[j]), prod(sq, w[j], v[j])), ONE)
    p0 = ONE
    for j in range(modes):
        p0 = prod(sq, p0, w[j], v[j])
    assert p0[()] == F(1, 8) and GA.eq(dagger(p0, sq), p0) and GA.eq(prod(sq, p0, p0), p0)
    subsets = [s for k in range(modes + 1) for s in combinations(range(modes), k)]
    s = [prod(sq, *([v[j] for j in sub] + [p0])) for sub in subsets]
    size = len(s)
    assert size == 8
    sd = [dagger(x, sq) for x in s]
    for i in range(size):
        for j in range(size):
            assert GA.eq(prod(sq, sd[i], s[j]), p0 if i == j else {})
    assert GA.eq(GA.add(*[prod(sq, s[i], sd[i]) for i in range(size)]), ONE)

    def matrix_of(x):
        out = []
        for i in range(size):
            xi = prod(sq, sd[i], x)
            row = []
            for j in range(size):
                z = prod(sq, xi, s[j])
                c = z.get((), F(0)) / p0[()]
                assert GA.eq(z, GA.scal(c, p0))
                row.append(c)
            out.append(row)
        return out

    blades = GA.all_blades(2 * modes)
    mats = {b: matrix_of({b: F(1)}) for b in blades}
    assert rank([[c for row in mats[b] for c in row] for b in blades]) == 64
    for g in range(2 * modes):
        for b in blades[:16]:
            assert matrix_of(prod(sq, GA.gen(g), {b: F(1)})) == GA.mat_mul(mats[(g,)], mats[b])
    for b in blades:
        assert matrix_of(dagger({b: F(1)}, sq)) == [list(col) for col in zip(*mats[b])]
    parity = [len(sub) % 2 for sub in subsets]
    for b in blades:
        for i in range(size):
            for j in range(size):
                if (parity[i] + parity[j] + len(b)) % 2 == 1:
                    assert mats[b][i][j] == 0
    even = [[c for row in mats[b] for c in row] for b in blades if len(b) % 2 == 0]
    assert len(even) == 32 and rank(even) == 32 and parity.count(0) == 4 and parity.count(1) == 4
    return True


def check_every_positive_rational_is_the_norm_of_a_rational_rotor():
    premise("std-algebra.quaternions")
    memo = {}
    x, y = (1, 2, 3, 4), (5, -1, 0, 2)
    z = rmul(x, y)
    assert z == (-1, 15, 7, 25) and dot(z, z) == dot(x, x) * dot(y, y) == 900
    assert rmul(x, rinv(x)) == (1, 0, 0, 0) and dot(rinv(x), rinv(x)) == F(1, 30)
    assert rmul((1, 1, 0, 0), rrev((1, 1, 0, 0))) == (2, 0, 0, 0)
    total = 0
    for k in range(293):
        q = rotor_of_integer(k + 1, memo)
        assert dot(q, q) == k + 1 and rmul(q, rrev(q)) == (k + 1, 0, 0, 0)
        total += k + 1
    assert total == 43071 and len(memo) == 62 and max(memo) == 293
    assert memo[7] == (F(5, 2), F(-1, 2), F(1, 2), F(1, 2)) and memo[23] == (F(11, 3), F(-2), F(-7, 3), F(-1, 3))
    q = rotor_of_rational(F(15, 28), memo)
    assert dot(q, q) == F(15, 28) and q == (F(-11, 28), F(3, 28), F(-11, 28), F(13, 28))
    return True


def check_one_reflection_puts_a_vector_in_a_four_space_isometric_to_the_standard_one():
    premise("std-algebra.quaternions")
    memo = {}
    for r in SAMPLES:
        n = len(r)
        s, m, w = standard_four_space_through(r, memo)
        assert dot(s, s) == dot(r, r) and all(c == 0 for c in s[4:])
        assert reflect(m, s) == tuple(F(c) for c in r)
        assert all(dot(w[i], w[j]) == (1 if i == j else 0) for i in range(4) for j in range(4))
        cr = [dot(r, w[i]) for i in range(4)]
        assert tuple(sum(cr[i] * w[i][k] for i in range(4)) for k in range(n)) == tuple(F(c) for c in r)
        # W lies in the span of e_0..e_3 and r
        gens = [tuple(F(1) if j == i else F(0) for j in range(n)) for i in range(4)] + [tuple(F(c) for c in r)]
        assert rank(gens) == 5 and all(in_span(gens, x) for x in w)
    # the reflection is x -> -m x m^-1 in the algebra of Q^5 with Q(x) = x.x
    sq5 = (1, 1, 1, 1, 1)
    r = SAMPLES[1]
    s, m, w = standard_four_space_through(r, memo)
    mv = GA.add(*[GA.scal(m[k], GA.gen(k)) for k in range(5)])
    minv = GA.scal(1 / dot(m, m), mv)
    assert GA.eq(prod(sq5, mv, minv), ONE)
    for i in range(4):
        image = GA.neg(prod(sq5, mv, GA.gen(i), minv))
        assert GA.eq(image, GA.add(*[GA.scal(w[i][k], GA.gen(k)) for k in range(5)]))
    return True


def check_quadratic_form_on_the_four_space_is_fixed_by_vectors_of_smaller_support():
    premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")
    premise("std-algebra.quaternions")
    memo = {}
    for r in SAMPLES:
        n = len(r)
        s, w, forms, classes, evs = hyperplane_data(r, memo)
        assert all(any(f) for f in forms) and rank(forms) == 4 and len(classes) >= 4
        cr = [dot(r, w[i]) for i in range(4)]
        # every vector used lies in W and has a zero coordinate where r has none
        for f, block in zip(classes, evs):
            assert len(block) == 6 and rank(block) == 6
        three = [e for block in evs[:3] for e in block]
        two = [e for block in evs[:2] for e in block]
        assert rank(three) == 10 and in_span(three, quad_eval(cr))
        assert rank(two) == 9 and not in_span(two, quad_eval(cr))
    return True


def check_two_vectors_embed_only_if_their_determinant_is_a_sum_of_three_squares():
    premise("std-algebra.quaternions")
    for x, y in [((1, 2, 3, 4), (0, 1, -1, 5)), ((2, 0, 1, 1), (3, 1, 4, 1)), ((1, 0, 0, 0), (0, 1, 1, 1)),
                 ((3, -2, 5, 1), (1, 1, 1, 7))]:
        z = rmul(y, rrev(x))
        assert z[0] == dot(x, y)
        assert dot(x, x) * dot(y, y) - dot(x, y) ** 2 == z[1] ** 2 + z[2] ** 2 + z[3] ** 2
    u = (1, 0, 0, 0, 0, 0, 0, 0)
    v = (0, 1, 1, 1, 2, 0, 0, 0)
    assert dot(u, u) * dot(v, v) - dot(u, v) ** 2 == 7
    residues = {(a * a + b * b + c * c) % 8 for a in range(8) for b in range(8) for c in range(8)}
    assert residues == {0, 1, 2, 3, 4, 5, 6}
    assert all((7 * m * m) % 8 == 7 for m in range(1, 8, 2))
    assert all(a % 2 == 0 and b % 2 == 0 and c % 2 == 0
               for a in range(4) for b in range(4) for c in range(4) if (a * a + b * b + c * c) % 4 == 0)
    bound = 24
    squares = {k * k for k in range(3 * bound)}
    for m in range(1, bound):
        t = 7 * m * m
        assert not any(t - a * a - b * b in squares for a in range(3 * bound) for b in range(a + 1) if a * a + b * b <= t)
    # for comparison: 6 = 1 + 1 + 4 is a sum of three squares, and e_0 with (0,1,1,2) lies in the standard four-space
    assert 6 == 1 + 1 + 4 and dot((0, 1, 1, 2), (0, 1, 1, 2)) == 6
    return True


def check_linear_functionals_give_additive_weights_and_fifteen_values_recover_them():
    premise("synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear")
    n = 5
    rho = [[F((i + 1) * (j + 1) + (3 if i == j else 0), 7) - (F(3) if (i, j) in ((0, 4), (4, 0)) else 0)
            for j in range(n)] for i in range(n)]
    assert all(rho[i][j] == rho[j][i] for i in range(n) for j in range(n))

    def big_f(r):
        return sum(rho[i][j] * r[i] * r[j] for i in range(n) for j in range(n))

    def f(r):
        return big_f(r) / dot(r, r)

    def orthogonalise(vectors):
        out = []
        for x in vectors:
            y = tuple(F(c) for c in x)
            for z in out:
                k = dot(y, z) / dot(z, z)
                y = tuple(a - k * b for a, b in zip(y, z))
            assert any(y)
            out.append(y)
        return out

    trace = sum(rho[i][i] for i in range(n))
    assert trace == 10
    frame = orthogonalise([(1, 1, 1, 1, 1), (1, 2, 0, 0, 0), (0, 1, 3, 0, 0), (0, 0, 1, -1, 0), (0, 0, 0, 1, 4)])
    assert all(dot(frame[i], frame[j]) == 0 for i, j in combinations(range(n), 2))
    values = [f(r) for r in frame]
    assert values == [F(198, 35), F(223, 140), F(-3, 28), F(-5, 7), F(25, 7)] and sum(values) == trace
    unit = [tuple(F(1) if k == i else F(0) for k in range(n)) for i in range(n)]
    assert sum(f(r) for r in unit) == trace
    # the reconstruction of clause (v): rho from the values at e_i and e_i + e_j
    for i in range(n):
        assert big_f(unit[i]) == rho[i][i]
        for j in range(i + 1, n):
            pair = tuple(a + b for a, b in zip(unit[i], unit[j]))
            assert (big_f(pair) - big_f(unit[i]) - big_f(unit[j])) / 2 == rho[i][j]
    # sign: this rho is negative on one ray, so the functional is additive and is not a state
    assert f((2, 0, 0, 0, 1)) == F(-4, 7) and f((1, 0, 0, 0, -1)) == F(32, 7)
    return True
