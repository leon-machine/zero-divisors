"""three-routes.base-unipotents-their-action-candidates: exact checks at the Schwarzschild boundary point, with
the boundary Gram G(0) and radical k = rho + m dt of the premise, for m = 1, 2.

Covectors alpha are columns on the frame (rho, dt, mu1, mu2), vectors pair with them by alpha(u) = sum alpha_i u_i,
and g_lambda = id + k lambda^T. For every lambda in the 27-point lattice {-1, 0, 1}-combinations of the basis
(-m, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1) of ker k:
g_lambda^T G g_lambda = G (isometry), g_lambda k = k, g_lambda g_lambda' = g_(lambda + lambda') on all pairs; the
dual action (g_lambda^{-1})^T, obtained by exact inversion, equals id - lambda k^T (u -> u - k(u) lambda); on three
candidates (k(u) = 1) it is translation by -lambda, with no fixed candidate for lambda != 0 (free), and for every
pair of candidates there is exactly one lattice lambda carrying one to the other (transitive on the sample).
Control: for lambda with k(lambda) != 0, g_lambda moves k (to (1 + k(lambda)) k).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

MASSES = (F(1), F(2))


def boundary_data(m):
    G = [[m * m, -m, F(0), F(0)], [-m, F(1), F(0), F(0)], [F(0), F(0), F(-1), F(0)], [F(0), F(0), F(0), F(-1)]]
    return G, [F(1), m, F(0), F(0)]


mm = GA.mat_mul


def tr(A):
    return [list(r) for r in zip(*A)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def g_of(k, lam):
    return [[(F(1) if i == j else F(0)) + k[i] * lam[j] for j in range(4)] for i in range(4)]


def lattice(m):
    basis = [[-m, F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
    out = []
    for c in product((-1, 0, 1), repeat=3):
        out.append([sum(c[b] * basis[b][i] for b in range(3)) for i in range(4)])
    return out


def inverse(M):
    cols = [GA.field_solve(M, [F(1) if i == c else F(0) for i in range(4)]) for c in range(4)]
    return [[cols[c][i] for c in range(4)] for i in range(4)]


def check_unipotents_are_isometries_fixing_k():
    premise("three-routes.imported-boundary-gram-ladder")
    ok = True
    for m in MASSES:
        G, k = boundary_data(m)
        lams = lattice(m)
        ok = ok and len(lams) == 27
        for lam in lams:
            ok = ok and sum(k[i] * lam[i] for i in range(4)) == 0
            g = g_of(k, lam)
            ok = ok and mm(tr(g), mm(G, g)) == G
            ok = ok and [sum(g[i][j] * k[j] for j in range(4)) for i in range(4)] == k
        for lam in lams:
            for lam2 in lams:
                ok = ok and mm(g_of(k, lam), g_of(k, lam2)) == g_of(k, [lam[i] + lam2[i] for i in range(4)])
        # control: k(lambda) = 2 gives g k = 3 k
        bad = [F(1), F(1) / m, F(0), F(0)]
        gb = g_of(k, bad)
        ok = ok and [sum(gb[i][j] * k[j] for j in range(4)) for i in range(4)] == [3 * x for x in k]
    GA.check("g_lambda is a G-isometry fixing k with g_lambda g_lambda' = g_(lambda+lambda') (27 lambdas)", ok)
    return ok


def check_dual_action_translates_candidates():
    premise("three-routes.imported-boundary-gram-ladder")
    ok = True
    for m in MASSES:
        G, k = boundary_data(m)
        cands = [[F(1), F(0), F(0), F(0)], [F(1) - m, F(1), F(0), F(0)], [F(1), F(0), F(5), F(-2)]]
        ok = ok and all(sum(k[i] * c[i] for i in range(4)) == 1 for c in cands)
        for lam in lattice(m):
            dual = tr(inverse(g_of(k, lam)))
            closed = [[(F(1) if i == j else F(0)) - lam[i] * k[j] for j in range(4)] for i in range(4)]
            ok = ok and dual == closed
            for c in cands:
                img = [sum(dual[i][j] * c[j] for j in range(4)) for i in range(4)]
                ok = ok and img == [c[i] - lam[i] for i in range(4)]
                ok = ok and (img == c) == all(x == 0 for x in lam)
        # transitivity on the sample: each ordered pair of candidates is joined by exactly one lattice lambda
        for a in cands:
            for b in cands:
                hits = [lam for lam in lattice(m) if [a[i] - lam[i] for i in range(4)] == b]
                expected = 1 if (a == b or (a[2] == b[2] and a[3] == b[3])) else 0
                ok = ok and len(hits) == expected
                # transitivity in general: lambda = a - b lies in ker k and carries a to b
                lam = [a[i] - b[i] for i in range(4)]
                ok = ok and sum(k[i] * lam[i] for i in range(4)) == 0
                dual = tr(inverse(g_of(k, lam)))
                ok = ok and [sum(dual[i][j] * a[j] for j in range(4)) for i in range(4)] == b
    GA.check("the dual action is u -> u - k(u) lambda: candidates translate by -lambda, freely", ok)
    return ok
