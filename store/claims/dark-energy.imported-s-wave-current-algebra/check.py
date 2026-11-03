"""dark-energy.imported-s-wave-current-algebra: exact checks of the finite-window content of this imported Fact.

Fermionic window on bitmask states, mode index i = 0..L-1 with Jordan-Wigner signs, currents
a_m = sum_i psi_i^dag psi_{i+m} (m > 0, lowering the weight by m kappa), a_m^dag = sum_i psi_{i+m}^dag psi_i.
(1) Current algebra with the edge split (Proposition hawking.current-commutator-exactly-edge-split): on all
    2^7 states of a 7-mode window, [a_m, a_m^dag] = B_m - T_m (bottom m minus top m number operators) for
    m = 1, 2, 3, so it acts as the scalar m on edge-clean states, and [a_m, a_m'] = 0 for m != m'.
(2) Modular invariance: with the s-wave weights w_k = kappa k (k = i - 3, sea level at k = 0) and
    K = sum_k w_k N_k, [K, a_m] = -m kappa a_m on every state; control: for the non-affine weights k^2 the current
    a_1 is not a weight vector.
(3) Under (Q) (Premise singularity.q-joint-quasi-freeness-s-wave): the quasi-free (product Fermi-Dirac) state
    with n_k = 1/(x^{-k} + 1), x = e^{-beta kappa} = 1/2, equals e^{-beta K}/Z state by state, and its
    restriction to the currents is KMS: omega(a_m B) = x^{-m} omega(B a_m) for B in {a_m^dag, a_m'^dag a_m',
    a_m a_m^dag}, m = 1, 2. Without (Q): a state with the same thermal single-mode marginals and one connected
    two-mode correlation fails the KMS identity on a current pair.
(4) Charge-zero sector and the bosonic Fock space (the boson-fermion correspondence, cited to Pressley and Segal):
    on an 8-mode window with the sea filled below k = 0, the charge-zero states of energy level E <= 4 number
    p(E) = 1, 1, 2, 3, 5, and the vectors a_m^dag-monomials a_{-l1} ... a_{-lr}|sea> over the partitions l of E
    span that level (rank p(E)).
Not checked: the completed (infinite) limit itself and the modular invariance of the whole current sector beyond
its weight-vector form.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

L7 = 7
OFF7 = 3
L8 = 8
SEA8 = 0b00001111
XQ = F(1, 2)
KAPPA = F(1, 3)
MS = (1, 2, 3)
CROSS = ((1, 2), (1, 3), (2, 3))
EPS = F(1, 50)
SQW = [F((i - OFF7) ** 2) for i in range(L7)]


def popcount(s):
    return bin(s).count("1")


def bilin(a, b, vec):
    """psi_a^dag psi_b on a dict state."""
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


def cur(m, L, dag=False):
    return [(i + m, i) for i in range(L - m)] if dag else [(i, i + m) for i in range(L - m)]


def vsub(u, v):
    out = dict(u)
    for s, c in v.items():
        out[s] = out.get(s, F(0)) - c
    return {s: c for s, c in out.items() if c != 0}


def comm(p1, p2, vec):
    return vsub(apply(p1, apply(p2, vec)), apply(p2, apply(p1, vec)))


def gibbs_weight(s, L, off, x):
    w = F(1)
    for i in range(L):
        if (s >> i) & 1:
            w *= x ** (i - off)
    return w


def expect(rho, ops_right_to_left, L):
    """sum_s rho(s) <s| O_1 ... O_r |s> for a diagonal rho; ops given as lists of bilinear pairs."""
    tot = F(0)
    for s, p in rho.items():
        v = {s: F(1)}
        for op in ops_right_to_left:
            v = apply(op, v)
        tot += p * v.get(s, F(0))
    return tot


def check_current_algebra_with_edge_split():
    premise("hawking.current-commutator-exactly-edge-split")
    ok = True
    for m in MS:
        bottom = [(k, k) for k in range(m)]
        top = [(k, k) for k in range(L7 - m, L7)]
        clean = 0
        for s in range(1 << L7):
            v = {s: F(1)}
            lhs = comm(cur(m, L7), cur(m, L7, True), v)
            ok = ok and lhs == vsub(apply(bottom, v), apply(top, v))
            if all((s >> k) & 1 for k in range(m)) and not any((s >> k) & 1 for k in range(L7 - m, L7)):
                ok = ok and lhs == {s: F(m)}
                clean += 1
        ok = ok and clean == 2 ** (L7 - 2 * m)
    for m, mp in CROSS:
        ok = ok and all(comm(cur(m, L7), cur(mp, L7), {s: F(1)}) == {} for s in range(1 << L7))
    _tp_rv = (ok); assert _tp_rv is not False, "check_current_algebra_with_edge_split"; return _tp_rv


def check_currents_are_weight_vectors_of_the_boost():
    premise("singularity.bosonisation-bridge-s-wave-sector")
    diag = [(i, i) for i in range(L7)]
    lin = [KAPPA * (i - OFF7) for i in range(L7)]
    ok = True
    for m in MS:
        for s in range(1 << L7):
            v = {s: F(1)}
            Kam = apply(diag, apply(cur(m, L7), v), lin)
            amK = apply(cur(m, L7), apply(diag, v, lin))
            # weight -m kappa, kappa = 1/3
            ok = ok and vsub(Kam, amK) == {t: F(-1, 3) * m * c for t, c in apply(cur(m, L7), v).items()}
    # control, non-affine weights k^2: the summands psi_k^dag psi_{k+1} of a_1 carry the weights
    # k^2 - (k+1)^2 = -(2k+1), k = -3..2, so a_1 is not a weight vector
    ratios = set()
    for s in range(1 << L7):
        v = {s: F(1)}
        Kq = vsub(apply(diag, apply(cur(1, L7), v), SQW), apply(cur(1, L7), apply(diag, v, SQW)))
        img = apply(cur(1, L7), v)
        ok = ok and set(Kq) <= set(img)
        ratios |= {Kq.get(t, F(0)) / c for t, c in img.items()}
    _tp_rv = (ok and sorted(ratios) == [-5, -3, -1, 1, 3, 5]); assert _tp_rv is not False, "check_currents_are_weight_vectors_of_the_boost"; return _tp_rv


def check_quasi_free_state_restricts_to_kms_on_currents():
    premise("singularity.q-joint-quasi-freeness-s-wave")
    premise("singularity.bosonisation-bridge-s-wave-sector")
    ok = True
    Z = sum(gibbs_weight(s, L7, OFF7, XQ) for s in range(1 << L7))
    rho = {s: gibbs_weight(s, L7, OFF7, XQ) / Z for s in range(1 << L7)}
    nk = [1 / (XQ ** (-(i - OFF7)) + 1) for i in range(L7)]
    for s in range(1 << L7):
        prod = F(1)
        for i in range(L7):
            prod *= nk[i] if (s >> i) & 1 else 1 - nk[i]
        ok = ok and prod == rho[s]
    for m in MS[:2]:
        am, ad = cur(m, L7), cur(m, L7, True)
        for B in ([ad], [cur(3 - m, L7), cur(3 - m, L7, True)], [ad, am]):
            # omega(a_m B) and omega(B a_m); ops listed right to left
            lhs = expect(rho, B + [am], L7)
            rhs = expect(rho, [am] + B, L7)
            ok = ok and lhs == XQ ** (-m) * rhs
    # without (Q): same marginals, one connected correlation between modes 2 and 3 -> KMS fails
    eps = EPS
    rho2 = dict(rho)
    for s in range(1 << L7):
        b2, b3 = (s >> 2) & 1, (s >> 3) & 1
        base = F(1)
        for i in range(L7):
            if i in (2, 3):
                continue
            base *= nk[i] if (s >> i) & 1 else 1 - nk[i]
        rho2[s] = rho[s] + eps * base * (1 if b2 == b3 else -1)
    marg_ok = all(sum(p for s, p in rho2.items() if (s >> i) & 1) == nk[i] for i in range(L7))
    ok = ok and marg_ok
    am, ad = cur(1, L7), cur(1, L7, True)
    ok = ok and expect(rho2, [ad, am], L7) != XQ ** (-1) * expect(rho2, [am, ad], L7)
    _tp_rv = (ok); assert _tp_rv is not False, "check_quasi_free_state_restricts_to_kms_on_currents"; return _tp_rv


def check_charge_zero_levels_are_bosonic_fock_space():
    premise("dark-energy.imported-s-wave-current-algebra-external")
    premise("singularity.bosonisation-bridge-s-wave-sector")
    ok = True
    weights = [i - 4 for i in range(L8)]
    sea_e = sum(weights[i] for i in range(L8) if (SEA8 >> i) & 1)
    expected = [1, 1, 2, 3, 5]
    for E in range(5):
        level = [s for s in range(1 << L8) if popcount(s) == 4 and
                 sum(weights[i] for i in range(L8) if (s >> i) & 1) - sea_e == E]
        ok = ok and len(level) == expected[E]
        parts = []

        def gen(rest, mx, acc):
            if rest == 0:
                parts.append(acc)
                return
            for k in range(min(rest, mx), 0, -1):
                gen(rest - k, k, acc + [k])
        gen(E, E, [])
        ok = ok and len(parts) == expected[E]
        vecs = []
        for lam in parts:
            v = {SEA8: F(1)}
            for k in lam:
                v = apply(cur(k, L8, True), v)
            ok = ok and set(v) <= set(level)
            vecs.append([v.get(s, F(0)) for s in level])
        ok = ok and GA.field_rank(vecs) == expected[E]
    _tp_rv = (ok); assert _tp_rv is not False, "check_charge_zero_levels_are_bosonic_fock_space"; return _tp_rv
