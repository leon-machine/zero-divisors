"""tower.wall-package: exact checks of the computable clauses in the iterated collar model of
sheaf.infinite-wall-sequence (its EXPORTS: G = diag(tau, -1, -1, -1), physical side tau > 0 of signature (1,3),
couplings mu = nu = 1/2 at every stage, walls tau_k = -k/2).

(1) Tameness of the input (corank one at tau = 0, det G = -tau: a simple zero) and the one-sided completion: h_1 is
nondegenerate of signature (2,4) at the wall and on the physical side.
(2) Conservation of degeneracy, located: h_1 degenerates exactly at the shadow wall tau_1 = -2 mu nu = -1/2 (corank
one), with signature (2,4) between the walls and (1,5) beyond; absolute form, in this model: for every coupling
constant c = mu nu in {-3, -1/2, 0, 1/4, 2}, det h_1 = tau + 2c (computed at two points, affine) vanishes at
tau = -2c, so no completion of this kind is nondegenerate everywhere; degeneracy is displaced, not destroyed.
(3) The iteration: every shadow wall is a simple corank-one zero (tame for the good coupling), its radical line
has the explicit section of the sequence (e(x) = -2 != 0, so collar data exist automatically), and the ambient
signature at the k-th wall is (2 + k, 4 + k) for k = 0..3: one hyperbolic plane per wall.
Not checked: the clause that the transported reciprocal divides totally (transport.totality, a theorem of T1 about
the conformal quadric), which this model does not reach.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def check_completion_nondegenerate_up_to_the_wall():
    premise("sheaf.tameness")
    premise("sheaf.one-sided-completion")
    ex = premise("sheaf.infinite-wall-sequence")
    ok = True
    st, det = ex["stage"], ex["det"]
    ok = ok and det(st(0, F(0))) == 0 and det(st(0, F(1))) == -1 and GA.mat_rank(st(0, F(0))) == 3
    for t0 in (F(0), F(1, 5), F(2)):
        ok = ok and GA.congruence_signature(st(1, t0)) == (2, 4, 0)
    ok = ok and GA.congruence_signature(st(0, F(1, 5))) == (1, 3, 0)
    GA.check("the completion of a tame wall is nondegenerate of signature (2,4) up to and including the wall", ok)
    return ok


def h1(c, tau0):
    """Stage-1 form with coupling nu = 1, mu = c (mu nu = c)."""
    h = [[F(0)] * 6 for _ in range(6)]
    h[0][0] = F(tau0)
    for i in (1, 2, 3):
        h[i][i] = F(-1)
    h[0][4] = h[4][0] = F(1)
    h[0][5] = h[5][0] = F(c)
    h[4][5] = h[5][4] = F(-1)
    return h


def check_degeneracy_relocated_to_shadow_wall():
    premise("sheaf.conservation-degeneracy-located")
    premise("sheaf.conservation-degeneracy-absolute-form")
    ex = premise("sheaf.infinite-wall-sequence")
    ok = True
    st, det = ex["stage"], ex["det"]
    tp = -2 * ex["mu"] * ex["nu"]
    ok = ok and tp == F(-1, 2) and det(st(1, tp)) == 0 and GA.mat_rank(st(1, tp)) == 5
    ok = ok and GA.congruence_signature(st(1, F(-1, 4))) == (2, 4, 0)
    ok = ok and GA.congruence_signature(st(1, F(-1))) == (1, 5, 0)
    for c in (F(-3), F(-1, 2), F(0), F(1, 4), F(2)):
        d0, d1 = det(h1(c, F(0))), det(h1(c, F(1)))
        root = -d0 / (d1 - d0)
        ok = ok and d1 - d0 == 1 and d0 == 2 * c and root == -2 * c and det(h1(c, root)) == 0
    GA.check("degeneracy moves to the shadow wall -2 mu nu; every coupling degenerates somewhere", ok)
    return ok


def check_iterated_walls_tame_one_plane_each():
    premise("sheaf.tame-wall-induction")
    ex = premise("sheaf.infinite-wall-sequence")
    ok = True
    st, det, walls = ex["stage"], ex["det"], ex["walls"]
    mu, nu = ex["mu"], ex["nu"]
    for k in range(4):
        wk, wn = walls[k], walls[k + 1]
        ok = ok and wn == wk - F(1, 2)
        ok = ok and GA.congruence_signature(st(k + 1, wk)) == (2 + k, 4 + k, 0)
        hn = st(k + 1, wn)
        ok = ok and GA.mat_rank(hn) == len(hn) - 1
        ok = ok and det(st(k + 1, wn + 1)) - det(hn) != 0
        n = len(st(k, wn))
        a0 = GA.field_solve(st(k, wn), [F(1)] + [F(0)] * (n - 1))
        x = a0 + [mu * a0[0], nu * a0[0]]
        ok = ok and all(sum(hn[i][j] * x[j] for j in range(n + 2)) == 0 for i in range(n + 2)) and x[0] == -2
    GA.check("each shadow wall is a simple corank-one zero with a global radical section; signature (2+k, 4+k)", ok)
    return ok
