"""dark-energy.vacuum-region-registration-condition: exact GTG checks in Cl(2,4) of clauses (i) and (ii),
ported from legacy verify_T10.py (prop:w) and recast with gauge fields. Clause (iii) is a registration
(a conditional stance and a record of the 2026 data) with no computable content beyond (i).

Fields (synchronous diagonal, GTG sign, curvature and Schouten map computed from Omega): de Sitter
(a, adot, addot) = (2, 2H, 2H^2), H = 1/2, 3/2; the matter-dominated field a = tau^(2/3) at tau = 8 and 27.
kappa stands for 8 pi G (a rational stand-in: only its cancellation matters).
  (i) The tractor gauge field preserves the metric, V . (Omega_T(a) x V) = 0 on sample tractors, and I is
      parallel with constant slots, so Q(I) = Lambda/3 cannot vary. The store-sign field equation
      calR(a) + kappa T(a) = (Lambda_0 + (kappa/2) tr T) a holds for the de Sitter field both as the vacuum
      with Lambda_0 = Lambda (T = 0) and with Lambda moved into T^Lambda(a) = (Lambda/kappa) a (Lambda_0 = 0);
      rho = e0 . T(e0) = Lambda/kappa > 0 and T(e_i) = -p e_i gives p = -rho: w = -1.
  (ii) I_g = ninf + (J/4) n0 with J = tr P (P computed from the field): Q(I_g) = J/2 = R/12 on every field;
      on de Sitter R = 4 Lambda and Q(I_g) = Lambda/3, I_g parallel; on the matter field the mu-slot of
      Omega_T(a) x I_g = (J/4) A - P(A) is nonzero (I_g not parallel) and R differs between tau = 8 and 27.
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

KAPPA = F(5, 2)
TRACTORS = [tractor(F(2), vec4([1, 0, 3, -1]), F(-7)), tractor(F(-1, 3), vec4([0, 4, 1, 1]), F(5, 2))]


def de_sitter(H):
    return Synchronous([(F(2), 2 * H, 2 * H * H)] * 3)


def matter(base):
    tau, data = kasner((F(2, 3), F(2, 3), F(2, 3)), base)
    return Synchronous(data)


def J_of(f):
    return sum(sp(mul(ER[m], f.schouten(E[m]))) for m in range(4))


def check_norm_constant_and_w_minus_one():
    premise("dark-energy.imported-frozen-point-geometry")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    for H in (F(1, 2), F(3, 2)):
        f = de_sitter(H)
        lam = f.scalar() / 4
        ok = ok and lam == 3 * H * H
        I = tractor(F(1), {}, lam / 6)
        for m in range(4):
            OT = f.omega_T(m, f.schouten)
            ok = ok and GA.is_zero(comm(OT, I))
            ok = ok and all(dot(V, comm(OT, V)) == 0 for V in TRACTORS + [I])
        T = lambda a: GA.scal(lam / KAPPA, a)
        trT = sum(sp(mul(ER[m], T(E[m]))) for m in range(4))
        for m in range(4):
            a = E[m]
            ok = ok and GA.eq(f.ricci(a), GA.scal(lam, a))                                     # vacuum form
            ok = ok and GA.eq(GA.add(f.ricci(a), GA.scal(KAPPA, T(a))), GA.scal(KAPPA * trT / 2, a))
        rho = dot(E[0], T(E[0]))
        p = dot(E[1], T(E[1]))                       # T(e1) = -p e1 and e1.e1 = -1
        ok = ok and rho == lam / KAPPA and rho > 0 and p == -rho and p / rho == -1
    GA.check("Q(I) constant; T^Lambda = (Lambda/8 pi G) a with w = -1", ok)
    assert ok


def check_general_scale_tractor_norm_is_r_over_twelve():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    fields = [de_sitter(F(1, 2)), de_sitter(F(3, 2)), matter(2), matter(3)]
    for f in fields:
        J = J_of(f)
        Ig = tractor(F(1), {}, J / 4)
        ok = ok and dot(Ig, Ig) == J / 2 and J / 2 == f.scalar() / 12
    for f in fields[:2]:
        lam = f.scalar() / 4
        Ig = tractor(F(1), {}, J_of(f) / 4)
        ok = ok and dot(Ig, Ig) == lam / 3 and all(GA.is_zero(comm(f.omega_T(m, f.schouten), Ig)) for m in range(4))
    m8, m27 = fields[2], fields[3]
    for f in (m8, m27):
        J = J_of(f)
        Ig = tractor(F(1), {}, J / 4)
        mu_parts = []
        for m in range(4):
            A = f.hb_inv(m)
            d = comm(f.omega_T(m, f.schouten), Ig)
            mu = {b: c for b, c in d.items() if len(b) == 1 and b[0] < 4}
            ok = ok and GA.eq(mu, GA.sub(GA.scal(J / 4, A), f.schouten(A)))
            mu_parts.append(mu)
        ok = ok and not all(GA.is_zero(x) for x in mu_parts)
    ok = ok and m8.scalar() != m27.scalar() and m8.scalar() != 0
    # hand value: matter a = tau^(2/3) at tau = 8: store-sign R = 6(addot/a + adot^2/a^2) = 4/(3 tau^2) = 1/48
    ok = ok and m8.scalar() == F(1, 48)
    GA.check("Q(I_g) = R/12; parallel only on the Einstein field; R varies on matter", ok)
    assert ok
