"""synthesis.operator-join-ordering-constants: exact checks.

Palatial oscillators x = Z^a_i, y = bar Z_{i,a} with [x, y] = hbar. Two independent routes:
route 1 composes Weyl symbols by the Moyal product (exact on products of quadratics) and reads off
the hbar^1 and hbar^2 parts; route 2 realises bar Z = -hbar d/dZ on polynomials and applies the
operators to random test functions with hbar a number. Coefficients are Gaussian rationals.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is in Gaussian rationals)
from tp_premise import premise


class _Rng:
    """Deterministic integer generator (Lehmer, modulus 2^31 - 1) giving a fixed, reproducible list
    of rational test points; no floats and no random module."""

    def __init__(self, seed):
        self.s = seed % 2147483647 or 1

    def _next(self):
        self.s = (self.s * 48271) % 2147483647
        return self.s

    def randint(self, a, b):
        return a + self._next() % (b - a + 1)

    def randrange(self, n):
        return self._next() % n

class C:
    """Gaussian rational a + i b, i the chart's complex unit (I6)."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(s, o):
        o = cc(o); return C(s.re + o.re, s.im + o.im)
    __radd__ = __add__

    def __sub__(s, o):
        o = cc(o); return C(s.re - o.re, s.im - o.im)

    def __rsub__(s, o):
        return cc(o) - s

    def __neg__(s):
        return C(-s.re, -s.im)

    def __mul__(s, o):
        o = cc(o); return C(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = cc(o); n = o.re * o.re + o.im * o.im
        return s * C(o.re / n, -o.im / n)

    def conj(s):
        return C(s.re, -s.im)

    def abs2(s):
        return s.re * s.re + s.im * s.im

    def __eq__(s, o):
        o = cc(o); return s.re == o.re and s.im == o.im

    def __repr__(s):
        return f"({s.re}+{s.im}i)"


def cc(x):
    return x if isinstance(x, C) else C(x)


I = C(0, 1)
EPS = [[0, 1], [-1, 0]]          # eps_12 = 1: eps^T eps = 1, eps^2 = -1, det = 1


def rnd(rng, k=3):
    return C(F(rng.randint(-k, k), rng.randint(1, 3)), F(rng.randint(-k, k), rng.randint(1, 3)))




def herm(Z, W):
    return sum((Z[2 + a].conj() * W[a] + Z[a].conj() * W[2 + a] for a in range(2)), C())

def matvec(A, Z):
    return [sum((cc(A[r][c]) * Z[c] for c in range(4)), C()) for r in range(4)]


def _unused_moment(A, Zs):
    """M_A = i sum_i bar Z^i . A Z^i."""
    return I * sum((herm(Z, matvec(A, Z)) for Z in Zs), C())


def A_grading():          # A(n_inf ^ n_0)
    h = F(1, 2)
    return [[-h, 0, 0, 0], [0, -h, 0, 0], [0, 0, h, 0], [0, 0, 0, h]]


def A_trans(x):           # A(x ^ n_inf): omega-block <- b_x pi, (b_x pi)^a = x^{aa'} eps_{a'b'} pi^{b'}
    A = [[0] * 4 for _ in range(4)]
    for a in range(2):
        for bp in range(2):
            A[a][2 + bp] = sum(x[a][ap] * EPS[ap][bp] for ap in range(2))
    return A


def A_spec(x):            # A(x ^ n_0): pi-block <- c_x omega, (c_x w)^{a'} = -x^{ba'} eps_{ba} w^a
    A = [[0] * 4 for _ in range(4)]
    for ap in range(2):
        for a in range(2):
            A[2 + ap][a] = -sum(x[b][ap] * EPS[b][a] for b in range(2))
    return A


def unit_x(a, ap):
    x = [[0, 0], [0, 0]]
    x[a][ap] = 1
    return x


# ambient basis: n_inf, n_0, E_{aa'} (a, a' in 0..1 standing for 1,2 and 3,4)
XS = [(a, ap) for a in range(2) for ap in range(2)]


def gram():
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][1] = G[1][0] = F(1)
    for r, (a, ap) in enumerate(XS):
        for s, (b, bp) in enumerate(XS):
            G[2 + r][2 + s] = F(-EPS[a][b] * EPS[ap][bp])
    return G


def inverse(G):
    n = len(G)
    M = [[cc(G[r][c]) for c in range(n)] + [C(1 if r == c else 0) for c in range(n)] for r in range(n)]
    for col in range(n):
        piv = next(r for r in range(col, n) if not (M[r][col] == 0))
        M[col], M[piv] = M[piv], M[col]
        p = M[col][col]
        M[col] = [v / p for v in M[col]]
        for r in range(n):
            if r != col and not (M[r][col] == 0):
                f = M[r][col]
                M[r] = [M[r][c] - f * M[col][c] for c in range(2 * n)]
    return [row[n:] for row in M]


GI = inverse(gram())



# ---- polynomials: dict {exponent tuple: C}


def padd(*ps):
    out = {}
    for p in ps:
        for m, c in p.items():
            out[m] = out.get(m, C()) + c
    return {m: c for m, c in out.items() if not (c == 0)}


def pscale(p, s):
    s = cc(s)
    return {m: c * s for m, c in p.items() if not (c * s == 0)}


def pmul(p, q):
    out = {}
    for m1, c1 in p.items():
        for m2, c2 in q.items():
            m = tuple(a + b for a, b in zip(m1, m2))
            out[m] = out.get(m, C()) + c1 * c2
    return {m: c for m, c in out.items() if not (c == 0)}


def pdiff(p, v):
    out = {}
    for m, c in p.items():
        if m[v]:
            mm_ = list(m); mm_[v] -= 1
            out[tuple(mm_)] = out.get(tuple(mm_), C()) + c * m[v]
    return {m: c for m, c in out.items() if not (c == 0)}


class Space:
    def __init__(self, N):
        self.N = N
        self.nv = 8 * N          # x_{i,a} at 8i+a, y_{i,a} at 8i+4+a

    def x(self, i, a):
        return 8 * i + a

    def y(self, i, a):
        return 8 * i + 4 + a

    def var(self, v):
        m = [0] * self.nv; m[v] = 1
        return {tuple(m): C(1)}

    def const(self, c):
        return {tuple([0] * self.nv): cc(c)} if not (cc(c) == 0) else {}

    def pairs(self):
        return [(self.x(i, a), self.y(i, a)) for i in range(self.N) for a in range(4)]

    def P(self, f, g):
        out = {}
        for (xv, yv) in self.pairs():
            out = padd(out, pmul(pdiff(f, xv), pdiff(g, yv)), pscale(pmul(pdiff(f, yv), pdiff(g, xv)), -1))
        return out

    def P2(self, f, g):
        out = {}
        for (xk, yk) in self.pairs():
            for (xl, yl) in self.pairs():
                fx = pdiff(f, xk); fy = pdiff(f, yk)
                gx = pdiff(g, xk); gy = pdiff(g, yk)
                out = padd(out,
                           pmul(pdiff(fx, xl), pdiff(gy, yl)),
                           pscale(pmul(pdiff(fx, yl), pdiff(gy, xl)), -1),
                           pscale(pmul(pdiff(fy, xl), pdiff(gx, yl)), -1),
                           pmul(pdiff(fy, yl), pdiff(gx, xl)))
        return out

    def star(self, f, g):
        """Moyal product of two polynomials of degree <= 2, as (hbar^0, hbar^1, hbar^2) parts."""
        return (pmul(f, g), pscale(self.P(f, g), F(1, 2)), pscale(self.P2(f, g), F(1, 8)))


def tri_add(*ts):
    return tuple(padd(*[t[k] for t in ts]) for k in range(3))


def tri_scale(t, s):
    return tuple(pscale(p, s) for p in t)


S_SWAP = [2, 3, 0, 1]     # S exchanges the halves: (S v)_a = v_{S_SWAP[a]}


def moment(sp, A):
    """M_A = i sum_i bar Z_i . A Z^i = i sum_i y_{i,b} A^b_a x_{i,a} (y = bar Z as a dual vector).
    Here bar Z . W = conj(Z)^T S W, so y_b = sum_a conj(Z)_a S_ab and bar Z . A Z = y . (A x)."""
    out = {}
    for i in range(sp.N):
        for b in range(4):
            for a in range(4):
                if A[b][a]:
                    out = padd(out, pscale(pmul(sp.var(sp.y(i, b)), sp.var(sp.x(i, a))), I * cc(A[b][a])))
    return out


def omega_mat(lam):
    O = [[F(0)] * 4 for _ in range(4)]
    for a in range(2):
        for b in range(2):
            O[a][b] = lam * EPS[a][b]
            O[2 + a][2 + b] = F(EPS[a][b])
    return O


def Bpoly(sp, i, l, lam):
    O = omega_mat(lam)
    out = {}
    for a in range(4):
        for b in range(4):
            if O[a][b]:
                out = padd(out, pscale(pmul(sp.var(sp.x(i, a)), sp.var(sp.x(l, b))), O[a][b]))
    return out


def Bbar_poly(sp, i, l, lam):
    """conj(B) = conj(x_i)^T O conj(x_l), conj(x) = S y (S real, symmetric, S^2 = 1)."""
    O = omega_mat(lam)
    out = {}
    for a in range(4):
        for b in range(4):
            if O[a][b]:
                out = padd(out, pscale(pmul(sp.var(sp.y(i, S_SWAP[a])), sp.var(sp.y(l, S_SWAP[b]))), O[a][b]))
    return out


def hpoly(sp, i, l):
    """h_il = bar Z^i . Z^l = y_i . x_l."""
    out = {}
    for a in range(4):
        out = padd(out, pmul(sp.var(sp.y(i, a)), sp.var(sp.x(l, a))))
    return out


def grip_values(sp, lam):
    d = moment(sp, A_grading())
    v = [pscale(d, lam), pscale(d, -1)]
    for (a, ap) in XS:
        x = unit_x(a, ap)
        v.append(padd(moment(sp, A_trans(x)), pscale(moment(sp, A_spec(x)), lam)))
    return v


def run(N, lam):
    sp = Space(N)
    v = grip_values(sp, lam)
    lhs = ({}, {}, {})
    cl = {}
    for r in range(6):
        for s in range(6):
            if not (GI[r][s] == 0):
                lhs = tri_add(lhs, tri_scale(sp.star(v[r], v[s]), GI[r][s]))
                cl = padd(cl, pscale(pmul(v[r], v[s]), GI[r][s]))
    # RHS in symmetric (palatial) ordering
    rhs = ({}, {}, {})
    rcl = {}
    for i in range(N):
        for l in range(i + 1, N):
            Bp, Bb = Bpoly(sp, i, l, lam), Bbar_poly(sp, i, l, lam)
            rhs = tri_add(rhs, sp.star(Bb, Bp), sp.star(Bp, Bb))          # (B^dag B + B B^dag)
            rcl = padd(rcl, pscale(pmul(Bb, Bp), 2))
    H = [[hpoly(sp, i, l) for l in range(N)] for i in range(N)]
    trh = padd(*[H[i][i] for i in range(N)])
    for i in range(N):
        for l in range(N):
            rhs = tri_add(rhs, tri_scale(sp.star(H[i][l], H[l][i]), lam))   # 2 lam (1/2) tr h^2
            rcl = padd(rcl, pscale(pmul(H[i][l], H[l][i]), lam))
    rhs = tri_add(rhs, tri_scale(sp.star(trh, trh), -lam / 2))             # 2 lam (-1/4)(tr h)^2
    rcl = padd(rcl, pscale(pmul(trh, trh), -lam / 2))
    assert padd(cl, pscale(rcl, -1)) == {}, "classical identity fails"
    assert lhs[0] == cl
    diff = [padd(lhs[k], pscale(rhs[k], -1)) for k in range(3)]
    return sp, lhs, rhs, diff, H, trh



def mono(nv, k):
    m = [0]*nv; m[k] = 1; return tuple(m)

class Rep:
    def __init__(self, N, hb):
        self.N, self.nv, self.hb = N, 4*N, F(hb)
    def X(self, k):            # multiplication by x_k
        return lambda f: pmul({mono(self.nv, k): C(1)}, f)
    def Y(self, k):            # -hbar d/dx_k
        return lambda f: pscale(pdiff(f, k), -self.hb)
    def ix(self, i, a): return 4*i + a

def comp(*ops):
    def g(f):
        for op in reversed(ops):
            f = op(f)
        return f
    return g

def lin(terms):
    """terms: list of (coef, op)"""
    return lambda f: padd(*[pscale(op(f), c) for c, op in terms]) if terms else {}

def sym2(R, yk, xk):
    """Weyl quantisation of the classical product y_k x_k' : 1/2 (Y X + X Y)."""
    return lin([(F(1,2), comp(R.Y(yk), R.X(xk))), (F(1,2), comp(R.X(xk), R.Y(yk)))])

def moment_op(R, A):
    terms = []
    for i in range(R.N):
        for b in range(4):
            for a in range(4):
                if A[b][a]:
                    terms.append((I*cc(A[b][a]), sym2(R, R.ix(i,b), R.ix(i,a))))
    return lin(terms)

def grip_sq(R, lam):
    d = moment_op(R, A_grading())
    v = [lin([(lam, d)]), lin([(-1, d)])]
    for (a, ap) in XS:
        x = unit_x(a, ap)
        v.append(lin([(1, moment_op(R, A_trans(x))), (lam, moment_op(R, A_spec(x)))]))
    terms = []
    for r in range(6):
        for s in range(6):
            if not (GI[r][s] == 0):
                terms.append((GI[r][s], comp(v[r], v[s])))
    return lin(terms)

def rhs_op(R, lam):
    O = omega_mat(lam)
    terms = []
    N = R.N
    for i in range(N):
        for l in range(i+1, N):
            Bt, Bbt = [], []
            for a in range(4):
                for b in range(4):
                    if O[a][b]:
                        Bt.append((O[a][b], comp(R.X(R.ix(i,a)), R.X(R.ix(l,b)))))
                        Bbt.append((O[a][b], comp(R.Y(R.ix(i,S_SWAP[a])), R.Y(R.ix(l,S_SWAP[b])))))
            Bo, Bbo = lin(Bt), lin(Bbt)
            terms += [(1, comp(Bbo, Bo)), (1, comp(Bo, Bbo))]
    H = [[lin([(1, sym2(R, R.ix(i,a), R.ix(l,a))) for a in range(4)]) for l in range(N)] for i in range(N)]
    trh = lin([(1, H[i][i]) for i in range(N)])
    for i in range(N):
        for l in range(N):
            terms.append((lam, comp(H[i][l], H[l][i])))
    terms.append((-lam/2, comp(trh, trh)))
    return lin(terms), trh



def check_operator_join():
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    premise("correspondence.shared-core-ordering-dictionary")
    premise("mass.chart-form-spin-isomorphism")
    premise("mass.imported-flat-model-twistor-chart-infinity")
    premise("mass.de-sitter-scale-frozen-point")
    premise("mass.exact-join")
    rng = _Rng(11)
    # (1) every grip generator A(U ^ I) is traceless, so its symmetrised quadratic has no shift
    for lam in (F(1), F(-2, 3)):
        mats = [A_grading()] + [A_trans(unit_x(a, ap)) for (a, ap) in XS] + [A_spec(unit_x(a, ap)) for (a, ap) in XS]
        for A in mats:
            assert sum(F(A[k][k]) for k in range(4)) == 0
    # (2) the key matrix: sum_{U,V} G^{UV} A(U^I) A(V^I) = -(5/4) <I,I> 1 = -(5/2) lam 1
    for lam in (F(1), F(1, 6), F(-2, 3)):
        As = [[[cc(v) * lam for v in row] for row in A_grading()],
              [[cc(v) * -1 for v in row] for row in A_grading()]]
        for (a, ap) in XS:
            T, K = A_trans(unit_x(a, ap)), A_spec(unit_x(a, ap))
            As.append([[cc(T[r][c]) + cc(K[r][c]) * lam for c in range(4)] for r in range(4)])
        tot = [[C() for _ in range(4)] for _ in range(4)]
        for r in range(6):
            for s in range(6):
                if not (GI[r][s] == 0):
                    prod = [[sum((As[r][p][q] * As[s][q][t] for q in range(4)), C()) for t in range(4)] for p in range(4)]
                    tot = [[tot[p][t] + GI[r][s] * prod[p][t] for t in range(4)] for p in range(4)]
        assert tot == [[C(-F(5, 2) * lam if p == t else 0) for t in range(4)] for p in range(4)]
    # (3) route 1 (Moyal product of Weyl symbols, exact for products of quadratics), N = 2, 3:
    # the operator grip minus the symmetrised right side is the central constant -2 N lam hbar^2,
    # with no hbar^1 part; the classical parts agree (run() asserts the polynomial identity)
    def lap(sp, p):
        out = {}
        for (xv, yv) in sp.pairs():
            out = padd(out, pdiff(pdiff(p, xv), yv))
        return out
    for N in (2, 3):
        for lam in (F(1), F(-2, 3)):
            sp, lhs, rhs, diff, H, trh = run(N, lam)
            zero = tuple([0] * sp.nv)
            assert diff[0] == {} and diff[1] == {}
            assert diff[2] == {zero: C(-2 * N * lam)}
            # normal (Z-left) form: N-symbol = exp(-(hbar/2) Delta) W-symbol; Delta m^2 = 5 lam tr h and
            # (1/8) Delta^2 m^2 cancels the Weyl constant -(5N/2) lam: m^2_op = :m^2: - (5/2) lam hbar :tr h:
            # the Weyl-relative constant: m^2_op = W(m^2) - (5N/2) lam hbar^2 = W(m^2) - (5 N Lambda/12) hbar^2,
            # while relative to the Jordan-symmetrised RHS it is -2N lam hbar^2 = -(N Lambda/3) hbar^2 (asserted above)
            assert lhs[1] == {} and lhs[2] == {zero: C(-F(5 * N, 2) * lam)}
            L1 = lap(sp, lhs[0])
            assert L1 == pscale(trh, 5 * lam)
            assert lap(sp, L1) == {zero: C(20 * N * lam)}
            # the commutator [B, Bbar] = hbar lam (h_ii + h_ll) (symmetrised Gram operators)
            Bp, Bb = Bpoly(sp, 0, 1, lam), Bbar_poly(sp, 0, 1, lam)
            assert sp.P(Bp, Bb) == pscale(padd(H[0][0], H[1][1]), lam)
    # (4) route 2 (holomorphic realisation Zbar = -hbar d/dZ, no Moyal product), N = 2, hbar = 1, 3:
    # the palatial form and the normal form on random polynomial test functions
    def normal_op(R, poly):
        def g(f):
            out = {}
            for m, c in poly.items():
                h = f
                for i in range(R.N):
                    for a in range(4):
                        for _ in range(m[8 * i + 4 + a]):
                            h = R.Y(R.ix(i, a))(h)
                for i in range(R.N):
                    for a in range(4):
                        for _ in range(m[8 * i + a]):
                            h = R.X(R.ix(i, a))(h)
                out = padd(out, pscale(h, c))
            return out
        return g

    def randpoly(nv, deg):
        f = {}
        for _ in range(5):
            m = [0] * nv
            for _ in range(rng.randint(0, deg)):
                m[rng.randrange(nv)] += 1
            f[tuple(m)] = f.get(tuple(m), C()) + C(rng.randint(-3, 3), rng.randint(-3, 3))
        return {k: v for k, v in f.items() if not (v == 0)}
    N = 2
    for lam in (F(1), F(-2, 3)):
        sp, lhs, rhs, diff, H, trh_poly = run(N, lam)
        for hb in (1, 3):
            R = Rep(N, hb)
            G = grip_sq(R, lam)
            Rh, trh = rhs_op(R, lam)
            nm, ntr = normal_op(R, lhs[0]), normal_op(R, trh_poly)
            for _ in range(2):
                f = randpoly(R.nv, 3)
                Gf = G(f)
                assert padd(Gf, pscale(Rh(f), -1), pscale(f, 2 * N * lam * R.hb ** 2)) == {}
                assert padd(Gf, pscale(nm(f), -1), pscale(ntr(f), F(5, 2) * lam * R.hb)) == {}
            # palatial helicity: the symmetrised h_ii acts on homogeneity d as -(d + 2) hbar
            d = 3
            f = {tuple([d] + [0] * (R.nv - 1)): C(1)}
            assert lin([(1, sym2(R, R.ix(0, a), R.ix(0, a))) for a in range(4)])(f) == pscale(f, -(d + 2) * R.hb)
    # Lambda = 0: no ordering terms at all
    sp, lhs, rhs, diff, H, trh = run(2, F(0))
    assert diff == [{}, {}, {}] and lhs[1] == {} and lhs[2] == {}
    return True
