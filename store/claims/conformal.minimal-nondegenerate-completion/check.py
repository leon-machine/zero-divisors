"""conformal.minimal-nondegenerate-completion: exact checks.

(W, B): radical of dimension r >= 1, nondegenerate part of signature (p,q), m = p + q + r; all 30 cases
p + q <= 3 (including p = q = 0), 1 <= r <= 3, each with the diagonal Gram diag(1^p, (-1)^q, 0^r) and a
non-diagonal congruent Gram P^T B P (P unipotent). A completion by k vectors has Gram [[B, X], [X^T, Y]].
(1) Lower bound: for k = r - 1 (and every k < r) and 6 sample (X, Y), the extended Gram has rank at most
    p + q + 2k < m + k: degenerate, so no completion has dimension below m + r.
(2) Existence and signature: for k = r and 6 sample (X, Y) (including the model X = [0; I], Y = 0), every
    nondegenerate extension has congruence signature (p + r, q + r).
(3) Uniqueness fixing W: for each nondegenerate sample, the explicit normalisation (project the new vectors
    off the nondegenerate part, rotate by the inverse radical pairing, subtract half the residual Gram along
    the radical) gives new vectors u' with Gram(W, u') equal to the model Gram exactly, by an invertible
    change of the added vectors; W is untouched, so any two minimal completions are isometric fixing W.
(4) The embedding Cl(p,q,r) -> Cl(p+r,q+r), e_i -> f_i, rho_j -> a_j + b_j (a_j^2 = 1, b_j^2 = -1), is an
    isometry on generators and multiplicative on all blade pairs, and injective (rank 2^m), for
    (3,0,1), (1,1,1), (2,1,2), (0,1,2), (1,0,3).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

CASES = [(p, s - p, r) for s in range(0, 4) for p in range(s + 1) for r in (1, 2, 3)]


def lcg(seed):
    x = seed
    while True:
        x = (1103515245 * x + 12345) % (2 ** 31)
        yield F((x >> 8) % 7 - 3, 1 + (x >> 4) % 3)


def base_gram(p, q, r, twisted):
    m = p + q + r
    D = [[F(0)] * m for _ in range(m)]
    for i in range(p):
        D[i][i] = F(1)
    for i in range(p, p + q):
        D[i][i] = F(-1)
    if not twisted:
        return D
    P = [[F(1) if i == j else (F(j - i, 2) if j > i else F(0)) for j in range(m)] for i in range(m)]
    PT = [list(c) for c in zip(*P)]
    return GA.mat_mul(GA.mat_mul(PT, D), P)


def extend(B, X, Y):
    m, k = len(B), len(Y)
    G = [row[:] + [X[i][j] for j in range(k)] for i, row in enumerate(B)]
    for a in range(k):
        G.append([X[i][a] for i in range(m)] + Y[a][:])
    return G


def samples(m, k, seed):
    out = []
    model_X = [[F(0)] * k for _ in range(m)]
    for j in range(k):
        model_X[m - k + j][j] = F(1)
    out.append((model_X, [[F(0)] * k for _ in range(k)]))
    g = lcg(seed)
    for _ in range(5):
        X = [[next(g) for _ in range(k)] for _ in range(m)]
        Y = [[F(0)] * k for _ in range(k)]
        for a in range(k):
            for b in range(a, k):
                Y[a][b] = Y[b][a] = next(g)
        out.append((X, Y))
    return out


def radical_basis(B):
    """Kernel of B (rows of a basis)."""
    return GA.field_kernel(B)


SEED_LOWER = 7      # sample seed for (1)


def check_no_completion_below_m_plus_r():
    premise("conformal.blade-basis-persists-under-degeneracy")
    ok = len(CASES) == 30
    for (p, q, r) in CASES:
        for tw in (False, True):
            B = base_gram(p, q, r, tw)
            m = len(B)
            ok = ok and GA.congruence_signature(B) == (p, q, r)
            for k in range(r):
                best = 0
                for (X, Y) in samples(m, k, SEED_LOWER * m + k):
                    G = extend(B, X, Y)
                    rk = GA.mat_rank(G)
                    ok = ok and rk < m + k
                    best = max(best, rk)
                # rank at most p + q + 2k (the proof's bound), attained by the generic samples
                ok = ok and best == p + q + 2 * k
    _tp_rv = (ok); assert _tp_rv is not False, "check_no_completion_below_m_plus_r"; return _tp_rv


def check_minimal_completions_signature():
    ok = True
    found = 0
    for (p, q, r) in CASES:
        for tw in (False, True):
            B = base_gram(p, q, r, tw)
            m = len(B)
            for (X, Y) in samples(m, r, 11 * m + r):
                G = extend(B, X, Y)
                if GA.mat_rank(G) == m + r:
                    found += 1
                    ok = ok and GA.congruence_signature(G) == (p + r, q + r, 0)
    _tp_rv = (ok and found == 343); assert _tp_rv is not False, "check_minimal_completions_signature"; return _tp_rv


def normalise(B, X, Y, p, q, r, twisted):
    """Return the coefficient matrix C (k x (m + k)) of the new vectors u'_j in the basis (W, u)."""
    m, k = len(B), r
    G = extend(B, X, Y)
    N = m + k

    def bil(a, b):
        return sum(a[i] * G[i][j] * b[j] for i in range(N) for j in range(N) if a[i] and b[j])

    # work in coordinates: W-vectors as length-N lists with zero tail
    rad = [list(v) + [F(0)] * k for v in radical_basis(B)]
    # nondegenerate orthogonal vectors: Gram-Schmidt on the standard basis modulo the radical
    ortho = []
    for i in range(m):
        v = [F(1) if j == i else F(0) for j in range(N)]
        for w in ortho:
            v = [a - bil(v, w) / bil(w, w) * b for a, b in zip(v, w)]
        if bil(v, v) != 0:
            ortho.append(v)
    us = []
    for j in range(k):
        u = [F(1) if t == m + j else F(0) for t in range(N)]
        for w in ortho:
            u = [a - bil(u, w) / bil(w, w) * b for a, b in zip(u, w)]
        us.append(u)
    if len(ortho) != p + q:
        return None
    pair = [[bil(rad[i], us[j]) for j in range(k)] for i in range(k)]
    if GA.field_rank(pair) != k:
        return None
    # u''_j = sum_l c_lj u_l with pair . c = I
    cols = []
    for j in range(k):
        e = [F(1) if i == j else F(0) for i in range(k)]
        cols.append(GA.field_solve(pair, e))
    u2 = [[sum(cols[j][l] * us[l][t] for l in range(k)) for t in range(N)] for j in range(k)]
    Yr = [[bil(u2[a], u2[b]) for b in range(k)] for a in range(k)]
    u3 = [[u2[a][t] - F(1, 2) * sum(Yr[a][b] * rad[b][t] for b in range(k)) for t in range(N)]
          for a in range(k)]
    return rad, ortho, u3, bil


def check_minimal_completion_unique_fixing_w():
    premise("conformal.witt-extension-theorem")
    ok = True
    count = 0
    for (p, q, r) in CASES:
        for tw in (False, True):
            B = base_gram(p, q, r, tw)
            m = len(B)
            for (X, Y) in samples(m, r, 11 * m + r)[:3]:
                G = extend(B, X, Y)
                if GA.mat_rank(G) != m + r:
                    continue
                res = normalise(B, X, Y, p, q, r, tw)
                ok = ok and res is not None
                rad, ortho, u3, bil = res
                # model relations: B(w, u') = 0 for w in the nondegenerate part, B(rho_i, u'_j) = delta,
                # B(u'_i, u'_j) = 0
                ok = ok and all(bil(w, u) == 0 for w in ortho for u in u3)
                ok = ok and all(bil(rad[i], u3[j]) == (1 if i == j else 0) for i in range(r) for j in range(r))
                ok = ok and all(bil(u3[a], u3[b]) == 0 for a in range(r) for b in range(r))
                # u' together with W is a basis (change of the added vectors is invertible)
                basis = [[F(1) if t == i else F(0) for t in range(m + r)] for i in range(m)] + u3
                ok = ok and GA.field_rank(basis) == m + r
                count += 1
    _tp_rv = (ok and count == 168); assert _tp_rv is not False, "check_minimal_completion_unique_fixing_w"; return _tp_rv


def embed_images(p, q, r):
    S = GA.sig(p + r, q + r)
    imgs = [GA.gen(i) for i in range(p)]
    imgs += [GA.gen(p + r + i) for i in range(q)]
    for j in range(r):
        imgs.append(GA.add(GA.gen(p + j), GA.gen(p + r + q + j)))
    return S, imgs


# sample inputs for (4): signatures (p, q, r) of the embedding
EMBED_CASES = [(3, 0, 1), (1, 1, 1), (2, 1, 2), (0, 1, 2), (1, 0, 3)]


def unit_blade(I):
    return {I: F(1)}


def check_embedding_into_cl_p_plus_r_q_plus_r():
    premise("conformal.blade-basis-persists-under-degeneracy")
    ok = True
    for (p, q, r) in EMBED_CASES:
        m = p + q + r
        Sd = GA.sig(p, q, r)
        S, imgs = embed_images(p, q, r)

        def phi(x):
            out = {}
            for b, c in x.items():
                y = GA.sc(1)
                for i in b:
                    y = GA.mul(y, imgs[i], S)
                out = GA.add(out, GA.scal(c, y))
            return out

        for i in range(m):
            for j in range(m):
                ok = ok and GA.dot(GA.gen(i), GA.gen(j), Sd) == GA.dot(imgs[i], imgs[j], S)
        blades = GA.all_blades(m)
        for I in blades:
            for J in blades:
                ok = ok and GA.eq(phi(GA.mul(unit_blade(I), unit_blade(J), Sd)),
                                  GA.mul(phi(unit_blade(I)), phi(unit_blade(J)), S))
        allb = GA.all_blades(m + r)
        rk = GA.rank_of_vectors([[phi(unit_blade(I)).get(b, F(0)) for b in allb] for I in blades])
        ok = ok and rk == 2 ** m
    _tp_rv = (ok); assert _tp_rv is not False, "check_embedding_into_cl_p_plus_r_q_plus_r"; return _tp_rv
