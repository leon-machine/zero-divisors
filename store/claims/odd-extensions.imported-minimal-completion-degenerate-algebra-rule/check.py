"""odd-extensions.imported-minimal-completion-degenerate-algebra-rule: exact checks.

V = R^(p,q,r): Gram diag(+1^p, -1^q, 0^r), radical spanned by rho_1..rho_r. An extension by k new
vectors has Gram [[G_V, X], [X^T, Y]] (X, Y sample rational blocks from a fixed generator).
(1) Lower bound: every extension by k = r - 1 vectors is degenerate (the r radical rows lie in a
    space of dimension r - 1); for the samples the rank is exactly p + q + 2r - 2. All (p, q, r)
    with p + q <= 3, 1 <= r <= 3.
(2) Minimal completions: every nondegenerate extension by k = r vectors has signature
    (p + r, q + r); the model (rho_j . phi_k = delta_jk, phi . phi = 0, phi orthogonal to the
    nondegenerate part) is nondegenerate with that signature.
(3) Uniqueness fixing V pointwise: from any sample nondegenerate extension the vectors
    phi = P^{-1}(w - projection onto N) - S rho / 2 are computed and have exactly the model Gram,
    so the extension is isometric to the model by a map fixing V.
(4) Type N in a nondegenerate algebra: the forced increment is (+1, +1) (the hyperbolic-plane
    completion exported by the transport.minimality check: lift null, signature (p+1, q+1)).
(5) Type C: Cl(p+1, q) and Cl(p, q+1) are isomorphic for p - q = 1 mod 4, n <= 5 (nu -> omega nu
    satisfies the relations; the images span), while the signs differ: the algebra forgets the sign.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

CASES = [(p, s - p, r) for s in range(0, 4) for p in range(s + 1) for r in range(1, 4)]
TYPE_N_SIGS = [(1, 1), (1, 3), (3, 1), (2, 2), (2, 1)]    # sample nondegenerate signatures (p, q) for type N
_SEED = [7]


def _rnd():
    _SEED[0] = (_SEED[0] * 1103515245 + 12345) % 2147483648
    return F(_SEED[0] % 11 - 5)


SAMPLES = {}
for _c in CASES:
    _p, _q, _r = _c
    _m = _p + _q + _r
    for _k in (_r - 1, _r):
        SAMPLES[(_c, _k)] = [([[_rnd() for _ in range(_k)] for _ in range(_m)],
                              [[_rnd() for _ in range(_k)] for _ in range(_k)]) for _t in range(3)]


def _gram(p, q, r, X, Y):
    m = p + q + r
    k = len(Y)
    G = [[F(0)] * (m + k) for _ in range(m + k)]
    for i in range(p + q):
        G[i][i] = F(1 if i < p else -1)
    for i in range(m):
        for j in range(k):
            G[i][m + j] = G[m + j][i] = X[i][j]
    for i in range(k):
        for j in range(k):
            G[m + i][m + j] = (Y[i][j] + Y[j][i]) / 2
    return G


def _bil(G, u, v):
    return sum(u[i] * G[i][j] * v[j] for i in range(len(G)) for j in range(len(G)) if u[i] and v[j])


def _inverse(P):
    n = len(P)
    A = [list(P[i]) + [F(1) if j == i else F(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        piv = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[piv] = A[piv], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def check_lower_bound_dimension():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    for (p, q, r) in CASES:
        m = p + q + r
        for X, Y in SAMPLES[((p, q, r), r - 1)]:
            G = _gram(p, q, r, X, Y)
            ok = ok and GA.mat_rank(G) == p + q + 2 * r - 2
    GA.check("every extension by r - 1 vectors is degenerate (rank p + q + 2r - 2), 30 radical cases", ok)
    return ok


def check_minimal_completions_signature():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    nondeg = 0
    for (p, q, r) in CASES:
        m = p + q + r
        for X, Y in SAMPLES[((p, q, r), r)]:
            G = _gram(p, q, r, X, Y)
            P, N, Z = GA.congruence_signature(G)
            if Z == 0:
                nondeg += 1
                ok = ok and (P, N) == (p + r, q + r)
        # the model: X pairs rho_j with phi_j, Y = 0
        X = [[F(1) if (i >= p + q and i - p - q == j) else F(0) for j in range(r)] for i in range(m)]
        Y = [[F(0)] * r for _ in range(r)]
        ok = ok and GA.congruence_signature(_gram(p, q, r, X, Y)) == (p + r, q + r, 0)
    ok = ok and nondeg == 87                 # of the 90 samples, 87 are nondegenerate
    GA.check("nondegenerate extensions by r vectors have signature (p+r, q+r); the model too", ok)
    return ok


def check_minimal_completion_unique_fixing_v():
    premise("conformal.minimal-nondegenerate-completion")
    ok = True
    done = 0
    for (p, q, r) in CASES:
        m = p + q + r
        for X, Y in SAMPLES[((p, q, r), r)]:
            G = _gram(p, q, r, X, Y)
            if GA.congruence_signature(G)[2] != 0:
                continue
            tot = m + r
            e = [[F(1) if j == i else F(0) for j in range(tot)] for i in range(tot)]
            rho = e[p + q:m]
            # w' = w - sum_i (w . e_i)/e_i^2 e_i over the nondegenerate part
            wp = []
            for j in range(r):
                w = list(e[m + j])
                for i in range(p + q):
                    c = _bil(G, e[m + j], e[i]) / G[i][i]
                    w = [a - c * b for a, b in zip(w, e[i])]
                wp.append(w)
            Pm = [[_bil(G, wp[j], rho[k]) for k in range(r)] for j in range(r)]
            Pi = _inverse(Pm)
            w2 = [[sum(Pi[j][l] * wp[l][t] for l in range(r)) for t in range(tot)] for j in range(r)]
            S = [[_bil(G, w2[j], w2[k]) for k in range(r)] for j in range(r)]
            phi = [[w2[j][t] - sum(S[j][k] * rho[k][t] for k in range(r)) / 2 for t in range(tot)]
                   for j in range(r)]
            basis = e[:m] + phi
            gram = [[_bil(G, u, v) for v in basis] for u in basis]
            model = [[F(0)] * tot for _ in range(tot)]
            for i in range(p + q):
                model[i][i] = F(1 if i < p else -1)
            for j in range(r):
                model[p + q + j][m + j] = model[m + j][p + q + j] = F(1)
            ok = ok and gram == model and GA.mat_rank(basis) == tot
            done += 1
    ok = ok and done == 87
    GA.check("each sample minimal completion is isometric to the model by a map fixing V", ok)
    return ok


def check_type_n_increment_forced():
    ex = premise("transport.minimality")
    conformal = ex["conformal"]
    ok = True
    for (p, q) in TYPE_N_SIGS:
        M = conformal(p, q)
        n, sq = M["n"], M["sq"]
        v = M["vec"]([int(i in (0, p)) for i in range(n)])     # a type-N null vector e_0 + e_p
        Xv = M["X"](v)
        ok = ok and GA.is_zero(GA.mul(v, v, sq)) and GA.is_zero(GA.mul(Xv, Xv, sq))
        basis = [GA.gen(i) for i in range(n + 2)]
        G = [[GA.dot(a, b, sq) for b in basis] for a in basis]
        ok = ok and GA.congruence_signature(G) == (p + 1, q + 1, 0)
    GA.check("type N: the hyperbolic-plane completion, increment (+1,+1)", ok)
    return ok


def check_type_c_sign_forgotten():
    premise("transport.one-generator-minimal-minimal-completions-classified")
    ok = True
    for (p, q) in [(1, 0), (2, 1), (0, 3), (3, 2), (1, 4), (5, 0)]:
        n = p + q
        sqm = GA.sig(p, q) + (-1,)
        om = {tuple(range(n)): F(1)}
        images = [GA.gen(i) for i in range(n)] + [GA.mul(om, GA.gen(n), sqm)]
        target = GA.sig(p, q) + (1,)
        for i in range(n + 1):
            ok = ok and GA.eq(GA.mul(images[i], images[i], sqm), GA.sc(target[i]))
            for j in range(i + 1, n + 1):
                ok = ok and GA.anticommutes(images[i], images[j], sqm)
        prods = []
        for b in GA.all_blades(n + 1):
            x = GA.sc(1)
            for i in b:
                x = GA.mul(x, images[i], sqm)
            prods.append(GA.basis_vector_of(x, GA.all_blades(n + 1)))
        ok = ok and GA.rank_of_vectors(prods) == 2 ** (n + 1)
        ok = ok and target.count(1) == p + 1 and sqm.count(1) == p
    GA.check("type C: Cl(p+1,q) = Cl(p,q+1) as algebras, n <= 5; the adjoined sign is not detected", ok)
    return ok
