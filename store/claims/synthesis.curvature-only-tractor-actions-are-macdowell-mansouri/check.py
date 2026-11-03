"""Curvature-only actions of the Cl(2,4) tractor gauge field: exact checks of the classification.

Cl(2,4) with generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1); n0 = (e+ + e-)/2, ninf = e+ - e-;
frozen point I = ninf + (Lambda/6) n0 (Q(I) = Lambda/3), canonical tractor X = n0, Stelle-West vector
V = X - (3/Lambda) I (Q(V) = -3/Lambda, I.V = 0); W = span(e0, e1, e2, e3) = {I, V}^perp.
The gauge algebra acts on bivectors by the commutator product. A curvature-only density is B(F ^ F) with
B a symmetric bilinear form on the values of F; it is gauge invariant iff B is invariant under the algebra.
  K(F, G) = <F G>_0                       (Killing form: the Chern-Weil density)
  H(F, G) = <(F^I^V)(G^I^V)>_0            (Killing form of the W block: Holst type)
  M(F, G) = <(F^G^I^V) i6>_0 = eps(I, V, F, G) = eps(I, X, F, G)   (MacDowell-Mansouri)
(1) so(2,4) (no datum): invariant symmetric forms dim 1 (= K); parabolic algebra of the line of X: dim 1;
    stab(X) on all bivectors: dim 2, none odd under the internal reflection in e1 (which fixes X);
    stab(X) on Lambda^2(X^perp) (= stab(X) as a space; F.X = 0): dim 2, exactly one internally odd,
    spanned by eps(I, X, ., .) restricted there.
(2) stab(I) on Lambda^2(I^perp) = stab(I): dim 1 (= K), for Lambda = 3, -3.
(3) stab(I) cap stab(V) on Lambda^2(I^perp): dim 3 = span(K, H, M); M = eps(I, X, ., .); under the
    internal reflection in e1 (values only, spacetime orientation fixed): K, H even, M odd, the odd subspace is span(M); K is stab(I)-invariant, H and M are
    not. For Lambda = 3, -3, 9/7.
(4) Frame Euler-Lagrange map (frame = identity at a point, F_W = -R + (Lambda/3) e^e):
    E_B(d, u) = sum eps^{d nu rho sigma} B(u ^ e_nu, F_W(rho, sigma)). M: rank 10 on the 20 algebraic
    curvature tensors (first Bianchi kernel of the 36 curvature 2-forms), 16 on all; zero on de Sitter.
    H: rank 0 on algebraic curvatures, 16 on all 36 (only torsion feeds it).
(5) Hypotheses: first-order e^e^F invariants (B on Lambda^2 W x Lambda^2(I^perp)) dim 2; without reduction
    by I (F anywhere, invariance under stab(I, V)) dim 6; Lorentz commutant on W dim 1, and the slot
    rho e makes I_rho = ninf + rho n0 parallel.
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
BIV = [GA.mul(E[i], E[j], S) for i, j in combinations(range(6), 2)]
W = E[:4]
L2W = [GA.mul(W[a], W[b], S) for a, b in combinations(range(4), 2)]
PAIRS = list(combinations(range(4), 2))


def mul(x, y):
    return GA.mul(x, y, S)


I6 = mul(mul(mul(E[0], E[1]), mul(E[2], E[3])), mul(E[4], E[5]))


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def wedge(x, y, r, s):
    return grade(mul(x, y), r + s)


def comm(x, y):
    return GA.scal(Fr(1, 2), GA.sub(mul(x, y), mul(y, x)))


def sc(x):
    return x.get((), Fr(0))


def dot(a, b):
    return GA.dot(a, b, S)


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
        p = r[c0]
        r = [a / p for a in r]
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


def coords(x, basis):
    blades = sorted({b for u in basis for b in u} | set(x))
    n = len(basis)
    m = [[u.get(b, Fr(0)) for u in basis] + [x.get(b, Fr(0))] for b in blades]
    cols, row = [], 0
    for col in range(n):
        p = next((r for r in range(row, len(m)) if m[r][col] != 0), None)
        if p is None:
            continue
        m[row], m[p] = m[p], m[row]
        pv = m[row][col]
        m[row] = [a / pv for a in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[row])]
        cols.append(col)
        row += 1
    assert all(m[r][n] == 0 for r in range(row, len(m)))
    out = [Fr(0)] * n
    for i, col in enumerate(cols):
        out[col] = m[i][n]
    return out


def stabiliser(vectors):
    rows = []
    for v in vectors:
        imgs = [comm(b, v) for b in BIV]
        for bb in sorted({k for im in imgs for k in im}):
            rows.append([im.get(bb, Fr(0)) for im in imgs])
    return [GA.add(*[GA.scal(c, BIV[i]) for i, c in enumerate(x) if c != 0]) for x in nullspace(rows, 15)]


def act(xi, U, how=comm):
    cols = [coords(how(xi, u), U) for u in U]
    return [[cols[j][i] for j in range(len(U))] for i in range(len(U))]


def invariant_forms(U1, U2, gens, symmetric, parity=None):
    """Bilinear B on U1 x U2 with B(xi.u, v) + B(u, xi.v) = 0; parity = (sign, matrix) imposes
    B(Ru, Rv) = sign B(u, v)."""
    k1, k2 = len(U1), len(U2)
    if symmetric:
        idx = {}
        for i in range(k1):
            for j in range(i, k1):
                idx[(i, j)] = len(idx)
        var = lambda i, j: idx[(min(i, j), max(i, j))]
        nv = len(idx)
    else:
        var = lambda i, j: i * k2 + j
        nv = k1 * k2
    rows = []
    for xi in gens:
        A1 = act(xi, U1)
        A2 = A1 if symmetric else act(xi, U2)
        for i in range(k1):
            for j in range(k2):
                r = [Fr(0)] * nv
                for m in range(k1):
                    r[var(m, j)] += A1[m][i]
                for m in range(k2):
                    r[var(i, m)] += A2[m][j]
                rows.append(r)
    if parity is not None:
        sgn, R = parity
        for i in range(k1):
            for j in range(k2):
                r = [Fr(0)] * nv
                for m in range(k1):
                    for n in range(k2):
                        r[var(m, n)] += R[m][i] * R[n][j]
                r[var(i, j)] -= sgn
                rows.append(r)
    return [[[x[var(i, j)] for j in range(k2)] for i in range(k1)] for x in nullspace(rows, nv)]


def flat(Mt):
    return [c for row in Mt for c in row]


def rank(ms):
    return GA.rank_of_vectors([flat(m) for m in ms]) if ms else 0


def spans(basis, ms):
    return rank(basis) == len(basis) and rank(basis + ms) == len(basis)


def reflection(w, U):
    winv = GA.scal(Fr(1) / dot(w, w), w)
    return act(w, U, how=lambda a, u: mul(mul(a, u), winv))


def data(lam):
    I = GA.add(NI, GA.scal(lam / 6, N0))
    X = N0
    V = GA.sub(X, GA.scal(Fr(3) / lam, I))
    return I, X, V


def forms(I, X, V):
    K = lambda a, b: sc(mul(a, b))
    H = lambda a, b: sc(mul(wedge(wedge(a, I, 2, 1), V, 3, 1), wedge(wedge(b, I, 2, 1), V, 3, 1)))
    M = lambda a, b: sc(mul(wedge(wedge(wedge(a, b, 2, 2), I, 4, 1), V, 5, 1), I6))
    MX = lambda a, b: sc(mul(wedge(wedge(wedge(a, b, 2, 2), I, 4, 1), X, 5, 1), I6))
    return K, H, M, MX


def gram(B, U):
    return [[B(u, v) for v in U] for u in U]


def _premises():
    for pid in ("dark-energy.frozen-point-makes-stelle-west-vector",
                "synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection"):
        premise(pid)


def check_pure_transport_admits_only_the_chern_weil_density():
    _premises()
    inv = invariant_forms(BIV, BIV, BIV, True)
    K = gram(lambda a, b: sc(mul(a, b)), BIV)
    ok = len(inv) == 1 and spans(inv, [K])
    X = N0
    gX = stabiliser([X])
    dil = wedge(N0, NI, 1, 1)
    ok = ok and len(gX) == 10 and GA.eq(comm(dil, X), X)
    ok = ok and len(invariant_forms(BIV, BIV, gX + [dil], True)) == 1
    ok = ok and len(invariant_forms(BIV, BIV, gX, True)) == 2
    R1 = reflection(E[1], BIV)
    ok = ok and len(invariant_forms(BIV, BIV, gX, True, (Fr(-1), R1))) == 0
    # on Lambda^2(X^perp) (= stab(X) as a space: F.X = 0) the count is 2 with exactly one internally odd
    RX = reflection(E[1], gX)
    ok = ok and len(invariant_forms(gX, gX, gX, True)) == 2
    oddX = invariant_forms(gX, gX, gX, True, (Fr(-1), RX))
    ok = ok and len(oddX) == 1
    I, _, _ = data(Fr(3))
    epsX = gram(lambda a, b: sc(mul(wedge(wedge(wedge(a, b, 2, 2), I, 4, 1), X, 5, 1), I6)), gX)
    ok = ok and any(flat(epsX)) and spans(oddX, [epsX])
    GA.check("so(2,4) and parabolic: only K; stab(X) on all bivectors: no internally odd form; on X-perp: one, eps(I,X,.,.)", ok)
    assert ok


def check_frozen_point_alone_admits_only_the_chern_weil_density():
    _premises()
    ok = True
    for lam in (Fr(3), Fr(-3)):
        I, X, V = data(lam)
        ok = ok and dot(I, I) == lam / 3
        gI = stabiliser([I])
        inv = invariant_forms(gI, gI, gI, True)
        ok = ok and len(gI) == 10 and len(inv) == 1 and spans(inv, [gram(forms(I, X, V)[0], gI)])
    GA.check("frozen point alone: the only stab(I)-invariant density is the Chern-Weil one", ok)
    assert ok


def check_frozen_point_and_canonical_tractor_give_three_and_one_odd():
    _premises()
    ok = True
    for lam in (Fr(3), Fr(-3), Fr(9, 7)):
        I, X, V = data(lam)
        ok = ok and dot(V, V) == Fr(-3) / lam and dot(I, V) == 0 and dot(I, I) == lam / 3
        gI = stabiliser([I])
        gIV = stabiliser([I, V])
        inv = invariant_forms(gI, gI, gIV, True)
        K, H, M, MX = [gram(f, gI) for f in forms(I, X, V)]
        ok = ok and len(gIV) == 6 and len(inv) == 3 and spans(inv, [K, H, M])
        ok = ok and M == MX and any(flat(M))
        R1 = reflection(E[1], gI)
        odd = invariant_forms(gI, gI, gIV, True, (Fr(-1), R1))
        even = invariant_forms(gI, gI, gIV, True, (Fr(1), R1))
        ok = ok and len(odd) == 1 and spans(odd, [M]) and len(even) == 2 and spans(even, [K, H])
        invI = invariant_forms(gI, gI, gI, True)
        ok = ok and spans(invI, [K]) and rank(invI + [H]) == 2 and rank(invI + [M]) == 2
    GA.check("frozen point + canonical tractor: span(K, H, M), internally odd part span(eps(I,X,F,F))", ok)
    assert ok


EPS4 = {}
for p in permutations(range(4)):
    s = 1
    for i in range(4):
        for j in range(i + 1, 4):
            if p[i] > p[j]:
                s = -s
    EPS4[p] = s


def curvature(x):
    Rd = {}
    for k, (r, s) in enumerate(PAIRS):
        b = {}
        for m in range(6):
            if x[6 * k + m] != 0:
                b = GA.add(b, GA.scal(x[6 * k + m], L2W[m]))
        Rd[(r, s)] = b
        Rd[(s, r)] = GA.neg(b)
    return Rd


def frame_el(B, Rd, c):
    out = []
    for d in range(4):
        for u in range(4):
            tot = Fr(0)
            for p, s in EPS4.items():
                if p[0] == d:
                    Fw = GA.add(GA.neg(Rd[(p[2], p[3])]), GA.scal(c, wedge(W[p[2]], W[p[3]], 1, 1)))
                    tot += s * B(wedge(W[u], W[p[1]], 1, 1), Fw)
            out.append(tot)
    return out


def bianchi(x):
    Rd = curvature(x)
    out = []
    for a, b, c in combinations(range(4), 3):
        v = GA.add(comm(Rd[(a, b)], W[c]), comm(Rd[(b, c)], W[a]), comm(Rd[(c, a)], W[b]))
        out.extend([v.get((i,), Fr(0)) for i in range(4)])
    return out


def check_frame_equations_of_the_two_non_topological_densities():
    _premises()
    lam = Fr(9, 7)
    I, X, V = data(lam)
    K, H, M, MX = forms(I, X, V)
    c = lam / 3
    unit = [[Fr(1) if i == j else Fr(0) for i in range(36)] for j in range(36)]
    alg = nullspace([list(r) for r in zip(*[bianchi(x) for x in unit])], 36)
    zero = curvature([Fr(0)] * 36)
    def lin(B, x):
        return [p - q for p, q in zip(frame_el(B, curvature(x), c), frame_el(B, zero, c))]
    ok = len(alg) == 20
    ok = ok and GA.rank_of_vectors([lin(M, x) for x in alg]) == 10
    ok = ok and GA.rank_of_vectors([lin(M, x) for x in unit]) == 16
    ok = ok and GA.rank_of_vectors([lin(H, x) for x in alg]) == 0
    ok = ok and GA.rank_of_vectors([lin(H, x) for x in unit]) == 16
    ok = ok and any(frame_el(M, zero, c)) and not any(frame_el(H, zero, c))
    xds = []
    for (r, s) in PAIRS:
        xds.extend(coords(GA.scal(c, wedge(W[r], W[s], 1, 1)), L2W))
    ok = ok and not any(frame_el(M, curvature(xds), c))
    xwrong = [3 * t for t in xds]
    ok = ok and any(frame_el(M, curvature(xwrong), c))
    GA.check("frame equations: M rank 10 on algebraic curvatures, H zero there and fed only by torsion", ok)
    assert ok


def check_which_hypotheses_do_the_work():
    _premises()
    lam = Fr(9, 7)
    I, X, V = data(lam)
    gI = stabiliser([I])
    gIV = stabiliser([I, V])
    ok = len(invariant_forms(L2W, gI, gIV, False)) == 2
    ok = ok and len(invariant_forms(BIV, BIV, gIV, True)) == 6
    rows = []
    for xi in gIV:
        A = act(xi, W)
        for i in range(4):
            for j in range(4):
                r = [Fr(0)] * 16
                for k in range(4):
                    r[i * 4 + k] += A[k][j]
                    r[k * 4 + j] -= A[i][k]
                rows.append(r)
    ok = ok and len(nullspace(rows, 16)) == 1
    rho = lam / 6
    for a in ([3, 1, -2, 5], [0, 1, 0, 0]):
        Avec = GA.add(*[GA.scal(Fr(a[i]), W[i]) for i in range(4) if a[i]])
        theta = GA.add(GA.neg(wedge(NI, Avec, 1, 1)), wedge(N0, GA.scal(rho, Avec), 1, 1))
        ok = ok and GA.is_zero(comm(theta, I))
        theta2 = GA.add(GA.neg(wedge(NI, Avec, 1, 1)), wedge(N0, GA.scal(2 * rho, Avec), 1, 1))
        ok = ok and not GA.is_zero(comm(theta2, I))
    GA.check("first-order class adds 2 + 1, unreduced class has 6, Schouten slot rho e fixes the frozen point", ok)
    assert ok
