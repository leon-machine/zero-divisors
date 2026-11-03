"""conformal.principal-case: exact checks.

V = R^(n,0,1) (Gram diag(1, ..., 1, 0), radical rho), the space of the n-dimensional Euclidean PGA
Cl(n,0,1), for n = 1..6 (n = 2: the plane, n = 3: PGA).
(1) No completion of dimension n + 1 (the radical row of the Gram matrix is zero), and every
    one-vector extension, Gram [[I_n, 0, a], [0, 0, c], [a^T, c, d]], has determinant -c^2 (checked
    at sample (a, c, d) against the hand value): it is nondegenerate exactly when c != 0, and then
    its signature is (n+1, 1), the signature of CGA Cl(n+1, 1); for n = 3 that is Cl(4,1), for
    n = 2 Cl(3,1).
(2) Uniqueness fixing V: phi = (w - sum a_i e_i)/c - (d - |a|^2)/(2c^2) rho has phi.rho = 1,
    phi.phi = 0, phi orthogonal to the e_i, so every minimal completion is isometric to the model
    by a map fixing V pointwise.
(3) The embedding Cl(n,0,1) -> Cl(n+1, 1) in GA: with e+ (square +1), e- (square -1) of the
    completion, rho = e+ + e- is null, anticommutes with the e_i, and the images of
    e_1..e_n, rho satisfy the relations of Cl(n,0,1) and are linearly independent products
    (rank 2^(n+1)), so the subalgebra they generate is a copy of Cl(n,0,1).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

EXT = [([1, -2, 3, 0, 1, 2], 1, 0), ([0, 0, 0, 0, 0, 0], 2, 5), ([F(1, 2), 1, -1, 2, 0, 3], -3, F(7, 4)),
       ([2, 2, 2, 2, 2, 2], F(1, 3), -1)]


def _gram(n, a, c, d):
    m = n + 2
    G = [[F(0)] * m for _ in range(m)]
    for i in range(n):
        G[i][i] = F(1)
        G[i][m - 1] = G[m - 1][i] = F(a[i])
    G[n][m - 1] = G[m - 1][n] = F(c)
    G[m - 1][m - 1] = F(d)
    return G


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


def _bil(G, u, v):
    return sum(u[i] * G[i][j] * v[j] for i in range(len(G)) for j in range(len(G)))


def check_minimal_completion_is_cga():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    for n in range(1, 7):
        V = [[F(1) if (i == j and i < n) else F(0) for j in range(n + 1)] for i in range(n + 1)]
        ok = ok and GA.mat_rank(V) == n                       # radical of dimension one
        for a, c, d in EXT:
            G = _gram(n, a[:n], c, d)
            ok = ok and _det(G) == -F(c) ** 2
            ok = ok and GA.congruence_signature(G) == (n + 1, 1, 0)
        G0 = _gram(n, EXT[0][0][:n], 0, 3)                     # c = 0: still degenerate
        ok = ok and GA.congruence_signature(G0)[2] >= 1
    sig_pga3 = GA.congruence_signature(_gram(3, [0, 0, 0], 1, 0))
    sig_pga2 = GA.congruence_signature(_gram(2, [0, 0], 1, 0))
    ok = ok and sig_pga3 == (4, 1, 0) and sig_pga2 == (3, 1, 0)
    GA.check("every nondegenerate one-vector completion of R^(n,0,1) has signature (n+1,1); PGA -> Cl(4,1)", ok)
    return ok


def check_completion_unique_fixing_v():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    for n in range(1, 7):
        for a, c, d in EXT:
            a = [F(x) for x in a[:n]]
            c, d = F(c), F(d)
            G = _gram(n, a, c, d)
            m = n + 2
            e = [[F(1) if j == i else F(0) for j in range(m)] for i in range(m)]
            w, rho = e[n + 1], e[n]
            aa = sum(x * x for x in a)
            phi = [(w[t] - sum(a[i] * e[i][t] for i in range(n))) / c - (d - aa) / (2 * c * c) * rho[t]
                   for t in range(m)]
            ok = ok and _bil(G, phi, rho) == 1 and _bil(G, phi, phi) == 0
            ok = ok and all(_bil(G, phi, e[i]) == 0 for i in range(n))
    GA.check("phi with phi.rho = 1, phi^2 = 0, phi orthogonal to the e_i: the completion is the model", ok)
    return ok


def check_pga_embeds_in_cga():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    for n in range(1, 5):
        sq = GA.sig(n + 1, 1)                  # e_0..e_{n-1}, e+ = e_n, e- = e_{n+1}
        rho = GA.add(GA.gen(n), GA.gen(n + 1))
        imgs = [GA.gen(i) for i in range(n)] + [rho]
        target = (1,) * n + (0,)
        for i in range(n + 1):
            ok = ok and GA.eq(GA.mul(imgs[i], imgs[i], sq), GA.sc(target[i]))
            for j in range(i + 1, n + 1):
                ok = ok and GA.anticommutes(imgs[i], imgs[j], sq)
        prods = []
        for b in GA.all_blades(n + 1):
            x = GA.sc(1)
            for i in b:
                x = GA.mul(x, imgs[i], sq)
            prods.append(GA.basis_vector_of(x, GA.all_blades(n + 2)))
        ok = ok and GA.rank_of_vectors(prods) == 2 ** (n + 1)
    GA.check("Cl(n,0,1) embeds in Cl(n+1,1) with rho = e+ + e- (relations and rank 2^(n+1)), n <= 4", ok)
    return ok
