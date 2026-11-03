"""hawking.imported-s-wave-bosonic-sector: exact checks of both halves on finite windows.

Fermionic window on bitmask states (Jordan-Wigner signs), currents a_m = sum_i psi_i^dag psi_{i+m} (m > 0),
a_m^dag = sum_i psi_{i+m}^dag psi_i; weights w_k = kappa k with k = i - 3 on a 7-mode window.
Unconditional half.
(1) The exact finite-window identity [a_m, a_m^dag] = B_m - T_m (edge operators, Fact
    singularity.bosonisation-bridge-s-wave-sector (1)) on all 2^7 states for m = 1, 2, 3; hence the free-boson value m
    on edge-clean states.
(2) The bilinear subalgebra is invariant under the modular boost: [K, psi_i^dag psi_j] = (w_i - w_j) psi_i^dag psi_j
    for all i, j and every state, for the s-wave weights and also for non-affine weights (invariance of the
    bilinear span needs no affine law; the currents being weight vectors does, Fact
    singularity.bosonisation-bridge-s-wave-sector).
Conditional half, under (Q).
(3) The product Fermi-Dirac state (n_k = 1/(x^{-k} + 1), x = e^{-beta kappa}) is the Gibbs state of K, and its
    restriction to the current algebra is KMS: omega(a_m B) = x^{-m} omega(B a_m) on sample current products
    (an instance of Lemma hawking.kms-restricts-invariant-subalgebras).
(4) Bose-Einstein occupancy: the detailed-balance identity n_k - n_{k+m} = (x^{-m} - 1) n_{k+m}(1 - n_k) at sample
    x and k; on the window the density-matrix value of <a_m^dag a_m> equals the Wick sum sum n_{k+m}(1 - n_k); the
    window sums equal (edge numerator)/(x^{-m} - 1) exactly and approach m/(x^{-m} - 1) = m nbar(m kappa) from
    below within 2 m x^{K-m}/(1 - x); and nbar/(1 + nbar) = x^m (Bose-Einstein detailed balance).
"""
import GA
from fractions import Fraction as F

from tp_premise import premise

L7 = 7
OFF7 = 3
XQS = [F(1, 2), F(1, 3)]
KS = [20, 30]
WEIGHT_SETS = [[F(i - OFF7, 4) for i in range(L7)], [F((i - OFF7) ** 3) for i in range(L7)]]


def popcount(s):
    return bin(s).count("1")


def bilin(a, b, vec):
    out = {}
    for s, c in vec.items():
        if not (s >> b) & 1:
            continue
        sg = -1 if popcount(s & ((1 << b) - 1)) % 2 else 1
        s1 = s & ~(1 << b)
        if (s1 >> a) & 1:
            continue
        sg *= -1 if popcount(s1 & ((1 << a) - 1)) % 2 else 1
        s2 = s1 | (1 << a)
        out[s2] = out.get(s2, F(0)) + sg * c
    return {s: c for s, c in out.items() if c != 0}


def apply(pairs, vec, coef=None):
    out = {}
    for idx, (a, b) in enumerate(pairs):
        w = F(1) if coef is None else coef[idx]
        for s, c in bilin(a, b, vec).items():
            out[s] = out.get(s, F(0)) + w * c
    return {s: c for s, c in out.items() if c != 0}


def cur(m, dag=False):
    return [(i + m, i) for i in range(L7 - m)] if dag else [(i, i + m) for i in range(L7 - m)]


def vsub(u, v):
    out = dict(u)
    for s, c in v.items():
        out[s] = out.get(s, F(0)) - c
    return {s: c for s, c in out.items() if c != 0}


def gibbs(x):
    w = {}
    for s in range(1 << L7):
        p = F(1)
        for i in range(L7):
            if (s >> i) & 1:
                p *= x ** (i - OFF7)
        w[s] = p
    Z = sum(w.values())
    return {s: p / Z for s, p in w.items()}


def expect(rho, ops):
    tot = F(0)
    for s, p in rho.items():
        v = {s: F(1)}
        for op in ops:
            v = apply(op, v)
        tot += p * v.get(s, F(0))
    return tot


def check_edge_identity_on_the_window():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    ok = True
    for m in (1, 2, 3):
        bottom = [(k, k) for k in range(m)]
        top = [(k, k) for k in range(L7 - m, L7)]
        clean = 0
        for s in range(1 << L7):
            v = {s: F(1)}
            lhs = vsub(apply(cur(m), apply(cur(m, True), v)), apply(cur(m, True), apply(cur(m), v)))
            ok = ok and lhs == vsub(apply(bottom, v), apply(top, v))
            if all((s >> k) & 1 for k in range(m)) and not any((s >> k) & 1 for k in range(L7 - m, L7)):
                ok = ok and lhs == {s: F(m)}
                clean += 1
        ok = ok and clean == 2 ** (L7 - 2 * m)
    _tp_rv = (ok); assert _tp_rv is not False, "check_edge_identity_on_the_window"; return _tp_rv


def check_bilinear_subalgebra_invariant_under_boost():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    diag = [(i, i) for i in range(L7)]
    ok = True
    for weights, edge in zip(WEIGHT_SETS, (F(-3, 2), F(-54))):
        # hand value: psi_0^dag psi_6 on |mode 6 occupied> carries weight w_0 - w_6
        v6 = {1 << 6: F(1)}
        img = bilin(0, 6, v6)
        ok = ok and vsub(apply(diag, img, weights), bilin(0, 6, apply(diag, v6, weights))) == \
            {t: edge * c for t, c in img.items()}
        for i in range(L7):
            for j in range(L7):
                for s in range(1 << L7):
                    v = {s: F(1)}
                    lhs = vsub(apply(diag, bilin(i, j, v), weights), bilin(i, j, apply(diag, v, weights)))
                    ok = ok and lhs == {t: (weights[i] - weights[j]) * c for t, c in bilin(i, j, v).items() if i != j}
    _tp_rv = (ok); assert _tp_rv is not False, "check_bilinear_subalgebra_invariant_under_boost"; return _tp_rv


def check_restriction_to_currents_is_kms():
    premise("singularity.q-joint-quasi-freeness-s-wave")
    premise("hawking.kms-restricts-invariant-subalgebras")
    ok = True
    for x in XQS:
        rho = gibbs(x)
        nk = [1 / (x ** (-(i - OFF7)) + 1) for i in range(L7)]
        for s in range(1 << L7):
            p = F(1)
            for i in range(L7):
                p *= nk[i] if (s >> i) & 1 else 1 - nk[i]
            ok = ok and p == rho[s]
        for m in (1, 2):
            am, ad = cur(m), cur(m, True)
            for B in ([ad], [cur(1), cur(1, True)], [ad, am]):
                ok = ok and expect(rho, B + [am]) == x ** (-m) * expect(rho, [am] + B)
    _tp_rv = (ok); assert _tp_rv is not False, "check_restriction_to_currents_is_kms"; return _tp_rv


def check_bose_einstein_occupancy_of_the_currents():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    premise("singularity.q-joint-quasi-freeness-s-wave")
    ok = True
    for x in XQS:
        def n(k):
            return 1 / (x ** (-k) + 1)
        for m in (1, 2, 3):
            ok = ok and all(n(k) - n(k + m) == (x ** (-m) - 1) * n(k + m) * (1 - n(k)) for k in range(-4, 5))
            closed = F(m) / (x ** (-m) - 1)
            nbar = closed / m
            ok = ok and nbar / (1 + nbar) == x ** m
            for K in KS:
                S = sum(n(k + m) * (1 - n(k)) for k in range(-K, K - m + 1))
                edge = sum(n(k) for k in range(-K, -K + m)) - sum(n(k) for k in range(K - m + 1, K + 1))
                ok = ok and S == edge / (x ** (-m) - 1)
                ok = ok and 0 < closed - S <= 2 * m * x ** (K - m) / (1 - x)
        # density matrix against Wick on the 7-mode window
        rho = gibbs(x)
        for m in (1, 2):
            dm = expect(rho, [cur(m), cur(m, True)])
            wick = sum(n(i + m - OFF7) * (1 - n(i - OFF7)) for i in range(L7 - m))
            ok = ok and dm == wick
    _tp_rv = (ok); assert _tp_rv is not False, "check_bose_einstein_occupancy_of_the_currents"; return _tp_rv
