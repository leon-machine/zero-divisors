"""singularity.descent-what-it-erases: exact checks.

(1) P = v* v is an idempotent with 1 - P = v v*, from the CAR, in three realisations: the defining
2 x 2 representation v = E_12, v* = E_21, the hyperbolic atom of Cl(1,1) (blade engine, v = (e0 +
e1)/2, v* = (e0 - e1)/2) and the second Jordan-Wigner mode on two modes (4 x 4). In the defining
representation P = diag(0, 1).
(2) The pinching E(x) = P x P + (1 - P) x (1 - P), as a linear map on Mat_2, is computed on the four
matrix units: it fixes E_11 and E_22 and kills E_12 and E_21, so E(a, b; c, d) = diag(a, d) for every
x (the map is linear, so the matrix units are the general case); this is compared with a direct
evaluation on symbolic-sample matrices, over Q and over Q(i). The occupation data are retained: the
diagonal and tr(P x) are unchanged, and the coherences b, c are erased.
"""
from fractions import Fraction as F

import GA
import fock
from GA import QI

SAMPLES = [[[F(2, 3), F(5, 7)], [F(-3, 11), F(4, 9)]],
           [[QI(1, 2), QI(3, -1)], [QI(-2, 5), QI(7, 3)]],
           [[F(9, 25), F(12, 25)], [F(12, 25), F(16, 25)]]]


def zeros(n):
    return [[F(0)] * n for _ in range(n)]


def eye(n):
    return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]


def unit(n, a, b):
    M = zeros(n)
    M[a][b] = F(1)
    return M


mm = GA.mat_mul


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


meq = GA.mat_eq


def pinch(x, P):
    Q = msub(eye(len(P)), P)
    return madd(mm(mm(P, x), P), mm(mm(Q, x), Q))


def realisations():
    """(v, v*) as matrices: the defining representation and the second Jordan-Wigner mode."""
    v, vs = unit(2, 0, 1), unit(2, 1, 0)
    return [(v, vs), (fock.to_dense(fock.ann(1, 2, fock.MSB), 4), fock.to_dense(fock.cre(1, 2, fock.MSB), 4))]


def check_occupation_projector():
    out = []
    for v, vs in realisations():
        n = len(v)
        P = mm(vs, v)
        car = meq(madd(mm(v, vs), mm(vs, v)), eye(n)) and meq(mm(v, v), zeros(n))
        out.append(car and meq(mm(P, P), P) and meq(msub(eye(n), P), mm(v, vs)) and not meq(P, zeros(n)))
    # the defining representation: P = E_22 = diag(0, 1)
    v, vs = realisations()[0]
    out.append(meq(mm(vs, v), [[F(0), F(0)], [F(0), F(1)]]))
    # the hyperbolic atom, blade-exact
    sq = GA.sig(1, 1)
    e0, e1 = GA.gen(0), GA.gen(1)
    va = GA.scal(F(1, 2), GA.add(e0, e1))
    vsa = GA.scal(F(1, 2), GA.sub(e0, e1))
    Pa = GA.mul(vsa, va, sq)
    out.append(GA.eq(GA.mul(Pa, Pa, sq), Pa) and GA.eq(GA.sub(GA.sc(1), Pa), GA.mul(va, vsa, sq)))
    out.append(GA.eq(Pa, GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(e0, e1, sq)))))
    assert all(out), out


def check_pinching_keeps_diagonal_erases_coherences():
    v, vs = realisations()[0]
    P = mm(vs, v)
    # the pinching as a 4 x 4 matrix on the matrix units, (row, col) = (out unit, in unit)
    units = [(a, b) for a in range(2) for b in range(2)]
    Emat = [[pinch(unit(2, a, b), P)[c][d] for (a, b) in units] for (c, d) in units]
    want = [[F(1), F(0), F(0), F(0)], [F(0), F(0), F(0), F(0)],
            [F(0), F(0), F(0), F(0)], [F(0), F(0), F(0), F(1)]]
    assert meq(Emat, want), Emat
    for x in SAMPLES:
        Ex = pinch(x, P)
        assert meq(Ex, [[x[0][0], F(0)], [F(0), x[1][1]]])
        trP = lambda y: sum((mm(P, y)[i][i] for i in range(2)), F(0))
        assert trP(Ex) == trP(x) and x[0][1] != 0 and Ex[0][1] == 0 and Ex[1][0] == 0
    # idempotent and trace preserving, on the matrix units
    for (a, b) in units:
        Eu = pinch(unit(2, a, b), P)
        assert meq(pinch(Eu, P), Eu)
        assert Eu[0][0] + Eu[1][1] == (1 if a == b else 0)
