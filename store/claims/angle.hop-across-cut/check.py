"""angle.hop-across-cut: exact checks.

Two fermionic modes in the Jordan-Wigner basis |n0 n1>, index n0 + 2 n1, with |10> = a0^dag|00>,
|01> = a1^dag|00>, |11> = a0^dag a1^dag|00>; a1 carries the string (-1)^{N0}. Matrices are 4 x 4 over Q.
(i) H = 7 N0 - 12 (a0^dag a1 + a1^dag a0) is symmetric, commutes with N0 + N1, is 0 on |00> and 7 on |11>, its
    one-particle block is [[7, -12], [-12, 0]] with eigenvectors (4, -3) at 16 and (3, 4) at -9; the four
    eigenvectors are a basis, so psi = 3/5|10> + 4/5|01> (norm 1) is the unique ground state.
    The generator is outside the supplied class: [N0, hop] = a0^dag a1 - a1^dag a0 != 0, while every supplied
    generator commutes with every N_x (Theorem singularity.class-relative-no-go-no-supplied).
(ii) psi is odd (Gamma psi = -psi), its state vanishes on the odd operators, the restriction to mode 0 is
    diag(16/25, 9/25) = Gibbs for N0 at q = 9/16, the restriction to mode 1 is diag(9/25, 16/25), and the left
    marginal is mixed (entangled across the cut).
(iii) psi is an eigenvector of N0 + N1 (eigenvalue 1) and not of N0 - N1.
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


def comm(a, b):
    return madd(mm(a, b), msc(-1, mm(b, a)))


def ann(j):
    """a_j in the Jordan-Wigner basis (index n0 + 2 n1), dense: lib/fock.py in LSB order."""
    return fock.to_dense(fock.ann(j, 2), DIM)


A0, A1 = ann(0), ann(1)
C0, C1 = tr(A0), tr(A1)
N0, N1 = mm(C0, A0), mm(C1, A1)
HOP = madd(mm(C0, A1), mm(C1, A0))
GAMMA = [[F((-1) ** bin(i).count("1")) if i == j else F(0) for j in range(DIM)] for i in range(DIM)]
K00, K10, K01, K11 = 0, 1, 2, 3
SUPPLIED = madd(msc(7, N0), msc(3, mm(N0, N1)), msc(-2, N1))


def ket(i):
    v = [F(0)] * DIM
    v[i] = F(1)
    return v


def expect(v, op):
    w = mv(op, v)
    return sum(v[i] * w[i] for i in range(DIM))


def generator():
    return madd(msc(7, N0), msc(-12, HOP))


def check_spectrum_and_unique_ground_state():
    H = generator()
    ok = H == tr(H) and comm(H, madd(N0, N1)) == zero()
    ok = ok and mv(H, ket(K00)) == [F(0)] * DIM and mv(H, ket(K11)) == [F(7) * x for x in ket(K11)]
    block = [[H[K10][K10], H[K10][K01]], [H[K01][K10], H[K01][K01]]]
    ok = ok and block == [[7, -12], [-12, 0]]
    ok = ok and block[0][0] + block[1][1] == 7 and block[0][0] * block[1][1] - block[0][1] * block[1][0] == -144
    psi = [F(0), F(3, 5), F(4, 5), F(0)]
    up = [F(0), F(4), F(-3), F(0)]
    ok = ok and sum(x * x for x in psi) == 1
    ok = ok and mv(H, psi) == [F(-9) * x for x in psi] and mv(H, up) == [F(16) * x for x in up]
    # the four eigenvectors form a basis; all other eigenvalues (0, 7, 16) exceed -9
    ok = ok and GA.field_rank([ket(K00), ket(K11), psi, up]) == 4
    ok = ok and min(F(0), F(7), F(16)) > F(-9)
    _tp_rv = (ok); assert _tp_rv is not False, "check_spectrum_and_unique_ground_state"; return _tp_rv


def check_generator_outside_supplied_class():
    premise("singularity.class-relative-no-go-no-supplied")
    c = comm(N0, HOP)
    ok = c == madd(mm(C0, A1), msc(-1, mm(C1, A0))) and c != zero()
    # hand values: [N0, hop] |01> = |10> and [N0, hop] |10> = -|01>
    ok = ok and c[K10][K01] == 1 and c[K01][K10] == -1
    # a supplied (number-polynomial) generator commutes with every N_x; H does not
    ok = ok and comm(SUPPLIED, N0) == zero() and comm(SUPPLIED, N1) == zero()
    ok = ok and comm(generator(), N1)[K10][K01] == -12
    _tp_rv = (ok); assert _tp_rv is not False, "check_generator_outside_supplied_class"; return _tp_rv


def check_parity_and_marginals():
    psi = [F(0), F(3, 5), F(4, 5), F(0)]
    ok = mv(GAMMA, psi) == [-x for x in psi]
    for op in (A0, A1, C0, C1, mm(A0, N1), mm(C1, N0)):
        ok = ok and expect(psi, op) == 0
    # restriction to mode 0: diag(<1 - N0>, <N0>), off-diagonal <a0> = 0
    left = (1 - expect(psi, N0), expect(psi, N0))
    right = (1 - expect(psi, N1), expect(psi, N1))
    ok = ok and left == (F(16, 25), F(9, 25)) and right == (F(9, 25), F(16, 25))
    q = F(9, 16)
    ok = ok and left == (1 / (1 + q), q / (1 + q))
    # mixed marginal: not a rank-one idempotent
    ok = ok and left[0] * left[1] != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_parity_and_marginals"; return _tp_rv


def check_boost_eigenvector_statements():
    psi = [F(0), F(3, 5), F(4, 5), F(0)]
    ok = mv(madd(N0, N1), psi) == psi
    d = mv(madd(N0, msc(-1, N1)), psi)
    # (N0 - N1) psi = 3/5|10> - 4/5|01> is not a multiple of psi
    ok = ok and d == [F(0), F(3, 5), F(-4, 5), F(0)]
    ok = ok and GA.field_rank([psi, d]) == 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_boost_eigenvector_statements"; return _tp_rv
