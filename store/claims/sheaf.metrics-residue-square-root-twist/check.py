"""sheaf.metrics-residue-square-root-twist: exact checks.

Collar models along a transversal with parameter tau (exact rational functions, GA.RF), in the frame
(k, m_1, ..., m_(n-1)) of covectors: Gram G(tau) = [[lambda, b^T], [b, G1(tau)]] with lambda = T tau +
c2 tau^2 + c3 tau^3, b = O(tau) with nonzero tau and tau^2 terms, G1(0) invertible and tau-dependent;
n = 3, 4 and T = 1, 2, -3 (every model has b != 0). C = G^-1 is the matrix of the inverse cometric in the
covector basis, G^-1 = sum C_ab kappa_a (x) kappa_b.
(1) tau C -> (1/T) k (x) k exactly (all n^2 entries at tau = 0), with T = d/dtau G(k, k) at 0, the
    transversality datum delta(k (x) k) = T dtau; the same tensor limit holds in a second, non-adapted
    covector basis (C' = P^-1 C P^-T, limit (1/T) k' k'^T with k' the coordinates of k there).
(2) The weights: the extension of k off the wall (k + tau w) does not change T; k -> c k multiplies T by c^2
    and leaves the residue tensor unchanged; tau -> a tau multiplies the residue by a (the weight of a
    section of N Sigma); residue coefficient times T is 1 (the residue is delta^-1); and the joint change
    k -> c k, tau -> c^2 tau leaves both T and the residue coefficient unchanged (k carries the weight of a
    half-power of a defining function).
(3) The partner line: at the wall Gram with the ladder partner k* = n0/(2 nu) of k, the partner of c k in
    span(n0) is k*/c (solved from 2 h(c k, x n0) = 1), so the partner line scales inversely to the dying line.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RF = GA.RF
TAU = RF.var()
MODELS = [(3, F(1)), (3, F(-3)), (4, F(2)), (4, F(1))]
C_SCALES = [F(2), F(-1, 2), F(3)]
A_SCALES = [F(3), F(1, 2)]


def _c(x):
    return RF.const(F(x))


def model(n, T, scale_k=F(1), a=F(1), ext=False):
    """G(a tau) in the frame (c k [+ tau w], m_1..m_(n-1)); returns the RF Gram."""
    t = TAU * _c(a)
    lam = _c(T) * t + _c(2) * t * t + _c(-1) * t * t * t
    b = [_c(3 - i) * t + _c(i) * t * t for i in range(1, n)]
    G1 = [[_c((-1 if i == j else 0) + (F(1, 2) if i + j == 3 else 0)) + _c((i + j) % 3) * t for j in range(1, n)]
          for i in range(1, n)]
    G = [[None] * n for _ in range(n)]
    G[0][0] = lam
    for i in range(1, n):
        G[0][i] = G[i][0] = b[i - 1]
        for j in range(1, n):
            G[i][j] = G1[i - 1][j - 1]
    if ext:   # k -> k + tau w, w = m_1 - m_2
        w = [RF.const(0)] + [_c(1 if i == 1 else (-1 if i == 2 else 0)) for i in range(1, n)]
        row = [G[0][j] + TAU * sum((w[i] * G[i][j] for i in range(1, n)), RF.const(0)) for j in range(n)]
        G[0] = row
        for j in range(n):
            G[j][0] = row[j]
        G[0][0] = row[0] + TAU * sum((w[i] * row[i] for i in range(1, n)), RF.const(0))
    if scale_k != 1:
        c = _c(scale_k)
        for j in range(n):
            G[0][j] = c * G[0][j]
            if j:
                G[j][0] = c * G[j][0]
        G[0][0] = c * G[0][0]
    return G


# slot of the dying covector k in the frame (k, m_1, ..., m_(n-1))
K_SLOT = 0


def non_adapted_basis(n):
    """Sample change of covector basis P = U L (unit upper times unit lower triangular, so invertible)."""
    U = [[F(1) if i == j else (F((i + 2 * j) % 3 - 1) if j > i else F(0)) for j in range(n)] for i in range(n)]
    L = [[F(1) if i == j else (F((2 * i + j) % 3 - 1) if j < i else F(0)) for j in range(n)] for i in range(n)]
    return [[sum((U[i][t] * L[t][j] for t in range(n)), F(0)) for j in range(n)] for i in range(n)]


def transversality(G):
    return G[0][0].deriv().eval(0)


def residue(G):
    C = GA.rf_mat_inverse(G)
    return [[(TAU * C[i][j]).eval(0) for j in range(len(G))] for i in range(len(G))]


def check_residue_is_inverse_transversality():
    premise("sheaf.invariant-form-t3")
    premise("sheaf.tameness")
    ok = True
    for n, T in MODELS:
        G = model(n, T)
        k = K_SLOT
        ok = ok and G[k][k].eval(0) == 0 and all(G[k][i].eval(0) == 0 and not G[k][i].is_zero()
                                                 for i in range(n) if i != k)
        Tm = transversality(G)
        ok = ok and Tm == T
        R = residue(G)
        ok = ok and R == [[(1 / Tm if (i, j) == (0, 0) else F(0)) for j in range(n)] for i in range(n)]
        # a non-adapted covector basis: kappa'_a = sum_b P_ba kappa_b
        P = non_adapted_basis(n)
        Gp = [[sum((_c(P[a][i]) * G[a][b] * _c(P[b][j]) for a in range(n) for b in range(n)), RF.const(0))
               for j in range(n)] for i in range(n)]
        kp = GA.field_solve(P, [F(1)] + [F(0)] * (n - 1))        # coordinates of k = kappa_0 in the new basis
        Rp = residue(Gp)
        ok = ok and Rp == [[kp[i] * kp[j] / T for j in range(n)] for i in range(n)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_residue_is_inverse_transversality"; return _tp_rv


def check_residue_weights():
    premise("sheaf.invariant-form-t3")
    premise("sheaf.tameness")
    ok = True
    for n, T in MODELS:
        G = model(n, T)
        base = residue(G)[0][0]
        ok = ok and transversality(model(n, T, ext=True)) == T
        ok = ok and residue(model(n, T, ext=True))[0][0] == base
        for c in C_SCALES:
            Gc = model(n, T, scale_k=c)
            ok = ok and transversality(Gc) == c * c * T
            rc = residue(Gc)[0][0]
            ok = ok and rc * c * c == base and rc != base         # (c k) (x) (c k) times 1/(c^2 T)
        for a in A_SCALES:
            Ga = model(n, T, a=1 / a)                             # the same metric in the parameter a tau
            ok = ok and residue(Ga)[0][0] == a * base
        ok = ok and base * T == 1
        for c in C_SCALES[:2]:
            Gj = model(n, T, scale_k=c, a=1 / (c * c))
            ok = ok and transversality(Gj) == T and residue(Gj)[0][0] == base
    _tp_rv = (ok); assert _tp_rv is not False, "check_residue_weights"; return _tp_rv


def check_partner_line_is_dual_to_dying_line():
    premise("sheaf.localised-transport")
    ok = True
    for mu, nu in ((F(2), F(3)), (F(-1), F(5))):
        # wall block (k, n0, ninf) of the ambient form
        blk = [[F(0), nu, mu], [nu, F(0), F(-1)], [mu, F(-1), F(0)]]
        kstar = F(1) / (2 * nu)
        ok = ok and 2 * blk[0][1] * kstar == 1
        for c in C_SCALES:
            x = F(1) / (2 * c * blk[0][1])                         # solve 2 h(c k, x n0) = 1
            ok = ok and x == kstar / c and blk[1][1] == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_partner_line_is_dual_to_dying_line"; return _tp_rv
