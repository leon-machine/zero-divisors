"""dark-energy.stelle-west-vector-frozen-point: exact GTG checks in Cl(2,4), ported from legacy
verify_T10.py (lem:sw) and recast with the gauge fields hb and Omega of a concrete Einstein field.

The Einstein field is de Sitter in synchronous (flat) slicing on flat spacetime: hb^{-1}(e_0) = e_0,
hb^{-1}(e_i) = a e_i with (a, adot, addot) = (A, H A, H^2 A) at an instant, Omega(e_i) = -adot e_0 ^ e_i
(GTG sign); its store-sign curvature is computed from Omega, and its Schouten map from that curvature.
Lambda = 3 H^2 with H rational (Lambda = 3/4, 12, 27/4); Lambda < 0 (no real flat-sliced field) is
checked algebraically at Lambda = -3/2, -6.
  (i) I = ninf + (Lambda/6) n0, X = n0, V = X - (<X,I>/Q(I)) I, W = V/Q(V): Q(X) = 0, <X,I> = 1,
      <V,I> = 0, Q(V) = -3/Lambda, slots V = (-3/Lambda, 0, 1/2), W = ninf - (Lambda/6) n0.
  (ii) For the field: calR(B) = (Lambda/3) B, P = (Lambda/6) id (Einstein); the tractor gauge field
      Omega_T(a) = Omega(a) - ninf ^ hb^{-1}(a) + n0 ^ P(hb^{-1}(a)) gives D_a X = D_a V = hb^{-1}(a)
      (the soldering form, the physical frame) and D_a I = 0 (I, X, V have constant slots); <e_a, I> = 0.
  (iii) Omega_T(a) = Omega(a) + hb^{-1}(a) ^ W, and on tractors without a mu-component Omega(a) acts as zero,
      so D_a = d_a + e_a ^ W there.
  (iv) [e_a ^ W, e_b ^ W] = -Q(W) e_a ^ e_b = (Lambda/3) e_a ^ e_b on the physical frame (both signs).
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

HS = [F(1, 2), F(2), F(3, 2)]
NEG = [F(-3, 2), F(-6)]
SAMPLE_TRACTORS = [tractor(F(3), {}, F(-2)), tractor(F(-1, 2), {}, F(5))]


def de_sitter(H, A=F(2)):
    return Synchronous([(A, H * A, H * H * A)] * 3)


def datum(lam):
    I = tractor(F(1), {}, lam / 6)
    X = N0
    V = GA.sub(X, GA.scal(dot(X, I) / dot(I, I), I))
    W = GA.scal(1 / dot(V, V), V)
    return I, X, V, W


def check_constraints_and_slots():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lam in [3 * H * H for H in HS] + NEG:
        I, X, V, W = datum(lam)
        ok = ok and dot(X, X) == 0 and dot(X, I) == 1 and dot(V, I) == 0 and dot(V, V) == -3 / lam
        ok = ok and GA.eq(V, tractor(-3 / lam, {}, F(1, 2)))
        ok = ok and GA.eq(W, GA.sub(NI, GA.scal(lam / 6, N0))) and dot(I, I) * dot(V, V) == -1
    # hand value: Lambda = 3/4: Q(V) = -4, V = -4 ninf + n0/2
    I, X, V, W = datum(F(3, 4))
    ok = ok and dot(V, V) == -4 and GA.eq(V, GA.add(GA.scal(-4, NI), GA.scal(F(1, 2), N0)))
    GA.check("Stelle-West vector: constraints and slots", ok)
    assert ok


def check_de_sitter_field_soldering_and_parallel_frozen_point():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for H in HS:
        f = de_sitter(H)
        lam = 3 * H * H
        ok = ok and f.torsion_free()
        for m, n in PLANES:
            ok = ok and GA.eq(f.calR(wedge(E[m], E[n])), GA.scal(lam / 3, wedge(E[m], E[n])))
        ok = ok and all(GA.eq(f.schouten(E[m]), GA.scal(lam / 6, E[m])) for m in range(4))
        I, X, V, W = datum(lam)
        for m in range(4):
            OT = f.omega_T(m, f.schouten)
            e_a = f.hb_inv(m)
            # the slots of I, X, V are constant, so D_a = Omega_T(a) x on them
            ok = ok and GA.is_zero(comm(OT, I))
            ok = ok and GA.eq(comm(OT, X), e_a) and GA.eq(comm(OT, V), e_a)
            ok = ok and dot(e_a, I) == 0
    # hand value: H = 1/2, A = 2: e_1 = hb^{-1}(e_1) = 2 e_1 = D_1 V
    f = de_sitter(F(1, 2))
    ok = ok and GA.eq(comm(f.omega_T(1, f.schouten), datum(F(3, 4))[2]), GA.scal(2, E[1]))
    GA.check("de Sitter field: D X = D V = soldering form, D I = 0", ok)
    assert ok


def check_gauge_field_is_omega_plus_frame_wedge_w():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for H in HS:
        f = de_sitter(H)
        lam = 3 * H * H
        I, X, V, W = datum(lam)
        for m in range(4):
            OT = f.omega_T(m, f.schouten)
            ok = ok and GA.eq(OT, GA.add(f.Omega(m), wedge(f.hb_inv(m), W)))
            ok = ok and GA.eq(OT, GA.add(f.Omega(m), wedge(f.hb_inv(m), GA.scal(1 / dot(V, V), V))))
            for T in SAMPLE_TRACTORS:
                ok = ok and GA.is_zero(comm(f.Omega(m), T))
                ok = ok and GA.eq(comm(OT, T), comm(wedge(f.hb_inv(m), W), T))
    GA.check("Omega_T(a) = Omega(a) + hb^{-1}(a) ^ W", ok)
    assert ok


def check_bracket_of_soldering_bivectors():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lam, f in [(3 * H * H, de_sitter(H)) for H in HS] + [(l, de_sitter(F(1))) for l in NEG]:
        I, X, V, W = datum(lam)
        for m in range(4):
            for n in range(4):
                ea, eb = f.hb_inv(m), f.hb_inv(n)
                lhs = comm(wedge(ea, W), wedge(eb, W))
                ok = ok and GA.eq(lhs, GA.scal(-dot(W, W), wedge(ea, eb)))
                ok = ok and GA.eq(lhs, GA.scal(lam / 3, wedge(ea, eb)))
    GA.check("[e_a ^ W, e_b ^ W] = (Lambda/3) e_a ^ e_b", ok)
    assert ok
