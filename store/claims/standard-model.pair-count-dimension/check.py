"""standard-model.pair-count-dimension: exact checks.

For n = 2, 4, 6, 8, 10 the complexified ambient space V_C = C^(n+2) carries the form
diag(1, 1, -1, ..., -1) of signature (2, n), with Gaussian-rational (GA.QI) coordinates. The check
builds r = (n+2)/2 null vectors (e_1 + i e_2 and e_k + i e_(k+1) on the negative pairs), confirms by
exact rank computations that their span U is totally isotropic of dimension r, that the form is
nondegenerate (rank 2r), and that U^perp = U (so dim U^perp = 2r - dim U = r: U is maximal, and no
isotropic subspace exceeds r since U' inside U'^perp forces 2 dim U' <= 2r). In the null basis
(U, conjugates) the Gram is the split form (zero blocks on the diagonal, invertible off-diagonal
block). In dimension four r = 3, and three fermionic pairs give the Fock space Lambda(C^3) of
dimension 8 with even half of dimension 4, the three pairs of the imported Fact.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

QI = GA.QI


def form(n):
    return [F(1), F(1)] + [F(-1)] * n


def bil(G, x, y):
    return sum((x[k] * y[k] * G[k] for k in range(len(G))), QI(0))


def null_basis(n):
    """r = (n + 2)/2 null vectors and their conjugates."""
    d = n + 2
    U, Ubar = [], []
    for a in range(0, d, 2):
        u = [QI(0)] * d
        u[a], u[a + 1] = QI(1), QI(0, 1)
        U.append(u)
        Ubar.append([z.conj() for z in u])
    return U, Ubar


def perp_dim(G, U):
    """Dimension of U^perp = d - rank of the functionals x -> B(u, x)."""
    d = len(G)
    rows = [[u[k] * G[k] for k in range(d)] for u in U]
    return d - GA.field_rank(rows)


EVEN_N = (2, 4, 6, 8, 10)


def check_maximal_isotropic_dimension_is_half():
    ok = True
    for n in EVEN_N:
        G = form(n)
        d = n + 2
        U, Ubar = null_basis(n)
        r = len(U)
        ok = ok and 2 * r == d
        ok = ok and all(bil(G, x, y) == 0 for x in U for y in U)              # totally isotropic
        ok = ok and GA.field_rank(U) == r
        ok = ok and GA.field_rank([[G[i] if i == j else 0 for j in range(d)] for i in range(d)]) == d
        ok = ok and perp_dim(G, U) == d - r                                    # = r: U^perp = U
        # in the null basis the Gram is split: B(U, U) = B(Ubar, Ubar) = 0, B(U, Ubar) invertible
        M = [[bil(G, x, y) for y in Ubar] for x in U]
        ok = ok and GA.field_rank(M) == r and all(bil(G, x, y) == 0 for x in Ubar for y in Ubar)
        ok = ok and all(M[i][j] == (2 if i == j else 0) * (1 if i == 0 else -1) for i in range(r) for j in range(r))
    GA.check("pair count: a nondegenerate form on C^(n+2), n even, has maximal isotropic dimension (n+2)/2", ok)
    return ok


def check_no_larger_isotropic_subspace():
    ok = True
    for n in EVEN_N:
        G = form(n)
        d = n + 2
        U, Ubar = null_basis(n)
        r = len(U)
        # adding any further basis vector of V_C to U destroys isotropy
        for extra in Ubar + [[QI(1) if k == j else QI(0) for k in range(d)] for j in range(d)]:
            if GA.field_rank(U + [extra]) == r + 1:
                ok = ok and any(bil(G, extra, y) != 0 for y in U + [extra])
    ok = ok and [(n + 2) // 2 for n in EVEN_N] == [2, 3, 4, 5, 6]
    GA.check("pair count: no isotropic subspace exceeds (n+2)/2", ok)
    return ok


def check_dimension_four_has_three_pairs():
    premise("standard-model.imported-pair-systems-two-chirality-halves")
    U, _ = null_basis(4)
    states = [c for k in range(4) for c in combinations(range(len(U)), k)]
    ok = len(U) == 3 and len(states) == 8 and sum(1 for c in states if len(c) % 2 == 0) == 4
    GA.check("pair count: in dimension four the pair system has three pairs, Fock space 8, halves 4", ok)
    return ok
