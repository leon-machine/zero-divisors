"""synthesis.additive-weights-on-the-rational-projectors-of-two-modes-are-linear: exact checks.

Two algebras are used.  Cl(2,2) of two modes: e_k (square +1, index 2k), f_k (square -1, index 2k+1); the dagger
sends a blade to its inverse; s_0..s_3 span a minimal left ideal.  Cl(3,0): its even subalgebra holds the rational
rotors x = x_0 + x_1 B_1 + x_2 B_2 + x_3 B_3 with B_1 = e_3 e_2, B_2 = e_1 e_3, B_3 = e_2 e_1 (B_1 B_2 = B_3,
B_k^2 = -1); a ray of Q^4 is a rotor up to scale.  Everything is integer or Fraction arithmetic.
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA
from tp_premise import premise

ONE = GA.sc(F(1))
SQ22 = (1, -1, 1, -1)
SQ3 = (1, 1, 1)

# certificate of clause (ii): sum over the 34 frames of (num/den) * indicator(frame)
#   = indicator((2,1,0,0)) + a combination of the 24 octahedral rays; the coefficients sum to 2/5.
CERT = [
    (3, 10, ((0, 0, 0, 1), (0, 0, 1, 0), (1, -2, 0, 0), (2, 1, 0, 0))),
    (-1, 5, ((1, -2, -3, -1), (1, -2, 2, -1), (1, 0, 0, 1), (1, 1, 0, -1))),
    (-1, 5, ((1, -2, -2, 1), (1, -2, 3, 1), (1, 0, 0, -1), (1, 1, 0, 1))),
    (1, 10, ((0, 0, 0, 1), (0, 1, -1, 0), (1, 1, 1, 0), (2, -1, -1, 0))),
    (1, 10, ((0, 0, 0, 1), (0, 1, 1, 0), (1, 1, -1, 0), (2, -1, 1, 0))),
    (1, 10, ((0, 0, 1, -3), (1, -2, -3, -1), (2, -4, 3, 1), (2, 1, 0, 0))),
    (-1, 10, ((0, 0, 1, -3), (1, -2, 0, 0), (2, 1, -3, -1), (4, 2, 3, 1))),
    (-1, 10, ((0, 0, 1, -3), (1, -2, 0, 0), (2, 1, 3, 1), (4, 2, -3, -1))),
    (1, 10, ((0, 0, 1, -3), (1, -2, 3, 1), (2, -4, -3, -1), (2, 1, 0, 0))),
    (1, 10, ((0, 0, 1, 0), (0, 1, 0, -1), (1, 1, 0, 1), (2, -1, 0, -1))),
    (1, 10, ((0, 0, 1, 0), (0, 1, 0, 1), (1, 1, 0, -1), (2, -1, 0, 1))),
    (-1, 10, ((0, 0, 1, 0), (1, -1, 0, -2), (1, -1, 0, 1), (1, 1, 0, 0))),
    (-1, 10, ((0, 0, 1, 0), (1, -1, 0, -1), (1, -1, 0, 2), (1, 1, 0, 0))),
    (1, 10, ((0, 0, 1, 0), (1, -1, 0, 0), (1, 1, 0, -2), (1, 1, 0, 1))),
    (1, 10, ((0, 0, 1, 0), (1, -1, 0, 0), (1, 1, 0, -1), (1, 1, 0, 2))),
    (1, 10, ((0, 0, 1, 2), (1, -2, -2, 1), (1, -2, 2, -1), (2, 1, 0, 0))),
    (-1, 10, ((0, 0, 1, 2), (1, -2, 0, 0), (2, 1, -2, 1), (2, 1, 2, -1))),
    (1, 10, ((0, 1, 0, -1), (1, -1, 0, -1), (2, 1, -2, 1), (2, 1, 3, 1))),
    (1, 10, ((0, 1, 0, 1), (1, -1, 0, 1), (2, 1, -3, -1), (2, 1, 2, -1))),
    (1, 10, ((1, -2, -4, -3), (1, -2, -1, 3), (1, -2, 2, -1), (2, 1, 0, 0))),
    (-1, 10, ((1, -2, -4, -3), (1, 1, -1, 1), (1, 3, 1, -3), (2, -1, 1, 0))),
    (1, 10, ((1, -2, -3, -1), (1, -2, 1, 2), (1, -2, 3, -4), (2, 1, 0, 0))),
    (1, 10, ((1, -2, -3, 4), (1, -2, -1, -2), (1, -2, 3, 1), (2, 1, 0, 0))),
    (-1, 10, ((1, -2, -3, 4), (1, 1, 1, 1), (1, 3, -3, -1), (2, -1, 0, -1))),
    (1, 10, ((1, -2, -2, 1), (1, -2, 1, -3), (1, -2, 4, 3), (2, 1, 0, 0))),
    (-1, 10, ((1, -2, -1, -2), (1, -2, -1, 3), (1, 0, 1, 0), (1, 1, -1, 0))),
    (-1, 10, ((1, -2, 1, -3), (1, -2, 1, 2), (1, 0, -1, 0), (1, 1, 1, 0))),
    (-1, 10, ((1, -2, 3, -4), (1, 1, -1, -1), (1, 3, 3, 1), (2, -1, 0, 1))),
    (-1, 10, ((1, -2, 4, 3), (1, 1, 1, -1), (1, 3, -1, 3), (2, -1, -1, 0))),
    (1, 10, ((1, -1, -1, 1), (1, -1, 0, -2), (1, 3, -3, -1), (4, 2, 3, 1))),
    (1, 10, ((1, -1, 0, 2), (1, -1, 1, -1), (1, 3, 3, 1), (4, 2, -3, -1))),
    (-1, 10, ((1, 1, -1, 1), (1, 1, 0, -2), (2, -4, -3, -1), (3, -1, 3, 1))),
    (-1, 10, ((1, 1, 0, 2), (1, 1, 1, -1), (2, -4, 3, 1), (3, -1, -3, -1))),
    (1, 10, ((1, 3, -1, 3), (1, 3, 1, -3), (3, -1, -3, -1), (3, -1, 3, 1))),
]
TARGET = (2, 1, 0, 0)
CERT_WEIGHT = F(2, 5)
# bivectors n (as integer triples) for the end-to-end samples of clause (iv)
AXES = [(1, 2, 3), (1, 1, 1), (0, 1, 2), (3, 4, 5), (1, 2, 4), (2, 3, 6), (1, 3, 5), (2, 5, 5), (7, 1, 0), (3, 1, 1)]
# orthogonal triples of bivectors for the half-turn relation of clause (v)
TRIPLES = [((1, 0, 0), (0, 1, 0), (0, 0, 1)), ((0, 0, 1), (1, 1, 0), (1, -1, 0)), ((1, 1, 1), (1, -1, 0), (1, 1, -2)),
           ((0, 1, 2), (0, 2, -1), (1, 0, 0)), ((-2, 0, 1), (1, 1, 2), (1, -5, 2)), ((1, 2, 3), (1, 1, -1), (5, -4, 1))]
UNIT_BOX = 4          # clause (vii): rays with entries up to this bound
FACTOR_BOX = 11       # clause (iii): every integer rotor of norm 25 or 125 with entries up to this bound
POWER_RANGE = 60      # clause (iv): (2 + B_1)^s has both components prime to 5 for s up to this


# ---------------------------------------------------------------- rotors (even subalgebra of Cl(3,0))
def rotor(r):
    b1 = GA.mul(GA.gen(2), GA.gen(1), SQ3)
    b2 = GA.mul(GA.gen(0), GA.gen(2), SQ3)
    b3 = GA.mul(GA.gen(1), GA.gen(0), SQ3)
    return clean(GA.add(GA.sc(F(r[0])), GA.scal(F(r[1]), b1), GA.scal(F(r[2]), b2), GA.scal(F(r[3]), b3)))


def clean(x):
    return {b: c for b, c in x.items() if c != 0}


def coords(x):
    """Components of an even element of Cl(3,0) on 1, B_1, B_2, B_3."""
    return (x.get((), F(0)), -x.get((1, 2), F(0)), x.get((0, 2), F(0)), -x.get((0, 1), F(0)))


def qmul(a, b):
    """The rotor product in components (checked against GA.mul in check_frames_are_cosets...)."""
    a0, a1, a2, a3 = a
    b0, b1, b2, b3 = b
    return (a0 * b0 - a1 * b1 - a2 * b2 - a3 * b3,
            a0 * b1 + a1 * b0 - a2 * b3 + a3 * b2,
            a0 * b2 - a1 * b3 + a2 * b0 + a3 * b1,
            a0 * b3 + a1 * b2 - a2 * b1 + a3 * b0)


def rev(a):
    return (a[0], -a[1], -a[2], -a[3])


def norm(a):
    return sum(c * c for c in a)


def igcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)


def ray(v):
    """Primitive integer representative of the ray of an integer vector, first nonzero entry positive."""
    g = 0
    for c in v:
        g = igcd(g, c)
    v = tuple(c // g for c in v)
    for c in v:
        if c != 0:
            return v if c > 0 else tuple(-t for t in v)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def rot(x):
    """Integer matrix M with x B_b x~ = sum_a M[a][b] B_a; the rotation is M / norm(x)."""
    cols = []
    for b in range(3):
        v = [0, 0, 0, 0]
        v[b + 1] = 1
        y = qmul(qmul(x, tuple(v)), rev(x))
        assert y[0] == 0
        cols.append(y[1:])
    return [[cols[b][a] for b in range(3)] for a in range(3)]


def rotq(x):
    n = norm(x)
    return [[F(c, n) for c in row] for row in rot(x)]


def octahedral():
    rays = set()
    for v in product((-1, 0, 1), repeat=4):
        if norm(v) in (1, 2, 4):
            rays.add(ray(v))
    return sorted(rays)


PRIMES5 = [(2, 1, 0, 0), (2, -1, 0, 0), (2, 0, 1, 0), (2, 0, -1, 0), (2, 0, 0, 1), (2, 0, 0, -1)]


def left_divide(y):
    """y = pi y' with pi one of 2 +- B_k, when 5 divides the norm of the integer rotor y."""
    for pi in PRIMES5:
        z = qmul(rev(pi), y)
        if all(c % 5 == 0 for c in z):
            return pi, tuple(c // 5 for c in z)
    return None


def factor(y):
    """Factor an integer rotor of norm 5^t into the six rotors and a unit; None if it fails."""
    out = []
    while norm(y) > 1:
        if norm(y) % 5 != 0:
            return None
        step = left_divide(y)
        if step is None:
            return None
        out.append(step[0])
        y = step[1]
    return out, y


# ---------------------------------------------------------------- Cl(2,2)
def dsign(b):
    g = len(b)
    s = (-1) ** (g * (g - 1) // 2)
    for i in b:
        s *= SQ22[i]
    return s


def dagger(x):
    return {b: c * dsign(b) for b, c in x.items()}


def prod(*xs):
    r = ONE
    for x in xs:
        r = GA.mul(r, x, SQ22)
    return clean(r)


def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return clean(r)


def s0(x):
    return x.get((), F(0))


def setup22():
    e = [GA.gen(0), GA.gen(2)]
    f = [GA.gen(1), GA.gen(3)]
    p = [prod(f[k], e[k]) for k in range(2)]
    blades = [ONE] + [{tuple(c): F(1)} for r in range(1, 5) for c in combinations(range(4), r)]
    v = [lin((F(1, 2), e[j]), (F(1, 2), f[j])) for j in range(2)]
    w = [lin((F(1, 2), e[j]), (F(-1, 2), f[j])) for j in range(2)]
    p0 = prod(w[0], v[0], w[1], v[1])
    s = [p0, prod(v[0], p0), prod(v[1], p0), prod(v[0], v[1], p0)]
    return e, f, p, blades, p0, s


def matrix_of(x, p0, s):
    """m(x)_ij defined by s_i^dagger x s_j = m_ij P_0."""
    m = [[F(0)] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            y = prod(dagger(s[i]), x, s[j])
            c = 4 * s0(y)
            assert y == clean(GA.scal(c, p0))
            m[i][j] = c
    return m


def mmul(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def quad(rho, r):
    return sum(F(rho[i][j]) * r[i] * r[j] for i in range(4) for j in range(4)) / F(dot(r, r))


def sym_basis():
    out = []
    for i in range(4):
        for j in range(i, 4):
            m = [[0] * 4 for _ in range(4)]
            m[i][j] = 1
            m[j][i] = 1
            out.append(m)
    return out


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def det4(m):
    tot = 0
    for j in range(4):
        minor = [[m[i][k] for k in range(4) if k != j] for i in range(1, 4)]
        tot += (-1) ** j * m[0][j] * det3(minor)
    return tot


# ---------------------------------------------------------------- checks
def check_two_modes_are_the_rational_matrices_of_size_four_and_the_adjoint_is_the_transpose():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    e, f, p, blades, p0, s = setup22()
    for i in range(4):
        for j in range(4):
            assert prod(dagger(s[i]), s[j]) == (p0 if i == j else {})
    assert lin(*[(1, prod(s[i], dagger(s[i]))) for i in range(4)]) == ONE and s0(p0) == F(1, 4)
    mats = [matrix_of(b, p0, s) for b in blades]
    assert GA.mat_rank([[c for row in m for c in row] for m in mats]) == 16
    gens = [GA.gen(i) for i in range(4)]
    gmats = [matrix_of(g, p0, s) for g in gens]
    for g, gm in zip(gens, gmats):
        for b, bm in zip(blades, mats):
            assert matrix_of(prod(g, b), p0, s) == mmul(gm, bm)
    for b, bm in zip(blades, mats):
        assert matrix_of(clean(dagger(b)), p0, s) == [[bm[j][i] for j in range(4)] for i in range(4)]
    for r in [(1, 0, 0, 0), (1, 1, 0, 0), (2, 1, 0, 0), (1, -2, 3, 1), (3, 1, 1, -1)]:
        y = lin(*[(r[i], s[i]) for i in range(4)])
        pi = clean(GA.scal(F(1, dot(r, r)), prod(y, dagger(y))))
        assert prod(pi, pi) == pi and clean(dagger(pi)) == pi
        assert matrix_of(pi, p0, s) == [[F(r[i] * r[j], dot(r, r)) for j in range(4)] for i in range(4)]
    return True


def check_frames_are_cosets_of_the_klein_groups_of_half_turns():
    premise("std-algebra.quaternions")
    samples = [(1, 2, 0, -1), (0, 1, 1, 3), (2, -1, 4, 1), (1, 1, 1, 1), (3, 0, -2, 5)]
    for a in samples:
        for b in samples:
            x = clean(GA.mul(rotor(a), rotor(b), SQ3))
            assert coords(x) == tuple(F(c) for c in qmul(a, b))
            xr = clean(GA.mul(rotor(a), rotor(rev(b)), SQ3))
            assert xr.get((), F(0)) == dot(a, b)
    for num, den, fr in CERT:
        for i in range(4):
            for j in range(i):
                assert dot(fr[i], fr[j]) == 0
        u = [qmul(fr[a], rev(fr[0])) for a in (1, 2, 3)]
        assert all(t[0] == 0 for t in u)
        for a in range(3):
            for b in range(a):
                assert dot(u[a], u[b]) == 0
                assert qmul(u[a], u[b]) == tuple(-c for c in qmul(u[b], u[a]))
        assert ray(qmul(u[0], u[1])) == ray(u[2])
    for tr in TRIPLES:
        assert all(dot(tr[a], tr[b]) == 0 for a in range(3) for b in range(a))
        for x in samples:
            fr = [x] + [qmul((0,) + n, x) for n in tr]
            assert all(dot(fr[i], fr[j]) == 0 for i in range(4) for j in range(i))
    return True


def check_octahedral_rays_span_a_copy_of_the_three_by_three_matrices():
    premise("std-algebra.quaternions")
    octa = octahedral()
    assert len(octa) == 24
    idx = {r: i for i, r in enumerate(octa)}
    for a in octa:
        assert ray(rev(a)) in idx
        for b in octa:
            assert ray(qmul(a, b)) in idx
    turns = [r for r in octa if r[0] == 0]
    assert len(turns) == 9
    kleins = [t for t in combinations(turns, 3) if all(dot(t[a], t[b]) == 0 for a in range(3) for b in range(a))]
    assert len(kleins) == 4
    frames = set()
    for k in kleins:
        for x in octa:
            frames.add(tuple(sorted([idx[x]] + [idx[ray(qmul(n, x))] for n in k])))
    frames = sorted(frames)
    assert len(frames) == 24 and all(len(set(fr)) == 4 for fr in frames)
    rows = [[F(1) if i in fr else F(0) for i in range(24)] for fr in frames]
    assert GA.mat_rank(rows) == 15
    rots = [[c for row in rotq(x) for c in row] for x in octa]
    assert GA.mat_rank(rots) == 9
    # the nine-dimensional space of rotation matrix elements satisfies the 24 relations
    for fr in frames:
        tot = [sum(rots[i][t] for i in fr) for t in range(9)]
        assert tot == [0] * 9
    return True


def check_certificate_puts_the_rotor_two_plus_b1_in_the_octahedral_span():
    premise("std-algebra.quaternions")
    octa = set(octahedral())
    assert len(CERT) == 34
    tot = {}
    wsum = F(0)
    for num, den, fr in CERT:
        assert all(ray(v) == v for v in fr)
        assert all(dot(fr[i], fr[j]) == 0 for i in range(4) for j in range(i))
        q = F(num, den)
        wsum += q
        for v in fr:
            tot[v] = tot.get(v, F(0)) + q
    tot = {v: c for v, c in tot.items() if c != 0}
    assert wsum == CERT_WEIGHT
    assert tot[TARGET] == 1
    rest = {v: c for v, c in tot.items() if v != TARGET}
    assert set(rest) <= octa and len(rest) == 18
    # the identity agrees with the quadratic value on a basis of the ten quadratic forms
    for rho in sym_basis():
        trace = sum(rho[i][i] for i in range(4))
        assert quad(rho, TARGET) == CERT_WEIGHT * trace - sum(c * quad(rho, v) for v, c in rest.items())
    return True


def check_integer_rotors_of_norm_a_power_of_five_factor_into_six_rotors_and_a_unit():
    premise("std-algebra.quaternions")
    count = 0
    for y in product(range(5), repeat=4):
        if norm(y) % 5 == 0:
            count += 1
            assert any(all(c % 5 == 0 for c in qmul(rev(pi), y)) for pi in PRIMES5)
    assert count == 145
    octa = octahedral()
    reached = set()
    for u in octa:
        z = qmul(qmul(u, (2, 1, 0, 0)), rev(u))
        g = norm(u)
        assert all(c % g == 0 for c in z)
        reached.add(tuple(c // g for c in z))
    assert reached == set(PRIMES5)
    seen = {25: 0, 125: 0}
    for y in product(range(-FACTOR_BOX, FACTOR_BOX + 1), repeat=4):
        n = norm(y)
        if n in seen:
            seen[n] += 1
            res = factor(y)
            assert res is not None and norm(res[1]) == 1 and len(res[0]) == (2 if n == 25 else 3)
            z = res[1]
            for pi in reversed(res[0]):
                z = qmul(pi, z)
            assert z == y
    assert seen == {25: 248, 125: 1248}
    return True


def check_conjugate_of_a_power_by_a_half_turn_is_an_integer_rotor_of_norm_a_power_of_five():
    premise("std-algebra.quaternions")
    g = (1, 0, 0, 0)
    for s in range(1, POWER_RANGE + 1):
        g = qmul(g, (2, 1, 0, 0))
        assert g[2] == 0 and g[3] == 0 and g[0] % 5 != 0 and g[1] % 5 != 0
    one = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    for n in AXES:
        big = norm(n)
        prime_to_5 = big
        while prime_to_5 % 5 == 0:
            prime_to_5 //= 5
        gens = []
        for k in (1, 2):
            base = [2, 0, 0, 0]
            base[k] = 1
            base = tuple(base)
            g = base
            s = 1
            while g[k] % prime_to_5 != 0:
                g = qmul(g, base)
                s += 1
            assert g[0] != 0 and g[k] != 0 and norm(g) == 5 ** s
            nq = (0,) + n
            y = qmul(qmul(nq, g), rev(nq))
            cont = 0
            for c in y:
                cont = igcd(cont, c)
            yp = tuple(c // cont for c in y)
            m = norm(yp)
            while m % 5 == 0:
                m //= 5
            assert m == 1
            res = factor(yp)
            assert res is not None and norm(res[1]) == 1
            # the conjugate is the rotation about the reflected bivector by the same angle
            hn = rotq(nq)
            assert mmul(mmul(hn, rotq(g)), hn) == rotq(yp)
            gens.append(rotq(g))
        # the two rotations generate the nine-dimensional matrix algebra
        words = [one, gens[0], gens[1]]
        for _ in range(3):
            words = words + [mmul(a, b) for a in words[:9] for b in (gens[0], gens[1])]
        assert GA.mat_rank([[c for row in w for c in row] for w in words]) == 9
    return True


def check_half_turn_relation_forces_the_central_factor_to_be_one():
    premise("std-algebra.quaternions")
    one = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    for tr in TRIPLES:
        ra, rb = rotq((0,) + tr[0]), rotq((0,) + tr[1])
        rab = mmul(ra, rb)
        assert rab == rotq((0,) + tr[2])
        assert all(one[i][j] + ra[i][j] + rb[i][j] + rab[i][j] == 0 for i in range(3) for j in range(3))
        assert mmul(ra, ra) == one
    grid = [F(k, 2) for k in range(-6, 7)]
    sols = []
    for ca in grid:
        for cb in grid:
            eqs = (1 + ca - cb - ca * cb, 1 - ca + cb - ca * cb, 1 - ca - cb + ca * cb)
            if eqs == (0, 0, 0):
                sols.append((ca, cb))
    assert sols == [(F(1), F(1))]
    return True


def check_linear_functionals_give_the_weights_and_non_negative_weights_are_states():
    premise("synthesis.signed-directions-and-the-integer-clifford-algebra")
    premise("tower.ladder-pairs-satisfy-car-vectors")
    e, f, p, blades, p0, s = setup22()
    rho = [[3, 1, 0, -1], [1, 2, 1, 0], [0, 1, 4, 2], [-1, 0, 2, 5]]
    units = [[prod(s[i], dagger(s[j])) for j in range(4)] for i in range(4)]
    rho_el = lin(*[(F(rho[i][j]), units[i][j]) for i in range(4) for j in range(4)])
    for r in [(1, 0, 0, 0), (1, 1, 0, 0), (2, 1, 0, 0), (1, -2, 3, 1), (3, 1, 1, -1), (0, 2, -1, 5)]:
        y = lin(*[(r[i], s[i]) for i in range(4)])
        pi = clean(GA.scal(F(1, dot(r, r)), prod(y, dagger(y))))
        assert 4 * s0(prod(rho_el, pi)) == quad(rho, r)
    for num, den, fr in CERT:
        assert sum(quad(rho, v) for v in fr) == sum(rho[i][i] for i in range(4))
    for b in blades:
        assert s0(prod(rho_el, clean(dagger(b)))) == s0(prod(rho_el, b))
    # rho is positive definite (leading minors) and then L(x x^dagger) = 4 <rho x x^dagger>_0 >= 0 on samples
    minors = [GA.mat_rank([[F(c) for c in row[:k]] for row in rho[:k]]) for k in range(1, 5)]
    assert minors == [1, 2, 3, 4] and rho[0][0] == 3 and rho[0][0] * rho[1][1] - rho[0][1] ** 2 == 5
    assert det3([row[:3] for row in rho[:3]]) == 17 and det4(rho) == 62
    for x in [lin((1, e[0]), (2, f[1])), lin((1, ONE), (1, prod(e[0], f[1])), (-3, p[1])), lin((2, e[1]), (1, prod(f[0], e[1], f[1])))]:
        assert 4 * s0(prod(rho_el, x, clean(dagger(x)))) > 0
    # the stored functional with value 4: linear, additive on projectors, negative on an atom
    a1, a2, b1, b2 = e[0], p[0], prod(e[1], p[0]), p[1]
    c = lin((1, prod(a1, b1)), (1, prod(a1, b2)), (1, prod(a2, b1)), (-1, prod(a2, b2)))
    box = lin((1, ONE), (1, c))
    lam = [[s0(prod(box, units[i][j])) for j in range(4)] for i in range(4)]
    assert all(lam[i][j] == lam[j][i] for i in range(4) for j in range(4))
    assert sum(lam[i][i] for i in range(4)) == 1
    assert quad(lam, (1, 0, 0, 1)) == F(-1, 4) and quad(lam, (2, 1, -1, 2)) == F(-9, 20)
    y = lin((1, s[0]), (1, s[3]))
    atom = clean(GA.scal(F(1, 2), prod(y, dagger(y))))
    assert prod(atom, atom) == atom and clean(dagger(atom)) == atom and s0(prod(box, atom)) == F(-1, 4)
    return True


def check_atoms_of_rational_unit_vectors_admit_an_additive_weight_that_is_not_linear():
    squares = set(k * k for k in range(1, 2 * UNIT_BOX + 2))
    rays = sorted(set(ray(v) for v in product(range(-UNIT_BOX, UNIT_BOX + 1), repeat=4) if norm(v) in squares))

    def kind(r):
        odd = [i for i in range(4) if r[i] % 2]
        assert len(odd) in (1, 4)
        return odd[0] if len(odd) == 1 else 4

    weight = {0: F(1), 1: F(0), 2: F(0), 3: F(0), 4: F(1, 4)}
    kinds = {r: kind(r) for r in rays}
    assert set(kinds.values()) == {0, 1, 2, 3, 4}
    orth = {r: [t for t in rays if dot(r, t) == 0] for r in rays}
    nframes = 0
    for r in rays:
        for t in orth[r]:
            assert (kinds[r] == 4) == (kinds[t] == 4) and (kinds[r] == 4 or kinds[r] != kinds[t])
            if t <= r:
                continue
            for u in orth[t]:
                if u <= t or dot(u, r) != 0:
                    continue
                for v in orth[u]:
                    if v <= u or dot(v, r) != 0 or dot(v, t) != 0:
                        continue
                    nframes += 1
                    assert sum(weight[kinds[x]] for x in (r, t, u, v)) == 1
    assert nframes > 20
    # not a quadratic form: four rays of kind 0 whose quadratic values would sum to 4/9
    four = [(1, 2, 2, 0), (1, -2, 2, 0), (1, 2, -2, 0), (1, -2, -2, 0)]
    assert all(kinds[ray(v)] == 0 for v in four)
    for rho in sym_basis():
        total = sum(quad(rho, v) for v in four)
        assert total == F(4, 9) * (rho[0][0] + 4 * rho[1][1] + 4 * rho[2][2])
    assert sum(weight[kinds[ray(v)]] for v in four) == 4
    return True
