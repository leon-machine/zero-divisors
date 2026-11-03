"""rungs.mass-bracket-frozen-points-grip-slot: exact checks over the Gaussian rationals (GA.QI), ported
from legacy verify_T12_rungs.py (lem:bracket) and widened (complex instances, the volume form computed
as a 4x4 determinant independently of the ambient pairing, the symmetric-square component).

Basis of CS = S_omega + S_pi: e1, e2, pi1, pi2 (the E = -1 and E = +1 eigenspaces of the grading
E = diag(-1, -1, 1, 1)), eps(e1 ^ e2 ^ pi1 ^ pi2) = 1, n_inf = e1 ^ e2, n_0 = pi1 ^ pi2.
  (1) eps(n_inf ^ Z1 ^ Z2) = <pi1 pi2>, eps(n_0 ^ Z1 ^ Z2) = <omega1 omega2>, and
      eps(I_Lambda ^ Z1 ^ Z2) = <pi1 pi2> + (Lambda/6) <omega1 omega2> (by the determinant, and equal to the
      ambient pairing); m^2 = 2 |eps(n_inf ^ Z1 ^ Z2)|^2 equals p^2 of the spinor momentum.
  (2) Psi = e1' (x) Z1 + e2' (x) Z2 in C^2 (x) CS: the slot trace of Psi (x) conj(Psi), restricted to the
      pi-block, is the total momentum; the Lambda^2 C^2 (x) Lambda^2 CS component of Psi (x) Psi is
      (1/2) (e1' ^ e2') (x) (Z1 ^ Z2).
  (3) At Lambda = 0 the mass vanishes exactly when Z1 ^ Z2 is orthogonal to n_inf (aligned pi parts).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# Twistor core (shared text, ported from legacy/verify_T11.py Parts B-D; self-contained).
# CS = C^4 with basis e1, e2 (omega-plane) and e3, e4 (pi-plane); the ambient space is
# Lambda^2 CS in the basis e_i ^ e_j (i < j), with n_inf = e1^e2, n_0 = e3^e4 and the pairing
# <P, P'> = coefficient of e1^e2^e3^e4 in P ^ P'. Everything is over the Gaussian rationals GA.QI.
# ---------------------------------------------------------------------------
from itertools import combinations as _comb

QZ = GA.qi(0)
QO = GA.qi(1)
PAIRS4 = list(_comb(range(4), 2))


def q(re, im=0):
    return GA.qi(re, im)


def eps2(a, b):
    """<ab> = a_0 b_1 - a_1 b_0."""
    return a[0] * b[1] - a[1] * b[0]


def wedge2(z1, z2):
    return [z1[i] * z2[j] - z1[j] * z2[i] for (i, j) in PAIRS4]


def perm_sign(perm):
    s, p = 1, list(perm)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def amb_pair(P, R):
    tot = QZ
    for a, (i, j) in enumerate(PAIRS4):
        if not P[a]:
            continue
        for b, (k, l) in enumerate(PAIRS4):
            if R[b] and len({i, j, k, l}) == 4:
                tot = tot + q(perm_sign((i, j, k, l))) * P[a] * R[b]
    return tot


def biv(i, j):
    out = [QZ] * 6
    out[PAIRS4.index((min(i, j), max(i, j)))] = QO if i < j else -QO
    return out


def vadd(*us):
    return [sum((u[k] for u in us), QZ) for k in range(len(us[0]))]


def vscal(c, u):
    return [c * a for a in u]


N_INF, N_0 = biv(0, 1), biv(2, 3)
EAMB = [biv(i, j) for (i, j) in PAIRS4]
X_SLOT = [biv(0, 2), biv(0, 3), biv(1, 2), biv(1, 3)]


def twistor(om, pi):
    return [om[0], om[1], pi[0], pi[1]]


def i_lam(lam):
    """I = n_inf + lam n_0 (lam = Lambda/6)."""
    return vadd(N_INF, vscal(q(lam), N_0))


def xslot(co):
    return vadd(*[vscal(q(c), v) for c, v in zip(co, X_SLOT)])


def xpoint(x):
    """X(x) = n_0 + x - (1/2) <x,x> n_inf."""
    return vadd(N_0, x, vscal(-amb_pair(x, x) / q(2), N_INF))


def on_line(co, pi):
    """The twistor (mu_x pi, pi) on the incidence line of x = (x13, x14, x23, x24)."""
    x13, x14, x23, x24 = co
    om = [-q(x13) * pi[1] + q(x14) * pi[0], -q(x23) * pi[1] + q(x24) * pi[0]]
    return twistor(om, pi)


def act(A, P):
    """A.(u^v) = Au^v + u^Av, extended linearly to bivectors."""
    out = [QZ] * 6
    for a, (i, j) in enumerate(PAIRS4):
        if not P[a]:
            continue
        Aei = [A[r][i] for r in range(4)]
        Aej = [A[r][j] for r in range(4)]
        ei = [QO if r == i else QZ for r in range(4)]
        ej = [QO if r == j else QZ for r in range(4)]
        out = vadd(out, vscal(P[a], vadd(wedge2(Aei, ej), wedge2(ei, Aej))))
    return out


def rot(U, V, W):
    """R_{U^V}(W) = <U,W> V - <V,W> U."""
    return vadd(vscal(amb_pair(U, W), V), vscal(-amb_pair(V, W), U))


def gsolve(rows, rhs):
    """Exact solution of a consistent (possibly overdetermined) system over Q(i)."""
    m, n = len(rows), len(rows[0])
    A = [rows[i][:] + [rhs[i]] for i in range(m)]
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if A[i][c]), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        inv = QO / A[r][c]
        A[r] = [x * inv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [x - f * y for x, y in zip(A[i], A[r])]
        piv.append(c)
        r += 1
    if any(A[i][n] for i in range(r, m)):
        raise ValueError("inconsistent linear system")
    if len(piv) != n:
        raise ValueError("underdetermined linear system")
    sol = [QZ] * n
    for i, c in enumerate(piv):
        sol[c] = A[i][n]
    return sol


_UNIT_ACT = []


def _unit_act():
    if not _UNIT_ACT:
        for r in range(4):
            for c in range(4):
                A = [[QZ] * 4 for _ in range(4)]
                A[r][c] = QO
                _UNIT_ACT.append([act(A, EAMB[b]) for b in range(6)])
    return _UNIT_ACT


_SP = {}


def spin_preimage(U, V):
    """The traceless A in gl(4) whose action on Lambda^2 CS is the rotation R_{U^V} (memoised)."""
    key = tuple((c.re, c.im) for c in U + V)
    if key not in _SP:
        _SP[key] = _spin_preimage(U, V)
    return [row[:] for row in _SP[key]]


def _spin_preimage(U, V):
    ua = _unit_act()
    rows, rhs = [], []
    for b in range(6):
        target = rot(U, V, EAMB[b])
        for comp in range(6):
            rows.append([ua[k][b][comp] for k in range(16)])
            rhs.append(target[comp])
    rows.append([QO if r == c else QZ for r in range(4) for c in range(4)])
    rhs.append(QZ)
    sol = gsolve(rows, rhs)
    return [[sol[4 * r + c] for c in range(4)] for r in range(4)]


SIG = [[QO if abs(a - b) == 2 else QZ for b in range(4)] for a in range(4)]


def herm(zi, zj):
    """conj(zi)^T Sigma zj: the (2,2) Hermitian form pairing omega with conj(pi)."""
    return sum((zi[a].conj() * zj[b] for a in range(4) for b in range(4) if SIG[a][b]), QZ)


def moment(A, Zs):
    """M_A = i sum_i conj(Z_i)^T Sigma A Z_i."""
    tot = QZ
    for z in Zs:
        Az = [sum((A[r][c] * z[c] for c in range(4)), QZ) for r in range(4)]
        tot = tot + herm(z, Az)
    return GA.QI_I * tot


def gram_inverse(basis):
    n = len(basis)
    Gs = [[amb_pair(u, v) for v in basis] for u in basis]
    cols = [gsolve([row[:] for row in Gs], [QO if r == c else QZ for r in range(n)]) for c in range(n)]
    return [[cols[c][r] for c in range(n)] for r in range(n)]


_GI = []


def grip(Zs, I):
    """P = M(I): the ambient vector with <P, U> = M_{A(U ^ I)} for every U."""
    if not _GI:
        _GI.append(gram_inverse(EAMB))
    vals = [moment(spin_preimage(EAMB[a], I), Zs) for a in range(6)]
    P = [sum((vals[a] * _GI[0][a][J] for a in range(6)), QZ) for J in range(6)]
    assert all(amb_pair(P, EAMB[a]) == vals[a] for a in range(6))
    return P


def gram_h(Zs):
    return [[herm(a, b) for b in Zs] for a in Zs]


def internal_casimir(Z1, Z2):
    """C = (h11 - h22)^2/4 + |h12|^2 = tr(h_0^2)/2."""
    h11, h22, h12 = herm(Z1, Z1), herm(Z2, Z2), herm(Z1, Z2)
    return (h11 - h22) * (h11 - h22) / q(4) + h12 * h12.conj()


def casimir(Zs, basis):
    """C2(W) = (1/2) g^{ac} g^{bd} M_ab M_cd over the span of `basis`."""
    n = len(basis)
    Gi = gram_inverse(basis)
    Mm = [[moment(spin_preimage(u, v), Zs) if a != b else QZ for b, v in enumerate(basis)]
          for a, u in enumerate(basis)]
    tot = QZ
    for a in range(n):
        for b in range(n):
            if not Mm[a][b]:
                continue
            for c in range(n):
                if not Gi[a][c]:
                    continue
                for d in range(n):
                    if Gi[b][d] and Mm[c][d]:
                        tot = tot + Gi[a][c] * Gi[b][d] * Mm[a][b] * Mm[c][d]
    return tot / q(2)


def xreal(t, x_, y, z):
    """The real slice x = i K eps, K the Hermitian matrix of (t, x, y, z)."""
    K = [[q(t + z), q(x_, -y)], [q(x_, y), q(t - z)]]
    eps = [[QZ, QO], [-QO, QZ]]
    X = [[sum((K[a][b] * eps[b][c] for b in range(2)), QZ) * GA.QI_I for c in range(2)] for a in range(2)]
    return vadd(*[vscal(c_, v) for c_, v in zip((X[0][0], X[0][1], X[1][0], X[1][1]), X_SLOT)])


def in_su22(A):
    SA = [[sum((SIG[i][k] * A[k][j] for k in range(4)), QZ) for j in range(4)] for i in range(4)]
    return all(SA[i][j] + SA[j][i].conj() == QZ for i in range(4) for j in range(4))

INST = [
    ([q(2), q(-1), q(3), q(5)], [q(1), q(4), q(-2), q(7)]),
    ([q(F(1, 2)), q(3), q(-1), q(F(2, 3))], [q(5), q(-2), q(4), q(1)]),
    ([q(1, 1), q(2), q(3, -1), q(F(1, 2))], [q(0, 2), q(-1), q(1, 1), q(2, 3)]),
    ([q(0), q(1, 4), q(1, 1), q(0)], [q(1), q(0), q(0), q(2, -1)]),
]
BASIS4 = [[q(1) if r == i else QZ for r in range(4)] for i in range(4)]


def det(M):
    if len(M) == 1:
        return M[0][0]
    return sum((q((-1) ** c) * M[0][c] * det([row[:c] + row[c + 1:] for row in M[1:]])
                for c in range(len(M)) if M[0][c]), QZ)


def eps_biv(I_terms, Z1, Z2):
    """eps(I ^ Z1 ^ Z2) for I = sum c (u ^ v), given as [(c, u, v)]: a 4x4 determinant per term."""
    return sum((c * det([u, v, Z1, Z2]) for c, u, v in I_terms), QZ)


def spinor_p2(p1, p2):
    p = [[p1[A] * p1[B].conj() + p2[A] * p2[B].conj() for B in range(2)] for A in range(2)]
    tot = QZ
    for A, B, s1 in ((0, 1, 1), (1, 0, -1)):
        for Ap, Bp, s2 in ((0, 1, 1), (1, 0, -1)):
            tot = tot + q(s1 * s2) * p[A][Ap] * p[B][Bp]
    return tot


def check_volume_identities_and_mass():
    premise("rungs.imported-spinor-identification-witt-data-line")
    premise("rungs.imported-mass-symplectic-area")
    e1, e2, pi1, pi2 = BASIS4
    ok = det([e1, e2, pi1, pi2]) == q(1)
    for Z1, Z2 in INST:
        pp = Z1[2] * Z2[3] - Z1[3] * Z2[2]
        ww = Z1[0] * Z2[1] - Z1[1] * Z2[0]
        a = eps_biv([(QO, e1, e2)], Z1, Z2)
        b = eps_biv([(QO, pi1, pi2)], Z1, Z2)
        ok = ok and a == pp and b == ww
        ok = ok and a == amb_pair(N_INF, wedge2(Z1, Z2)) and b == amb_pair(N_0, wedge2(Z1, Z2))
        for lam in (F(1, 2), F(-2, 3)):
            ok = ok and eps_biv([(QO, e1, e2), (q(lam), pi1, pi2)], Z1, Z2) == pp + q(lam) * ww
        ok = ok and q(2) * a * a.conj() == spinor_p2(Z1[2:], Z2[2:])
    # hand value: Z1 = (2,-1,3,5), Z2 = (1,4,-2,7): <pi pi> = 21 + 10 = 31, <w w> = 8 + 1 = 9
    ok = ok and eps_biv([(QO, e1, e2)], *INST[0]) == q(31) and eps_biv([(QO, pi1, pi2)], *INST[0]) == q(9)
    GA.check("eps(n_inf ^ Z1 ^ Z2) = <pi1 pi2>, eps(n_0 ^ Z1 ^ Z2) = <omega1 omega2>, m^2 = 2|.|^2", ok)
    assert ok


def check_slot_trace_and_symmetric_square_component():
    premise("rungs.imported-mass-symplectic-area")
    ok = True
    for Z1, Z2 in INST:
        vec = Z1 + Z2                                    # index (i, c) -> 4 i + c
        outer = [[vec[r] * vec[c].conj() for c in range(8)] for r in range(8)]
        pt = [[outer[x][y] + outer[4 + x][4 + y] for y in range(4)] for x in range(4)]
        mom = [[Z1[2 + A] * Z1[2 + B].conj() + Z2[2 + A] * Z2[2 + B].conj() for B in range(2)] for A in range(2)]
        ok = ok and all(pt[2 + A][2 + B] == mom[A][B] for A in range(2) for B in range(2))
        ok = ok and sum((pt[x][x] for x in range(4)), QZ) == sum((v * v.conj() for v in vec), QZ)
        # Psi (x) Psi projected to Lambda^2 C^2 (x) Lambda^2 CS: antisymmetrise slots and CS indices
        T = {}
        for i in range(2):
            for j in range(2):
                for a in range(4):
                    for b in range(4):
                        T[(i, a, j, b)] = (vec[4 * i + a] * vec[4 * j + b] - vec[4 * j + a] * vec[4 * i + b]
                                           - vec[4 * i + b] * vec[4 * j + a] + vec[4 * j + b] * vec[4 * i + a]) / q(4)
        W = wedge2(Z1, Z2)
        for a in range(4):
            for b in range(4):
                if a == b:
                    continue
                k = PAIRS4.index((min(a, b), max(a, b)))
                wab = W[k] if a < b else -W[k]
                ok = ok and T[(0, a, 1, b)] == wab / q(2) and T[(1, a, 0, b)] == -wab / q(2)
    GA.check("slot trace gives the momentum; the Lambda^2 C^2 (x) Lambda^2 CS component is Z1 ^ Z2", ok)
    assert ok


def check_mass_zero_iff_orthogonal_to_frozen_point():
    premise("rungs.imported-mass-symplectic-area")
    ok = True
    zeros = 0
    cases = list(INST) + [([q(1), q(2), q(1, 1), q(2)], [q(3), q(0), q(2, 2), q(4)]),
                          ([q(0), q(1), q(0), q(0)], [q(5), q(1), q(0), q(0)])]
    for Z1, Z2 in cases:
        pair = amb_pair(N_INF, wedge2(Z1, Z2))
        m2 = spinor_p2(Z1[2:], Z2[2:])
        ok = ok and ((m2 == QZ) == (pair == QZ))
        zeros += m2 == QZ
    ok = ok and zeros == 2
    GA.check("at Lambda = 0 the mass vanishes exactly when Z1 ^ Z2 is orthogonal to n_inf", ok)
    assert ok
