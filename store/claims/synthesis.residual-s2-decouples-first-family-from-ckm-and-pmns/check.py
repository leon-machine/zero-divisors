"""synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns: exact checks (Q(i) matrices).

P exchanges e1 and e2 (the residual S2 of the S3 -> S2 direction e3 e3^T); a = (1,-1,0) spans its odd line.
  (1) the S2-invariant complex 3x3 matrices form a 5-dimensional algebra closed under products, adjoints,
      transposes and inverses, and every member has a as an eigenvector with eigenvalue X11 - X12;
  (2) Pati-Salam textures (10s, 126, 120 with the Clebsch structure, complex vevs) built from S2-invariant
      Yukawas: M_u, M_d, M_e, M_nu, M_R, the Hermitian squares and the seesaw m_nu all commute with P, a is
      a common eigenvector, and its eigenvalue is simple in each (the 2x2 even block does not share it),
      so each mixing matrix has an entry of modulus one with zero row and column; a control with one
      S2-odd 120 entry couples a to the even block in H_e, H_d and m_nu;
  (3) the stored S3 -> S2 textures (M_D = d(J + delta e3 e3^T), M_R = alpha Pi + M_3 J/3 + eps e3 e3^T,
      M_e = J + delta_c e3 e3^T) are S2-invariant with a a null vector of M_D and M_e: the first family.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

Z = (F(0), F(0))


def C(a, b=0):
    return (F(a), F(b))


def cadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def cmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def cconj(x):
    return (x[0], -x[1])


def cneg(x):
    return (-x[0], -x[1])


def cinv(x):
    n = x[0] ** 2 + x[1] ** 2
    return (x[0] / n, -x[1] / n)


def mat(rows):
    return [[C(*e) if isinstance(e, tuple) else C(e) for e in r] for r in rows]


def mm(A, B):
    return [[_sum(cmul(A[i][k], B[k][j]) for k in range(3)) for j in range(3)] for i in range(3)]


def _sum(it):
    s = Z
    for x in it:
        s = cadd(s, x)
    return s


def madd(*Ms):
    out = [[Z] * 3 for _ in range(3)]
    for M in Ms:
        out = [[cadd(out[i][j], M[i][j]) for j in range(3)] for i in range(3)]
    return out


def msc(c, M):
    return [[cmul(c, x) for x in r] for r in M]


def dag(M):
    return [[cconj(M[j][i]) for j in range(3)] for i in range(3)]


def tr_(M):
    return [[M[j][i] for j in range(3)] for i in range(3)]


def det(M):
    def m2(a, b, c, d):
        return cadd(cmul(a, d), cneg(cmul(b, c)))
    return _sum([cmul(M[0][0], m2(M[1][1], M[1][2], M[2][1], M[2][2])),
                 cneg(cmul(M[0][1], m2(M[1][0], M[1][2], M[2][0], M[2][2]))),
                 cmul(M[0][2], m2(M[1][0], M[1][1], M[2][0], M[2][1]))])


def inv(M):
    d = det(M)
    assert d != Z
    cof = [[Z] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            rows = [r for r in range(3) if r != i]
            cols = [c for c in range(3) if c != j]
            minor = cadd(cmul(M[rows[0]][cols[0]], M[rows[1]][cols[1]]), cneg(cmul(M[rows[0]][cols[1]], M[rows[1]][cols[0]])))
            cof[i][j] = minor if (i + j) % 2 == 0 else cneg(minor)
    di = cinv(d)
    return [[cmul(di, cof[j][i]) for j in range(3)] for i in range(3)]


def mv(M, v):
    return [_sum(cmul(M[i][j], v[j]) for j in range(3)) for i in range(3)]


ID = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
P = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
A_ODD = [C(1), C(-1), C(0)]
EVEN = ([C(1), C(1), C(0)], [C(0), C(0), C(1)])


def s2_invariant(M):
    return mm(mm(P, M), P) == M


def is_eigvec(M, v):
    w = mv(M, v)
    k = next(i for i in range(3) if v[i] != Z)
    lam = cmul(w[k], cinv(v[k]))
    return all(w[i] == cmul(lam, v[i]) for i in range(3)), lam


def even_block(M):
    """The 2x2 block of M on the even plane (basis (1,1,0), e3) and its coupling to a."""
    b1, b2 = EVEN
    Mb1, Mb2 = mv(M, b1), mv(M, b2)
    # coordinates: x = x_a a + x_1 b1 + x_2 b2 with x_a = (x0 - x1)/2, x_1 = (x0 + x1)/2, x_2 = x2
    def coords(x):
        return (cmul(C(F(1, 2)), cadd(x[0], cneg(x[1]))), cmul(C(F(1, 2)), cadd(x[0], x[1])), x[2])
    c1, c2 = coords(Mb1), coords(Mb2)
    block = [[c1[1], c2[1]], [c1[2], c2[2]]]
    coupling = (c1[0], c2[0])
    return block, coupling


def block_has_eigenvalue(B, lam):
    """det(B - lam) == 0 for a 2x2 complex block."""
    d = cadd(cmul(cadd(B[0][0], cneg(lam)), cadd(B[1][1], cneg(lam))), cneg(cmul(B[0][1], B[1][0])))
    return d == Z


def check_s2_invariant_matrices_share_the_odd_eigenvector():
    premise("synthesis.residual-s2-fixes-120-family-form")
    premise("neutrino.invariant-symmetric-matrices")
    # the S2-invariant matrices: X11 = X22, X12 = X21, X13 = X23, X31 = X32 (five complex parameters)
    rows = []
    for i in range(3):
        for j in range(3):
            # (P X P - X)_{ij} = X_{p(i) p(j)} - X_{ij}
            p = {0: 1, 1: 0, 2: 2}
            row = [F(0)] * 9
            row[3 * p[i] + p[j]] += 1
            row[3 * i + j] -= 1
            if any(row):
                rows.append(row)
    GA.check("S2-invariant matrices form a five-dimensional space", 9 - GA.mat_rank(rows) == 5)
    X = mat([[(1, 2), (3, -1), (0, 5)], [(3, -1), (1, 2), (0, 5)], [(2, 2), (2, 2), (-1, 7)]])
    Y = mat([[(2, 0), (-1, 1), (4, -3)], [(-1, 1), (2, 0), (4, -3)], [(1, 1), (1, 1), (3, 3)]])
    for M in (X, Y):
        GA.check("instance is S2-invariant", s2_invariant(M))
    for M in (mm(X, Y), dag(X), tr_(Y), inv(X), inv(Y), mm(mm(X, inv(Y)), tr_(X))):
        GA.check("closure under products, adjoints, transposes, inverses", s2_invariant(M))
        ok, lam = is_eigvec(M, A_ODD)
        GA.check("a is an eigenvector", ok)
        GA.check("eigenvalue is M11 - M12", lam == cadd(M[0][0], cneg(M[0][1])))
    GA.check("eigenvalue of X on a is -2 + 3i", is_eigvec(X, A_ODD)[1] == C(-2, 3))
    # the 120 line of the stored result, (e1 + e2) ^ e3, is S2-invariant and annihilates a
    h = mat([[0, 0, 1], [0, 0, 1], [-1, -1, 0]])
    GA.check("the residual-S2 120 line is S2-invariant", s2_invariant(h))
    GA.check("it annihilates a", mv(h, A_ODD) == [Z, Z, Z])
    return True


def textures(Y1, Y2, f, h):
    """Clebsch structure: complex vevs v_u^a, v_d^a, w_u, w_d and four 120 coefficients."""
    vu = (C(3, 1), C(-1, 2))
    vd = (C(1, -1), C(2, 0))
    wu, wd = C(F(1, 2), F(1, 3)), C(-2, 1)
    cu, cnu, cd, ce = C(1, 1), C(0, 2), C(F(3, 2)), C(-1, F(1, 2))
    Mu = madd(msc(vu[0], Y1), msc(vu[1], Y2), msc(wu, f), msc(cu, h))
    Mnu = madd(msc(vu[0], Y1), msc(vu[1], Y2), msc(C(-3), msc(wu, f)), msc(cnu, h))
    Md = madd(msc(vd[0], Y1), msc(vd[1], Y2), msc(wd, f), msc(cd, h))
    Me = madd(msc(vd[0], Y1), msc(vd[1], Y2), msc(C(-3), msc(wd, f)), msc(ce, h))
    vR = C(7, 0)
    MR = msc(vR, f)
    mnu = msc(C(-1), mm(mm(Mnu, inv(MR)), tr_(Mnu)))
    return Mu, Md, Me, Mnu, MR, mnu


def check_pati_salam_textures_with_s2_couplings_decouple_first_family():
    premise("standard-model.imported-clebsch-structure-seesaw")
    premise("synthesis.residual-s2-fixes-120-family-form")
    premise("standard-model.imported-spinor-bilinears")
    premise("synthesis.solar-angle-light-plane-sum-rule")
    Y1 = mat([[(2, 1), (1, 0), (0, 1)], [(1, 0), (2, 1), (0, 1)], [(0, 1), (0, 1), (3, -1)]])
    Y2 = mat([[(1, 0), (-1, 1), (2, 0)], [(-1, 1), (1, 0), (2, 0)], [(2, 0), (2, 0), (0, 2)]])
    f = mat([[(1, 1), (2, -1), (1, 0)], [(2, -1), (1, 1), (1, 0)], [(1, 0), (1, 0), (5, 0)]])
    h = mat([[0, 0, (1, 2)], [0, 0, (1, 2)], [(-1, -2), (-1, -2), 0]])
    for M in (Y1, Y2, f):
        GA.check("symmetric S2-invariant Yukawa", M == tr_(M) and s2_invariant(M))
    GA.check("antisymmetric S2-invariant 120", h == msc(C(-1), tr_(h)) and s2_invariant(h))
    Mu, Md, Me, Mnu, MR, mnu = textures(Y1, Y2, f, h)
    Hs = {'H_u': mm(Mu, dag(Mu)), 'H_d': mm(Md, dag(Md)), 'H_e': mm(Me, dag(Me)), 'm_nu': mnu,
          'm_nu m_nu^dag': mm(mnu, dag(mnu))}
    GA.check("seesaw matrix symmetric", mnu == tr_(mnu))
    for name, M in list(Hs.items()) + [('M_u', Mu), ('M_d', Md), ('M_e', Me), ('M_nu', Mnu), ('M_R', MR)]:
        GA.check("commutes with P: " + name, s2_invariant(M))
        ok, lam = is_eigvec(M, A_ODD)
        GA.check("a is an eigenvector: " + name, ok)
        block, coupling = even_block(M)
        GA.check("no coupling of a to the even plane: " + name, coupling == (Z, Z))
        if name in Hs:
            GA.check("the eigenvalue of a is simple: " + name, not block_has_eigenvalue(block, lam))
    GA.check("H_e eigenvalue on a pinned", is_eigvec(Hs["H_e"], A_ODD)[1] == C(205))
    # control: one S2-odd entry in the 120, e1 ^ e3 alone
    h_odd = madd(h, msc(C(F(1, 3)), mat([[0, 0, 1], [0, 0, 0], [-1, 0, 0]])))
    GA.check("control 120 is antisymmetric and not S2-invariant", h_odd == msc(C(-1), tr_(h_odd)) and not s2_invariant(h_odd))
    Mu2, Md2, Me2, Mnu2, MR2, mnu2 = textures(Y1, Y2, f, h_odd)
    for name, M in (('H_e', mm(Me2, dag(Me2))), ('H_d', mm(Md2, dag(Md2))), ('m_nu', mnu2)):
        GA.check("control couples a to the even plane: " + name, even_block(M)[1] != (Z, Z))
        GA.check("control: a is not an eigenvector: " + name, not is_eigvec(M, A_ODD)[0])
    return True


def check_stored_s3_to_s2_textures_are_s2_invariant_with_a_null():
    premise("neutrino.breaking-relation")
    premise("neutrino.invariant-symmetric-matrices")
    J = mat([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    E3 = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
    Pi = madd(ID, msc(C(F(-1, 3)), J))
    d, delta, delta_c = C(2), C(F(2, 7)), C(F(-2, 7))
    alpha, M3, eps = C(F(1, 5)), C(100), C(F(3, 4))
    MD = msc(d, madd(J, msc(delta, E3)))
    MR = madd(msc(alpha, Pi), msc(cmul(M3, C(F(1, 3))), J), msc(eps, E3))
    Me = madd(J, msc(delta_c, E3))
    mnu = mm(mm(MD, inv(MR)), tr_(MD))
    for name, M in (('M_D', MD), ('M_R', MR), ('M_e', Me), ('m_nu', mnu), ('H_e', mm(Me, dag(Me)))):
        GA.check("stored texture is S2-invariant: " + name, s2_invariant(M))
        GA.check("a is an eigenvector: " + name, is_eigvec(M, A_ODD)[0])
    GA.check("a is a null vector of M_D and M_e (the first family at the S2 stage)",
             mv(MD, A_ODD) == [Z, Z, Z] and mv(Me, A_ODD) == [Z, Z, Z])
    GA.check("m_nu a = 0: the first neutrino is massless at this stage", mv(mnu, A_ODD) == [Z, Z, Z])
    GA.check("M_R a = alpha a", is_eigvec(MR, A_ODD)[1] == alpha)
    GA.check("the even block of m_nu is not identically zero", even_block(mnu)[0] != [[Z, Z], [Z, Z]])
    return True


EXPORTS = {}
