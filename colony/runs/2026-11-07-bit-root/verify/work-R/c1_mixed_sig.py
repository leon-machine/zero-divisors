"""synthesis.completion-recovers-the-real-clifford-algebras: exact checks.

Quadratic spaces are given by rational Gram matrices G (B(x, y) = x^T G y); their Clifford algebra is
realised exactly by GA.ext_c on the exterior algebra (faithful for every Gram matrix, degenerate
included), so "u w = -w u" is checked as an operator identity on all 2^n basis states.
(1) The square-root step of a complete ordered field: the two inequalities that rule out s^2 < a and
    s^2 > a for the least upper bound s, at rational instances, with hand values for a = 2.
(2) Orthogonal bases by rejection x -> x - B(x, u) u^{-1}: for nondiagonal and degenerate Gram
    matrices the rejected vectors anticommute pairwise in the Clifford algebra and square to the
    stated values; with G = A^T D A (A unitriangular, D = diag of +-squares and 0) the values are
    exactly D, and dividing by the square roots gives squares 1, -1, 0.
(3) Inertia: the counts (p, q, r) of the orthogonal bases obtained from many orderings and changes of
    basis agree with each other, with r = n - rank G, and with hand-stated signatures.
(4) The base change and the degenerate embedding: the blade products of Cl(p,q,r) have structure
    constants in {0, 1, -1} (so Cl(p,q,r) is a rational algebra extended by scalars), and r null vectors
    e'_k + f'_k of r added hyperbolic planes realise Cl(p,q,r) inside Cl(p+r,q+r), injectively.
(5) Square classes over Q: x xbar = a^2 - 2 b^2 for e^2 = 2 and a^2 - 2b^2 - 3c^2 + 6d^2 for the plane
    with squares 2, 3 (computed with GA); the descent lemmas modulo 4 and modulo 9 that show they
    have no nontrivial rational zero; Cl(1,0) and Cl(2,0) have zero divisors over Q.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product

import GA
from tp_premise import premise


# ---- the exterior model of Cl(V, G) ----------------------------------------------------------

def states(n):
    return [frozenset(S) for k in range(n + 1) for S in combinations(range(n), k)]


def act(vecs, G, st):
    """c(v_1) c(v_2) ... c(v_k) applied to the state st (rightmost first)."""
    for v in reversed(vecs):
        st = GA.ext_c(v, G, st)
    return st


def anticommutator_is_scalar(u, w, G, val):
    n = len(G)
    for S in states(n):
        st = {S: F(1)}
        lhs = GA.add(act([u, w], G, st), act([w, u], G, st))
        if not GA.ext_state_eq(lhs, {S: 2 * val}) and not (val == 0 and lhs == {}):
            return False
    return True


def bil(x, y, G):
    n = len(G)
    return sum(F(x[i]) * F(G[i][j]) * F(y[j]) for i in range(n) for j in range(n))


def orthogonalise(basis, G):
    """Orthogonal basis by repeated rejection; a pair with zero squares and B != 0 is replaced by
    its sum first (Q(x + y) = 2B(x, y))."""
    rest = [list(map(F, b)) for b in basis]
    out = []
    while rest:
        k = next((i for i, x in enumerate(rest) if bil(x, x, G) != 0), None)
        if k is None:
            pair = next(((i, j) for i in range(len(rest)) for j in range(len(rest))
                         if i != j and bil(rest[i], rest[j], G) != 0), None)
            if pair is None:
                out.extend(rest)
                break
            i, j = pair
            rest[i] = [a + b for a, b in zip(rest[i], rest[j])]
            continue
        u = rest.pop(k)
        Qu = bil(u, u, G)
        rest = [[a - bil(x, u, G) / Qu * b for a, b in zip(x, u)] for x in rest]
        out.append(u)
    return out


def counts(G, basis):
    us = orthogonalise(basis, G)
    vals = [bil(u, u, G) for u in us]
    return (sum(1 for v in vals if v > 0), sum(1 for v in vals if v < 0),
            sum(1 for v in vals if v == 0)), us, vals


def matmul(A, B):
    return [[sum(F(A[i][k]) * F(B[k][j]) for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


GRAMS = {
    # name: (Gram matrix, hand signature (p, q, r))
    "hyperbolic": ([[0, 1], [1, 0]], (1, 1, 0)),
    "plane-2-3": ([[2, 0], [0, 3]], (2, 0, 0)),
    "mixed": ([[1, 2, 0], [2, 1, 0], [0, 0, -3]], (2, 1, 0)),
    "degenerate": ([[1, 1, 0], [1, 1, 0], [0, 0, 0]], (1, 0, 2)),
    "null-pair-and-radical": ([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 5]], (2, 1, 1)),
    "lorentz-skew": ([[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, -1, 1], [1, 1, 1, -2]], (1, 3, 0)),
}


def check_complete_field_square_root_step():
    for a in (F(2), F(3), F(1, 2), F(10), F(7, 3)):
        for s in (F(1, 3), F(1), F(5, 4), F(3, 2), F(2), F(4)):
            if s * s < a:
                h = min(F(1), (a - s * s) / (2 * s + 1))
                assert h > 0 and (s + h) ** 2 <= a
            elif s * s > a:
                h = (s * s - a) / (2 * s)
                assert 0 < h < s and (s - h) ** 2 > a
    # hand values for a = 2
    s = F(1)
    h = min(F(1), (2 - s * s) / (2 * s + 1))
    assert h == F(1, 3) and (s + h) ** 2 == F(16, 9)
    s = F(3, 2)
    h = (s * s - 2) / (2 * s)
    assert h == F(1, 12) and (s - h) ** 2 == F(289, 144)
    # 2 has no rational square root: a^2 = 2 b^2 forces a, b even (residues mod 4)
    bad = [(x, y) for x in range(4) for y in range(4)
           if (x * x - 2 * y * y) % 4 == 0 and (x % 2, y % 2) != (0, 0)]
    assert bad == []
    return True


def check_orthogonal_basis_by_rejection():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.polarisation")
    premise("std-algebra.inverse-of-vector")
    for name, (G, sig) in GRAMS.items():
        n = len(G)
        std = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        _, us, vals = counts(G, std)
        for i in range(n):
            for j in range(n):
                val = vals[i] if i == j else F(0)
                assert bil(us[i], us[j], G) == val
                assert anticommutator_is_scalar(us[i], us[j], G, val)
    # G = A^T D A with A unitriangular: rejection in order gives D; normalise by square roots
    A = [[1, 2, -1, 3], [0, 1, 4, -2], [0, 0, 1, 5], [0, 0, 0, 1]]
    D = [F(4), F(-9), F(0), F(1, 4)]
    roots = [F(2), F(3), None, F(1, 2)]
    G = matmul(transpose(A), matmul([[D[i] if i == j else 0 for j in range(4)] for i in range(4)], A))
    std = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    us = []
    for i in range(4):
        x = [F(v) for v in std[i]]
        for u in us:
            Qu = bil(u, u, G)
            if Qu != 0:
                x = [a - bil(x, u, G) / Qu * b for a, b in zip(x, u)]
        us.append(x)
    assert [bil(u, u, G) for u in us] == D
    es = [[c / roots[i] for c in us[i]] if roots[i] else us[i] for i in range(4)]
    assert [bil(e, e, G) for e in es] == [1, -1, 0, 1]
    for i in range(4):
        for j in range(4):
            assert anticommutator_is_scalar(es[i], es[j], G, bil(es[i], es[j], G))
            if i != j:
                assert bil(es[i], es[j], G) == 0
    return True


CHANGES = [
    [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
    [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]],
    [[2, 1, 0, 1], [1, 1, 0, 0], [0, 3, 1, 0], [1, 0, 0, 1]],
    [[0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 1, 0], [1, 1, 1, 1]],
]


def check_inertia_is_basis_independent():
    premise("std-algebra.polarisation")
    hand = {"hyperbolic": (1, 1, 0), "plane-2-3": (2, 0, 0), "mixed": (1, 2, 0),
            "degenerate": (1, 0, 2), "null-pair-and-radical": (2, 1, 1), "lorentz-skew": (1, 3, 0)}
    for name, (G, sig) in GRAMS.items():
        n = len(G)
        seen = set()
        for P in CHANGES:
            M = [row[:n] for row in P[:n]]
            if GA.mat_rank(GA.frac_matrix(M)) < n:
                continue
            for order in permutations(range(n)):
                basis = [M[k] for k in order]
                c, _, _ = counts(G, basis)
                seen.add(c)
        assert seen == {hand[name]} == {sig}
        assert hand[name][2] == n - GA.mat_rank(GA.frac_matrix(G))
        assert GA.congruence_signature(G) == hand[name]
    return True


CONST_SIGS = ((1, 1, 0), (2, 1, 1), (0, 2, 2), (1, 3, 0))
EMBED_SIGS = ((1, 0, 1), (0, 1, 1), (1, 1, 1), (0, 0, 2), (2, 0, 1))


def check_base_change_and_degenerate_embedding():
    premise("std-algebra.orthogonal-anticommute")
    premise("std-algebra.blade-basis")
    premise("conformal.minimal-nondegenerate-completion")
    # structure constants of Cl(p,q,r) lie in {0, 1, -1}; the nonzero ones are the pairs of blades
    # sharing no radical index: 4^(p+q) 3^r of them
    nonzero = []
    for (p, q, r) in CONST_SIGS:
        sq = GA.sig(p, q, r)
        bl = GA.all_blades(p + q + r)
        k = 0
        for S in bl:
            for T in bl:
                c, X = GA.blade_mul(S, T, sq)
                assert c in (0, 1, -1)
                if c != 0:
                    assert set(X) == set(S) ^ set(T)
                    k += 1
        nonzero.append(k)
    assert nonzero == [16, 192, 144, 256]
    # Cl(p,q,r) inside Cl(p+r, q+r): radical generators -> e'_k + f'_k
    ranks = []
    for (p, q, r) in EMBED_SIGS:
        P, Qn = p + r, q + r
        sq = GA.sig(P, Qn)
        pos = list(range(p))
        neg = list(range(P, P + q))
        newpos = list(range(p, P))
        newneg = list(range(P + q, P + Qn))
        imgs = [GA.gen(i) for i in pos] + [GA.gen(i) for i in neg]
        imgs += [GA.add(GA.gen(a), GA.gen(b)) for a, b in zip(newpos, newneg)]
        squares = [1] * p + [-1] * q + [0] * r
        n = p + q + r
        for i in range(n):
            assert GA.mul(imgs[i], imgs[i], sq) == GA.sc(squares[i])
            for j in range(i + 1, n):
                assert GA.anticommutes(imgs[i], imgs[j], sq)
        big = GA.all_blades(P + Qn)
        rows = []
        for S in GA.all_blades(n):
            x = GA.sc(1)
            for k in S:
                x = GA.mul(x, imgs[k], sq)
            rows.append(GA.basis_vector_of(x, big))
        ranks.append(GA.rank_of_vectors(rows))
    assert ranks == [4, 4, 8, 4, 8]
    return True


def check_square_classes_survive_over_the_rationals():
    def conj(x):
        return GA.grade_inv(GA.reverse(x))
    # the line with e^2 = 2, and the plane with squares 2 and 3
    for sq, form in (((F(2),), lambda a, b, c, d: a * a - 2 * b * b),
                     ((F(2), F(3)), lambda a, b, c, d: a * a - 2 * b * b - 3 * c * c + 6 * d * d)):
        n = len(sq)
        bl = GA.all_blades(n)
        for cs in product((-2, -1, 0, 1, 3), repeat=2 ** n):
            x = {S: F(c) for S, c in zip(bl, cs) if c != 0}
            a, b, c, d = (list(cs) + [0, 0])[:4]
            N = form(a, b, c, d)
            assert GA.mul(x, conj(x), sq) == GA.sc(N)
            assert (N == 0) == (not any(cs))
            if N != 0:
                assert GA.mul(x, GA.scal(F(1, N), conj(x)), sq) == GA.sc(1)
    # descent modulo 4 for a^2 - 2b^2, modulo 9 for a^2 - 2b^2 - 3c^2 + 6d^2
    for a, b in product(range(4), repeat=2):
        if (a * a - 2 * b * b) % 4 == 0:
            assert a % 2 == 0 and b % 2 == 0
    for a, b, c, d in product(range(9), repeat=4):
        if (a * a - 2 * b * b - 3 * c * c + 6 * d * d) % 3 == 0:
            assert a % 3 == 0 and b % 3 == 0
            if (a * a - 2 * b * b - 3 * c * c + 6 * d * d) % 9 == 0:
                assert c % 3 == 0 and d % 3 == 0
    # the +-1 forms of the same signs have rational zero divisors
    for sq in (GA.sig(1, 0), GA.sig(2, 0)):
        z = GA.mul(GA.add(GA.sc(1), GA.gen(0)), GA.sub(GA.sc(1), GA.gen(0)), sq)
        assert z == {}
    # squares change by squares: Q(l e) = l^2 Q(e)
    for l in (F(2), F(1, 3), F(-5, 2)):
        e = GA.scal(l, GA.gen(0))
        assert GA.mul(e, e, (F(2),)) == GA.sc(2 * l * l)
    return True
