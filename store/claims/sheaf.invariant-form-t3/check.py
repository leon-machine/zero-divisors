"""sheaf.invariant-form-t3: exact checks in a polynomial model.

Coordinates (tau, y) near the wall Sigma = {tau = 0}; covector coordinates on a 2-dimensional fibre. The cometric is
G = P^T D P with P = [[1, 0], [y, 1]] and D = [[lambda, tau b], [tau b, -1 + y tau]], lambda = tau (2 + y) + tau^2,
b = 1 + y: symmetric, polynomial, with G|Sigma of corank exactly one and radical spanned by k = (1, -y) (so
g_k = lambda, hand-derived). Polynomials in (tau, y) are handled exactly.
(1) g_k vanishes on Sigma and d g_k|Sigma annihilates T Sigma: d/dy g_k = 0 at tau = 0, for k and for every
extension below.
(2) Extensions k + tau m~ for five polynomial m~: d/dtau g at tau = 0 is 2 + y for all of them (independent of the
extension).
(3) k -> c k for three nonvanishing c(tau, y): d/dtau g_ck at tau = 0 equals c(0, y)^2 (2 + y).
The bundle map delta(k (x) k) = (2 + y) d tau is nowhere zero exactly off y = -2 (checked on sample points), where
(T3) would fail. Control: adding a non-radical covector field (m~ = (0,1) without the factor tau) changes
d g|Sigma, so the radical condition is what makes delta well defined.
"""
from fractions import Fraction as F
import GA


def P(d):
    return {k: F(v) for k, v in d.items() if v != 0}


def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pmul(a, b):
    out = {}
    for (i, j), u in a.items():
        for (k, l), v in b.items():
            out[(i + k, j + l)] = out.get((i + k, j + l), F(0)) + u * v
    return {k: v for k, v in out.items() if v != 0}


def d_tau(a):
    return {(i - 1, j): i * v for (i, j), v in a.items() if i > 0}


def d_y(a):
    return {(i, j - 1): j * v for (i, j), v in a.items() if j > 0}


def on_sigma(a):
    return {(0, j): v for (i, j), v in a.items() if i == 0}


TAU, Y, ONE = P({(1, 0): 1}), P({(0, 1): 1}), P({(0, 0): 1})
LAM = padd(pmul(TAU, padd(P({(0, 0): 2}), Y)), pmul(TAU, TAU))
BB = padd(ONE, Y)
D = [[LAM, pmul(TAU, BB)], [pmul(TAU, BB), padd(P({(0, 0): -1}), pmul(Y, TAU))]]
PM = [[ONE, {}], [Y, ONE]]


def mat_mul(A, B):
    return [[padd(*[pmul(A[i][t], B[t][j]) for t in range(2)]) for j in range(2)] for i in range(2)]


G = mat_mul(mat_mul([[PM[j][i] for j in range(2)] for i in range(2)], D), PM)
K = [ONE, P({(0, 1): -1})]
EXTENSIONS = [
    [{}, {}],
    [P({(0, 0): 3}), P({(0, 2): 1})],
    [pmul(TAU, Y), P({(1, 1): 5, (0, 0): -2})],
    [P({(0, 3): 1, (2, 0): 7}), P({(0, 0): F(1, 2)})],
    [P({(1, 0): -1}), P({(0, 1): 4, (1, 2): 1})],
]
SCALINGS = [padd(P({(0, 0): 2}), Y, TAU), P({(0, 0): 1, (0, 2): 1, (1, 1): -3}), P({(0, 0): -5})]


def gform(a):
    return padd(*[pmul(pmul(a[i], G[i][j]), a[j]) for i in range(2) for j in range(2)])


def extend(m):
    return [padd(K[i], pmul(TAU, m[i])) for i in range(2)]


def check_radical_and_tangential_vanishing():
    ok = True
    G0 = [[on_sigma(G[i][j]) for j in range(2)] for i in range(2)]
    # G|Sigma k = 0 and G|Sigma has a nonzero entry: corank exactly one with radical k
    ok = ok and all(padd(pmul(G0[i][0], K[0]), pmul(G0[i][1], K[1])) == {} for i in range(2))
    ok = ok and G0[1][1] == {(0, 0): F(-1)}
    for m in EXTENSIONS:
        g = gform(extend(m))
        ok = ok and on_sigma(g) == {} and on_sigma(d_y(g)) == {}
    ok = ok and gform(K) == LAM
    GA.check("g_k vanishes on Sigma and d g_k|Sigma kills T Sigma, for every extension", ok)
    return ok


def check_independent_of_extension():
    ok = True
    want = {(0, 0): F(2), (0, 1): F(1)}               # 2 + y
    vals = [on_sigma(d_tau(gform(extend(m)))) for m in EXTENSIONS]
    ok = ok and all(v == want for v in vals) and len(vals) == 5
    # control: a non-radical perturbation (no factor tau) changes the differential on Sigma
    bad = gform([K[0], padd(K[1], ONE)])
    ok = ok and on_sigma(bad) != {}
    GA.check("d g_k|Sigma = (2 + y) d tau for all five extensions of k", ok)
    return ok


def check_scales_by_c_squared():
    ok = True
    base = {(0, 0): F(2), (0, 1): F(1)}
    for c in SCALINGS:
        ck = [pmul(c, K[i]) for i in range(2)]
        lhs = on_sigma(d_tau(gform(ck)))
        c0 = on_sigma(c)
        ok = ok and lhs == pmul(pmul(c0, c0), base)
    # delta = (2 + y) d tau is nowhere zero except at y = -2
    delta = on_sigma(d_tau(gform(K)))
    zeros = [y for y in (F(-3), F(-2), F(-1), F(0), F(1, 2), F(4))
             if sum(v * y ** j for (_, j), v in delta.items()) == 0]
    ok = ok and zeros == [F(-2)]
    GA.check("k -> c k scales d g_k|Sigma by c^2: delta is a bundle map on L (x) L", ok)
    return ok
