"""singularity.modular-descent: exact checks of the finite core.

Pair (x) partner = C^2 (x) C^2 (|ij> at 2i + j), G = N (x) 1 - 1 (x) N, K = sigma/2 = N - 1/2 on the
pair (premise: sigma = 2N - 1). States are built from rational t = tan theta with an optional unit
phase, Omega ~ |00> + t e^{i chi}|11> (normalised exactly as a density matrix).
(1) Hypotheses (i)-(iii) and the descent: for t = 3/4, 4/3, 1, 5/12 (beta > 0, < 0, = 0, > 0) the
state is pure, is fixed by e^{isG} at the exact unit-circle point (3 + 4i)/5, and is cyclic and
separating (orbit rank 4 under the pair factor); its partial trace over the partner is diagonal (so
it equals its pinching) and is KMS for Ad(e^{itK}) at the beta with e^{-beta} = t^2 = tan^2 theta,
on all matrix units; KMS at a different beta fails. The endpoint t = 0 (|00>) is not cyclic and
separating (rank 2): (iii) removes exactly the endpoints beta = +-infinity.
(2) The normalisation: with beta = 2 pi in rapidity and kappa = 1/(4M) (plane-rate premise),
T = kappa/(2 pi) = 1/(8 pi M), checked as an identity in (pi, M) at rational sample values; the
reduced matrix diag(1, y)/(1 + y) with y = e^{-omega/T} has occupancy y/(1 + y) = 1/(e^{omega/T} + 1),
and the thermofield reduction diag(c^2, s^2) is this matrix exactly when tan^2 theta = y.
(3) Sufficient, not necessary: c|01> + s|10> is pure, cyclic and separating, not invariant up to phase
under e^{isG} (violates (ii)), yet reduces to diag(c^2, s^2), thermal; c|+0> + s|-1> is pure, cyclic
and separating, violates (ii), and reduces to a matrix with coherence (c^2 - s^2)/2, while every KMS
state of the phase flow, at every beta (x = e^{-beta} kept as an indeterminate), has zero coherence.
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

U = QI(F(3, 5), F(4, 5))
TS = [(F(3, 4), QI(1)), (F(4, 3), QI(0, 1)), (F(1), QI(1)), (F(5, 12), QI(F(3, 5), F(-4, 5)))]


def dm(vec):
    nrm = sum((a * a.conj() for a in vec), QI(0))
    return [[vec[i] * vec[j].conj() / nrm for j in range(4)] for i in range(4)]


def act_pair(A, v):
    out = [QI(0)] * 4
    for i in range(2):
        for j in range(2):
            for k in range(2):
                out[2 * i + j] = out[2 * i + j] + A[i][k] * v[2 * k + j]
    return out


def units():
    return [[[QI(1) if (i, j) == (a, b) else QI(0) for j in range(2)] for i in range(2)]
            for a in range(2) for b in range(2)]


def reduce_pair(rho):
    return [[rho[2 * i][2 * j] + rho[2 * i + 1][2 * j + 1] for j in range(2)] for i in range(2)]


def kms(m, x):
    """omega(ab) = omega(b E a E^{-1}) on all matrix units, E = diag(1, x) (e^{-beta K} up to scale)."""
    E, Ei = [F(1), x], [F(1), 1 / x]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    lhs = m[d][a] if b == c else QI(0)
                    rhs = m[b][c] * E[a] * Ei[b] if d == a else QI(0)
                    if lhs != rhs:
                        return False
    return True


def invariant_up_to_phase(v):
    Gd = [0, -1, 1, 0]
    ph = {0: QI(1), -1: U.conj(), 1: U}
    w = [ph[Gd[i]] * v[i] for i in range(4)]
    return all(w[i] * v[j] == w[j] * v[i] for i in range(4) for j in range(4))


def check_invariant_cyclic_state_descends_to_kms_beta_free():
    premise("singularity.schmidt-forcing-proved-outright")
    premise("singularity.modular-theory-matrix-factor-proved-outright")
    premise("singularity.modular-structure-completed-pair")
    signs = []
    for t, ph in TS:
        v = [QI(1), QI(0), QI(0), ph * t]
        rho = dm(v)
        assert invariant_up_to_phase(v)
        assert GA.field_rank([act_pair(A, v) for A in units()]) == 4
        m = reduce_pair(rho)
        assert m[0][1] == 0 and m[1][0] == 0                      # diagonal: equals its pinching
        x = t * t
        assert m[1][1] / m[0][0] == x and kms(m, x) and not kms(m, x * F(2))
        signs.append((x < 1) - (x > 1))
    assert signs == [1, -1, 0, 1]                                 # beta > 0, < 0, = 0, > 0
    # the endpoint: |00> (t = 0) is invariant but not cyclic and separating
    assert GA.field_rank([act_pair(A, [QI(1), QI(0), QI(0), QI(0)]) for A in units()]) == 2


def check_hawking_temperature_and_fermi_dirac():
    premise("singularity.plane-rate")
    premise("singularity.r-regularity-fixed-locus")
    for p in (F(22, 7), F(3), F(355, 113)):                       # pi as an indeterminate, sampled
        for M in (F(1), F(5, 2), F(1, 3)):
            kappa = 1 / (4 * M)
            T = kappa / (2 * p)
            assert T == 1 / (8 * p * M)
            assert 2 * p / kappa == 8 * p * M                     # 2 pi of rapidity = 8 pi M of time
    for y in (F(9, 16), F(1, 3), F(25, 144)):                     # y = e^{-omega/T}
        Z = 1 + y
        occ = y / Z
        assert occ == 1 / (1 / y + 1)
        c2, s2 = 1 / Z, y / Z                                     # thermofield: tan^2 theta = y
        assert s2 / c2 == y and c2 + s2 == 1


def check_hypotheses_sufficient_not_necessary():
    premise("singularity.schmidt-forcing-proved-outright")
    c, s = F(3, 5), F(4, 5)
    # c|01> + s|10>: violates (ii) but descends thermally
    v = [QI(0), QI(c), QI(s), QI(0)]
    assert not invariant_up_to_phase(v)
    assert GA.field_rank([act_pair(A, v) for A in units()]) == 4
    m = reduce_pair(dm(v))
    assert m == [[QI(c * c), QI(0)], [QI(0), QI(s * s)]] and kms(m, s * s / (c * c))
    # c|+0> + s|-1> (times sqrt2): violates (ii) and does not descend thermally
    w = [QI(c), QI(s), QI(c), QI(-s)]
    assert not invariant_up_to_phase(w)
    assert GA.field_rank([act_pair(A, w) for A in units()]) == 4
    m = reduce_pair(dm(w))
    assert m[0][1] == QI((c * c - s * s) / 2) and m[0][0] == QI(F(1, 2))
    # every KMS state of the phase flow has zero coherence, for every beta: the constraint from
    # (a, b) = (E_00, E_01) reads rho_10 = (E_01 E E_00 E^{-1})-term = 0, independent of x
    x = GA.RF.var()
    E = [[GA.RF1, GA.RF0], [GA.RF0, x]]
    Ei = [[GA.RF1, GA.RF0], [GA.RF0, GA.RF1 / x]]
    E00 = [[GA.RF1, GA.RF0], [GA.RF0, GA.RF0]]
    E01 = [[GA.RF0, GA.RF1], [GA.RF0, GA.RF0]]

    def rmm(A, B):
        return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in range(2)] for i in range(2)]

    prod = rmm(rmm(rmm(E01, E), E00), Ei)
    assert all(z.is_zero() for r in prod for z in r)              # RHS vanishes: rho_10 = 0
    lhs = rmm(E00, E01)                                           # tr(rho E00 E01) = rho_10
    assert not lhs[0][1].is_zero()
