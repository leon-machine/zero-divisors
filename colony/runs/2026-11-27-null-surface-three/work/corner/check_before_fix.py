"""Corner charge of the boost on a null-plane pair: exact checks.

Conventions of the first-order result (Cl(1,3), signature (+,-,-,-)): a symmetric map is held as a matrix H
with h(a) = sum H[m][k] (a.e_m) e_k; the stored first-order curvature is R_p[h](B) = -1/2 p ^ h(B.p), with
Einstein map G_p; omega is the symbol of the symplectic current of that result, clause (i), copied from its
check. Null vectors n = e_0 + e_3, nbar = e_0 - e_3, corner = the plane of e_1, e_2 through the origin,
B = e_0 e_3 the unit bivector of the n ^ nbar plane (B^2 = +1), boost field xi_B(x) = x.B = z e_0 + t e_3, the
velocity of x -> R x R~ with R = exp(-chi B/2). Null plane N = {n.x = 0} = {t = z = lam}, its future half
N+ = {lam >= 0}; Nbar = {nbar.x = 0} = {t = -z = mu}.

Two layers. Symbols: a constant-coefficient bilinear differential identity holds for all fields exactly when
its symbol identity holds for all vectors; the identity of clause (i) is homogeneous of degree two in the pair
of momenta and linear in each field, so it is verified completely on a basis. Polynomials: fields with
polynomial coefficients (gtg.Jet of infinite order, an exact polynomial ring over the rationals), with exact
derivatives, restriction to the null planes and exact integration over a finite window.

(i)    omega(h, Delta_xi) = 2 E[h](xi) + div Psi_xi[h] for every field h and every vector field xi (the
       potential Psi is held in the variables named K below);
(ii)   B.Psi at the corner is minus the transverse trace, in every gauge; behaviour under displacements;
(iii)  the area density of the corner from hb, to first order and on a field that is not weak;
(iv)   for a vacuum field in a generic gauge the flux through N+ of omega(h, Delta_xi), xi the boost near the
       corner cut off away from it, is exactly minus the weighted transverse trace on the corner, and
       through Nbar+ plus it;
(v)    the exact boost: the conservation law on N and on Nbar, the first law on a window by two routes;
(vi)   (a) the flux of omega(h, L_B h) in the gauge h(n) = 0; (b) the focusing equation in area form (in the
       function for (iii)); (c) has no check of its own: it is the combination of (a) and (b);
(vii)  the dual of the boost plane is the corner plane; the periods; 2 pi times the boost energy of a source
       on a window against the area change over 4 G.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sub
from tp_premise import premise
import gtg

R1 = "synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators"
TWO = "synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints"
DUAL = "synthesis.modular-period-on-values-is-the-dual-plane-turn"
MODULAR = "synthesis.imported-null-plane-modular-hamiltonian-first-law"

D = 4
S = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
REC = [scal(ETA[i], E[i]) for i in range(D)]


# ---------------------------------------------------------------------------------------------------------
# symbols (helpers of the first-order result's check, copied; apply and tr_map read components directly)
# ---------------------------------------------------------------------------------------------------------

def vec(c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def dot(a, b):
    return GA.dot(a, b, S)


def g1(x):
    return {b: c for b, c in x.items() if len(b) == 1}


def wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, S), mul(b, a, S)))


def vdotB(a, B):
    return g1(scal(F(1, 2), sub(mul(a, B, S), mul(B, a, S))))


def upper(v):
    return [F(ETA[i]) * dot(v, E[i]) for i in range(D)]


def apply(H, a):
    """h(a); a.e_m is read off the components of the vector a (compared with the product in the first check)."""
    out = {}
    for m in range(D):
        am = ETA[m] * a.get((m,), 0)
        if am == 0:
            continue
        for k in range(D):
            if H[m][k]:
                out = add(out, scal(am * H[m][k], E[k]))
    return out


def riem(H, p, B):
    return scal(F(-1, 2), wedge(p, apply(H, GA.neg(vdotB(p, B)))))


def trace(M):
    return sum(ETA[a] * M[a][a] for a in range(D))


def einstein(H, p):
    R = [[F(0)] * D for _ in range(D)]
    for m in range(D):
        img = {}
        for b in range(D):
            img = add(img, vdotB(REC[b], riem(H, p, wedge(E[b], REC[m]))))
        for k in range(D):
            R[m][k] = dot(img, REC[k])
    t = trace(R)
    return [[R[m][k] - (F(1, 2) * t * ETA[m] if m == k else 0) for k in range(D)] for m in range(D)]


def pair(A, B):
    return sum(ETA[a] * ETA[k] * A[a][k] * B[a][k] for a in range(D) for k in range(D))


def tr_map(H):
    """the trace sum_a e^a . h(e_a) of the map, which for the matrix convention above is sum_a eta_a H[a][a]
    (compared with the product form in the first check)."""
    return trace(H)


def tr_by_product(H):
    return sum(dot(REC[a], apply(H, E[a])) for a in range(D))


def outer(x, y):
    """the symmetric map a -> (a.x) y + (a.y) x."""
    xu, yu = upper(x), upper(y)
    return [[xu[m] * yu[k] + yu[m] * xu[k] for k in range(D)] for m in range(D)]


def madd(A, B, c=1):
    return [[A[m][k] + c * B[m][k] for k in range(D)] for m in range(D)]


def mscal(c, A):
    return [[c * x for x in row] for row in A]


ZERO = [[F(0)] * D for _ in range(D)]
N = vec([1, 0, 0, 1])
NBAR = vec([1, 0, 0, -1])
M1 = vec([0, 1, 0, 0])
M2 = vec([0, 0, 1, 0])
NPLUS = mscal(F(1, 2), madd(outer(M1, M1), outer(M2, M2), -1))      # a -> (a.m1) m1 - (a.m2) m2
NCROSS = outer(M1, M2)                                              # a -> (a.m1) m2 + (a.m2) m1
GAUGE_BASIS = [outer(N, N), outer(N, M1), outer(N, M2), outer(M1, M1), outer(M1, M2), outer(M2, M2)]
SYM = [[3, -1, 2, 5, 4, -2, 1, -3, 2, 1], [-2, 4, 1, -1, 3, 2, -5, 1, 4, -3],
       [1, 2, -3, 4, -1, 5, 2, -2, 3, 1], [5, -3, 1, 2, -4, 1, 3, 2, -1, 4]]
VECS = [(2, 1, -1, 3), (1, -2, 3, 4), (3, 2, 1, -1), (-1, 4, 2, 1), (4, -1, -3, 1)]


def sym(c):
    H = [[F(0)] * D for _ in range(D)]
    i = 0
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = F(c[i])
            i += 1
    return H


def sym_units():
    out = []
    for m in range(D):
        for k in range(m, D):
            H = [[F(0)] * D for _ in range(D)]
            H[m][k] = F(1)
            H[k][m] = F(1)
            out.append(H)
    return out


def omega(H1, p1, H2, p2):
    """symbol of the symplectic current: derivatives of the first field -> p1, of the second -> p2."""
    t1, t2 = tr_map(H1), tr_map(H2)
    w = scal(F(1, 2) * pair(H1, H2), sub(p1, p2))
    w = add(w, scal(F(1, 2), sub(scal(t1, apply(H2, p1)), scal(t2, apply(H1, p2)))))
    w = add(w, scal(F(1, 2), sub(scal(t2, apply(H1, p1)), scal(t1, apply(H2, p2)))))
    w = add(w, sub(apply(H1, apply(H2, p2)), apply(H2, apply(H1, p1))))
    w = add(w, scal(F(-1, 2) * t1 * t2, sub(p1, p2)))
    return w


def potential_symbol(H, p, xi, q, coef):
    """symbol of K_xi[h] = c0 xi ^ (d - grad tau) + c1 grad ^ h(xi) [on h] + c2 grad ^ h(xi) [on xi]
    + c3 tau grad ^ xi; derivatives of h -> p, of xi -> q."""
    hx = apply(H, xi)
    K = scal(coef[0], wedge(xi, sub(apply(H, p), scal(tr_map(H), p))))
    K = add(K, scal(coef[1], wedge(p, hx)))
    K = add(K, scal(coef[2], wedge(q, hx)))
    return add(K, scal(coef[3] * tr_map(H), wedge(q, xi)))


def quadratic_points():
    """36 points of the eight-dimensional space of pairs (p, q) on which a homogeneous quadratic polynomial
    is determined: the unit points and the sums of two of them."""
    units = [tuple(1 if i == j else 0 for i in range(2 * D)) for j in range(2 * D)]
    pts = list(units)
    for i in range(2 * D):
        for j in range(i + 1, 2 * D):
            pts.append(tuple(a + b for a, b in zip(units[i], units[j])))
    return [(c[:D], c[D:]) for c in pts]


# ---------------------------------------------------------------------------------------------------------
# polynomial fields: gtg.Jet of infinite order is an exact polynomial in the labels t, x, y, z
# ---------------------------------------------------------------------------------------------------------

J = gtg.Jet
X = [J.var(i, 0, D, None) for i in range(D)]
ZJ = J.const(0, D)
ONE = J.const(1, D)
NU = [ONE, ZJ, ZJ, ONE]                    # n, upper components
NBU = [ONE, ZJ, ZJ, ONE * (-1)]            # nbar
XIB = [X[3], ZJ, ZJ, X[0]]                 # the boost field x.B = z e_0 + t e_3, B = e_0 e_3


def jsum(terms):
    out = ZJ
    for x in terms:
        out = out + x
    return out


def pzeros():
    return [[ZJ for _ in range(D)] for _ in range(D)]


def padd(A, B, c=1):
    return [[A[m][k] + B[m][k] * c for k in range(D)] for m in range(D)]


def pconst(M, f):
    """the field f(x) M for a constant map M and a polynomial f."""
    return [[f * M[m][k] for k in range(D)] for m in range(D)]


def ptrace(H):
    return jsum(H[a][a] * ETA[a] for a in range(D))


def ppair(A, B):
    return jsum(A[a][k] * B[a][k] * (ETA[a] * ETA[k]) for a in range(D) for k in range(D))


def papply(H, v):
    return [jsum(H[m][k] * v[m] * ETA[m] for m in range(D)) for k in range(D)]


def grad(f):
    return [f.d(mu) * ETA[mu] for mu in range(D)]


def pdiv(H):
    """d = h(grad), the derivative on h."""
    return [jsum(H[mu][k].d(mu) for mu in range(D)) for k in range(D)]


def vdiv(v):
    return jsum(v[mu].d(mu) for mu in range(D))


def vadd(u, v, c=1):
    return [u[k] + v[k] * c for k in range(D)]


def vscal(c, u):
    return [u[k] * c for k in range(D)]


def vdot(u, v):
    return jsum(u[k] * v[k] * ETA[k] for k in range(D))


def vzero(v):
    return all(not bool(c) for c in v)


def pzero(H):
    return all(not bool(c) for row in H for c in row)


def pomega(H1, H2):
    """the symplectic current of the first-order result, clause (i), on polynomial fields."""
    t1, t2 = ptrace(H1), ptrace(H2)
    d1, d2 = pdiv(H1), pdiv(H2)
    a1, a2 = grad(t1), grad(t2)
    w = []
    for mu in range(D):
        acc = jsum((H1[m][k].d(mu) * H2[m][k] - H1[m][k] * H2[m][k].d(mu)) * (ETA[m] * ETA[k])
                   for m in range(D) for k in range(D))
        w.append(acc * (F(1, 2) * ETA[mu]))
    w = vadd(w, vadd(papply(H2, a1), papply(H1, a2), -1), F(1, 2))
    w = vadd(w, vadd(vscal(t2, d1), vscal(t1, d2), -1), F(1, 2))
    w = vadd(w, vadd(papply(H1, d2), papply(H2, d1), -1))
    return vadd(w, vadd(vscal(t2, a1), vscal(t1, a2), -1), F(-1, 2))


def box(f):
    return jsum(f.d(mu).d(mu) * ETA[mu] for mu in range(D))


def peinstein(H):
    """E[h](a) = 1/2 (box h(a) + (a.grad) grad tau - (a.grad) d - grad(a.d)) - 1/2 a (box tau - div d)."""
    t, d = ptrace(H), pdiv(H)
    s = box(t) - vdiv(d)
    out = pzeros()
    for m in range(D):
        for k in range(D):
            x = box(H[m][k]) + t.d(m).d(k) * (ETA[m] * ETA[k]) - d[k].d(m) * ETA[m] - d[m].d(k) * ETA[k]
            if m == k:
                x = x - s * ETA[m]
            out[m][k] = x * F(1, 2)
    return out


def displacement(xi):
    """D_xi(a) = a.grad xi + grad(xi.a)."""
    return [[xi[k].d(m) * ETA[m] + xi[m].d(k) * ETA[k] for k in range(D)] for m in range(D)]


def boost_variation(H):
    """L h (a) = (xi_B.grad) h(a) + B.h(a) - h(B.a): minus the derivative at chi = 0 of
    R h(R~ a R; R~ x R) R~, R = exp(-chi B/2)."""
    out = pzeros()
    for m in range(D):
        for k in range(D):
            x = jsum(XIB[a] * H[m][k].d(a) for a in range(D))
            x = x - jsum(H[a][k] * XIB[m].d(a) + H[m][a] * XIB[k].d(a) for a in range(D))
            out[m][k] = x
    return out


def bwedge(u, v):
    return {(i, j): u[i] * v[j] - u[j] * v[i] for i in range(D) for j in range(i + 1, D)}


def badd(A, B, c=1):
    return {b: A[b] + B[b] * c for b in A}


def potential(H, xi, coef):
    """K_xi[h] with the coefficients of potential_symbol, on polynomial fields."""
    t, d = ptrace(H), pdiv(H)
    K = {b: x * coef[0] for b, x in bwedge(xi, vadd(d, grad(t), -1)).items()}
    for mu in range(D):
        emu = [ONE * ETA[mu] if k == mu else ZJ for k in range(D)]
        dH = [[H[m][k].d(mu) for k in range(D)] for m in range(D)]
        dxi = [xi[k].d(mu) for k in range(D)]
        K = badd(K, bwedge(emu, papply(dH, xi)), coef[1])
        K = badd(K, bwedge(emu, papply(H, dxi)), coef[2])
        K = badd(K, bwedge(emu, dxi), t * coef[3])
    return K


def bcomp(K, i, j):
    if i < j:
        return K[(i, j)]
    if i > j:
        return K[(j, i)] * (-1)
    return ZJ


def bdiv(K):
    """grad . K, a vector field: (grad.K)^j = sum_i d_i K^{ij}."""
    return [jsum(bcomp(K, i, j).d(i) for i in range(D)) for j in range(D)]


def bdotv(K, v):
    """K . v for a bivector field K and a constant vector v (upper components)."""
    return [jsum(bcomp(K, j, i) * v[i] * ETA[i] for i in range(D)) for j in range(D)]


def dn(f):
    """n.grad f = d/d lam along the generators of N."""
    return f.d(0) + f.d(3)


def dnb(f):
    """nbar.grad f = d/d mu along the generators of Nbar."""
    return f.d(0) - f.d(3)


def on_N(f):
    """restriction to N (t = z = lam): a polynomial {(a, b, c): coefficient} in (lam, x, y)."""
    out = {}
    for e, c in f.c.items():
        key = (e[0] + e[3], e[1], e[2])
        out[key] = out.get(key, F(0)) + c
    return {k: v for k, v in out.items() if v}


def on_Nbar(f):
    """restriction to Nbar (t = mu, z = -mu)."""
    out = {}
    for e, c in f.c.items():
        key = (e[0] + e[3], e[1], e[2])
        out[key] = out.get(key, F(0)) + c * (-1) ** e[3]
    return {k: v for k, v in out.items() if v}


def cut(P, lam):
    """a polynomial on N at the cut lam: {(b, c): coefficient} in (x, y)."""
    out = {}
    for e, c in P.items():
        key = (e[1], e[2])
        out[key] = out.get(key, F(0)) + c * F(lam) ** e[0]
    return {k: v for k, v in out.items() if v}


def integrate(P, lo, hi):
    """exact integral of a polynomial {exponents: coefficient} over the box prod [lo_i, hi_i]."""
    tot = F(0)
    for e, c in P.items():
        term = c
        for i in range(len(e)):
            k = e[i] + 1
            term = term * (F(hi[i]) ** k - F(lo[i]) ** k) * F(1, k)
        tot += term
    return tot


def side(P, i, val):
    """a polynomial {(a, b, c)} on N with its i-th variable set to val: a polynomial in the other two."""
    out = {}
    for e, c in P.items():
        key = tuple(e[j] for j in range(3) if j != i)
        out[key] = out.get(key, F(0)) + c * F(val) ** e[i]
    return {k: v for k, v in out.items() if v}


def side_xy(P, i, val):
    """a polynomial {(b, c)} on the corner with its i-th variable set to val."""
    out = {}
    for e, c in P.items():
        key = tuple(e[j] for j in range(2) if j != i)
        out[key] = out.get(key, F(0)) + c * F(val) ** e[i]
    return {k: v for k, v in out.items() if v}


class Stream(object):
    """a fixed stream of small integers (a linear congruential sequence): generic sample data."""

    def __init__(self, seed):
        self.s = seed

    def next(self, lo, hi):
        self.s = (self.s * 1103515245 + 12345) % 2147483648
        return lo + (self.s // 65536) % (hi - lo + 1)


def sample_poly(st, deg, terms):
    """a polynomial with small rational coefficients; every other term is free of t and z, so that the
    restriction to the corner t = z = 0 is generic too."""
    f = ZJ
    for j in range(terms):
        m = ONE * F(st.next(1, 4) * (1 - 2 * st.next(0, 1)), st.next(1, 3))
        for i in range(D):
            e = st.next(0, deg)
            if j % 2 == 0 and i in (0, 3):
                e = 0
            m = m * X[i] ** e
        f = f + m
    return f


def sample_field(seed, deg=2, terms=4):
    """a generic symmetric field with polynomial coefficients (no gauge condition)."""
    st = Stream(seed)
    H = pzeros()
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = sample_poly(st, deg, terms)
    return H


def sample_vector(seed, deg=2, terms=4):
    st = Stream(seed)
    return [sample_poly(st, deg, terms) for _ in range(D)]


def sample_gauge_field(seed, deg=2, terms=4):
    """a generic polynomial field in the gauge h(n) = 0."""
    st = Stream(seed)
    H = pzeros()
    for Bm in GAUGE_BASIS:
        H = padd(H, pconst(Bm, sample_poly(st, deg, terms)))
    return H


def lin(p):
    """the polynomial p.x for a constant vector p (upper components)."""
    return jsum(X[i] * (ETA[i] * p[i]) for i in range(D))


# null momenta with two unit spacelike vectors orthogonal to each and to one another (up to the scale shown)
WAVES = [((1, 0, 0, -1), (0, 1, 0, 0), 1, (0, 0, 1, 0), 1, (2, -1, 3, 1), (3, -2), 2),
         ((5, 3, 0, 4), (0, 0, 1, 0), 1, (0, 4, 0, -3), 25, (1, 2, -1, 3), (-1, 2), 3),
         ((3, 2, 2, 1), (0, 1, -1, 0), 2, (0, 1, 1, -4), 18, (-2, 1, 1, 2), (2, 1), 2)]


def wave_maps():
    """for each null momentum p a symmetric map in the kernel of G_p: transverse trace-free plus a
    displacement a -> (a.p) w + (a.w) p; with the power of p.x that multiplies it."""
    out = []
    for pc, m1, q1, m2, q2, wc, (alpha, beta), power in WAVES:
        p, a, b = vec(pc), vec(m1), vec(m2)
        plus = madd(mscal(F(1, 2 * q1), outer(a, a)), mscal(F(1, 2 * q2), outer(b, b)), -1)
        H = madd(madd(mscal(F(alpha), plus), outer(a, b), F(beta)), outer(p, vec(wc)))
        out.append((pc, H, power))
    return out


def vacuum_field(seed):
    """a polynomial solution of the first-order equation without source, in a generic gauge: a sum of
    powers of p.x times maps in the kernel of G_p at three null momenta, plus a polynomial displacement."""
    h = pzeros()
    for pc, H, power in wave_maps():
        h = padd(h, pconst(H, lin(pc) ** power))
    return padd(h, displacement(sample_vector(seed, 2, 3)))


def not_weak_field():
    """the field of the first-order result's check: hb^{-1} = id + s, s symmetric, s(n) = 0, polynomial and
    not small, Omega solved from the torsion equation."""
    up = [upper(N), upper(M1), upper(M2)]
    maps = [[[up[i][m] * up[j][k] + up[j][m] * up[i][k] for k in range(D)] for m in range(D)]
            for i, j in ((0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2))]

    def hbinv(Y):
        t, x, y, z = Y
        v = t + z
        cs = [F(1, 7) * v * x, F(1, 5) * v, F(1, 11) * y, F(1, 6) * v + F(1, 10) * v * v,
              F(1, 8) * v + F(1, 12) * y * v, F(-1, 9) * v + F(1, 14) * x]
        H = [[sum((cs[i] * maps[i][m][k] for i in range(6)), gtg.Jet.const(0, D)) for k in range(D)]
             for m in range(D)]
        return [[(1 if mu == a else 0) + ETA[mu] * H[mu][a] for a in range(D)] for mu in range(D)]

    return gtg.field_from_hbinv(hbinv, (F(1, 2), F(1, 3), F(-1, 4), F(1, 5)), S, order=1)


# ---------------------------------------------------------------------------------------------------------
# sample data and windows (module level: none of this is an asserted value)
# ---------------------------------------------------------------------------------------------------------

COEF_NOTE = "Psi = xi^(d - grad tau) - grad^h(xi)[on h] + grad^h(xi)[on xi] - 1/2 tau grad^xi"
COEF = (F(1), F(-1), F(1), F(-1, 2))       # the coefficients of the potential; asserted in the first check
Z0 = F(0)
B03 = (0, 3)                               # the blade e_0 e_3 = B: the component of a bivector on it is B.Psi
LO, HI = (0, 0, -1), (2, 2, 2)             # the window 0 < lam < 2, 0 < x < 2, -1 < y < 2 of N+
GENERIC = [(i, i, i + 1, (i + 3) % 5) for i in range(len(SYM))]   # indices of (map, p, xi, q) in SYM, VECS
FRAME_PLANE = wedge(E[0], E[1])

VACUUM_SEED, OFF_SHELL_SEED, SOURCE_SEED, GAUGE_SEED = 7, 13, 17, 19
BOOST_SEED, SECOND_SEED, COVARIANCE_SEED, BRACKET_SEED = 29, 53, 31, 37
CORNER_AXES = (1, 2)
FAR = HI[0]                                # the far cut lam = 2 of the window


def gauge_sample(seed):
    """a generic polynomial field in the gauge h(n) = 0, of degree two in each label, five terms a component."""
    return sample_gauge_field(seed, 2, 5)


def source_sample(seed):
    """a generic polynomial field in no gauge, with a source."""
    return sample_field(seed, 2, 5)


def corner_gram(gs):
    """(g_1.g_1)(g_2.g_2) - (g_1.g_2)^2 for vectors with components polynomial in eps."""
    a, b = (gs[j] for j in CORNER_AXES)
    return eps_dot(a, a) * eps_dot(b, b) - eps_dot(a, b) * eps_dot(a, b)
EPS = gtg.Jet.var(0, 0, 1, None)           # the parameter eps of hb^{-1} = id + eps s, as an exact polynomial
EPS0, EPS1 = (0,), (1,)                    # exponents: the constant term and the term linear in eps


def eps_vector(sm, j):
    """g_j = e_j + eps s(e_j), components on the frame as polynomials in eps."""
    img = apply(sm, E[j])
    return [gtg.Jet.const(1 if k == j else 0, 1) + EPS * (F(ETA[k]) * dot(img, E[k])) for k in range(D)]


def eps_dot(u, v):
    out = gtg.Jet.const(0, 1)
    for k in range(D):
        out = out + u[k] * v[k] * ETA[k]
    return out


def gram_det(fld):
    """a^2 = (g_1.g_1)(g_2.g_2) - (g_1.g_2)^2 for g_j = hb^{-1}(e_j), as a jet."""
    def gram(i, j):
        return sum((ETA[c] * fld.TH[c][i] * fld.TH[c][j] for c in range(D)), gtg.Jet.const(0, D))
    return gram(1, 1) * gram(2, 2) - gram(1, 2) * gram(1, 2)


def screen_data(fld):
    """expansion, <sigma, sigma> and n.R(n) of the generators along n, as in the first-order result's check:
    B(A) = A.D n on the physical frame, its trace, its screen block on gamma_1, gamma_2, and the Ricci map."""
    Bj = [gtg.comm(fld.om[c], N, S) for c in range(D)]
    Bv = [gtg.m_val(b) for b in Bj]
    th = sum(dot(REC[c], Bv[c]) for c in range(D))
    Sc = [[dot(REC[a], Bv[b]) for b in CORNER_AXES] for a in CORNER_AXES]
    sig2 = Sc[0][0] ** 2 + 2 * Sc[0][1] * Sc[1][0] + Sc[1][1] ** 2 - F(1, 2) * th * th
    nRn = dot(N, gtg.ricci(gtg.as_op(fld.curvature()), N, S))
    return th, sig2, nRn


def conj(R, v):
    """R v R~ for an unnormalised rotor R (the factor R R~ is left in)."""
    return g1(mul(mul(R, v, S), GA.reverse(R), S))


def carried_map(W, H, m):
    """the map a -> W h(W~ a W) W~ on the reciprocal frame vector e^m, for a rotor W with W W~ = 1."""
    return conj(W, apply(H, g1(mul(mul(GA.reverse(W), REC[m], S), W, S))))


def generic_symbols():
    return [(sym(SYM[a]), vec(VECS[b]), vec(VECS[c]), vec(VECS[d])) for a, b, c, d in GENERIC]


def tr_perp(H):
    """the trace over the corner plane, frame-free: tr h - n.h(nbar) (the reciprocals of n, nbar are nbar/2, n/2)."""
    return ptrace(H) - vdot(NU, papply(H, NBU))


def tr_perp_by_frame(H):
    """e^1.h(e_1) + e^2.h(e_2) in the matrix convention."""
    return (H[1][1] + H[2][2]) * (-1)


def corner(f):
    """restriction to the corner t = z = 0: a polynomial {(b, c): coefficient} in (x, y)."""
    return cut(on_N(f), 0)


def div_perp(v):
    """the divergence along the corner of the part of a vector field along the corner."""
    return v[1].d(1) + v[2].d(2)


def window_total(f):
    return integrate(on_N(f), LO, HI)


def cut_total(f, lam):
    return integrate(cut(on_N(f), lam), LO[1:], HI[1:])


def corner_total(f):
    return cut_total(f, 0)


def side_flux(v):
    """the flux of the transverse part of a vector field through the four sides of the window of N+."""
    J1, J2 = on_N(v[1]), on_N(v[2])
    return (integrate(side(J1, 1, HI[1]), (LO[0], LO[2]), (HI[0], HI[2]))
            - integrate(side(J1, 1, LO[1]), (LO[0], LO[2]), (HI[0], HI[2]))
            + integrate(side(J2, 2, HI[2]), (LO[0], LO[1]), (HI[0], HI[1]))
            - integrate(side(J2, 2, LO[2]), (LO[0], LO[1]), (HI[0], HI[1])))


def edge_flux(v):
    """the flux of the part of a vector field along the corner through the edge of the corner window."""
    z1, z2 = corner(v[1]), corner(v[2])
    return (integrate(side_xy(z1, 0, HI[1]), LO[2:], HI[2:]) - integrate(side_xy(z1, 0, LO[1]), LO[2:], HI[2:])
            + integrate(side_xy(z2, 1, HI[2]), LO[1:2], HI[1:2]) - integrate(side_xy(z2, 1, LO[2]), LO[1:2], HI[1:2]))


def cutoff_boost():
    """xi = f g xi_B and g: the boost at the corner with weight g(x, y) there, vanishing to second order on
    the far cut lam = 2 (f = (1 - nbar.x/4)^2) and on the sides of the window (g)."""
    t, x, y, z = X
    f = (ONE - (t + z) * F(1, 4)) ** 2
    g = (x * (ONE * 2 - x)) ** 2 * ((ONE + y) * (ONE * 2 - y)) ** 2 * F(1, 4)
    return vscal(f * g, XIB), g


def cutoff_boost_bar():
    """the same on Nbar+: xi = fbar g xi_B with fbar = (1 - n.x/4)^2, vanishing to second order on the far cut
    mu = 2 of the window of Nbar+ (n.x = 2 mu there), and the same weight g on the corner."""
    t, x, y, z = X
    fbar = (ONE - (t - z) * F(1, 4)) ** 2
    g = (x * (ONE * 2 - x)) ** 2 * ((ONE + y) * (ONE * 2 - y)) ** 2 * F(1, 4)
    return vscal(fbar * g, XIB), g


def window_total_bar(f):
    """the integral over the window 0 < mu < 2, 0 < x < 2, -1 < y < 2 of Nbar+."""
    return integrate(on_Nbar(f), LO, HI)


def corner_samples():
    """a generic field in no gauge, a generic weight, and vector fields for the displacements of clause (ii)."""
    t, z = X[0], X[3]
    h = sample_field(11)
    wgt = sample_poly(Stream(5), 2, 4) + 1
    zeta = sample_vector(23)
    zfix = vadd(vscal(t, sample_vector(31)), vscal(z, sample_vector(37)))      # vanishes on the corner
    a_, b_ = sample_poly(Stream(41), 2, 4), sample_poly(Stream(43), 2, 4)
    zoff = vadd(vadd(vscal(a_, NU), vscal(b_, NBU)), [ZJ, t * a_, z * b_, ZJ])  # along n, nbar on the corner
    ztan = [ZJ, zeta[1] + X[2] * X[2], zeta[2] + X[1] * X[2] * 2, ZJ]           # along the corner
    return h, wgt, zeta, zfix, zoff, ztan


def half_turn_parts():
    kept = (NPLUS, NCROSS, outer(M1, M1), outer(N, NBAR), outer(N, N))
    mixed = (outer(N, M1), outer(N, M2), outer(NBAR, M1), outer(NBAR, M2))
    return kept, mixed


# ---------------------------------------------------------------------------------------------------------
# checks
# ---------------------------------------------------------------------------------------------------------

def check_pairing_with_a_displacement_is_the_field_equation_plus_a_divergence():
    premise(R1)
    coef = (F(1), F(-1), F(1), F(-1, 2))
    ok, count, nonzero = coef == COEF, 0, 0
    pts = quadratic_points()
    # complete verification: the identity is linear in h and in xi and homogeneous quadratic in (p, q)
    for H in sym_units():
        cache = {}
        for xi in E:
            for pc, qc in pts:
                p, q = vec(pc), vec(qc)
                if pc not in cache:
                    cache[pc] = einstein(H, p)
                lhs = omega(H, p, outer(q, xi), q)
                rhs = add(scal(2, apply(cache[pc], xi)), vdotB(add(p, q), potential_symbol(H, p, xi, q, coef)))
                ok = ok and GA.eq(lhs, rhs)
                count += 1
                nonzero += not GA.is_zero(lhs)
    ok = ok and len(pts) == 36 and count == 1440 and nonzero == 618
    # the same on generic symbols, every term present
    seen, rows = 0, []
    for H, p, xi, q in generic_symbols():
        lhs = omega(H, p, outer(q, xi), q)
        field_eq = scal(2, apply(einstein(H, p), xi))
        div = vdotB(add(p, q), potential_symbol(H, p, xi, q, coef))
        ok = ok and GA.eq(lhs, add(field_eq, div))
        seen += not (GA.is_zero(lhs) or GA.is_zero(field_eq) or GA.is_zero(div))
        # the six bivectors with one derivative: xi^h(p), tau xi^p, p^h(xi), q^h(xi), tau q^xi, h(q)^xi
        hx, tau = apply(H, xi), tr_map(H)
        cands = [wedge(xi, apply(H, p)), scal(tau, wedge(xi, p)), wedge(p, hx), wedge(q, hx),
                 scal(tau, wedge(q, xi)), wedge(apply(H, q), xi)]
        cols = [vdotB(add(p, q), Kc) for Kc in cands]
        for comp in range(D):
            rows.append([c.get((comp,), Z0) for c in cols])
    # no other combination of the six will do: the system for the coefficients has rank six
    ok = ok and seen == 4 and len(rows) == 16 and GA.mat_rank(rows) == 6
    # the component forms of the trace and of a.e_m used by the copied helpers agree with the product
    ok = ok and all(tr_map(sym(c)) == tr_by_product(sym(c)) for c in SYM)
    ok = ok and all(tr_map(U) == tr_by_product(U) for U in sym_units())
    ok = ok and all(dot(vec(c), E[m]) == ETA[m] * vec(c).get((m,), Z0) for c in VECS for m in range(D))
    GA.check("(i) omega(h, Delta_xi) = 2 E[h](xi) + div Psi_xi[h], " + COEF_NOTE + ": verified completely "
             "(ten unit maps, four frame vectors, 36 points determining a quadratic form in the two momenta) "
             "and on four generic symbols with every term nonzero; the coefficients are the only ones", ok)
    return ok


def check_corner_value_of_the_potential_is_the_transverse_trace():
    premise(R1)
    h, wgt, zeta, zfix, zoff, ztan = corner_samples()
    xi = vscal(wgt, XIB)
    K = potential(h, xi, COEF)
    tp = tr_perp(h)
    # frame-free trace against components; the corner value; it is not the full trace
    ok = (tp - tr_perp_by_frame(h)) == 0
    ok = ok and corner(K[B03] + wgt * tp) == {} and bool(corner(wgt * tp))
    ok = ok and bool(corner(K[B03] + wgt * ptrace(h)))
    # with the corner coefficient -1 the density is -2 w (delta a), delta a = 1/2 tr_perp h; other values fail
    ok = ok and corner(K[B03] * (-1) - wgt * (tp * F(1, 2)) * 2) == {}
    # the area variation of the corner under a displacement: tr_perp Delta_zeta = 2 div_perp zeta, identically
    ok = ok and (tr_perp(displacement(zeta)) - div_perp(zeta) * 2) == 0 and bool(div_perp(zeta))
    # a displacement that fixes the corner pointwise changes Delta_zeta there but not the charge
    Dfix = displacement(zfix)
    ok = ok and all(corner(c) == {} for c in zfix) and any(bool(corner(c)) for row in Dfix for c in row)
    ok = ok and corner(potential(Dfix, xi, COEF)[B03]) == {} and corner(tr_perp(Dfix)) == {}
    # a displacement that moves the corner off itself, with transverse part vanishing on it: no change
    ok = ok and any(bool(corner(c)) for c in zoff)
    ok = ok and corner(potential(displacement(zoff), xi, COEF)[B03]) == {}
    # a displacement along the corner changes the density by a divergence: the total is a flux through the edge
    dens = corner(potential(displacement(ztan), XIB, COEF)[B03])
    total = integrate(dens, LO[1:], HI[1:])
    ok = ok and total == -2 * edge_flux(ztan) and total == -4
    GA.check("(ii) at the corner B.Psi_xi[h] = -w tr_perp h for xi = w x.B, in every gauge (tr_perp h = tr h - "
             "n.h(nbar), twice the first-order change of the area density); tr_perp Delta_zeta = 2 div_perp "
             "zeta: no change under displacements whose transverse part vanishes on the corner, a divergence "
             "on the corner otherwise", ok)
    return ok



def check_area_density_of_the_corner_from_the_position_gauge_field():
    premise(R1)
    ok = True
    # first order: hb^{-1} = id + eps s for a symmetric map s in no particular gauge; the physical bivector
    # over e_1 ^ e_2 is g_1 ^ g_2, g_j = hb^{-1}(e_j), and a^2 = -(g_1 ^ g_2)^2 = (g_1.g_1)(g_2.g_2) - (g_1.g_2)^2
    for c in SYM:
        sm = sym(c)
        gs = [eps_vector(sm, j) for j in range(D)]
        asq = corner_gram(gs)
        trp = sum(dot(REC[j], apply(sm, E[j])) for j in CORNER_AXES)
        # a^2 = 1 + 2 eps tr_perp s + ..., so a = 1 + eps tr_perp s = 1 + 1/2 tr_perp h with h = 2 eps s
        ok = ok and asq.coeff(EPS0) == 1 and asq.coeff(EPS1) == 2 * trp and bool(trp)
        # the derived metric is a.b + 2 eps s(a).b to first order
        ok = ok and all(eps_dot(gs[j], gs[k]).coeff(EPS1) == 2 * dot(apply(sm, E[j]), E[k])
                        for j in range(D) for k in range(D))
    # a field that is not weak, in the gauge s(n) = 0: a^2 = -(g_1 ^ g_2)^2, g_j orthogonal to n (the screen),
    # theta = d/d lam ln a, and the focusing equation in area form a'' = a (theta^2/2 - <sigma,sigma> + n.R(n))
    fld = not_weak_field()
    th, sig2, nRn = screen_data(fld)
    asq = gram_det(fld)
    gv = [gtg.m_val(x) for x in fld.g]
    blade = wedge(*(gv[j] for j in CORNER_AXES))
    ok = ok and fld.torsion_free() and -mul(blade, blade, S).get((), Z0) == asq.v
    ok = ok and asq.v == F(7915466412774649, 14631321600000000)
    ok = ok and all(dot(gv[j], N) == 0 for j in CORNER_AXES)
    first = dn(asq).v                                                  # d/d lam (a^2)
    second = dn(dn(asq)).v                                             # d^2/d lam^2 (a^2)
    ok = ok and first == 2 * th * asq.v and th == F(-132120440, 88968907)
    # (a^2)'' = 2 a a'' + 2 a'^2 with a' = theta a
    ok = ok and second == 2 * asq.v * (F(1, 2) * th * th - sig2 + nRn) + 2 * th * th * asq.v
    ok = ok and sig2 == F(21403027745395200, 7915466412774649)
    ok = ok and nRn == F(-19070478282739200, 7915466412774649)
    GA.check("(iii) the physical bivector over the corner plane is hb^{-1}(e_1) ^ hb^{-1}(e_2) and its size a has "
             "a = 1 + 1/2 tr_perp h to first order (four generic maps, no gauge); (vi)(b) on a field that is not "
             "weak, in the gauge s(n) = 0, theta = d ln a/d lam and a'' = a (theta^2/2 - <sigma,sigma> + n.R(n))",
             ok)
    return ok


def check_flux_of_a_vacuum_field_against_the_corner_boost_is_a_pure_corner_term():
    premise(R1)
    premise(TWO)
    ok = True
    # the three plane-wave maps: null momenta crossing N, maps in the kernel of G_p, not pure displacements,
    # not in the gauge h(n) = 0
    waves = 0
    for pc, H, power in wave_maps():
        p = vec(pc)
        ok = ok and dot(p, p) == 0 and bool(dot(N, p)) and einstein(H, p) == ZERO
        ok = ok and not GA.is_zero(riem(H, p, FRAME_PLANE)) and not GA.is_zero(apply(H, N))
        waves += 1
    h = vacuum_field(VACUUM_SEED)
    ok = ok and waves == 3 and pzero(peinstein(h)) and not vzero(papply(h, NU))
    # xi = f g xi_B: the boost at the corner with weight g(x, y) there, zero to first order on the far cut
    # and on the sides of the window
    xi, g = cutoff_boost()
    Dxi = displacement(xi)
    ok = ok and not pzero(Dxi) and all(corner(c) == {} for row in Dxi for c in row)
    w = pomega(h, Dxi)
    flux = window_total(vdot(NU, w))
    area = corner_total(g * tr_perp(h) * F(1, 2))                      # int g (delta a) over the corner
    # (1/16 pi G) flux = -(1/8 pi G) int g delta a
    ok = ok and F(1, 16) * flux == -F(1, 8) * area and area == F(306678, 875)
    # on Nbar+ the corner term has the opposite sign: a flow smooth across the corner has none, and the pair
    # carries (1/8 pi G) int (w_Nbar - w_N) delta a
    xib, gb = cutoff_boost_bar()
    flux_bar = window_total_bar(vdot(NBU, pomega(h, displacement(xib))))
    ok = ok and (gb - g) == 0 and F(1, 16) * flux_bar == F(1, 8) * area and flux + flux_bar == 0
    # off the solutions the same flux is the field-equation term plus the corner term
    h2 = padd(h, sample_field(OFF_SHELL_SEED))
    ok = ok and not pzero(peinstein(h2))
    w2 = pomega(h2, Dxi)
    flux2 = window_total(vdot(NU, w2))
    bulk = window_total(vdot(NU, papply(peinstein(h2), xi)) * 2)
    area2 = corner_total(g * tr_perp(h2) * F(1, 2))
    ok = ok and flux2 == bulk - 2 * area2 and bulk == F(-184248, 6125) and area2 == F(619881, 1750)
    GA.check("(iv) for a polynomial vacuum field in a generic gauge (three null plane waves and a displacement) "
             "the flux through the window of N+ of omega(h, Delta_xi), xi = f g x.B, is exactly -2 int g delta a "
             "over the corner: with the stored constant 1/(16 pi G) the corner term is -(1/8 pi G) int g delta a; "
             "on Nbar+ it is +(1/8 pi G) int g delta a; off the solutions the difference is 2 int n.E[h](xi)", ok)
    return ok


def check_boost_weighted_flux_through_the_half_plane_and_the_corner_by_two_routes():
    premise(R1)
    lam = X[0]                                                         # t = z = lam on N; t = mu on Nbar
    # the exact boost is a symmetry of the flat field: no displacement; xi = lam n on N, -mu nbar on Nbar
    ok = pzero(displacement(XIB)) and all(on_N(XIB[k] - lam * NU[k]) == {} for k in range(D))
    ok = ok and all(on_Nbar(XIB[k] + lam * NBU[k]) == {} for k in range(D))
    # a generic field with a source, no gauge: the conservation law, and its form on N and on Nbar
    h = source_sample(SOURCE_SEED)
    Eh = peinstein(h)
    K = potential(h, XIB, COEF)
    dK = bdiv(K)
    ok = ok and not pzero(Eh) and vzero(vadd(dK, vscal(2, papply(Eh, XIB))))
    Kn, Knb = bdotv(K, NU), bdotv(K, NBU)
    ok = ok and (vdot(NU, dK) - (dn(K[B03] * (-1)) + div_perp(Kn))) == 0
    ok = ok and (vdot(NBU, dK) - (dnb(K[B03]) + div_perp(Knb))) == 0
    # on the window of N+: charges -B.Psi at the two cuts, side fluxes, and the weighted source
    far = cut_total(K[B03] * (-1), FAR)
    near = corner_total(K[B03] * (-1))
    weighted = window_total(lam * vdot(NU, papply(Eh, NU)))            # int lam n.E[h](n)
    ok = ok and far - near + side_flux(Kn) == -2 * weighted and weighted == F(-7406, 15)
    ok = ok and near == corner_total(tr_perp(h)) and near == F(-61, 2)
    # second route, in the gauge h(n) = 0: the first-order focusing equation with the boost weight
    hg = gauge_sample(GAUGE_SEED)
    Kg = potential(hg, XIB, COEF)
    tau = ptrace(hg)
    nEn = vdot(NU, papply(peinstein(hg), NU))
    ok = ok and vzero(papply(hg, NU)) and (nEn - dn(dn(tau)) * F(1, 2)) == 0
    ok = ok and on_N(Kg[B03] * (-1) - (tau - lam * dn(tau))) == {}
    ok = ok and on_N(div_perp(bdotv(Kg, NU))) == {}
    da = tau * F(1, 2)                                                 # delta a, the change of the area density
    route1 = cut_total(Kg[B03] * (-1), FAR) - corner_total(Kg[B03] * (-1))
    route2 = cut_total(da - lam * dn(da), FAR) - corner_total(da)
    source = window_total(lam * nEn)                                   # int lam n.E[h](n) = -8 pi G int lam n.T(n)
    ok = ok and route1 == 2 * route2 and route2 == -source and route2 == 192
    # with E[h] = -8 pi G T: int lam n.T(n) = (1/8 pi G) ((delta a - lam delta a')(far) - delta a(corner))
    ok = ok and F(1, 16) * route1 == F(1, 8) * route2 and -F(1, 8) * source == F(1, 8) * route2
    GA.check("(v) for the exact boost div Psi = -2 E[h](xi) identically; n.(div Psi) = d/d lam(-B.Psi) + div_perp "
             "and nbar.(div Psi) = d/d mu(+B.Psi) + div_perp; on a window of N+ the charges at the two cuts and "
             "the side fluxes balance -2 int lam n.E[h](n); in the gauge h(n) = 0, -B.Psi = tau - lam d_n tau and "
             "the integrated focusing equation gives the same number: (da - lam da')(far) - da(corner) = "
             "-int lam n.E[h](n)", ok)
    return ok


def check_flux_of_the_boost_variation_is_the_boost_weighted_null_energy():
    premise(R1)
    lam = X[0]
    hg = gauge_sample(BOOST_SEED)
    L = boost_variation(hg)
    ok = vzero(papply(hg, NU)) and vzero(papply(L, NU)) and not pzero(L)
    dh = [[dn(c) for c in row] for row in hg]
    tau = ptrace(hg)
    hp = ppair(hg, pconst(NPLUS, ONE)) * F(1, 2)
    hc = ppair(hg, pconst(NCROSS, ONE)) * F(1, 2)
    sig2 = (dn(hp) * dn(hp) + dn(hc) * dn(hc)) * F(1, 2)              # <sigma, sigma>, sigma = 1/2 d_n h^TT
    theta = dn(tau) * F(1, 2)
    ok = ok and (ppair(dh, dh) - dn(tau) * dn(tau) - (sig2 * 4 - theta * theta * 2)) == 0
    ok = ok and on_N(ptrace(L) - lam * dn(tau)) == {}
    nw = vdot(NU, pomega(hg, L))
    edge = lam * (ppair(hg, dh) - tau * dn(tau))
    want = lam * (sig2 - theta * theta * F(1, 2)) * 4 - dn(edge) * F(1, 2)
    ok = ok and on_N(nw - want) == {} and bool(nw - want)
    flux = window_total(nw)
    energy = window_total(lam * (sig2 - theta * theta * F(1, 2)))
    far = cut_total(edge, FAR)
    ok = ok and corner(edge) == {} and flux == 4 * energy - F(1, 2) * far
    ok = ok and flux == F(124816, 15) and far == F(-3564832, 15) and energy == F(-82880, 3)
    # (1/32 pi G) flux = (1/8 pi G) int lam (<sigma,sigma> - theta^2/2) - (1/64 pi G) far
    ok = ok and F(1, 32) * flux == F(1, 8) * energy - F(1, 64) * far
    # the flux form is carried into itself: n.omega(L h, k) + n.omega(h, L k) = d/d lam (lam n.omega(h, k)) on N,
    # so the variation of (1/32 pi G) flux(h, L h) is (1/16 pi G) flux(delta h, L h) up to a term on the far cut
    hk = gauge_sample(SECOND_SEED)
    n0 = vdot(NU, pomega(hg, hk))
    carried = vdot(NU, pomega(L, hk)) + vdot(NU, pomega(hg, boost_variation(hk)))
    ok = ok and on_N(carried - dn(lam * n0)) == {} and bool(on_N(n0))
    # the boost variation carries solutions to solutions and displacements to displacements
    hgen, zeta = sample_field(COVARIANCE_SEED), sample_vector(BRACKET_SEED)
    ok = ok and not pzero(peinstein(hgen))
    ok = ok and pzero(padd(peinstein(boost_variation(hgen)), boost_variation(peinstein(hgen)), -1))
    bracket = [jsum(XIB[a] * zeta[k].d(a) - zeta[a] * XIB[k].d(a) for a in range(D)) for k in range(D)]
    ok = ok and pzero(padd(boost_variation(displacement(zeta)), displacement(bracket), -1))
    GA.check("(vi)(a) in the gauge h(n) = 0 the boost variation L h keeps the gauge and on N "
             "n.omega(h, L h) = 4 lam (<sigma,sigma> - theta^2/2) - 1/2 d/d lam (lam (<h, d_n h> - tau d_n tau)): "
             "its flux through a window of N+ is 32 pi G times (1/8 pi G) int lam (<sigma,sigma> - theta^2/2), "
             "less a term on the far cut and none on the corner; the flux form is carried into itself; "
             "E[L h] = L E[h]", ok)
    return ok


def check_dual_of_the_boost_plane_is_the_corner_plane_and_the_periods():
    premise(DUAL)
    I4 = mul(mul(E[0], E[1], S), mul(E[2], E[3], S), S)
    B = mul(E[0], E[3], S)
    Bs = mul(I4, B, S)
    ok = GA.eq(mul(B, B, S), GA.sc(1)) and GA.eq(Bs, mul(E[1], E[2], S)) and GA.eq(mul(Bs, Bs, S), GA.sc(-1))
    ok = ok and GA.eq(mul(B, Bs, S), mul(Bs, B, S))
    # x.B: the velocity of the boost; n.B = n, nbar.B = -nbar, the corner is fixed
    ok = ok and GA.eq(vdotB(N, B), N) and GA.eq(vdotB(NBAR, B), GA.neg(NBAR))
    ok = ok and GA.is_zero(vdotB(M1, B)) and GA.is_zero(vdotB(M2, B))
    # the boost rotor 2 - B is exp(-chi B/2) up to scale with tanh(chi/2) = 1/2, e^chi = 3
    R = sub(GA.sc(2), B)
    ok = ok and GA.eq(mul(R, GA.reverse(R), S), GA.sc(3))
    ok = ok and GA.eq(conj(R, N), scal(3 * 3, N)) and GA.eq(conj(R, NBAR), NBAR)
    ok = ok and GA.eq(conj(R, M1), scal(3, M1)) and GA.eq(conj(R, M2), scal(3, M2))
    # the rotor of the dual plane, 2 - B* (cos phi = 3/5): fixes n and nbar, turns the corner plane
    Q = sub(GA.sc(2), Bs)
    ok = ok and GA.eq(mul(Q, GA.reverse(Q), S), GA.sc(5))
    ok = ok and GA.eq(conj(Q, N), scal(5, N)) and GA.eq(conj(Q, NBAR), scal(5, NBAR))
    ok = ok and GA.eq(conj(Q, M1), add(scal(3, M1), scal(-4, M2)))
    # the two rotors commute: the continued rotor is their product
    ok = ok and GA.eq(mul(R, Q, S), mul(Q, R, S))
    # half a period: exp(-pi B*/2) = -B*, reversing the corner vectors and fixing n, nbar; under
    # h -> W h(W~ a W) W~ the transverse trace-free components, the transverse trace and the n, nbar block are
    # unchanged and the components mixing the corner with n, nbar are reversed; a full period is -1
    W = GA.neg(Bs)
    ok = ok and GA.eq(mul(W, GA.reverse(W), S), GA.sc(1)) and GA.eq(mul(W, W, S), GA.sc(-1))
    ok = ok and GA.eq(conj(W, N), N) and GA.eq(conj(W, M1), GA.neg(M1)) and GA.eq(conj(W, M2), GA.neg(M2))
    kept, mixed = half_turn_parts()
    same = sum(all(GA.eq(carried_map(W, H, m), apply(H, REC[m])) for m in range(D)) for H in kept)
    flipped = sum(all(GA.eq(carried_map(W, H, m), GA.neg(apply(H, REC[m]))) for m in range(D)) for H in mixed)
    ok = ok and same == 5 and flipped == 4
    # (b) the modular energy of the imported Fact on a window, for a polynomial source in the gauge h(n) = 0:
    # with T = -E[h]/(8 pi G) the boost energy is K = int lam n.T(n) (held here times pi G), the modular
    # Hamiltonian of the Fact is 2 pi K, and it equals the area change over 4 G; half a period gives 1/8
    premise(MODULAR)
    hg = gauge_sample(GAUGE_SEED)
    lam = X[0]
    da = ptrace(hg) * F(1, 2)
    boost_energy = -F(1, 8) * window_total(lam * vdot(NU, papply(peinstein(hg), NU)))
    area_change = cut_total(da - lam * dn(da), FAR) - corner_total(da)
    ok = ok and 2 * boost_energy == F(1, 4) * area_change and boost_energy == F(1, 8) * area_change
    ok = ok and area_change == 192
    GA.check("(vii) I_4 B = e_1 e_2: the dual of the boost plane is the corner plane; exp(-chi B/2) scales n by "
             "e^chi and nbar by e^-chi and fixes the corner; the rotor of the dual plane commutes with it, fixes "
             "n and nbar and turns the corner; at half a period it is -B*, which leaves the transverse "
             "trace-free components, the trace and the n, nbar block of a symmetric map unchanged and reverses "
             "the components mixing the corner with n, nbar; on a window, 2 pi times the boost energy of a "
             "polynomial source is the area change over 4 G", ok)
    return ok
