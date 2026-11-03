"""synthesis.twistor-form-states-only-off-the-real-slice: exact checks on the store's own Sigma.

The twistor form is rebuilt as the stored construction defines it (correspondence.fock-model-
complexified-ascended-algebra, correspondence.chevalley-pairing, correspondence.reality-conjugation-
twistor-form-factor): the Fock model on Lambda W with the wedge-plus-contraction operator C(v)
(c = sqrt(2) C, a positive rescaling that never changes a sign), the Chevalley pairing B, the real
orthonormal basis a1, a2, b1, ..., b4 with w3 = b3 + i b4, kappa = Gamma C(b4) J, and
Sigma(Z1, Z2) = mu B(kappa Z1, Z2) on CS in the t-basis, with the phase mu of the stored clause (2)
(here lambda = 1, mu = 2 > 0). The chart is the stored one: the graph line {A pi + pi} with the stored
bases pi1, pi2, e1, e2 and m(A) read through the spinor identification Psi. The Minkowski complement
of the Witt pair is e0 = a2, e1 = b2, e2 = b3, e3 = b4.
check_store_sigma_and_real_lines: Sigma Hermitian, rank four, both halves null, lambda = 1; the lines of
real points are Sigma-null.
check_restricted_form_is_imaginary_part: the Gram matrix of Sigma on the line of x + i y does not depend on
x, has determinant 4 Q(y) and trace 4 y^0 in the stored line basis (definite iff Q(y) > 0, positive iff
moreover y^0 > 0; split iff Q(y) < 0; rank one iff y null and nonzero).
check_imaginary_boost_half_strip: x(theta) = rho cos(theta) e1 + i rho sin(theta) e0 gives Gram 2 rho sin(theta)
times the identity: positive on 0 < theta < pi, negative on pi < theta < 2 pi, null at 0 and pi.
"""
from fractions import Fraction
from fractions import Fraction as F
from itertools import combinations
import GA as g
from tp_premise import premise

ZERO, ONE, I = g.QI(0), g.QI(1), g.QI(0, 1)


def zeros(n, m):
    return [[g.QI(0) for _ in range(m)] for _ in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscal(c, A):
    c = g.QI(c) if not isinstance(c, g.QI) else c
    return [[c * x for x in row] for row in A]


mmul = g.field_mat_mul


def pc(m):
    return bin(m).count("1")


def sgn_below(mask, i):
    return g.QI(-1) if pc(mask & ((1 << i) - 1)) % 2 else g.QI(1)


def wedge_op(i):
    M = zeros(8, 8)
    for m in range(8):
        if not (m >> i) & 1:
            M[m | (1 << i)][m] = sgn_below(m, i)
    return M


def contract_op(i):
    M = zeros(8, 8)
    for m in range(8):
        if (m >> i) & 1:
            M[m & ~(1 << i)][m] = sgn_below(m, i)
    return M


AOPS = [wedge_op(i) for i in range(3)]
BOPS = [contract_op(i) for i in range(3)]


def C_of(v):
    M = zeros(8, 8)
    for i in range(3):
        if v[i]:
            M = madd(M, mscal(v[i], AOPS[i]))
        if v[3 + i]:
            M = madd(M, mscal(v[3 + i], BOPS[i]))
    return M


def ip6(u, v):
    return sum((u[i] * v[3 + i] + u[3 + i] * v[i] for i in range(3)), g.QI(0))


def basis6(k):
    v = [g.QI(0)] * 6
    v[k] = g.QI(1)
    return v


EPSK = {0: 1, 1: 1, 2: -1, 3: -1}


def wedge_sign(S, T):
    vals = [x for x in range(3) if (S >> x) & 1] + [x for x in range(3) if (T >> x) & 1]
    inv = sum(1 for i in range(len(vals)) for j in range(i + 1, len(vals)) if vals[i] > vals[j])
    return g.QI(-1) if inv % 2 else g.QI(1)


def B_mono(S, T):
    if (S | T) != 7 or (S & T):
        return g.QI(0)
    return g.QI(EPSK[pc(S)]) * wedge_sign(S, T)


def B_pair(x, y):
    out = g.QI(0)
    for S in range(8):
        if x[S]:
            for T in range(8):
                if y[T]:
                    out = out + x[S] * y[T] * B_mono(S, T)
    return out


def e8(mask):
    v = [g.QI(0)] * 8
    v[mask] = g.QI(1)
    return v


def apply_op(M, x):
    return [sum((M[i][j] * x[j] for j in range(8)), g.QI(0)) for i in range(8)]


H = g.QI(Fraction(1, 2))
REAL = [[H, 0, 0, 1, 0, 0], [0, H, 0, 0, 1, 0], [H, 0, 0, -1, 0, 0], [0, H, 0, 0, -1, 0],
        [0, 0, H, 0, 0, -1], [0, 0, g.QI(0, Fraction(-1, 2)), 0, 0, g.QI(0, -1)]]
REAL = [[g.QI(x) if not isinstance(x, g.QI) else x for x in v] for v in REAL]   # a1 a2 b1 b2 b3 b4
GAMMA = zeros(8, 8)
for m_ in range(8):
    GAMMA[m_][m_] = g.QI(-1) if pc(m_) % 2 else g.QI(1)
KMAT = mmul(GAMMA, C_of(REAL[5]))


def kappa(x):
    return apply_op(KMAT, [xi.conj() for xi in x])


t2 = [g.QI(0)] * 8
t2[5] = g.QI(-1)
T_VECS = [e8(0), e8(6), t2, e8(3)]
TP = [1, 2, 4, 7]
SIG = [[B_pair(kappa(T_VECS[i]), T_VECS[j]) for j in range(4)] for i in range(4)]
lam = None
for S in range(8):
    for T in range(8):
        b = B_mono(S, T)
        if b:
            lam = B_pair(kappa(e8(S)), kappa(e8(T))).conj() / b
            break
    if lam is not None:
        break
LAM = (lam * g.QI(2)).conj()
MU = g.QI(0, 1) if LAM == g.QI(-1) else ONE + LAM.conj()
HH = [[MU * SIG[i][j] for j in range(4)] for i in range(4)]

Bst = [[B_pair(e8(TP[i]), T_VECS[j]) for j in range(4)] for i in range(4)]
Binv = [g.field_solve([r[:] for r in Bst], [ONE if r == j else ZERO for r in range(4)]) for j in range(4)]
Binv = [[Binv[j][i] for j in range(4)] for i in range(4)]


def Psi(v):
    Cv = C_of(v)
    G = [[B_pair(e8(TP[i]), apply_op(Cv, e8(TP[j]))) for j in range(4)] for i in range(4)]
    P = zeros(4, 4)
    for k in range(4):
        for l in range(4):
            P[k][l] = sum((Binv[k][i] * G[i][j] * Binv[l][j] for i in range(4) for j in range(4)), g.QI(0))
    return P


PSI = [Psi(basis6(k)) for k in range(6)]
PSIMAT_T = [[[PSI[k][0][1], PSI[k][0][2], PSI[k][0][3], PSI[k][1][2], PSI[k][1][3], PSI[k][2][3]][c]
             for k in range(6)] for c in range(6)]
N0, NINF = PSI[0], PSI[3]
PI1 = [g.QI(0), g.QI(0), g.QI(-1), g.QI(0)]
PI2 = [g.QI(0), g.QI(0), g.QI(0), g.QI(1)]
E1 = [g.QI(1), g.QI(0), g.QI(0), g.QI(0)]
E2 = [g.QI(0), g.QI(1), g.QI(0), g.QI(0)]


def wedge4(u, v):
    return [[u[k] * v[l] - u[l] * v[k] for l in range(4)] for k in range(4)]


def line(A):
    u = [PI1[k] + A[0][0] * E1[k] + A[1][0] * E2[k] for k in range(4)]
    v = [PI2[k] + A[0][1] * E1[k] + A[1][1] * E2[k] for k in range(4)]
    return u, v


def m_of(A):
    u, v = line(A)
    P = wedge4(u, v)
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    ph = [[P[i][j] - N0[i][j] - d * NINF[i][j] for j in range(4)] for i in range(4)]
    return g.field_solve([r[:] for r in PSIMAT_T], [ph[0][1], ph[0][2], ph[0][3], ph[1][2], ph[1][3], ph[2][3]])


RMAT = [[REAL[k][r] for k in range(6)] for r in range(6)]


def real_coords(v):
    return g.field_solve([r[:] for r in RMAT], list(v))


def herm(Z1, Z2):
    return sum((Z1[a].conj() * HH[a][b] * Z2[b] for a in range(4) for b in range(4)), g.QI(0))


def gram_on_line(A):
    u, v = line(A)
    return [[herm(x, y) for y in (u, v)] for x in (u, v)]


def A_for_real(target):
    """The 2x2 A (complex linear chart) with m(A) = the given real-basis vector."""
    units = [[[ONE if (i, j) == (p, q) else ZERO for j in range(2)] for i in range(2)] for p in range(2) for q in range(2)]
    cols = [real_coords(m_of(U)) for U in units]   # m is linear in A
    M = [[cols[c][r] for c in range(4)] for r in range(6)]
    for pick in combinations(range(6), 4):
        sub = [M[r][:] for r in pick]
        if g.field_rank([s[:] for s in sub]) == 4:
            x = g.field_solve(sub, [target[r] for r in pick])
            ok = all(sum((M[r][c] * x[c] for c in range(4)), g.QI(0)) == target[r] for r in range(6))
            assert ok
            return [[x[0], x[1]], [x[2], x[3]]]
    raise ValueError


def coords_of(xc):
    return [g.QI(0), g.QI(xc[0]), g.QI(0), g.QI(xc[1]), g.QI(xc[2]), g.QI(xc[3])]


BASE = {}


def A_of(xc, yc):
    """Chart A of the complex point x + i y, x, y given in (e0, e1, e2, e3); the chart is complex linear."""
    if not BASE:
        for j, k in enumerate((1, 3, 4, 5)):
            BASE[j] = A_for_real([g.QI(1 if r == k else 0) for r in range(6)])
    return [[sum((BASE[k][i][j] * (g.QI(xc[k]) + I * g.QI(yc[k])) for k in range(4)), g.QI(0))
             for j in range(2)] for i in range(2)]


def det2(G):
    return G[0][0] * G[1][1] - G[0][1] * G[1][0]


def check_store_sigma_and_real_lines():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    premise("correspondence.incidence-relation-chart")
    assert LAM == ONE and MU == g.QI(2)
    assert all(HH[j][i] == HH[i][j].conj() for i in range(4) for j in range(4))
    assert g.field_rank([r[:] for r in HH]) == 4
    assert all(not HH[i][j] for i in (0, 1) for j in (0, 1)) and all(not HH[i][j] for i in (2, 3) for j in (2, 3))
    assert all(kappa(kappa(e8(S))) == [x * g.QI(Fraction(-1, 2)) for x in e8(S)] for S in range(8))
    # the chart reproduces the real basis vectors
    for j, k in enumerate((1, 3, 4, 5)):
        A = A_of([1 if r == j else 0 for r in range(4)], [0, 0, 0, 0])
        assert real_coords(m_of(A)) == [g.QI(1 if r == k else 0) for r in range(6)]
    for x in [(1, 0, 0, 0), (0, 1, 0, 0), (2, -1, 3, 1), (0, 0, 5, -2)]:
        G = gram_on_line(A_of(x, [0, 0, 0, 0]))
        assert G == [[ZERO, ZERO], [ZERO, ZERO]]
    return True


def check_restricted_form_is_imaginary_part():
    premise("correspondence.reality-conjugation-twistor-form-factor")
    premise("synthesis.incidence-vacua-thermofield-real-capacity")
    cases = [((1, 0, 0, 0), (4, 4)), ((2, 1, 0, 1), (8, 8)), ((-3, 0, 2, 0), (20, -12)),
             ((1, 2, 0, 0), (-12, 4)), ((0, 0, 0, 1), (-4, 0)), ((1, 1, 0, 0), (0, 4))]
    for y, (de, te) in cases:
        G = gram_on_line(A_of((0, 0, 0, 0), y))
        for x in [(1, 2, 3, -1), (F(1, 2), 0, -2, 7)]:
            assert gram_on_line(A_of(x, y)) == G                     # depends on Im only
        qy = y[0] ** 2 - y[1] ** 2 - y[2] ** 2 - y[3] ** 2
        d, t = det2(G), G[0][0] + G[1][1]
        assert (d, t) == (g.QI(de), g.QI(te))
        assert d == g.QI(4 * qy) and t == g.QI(4 * y[0])
        if qy > 0:
            assert (t.re > 0) == (y[0] > 0)                           # positive iff future along e0
    return True


def check_imaginary_boost_half_strip():
    premise("correspondence.incidence-relation-chart")
    premise("one-relation.two-capacities-three-consequences")
    rho = F(3, 2)
    seen = []
    for c, s in [(F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)), (F(-3, 5), F(-4, 5)), (F(3, 5), F(-4, 5)),
                 (F(1), F(0)), (F(-1), F(0))]:
        assert c * c + s * s == 1
        G = gram_on_line(A_of((0, rho * c, 0, 0), (rho * s, 0, 0, 0)))
        assert G == [[g.QI(2 * rho * s), ZERO], [ZERO, g.QI(2 * rho * s)]]
        seen.append((G[0][0].re > 0, G[0][0].re < 0))
    assert seen == [(True, False)] * 2 + [(False, True)] * 2 + [(False, False)] * 2
    return True
