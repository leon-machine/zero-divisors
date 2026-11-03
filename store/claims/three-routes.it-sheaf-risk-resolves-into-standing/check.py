"""three-routes.it-sheaf-risk-resolves-into-standing: exact checks on a finite model.

(1) Fibre: one ladder mode k = [[0,1],[0,0]], k* = k^T (CAR checked), sigma = k* k - k k*. Ad sigma is an
    automorphism with sigma^2 = 1; Fix(Ad sigma) = span(1, sigma) (computed kernel, dimension 2) is a
    subalgebra containing 1, and k is not even.
(2) Sheaf axioms on a finite model: U = {0, 1, 2} with the cover {0, 1}, {1, 2}; families of fibre elements
    even at every point that agree on the overlap glue to a unique family, even at every point; products of
    even families and function multiples of even families are even (restriction is restriction of
    coefficient functions).
(3) sigma does not change under the ladder rescaling k -> c k, k* -> k*/c.
(4) The untwisted ladder bundle exists exactly when w1(L) = 0: on the two-chart circle with overlap
    transitions (g1, g2) in {+1, -1}^2 for the line L (w1 = 0 iff g1 g2 = +1), a nowhere-zero section of L,
    sign-constant on each chart, exists for the two untwisted choices (two sign patterns each) and for
    neither twisted choice.
(5) M does not see the twist: under the twisted transition k -> -k, k* -> -k*, sigma is unchanged; the
    transition is Ad sigma itself (sigma k sigma = -k, sigma k* sigma = -k*), the identity on Fix(Ad sigma);
    so on every one of the four transition choices each even fibre element glues to a global section of M,
    while the odd element k (taken as k or -k on the second chart) glues only on the two untwisted ones.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise


def _mm(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def _add(*Ms):
    return [[sum(M[i][j] for M in Ms) for j in range(len(Ms[0][0]))] for i in range(len(Ms[0]))]


def _sc(c, A):
    return [[c * x for x in r] for r in A]


def _tr(A):
    return [list(r) for r in zip(*A)]


I2 = [[1, 0], [0, 1]]
K = [[0, 1], [0, 0]]
KS = _tr(K)


def sigma(k, ks):
    return _add(_mm(ks, k), _sc(-1, _mm(k, ks)))


def is_even(s, X):
    return _mm(s, _mm(X, s)) == X


def check_fibrewise_even_part_is_subalgebra():
    premise("sheaf.function-linearity-tame-constructions")
    ok = _add(_mm(K, KS), _mm(KS, K)) == I2 and _mm(K, K) == [[0, 0], [0, 0]]
    s = sigma(K, KS)
    ok = ok and _mm(s, s) == I2
    rows = []
    for i, j in product(range(2), repeat=2):
        E = [[1 if (a, b) == (i, j) else 0 for b in range(2)] for a in range(2)]
        D = _add(_mm(s, _mm(E, s)), _sc(-1, E))
        rows.append([F(x) for r in D for x in r])
    fix = GA.field_kernel([list(c) for c in zip(*rows)])
    ok = ok and len(fix) == 2 and is_even(s, I2) and is_even(s, s) and not is_even(s, K)
    ok = ok and is_even(s, _mm(s, s))
    _tp_rv = (ok); assert _tp_rv is not False, "check_fibrewise_even_part_is_subalgebra"; return _tp_rv


def check_even_families_glue_and_form_an_algebra():
    premise("sheaf.function-linearity-tame-constructions")
    s = sigma(K, KS)
    left = {0: _add(_sc(2, I2), _sc(3, s)), 1: _add(_sc(5, I2), _sc(-1, s))}
    right = {1: _add(_sc(5, I2), _sc(-1, s)), 2: _sc(7, s)}
    ok = left[1] == right[1]
    glued = {x: (left[x] if x in left else right[x]) for x in (0, 1, 2)}
    ok = ok and all(glued[x] == (left.get(x) or right.get(x)) for x in (0, 1, 2))
    ok = ok and all(is_even(s, X) for X in glued.values())
    f = {0: 3, 1: -2, 2: 5}
    other = {x: _add(I2, _sc(x - 1, s)) for x in (0, 1, 2)}
    ok = ok and all(is_even(s, _mm(glued[x], other[x])) and is_even(s, _sc(f[x], glued[x])) for x in (0, 1, 2))
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_families_glue_and_form_an_algebra"; return _tp_rv


# sample ladder rescalings k -> c k, k* -> k*/c
RESCALINGS = (F(2), F(-3), F(1, 2))


def check_parity_insensitive_to_ladder_rescaling():
    premise("three-routes.imported-collar-data-coupling")
    ok = True
    for c in RESCALINGS:
        k = _sc(c, K)
        ks = _sc(1 / c, KS)
        # by hand: k* k = E_22 and k k* = E_11 for every c, so sigma = diag(-1, 1)
        ok = ok and _add(_mm(k, ks), _mm(ks, k)) == I2 and sigma(k, ks) == sigma(K, KS) == [[-1, 0], [0, 1]]
    _tp_rv = (ok); assert _tp_rv is not False, "check_parity_insensitive_to_ladder_rescaling"; return _tp_rv


G_CHOICES = [(1, 1), (-1, -1), (1, -1), (-1, 1)]


def transition(g, X):
    """The ladder transition k -> g k, k* -> g k* acting on the fibre algebra: identity or Ad sigma."""
    if g == 1:
        return X
    s = sigma(K, KS)
    return _mm(s, _mm(X, s))


def check_untwisted_ladder_exists_iff_w1_zero():
    premise("three-routes.imported-collar-data-coupling")
    counts = {}
    for g1, g2 in G_CHOICES:
        # a section a on chart A, b on chart B (signs), with a = g1 b on one overlap and a = g2 b on the other
        counts[(g1, g2)] = sum(1 for a, b in product((1, -1), repeat=2) if a == g1 * b and a == g2 * b)
    _tp_rv = ([counts[g] for g in G_CHOICES] == [2, 2, 0, 0]); assert _tp_rv is not False, "check_untwisted_ladder_exists_iff_w1_zero"; return _tp_rv


def check_even_part_does_not_see_the_twist():
    premise("three-routes.imported-collar-data-coupling")
    s = sigma(K, KS)
    flip_k, flip_ks = _sc(-1, K), _sc(-1, KS)
    ok = sigma(flip_k, flip_ks) == s
    ok = ok and transition(-1, K) == flip_k and transition(-1, KS) == flip_ks
    evens = [I2, s, _add(_sc(3, I2), _sc(-2, s))]
    glue_even = glue_odd = 0
    for g1, g2 in G_CHOICES:
        for X in evens:
            if transition(g1, X) == X and transition(g2, X) == X:
                glue_even += 1
        # k on chart A, e k on chart B (e = +1 or -1)
        if any(K == transition(g1, _sc(e, K)) and K == transition(g2, _sc(e, K)) for e in (1, -1)):
            glue_odd += 1
    ok = ok and glue_even == 12 and glue_odd == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_even_part_does_not_see_the_twist"; return _tp_rv
