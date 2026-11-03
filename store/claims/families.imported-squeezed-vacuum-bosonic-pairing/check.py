"""families.imported-squeezed-vacuum-bosonic-pairing: exact checks.

Exact model: two bosonic modes, Gaussian-rational unitary U (module level), and "hyperbolic" pairs
(cosh sigma_j, sinh sigma_j) = (5/4, 3/4), (13/12, 5/12) (rational points of c^2 - s^2 = 1, so no transcendental
is needed). Reference modes c_j act on the unnormalised Fock basis (c^dagger)^k |0> (c^dagger raises, c lowers with
factor k), so all matrix elements are rational; <0| X |0> is the |0,0> coefficient of X|0>. Occupations up to 4
are kept, which is exact for every product of at most four mode operators applied to the vacuum.
The squeezed vacuum of the pairing xi = U Sigma U^T is the vacuum of the c_j with a = U (C c - S c^dagger),
C = cosh Sigma, S = sinh Sigma.
(1) Bogoliubov consistency: [a_p, a_q^dagger] = (U (C^2 - S^2) U^dagger)_pq = delta_pq and [a_p, a_q] = 0, from the
    coefficient matrices.
(2) Two-point functions computed in the Fock model: N_pq = <a_p^dagger a_q> = conj(U S^2 U^dagger)_pq and
    M_pq = <a_p a_q> = -(U S C U^T)_pq, for all p, q.
(3) Wick: for all 16 index choices, <a_p^dag a_q^dag a_r a_s> = N_ps N_qr + N_pr N_qs + conj(M_pq) M_rs and
    <a_r a_s a_p^dag a_q^dag> = D_rq D_sp + D_rp D_sq + M_rs conj(M_pq) with D_rp = delta_rp + N_pr.
(4) Takagi functional calculus at rational Sigma' (generic and degenerate): xi' = U Sigma' U^T is symmetric,
    xi' xi'^dagger = U Sigma'^2 U^dagger, and U f(Sigma') U^T = g(xi' xi'^dagger) xi' for the odd polynomials
    f(s) = s^3, s^5 + 2 s (g(t) = t, t^2 + 2).
The literature entity (the external restatement) is not touched: the check recomputes its content.
"""
from fractions import Fraction as F

import GA
from GA import QI

R0 = [[QI(F(3, 5)), QI(0, F(4, 5))], [QI(0, F(4, 5)), QI(F(3, 5))]]
PH = [QI(1), QI(F(5, 13), F(12, 13))]
U = [[R0[i][j] * PH[j] for j in range(2)] for i in range(2)]
CS = [(F(5, 4), F(3, 4)), (F(13, 12), F(5, 12))]
SIGMAS = [[F(2), F(1, 3)], [F(3, 2), F(3, 2)]]
KMAX = 4


def conjm(A):
    return [[A[i][j].conj() for j in range(2)] for i in range(2)]


def tp(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def mmul(*Ms):
    out = Ms[0]
    for B in Ms[1:]:
        out = [[sum((out[i][k] * B[k][j] for k in range(2)), QI(0)) for j in range(2)] for i in range(2)]
    return out


def dg(xs):
    return [[QI(xs[0]), QI(0)], [QI(0), QI(xs[1])]]


def apply(op, vec):
    """op = list of (coefficient, mode, kind) with kind +1 create, -1 annihilate; vec {(k0, k1): QI}."""
    out = {}
    for coef, m, kind in op:
        for occ, x in vec.items():
            k = occ[m]
            if kind == 1:
                if k == KMAX:
                    raise ValueError("truncation reached")
                new, fac = k + 1, 1
            else:
                if k == 0:
                    continue
                new, fac = k - 1, k
            o = list(occ)
            o[m] = new
            o = tuple(o)
            out[o] = out.get(o, QI(0)) + coef * x * fac
    return {k: v for k, v in out.items() if v}


def a_op(p):
    return [(U[p][j] * CS[j][0], j, -1) for j in range(2)] + [(-U[p][j] * CS[j][1], j, 1) for j in range(2)]


def ad_op(p):
    return [(U[p][j].conj() * CS[j][0], j, 1) for j in range(2)] + [(-U[p][j].conj() * CS[j][1], j, -1) for j in range(2)]


def vev(*ops):
    vec = {(0, 0): QI(1)}
    for op in reversed(ops):
        vec = apply(op, vec)
    return vec.get((0, 0), QI(0))


def check_bogoliubov_relations():
    C2mS2 = dg([c * c - s * s for c, s in CS])
    ok = mmul(U, C2mS2, conjm(tp(U))) == [[QI(1), QI(0)], [QI(0), QI(1)]]
    comm_aa = [[sum((U[p][j] * U[q][j] * (-CS[j][0] * CS[j][1] + CS[j][1] * CS[j][0]) for j in range(2)), QI(0))
                for q in range(2)] for p in range(2)]
    ok = ok and all(x == 0 for r in comm_aa for x in r)
    ok = ok and mmul(U, conjm(tp(U))) == [[QI(1), QI(0)], [QI(0), QI(1)]]
    GA.check("a = U (C c - S c^dag) obeys the CCR", ok)
    return ok


def two_point():
    S2 = dg([s * s for _, s in CS])
    SC = dg([s * c for c, s in CS])
    N = conjm(mmul(U, S2, conjm(tp(U))))
    M = [[-x for x in r] for r in mmul(U, SC, tp(U))]
    return N, M


def check_two_point_functions():
    N, M = two_point()
    ok = True
    for p in range(2):
        for q in range(2):
            ok = ok and vev(ad_op(p), a_op(q)) == N[p][q] and vev(a_op(p), a_op(q)) == M[p][q]
    ok = ok and N[0][1] != 0 and M[0][1] != 0 and M[0][0] != 0
    GA.check("N = conj(U sinh^2 U^dag), M = -(U sinh cosh U^T) in the Fock model", ok)
    return ok


def check_wick_four_point():
    N, M = two_point()
    D = [[QI(1 if r == p else 0) + N[p][r] for p in range(2)] for r in range(2)]
    ok = True
    for p in range(2):
        for q in range(2):
            for r in range(2):
                for s in range(2):
                    lhs = vev(ad_op(p), ad_op(q), a_op(r), a_op(s))
                    rhs = N[p][s] * N[q][r] + N[p][r] * N[q][s] + M[p][q].conj() * M[r][s]
                    lhs2 = vev(a_op(r), a_op(s), ad_op(p), ad_op(q))
                    rhs2 = D[r][q] * D[s][p] + D[r][p] * D[s][q] + M[r][s] * M[p][q].conj()
                    ok = ok and lhs == rhs and lhs2 == rhs2
    GA.check("Wick's theorem for both four-point orderings, all 16 index choices", ok)
    return ok


def check_takagi_functional_calculus():
    ok = True
    for sig in SIGMAS:
        xi = mmul(U, dg(sig), tp(U))
        ok = ok and xi == tp(xi)
        h = mmul(xi, conjm(tp(xi)))
        ok = ok and h == mmul(U, dg([x * x for x in sig]), conjm(tp(U)))
        f3 = mmul(U, dg([x ** 3 for x in sig]), tp(U))
        ok = ok and f3 == mmul(h, xi)
        f5 = mmul(U, dg([x ** 5 + 2 * x for x in sig]), tp(U))
        g5 = [[h2 + (QI(2) if i == j else QI(0)) for j, h2 in enumerate(row)] for i, row in enumerate(mmul(h, h))]
        ok = ok and f5 == mmul(g5, xi)
    GA.check("U f(Sigma) U^T = g(xi xi^dag) xi, generic and degenerate singular values", ok)
    return ok
