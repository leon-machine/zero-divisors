"""synthesis.light-pair-split-needs-broken-source-stabiliser: exact checks.

Six bosonic face modes a_p, p = (i, A), i a family index, A a spinor slot; states are finite
combinations of (a^dag)^m |0> with complex-rational coefficients (pairs of Fractions);
Theta_k = (1/2) eps_kij eps_AB and Omega_k = sum Theta_k[p,q] a_p a_q as in the skeleton theorem;
H_kl = (1/2)<Omega_k^dag Omega_l + Omega_l Omega_k^dag> is the mass form (unnormalised here, divided
by <psi|psi> where compared). A family matrix U acts on states by the Fock map
a^dag_{iA} -> sum_j U[j][i] a^dag_{jA}. Checks:
  (a) covariance: H(U psi) = N H(psi) N^dag with N = conj(det U) U, and U Omega(c)^dag = Omega(N c)^dag U,
      for several rational unitaries (det 1 and det != 1) on generic states;
  (b) Schur: states invariant under the Fock maps of the stabiliser {U : N(U) v = v} of one face
      vector v, built from Omega(v)^dag and the U(3)-invariant word V = sum_k Omega_k^dag Omega_k, have
      H = h_v P_v + h_perp (1 - P_v): the light pair is exactly degenerate; two stabiliser elements
      already have commutant span{P_v, 1 - P_v};
  (c) these states are not Gaussian: an ordered truncated four-point function is nonzero;
  (d) controls: a state breaking the stabiliser splits the pair; words using the real structure
      (Omega(conj v)^dag) split it for complex v (generic and isotropic) and not for real v.
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


def V(st):
    return lin([(ONE, omega_dag(k, omega(k, st))) for k in range(3)])


def normalised_H(psi):
    H, n = mass_form(psi)
    assert n[1] == 0 and n[0] > 0
    return [[(H[k][l][0] / n[0], H[k][l][1] / n[0]) for l in range(3)] for k in range(3)]


def cubic_disc(H):
    """Discriminant of the characteristic polynomial of a Hermitian 3x3 (zero iff a repeated eigenvalue)."""
    a = sum(H[i][i][0] for i in range(3))
    b = F(0)
    for i in range(3):
        for j in range(i + 1, 3):
            b += H[i][i][0] * H[j][j][0] - (H[i][j][0] ** 2 + H[i][j][1] ** 2)
    c = cdet3(H)[0]
    B, Cc, D = -a, b, -c
    return 18 * B * Cc * D - 4 * B ** 3 * D + B ** 2 * Cc ** 2 - 4 * Cc ** 3 - 27 * D ** 2


def reflection(w):
    nw = sum(x[0] * x[0] + x[1] * x[1] for x in w)
    return [[cadd(C(1 if i == j else 0), cmul(C(F(-2) / nw), cmul(w[i], cconj(w[j])))) for j in range(3)]
            for i in range(3)]


def is_unitary(U):
    return cmatmul(U, cdagger(U)) == [[C(1 if i == j else 0) for j in range(3)] for i in range(3)]


def Nof(U):
    d = cconj(cdet3(U))
    return [[cmul(d, U[i][j]) for j in range(3)] for i in range(3)]


def cmatvec(M, v):
    return [lin_c([cmul(M[i][j], v[j]) for j in range(3)]) for i in range(3)]


def lin_c(xs):
    s = Z
    for x in xs:
        s = cadd(s, x)
    return s


SU2_A = [[C(F(1, 2), F(1, 2)), C(F(-1, 2), F(-1, 2)), C(0)], [C(F(1, 2), F(-1, 2)), C(F(1, 2), F(-1, 2)), C(0)],
         [C(0), C(0), C(1)]]
SU2_B = [[C(F(3, 5)), C(0, F(4, 5)), C(0)], [C(0, F(4, 5)), C(F(3, 5)), C(0)], [C(0), C(0), C(1)]]
GEN_U = cmatmul([[C(F(3, 5), F(4, 5)), C(0), C(0)], [C(0), C(0, 1), C(0)], [C(0), C(0), C(-1)]],
                [[C(F(5, 13)), C(0), C(F(-12, 13))], [C(0), C(1), C(0)], [C(F(12, 13)), C(0), C(F(5, 13))]])
PERM_U = [[C(0), C(0), C(0, 1)], [C(1), C(0), C(0)], [C(0), C(1), C(0)]]

GENERIC = [
    {(0, 0, 0, 0, 0, 0): C(1), (1, 0, 0, 1, 0, 0): C(2, -1), (0, 1, 1, 0, 0, 0): C(0, F(3, 2)),
     (0, 0, 1, 1, 1, 0): C(F(-2, 3)), (2, 1, 0, 0, 0, 1): C(F(1, 5), F(-1, 7))},
    {(1, 1, 1, 1, 0, 0): C(1), (0, 0, 1, 1, 1, 1): C(-1, 2), (1, 0, 0, 0, 0, 1): C(F(3, 4)),
     (0, 2, 0, 1, 0, 0): C(1, 1)},
]


def check_covariance():
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("families.skeleton-rank-one-plus-ordering-shift")
    for U in (SU2_A, SU2_B, GEN_U, PERM_U):
        assert is_unitary(U)
        N = Nof(U)
        for psi in GENERIC:
            Up = transform(U, psi)
            H, n = mass_form(psi)
            H2, n2 = mass_form(Up)
            assert n == n2
            assert H2 == cmatmul(cmatmul(N, H), cdagger(N))
            c = [C(1, -2), C(F(1, 3)), C(0, 1)]
            Nc = cmatmul(N, [[x] for x in c])
            Nc = [r[0] for r in Nc]
            assert transform(U, omega_c_dag(c, psi)) == omega_c_dag(Nc, Up)
    assert cdet3(GEN_U) != C(1) and cdet3(PERM_U) != C(1)
    H, n = mass_form(transform(GEN_U, GENERIC[0]))                  # pinned values
    assert n == C(F(388753, 44100)) and H[0][0] == C(F(74437067, 2981160))


def truncated4(psi, ops):
    """Ordered truncated four-point function for a zero-mean state; ops are ('c'|'a', mode)."""
    def apply(op, st):
        return cre(op[1], st) if op[0] == 'c' else ann(op[1], st)
    n = inner(psi, psi)[0]
    def w(seq):
        st = psi
        for op in reversed(seq):
            st = apply(op, st)
        val = inner(psi, st)
        return (val[0] / n, val[1] / n)
    for op in ops:
        assert w([op]) == Z                                     # zero mean
    x1, x2, x3, x4 = ops
    t = w(ops)
    for (p, q), (r, s) in [((x1, x2), (x3, x4)), ((x1, x3), (x2, x4)), ((x1, x4), (x2, x3))]:
        pr = cmul(w([p, q]), w([r, s]))
        t = (t[0] - pr[0], t[1] - pr[1])
    return t


def invariant_states():
    v0 = vac()
    O2 = lambda st: omega_dag(2, st)
    psi1 = addst(v0, O2(O2(O2(v0))))                              # one source, non-Gaussian amplitudes
    psi2 = addst(O2(v0), scalev(C(F(1, 3)), V(O2(O2(v0)))), scalev(C(0, 2), O2(V(O2(O2(v0))))))
    return psi1, psi2


def check_stabiliser_invariant_states_degenerate():
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("families.skeleton-rank-one-plus-ordering-shift")
    premise("families.imported-squeezed-vacuum-bosonic-pairing")
    e = 2
    for psi in invariant_states():
        for U in (SU2_A, SU2_B):
            assert Nof(U)[e][e] == C(1) and transform(U, psi) == psi
        H = normalised_H(psi)
        assert H[0][0] == H[1][1] and H[0][1] == Z and H[0][2] == Z and H[1][2] == Z
        assert H[2][2] != H[0][0]
        assert cubic_disc(H) == 0
        if psi == invariant_states()[0]:
            assert (H[0][0], H[2][2]) == (C(F(361, 145)), C(F(461, 29)))
        # non-Gaussian: nonzero ordered truncated four-point function (Wick's theorem fails)
        t = truncated4(psi, [('c', 0), ('c', 3), ('a', 0), ('a', 3)])
        assert t != Z
    # a complex face vector v and U(3)-covariant words: Omega(v)^dag and V
    v = [C(1), C(0, 1), C(F(1, 2), F(1, 3))]
    w1, w2 = [C(0, 1), C(1), C(0)], [C(F(-1, 2), F(1, 3)), C(0), C(1)]
    w3 = [cadd(w1[k], cmul(C(1, 2), w2[k])) for k in range(3)]       # a third direction in v-perp
    for w in (w1, w2, w3):
        assert lin_c([cmul(cconj(v[k]), w[k]) for k in range(3)]) == Z        # w orthogonal to v
    S1 = cmatmul(reflection(w1), reflection(w2))
    S2 = cmatmul(reflection(w2), reflection(w3))
    assert cmatmul(S1, S2) != cmatmul(S2, S1)
    v0 = vac()
    Ov = lambda st: omega_c_dag(v, st)
    psiU = addst(v0, Ov(v0), scalev(C(F(2, 3)), Ov(Ov(v0))), scalev(C(F(1, 5)), V(Ov(Ov(v0)))))
    for S in (S1, S2):
        assert is_unitary(S) and cdet3(S) == C(1) and cmatvec(Nof(S), v) == v
        assert transform(S, psiU) == psiU
    H = normalised_H(psiU)
    assert cubic_disc(H) == 0
    lam = None                                                    # H acts as one scalar on v-perp
    for w in (w1, w2, w3):
        Hw = cmatvec(H, w)
        k = next(i for i in range(3) if w[i] != Z)
        den = w[k][0] ** 2 + w[k][1] ** 2
        q = cmul(Hw[k], cconj(w[k]))
        q = (q[0] / den, q[1] / den)
        assert all(Hw[i] == cmul(q, w[i]) for i in range(3))
        lam = q if lam is None else lam
        assert q == lam
    Hv = cmatvec(H, v)
    hv = cmul(Hv[0], cconj(v[0]))
    assert all(Hv[i] == cmul(hv, v[i]) for i in range(3)) and hv != lam   # v is an eigenvector, other value
    # commutant of {N(S1), N(S2)} in M_3(C) is two-dimensional (span{P_v, 1 - P_v})
    rows = []
    for S in (Nof(S1), Nof(S2)):
        for i in range(3):
            for j in range(3):
                re, im = [F(0)] * 18, [F(0)] * 18
                for k in range(3):
                    # (X S - S X)_{ij} = sum_k X_ik S_kj - S_ik X_kj ; X_ab = x[2(3a+b)] + i x[2(3a+b)+1]
                    for (a, b, s) in ((i, k, S[k][j]), (k, j, (-S[i][k][0], -S[i][k][1]))):
                        idx = 2 * (3 * a + b)
                        re[idx] += s[0]; im[idx] += s[1]
                        re[idx + 1] += -s[1]; im[idx + 1] += s[0]
                rows.append(re); rows.append(im)
    assert 18 - GA.mat_rank(rows) == 4                            # real dimension 4 = complex dimension 2


def check_breaking_controls():
    premise("synthesis.face-mass-form-unit-plus-gram")
    premise("synthesis.coherent-face-vector-real-slices")
    v0 = vac()
    psi1 = invariant_states()[0]
    psi3 = addst(psi1, omega_dag(0, omega_dag(0, v0)))             # breaks the stabiliser
    assert cubic_disc(normalised_H(psi3)) == F(92252253077913600, 14976071831449)
    def real_structure_words(v):
        vb = [cconj(x) for x in v]
        return addst(v0, omega_c_dag(v, v0), scalev(C(F(2, 3)), omega_c_dag(v, omega_c_dag(vb, v0))))
    complex_v = [C(1), C(0, 1), C(F(1, 2), F(1, 3))]
    isotropic_v = [C(1), C(0, 1), C(0)]                              # sum v_k^2 = 0
    real_v = [C(1), C(2), C(F(-1, 2))]
    assert lin_c([cmul(x, x) for x in isotropic_v]) == Z
    assert cubic_disc(normalised_H(real_structure_words(complex_v))) != 0
    assert cubic_disc(normalised_H(real_structure_words(isotropic_v))) != 0
    assert cubic_disc(normalised_H(real_structure_words(real_v))) == 0
    # the same words without the real structure (Omega(v)^dag twice) stay degenerate for complex v
    Ov = lambda st: omega_c_dag(complex_v, st)
    assert cubic_disc(normalised_H(addst(v0, Ov(v0), scalev(C(F(2, 3)), Ov(Ov(v0)))))) == 0


EXPORTS = {}
