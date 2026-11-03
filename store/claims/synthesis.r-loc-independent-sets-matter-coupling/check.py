"""synthesis.r-loc-independent-sets-matter-coupling: exact checks.

Boltzmann factors are kept symbolic as rational functions of u = e^{-2 pi} (one unit of rapidity weight at
period 2 pi), with GA.RF.
(1) The model's local window: sheet-labelled modes with rapidity weights 1, 2, 3, state the quasi-free Gibbs state
at rapidity period 2 pi c with c = 2 (occupations u^{2w}/(1 + u^{2w})). It is diagonal (even, stationary under the
boost and under every number-diagonal generator) and KMS at period 4 pi; it is not KMS at 2 pi at any nonzero weight
(occupations differ as rational functions of u). A Killing window (weights -1, 0, 1) keeps the period-2 pi state.
(2) Clausius with temperature T_chi = s kappa / 2 pi (s = 1/c) on a thin pencil: with chi = -kappa lambda k,
theta = -lambda Ric(k,k), exact polynomial integration gives
delta Q - T_chi eta delta A = (kappa/2)(T(k,k) - (s eta / 2 pi) Ric(k,k)) lambda_0^2, tracked with 2 pi as a symbol.
(3) Polarisation: the map from symmetric tensors S to (S(k,k)) over twelve rational null vectors has rank 9 and
kernel spanned by g, so the null-null equation for all k is a tensor equation up to a multiple of g.
(4) Coupling read off the integrated defect: balancing its T(k,k) and Ric(k,k) coefficients gives Ric(k,k) = mu T(k,k),
mu = 8 pi G_cl, and G_cl = c at eta = 1/4 (2 pi kept as a rational symbol, so the result cannot use its value).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

U = GA.RF.var()        # u = e^{-2 pi}
ONE = GA.RF.const(1)


def upow(k):
    if k >= 0:
        r = ONE
        for _ in range(k):
            r = r * U
        return r
    r = ONE
    for _ in range(-k):
        r = r / U
    return r


def occ(w, c):
    """Occupation of a weight-w mode in the Gibbs state at rapidity period 2 pi c."""
    b = upow(c * w)
    return b / (ONE + b)


def kms_occ_ok(n_occ, w, c):
    """Single-mode KMS at period 2 pi c for weight w: n/(1-n) = u^{c w}."""
    return (n_occ / (ONE - n_occ)).eqrf(upow(c * w))


def check_local_window_fails_r_loc_only():
    premise("synthesis.boundary-mode-premises-finite-models")
    premise("synthesis.local-boost-temperature-is-local-regularity")
    c = 2
    ok = True
    for w in (1, 2, 3):
        n_w = occ(w, c)
        ok = ok and kms_occ_ok(n_w, w, c)            # KMS at period 4 pi
        ok = ok and not kms_occ_ok(n_w, w, 1)        # not KMS at period 2 pi: (R_loc) fails
        ok = ok and not n_w.eqrf(occ(w, 1))
    # explicit occupations: u^2/(1+u^2) at period 4 pi and u/(1+u) at 2 pi for weight 1
    ok = ok and occ(1, c).eqrf((U * U) / (ONE + U * U)) and occ(1, 1).eqrf(U / (ONE + U))
    ok = ok and occ(3, c).eqrf(upow(6) / (ONE + upow(6)))
    ok = ok and occ(-1, 1).eqrf(ONE / (ONE + U))
    # zero weight is the only exception (both periods give 1/2)
    ok = ok and occ(0, c).eqrf(occ(0, 1))
    # the Killing window keeps the store's period-2 pi state (weights -1, 0, 1 of the array)
    for w in (-1, 0, 1):
        ok = ok and kms_occ_ok(occ(w, 1), w, 1)
    # the product Gibbs state is diagonal in the number basis: even and stationary under
    # every number-diagonal generator; on three modes check the density diagonal is a product
    dens = {}
    for bits in range(8):
        p = ONE
        for j, w in enumerate((1, 2, 3)):
            nj = occ(w, c)
            p = p * (nj if (bits >> j) & 1 else (ONE - nj))
        dens[bits] = p
    total = GA.RF.const(0)
    for v in dens.values():
        total = total + v
    ok = ok and total.eqrf(ONE)
    GA.check("local window at period 4 pi: KMS there, not at 2 pi; Killing window unchanged", ok)
    return ok


def pint(p, a, b):
    """Integral of the polynomial p from a to b."""
    # antiderivative by hand: coefficients ascending
    anti = [F(0)] + [F(cf) / (k + 1) for k, cf in enumerate(p)]
    return GA.peval(anti, b) - GA.peval(anti, a)


def check_clausius_defect_with_temperature_factor():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    ok = True
    # symbols: Tkk, Rkk (values at p), kappa, eta, s, and P = 2 pi (kept as a rational stand-in symbol)
    for (Tkk, Rkk, kappa, eta, s, P, lam0) in ((F(3), F(5), F(1, 2), F(1, 4), F(1, 2), F(7), F(-1, 3)),
                                              (F(-2), F(9, 4), F(2), F(1, 4), F(1), F(11, 2), F(-2, 5)),
                                              (F(1, 7), F(-3), F(5, 3), F(2, 9), F(3, 4), F(13, 3), F(-1))):
        # chi = -kappa lambda k: delta Q = int_{lam0}^0 T(k,k) (-kappa lambda) d lambda
        dQ = pint([F(0), -kappa * Tkk], lam0, F(0))
        # theta = -lambda Ric(k,k): delta A = int_{lam0}^0 theta d lambda (per unit area)
        dA = pint([F(0), -Rkk], lam0, F(0))
        Tchi = s * kappa / P
        defect = dQ - Tchi * eta * dA
        ok = ok and defect == (kappa / 2) * (Tkk - (s * eta / P) * Rkk) * lam0 ** 2
        # the defect vanishes iff T(k,k) = (s eta / P) Ric(k,k)
        ok = ok and ((defect == 0) == (Tkk == (s * eta / P) * Rkk))
        if Tkk == 3:
            ok = ok and dQ == F(1, 12) and dA == F(5, 18) and defect == F(163, 2016)
    # at the balance point the defect vanishes, and only there
    Rb = F(8)
    Tb = F(1, 2) * F(1, 4) / F(7) * Rb
    dQb = pint([F(0), -F(1, 2) * Tb], F(-1, 3), F(0))
    dAb = pint([F(0), -Rb], F(-1, 3), F(0))
    ok = ok and dQb - F(1, 2) * F(1, 2) / F(7) * F(1, 4) * dAb == 0 and Tb == F(1, 7)
    GA.check("Clausius defect with T = s kappa/2pi is (kappa/2)(T - s eta Ric/2pi) lambda_0^2", ok)
    return ok


NULLS = [(1, 1, 0, 0), (1, -1, 0, 0), (1, 0, 1, 0), (1, 0, -1, 0), (1, 0, 0, 1), (1, 0, 0, -1),
         (5, 3, 4, 0), (5, 0, 3, 4), (5, 4, 0, 3), (3, 1, 2, 2), (3, -2, 1, 2), (9, 4, 4, 7)]
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]
G = [1, -1, -1, -1]


def check_polarisation_is_a_tensor_equation():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    ok = all(k[0] ** 2 == k[1] ** 2 + k[2] ** 2 + k[3] ** 2 for k in NULLS)
    rows = []
    for k in NULLS:
        rows.append([F(k[a] * k[b] * (1 if a == b else 2)) for (a, b) in PAIRS])
    rank = GA.field_rank(rows)
    # g lies in the kernel: g(k,k) = 0 for null k
    gvec = [F(G[a]) if a == b else F(0) for (a, b) in PAIRS]
    in_kernel = all(sum(r[i] * gvec[i] for i in range(10)) == 0 for r in rows)
    ok = ok and rank == 9 and in_kernel
    GA.check("S(k,k) = 0 for all null k forces S proportional to g (rank 9 of 10)", ok)
    return ok


def check_coupling_scales_with_period():
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    premise("synthesis.quarter-from-temperature")
    eta = F(1, 4)           # Killing calibration, made with the period-2 pi temperature
    P = F(13, 2)            # rational stand-in for 2 pi; the result must not depend on it
    kappa, lam0 = F(3, 5), F(-2, 7)
    ok = True
    for c in (1, 2, 3):
        s = F(1, c)
        Tchi = s * kappa / P

        def defect(Tkk, Rkk):
            dQ = pint([F(0), -kappa * Tkk], lam0, F(0))
            dA = pint([F(0), -Rkk], lam0, F(0))
            return dQ - Tchi * eta * dA
        a = defect(F(1), F(0))      # coefficient of T(k,k)
        b = defect(F(0), F(1))      # coefficient of Ric(k,k)
        ok = ok and a != 0 and b != 0
        mu = -a / b                 # balance: Ric(k,k) = mu T(k,k)
        # Einstein's null-null component: Ric(k,k) = 8 pi G_cl T(k,k), and 8 pi = 4 (2 pi)
        G_cl = mu / (4 * P)
        ok = ok and G_cl == c
    GA.check("G_cl read off the Clausius defect: G at period 2 pi, 2G at 4 pi, 3G at 6 pi", ok)
    return ok
