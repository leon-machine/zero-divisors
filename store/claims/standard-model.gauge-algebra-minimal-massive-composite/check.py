"""standard-model.gauge-algebra-minimal-massive-composite: exact checks.

The automorphisms of the hierarchy C^m (x) C^k are the maps A (x) B; their Lie algebra is the image of
u(m) + u(k) under (X, Y) -> X (x) 1 + 1 (x) Y, computed here as exact real ranks (Gaussian rationals split into
real and imaginary parts).
(1) Maximal hierarchy C^3 (x) C^3: 18 generators, image of dimension 17, derived algebra 16 = 8 + 8, centre of
    dimension 1: su(3) + su(3) + u(1), not the Standard Model algebra.
(2) Mass first exists at two constituents (the premise, checked at Gaussian-rational samples): one spinor gives
    p = pi pibar^T with det p = 0 (massless); two give det p = |<pi1 pi2>|^2, so p^2 = 2 det p = 2|<pi1 pi2>|^2,
    nonzero unless the spinors are aligned.
(3) Minimal massive hierarchy C^2 (x) C^3: 13 generators, image of dimension 12 = 4 + 9 - 1 = 3 + 8 + 1, derived
    algebra 11 = 3 + 8, centre 1; the kernel of the Lie algebra action is exactly the line of (i I_2, -i I_3)
    (the diagonal phase), and at the group level (lambda I_2, lambda^-1 I_3) acts trivially for a unit Gaussian
    lambda while (lambda I_2, lambda I_3) does not.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI
SPINORS = [[QI(1), QI(0)], [QI(1, 1), QI(2)], [QI(2, -1), QI(F(1, 3), 1)], [QI(0, 3), QI(-1, 2)]]
LAM = QI(F(3, 5), F(4, 5))


def _basis_u(n):
    out = []
    for k in range(n):
        out.append({(k, k): QI(0, 1)})
    for j in range(n):
        for k in range(j + 1, n):
            out.append({(j, k): QI(1), (k, j): QI(-1)})
            out.append({(j, k): QI(0, 1), (k, j): QI(0, 1)})
    return out


def _act(X, Y, m, k):
    M = {}
    for (a, c), z in X.items():
        for b in range(k):
            key = (a * k + b, c * k + b)
            M[key] = M.get(key, QI(0)) + z
    for (b, d), z in Y.items():
        for a in range(m):
            key = (a * k + b, a * k + d)
            M[key] = M.get(key, QI(0)) + z
    return {kk: v for kk, v in M.items() if v}


def _real_row(M, N):
    row = [F(0)] * (2 * N * N)
    for (r, c), z in M.items():
        row[r * N + c] = z.re
        row[N * N + r * N + c] = z.im
    return row


def _mmul(A, B):
    out = {}
    for (r, c), z in A.items():
        for (c2, d), w in B.items():
            if c == c2:
                out[(r, d)] = out.get((r, d), QI(0)) + z * w
    return {kk: v for kk, v in out.items() if v}


def _comm(A, B):
    out = dict(_mmul(A, B))
    for kk, v in _mmul(B, A).items():
        out[kk] = out.get(kk, QI(0)) - v
    return {kk: v for kk, v in out.items() if v}


def _rank(mats, N):
    return GA.rank_of_vectors([_real_row(M, N) for M in mats]) if mats else 0


def _structure(m, k):
    """(generators, image dim, derived dim, A-side derived, B-side derived, centre dim, kernel basis)."""
    zm, zk = {}, {}
    A = [_act(X, zk, m, k) for X in _basis_u(m)]
    B = [_act(zm, Y, m, k) for Y in _basis_u(k)]
    N = m * k
    gens = A + B
    img = _rank(gens, N)
    pairs = lambda L: [_comm(L[i], L[j]) for i in range(len(L)) for j in range(i + 1, len(L))]
    der, dA, dB = _rank(pairs(gens), N), _rank(pairs(A), N), _rank(pairs(B), N)
    rows = []
    for j in range(len(gens)):
        cols = [_real_row(_comm(g, gens[j]), N) for g in gens]
        rows.extend([[cols[i][r] for i in range(len(gens))] for r in range(2 * N * N)])
    cent = []
    for c in GA.field_kernel(rows):
        M = {}
        for g, ci in zip(gens, c):
            for kk, z in g.items():
                M[kk] = M.get(kk, QI(0)) + z * QI(ci)
        cent.append({kk: v for kk, v in M.items() if v})
    kern = GA.field_kernel([[_real_row(g, N)[r] for g in gens] for r in range(2 * N * N)])
    return len(gens), img, der, dA, dB, _rank(cent, N), kern


def _det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def _momentum(spinors):
    p = [[QI(0), QI(0)], [QI(0), QI(0)]]
    for s in spinors:
        for A in range(2):
            for Ap in range(2):
                p[A][Ap] = p[A][Ap] + s[A] * s[Ap].conj()
    return p


def check_maximal_hierarchy_is_seventeen():
    n, img, der, dA, dB, cen, kern = _structure(3, 3)
    ok = (n, img, der, dA, dB, cen) == (18, 17, 16, 8, 8, 1) and len(kern) == 1
    GA.check("aut(C^3 x C^3): 18 generators, dimension 17 = 8 + 8 + 1", ok)
    return ok


def check_mass_first_at_two_constituents():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    ok = True
    for s in SPINORS:
        ok = ok and _det2(_momentum([s])) == QI(0)
    nonzero = 0
    for i in range(len(SPINORS)):
        for j in range(i + 1, len(SPINORS)):
            a, b = SPINORS[i], SPINORS[j]
            br = a[0] * b[1] - a[1] * b[0]
            d = _det2(_momentum([a, b]))
            ok = ok and d == br * br.conj() and d.im == 0
            nonzero += 1 if d != QI(0) else 0
    aligned = [QI(2, 1) * x for x in SPINORS[1]]
    ok = ok and _det2(_momentum([SPINORS[1], aligned])) == QI(0) and nonzero == 6
    GA.check("one spinor: det p = 0; two: det p = |<pi1 pi2>|^2 (m^2 = 2 det p), zero only when aligned", ok)
    return ok


def check_minimal_massive_is_standard_model():
    premise("mass.mass-symplectic-area-two-twistor-formula")
    n, img, der, dA, dB, cen, kern = _structure(2, 3)
    ok = (n, img, der, dA, dB, cen) == (13, 12, 11, 3, 8, 1) and img == 4 + 9 - 1 == 3 + 8 + 1
    # the kernel line: coefficient vector proportional to (i E_00 + i E_11) - (i E_00 + i E_11 + i E_22) parts
    ok = ok and len(kern) == 1
    v = kern[0]
    X = {}
    for c, M in zip(v[:4], _basis_u(2)):
        for kk, z in M.items():
            X[kk] = X.get(kk, QI(0)) + z * QI(c)
    Y = {}
    for c, M in zip(v[4:], _basis_u(3)):
        for kk, z in M.items():
            Y[kk] = Y.get(kk, QI(0)) + z * QI(c)
    X = {kk: z for kk, z in X.items() if z}
    Y = {kk: z for kk, z in Y.items() if z}
    s = X.get((0, 0))
    ok = ok and s is not None and s.re == 0 and X == {(0, 0): s, (1, 1): s}
    ok = ok and Y == {(0, 0): -s, (1, 1): -s, (2, 2): -s}
    # group level: (lam I2, lam^-1 I3) acts as lam * lam^-1 = 1 on every basis tensor; (lam I2, lam I3) as lam^2
    inv = QI(1) / LAM
    ok = ok and LAM * inv == QI(1) and LAM * LAM != QI(1) and LAM * LAM.conj() == QI(1)
    GA.check("aut(C^2 x C^3): 13 generators, dimension 12 = su(2) + su(3) + u(1); kernel = diagonal phase", ok)
    return ok
