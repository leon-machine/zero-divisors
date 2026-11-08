import sys, itertools
sys.path.insert(0, '.')
from fock import cre, ann, add, scal, popc
from fractions import Fraction as F

# five modes: 0,1 slots, 2,3,4 pairs; V_+ = even subsets
CH = [S for S in range(32) if popc(S) % 2 == 0]
CH.sort(key=lambda S: (popc(S), S))
POS = {S: i for i, S in enumerate(CH)}
n = len(CH)

def rep_bil(a, b, kind='ab'):
    """matrix of a^dag_a a_b (kind 'ab'), a^dag_a a^dag_b ('cc'), a_a a_b ('aa') on V_+"""
    M = [[F(0)] * n for _ in range(n)]
    for S in CH:
        if kind == 'ab': out = cre(a, ann(b, {S: F(1)}))
        elif kind == 'cc': out = cre(a, cre(b, {S: F(1)}))
        else: out = ann(a, ann(b, {S: F(1)}))
        for T, c in out.items():
            M[POS[T]][POS[S]] += c
    return M

def rep(X):  # X 5x5 -> derivation on V_+
    M = [[F(0)] * n for _ in range(n)]
    for a in range(5):
        for b in range(5):
            if X[a][b]:
                R = rep_bil(a, b)
                for i in range(n):
                    for j in range(n):
                        M[i][j] += X[a][b] * R[i][j]
    return M

def E5(a, b):
    return [[F(1) if (i, j) == (a, b) else F(0) for j in range(5)] for i in range(5)]
def lin(*pairs):
    out = [[F(0)] * 5 for _ in range(5)]
    for c, X in pairs:
        for i in range(5):
            for j in range(5):
                out[i][j] += c * X[i][j]
    return out
def mm(A, B):
    k = len(B)
    return [[sum(A[i][l] * B[l][j] for l in range(k)) for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return sum(A[i][i] for i in range(len(A)))
def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def comm(A, B):
    return msub(mm(A, B), mm(B, A))

su2 = [E5(0, 1), E5(1, 0), lin((1, E5(0, 0)), (-1, E5(1, 1)))]
su3 = [E5(a, b) for a in (2, 3, 4) for b in (2, 3, 4) if a != b] + [lin((1, E5(2, 2)), (-1, E5(3, 3))), lin((1, E5(3, 3)), (-1, E5(4, 4)))]
Y5 = lin((F(1, 2), E5(0, 0)), (F(1, 2), E5(1, 1)), (F(-1, 3), E5(2, 2)), (F(-1, 3), E5(3, 3)), (F(-1, 3), E5(4, 4)))
