"""dark-energy.under-action-written-norm-parameter-laws: exact checks in Cl(2,4), ported from legacy
verify_T10.py (prop:parameter) and widened (three Lambda of both signs, the de Sitter field, the family).

I = ninf + (Lambda/6) n0, V = n0 - (3/Lambda) I; fluctuations are vector coordinates on e0..e3, e+, e-.
  (i) Lambda fixed: the linearised constraints on (dI, dV) have rank 3 (dimension 9) and the 15 bivectors
      act onto that space with rank 9. On the de Sitter field (hb, Omega) (a, adot, addot) = (2, 2H, 2H^2),
      Lambda read off its store-sign curvature (calR(a) = Lambda a) gives H^2 = (adot/a)^2 = Q(I) = Lambda/3,
      so N = M_P/H = M_P sqrt(3/Lambda) is fixed by Lambda.
  (ii) N^2 = 3 M_P^2/Lambda has d(N^2)/dLambda = -3 M_P^2/Lambda^2 != 0 (GA.RF derivative); the rescaling
      I -> s I multiplies Q(I) by s^2 (Lambda -> s^2 Lambda) and N^2 by 1/s^2 (N -> N/s).
  (iii) Lambda varying: the linearised constraints 2 I.dI = dLambda/3, V.dI + I.dV = 0,
      2 V.dV = (3/Lambda^2) dLambda on 13 components have rank 3 (dimension 10); the gauge orbit
      (xi x I, xi x V, 0) has dimension 9; the norm mode (I/(2 Lambda), -V/(2 Lambda), 1) satisfies the
      constraints and lies outside the orbit; the family (s I, V/s, s^2 Lambda) satisfies the constraints at
      five s, and the norm mode is (1/(2 Lambda)) times (I, -V, 2 Lambda), its tangent at s = 1.
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
LAMS = [F(3, 4), F(12), F(-3, 2)]
MP = F(7)


def pair(lam):
    I = tractor(F(1), {}, lam / 6)
    return I, GA.sub(N0, GA.scal(3 / lam, I))


def vc(v):
    return [v.get((k,), F(0)) for k in range(6)]


def met(v):
    return [S[k] * c for k, c in enumerate(vc(v))]


def check_fixed_lambda_nine_and_de_sitter_scale():
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lam in LAMS:
        I, V = pair(lam)
        z = [F(0)] * 6
        rows = [met(I) + z, met(V) + met(I), z + met(V)]
        ok = ok and GA.field_rank(rows) == 3 and len(GA.field_kernel(rows)) == 9
        ok = ok and GA.field_rank([vc(comm(B, I)) + vc(comm(B, V)) for B in BIV]) == 9
    for H in (F(1, 2), F(3, 2)):
        f = Synchronous([(F(2), 2 * H, 2 * H * H)] * 3)
        lam = f.scalar() / 4
        ok = ok and all(GA.eq(f.ricci(E[m]), GA.scal(lam, E[m])) for m in range(4))
        I, V = pair(lam)
        ok = ok and (f.d[1][1] / f.d[1][0]) ** 2 == dot(I, I) and dot(I, I) == lam / 3
        ok = ok and all(GA.is_zero(comm(f.omega_T(m, f.schouten), I)) for m in range(4))
        ok = ok and (MP / H) ** 2 == 3 * MP ** 2 / lam
    GA.check("Lambda fixed: 9 = 9, and H^2 = Q(I) = Lambda/3 on the de Sitter field", ok)
    assert ok


def check_n_varies_with_lambda():
    premise("standard-model.trichotomy-what-kind-number")
    lam = GA.RF.var()
    N2 = GA.RF.const(3 * MP * MP) / lam
    dN2 = N2.deriv()
    ok = dN2.eqrf(GA.RF.const(-3 * MP * MP) / (lam * lam))
    ok = ok and dN2.eval(F(3, 4)) == F(-3 * 49 * 16, 9) and dN2.eval(F(12)) != 0
    for s in (F(2), F(1, 3), F(5)):
        for l0 in LAMS:
            I, V = pair(l0)
            sI = GA.scal(s, I)
            ok = ok and dot(sI, sI) == s * s * l0 / 3
            ok = ok and MP ** 2 / dot(sI, sI) == MP ** 2 / dot(I, I) / (s * s)       # N^2 = M_P^2/Q(I)
    GA.check("d(N^2)/dLambda = -3 M_P^2/Lambda^2 != 0; I -> s I gives N -> N/s", ok)
    assert ok


def check_varying_lambda_single_norm_mode():
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")
    ok = True
    for lam in LAMS:
        I, V = pair(lam)
        z = [F(0)] * 6
        rows = [[2 * c for c in met(I)] + z + [F(-1, 3)],
                met(V) + met(I) + [F(0)],
                z + [2 * c for c in met(V)] + [-3 / (lam * lam)]]
        ok = ok and GA.field_rank(rows) == 3 and len(GA.field_kernel(rows)) == 10
        orbit = [vc(comm(B, I)) + vc(comm(B, V)) + [F(0)] for B in BIV]
        ok = ok and GA.field_rank(orbit) == 9
        ok = ok and all(sum(r[j] * o[j] for j in range(13)) == 0 for r in rows for o in orbit)
        mode = [c / (2 * lam) for c in vc(I)] + [-c / (2 * lam) for c in vc(V)] + [F(1)]
        ok = ok and all(sum(r[j] * mode[j] for j in range(13)) == 0 for r in rows)
        ok = ok and GA.field_rank(orbit + [mode]) == 10
        tangent = vc(I) + [-c for c in vc(V)] + [2 * lam]
        ok = ok and (len(tangent) == len(mode) and all(t == 2 * lam * m for t, m in zip(tangent, mode)))
        for s in (F(1, 2), F(1), F(2), F(3), F(-1)):
            sI, Vs, ls = GA.scal(s, I), GA.scal(1 / s, V), s * s * lam
            ok = ok and dot(sI, sI) == ls / 3 and dot(Vs, Vs) == -3 / ls and dot(Vs, sI) == 0
    GA.check("Lambda varying: dimension 10, orbit 9, one norm mode (I/2Lambda, -V/2Lambda, 1)", ok)
    assert ok
