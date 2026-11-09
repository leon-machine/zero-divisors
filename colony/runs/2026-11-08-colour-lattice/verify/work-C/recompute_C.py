"""Referee C: independent exact recomputations for the colour-lattice proposals (A, B1, B2).

Routes differ from the proposals' checks where possible:
 (1) G by brute-force enumeration of all 46080 signed permutations of e3..e8 (not by generators);
 (2) SU(3) moments by the Weyl integration formula (constant term of a Laurent polynomial on the torus),
     not by su(3)-annihilated invariants;
 (3) the frozen-triplet fourth moment by the Gaussian/sphere route;
 (4) a counterexample to A's literal definition of a colour rotor;
 (5) the centre of G and the commutant of G (Schur);
 (6) the Wilson-quark kappa^4 coefficient by the trace of H^4 as a matrix on the real regular module of Cl(4,0);
 (7) the smallest plaquette set with every link covered at least twice (B1's 'first closed surface is the cube').
Exact Fractions throughout.
"""
import sys
from fractions import Fraction as F
from itertools import permutations, product, combinations
from collections import defaultdict

sys.path.insert(0, '/home/claude/phys-graph/lib')
import GA  # noqa: E402

S9 = (1,) * 9
N = 6


def blade(*ix):
    r = GA.sc(1)
    for i in ix:
        r = GA.mul(r, GA.gen(i), S9)
    return r


RE_OM = GA.add(blade(3, 5, 7), GA.scal(-1, blade(3, 6, 8)), GA.scal(-1, blade(4, 5, 8)), GA.scal(-1, blade(4, 6, 7)))
IM_OM = GA.add(blade(4, 5, 7), blade(3, 6, 7), blade(3, 5, 8), GA.scal(-1, blade(4, 6, 8)))
JB = GA.add(blade(3, 4), blade(5, 6), blade(7, 8))


def jvec(m):  # j(e_{m+3}) = e_{m+3} . J as (index, sign)
    y = GA.mul(GA.gen(m + 3), JB, S9)
    (b, c), = [(b, c) for b, c in y.items() if len(b) == 1]
    return b[0] - 3, int(c)


JM = [jvec(m) for m in range(N)]


def outer3(g, T):
    out = {}
    for b, c in T.items():
        idx = []
        sgn = c
        for k in b:
            n, s = g[k - 3]
            idx.append(n + 3)
            sgn *= s
        if len(set(idx)) < 3:
            continue
        # sort with sign
        perm = sorted(range(3), key=lambda i: idx[i])
        inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
        key = tuple(sorted(idx))
        out[key] = out.get(key, 0) + sgn * (-1) ** inv
    return {k: v for k, v in out.items() if v}


def commutes_with_j(g):
    # g(j e_m) == j g(e_m)
    for m in range(N):
        a, sa = JM[m]
        n1, s1 = g[a]
        lhs = (n1, s1 * sa)
        n2, s2 = g[m]
        b, sb = JM[n2]
        rhs = (b, sb * s2)
        if lhs != rhs:
            return False
    return True


# ---------------------------------------------------------------- (1) G by enumeration
ALL = []
for p in permutations(range(N)):
    for sg in product((1, -1), repeat=N):
        g = tuple((p[m], sg[m]) for m in range(N))
        if commutes_with_j(g):
            ALL.append(g)
assert len(ALL) == 384, len(ALL)
G = [g for g in ALL if GA.eq(outer3(g, RE_OM), RE_OM)]
assert len(G) == 96
assert all(GA.eq(outer3(g, IM_OM), IM_OM) for g in G)
# J-complex determinant of each, as an element a + b j: monomial complex 3x3 matrix
def cmat(g):
    M = [[(0, 0)] * 3 for _ in range(3)]
    for col in range(3):
        n, s = g[2 * col]
        row = n // 2
        M[row][col] = (s, 0) if n % 2 == 0 else (0, s)
    return M


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cdet_monomial(g):
    M = cmat(g)
    perm = [next(r for r in range(3) if M[r][c] != (0, 0)) for c in range(3)]
    inv = sum(1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j])
    d = ((-1) ** inv, 0)
    for c in range(3):
        d = cmul(d, M[perm[c]][c])
    return d


dets_all = defaultdict(int)
for g in ALL:
    dets_all[cdet_monomial(g)] += 1
assert dict(dets_all) == {(1, 0): 96, (-1, 0): 96, (0, 1): 96, (0, -1): 96}
assert all(cdet_monomial(g) == (1, 0) for g in G)
print('(1) J-commuting signed permutations: 384; fixing Re Omega: 96 = those of J-determinant 1;',
      'determinants equidistributed over {1,-1,j,-j}')


def compose(g, h):
    return tuple((g[h[m][0]][0], h[m][1] * g[h[m][0]][1]) for m in range(N))


# ---------------------------------------------------------------- (5) centre and commutant
centre = [z for z in G if all(compose(z, g) == compose(g, z) for g in G)]
assert centre == [tuple((m, 1) for m in range(N))]


def rmat(g):
    M = [[0] * N for _ in range(N)]
    for m, (n, s) in enumerate(g):
        M[n][m] = s
    return M


# commutant: X with X M = M X for all M in G (36 unknowns)
rows = []
for g in G[:40]:
    M = rmat(g)
    for i in range(N):
        for k in range(N):
            r = [F(0)] * 36
            for l in range(N):
                r[i * N + l] += M[l][k]      # (X M)_{ik} = sum_l X_il M_lk
                r[l * N + k] -= M[i][l]      # (M X)_{ik} = sum_l M_il X_lk
            rows.append(r)
comm_dim = 36 - GA.field_rank(rows)
assert comm_dim == 2
print('(5) centre of G (computed directly) = {1}; commutant of G in real 6x6 matrices has dim 2 = span{1, j}',
      '(irreducible on the J-complex 3-space: Schur)')

# ---------------------------------------------------------------- invariant dimensions over G by characters
tr = [sum(s for m, (n, s) in enumerate(g) if n == m) for g in G]


def tJ(g):  # J-complex trace (a, b)
    M = cmat(g)
    return (sum(M[k][k][0] for k in range(3)), sum(M[k][k][1] for k in range(3)))


def cpow(a, k):
    r = (1, 0)
    for _ in range(k):
        r = cmul(r, a)
    return r


def cconj(a):
    return (a[0], -a[1])


dimsG = [F(sum(x ** k for x in tr), 96) for k in range(1, 5)]
assert dimsG == [0, 2, 2, 20]
t4G = [F(sum(cpow(tJ(g), 4)[i] for g in G), 96) for i in (0, 1)]
t3G = [F(sum(cpow(tJ(g), 3)[i] for g in G), 96) for i in (0, 1)]
abs4G = F(sum((tJ(g)[0] ** 2 + tJ(g)[1] ** 2) ** 2 for g in G), 96)
t3tbG = [F(sum(cmul(cpow(tJ(g), 3), cconj(tJ(g)))[i] for g in G), 96) for i in (0, 1)]
assert t4G == [1, 0] and t3G == [1, 0] and abs4G == 3 and t3tbG == [0, 0]
print('    G: avg tr^k (k=1..4) =', [str(x) for x in dimsG], '; avg t^3 = 1, t^4 = 1, |t|^4 = 3, t^3 tbar = 0')

# ---------------------------------------------------------------- (2) SU(3) by Weyl integration
# Laurent polynomials in z1, z2 (z3 = 1/(z1 z2)) as dicts {(a, b): coeff}


def lmul(p, q):
    out = defaultdict(F)
    for (a, b), c in p.items():
        for (d, e), f in q.items():
            out[(a + d, b + e)] += c * f
    return {k: v for k, v in out.items() if v}


def ladd(p, q):
    out = defaultdict(F, p)
    for k, v in q.items():
        out[k] += v
    return {k: v for k, v in out.items() if v}


Z = [{(1, 0): F(1)}, {(0, 1): F(1)}, {(-1, -1): F(1)}]
Zi = [{(-1, 0): F(1)}, {(0, -1): F(1)}, {(1, 1): F(1)}]
t_poly = ladd(ladd(Z[0], Z[1]), Z[2])
tb_poly = ladd(ladd(Zi[0], Zi[1]), Zi[2])
VdM = {(0, 0): F(1)}
for i in range(3):
    for j in range(3):
        if i != j:
            VdM = lmul(VdM, ladd({(0, 0): F(1)}, {k: -v for k, v in lmul(Z[i], Zi[j]).items()}))


def haar(p):
    return lmul(p, VdM).get((0, 0), F(0)) / 6


def ppow(p, k):
    r = {(0, 0): F(1)}
    for _ in range(k):
        r = lmul(r, p)
    return r


trR = ladd(t_poly, tb_poly)
dimsSU = [haar(ppow(trR, k)) for k in range(1, 5)]
assert dimsSU == [0, 2, 2, 12]
assert haar(ppow(t_poly, 3)) == 1 and haar(ppow(t_poly, 4)) == 0
assert haar(lmul(ppow(t_poly, 2), ppow(tb_poly, 2))) == 2 and haar(lmul(ppow(t_poly, 2), tb_poly)) == 0
print('(2) SU(3) by Weyl integration: int tr^k (k=1..4) =', [str(x) for x in dimsSU],
      '; int t^3 = 1, t^4 = 0, |t|^4 = 2, t^2 tbar = 0')

# plaquette: <chi> = (ln z)'(beta), z = int exp(beta chi), chi = tr/6
def series_mean(moments, order=4):
    # moments m_k = E[chi^k], k = 0..order; returns coefficients of E[chi e^{bx}]/E[e^{bx}] up to beta^(order-1)
    fact = [1, 1, 2, 6, 24, 120]
    num = [moments[n + 1] / fact[n] for n in range(order)]
    den = [moments[n] / fact[n] for n in range(order)]
    inv = [F(0)] * order
    inv[0] = 1 / den[0]
    for n in range(1, order):
        inv[n] = -sum(den[k] * inv[n - k] for k in range(1, n + 1)) / den[0]
    return [sum(num[k] * inv[n - k] for k in range(n + 1)) for n in range(order)]


mSU = [F(1)] + [x / F(6) ** (k + 1) for k, x in enumerate(dimsSU)]
mG = [F(1)] + [x / F(6) ** (k + 1) for k, x in enumerate(dimsG)]
sSU, sG = series_mean(mSU), series_mean(mG)
assert sSU[1:] == [F(1, 18), F(1, 216), F(0)] and sG[1:] == [F(1, 18), F(1, 216), F(1, 972)] and sSU[0] == 0
print('    plaquette (single-plaquette part): SU(3)', [str(x) for x in sSU[1:]], ' G', [str(x) for x in sG[1:]])

# ---------------------------------------------------------------- (3) frozen triplet moments, sphere route
# x = coordinate of a uniform unit vector of R^6: E[x^2] = 1/n, E[x^4] = 3/(n(n+2)) (Gaussian moments / radial moments)
n = 6
Ex2, Ex4 = F(1, n), F(3, n * (n + 2))
assert (Ex2, Ex4) == (F(1, 6), F(1, 16))
# same by U(3)-type route: x = Re u11, E|u11|^4 = 2/(N(N+1)) for the Haar unitary column, E u^4 = E u^3 ubar = 0 (centre)
Eabs4 = F(2, 3 * 4)
assert F(6, 16) * Eabs4 == Ex4
c3 = Ex4 / 6 - Ex2 ** 2 / 2
assert c3 == F(-1, 288)
print('(3) E[x^2] = 1/6, E[x^4] = 1/16 (sphere and unitary-column routes), c = k/6 - k^3/288')

# ---------------------------------------------------------------- (4) A's literal definition of a colour rotor
IDX = tuple(range(3, 9))
I6 = blade(*IDX)
E = GA.sc(1)
for (a, b) in ((3, 4), (5, 6), (7, 8)):
    E = GA.mul(E, GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(I6, blade(a, b), S9))), S9)
c, s = F(3, 5), F(4, 5)                           # cos(phi/2), sin(phi/2)
RJ = GA.sc(1)
for (a, b) in ((3, 4), (5, 6), (7, 8)):
    RJ = GA.mul(RJ, GA.add(GA.sc(c), GA.scal(-s, blade(a, b))), S9)   # exp(-phi J / 2)
eI = GA.add(GA.sc(c), GA.scal(-s, I6))            # exp(-phi I / 2)
RI = GA.mul(GA.mul(eI, eI, S9), eI, S9)           # exp(-3 phi I / 2)
R = GA.mul(RI, RJ, S9)
Rt = GA.reverse(R)
assert GA.eq(GA.mul(R, Rt, S9), GA.sc(1))
assert GA.eq(GA.mul(R, E, S9), E)
assert all(len(b) % 2 == 0 for b in R)
img = GA.mul(GA.mul(R, GA.gen(3), S9), Rt, S9)
grades = sorted({len(b) for b in img})
assert grades != [1]
print('(4) R = exp(-3 phi I/2) exp(-phi J/2), cos(phi/2) = 3/5: even, R~R = 1, R E = E, but R e3 ~R has grades',
      grades, ': the literal definition admits non-rotors (a U(3) of elements, not SU(3))')

# ---------------------------------------------------------------- (6) Wilson quarks: Tr H^4 on a plaquette
S4 = (1, 1, 1, 1)
BL4 = [b for k in range(5) for b in combinations(range(4), k)]
P4 = {b: i for i, b in enumerate(BL4)}


def lmat(x):
    """16x16 left-multiplication matrix of x in Cl(4,0) (columns = basis blades)."""
    M = [[F(0)] * 16 for _ in range(16)]
    for j, b in enumerate(BL4):
        y = GA.mul(x, {b: F(1)}, S4)
        for bb, cc in y.items():
            M[P4[bb]][j] += cc
    return M


def hopf(mu, sign):
    return GA.add(GA.sc(1), GA.scal(-sign, GA.gen(mu)))


sites = [(0, 0), (1, 0), (1, 1), (0, 1)]
links = {((0, 0), (1, 0)): 0, ((0, 1), (1, 1)): 0, ((0, 0), (0, 1)): 1, ((1, 0), (1, 1)): 1}
results = []
for sample in range(10):
    Ug = {l: G[(13 * k + 29 * sample + 5 + 7 * sample * k) % 96] for k, l in enumerate(links)}

    def inverse(g):
        out = [None] * N
        for m, (nn, ss) in enumerate(g):
            out[nn] = (m, ss)
        return tuple(out)
    # H: block (x, y) = S(x->y) (x) U(x->y)
    blocks = {}
    for (a, b), mu in links.items():
        blocks[(a, b)] = (lmat(hopf(mu, 1)), rmat(Ug[(a, b)]))
        blocks[(b, a)] = (lmat(hopf(mu, -1)), rmat(inverse(Ug[(a, b)])))
    sidx = {x: i for i, x in enumerate(sites)}
    dim = 4 * 16 * 6

    def apply(vec):
        out = defaultdict(F)
        for (x, sp, co), v in vec.items():
            # (H psi)(y) gets S(y->x) U(y->x) psi(x): column (x, sp, co) contributes to rows (y, ., .)
            for (y, xx), (Sm, Um) in blocks.items():
                if xx != x:
                    continue
                for r in range(16):
                    sv = Sm[r][sp]
                    if not sv:
                        continue
                    for q in range(6):
                        uv = Um[q][co]
                        if uv:
                            out[(y, r, q)] += v * sv * uv
        return {k: val for k, val in out.items() if val}
    trace4 = F(0)
    for x in sites:
        for sp in range(16):
            for co in range(6):
                v = {(x, sp, co): F(1)}
                for _ in range(4):
                    v = apply(v)
                trace4 += v.get((x, sp, co), F(0))
    # holonomy round the square (0,0)->(1,0)->(1,1)->(0,1)->(0,0)
    UC = compose(compose(compose(Ug[((0, 0), (1, 0))], Ug[((1, 0), (1, 1))]),
                         inverse(Ug[((0, 1), (1, 1))])), inverse(Ug[((0, 0), (0, 1))]))
    trUC = sum(ss for m, (nn, ss) in enumerate(UC) if nn == m)
    # real regular module: per walk 16 <s>_0 tr_R(U_w) = 8 x (4 <s>_0 Re tr_J(U_w)), so Re Tr_C H^4 = Tr_R H^4 / 8
    term = -trace4 / 8 / 4
    results.append((term, 8 * trUC))
    assert term == 8 * trUC, (term, trUC)
assert len({b for a, b in results if b}) >= 3
print('(6) Wilson quarks, single plaquette: -(1/4) Tr_C H^4 = 2^(P-1) tr_R(U_C) = 8 tr_R(U_C) on 10 link samples, values', sorted({int(b) for a, b in results}))

# ---------------------------------------------------------------- (7) smallest plaquette set with every link covered twice
def plaquettes_of_link(link, d):
    (x, mu) = link
    out = []
    for nu in range(d):
        if nu == mu:
            continue
        for sgn in (0, -1):
            base = list(x)
            base[nu] += sgn
            out.append((tuple(base), min(mu, nu), max(mu, nu)))
    return out


def links_of_plaq(p):
    x, mu, nu = p
    e = lambda v, k: tuple(v[i] + (1 if i == k else 0) for i in range(len(v)))
    return [(x, mu), (e(x, mu), nu), (e(x, nu), mu), (x, nu)]


def min_closed(d, cap):
    p0 = ((0,) * d, 0, 1)
    best = [None]

    def rec(S, cnt):
        if best[0] is not None and len(S) >= best[0]:
            return
        once = [l for l, c in cnt.items() if c == 1]
        if not once:
            best[0] = len(S)
            return
        if len(S) >= cap:
            return
        l = min(once)
        for p in plaquettes_of_link(l, d):
            if p in S:
                continue
            c2 = dict(cnt)
            for ll in links_of_plaq(p):
                c2[ll] = c2.get(ll, 0) + 1
            rec(S | {p}, c2)
    cnt = {}
    for ll in links_of_plaq(p0):
        cnt[ll] = 1
    rec({p0}, cnt)
    return best[0]


assert min_closed(3, 6) == 6 and min_closed(4, 6) == 6
print('(7) smallest set of plaquettes containing a given one with every link in at least two of them: 6 (d = 3, 4)')
print('ALL RECOMPUTATIONS PASSED')
