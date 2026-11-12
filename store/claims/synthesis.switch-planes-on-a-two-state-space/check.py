"""synthesis.switch-planes-on-a-two-state-space: exact checks over the rationals.

Planes are spanned by pairs of integer matrices in small boxes; the form on trace-free maps is
Q(x) = x^2 = -det x. Null lines are found exactly (rational square discriminants).
"""
from fractions import Fraction as F
from itertools import combinations, product

import GA


def M(a, b, c, d):
    return ((F(a), F(b)), (F(c), F(d)))


def mm(A, B):
    n = len(A)
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)) for i in range(n))


def ma(A, B):
    return tuple(tuple(x + y for x, y in zip(r, s)) for r, s in zip(A, B))


def ms(c, A):
    return tuple(tuple(F(c) * x for x in r) for r in A)


def flat(A):
    return [x for r in A for x in r]


I2, Z2 = M(1, 0, 0, 1), M(0, 0, 0, 0)
# states: s_off = (1,0)^T, s_on = (0,1)^T
V = M(0, 0, 1, 0)      # set:   off -> on, on -> 0
W = M(0, 1, 0, 0)      # clear: on -> off, off -> 0
VW, WV = mm(V, W), mm(W, V)


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    d = det(A)
    return ms(1 / d, ((A[1][1], -A[0][1]), (-A[1][0], A[0][0])))


def is_scalar(A):
    return A[0][1] == 0 and A[1][0] == 0 and A[0][0] == A[1][1]

import pyutil
from tp_premise import premise


def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def isqrt(n):
    """Integer square root of n >= 0 (Newton's iteration on integers)."""
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def T(a, b, c):
    return M(a, b, c, -a)


def Qf(X):
    return X[0][0] * X[0][0] + X[0][1] * X[1][0]


def Bf(X, Y):
    return (Qf(ma(X, Y)) - Qf(X) - Qf(Y)) / 2


def indep(X, Y):
    return GA.rank_of_vectors([flat(X), flat(Y)]) == 2


def is_square(q):
    q = F(q)
    return q >= 0 and isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator


def gen_dim(X, Y):
    S = [I2, X, Y]
    r = GA.rank_of_vectors([flat(s) for s in S])
    while True:
        new = S + [mm(a, b) for a in S for b in (X, Y)]
        r2 = GA.rank_of_vectors([flat(s) for s in new])
        if r2 == r:
            return r
        S, r = new, r2


def null_lines(X, Y):
    """One null vector per rational null line of Q on span{X, Y}; None if the plane is totally null."""
    a, b, c = Qf(X), 2 * Bf(X, Y), Qf(Y)       # Q(sX + tY) = a s^2 + b st + c t^2
    out = []
    if a == 0:
        out.append(X)
        if b != 0:
            out.append(ma(ms(-c, X), ms(b, Y)))
        elif c == 0:
            return None
        return out
    disc = b * b - 4 * a * c
    if disc == 0:
        out.append(ma(ms(-b, X), ms(2 * a, Y)))
    elif is_square(disc):
        rt = F(isqrt(disc.numerator), isqrt(disc.denominator))
        out.append(ma(ms(-b + rt, X), ms(2 * a, Y)))
        out.append(ma(ms(-b - rt, X), ms(2 * a, Y)))
    return out


def kerline(N):
    k = (N[0][1], -N[0][0]) if (N[0][0], N[0][1]) != (0, 0) else (N[1][1], -N[1][0])
    L = 1
    for x in k:
        L = L * x.denominator // gcd(L, x.denominator)
    k = [int(x * L) for x in k]
    g = gcd(abs(k[0]), abs(k[1]))
    k = [x // g for x in k]
    if k[0] < 0 or (k[0] == 0 and k[1] < 0):
        k = [-x for x in k]
    return tuple(k)


def plane_key(X, Y):
    m = [flat(X), flat(Y)]
    row = 0
    for col in range(4):
        p = next((r for r in range(row, 2) if m[r][col] != 0), None)
        if p is None:
            continue
        m[row], m[p] = m[p], m[row]
        m[row] = [x / m[row][col] for x in m[row]]
        for r in range(2):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [x - f * y for x, y in zip(m[r], m[row])]
        row += 1
    return tuple(tuple(r) for r in m)


def _planes():
    vecs = [T(a, b, c) for a, b, c in product(range(-2, 3), repeat=3) if (a, b, c) != (0, 0, 0)]
    planes = {}
    for X, Y in combinations(vecs, 2):
        if indep(X, Y):
            pyutil.get_or_set(planes, plane_key(X, Y), (X, Y))
    return planes


def check_scalar_square_planes_are_trace_free():
    premise("synthesis.set-and-clear-of-a-bit-generate-the-hyperbolic-plane")
    box = [M(*t) for t in product(range(-1, 2), repeat=4)]
    found = 0
    for X, Y in combinations(box, 2):
        if not indep(X, Y):
            continue
        if all(is_scalar(mm(Z, Z)) for Z in (X, Y, ma(X, Y), ma(X, ms(-1, Y)), ma(X, ms(2, Y)))):
            found += 1
            assert X[0][0] + X[1][1] == 0 and Y[0][0] + Y[1][1] == 0
    assert found == 312     # planes of the box, counted by this search and by the pre-registered run
    return True


def check_form_on_trace_free_maps():
    for a, b, c in product(range(-3, 4), repeat=3):
        x = T(a, b, c)
        assert mm(x, x) == ms(Qf(x), I2) and Qf(x) == -det(x)
    h, ep, em = ma(WV, ms(-1, VW)), ma(V, W), ma(V, ms(-1, W))
    basis = (h, ep, em)
    assert [[Bf(x, y) for y in basis] for x in basis] == [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
    assert GA.rank_of_vectors([flat(x) for x in basis]) == 3
    return True


def check_planes_by_signature_and_nilpotent_lines():
    planes = _planes()
    assert len(planes) == 349
    counts = {0: 0, 1: 0, 2: 0}
    hyperbolic_without_lines = 0
    for X, Y in planes.values():
        sg = GA.congruence_signature([[Bf(X, X), Bf(X, Y)], [Bf(X, Y), Bf(Y, Y)]])
        assert sg in ((2, 0, 0), (1, 1, 0), (1, 0, 1))
        nl = null_lines(X, Y)
        assert nl is not None                                   # no totally null plane
        assert all(mm(N, N) == Z2 and N != Z2 for N in nl)
        counts[len(nl)] += 1
        degenerate = sg[2] > 0
        assert (len(nl) == 1) == degenerate
        if len(nl) == 2:
            assert sg == (1, 1, 0)
        if sg == (1, 1, 0) and len(nl) == 0:
            hyperbolic_without_lines += 1
        assert gen_dim(X, Y) == (3 if degenerate else 4)
    assert counts == {0: 297, 1: 4, 2: 48}
    assert hyperbolic_without_lines == 164     # over Q signature (1,1) is not enough: the square hypothesis of (iii)
    return True


def check_switch_planes_and_pairs_of_states():
    planes = _planes()
    seen = {}
    for key, (X, Y) in planes.items():
        nl = null_lines(X, Y)
        if len(nl) != 2:
            continue
        n1, n2 = nl
        c = ma(mm(n1, n2), mm(n2, n1))
        assert is_scalar(c) and c[0][0] != 0
        a, b = n1, ms(1 / c[0][0], n2)
        assert mm(a, a) == Z2 and mm(b, b) == Z2 and ma(mm(a, b), mm(b, a)) == I2
        k1, k2 = kerline(n1), kerline(n2)
        assert k1 != k2
        g = M(k1[0], k2[0], k1[1], k2[1])
        gi = inv(g)
        c1, c2 = mm(mm(gi, n1), g), mm(mm(gi, n2), g)       # conjugate to a multiple of w and of v
        assert c1[0][0] == c1[1][1] == c1[1][0] == 0 and c1[0][1] != 0
        assert c2[0][0] == c2[1][1] == c2[0][1] == 0 and c2[1][0] != 0
        seen[key] = frozenset([k1, k2])
    assert len(set(seen.values())) == len(seen) == 48             # injective
    lines = sorted({kerline(((F(y), F(-x)), (F(0), F(0)))) for x, y in product(range(-3, 4), repeat=2) if (x, y) != (0, 0)})
    for l0, l1 in combinations(lines, 2):                       # onto
        g = M(l0[0], l1[0], l0[1], l1[1])
        gi = inv(g)
        a, b = mm(mm(g, V), gi), mm(mm(g, W), gi)
        assert mm(a, a) == Z2 and mm(b, b) == Z2 and ma(mm(a, b), mm(b, a)) == I2
        assert frozenset([kerline(a), kerline(b)]) == frozenset([l0, l1])
    return True
