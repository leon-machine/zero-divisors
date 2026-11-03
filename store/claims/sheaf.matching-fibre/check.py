"""sheaf.matching-fibre: exact checks of the exceptional fibre, the weight bivector and the ladder boost.

(1) The bivector algebra of the exceptional fibre, Cl(1,3) with eta = diag(1, -1, -1, -1): the map
    x ^ y -> (z -> eta(x, z) y - eta(y, z) x) agrees on all 6 blades and 4 basis vectors with the
    Clifford action z -> (zB - Bz)/2, gives eta-antisymmetric matrices, is injective (rank 6 = dim
    so(1,3)), and turns the Clifford bracket into the matrix commutator:
    [phi(A), phi(B)] = -phi([A, B]/2), with [A, B]/2 again a bivector (closure).
(2) The weight bivector B_w = sum p_i e0 ^ e_i, at the forced exponents (-1/3, 2/3, 2/3) and at three
    rational points p(u) = (-u, 1 + u, u(1 + u))/(1 + u + u^2) of the Kasner circle: sum p_i = sum p_i^2 = 1,
    the action sends e0 -> sum p_i e_i and e_j -> p_j e0, kills the 2-plane of spatial vectors
    orthogonal to p-hat, has characteristic polynomial lambda^4 - lambda^2 (Faddeev-LeVerrier, exact),
    and B_w^2 = sum p_i^2 = 1 in the Clifford algebra: a unit boost. Control: off the circle
    (p = (1/2, 1/2, 1/2)) the polynomial is lambda^4 - (3/4) lambda^2, not a unit boost.
(3) The ladder boost on the ambient fibre Cl(2,4): for a ladder pair k, k* (null, kk* + k*k = 1),
    K = [k, k*]/2 equals the wedge k ^ k* and N - 1/2 with N = k k* idempotent, K^2 = 1/4 as an element
    (hence on all 64 states), [K, k] = k and [K, k*] = -k* (an so(1,1)), and K commutes with the four
    generators orthogonal to the pair.
Not checked: the canonicity of the fibre identification up to Kasner-preserving isometries.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

SQ = GA.sig(1, 3)
ETA = [[F(SQ[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
BLADES2 = list(combinations(range(4), 2))
FORCED = (F(-1, 3), F(2, 3), F(2, 3))
US = (F(2), F(3), F(1, 2))
CONTROL = (F(1, 2), F(1, 2), F(1, 2))


def kasner(u):
    d = 1 + u + u * u
    return (-u / d, (1 + u) / d, u * (1 + u) / d)


def act(B):
    """Matrix of z -> (zB - Bz)/2 on vectors: column j is the image of e_j."""
    cols = []
    for j in range(4):
        z = GA.gen(j)
        img = GA.scal(F(1, 2), GA.sub(GA.mul(z, B, SQ), GA.mul(B, z, SQ)))
        cols.append([img.get((i,), F(0)) for i in range(4)])
    return [[cols[j][i] for j in range(4)] for i in range(4)]


def phi(x, y):
    """Matrix of z -> eta(x, z) y - eta(y, z) x for basis vectors x = e_a, y = e_b."""
    a, b = x, y
    M = [[F(0)] * 4 for _ in range(4)]
    M[b][a] += ETA[a][a]
    M[a][b] -= ETA[b][b]
    return M


def mat_sub(A, B):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(A, B)]


def charpoly(A):
    n = len(A)
    c = [F(0)] * (n + 1)
    c[n] = F(1)
    Mk = [[F(0)] * n for _ in range(n)]
    for k in range(1, n + 1):
        AM = GA.mat_mul(A, Mk)
        Mk = [[AM[i][j] + (c[n - k + 1] if i == j else 0) for j in range(n)] for i in range(n)]
        c[n - k] = -sum((GA.mat_mul(A, Mk)[i][i] for i in range(n)), F(0)) / F(k)
    return c


def check_bivectors_are_so13():
    premise("sheaf.weighted-limit")
    ok = True
    mats = []
    for a, b in BLADES2:
        B = {(a, b): F(1)}
        M = act(B)
        ok = ok and M == phi(a, b)
        EM = GA.mat_mul(ETA, M)
        ok = ok and all(EM[i][j] == -EM[j][i] for i in range(4) for j in range(4))
        mats.append(M)
    ok = ok and GA.rank_of_vectors([[x for r in M for x in r] for M in mats]) == 6
    for (a, b), (c, d) in combinations(BLADES2, 2):
        A, B = {(a, b): F(1)}, {(c, d): F(1)}
        C = GA.scal(F(1, 2), GA.sub(GA.mul(A, B, SQ), GA.mul(B, A, SQ)))
        ok = ok and all(len(bl) == 2 for bl in C)
        lhs = mat_sub(GA.mat_mul(act(A), act(B)), GA.mat_mul(act(B), act(A)))
        ok = ok and lhs == [[-x for x in r] for r in act(C)]
    GA.check("bivectors of Cl(1,3) = eta-antisymmetric endomorphisms (rank 6), bracket matched, closed", ok)
    return ok


def check_weight_bivector_is_unit_boost():
    premise("sheaf.weights-are-forced-are-kasner-exponents")
    premise("sheaf.weighted-limit")
    ok = True
    points = [FORCED] + [kasner(u) for u in US]
    for p in points + [CONTROL]:
        Bw = GA.add(*[GA.scal(p[i], {(0, i + 1): F(1)}) for i in range(3)])
        M = act(Bw)
        s1, s2 = sum(p), sum(x * x for x in p)
        ok = ok and [M[i][0] for i in range(4)] == [0, p[0], p[1], p[2]]
        ok = ok and all(M[0][j] == p[j - 1] and all(M[i][j] == 0 for i in range(1, 4)) for j in range(1, 4))
        ok = ok and charpoly(M) == [0, 0, -s2, 0, 1]
        ok = ok and GA.eq(GA.mul(Bw, Bw, SQ), GA.sc(s2))
        if p is CONTROL:
            ok = ok and s1 == F(3, 2) and s2 == F(3, 4)
        else:
            ok = ok and s1 == 1 and s2 == 1
            perp = GA.field_kernel([[F(0), p[0], p[1], p[2]], [F(1), F(0), F(0), F(0)]])
            ok = ok and len(perp) == 2
            ok = ok and all(all(sum(M[i][j] * v[j] for j in range(4)) == 0 for i in range(4)) for v in perp)
    ok = ok and kasner(F(1)) == (F(-1, 3), F(2, 3), F(2, 3))
    GA.check("B_w = sum p_i e0 ^ e_i: e0 -> p, e_j -> p_j e0, char poly lambda^4 - lambda^2, B_w^2 = 1 on the circle", ok)
    return ok


def check_ladder_boost_on_ambient_fibre():
    ok = True
    sq = GA.sig(2, 4)
    k = GA.scal(F(1, 2), GA.add(GA.gen(0), GA.gen(5)))
    ks = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(5)))
    ok = ok and GA.is_zero(GA.mul(k, k, sq)) and GA.is_zero(GA.mul(ks, ks, sq))
    ok = ok and GA.eq(GA.add(GA.mul(k, ks, sq), GA.mul(ks, k, sq)), GA.sc(1))
    K = GA.scal(F(1, 2), GA.sub(GA.mul(k, ks, sq), GA.mul(ks, k, sq)))
    N = GA.mul(k, ks, sq)
    ok = ok and all(len(b) in (0, 2) for b in K) and K.get((), F(0)) == 0          # K is the wedge k ^ ks
    ok = ok and GA.eq(K, GA.sub(N, GA.sc(F(1, 2)))) and GA.eq(GA.mul(N, N, sq), N)
    ok = ok and GA.eq(GA.mul(K, K, sq), GA.sc(F(1, 4)))
    ok = ok and GA.eq(GA.sub(GA.mul(K, k, sq), GA.mul(k, K, sq)), k)
    ok = ok and GA.eq(GA.sub(GA.mul(K, ks, sq), GA.mul(ks, K, sq)), GA.neg(ks))
    ok = ok and all(GA.commutes(K, GA.gen(i), sq) for i in (1, 2, 3, 4))
    GA.check("ladder boost K = [k, k*]/2 = k ^ k* = N - 1/2, K^2 = 1/4, [K, k] = k, [K, k*] = -k*", ok)
    return ok
