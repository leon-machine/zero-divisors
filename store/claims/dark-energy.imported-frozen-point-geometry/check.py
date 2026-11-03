"""dark-energy.imported-frozen-point-geometry: exact GTG checks in Cl(2,4) of the imported Fact's
computable content, ported from legacy verify_T10.py (fact:frozen) and recast with gauge fields.

Fields (synchronous diagonal, GTG sign, curvature and Schouten map computed from Omega): the Kasner
vacuum (2/3, 2/3, -1/3) at tau = 8, the de Sitter field (a, adot, addot) = (2, 2H, 2H^2) with H = 1/2,
3/2 (Lambda = 3H^2), and the non-vacuum matter field (2/3, 2/3, 2/3) at tau = 8.
  (1) The tractor gauge field Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)) acts on
      V = sigma ninf + mu + rho n0 by its algebraic part with slots (-mu.A, A rho - P(A) sigma, P(A).mu),
      A = hb^{-1}(a), nothing outside the three slots, and V . (Omega_T(a) x V) = 0 (metric preserved);
      on the Einstein field P = (Lambda/6) id.
  (2) Vacuum iff the null scale tractor is parallel: Omega_T(a) x ninf = -P(A), zero for the Kasner vacuum
      and nonzero for the matter field; on the de Sitter field I = ninf + (Lambda/6) n0 is parallel and
      Q(I) = Lambda/3.
  (3) The stabiliser {B bivector : B x I = 0} of a non-null I has dimension 10, I-perp has signature (1,4)
      for Lambda > 0 and (2,3) for Lambda < 0, and the trace form tr(ad B ad C) is nondegenerate on it
      (reductive); for the null ninf the stabiliser also has dimension 10, but the four ninf ^ e_m span an
      abelian ideal on which the trace form vanishes (parabolic). The rotation: [I ^ u, I ^ v] = -Q(I) u ^ v
      for u, v in {I, ninf, n0}-perp, which is zero exactly at the null end.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

# ---------------------------------------------------------------------------
# GTG core (shared text, self-contained). Cl(2,4): generators e0 (+1), e1, e2, e3 (-1), e+ (+1), e- (-1);
# the spacetime algebra Cl(1,3) is the span of e0..e3. n0 = (e+ + e-)/2, ninf = e+ - e-, so
# Q(n0) = Q(ninf) = 0, n0 . ninf = 1; a tractor is sigma ninf + mu + rho n0.
# A synchronous diagonal gravitational field on flat spacetime: hb^{-1}(e0) = e0, hb^{-1}(e_i) = a_i e_i,
# hence hb(e_i) = e_i/a_i; its rotation-gauge field in the GTG sign (DICTIONARY C10) is Omega(e0) = 0,
# Omega(e_i) = -adot_i e0 ^ e_i, checked here through the torsion condition. Fields depend on the time
# coordinate only, so a.grad = (a . e^0) d/dtau. The field is given at one instant by the triples
# (a_i, adot_i, addot_i). Field strength (LDG sign) R(a ^ b) = a.grad Omega(b) - b.grad Omega(a)
# + Omega(a) x Omega(b); the store's curvature is calR(B) = -R(hb(B)) (DICTIONARY C5-C6).
# ---------------------------------------------------------------------------
S = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
ER = [GA.scal(F(1, S[i]), E[i]) for i in range(4)]            # reciprocal spacetime frame
N0 = GA.scal(F(1, 2), GA.add(E[4], E[5]))
NI = GA.sub(E[4], E[5])
PLANES = [(m, n) for m in range(4) for n in range(m + 1, 4)]


def mul(x, y):
    return GA.mul(x, y, S)


def comm(X, Y):
    return GA.scal(F(1, 2), GA.sub(mul(X, Y), mul(Y, X)))


def wedge(a, b):
    """Outer product of two vectors (= their commutator product)."""
    return comm(a, b)


def dot(a, b):
    return GA.dot(a, b, S)


def sp(x):
    return x.get((), F(0))


def grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def vec4(c):
    return GA.add(*[GA.scal(F(c[i]), E[i]) for i in range(4)])


def tractor(sig, mu, rho):
    return GA.add(GA.scal(sig, NI), mu, GA.scal(rho, N0))


class Synchronous(object):
    """hb^{-1}(e_i) = a_i e_i at one instant: data[i] = (a, adot, addot) for i = 1, 2, 3."""

    def __init__(self, data):
        self.d = {0: (F(1), F(0), F(0))}
        self.d.update({i + 1: tuple(F(v) for v in data[i]) for i in range(3)})

    def a(self, m):
        return self.d[m][0]

    def hb_inv(self, m):
        return GA.scal(self.d[m][0], E[m])

    def d_hb_inv(self, m):
        return GA.scal(self.d[m][1], E[m])

    def Omega(self, m):
        return {} if m == 0 else GA.scal(-self.d[m][1], wedge(E[0], E[m]))

    def d_Omega(self, m):
        return {} if m == 0 else GA.scal(-self.d[m][2], wedge(E[0], E[m]))

    def D_hb_inv(self, m, n):
        """D_{e_m} hb^{-1}(e_n) = e_m.grad hb^{-1}(e_n) + Omega(e_m) x hb^{-1}(e_n)."""
        deriv = self.d_hb_inv(n) if m == 0 else {}
        return GA.add(deriv, comm(self.Omega(m), self.hb_inv(n)))

    def torsion_free(self):
        return all(GA.eq(self.D_hb_inv(m, n), self.D_hb_inv(n, m)) for m in range(4) for n in range(4))

    def R_bg(self, m, n):
        """Background field strength R(e_m ^ e_n), LDG sign."""
        t1 = self.d_Omega(n) if m == 0 else {}
        t2 = self.d_Omega(m) if n == 0 else {}
        return GA.add(t1, GA.neg(t2), comm(self.Omega(m), self.Omega(n)))

    def calR(self, B):
        """Store-sign curvature on a physical bivector: -R(hb(B)), by linearity on e_m ^ e_n."""
        out = {}
        for m, n in PLANES:
            c = sp(mul(B, wedge(ER[n], ER[m])))                # coefficient of e_m ^ e_n in B
            if c:
                out = GA.add(out, GA.scal(-c / (self.a(m) * self.a(n)), self.R_bg(m, n)))
        return out

    def ricci(self, b):
        return GA.add(*[grade(comm(ER[m], self.calR(wedge(E[m], b))), 1) for m in range(4)])

    def scalar(self):
        return sum(sp(mul(ER[m], self.ricci(E[m]))) for m in range(4))

    def schouten(self, a):
        return GA.scal(F(1, 2), GA.sub(self.ricci(a), GA.scal(self.scalar() / 6, a)))

    def kretschmann(self):
        return 2 * sum(sp(mul(self.calR(wedge(E[m], E[n])), self.calR(wedge(ER[n], ER[m]))))
                       for m in range(4) for n in range(4))

    def ricci_sq(self):
        return sum(sp(mul(self.ricci(E[m]), self.ricci(ER[m]))) for m in range(4))

    def omega_T(self, m, P):
        """Tractor gauge field Omega_T(e_m) = Omega(e_m) - ninf ^ hb^{-1}(e_m) + n0 ^ P(hb^{-1}(e_m))."""
        A = self.hb_inv(m)
        return GA.add(self.Omega(m), GA.neg(wedge(NI, A)), wedge(N0, P(A)))


def _gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def kasner(p, base):
    """Kasner data a_i = tau^{p_i} at tau = base^d, d the lcm of the denominators of p (exact).
    Returns (tau, data) with data[i] = (a_i, adot_i, addot_i), adot = p a/tau, addot = p(p-1) a/tau^2."""
    d = 1
    for x in p:
        den = F(x).denominator
        d = d * den // _gcd(d, den)
    tau = F(base) ** d
    out = []
    for x in p:
        x = F(x)
        a = F(base) ** int(x * d)
        out.append((a, x * a / tau, x * (x - 1) * a / (tau * tau)))
    return tau, out

BIV = [wedge(E[i], E[j]) for i in range(6) for j in range(i + 1, 6)]
BLADES = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def coords(B):
    return [B.get(b, F(0)) for b in BLADES]


def fields():
    tau, data = kasner((F(2, 3), F(2, 3), F(-1, 3)), 2)
    vac = Synchronous(data)
    tau, data = kasner((F(2, 3), F(2, 3), F(2, 3)), 2)
    mat = Synchronous(data)
    ds = [(3 * H * H, Synchronous([(F(2), 2 * H, 2 * H * H)] * 3)) for H in (F(1, 2), F(3, 2))]
    return vac, mat, ds


def slots(V):
    return dot(V, N0), {b: c for b, c in V.items() if len(b) == 1 and b[0] < 4}, dot(V, NI)


def stabiliser(I):
    rows = [[comm(B, I).get((k,), F(0)) for B in BIV] for k in range(6)]
    return [GA.add(*[GA.scal(c, B) for c, B in zip(v, BIV)]) for v in GA.field_kernel(rows)]


def trace_form(basis):
    def ad(B):
        return [coords(comm(B, C)) for C in BIV]

    def tr(M1, M2):
        # matrices as lists of columns (images of the basis bivectors), in blade coordinates
        A = [[M1[j][i] for j in range(15)] for i in range(15)]
        Bm = [[M2[j][i] for j in range(15)] for i in range(15)]
        return sum(A[i][k] * Bm[k][i] for i in range(15) for k in range(15))
    ads = [ad(B) for B in basis]
    return [[tr(x, y) for y in ads] for x in ads]


# Sample tractors (sigma, mu, rho) acted on by the algebraic part of the tractor gauge field.
TRACTOR_SAMPLES = [(F(2), vec4([1, 0, 3, -1]), F(-7)), (F(-1, 3), vec4([0, 4, 1, 1]), F(5, 2))]


def check_tractor_gauge_field_reproduces_connection():
    premise("interior.imported-tractor-connection")
    vac, mat, ds = fields()
    ok = True
    samples = TRACTOR_SAMPLES
    for f in [vac, mat] + [x[1] for x in ds]:
        for m in range(4):
            A = f.hb_inv(m)
            alg = GA.sub(f.omega_T(m, f.schouten), f.Omega(m))
            for sig, mu, rho in samples:
                V = tractor(sig, mu, rho)
                dV = comm(alg, V)
                s1, m1, r1 = slots(dV)
                ok = ok and s1 == -dot(mu, A) and r1 == dot(f.schouten(A), mu)
                ok = ok and GA.eq(m1, GA.sub(GA.scal(rho, A), GA.scal(sig, f.schouten(A))))
                ok = ok and GA.eq(dV, tractor(s1, m1, r1))
                ok = ok and dot(V, comm(f.omega_T(m, f.schouten), V)) == 0
    for lam, f in ds:
        ok = ok and all(GA.eq(f.schouten(E[m]), GA.scal(lam / 6, E[m])) for m in range(4))
    GA.check("tractor gauge field reproduces the connection and preserves the metric", ok)
    assert ok


def check_vacuum_iff_null_scale_tractor_parallel():
    premise("interior.covariant-form-vacuum-equations")
    premise("interior.scale-tractor-leaves-cone")
    vac, mat, ds = fields()
    ok = True
    for m in range(4):
        ok = ok and GA.is_zero(comm(vac.omega_T(m, vac.schouten), NI))
        ok = ok and GA.eq(comm(mat.omega_T(m, mat.schouten), NI), GA.neg(mat.schouten(mat.hb_inv(m))))
    ok = ok and not all(GA.is_zero(comm(mat.omega_T(m, mat.schouten), NI)) for m in range(4))
    for lam, f in ds:
        I = tractor(F(1), {}, lam / 6)
        ok = ok and dot(I, I) == lam / 3
        ok = ok and all(GA.is_zero(comm(f.omega_T(m, f.schouten), I)) for m in range(4))
    ok = ok and ds[0][0] == F(3, 4)
    GA.check("vacuum iff ninf parallel; Einstein: I parallel with Q(I) = Lambda/3", ok)
    assert ok


def check_stabilisers_reductive_and_parabolic():
    premise("interior.non-null-stabilisers-section-they-act")
    premise("interior.stabiliser-rotates-parabolic-reductive")
    premise("interior.sign-fixed-internally")
    ok = True
    for lam, sig_exp in ((F(3, 4), (1, 4)), (F(-3, 2), (2, 3))):
        I = tractor(F(1), {}, lam / 6)
        st = stabiliser(I)
        ok = ok and len(st) == 10
        ok = ok and GA.field_rank(trace_form(st)) == 10
        ker = GA.field_kernel([[dot(I, E[k]) for k in range(6)]])
        G = [[sum(u[i] * v[i] * S[i] for i in range(6)) for v in ker] for u in ker]
        ok = ok and GA.congruence_signature(G)[:2] == sig_exp
        for u in E[:4]:
            for v in E[:4]:
                ok = ok and GA.eq(comm(wedge(I, u), wedge(I, v)), GA.scal(-dot(I, I), wedge(u, v)))
    st = stabiliser(NI)
    ok = ok and len(st) == 10
    tr = trace_form(st)
    ok = ok and GA.field_rank(tr) < 10
    trans = [wedge(NI, E[m]) for m in range(4)]
    ok = ok and all(GA.is_zero(comm(x, y)) for x in trans for y in trans)
    span = [coords(t) for t in trans]
    for B in st:
        for t in trans:
            ok = ok and GA.rank_of_vectors(span + [coords(comm(B, t))]) == 4
    tt = trace_form(trans)
    ok = ok and all(x == 0 for row in tt for x in row)
    GA.check("non-null stabiliser reductive of dimension 10; null one parabolic", ok)
    assert ok
