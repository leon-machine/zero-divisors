"""conformal.blade-basis-persists-under-degeneracy: exact checks.

Cl(W, B) is realised on the exterior algebra Lambda(W) by the Chevalley action c(a) = a ^ . + i_a,
the contraction taken with B (GA.ext_c, valid for any rational Gram matrix, non-diagonal and
degenerate included). For four (form, basis) pairs: a diagonal degenerate form in a skew basis, a
non-diagonal form with a two-dimensional radical in a skew basis, the zero form (Grassmann case) and
a nondegenerate non-diagonal form, with dimensions m = 3, 4, 3, 4:
  (1) the Gram matrix B(e_i, e_j) = (P G P^T)_ij of the chosen basis is compared with a hand-computed
      matrix, and its radical dimension with the stated degeneracy;
  (2) the Clifford relation c(e_i) c(e_j) + c(e_j) c(e_i) = 2 B(e_i, e_j) holds on Lambda(W), so c
      factors through Cl(W, B);
  (3) the images e_I . 1 of the 2^m blades are linearly independent (rank 2^m), so the blades are
      independent in Cl(W, B);
  (4) the span of the 2^m blade operators is closed under right multiplication by each c(e_j),
      so the image algebra has dimension exactly 2^m, as the blade basis requires.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise


def subsets(m):
    out = []
    for k in range(m + 1):
        out.extend(frozenset(c) for c in combinations(range(m), k))
    return out


def op_apply(vecs, I, G, state):
    """Apply the blade e_I = e_{i1} ... e_{ik} (I sorted) to an exterior state."""
    for i in reversed(sorted(I)):
        state = GA.ext_c(vecs[i], G, state)
    return state


def op_matrix_cols(fn, m):
    basis = subsets(m)
    cols = []
    for S in basis:
        out = fn({S: F(1)})
        cols.extend(out.get(T, F(0)) for T in basis)
    return cols


def gram(P, G):
    m = len(P)
    return [[sum(F(P[i][a]) * G[a][b] * P[j][b] for a in range(m) for b in range(m))
             for j in range(m)] for i in range(m)]


def run_case(G, P, Bexp, radical):
    m = len(G)
    G = [[F(x) for x in r] for r in G]
    vecs = [[F(x) for x in r] for r in P]
    ok = gram(P, G) == [[F(x) for x in r] for r in Bexp]
    ok = ok and m - GA.field_rank([[F(x) for x in r] for r in Bexp]) == radical
    basis = subsets(m)
    # (2) Clifford relation on every basis state
    for i in range(m):
        for j in range(m):
            for S in basis:
                s = {S: F(1)}
                lhs = GA.ext_c(vecs[i], G, GA.ext_c(vecs[j], G, s))
                rhs = GA.ext_c(vecs[j], G, GA.ext_c(vecs[i], G, s))
                tot = dict(lhs)
                for k, c in rhs.items():
                    tot[k] = tot.get(k, F(0)) + c
                ok = ok and GA.ext_state_eq(tot, {S: 2 * Bexp[i][j]})
    # (3) blade images of 1 are independent
    one = {frozenset(): F(1)}
    imgs = [op_apply(vecs, I, G, one) for I in basis]
    ok = ok and GA.field_rank([[x.get(T, F(0)) for T in basis] for x in imgs]) == 2 ** m
    # (4) blade operators span an algebra of dimension 2^m
    blade_ops = [op_matrix_cols(lambda s, I=I: op_apply(vecs, I, G, s), m) for I in basis]
    prods = [op_matrix_cols(lambda s, I=I, j=j: op_apply(vecs, I, G, GA.ext_c(vecs[j], G, s)), m)
             for I in basis for j in range(m)]
    ok = ok and GA.field_rank(blade_ops) == 2 ** m
    ok = ok and GA.field_rank(blade_ops + prods) == 2 ** m
    return ok


def check_blades_form_a_basis_for_any_form_and_basis():
    premise("sheaf.blade-basis-degenerate-forms-included")
    cases = [
        # (Gram G in the reference basis, basis P (rows), B(e_i, e_j) by hand, radical dimension)
        ([[1, 0, 0], [0, 0, 0], [0, 0, -1]],
         [[1, 1, 0], [0, 1, 1], [1, 0, 1]],
         [[1, 0, 1], [0, -1, -1], [1, -1, 0]], 1),
        ([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
         [[1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 1]],
         [[0, 1, 0, 0], [1, 0, 0, 1], [0, 0, 0, 0], [0, 1, 0, 0]], 2),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]],
         [[2, 1, 0], [0, 1, 0], [0, 3, 1]],
         [[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3),
        ([[2, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 1], [0, 0, 1, 1]],
         [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
         [[2, 1, 0, 0], [1, 0, 0, 0], [0, 0, -1, 1], [0, 0, 1, 1]], 0),
    ]
    ok = True
    for G, P, Bexp, rad in cases:
        ok = ok and run_case(G, P, Bexp, rad)
    GA.check("the 2^m blades of any basis are a basis of Cl(W,B), degenerate B included", ok)
    return ok
