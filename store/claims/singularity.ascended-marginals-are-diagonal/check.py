"""singularity.ascended-marginals-are-diagonal: exact checks.

Boundary modes are realised by Jordan-Wigner on N = 2, 3, 4 modes: v_k = Z x ... x Z x E_12 x 1 x
... x 1, number basis |b>, total parity Gamma = diag((-1)^popcount(b)). (P) is evenness,
Gamma rho Gamma = rho (premise p-univalence).
(1) General case, by linearity: every even matrix unit E_bc (popcount(b) = popcount(c) mod 2) has
tr(E_bc v_k) = tr(E_bc v_k*) = 0 and a diagonal single-mode marginal at every k, for all N <= 4 and
all k. So omega(v_k) = omega(v_k*) = 0 and rho_k is diagonal for every even state, hence equals
E_k(rho_k) (partial trace and pinching coincide), and by the premise's descended form it is the
Gibbs matrix diag(1, x)/(1 + x) with x = (1 - p)/p, checked on sample even states (mixed, complex
coherences). The odd matrix units are exactly those that can carry omega(v_k) (control).
(2) Zero-weight mode: the Gibbs form id/2 requires p = 1/2; a sample even state has p != 1/2 at a
mode (p = 2771/12675), so it is diagonal there but not Gibbs for omega_k = 0.
(3) Parity protection as the special case: the finite-mode model's states (thermofield pairs
c_k|00> + s_k|11> with controlled-Z signs) are supported on configurations of even total
occupation, are even, and have diagonal marginals diag(c_k^2, s_k^2). A parity-mixed state has
marginal coherence 12/25 (control).
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

MODEL = [(F(3, 5), F(4, 5)), (F(4, 5), F(3, 5)), (F(5, 13), F(12, 13))]


def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def popcount(b):
    return bin(b).count("1")


def zeros(D):
    return [[QI(0)] * D for _ in range(D)]


def ket(n, amps):
    rho = zeros(2 ** n)
    for i, a in amps.items():
        for j, b in amps.items():
            rho[i][j] = rho[i][j] + QI(a) * QI(b).conj()
    return rho


def lower(n, k):
    """Jordan-Wigner v_k as a sparse map {column: (row, sign)}: v_k|b> = (-1)^{#occupied before k}|b - e_k>."""
    out = {}
    for b in range(2 ** n):
        if bit(b, k, n):
            sign = (-1) ** sum(bit(b, t, n) for t in range(k))
            out[b] = (b ^ (1 << (n - 1 - k)), sign)
    return out


def expect_lower(rho, n, k):
    """tr(rho v_k) = sum_b rho[b][row(b)] * sign."""
    return sum((rho[b][r] * s for b, (r, s) in lower(n, k).items()), QI(0))


def expect_raise(rho, n, k):
    return sum((rho[r][b] * s for b, (r, s) in lower(n, k).items()), QI(0))


def marginal(rho, k, n):
    out = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for b in range(2 ** n):
        for c in range(2 ** n):
            if all(bit(b, t, n) == bit(c, t, n) for t in range(n) if t != k):
                out[bit(b, k, n)][bit(c, k, n)] = out[bit(b, k, n)][bit(c, k, n)] + rho[b][c]
    return out


def is_even(rho):
    D = len(rho)
    return all(rho[b][c] == 0 for b in range(D) for c in range(D) if (popcount(b) + popcount(c)) % 2)


def even_sample(n):
    """A mixed even state with complex coherences: two even pure states mixed 1/3 : 2/3."""
    ev = [b for b in range(2 ** n) if popcount(b) % 2 == 0]
    if n == 2:
        a = ket(n, {ev[0]: F(3, 5), ev[1]: QI(0, F(4, 5))})
        b = ket(n, {ev[0]: F(5, 13), ev[1]: F(-12, 13)})
    else:
        a = ket(n, {ev[0]: F(1, 2), ev[1]: QI(0, F(1, 2)), ev[2]: F(1, 2), ev[-1]: F(-1, 2)})
        b = ket(n, {ev[0]: F(3, 5), ev[-1]: F(4, 5)})
    return [[a[i][j] * F(1, 3) + b[i][j] * F(2, 3) for j in range(2 ** n)] for i in range(2 ** n)]


def model_state(pairs):
    """Thermofield pairs (R_k, L_k) at qubits (2k, 2k+1), with a controlled-Z sign on the L's."""
    n = 2 * len(pairs)
    amps = {0: F(1)}
    for k, (c, s) in enumerate(pairs):
        new = {}
        for m, a in amps.items():
            new[m] = new.get(m, F(0)) + a * c
            m2 = m | (1 << (n - 1 - 2 * k)) | (1 << (n - 2 - 2 * k))
            new[m2] = new.get(m2, F(0)) + a * s
        amps = new
    cz = {m: (-a if bit(m, 1, n) and bit(m, 3, n) else a) for m, a in amps.items()}
    return n, cz


def check_even_units_have_zero_ladder_expectation_and_diagonal_marginals():
    premise("singularity.p-univalence")
    total = odd_carrying = 0
    for n in (2, 3, 4):
        D = 2 ** n
        for b in range(D):
            for c in range(D):
                Eu = zeros(D)
                Eu[b][c] = QI(1)
                for k in range(n):
                    vk, vks = expect_lower(Eu, n, k), expect_raise(Eu, n, k)
                    mk = marginal(Eu, k, n)
                    if (popcount(b) + popcount(c)) % 2 == 0:
                        assert vk == 0 and vks == 0 and mk[0][1] == 0 and mk[1][0] == 0
                        total += 1
                    elif vk != 0 or vks != 0:
                        odd_carrying += 1
    # even units x modes: n * D^2 / 2 per n; ladder-carrying odd units: 2 * n * D / 2 per n
    assert total == 2 * 8 + 3 * 32 + 4 * 128, total
    assert odd_carrying == 2 * 4 + 3 * 8 + 4 * 16, odd_carrying


def check_even_state_marginals_are_descended_gibbs():
    premise("singularity.p-univalence")
    premise("singularity.descended-form-state-independent")
    seen = 0
    for n in (2, 3, 4):
        rho = even_sample(n)
        assert is_even(rho) and sum((rho[i][i] for i in range(2 ** n)), QI(0)) == 1
        assert any(rho[i][j] != 0 for i in range(2 ** n) for j in range(2 ** n) if i != j)
        for k in range(n):
            assert expect_lower(rho, n, k) == 0 and expect_raise(rho, n, k) == 0
            mk = marginal(rho, k, n)
            assert mk[0][1] == 0 and mk[1][0] == 0
            p = mk[0][0].re
            x = (1 - p) / p
            assert mk[0][0] == 1 / (1 + x) and mk[1][1] == x / (1 + x)
            seen += 1
    assert seen == 9
    # zero-weight mode: the Gibbs form id/2 needs p = 1/2; mode 0 of the 2-mode sample has
    # p = (1/3)(9/25) + (2/3)(25/169), by hand from the two pure components
    m0 = marginal(even_sample(2), 0, 2)
    assert m0[0][0] == F(1, 3) * F(9, 25) + F(2, 3) * F(25, 169) and m0[0][0] != F(1, 2)


def check_parity_protection_is_special_case():
    premise("singularity.p-univalence")
    for pairs in (MODEL[:2], MODEL):
        n, amps = model_state(pairs)
        assert all(popcount(m) % 2 == 0 for m in amps)
        rho = ket(n, amps)
        assert is_even(rho)
        for k in range(n):
            mk = marginal(rho, k, n)
            c, s = pairs[k // 2]
            assert mk == [[QI(c * c), QI(0)], [QI(0), QI(s * s)]]
            assert expect_lower(rho, n, k) == 0
    # control: (3/5)|000> + (4/5)|001> is parity mixed and its third marginal carries coherence 12/25
    rho = ket(3, {0b000: F(3, 5), 0b001: F(4, 5)})
    assert not is_even(rho) and marginal(rho, 2, 3)[0][1] == F(12, 25)
    assert expect_lower(rho, 3, 2) == F(12, 25)
