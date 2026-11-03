"""transport.minimality: exact checks.

(1) The hyperbolic-plane completion works in every signature: in Cl(p+1, q+1) with
    n0 = (e- - e+)/2, ninf = e- + e+ (n0^2 = ninf^2 = 0, n0.ninf = -1) the lift
    X(x) = f(x) + x, f(x) = n0 + Q(x)/2 ninf, is null for sample x of 14 signatures (definite,
    mixed, and n = 0), Q_W(f(x)) = -Q(x) is computed, f(0) = n0 is a nonzero null vector of W,
    and the signature of V + W is (p+1, q+1) by congruence diagonalisation: increment (+1, +1).
(2) A nondegenerate W containing a nonzero null vector is indefinite: for sample Gram matrices
    (dimensions 2 to 4, non-diagonal) with a rational null vector v, a partner w with v.w = 1 is
    solved for, normalised to a null w', and v + w', v - w' have squares +2 and -2; the computed
    signatures have both entries >= 1, so increments (+k, 0) and (0, +k) cannot occur.
(3) A two-dimensional nondegenerate W containing a null vector is the hyperbolic plane: for
    sample 2 x 2 Grams the signature is (1, 1) and an explicit basis change gives the Gram
    [[0, 1], [1, 0]], so the minimal W is unique up to isometry.
(4) The second route for mixed V: -Q takes both signs on V, hence so does Q_W o f.
No premises: the proof uses classical quadratic-space facts and the definition.
EXPORTS["conformal"](p, q) returns the conformal model used here (signature tuple, e+, e-,
n0, ninf, the lift X, the form Q, and iota(N) = e+ N e+), for reuse by dependent checks.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise  # noqa: F401  (no store premises)


def conformal(p, q):
    n = p + q
    sq = GA.sig(p, q) + (1, -1)
    ep, em = GA.gen(n), GA.gen(n + 1)
    n0 = GA.scal(F(1, 2), GA.sub(em, ep))
    ninf = GA.add(em, ep)

    def vec(coeffs):
        return {(i,): F(c) for i, c in enumerate(coeffs) if c != 0}

    def Q(x):
        return GA.mul(x, x, sq).get((), F(0))

    def X(x):
        return GA.add(n0, x, GA.scal(Q(x) / 2, ninf))

    def iota(N):
        return GA.mul(GA.mul(ep, N, sq), ep, sq)

    def coords(N):
        """(s, x, t) with N = s n0 + x + t ninf."""
        s = -GA.dot(N, ninf, sq)
        t = -GA.dot(N, n0, sq)
        x = {b: c for b, c in N.items() if b[0] < n}
        return s, x, t

    return {"n": n, "sq": sq, "ep": ep, "em": em, "n0": n0, "ninf": ninf, "vec": vec,
            "Q": Q, "X": X, "iota": iota, "coords": coords}


EXPORTS = {"conformal": conformal}

SIGS = [(0, 0), (1, 0), (0, 1), (2, 0), (0, 2), (1, 1), (3, 0), (0, 3), (2, 1), (1, 2),
        (1, 3), (3, 1), (2, 2), (2, 3)]
SAMPLE_COEFFS = [[F(1), F(2), F(-1), F(3), F(1, 2)], [F(2), F(-1, 3), F(1), F(0), F(5)],
                 [F(1), F(1), F(1), F(1), F(1)], [F(0), F(0), F(0), F(0), F(0)]]

# nondegenerate Grams with a rational null vector v (dimension 2 to 4), non-diagonal
NULL_GRAMS = [
    ([[0, 1], [1, 0]], [1, 0]),
    ([[1, 2], [2, 3]], [1 - 2, 1]),            # Q(-1, 1) = 1 - 4 + 3 = 0
    ([[2, 1], [1, -4]], [1, 1]),
    ([[1, 0, 0], [0, 1, 0], [0, 0, -1]], [1, 0, 1]),
    ([[3, 1, 0], [1, -1, 2], [0, 2, 1]], [-1, 1, 0]),
    ([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]], [5, 3, 4, 0]),
    ([[2, 1, 0, 0], [1, 0, 1, 0], [0, 1, -1, 1], [0, 0, 1, 3]], [0, 1, 0, 0]),
]
MIXED_SIGS = [(1, 1), (1, 3), (3, 1), (2, 2), (2, 1)]
TWO_DIM = [[[0, 1], [1, 0]], [[1, 2], [2, 3]], [[1, 0], [0, -1]], [[4, 3], [3, 2]],
           [[0, 5], [5, 7]], [[-2, 1], [1, 4]], [[1, 0], [0, 1]], [[2, 1], [1, 3]]]


def _qf(G, v):
    n = len(G)
    return sum(F(G[i][j]) * v[i] * v[j] for i in range(n) for j in range(n))


def _bf(G, v, w):
    n = len(G)
    return sum(F(G[i][j]) * v[i] * w[j] for i in range(n) for j in range(n))


def _null_vectors_2d(G):
    """Rational null vectors of a 2 x 2 Gram: roots of a + 2 b t + c t^2 with a rational sqrt."""
    a, b, c = F(G[0][0]), F(G[0][1]), F(G[1][1])
    if a == 0:
        return [F(1), F(0)]
    disc = b * b - a * c
    num, den = disc.numerator, disc.denominator
    rn, rd = _isqrt(num), _isqrt(den)
    if disc < 0 or rn * rn != num or rd * rd != den:
        return None
    r = F(rn, rd)
    # a x^2 + 2 b x y + c y^2 = 0 at y = 1: x = (-b + r) / a
    return [(-b + r) / a, F(1)]


def _isqrt(m):
    if m < 0:
        return -1
    x = 0
    while (x + 1) * (x + 1) <= m:
        x += 1
    return x


def _partner(G, v):
    """Solve for w with v.w = 1 (G v has a nonzero entry by nondegeneracy), then make it null."""
    n = len(G)
    Gv = [sum(F(G[i][j]) * v[j] for j in range(n)) for i in range(n)]
    k = next(i for i in range(n) if Gv[i] != 0)
    w = [F(0)] * n
    w[k] = 1 / Gv[k]
    qw = _qf(G, w)
    return [w[i] - qw / 2 * v[i] for i in range(n)]


def check_hyperbolic_plane_completion_in_every_signature():
    ok = True
    count = 0
    for (p, q) in SIGS:
        M = conformal(p, q)
        n, sq = M["n"], M["sq"]
        ok = ok and GA.is_zero(GA.mul(M["n0"], M["n0"], sq))
        ok = ok and GA.is_zero(GA.mul(M["ninf"], M["ninf"], sq))
        ok = ok and GA.dot(M["n0"], M["ninf"], sq) == -1
        for cs in SAMPLE_COEFFS:
            x = M["vec"](cs[:n])
            f = GA.add(M["n0"], GA.scal(M["Q"](x) / 2, M["ninf"]))
            Xx = GA.add(f, x)
            ok = ok and GA.is_zero(GA.mul(Xx, Xx, sq))           # X(x) null
            ok = ok and GA.dot(f, f, sq) + M["Q"](x) == 0        # Q_W(f(x)) = -Q(x)
            ok = ok and all(GA.dot(f, GA.gen(i), sq) == 0 for i in range(n))   # W orthogonal to V
            count += 1
        # f(0) = n0 is nonzero and null
        f0 = GA.sub(M["X"]({}), {})
        ok = ok and f0 == M["n0"] and not GA.is_zero(f0)
        # signature of V + W from its Gram matrix: increment (+1, +1)
        basis = [GA.gen(i) for i in range(n + 2)]
        G = [[GA.dot(a, b, sq) for b in basis] for a in basis]
        ok = ok and GA.congruence_signature(G) == (p + 1, q + 1, 0)
    ok = ok and count == 56
    GA.check("hyperbolic-plane completion: X(x) null, Q_W(f(x)) = -Q(x), f(0) = n0, increment (+1,+1), 14 signatures", ok)
    return ok


def check_null_vector_forces_both_signs():
    ok = True
    seen = 0
    for G, v0 in NULL_GRAMS:
        v = [F(c) for c in v0]
        ok = ok and any(c != 0 for c in v) and _qf(G, v) == 0
        w = _partner(G, v)
        ok = ok and _qf(G, w) == 0 and _bf(G, v, w) == 1
        plus = [a + b for a, b in zip(v, w)]
        minus = [a - b for a, b in zip(v, w)]
        ok = ok and _qf(G, plus) == 2 and _qf(G, minus) == -2
        P, N, Z = GA.congruence_signature(G)
        ok = ok and Z == 0 and P >= 1 and N >= 1
        seen += 1
    ok = ok and seen == 7
    # a definite W of any dimension k has signature (k, 0) or (0, k): no null vector
    for k in range(1, 6):
        for s in (1, -1):
            G = [[F(s) * (2 if i == j else (1 if abs(i - j) == 1 else 0)) for j in range(k)]
                 for i in range(k)]
            sg = GA.congruence_signature(G)
            ok = ok and sg == ((k, 0, 0) if s == 1 else (0, k, 0))
    GA.check("a nondegenerate W with a null vector has directions of both signs; definite W excluded", ok)
    return ok


def check_two_dimensional_w_is_hyperbolic_plane():
    ok = True
    found = 0
    for G in TWO_DIM:
        v = _null_vectors_2d(G)
        if v is None:
            continue
        found += 1
        ok = ok and GA.congruence_signature(G) == (1, 1, 0)
        w = _partner(G, v)
        Gram = [[_bf(G, a, b) for b in (v, w)] for a in (v, w)]
        ok = ok and Gram == [[0, 1], [1, 0]]
        # the basis change is invertible
        ok = ok and v[0] * w[1] - v[1] * w[0] != 0
    # [[1,0],[0,-1]] has null vector (1,1); [[1,2],[2,3]] has (-1,1); [[4,3],[3,2]] disc 1;
    # [[-2,1],[1,4]] disc 9; [[0,1],[1,0]] and [[0,5],[5,7]] start null: six qualify, and the
    # two definite controls [[1,0],[0,1]], [[2,1],[1,3]] have no null vector
    ok = ok and found == 6
    GA.check("every two-dimensional admissible W is the hyperbolic plane, unique up to isometry", ok)
    return ok


def check_mixed_signature_second_route():
    ok = True
    for (p, q) in MIXED_SIGS:
        M = conformal(p, q)
        n, sq = M["n"], M["sq"]
        xp = M["vec"]([1] + [0] * (n - 1))             # Q = +1
        xm = M["vec"]([0] * p + [2] + [0] * (q - 1))   # Q = -4
        for x, expect in ((xp, -1), (xm, 4)):
            f = GA.add(M["n0"], GA.scal(M["Q"](x) / 2, M["ninf"]))
            ok = ok and GA.dot(f, f, sq) == expect
    GA.check("mixed V: Q_W o f takes both signs (-1 and +4 at the samples)", ok)
    return ok
