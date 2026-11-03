"""singularity.descent-parity-average: exact checks on the mode algebra Mat_2 (defining
representation v = E_12, v* = E_21, sigma = v* v - v v*, alpha = Ad(sigma)).

(1) E(x) = P x P + (1 - P) x (1 - P) (the descent of the premise, P = v* v) equals (x + alpha(x))/2
and (x + sigma x sigma)/2 on all four matrix units, hence on every x (both maps are linear), and on
sample matrices over Q(i). alpha is an involutive automorphism (sigma^2 = 1).
(2) The fixed-point algebra of alpha, computed as the kernel of alpha - id, is 2-dimensional and is
the range of E; the kernel of E is 2-dimensional and is span{v, v*}, the (-1)-eigenspace of alpha.
(3) Uniqueness: a linear map F: Mat_2 -> Mat_2 with F = id on the fixed algebra, range in it, and
F(a x b) = a F(x) b for a, b in it is solved for (16 unknowns); the homogeneous system has only the
zero solution and E satisfies it, so E is the unique conditional expectation onto the fixed algebra.
(4) E preserves every alpha-invariant state (diagonal density matrices) on all matrix units, and a
state with coherences is not preserved (control).
"""
from fractions import Fraction as F

import GA
from GA import QI
from tp_premise import premise

SAMPLES = [[[QI(2, 3), QI(5, 7)], [QI(-3, 11), QI(4, 9)]],
           [[F(1), F(-4)], [F(7, 2), F(0)]]]
STATES_INV = [[[F(9, 25), F(0)], [F(0), F(16, 25)]], [[F(1, 3), F(0)], [F(0), F(2, 3)]]]
STATE_COH = [[F(1, 2), F(1, 4)], [F(1, 4), F(1, 2)]]
UNITS = [(a, b) for a in range(2) for b in range(2)]


def zeros(n):
    return [[F(0)] * n for _ in range(n)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def unit(a, b):
    M = zeros(2)
    M[a][b] = F(1)
    return M


mm = GA.mat_mul


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


meq = GA.mat_eq


def tr(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def flat(A):
    return [A[a][b] for (a, b) in UNITS]


V, VS = unit(0, 1), unit(1, 0)
P = mm(VS, V)
SIGMA = msub(mm(VS, V), mm(V, VS))


def descent(x):
    Q = msub(eye(2), P)
    return madd(mm(mm(P, x), P), mm(mm(Q, x), Q))


def alpha(x):
    return mm(mm(SIGMA, x), SIGMA)


def check_descent_is_parity_average():
    premise("singularity.descent-what-it-erases")
    assert meq(mm(SIGMA, SIGMA), eye(2)) and not meq(SIGMA, eye(2))
    for (a, b) in UNITS:
        x = unit(a, b)
        assert meq(descent(x), mscal(F(1, 2), madd(x, alpha(x))))
        # alpha is multiplicative
        for (c, d) in UNITS:
            y = unit(c, d)
            assert meq(alpha(mm(x, y)), mm(alpha(x), alpha(y)))
    for x in SAMPLES:
        assert meq(descent(x), mscal(F(1, 2), madd(x, alpha(x))))
    # alpha fixes the diagonal units and negates the off-diagonal ones
    signs = [alpha(unit(a, b))[a][b] for (a, b) in UNITS]
    assert signs == [F(1), F(-1), F(-1), F(1)], signs


def check_range_kernel_and_uniqueness():
    premise("singularity.descent-what-it-erases")
    # fixed algebra = ker(alpha - id), odd part = ker(alpha + id)
    Amat = [[flat(alpha(unit(a, b)))[k] for (a, b) in UNITS] for k in range(4)]
    fix = GA.field_kernel([[Amat[i][j] - (1 if i == j else 0) for j in range(4)] for i in range(4)])
    odd = GA.field_kernel([[Amat[i][j] + (1 if i == j else 0) for j in range(4)] for i in range(4)])
    assert len(fix) == 2 and len(odd) == 2
    Emat = [[flat(descent(unit(a, b)))[k] for (a, b) in UNITS] for k in range(4)]
    kerE = GA.field_kernel(Emat)
    assert len(kerE) == 2 and GA.field_rank(Emat) == 2
    # range(E) = fixed algebra, ker(E) = span{v, v*}
    assert GA.field_rank([list(r) for r in zip(*Emat)] + fix) == 2
    assert GA.field_rank(kerE + [flat(V), flat(VS)]) == 2 and GA.field_rank(kerE + odd) == 2
    # uniqueness: unknown linear map M (M[o][i] at index 4 o + i), homogeneous constraints
    fixmats = [[[f[2 * r + c] for c in range(2)] for r in range(2)] for f in fix]
    rows = []
    for f in fixmats:                           # F(a) = a, homogeneous part: F(a) = 0
        for o in range(4):
            row = [F(0)] * 16
            for i in range(4):
                row[4 * o + i] += flat(f)[i]
            rows.append(row)
    for i in range(4):                          # range in the fixed algebra: alpha(F(u_i)) = F(u_i)
        for c in range(4):
            row = [F(0)] * 16
            for o in range(4):
                row[4 * o + i] += Amat[c][o] - (1 if c == o else 0)
            rows.append(row)
    for a in fixmats:                           # bimodularity F(a u_i b) = a F(u_i) b
        for b in fixmats:
            for i, (p, q) in enumerate(UNITS):
                lhs = flat(mm(mm(a, unit(p, q)), b))
                imgs = [flat(mm(mm(a, unit(*UNITS[o])), b)) for o in range(4)]
                for c in range(4):
                    row = [F(0)] * 16
                    for j in range(4):
                        row[4 * c + j] += lhs[j]
                    for o in range(4):
                        row[4 * o + i] -= imgs[o][c]
                    rows.append(row)
    assert GA.field_kernel(rows) == [] and GA.field_rank(rows) == 16
    # E satisfies the inhomogeneous constraints: bimodule property and identity on the fixed algebra
    for a in fixmats:
        assert meq(descent(a), a)
        for b in fixmats:
            for x in SAMPLES:
                assert meq(descent(mm(mm(a, x), b)), mm(mm(a, descent(x)), b))


def check_preserves_alpha_invariant_states():
    premise("singularity.descent-what-it-erases")
    for rho in STATES_INV:
        assert meq(alpha(rho), rho) and tr(rho) == 1
        for (a, b) in UNITS:
            x = unit(a, b)
            assert tr(mm(rho, descent(x))) == tr(mm(rho, x))
    # control: a state with coherence 1/4 is not alpha-invariant and E changes its value on v
    assert not meq(alpha(STATE_COH), STATE_COH)
    assert tr(mm(STATE_COH, V)) == F(1, 4) and tr(mm(STATE_COH, descent(V))) == 0
