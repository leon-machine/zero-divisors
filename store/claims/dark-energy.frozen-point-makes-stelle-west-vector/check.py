"""dark-energy.frozen-point-makes-stelle-west-vector: exact GTG checks in Cl(2,4), ported from legacy
verify_T10.py (thm:action) and recast with gauge fields.

Fields (synchronous diagonal, GTG sign): de Sitter (a, adot, addot) = (2, 2H, 2H^2), Lambda = 3H^2 at
H = 1/2, 2; the Kasner vacuum (2/3, 2/3, -1/3) at tau = 8 (Lambda = 0, frozen point ninf). The tractor
field strength is computed with its derivative terms,
F_T(e_m ^ e_n) = e_m.grad Omega_T(e_n) - e_n.grad Omega_T(e_m) + Omega_T(e_m) x Omega_T(e_n),
for fields whose Schouten map is a constant multiple of the identity (de Sitter, vacuum).
  (i) Stabiliser of I = ninf + (Lambda/6) n0 has dimension 10 and I-perp signature (1,4) / (2,3); the
      curvature takes values in Lambda^2 I-perp: F_T = 0 on de Sitter, and on the Kasner vacuum F_T x ninf = 0
      with spacetime block -calR(hb^{-1} ^ hb^{-1}) (the Weyl curvature); for Lambda != 0 with Weyl part
      (calR = (Lambda/3) id + the Kasner Weyl operator) the algebraic field strength is -W, which
      annihilates I and V.
  (ii) V = X - (3/Lambda) I is in I-perp with Q(V) = -3/Lambda; the stabiliser of (I, V) has dimension 6
      and {I, V}-perp signature (1,3) on both branches; the reduced connection is Omega(a) - hb^{-1}(a) ^ V/l^2
      (= Omega_T for P = (Lambda/6) id), its D V is the soldering form, its Lorentz block is
      -calR + (Lambda/3) e ^ e (zero on de Sitter).
  (iii) The fibre volume form eps(a, b, F, G) = <a ^ b ^ F ^ G I6^-1>: eps(I, V, ., .) = eps(I, X, ., .) =
      eps(ninf, n0, ., .); (1/Q(I)) eps(I, V, F, F) = (3/Lambda) eps(I, X, F, F); with F = R + (Lambda/3) e ^ e
      it is (3/Lambda) eps(R,R) + 2 eps(R, ee) + (Lambda/3) eps(ee, ee) (checked at 4 Lambda, so the
      Lambda-polynomial part of Lambda S is quadratic and the only pole is the R ^ R term); Q(I) Q(V) = -1
      for either sign; [I ^ u, I ^ v] = -Q(I) u ^ v; the ambient group carries the field space to itself:
      R (B x I) R~ = (R B R~) x (R I R~) for a sample rotor R, and eps is invariant under it.
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
RB = GA.add(*[GA.scal(F(c), wedge(E[i], E[j])) for c, (i, j) in zip((1, -2, 3, 1, 2, -1),
                                                                   ((0, 1), (0, 2), (1, 3), (2, 3), (0, 3), (1, 2)))])
EE = GA.add(wedge(E[0], E[2]), GA.scal(F(2), wedge(E[1], E[3])), GA.scal(F(-1), wedge(E[0], E[1])))
ROTOR = mul(GA.add(E[0], GA.scal(F(2), E[4]), E[2]), GA.add(E[1], E[5], GA.scal(F(3), E[3])))


def de_sitter(H):
    return Synchronous([(F(2), 2 * H, 2 * H * H)] * 3)


def field_strength(f, c):
    """F_T(e_m ^ e_n) for a field with Schouten map c id (c constant)."""
    P = lambda A: GA.scal(c, A)

    def dOT(n):
        # time derivative of Omega_T(e_n): d Omega(e_n) - ninf ^ d hb^{-1}(e_n) + c n0 ^ d hb^{-1}(e_n)
        dh = f.d_hb_inv(n)
        return GA.add(f.d_Omega(n), GA.neg(wedge(NI, dh)), GA.scal(c, wedge(N0, dh)))

    out = {}
    for m in range(4):
        for n in range(4):
            t1 = dOT(n) if m == 0 else {}
            t2 = dOT(m) if n == 0 else {}
            out[(m, n)] = GA.add(t1, GA.neg(t2), comm(f.omega_T(m, P), f.omega_T(n, P)))
    return out


def stabiliser(vectors):
    rows = []
    for v in vectors:
        rows += [[comm(B, v).get((k,), F(0)) for B in BIV] for k in range(6)]
    return GA.field_kernel(rows)


def eps(a, b, Fm, G):
    return sp(mul(mul(mul(mul(a, b), Fm), G), GA.scal(1 / sp(mul(I6, I6)), I6)))


def ev(x):
    return mul(mul(ROTOR, x), GA.reverse(ROTOR))


# Sample inputs for check_reduction_and_curvature_in_i_perp: one Lambda per sign, with the expected
# I-perp signature for that sign; two de Sitter rates; one Kasner vacuum (exponents, base of tau).
LAMBDA_CASES = ((F(3, 4), (1, 4)), (F(-3, 2), (2, 3)))
H_SAMPLES = (F(1, 2), F(2))
KASNER_P = (F(2, 3), F(2, 3), F(-1, 3))
KASNER_BASE = 2


def check_reduction_and_curvature_in_i_perp():
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    for lam, sig_exp in LAMBDA_CASES:
        I = tractor(F(1), {}, lam / 6)
        # normalisation of I = ninf + (Lambda/6) n0: Q(I) = Lambda/3, so that Q(I) Q(V) = -1 with Q(V) = -3/Lambda
        ok = ok and sp(mul(I, I)) == lam / 3
        ok = ok and len(stabiliser([I])) == 10
        ker = GA.field_kernel([[dot(I, E[k]) for k in range(6)]])
        G = [[sum(u[i] * v[i] * S[i] for i in range(6)) for v in ker] for u in ker]
        ok = ok and GA.congruence_signature(G)[:2] == sig_exp
    for H in H_SAMPLES:
        f = de_sitter(H)
        c = H * H / 2
        # field_strength needs Schouten = c id: de Sitter has Lambda = 3H^2, Schouten = (Lambda/6) id
        ok = ok and all(GA.eq(f.schouten(a), GA.scal(3 * H * H / 6, a)) for a in ER)
        Fs = field_strength(f, c)
        ok = ok and f.torsion_free() and all(GA.is_zero(x) for x in Fs.values())
    tau, data = kasner(KASNER_P, KASNER_BASE)
    k = Synchronous(data)
    # the Kasner field is a vacuum (Schouten = 0), which field_strength(k, 0) presupposes
    ok = ok and all(GA.is_zero(k.schouten(a)) for a in ER)
    Fs = field_strength(k, F(0))
    nonzero = 0
    for m, n in PLANES:
        Fmn = Fs[(m, n)]
        ok = ok and GA.is_zero(comm(Fmn, NI))
        phys = GA.scal(k.a(m) * k.a(n), k.calR(wedge(E[m], E[n])))     # calR(hb^{-1}(e_m) ^ hb^{-1}(e_n))
        ok = ok and GA.eq(Fmn, GA.neg(phys))
        nonzero += not GA.is_zero(Fmn)
    ok = ok and nonzero == 6
    GA.check("reduction to I-perp; curvature in Lambda^2 I-perp (de Sitter zero, Kasner Weyl)", ok)
    assert ok


def check_stelle_west_datum_and_lorentz_block():
    premise("dark-energy.stelle-west-vector-frozen-point")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    ok = True
    for lam in (F(3, 4), F(12), F(-3, 2)):
        I = tractor(F(1), {}, lam / 6)
        V = GA.sub(N0, GA.scal(3 / lam, I))
        ok = ok and dot(V, I) == 0 and dot(V, V) == -3 / lam
        st = stabiliser([I, V])
        ok = ok and len(st) == 6
        ker = GA.field_kernel([[dot(I, E[k]) for k in range(6)], [dot(V, E[k]) for k in range(6)]])
        G = [[sum(u[i] * v[i] * S[i] for i in range(6)) for v in ker] for u in ker]
        ok = ok and GA.congruence_signature(G)[:2] == (1, 3)
    for H in (F(1, 2), F(2)):
        f = de_sitter(H)
        lam = 3 * H * H
        I = tractor(F(1), {}, lam / 6)
        V = GA.sub(N0, GA.scal(3 / lam, I))
        for m in range(4):
            red = GA.sub(f.Omega(m), GA.scal(lam / 3, wedge(f.hb_inv(m), V)))      # Omega - e ^ V / l^2
            ok = ok and GA.eq(red, f.omega_T(m, f.schouten))
            ok = ok and GA.eq(comm(red, V), f.hb_inv(m))
        for m, n in PLANES:
            ea, eb = f.hb_inv(m), f.hb_inv(n)
            block = GA.add(GA.neg(f.calR(wedge(ea, eb))), GA.scal(lam / 3, wedge(ea, eb)))
            ok = ok and GA.is_zero(block)
    # Lambda != 0 with a Weyl part: calR = (Lambda/3) id + Kasner Weyl operator; algebraic F = -W, kills I, V
    tau, data = kasner((F(2, 3), F(2, 3), F(-1, 3)), 2)
    k = Synchronous(data)
    lam = F(3, 4)
    I = tractor(F(1), {}, lam / 6)
    V = GA.sub(N0, GA.scal(3 / lam, I))
    W = GA.scal(1 / dot(V, V), V)
    for m, n in PLANES:
        Bmn = wedge(E[m], E[n])
        calR = GA.add(GA.scal(lam / 3, Bmn), k.calR(Bmn))
        Falg = GA.add(GA.neg(calR), comm(wedge(E[m], W), wedge(E[n], W)))
        ok = ok and GA.eq(Falg, GA.neg(k.calR(Bmn))) and GA.is_zero(comm(Falg, I)) and GA.is_zero(comm(Falg, V))
    GA.check("Stelle-West datum: stabiliser Lorentz (1,3), D V = soldering, Lorentz block R + e^e/l^2", ok)
    assert ok


def check_action_prefactor_expansion_and_invariance():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.stelle-west-vector-frozen-point")
    ok = True
    vals = {}
    for lam in (F(3, 4), F(12), F(-3, 2), F(2)):
        I = tractor(F(1), {}, lam / 6)
        X = N0
        V = GA.sub(X, GA.scal(3 / lam, I))
        ok = ok and dot(I, I) * dot(V, V) == -1
        Fm = GA.add(RB, GA.scal(lam / 3, EE))
        e_IV = eps(I, V, Fm, Fm)
        ok = ok and e_IV == eps(I, X, Fm, Fm) and e_IV == eps(NI, N0, Fm, Fm)
        S_ = e_IV / dot(I, I)
        ok = ok and S_ == (3 / lam) * eps(I, X, Fm, Fm)
        expected = (3 / lam) * eps(NI, N0, RB, RB) + 2 * eps(NI, N0, RB, EE) + (lam / 3) * eps(NI, N0, EE, EE)
        ok = ok and S_ == expected
        vals[lam] = S_ * lam
        for u in E[:4]:
            for v in E[:4]:
                ok = ok and GA.eq(comm(wedge(I, u), wedge(I, v)), GA.scal(-dot(I, I), wedge(u, v)))
    # Lambda S is a quadratic polynomial in Lambda: the Lagrange interpolant through three points hits the fourth
    xs = [F(3, 4), F(12), F(-3, 2)]
    lag = F(0)
    for i, xi in enumerate(xs):
        term = vals[xi]
        for j, xj in enumerate(xs):
            if j != i:
                term *= (F(2) - xj) / (xi - xj)
        lag += term
    ok = ok and lag == vals[F(2)] and eps(NI, N0, RB, RB) != 0
    # gauge covariance: R (B x I) R~ = (R B R~) x (R I R~) / (R R~), and eps invariant under the rotor
    nrm = sp(mul(ROTOR, GA.reverse(ROTOR)))
    lam = F(3, 4)
    I = tractor(F(1), {}, lam / 6)
    V = GA.sub(N0, GA.scal(3 / lam, I))
    ok = ok and nrm != 0 and GA.eq(GA.scal(nrm, ev(comm(RB, I))), comm(ev(RB), ev(I)))
    ok = ok and eps(ev(I), ev(V), ev(RB), ev(EE)) == nrm ** 4 * eps(I, V, RB, EE)
    GA.check("action: prefactor 1/Q(I) = 3/Lambda, MacDowell-Mansouri expansion, ambient invariance", ok)
    assert ok
