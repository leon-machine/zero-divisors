"""tower.witt-index-quantum-capacity: exact checks.

Real quadratic spaces R^(p,q) (diagonal, nondegenerate) and their Clifford algebras in GA.py.
(1) Attained: for every (p,q) with n = p+q <= 7, the Witt decomposition pairs e_i (square +1) with
    f_i (square -1), i < min(p,q); a_i = (e_i + f_i)/2, b_i = (e_i - f_i)/2 is a mode family (all CAR
    as vector identities), the a_i are independent and span a totally isotropic subspace W, and the
    pairing matrix <a_i, b_j> is delta_ij/2 (which forces independence of any mode family).
(2) Not exceeded: W is maximal. The form restricted to the orthogonal complement W^perp has
    signature (|p-q|, 0, m) or (0, |p-q|, m), m = min(p,q): W^perp / W is definite, so no isotropic
    vector of W^perp lies outside W. (All maximal isotropic subspaces have one dimension by Witt's
    theorem, the classical input of the proof.) Independently, without Witt's theorem: for every
    (p,q) with n <= 4, an exhaustive search over the isotropic vectors with coefficients in {-1,0,1}
    finds totally isotropic subspaces of dimension min(p,q) and none larger.
(3) The tower: T_k = Cl(p+k, q+k) has Witt index min(p,q) + k: the construction and the maximality
    test of (1)-(2) for every ground with n <= 3 and k <= 2, so each rung adds exactly one mode.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(1, 8) for p in range(n + 1)]
SMALL = [(p, n - p) for n in range(1, 5) for p in range(n + 1)]


def squares(p, q):
    return GA.sig(p, q)


def witt_family(p, q):
    m = min(p, q)
    a = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(p + i))) for i in range(m)]
    b = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(p + i))) for i in range(m)]
    return a, b


def vec(x, n):
    return [x.get((i,), F(0)) for i in range(n)]


def gram_on(vectors, S):
    n = len(S)
    return [[sum(S[i] * u[i] * w[i] for i in range(n)) for w in vectors] for u in vectors]


def perp_signature(W, S):
    """Signature of the form restricted to the orthogonal complement of span(W)."""
    n = len(S)
    rows = [[S[i] * w[i] for i in range(n)] for w in W]
    basis = GA.field_kernel([[F(x) for x in r] for r in rows]) if rows else \
        [[F(1) if i == j else F(0) for i in range(n)] for j in range(n)]
    return GA.congruence_signature(gram_on(basis, S)), len(basis)


def max_isotropic_lattice(p, q):
    S = squares(p, q)
    n = p + q
    vs = []

    def rec(prefix):
        if len(prefix) == n:
            if any(prefix) and sum(S[i] * prefix[i] ** 2 for i in range(n)) == 0:
                first = next(x for x in prefix if x)
                if first > 0:
                    vs.append(tuple(F(x) for x in prefix))
            return
        for c in (-1, 0, 1):
            rec(prefix + [c])
    rec([])

    def orth(u, w):
        return sum(S[i] * u[i] * w[i] for i in range(n)) == 0
    best = [0]

    def grow(chosen, cands):
        r = GA.rank_of_vectors([list(c) for c in chosen]) if chosen else 0
        best[0] = max(best[0], r)
        for idx, c in enumerate(cands):
            new = chosen + [c]
            if GA.rank_of_vectors([list(x) for x in new]) > r:
                grow(new, [d for d in cands[idx + 1:] if orth(c, d)])
    grow([], vs)
    return best[0]


def check_mode_family_attains_witt_index():
    premise("tower.ladder-pairs-satisfy-car-vectors")
    for p, q in SIGS:
        S, n, m = squares(p, q), p + q, min(p, q)
        a, b = witt_family(p, q)
        assert len(a) == m
        for i in range(m):
            for j in range(m):
                assert GA.is_zero(GA.add(GA.mul(a[i], a[j], S), GA.mul(a[j], a[i], S)))
                assert GA.is_zero(GA.add(GA.mul(b[i], b[j], S), GA.mul(b[j], b[i], S)))
                assert GA.eq(GA.add(GA.mul(a[i], b[j], S), GA.mul(b[j], a[i], S)),
                             GA.sc(1) if i == j else {})
                assert GA.dot(a[i], b[j], S) == (F(1, 2) if i == j else 0)
        assert GA.rank_of_vectors([vec(x, n) for x in a]) == m
    return True


def check_witt_subspace_is_maximal():
    for p, q in SIGS:
        S, n, m = squares(p, q), p + q, min(p, q)
        a, _ = witt_family(p, q)
        (pos, neg, zer), dim = perp_signature([vec(x, n) for x in a], S)
        assert dim == n - m and zer == m
        assert (pos, neg) == ((p - q, 0) if p >= q else (0, q - p))
    for p, q in SMALL:
        assert max_isotropic_lattice(p, q) == min(p, q), (p, q)
    return True


def check_each_rung_adds_one_mode():
    for n in range(4):
        for p in range(n + 1):
            q = n - p
            for k in range(3):
                P, Q = p + k, q + k
                S = squares(P, Q)
                a, _ = witt_family(P, Q)
                assert len(a) == min(p, q) + k
                (pos, neg, zer), _ = perp_signature([vec(x, P + Q) for x in a], S)
                assert zer == min(p, q) + k and pos * neg == 0
                assert pos + neg == abs(p - q)
    return True
