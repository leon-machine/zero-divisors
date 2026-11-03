"""angle.hop-sea-filled-pairing: exact checks.

Two fermionic modes in the Jordan-Wigner basis |n0 n1>, index n0 + 2 n1, |11> = a0^dag a1^dag |00>, as in the
check of angle.hop-across-cut, whose psi = 3/5|10> + 4/5|01> and H = 7 N0 - 12 (a0^dag a1 + a1^dag a0) are used.
V = (a1 + a1^dag) Gamma_0, Gamma_0 = (-1)^{N0}.
- V is symmetric and orthogonal (unitary and Hermitian), V^2 = 1; V a0 V = a0, V a1 V = a1^dag,
  V a1^dag V = a1, V a0^dag V = a0^dag.
(i) V psi = 4/5|00> + 3/5|11>, even, with left marginal diag(16/25, 9/25).
(ii) V H V^{-1} = 7 N0 - 12 (a0^dag a1^dag + a1 a0) entry by entry; the same eigenvalues 0, 7, 16, -9 on the
    image eigenbasis, so V psi is its unique ground state.
(iii) V (N0 + N1 - 1) V^{-1} = N0 - N1.
"""
from fractions import Fraction as F

import GA
import fock
from tp_premise import premise

DIM = 4


def zero():
    return [[F(0)] * DIM for _ in range(DIM)]


def ident():
    m = zero()
    for i in range(DIM):
        m[i][i] = F(1)
    return m


mm = GA.mat_mul                         # dense matrix product


def madd(*ms):
    return [[sum(m[i][j] for m in ms) for j in range(DIM)] for i in range(DIM)]


def msc(c, a):
    return [[F(c) * a[i][j] for j in range(DIM)] for i in range(DIM)]


def tr(a):
    return [[a[j][i] for j in range(DIM)] for i in range(DIM)]


def mv(a, v):
    return [sum(a[i][k] * v[k] for k in range(DIM)) for i in range(DIM)]


def ann(j):
    """a_j in the Jordan-Wigner basis (index n0 + 2 n1), dense: lib/fock.py in LSB order."""
    return fock.to_dense(fock.ann(j, 2), DIM)


A0, A1 = ann(0), ann(1)
C0, C1 = tr(A0), tr(A1)
N0, N1 = mm(C0, A0), mm(C1, A1)
G0 = madd(ident(), msc(-2, N0))
V = mm(madd(A1, C1), G0)
H = madd(msc(7, N0), msc(-12, madd(mm(C0, A1), mm(C1, A0))))
PSI = [F(0), F(3, 5), F(4, 5), F(0)]
UP = [F(0), F(4), F(-3), F(0)]


def check_v_is_the_particle_hole_automorphism():
    ok = V == tr(V) and mm(V, V) == ident()
    ok = ok and mm(mm(V, A0), V) == A0 and mm(mm(V, C0), V) == C0
    ok = ok and mm(mm(V, A1), V) == C1 and mm(mm(V, C1), V) == A1
    # the Majorana factor alone flips the sign of a0; Gamma_0 restores it
    M = madd(A1, C1)
    ok = ok and mm(mm(M, A0), M) == msc(-1, A0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_v_is_the_particle_hole_automorphism"; return _tp_rv


def check_image_state_and_pairing_generator():
    premise("angle.hop-across-cut")
    ok = True
    vpsi = mv(V, PSI)
    ok = ok and vpsi == [F(4, 5), F(0), F(0), F(3, 5)]
    gam = mm(G0, madd(ident(), msc(-2, N1)))
    ok = ok and mv(gam, vpsi) == vpsi                       # even
    n0 = sum(vpsi[i] * mv(N0, vpsi)[i] for i in range(DIM))
    ok = ok and (1 - n0, n0) == (F(16, 25), F(9, 25))
    # conjugated generator against the pairing generator, entry by entry
    pair = madd(msc(7, N0), msc(-12, madd(mm(C0, C1), mm(A1, A0))))
    VHV = mm(mm(V, H), V)
    ok = ok and VHV == pair
    # spectrum carried over: eigenvalues 0, 7, 16, -9 on the image eigenbasis
    basis = [[F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)], UP, PSI]
    vals = [F(0), F(7), F(16), F(-9)]
    for b, lam in zip(basis, vals):
        ok = ok and mv(H, b) == [lam * x for x in b]
        vb = mv(V, b)
        ok = ok and mv(pair, vb) == [lam * x for x in vb]
    ok = ok and GA.field_rank([mv(V, b) for b in basis]) == 4
    ok = ok and min(vals[:3]) > vals[3]
    _tp_rv = (ok); assert _tp_rv is not False, "check_image_state_and_pairing_generator"; return _tp_rv


def check_equal_frequency_boost_becomes_number_difference():
    lhs = mm(mm(V, madd(N0, N1, msc(-1, ident()))), V)
    _tp_rv = (lhs == madd(N0, msc(-1, N1))); assert _tp_rv is not False, "check_equal_frequency_boost_becomes_number_difference"; return _tp_rv
