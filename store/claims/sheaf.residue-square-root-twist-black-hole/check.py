"""sheaf.residue-square-root-twist-black-hole: exact checks on the Schwarzschild boundary data.

Data: the Gram of W on the frame (rho, dt_PG, mu1, mu2) from Fact
sheaf.schwarzschild-degeneration-boundary-tame, G(r) = [[m^2 - r, -m], [-m, 1]] + diag(-1, -1),
taken for three masses m (2M = m^2), as matrices over the rational-function field in r (GA.RF).

(1) The residue. r G^{-1} is computed by exact inversion and equals
    -[[1, m], [m, m^2 - r]] + diag(-r, -r) identically, so lim_{r -> 0} r G^{-1} = -k (x) k with
    k = rho + m dt_PG, a rank-one matrix. For other defining functions tau (tau = 2r + r^2,
    tau = r/(1 + r)) the limit is -(dtau/dr)(0) k (x) k, which is the residue formula
    k (x) k / (delta(k (x) k)/dtau) of the general theorem with delta(k (x) k) = -dr.
(2) The transversality datum. g_k = G(k, k) = -r exactly, so delta(k (x) k) = dg_k|_E = -dr|_E is
    nowhere zero: an isomorphism L^2 -> N*_r E. Under k -> c k for three polynomial units c,
    g_{ck} = -c^2 r and delta scales by c(0)^2 (Lemma T3 (3)); the partner normalised by
    2 h(ck, k*') = 1 is k*' = k*/c(0), so delta(ck (x) ck) k*' (x) k*' is unchanged: the partner
    line transforms as L^*, a square root of the dual N_r E. The dying line on E is the Killing-time
    line: with dt_S = dt_PG + m/(m^2 - r) rho (clause (4) of the Fact), G(dt_S, rho) = 0 and
    k = m dt_S + r/(r - m^2) rho identically, whose rho-part vanishes at r = 0.
(3) The rescaled frame. On (rho, k/sqrt r, mu1, mu2), written in u = sqrt r, the Gram has
    G(rho, k/u) = -u and G(k/u, k/u) = -1 exactly, with limit diag(m^2, -1, -1, -1) at E.

Not checked: the invariant readings (which bundle is which) beyond the scaling laws above.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

MASSES = (F(1), F(2), F(3, 2))
UNITS = ([F(1), F(1)], [F(-2), F(0), F(3)], [F(1, 2), F(-5), F(0), F(1)])   # c(r) coefficient lists
TAUS = ([F(0), F(2), F(1)], None)       # tau = 2r + r^2; None marks tau = r/(1 + r)


def C(x):
    return GA.RF.const(F(x))


def gram_r(m, var):
    """G as RF matrix in the variable var standing for r."""
    Z = GA.RF0
    return [[C(m * m) - var, C(-m), Z, Z], [C(-m), GA.RF1, Z, Z],
            [Z, Z, C(-1), Z], [Z, Z, Z, C(-1)]]


def form(G, a, b):
    out = GA.RF0
    for i in range(4):
        for j in range(4):
            out = out + a[i] * G[i][j] * b[j]
    return out


def check_residue_is_minus_k_tensor_k():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    premise("sheaf.metrics-residue-square-root-twist")
    r = GA.RF.var()
    ok = True
    for m in MASSES:
        G = gram_r(m, r)
        ok = ok and GA.rf_mat_det(G).eqrf(-r)
        Gi = GA.rf_mat_inverse(G)
        rGi = [[r * e for e in row] for row in Gi]
        expect = [[C(-1), C(-m), GA.RF0, GA.RF0], [C(-m), r - C(m * m), GA.RF0, GA.RF0],
                  [GA.RF0, GA.RF0, -r, GA.RF0], [GA.RF0, GA.RF0, GA.RF0, -r]]
        ok = ok and all(rGi[i][j].eqrf(expect[i][j]) for i in range(4) for j in range(4))
        lim = [[e.eval(F(0)) for e in row] for row in rGi]
        k = [F(1), m, F(0), F(0)]
        ok = ok and lim == [[-k[i] * k[j] for j in range(4)] for i in range(4)]
        ok = ok and GA.mat_rank(lim) == 1
        # other defining functions: lim tau G^{-1} = -(dtau/dr)(0) k (x) k
        for t in TAUS:
            tau = GA.RF(t) if t is not None else r / (GA.RF1 + r)
            slope = tau.deriv().eval(F(0))
            ok = ok and slope == (2 if t is not None else 1)
            limt = [[(tau * e).eval(F(0)) for e in row] for row in Gi]
            ok = ok and limt == [[-slope * k[i] * k[j] for j in range(4)] for i in range(4)]
    GA.check("r G^{-1} -> -k (x) k, rank one, k = rho + m dt_PG; for tau the residue is -(dtau/dr) k (x) k", ok)
    return ok


def check_transversality_datum_and_scaling():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    premise("sheaf.invariant-form-t3")
    premise("sheaf.metrics-residue-square-root-twist")
    r = GA.RF.var()
    ok = True
    for m in MASSES:
        G = gram_r(m, r)
        k = [GA.RF1, C(m), GA.RF0, GA.RF0]
        gk = form(G, k, k)
        ok = ok and gk.eqrf(-r) and gk.deriv().eval(F(0)) == -1
        for cl in UNITS:
            c = GA.RF(cl)
            c0 = c.eval(F(0))
            ck = [c * x for x in k]
            gck = form(G, ck, ck)
            ok = ok and gck.eqrf(-(c * c * r))
            delta = gck.deriv().eval(F(0))
            ok = ok and delta == -c0 * c0
            # partner normalised by 2 h(ck, x k*) = 1, with 2 h(k, k*) = 1: x = 1/c(0)
            x = F(1) / c0
            ok = ok and delta * x * x == -1
        # Killing-time line: dt_S = dt_PG + m/(m^2 - r) rho
        a = C(m) / (C(m * m) - r)
        dts = [a, GA.RF1, GA.RF0, GA.RF0]
        rho = [GA.RF1, GA.RF0, GA.RF0, GA.RF0]
        ok = ok and form(G, dts, rho).is_zero()
        coef = r / (r - C(m * m))
        recomb = [C(m) * dts[i] + coef * rho[i] for i in range(4)]
        ok = ok and all(recomb[i].eqrf(k[i]) for i in range(4))
        ok = ok and coef.eval(F(0)) == 0 and (C(m) * dts[1]).eval(F(0)) == m
    GA.check("g_k = -r: delta(k (x) k) = -dr is an isomorphism, scales by c(0)^2, the partner by 1/c(0); "
             "on E the dying line is the Killing-time line", ok)
    return ok


def check_rescaled_frame_limit():
    premise("sheaf.schwarzschild-degeneration-boundary-tame")
    u = GA.RF.var()
    ok = True
    for m in MASSES:
        G = gram_r(m, u * u)
        rows = [[GA.RF1, GA.RF0, GA.RF0, GA.RF0],
                [GA.RF1 / u, C(m) / u, GA.RF0, GA.RF0],
                [GA.RF0, GA.RF0, GA.RF1, GA.RF0],
                [GA.RF0, GA.RF0, GA.RF0, GA.RF1]]
        H = [[form(G, rows[i], rows[j]) for j in range(4)] for i in range(4)]
        ok = ok and H[0][1].eqrf(-u) and H[1][1].eqrf(C(-1)) and H[0][0].eqrf(C(m * m) - u * u)
        lim = [[e.eval(F(0)) for e in row] for row in H]
        ok = ok and lim == [[m * m, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]]
        ok = ok and GA.congruence_signature(lim) == (1, 3, 0)
    GA.check("on (rho, k/sqrt r, mu1, mu2): G(rho, k/u) = -u, G(k/u, k/u) = -1, limit diag(m^2, -1, -1, -1)", ok)
    return ok
