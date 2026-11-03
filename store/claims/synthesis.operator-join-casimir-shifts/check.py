"""synthesis.operator-join-casimir-shifts: exact checks.

Single conformal spinor (N = 1), palatial oscillators in the holomorphic realisation
bar Z = -hbar d/dZ on polynomials in Z^1..Z^4 (homogeneity d), as in the store's operator-join
check, whose grip construction (chart matrices A(U ^ I_Lambda), inverse ambient Gram matrix) is
reproduced verbatim below. The conformal Casimir is sum_ab E_ab E_ba - (1/4)(tr E)^2 with
E_ab the symmetrised quadratic of Z^a bar Z_b, the operator form of C_2(Lambda^2 CS) =
tr(h^2) - (1/4)(tr h)^2.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is in Gaussian rationals)
from tp_premise import premise


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





def monomials(nv, d):
    if nv == 1:
        return [(d,)]
    return [(k,) + m for k in range(d + 1) for m in monomials(nv - 1, d - k)]


def conf_casimir(R):
    E = [[sym2(R, R.ix(0, b), R.ix(0, a)) for b in range(4)] for a in range(4)]   # E_ab ~ Z^a bar Z_b
    trE = lin([(1, E[a][a]) for a in range(4)])
    terms = [(1, comp(E[a][b], E[b][a])) for a in range(4) for b in range(4)]
    terms.append((F(-1, 4), comp(trE, trE)))
    return lin(terms), trE


def check_operator_join_casimir_shifts():
    premise("synthesis.operator-join-ordering-constants")
    premise("mass.casimir-form-join")
    premise("mass.imported-palatial-quadratics-homogeneity-charge")
    premise("mass.imported-unitary-representations-de-sitter-group")
    premise("mass.mass-weight-dictionary")
    premise("mass.weight-polynomial-two-series")
    premise("field-theory.imported-standard-field-theory")
    premise("mass.de-sitter-scale-frozen-point")
    premise("mass.chart-form-spin-isomorphism")
    # Weyl-algebra identities by the Moyal product (exact on products of quadratics), N = 1:
    # m^2_op = (lam/2) h*h - 2 lam hbar^2 and C_conf = (3/4) h*h - 3 hbar^2, h the helicity symbol
    for lam in (F(1), F(-2, 3), F(0)):
        sp = Space(1)
        v = grip_values(sp, lam)
        lhs = ({}, {}, {})
        for r in range(6):
            for s in range(6):
                if not (GI[r][s] == 0):
                    lhs = tri_add(lhs, tri_scale(sp.star(v[r], v[s]), GI[r][s]))
        hs = hpoly(sp, 0, 0)
        hh = sp.star(hs, hs)
        zero = tuple([0] * sp.nv)
        assert lhs[0] == pscale(hh[0], lam / 2) and lhs[1] == {} and hh[1] == {}
        assert lhs[2] == padd(pscale(hh[2], lam / 2), {zero: C(-2 * lam)} if lam else {})
        e = [[pmul(sp.var(sp.x(0, a)), sp.var(sp.y(0, b))) for b in range(4)] for a in range(4)]
        cas = ({}, {}, {})
        for a in range(4):
            for b in range(4):
                cas = tri_add(cas, sp.star(e[a][b], e[b][a]))
        cas = tri_add(cas, tri_scale(sp.star(hs, hs), F(-1, 4)))
        assert cas[0] == pscale(hh[0], F(3, 4)) and cas[1] == {}
        assert cas[2] == padd(pscale(hh[2], F(3, 4)), {zero: C(-3)})
    for lam in (F(1), F(-2, 3)):
        for hb in (1, 3):
            R = Rep(1, hb)
            G = grip_sq(R, lam)
            Cc, h = conf_casimir(R)
            for d in range(4):
                for m in monomials(4, d):
                    f = {m: C(1)}
                    # helicity: h acts as -(d + 2) hbar (imported), so h^2 - 4 hbar^2 = d (d + 4) hbar^2
                    assert h(f) == pscale(f, -(d + 2) * R.hb)
                    q = d * (d + 4) * R.hb ** 2
                    assert G(f) == pscale(f, lam * q / 2)            # m^2_op = (lam/2)(h^2 - 4 hbar^2)
                    assert Cc(f) == pscale(f, F(3, 4) * q)           # C_conf = (3/4)(h^2 - 4 hbar^2)
                    # de Sitter Casimir from the split C_dS = C_conf - m^2/<I,I>, <I,I> = 2 lam
                    cds = F(3, 4) * q - (lam * q / 2) / (2 * lam)
                    assert cds == F(1, 2) * q
            # operator identities on a mixed-degree test function (Weyl-algebra identities)
            f = {(2, 0, 1, 0): C(1, 2), (0, 1, 0, 0): C(-3), (1, 1, 1, 1): C(0, 1), (0, 0, 0, 0): C(5)}
            hh = comp(h, h)
            assert G(f) == padd(pscale(hh(f), lam / 2), pscale(f, -2 * lam * R.hb ** 2))
            assert Cc(f) == padd(pscale(hh(f), F(3, 4)), pscale(f, -3 * R.hb ** 2))
    # helicity values: on homogeneity n the palatial helicity is -(n + 2) hbar = 2 s hbar, so with
    # q = h^2 - 4 hbar^2 = 4 (s^2 - 1) hbar^2: C_conf = 3 (s^2 - 1), C_dS = 2 (s^2 - 1), m^2 = 2 lam (s^2 - 1)
    for s2 in (F(0), F(1, 4), F(1), F(4)):           # s^2 for s = 0, 1/2, 1, 2
        q = 4 * (s2 - 1)
        assert F(3, 4) * q == 3 * (s2 - 1) and F(1, 2) * q == 2 * (s2 - 1)
    # the scalar module (n = -2, s = 0): C_dS = -2, the scalar-module Casimir -m^2/H^2 of m^2 = 2 H^2,
    # i.e. Delta (3 - Delta) = 2 at Delta = 1, 2, and the weight dictionary -w (w + 3) = 2 at w = -1
    s2 = F(0)
    cds = 2 * (s2 - 1)
    m2_field = -cds
    assert m2_field == 2 and [D for D in range(4) if D * (3 - D) == m2_field] == [1, 2]
    assert -(-1) * (-1 + 3) == m2_field
    m2_grip = 2 * F(1, 2) * (s2 - 1) * 1                 # 2 lam (s^2 - 1) at lam = H^2 / 2, H = 1
    cconf = 3 * (s2 - 1)
    assert m2_grip == -1 and m2_field - m2_grip == -cconf == 3
    # classical values (no ordering): C_conf = 3 s^2, C_dS = 2 s^2, m^2 = 2 lam s^2: at s = 0 all vanish,
    # so the classical dS Casimir gives m^2 = 0, not the conformally coupled 2 H^2
    assert 2 * s2 == 0
    return True
