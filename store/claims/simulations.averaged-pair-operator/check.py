"""simulations.averaged-pair-operator: exact checks.

P_ij = I - (n_i n_i^T + n_j n_j^T)/2 for unit normals, with rational unit vectors (Pythagorean data).
(i)   P_ij = P_ji and P_ij is symmetric; on a rational instance with distinct normals, an
      antisymmetric kernel gradient g_ji = -g_ij and a symmetric bracket F_ij (pressure and viscous
      parts), the pair forces f_ij = -m_i m_j F_ij P_ij g_ij and f_ji sum to zero (momentum), and the
      kinetic power v_i.f_ij + v_j.f_ji plus the two internal-energy terms, each
      (1/2) m_i m_j F_ij v_ij . P_ij g_ij, sum to zero (energy).
(ii)  For n_i = n_j = n, in GA.py over Cl(3,0): (v ^ n) n = v - (v.n) n = P v for sample v, and
      P n = 0.
(iii) For orthogonal normals P n_i = n_i/2, P n_j = n_j/2 and P fixes n_i x n_j: eigenvalues 1, 1/2,
      1/2, and P^2 != P. In general P^2 = P exactly when n_i n_i^T = n_j n_j^T: checked over all
      ordered pairs of eight rational unit vectors (including antipodal pairs).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

UNITS = [
    [F(1), F(0), F(0)], [F(0), F(0), F(1)], [F(3, 5), F(4, 5), F(0)], [F(-3, 5), F(-4, 5), F(0)],
    [F(2, 7), F(3, 7), F(6, 7)], [F(-2, 7), F(-3, 7), F(-6, 7)], [F(0), F(4, 5), F(-3, 5)],
    [F(1, 3), F(2, 3), F(-2, 3)],
]
NI, NJ = [F(3, 5), F(4, 5), F(0)], [F(2, 7), F(3, 7), F(6, 7)]
MI, MJ = F(2), F(5, 3)
VI, VJ = [F(1), F(-2), F(1, 2)], [F(-1, 3), F(4), F(2)]
GIJ = [F(1, 4), F(-3), F(5, 2)]
F_PRESS, F_VISC = F(7, 3), F(-1, 5)
VECTORS = [[F(1), F(2), F(3)], [F(-1, 2), F(0), F(5)], [F(3), F(-4), F(1, 7)]]


def outer(a):
    return [[a[i] * a[j] for j in range(3)] for i in range(3)]


def P(ni, nj):
    A, B = outer(ni), outer(nj)
    return [[(F(1) if i == j else F(0)) - (A[i][j] + B[i][j]) / 2 for j in range(3)] for i in range(3)]


def mv(M, v):
    return [sum(M[i][k] * v[k] for k in range(3)) for i in range(3)]


mm = GA.mat_mul


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def check_conservation():
    Pij, Pji = P(NI, NJ), P(NJ, NI)
    assert Pij == Pji and all(Pij[i][j] == Pij[j][i] for i in range(3) for j in range(3))
    Fij = F_PRESS + F_VISC
    gji = [-x for x in GIJ]
    fij = [-MI * MJ * Fij * x for x in mv(Pij, GIJ)]
    fji = [-MJ * MI * Fij * x for x in mv(Pji, gji)]
    assert (len(fij) == len(fji) and all(a + b == 0 for a, b in zip(fij, fji)))
    vij = [a - b for a, b in zip(VI, VJ)]
    vji = [-x for x in vij]
    kinetic = dot(VI, fij) + dot(VJ, fji)
    work = MI * MJ * Fij * dot(vij, mv(Pij, GIJ))
    assert kinetic == -work and work != 0
    assert dot(vji, mv(Pji, gji)) == dot(vij, mv(Pij, GIJ))
    u_i = F(1, 2) * MI * MJ * Fij * dot(vij, mv(Pij, GIJ))
    u_j = F(1, 2) * MJ * MI * Fij * dot(vji, mv(Pji, gji))
    assert kinetic + u_i + u_j == 0
    return True


def to_ga(v):
    return {(i,): c for i, c in enumerate(v) if c != 0}


def check_parallel_normals_rejection():
    sq = GA.sig(3, 0)
    for n in UNITS:
        Pn = P(n, n)
        nn = to_ga(n)
        assert GA.eq(GA.mul(nn, nn, sq), GA.sc(1))
        assert mv(Pn, n) == [0, 0, 0]
        for v in VECTORS:
            vv = to_ga(v)
            wedge = GA.scal(F(1, 2), GA.sub(GA.mul(vv, nn, sq), GA.mul(nn, vv, sq)))
            rej = GA.mul(wedge, nn, sq)
            assert GA.eq(rej, to_ga(mv(Pn, v)))
            assert GA.eq(rej, GA.sub(vv, GA.scal(dot(v, n), nn)))
    return True


def check_orthogonal_normals_and_idempotence():
    ni, nj = [F(3, 5), F(4, 5), F(0)], [F(0), F(0), F(1)]
    assert dot(ni, nj) == 0
    Pm = P(ni, nj)
    assert mv(Pm, ni) == [x / 2 for x in ni] and mv(Pm, nj) == [x / 2 for x in nj]
    t = cross(ni, nj)
    assert mv(Pm, t) == t and t != [0, 0, 0]
    assert mm(Pm, Pm) != Pm
    idem = 0
    for a in UNITS:
        for b in UNITS:
            Pab = P(a, b)
            same_line = outer(a) == outer(b)
            assert (mm(Pab, Pab) == Pab) == same_line
            idem += same_line
    assert idem == 8 + 2 * 2
    return True
