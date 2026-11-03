"""synthesis.second-doublet-of-one-family-coupling-gives-no-quark-mixing: exact checks.

Family matrices over the Gaussian rationals (GA.QI). H = M M^dag. The CKM matrix is V = U_u^dag U_d with U the
unitaries diagonalising H_u, H_d; a common eigenvector of H_u and H_d is a mass eigenstate of both sectors, so its
row and column of V carry a single entry of modulus one, and det[H_u, H_d] = 0 (Jarlskog invariant J = 0).
Family basis of synthesis.residual-s2-fixes-120-family-form: u' = (1,1,1), s = (1,1,-2), a = (1,-1,0); the residual
S2 is the exchange P of e1 and e2.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

Q = GA.QI
I = GA.QI_I


def z(x):
    return Q(x)


def mat(rows):
    return [[Q(x) for x in r] for r in rows]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Q(0)) for j in range(3)] for i in range(3)]


def madd(*Ms):
    return [[sum((M[i][j] for M in Ms), Q(0)) for j in range(3)] for i in range(3)]


def msc(c, M):
    return [[Q(c) * M[i][j] for j in range(3)] for i in range(3)]


def dag(M):
    return [[M[j][i].conj() for j in range(3)] for i in range(3)]


def tr_(M):
    return [[M[j][i] for j in range(3)] for i in range(3)]


def comm(A, B):
    return madd(mm(A, B), msc(-1, mm(B, A)))


def det(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def apply(M, v):
    return [sum((M[i][k] * v[k] for k in range(3)), Q(0)) for i in range(3)]


def is_eigvec(M, v):
    w = apply(M, v)
    k = next(i for i in range(3) if v[i] != 0)
    lam = w[k] / v[k]
    return all(w[i] == lam * v[i] for i in range(3))


def outer(x, y):
    return mat([[x[i] * y[j] for j in range(3)] for i in range(3)])


def wedge(x, y):
    return madd(outer(x, y), msc(-1, outer(y, x)))


U1, S, A = [1, 1, 1], [1, 1, -2], [1, -1, 0]
P = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
S2_BASIS = [outer(U1, U1), outer(S, S), outer(A, A), madd(outer(U1, S), outer(S, U1)), wedge(U1, S)]
ZERO = mat([[0] * 3] * 3)


def H(M):
    return mm(M, dag(M))


def gen_S2(coefs):
    return madd(*[msc(c, B) for c, B in zip(coefs, S2_BASIS)])


def check_proportional_coupling_gives_no_mixing():
    premise("standard-model.one-vev-vector-relations-breaking-pattern")
    premise("standard-model.bidoublet-complex")
    premise("standard-model.imported-clebsch-structure-seesaw")
    # one family matrix Y read through any doublet vevs: M_u = v_u Y, M_d = v_d Y
    Y = mat([[Q(1, 2), Q(3, 1), Q(0, -1)], [Q(2), Q(-1, 1), Q(5)], [Q(0, 4), Q(1), Q(-2, 3)]])
    GA.check("tr(Y Y^dag) tabulated", sum((H(Y)[i][i] for i in range(3)), Q(0)) == Q(77))
    ratios = []
    for vu, vd in [(Q(7, 2), Q(1, -1)), (Q(41), Q(1)), (Q(0, 3), Q(2, 5))]:
        Mu, Md = msc(vu, Y), msc(vd, Y)
        Hu, Hd = H(Mu), H(Md)
        n2 = (vu * vu.conj()) / (vd * vd.conj())
        ratios.append(n2)
        GA.check("H_u = |v_u/v_d|^2 H_d (every up/down mass ratio is |v_u/v_d|)", Hu == msc(n2, Hd))
        GA.check("[H_u, H_d] = 0 (V = 1 for nondegenerate masses)", comm(Hu, Hd) == ZERO)
    GA.check("squared vev ratios tabulated", ratios == [Q(F(53, 2)), Q(1681), Q(F(9, 29))])
    # control: two independent family matrices (a second 10 with its own Yukawa) do mix
    Y2 = mat([[1, 0, 0], [0, 0, 1], [0, 1, 3]])
    Mu = madd(msc(Q(3), Y), msc(Q(1), Y2))
    Md = madd(msc(Q(1), Y), msc(Q(0, 2), Y2))
    GA.check("control: independent couplings give det[H_u, H_d] != 0 (tabulated)",
             det(comm(H(Mu), H(Md))) == Q(0, 301626160668))
    # record values (memory, MS-bar at M_Z, MeV): the three up/down ratios differ, |V_us| != 0
    mu, md, mc, ms, mt, mb = F(127, 100), F(29, 10), F(619), F(55), F(171700), F(2890)
    r = [mu / md, mc / ms, mt / mb]
    GA.check("record: m_u/m_d < 1 < m_c/m_s < m_t/m_b", r[0] < 1 < r[1] < r[2])
    GA.check("record ratios tabulated", r == [F(127, 290), F(619, 55), F(17170, 289)])
    GA.check("record: |V_us| = 0.225 is not zero", F(225, 1000) != 0)
    return True


def check_s3_invariant_couplings_are_degenerate():
    premise("synthesis.residual-s2-fixes-120-family-form")
    premise("neutrino.breaking-relation")
    # S3-invariant symmetric matrices: alpha 1 + beta J (J all ones); S3 admits no 120 (clause (i))
    one = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    Jm = mat([[1, 1, 1]] * 3)
    Mu = madd(msc(Q(2, 1), one), msc(Q(5), Jm))
    Md = madd(msc(Q(0, 3), one), msc(Q(-1, 2), Jm))
    plane = ([Q(1), Q(-1), Q(0)], [Q(1), Q(0), Q(-1)])
    for M, low, high in ((Mu, Q(5), Q(290)), (Md, Q(9), Q(90))):
        Hm = H(M)
        for x in plane:
            GA.check("two degenerate families: H x = |alpha|^2 x on the plane orthogonal to u'",
                     apply(Hm, x) == [low * t for t in x])
        GA.check("third family: H u' = |alpha + 3 beta|^2 u'", apply(Hm, [Q(1)] * 3) == [high] * 3)
    # the S3-invariant antisymmetric matrices are zero: u' ^ s, the S2 line, is not S3-invariant
    P3 = mat([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    X = wedge(U1, S)
    GA.check("u' ^ s is not S3-invariant", mm(mm(P3, X), tr_(P3)) != X)
    return True
