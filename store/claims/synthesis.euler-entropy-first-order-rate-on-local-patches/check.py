"""synthesis.euler-entropy-first-order-rate-on-local-patches: exact checks.

Spacetime metrics with rational polynomial components in coordinates (u, v, x, y), equal to
-2 du dv + dx^2 + dy^2 at p = 0 with no linear terms (so the Christoffel symbols vanish at p).
A local Rindler element through p: a polynomial embedding X0(s1, s2) tangent to d_x, d_y at p, its
future null normal k (k = d_u at p, k^u = n(s) prescribed) solved as a truncated power series, and the
generators X0 + lam k. Everything is exact truncated multivariate power series over Q.
check_first_order_rate_formula: on three polynomial metrics with generic Ricci, Weyl and gradients and
elements with theta_k = sigma_k = 0 at p and generic l-extrinsic curvature, normalisation gradient and
cubic data, the lam-derivative at p of sqrt(h) R_Sigma (Jacobson-Myers) equals
theta_l Ric(k,k) - 2 sigma_l:C(.,k,.,k) + 4 omega.Z + (nabla_k R)(e_a,e_b,e_a,e_b), and that of
h^{ac}h^{bd}R_abcd (Noether form) equals 4 omega.Z + (nabla_k R)(e_a,e_b,e_a,e_b); the gradient term is
2 D^b Z_b (second Bianchi identity).
check_ppwave_cases: flat space (zero for a curved element), vacuum pp-wave (rate -2 sigma_l:C, nonzero),
null dust (rate theta_l Ric(k,k)), and independence of third- and fourth-order element data.
check_flat_element_vacuum: vacuum pp-wave, tilted null direction, flat element, omega = 0: both forms give
(nabla_k R)(e,e,e,e) = 6, nonzero, with Ric(k,k) = 0.
check_null_data_force_constant_curvature: Ric(k,k) = 0 for every null k forces the trace-free Ricci tensor
to vanish (rank 9), and C(e_a,k,e_b,k) = 0 for every null k and screen forces the Weyl tensor to vanish
(rank 10).
check_first_order_defect: order counting of the Clausius balance with the Jacobson-Myers entropy.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise


def setup_rate():
    premise("synthesis.euler-term-horizon-entropy-shift")
    premise("synthesis.imported-wald-noether-charge-entropy")
    premise("synthesis.imported-raychaudhuri-null-congruence")


def setup_clausius():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.imported-jacobson-clausius-1995")
    premise("synthesis.euler-term-horizon-entropy-shift")


# ---------------------------------------------------------------- truncated power series over Q
class S:
    """Truncated power series in n variables, total degree <= D, exact rational coefficients."""
    __slots__ = ("c", "n", "D")

    def __init__(self, c, n, D):
        self.n, self.D = n, D
        self.c = {e: F(v) for e, v in c.items() if v != 0 and sum(e) <= D}

    @staticmethod
    def k(a, n, D):
        return S({(0,) * n: a}, n, D)

    def _l(self, o):
        return o if isinstance(o, S) else S.k(o, self.n, self.D)

    def __add__(self, o):
        o = self._l(o)
        c = dict(self.c)
        for e, v in o.c.items():
            c[e] = c.get(e, F(0)) + v
        return S(c, self.n, self.D)

    __radd__ = __add__

    def __neg__(self):
        return S({e: -v for e, v in self.c.items()}, self.n, self.D)

    def __sub__(self, o):
        return self + (-self._l(o))

    def __mul__(self, o):
        if not isinstance(o, S):
            return S({e: v * o for e, v in self.c.items()}, self.n, self.D)
        c = {}
        for e1, v1 in self.c.items():
            d1 = sum(e1)
            for e2, v2 in o.c.items():
                if d1 + sum(e2) <= self.D:
                    e = tuple(a + b for a, b in zip(e1, e2))
                    c[e] = c.get(e, F(0)) + v1 * v2
        return S(c, self.n, self.D)

    __rmul__ = __mul__

    def c0(self):
        return self.c.get((0,) * self.n, F(0))

    def at(self, e):
        return self.c.get(tuple(e), F(0))

    def d(self, i):
        c = {}
        for e, v in self.c.items():
            if e[i]:
                f = list(e)
                f[i] -= 1
                c[tuple(f)] = c.get(tuple(f), F(0)) + v * e[i]
        return S(c, self.n, self.D)

    def inv(self):
        a0 = self.c0()
        x = (self - a0) * (1 / a0)
        out, p = S.k(1, self.n, self.D), S.k(1, self.n, self.D)
        for _ in range(self.D):
            p = p * (-x)
            out = out + p
        return out * (1 / a0)

    def sqrt1(self):
        x = self - 1
        out, p, cf = S.k(1, self.n, self.D), S.k(1, self.n, self.D), F(1)
        for j in range(1, self.D + 1):
            cf = cf * (F(1, 2) - (j - 1)) / j
            p = p * x
            out = out + p * cf
        return out


def peval(poly, args, n, D):
    out = S.k(0, n, D)
    pw = {}
    for e, v in poly.items():
        t = S.k(v, n, D)
        for i, m in enumerate(e):
            if m:
                if (i, m) not in pw:
                    q = S.k(1, n, D)
                    for _ in range(m):
                        q = q * args[i]
                    pw[(i, m)] = q
                t = t * pw[(i, m)]
        out = out + t
    return out


BASE = {(0, 1): {(0, 0, 0, 0): F(-1)}, (2, 2): {(0, 0, 0, 0): F(1)}, (3, 3): {(0, 0, 0, 0): F(1)}}


def with_base(pert):
    met = {}
    for key in set(BASE) | set(pert):
        p = dict(BASE.get(key, {}))
        for e, v in pert.get(key, {}).items():
            p[e] = p.get(e, F(0)) + v
        met[key] = p
    return met


def gmat(met, X, n, D):
    g = [[None] * 4 for _ in range(4)]
    for a in range(4):
        for b in range(a, 4):
            p = met.get((a, b), {})
            g[a][b] = g[b][a] = peval(p, X, n, D) if p else S.k(0, n, D)
    return g


def gdot(g, x, y):
    out = S.k(0, x[0].n, x[0].D)
    for a in range(4):
        for b in range(4):
            if g[a][b].c:
                out = out + g[a][b] * x[a] * y[b]
    return out


def inv3(M):
    det = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
           + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    C = [[(-1) ** (i + j) * ((lambda m: m[0][0] * m[1][1] - m[0][1] * m[1][0])(
        [[M[r][c] for c in range(3) if c != j] for r in range(3) if r != i])) for j in range(3)] for i in range(3)]
    return [[C[j][i] / det for j in range(3)] for i in range(3)]


N3, DD = 3, 5   # variables (s1, s2, lam); truncation degree


def ser(c):
    """Polynomial in (s1, s2) given as {(i, j): coeff}."""
    return S({(i, j, 0): v for (i, j), v in c.items()}, N3, DD)


def element(met, X0, k0, nfun, fixed):
    """Null normal k along the element X0 with k[fixed] = nfun and k = k0 at p."""
    free = [i for i in range(4) if i != fixed]
    e1 = [X0[m].d(0) for m in range(4)]
    e2 = [X0[m].d(1) for m in range(4)]
    g = gmat(met, X0, N3, DD)
    k = [S.k(k0[m], N3, DD) for m in range(4)]
    k[fixed] = nfun
    g0 = [[g[a][b].c0() for b in range(4)] for a in range(4)]
    J = [[sum(g0[m][q] * v[q].c0() for q in range(4)) for m in free] for v in (e1, e2)]
    J.append([sum(g0[m][q] * k0[q] for q in range(4)) for m in free])
    Ji = inv3(J)
    for _ in range(DD + 3):
        Fv = [gdot(g, k, e1), gdot(g, k, e2), gdot(g, k, k) * F(1, 2)]
        for i, m in enumerate(free):
            corr = S.k(0, N3, DD)
            for j in range(3):
                if Ji[i][j]:
                    corr = corr + Fv[j] * Ji[i][j]
            k[m] = k[m] - corr
    assert not any(f.c for f in (gdot(g, k, e1), gdot(g, k, e2), gdot(g, k, k)))
    return k


def jm_rate(met, X0, k0, nfun, fixed):
    """lam-coefficient at p of sqrt(det h) R_Sigma, and B_k(p) = (1/2) lam-coefficient of h at p."""
    k = element(met, X0, k0, nfun, fixed)
    lam = S({(0, 0, 1): 1}, N3, DD)
    X = [X0[m] + lam * k[m] for m in range(4)]
    g = gmat(met, X, N3, DD)
    e = [[X[m].d(a) for m in range(4)] for a in range(2)]
    h = [[gdot(g, e[a], e[b]) for b in range(2)] for a in range(2)]
    det = h[0][0] * h[1][1] - h[0][1] * h[1][0]
    di = det.inv()
    hi = [[h[1][1] * di, -h[0][1] * di], [-h[1][0] * di, h[0][0] * di]]
    dh = [[[h[a][b].d(c) for c in range(2)] for b in range(2)] for a in range(2)]
    G = [[[sum(((hi[c][q] * (dh[q][b][a] + dh[q][a][b] - dh[a][b][q])) for q in range(2)), S.k(0, N3, DD)) * F(1, 2)
           for b in range(2)] for a in range(2)] for c in range(2)]
    R = S.k(0, N3, DD)
    for a in range(2):
        for b in range(2):
            t = S.k(0, N3, DD)
            for c in range(2):
                t = t + G[c][a][b].d(c) - G[c][a][c].d(b)
                for q in range(2):
                    t = t + G[c][c][q] * G[q][a][b] - G[c][b][q] * G[q][a][c]
            R = R + hi[a][b] * t
    Bk = [[h[a][b].at((0, 0, 1)) / 2 for b in range(2)] for a in range(2)]
    return (det.sqrt1() * R).at((0, 0, 1)), Bk, k, [[e[a][m].c0() for m in range(4)] for a in range(2)]


def riemann(met):
    """R_abcd as series in the coordinates (degree <= 1 reliable); convention R^a_bcd = d_c G^a_db - ..."""
    n, D = 4, 3
    xs = [S({tuple(int(j == i) for j in range(4)): 1}, n, D) for i in range(4)]
    g = gmat(met, xs, n, D)
    g0 = [[g[a][b].c0() for b in range(4)] for a in range(4)]
    # inverse of g0 by hand (g0 is the null form at p): rows solve g0 x = e_i
    g0i = [[F(0)] * 4 for _ in range(4)]
    g0i[0][1] = g0i[1][0] = F(-1)
    g0i[2][2] = g0i[3][3] = F(1)
    assert all(sum(g0[a][q] * g0i[q][b] for q in range(4)) == int(a == b) for a in range(4) for b in range(4))
    dg = [[g[a][b] - g0[a][b] for b in range(4)] for a in range(4)]
    M = [[sum((g0i[a][q] * dg[q][b] for q in range(4)), S.k(0, n, D)) for b in range(4)] for a in range(4)]
    term = [[S.k(g0i[a][b], n, D) for b in range(4)] for a in range(4)]
    gi = [row[:] for row in term]
    for _ in range(D + 1):
        term = [[sum((M[a][q] * term[q][b] for q in range(4)), S.k(0, n, D)) * (-1) for b in range(4)] for a in range(4)]
        gi = [[gi[a][b] + term[a][b] for b in range(4)] for a in range(4)]
    dg1 = [[[g[a][b].d(c) for c in range(4)] for b in range(4)] for a in range(4)]
    G = [[[sum((gi[c][q] * (dg1[q][b][a] + dg1[q][a][b] - dg1[a][b][q]) for q in range(4) if gi[c][q].c),
               S.k(0, n, D)) * F(1, 2) for b in range(4)] for a in range(4)] for c in range(4)]
    Ru = {}
    for a, b, c, d in product(range(4), repeat=4):
        t = G[a][d][b].d(c) - G[a][c][b].d(d)
        for q in range(4):
            t = t + G[a][c][q] * G[q][d][b] - G[a][d][q] * G[q][c][b]
        Ru[(a, b, c, d)] = t
    Rl = {}
    for a, b, c, d in product(range(4), repeat=4):
        t = S.k(0, n, D)
        for q in range(4):
            if g[a][q].c and Ru[(q, b, c, d)].c:
                t = t + g[a][q] * Ru[(q, b, c, d)]
        Rl[(a, b, c, d)] = t
    return Rl


def Rv(Rl, v, deriv=None):
    """R(v1,v2,v3,v4) at p, or its coordinate derivative along deriv (a vector) at p."""
    out = F(0)
    for (a, b, c, d), t in Rl.items():
        co = v[0][a] * v[1][b] * v[2][c] * v[3][d]
        if co:
            if deriv is None:
                out += co * t.c0()
            else:
                out += co * sum(deriv[i] * t.at(tuple(int(j == i) for j in range(4))) for i in range(4))
    return out


def noether_rate(Rl, k, E):
    """lam-derivative at p of h^{ac}h^{bd}R(e_a,e_b,e_c,e_d) along the dragged element (e_a + lam d_a k)."""
    k0 = [k[m].c0() for m in range(4)]
    dk = [[k[m].d(a).c0() for m in range(4)] for a in range(2)]
    # h at p is the identity in (e1, e2) and its lam-derivative is 2 B_k = 0 (checked by the caller)
    tot = F(0)
    for a, b in product(range(2), repeat=2):
        idx = [a, b, a, b]
        tot += Rv(Rl, [E[i] for i in idx], deriv=k0)
        for slot in range(4):
            vs = [E[i] for i in idx]
            vs[slot] = dk[idx[slot]]
            tot += Rv(Rl, vs)
    return tot


def formula_terms(Rl, E, K, Bl, om):
    """theta_l Ric(k,k), sigma_l:C(.,k,.,k), omega.Z, (nabla_k R)(e,e,e,e), 2 D^b Z_b at p (Gamma(p) = 0)."""
    Rk = [[Rv(Rl, [E[a], K, E[b], K]) for b in range(2)] for a in range(2)]
    Rkk = Rk[0][0] + Rk[1][1]
    thl = Bl[0][0] + Bl[1][1]
    sig = [[Bl[a][b] - (thl / 2) * int(a == b) for b in range(2)] for a in range(2)]
    Ck = [[Rk[a][b] - (Rkk / 2) * int(a == b) for b in range(2)] for a in range(2)]
    sC = sum(sig[a][b] * Ck[a][b] for a in range(2) for b in range(2))
    Z = [sum(Rv(Rl, [E[a], K, E[a], E[b]]) for a in range(2)) for b in range(2)]
    oZ = om[0] * Z[0] + om[1] * Z[1]
    gradR = sum(Rv(Rl, [E[a], E[b], E[a], E[b]], deriv=K) for a in range(2) for b in range(2))
    divZ = sum(Rv(Rl, [E[a], K, E[a], E[b]], deriv=E[b]) for a in range(2) for b in range(2))
    return thl * Rkk, sC, oZ, gradR, 2 * divZ, Rkk


K0 = [F(1), F(0), F(0), F(0)]
L0 = [F(0), F(1), F(0), F(0)]
E0 = [[F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]


def run_case(pert, cut):
    met = with_base(pert)
    xc = {(1, 0): F(1)}
    xc.update(cut['X'])
    yc = {(0, 1): F(1)}
    yc.update(cut['Y'])
    nc = {(0, 0): F(1)}
    nc.update(cut['n'])
    X0 = [ser(cut['U']), ser(cut['V']), ser(xc), ser(yc)]
    nf = ser(nc)
    rate, Bk, k, E = jm_rate(met, X0, K0, nf, 0)
    Rl = riemann(met)
    U = cut['U']
    Bl = [[2 * U.get((2, 0), 0), U.get((1, 1), 0)], [U.get((1, 1), 0), 2 * U.get((0, 2), 0)]]
    # omega_b = -g(l, nabla_b k) at p = d_b k^u (Gamma(p) = 0, l = d_v)
    om = [k[0].d(0).c0(), k[0].d(1).c0()]
    return rate, Bk, k, E, Rl, Bl, om

DATA = [
    ({(0, 0): {(0, 0, 2, 0): F(-2, 1), (1, 0, 1, 1): F(1, 2), (0, 1, 2, 0): F(1, 1)}, (0, 1): {(1, 1, 1, 0): F(2, 1), (1, 0, 0, 1): F(1, 1), (1, 0, 1, 1): F(1, 1)}, (0, 2): {(0, 0, 1, 1): F(-1, 1), (2, 0, 0, 0): F(1, 1), (0, 0, 0, 3): F(2, 1)}, (0, 3): {(1, 0, 2, 0): F(-2, 1), (0, 3, 0, 0): F(3, 2), (0, 0, 1, 1): F(1, 2)}, (1, 1): {(1, 0, 1, 1): F(3, 1), (0, 2, 0, 1): F(-1, 1), (2, 0, 0, 1): F(-3, 1)}, (1, 2): {(1, 0, 2, 0): F(1, 2), (0, 1, 1, 0): F(1, 1), (0, 2, 0, 1): F(3, 2), (0, 0, 2, 0): F(1, 1)}, (1, 3): {(1, 0, 2, 0): F(2, 1), (0, 2, 1, 0): F(2, 1), (2, 0, 1, 0): F(1, 1)}, (2, 2): {(1, 0, 0, 2): F(-3, 2), (2, 0, 0, 1): F(-3, 2), (0, 1, 2, 0): F(3, 1), (1, 0, 0, 1): F(-1, 1)}, (2, 3): {(1, 0, 0, 1): F(-1, 1)}, (3, 3): {(0, 0, 2, 1): F(-1, 1), (0, 1, 0, 1): F(1, 1), (1, 0, 0, 1): F(-3, 1)}},
     {'U': {(2, 0): F(-1, 1), (1, 1): F(-1, 1), (0, 2): F(-3, 1), (3, 0): F(3, 1)}, 'V': {(3, 0): F(-3, 2), (1, 2): F(-1, 2)}, 'X': {(0, 2): F(-1, 2)}, 'Y': {}, 'n': {(1, 0): F(1, 1), (0, 1): F(3, 1), (2, 0): F(-3, 2)}}),
    ({(0, 0): {(1, 1, 0, 1): F(1, 2), (2, 1, 0, 0): F(-3, 2), (0, 3, 0, 0): F(3, 1), (0, 0, 0, 2): F(-1, 1)}, (0, 1): {(0, 1, 2, 0): F(1, 1), (0, 2, 0, 1): F(2, 1), (0, 2, 1, 0): F(1, 1), (1, 1, 1, 0): F(-1, 2)}, (0, 2): {(1, 0, 2, 0): F(-1, 2), (0, 0, 2, 0): F(-1, 1), (0, 0, 2, 1): F(-1, 2), (0, 1, 0, 2): F(-1, 1)}, (0, 3): {(0, 0, 2, 0): F(-3, 2), (0, 2, 0, 1): F(-3, 1), (0, 0, 1, 1): F(3, 2)}, (1, 1): {(0, 1, 0, 2): F(-2, 1), (0, 2, 1, 0): F(-2, 1)}, (1, 2): {(0, 0, 3, 0): F(1, 1), (0, 1, 1, 1): F(-1, 1), (1, 0, 1, 0): F(-1, 1), (2, 1, 0, 0): F(1, 2)}, (1, 3): {(1, 0, 0, 2): F(1, 1), (0, 2, 1, 0): F(-1, 1), (0, 0, 3, 0): F(3, 1)}, (2, 2): {(0, 0, 2, 1): F(-1, 1), (1, 0, 1, 0): F(2, 1), (0, 0, 0, 3): F(3, 2)}, (2, 3): {(1, 0, 0, 2): F(-2, 1), (3, 0, 0, 0): F(1, 1), (2, 0, 0, 1): F(-3, 2), (0, 0, 0, 2): F(-1, 1)}, (3, 3): {(0, 0, 3, 0): F(-3, 1), (2, 0, 0, 0): F(1, 2), (0, 0, 2, 0): F(1, 1), (1, 0, 2, 0): F(-3, 2)}},
     {'U': {(2, 0): F(3, 2), (1, 1): F(-3, 2), (0, 2): F(1, 1), (3, 0): F(-3, 2)}, 'V': {(3, 0): F(-1, 1), (1, 2): F(-1, 1)}, 'X': {(2, 1): F(-1, 1)}, 'Y': {(2, 0): F(-3, 2)}, 'n': {(1, 0): F(-3, 1), (0, 1): F(1, 1), (2, 0): F(1, 1)}}),
    ({(0, 0): {(1, 0, 1, 0): F(-2, 1), (1, 0, 1, 1): F(-2, 1), (0, 2, 1, 0): F(2, 1)}, (0, 1): {(3, 0, 0, 0): F(1, 1), (1, 0, 2, 0): F(1, 1), (0, 3, 0, 0): F(-1, 1), (0, 0, 1, 1): F(3, 2)}, (0, 2): {(0, 2, 0, 0): F(-1, 2), (0, 2, 0, 1): F(3, 1), (2, 0, 0, 0): F(-1, 1)}, (0, 3): {(0, 0, 3, 0): F(-1, 1), (0, 2, 0, 0): F(-2, 1)}, (1, 1): {(1, 0, 0, 2): F(-2, 1), (2, 1, 0, 0): F(-1, 1), (1, 1, 0, 1): F(2, 1), (1, 0, 2, 0): F(1, 2)}, (1, 2): {(1, 1, 0, 1): F(-1, 1), (3, 0, 0, 0): F(1, 2)}, (1, 3): {(2, 0, 0, 0): F(-1, 1), (0, 0, 0, 3): F(3, 1)}, (2, 2): {(2, 0, 0, 0): F(-3, 2), (1, 0, 0, 2): F(3, 1), (1, 0, 1, 0): F(1, 1)}, (2, 3): {(0, 3, 0, 0): F(3, 2), (0, 0, 2, 1): F(2, 1), (0, 0, 1, 2): F(3, 2)}, (3, 3): {(0, 2, 0, 0): F(2, 1), (2, 0, 0, 0): F(-1, 2), (2, 1, 0, 0): F(-3, 2), (1, 0, 1, 0): F(1, 2)}},
     {'U': {(2, 0): F(1, 1), (0, 2): F(3, 1), (3, 0): F(-1, 1)}, 'V': {(3, 0): F(1, 2), (1, 2): F(1, 1)}, 'X': {(0, 2): F(1, 2), (2, 1): F(3, 1)}, 'Y': {(2, 0): F(-1, 1)}, 'n': {(1, 0): F(1, 1), (0, 1): F(1, 1), (2, 0): F(3, 1)}}),
]


def check_first_order_rate_formula():
    setup_rate()
    seen = [False] * 5
    rates = []
    for pert, cut in DATA:
        rate, Bk, k, E, Rl, Bl, om = run_case(pert, cut)
        rates.append(rate)
        GA.check("element admissible: theta_k = sigma_k = 0 at p", all(x == 0 for r in Bk for x in r))
        GA.check("screen frame at p is (d_x, d_y)", E == E0)
        tR, sC, oZ, gR, dZ, Rkk = formula_terms(Rl, E0, K0, Bl, om)
        rN = noether_rate(Rl, k, E0)
        GA.check("JM rate = theta_l Ric(k,k) - 2 sigma_l:C + 4 omega.Z + (nabla_k R)(e,e,e,e): %s" % rate,
                 rate == tR - 2 * sC + 4 * oZ + gR)
        GA.check("Noether-form rate = 4 omega.Z + (nabla_k R)(e,e,e,e): %s" % rN, rN == 4 * oZ + gR)
        GA.check("JM - Noether = theta_l Ric(k,k) - 2 sigma_l:C (Gauss extrinsic term)", rate - rN == tR - 2 * sC)
        GA.check("second Bianchi: (nabla_k R)(e,e,e,e) = 2 D^b Z_b", gR == dZ)
        for i, v in enumerate((tR, sC, oZ, gR, rate - rN)):
            seen[i] = seen[i] or v != 0
    GA.check("every term of the formula is exercised (nonzero in some case)", all(seen))
    GA.check("rates of the three cases: -22, 3, 13", rates == [F(-22), F(3), F(13)])


def pp(H):
    return {(0, 0): H}


def check_ppwave_cases():
    setup_rate()
    base = {'V': {}, 'X': {}, 'Y': {}, 'n': {}}
    # flat space, curved element: zero
    r = run_case({}, dict(base, U={(2, 0): F(3), (1, 1): F(1), (0, 2): F(-2)}, V={(3, 0): F(5)}))[0]
    GA.check("flat space, curved element: rate 0", r == 0)
    # vacuum pp-wave H = 3x^2 - 3y^2 + 2xy (Ricci-flat, Weyl nonzero), anisotropic element
    H = {(0, 0, 2, 0): F(3), (0, 0, 0, 2): F(-3), (0, 0, 1, 1): F(2)}
    rate, Bk, k, E, Rl, Bl, om = run_case(pp(H), dict(base, U={(2, 0): F(1), (0, 2): F(-1), (1, 1): F(2)}))
    tR, sC, oZ, gR, dZ, Rkk = formula_terms(Rl, E0, K0, Bl, om)
    GA.check("vacuum pp-wave: Ric(k,k) = 0, omega.Z = 0, gradient 0", Rkk == 0 and oZ == 0 and gR == 0)
    GA.check("vacuum pp-wave: rate = -2 sigma_l:C = 32", rate == -2 * sC and rate == 32)
    # isotropic element in the same vacuum: theta_l only, rate 0
    r2 = run_case(pp(H), dict(base, U={(2, 0): F(1), (0, 2): F(1)}))[0]
    GA.check("vacuum pp-wave, isotropic element (theta_l only): rate 0", r2 == 0)
    # null dust H = x^2 - 5y^2 + 2xy: Ric(k,k) = 4; isotropic element theta_l = 4
    Hd = {(0, 0, 2, 0): F(1), (0, 0, 0, 2): F(-5), (0, 0, 1, 1): F(2)}
    rate, Bk, k, E, Rl, Bl, om = run_case(pp(Hd), dict(base, U={(2, 0): F(1), (0, 2): F(1)}))
    tR, sC, oZ, gR, dZ, Rkk = formula_terms(Rl, E0, K0, Bl, om)
    GA.check("null dust: Ric(k,k) = 4, theta_l = 4, rate = theta_l Ric(k,k) = 16",
             Rkk == 4 and Bl[0][0] + Bl[1][1] == 4 and rate == 16)
    # higher-order element data and normalisation do not enter (Z = 0 here)
    ref = run_case(pp(Hd), dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5)}))[0]
    alts = [dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5)}, V={(4, 0): F(3), (2, 2): F(1), (1, 3): F(-2)}),
            dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5)}, V={(3, 0): F(3), (1, 2): F(1)}),
            dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5), (3, 0): F(4), (1, 2): F(-7)}),
            dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5)}, X={(2, 0): F(3), (0, 3): F(1)}),
            dict(base, U={(2, 0): F(1), (1, 1): F(2), (0, 2): F(5)}, n={(1, 0): F(3), (0, 2): F(2), (1, 1): F(-1)})]
    GA.check("null dust: third/fourth-order element data and normalisation leave the rate 8 = 2 theta_l Ric - 2 B_l:R",
             all(run_case(pp(Hd), c)[0] == ref for c in alts) and ref == 8)


def check_flat_element_vacuum():
    setup_rate()
    # vacuum pp-wave H = x^3 - 3 x y^2 (harmonic), tilted null direction k = d_u + (1/2) d_v + d_x,
    # flat element spanned by e1 = d_u + (3/2) d_v + 2 d_x and e2 = d_y, k^u = 1
    met = with_base(pp({(0, 0, 3, 0): F(1), (0, 0, 1, 2): F(-3)}))
    k0 = [F(1), F(1, 2), F(1), F(0)]
    e1 = [F(1), F(3, 2), F(2), F(0)]
    e2 = [F(0), F(0), F(0), F(1)]
    l0 = [F(1, 2), F(9, 4), F(3, 2), F(0)]

    def ip(a, b):
        return -a[0] * b[1] - a[1] * b[0] + a[2] * b[2] + a[3] * b[3]
    GA.check("tilted frame at p: k, l null, k.l = -1, e orthonormal and orthogonal to k, l",
             ip(k0, k0) == 0 and ip(l0, l0) == 0 and ip(k0, l0) == -1 and ip(e1, e1) == 1 and ip(e2, e2) == 1
             and ip(e1, e2) == 0 and all(ip(v, w) == 0 for v in (e1, e2) for w in (k0, l0)))
    X0 = [S({(1, 0, 0): e1[m], (0, 1, 0): e2[m]}, N3, DD) for m in range(4)]
    rate, Bk, k, E = jm_rate(met, X0, k0, S.k(1, N3, DD), 0)
    Rl = riemann(met)
    rN = noether_rate(Rl, k, [e1, e2])
    om = [-ip(l0, [k[m].d(a).c0() for m in range(4)]) for a in range(2)]
    nulls = [[F(1), F(0), F(0), F(0)], k0, [F(1), F(1), F(1), F(1)], [F(2), F(25, 4), F(3), F(4)], [F(0), F(1), F(0), F(0)]]
    GA.check("vacuum: Ric(k,k) = 0 at p for five null k",
             all(ip(v, v) == 0 and Rv_ric(Rl, v) == 0 for v in nulls))
    gR = sum(Rv(Rl, [a, b, a, b], deriv=k0) for a in (e1, e2) for b in (e1, e2))
    GA.check("flat element: B_k = 0, omega = 0 at p", all(x == 0 for r in Bk for x in r) and om == [0, 0])
    GA.check("flat element in vacuum: JM rate = Noether rate = (nabla_k R)(e,e,e,e) = 6",
             rate == rN == gR == 6)


def Rv_ric(Rl, v):
    """Ric(v, v) = g^{ab} R(e_a, v, e_b, v) with g^{-1} at p (null form): -2 R(u,v,v,v)-type terms."""
    U, V, Xd, Yd = ([F(int(i == j)) for i in range(4)] for j in range(4))
    return (Rv(Rl, [Xd, v, Xd, v]) + Rv(Rl, [Yd, v, Yd, v]) - Rv(Rl, [U, v, V, v]) - Rv(Rl, [V, v, U, v]))


def check_null_data_force_constant_curvature():
    setup_rate()
    # Minkowski (-,+,+,+) diagonal; null vectors with rational components
    eta = [F(-1), F(1), F(1), F(1)]
    nulls = [[1, 1, 0, 0], [1, -1, 0, 0], [1, 0, 1, 0], [1, 0, -1, 0], [1, 0, 0, 1], [1, 0, 0, -1],
             [3, 2, 2, 1], [7, 2, 3, 6], [9, 4, 4, 7], [3, -1, 2, -2], [11, -2, 6, 9]]
    nulls = [[F(x) for x in v] for v in nulls]
    GA.check("sample vectors null", all(sum(eta[i] * v[i] * v[i] for i in range(4)) == 0 for v in nulls))
    # trace-free symmetric matrices (9-dim): S(k,k) = 0 for all sample null k forces S = 0
    basis = []
    for i in range(4):
        for j in range(i, 4):
            Sm = [[F(0)] * 4 for _ in range(4)]
            Sm[i][j] = Sm[j][i] = F(1)
            basis.append(Sm)
    # impose trace-free by projecting out the trace with eta
    tf = []
    for Sm in basis:
        tr = sum(eta[i] * Sm[i][i] for i in range(4))
        tf.append([[Sm[i][j] - tr * eta[i] * int(i == j) / 4 for j in range(4)] for i in range(4)])
    rows = [[sum(Sm[i][j] * v[i] * v[j] for i in range(4) for j in range(4)) for Sm in tf] for v in nulls]
    GA.check("Ric(k,k) = 0 for all null k forces trace-free Ricci = 0 (rank 9)", GA.field_rank(rows) == 9)
    # Weyl tensors: algebraic curvature tensors from Kulkarni-Nomizu products of symmetric matrices,
    # trace-free part; the map C -> trace-free C(e_a, k, e_b, k) on screens of the sample null k is injective
    def kn(A, B):
        return {(a, b, c, d): A[a][c] * B[b][d] + A[b][d] * B[a][c] - A[a][d] * B[b][c] - A[b][c] * B[a][d]
                for a, b, c, d in product(range(4), repeat=4)}
    sym = basis
    curv = []
    for i in range(len(sym)):
        for j in range(i, len(sym)):
            curv.append(kn(sym[i], sym[j]))
    def ricci(R):
        return [[sum(eta[q] * R[(q, a, q, b)] for q in range(4)) for b in range(4)] for a in range(4)]
    # linear space of curvature tensors as vectors; Weyl = kernel of the Ricci map
    keys = list(product(range(4), repeat=4))
    M = [[R[key] for key in keys] for R in curv]
    rk = GA.field_rank(M)
    GA.check("Kulkarni-Nomizu products span the 20-dim space of algebraic curvature tensors", rk == 20)
    ricrows = [[ricci(R)[a][b] for a in range(4) for b in range(4)] for R in curv]
    # kernel combination coefficients x with sum x_i ricci(curv_i) = 0
    Kmat = [[ricrows[i][m] for i in range(len(curv))] for m in range(16)]
    ker = GA.field_kernel(Kmat)
    weyl = [{key: sum(x[i] * curv[i][key] for i in range(len(curv))) for key in keys} for x in ker]
    GA.check("Weyl space has dimension 10", GA.field_rank([[W[key] for key in keys] for W in weyl]) == 10)
    def screen(v):
        # two vectors orthogonal to v and to its partner (reflected spatial part), from the spatial frame
        p = [v[0], -v[1], -v[2], -v[3]]
        cands = [[F(0), F(1), F(0), F(0)], [F(0), F(0), F(1), F(0)], [F(0), F(0), F(0), F(1)]]
        def ipm(a, b):
            return sum(eta[i] * a[i] * b[i] for i in range(4))
        out = []
        for c in cands:
            w = [c[i] - ipm(c, p) / ipm(v, p) * v[i] - ipm(c, v) / ipm(p, v) * p[i] for i in range(4)]
            if any(w):
                out.append(w)
        return out
    def comp(W, a, k, b):
        return sum(W[(i, j, m, n)] * a[i] * k[j] * b[m] * k[n] for i, j, m, n in keys if W[(i, j, m, n)] != 0)
    rows = []
    for W in weyl:
        row = []
        for v in nulls:
            sc = screen(v)
            for a in sc:
                for b in sc:
                    row.append(comp(W, a, v, b))
        rows.append(row)
    GA.check("C(e_a,k,e_b,k) = 0 for all null k forces C = 0 (rank 10)", GA.field_rank(rows) == 10)


def integrate_patch(poly):
    """int_{lam0}^{0} poly(lam) dlam as a polynomial in lam0 (coefficient lists, exact)."""
    anti = [F(0)] + [c / (i + 1) for i, c in enumerate(poly)]
    return [-c for c in anti]


def check_first_order_defect():
    setup_clausius()
    # per unit cross-section area, patch lam in [lam0, 0]; chi = -kappa lam k; pi kept formal:
    # every quantity below is the coefficient of 1/pi or of pi^0 as stated.
    out = []
    for Lam in (F(1, 3), F(3, 100), F(-2)):
        alpha = F(-3, 4) / Lam
        for rate, Rkk, Tkk in ((F(16), F(4), F(1, 2)), (F(-48), F(-2), F(-1, 4)), (F(6), F(0), F(0))):
            kappa, G = F(2), F(1)
            heat = integrate_patch([F(0), -kappa * Tkk])            # T(k,k) chi.k = kappa (-lam) T
            area = integrate_patch([F(0), -Rkk])                    # theta = -lam Ric(k,k)
            euler = integrate_patch([rate])                         # d(sqrt h R2)/dlam = rate at leading order
            # entropy change: area/4G + (alpha/2G) euler ; Clausius defect: heat - (kappa/2 pi) dS
            # lam0^1 coefficient (coefficient of 1/pi): -(kappa/2)(alpha/2G) euler_1
            GA.check("heat and area change start at lam0^2", heat[1] == 0 and area[1] == 0 and area[2] == Rkk / 2)
            d1 = -(kappa / 2) * (alpha / (2 * G)) * euler[1]
            GA.check("first-order Clausius defect (1/pi) kappa alpha rate/(4G) lam0: %s (Lambda %s)" % (d1, Lam),
                     d1 == kappa * alpha * rate / (4 * G) and ((d1 != 0) == (rate != 0)))
            out.append(d1)
    GA.check("defect values: -18, 54, -27/4; -200, 600, -75; 3, -9, 9/8",
             out == [F(-18), F(54), F(-27, 4), F(-200), F(600), F(-75), F(3), F(-9), F(9, 8)])
