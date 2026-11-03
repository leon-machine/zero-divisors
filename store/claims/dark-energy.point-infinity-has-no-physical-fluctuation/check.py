"""dark-energy.point-infinity-has-no-physical-fluctuation: exact checks in Cl(2,4), ported from legacy
verify_T10.py (prop:goldstone) and widened (three values of Lambda of both signs, the fibration, the
gauge orbit on a concrete de Sitter gravitational field).

I = ninf + (Lambda/6) n0, V = n0 - (3/Lambda) I (the canonical solution), fluctuations (dI, dV) in R^12
(vector coordinates on e0..e3, e+, e-), bivectors xi in the 15-dimensional so(2,4) acting by x.
  (1) The linearised constraints I.dI = 0, V.dI + I.dV = 0, V.dV = 0 have rank 3: the fluctuation space
      has dimension 9; it projects onto I-perp (dimension 5) in dI with 4-dimensional fibres in dV, and it is
      not the product of its two projections (5 + 5 != 9).
  (2) The stabiliser of (I, V) has dimension 6, the broken generators 15 - 6 = 9; xi -> (xi x I, xi x V) has
      rank 9 and image inside the constraint space, hence onto it: bijective on the broken generators.
  (3) The integrand eps(I, V, F, F) is invariant under a rotor acting on all three arguments (up to the
      rotor's norm to the fourth power) and not under one acting on I and F alone.
  (4) On the de Sitter field (hb, Omega) with Lambda = 3/4: a finite rotor R built from two vectors of
      I-perp fixes I and moves V (a pure dV); transforming Omega_T, I, V together keeps the constraints
      and gives D'_a V' = R hb^{-1}(a) R~ / |R|^2: the fluctuation is a gauge transformation, absorbed by a
      change of the soldering frame.
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
I6 = mul(mul(mul(E[0], E[1]), mul(E[2], E[3])), mul(E[4], E[5]))
LAMS = [F(3, 4), F(12), F(-3, 2)]
FB = GA.add(wedge(E[0], E[1]), GA.scal(F(2), wedge(E[2], E[3])), GA.scal(F(-1), wedge(E[1], E[4])),
            wedge(E[0], E[5]))


def pair(lam):
    I = tractor(F(1), {}, lam / 6)
    return I, GA.sub(N0, GA.scal(3 / lam, I))


def vcoords(v):
    return [v.get((k,), F(0)) for k in range(6)]


def constraint_rows(I, V):
    cI = [S[k] * c for k, c in enumerate(vcoords(I))]
    cV = [S[k] * c for k, c in enumerate(vcoords(V))]
    zero = [F(0)] * 6
    return [cI + zero, cV + cI, zero + cV]


def eps(a, b, Fm, G):
    return sp(mul(mul(mul(mul(a, b), Fm), G), GA.scal(1 / sp(mul(I6, I6)), I6)))


def check_constrained_fluctuations_nine():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    for lam in LAMS:
        I, V = pair(lam)
        rows = constraint_rows(I, V)
        ok = ok and GA.field_rank(rows) == 3
        space = GA.field_kernel(rows)
        ok = ok and len(space) == 9
        ok = ok and GA.field_rank([v[:6] for v in space]) == 5
        fibre = [v for v in GA.field_kernel(rows + [[F(1) if j == k else F(0) for j in range(12)] for k in range(6)])]
        ok = ok and len(fibre) == 4
        ok = ok and GA.field_rank([v[6:] for v in space]) == 5
    GA.check("constrained fluctuation space of (I, V) has dimension 9, fibred 5 + 4", ok)
    assert ok


def check_broken_generators_act_bijectively():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    for lam in LAMS:
        I, V = pair(lam)
        images = [vcoords(comm(B, I)) + vcoords(comm(B, V)) for B in BIV]
        cols = [[images[b][r] for b in range(15)] for r in range(12)]
        ok = ok and GA.field_rank(images) == 9 and len(GA.field_kernel(cols)) == 6
        rows = constraint_rows(I, V)
        ok = ok and all(sum(r[j] * im[j] for j in range(12)) == 0 for r in rows for im in images)
    GA.check("15 - 6 = 9 broken generators act onto the constraint space", ok)
    assert ok


INV_LAM = F(3, 4)
INV_RA = GA.add(E[0], GA.scal(F(2), E[4]), E[2])
INV_RB = GA.add(E[1], E[5], GA.scal(F(3), E[3]))


def check_integrand_invariant_under_ambient_group():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    I, V = pair(INV_LAM)
    # By hand: I ^ V = ninf ^ n0 = e+ ^ e- for every Lambda (the Lambda terms cancel); the grade-4 part of
    # FB FB along e0123 is 2 (e01)(2 e23) = 4 e0123, so eps(I, V, FB, FB) = 4.
    ok = GA.eq(grade(mul(I, V), 2), wedge(E[4], E[5]))
    R = mul(INV_RA, INV_RB)
    nrm = sp(mul(R, GA.reverse(R)))
    # R R~ = a^2 b^2 with a^2 = 1 + 4 - 1 = 4 and b^2 = -1 - 1 - 9 = -11.
    ok = ok and sp(mul(INV_RA, INV_RA)) == 4 and sp(mul(INV_RB, INV_RB)) == -11 and nrm == -44
    act = lambda x: mul(mul(R, x), GA.reverse(R))
    base = eps(I, V, FB, FB)
    ok = ok and base == 4
    ok = ok and eps(act(I), act(V), act(FB), act(FB)) == nrm ** 4 * base
    ok = ok and eps(GA.scal(1 / nrm, act(I)), V, GA.scal(1 / nrm, act(FB)), GA.scal(1 / nrm, act(FB))) != base
    GA.check("eps(I, V, F, F) invariant under the ambient group on all three arguments only", ok)
    assert ok


def check_fluctuation_is_gauge_on_de_sitter_field():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    H = F(1, 2)
    lam = 3 * H * H
    f = Synchronous([(F(2), 2 * H, 2 * H * H)] * 3)
    I, V = pair(lam)
    a, b = GA.add(E[1], GA.scal(F(2), E[0])), GA.add(GA.sub(NI, GA.scal(lam / 6, N0)), E[2])
    ok = dot(a, I) == 0 and dot(b, I) == 0 and dot(a, a) != 0 and dot(b, b) != 0
    R = mul(a, b)
    nrm = sp(mul(R, GA.reverse(R)))
    act = lambda x: GA.scal(1 / nrm, mul(mul(R, x), GA.reverse(R)))
    I2, V2 = act(I), act(V)
    ok = ok and GA.eq(I2, I) and not GA.eq(V2, V)
    ok = ok and dot(V2, I2) == 0 and dot(V2, V2) == -3 / lam
    for m in range(4):
        OT = f.omega_T(m, f.schouten)
        ok = ok and GA.eq(comm(OT, V), f.hb_inv(m))
        ok = ok and GA.eq(comm(act(OT), V2), act(f.hb_inv(m)))
        ok = ok and GA.is_zero(comm(act(OT), I2))
    GA.check("a dV fluctuation is a gauge transformation absorbed by the soldering frame", ok)
    assert ok
