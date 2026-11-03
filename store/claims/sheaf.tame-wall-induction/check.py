"""sheaf.tame-wall-induction: exact checks in two collar models (n = 4, frame (k-slot, m1, m2, m3, n0, ninf)).

Model A (shadow wall at a rational point): G(tau) = [[tau - b^2, b], [b, -1]] + diag(-1, -1), b = 2, which is tame
at tau = 0 (det G = -tau, radical k = (1, b, 0, 0), k(u) = 1 for u = (1, 0, 0, 0)), so s = G^{-1}(e, e) = 1/tau
exactly and s is strictly monotone on the far side; coupling mu = nu = 1/2 (mu nu = 1/4, good for this model).
Model B (the general collar model): lambda = tau + 2 tau^2, cross terms b = (3 tau, tau^2, 0), G1 =
diag(-1, -1, -1 + tau), e = (1, 1/2, 0, 0).
(1) det h = det G (-(1 + 2 mu nu s)) as rational-function identities (both models, two couplings for B), and
(tau s)(0) = 1/lambda'(0) = 1 in B (s = 1/lambda + O(1)). In A: F = 1 + 2 mu nu / tau has the single far-side zero
tau' = -2 mu nu = -1/2 (F >= 1 on the physical side, F < 0 between the walls, F > 0 beyond); dF = 2 mu nu ds
equals -2 at tau'; the zero of det h at tau' is simple.
(2) At tau': h has rank 5 (exactly one vanishing eigenvalue, the zero being simple); adj(h) has rank one,
h adj(h) = 0, and a nonzero column of adj(h) spans ker h.
(3) Jacobi's formula (det h)' = tr(adj(h) h') at three points of each model; at tau' in A,
adj(h) = c k~ k~^T with k~ spanning ker h, and (det h)'(tau') = c h'(k~, k~), so h'(k~, k~) != 0: the
transversality datum of the invariant-form lemma is nonzero (and unchanged when k~ is extended by (tau - tau') m
for two fields m). Hence (T1)-(T3) hold at the shadow wall.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

T = GA.RF.var()
B_CROSS = F(2)
MU_A, NU_A = F(1, 2), F(1, 2)
MU_B, NU_B = F(2), F(3)
JACOBI_A = (F(1, 3), F(-1, 2), F(2))
JACOBI_B = (F(1, 3), F(-1, 5), F(1, 2))
EXT_FIELDS = ([F(1)] * 6, [F(0), F(2), F(-1), F(0), F(3), F(1)])


def C(x):
    return GA.RF.const(F(x))


def model_a():
    b = C(B_CROSS)
    Z = GA.RF0
    G = [[T - b * b, b, Z, Z], [b, C(-1), Z, Z], [Z, Z, C(-1), Z], [Z, Z, Z, C(-1)]]
    return G, [GA.RF1, Z, Z, Z]


def model_b():
    Z = GA.RF0
    lam = T + C(2) * T * T
    bb = [C(3) * T, T * T, Z]
    G = [[lam, bb[0], bb[1], bb[2]], [bb[0], C(-1), Z, Z], [bb[1], Z, C(-1), Z], [bb[2], Z, Z, C(-1) + T]]
    return G, [GA.RF1, C(F(1, 2)), Z, Z]


def coupled(G, e, mu, nu):
    h = [[GA.RF0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = G[i][j]
        h[i][4] = h[4][i] = C(nu) * e[i]
        h[i][5] = h[5][i] = C(mu) * e[i]
    h[4][5] = h[5][4] = C(-1)
    return h


def s_of(G, e):
    x = GA.rf_mat_solve(G, e)
    out = GA.RF0
    for i in range(4):
        out = out + e[i] * x[i]
    return out


def at(M, t0):
    return [[x.eval(t0) for x in row] for row in M]


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
            A[r] = [a - f * bq for a, bq in zip(A[r], A[c])]
    return d


def adj(M):
    n = len(M)
    out = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            minor = [[M[r][c] for c in range(n) if c != i] for r in range(n) if r != j]
            out[i][j] = (-1) ** (i + j) * det(minor)
    return out


def check_shadow_wall_is_a_simple_regular_level_set():
    premise("sheaf.determinant-identity-blow-up-expansion")
    premise("sheaf.tameness")
    ok = True
    G, e = model_a()
    ok = ok and GA.rf_mat_det(G).eqrf(-T) and GA.mat_rank(at(G, F(0))) == 3
    s = s_of(G, e)
    ok = ok and s.eqrf(GA.RF1 / T)
    h = coupled(G, e, MU_A, NU_A)
    Fn = GA.RF1 + C(2 * MU_A * NU_A) * s
    deth = GA.rf_mat_det(h)
    ok = ok and deth.eqrf(GA.rf_mat_det(G) * (-Fn))
    tp = -2 * MU_A * NU_A
    ok = ok and tp == F(-1, 2) and Fn.eval(tp) == 0
    ok = ok and len(Fn.num) == 2                          # numerator linear: a single zero
    # F >= 1 on the physical side, F -> -infinity at the wall from the far side, F > 0 beyond tau'
    ok = ok and all(Fn.eval(t0) >= 1 for t0 in (F(3), F(1, 5)))
    ok = ok and all(Fn.eval(t0) < 0 for t0 in (F(-1, 5), F(-2, 5))) and all(Fn.eval(t0) > 0 for t0 in (F(-1), F(-3)))
    ok = ok and (C(2 * MU_A * NU_A) * s.deriv()).eval(tp) == -2 and deth.deriv().eval(tp) != 0
    # model B: the identity at two couplings, and the blow-up expansion
    Gb, eb = model_b()
    sb = s_of(Gb, eb)
    for mu, nu in ((2, 3), (F(-1, 2), 1)):
        hb = coupled(Gb, eb, mu, nu)
        ok = ok and GA.rf_mat_det(hb).eqrf(GA.rf_mat_det(Gb) * (-(GA.RF1 + C(2 * F(mu) * nu) * sb)))
    ok = ok and (T * sb).eval(F(0)) == 1
    GA.check("the shadow wall {F = 0} is a single simple zero tau' = -2 mu nu of det h; det identity holds", ok)
    return ok


def check_radical_line_is_an_adjugate_column():
    ok = True
    G, e = model_a()
    hp = at(coupled(G, e, MU_A, NU_A), -2 * MU_A * NU_A)
    ok = ok and GA.mat_rank(hp) == 5
    A = adj(hp)
    ok = ok and GA.mat_rank(A) == 1
    prod = [[sum(hp[i][t] * A[t][j] for t in range(6)) for j in range(6)] for i in range(6)]
    ok = ok and all(x == 0 for row in prod for x in row)
    ker = GA.field_kernel(hp)
    col = next([A[i][j] for i in range(6)] for j in range(6) if any(A[i][j] != 0 for i in range(6)))
    ok = ok and len(ker) == 1 and GA.mat_rank([ker[0], col]) == 1
    GA.check("at tau' h has corank one and the radical line is spanned by a column of adj(h)", ok)
    return ok


def check_jacobi_formula_gives_transversality():
    premise("sheaf.invariant-form-t3")
    ok = True
    for (G, e), (mu, nu), pts in ((model_a(), (MU_A, NU_A), JACOBI_A), (model_b(), (MU_B, NU_B), JACOBI_B)):
        h = coupled(G, e, mu, nu)
        dh = [[x.deriv() for x in row] for row in h]
        deth = GA.rf_mat_det(h)
        for t0 in pts:
            A = adj(at(h, t0))
            D1 = at(dh, t0)
            ok = ok and deth.deriv().eval(t0) == sum(A[i][j] * D1[j][i] for i in range(6) for j in range(6))
    G, e = model_a()
    h = coupled(G, e, MU_A, NU_A)
    tp = -2 * MU_A * NU_A
    hp, D1 = at(h, tp), at([[x.deriv() for x in row] for row in h], tp)
    kt = GA.field_kernel(hp)[0]
    A = adj(hp)
    i0 = next(i for i in range(6) if kt[i] != 0)
    c = A[i0][i0] / (kt[i0] * kt[i0])
    ok = ok and all(A[i][j] == c * kt[i] * kt[j] for i in range(6) for j in range(6))
    q = sum(kt[i] * D1[i][j] * kt[j] for i in range(6) for j in range(6))
    ok = ok and GA.rf_mat_det(h).deriv().eval(tp) == c * q and q != 0 and c != 0
    # the datum d h(k~, k~) at tau' does not depend on extending k~ by (tau - tau') m
    for m in EXT_FIELDS:
        ext = [GA.RF.const(kt[i]) + (T - C(tp)) * C(m[i]) for i in range(6)]
        g = GA.RF0
        for i in range(6):
            for j in range(6):
                if not h[i][j].is_zero():
                    g = g + ext[i] * h[i][j] * ext[j]
        ok = ok and g.eval(tp) == 0 and g.deriv().eval(tp) == q
    GA.check("Jacobi: (det h)'(tau') = c h'(k~, k~), so the transversality datum at the shadow wall is nonzero", ok)
    return ok
