"""Scratch engine: the Einstein map of hb = id + eps H1 + eps^2 H2 to second order in eps, exactly.

eps is carried as a truncated polynomial (class Eps, degree <= 2) in the coefficients of gtg jets.
A linear map M of the vectors is a 4 x 4 matrix Mm with M(e_a) = sum_mu Mm[mu][a] e_mu (jets).
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/zero-divisors/lib")
import GA
import gtg

D = 4
S = GA.sig(1, 3)
ETA = [1, -1, -1, -1]
NE = 3                      # eps^0, eps^1, eps^2


class Eps(object):
    """a0 + a1 eps + a2 eps^2 modulo eps^3, exact: the ring in which the expansion to second order is carried."""
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

    def __repr__(self):
        return "Eps%s" % (tuple(str(x) for x in self.a),)


EPS = Eps((F(0), F(1), F(0)))
EPS2 = Eps((F(0), F(0), F(1)))


def part(x, j):
    """the eps^j coefficient of a number, an Eps, or a jet with Eps coefficients (returns a rational jet)."""
    if isinstance(x, gtg.Jet):
        cc = {}
        for e, c in x.c.items():
            v = c.a[j] if isinstance(c, Eps) else (c if j == 0 else 0)
            if v:
                cc[e] = F(v)
        return gtg.Jet(c=cc, nv=x.nv, order=x.order)
    if isinstance(x, Eps):
        return x.a[j]
    return x if j == 0 else F(0)


def labels(x0, order):
    return [gtg.Jet.var(i, x0[i], D, order) for i in range(D)]


def mat_id():
    return [[F(1) if m == a else F(0) for a in range(D)] for m in range(D)]


def omega_from_coframe(TH, HJ):
    """om[c] = Omega(hb(gamma_c)) from the torsion equation, explicitly:
    om[a].gamma_b - om[b].gamma_a = C_ab := -sum Hi[mu][a] Hi[nu][b] (d_mu g_nu - d_nu g_mu),
    w_abk = (om[a].gamma_b).gamma_k = 1/2 (c_abk - c_bka + c_kab), om[a] = -sum_{b<k} eta_b eta_k w_abk gamma_b gamma_k."""
    z = gtg.Jet.const(0, D)
    # dg[mu][nu][k]: component along gamma_k of d_mu g_nu - d_nu g_mu
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
                w = (c[a][b][k] - c[b][k][a] + c[k][a][b]) * F(1, 2)
                t = w * (-ETA[b] * ETA[k])
                if t:
                    o[(b, k)] = t
        om.append(o)
    return om


def field_of_hb(Hm):
    """the gravitational field with hb(gamma_a) = sum_mu Hm[mu][a] e_mu (jets), Omega from the torsion equation."""
    HJ = [[gtg._jc(Hm[mu][a], D) for a in range(D)] for mu in range(D)]
    TH = gtg.mat_inv(HJ)                 # TH[a][mu]
    om = omega_from_coframe(TH, HJ)
    return gtg.Field(TH, om=om, sq=S)


def einstein_jets(fld):
    """Gm[k][c]: component along gamma_k of G(gamma_c), as jets; and the Ricci scalar."""
    Rj = fld.curvature_jet()

    def Rop(B):
        out = {}
        for (a, b), co in B.items():
            out = gtg.m_add(out, gtg.m_scal(co, Rj[(a, b)]))
        return out

    E = [GA.gen(i) for i in range(D)]
    Ric = [gtg.ricci(Rop, E[c], S) for c in range(D)]
    z = gtg.Jet.const(0, D)
    sc = z
    for c in range(D):
        sc = sc + Ric[c].get((c,), z)
    Gm = [[Ric[c].get((k,), z) - (sc * F(1, 2) if k == c else z) for c in range(D)] for k in range(D)]
    return Gm, sc, Rop


def hb_series(H1, H2=None):
    """matrix of id + eps H1 + eps^2 H2."""
    out = [[None] * D for _ in range(D)]
    for m in range(D):
        for a in range(D):
            x = gtg.Jet.const(1 if m == a else 0, D)
            x = x + H1[m][a] * EPS
            if H2 is not None:
                x = x + H2[m][a] * EPS2
            out[m][a] = x
    return out


def einstein_orders(H1, H2=None):
    """(G1, G2tot, fld): eps and eps^2 coefficients of the Einstein map matrix, rational jets."""
    fld = field_of_hb(hb_series(H1, H2))
    Gm, sc, Rop = einstein_jets(fld)
    G1 = [[part(Gm[k][c], 1) for c in range(D)] for k in range(D)]
    G2 = [[part(Gm[k][c], 2) for c in range(D)] for k in range(D)]
    G0 = [[part(Gm[k][c], 0) for c in range(D)] for k in range(D)]
    assert all(not G0[k][c] for k in range(D) for c in range(D))
    return G1, G2, fld


# ---- operations on matrices of rational jets -------------------------------------------------

def jz():
    return gtg.Jet.const(0, D)


def mmul(A, B):
    return [[sum((A[m][k] * B[k][a] for k in range(D)), jz()) for a in range(D)] for m in range(D)]


def madd(A, B, c=1):
    return [[A[m][a] + B[m][a] * c for a in range(D)] for m in range(D)]


def mscal(c, A):
    return [[A[m][a] * c for a in range(D)] for m in range(D)]


def transpose(A):
    """adjoint for the flat product: (A^T)[mu][a] = eta_mu eta_a A[a][mu]."""
    return [[A[a][m] * (ETA[m] * ETA[a]) for a in range(D)] for m in range(D)]


def mtrace(A):
    return sum((A[m][m] for m in range(D)), jz())


def mval(A):
    return [[gtg._val(A[m][a]) for a in range(D)] for m in range(D)]


def first_order_einstein(h):
    """the stored operator E[h](a) = 1/2 (grad^2 h(a) + (a.grad) grad tau - (a.grad) d - grad (a.d))
    - 1/2 a (grad^2 tau - grad.d) for a symmetric map field h (matrix of jets); d = h-dot(grad-dot)."""
    def box(f):
        return sum((f.d(m).d(m) * ETA[m] for m in range(D)), jz())
    tau = mtrace(h)
    # d = sum_mu d_mu h(e^mu): component k: sum_mu eta_mu d_mu h[k][mu]
    dv = [sum((h[k][m].d(m) * ETA[m] for m in range(D)), jz()) for k in range(D)]
    divd = sum((dv[k].d(k) for k in range(D)), jz())
    out = [[None] * D for _ in range(D)]
    for k in range(D):
        for a in range(D):
            t = box(h[k][a])
            t = t + tau.d(a).d(k) * ETA[k]                 # (a.grad) grad tau, component k (grad^k = eta_k d_k)
            t = t - dv[k].d(a)                             # (e_a.grad) d
            # grad (e_a . d): e_a.d = eta_a dv[a]
            t = t - dv[a].d(k) * (ETA[a] * ETA[k])
            t = t * F(1, 2)
            if k == a:
                t = t - (box(tau) - divd) * F(1, 2)
            out[k][a] = t
    return out


def G1_of(H1):
    """G1[H1] = E[h], h = -(H1 + H1^T)."""
    return first_order_einstein(mscal(-1, madd(H1, transpose(H1))))


def flat_div(M):
    """C -> grad . (M(C)): list over c of sum_k d_k M[k][c]."""
    return [sum((M[k][c].d(k) for k in range(D)), jz()) for c in range(D)]
