"""sheaf.infinite-wall-sequence: exact checks in an iterated collar model.

Stage 0: G = diag(tau, -1, -1, -1) on a collar of the wall tau = 0, physical side tau > 0 of signature (1,3).
Stage k + 1: h_(k+1) = h_k (+) H + coupling, H the hyperbolic plane on (n0, ninf) (h(n0, ninf) = -1), coupling
columns nu e and mu e with e the slot-0 functional, mu = nu = 1/2 at every stage (mu nu = 1/4 > 0, a good coupling
here: s is monotone on the whole far side). Checked for k = 0..3 (forms of size 4, 6, 8, 10, 12):
(1) s_k = h_k^{-1}(e, e) equals 1/(tau - tau_k) at four rational points, with walls tau_k = -k/2: each shadow
wall lies strictly beyond the last, in the unphysical direction; the step s -> s/(1 + 2 mu nu s) of the block
inversion carries 1/(tau - a) to 1/(tau - a + 2 mu nu) as a rational-function identity (the induction step).
(2) det h_k vanishes only at tau_k, with a simple zero (det is affine in tau with nonzero slope; the tame-wall
lemma's simple zero), and h_k has corank exactly one there.
(3) Physical-side fibres ascend the Witt tower: h_(k+1) is nondegenerate of signature (2 + k, 4 + k) at the wall
tau_k and on its physical side, one hyperbolic plane per wall; the Clifford ranks are 2^(4+2k).
(4) The radical line of each shadow wall has the global section x = alpha0 + mu s n0 + nu s ninf
(alpha0 = h^{-1} e, s = e(alpha0)): h(x, .) = e(.) F at two generic points, h x = 0 at the wall, and e(x) = s =
-2 != 0 there, so the slot-0 functional is a transversal for the next coupling.
EXPORTS stage(k, tau0) (the Fraction matrix of h_k), WALLS and the coupling constants, for tower.wall-package.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

MU, NU = F(1, 2), F(1, 2)
STAGES = 4


def stage(k, tau0):
    """h_k at tau = tau0 (k = 0 is G itself)."""
    h = [[F(0)] * 4 for _ in range(4)]
    h[0][0] = F(tau0)
    for i in (1, 2, 3):
        h[i][i] = F(-1)
    for _ in range(k):
        n = len(h)
        new = [row + [F(0), F(0)] for row in h] + [[F(0)] * (n + 2), [F(0)] * (n + 2)]
        new[0][n] = new[n][0] = NU
        new[0][n + 1] = new[n + 1][0] = MU
        new[n][n + 1] = new[n + 1][n] = F(-1)
        h = new
    return h


def s_value(k, tau0):
    h = stage(k, tau0)
    x = GA.field_solve(h, [F(1)] + [F(0)] * (len(h) - 1))
    return x[0]


def det(M):
    A = [list(r) for r in M]
    n, d = len(A), F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


WALLS = [F(-k, 2) for k in range(STAGES + 1)]
EXPORTS = {"stage": stage, "walls": WALLS, "mu": MU, "nu": NU, "det": det, "s_value": s_value}
SAMPLE_TAUS = (F(3), F(1, 7), F(-3, 4), F(-9, 5))
# sample wall positions a for the rational-function identity of the induction step
STEP_SAMPLES = (F(0), F(-1, 2), F(5, 3))


def check_walls_displaced_successively():
    premise("sheaf.one-sided-completion")
    ok = True
    for k in range(STAGES):
        wall = -F(k, 2)
        for t0 in SAMPLE_TAUS:
            if t0 != wall:
                ok = ok and s_value(k, t0) == 1 / (t0 - wall)
        ok = ok and WALLS[k] == wall and WALLS[k + 1] < WALLS[k]
    tvar = GA.RF.var()
    c = GA.RF.const(2 * MU * NU)
    for a in STEP_SAMPLES:
        s = GA.RF1 / (tvar - GA.RF.const(a))
        ok = ok and (s / (GA.RF1 + c * s)).eqrf(GA.RF1 / (tvar - GA.RF.const(a) + c))
    # the block-inversion step s -> s/(1 + 2 mu nu s) carries s_k to s_(k+1): it moves wall k onto wall k + 1
    for k in range(STAGES):
        s = GA.RF1 / (tvar - GA.RF.const(WALLS[k]))
        ok = ok and (s / (GA.RF1 + c * s)).eqrf(GA.RF1 / (tvar - GA.RF.const(WALLS[k + 1])))
    GA.check("s_k = 1/(tau - tau_k) with tau_k = -k/2: each wall displaced beyond the last", ok)
    return ok


def check_each_wall_is_a_simple_corank_one_zero():
    premise("sheaf.tame-wall-induction")
    ok = True
    for k in range(STAGES + 1):
        wall = -F(k, 2)
        d0, d1 = det(stage(k, F(0))), det(stage(k, F(1)))
        d2 = det(stage(k, F(2)))
        slope = d1 - d0
        ok = ok and d2 - d1 == slope and slope != 0                 # affine in tau, nonzero slope
        ok = ok and d0 + slope * wall == 0                           # its only zero is the wall
        ok = ok and slope == (-1) ** (k + 1)
        hw = stage(k, wall)
        ok = ok and GA.mat_rank(hw) == len(hw) - 1
    GA.check("det h_k is affine in tau with its single simple zero at tau_k; corank one there", ok)
    return ok


def check_one_hyperbolic_plane_per_wall():
    premise("sheaf.one-sided-completion")
    ok = True
    for k in range(STAGES):
        wall = -F(k, 2)
        for t0 in (wall, wall + F(1, 4), wall + F(1, 10)):
            sig = GA.congruence_signature(stage(k + 1, t0))
            ok = ok and sig == (2 + k, 4 + k, 0)
        ok = ok and len(stage(k + 1, wall)) == 6 + 2 * k and 2 ** len(stage(k + 1, wall)) == 4 ** (k + 3)
        if k >= 1:
            # the stage-k form on the physical side of its wall carries (1 + k, 3 + k)
            ok = ok and GA.congruence_signature(stage(k, wall + F(1, 10))) == (1 + k, 3 + k, 0)
    GA.check("each completion adds one hyperbolic plane: signatures (2,4), (3,5), (4,6), (5,7) at the walls", ok)
    return ok


def check_radical_lines_have_global_sections():
    premise("sheaf.tame-wall-induction")
    ok = True
    for k in range(STAGES):
        n = 4 + 2 * k
        nxt = -F(k + 1, 2)
        for t0 in (nxt, F(1, 3), F(-5, 2)):
            hk = stage(k, t0)
            e = [F(1)] + [F(0)] * (n - 1)
            a0 = GA.field_solve(hk, e)
            s = a0[0]
            x = a0 + [MU * s, NU * s]
            h1 = stage(k + 1, t0)
            Fv = 1 + 2 * MU * NU * s
            hx = [sum(h1[i][j] * x[j] for j in range(n + 2)) for i in range(n + 2)]
            ok = ok and hx == [Fv * (1 if i == 0 else 0) for i in range(n)] + [F(0), F(0)]
            if t0 == nxt:
                ok = ok and Fv == 0 and all(v == 0 for v in hx) and s == -2 and x[0] != 0
    GA.check("x = alpha0 + mu s n0 + nu s ninf has h(x, .) = e(.) F: a global nowhere-zero radical section", ok)
    return ok
