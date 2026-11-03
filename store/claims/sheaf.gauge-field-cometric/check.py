"""sheaf.gauge-field-cometric: exact checks of the Painleve-Gullstrand gauge field.

Vectors of R^{1,3} in the frame (e_t, e_r, e_theta, e_phi), eta = diag(1, -1, -1, -1); linear maps as
4 x 4 matrices whose entries are rational functions of u = sqrt(r) (GA.RF), with 2M = m^2 for
m = 1, 2, 3, so beta = sqrt(2M/r) = m/u is rational in u.
  (1) P(a) = (a . e_t) e_r has P^2 = 0 identically; hbar = 1 - beta P has the closed-form inverse
      1 + beta P at every r > 0 (both products are the identity as rational-function identities, so
      at the horizon u = m as well), and det hbar = 1.
  (2) The induced metric g(a, b) = hbar^-1(a) . hbar^-1(b), read on the coordinate frame
      (d_t, d_r, d_theta, d_phi/sin theta) -> (e_t, e_r, r e_theta, r e_phi), is exactly
      dt^2 - (dr + beta dt)^2 - r^2 dOmega^2: g_tt = 1 - beta^2, g_tr = -beta, g_rr = -1,
      g_angular = -r^2; the cometric (its inverse) is [[1, -beta], [-beta, -(1 - beta^2)]] on (t, r),
      equal to hbar_adj(e^mu) . hbar_adj(e^nu) with hbar_adj = 1 - beta Pbar, Pbar(a) = (a . e_r) e_t
      the metric adjoint of P.
  (3) Failure at r = 0 through a null kernel: with eps = 1/beta = u/m, eps hbar = eps - P is a
      polynomial in eps whose value at eps = 0 is -P, of rank one with image R e_r and kernel
      e_t-perp = span(e_r, e_theta, e_phi); beta^-2 g = eps^2 eta + eps(P^T eta + eta P) + P^T eta P
      with limit g_hat(a, b) = -(a . e_t)(b . e_t), rank one with radical e_t-perp; e_r is g_hat-null
      while g(e_r, e_r) = -1 at every finite r. The radial null directions e_t + (-beta +- 1) e_r,
      normalised by their e_r coefficient, tend to e_r as u -> 0.
The claim imports these from the singularity paper (its uses); the check computes the finite core
directly. The premise calls mark where each imported statement is used.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

U = GA.RF.var()
MASSES = (F(1), F(2), F(3))
ETA = [1, -1, -1, -1]


def C(x):
    return GA.RF.const(F(x))


def zero():
    return [[GA.RF0] * 4 for _ in range(4)]


def ident():
    return [[GA.RF1 if i == j else GA.RF0 for j in range(4)] for i in range(4)]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), GA.RF0) for j in range(4)] for i in range(4)]


def lin(A, B, c):
    return [[A[i][j] + c * B[i][j] for j in range(4)] for i in range(4)]


def T(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def eta_mat():
    return [[C(ETA[i]) if i == j else GA.RF0 for j in range(4)] for i in range(4)]


def P_mat():
    P = zero()
    P[1][0] = GA.RF1          # P(e_t) = (e_t . e_t) e_r = e_r; P kills e_r, e_theta, e_phi
    return P


def meq(A, B):
    return all(A[i][j].eqrf(B[i][j]) for i in range(4) for j in range(4))


def check_unipotent_gauge_field_invertible_off_zero():
    premise("singularity.unipotent-ray")
    premise("singularity.solution-where-divergence-lies")
    ok = True
    P = P_mat()
    ok = ok and meq(mm(P, P), zero())
    for m in MASSES:
        beta = C(m) / U
        h = lin(ident(), P, -beta)
        hinv = lin(ident(), P, beta)
        ok = ok and meq(mm(h, hinv), ident()) and meq(mm(hinv, h), ident())
        ok = ok and GA.rf_mat_det(h).eqrf(GA.RF1)
        # at the horizon u = m, beta = 1: still invertible
        hm = [[e.eval(m) for e in row] for row in h]
        ok = ok and GA.mat_rank(hm) == 4 and hm[1][0] == -1
    GA.check("P^2 = 0, hbar^-1 = 1 + beta P at every r > 0 (horizon included), det hbar = 1", ok)
    return ok


def check_induced_metric_is_painleve_gullstrand():
    ok = True
    P = P_mat()
    for m in MASSES:
        beta = C(m) / U
        r = U * U
        H = lin(ident(), P, beta)                     # hbar^-1
        S = ident()
        S[2][2], S[3][3] = r, r
        g = mm(mm(T(mm(H, S)), eta_mat()), mm(H, S))
        want = zero()
        want[0][0], want[0][1], want[1][0], want[1][1] = GA.RF1 - beta * beta, -beta, -beta, C(-1)
        want[2][2], want[3][3] = -r * r, -r * r
        ok = ok and meq(g, want)
        # ds^2 = dt^2 - (dr + beta dt)^2: the same quadratic form
        ok = ok and (GA.RF1 - (beta * beta)).eqrf(g[0][0]) and (-beta).eqrf(g[0][1])
        # the cometric on (t, r) from the adjoint frame hbar_adj(e^mu)
        blk = [[g[0][0], g[0][1]], [g[1][0], g[1][1]]]
        inv = GA.rf_mat_inverse(blk)
        # adjoint frame: hbar_adj = 1 - beta Pbar, Pbar(a) = (a . e_r) e_t, on e^t = e_t, e^r = -e_r
        Pbar = zero()
        Pbar[0][1] = C(-1)
        hadj = lin(ident(), Pbar, -beta)
        ups = [[GA.RF1, GA.RF0, GA.RF0, GA.RF0], [GA.RF0, C(-1), GA.RF0, GA.RF0]]
        imgs = [[sum((hadj[i][k] * v[k] for k in range(4)), GA.RF0) for i in range(4)] for v in ups]
        frame = [[sum((C(ETA[k]) * a[k] * b[k] for k in range(4)), GA.RF0) for b in imgs] for a in imgs]
        cometric = [[GA.RF1, -beta], [-beta, -(GA.RF1 - beta * beta)]]
        ok = ok and all(inv[i][j].eqrf(cometric[i][j]) for i in range(2) for j in range(2))
        ok = ok and all(frame[i][j].eqrf(cometric[i][j]) for i in range(2) for j in range(2))
    GA.check("g = hbar^-1 . hbar^-1 is dt^2 - (dr + beta dt)^2 - r^2 dOmega^2; cometric [[1,-b],[-b,-(1-b^2)]]", ok)
    return ok


def check_degeneration_through_a_null_kernel():
    premise("singularity.degeneration-exactly")
    premise("singularity.cones-fold")
    ok = True
    P = [[F(0)] * 4 for _ in range(4)]
    P[1][0] = F(1)
    eta = [[F(ETA[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
    for m in MASSES:
        # eps hbar = eps - P with eps = u/m: polynomial in u, value -P at u = 0
        eps = U / C(m)
        h = lin(ident(), [[C(x) for x in row] for row in P], -(C(m) / U))
        eh = [[eps * e for e in row] for row in h]
        lim = [[e.eval(F(0)) for e in row] for row in eh]
        ok = ok and lim == [[-x for x in row] for row in P]
    ok = ok and GA.mat_rank(P) == 1
    ker = GA.field_kernel(P)
    ok = ok and len(ker) == 3 and all(v[0] == 0 for v in ker)
    ok = ok and [P[i][0] for i in range(4)] == [0, 1, 0, 0]
    # beta^-2 g = eps^2 eta + eps (P^T eta + eta P) + P^T eta P, limit g_hat = P^T eta P
    PT = [list(r) for r in zip(*P)]

    def fm(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

    ghat = fm(fm(PT, eta), P)
    ok = ok and ghat == [[-1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    ok = ok and GA.congruence_signature(ghat) == (0, 1, 3)
    for m in MASSES:
        beta = C(m) / U
        H = lin(ident(), [[C(x) for x in row] for row in P], beta)
        g = mm(mm(T(H), eta_mat()), H)
        scaled = [[e / (beta * beta) for e in row] for row in g]
        ok = ok and [[e.eval(F(0)) for e in row] for row in scaled] == ghat
        ok = ok and g[1][1].eqrf(C(-1))
        # radial null directions e_t + lam e_r with lam = -beta +- 1, normalised by the e_r coefficient
        for s in (1, -1):
            lam = -beta + C(s)
            ok = ok and (GA.RF1 - (lam + beta) * (lam + beta)).is_zero()
            ok = ok and (GA.RF1 / lam).eval(F(0)) == 0
    GA.check("eps hbar -> -P (kernel e_t-perp), beta^-2 g -> -(a.e_t)(b.e_t); e_r is the folded null direction", ok)
    return ok
