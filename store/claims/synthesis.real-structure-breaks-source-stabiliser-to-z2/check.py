"""synthesis.real-structure-breaks-source-stabiliser-to-z2: exact checks.

Two exact arithmetics. (A) Q(sqrt2, sqrt3)(i), for face space in the family coordinates of the
coherent face vector v = kappa (u' + w f_+), w = lambda e^{i chi}, f_+ = (1, zeta, zeta^2), and the
S3-equivariant real structures sigma_{x,y} = (x P_s + y P_d) conj: a face unitary M = F R Q^dag (Q the
slice map, R a rotation about the democratic axis, F the orthonormal frame u, d1, d2) carries sigma to
complex conjugation and v to e^{i alpha} sqrt3 |kappa| (1, a, i a), a = lambda/sqrt2 (a = 1 at the Koide
point lambda^2 = 2); the forced direction n, carried back, has real slice coordinates proportional to
a - sqrt2 cos(delta + 2 pi k/3) and is orthogonal to the projected (Koide) vector 1 + lambda cos(delta_k).
(B) Q(i), in that frame: the six-mode Fock space of the stored stabiliser check (face operators
Omega_k = (1/2) eps_kij eps_AB a_iA a_jB, mass form H_kl = (1/2) <Omega_k^dag Omega_l + Omega_l Omega_k^dag>,
family unitaries acting by a^dag_iA -> sum_j U_ji a^dag_jA with N(U) = conj(det U) U on face space).
  (1) normal form, (2) the residual stabiliser {N : N conj = conj N, N c = c} is {1, R_n} with
  n = c_R x c_I, its commutant five-dimensional, (3) in Z2-invariant states n is an exact eigenvector
  while the rest of H is free (affine rank 5, tilted source, state-dependent split, both orderings),
  (4) the cubic family word Omega_1^dag Omega_2^dag Omega_3^dag has the monomial group as its symmetry,
  which fixes the coherent vector only trivially because its three moduli are distinct.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

# ----------------------------------------------------------------------------- Q(sqrt2, sqrt3)(i)


def r(c=0, s2=0, s3=0, s6=0):
    out = {}
    for k, v in (((0, 0), c), ((1, 0), s2), ((0, 1), s3), ((1, 1), s6)):
        v = F(v)
        if v:
            out[k] = v
    return out


def radd(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, F(0)) + v
        if out[k] == 0:
            del out[k]
    return out


def rneg(a):
    return {k: -v for k, v in a.items()}


def rmul(a, b):
    out = {}
    for (p2, p3), u in a.items():
        for (q2, q3), v in b.items():
            coef = u * v
            e2, e3 = p2 + q2, p3 + q3
            if e2 == 2:
                coef *= 2
                e2 = 0
            if e3 == 2:
                coef *= 3
                e3 = 0
            k = (e2, e3)
            out[k] = out.get(k, F(0)) + coef
            if out[k] == 0:
                del out[k]
    return out


def rscal(q, a):
    return rmul(r(q), a)


def rinv(a):
    x = {k: v for k, v in a.items() if k[1] == 0}
    y = {(k[0], 0): v for k, v in a.items() if k[1] == 1}
    conj3 = radd(x, rneg(rmul(y, r(s3=1))))
    nrm = radd(rmul(x, x), rneg(rscal(3, rmul(y, y))))
    p = nrm.get((0, 0), F(0))
    q = nrm.get((1, 0), F(0))
    d = p * p - 2 * q * q
    return rmul(conj3, {(0, 0): p / d, (1, 0): -q / d})


def c(re=None, im=None):
    return (re if re is not None else {}, im if im is not None else {})


def cadd(x, y):
    return (radd(x[0], y[0]), radd(x[1], y[1]))


def cneg(x):
    return (rneg(x[0]), rneg(x[1]))


def cmul(x, y):
    return (radd(rmul(x[0], y[0]), rneg(rmul(x[1], y[1]))), radd(rmul(x[0], y[1]), rmul(x[1], y[0])))


def cconj(x):
    return (x[0], rneg(x[1]))


def ciszero(x):
    return not x[0] and not x[1]


def ceq(x, y):
    return ciszero(cadd(x, cneg(y)))


def cabs2(x):
    return radd(rmul(x[0], x[0]), rmul(x[1], x[1]))


def cinv(x):
    n = rinv(cabs2(x))
    return (rmul(x[0], n), rneg(rmul(x[1], n)))


def cr(q):
    return c(r(q), {})


def ci(q):
    return c({}, r(q))


def matvec(M, v):
    out = []
    for i in range(len(M)):
        s = c()
        for j in range(len(v)):
            s = cadd(s, cmul(M[i][j], v[j]))
        out.append(s)
    return out


def matmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = c()
            for k in range(len(B)):
                s = cadd(s, cmul(A[i][k], B[k][j]))
            row.append(s)
        out.append(row)
    return out


def dagger(M):
    return [[cconj(M[j][i]) for j in range(len(M))] for i in range(len(M[0]))]


def transpose(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]


def conjm(M):
    return [[cconj(x) for x in row] for row in M]


def mateq(A, B):
    return all(ceq(A[i][j], B[i][j]) for i in range(len(A)) for j in range(len(A[0])))


def ident(n):
    return [[cr(1 if i == j else 0) for j in range(n)] for i in range(n)]


def scalm(s, M):
    return [[cmul(s, x) for x in row] for row in M]


def addm(A, B):
    return [[cadd(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


S2 = r(s2=1)
S3 = r(s3=1)
ZETA = c(r(F(-1, 2)), r(s3=F(1, 2)))
U_PRIME = [cr(1), cr(1), cr(1)]
F_PLUS = [cr(1), ZETA, cmul(ZETA, ZETA)]
P_S = [[cr(F(1, 3)) for _ in range(3)] for _ in range(3)]
P_D = addm(ident(3), scalm(cr(-1), P_S))
# orthonormal frame rows u = u'/sqrt3, d1 = (2,-1,-1)/sqrt6, d2 = (0,1,-1)/sqrt2
FRAME = [[c(r(s3=F(1, 3)))] * 3,
         [c(r(s6=F(1, 3))), c(r(s6=F(-1, 6))), c(r(s6=F(-1, 6)))],
         [cr(0), c(r(s2=F(1, 2))), c(r(s2=F(-1, 2)))]]


def coherent(kappa, w):
    return [cmul(kappa, cadd(U_PRIME[k], cmul(w, F_PLUS[k]))) for k in range(3)]


def sigma_matrix(x, y):
    return addm(scalm(cr(x), P_S), scalm(cr(y), P_D))


def rot_about_u(cosd, sind):
    """P_s + cos d P_d + sin d [u]_x: the rotation about the democratic axis by d."""
    inv3 = r(s3=F(1, 3))
    ux = [[cr(0), cneg(c(inv3)), c(inv3)], [c(inv3), cr(0), cneg(c(inv3))], [cneg(c(inv3)), c(inv3), cr(0)]]
    return addm(addm(P_S, scalm(c(cosd), P_D)), scalm(c(sind), ux))


def normal_form_map(kappa, w, lam, Q):
    """The unitary M = F R Q^dag and the phase e^{i alpha} with M v = e^{i alpha} sqrt3 |kappa| (1, a, i a).
    Q^dag v = s0 (u' + w' f_+); R rotates about u by -arg(w'); returns (M, 1/s0 normalised to a phase)."""
    v1 = matvec(dagger(Q), coherent(kappa, w))
    s0 = c()
    for k in range(3):
        s0 = cadd(s0, v1[k])
    s0 = cmul(cr(F(1, 3)), s0)                      # singlet coefficient of Q^dag v
    ph = cinv(s0)
    v2 = [cmul(ph, z) for z in v1]                  # u' + w' f_+
    wp = cadd(v2[0], cr(-1))
    laminv = rinv(lam)
    R = rot_about_u(rmul(wp[0], laminv), rmul(wp[1], laminv))
    M = matmul(FRAME, matmul(R, dagger(Q)))
    return M, ph, v2, wp


def check_normal_form_under_a_face_unitary():
    """(i) For sigma_{-1,1} (the Lorentzian quarter-turn structure), sigma_{-1,-1} (Euclidean) and
    sigma_{1,-1}: M unitary, M sigma M^-1 = conj (M A M^T = 1), M v = e^{i alpha} sqrt3 |kappa| (1, a, i a),
    at lambda = sqrt2 (Koide, a = 1) and lambda = 2 sqrt2 / 3 (a = 2/3), at two channel phases; the forced
    direction n = M^dag (a, -1, 0) has real slice coordinates proportional to a - sqrt2 cos(delta_k),
    orthogonal to the projected vector 1 + lambda cos(delta_k), and at a = 1 equals 2 u' minus it."""
    premise("synthesis.coherent-face-vector-real-slices")
    premise("families.rigidity-pairing-sector-one-event")
    premise("synthesis.light-cone-koide-is-quarter-turn")
    premise("families.chart-computation-sign-twist-bracket-form")
    kappa = c(r(0), r(-1))                          # kappa = -i, |kappa| = 1
    Q_lor = addm(P_D, scalm(ci(-1), P_S))           # slice map of sigma_{-1,1}: P_d - i P_s
    Q_euc = scalm(ci(-1), ident(3))                 # slice map of sigma_{-1,-1}: -i
    Q_mix = addm(P_S, scalm(ci(-1), P_D))           # slice map of sigma_{1,-1}
    cases = [(F(1), F(3, 5), F(4, 5), -1, 1, Q_lor), (F(2, 3), F(5, 13), F(12, 13), -1, 1, Q_lor),
             (F(1), F(5, 13), F(-12, 13), -1, 1, Q_lor), (F(1), F(3, 5), F(4, 5), -1, -1, Q_euc),
             (F(1), F(3, 5), F(4, 5), 1, -1, Q_mix)]
    GA.check("five cases", len(cases) == 5)
    for a, cosx, sinx, x, y, Q in cases:
        lam = rscal(a, S2)                          # lambda = a sqrt2
        w = cmul(c(lam), c(r(cosx), r(sinx)))
        A = sigma_matrix(x, y)
        GA.check("Q carries sigma to conjugation", mateq(matmul(matmul(dagger(Q), A), conjm(Q)), ident(3)))
        M, ph, v2, wp = normal_form_map(kappa, w, lam, Q)
        GA.check("M unitary", mateq(matmul(M, dagger(M)), ident(3)))
        GA.check("M sigma M^-1 = conj", mateq(matmul(matmul(M, A), transpose(M)), ident(3)))
        GA.check("|w'| = lambda", radd(cabs2(wp), rneg(rmul(lam, lam))) == {})
        Mv = [cmul(ph, z) for z in matvec(M, coherent(kappa, w))]
        target = [c(S3), c(rscal(a, S3)), c({}, rscal(a, S3))]
        GA.check("M v = e^{i alpha} sqrt3 (1, a, i a)", all(ceq(Mv[k], target[k]) for k in range(3)))
        GA.check("the prefactor is a phase", radd(cabs2(ph), rneg(r(1))) == {})
        # the forced direction, carried back: n = M^dag (a, -1, 0); slice coordinates Q^dag n are real
        n_frame = [cr(a), cr(-1), cr(0)]
        n_orig = matvec(dagger(M), n_frame)
        n_slice = matvec(dagger(Q), n_orig)
        GA.check("slice coordinates of n are real", all(not z[1] for z in n_slice))
        # p = Re(u' + w' f_+) = 1 + lambda cos(delta_k): the projected (Koide) vector; q = Im = lambda sin(delta_k)
        p = [v2[k][0] for k in range(3)]
        q = [v2[k][1] for k in range(3)]
        cosd = [rmul(radd(p[k], r(-1)), rinv(lam)) for k in range(3)]
        # n_slice_k proportional to a - sqrt2 cos(delta_k): the ratio n_k/(a - sqrt2 cos delta_k) is one constant
        expected = [radd(r(a), rneg(rmul(S2, cosd[k]))) for k in range(3)]
        ratio = rmul(n_slice[0][0], rinv(expected[0]))
        GA.check("n_k proportional to a - sqrt2 cos(delta_k)",
                 all(radd(n_slice[k][0], rneg(rmul(ratio, expected[k]))) == {} for k in range(3)))
        dot = {}
        for k in range(3):
            dot = radd(dot, rmul(n_slice[k][0], p[k]))
        GA.check("n orthogonal to the Koide vector", dot == {})
        dotq = {}
        for k in range(3):
            dotq = radd(dotq, rmul(n_slice[k][0], q[k]))
        GA.check("n orthogonal to the imaginary part too", dotq == {})
        if a == 1:
            refl = [radd(r(2), rneg(p[k])) for k in range(3)]       # 2 u' - p, the reflection through the axis
            ratio2 = rmul(n_slice[0][0], rinv(refl[0]))
            GA.check("at Koide n is the reflection of the Koide vector through the democratic axis",
                     all(radd(n_slice[k][0], rneg(rmul(ratio2, refl[k]))) == {} for k in range(3)))
            sump = {}
            sump2 = {}
            for k in range(3):
                sump = radd(sump, refl[k])
                sump2 = radd(sump2, rmul(refl[k], refl[k]))
            GA.check("the reflected vector is itself Koide: sum n^2 = (2/3)(sum n)^2",
                     radd(rscal(3, sump2), rneg(rscal(2, rmul(sump, sump)))) == {})
    return True


# ----------------------------------------------------------------------------- Q(i) Fock space (the frame)

MODES = [(i, A) for i in range(3) for A in range(2)]
IDX = {m: n for n, m in enumerate(MODES)}
Z = (F(0), F(0))
ONE = (F(1), F(0))
CL3 = GA.sig(3, 0)


def eps3(k, i, j):
    if len({k, i, j}) < 3:
        return 0
    prod = GA.mul(GA.mul(GA.gen(k), GA.gen(i), CL3), GA.gen(j), CL3)
    return int(prod.get((0, 1, 2), 0))


def eps2(A, B):
    return 0 if A == B else (1 if (A, B) == (0, 1) else -1)


THETA = [[[F(1, 2) * eps3(k, p[0], q[0]) * eps2(p[1], q[1]) for q in MODES] for p in MODES] for k in range(3)]


def qadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def qmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def qconj(x):
    return (x[0], -x[1])


def qreal(v):
    return (F(v), F(0))


def C(a, b=0):
    return (F(a), F(b))


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def sadd(s, m, co):
    s[m] = qadd(s.get(m, Z), co)
    if s[m] == Z:
        del s[m]


def ann(p, st):
    out = {}
    for m, co in st.items():
        if m[p]:
            mm = list(m)
            mm[p] -= 1
            sadd(out, tuple(mm), qmul(qreal(m[p]), co))
    return out


def cre(p, st):
    out = {}
    for m, co in st.items():
        mm = list(m)
        mm[p] += 1
        sadd(out, tuple(mm), co)
    return out


def lin(terms):
    out = {}
    for coef, st in terms:
        for m, co in st.items():
            sadd(out, m, qmul(coef, co))
    return out


def inner(s, t):
    tot = Z
    for m, co in s.items():
        if m in t:
            wgt = 1
            for x in m:
                wgt *= factorial(x)
            tot = qadd(tot, qmul(qconj(co), qmul(qreal(wgt), t[m])))
    return tot


def omega(k, st):
    return lin([(qreal(THETA[k][p][q]), ann(p, ann(q, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_dag(k, st):
    return lin([(qreal(THETA[k][p][q]), cre(q, cre(p, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_c_dag(cv, st):
    return lin([(qconj(cv[k]), omega_dag(k, st)) for k in range(3) if cv[k] != Z])


def vac():
    return {tuple([0] * 6): ONE}


def mass_form(psi):
    Om = [omega(k, psi) for k in range(3)]
    Od = [omega_dag(k, psi) for k in range(3)]
    H = [[qmul((F(1, 2), F(0)), qadd(inner(Om[k], Om[l]), inner(Od[l], Od[k]))) for l in range(3)] for k in range(3)]
    return H, inner(psi, psi)


def normalised_H(psi):
    H, n = mass_form(psi)
    assert n[1] == 0 and n[0] > 0
    return [[(H[k][l][0] / n[0], H[k][l][1] / n[0]) for l in range(3)] for k in range(3)]


def transform(U, st):
    out = {}
    for m, co in st.items():
        terms = {tuple([0] * 6): co}
        for p, mp in enumerate(m):
            i, A = MODES[p]
            for _ in range(mp):
                new = {}
                for mm, cc in terms.items():
                    for j in range(3):
                        u = U[j][i]
                        if u == Z:
                            continue
                        q = IDX[(j, A)]
                        m2 = list(mm)
                        m2[q] += 1
                        sadd(new, tuple(m2), qmul(u, cc))
                terms = new
        for mm, cc in terms.items():
            sadd(out, mm, cc)
    return out


def qmatmul(A, B):
    out = []
    for i in range(len(A)):
        row = []
        for j in range(len(B[0])):
            s = Z
            for t in range(len(B)):
                s = qadd(s, qmul(A[i][t], B[t][j]))
            row.append(s)
        out.append(row)
    return out


def qdagger(A):
    return [[qconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def qdet3(U):
    def m2(a, b, cc, d):
        return qadd(qmul(a, d), qmul((-b[0], -b[1]), cc))
    t0 = qmul(U[0][0], m2(U[1][1], U[1][2], U[2][1], U[2][2]))
    t1 = qmul(U[0][1], m2(U[1][0], U[1][2], U[2][0], U[2][2]))
    t2 = qmul(U[0][2], m2(U[1][0], U[1][1], U[2][0], U[2][1]))
    return qadd(qadd(t0, (-t1[0], -t1[1])), t2)


def Nof(U):
    d = qconj(qdet3(U))
    return [[qmul(d, U[i][j]) for j in range(3)] for i in range(3)]


def qmatvec(M, v):
    out = []
    for i in range(3):
        s = Z
        for j in range(3):
            s = qadd(s, qmul(M[i][j], v[j]))
        out.append(s)
    return out


def is_unitary(U):
    return qmatmul(U, qdagger(U)) == [[C(1 if i == j else 0) for j in range(3)] for i in range(3)]


def addst(*sts):
    return lin([(ONE, s) for s in sts])


def scalev(co, st):
    return lin([(co, st)])


def V(st):
    return lin([(ONE, omega_dag(k, omega(k, st))) for k in range(3)])


def cubic_disc(H):
    a = sum(H[i][i][0] for i in range(3))
    b = F(0)
    for i in range(3):
        for j in range(i + 1, 3):
            b += H[i][i][0] * H[j][j][0] - (H[i][j][0] ** 2 + H[i][j][1] ** 2)
    cc = qdet3(H)[0]
    B, Cc, D = -a, b, -cc
    return 18 * B * Cc * D - 4 * B ** 3 * D + B ** 2 * Cc ** 2 - 4 * Cc ** 3 - 27 * D ** 2


def commutant_complex_dim(mats):
    """Complex dimension of {X in M_3(C): X S = S X for all S in mats}, by a real linear system."""
    rows = []
    for S in mats:
        for i in range(3):
            for j in range(3):
                re, im = [F(0)] * 18, [F(0)] * 18
                for k in range(3):
                    for (a, b, s) in ((i, k, S[k][j]), (k, j, (-S[i][k][0], -S[i][k][1]))):
                        idx = 2 * (3 * a + b)
                        re[idx] += s[0]
                        im[idx] += s[1]
                        re[idx + 1] += -s[1]
                        im[idx + 1] += s[0]
                rows.append(re)
                rows.append(im)
    return (18 - GA.mat_rank(rows)) // 2


def reflection_real(n):
    nn = sum(x * x for x in n)
    return [[C(F(1 if i == j else 0) - 2 * n[i] * n[j] / nn) for j in range(3)] for i in range(3)]


def source_in_frame(a):
    return [C(1), C(a), C(0, a)]


def check_residual_stabiliser_is_z2():
    """(ii) In the frame (conjugation, c = (1, a, i a)): real X with X c_R = X c_I = 0 form a 3-dimensional
    space (so a real orthogonal N fixing c is 1 + y n^T with y along n, hence 1 or R_n); R_n = 1 - 2 n n^T / |n|^2
    with n = c_R x c_I = a (a, -1, 0) is orthogonal, fixes c, equals N(i R_n), commutes with conjugation, and
    is the transposition of the two real axes at a = 1; its commutant has complex dimension 5; a unitary
    fixing c that does not commute with conjugation exists (the phase rotation of the source), so the cut
    from SU(2) to Z2 is the real structure's."""
    premise("synthesis.light-pair-split-needs-broken-source-stabiliser")
    premise("synthesis.coherent-face-vector-real-slices")
    for a in (F(1), F(2, 3)):
        cR = [F(1), a, F(0)]
        cI = [F(0), F(0), a]
        # X c_R = 0 and X c_I = 0 for a real 3x3 X: 6 equations in 9 unknowns
        rows = []
        for i in range(3):
            for vec in (cR, cI):
                row = [F(0)] * 9
                for j in range(3):
                    row[3 * i + j] = vec[j]
                rows.append(row)
        GA.check("kernel {X : X c_R = X c_I = 0} is three-dimensional", 9 - GA.mat_rank(rows) == 3)
        n = [a * a, -a, F(0)]                       # c_R x c_I
        GA.check("n = c_R x c_I", n == [cR[1] * cI[2] - cR[2] * cI[1], cR[2] * cI[0] - cR[0] * cI[2],
                                        cR[0] * cI[1] - cR[1] * cI[0]])
        GA.check("n orthogonal to c_R and c_I", sum(n[k] * cR[k] for k in range(3)) == 0
                 and sum(n[k] * cI[k] for k in range(3)) == 0)
        Rn = reflection_real(n)
        cv = source_in_frame(a)
        GA.check("R_n orthogonal", is_unitary(Rn) and all(Rn[i][j][1] == 0 for i in range(3) for j in range(3)))
        GA.check("R_n fixes c", qmatvec(Rn, cv) == cv)
        GA.check("R_n is not the identity", Rn != [[C(1 if i == j else 0) for j in range(3)] for i in range(3)])
        U = [[qmul(C(0, 1), x) for x in row] for row in Rn]
        GA.check("R_n = N(i R_n)", Nof(U) == Rn)
        # the only t with (1 + t n n^T) orthogonal: t = 0 or t = -2/|n|^2 (the quadratic 2 t + t^2 |n|^2 = 0)
        nn = sum(x * x for x in n)
        GA.check("two solutions of the orthogonality quadratic", 2 * (-2 / nn) + (-2 / nn) ** 2 * nn == 0 and nn > 0)
        GA.check("commutant of R_n has complex dimension 5", commutant_complex_dim([Rn]) == 5)
        if a == 1:
            P12 = [[C(0), C(1), C(0)], [C(1), C(0), C(0)], [C(0), C(0), C(1)]]
            GA.check("at Koide R_n is the transposition of the two real axes", Rn == P12)
        # a unitary fixing c without commuting with conjugation: e^{i phi} P_c + (1 - P_c)
        cc = sum(x[0] * x[0] + x[1] * x[1] for x in cv)
        Pc = [[qmul(C(F(1) / cc), qmul(cv[i], qconj(cv[j]))) for j in range(3)] for i in range(3)]
        ph = C(F(3, 5), F(4, 5))
        Uph = [[qadd(qmul(ph, Pc[i][j]), qadd(C(1 if i == j else 0), (-Pc[i][j][0], -Pc[i][j][1]))) for j in range(3)]
               for i in range(3)]
        GA.check("phase rotation of the source is unitary and fixes c up to phase", is_unitary(Uph)
                 and qmatvec(Uph, cv) == [qmul(ph, x) for x in cv])
        GA.check("it does not commute with conjugation (it is not real)",
                 any(Uph[i][j][1] != 0 for i in range(3) for j in range(3)))
    return True


def z2_states(cv):
    v0 = vac()
    cb = [qconj(x) for x in cv]

    def Oc(st):
        return omega_c_dag(cv, st)

    def Ob(st):
        return omega_c_dag(cb, st)
    S = []
    S.append(('gauss', addst(v0, Oc(v0), scalev(C(F(1, 2)), Oc(Oc(v0))))))
    S.append(('words_a', addst(v0, Oc(v0), scalev(C(F(2, 3)), Oc(Ob(v0))))))
    S.append(('words_c', addst(v0, Oc(v0), Ob(v0), scalev(C(F(1, 2)), Oc(Ob(v0))), scalev(C(F(1, 5)), V(Oc(Ob(v0)))))))
    S.append(('words_d', addst(v0, scalev(C(2), Oc(Oc(v0))), scalev(C(F(1, 3)), Ob(Ob(Ob(v0)))))))
    S.append(('words_e', addst(Oc(v0), scalev(C(0, 1), Ob(v0)), scalev(C(F(1, 4)), V(Oc(v0))))))
    S.append(('words_f', addst(v0, scalev(C(1, 1), Oc(v0)), scalev(C(F(3, 7)), Ob(Oc(Ob(v0)))))))
    S.append(('words_g', addst(v0, Oc(Oc(v0)), scalev(C(F(1, 2)), Ob(Ob(v0))), scalev(C(F(1, 3)), V(V(Oc(v0)))))))
    for beta in (F(0), F(1), F(2), F(-1, 2)):
        S.append(('real_%s' % beta, addst(v0, Oc(v0), Ob(v0), scalev(C(beta), Oc(Ob(v0))))))
    return S


def block_data(H):
    """For H in the commutant of P12: h_n (on n = (1,-1,0)), and the block on span{(1,1,0)/sqrt2, e3}:
    p = h11 + h12, q = h13, s = h33; det(B - h_n) and tr B - 2 h_n decide the position of h_n."""
    hn = H[0][0][0] - H[0][1][0]
    p = H[0][0][0] + H[0][1][0]
    q = H[0][2]
    s = H[2][2][0]
    det = (p - hn) * (s - hn) - 2 * (q[0] ** 2 + q[1] ** 2)
    return hn, p, q, s, det, p + s - 2 * hn


def check_forced_eigenvector_and_free_block():
    """(iii) At a = 1 in the frame: eleven states built from Omega(c)^dag, Omega(conj c)^dag and V are invariant
    under the Fock map of U = i P12 (N(U) = R_n), their mass forms lie in the commutant and have n as an
    exact eigenvector; the affine span of the achieved forms is the whole five-dimensional commutant; the
    truncated single-source state keeps the source as an eigenvector and the pair degenerate, the two-word
    states tilt the heavy direction off the source; the real one-parameter family 1 + Omega(c)^dag +
    Omega(conj c)^dag + beta Omega(c)^dag Omega(conj c)^dag is degenerate at beta = 0 (one real source) and
    split with beta-dependent values otherwise (h_n = 145/77 at beta = 1); in every split source-word instance
    n is the lowest eigenvector, and the Z2-invariant word (Omega(n)^dag)^2 puts it on top."""
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("synthesis.light-pair-split-needs-broken-source-stabiliser")
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    cv = source_in_frame(F(1))
    n = [C(1), C(-1), C(0)]
    P12 = [[C(0), C(1), C(0)], [C(1), C(0), C(0)], [C(0), C(0), C(1)]]
    U = [[qmul(C(0, 1), x) for x in row] for row in P12]
    GA.check("N(iP12) = P12 fixes c", Nof(U) == P12 and qmatvec(P12, cv) == cv)
    S = z2_states(cv)
    GA.check("eleven states", len(S) == 11)
    coords = []
    results = {}
    for name, psi in S:
        GA.check("invariant under the Fock map of i P12: " + name, transform(U, psi) == psi)
        H = normalised_H(psi)
        GA.check("H in the commutant of P12: " + name,
                 H[0][0] == H[1][1] and H[0][1] == H[1][0] and H[0][1][1] == 0 and H[0][2] == H[1][2])
        hn, p, q, s, det, trm = block_data(H)
        GA.check("n is an exact eigenvector: " + name, qmatvec(H, n) == [qmul(C(hn), x) for x in n])
        Hc = qmatvec(H, cv)
        ratio = qmul(Hc[0], qconj(cv[0]))
        source_eig = all(Hc[i] == qmul(ratio, cv[i]) for i in range(3))
        results[name] = (hn, p, q, s, det, trm, cubic_disc(H) != 0, source_eig)
        coords.append([H[0][0][0], H[0][1][0], H[0][2][0], H[0][2][1], H[2][2][0]])
    diff = [[coords[i][k] - coords[0][k] for k in range(5)] for i in range(1, len(coords))]
    GA.check("affine span of the achieved mass forms is the whole commutant", GA.mat_rank(diff) == 5)
    GA.check("truncated single source: degenerate, source an eigenvector",
             results['gauss'][6] is False and results['gauss'][7] is True and results['gauss'][0] == F(32, 17))
    GA.check("two-word state: split, source not an eigenvector, h_n = 190/101",
             results['words_a'][6] is True and results['words_a'][7] is False and results['words_a'][0] == F(190, 101))
    GA.check("real family at beta = 0 is one real source: degenerate", results['real_0'][6] is False)
    GA.check("real family at beta = 1: split, h_n = 145/77, p = 521/77, s = 229/77, q = 0",
             results['real_1'][6] is True and results['real_1'][0] == F(145, 77) and results['real_1'][1] == F(521, 77)
             and results['real_1'][3] == F(229, 77) and results['real_1'][2] == Z)
    GA.check("real family at beta = 2: a different split (h_n = 505/257)",
             results['real_2'][6] is True and results['real_2'][0] == F(505, 257))
    GA.check("real family at beta = -1/2: split (h_n = 55/32)",
             results['real_-1/2'][6] is True and results['real_-1/2'][0] == F(55, 32))
    split = [nm for nm in results if results[nm][6]]
    GA.check("eight split instances", len(split) == 8)
    GA.check("in every split source-word instance n is the lowest eigenvector",
             all(results[nm][4] > 0 and results[nm][5] > 0 for nm in split))
    # the Z2-invariant word (Omega(n)^dag)^2 puts n on top
    v0 = vac()
    psi_top = addst(v0, omega_c_dag(cv, v0), scalev(C(2), omega_c_dag(n, omega_c_dag(n, v0))))
    GA.check("the (Omega(n)^dag)^2 state is Z2-invariant", transform(U, psi_top) == psi_top)
    H = normalised_H(psi_top)
    hn, p, q, s, det, trm = block_data(H)
    GA.check("there n is the top eigenvector (h_n = 1738/199)", det > 0 and trm < 0 and hn == F(1738, 199)
             and cubic_disc(H) != 0)
    return True


def check_cubic_family_word_has_no_residual_symmetry():
    """(iv) The cubic family word W = Omega_1^dag Omega_2^dag Omega_3^dag |0> is invariant under the Fock maps of
    monomial unitaries whose N has unit product of phases (two instances: a phase-diagonal, a 3-cycle with
    phases) and moved by a non-monomial one; the coherent vector v = kappa (u' + w f_+) at lambda = sqrt2 has
    three distinct moduli |v_k|^2 = 1 + lambda^2 + 2 lambda cos(chi + 2 pi k/3) at cos chi = 3/5 and at
    cos chi = 5/13, so no monomial unitary other than 1 fixes it; the degenerate case needs two equal
    cosines, which cos chi = -1/2 (chi = 2 pi/3) exhibits as a control."""
    premise("synthesis.channel-phase-invisible-to-axially-covariant-completions")
    premise("families.rigidity-pairing-sector-one-event")
    v0 = vac()
    W = omega_dag(0, omega_dag(1, omega_dag(2, v0)))
    diag = [[C(0, 1), C(0), C(0)], [C(0), C(0, -1), C(0)], [C(0), C(0), C(1)]]            # N = diag(i, -i, 1)
    cyc = [[C(0), C(0), C(0, 1)], [C(1), C(0), C(0)], [C(0), C(0, -1), C(0)]]              # a 3-cycle with phases
    for U in (diag, cyc):
        GA.check("monomial unitary", is_unitary(U))
        N = Nof(U)
        prod = C(1)
        for i in range(3):
            prod = qmul(prod, next(x for x in N[i] if x != Z))
        GA.check("product of the phases of N is 1", prod == C(1))
        GA.check("the cubic word is invariant", transform(U, W) == W)
    rot = [[C(F(3, 5)), C(F(4, 5)), C(0)], [C(F(-4, 5)), C(F(3, 5)), C(0)], [C(0), C(0), C(1)]]
    GA.check("a non-monomial unitary moves the cubic word", is_unitary(rot) and transform(rot, W) != W)
    # moduli of the coherent vector at lambda = sqrt2
    lam = S2
    for cosx, sinx, distinct in ((F(3, 5), F(4, 5), True), (F(5, 13), F(12, 13), True), (F(-1, 2), None, False)):
        if sinx is None:
            w = cmul(c(lam), c(r(cosx), r(s3=F(1, 2))))                 # chi = 2 pi/3
        else:
            w = cmul(c(lam), c(r(cosx), r(sinx)))
        v = coherent(c(r(0), r(-1)), w)
        mods = [cabs2(v[k]) for k in range(3)]
        pairs_equal = [radd(mods[i], rneg(mods[j])) == {} for i in range(3) for j in range(i + 1, 3)]
        GA.check("moduli distinct exactly when expected", (not any(pairs_equal)) == distinct)
        if distinct:
            # the only monomial unitary fixing v: permutation must preserve moduli (so is trivial), phases 1
            perms = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
            fixing = 0
            for pm in perms:
                if all(radd(mods[k], rneg(mods[pm[k]])) == {} for k in range(3)):
                    fixing += 1
            GA.check("only the identity permutation preserves the moduli", fixing == 1)
    return True


EXPORTS = {}
