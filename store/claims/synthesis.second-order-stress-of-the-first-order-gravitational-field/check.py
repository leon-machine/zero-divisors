"""The second-order stress of the first-order gravitational field: exact checks.

Cl(1,3), signature (+,-,-,-). A gravitational field hb = id + eps H1 + eps^2 H2 is built with lib/gtg.py,
with eps carried as a truncated polynomial (class Eps, arithmetic modulo eps^3) in the coefficients of the
gtg jets, and Omega solved exactly from the torsion equation. The Einstein map on the constant physical frame
is then G = eps G1[H1] + eps^2 (G1[H2] + G2[H1, H1]); the checks read off the two coefficients exactly.

A linear map M of the vectors is held as a 4 x 4 matrix of jets with M(e_a) = sum_k M[k][a] e_k.

(i)    the first-order part is the stored first-order Einstein map of h = -(H1 + H1^T), blind to the
       antisymmetric part of H1, and the first-order rotation gauge field is grad ^ S(a) - (a.grad) B;
(ii)   G2[H1, H1] is a symmetric map for every H1, symmetric or not, solution or not;
(iii)  its flat divergence is a combination of G1[H1] and its first derivatives (checked off solutions),
       and vanishes on first-order solutions that are neither symmetric nor plane waves;
(iv)   its change under a first-order displacement, a first-order rotation gauge change and a change of the
       second-order parametrisation, off and on solutions: on solutions it is G1 of a quadratic field;
(v)    the first-order Einstein map is the divergence of a bivector (superpotential), and its null-null
       component on a null plane is a derivative along the generator plus a transverse divergence;
(vi)   in the gauge h(n) = 0 the null-null component of G2 is <sigma, sigma> + theta^2/2 plus a second
       derivative along the generator whose coefficient depends on the parametrisation (a hand expansion,
       from the stored focusing equation, of one component of G2);
(vii)  on one plane wave the whole of G2 is (a.k) k times 1/4 <h', h'> plus such a derivative;
(viii) dust falling in its own first-order field: the flat divergence of its second-order stress is the
       force, and it is balanced exactly by the flat divergence of G2/(8 pi G);
Reading: the plane wave in the Kerr-Schild gauge has no quadratic part at all, and differs from the transverse
       trace-free wave of (vii) by a displacement that grows quadratically across the plane and a rotation.
"""
from fractions import Fraction as F

import GA
from GA import add, gen, mul, scal, sub
from tp_premise import premise
import gtg

D = 4
S = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
E = [gen(i) for i in range(D)]
REC = [scal(ETA[i], E[i]) for i in range(D)]
R1_ID = "synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators"
R2_ID = "synthesis.field-equation-linear-in-the-curvature-with-a-conserved-source-is-einsteins"
WEYL_FLAT_ID = ("synthesis.weyl-flat-variations-carry-only-the-stress-trace-and-the-whole-stress-clause-"
                "is-the-trace-free-channel")


# --------------------------------------------------------------------------------------------------
# eps as a truncated polynomial, and the field to second order
# --------------------------------------------------------------------------------------------------

class Eps(object):
    """a0 + a1 eps + a2 eps^2 modulo eps^3, exact: the ring in which the expansion is carried."""
    __slots__ = ("a",)

    def __init__(self, a):
        self.a = a

    def __add__(self, o):
        x = self.a
        if isinstance(o, Eps):
            y = o.a
            return Eps((x[0] + y[0], x[1] + y[1], x[2] + y[2]))
        return Eps((x[0] + o, x[1], x[2]))

    __radd__ = __add__

    def __neg__(self):
        x = self.a
        return Eps((-x[0], -x[1], -x[2]))

    def __sub__(self, o):
        x = self.a
        if isinstance(o, Eps):
            y = o.a
            return Eps((x[0] - y[0], x[1] - y[1], x[2] - y[2]))
        return Eps((x[0] - o, x[1], x[2]))

    def __rsub__(self, o):
        x = self.a
        return Eps((o - x[0], -x[1], -x[2]))

    def __mul__(self, o):
        x = self.a
        if isinstance(o, Eps):
            y = o.a
            return Eps((x[0] * y[0], x[0] * y[1] + x[1] * y[0], x[0] * y[2] + x[1] * y[1] + x[2] * y[0]))
        return Eps((x[0] * o, x[1] * o, x[2] * o))

    __rmul__ = __mul__

    def inv(self):
        x = self.a
        if not x[0]:
            raise ZeroDivisionError("Eps: not a unit")
        i0 = F(1) / x[0]
        i1 = -x[1] * i0 * i0
        i2 = -(x[1] * i1 + x[2] * i0) * i0
        return Eps((i0, i1, i2))

    def __truediv__(self, o):
        if isinstance(o, Eps):
            return self * o.inv()
        return self * (F(1) / o)

    def __rtruediv__(self, o):
        return self.inv() * o

    def __eq__(self, o):
        if isinstance(o, Eps):
            return self.a == o.a
        return self.a[0] == o and not self.a[1] and not self.a[2]

    def __ne__(self, o):
        return not self.__eq__(o)

    __hash__ = None

    def __bool__(self):
        x = self.a
        return bool(x[0] or x[1] or x[2])


EPS1 = Eps((F(0), F(1), F(0)))
EPS2 = Eps((F(0), F(0), F(1)))


def part(x, j):
    """the eps^j coefficient of a jet with Eps coefficients, as a rational jet."""
    cc = {}
    for e, c in x.c.items():
        v = c.a[j] if isinstance(c, Eps) else (c if j == 0 else 0)
        if v:
            cc[e] = F(v)
    return gtg.Jet(c=cc, nv=x.nv, order=x.order)


def jz():
    return gtg.Jet.const(0, D)


def labels(order):
    return [gtg.Jet.var(i, X0[i], D, order) for i in range(D)]


def omega_from_torsion(TH, HJ):
    """om[a] = Omega(hb(gamma_a)) from the torsion equation D_mu g_nu = D_nu g_mu, solved in the frame:
    om[a].gamma_b - om[b].gamma_a = C_ab = -sum HJ[mu][a] HJ[nu][b] (d_mu g_nu - d_nu g_mu), and with
    w_abk = (om[a].gamma_b).gamma_k = 1/2 (c_abk - c_bka + c_kab), om[a] = -sum_{b<k} eta_b eta_k w_abk gamma_b gamma_k."""
    z = jz()
    dg = [[[TH[k][nu].d(mu) - TH[k][mu].d(nu) for k in range(D)] for nu in range(D)] for mu in range(D)]
    half = [[[sum((HJ[nu][b] * dg[mu][nu][k] for nu in range(D) if nu != mu), z) for k in range(D)]
             for b in range(D)] for mu in range(D)]
    c = [[[sum((HJ[mu][a] * half[mu][b][k] for mu in range(D)), z) * (-ETA[k]) for k in range(D)]
          for b in range(D)] for a in range(D)]
    om = []
    for a in range(D):
        o = {}
        for b in range(D):
            for k in range(b + 1, D):
                t = (c[a][b][k] - c[b][k][a] + c[k][a][b]) * F(-ETA[b] * ETA[k], 2)
                if t:
                    o[(b, k)] = t
        om.append(o)
    return om


def einstein_orders(H1, H2=None):
    """(G1, G2, fld): the eps and eps^2 coefficients of the Einstein map of hb = id + eps H1 + eps^2 H2 on the
    physical frame, G[k][c] the component along gamma_k of G(gamma_c), as rational jets; fld the gtg field."""
    HJ = [[gtg.Jet.const(1 if m == a else 0, D) + H1[m][a] * EPS1 + (H2[m][a] * EPS2 if H2 is not None else 0)
           for a in range(D)] for m in range(D)]
    TH = gtg.mat_inv(HJ)
    fld = gtg.Field(TH, om=omega_from_torsion(TH, HJ), sq=S)
    Rj = fld.curvature_jet()

    def Rop(B):
        out = {}
        for (a, b), co in B.items():
            out = gtg.m_add(out, gtg.m_scal(co, Rj[(a, b)]))
        return out

    Ric = [gtg.ricci(Rop, E[c], S) for c in range(D)]
    sc = jz()
    for c in range(D):
        sc = sc + Ric[c].get((c,), jz())
    Gm = [[Ric[c].get((k,), jz()) - (sc * F(1, 2) if k == c else jz()) for c in range(D)] for k in range(D)]
    flat = all(not part(Gm[k][c], 0) for k in range(D) for c in range(D))
    G1 = [[part(Gm[k][c], 1) for c in range(D)] for k in range(D)]
    G2 = [[part(Gm[k][c], 2) for c in range(D)] for k in range(D)]
    return G1, G2, (fld if flat else None)


# --------------------------------------------------------------------------------------------------
# matrices of jets
# --------------------------------------------------------------------------------------------------

def mmul(A, B):
    return [[sum((A[m][k] * B[k][a] for k in range(D)), jz()) for a in range(D)] for m in range(D)]


def madd(A, B, c=1):
    return [[A[m][a] + B[m][a] * c for a in range(D)] for m in range(D)]


def mscal(c, A):
    return [[A[m][a] * c for a in range(D)] for m in range(D)]


def transpose(A):
    """the adjoint for the flat product."""
    return [[A[a][m] * (ETA[m] * ETA[a]) for a in range(D)] for m in range(D)]


def mtrace(A):
    return sum((A[m][m] for m in range(D)), jz())


def msub(A, B):
    return madd(A, B, -1)


def msum(parts, skip=None):
    """the sum of a list of matrices, optionally leaving one out."""
    out = [[jz() for _ in range(D)] for _ in range(D)]
    for j, P in enumerate(parts):
        if j != skip:
            out = madd(out, P)
    return out


def lowered(A):
    """the same matrix of jets, truncated one order lower (exact constants are left as they are)."""
    return [[x if x.order is None else x.trunc(x.order - 1) for x in row] for row in A]


def jets_equal(A, B):
    """equality of two matrices of jets, each pair compared to the lower of its two orders."""
    def same(x, y):
        orders = [o for o in (x.order, y.order) if o is not None]
        return x == y if not orders else x.trunc(min(orders)) == y.trunc(min(orders))

    return all(same(A[m][a], B[m][a]) for m in range(D) for a in range(D))


def meq(A, B):
    """equality of the values at the point."""
    return all(A[m][a].v == B[m][a].v for m in range(D) for a in range(D))


def nonzero(A):
    """the number of entries with nonzero value at the point."""
    return sum(1 for m in range(D) for a in range(D) if A[m][a].v != 0)


def symmetric(A):
    """A is a symmetric map at the point: a . A(b) = b . A(a)."""
    return all(ETA[k] * A[k][c].v == ETA[c] * A[c][k].v for k in range(D) for c in range(D))


def pairm(A, B):
    """<A, B> = sum_a A(e_a) . B(e^a)."""
    return sum((A[k][a] * B[k][a] * (ETA[k] * ETA[a]) for k in range(D) for a in range(D)), jz())


def advect(xi, M):
    """(xi . grad) M."""
    return [[sum((xi[m] * M[k][c].d(m) for m in range(D)), jz()) for c in range(D)] for k in range(D)]


def flat_div(M):
    """C -> grad . (M(C)), on the frame."""
    return [sum((M[k][c].d(k) for k in range(D)), jz()) for c in range(D)]


def first_order_einstein(h):
    """the stored first-order Einstein map as an operator on a field h of symmetric maps (the formula of the
    first-order result): E[h](a) = 1/2 (grad^2 h(a) + (a.grad) grad tau - (a.grad) d - grad (a.d))
    - 1/2 a (grad^2 tau - grad.d), tau = tr h, d = h-dot(grad-dot)."""
    def box(f):
        return sum((f.d(m).d(m) * ETA[m] for m in range(D)), jz())

    tau = mtrace(h)
    dv = [sum((h[k][m].d(m) * ETA[m] for m in range(D)), jz()) for k in range(D)]
    divd = sum((dv[k].d(k) for k in range(D)), jz())
    out = [[None] * D for _ in range(D)]
    for k in range(D):
        for a in range(D):
            t = box(h[k][a]) + tau.d(a).d(k) * ETA[k] - dv[k].d(a) - dv[a].d(k) * (ETA[a] * ETA[k])
            t = t * F(1, 2)
            if k == a:
                t = t - (box(tau) - divd) * F(1, 2)
            out[k][a] = t
    return out


def G1_of(M):
    """G1[M] = E[h] with h = -(M + M^T): the first-order part of the Einstein map of hb = id + eps M."""
    return first_order_einstein(mscal(-1, madd(M, transpose(M))))


# --------------------------------------------------------------------------------------------------
# symbols (constant maps and a momentum), with the stored first-order curvature
# --------------------------------------------------------------------------------------------------

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


def apply_map(M, a):
    """M(a) for a matrix of numbers M[k][c] (M(e_c) = sum_k M[k][c] e_k) and a vector a."""
    out = {}
    for c in range(D):
        ac = F(ETA[c]) * dot(a, E[c])
        if ac:
            for k in range(D):
                if M[k][c]:
                    out = add(out, scal(ac * M[k][c], E[k]))
    return out


def sym_map(c):
    """the symmetric map with contravariant components c (ten numbers), as a mixed matrix."""
    H = [[F(0)] * D for _ in range(D)]
    i = 0
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = F(c[i])
            i += 1
    return [[H[k][a] * ETA[a] for a in range(D)] for k in range(D)]


def riem_symbol(M, p, B):
    """the stored first-order curvature R_p[h](B) = -1/2 p ^ h(B.p)."""
    return scal(F(-1, 2), wedge(p, apply_map(M, GA.neg(vdotB(p, B)))))


def einstein_symbol(M, p):
    """the stored first-order Einstein map G_p[h], from the stored curvature: matrix [k][c]."""
    Ric = []
    for c in range(D):
        img = {}
        for b in range(D):
            img = add(img, vdotB(REC[b], riem_symbol(M, p, wedge(E[b], E[c]))))
        Ric.append(img)
    t = sum(dot(REC[c], Ric[c]) for c in range(D))
    return [[F(ETA[k]) * dot(Ric[c], E[k]) - (F(1, 2) * t if k == c else 0) for c in range(D)] for k in range(D)]


# --------------------------------------------------------------------------------------------------
# sample fields: fixed rational data, generic (the checks assert the genericity they use)
# --------------------------------------------------------------------------------------------------

X0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
SYM = [[3, -1, 2, 5, 4, -2, 1, -3, 2, 1], [-2, 4, 1, -1, 3, 2, -5, 1, 4, -3],
       [1, 2, -3, 4, -1, 5, 2, -2, 3, 1], [5, -3, 1, 2, -4, 1, 3, 2, -1, 4]]
VECS = [(2, 1, -1, 3), (1, -2, 3, 4), (3, 2, 1, -1), (-1, 4, 2, 1)]
NV, NB, M1, M2 = (1, 0, 0, 1), (1, 0, 0, -1), (0, 1, 0, 0), (0, 0, 1, 0)
# null momenta with orthonormal transverse pairs
WAVES = [((5, 3, 4, 0), (0, F(4, 5), F(-3, 5), 0), (0, 0, 0, 1)),
         ((3, 2, 1, 2), (0, F(2, 3), F(-2, 3), F(-1, 3)), (0, F(1, 3), F(2, 3), F(-2, 3))),
         ((9, 1, 4, 8), (0, F(8, 9), F(-4, 9), F(1, 9)), (0, F(4, 9), F(7, 9), F(-4, 9)))]
PROFILES = [((F(1, 2), F(1, 3), 2, -1), (F(-1, 3), F(1, 4), 1, 3), (F(1, 5), F(-1, 6), -2, 1), (F(1, 4), F(1, 5), 1, -2)),
            ((F(2, 3), F(-1, 5), 1, 2), (F(1, 4), F(1, 7), -3, 1), (F(-1, 2), F(1, 9), 2, 5), (F(-1, 3), F(1, 2), 3, 1))]
KAPPA = F(3)                      # stands for 8 pi G in the check of (viii); any nonzero rational would do


def low(v):
    return [F(ETA[i]) * F(v[i]) for i in range(D)]


def vdot4(u, v):
    return sum(F(ETA[i]) * F(u[i]) * F(v[i]) for i in range(D))


def outer_map(u, v):
    """the constant map a -> (a.u) v."""
    ul = low(u)
    return [[gtg.Jet.const(F(v[m]) * ul[a], D) for a in range(D)] for m in range(D)]


def tt_maps(m1, m2):
    return (madd(outer_map(m1, m1), outer_map(m2, m2), -1), madd(outer_map(m1, m2), outer_map(m2, m1)))


EPSP, EPSX = tt_maps(M1, M2)


def generic_map(seed, order):
    """a polynomial field of maps, not symmetric and not a solution of anything."""
    t, x, y, z = labels(order)
    mons = [t, x, y, z, t * x, y * z, t * t, x * y, z * z, t * z, x * x * y, t * y * z, z * z * z, t * t * x,
            x * y * z, y * y * y]
    out = [[None] * D for _ in range(D)]
    k = seed
    for m in range(D):
        for a in range(D):
            acc = jz()
            for j in range(4):
                k = (k * 7 + 3) % 101
                acc = acc + mons[(k + m * 5 + a * 3 + j * 4) % len(mons)] * F((k % 9) - 4, (k % 5) + 2)
            out[m][a] = acc
    return out


def waves_field(order, waves, profiles):
    """h = sum_j f_j(p_j.x) (c_j n_plus + d_j n_cross), f_j(u) = a_j u^2 + b_j u^3 + u/3: E[h] = 0."""
    X = labels(order)
    h = [[jz() for _ in range(D)] for _ in range(D)]
    for (p, m1, m2), (a, b, c, d) in zip(waves, profiles):
        pl = low(p)
        phi = sum((X[i] * pl[i] for i in range(D)), jz())
        f = phi * phi * a + phi * phi * phi * b + phi * F(1, 3)
        npl, ncr = tt_maps(m1, m2)
        T = madd(mscal(c, npl), mscal(d, ncr))
        h = madd(h, [[T[m][k] * f for k in range(D)] for m in range(D)])
    return h


def grad_map(xi):
    """the map a -> (a.grad) xi of a vector field xi (four jets)."""
    return [[xi[m].d(a) for a in range(D)] for m in range(D)]


def xi_field(k, order):
    """a polynomial vector field (jets of the given order)."""
    t, x, y, z = labels(order)
    polys = [t * x * F(1, 3) + y * y * z * F(1, 5) - z * z * z * z * F(1, 7) + t * t * y * F(2, 9),
             x * y * F(-1, 4) + t * z * z * F(1, 6) + x * x * x * t * F(1, 8) + y * z * F(1, 5),
             z * t * F(2, 5) - x * x * y * F(1, 7) + t * t * t * z * F(1, 9) + x * x * F(1, 11),
             y * y * F(1, 6) + t * x * z * F(-1, 5) + y * y * x * x * F(1, 10) + t * z * F(3, 7)]
    return [polys[(i + k) % 4] * F(k + 1, 2) for i in range(D)]


def biv_field(k, order):
    """a polynomial bivector field B."""
    t, x, y, z = labels(order)
    co = [t * F(1, 4) + x * y * F(1, 6), z * F(-1, 5) + t * t * F(1, 7), x * F(1, 3) - y * z * t * F(1, 8),
          y * F(2, 7) + x * x * F(1, 9), t * z * F(1, 5) - x * F(1, 6), z * z * F(1, 4) + y * F(1, 10) + x * y * z * F(1, 3)]
    bl = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    return {bl[i]: co[(i + k) % 6] * F(k + 2, 3) for i in range(6)}


def biv_map(B):
    """the antisymmetric map beta(a) = a . B of a bivector field B."""
    out = [[jz() for _ in range(D)] for _ in range(D)]
    for a in range(D):
        for (m,), c in gtg.inner_vb(E[a], B, S).items():
            out[m][a] = c
    return out


def solution(i, order):
    """a first-order solution that is neither symmetric nor a plane wave: three null waves, a displacement
    and a rotation gauge: H1 = -1/2 h + xi_ + beta, G1[H1] = 0."""
    H1 = mscal(F(-1, 2), waves_field(order, WAVES, PROFILES[i]))
    H1 = madd(H1, grad_map(xi_field(i, order + 1)))
    return madd(H1, biv_map(biv_field(i, order)))


def light_cone_waves():
    """four null momenta with n.p != 0, polarisation vectors m_i - (m_i.n)/(p.n) p orthogonal to p and to n."""
    out = []
    for p, m1, m2 in WAVES:
        pn = vdot4(p, NV)
        ms = [tuple(F(m[i]) - vdot4(m, NV) / pn * F(p[i]) for i in range(D)) for m in (m1, m2)]
        out.append((p, ms[0], ms[1]))
    out.append((NB, M1, M2))
    return out


def light_cone_solution(i, order):
    """a field h of symmetric maps with h(n) = 0 and E[h] = 0, with expansion: four null waves and the
    displacement xi = 1/2 nu nbar - 1/2 (nbar.x) grad nu, nu a polynomial of the transverse labels."""
    h = waves_field(order, light_cone_waves(), PROFILES[i])
    t, x, y, z = labels(order + 2)
    nu = x * x * F(i + 1, 3) + x * y * F(1, 4) - y * y * y * F(1, 5) + x * x * y * y * F(1, 7)
    gradnu = [jz(), -nu.d(1), -nu.d(2), jz()]
    xi = [nu * F(NB[i2], 2) - (t + z) * gradnu[i2] * F(1, 2) for i2 in range(D)]
    xb = grad_map(xi)
    return madd(h, madd(xb, transpose(xb)))


def dn(f):
    """n . grad of a scalar, n = e_0 + e_3."""
    return f.d(0) + f.d(3)


def nn(M):
    """n . M(n)."""
    nl = low(NV)
    return sum((M[k][a] * (nl[k] * NV[a]) for k in range(D) for a in range(D)), jz())


def plane_wave(jet):
    """h = f_plus(nbar.x) eps_plus + f_cross(nbar.x) eps_cross with the 2-jets jet = (f+, f+', f+'', fx, fx', fx'')
    of the two profiles at the point."""
    t, x, y, z = labels(2)
    u = t + z - (X0[0] + X0[3])
    fp = u * jet[1] + u * u * (F(jet[2]) * F(1, 2)) + jet[0]
    fx = u * jet[4] + u * u * (F(jet[5]) * F(1, 2)) + jet[3]
    return madd(mscal(fp, EPSP), mscal(fx, EPSX))


def quadratic_form_arguments():
    """the six unit vectors of a six-dimensional space and the fifteen sums of two of them: two quadratic forms
    that agree on these 21 arguments are equal."""
    units = [tuple(1 if i == j else 0 for i in range(6)) for j in range(6)]
    return units + [tuple(a + b for a, b in zip(units[i], units[j])) for i in range(6) for j in range(i + 1, 6)]


def dust(order):
    """dust at rest in its own first-order field. h(a) = phi (2 (a.e_0) e_0 - a), phi static, so that
    E[h] = -(Laplacian phi) (a.e_0) e_0 = -kappa T1 with T1 = rho0 (a.e_0) e_0, rho0 = Laplacian(phi)/kappa.
    Second order of T(a) = rho (a.v) v, rho = eps rho0 + eps^2 rho1, v = e_0 + eps v1: the geodesic equation
    v.D v = 0 at first order is d_t v1 = -Omega1(e_0).e_0 = -1/2 grad phi (Newton's law), and the continuity
    equation D.(rho v) = 0 at second order is d_t rho1 + grad.(rho0 v1) = 0 for this field.
    Returns H1 = -1/2 h, T1, T2 as matrices of jets."""
    t, x, y, z = labels(order + 2)
    phi = x * x * F(1, 2) + y * y * z * F(1, 3) - x * z * z * z * F(1, 4) + x * y * F(1, 5) + z * z * F(2, 3)
    rho0 = (phi.d(1).d(1) + phi.d(2).d(2) + phi.d(3).d(3)) * (F(1) / KAPPA)
    H1 = [[(phi * F((1 if k == a else 0) - (2 if k == a == 0 else 0), 2)).trunc(order) for a in range(D)]
          for k in range(D)]
    w = [jz(), y * F(1, 3) + x * z * F(1, 4), z * z * F(1, 5) - x * F(1, 2), x * y * F(1, 6) + y * F(1, 7)]
    v1 = [jz()] + [t * phi.d(k) * F(-1, 2) + w[k] for k in (1, 2, 3)]
    fd = sum(((rho0 * v1[k]).d(k) for k in (1, 2, 3)), jz())
    A = fd.d(0)
    rho1 = -(t * t * A * F(1, 2) + t * (fd - t * A)) + x * y * F(1, 3) + z * F(1, 4)
    T1 = [[rho0 if k == a == 0 else jz() for a in range(D)] for k in range(D)]
    T2 = [[jz() for _ in range(D)] for _ in range(D)]
    for k in range(D):
        for c in range(D):
            v = jz()
            if k == 0 and c == 0:
                v = v + rho1
            if k == 0:
                v = v + rho0 * v1[c] * ETA[c]
            if c == 0:
                v = v + rho0 * v1[k]
            T2[k][c] = v
    return H1, T1, T2, v1


# the samples the checks use, built here so that the integer literals inside a check function are expected
# values and coefficients of the identities, not sample data

GENERIC_JET = (F(2, 3), F(-1, 2), F(3, 4), F(1, 5), F(2, 7), F(-1, 3))
SPATIAL = (1, 2, 3)


def sample_field():
    """a polynomial H1, not symmetric and not a solution, with jets of third order."""
    return generic_map(5, 3)


def sample_field_low():
    return generic_map(5, 2)


def sample_second_order():
    return generic_map(11, 2)


def sample_displacement():
    xi = xi_field(2, 4)
    return xi, grad_map(xi)


def sample_rotation():
    return biv_map(biv_field(1, 3))


def sample_second_solution():
    return solution(1, 3)


def sample_solution():
    return solution(0, 3)


def sample_solution_low():
    return solution(1, 2)


def sample_light_cone_solutions():
    return [light_cone_solution(0, 2), light_cone_solution(1, 2)]


def sample_stored_wave():
    """a constant symmetric map h0 and a momentum p, with H1 = -1/4 (p.x)^2 h0: derived metric
    a.b + 1/2 (p.x)^2 h0(a).b at first order, the field on which the stored G_p[h0] is defined."""
    M0 = sym_map(SYM[0])
    X = labels(2)
    pl = low(VECS[0])
    P = sum((X[i] * pl[i] for i in range(D)), jz())
    H1 = [[P * P * (M0[k][a] * F(-1, 4)) for a in range(D)] for k in range(D)]
    return M0, vec(VECS[0]), H1


def light_cone_non_solution():
    """a polynomial field h of symmetric maps with h(n) = 0 that is not a solution of the first-order equation."""
    t, x, y, z = labels(2)
    maps = [outer_map(NV, NV), madd(outer_map(NV, M1), outer_map(M1, NV)), madd(outer_map(NV, M2), outer_map(M2, NV)),
            outer_map(M1, M1), madd(outer_map(M1, M2), outer_map(M2, M1)), outer_map(M2, M2)]
    polys = [t * x * F(1, 3) + z * z * F(1, 5) + y, x * y * F(1, 4) - t * t * F(1, 6) + z,
             z * t * F(2, 5) + x * x * F(1, 7), y * y * F(1, 6) + t * z * F(1, 5) + t,
             t * t * F(1, 2) + x * z * F(1, 3) - y * z, z * z * F(1, 4) + t * y * F(1, 3) + x]
    h = [[jz() for _ in range(D)] for _ in range(D)]
    for P, Sm in zip(polys, maps):
        h = madd(h, mscal(P, Sm))
    return h


def sym_unit_maps():
    """the ten unit symmetric maps, as mixed matrices of numbers."""
    out = []
    for i in range(10):
        c = [0] * 10
        c[i] = 1
        out.append(sym_map(c))
    return out


def polarising_momenta():
    """e_i and e_i + e_j: a quadratic expression in a momentum is fixed by its values on these ten."""
    return E + [add(E[i], E[j]) for i in range(D) for j in range(i + 1, D)]


TRANSVERSE = (1, 2)
ELL = (F(1, 2), 0, 0, F(-1, 2))          # l = 1/2 nbar: Q(l) = 0, n.l = 1


def plane_wave_two_gauges(with_trace):
    """one plane wave in two gauges. F_lam: symmetric maps of the transverse plane, polynomial in lam = l.x
    (trace-free unless with_trace); w = 1/2 F''. Returns (F, H1KS, xi): the transverse wave h = F, the
    Kerr-Schild map H1KS(a) = 1/2 W (a.l) l with W = -y.w(y), and xi = -1/2 F(y) + 1/4 (y.F'(y)) l."""
    t, x, y, z = labels(4)
    lam = (t + z) * F(1, 2)
    fp = lam * lam * F(2, 3) + lam * lam * lam * F(1, 5) - lam * F(1, 2) + lam * lam * lam * lam * F(1, 7)
    fx = lam * lam * F(-1, 4) + lam * lam * lam * F(2, 7) + lam * F(1, 3)
    Fm = madd(mscal(fp, EPSP), mscal(fx, EPSX))
    if with_trace:
        Fm = madd(Fm, mscal(lam * lam * F(1, 3), outer_map(M1, M1)))
    F1 = [[dn(v) for v in row] for row in Fm]            # d/dlam = n.grad, since n.l = 1
    F2 = [[dn(v) for v in row] for row in F1]
    yv = [jz(), x, y, jz()]

    def quad(M):
        return sum((yv[k] * M[k][a] * yv[a] * ETA[k] for k in range(D) for a in range(D)), jz())

    W = quad(F2) * F(-1, 2)
    ll = outer_map(ELL, ELL)
    HKS = [[ll[k][a] * W * F(1, 2) for a in range(D)] for k in range(D)]
    Fy = [sum((Fm[k][a] * yv[a] for a in range(D)), jz()) for k in range(D)]
    q1 = quad(F1)
    xi = [Fy[k] * F(-1, 2) + q1 * (F(ELL[k]) * F(1, 4)) for k in range(D)]
    trw = mtrace(F2) * F(1, 2)
    return Fm, HKS, xi, trw


def second_order(A):
    """the same matrix of jets, truncated to second order."""
    return [[x.trunc(2) for x in row] for row in A]


def sample_dust():
    return dust(3)


def sample_dust_gauge():
    xi = xi_field(1, 4)
    return xi, grad_map(xi), biv_map(biv_field(2, 3))


def first_order_omega(fld):
    """the eps coefficient of Omega(hb(gamma_c)), as bivectors with rational jet coefficients."""
    return [{b: part(c, 1) for b, c in fld.om[k].items() if part(c, 1)} for k in range(D)]


# --------------------------------------------------------------------------------------------------
# the checks
# --------------------------------------------------------------------------------------------------

def check_first_order_part_is_the_stored_einstein_map_and_is_blind_to_the_rotation_gauge():
    premise(WEYL_FLAT_ID)
    premise(R1_ID)
    ok = True
    # (a) hb = id + eps H1 with H1 = -1/4 (p.x)^2 h0 + beta: G1 is the stored G_p[h0] (computed from the stored
    # curvature R_p[h](B) = -1/2 p ^ h(B.p)), whatever the antisymmetric part beta
    M0, p, H1 = sample_stored_wave()
    want = einstein_symbol(M0, p)
    beta = lowered(sample_rotation())
    G1a, _, flda = einstein_orders(H1)
    G1b, _, fldb = einstein_orders(madd(H1, beta))
    ok = ok and flda is not None and fldb is not None and flda.torsion_free() and fldb.torsion_free()
    ok = ok and all(G1a[k][c].v == want[k][c] and G1b[k][c].v == want[k][c] for k in range(D) for c in range(D))
    ok = ok and sum(1 for k in range(D) for c in range(D) if want[k][c]) == 14
    ok = ok and sum(want[k][k] for k in range(D)) == -21 and nonzero(beta) == 12
    # (b) on a polynomial H1 that is not symmetric: G1 is the stored operator on h = -(H1 + H1^T)
    Hg = sample_field_low()
    G1g, _, fldg = einstein_orders(Hg)
    ok = ok and fldg is not None and fldg.torsion_free() and meq(G1g, G1_of(Hg)) and nonzero(G1g) == 16
    ok = ok and nonzero(msub(Hg, transpose(Hg))) == 12
    # (c) the first-order rotation gauge field: Omega1(a) = grad ^ S(a) - (a.grad) A,
    # S = 1/2 (H1 + H1^T), A = 1/2 d_b ^ H1(b)
    om1 = first_order_omega(fldg)
    Ssym = mscal(F(1, 2), madd(Hg, transpose(Hg)))
    Av = {}
    for b in range(D):
        col = {(k,): Hg[k][b] for k in range(D) if Hg[k][b]}
        Av = gtg.m_add(Av, gtg.m_scal(F(1, 2), gtg.wedge(REC[b], col, S)))
    blades = 0
    for a in range(D):
        pred = {}
        for mu in range(D):
            dS = {(k,): Ssym[k][a].d(mu) for k in range(D) if Ssym[k][a].d(mu)}
            pred = gtg.m_add(pred, gtg.wedge(REC[mu], dS, S))
        pred = gtg.m_val(gtg.m_sub(pred, gtg.m_d(Av, a)))
        got = gtg.m_val(om1[a])
        ok = ok and pred == got
        blades += len(got)
    ok = ok and blades == 22
    GA.check("(i) the first-order part of the Einstein map of hb = id + eps H1 is the stored first-order "
             "Einstein map of h = -(H1 + H1^T), computed from the stored curvature, on all sixteen components "
             "(fourteen nonzero), with or without an antisymmetric part; Omega at first order is "
             "grad ^ S(a) - (a.grad) A", ok)
    return ok


def divergence_terms(H1, G1, om1):
    """the three terms grad-dot . H1(G1-dot(C)), G1(C) . w, C . (Omega1(d_a) . G1(a)) at the point, for C on
    the frame; w = d_a . Omega1(a)."""
    om1v = [gtg.m_val(o) for o in om1]
    w = {}
    for a in range(D):
        w = gtg.m_add(w, gtg.inner_vb(REC[a], om1v[a], S))
    acc = {}
    for a in range(D):
        ga = {(k,): ETA[a] * G1[k][a].v for k in range(D) if G1[k][a].v}
        acc = gtg.m_add(acc, gtg.bdot(om1v[a], ga, S))
    terms = []
    for c in range(D):
        A = sum(G1[j][c].d(mu).v * H1[mu][j].v for mu in range(D) for j in range(D))
        gc = {(k,): G1[k][c].v for k in range(D) if G1[k][c].v}
        terms.append((A, gtg.vdot(gc, w, S), gtg.vdot(E[c], acc, S)))
    return terms


def check_quadratic_part_is_symmetric_and_its_divergence_off_solutions():
    premise(R2_ID)
    ok = True
    H1 = sample_field()
    G1, G2, fld = einstein_orders(H1)
    ok = ok and fld is not None and fld.torsion_free()
    # H1 is not symmetric and not a solution
    ok = ok and nonzero(msub(H1, transpose(H1))) == 12 and nonzero(G1) == 16
    # (ii) G2 is a symmetric map (the Ricci map of every field obeying the torsion equation is symmetric)
    ok = ok and symmetric(G2) and nonzero(G2) == 16
    # the flat divergence of the first-order part vanishes identically
    ok = ok and not any(d.v for d in flat_div(G1))
    # (iii) the flat divergence of G2 is minus the sum of the three terms, from div G = 0 at second order
    lhs = [d.v for d in flat_div(G2)]
    terms = divergence_terms(H1, G1, first_order_omega(fld))
    ok = ok and lhs == [-sum(tr) for tr in terms] and sum(1 for x in lhs if x) == 4
    ok = ok and sum(1 for tr in terms for x in tr if x) == 12
    # leaving out any one of the three terms fails, in each of the four directions
    failing = sum(1 for j in range(3) for tr, x in zip(terms, lhs) if x != -(sum(tr) - tr[j]))
    ok = ok and failing == 12
    GA.check("(ii), (iii) on a polynomial H1 that is neither symmetric nor a solution: G2[H1] is a "
             "symmetric map with sixteen nonzero entries, the flat divergence of G1 vanishes, and "
             "grad.(G2(C)) = -[grad-dot.H1(G1-dot(C)) + G1(C).w + C.(Omega1(d_a).G1(a))] in all four "
             "directions, each of the twelve terms nonzero", ok)
    return ok


def conservation_on(H1):
    """for a field H1: (the torsion equation holds, the whole jet of G1 vanishes, G2 is symmetric, the number
    of nonzero entries of H1 - H1^T, of G2, of the flat divergence of G2, and of the terms d_k G2[k][c])."""
    G1, G2, fld = einstein_orders(H1)
    return (fld is not None and fld.torsion_free(), not any(G1[k][c] for k in range(D) for c in range(D)),
            symmetric(G2), nonzero(msub(H1, transpose(H1))), nonzero(G2), sum(1 for d in flat_div(G2) if d.v),
            sum(1 for k in range(D) for c in range(D) if G2[k][c].d(k).v))


def check_quadratic_part_is_conserved_on_a_first_order_solution():
    premise(R2_ID)
    torsion, solves, sym, anti, entries, div, terms = conservation_on(sample_solution())
    # a solution of the first-order equation (the whole jet of G1 vanishes) that is not symmetric; G2 is
    # symmetric with sixteen nonzero entries, and its flat divergence vanishes in all four directions, the
    # sixteen terms d_k G2[k][c] being nonzero: the vanishing is a cancellation
    ok = torsion and solves and sym and anti == 12 and entries == 16 and div == 0 and terms == 16
    GA.check("(iii) on a first-order solution that is neither symmetric nor a plane wave (three null waves, "
             "a displacement and a rotation gauge), G1[H1] = 0 as a jet and the flat divergence of G2[H1] "
             "vanishes in all four directions, a cancellation of sixteen nonzero terms", ok)
    return ok


def check_quadratic_part_is_conserved_on_a_second_solution_with_other_data():
    premise(R2_ID)
    torsion, solves, sym, anti, entries, div, terms = conservation_on(sample_second_solution())
    ok = torsion and solves and sym and anti == 12 and entries == 16 and div == 0 and terms == 16
    GA.check("(iii) the same on a second first-order solution, with other profiles, another displacement "
             "and another rotation gauge", ok)
    return ok


def check_displacement_changes_the_quadratic_part_by_the_first_order_map_of_a_quadratic_field():
    premise(R1_ID)
    premise(WEYL_FLAT_ID)
    ok = True
    xi, xb = sample_displacement()
    # off solutions: G2[H1 - xi_] = G2[H1] + (xi.grad) G1[H1] - G1[(xi.grad) H1 - xi_ H1 + xi_ xi_]
    H1 = sample_field()
    G1, G2, _ = einstein_orders(H1)
    G1p, G2p, fldp = einstein_orders(lowered(msub(H1, xb)))
    parts = [advect(xi, H1), mscal(-1, mmul(xb, H1)), mmul(xb, xb)]
    ok = ok and fldp is not None and fldp.torsion_free() and meq(G1p, G1)
    ok = ok and meq(G2p, msub(madd(G2, advect(xi, G1)), G1_of(msum(parts))))
    ok = ok and nonzero(advect(xi, G1)) == 16 and nonzero(G1_of(msum(parts))) == 16
    # leaving out any one of the three parts of the quadratic field changes every component
    wrong = sum(nonzero(msub(G2p, msub(madd(G2, advect(xi, G1)), G1_of(msum(parts, j))))) for j in range(len(parts)))
    ok = ok and wrong == 48
    # the displaced flat field, H1 = -xi_: a first-order solution with G2 = -G1[xi_ xi_], which is not zero
    G1f, G2f, fldf = einstein_orders(lowered(mscal(-1, xb)))
    ok = ok and fldf is not None and fldf.torsion_free() and not nonzero(G1f)
    ok = ok and meq(G2f, mscal(-1, G1_of(mmul(xb, xb)))) and nonzero(G2f) == 16
    # on a solution: the change is G1[X], X = -(xi.grad) H1 + xi_ H1 - xi_ xi_, and it does not vanish
    Hfull = sample_solution()
    Hs = lowered(Hfull)
    G1s, G2s, _ = einstein_orders(Hs)
    G1t, G2t, _ = einstein_orders(msub(Hs, xb))
    Xq = mscal(-1, msum([advect(xi, Hfull), mscal(-1, mmul(xb, Hfull)), mmul(xb, xb)]))
    change = msub(G2t, G2s)
    ok = ok and nonzero(G1s) + nonzero(G1t) == 0
    ok = ok and meq(change, G1_of(Xq)) and nonzero(change) == 16
    GA.check("(iv) under the displacement x -> x + eps xi, H1 -> H1 - xi_ and G2 changes by "
             "(xi.grad) G1[H1] - G1[(xi.grad) H1 - xi_ H1 + xi_ xi_], exactly, off solutions; on a solution "
             "the change is G1[X] with X = -(xi.grad) H1 + xi_ H1 - xi_ xi_, nonzero in all sixteen entries; "
             "the displaced flat field H1 = -xi_ has G1 = 0 and G2 = -G1[xi_ xi_], not zero: G2 is not invariant", ok)
    return ok


def check_rotation_gauge_and_parametrisation_change_the_quadratic_part_the_same_way():
    premise(R1_ID)
    premise(WEYL_FLAT_ID)
    ok = True
    be = sample_rotation()
    # off solutions: H1 -> H1 + beta, G2 -> G2 - G1[H1 beta + 1/2 beta beta] + G1[H1] beta - beta G1[H1]
    H1 = sample_field_low()
    G1, G2, _ = einstein_orders(H1)
    G1r, G2r, fldr = einstein_orders(madd(H1, be))
    parts = [mmul(H1, be), mscal(F(1, 2), mmul(be, be))]
    turn = msub(mmul(G1, be), mmul(be, G1))
    ok = ok and fldr is not None and fldr.torsion_free() and meq(G1r, G1)
    ok = ok and meq(G2r, madd(msub(G2, G1_of(msum(parts))), turn)) and nonzero(turn) == 16
    # leaving out either part of the quadratic field changes every component, and so does leaving out the
    # turning of G1
    wrong = sum(nonzero(msub(G2r, madd(msub(G2, G1_of(msum(parts, j))), turn))) for j in range(len(parts)))
    ok = ok and wrong == 32 and nonzero(msub(G2r, msub(G2, G1_of(msum(parts))))) == 16
    # on a solution the change is G1[X], X = -(H1 beta + 1/2 beta beta), nonzero
    Hs = sample_solution_low()
    G1s, G2s, _ = einstein_orders(Hs)
    G1t, G2t, _ = einstein_orders(madd(Hs, be))
    Xs = mscal(-1, madd(mmul(Hs, be), mscal(F(1, 2), mmul(be, be))))
    change = msub(G2t, G2s)
    ok = ok and nonzero(G1s) + nonzero(G1t) == 0 and meq(change, G1_of(Xs)) and nonzero(change) == 16
    # a change of the second-order parametrisation, hb = id + eps H1 + eps^2 q: G2 -> G2 + G1[q]
    q = sample_second_order()
    _, G2q, _ = einstein_orders(Hs, q)
    ok = ok and meq(G2q, madd(G2s, G1_of(q))) and nonzero(G1_of(q)) == 16
    GA.check("(iv) under the rotation gauge change with rotor exp(eps B/2), H1 -> H1 + beta, beta(a) = a.B, "
             "and G2 changes by -G1[H1 beta + beta beta/2] + G1 beta - beta G1, exactly, off solutions; on a "
             "solution the change is G1[X], nonzero; adding eps^2 q to hb adds G1[q]", ok)
    return ok


def check_first_order_einstein_map_is_the_divergence_of_a_bivector():
    premise(WEYL_FLAT_ID)
    premise(R1_ID)
    ok, pairs, cases, nonvanishing, null_null = True, 0, 0, 0, 0
    n, nb = vec(NV), vec(NB)
    # both identities are linear in the symmetric map and quadratic in the momentum, so their truth on the
    # ten unit symmetric maps and the ten momenta e_i, e_i + e_j is their truth for all maps and momenta
    for M in sym_unit_maps():
        for p in polarising_momenta():
            Gp = einstein_symbol(M, p)
            tau = sum(M[k][k] for k in range(D))
            hp = apply_map(M, p)
            for c in range(D):
                a = E[c]
                # the symbol of W_a[h] = 1/2 (grad ^ h(a) - a ^ d + a ^ grad tau)
                W = scal(F(1, 2), add(wedge(p, apply_map(M, a)), GA.neg(wedge(a, hp)), scal(tau, wedge(a, p))))
                div = vdotB(p, W)
                want = {(k,): Gp[k][c] for k in range(D) if Gp[k][c]}
                ok = ok and GA.eq(div, want)
                # the divergence of a divergence of a bivector vanishes, and n . W is tangent to the null plane
                ok = ok and not dot(p, div) and not dot(n, vdotB(n, W))
                cases += 1
                nonvanishing += 0 if GA.is_zero(div) else 1
            # the null-null component is intrinsic to the null plane: with p = 1/2 (n.p) nbar + 1/2 (nbar.p) n
            # + p_T, n.G_p[h](n) = 1/2 [ Q(p_T) n.h(n) + (n.p)^2 (tr h - nbar.h(n)) - 2 (n.p) p_T.h(n) ]
            np_, nbp = dot(n, p), dot(nb, p)
            pT = sub(p, add(scal(F(1, 2) * np_, nb), scal(F(1, 2) * nbp, n)))
            ok = ok and not dot(pT, n) and not dot(pT, nb)
            hn = apply_map(M, n)
            lhs = dot(n, apply_map(Gp, n))
            rhs = F(1, 2) * (dot(pT, pT) * dot(n, hn) + np_ ** 2 * (tau - dot(nb, hn)) - 2 * np_ * dot(pT, hn))
            ok = ok and lhs == rhs
            null_null += 1 if lhs else 0
            pairs += 1
    ok = ok and pairs == 100 and cases == 400 and nonvanishing == 192 and null_null == 41
    GA.check("(v) the stored first-order Einstein map is the divergence of the bivector "
             "W_a[h] = 1/2 (grad ^ h(a) - a ^ d + a ^ grad tau), and n.E[h](n) contains only derivatives along "
             "the null plane: both identities, in symbols, on the ten unit symmetric maps and the ten momenta "
             "e_i, e_i + e_j, which fixes them for all maps and momenta; n . W_a is tangent to the null plane", ok)
    return ok


def check_null_null_component_in_the_light_cone_gauge_is_the_square_of_the_shear():
    premise(R1_ID)
    ok, fields, negative = True, 0, 0
    for h in sample_light_cone_solutions():
        # the gauge, and a solution of the first-order equation
        ok = ok and not any(sum((h[k][a] * NV[a] for a in range(D)), jz()) for k in range(D))
        ok = ok and not nonzero(first_order_einstein(h))
        # shear sigma = 1/2 d_n h^TT and expansion theta = 1/2 d_n tr h of the generators (the first-order result)
        hp, hx = pairm(h, EPSP) * F(1, 2), pairm(h, EPSX) * F(1, 2)
        sig2 = ((dn(hp) * dn(hp) + dn(hx) * dn(hx)) * F(1, 2)).v
        theta = (dn(mtrace(h)) * F(1, 2)).v
        d2 = dn(dn(pairm(h, h))).v
        ok = ok and sig2 == abs(sig2) and bool(sig2) and bool(theta) and bool(d2)
        H1 = mscal(F(-1, 2), h)
        sq = mmul(H1, H1)
        # hb = id + eps H1 + eps^2 r H1 H1: r = 0 is hb = id + eps H1, r = 1 is hb^{-1} = id - eps H1,
        # r = 1/2 is hb = exp(eps H1). The coefficient of d_n^2 <h, h> is 1/8 - r/4.
        vals = []
        for r, coef in ((F(0), F(1, 8)), (F(1), F(-1, 8)), (F(1, 2), F(0))):
            G1, G2, fld = einstein_orders(H1, mscal(r, sq))
            ok = ok and fld is not None and not nonzero(G1)
            vals.append(nn(G2).v)
            ok = ok and vals[-1] == sig2 + F(1, 2) * theta * theta + coef * d2
        ok = ok and len(set(vals)) == 3
        negative += sum(1 for v in vals if v != abs(v))
        fields += 1
    ok = ok and fields == 2 and negative == 2
    GA.check("(vi) on two solutions in the gauge h(n) = 0 (four null waves and a displacement that gives the "
             "generators an expansion), n.G2(n) = <sigma, sigma> + theta^2/2 + (1/8 - r/4) d_n^2 <h, h> for "
             "hb = id + eps H1 + eps^2 r H1 H1, r = 0, 1, 1/2: equal to <sigma, sigma> + theta^2/2 at the "
             "point only for the exponential parametrisation, and negative at the point in two of the six cases", ok)
    return ok


def check_null_null_identity_holds_in_the_light_cone_gauge_off_solutions():
    premise(R1_ID)
    ok = True
    h = light_cone_non_solution()
    # the gauge h(n) = 0, and not a solution of the first-order equation
    ok = ok and not any(sum((h[k][a] * NV[a] for a in range(D)), jz()) for k in range(D))
    ok = ok and nonzero(first_order_einstein(h)) == 16
    hp, hx = pairm(h, EPSP) * F(1, 2), pairm(h, EPSX) * F(1, 2)
    sig2 = ((dn(hp) * dn(hp) + dn(hx) * dn(hx)) * F(1, 2)).v
    theta = (dn(mtrace(h)) * F(1, 2)).v
    d2 = dn(dn(pairm(h, h))).v
    ok = ok and bool(sig2) and bool(theta) and bool(d2)
    H1 = mscal(F(-1, 2), h)
    vals = []
    for r, coef in ((F(0), F(1, 8)), (F(1), F(-1, 8)), (F(1, 2), F(0))):
        G1, G2, fld = einstein_orders(H1, mscal(r, mmul(H1, H1)))
        ok = ok and fld is not None and nonzero(G1) == 16
        vals.append(nn(G2).v)
        ok = ok and vals[-1] == sig2 + F(1, 2) * theta * theta + coef * d2
    ok = ok and len(set(vals)) == 3
    GA.check("(vi) the identity n.G2(n) = <sigma, sigma> + theta^2/2 + (1/8 - r/4) d_n^2 <h, h> holds for "
             "r = 0, 1, 1/2 on a polynomial field in the gauge h(n) = 0 that is not a first-order solution", ok)
    return ok


def check_plane_wave_in_the_kerr_schild_gauge_has_no_quadratic_part():
    premise(R1_ID)
    premise(WEYL_FLAT_ID)
    ok = True
    Fm, HKS, xi, trw = plane_wave_two_gauges(False)
    H = second_order(HKS)
    G1, G2, fld = einstein_orders(H)
    # the Kerr-Schild map H1(a) = 1/2 W (a.l) l: its square vanishes, it is a first-order solution (the whole
    # jet of G1 vanishes) and its quadratic part vanishes identically
    ok = ok and fld is not None and fld.torsion_free() and nonzero(H) == 4 and not nonzero(mmul(H, H))
    ok = ok and not any(x for row in G1 for x in row) and not any(x for row in G2 for x in row)
    # the same wave in the transverse trace-free gauge, h = F: a first-order solution with G2 not zero
    HTT = mscal(F(-1, 2), Fm)
    G1t, G2t, _ = einstein_orders(second_order(HTT))
    ok = ok and not nonzero(G1t) and nonzero(G2t) == 4
    # the two differ by the displacement xi and the rotation beta = antisymmetric part of xi_:
    # H1KS = H1TT - xi_ + beta = H1TT - 1/2 (xi_ + xi_^T)
    xb = grad_map(xi)
    be = mscal(F(1, 2), msub(xb, transpose(xb)))
    ok = ok and jets_equal(H, second_order(madd(msub(HTT, xb), be))) and nonzero(be) == 8
    # and the quadratic parts by G1[X], X = X_xi[H1TT] + X_B[H1TT - xi_], as clause (iv) says
    Xxi = mscal(-1, msum([advect(xi, HTT), mscal(-1, mmul(xb, HTT)), mmul(xb, xb)]))
    Hd = msub(HTT, xb)
    XB = mscal(-1, madd(mmul(Hd, be), mscal(F(1, 2), mmul(be, be))))
    ok = ok and meq(msub(G2, G2t), G1_of(madd(Xxi, XB)))
    # xi grows quadratically across the plane: it has nonzero second derivatives in the transverse labels
    ok = ok and sum(1 for k in range(D) for i in TRANSVERSE for j in TRANSVERSE if xi[k].d(i).d(j).v) == 8
    # with a trace the Kerr-Schild field is not a solution, G1 = (tr w) (a.l) l, and G2 still vanishes
    _, HKSt, _, trw = plane_wave_two_gauges(True)
    G1n, G2n, fldn = einstein_orders(second_order(HKSt))
    ok = ok and fldn is not None and meq(G1n, mscal(trw, outer_map(ELL, ELL))) and nonzero(G1n) == 4
    ok = ok and not any(x for row in G2n for x in row)
    GA.check("Reading: the plane wave in the Kerr-Schild gauge, H1(a) = 1/2 W (a.l) l, W = -y.w(y), has "
             "H1 H1 = 0, first-order part (tr w)(a.l) l and no quadratic part; the same wave in the transverse "
             "trace-free gauge has G2 != 0; the two differ by a displacement with nonzero second transverse "
             "derivatives and a rotation, and their quadratic parts by G1[X] with the X of clause (iv)", ok)
    return ok


def wave_invariants(h):
    """<h', h'> and <h, h>'' at the point for a field of the phase nbar.x: d_n = (n.nbar) d/dphase = 2 d/dphase."""
    hprime = [[dn(h[k][a]) * F(1, 2) for a in range(D)] for k in range(D)]
    return pairm(hprime, hprime).v, dn(dn(pairm(h, h))).v * F(1, 4)


def check_one_plane_wave_has_the_quadratic_part_along_its_momentum():
    premise(R1_ID)
    ok, count = True, 0
    kk = outer_map(NB, NB)                       # a -> (a.k) k with k = nbar, the gradient of the phase
    # the two sides are quadratic forms in the 2-jets (f+, f+', f+'', fx, fx', fx'') of the two profiles;
    # equality on the six unit jets and the fifteen sums of two of them is equality of the forms
    for jet in quadratic_form_arguments():
        h = plane_wave(jet)
        H1 = mscal(F(-1, 2), h)
        G1, G2, fld = einstein_orders(H1, mscal(F(1, 2), mmul(H1, H1)))
        hp2, _ = wave_invariants(h)
        ok = ok and fld is not None and not nonzero(G1) and meq(G2, mscal(F(1, 4) * hp2, kk))
        count += 1
    ok = ok and count == 21
    # the three parametrisations on a generic jet: 1/4 (<h', h'> + (1/2 - r) <h, h>'') (a.k) k
    h = plane_wave(GENERIC_JET)
    H1 = mscal(F(-1, 2), h)
    hp2, hh2 = wave_invariants(h)
    ok = ok and bool(hp2) and bool(hh2)
    for r, coef in ((F(0), F(1, 2)), (F(1), F(-1, 2)), (F(1, 2), F(0))):
        G1, G2, fld = einstein_orders(H1, mscal(r, mmul(H1, H1)))
        ok = ok and meq(G2, mscal(F(1, 4) * (hp2 + coef * hh2), kk)) and nonzero(G2) == 4
    GA.check("(vii) for one plane wave h = f+(k.x) eps+ + fx(k.x) epsx, k = nbar, the whole of G2 in the "
             "exponential parametrisation is 1/4 <h', h'> (a.k) k (equality of two quadratic forms on six "
             "variables, on 21 arguments); in the parametrisations r = 0 and r = 1 it is "
             "1/4 (<h', h'> + (1/2 - r) <h, h>'') (a.k) k", ok)
    return ok


def check_dust_falling_in_its_own_field_is_balanced_by_the_quadratic_part():
    premise(R2_ID)
    ok = True
    H1, T1, T2, v1 = sample_dust()
    G1, G2, fld = einstein_orders(H1)
    ok = ok and fld is not None and fld.torsion_free()
    # first order: G1[H1] = -kappa T1, the stored equation with kappa in place of 8 pi G
    ok = ok and jets_equal(G1, mscal(-KAPPA, T1))
    ok = ok and nonzero(G1) == 1
    # the dust obeys Newton's law: d_t v1 = -Omega1(e_0) . e_0, from the field's own rotation gauge field
    acc = gtg.m_neg(gtg.bdot(first_order_omega(fld)[0], E[0], S))
    dv = [v1[k].d(0).v for k in SPATIAL]
    ok = ok and dv == [acc.get((k,), jz()).v for k in SPATIAL] and all(dv)
    # second order: the flat divergence of the matter's stress is not zero (the force), and
    # grad . ((T2 + G2/kappa)(C)) = 0; the force being nonzero, no other constant in front of G2 balances
    dT, dG = [d.v for d in flat_div(T2)], [d.v for d in flat_div(G2)]
    ok = ok and sum(1 for x in dT if x) == 3 and not any(a * KAPPA + b for a, b in zip(dT, dG))
    # the same after a displacement and a rotation gauge change, which make H1 not symmetric:
    # T2 -> T2 + (xi.grad) T1 + T1 beta - beta T1
    xi, xb, be = sample_dust_gauge()
    Hp = madd(msub(H1, xb), be)
    Tp = madd(madd(T2, advect(xi, T1)), msub(mmul(T1, be), mmul(be, T1)))
    G1p, G2p, fldp = einstein_orders(Hp)
    ok = ok and fldp is not None and nonzero(msub(Hp, transpose(Hp))) == 12
    ok = ok and jets_equal(G1p, mscal(-KAPPA, T1))
    dT, dG = [d.v for d in flat_div(Tp)], [d.v for d in flat_div(G2p)]
    ok = ok and sum(1 for x in dT if x) == 4 and not any(a * KAPPA + b for a, b in zip(dT, dG))
    GA.check("(viii) dust at rest in its own first-order field, moved by the geodesic and continuity "
             "equations: the flat divergence of its second-order stress is nonzero (the force) and "
             "grad.((T2 + G2/kappa)(C)) = 0 exactly, also after a displacement and a rotation gauge change "
             "(H1 not symmetric, all four components of the force nonzero)", ok)
    return ok
