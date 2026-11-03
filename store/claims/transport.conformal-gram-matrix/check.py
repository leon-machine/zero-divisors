"""transport.conformal-gram-matrix: exact checks.

The points p_0 = 0, p_i = e_i, p_{n+1} = 2 e_1 of an orthogonal basis of V = R^(p,q) and the matrix
M_ij = -Q(p_i - p_j)/2.
(1) For every signature (p,q) with 1 <= n = p + q <= 6, and for orthonormal and non-normalised orthogonal
    bases (Q(e_i) = +-c_i with several rational c_i > 0), M has rank n + 2 and congruence signature
    (p+1, q+1). The entries are formed from Q(p_i - p_j) computed in GA as the square of the vector
    p_i - p_j, not from a closed formula.
(2) The same M is the Gram matrix of the null lifts X(p_i) = n0 + p_i + Q(p_i) ninf/2 in Cl(p+1,q+1)
    (n0 = (e- - e+)/2, ninf = e- + e+), so its rank and signature are those of the span of the lifts;
    checked for every (p,q) with n <= 4.
No premise: the claim has no declared uses (the proof is a direct computation).
"""
from fractions import Fraction as F

import GA

SIGS = [(p, n - p) for n in range(1, 7) for p in range(n + 1)]
SCALES = [None, [F(2), F(1, 3), F(5), F(7, 2), F(3), F(4, 9)]]


def vec(coeffs):
    return {(i,): F(c) for i, c in enumerate(coeffs) if c != 0}


def points(n):
    pts = [[0] * n]
    for i in range(n):
        v = [0] * n
        v[i] = 1
        pts.append(v)
    v = [0] * n
    v[0] = 2
    pts.append(v)
    return pts


def gram_points(p, q, scales):
    """M_ij = -Q(p_i - p_j)/2 with Q the square in GA; scales rescale the basis e_i -> c_i e_i."""
    n = p + q
    S = GA.sig(p, q)
    c = [F(1)] * n if scales is None else scales[:n]
    pts = [[F(x) * c[i] for i, x in enumerate(pt)] for pt in points(n)]
    M = []
    for a in pts:
        row = []
        for b in pts:
            d = vec([x - y for x, y in zip(a, b)])
            sq = GA.mul(d, d, S)
            row.append(F(-1, 2) * sq.get((), F(0)))
        M.append(row)
    return M


def check_rank_and_signature():
    ok = True
    count = 0
    for (p, q) in SIGS:
        n = p + q
        for sc in SCALES:
            M = gram_points(p, q, sc)
            pos, neg, zer = GA.congruence_signature(M)
            ok = ok and GA.mat_rank(M) == n + 2
            ok = ok and (pos, neg, zer) == (p + 1, q + 1, 0)
            count += 1
    _tp_rv = (ok and count == 54); assert _tp_rv is not False, "check_rank_and_signature"; return _tp_rv


def check_gram_of_null_lifts():
    ok = True
    for (p, q) in [s for s in SIGS if s[0] + s[1] <= 4]:
        n = p + q
        S = GA.sig(p, q) + (1, -1)              # e+ at index n, e- at index n + 1
        ep, em = GA.gen(n), GA.gen(n + 1)
        n0 = GA.scal(F(1, 2), GA.sub(em, ep))
        ninf = GA.add(em, ep)
        lifts = []
        for pt in points(n):
            x = vec(pt)
            Qx = GA.mul(x, x, S).get((), F(0))
            X = GA.add(n0, x, GA.scal(Qx / 2, ninf))
            ok = ok and GA.is_zero(GA.mul(X, X, S))         # each lift is null
            lifts.append(X)
        M = gram_points(p, q, None)
        G = [[GA.dot(a, b, S) for b in lifts] for a in lifts]
        ok = ok and all(G[i][j] == M[i][j] for i in range(n + 2) for j in range(n + 2))
        ok = ok and G[0][1] == F(-1, 2) * (S[0]) and G[1][n + 1] == F(-1, 2) * S[0]
    _tp_rv = (ok); assert _tp_rv is not False, "check_gram_of_null_lifts"; return _tp_rv
