"""singularity.unipotent-ray: exact checks in Gauge Theory Gravity.

Flat spacetime: Cl(1,3) in GA.py, signature (+,-,-,-), e_t = gamma_0, e_r = gamma_1. The PG gauge field
hb(a) = a - beta P(a), P(a) = (a . e_t) e_r, acting on background vectors. Maps on vectors are
computed with GA.dot and GA.mul; as 4 x 4 matrices (columns = images of the frame) with entries in
Q(beta) (GA.RF, beta an indeterminate) for the identities in beta.
(1) P^2 = 0: on every frame vector and on sample vectors (GA), and as a matrix.
(2) hb^{-1} = 1 + beta P: (1 - beta P)(1 + beta P) = 1 = (1 + beta P)(1 - beta P) over Q(beta), and on
    the frame at beta = 3/7, 1 (the horizon), 5/2, 100 with GA; det hb = 1 over Q(beta).
(3) The trajectory is a ray of unipotent maps: (hb - 1)^2 = 0 over Q(beta) with hb - 1 nonzero, and
    hb(beta_1) hb(beta_2) = hb(beta_1 + beta_2) for sample pairs (beta >= 0), the horizon beta = 1 among
    them.
"""
from fractions import Fraction as F

import GA

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
FRAME = [GA.gen(i) for i in range(4)]
SAMPLES = [GA.add(GA.scal(F(2), GA.gen(0)), GA.scal(F(-3, 4), GA.gen(1)), GA.gen(3)),
           GA.add(GA.scal(F(1, 5), GA.gen(0)), GA.scal(F(7), GA.gen(2)))]


def P(a):
    return GA.scal(GA.dot(a, ET, S13), ER)


def hb(a, beta):
    return GA.sub(a, GA.scal(beta, P(a)))


def hb_inv(a, beta):
    return GA.add(a, GA.scal(beta, P(a)))


def pmat():
    return [[GA.RF.const(P(FRAME[j]).get((i,), F(0))) for j in range(4)] for i in range(4)]


def ident():
    return [[GA.RF.const(F(1 if i == j else 0)) for j in range(4)] for i in range(4)]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(4)), GA.RF0) for j in range(4)] for i in range(4)]


def lin(A, B, c):
    return [[A[i][j] + c * B[i][j] for j in range(4)] for i in range(4)]


def is_id(A):
    return all(A[i][j].eqrf(GA.RF.const(F(1 if i == j else 0))) for i in range(4) for j in range(4))


def check_p_squares_to_zero():
    for a in FRAME + SAMPLES:
        assert GA.is_zero(P(P(a)))
    assert not GA.is_zero(P(ET))
    Pm = pmat()
    assert all(x.is_zero() for row in mm(Pm, Pm) for x in row)
    assert not all(x.is_zero() for row in Pm for x in row)
    return True


INV_BETAS = (F(3, 7), F(1), F(5, 2), F(100))


def check_closed_form_inverse_horizon_included():
    b = GA.RF.var()
    Pm, I = pmat(), ident()
    H, Hi = lin(I, Pm, -b), lin(I, Pm, b)
    assert is_id(mm(H, Hi)) and is_id(mm(Hi, H))
    assert GA.rf_mat_det(H).eqrf(GA.RF1)
    # By hand: P(e_t) = (e_t . e_t) e_r = e_r and P kills e_r, e_theta, e_phi, so hb differs from the identity
    # in exactly one entry, row e_r column e_t, equal to -beta (+beta in hb^{-1}); its trace is 4.
    off = [(i, j) for i in range(4) for j in range(4) if not (H[i][j] - I[i][j]).is_zero()]
    assert off == [(1, 0)]
    assert H[1][0].eqrf(-b) and Hi[1][0].eqrf(b)
    assert sum((H[i][i] for i in range(4)), GA.RF0).eqrf(GA.RF.const(F(4)))
    # the horizon beta = 1: hb(e_t) = e_t - e_r and hb^{-1}(e_t) = e_t + e_r, no division
    assert GA.eq(hb(ET, F(1)), {(0,): F(1), (1,): F(-1)})
    assert GA.eq(hb_inv(ET, F(1)), {(0,): F(1), (1,): F(1)})
    for beta in INV_BETAS:
        for a in FRAME + SAMPLES:
            assert GA.eq(hb_inv(hb(a, beta), beta), a) and GA.eq(hb(hb_inv(a, beta), beta), a)
    return True


# Sample pairs (beta_1, beta_2), beta >= 0, for hb(beta_1) hb(beta_2) = hb(beta_1 + beta_2).
RAY_PAIRS = ((F(1, 3), F(2)), (F(1), F(1)), (F(0), F(5, 7)))


def check_trajectory_is_unipotent_ray():
    b = GA.RF.var()
    Pm, I = pmat(), ident()
    N = lin(lin(I, Pm, -b), I, GA.RF.const(-1))
    assert all(x.is_zero() for row in mm(N, N) for x in row)
    assert not all(x.is_zero() for row in N for x in row)
    assert any(b1 == 1 for b1, _ in RAY_PAIRS)         # the horizon beta = 1 is among the samples
    for b1, b2 in RAY_PAIRS:
        for a in FRAME + SAMPLES:
            assert GA.eq(hb(hb(a, b2), b1), hb(a, b1 + b2))
    return True
