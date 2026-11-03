"""sheaf.local-freeness-constant-rank: exact checks.

Pointwise blade frames along two degenerating cometrics (n = 4), using the exterior-algebra model of the Clifford
action for an arbitrary symmetric Gram (faithful symbol map):
(a) the Schwarzschild weighted Gram G(u) = [[m^2 - u^2, -m], [-m, 1]] + diag(-1, -1) (m = 2), corank one at u = 0;
(b) a non-diagonal family B(t) = B0 + t B1 with B0 of rank 2.
At every sample point the 16 blade symbols have rank 16, while the rank of the Gram itself jumps (3 or 2 at the
degenerate points, 4 elsewhere): the rank of the Clifford sheaf does not see the degeneration.
Structure functions are polynomials in the Gram entries: along (a), the symbols of e0 e1 and e0 e1 e0 have the
hand-derived coefficients B01 = -m on 1, 1 on e0e1, and 2 B01 = -2m on e0, -B00 = u^2 - m^2 on e1, at every sample
u, including u = m where B00 vanishes (so they are the stated polynomials in u).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

M_MASS = F(2)
U_SAMPLES = (F(0), F(1, 3), F(1, 2), F(1), F(2), F(5))
T_SAMPLES = (F(0), F(1, 2), F(-1), F(3))
B0 = [[1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, -2]]
B1 = [[0, 1, 2, 0], [1, 0, 0, 0], [2, 0, 1, 0], [0, 0, 0, 1]]


def schw(u):
    m = M_MASS
    return [[m * m - u * u, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)],
            [F(0), F(0), F(0), F(-1)]]


def family(t):
    return [[F(B0[i][j]) + t * B1[i][j] for j in range(4)] for i in range(4)]


def symbol_rank(B):
    blades = GA.all_blades(4)
    rows = []
    for I in blades:
        st = GA.ext_sigma_blade(I, B, 4)
        rows.append([st.get(frozenset(J), F(0)) for J in blades])
    return GA.rank_of_vectors(rows)


def check_constant_rank_sixteen_through_degeneration():
    premise("sheaf.blade-basis-degenerate-forms-included")
    ok = True
    gram_ranks, sym_ranks = [], []
    for u in U_SAMPLES:
        B = schw(u)
        gram_ranks.append(GA.mat_rank(B))
        sym_ranks.append(symbol_rank(B))
    ok = ok and gram_ranks == [3, 4, 4, 4, 4, 4] and sym_ranks == [16] * 6
    gram_ranks, sym_ranks = [], []
    for t in T_SAMPLES:
        B = family(t)
        gram_ranks.append(GA.mat_rank(B))
        sym_ranks.append(symbol_rank(B))
    ok = ok and gram_ranks[0] == 2 and all(r == 4 for r in gram_ranks[1:]) and sym_ranks == [16] * 4
    GA.check("the blades give 16 independent sections at every point, degenerate points included", ok)
    return ok


def check_structure_functions_polynomial_in_gram():
    premise("sheaf.blade-basis-degenerate-forms-included")
    ok = True
    m = M_MASS
    e0 = [F(1), F(0), F(0), F(0)]
    e1 = [F(0), F(1), F(0), F(0)]
    for u in U_SAMPLES:
        B = schw(u)
        vac = {frozenset(): F(1)}
        two = GA.ext_c(e0, B, GA.ext_c(e1, B, vac))
        three = GA.ext_c(e0, B, GA.ext_c(e1, B, GA.ext_c(e0, B, vac)))
        ok = ok and GA.ext_state_eq(two, {frozenset(): -m, frozenset({0, 1}): F(1)})
        ok = ok and GA.ext_state_eq(three, {frozenset({0}): -2 * m, frozenset({1}): u * u - m * m})
    GA.check("structure functions e0 e1 = B01 + e0^e1 and e0 e1 e0 = 2 B01 e0 - B00 e1 along the family", ok)
    return ok
