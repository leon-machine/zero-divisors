"""singularity.pinching-against-partial-trace-scope-coincidence: exact checks over Q(i).

(i) One mode. Global pure states on mode (x) partner whose Schmidt basis is the number basis,
Omega = a|00> + b|11> with Q(i) coefficients (phases included), and mixtures of such states: the
mode marginal tr_partner is diagonal, so the pinching E of the premise (P x P + (1-P) x (1-P)) fixes
it. Control: c|+0> + s|-1> (Schmidt basis not the number basis) has a marginal with coherence
(c^2 - s^2)/2 that E removes.
(ii) Many modes. Two thermofield pairs (R1, L1), (R2, L2) with one controlled-Z between L1 and L2
(the minimal scrambled instance of the transfer proposition): the partial trace over (R2, L2) leaves
on the two modes (R1, L1) the joint-number coherence c1 s1 gamma, gamma = c2^2 - s2^2 (nonzero);
E_N (complete joint dephasing) annihilates it and keeps both populations; the single-mode marginals
of tr_L rho and of E_N(tr_L rho) agree. Generally, marginal_k(E_N(x)) = E(marginal_k(x)) on every
matrix unit for N = 2, 3 modes, so on states with diagonal marginals the two maps agree mode by mode,
while tr_L and E_N differ as maps whenever a joint coherence is present.
"""
from fractions import Fraction as F

from GA import QI
from tp_premise import premise

SCHMIDT = [(QI(F(3, 5)), QI(F(4, 5))), (QI(F(4, 5)), QI(0, F(3, 5))),
           (QI(F(5, 13)) * QI(F(3, 5), F(4, 5)), QI(F(-12, 13)))]
PAIRS = [((F(3, 5), F(4, 5)), (F(4, 5), F(3, 5))), ((F(12, 13), F(5, 13)), (F(5, 13), F(12, 13)))]


def bit(b, k, n):
    return (b >> (n - 1 - k)) & 1


def dm(n, amps):
    D = 2 ** n
    rho = [[QI(0)] * D for _ in range(D)]
    for i, a in amps.items():
        for j, b in amps.items():
            rho[i][j] = rho[i][j] + QI(a) * QI(b).conj()
    return rho


def reduce(rho, keep, n):
    """Partial trace onto the modes in keep (ordered), dimension 2^len(keep)."""
    d = 2 ** len(keep)
    out = [[QI(0)] * d for _ in range(d)]
    rest = [t for t in range(n) if t not in keep]
    for b in range(2 ** n):
        for c in range(2 ** n):
            if all(bit(b, t, n) == bit(c, t, n) for t in rest):
                i = sum(bit(b, q, n) << (len(keep) - 1 - u) for u, q in enumerate(keep))
                j = sum(bit(c, q, n) << (len(keep) - 1 - u) for u, q in enumerate(keep))
                out[i][j] = out[i][j] + rho[b][c]
    return out


def pinch1(x):
    """E(x) = P x P + (1 - P) x (1 - P), P = v* v = diag(0, 1)."""
    P = [[QI(0), QI(0)], [QI(0), QI(1)]]
    Q = [[QI(1), QI(0)], [QI(0), QI(0)]]
    mm = lambda A, B: [[sum((A[i][t] * B[t][j] for t in range(2)), QI(0)) for j in range(2)] for i in range(2)]
    a, b = mm(mm(P, x), P), mm(mm(Q, x), Q)
    return [[a[i][j] + b[i][j] for j in range(2)] for i in range(2)]


def pinchN(x):
    return [[x[i][j] if i == j else QI(0) for j in range(len(x))] for i in range(len(x))]


def check_single_mode_partial_trace_equals_pinching():
    premise("singularity.descent-what-it-erases")
    mixed = None
    for a, b in SCHMIDT:
        assert a * a.conj() + b * b.conj() == 1
        rho = dm(2, {0b00: a, 0b11: b})
        mk = reduce(rho, [0], 2)
        assert mk[0][1] == 0 and pinch1(mk) == mk
        mixed = rho if mixed is None else [[F(1, 2) * mixed[i][j] + F(1, 2) * rho[i][j] for j in range(4)]
                                           for i in range(4)]
    mk = reduce(mixed, [0], 2)
    assert pinch1(mk) == mk and mk[0][1] == 0
    # control: c|+0> + s|-1> = (c|00> + c|10> + s|01> - s|11>)/sqrt2; the 1/sqrt2 squares away
    c, s = F(3, 5), F(4, 5)
    rho = dm(2, {0b00: c, 0b10: c, 0b01: s, 0b11: -s})
    rho = [[x * F(1, 2) for x in r] for r in rho]
    mk = reduce(rho, [0], 2)
    assert mk[0][1] == QI((c * c - s * s) / 2) and pinch1(mk) != mk


def scrambled_two_pairs(p1, p2):
    """Qubits R1, L1, R2, L2 = 0, 1, 2, 3; thermofield pairs, then a controlled-Z on (L1, L2)."""
    (c1, s1), (c2, s2) = p1, p2
    amps = {}
    for r1 in (0, 1):
        for r2 in (0, 1):
            m = (r1 << 3) | (r1 << 2) | (r2 << 1) | r2
            a = (s1 if r1 else c1) * (s2 if r2 else c2)
            amps[m] = -a if (r1 and r2) else a
    return dm(4, amps)


def check_many_modes_partial_trace_keeps_coherence_pinching_kills_it():
    premise("singularity.purity-correlation-transfer-recovery")
    premise("singularity.two-levels-finite-model")
    for p1, p2 in PAIRS:
        (c1, s1), (c2, s2) = p1, p2
        gamma = c2 * c2 - s2 * s2
        rho = scrambled_two_pairs(p1, p2)
        rR = reduce(rho, [0, 1], 4)                  # tr over (R2, L2)
        assert rR[0b00][0b11] == QI(c1 * s1 * gamma) and gamma != 0
        ER = pinchN(rR)
        assert ER[0b00][0b11] == 0 and ER != rR
        assert ER[0b00][0b00] == rR[0b00][0b00] == QI(c1 * c1) and ER[0b11][0b11] == QI(s1 * s1)
        for k in range(2):
            assert reduce(rR, [k], 2) == reduce(ER, [k], 2)
            assert reduce(rR, [k], 2)[0][1] == 0
        # unscrambled control: without the controlled-Z the coherence is c1 s1 (gamma -> 1)
        amps = {0b0000: c1 * c2, 0b0011: c1 * s2, 0b1100: s1 * c2, 0b1111: s1 * s2}
        assert reduce(dm(4, amps), [0, 1], 4)[0b00][0b11] == QI(c1 * s1)


def check_marginal_of_pinching_is_pinching_of_marginal():
    premise("singularity.descent-what-it-erases")
    count = 0
    for n in (2, 3):
        D = 2 ** n
        for b in range(D):
            for c in range(D):
                x = [[QI(0)] * D for _ in range(D)]
                x[b][c] = QI(1)
                for k in range(n):
                    assert reduce(pinchN(x), [k], n) == pinch1(reduce(x, [k], n))
                    count += 1
    assert count == 2 * 16 + 3 * 64
