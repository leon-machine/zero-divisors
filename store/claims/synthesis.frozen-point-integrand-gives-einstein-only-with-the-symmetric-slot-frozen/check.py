"""Field-space lattice of the frozen-point integrand: exact checks.

Cl(2,4) as in the stored checks: e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2,
ninf = e+ - e-, n0 . ninf = 1. At a point, frame the identity (hb^{-1}(a) = a), the general Cl(2,4)
connection with nondegenerate soldering is
    A(mu) = Omega(mu) - ninf ^ w_mu + n0 ^ S(w_mu) + beta_mu ninf ^ n0
(rotation gauge field, soldering, special-conformal slot S, dilation beta). Its Lorentz block is
F_W(mu, nu) = -Rd(mu, nu) + T_S(mu, nu), Rd the curvature operator on coordinate planes and T_S the
Lorentz block of Theta_mu x Theta_nu (commutator product), Theta = -ninf ^ w + n0 ^ S(w) + beta ninf ^ n0.
The integrand: eps(B, C) = coefficient of i6 in B ^ C ^ I ^ V, i6 = e0 e1 e2 e3 e+ e- (i6^2 = -1, so the
coefficient is -<(B ^ C ^ I ^ V) i6>_0); L = (1/4) sum over the 24 orderings of sgn eps(F_W, F_W).
Slot pieces (lowered with g = diag(1, -1, -1, -1)): trace (1), antisymmetric (6), trace-free symmetric (9).
A field space freezes each piece at its Lorentz-invariant value (trace rho, others 0) or varies it; varied
pieces are eliminated through their (algebraic, linear) equations. Invariant quadratic forms on the 20
algebraic curvature tensors: w2 = |W|^2/4, wd (Weyl times its dual), r2 = |Ric_tf|^2, s2 = R^2 (index
readings), so the Euler density is E4 = 4 w2 - 2 r2 + s2/6.
Exact arithmetic only (Fractions).
"""
from fractions import Fraction as Fr
from itertools import combinations, permutations

import GA
from tp_premise import premise

S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
N0 = GA.scal(Fr(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
WV = E[:4]
G4 = [Fr(1), Fr(-1), Fr(-1), Fr(-1)]
PAIRS = list(combinations(range(4), 2))


def mul(x, y):
    return GA.mul(x, y, S)


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def wedge(x, y, r, s):
    return grade(mul(x, y), r + s)


def comm(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def dot(a, b):
    return GA.dot(a, b, S)


def sc(x):
    return x.get((), Fr(0))


L2W = [wedge(WV[a], WV[b], 1, 1) for a, b in PAIRS]
I6 = mul(mul(mul(E[0], E[1]), mul(E[2], E[3])), mul(E[4], E[5]))
I4 = mul(mul(E[0], E[1]), mul(E[2], E[3]))


def lorentz(x):
    return {b: c for b, c in x.items() if len(b) == 2 and max(b) < 4}


def coordsL(b):
    return [b.get(p, Fr(0)) for p in PAIRS]


def fromL(c):
    out = {}
    for k, v in enumerate(c):
        if v:
            out = GA.add(out, GA.scal(v, L2W[k]))
    return out


def vec(cs):
    out = {}
    for k, c in enumerate(cs):
        if c:
            out = GA.add(out, GA.scal(c, WV[k]))
    return out


def data(lam):
    I = GA.add(NI, GA.scal(lam / 6, N0))
    V = GA.sub(N0, GA.scal(Fr(3) / lam, I))
    return I, N0, V


def eps_gram(lam):
    I, X, V = data(lam)
    IV = wedge(I, V, 1, 1)
    return [[-sc(mul(wedge(wedge(a, b, 2, 2), IV, 4, 2), I6)) for b in L2W] for a in L2W]


EPS = {}
for _p in permutations(range(4)):
    _s = 1
    for _i in range(4):
        for _j in range(_i + 1, 4):
            if _p[_i] > _p[_j]:
                _s = -_s
    EPS[_p] = _s


def pair_index(a, b):
    return (PAIRS.index((a, b)), 1) if a < b else (PAIRS.index((b, a)), -1)


def zmatrix(Mg):
    Z = [[Fr(0)] * 36 for _ in range(36)]
    for p, s in EPS.items():
        k1, s1 = pair_index(p[0], p[1])
        k2, s2 = pair_index(p[2], p[3])
        for m in range(6):
            for n in range(6):
                if Mg[m][n]:
                    Z[6 * k1 + m][6 * k2 + n] += Fr(s * s1 * s2, 4) * Mg[m][n]
    return [[(Z[i][j] + Z[j][i]) / 2 for j in range(36)] for i in range(36)]


def theta(Sm, mu, beta=None):
    t = GA.neg(wedge(NI, WV[mu], 1, 1))
    sw = vec([Sm[k][mu] for k in range(4)])
    if sw:
        t = GA.add(t, wedge(N0, sw, 1, 1))
    if beta is not None and beta[mu]:
        t = GA.add(t, GA.scal(beta[mu], wedge(NI, N0, 1, 1)))
    return t


def tvec(Sm, beta=None):
    th = [theta(Sm, mu, beta) for mu in range(4)]
    out = []
    for (a, b) in PAIRS:
        out.extend(coordsL(lorentz(comm(th[a], th[b]))))
    return out


def zero4():
    return [[Fr(0)] * 4 for _ in range(4)]


def scalar4(r):
    return [[r if i == j else Fr(0) for j in range(4)] for i in range(4)]


def unitS(j):
    M = zero4()
    M[j // 4][j % 4] = Fr(1)
    return M


def tmatrix():
    cols = [tvec(unitS(j)) for j in range(16)]
    return [[cols[j][i] for j in range(16)] for i in range(36)]


def matmul(A, B):
    m, p = len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m) if A[i][k] and B[k][j]), Fr(0))
             for j in range(p)] for i in range(len(A))]


def tr(A):
    return [list(r) for r in zip(*A)]


def inverse(M):
    n = len(M)
    A = [list(M[i]) + [Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def nullspace(rows, n):
    piv = {}
    for r in rows:
        r = list(r)
        for c, pr in piv.items():
            if r[c] != 0:
                f = r[c]
                r = [a - f * b for a, b in zip(r, pr)]
        c0 = next((c for c in range(n) if r[c] != 0), None)
        if c0 is None:
            continue
        pv = r[c0]
        r = [a / pv for a in r]
        for c, pr in list(piv.items()):
            if pr[c0] != 0:
                f = pr[c0]
                piv[c] = [a - f * b for a, b in zip(pr, r)]
        piv[c0] = r
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        x = [Fr(0)] * n
        x[fc] = Fr(1)
        for c, pr in piv.items():
            x[c] = -pr[fc]
        out.append(x)
    return out


def rd_of(x):
    Rd = {(r, r): {} for r in range(4)}
    for k, (r, s) in enumerate(PAIRS):
        b = fromL(x[6 * k:6 * k + 6])
        Rd[(r, s)] = b
        Rd[(s, r)] = GA.neg(b)
    return Rd


def bianchi(x):
    Rd = rd_of(x)
    out = []
    for a, b, c in combinations(range(4), 3):
        v = GA.add(comm(Rd[(a, b)], WV[c]), comm(Rd[(b, c)], WV[a]), comm(Rd[(c, a)], WV[b]))
        out.extend([v.get((i,), Fr(0)) for i in range(4)])
    return out


def ricci(x):
    """R(w_mu) = sum_b w^b . R(w_b ^ w_mu) (store convention: R(a) = Lambda a on de Sitter)."""
    Rd = rd_of(x)
    Ric = zero4()
    for mu in range(4):
        v = {}
        for b in range(4):
            if b != mu:
                v = GA.add(v, GA.scal(1 / G4[b], comm(WV[b], Rd[(b, mu)])))
        for k in range(4):
            Ric[k][mu] = v.get((k,), Fr(0))
    return Ric


def schouten(x):
    Ric = ricci(x)
    R = sum(Ric[k][k] for k in range(4))
    return [[(Ric[k][m] - (R / 6 if k == m else 0)) / 2 for m in range(4)] for k in range(4)], R


def weyl(x):
    P, _ = schouten(x)
    Rd = rd_of(x)
    out = {}
    for (a, b) in PAIRS:
        Pa, Pb = vec([P[k][a] for k in range(4)]), vec([P[k][b] for k in range(4)])
        corr = GA.add(wedge(Pa, WV[b], 1, 1) if Pa else {}, wedge(WV[a], Pb, 1, 1) if Pb else {})
        out[(a, b)] = GA.sub(Rd[(a, b)], corr)
    return out


def invariants(x):
    Wd = weyl(x)
    w2 = wd = Fr(0)
    for k, (a, b) in enumerate(PAIRS):
        n = sc(mul(L2W[k], L2W[k]))
        w2 += sc(mul(Wd[(a, b)], Wd[(a, b)])) / n
        wd += sc(mul(mul(Wd[(a, b)], Wd[(a, b)]), I4)) / n
    Ric = ricci(x)
    R = sum(Ric[k][k] for k in range(4))
    tf = [[Ric[k][m] - (R / 4 if k == m else 0) for m in range(4)] for k in range(4)]
    r2 = sum(tf[k][m] * tf[m][k] for k in range(4) for m in range(4))
    return [w2, wd, r2, R * R], R


def svec(M):
    return [M[j // 4][j % 4] for j in range(16)]


def slot_pieces():
    out = {'trace': [svec(scalar4(Fr(1)))], 'anti': [], 'tf': []}
    for k, l in PAIRS:
        M = zero4()
        M[k][l], M[l][k] = 1 / G4[k], -1 / G4[l]
        out['anti'].append(svec(M))
        M = zero4()
        M[k][l], M[l][k] = 1 / G4[k], 1 / G4[l]
        out['tf'].append(svec(M))
    for i in range(1, 4):
        M = zero4()
        M[0][0], M[i][i] = Fr(1), Fr(-1)
        out['tf'].append(svec(M))
    return out


_CACHE = {}


def setup():
    if not _CACHE:
        Z = zmatrix(eps_gram(Fr(9, 7)))
        T = tmatrix()
        unit = [[Fr(1) if i == j else Fr(0) for i in range(36)] for j in range(36)]
        alg = nullspace([list(r) for r in zip(*[bianchi(x) for x in unit])], 36)
        ZT = matmul(Z, T)
        Mtt = matmul(tr(T), ZT)
        Mgg = matmul(alg, matmul(Z, tr(alg)))
        Cg = [[-v for v in row] for row in matmul(alg, ZT)]
        n = len(alg)
        forms = []
        diag = [invariants(a)[0] for a in alg]
        cross = {}
        for i in range(n):
            for j in range(i + 1, n):
                cross[(i, j)] = invariants([p + q for p, q in zip(alg[i], alg[j])])[0]
        for f in range(4):
            Gm = [[Fr(0)] * n for _ in range(n)]
            for i in range(n):
                Gm[i][i] = diag[i][f]
                for j in range(i + 1, n):
                    Gm[i][j] = Gm[j][i] = (cross[(i, j)][f] - diag[i][f] - diag[j][f]) / 2
            forms.append(Gm)
        Rlin = [invariants(a)[1] for a in alg]
        _CACHE.update(Z=Z, T=T, ZT=ZT, alg=alg, Mtt=Mtt, Mgg=Mgg, Cg=Cg, forms=forms, Rlin=Rlin,
                      Mi=inverse(Mtt), pieces=slot_pieces())
    return _CACHE


def free_slot(x):
    """Solution of the slot equation with the whole slot varied: S* = Mtt^{-1} T^t Z x."""
    c = setup()
    v = [sum(c['ZT'][i][j] * x[i] for i in range(36) if x[i]) for j in range(16)]
    s = [sum(c['Mi'][a][b] * v[b] for b in range(16)) for a in range(16)]
    return [[s[4 * k + m] for m in range(4)] for k in range(4)]


def fit_invariants(Q):
    c = setup()
    n = len(c['alg'])
    rows = [[F[i][j] for F in c['forms']] + [-Q[i][j]] for i in range(n) for j in range(i, n)]
    ns = nullspace(rows, 5)
    if len(ns) != 1 or ns[0][4] == 0:
        return None
    return [v / ns[0][4] for v in ns[0][:4]]


def reduced(J, rho):
    """Reduced Lagrangian of the field space with the pieces in J varied: (quadratic part as a fit in
    (w2, wd, r2, s2), coefficient k of the linear part k R, constant)."""
    c = setup()
    P = [v for nm in J for v in c['pieces'][nm]]
    S0 = svec(scalar4(rho)) if 'trace' not in J else [Fr(0)] * 16
    Mtt, Cg, Mgg = c['Mtt'], c['Cg'], c['Mgg']
    CS0 = [sum(Cg[i][j] * S0[j] for j in range(16)) for i in range(20)]
    MS0 = [sum(Mtt[i][j] * S0[j] for j in range(16)) for i in range(16)]
    c0 = sum(a * b for a, b in zip(S0, MS0))
    if P:
        Pm = tr(P)
        Qi = inverse(matmul(P, matmul(Mtt, Pm)))
        CP = matmul(Cg, Pm)
        CPQ = matmul(CP, Qi)
        q = [[Mgg[i][j] - sum(CPQ[i][a] * CP[j][a] for a in range(len(P))) for j in range(20)] for i in range(20)]
        PM = [sum(P[a][j] * MS0[j] for j in range(16)) for a in range(len(P))]
        QPM = [sum(Qi[a][b] * PM[b] for b in range(len(P))) for a in range(len(P))]
        lin = [2 * CS0[i] - 2 * sum(CP[i][a] * QPM[a] for a in range(len(P))) for i in range(20)]
        const = c0 - sum(PM[a] * QPM[a] for a in range(len(P)))
    else:
        q, lin, const = Mgg, [2 * v for v in CS0], c0
    ks = nullspace([[l, -r] for l, r in zip(lin, c['Rlin'])], 2)
    k = None if len(ks) != 1 or ks[0][0] == 0 else ks[0][1] / ks[0][0]
    return fit_invariants(q), k, const


def preserves(Sm, beta, I):
    return all(GA.is_zero(comm(theta(Sm, mu, beta), I)) for mu in range(4))


# sample inputs (kept outside the check functions, so that literal perturbations hit asserted values)
LAMS = (Fr(9, 7), Fr(3), Fr(-3))
RHO1 = Fr(5, 11)
RHOS = (Fr(5, 11), Fr(-2, 3))
SG = [[Fr((3 * i + 5 * j) % 7 - 3) for j in range(4)] for i in range(4)]
BETA = [Fr(3), Fr(-2), Fr(7), Fr(1)]
BETA_BAD = [Fr(1), Fr(0), Fr(0), Fr(0)]
SAMPLES = ([3, -1, 4, 1, -5, 9, 2, -6, 5, 3, -5, 8, 9, 7, -9, 3, 2, -3, 8, 4],
           [1, 0, 2, 0, -1, 0, 0, 3, 0, 1, 0, 0, -2, 0, 1, 0, 0, 4, 0, -1])
KAP = Fr(2, 3)
XT_INDEX = 1
SPHERES = ((Fr(1), Fr(1)), (Fr(1), Fr(2)), (Fr(2), Fr(5)))
ALL_PARTS = ('trace', 'anti', 'tf')


def perturbed_slot(rho):
    bad = scalar4(rho)
    bad[0][1] = Fr(1)
    return bad


def preservation_kernel(I):
    """Dimension of the kernel of (S, beta) -> Theta x I (linear part; twenty unknowns)."""
    cols = []
    for j in range(20):
        Sm, bt = zero4(), [Fr(0)] * 4
        if j < 16:
            Sm[j // 4][j % 4] = Fr(1)
        else:
            bt[j - 16] = Fr(1)
        v = []
        for mu in range(4):
            c = comm(GA.sub(theta(Sm, mu, bt), theta(zero4(), mu)), I)
            v.extend([c.get((i,), Fr(0)) for i in range(6)])
        cols.append(v)
    return len(nullspace([list(r) for r in zip(*cols)], 20))


def algebraic_sample(y):
    alg = setup()['alg']
    return [sum(Fr(y[i]) * alg[i][r] for i in range(len(alg))) for r in range(36)]


def minus_weyl(x):
    Wd = weyl(x)
    out = []
    for (a, b) in PAIRS:
        out.extend([-v for v in coordsL(Wd[(a, b)])])
    return out


def lorentz_block(x, St):
    T = setup()['T']
    sv = svec(St)
    return [-a + sum(T[i][j] * sv[j] for j in range(16)) for i, a in enumerate(x)]


def has_antisymmetric_part(St):
    N = [[G4[a] * St[a][b] for b in range(4)] for a in range(4)]
    return any(N[a][b] != N[b][a] for a in range(4) for b in range(4))


def unit_curvature(idx):
    x = [Fr(0)] * 36
    x[idx] = Fr(1)
    return x


def de_sitter_curvature(kap):
    out = []
    for (a, b) in PAIRS:
        out.extend(coordsL(GA.scal(kap, wedge(WV[a], WV[b], 1, 1))))
    return out


def lattice_rows():
    out = []
    for r in range(4):
        out.extend(combinations(ALL_PARTS, r))
    return out


XI = GA.add(GA.scal(Fr(2), WV[1]), GA.scal(Fr(-1), WV[0]), GA.scal(Fr(3), WV[3]))


def special_conformal_rotor(xi):
    """U = 1 + (1/2) n0 xi, exact since (n0 ^ xi)^2 = 0."""
    return GA.add({(): Fr(1)}, GA.scal(Fr(1, 2), mul(N0, xi)))


def rotated_frozen_row(rho, xi):
    """Frozen-row connection values (constant xi, so no derivative term) after the rotor, and the rotated I."""
    U = special_conformal_rotor(xi)
    Ur = GA.reverse(U)
    I = GA.add(NI, GA.scal(rho, N0))
    th = [mul(mul(U, theta(scalar4(rho), mu)), Ur) for mu in range(4)]
    return th, mul(mul(U, I), Ur), I, GA.eq(mul(U, Ur), {(): Fr(1)})


def beta_part(rho, mu):
    I = GA.add(NI, GA.scal(rho, N0))
    bt = [Fr(0)] * 4
    bt[mu] = Fr(1)
    return GA.sub(comm(theta(zero4(), mu, bt), I), comm(theta(zero4(), mu), I))


REMAINDERS = (lambda r: -r[2] / 24, lambda r: r[1] / 2, lambda r: r[1] / 2 - r[2] / 24)


def check_integrand_sees_only_the_lorentz_block_and_the_blade():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.curvature-only-tractor-actions-are-macdowell-mansouri")
    grams = [eps_gram(lam) for lam in LAMS]
    first, *rest = grams
    ok = all(gm == first for gm in rest) and any(v for row in first for v in row)
    rho = RHO1
    want = []
    for (a, b) in PAIRS:
        want.extend(coordsL(GA.scal(2 * rho, wedge(WV[a], WV[b], 1, 1))))
    ok = ok and tvec(scalar4(rho)) == want and not any(tvec(zero4()))
    ok = ok and tvec(SG, BETA) == tvec(SG)
    I = GA.add(NI, GA.scal(rho, N0))
    ok = ok and preserves(scalar4(rho), None, I)
    ok = ok and not preserves(perturbed_slot(rho), None, I) and not preserves(scalar4(rho), BETA_BAD, I)
    ok = ok and preservation_kernel(I) == 0
    ok = ok and all(GA.eq(beta_part(rho, mu), GA.sub(NI, GA.scal(rho, N0))) for mu in range(4))
    th, Ip, I0, unit = rotated_frozen_row(rho, XI)
    ok = ok and unit and all(GA.is_zero(comm(t, Ip)) for t in th)
    ok = ok and not all(GA.is_zero(comm(t, I0)) for t in th)
    ok = ok and dot(N0, Ip) == 1 and dot(Ip, Ip) == 2 * rho
    GA.check("integrand depends only on I^X and the Lorentz block; T(rho id) = 2 rho e^e; dilation "
             "invisible; the connection preserves ninf + rho n0 iff S = rho id and beta = 0; a special-conformal "
             "rotor moves the frozen row to one preserving the rotated tractor (<X, I'> = 1)", ok)
    assert ok


def check_free_slot_returns_the_schouten_slot_and_the_weyl_square():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    c = setup()
    ok = len(c['alg']) == 20 and GA.rank_of_vectors(c['Mtt']) == 16
    for y in SAMPLES:
        x = algebraic_sample(y)
        P, R = schouten(x)
        St = free_slot(x)
        ok = ok and St == P and R != 0
        ok = ok and lorentz_block(x, St) == minus_weyl(x)
    ok = ok and free_slot(de_sitter_curvature(KAP)) == scalar4(KAP / 2)
    q, k, const = reduced(ALL_PARTS, RHO1)
    ok = ok and q == [Fr(1), Fr(0), Fr(0), Fr(0)] and k == 0 and const == 0
    xt = unit_curvature(XT_INDEX)
    ok = ok and any(bianchi(xt)) and has_antisymmetric_part(free_slot(xt))
    GA.check("free slot: S* = Schouten map, F_W = -Weyl, reduced Lagrangian |W|^2/4; with torsion the "
             "antisymmetric slot responds", ok)
    assert ok


def check_slot_lattice():
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("synthesis.curvature-only-tractor-actions-are-macdowell-mansouri")
    c = setup()
    euler = [Fr(1), Fr(0), Fr(-1, 2), Fr(1, 24)]
    ok = fit_invariants(c['Mgg']) == euler
    rows = lattice_rows()
    ok = ok and len(rows) == 8
    for rho in RHOS:
        for J in rows:
            q, k, const = reduced(J, rho)
            wq = list(euler)
            if 'trace' in J:
                wq[3] -= Fr(1, 24)
            if 'tf' in J:
                wq[2] += Fr(1, 2)
            frozen = 'trace' not in J
            ok = ok and q == wq
            ok = ok and k == (-2 * rho if frozen else 0)
            ok = ok and const == (24 * rho * rho if frozen else 0)
            if frozen:
                lam = 6 * rho
                ok = ok and const == -k * 2 * lam
    q, k, const = reduced((), Fr(0))
    ok = ok and q == euler and k == 0 and const == 0
    GA.check("slot lattice: Euler + Einstein-Hilbert + Lambda = 6 rho only with the symmetric slot frozen; "
             "trace free adds -R^2/24 and removes EH; trace-free part free adds |Ric_tf|^2/2", ok)
    assert ok


def sphere_product(K1, K2):
    """Riemannian S2 x S2, orthonormal frame: R_0101 = K1, R_2323 = K2. Returns pointwise
    (|W|^2, |Ric_tf|^2, R^2, E4) and the volume over 16 pi^2, 1/(K1 K2)."""
    Rm = {}
    for (a, b, K) in ((0, 1, K1), (2, 3, K2)):
        for (p, q, s) in ((a, b, 1), (b, a, -1)):
            Rm[(p, q, a, b)] = s * K
            Rm[(p, q, b, a)] = -s * K
    R4 = lambda a, b, c, d: Rm.get((a, b, c, d), Fr(0))
    Ric = [[sum(R4(c, a, c, b) for c in range(4)) for b in range(4)] for a in range(4)]
    R = sum(Ric[a][a] for a in range(4))
    P = [[(Ric[a][b] - (R / 6 if a == b else 0)) / 2 for b in range(4)] for a in range(4)]
    dl = lambda a, b: Fr(1) if a == b else Fr(0)
    rng = range(4)
    W2 = sum((R4(a, b, c, d) - (dl(a, c) * P[b][d] - dl(a, d) * P[b][c] + dl(b, d) * P[a][c]
                                - dl(b, c) * P[a][d])) ** 2 for a in rng for b in rng for c in rng for d in rng)
    Riem2 = sum(R4(a, b, c, d) ** 2 for a in rng for b in rng for c in rng for d in rng)
    Ric2 = sum(Ric[a][b] ** 2 for a in rng for b in rng)
    tf2 = Ric2 - R * R / 4
    return [W2, tf2, R * R, Riem2 - 4 * Ric2 + R * R], 1 / (K1 * K2)


def check_quadratic_remainders_are_not_variationally_trivial():
    premise("synthesis.imported-lovelock-and-anderson-duchamp-natural-lagrangians")
    premise("synthesis.imported-conformal-gravity-bach-equations-and-conformal-gauge-form")
    premise("synthesis.frozen-point-integrand-on-tractor-transport-is-weyl-squared")
    ints = []
    for K1, K2 in SPHERES:
        vals, vol = sphere_product(K1, K2)
        ints.append([v * vol for v in vals])
    ok = [row[3] for row in ints] == [8, 8, 8]
    ok = ok and [row[0] for row in ints] == [Fr(16, 3), Fr(6), Fr(98, 15)]
    ok = ok and [row[1] for row in ints] == [Fr(0), Fr(1, 2), Fr(9, 10)]
    ok = ok and [row[2] for row in ints] == [Fr(16), Fr(18), Fr(98, 5)]
    for f in REMAINDERS:
        ok = ok and len({f(row) for row in ints}) == 3
    GA.check("on S2 x S2 the Euler integral is constant (8 x 16 pi^2) while the R^2, |Ric_tf|^2 and |W|^2 "
             "remainders vary with K2/K1: none is variationally trivial", ok)
    assert ok
