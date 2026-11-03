"""singularity.bosonisation-bridge-s-wave-sector: exact checks.

Finite window W = {-5, ..., 4} of fermion sites, states = sets of occupied sites (sign by sorted order), sea =
the negative sites occupied. a_m = sum_{k, k+m in W} psi_k^dagger psi_{k+m} (m != 0; no normal-ordering
constant is needed for m != 0). B_m, T_m = number operators of the bottom and top m sites.
(1) Current algebra: on all 252 charge-zero states and for m = 1, 2, 3, [a_m, a_{-m}] = B_m - T_m (the edge
    operator identity; B_m - T_m - m vanishes on bulk states, so there [a_m, a_{-m}] = m); for m + n != 0
    (m, n in {+-1, +-2, 3}) [a_m, a_n] = 0 on the 6 bulk states (bottom three sites full, top three empty);
    a_m annihilates the sea for m > 0, and a_{-m} is the transpose of a_m on the charge-zero basis.
(2) KMS restriction: with H = sum_k omega_k N_k, [H, a_m] = -kappa m a_m on every charge-zero state for the
    linear weights omega_k = kappa k (kappa = 1, 3/2), so each current is a weight vector; for omega_k = k^2
    the commutator is not a multiple of a_m. For the window Gibbs state (product, n_k = x^k/(1 + x^k),
    x = e^{-beta kappa}) the KMS identity of the restricted flow gives
    <a_{-m} a_m> = x^m/(1 - x^m) <B_m - T_m>, checked exactly with <a_{-m} a_m> = sum n_{k+m}(1 - n_k)
    (x = 1/2, 2/3; m = 1, 2, 3).
(3) Planck factor: detailed balance h_k = x^{-m} g_k and g_k - h_k = n_{k+m} - n_k as rational-function
    identities in x; the exact finite identity S_K (1 - x^{-m}) = T_K for S_K = sum_{|k| <= K} g_k with
    the boundary sum T_K; and |S_K - m x^m/(1 - x^m)| <= 2m x^(K-m+1)/(x^{-m} - 1) at K = 30, so the infinite
    sum is m/(e^{beta kappa m} - 1). Without (Q): a correlated even state with the same marginals shifts
    <n_{k+m}(1 - n_k)> by its connected correlator (-1/100), so no exact spectrum follows.
The charge-zero Fock isomorphism (cited) is not checked.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

W = list(range(-5, 5))
SEA = frozenset(k for k in W if k < 0)
CHARGE0 = [frozenset(c) for c in combinations(W, 5)]
BULK = [s for s in CHARGE0 if {-5, -4, -3} <= s and not ({2, 3, 4} & s)]


def apply(ops, sv):
    for kind, k in reversed(ops):
        out = {}
        for occ, amp in sv.items():
            if (kind == 'c') == (k in occ):
                continue
            sign = (-1) ** sum(1 for j in occ if j < k)
            new = occ | {k} if kind == 'c' else occ - {k}
            out[new] = out.get(new, F(0)) + sign * amp
        sv = {o: a for o, a in out.items() if a != 0}
    return sv


def add(*terms):
    out = {}
    for sg, d in terms:
        for k, v in d.items():
            out[k] = out.get(k, F(0)) + sg * v
    return {k: v for k, v in out.items() if v != 0}


def cur(m, sv):
    return add(*[(1, apply([('c', k), ('a', k + m)], sv)) for k in W if k + m in W])


def num(sites, sv):
    return {o: a * sum(1 for j in sites if j in o) for o, a in sv.items() if any(j in o for j in sites)}


def comm(m, n, sv):
    return add((1, cur(m, cur(n, sv))), (-1, cur(n, cur(m, sv))))


def check_current_algebra_with_edge_operator():
    premise("singularity.modular-structure-completed-pair")
    ok = len(CHARGE0) == 252 and len(BULK) == 6
    for m in (1, 2, 3):
        bottom, top = W[:m], W[-m:]
        for s in CHARGE0:
            sv = {s: F(1)}
            ok = ok and comm(m, -m, sv) == add((1, num(bottom, sv)), (-1, num(top, sv)))
        for s in BULK:
            ok = ok and comm(m, -m, {s: F(1)}) == {s: F(m)}
        ok = ok and cur(m, {SEA: F(1)}) == {}
        # a_{-m} = a_m^T on the charge-zero basis
        for s in CHARGE0[:60]:
            for t, c in cur(m, {s: F(1)}).items():
                ok = ok and cur(-m, {t: F(1)}).get(s, F(0)) == c
    for (m, n) in [(1, 1), (1, -2), (2, -1), (-1, -2), (3, -1), (2, 1)]:
        for s in BULK:
            ok = ok and comm(m, n, {s: F(1)}) == {}
    _tp_rv = (ok); assert _tp_rv is not False, "check_current_algebra_with_edge_operator"; return _tp_rv


def ket(s):
    return {s: F(1)}


# Weight-vector samples: two kappa, three m, every seventh charge-zero state.
KAPPAS = (F(1), F(3, 2))
M_WEIGHT = (1, 2, -1)
STATE_SAMPLE = CHARGE0[::7]
# Current used in the omega_k = k^2 control.
CONTROL_M = 1
# KMS samples: x = e^{-beta kappa} and m.
X_KMS = (F(1, 2), F(2, 3))
M_KMS = (1, 2, 3)


def check_currents_are_weight_vectors_and_kms_restricts():
    premise("singularity.modular-structure-completed-pair")
    premise("singularity.q-joint-quasi-freeness-s-wave")
    ok = True
    for kappa in KAPPAS:
        for m in M_WEIGHT:
            for s in STATE_SAMPLE:
                sv = ket(s)
                am = cur(m, sv)
                H_am = {o: a * sum(kappa * j for j in o) for o, a in am.items()}
                am_H = {o: a * sum(kappa * j for j in s) for o, a in am.items()}
                ok = ok and add((1, H_am), (-1, am_H)) == {o: -kappa * m * a for o, a in am.items()}
    # control, omega_k = k^2: the hop k + m -> k picks up k^2 - (k + m)^2 = -m (2k + m), which depends on k,
    # so [H, a_m] is not a multiple of a_m
    m = CONTROL_M
    ratios = set()
    for s in STATE_SAMPLE:
        am = cur(m, ket(s))
        H_am = {o: a * sum(j * j for j in o) for o, a in am.items()}
        am_H = {o: a * sum(j * j for j in s) for o, a in am.items()}
        lhs = add((1, H_am), (-1, am_H))
        created = {o: min(o - s) for o in am}
        ok = ok and lhs == {o: -m * (2 * created[o] + m) * a for o, a in am.items()}
        ratios |= {lhs[o] / a for o, a in am.items()}
    ok = ok and max(ratios) > min(ratios)
    for x in X_KMS:
        n = {k: x ** k / (1 + x ** k) for k in W}
        ok = ok and n[0] == F(1, 2)                  # zero chemical potential: half filling at k = 0
        for m in M_KMS:
            lhs = sum(n[k + m] * (1 - n[k]) for k in W if k + m in W)
            edge = sum(n[k] for k in W[:m]) - sum(n[k] for k in W[-m:])
            ok = ok and lhs == x ** m / (1 - x ** m) * edge
    _tp_rv = (ok); assert _tp_rv is not False, "check_currents_are_weight_vectors_and_kms_restricts"; return _tp_rv


def check_planck_factor_and_role_of_q():
    premise("singularity.q-joint-quasi-freeness-s-wave")
    ok = True
    xv = GA.RF.var()
    one = GA.RF.const(1)

    def nk(k):
        if k >= 0:
            p = GA.RF([F(0)] * k + [F(1)])
            return p / (one + p)
        p = GA.RF([F(0)] * (-k) + [F(1)])
        return one / (one + p)
    for m in (1, 2):
        xm = GA.RF([F(0)] * m + [F(1)])
        for k in (-4, -1, 0, 3):
            gk = nk(k + m) * (one - nk(k))
            hk = nk(k) * (one - nk(k + m))
            ok = ok and hk.eqrf(gk / xm) and (gk - hk).eqrf(nk(k + m) - nk(k))
    for x in (F(1, 2), F(2, 3)):
        def n(k):
            return x ** k / (1 + x ** k)
        for m in (1, 2, 3):
            K = 30
            S = sum(n(k + m) * (1 - n(k)) for k in range(-K, K + 1))
            T = sum(n(j) for j in range(K + 1, K + m + 1)) - sum(n(j) for j in range(-K, -K + m))
            ok = ok and S * (1 - x ** (-m)) == T
            planck = m * x ** m / (1 - x ** m)
            bound = 2 * m * x ** (K - m + 1) / (x ** (-m) - 1)
            ok = ok and abs(S - planck) <= bound and S != planck
    # without (Q): correlated even state with the same marginals
    n1 = n2 = F(9, 25)
    eps = F(1, 100)
    pp = [(1 - n1) * (1 - n2), (1 - n1) * n2, n1 * (1 - n2), n1 * n2]        # basis (n_k, n_{k+m})
    qq = [pp[0] + eps, pp[1] - eps, pp[2] - eps, pp[3] + eps]
    ok = ok and qq[2] + qq[3] == n1 and qq[1] + qq[3] == n2 and all(v > 0 for v in qq)
    summand_p = pp[1]                     # n_{k+m} = 1 and n_k = 0
    summand_q = qq[1]
    ok = ok and summand_p == n2 * (1 - n1) and summand_q - summand_p == -eps
    _tp_rv = (ok); assert _tp_rv is not False, "check_planck_factor_and_role_of_q"; return _tp_rv
