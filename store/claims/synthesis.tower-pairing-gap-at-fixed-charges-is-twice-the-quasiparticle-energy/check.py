"""synthesis.tower-pairing-gap-at-fixed-charges-is-twice-the-quasiparticle-energy: exact checks.

The stored pairing element of the tower, H_4 = sum_b K(n_a + n_c) - G P* P with P = sum_b w_a w_c over n_b blocks
(field-theory.composite-scalars-mean-field-level), on the Fock space of its 2 n_b tower modes, built with GA's
exterior model of the CAR (creation = wedge, annihilation = contraction; the tower planes generate the CAR,
field-theory.imported-tower-limit). Mode 2b is a_b, mode 2b + 1 is c_b.
(1) Closed spectrum: in every sector of fixed (N_a, N_c), with s_a blocks holding a alone, s_c holding c alone,
    p pairs on the remaining Omega = n_b - s_a - s_c blocks and quasi-spin j (Omega/2, Omega/2 - 1, ...),
    E = K(2p + s_a + s_c) - G (j + m)(j - m + 1), m = p - Omega/2. Certified by: the product of (H - E) over the
    predicted values is zero on the sector (spectrum inside the predicted set) and each predicted value has an
    eigenvector (the product over the other values is nonzero).
(2) Gap at fixed charges: for N_a = N_c = n, 1 <= n <= n_b - 1, the two lowest levels differ by exactly G n_b.
(3) Mean field: the one-shell mean-field energy n_b(K - E) + Delta^2/G, E^2 = K^2 + Delta^2, is stationary exactly
    at E = G n_b/2 and convex there, so the exact gap G n_b equals 2E = 2 sqrt(K^2 + m^2) >= 2m, = 2m at K = 0.
(4) Record: twice the stored top mass exceeds the stored Higgs mass; the tree value M_Z of the D-term action and
    the measured m_h both bound a single constituent's mass below m_t.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise, quantity

SAMPLES = [(2, F(3), F(1)), (2, F(3), F(4)), (2, F(1, 2), F(5, 3)), (2, F(0), F(1)),
           (3, F(3), F(1)), (3, F(3), F(4)), (3, F(1, 2), F(5, 3)), (3, F(0), F(1))]
# Above-threshold mean-field samples (n_b, K, G) with E = G n_b/2 > K and Delta^2 = E^2 - K^2.
MF = [(3, F(3), F(10, 3)), (4, F(3), F(5, 2)), (24, F(3), F(5, 12)), (2, F(0), F(7))]


def _add_into(out, x, c):
    for k, v in x.items():
        out[k] = out.get(k, F(0)) + c * v


def _ann(i, st, m):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(m)], st)


def _h4(nb, K, G, st):
    m = 2 * nb
    out = {}
    for i in range(m):
        _add_into(out, GA.ext_wedge(i, _ann(i, st, m)), K)
    pst = {}
    for b in range(nb):
        _add_into(pst, _ann(2 * b, _ann(2 * b + 1, st, m), m), F(1))
    ppst = {}
    for b in range(nb):
        _add_into(ppst, GA.ext_wedge(2 * b + 1, GA.ext_wedge(2 * b, pst)), F(1))
    _add_into(out, ppst, -G)
    return {k: v for k, v in out.items() if v != 0}


def _sector_matrix(nb, K, G, na, nc):
    m = 2 * nb
    basis = [frozenset(S) for k in range(m + 1) for S in combinations(range(m), k)
             if sum(1 for j in S if j % 2 == 0) == na and sum(1 for j in S if j % 2 == 1) == nc]
    idx = {S: i for i, S in enumerate(basis)}
    M = [[F(0)] * len(basis) for _ in basis]
    for j, S in enumerate(basis):
        for T, v in _h4(nb, K, G, {S: F(1)}).items():
            M[idx[T]][j] += v
    return M


def _predicted(nb, K, G, na, nc):
    vals = set()
    for sa in range(nb + 1):
        for sc in range(nb + 1 - sa):
            p = na - sa
            if p < 0 or nc - sc != p or p > nb - sa - sc:
                continue
            om = nb - sa - sc
            for twoj in range(om, -1, -2):
                if abs(2 * p - om) > twoj:
                    continue
                j, mm = F(twoj, 2), F(2 * p - om, 2)
                vals.add(K * (2 * p + sa + sc) - G * (j + mm) * (j - mm + 1))
    return sorted(vals)


def _shift(M, e):
    return [[M[i][j] - (e if i == j else 0) for j in range(len(M))] for i in range(len(M))]


def _prod(M, vals):
    P = [[F(int(i == j)) for j in range(len(M))] for i in range(len(M))]
    for e in vals:
        P = GA.mat_mul(P, _shift(M, e))
    return P


def _zero(P):
    return all(x == 0 for r in P for x in r)


def check_closed_spectrum_on_floors():
    premise("field-theory.composite-scalars-mean-field-level")
    premise("field-theory.imported-tower-limit")
    ok = True
    for (nb, K, G) in SAMPLES:
        for na in range(nb + 1):
            for nc in range(nb + 1):
                M = _sector_matrix(nb, K, G, na, nc)
                vals = _predicted(nb, K, G, na, nc)
                ok = ok and len(vals) >= 1 and _zero(_prod(M, vals))
                for e in vals:
                    ok = ok and not _zero(_prod(M, [x for x in vals if x != e]))
        # the band of the stored element: n pairs, no blocked block, top quasi-spin
        for n in range(nb + 1):
            ok = ok and _predicted(nb, K, G, n, n)[0] == 2 * K * n - G * n * (nb - n + 1)
    GA.check("H_4 spectrum on n_b = 2, 3 floors is K(2p + s) - G(j + m)(j - m + 1) in every (N_a, N_c) sector", ok)
    return ok


def check_gap_at_fixed_charges_is_g_nb():
    premise("field-theory.composite-scalars-mean-field-level")
    premise("field-theory.how-close-tower-comes-ccr")
    premise("field-theory.imported-tower-limit")
    ok = True
    for (nb, K, G) in SAMPLES:
        for n in range(1, nb):
            vals = _predicted(nb, K, G, n, n)
            ok = ok and len(vals) >= 2 and vals[1] - vals[0] == G * nb
            M = _sector_matrix(nb, K, G, n, n)
            d = len(M)
            band = 2 * K * n - G * n * (nb - n + 1)
            # on the matrix itself, independently of the closed form: the stored band value and the band value
            # plus G n_b are eigenvalues (H - E singular), and H is real symmetric
            ok = ok and GA.mat_rank(_shift(M, band)) < d and GA.mat_rank(_shift(M, band + G * nb)) < d
            ok = ok and all(M[i][j] == M[j][i] for i in range(d) for j in range(d))
            ok = ok and not _zero(_prod(M, [x for x in vals if x != vals[1]]))
    GA.check("at N_a = N_c = n (0 < n < n_b) the lowest excitation is exactly G n_b above the band state", ok)
    return ok


def _isqrt(n):
    if n < 2:
        return n
    x, y = n, (n + 1) // 2
    while y < x:
        x, y = y, (y + n // y) // 2
    return x


def _fsqrt(q):
    r = F(_isqrt(q.numerator), _isqrt(q.denominator))
    return r if r * r == q else None


def check_mean_field_two_quasiparticle_energy():
    premise("field-theory.composite-scalars-mean-field-level")
    ok = True
    for (nb, K, G) in MF:
        E = G * nb / 2
        x = E * E - K * K                      # Delta^2 = m^2 at the stationary point
        ok = ok and x > 0 and E > K and G > 2 * K / nb
        # f(x) = nb (K - sqrt(K^2 + x)) + x/G; f'(x) = -nb/(2 sqrt(K^2 + x)) + 1/G; f''(x) = nb/(4 (K^2 + x)^(3/2))
        s = _fsqrt(K * K + x)
        ok = ok and s == E and -F(nb) / (2 * s) + 1 / G == 0 and F(nb) / (4 * s * s * s) > 0
        # exact gap G n_b equals 2E, and 2E >= 2m with equality iff K = 0
        m = _fsqrt(x)
        ok = ok and G * nb == 2 * E
        if m is not None:
            ok = ok and (2 * E == 2 * m) == (K == 0) and 2 * E >= 2 * m
    GA.check("mean-field stationary point E = G n_b/2 (convex), so the exact gap G n_b is 2E = 2 sqrt(K^2 + m^2)", ok)
    return ok


def check_constituent_bound_against_record():
    premise("synthesis.rung-field-d-term-action-and-tree-masses-on-the-lift-locus")
    mh = quantity("quantity.higgs-boson-mass")
    mt = quantity("quantity.top-quark-mass")
    mz = quantity("quantity.z-boson-mass")
    # constituent bounds m_f <= m_h/2 (measured) and m_f <= M_Z/2 (D-term tree value), pinned exactly,
    # both below m_t: 2 m_t = 345.14 GeV against m_h = 125.20 GeV and M_Z = 91.188 GeV
    ok = mh / 2 == F(313, 5) and mz / 2 == F(22797, 500) and 2 * mt == F(17257, 50)
    ok = ok and mt - mh / 2 == F(10997, 100) and mt - mz / 2 == F(15872, 125) and mh / 2 < mt and mz / 2 < mt
    GA.check("2 m_t exceeds both m_h and M_Z: a top-only tower composite is too heavy at this level", ok)
    return ok
