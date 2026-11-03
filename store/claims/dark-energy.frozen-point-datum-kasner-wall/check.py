"""dark-energy.frozen-point-datum-kasner-wall: exact GTG checks in GA (Cl(1,3) inside Cl(2,4)), ported
from legacy verify_T10.py (prop:kasnerwall) and recast with the gauge fields hb and Omega.

The field is the synchronous diagonal gravitational field hb^{-1}(e_tau) = e_tau, hb^{-1}(e_i) = a_i e_i
with a_i = tau^{p_i} (the leading Kasner term), evaluated exactly at tau = base^d (d clears the
denominators of p). Omega is in the GTG sign, Omega(e_i) = -adot_i e_0 ^ e_i (checked by the torsion
condition); the curvature is the store's calR(B) = -R(hb(B)) with R the field strength of Omega.
Points: Kasner (2/3, 2/3, -1/3) (Schwarzschild exponents) at tau = 8 and 27, Kasner (-2/7, 3/7, 6/7) at
tau = 128, non-Kasner (1/2, 1/2, 1/2) and (2/3, 2/3, 2/3), and the excluded flat Milne point (1, 0, 0).
  (i) Torsion-free; on unit physical directions u_i = hb(e_i) the connection is omega(u_i) = Omega(e_i)/a_i
      and tau omega(u_i) = -p_i B_i at two tau (a simple pole with residue -sum p_i B_i (x) e^i, no
      omega^{ij}); B_w = sum p_i B_i squares to sum p_i^2 (= 1, a unit boost, at the Kasner points). The
      tractor gauge field with Schouten map (Lambda/6) id: Omega_T(u_a) - omega(u_a) = -ninf ^ e_a +
      (Lambda/6) n0 ^ e_a is the same at both tau (regular, constant), I = ninf + (Lambda/6) n0 is parallel,
      Omega_T(u_a) x n0 = e_a (soldering of full rank 4), Q(I) = Lambda/3, Q(X) = 0.
  (ii) Cartan 2-forms from calR via Riem^o(u,v,w,z) = (w ^ z).calR(u ^ v) (DICTIONARY C11):
      R^{i0} = p_i(p_i - 1)/tau^2 e^0 ^ e^i, R^{ij} = -p_i p_j/tau^2 e^i ^ e^j, nothing else; store-sign
      Ricci tau^2 R_00 = sum p^2 - sum p, tau^2 R_ii = -p_i(sum p - 1), zero exactly at the Kasner points;
      it agrees with the premise's Bianchi I system (Hdot_i + H_i sum H = -R_ii, sum_{i<j} H_i H_j =
      -(R_00 - R/2)).
  (iii) Densities in the orthonormal frame: eps_{abcd} R^{ab} ^ R^{cd} = -16 p1 p2 p3 tau^-4 vol at the
      Kasner points (vol = tau^{sum p} dtau d^3x, so -16 p1 p2 p3 tau^-3 there), equal to the Kretschmann
      scalar (Euler = K - 4 Ric^2 + R^2 at every point; K != Euler off Kasner); Schwarzschild exponents give
      64/27; eps e e R = -2 R vol (zero at Kasner points; -8 Lambda on de Sitter); eps e e e e = 24 vol;
      on the de Sitter field -4 Ric^2 + R^2 = 0. Everything vanishes at (1, 0, 0).
The O(Lambda tau^2) corrections of the Einstein-Lambda solution are not computed here (they are the
content of dark-energy.cosmological-constant-does-not-change-residue).
"""
from fractions import Fraction as F
from itertools import permutations

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

SCHW = (F(2, 3), F(2, 3), F(-1, 3))
KASNER = [(SCHW, 2), (SCHW, 3), ((F(-2, 7), F(3, 7), F(6, 7)), 2)]
NONKASNER = [((F(1, 2), F(1, 2), F(1, 2)), 2), ((F(2, 3), F(2, 3), F(2, 3)), 2)]
MILNE = [((F(1), F(0), F(0)), 2), ((F(1), F(0), F(0)), 3)]
LAM = F(6, 5)


def field(p, base):
    tau, data = kasner(p, base)
    return tau, Synchronous(data)


def psign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def riem(f, a, b, c, d):
    """Riem^o(e_a, e_b, e_c, e_d) = (e_c ^ e_d) . calR(e_a ^ e_b) (orthonormal physical frame), memoised."""
    if not hasattr(f, "_cr"):
        f._cr = {(m, n): f.calR(wedge(E[m], E[n])) for m in range(4) for n in range(4)}
    return sp(mul(wedge(E[c], E[d]), f._cr[(a, b)]))


def rup(f, a, b, c, d):
    return S[a] * S[b] * riem(f, a, b, c, d)


def gauss_bonnet(f):
    tot = F(0)
    for i in permutations(range(4)):
        for j in permutations(range(4)):
            tot += psign(i) * psign(j) * rup(f, i[0], i[1], j[0], j[1]) * rup(f, i[2], i[3], j[2], j[3]) / 4
    return tot


def eeR(f):
    """eps_{abcd} e^a ^ e^b ^ R^{cd} on e^0123: the (e, f) legs of R^{cd} must be {c, d}, so the sum is
    sum over permutations of R^{cd}_{cd} (both orders of the legs, each with weight 1/2)."""
    tot = F(0)
    for i in permutations(range(4)):
        a, b, c, d = i
        tot += psign(i) * (psign((a, b, c, d)) * rup(f, c, d, c, d) + psign((a, b, d, c)) * rup(f, c, d, d, c)) / 2
    return tot


def check_torsion_free_pole_and_regular_datum():
    premise("dark-energy.cosmological-constant-does-not-change-residue")
    premise("sheaf.matching-fibre")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    ok = True
    I = tractor(F(1), {}, LAM / 6)
    ok = ok and dot(I, I) == LAM / 3 and dot(N0, N0) == 0
    P = lambda A: GA.scal(LAM / 6, A)
    for p, base in KASNER + NONKASNER:
        res, regular = [], []
        for b in (base, base + 1):
            tau, f = field(p, b)
            ok = ok and f.torsion_free()
            res.append([GA.scal(tau / f.a(m), f.Omega(m)) for m in range(4)])
            regular.append([GA.sub(GA.scal(1 / f.a(m), f.omega_T(m, P)), GA.scal(1 / f.a(m), f.Omega(m)))
                            for m in range(4)])
            sold = []
            for m in range(4):
                OT = GA.scal(1 / f.a(m), f.omega_T(m, P))
                ok = ok and GA.is_zero(comm(OT, I))
                sold.append(grade(comm(OT, N0), 1))
                ok = ok and GA.eq(sold[-1], E[m])
            ok = ok and GA.rank_of_vectors([[s.get((k,), F(0)) for k in range(6)] for s in sold]) == 4
        ok = ok and (len(res[0]) == len(res[1]) and all(GA.eq(x, y) for x, y in zip(res[0], res[1])))
        ok = ok and (len(regular[0]) == len(regular[1]) and all(GA.eq(x, y) for x, y in zip(regular[0], regular[1])))
        ok = ok and GA.is_zero(res[0][0])
        for i in range(1, 4):
            ok = ok and GA.eq(res[0][i], GA.scal(-p[i - 1], wedge(E[0], E[i])))
            ok = ok and GA.eq(regular[0][i], GA.add(GA.neg(wedge(NI, E[i])), GA.scal(LAM / 6, wedge(N0, E[i]))))
        Bw = GA.add(*[GA.scal(p[i], wedge(E[0], E[i + 1])) for i in range(3)])
        ok = ok and GA.eq(mul(Bw, Bw), GA.sc(sum(x * x for x in p)))
    for p, base in KASNER:
        Bw = GA.add(*[GA.scal(p[i], wedge(E[0], E[i + 1])) for i in range(3)])
        ok = ok and GA.eq(mul(Bw, Bw), GA.sc(1))
    GA.check("simple pole with residue -B_w; regular soldering and Schouten; I parallel", ok)
    assert ok


def check_double_pole_curvature_and_residue_equations():
    premise("dark-energy.cosmological-constant-does-not-change-residue")
    ok = True
    for p, base in KASNER + NONKASNER + MILNE:
        tau, f = field(p, base)
        s1, s2 = sum(p), sum(x * x for x in p)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        v = riem(f, a, b, c, d) * tau * tau
                        if {a, b} != {c, d} or a == b:
                            ok = ok and v == 0
        for i in range(1, 4):
            pi = p[i - 1]
            ok = ok and S[i] * riem(f, i, 0, 0, i) * tau * tau == pi * (pi - 1)
            for j in range(i + 1, 4):
                ok = ok and riem(f, i, j, i, j) * tau * tau == -pi * p[j - 1]
        R00 = dot(E[0], f.ricci(E[0])) * tau * tau
        ok = ok and R00 == s2 - s1
        for i in range(1, 4):
            ok = ok and dot(E[i], f.ricci(E[i])) * tau * tau == -p[i - 1] * (s1 - 1)
            for j in range(4):
                if j != i:
                    ok = ok and dot(E[j], f.ricci(E[i])) == 0
        # the premise's Bianchi I system: Hdot_i + H_i sum H = -R_ii, sum_{i<j} H_i H_j = -(R_00 - R/2)
        Hs = [f.d[i][1] / f.d[i][0] for i in range(1, 4)]
        Hd = [f.d[i][2] / f.d[i][0] - Hs[i - 1] ** 2 for i in range(1, 4)]
        for i in range(1, 4):
            ok = ok and Hd[i - 1] + Hs[i - 1] * sum(Hs) == -dot(E[i], f.ricci(E[i]))
        ok = ok and Hs[0] * Hs[1] + Hs[0] * Hs[2] + Hs[1] * Hs[2] == -(dot(E[0], f.ricci(E[0])) - f.scalar() / 2)
        flat = all(GA.is_zero(f.ricci(E[m])) for m in range(4))
        ok = ok and flat == (s1 == 1 and s2 == 1)
    GA.check("double-pole curvature; Ricci zero exactly at the Kasner relations", ok)
    assert ok


def check_action_densities_at_the_wall():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    premise("dark-energy.imported-weighted-limit-schwarzschild-singularity-matching")
    ok = True
    for p, base in KASNER:
        tau, f = field(p, base)
        prod = p[0] * p[1] * p[2]
        gb = gauss_bonnet(f)
        ok = ok and gb * tau ** 4 == -16 * prod and f.kretschmann() == gb
        ok = ok and gb * tau ** sum(p) * tau ** 3 == -16 * prod      # coordinate density, vol = tau dtau d3x
        ok = ok and eeR(f) == 0
    for p, base in NONKASNER + MILNE:
        tau, f = field(p, base)
        gb = gauss_bonnet(f)
        ok = ok and gb == f.kretschmann() - 4 * f.ricci_sq() + f.scalar() ** 2
        ok = ok and eeR(f) == -2 * f.scalar()
    tau, f = field(*NONKASNER[0])
    ok = ok and f.kretschmann() != gauss_bonnet(f) and f.ricci_sq() != 0
    for p, base in MILNE:
        tau, f = field(p, base)
        ok = ok and gauss_bonnet(f) == 0 and f.kretschmann() == 0
    # Schwarzschild exponents: p1 p2 p3 = -4/27, first density 64/27 tau^-3, Kretschmann 64/(27 tau^4)
    tau, f = field(SCHW, 2)
    ok = ok and SCHW[0] * SCHW[1] * SCHW[2] == F(-4, 27) and gauss_bonnet(f) * tau ** 3 * tau == F(64, 27)
    ok = ok and sum(psign(i) * psign(i) for i in permutations(range(4))) == 24
    # Einstein: de Sitter field (a = A, adot = H A, addot = H^2 A), -4 Ric^2 + R^2 = 0, eps e e R = -8 Lambda
    A, H = F(2), F(1, 2)
    ds = Synchronous([(A, H * A, H * H * A)] * 3)
    lam = 3 * H * H
    ok = ok and ds.torsion_free() and -4 * ds.ricci_sq() + ds.scalar() ** 2 == 0 and ds.scalar() == 4 * lam
    ok = ok and eeR(ds) == -8 * lam
    GA.check("Gauss-Bonnet density -16 p1p2p3 tau^-3 = Kretschmann; EC term zero; 24 vol", ok)
    assert ok
