from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def to_mat(M):
    return S.mat(M)


def kron(A, B):
    return [[A[i][j] * B[k][l] for j in range(len(A[0])) for l in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def right_matrix(x, sq):
    n = len(sq)
    blades = GA.all_blades(n)
    cols = [S.coords(GA.mul({b: F(1)}, x, sq), n) for b in blades]
    return [[cols[j][i] for j in range(len(blades))] for i in range(len(blades))]


def flat(M):
    return [a for row in M for a in row]


E12 = [[0, 1], [0, 0]]
E21 = [[0, 0], [1, 0]]


def check_hyperbolic_plane_is_m2r():
    premise("std-algebra.existence-uniqueness")
    premise("std-algebra.blade-basis")
    premise("std-algebra.witt-decomposition")
    a, b = to_mat(E12), to_mat(E21)
    e = S.mat_add(a, b)
    f = S.mat_add(a, S.mat_scal(-1, b))
    ok = S.check_matrix_rep([e, f], GA.sig(1, 1), 4)
    ok = ok and S.check_matrix_rep([to_mat([[1, 0], [0, -1]]), to_mat([[0, 1], [1, 0]])], GA.sig(2, 0), 4)
    # u = (e + f)/2 -> E12, w = (e - f)/2 -> E21, uw -> E11, wu -> E22
    u = S.mat_scal(F(1, 2), S.mat_add(e, f))
    w = S.mat_scal(F(1, 2), S.mat_add(e, S.mat_scal(-1, f)))
    ok = ok and S.mat_eq(u, a) and S.mat_eq(w, b)
    ok = ok and S.mat_eq(S.mat_mul(u, w), to_mat([[1, 0], [0, 0]]))
    ok = ok and S.mat_eq(S.mat_mul(w, u), to_mat([[0, 0], [0, 1]]))
    # control: the same matrices do not satisfy the relations of Cl(0,2)
    ok = ok and not S.check_matrix_rep([e, f], GA.sig(0, 2), 4)
    GA.check("Cl(1,1) and Cl(2,0) are M_2(R); a hyperbolic pair goes to the matrix units", ok)
    return ok
