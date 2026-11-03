"""synthesis.channel-phase-invisible-to-axially-covariant-completions: exact checks.

Six bosonic face modes a_p, p = (i, A), i a family index, A a spinor slot; states are finite
combinations of (a^dag)^m |0> with complex-rational coefficients (pairs of Fractions);
Theta_k = (1/2) eps_kij eps_AB and Omega_k = sum Theta_k[p,q] a_p a_q as in the skeleton theorem;
H_kl = (1/2)<Omega_k^dag Omega_l + Omega_l Omega_k^dag> is the mass form (unnormalised here, divided
by <psi|psi> where compared). A real family matrix R acts on states by the Fock map
a^dag_{iA} -> sum_j R[j][i] a^dag_{jA} (`transform`). Samples: two rational Cayley rotations R about
u' = (1,1,1) (t = 1/2, -2/7), two generic complex face vectors c, the real structures
sigma_{x,y} = (x P_s + y P_d) o conj. Checks:
  check_axial_rotation_is_symmetry_of_real_structure_words: (i) R is orthogonal, R != 1, R u' = u',
      R commutes with the cyclic family shift and with sigma_{x,y} for all four sign choices; (ii) for
      the word |0> + Omega(c)^dag|0> + (2/3) Omega(c)^dag Omega(sigma c)^dag|0> the characteristic
      polynomial of the normalised H is the same at c and Rc, for all four sigma_{x,y}; (iii) the
      family-basis word sum_k (Omega_k^dag)^3 (applied after the source, g = 1/2) gives different
      characteristic polynomials at c and Rc and equal ones at c and its cyclic shift.
  check_fock_rotation_covariance: (i), (ii) on the Fock space: sum_k (Omega_k^dag)^2 |0> is fixed by
      R^ and V = sum_k Omega_k^dag Omega_k commutes with R^ on the sample states; for the word above
      and a word also containing sum_k (Omega_k^dag)^2 and V (sigma_{1,1} and sigma_{-1,-1}),
      psi[Rc] = R^ psi[c], <psi|psi> is preserved, H(R^ psi) = R H(psi) R^T entrywise, and the
      characteristic polynomials agree (16 cases).
Not computed: R f_+ = e^{i theta} f_+ (it follows from R commuting with the cyclic shift, whose
eigenvalues 1, zeta, zeta^{-1} are distinct, with |e^{i theta}| = 1 from orthogonality), Hamiltonian
evolution, and the coherent face vector v(chi) itself (generic complex c is used).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

MODES = [(i, A) for i in range(3) for A in range(2)]
IDX = {m: n for n, m in enumerate(MODES)}
Z = (F(0), F(0))
ONE = (F(1), F(0))


CL3 = GA.sig(3, 0)


def eps3(k, i, j):
    """Levi-Civita symbol read off the Clifford product in Cl(3,0): coefficient of the pseudoscalar
    in e_k e_i e_j for distinct k, i, j."""
    if len({k, i, j}) < 3:
        return 0
    prod = GA.mul(GA.mul(GA.gen(k), GA.gen(i), CL3), GA.gen(j), CL3)
    return int(prod.get((0, 1, 2), 0))


def eps2(A, B):
    return 0 if A == B else (1 if (A, B) == (0, 1) else -1)


THETA = [[[F(1, 2) * eps3(k, p[0], q[0]) * eps2(p[1], q[1]) for q in MODES] for p in MODES] for k in range(3)]


def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def cconj(x): return (x[0], -x[1])
def creal(c): return (F(c), F(0))


def factorial(n):
    out = 1
    for j in range(2, n + 1):
        out *= j
    return out


def sadd(s, m, c):
    s[m] = cadd(s.get(m, Z), c)
    if s[m] == Z:
        del s[m]


def ann(p, st):
    out = {}
    for m, c in st.items():
        if m[p]:
            mm = list(m); mm[p] -= 1
            sadd(out, tuple(mm), cmul(creal(m[p]), c))
    return out


def cre(p, st):
    out = {}
    for m, c in st.items():
        mm = list(m); mm[p] += 1
        sadd(out, tuple(mm), c)
    return out


def lin(terms):
    out = {}
    for coef, st in terms:
        for m, c in st.items():
            sadd(out, m, cmul(coef, c))
    return out


def inner(s, t):
    tot = Z
    for m, c in s.items():
        if m in t:
            w = 1
            for x in m:
                w *= factorial(x)
            tot = cadd(tot, cmul(cconj(c), cmul(creal(w), t[m])))
    return tot


def omega(k, st):
    return lin([(creal(THETA[k][p][q]), ann(p, ann(q, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_dag(k, st):
    return lin([(creal(THETA[k][p][q]), cre(q, cre(p, st))) for p in range(6) for q in range(6) if THETA[k][p][q]])


def omega_c_dag(c, st):
    """Omega(c)^dag = sum_k conj(c_k) Omega_k^dag."""
    return lin([(cconj(c[k]), omega_dag(k, st)) for k in range(3) if c[k] != Z])


def vac():
    return {tuple([0] * 6): ONE}


def mass_form(psi):
    """H_kl = (1/2)<Omega_k^dag Omega_l + Omega_l Omega_k^dag> / <psi|psi>, unnormalised: returns (H, norm)."""
    Om = [omega(k, psi) for k in range(3)]
    Od = [omega_dag(k, psi) for k in range(3)]
    H = [[cmul((F(1, 2), F(0)), cadd(inner(Om[k], Om[l]), inner(Od[l], Od[k]))) for l in range(3)] for k in range(3)]
    return H, inner(psi, psi)


def transform(U, st):
    """Fock unitary of the family map: a_{iA}^dag -> sum_j U[j][i] a_{jA}^dag (U a 3x3 complex-rational matrix)."""
    out = {}
    for m, c in st.items():
        # expand prod_p (sum_j U[j][i(p)] a^dag_{(j,A(p))})^{m_p}
        terms = {tuple([0] * 6): c}
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
                        m2 = list(mm); m2[q] += 1
                        sadd(new, tuple(m2), cmul(u, cc))
                terms = new
        for mm, cc in terms.items():
            sadd(out, mm, cc)
    return out


def cmatmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        row = []
        for j in range(m):
            s = Z
            for t in range(k):
                s = cadd(s, cmul(A[i][t], B[t][j]))
            row.append(s)
        out.append(row)
    return out


def cdagger(A):
    return [[cconj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]


def cdet3(U):
    def m(a, b, c, d): return cadd(cmul(a, d), cmul((-b[0], -b[1]), c))
    t0 = cmul(U[0][0], m(U[1][1], U[1][2], U[2][1], U[2][2]))
    t1 = cmul(U[0][1], m(U[1][0], U[1][2], U[2][0], U[2][2]))
    t2 = cmul(U[0][2], m(U[1][0], U[1][1], U[2][0], U[2][1]))
    return cadd(cadd(t0, (-t1[0], -t1[1])), t2)


def C(a, b=0):
    return (F(a), F(b))


def addst(*sts):
    return lin([(ONE, s) for s in sts])


def scalev(c, st):
    return lin([(c, st)])


def charpoly(H, n):
    """Coefficients (a, b, c) of x^3 - a x^2 + b x - c for the normalised Hermitian H/n."""
    Hn = [[(H[k][l][0] / n[0], H[k][l][1] / n[0]) for l in range(3)] for k in range(3)]
    a = sum(Hn[i][i][0] for i in range(3))
    b = F(0)
    for i in range(3):
        for j in range(i + 1, 3):
            b += Hn[i][i][0] * Hn[j][j][0] - (Hn[i][j][0] ** 2 + Hn[i][j][1] ** 2)
    return a, b, cdet3(Hn)[0]


def rmat(rows):
    return [[C(x) for x in r] for r in rows]


def cayley_about_u(t):
    """Rational rotation about u' = (1,1,1): R = (1 - A)^(-1)(1 + A), A = t [u']_x."""
    A = [[F(0), -t, t], [t, F(0), -t], [-t, t, F(0)]]
    I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
    M = [[I[i][j] - A[i][j] for j in range(3)] for i in range(3)]
    # inverse of a 3x3 rational matrix by adjugate
    def det(X):
        return (X[0][0] * (X[1][1] * X[2][2] - X[1][2] * X[2][1]) - X[0][1] * (X[1][0] * X[2][2] - X[1][2] * X[2][0])
                + X[0][2] * (X[1][0] * X[2][1] - X[1][1] * X[2][0]))
    d = det(M)
    adj = [[(M[(j + 1) % 3][(i + 1) % 3] * M[(j + 2) % 3][(i + 2) % 3]
             - M[(j + 1) % 3][(i + 2) % 3] * M[(j + 2) % 3][(i + 1) % 3]) for j in range(3)] for i in range(3)]
    Minv = [[adj[i][j] / d for j in range(3)] for i in range(3)]
    P = [[I[i][j] + A[i][j] for j in range(3)] for i in range(3)]
    return [[sum(Minv[i][k] * P[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


CYC = [[F(0), F(0), F(1)], [F(1), F(0), F(0)], [F(0), F(1), F(0)]]
PS = [[F(1, 3)] * 3 for _ in range(3)]


def sigma(x, y, c):
    """S3-equivariant real structure sigma_{x,y} = (x P_s + y P_d) o conj, x, y in {+1, -1}."""
    cb = [cconj(z) for z in c]
    out = []
    for i in range(3):
        s = Z
        for j in range(3):
            coef = x * PS[i][j] + y * ((1 if i == j else 0) - PS[i][j])
            s = cadd(s, cmul(C(coef), cb[j]))
        out.append(s)
    return out


def words(c, x, y, g):
    v0 = vac()
    sc_ = sigma(x, y, c)
    return addst(v0, omega_c_dag(c, v0), scalev(C(g), omega_c_dag(c, omega_c_dag(sc_, v0))))


def diag_word(c, g):
    """A family-basis word: sum_k (Omega_k^dag)^3 applied after the source; invariant under family
    permutations (up to the sign det P = N(P) / P), not under rotations about u'."""
    v0 = vac()
    base = addst(v0, omega_c_dag(c, v0))
    sq = lin([(ONE, omega_dag(k, omega_dag(k, omega_dag(k, base)))) for k in range(3)])
    return addst(base, scalev(C(g), sq))


def rotate(R, c):
    return [lin_c([cmul(C(R[i][j]), c[j]) for j in range(3)]) for i in range(3)]


def lin_c(xs):
    s = Z
    for x in xs:
        s = cadd(s, x)
    return s


def check_axial_rotation_is_symmetry_of_real_structure_words():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("synthesis.face-mass-form-unit-plus-gram")
    for t in (F(1, 2), F(-2, 7)):
        R = cayley_about_u(t)
        RT = [list(r) for r in zip(*R)]
        I = [[F(int(i == j)) for j in range(3)] for i in range(3)]
        assert [[sum(R[i][k] * RT[k][j] for k in range(3)) for j in range(3)] for i in range(3)] == I
        assert [sum(R[i][j] for j in range(3)) for i in range(3)] == [F(1)] * 3       # R u' = u'
        RC = [[sum(R[i][k] * CYC[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        CR = [[sum(CYC[i][k] * R[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
        assert RC == CR                                   # R commutes with the cyclic family shift
        assert R != I
        for c in ([C(1), C(0, 1), C(F(1, 2), F(1, 3))], [C(2, -1), C(F(1, 3)), C(0, F(-3, 4))]):
            Rc = rotate(R, c)
            for (x, y) in ((1, 1), (-1, 1), (1, -1), (-1, -1)):
                assert sigma(x, y, Rc) == rotate(R, sigma(x, y, c))
                H1, n1 = mass_form(words(c, x, y, F(2, 3)))
                H2, n2 = mass_form(words(Rc, x, y, F(2, 3)))
                assert charpoly(H1, n1) == charpoly(H2, n2)
            # a family-basis (S3-only) word sees the rotation
            H1, n1 = mass_form(diag_word(c, F(1, 2)))
            H2, n2 = mass_form(diag_word(Rc, F(1, 2)))
            assert charpoly(H1, n1) != charpoly(H2, n2)
            # but it does not see a cyclic family shift
            Pc = rotate(CYC, c)
            H3, n3 = mass_form(diag_word(Pc, F(1, 2)))
            assert charpoly(H1, n1) == charpoly(H3, n3)


def omega_dag_omega_sum(st):
    """V st with V = sum_k Omega_k^dag Omega_k."""
    return lin([(ONE, omega_dag(k, omega(k, st))) for k in range(3)])


def square_word(st):
    """sum_k (Omega_k^dag)^2 applied to st."""
    return lin([(ONE, omega_dag(k, omega_dag(k, st))) for k in range(3)])


def invariant_words(c, x, y, g):
    """A word built from the source, its real-structure image and the rotation-invariant face words
    sum_k Omega_k^dag Omega_k and sum_k (Omega_k^dag)^2."""
    v0 = vac()
    sc_ = sigma(x, y, c)
    one = omega_c_dag(c, v0)
    two = omega_c_dag(sc_, square_word(v0))
    return addst(v0, one, scalev(C(g), two), omega_dag_omega_sum(omega_c_dag(sc_, one)))


ROT_TS = (F(1, 2), F(-2, 7))
SAMPLE_CS = ([C(1), C(0, 1), C(F(1, 2), F(1, 3))], [C(2, -1), C(F(1, 3)), C(0, F(-3, 4))])
SIGNS_COV = ((1, 1), (-1, -1))
G_PLAIN, G_INV = F(2, 3), F(-1, 4)


def check_fock_rotation_covariance():
    premise("synthesis.coherent-face-vector-real-slices")
    premise("synthesis.face-mass-form-unit-plus-gram")
    n_cases = 0
    for t in ROT_TS:
        R = cayley_about_u(t)
        RR = rmat(R)
        RRT = rmat([list(r) for r in zip(*R)])
        # the rotation-invariant face words commute with the Fock rotation
        # sum_k (Omega_k^dag)^2 |0>: Omega_0^dag = a10^ a21^ - a11^ a20^ (and cyclically), so three
        # monomials per k with coefficients 1, -2, 1 and factorial weights 2! 2!, 1, 2! 2!: squared
        # norm 4 + 4 + 4 per k
        sq0 = square_word(vac())
        assert len(sq0) == 9 and inner(sq0, sq0) == C(36)
        assert transform(RR, sq0) == sq0
        for c in SAMPLE_CS:
            Rc = rotate(R, c)
            for (x, y) in SIGNS_COV:
                for build in (lambda z: words(z, x, y, G_PLAIN), lambda z: invariant_words(z, x, y, G_INV)):
                    n_cases += 1
                    psi = build(c)
                    Rpsi = transform(RR, psi)
                    assert Rpsi == build(Rc)                       # psi[Rc] = R^ psi[c]
                    H1, n1 = mass_form(psi)
                    H2, n2 = mass_form(Rpsi)
                    assert n1 == n2
                    assert H2 == cmatmul(cmatmul(RR, H1), RRT)     # H(R^ psi) = R H(psi) R^T
                    assert charpoly(H1, n1) == charpoly(H2, n2)
                psi = words(c, x, y, G_PLAIN)
                assert transform(RR, omega_dag_omega_sum(psi)) == omega_dag_omega_sum(transform(RR, psi))
    assert n_cases == 16


EXPORTS = {}
