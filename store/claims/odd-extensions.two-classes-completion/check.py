"""odd-extensions.two-classes-completion: exact checks of the two classes of completion.

Model of Theorem odd-extensions.exceptional-algebra-residue-completion-both-sides (iii): ambient
R^(p,q) + H, H hyperbolic with null basis u, v, u.v = 1; the hyperplane family
H_t = span(f_1..f_n, u + t v / 2), tame corank-one wall at t = 0; the Lambda family is (p,q) = (1,3)
with t = -Lambda/3.
(1) Second class (rank one): Q(u + t v/2) = t, so H_t has signature (p+1, q) for t > 0, (p, q+1)
    for t < 0 and corank one at t = 0; its complement in the fixed ambient is the single line
    spanned by u - t v/2 with K = Q = -t (= Lambda/3), signature (0,1) on one side and (1,0) on the
    other, and the totals (p+1, q) + (0, 1) = (p, q+1) + (1, 0) = (p+1, q+1) match the fixed
    ambient on both sides. Samples t = +-3, +-1/2, +-1/7 and Lambda = +-3, +-1/2.
(2) The first class cannot be two-sided: for every constant complement K (all diagonal
    signatures of rank <= 3 and two non-diagonal ones) the signature of H_t + K differs between
    t = 1 and t = -1, det(H_t + K) is linear in t (checked at four t) with a sign change and a
    root at t = 0: a continuous family of such forms degenerates at the wall (conservation).
(3) The first class has rank two: at the wall the fibre is R^(p,q,1); its model completion
    (Fact odd-extensions.imported-minimal-completion-degenerate-algebra-rule, r = 1) adjoins phi with
    rho.phi = 1, phi^2 = 0, so over the nondegenerate part the completion adds the hyperbolic plane
    span(rho, phi) (signature (1,1), 2 = 2r directions), the standard complement off the wall.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(1, 3), (3, 1), (2, 2), (1, 1), (2, 0), (0, 3)]
T_SAMPLES = [F(3), F(-3), F(1, 2), F(-1, 2), F(1, 7), F(-1, 7)]


def _ambient(p, q):
    """Gram of R^(p,q) + H in the basis f_1..f_n, u, v."""
    n = p + q
    G = [[F(0)] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        G[i][i] = F(1 if i < p else -1)
    G[n][n + 1] = G[n + 1][n] = F(1)
    return G


def _bil(G, x, y):
    return sum(x[i] * G[i][j] * y[j] for i in range(len(G)) for j in range(len(G)))


def _hyperplane(p, q, t):
    n = p + q
    vecs = [[F(1) if j == i else F(0) for j in range(n + 2)] for i in range(n)]
    vecs.append([F(0)] * n + [F(1), t / 2])
    return vecs


def _gram_of(G, vecs):
    return [[_bil(G, a, b) for b in vecs] for a in vecs]


def _det(M):
    A = [list(r) for r in M]
    n = len(A)
    det = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return det


def check_second_class_complement_line_changes_type():
    premise("odd-extensions.exceptional-algebra-residue-completion-both-sides")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        G = _ambient(p, q)
        for t in T_SAMPLES + [F(0)]:
            Ht = _hyperplane(p, q, t)
            ok = ok and _bil(G, Ht[-1], Ht[-1]) == t
            sig = GA.congruence_signature(_gram_of(G, Ht))
            if t > 0:
                ok = ok and sig == (p + 1, q, 0)
            elif t < 0:
                ok = ok and sig == (p, q + 1, 0)
            else:
                ok = ok and sig == (p, q, 1)
            comp = [F(0)] * n + [F(1), -t / 2]
            ok = ok and all(_bil(G, comp, h) == 0 for h in Ht)
            K = _bil(G, comp, comp)
            ok = ok and K == -t
            if t != 0:
                kt = (1, 0) if K > 0 else (0, 1)
                tot = (sig[0] + kt[0], sig[1] + kt[1])
                ok = ok and tot == (p + 1, q + 1)
                ok = ok and kt == ((0, 1) if t > 0 else (1, 0))
    # the Lambda family: (1,3), t = -Lambda/3, K = Lambda/3
    G = _ambient(1, 3)
    for lam in (F(3), F(-3), F(1, 2), F(-1, 2)):
        t = -lam / 3
        comp = [F(0)] * 4 + [F(1), -t / 2]
        ok = ok and _bil(G, comp, comp) == lam / 3
        sig = GA.congruence_signature(_gram_of(G, _hyperplane(1, 3, t)))
        ok = ok and sig == ((2, 3, 0) if lam < 0 else (1, 4, 0))
    GA.check("second class: one fixed ambient, a rank-one complement whose type flips at the wall", ok)
    return ok


KS = [[[1]], [[-1]], [[1, 0], [0, 1]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]],
      [[1, 0, 0], [0, 1, 0], [0, 0, -1]], [[1, 0, 0], [0, -1, 0], [0, 0, -1]],
      [[2, 1], [1, -1]], [[0, 1, 0], [1, 0, 0], [0, 0, 3]]]


def check_first_class_cannot_be_two_sided():
    premise("odd-extensions.imported-tame-walls-exceptional-algebra-residue")
    ok = True
    for (p, q) in SIGS:
        G = _ambient(p, q)
        for K in KS:
            k = len(K)
            dets, sigs = {}, {}
            for t in (F(1), F(-1), F(0), F(2)):
                Gh = _gram_of(G, _hyperplane(p, q, t))
                m = len(Gh)
                T = [[F(0)] * (m + k) for _ in range(m + k)]
                for i in range(m):
                    for j in range(m):
                        T[i][j] = Gh[i][j]
                for i in range(k):
                    for j in range(k):
                        T[m + i][m + j] = F(K[i][j])
                dets[t] = _det(T)
                sigs[t] = GA.congruence_signature(T)
            ok = ok and sigs[F(1)] != sigs[F(-1)]
            ok = ok and sigs[F(1)][0] == sigs[F(-1)][0] + 1 and sigs[F(-1)][1] == sigs[F(1)][1] + 1
            ok = ok and dets[F(1)] * dets[F(-1)] < 0 and dets[F(0)] == 0
            ok = ok and dets[F(2)] == 2 * dets[F(1)]               # linear in t through 0
    GA.check("first class: any constant complement leaves a sign change, so the family degenerates", ok)
    return ok


def check_first_class_rank_two():
    premise("odd-extensions.imported-minimal-completion-degenerate-algebra-rule")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        # wall fibre R^(p,q,1) completed by phi: basis f_1..f_n, rho, phi
        G = [[F(0)] * (n + 2) for _ in range(n + 2)]
        for i in range(n):
            G[i][i] = F(1 if i < p else -1)
        G[n][n + 1] = G[n + 1][n] = F(1)
        ok = ok and GA.congruence_signature(G) == (p + 1, q + 1, 0)
        plane = [[G[i][j] for j in (n, n + 1)] for i in (n, n + 1)]
        ok = ok and GA.congruence_signature(plane) == (1, 1, 0)
        # the fibre itself is degenerate of corank one
        fib = [[G[i][j] for j in range(n + 1)] for i in range(n + 1)]
        ok = ok and GA.congruence_signature(fib) == (p, q, 1)
    GA.check("first class: the wall's minimal completion adds a hyperbolic plane (rank two)", ok)
    return ok
