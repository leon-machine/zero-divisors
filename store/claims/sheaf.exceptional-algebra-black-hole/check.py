"""sheaf.exceptional-algebra-black-hole: exact checks on Schwarzschild data, 2M = m^2 (m = 1, 2, 3),
as rational-function identities in u = sqrt(r) (GA.RF).

The Gram of W on the frame (rho, dt_PG, mu1, mu2) is derived from the inverse Painleve-Gullstrand
metric block (g_tt = 1 - m^2/r, g_tr = -m/u, g_rr = -1), as in Theorem
sheaf.schwarzschild-degeneration-boundary-tame. The rescaled frame of
sheaf.exceptional-algebra-deformation-normal-cone is (rho, k/sqrt r, mu1, mu2) with k = rho + m dt_PG.
  (1) In the rescaled frame: G(rho, rho) = m^2 - r, the cross term G(rho, k/sqrt r) = -u (vanishing at
      the wall), and G(k/sqrt r, k/sqrt r) = -1 identically in u (exact, not only in the limit); the
      limit Gram at u = 0 is diag(m^2, -1, -1, -1), of signature (1,3), and of determinant -m^2.
  (2) The residue: the (rho, dt) block has determinant -r and inverse
      -(1/r) [[1, m], [m, m^2 - r]] exactly, so r G^-1 -> -k (x) k (rank one) on that block while the
      angular block contributes r * (-1) -> 0.
  (3) The exceptional algebra: on the limit form the rescaled vectors rho/m, k/sqrt r, mu1, mu2 are
      orthonormal of signature (1,3), and the Clifford relations of Cl(1,3) hold for their images in
      the exterior (Chevalley) model of the limit Gram (GA.ext_c) on all 16 basis states.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

U = GA.RF.var()
R = U * U
MASSES = (F(1), F(2), F(3))


def C(x):
    return GA.RF.const(F(x))


def gram(m):
    beta = C(m) / U
    g_tt, g_tr, g_rr = GA.RF1 - beta * beta, -beta, C(-1)
    det = g_tt * g_rr - g_tr * g_tr
    Ctt, Ctr, Crr = g_rr / det, -g_tr / det, g_tt / det
    Z = GA.RF0
    return [[R * Crr, U * Ctr, Z, Z], [U * Ctr, Ctt, Z, Z], [Z, Z, C(-1), Z], [Z, Z, Z, C(-1)]]


def congr(P, G):
    n = len(G)
    return [[sum((P[i][a] * G[a][b] * P[j][b] for a in range(n) for b in range(n)), GA.RF0)
             for j in range(n)] for i in range(n)]


def rescaled(m):
    Z, O = GA.RF0, GA.RF1
    P = [[O, Z, Z, Z], [O / U, C(m) / U, Z, Z], [Z, Z, O, Z], [Z, Z, Z, O]]
    return congr(P, gram(m))


def check_rescaled_gram_and_its_limit():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    premise("sheaf.exceptional-algebra-deformation-normal-cone")
    ok = True
    for m in MASSES:
        Gp = rescaled(m)
        ok = ok and Gp[0][0].eqrf(C(m * m) - R) and Gp[0][1].eqrf(-U) and Gp[1][0].eqrf(-U)
        ok = ok and Gp[1][1].eqrf(C(-1))
        ok = ok and Gp[2][2].eqrf(C(-1)) and Gp[3][3].eqrf(C(-1))
        ok = ok and all(Gp[i][j].is_zero() for i in range(4) for j in range(4) if i != j and {i, j} != {0, 1})
        G0 = [[e.eval(F(0)) for e in row] for row in Gp]
        ok = ok and G0 == [[m * m, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        ok = ok and GA.congruence_signature(G0) == (1, 3, 0)
        ok = ok and GA.rf_mat_det(Gp).eval(F(0)) == -m * m
    GA.check("rescaled Gram: cross term -sqrt r, dying entry -1 exactly, limit diag(m^2,-1,-1,-1) of signature (1,3)", ok)
    return ok


def check_residue_is_minus_k_tensor_k():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    ok = True
    for m in MASSES:
        G = gram(m)
        blk = [[G[0][0], G[0][1]], [G[1][0], G[1][1]]]
        ok = ok and blk[0][0].eqrf(C(m * m) - R) and blk[0][1].eqrf(C(-m)) and blk[1][1].eqrf(GA.RF1)
        ok = ok and GA.rf_mat_det(blk).eqrf(-R)
        inv = GA.rf_mat_inverse(blk)
        want = [[-GA.RF1 / R, C(-m) / R], [C(-m) / R, -(C(m * m) - R) / R]]
        ok = ok and all(inv[i][j].eqrf(want[i][j]) for i in range(2) for j in range(2))
        lim = [[(R * inv[i][j]).eval(F(0)) for j in range(2)] for i in range(2)]
        ok = ok and lim == [[-1, -m], [-m, -m * m]] and GA.mat_rank(lim) == 1
        ok = ok and (R * (GA.RF1 / G[2][2])).eval(F(0)) == 0
    GA.check("r G^-1 -> -k (x) k on the (rho, dt) block (rank one), angular block -> 0", ok)
    return ok


def check_exceptional_algebra_is_cl13():
    ok = True
    for m in MASSES:
        G0 = [[m * m, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        vecs = [[1 / m, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        vecs = [[F(x) for x in v] for v in vecs]
        gram_v = [[sum(a[i] * G0[i][j] * b[j] for i in range(4) for j in range(4)) for b in vecs] for a in vecs]
        ok = ok and gram_v == [[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        for S in GA.all_blades(4):
            st = {frozenset(S): F(1)}
            for a in range(4):
                for b in range(4):
                    ab = GA.ext_c(vecs[a], G0, GA.ext_c(vecs[b], G0, st))
                    ba = GA.ext_c(vecs[b], G0, GA.ext_c(vecs[a], G0, st))
                    tot = {}
                    for d in (ab, ba):
                        for k, c in d.items():
                            tot[k] = tot.get(k, F(0)) + c
                    tot = {k: c for k, c in tot.items() if c != 0}
                    want = {frozenset(S): 2 * gram_v[a][b]} if gram_v[a][b] else {}
                    ok = ok and tot == want
    GA.check("on the limit form the rescaled frame generates Cl(1,3) (relations on all 16 exterior states)", ok)
    return ok
