"""Circulant charged leptons against the series' real neutrino sectors: exact checks.

Complex numbers are elements a + b s of Q(sqrt(-3)), s^2 = -3, held as pairs of Fractions; the cube
root of unity is w = (-1 + s)/2. The unnormalised Fourier vectors are f_k = (1, w^k, w^2k), with
|f_k|^2 = 3. For a unit family vector v the squared PMNS modulus is |<f_k|v>|^2 / 3.
(1) Every circulant c0 + c1 S + c2 S^2 (complex entries) has eigenvectors f_k, eigenvalue
    c0 + c1 w^k + c2 w^2k; a P12-invariant matrix has no component on A = S - S^T (the sign line);
    a circulant that is P12-invariant lies in span{1, J}; the neutrino paper's charged texture
    (J + d E)^2, d != 0, is not a circulant.
(2) For real orthogonal frames (Cayley transforms of rational antisymmetric matrices) the rows f_1 and
    f_2 have equal moduli in every column; a complex unitary frame (control) breaks it.
(3) The textures of the S3 -> S2 direction (real d, delta of both signs, alpha, M3), with or without
    a real P12-invariant addition, have the odd state (1,-1,0) as a Takagi vector, whose column has
    squared moduli (0, 1/2, 1/2) on (f_0, f_1, f_2).
(4) The NuFIT 6.0 three-sigma ranges (union of its four columns) exclude every assignment that (2)
    and (3) leave, and the surviving mu-tau reflection pattern forces sin^2 th23 = 1/2, cos delta = 0.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


# ---------- Q(sqrt(-3)) ----------
class Q3(object):
    __slots__ = ("a", "b")

    def __init__(self, a, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.a + o.a, self.b + o.b)
    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.a - o.a, self.b - o.b)

    def __neg__(self):
        return Q3(-self.a, -self.b)

    def __mul__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return Q3(self.a * o.a - 3 * self.b * o.b, self.a * o.b + self.b * o.a)
    __rmul__ = __mul__

    def conj(self):
        return Q3(self.a, -self.b)

    def norm2(self):
        return self.a * self.a + 3 * self.b * self.b

    def __eq__(self, o):
        o = o if isinstance(o, Q3) else Q3(o)
        return self.a == o.a and self.b == o.b


ZERO, ONE = Q3(0), Q3(1)
W = Q3(F(-1, 2), F(1, 2))                       # w = (-1 + sqrt(-3))/2


def wp(n):
    r = ONE
    for _ in range(n % 3):
        r = r * W
    return r


def fourier(k):
    return [wp(0), wp(k), wp(2 * k)]


def mat(rows):
    return [[x if isinstance(x, Q3) else Q3(x) for x in r] for r in rows]


def mmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(m)), ZERO) for j in range(p)] for i in range(n)]


def mvec(A, v):
    return [sum((A[i][t] * v[t] for t in range(len(v))), ZERO) for i in range(len(A))]


def meq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))


def dagger(A):
    return [[A[j][i].conj() for j in range(len(A))] for i in range(len(A[0]))]


def inner(u, v):                                 # <u|v>, antilinear in u
    return sum((u[i].conj() * v[i] for i in range(len(u))), ZERO)


I3 = mat([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
S = mat([[0, 1, 0], [0, 0, 1], [1, 0, 0]])       # (S x)_i = x_{i+1}
S2 = mmul(S, S)
P12 = mat([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
J = mat([[1, 1, 1]] * 3)
E = mat([[0, 0, 0], [0, 0, 0], [0, 0, 1]])


def lin(*terms):
    out = [[ZERO] * 3 for _ in range(3)]
    for c, M in terms:
        c = c if isinstance(c, Q3) else Q3(c)
        out = [[out[i][j] + c * M[i][j] for j in range(3)] for i in range(3)]
    return out


def lcg(seed):
    while True:
        seed = (1103515245 * seed + 12345) % 2147483648
        yield seed


def rq(g, lo=-9, hi=9):
    return F(lo + next(g) % (hi - lo + 1), 1 + next(g) % 7)


def rc(g):
    return Q3(rq(g), rq(g))


# ---------- real 3x3 helpers (Fractions) ----------
def rinv(M):
    n = len(M)
    A = [list(map(F, M[i])) + [F(int(i == j)) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [A[r][j] - f * A[c][j] for j in range(2 * n)]
    return [row[n:] for row in A]


def rmul(A, B):
    return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def rT(A):
    return [list(r) for r in zip(*A)]


def cayley(a, b, c):
    K = [[F(0), a, b], [-a, F(0), c], [-b, -c, F(0)]]
    Im = [[F(1) - K[i][j] if i == j else -K[i][j] for j in range(3)] for i in range(3)]
    Ip = [[F(1) + K[i][j] if i == j else K[i][j] for j in range(3)] for i in range(3)]
    return rmul(Im, rinv(Ip))


def col(O, j):
    return [Q3(O[i][j]) for i in range(3)]


def moduli_column(v):
    """3 |<f_k|v>|^2 / |v|^2 for k = 0, 1, 2 (v real or complex, unnormalised)."""
    nv = sum((x.norm2() for x in v), F(0))
    return [inner(fourier(k), v).norm2() / nv for k in range(3)]


# ---------- (1) ----------
def check_circulants_are_diagonal_in_the_fourier_basis():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    premise("synthesis.series-family-structures-give-no-lopsided-second-stage")
    g = lcg(20261101)
    ok = True
    for _ in range(8):
        c0, c1, c2 = rc(g), rc(g), rc(g)
        C = lin((c0, I3), (c1, S), (c2, S2))
        for k in range(3):
            lam = c0 + c1 * wp(k) + c2 * wp(2 * k)
            f = fourier(k)
            ok &= all(x == lam * y for x, y in zip(mvec(C, f), f))
        H = mmul(C, dagger(C))                    # the mass-squared matrix of a sqrt(m) circulant
        ok &= meq(mmul(S, H), mmul(H, S))
    GA.check("(i) circulants (and C C^dag) have the Fourier eigenvectors, any complex entries", ok)
    # the store's representative: eigenvalue 1 + 2 Re(beta w^k) is largest on f_0 for small delta > 0
    # (in Q(sqrt-3): beta = (1 + t s)/2 with t > 0 small gives Re(beta w^k) = 1/2, (-1 - 3t)/4, (-1 + 3t)/4)
    t = F(1, 20)
    beta = Q3(F(1, 2), t / 2)
    ev = [(beta * wp(k)).a for k in range(3)]
    GA.check("(i) the store's representative puts the largest root on the democratic line f_0",
             ev[0] > ev[2] > ev[1])
    # isotypic content: the sign line A = S - S^T
    A = lin((1, S), (-1, S2))
    PAP = mmul(mmul(P12, A), P12)
    GA.check("(i) the sign line is odd under P12", meq(PAP, lin((-1, A))))
    ok2 = True
    for _ in range(6):
        M = [[rc(g) for _ in range(3)] for _ in range(3)]
        Msym = lin((F(1, 2), M), (F(1, 2), mmul(mmul(P12, M), P12)))   # P12-invariant part
        ip = sum((A[i][j].conj() * Msym[i][j] for i in range(3) for j in range(3)), ZERO)
        ok2 &= ip == ZERO
    GA.check("(i) a P12-invariant matrix has no component on the sign line", ok2)
    ok3 = True
    for _ in range(6):
        a0, b = rc(g), rc(g)
        H = lin((a0, I3), (b, S), (b.conj(), S2))   # Hermitian circulant when a0 real
        inv = meq(mmul(mmul(P12, H), P12), H)
        ok3 &= inv == (b.b == 0)
        if b.b == 0:
            ok3 &= meq(H, lin((a0 - b, I3), (b, J)))
    GA.check("(i) a Hermitian circulant is P12-invariant exactly when it lies in span{1, J}", ok3)
    ok4, ok5 = True, True
    for dc in [F(286, 1000), F(-2), F(1, 3), F(-5, 7)]:
        Me = lin((1, J), (dc, E))
        He = mmul(Me, dagger(Me))
        ok4 &= not meq(mmul(S, He), mmul(He, S))
        ok4 &= He[2][2] == 2 + (1 + dc) ** 2 and He[0][0] == 3
        ok5 &= meq(mmul(mmul(P12, He), P12), He)
    GA.check("(i) the texture (J + delta_c E)^2 is not a circulant (delta_c = 0.286, -2, 1/3, -5/7)", ok4)
    GA.check("(i) ... and is P12-invariant", ok5)


# ---------- (2) ----------
def check_real_neutrino_frames_give_equal_conjugate_rows():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    g = lcg(7)
    ok, uni = True, True
    for _ in range(10):
        O = cayley(rq(g), rq(g), rq(g))
        orth = rmul(rT(O), O) == [[F(int(i == j)) for j in range(3)] for i in range(3)]
        ok &= orth
        rows = [[F(0)] * 3 for _ in range(3)]
        for j in range(3):
            m = moduli_column(col(O, j))
            ok &= m[1] == m[2]
            uni &= sum(m) == 3
            for k in range(3):
                rows[k][j] = m[k]
        uni &= all(sum(r) == 3 for r in rows)
    GA.check("(ii) real orthogonal frames: |U_{f1 j}| = |U_{f2 j}| for every column (10 frames)", ok)
    GA.check("(ii) the overlaps form a unistochastic matrix (rows and columns sum to 1)", uni)
    # column phases (Takagi factors i) do not change moduli
    v = col(cayley(F(1, 2), F(-1, 3), F(2, 5)), 0)
    vi = [x * Q3(0, F(1, 3)) * Q3(0, 1) for x in v]   # multiply by s^2/3 = -1: a sign
    GA.check("(ii) a column phase leaves the moduli unchanged", moduli_column(v) == moduli_column(vi))
    O = cayley(F(1, 2), F(-1, 3), F(2, 5))
    fp = [moduli_column(col(O, j)) for j in range(3)]
    GA.check("(ii) fingerprint frame: 3|U|^2 columns (2621161, 1500661, 1500661), (982081, 2320201, 2320201), "
             "(2019241, 1801621, 1801621) over 1874161",
             fp == [[F(2621161, 1874161), F(1500661, 1874161), F(1500661, 1874161)],
                    [F(982081, 1874161), F(2320201, 1874161), F(2320201, 1874161)],
                    [F(2019241, 1874161), F(1801621, 1874161), F(1801621, 1874161)]])
    # control: a complex unitary frame breaks the equality (realness is needed)
    u = [Q3(1), Q3(0, 1), Q3(2)]                  # (1, sqrt(-3), 2): complex
    m = moduli_column(u)
    GA.check("(ii) control: a complex frame vector gives 3|U|^2 = (3/2, 3/8, 9/8), |U_{f1}| != |U_{f2}|",
             m == [F(3, 2), F(3, 8), F(9, 8)] and m[1] != m[2])


# ---------- (3) ----------
def neutrino_texture(d, delta, alpha, M3, X=None):
    """m = mD MR^{-1} mD^T, mD = d(J + delta(E + X)), MR = alpha Pi + M3 J/3 (rational, real)."""
    Jr = [[F(1)] * 3 for _ in range(3)]
    Er = [[F(0)] * 3 for _ in range(3)]
    Er[2][2] = F(1)
    Xr = X or [[F(0)] * 3 for _ in range(3)]
    mD = [[d * (Jr[i][j] + delta * (Er[i][j] + Xr[i][j])) for j in range(3)] for i in range(3)]
    Pi = [[F(int(i == j)) - F(1, 3) for j in range(3)] for i in range(3)]
    MR = [[alpha * Pi[i][j] + M3 * Jr[i][j] / 3 for j in range(3)] for i in range(3)]
    return rmul(rmul(mD, rinv(MR)), rT(mD))


def check_odd_state_column_for_s2_invariant_neutrino_sectors():
    premise("synthesis.theta23-at-s3-s2-direction")
    premise("neutrino.breaking-relation")
    premise("synthesis.residual-s2-decouples-first-family-from-ckm-and-pmns")
    odd = [F(1), F(-1), F(0)]
    P = [[F(0), F(1), F(0)], [F(1), F(0), F(0)], [F(0), F(0), F(1)]]
    ok = True
    cases = [(F(1), F(286, 1000), F(1), F(176)), (F(1), F(286, 1000), F(1), F(4695, 10)),
             (F(1), F(-286, 1000), F(1), F(5307, 10)), (F(2, 3), F(1, 7), F(3), F(66))]
    for (d, de, al, M3) in cases:
        m = neutrino_texture(d, de, al, M3)
        ok &= rmul(m, [[x] for x in odd]) == [[F(0)]] * 3          # odd state in the kernel
        ok &= rmul(rmul(P, m), P) == m
    GA.check("(iii) S3 -> S2 textures (both roots, both signs): (1,-1,0) in the kernel, P12-invariant", ok)
    ok = True
    Xe = [[F(1, 5), F(2, 9), F(1, 3)], [F(2, 9), F(1, 5), F(1, 3)], [F(1, 3), F(1, 3), F(-1, 4)]]
    m = neutrino_texture(F(1), F(286, 1000), F(1), F(66), Xe)     # P12-invariant real addition
    v = rmul(m, [[x] for x in odd])
    lam = v[0][0] / odd[0]
    ok &= all(v[i][0] == lam * odd[i] for i in range(3))
    GA.check("(iii) with a real P12-invariant addition (1,-1,0) is still an eigenvector", ok)
    mods = moduli_column([Q3(x) for x in odd])
    GA.check("(iii) the odd state's column has squared moduli (0, 1/2, 1/2) on (f_0, f_1, f_2)",
             [x / 3 for x in mods] == [F(0), F(1, 2), F(1, 2)])
    # the even states (a, a, b): f_1 and f_2 moduli (b - a)^2/3, f_0 modulus (2a + b)^2/3
    a, b = F(3, 7), F(-5, 11)
    mods = moduli_column([Q3(a), Q3(a), Q3(b)])
    nv = 2 * a * a + b * b
    GA.check("(iii) even states: 3|<f_0|v>|^2 = (2a+b)^2, 3|<f_{1,2}|v>|^2 = (a-b)^2 (per |v|^2)",
             mods == [(2 * a + b) ** 2 / nv, (a - b) ** 2 / nv, (a - b) ** 2 / nv])


# ---------- (4) ----------
S13_MIN, S13_MAX = F(2023, 100000), F(2409, 100000)
S23_MIN, S23_MAX = F(430, 1000), F(597, 1000)
S12_MIN, S12_MAX = F(275, 1000), F(345, 1000)


def cadd(x, y): return (x[0] + y[0], x[1] + y[1])
def cmul(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def cn2(x): return x[0] * x[0] + x[1] * x[1]


def pyth(p, q):                                  # rational point on the unit circle
    n = p * p + q * q
    return F(p * p - q * q, n), F(2 * p * q, n)


def check_assignments_against_the_global_fit():
    premise("synthesis.koide-channel-phase-is-no-symmetry-angle")
    c13sq_min = 1 - S13_MAX
    Ue3_max = S13_MAX
    Umu3_min = S23_MIN * c13sq_min
    Utau3_min = (1 - S23_MAX) * c13sq_min
    GA.check("(iv) bounds: |U_e3|^2 <= 0.0241 < 0.393 < |U_tau3|^2, 0.419 < |U_mu3|^2",
             Ue3_max < F(241, 10000) and Utau3_min > F(393, 1000) and Umu3_min > F(419, 1000))
    GA.check("(iv) exact bound values 0.02409, 0.4196413, 0.39329173",
             Ue3_max == F(2409, 100000) and Umu3_min == F(4196413, 10 ** 7) and Utau3_min == F(39329173, 10 ** 8))
    # tau on f_0: e and mu on the conjugate pair, so |U_e3| = |U_mu3|: empty intersection
    GA.check("(iv) tau on f_0 (the store's representative): |U_e3| = |U_mu3| is excluded",
             Ue3_max < Umu3_min)
    GA.check("(iv) mu on f_0: |U_e3| = |U_tau3| is excluded", Ue3_max < Utau3_min)
    # e on f_0 with a P12-invariant real neutrino sector: one e-row entry vanishes,
    # but every |U_ej|^2 is bounded below by a positive number
    Ue_min = min(c13sq_min * (1 - S12_MAX), c13sq_min * S12_MIN, S13_MIN)
    GA.check("(iv) e on f_0 with a P12-invariant neutrino sector: U_{e,odd} = 0 against min |U_ej|^2 = 0.02023",
             Ue_min >= F(202, 10000) and Ue_min == F(2023, 100000))
    # mu-tau reflection: |U_mu j| = |U_tau j| forces s23^2 = c23^2 and c12 s12 s13 cos(delta) = 0.
    ok = True
    first = None
    for (p12, p13, p23, pd) in [((2, 1), (7, 1), (3, 2), (5, 2)), ((3, 1), (9, 2), (4, 3), (1, 3)),
                                ((5, 2), (11, 1), (2, 1), (7, 4))]:
        c12, s12 = pyth(*p12)
        c13, s13 = pyth(*p13)
        c23, s23 = pyth(*p23)
        cd, sd = pyth(*pd)
        e = (cd, sd)
        Umu1 = cadd((-s12 * c23, F(0)), cmul((-c12 * s23 * s13, F(0)), e))
        Utau1 = cadd((s12 * s23, F(0)), cmul((-c12 * c23 * s13, F(0)), e))
        lhs = cn2(Umu1) - cn2(Utau1)
        first = lhs if first is None else first
        rhs = (s12 ** 2 - c12 ** 2 * s13 ** 2) * (c23 ** 2 - s23 ** 2) + 4 * s12 * c12 * s13 * s23 * c23 * cd
        ok &= lhs == rhs
        ok &= (c13 ** 2 * s23 ** 2) - (c13 ** 2 * c23 ** 2) == c13 ** 2 * (s23 ** 2 - c23 ** 2)
    GA.check("(iv) |U_mu1|^2 - |U_tau1|^2 = (s12^2 - c12^2 s13^2)(c23^2 - s23^2) + 4 s12 c12 s13 s23 c23 cos delta", ok)
    GA.check("(iv) fingerprint of the first point: -1723393/5890625", first == F(-1723393, 5890625))


# ---------- (iii') complex P12-invariant sectors and every placement ----------
def cinv(M):
    """Inverse of a 3x3 matrix over Q(sqrt(-3)) by the adjugate."""
    def cof(i, j):
        r = [a for a in range(3) if a != i]
        c = [b for b in range(3) if b != j]
        return M[r[0]][c[0]] * M[r[1]][c[1]] - M[r[0]][c[1]] * M[r[1]][c[0]]
    det = sum((M[0][j] * cof(0, j) * (1 if j % 2 == 0 else -1) for j in range(3)), ZERO)
    n = det.norm2()
    dinv = Q3(det.a / n, -det.b / n)
    return [[cof(j, i) * (1 if (i + j) % 2 == 0 else -1) * dinv for j in range(3)] for i in range(3)]


def p12_sym(g):
    """A random complex symmetric P12-invariant matrix: entries a, b, c, e with M = [[a,b,c],[b,a,c],[c,c,e]]."""
    a, b, c, e = rc(g), rc(g), rc(g), rc(g)
    return [[a, b, c], [b, a, c], [c, c, e]]


def check_every_placement_excluded_for_p12_invariant_sectors():
    premise("synthesis.theta23-at-s3-s2-direction")
    premise("synthesis.rung-field-coupling-to-its-conjugate-is-the-second-family-matrix")
    g = lcg(4242)
    odd = [Q3(1), Q3(-1), Q3(0)]
    ok_eig, ok_herm, ok_inv = True, True, True
    used = 0
    for _ in range(6):
        # Dirac matrix of the covariant completion, alpha Y + conj(beta) Ytilde, with complex frame
        # coefficients and complex symmetric P12-invariant family matrices; complex M_R
        al, be = rc(g), rc(g)
        Y, Yt, MR = p12_sym(g), p12_sym(g), p12_sym(g)
        MD = lin((al, Y), (be.conj(), Yt))
        try:
            MRi = cinv(MR)
        except ZeroDivisionError:
            continue
        m = mmul(mmul(MD, MRi), [[MD[j][i] for j in range(3)] for i in range(3)])
        used += 1
        ok_inv &= meq(mmul(mmul(P12, m), P12), m)
        mv = mvec(m, odd)
        lam = mv[0]
        if used == 1:
            first_lam = lam
        ok_eig &= all(x == lam * y for x, y in zip(mv, odd))
        hv = mvec(mmul(m, dagger(m)), odd)
        ok_herm &= all(x == hv[0] * y for x, y in zip(hv, odd))
    GA.check("(iii) fingerprint: first instance's odd eigenvalue -39121365/3565744 - (43812753/1782872) sqrt(-3)",
             first_lam == Q3(F(-39121365, 3565744), F(-43812753, 1782872)))
    GA.check("(iii) complex P12-invariant m = MD MR^-1 MD^T (MD = alpha Y + conj(beta) Ytilde, MR complex) is P12-invariant",
             ok_inv)
    GA.check("(iii) (1,-1,0) is an eigenvector of every such m and of m m^dag (so a Takagi vector up to a phase)",
             ok_eig and ok_herm and used == 6 and not all(x.b == 0 for r in m for x in r))
    # the electron row then holds 0 (electron on f_0) or 1/2 (on f_1 or f_2); the fit ranges
    c13_lo, c13_hi = 1 - S13_MAX, 1 - S13_MIN
    e1 = ((1 - S12_MAX) * c13_lo, (1 - S12_MIN) * c13_hi)
    e2 = (S12_MIN * c13_lo, S12_MAX * c13_hi)
    e3 = (S13_MIN, S13_MAX)
    GA.check("(iv) |U_e1|^2 in [0.63922, 0.71033], |U_e2|^2 in [0.26838, 0.33802], |U_e3|^2 in [0.02023, 0.02409]",
             e1 == (F(655, 1000) * F(97591, 100000), F(725, 1000) * F(97977, 100000))
             and e2 == (F(275, 1000) * F(97591, 100000), F(345, 1000) * F(97977, 100000))
             and F(6392, 10000) < e1[0] and e1[1] < F(7104, 10000))
    outside = all(not (lo <= v <= hi) for v in [F(0), F(1, 2)] for (lo, hi) in [e1, e2, e3])
    GA.check("(iv) neither 0 nor 1/2 lies in any electron-row range: every placement excluded for every P12-invariant sector",
             outside)


if __name__ == "__main__":
    for fn in [check_circulants_are_diagonal_in_the_fourier_basis,
               check_real_neutrino_frames_give_equal_conjugate_rows,
               check_odd_state_column_for_s2_invariant_neutrino_sectors,
               check_assignments_against_the_global_fit,
               check_every_placement_excluded_for_p12_invariant_sectors]:
        fn()
    print("FAILURES", GA.FAILURES)
