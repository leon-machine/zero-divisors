#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_QFT.py: exact checks for the run "From the CAR limit towards a quantum field
theory" (15 October 2026).  Preregistration: preregistration_QFT_2026-10-15.md.
Findings: QFT_findings_2026-10-15.md.

Exact arithmetic only: fractions.Fraction and GA.QI (Gaussian rationals); no floating
point anywhere.  Imports GA.py from the suite root (run from the suite folder with
PYTHONPATH=. or with GA.py beside this file).

Parts (as registered):
  A  attaching the modes to spacetime (item 2)
  B  Lorentz invariance as a test (item 3)
  C  the odd-charge limit, the reading for T14's towers (item 4)
  D  the path integral (item 1)
"""

import sys
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial

import GA
from GA import (FAILURES, mul, add, neg, sub, sc, gen, reverse, eq, is_zero,
                commutes, anticommutes, sig, QI, rf_mat_det, RF)

# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

NCHECKS = [0]


def check(label, ok):
    NCHECKS[0] += 1
    GA.check(label, ok)


def scl(c, x):
    """Scalar multiple for Fraction or QI coefficients."""
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def acomm(x, y, s):
    return add(mul(x, y, s), mul(y, x, s))


def comm(x, y, s):
    return sub(mul(x, y, s), mul(y, x, s))


def pair(e, f):
    """Null pair of the plane (e, f), Q(e) = 1, Q(f) = -1: v = (e+f)/2, w = (e-f)/2."""
    v = add(scl(F(1, 2), gen(e)), scl(F(1, 2), gen(f)))
    w = add(scl(F(1, 2), gen(e)), scl(F(-1, 2), gen(f)))
    return v, w


def star(x, s):
    """T03 Lemma lem:cstar: conjugate-linear antiautomorphism, x* = x for Q(x) = 1,
    x* = -x for Q(x) = -1 on frame generators."""
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        cc = c.conj() if isinstance(c, QI) else c
        out[b] = sign * cc
    return {b: c for b, c in out.items() if c != 0}


def exp_nil(X, s, nmax):
    """exp(X) for nilpotent X (X^(nmax+1) = 0), exact."""
    out = sc(1)
    term = sc(1)
    for n in range(1, nmax + 1):
        term = scl(F(1, n), mul(term, X, s))
        if not term:
            break
        out = add(out, term)
    return out


# --- small exact matrices -------------------------------------------------

def mzero(n, m=None):
    return [[F(0)] * (m if m is not None else n) for _ in range(n)]


def mid(n):
    M = mzero(n)
    for i in range(n):
        M[i][i] = F(1)
    return M


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum((A[i][t] * B[t][j] for t in range(k)), F(0)) for j in range(m)] for i in range(n)]


def madd(A, B):
    return [[a + b for a, b in zip(r1, r2)] for r1, r2 in zip(A, B)]


def mscal(c, A):
    return [[c * a for a in r] for r in A]


def mdag(A):
    return [[(A[j][i].conj() if isinstance(A[j][i], QI) else A[j][i]) for j in range(len(A))]
            for i in range(len(A[0]))]


def meq(A, B):
    return all(a == b for r1, r2 in zip(A, B) for a, b in zip(r1, r2))


def mtrace(A):
    return sum((A[i][i] for i in range(len(A))), F(0))


def mdet(A):
    """Exact determinant by fraction-free elimination (Fraction entries)."""
    M = [list(r) for r in A]
    n = len(M)
    det = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            if f != 0:
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return det


def jw_ops(k):
    """Jordan-Wigner annihilators c_1..c_k on (C^2)^k, basis index bits b_j = occupation."""
    dim = 2 ** k
    ops = []
    for j in range(k):
        C = mzero(dim)
        for st in range(dim):
            if (st >> j) & 1:
                sign = (-1) ** bin(st & ((1 << j) - 1)).count("1")
                C[st ^ (1 << j)][st] = F(sign)
        ops.append(C)
    return ops


# --- multivariate polynomials (Fraction or QI coefficients) -----------------

class Poly(object):
    def __init__(self, d=None, n=4):
        self.n = n
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def var(i, n=4):
        e = [0] * n
        e[i] = 1
        return Poly({tuple(e): F(1)}, n)

    @staticmethod
    def const(c, n=4):
        return Poly({tuple([0] * n): c}, n)

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, F(0)) + v
        return Poly(d, self.n)

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()}, self.n)

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            return Poly({k: o * v for k, v in self.d.items()}, self.n)
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                d[k] = d.get(k, F(0)) + v1 * v2
        return Poly(d, self.n)

    __rmul__ = __mul__

    def deriv(self, i):
        d = {}
        for k, v in self.d.items():
            if k[i] > 0:
                kk = list(k)
                kk[i] -= 1
                d[tuple(kk)] = d.get(tuple(kk), F(0)) + v * k[i]
        return Poly(d, self.n)

    def is_zero(self):
        return not self.d

    def ev(self, pt):
        tot = F(0)
        for k, v in self.d.items():
            t = v
            for x, e in zip(pt, k):
                for _ in range(e):
                    t = t * x
            tot = tot + t
        return tot

    def subst_neg(self):
        return Poly({k: v * (-1) ** sum(k) for k, v in self.d.items()}, self.n)

    def pw(self, m):
        out = Poly.const(F(1), self.n)
        for _ in range(m):
            out = out * self
        return out


def qpow(z, n):
    out = QI(1)
    for _ in range(n):
        out = out * z
    return out


# ===========================================================================
# PART A. Attaching the modes to spacetime (item 2)
# ===========================================================================
print("=" * 72)
print("PART A. Attaching the modes to spacetime (item 2)")
print("=" * 72)

# --- A1. Blindness ------------------------------------------------------------
# ground Cl(2,4): generators 0,1 square +1, 2..5 square -1; planes (6,7), (8,9).
SA = (1, 1, -1, -1, -1, -1, 1, -1, 1, -1)
v1, w1 = pair(6, 7)
v2, w2 = pair(8, 9)
modes = [v1, w1, v2, w2]
biv = [mul(gen(i), gen(j), SA) for i, j in combinations(range(6), 2)]
check("A1.1 the 15 so(2,4) bivectors of the ground commute with all 4 mode operators of two planes",
      len(biv) == 15 and all(commutes(B, m, SA) for B in biv for m in modes))
ninf = add(gen(0), gen(2))                      # a null ground vector (n_inf)
check("A1.2 n_inf = e_0 + e_2 is null", is_zero(mul(ninf, ninf, SA)))
Tr = add(sc(1), scl(F(1, 2), mul(ninf, gen(1), SA)))       # translation rotor 1 + n_inf a / 2
Trt = add(sc(1), scl(F(-1, 2), mul(ninf, gen(1), SA)))
check("A1.3 the translation rotor 1 + n_inf e_1/2 is a rotor (T T~ = 1)", eq(mul(Tr, Trt, SA), sc(1)))
check("A1.4 Ad(translation) fixes every mode operator",
      all(eq(mul(mul(Tr, m, SA), Trt, SA), m) for m in modes))
Bb = mul(gen(1), gen(3), SA)                   # a boost bivector of the (1,3) chart, square +1
Rb = add(sc(F(5, 4)), scl(F(3, 4), Bb))
Rbi = add(sc(F(5, 4)), scl(F(-3, 4), Bb))
Br = mul(gen(3), gen(4), SA)                   # a rotation bivector, square -1
Rr = add(sc(F(3, 5)), scl(F(4, 5), Br))
Rri = add(sc(F(3, 5)), scl(F(-4, 5), Br))
check("A1.5 Spin(1,3) boost and rotation rotors (rational rapidity/angle) are rotors",
      eq(mul(Rb, Rbi, SA), sc(1)) and eq(mul(Rr, Rri, SA), sc(1)) and eq(mul(Bb, Bb, SA), sc(1)))
check("A1.6 Ad of the Lorentz rotors fixes every mode operator",
      all(eq(mul(mul(R, m, SA), Ri, SA), m) for R, Ri in ((Rb, Rbi), (Rr, Rri)) for m in modes))
omg = sc(1)
for i in range(6):
    omg = mul(omg, gen(i), SA)
check("A1.7 the ground volume element (even, six vectors) commutes with every mode operator",
      all(commutes(omg, m, SA) for m in modes))
check("A1.8 control: every ground vector anticommutes with every mode operator (odd part acts by sign)",
      all(anticommutes(gen(i), m, SA) for i in range(6) for m in modes))

# --- A3. Pointwise attachment on a chain -------------------------------------------
# L = 5 sites, plane x on generators (2x, 2x+1); a_x = w_x, a_x^* = v_x (T03).
L = 5
SC = tuple([1, -1] * L)
V = [pair(2 * x, 2 * x + 1)[0] for x in range(L)]
W = [pair(2 * x, 2 * x + 1)[1] for x in range(L)]
check("A3.0 star(v_x) = w_x on the chain (T03 Lemma lem:cstar)",
      all(eq(star(V[x], SC), W[x]) for x in range(L)))
H = {}
for x in range(L - 1):
    H = add(H, mul(V[x], W[x + 1], SC), mul(V[x + 1], W[x], SC))
adH = lambda y: comm(H, y, SC)
ok = True
for x in range(L):
    expect = {}
    for y in (x - 1, x + 1):
        if 0 <= y < L:
            expect = add(expect, neg(W[y]))
    ok = ok and eq(adH(W[x]), expect)
check("A3.1 [H, a_x] = -(a_{x-1} + a_{x+1}): the hop moves a mode one site", ok)
o = 2                                           # origin in the middle
coef = {}
for x in range(L):
    y = W[x]
    for n in range(0, 3):
        a = acomm(y, V[o], SC)
        coef[(abs(x - o), n, x)] = a
        y = adH(y)
ok_zero = all(is_zero(coef[(d, n, x)]) for (d, n, x) in coef if n < d)
ok_first = all(eq(coef[(d, n, x)], sc((-1) ** n)) for (d, n, x) in coef if n == d)
check("A3.2 {ad_H^n(a_x), a_o^*} = 0 for n < |x - o| (computed in the tower, |x - o| <= 2)", ok_zero)
check("A3.3 {ad_H^n(a_x), a_o^*} = (-1)^n != 0 at n = |x - o|: the t^|x-o| Taylor coefficient is nonzero",
      ok_first)
N_ch = 21
h = mzero(N_ch)
for x in range(N_ch - 1):
    h[x][x + 1] = F(1)
    h[x + 1][x] = F(1)
P = mid(N_ch)
okc = True
for n in range(0, 11):
    for d in range(0, 11):
        val = P[10 + d][10]
        if n < d and val != 0:
            okc = False
        if n == d and val != 1:
            okc = False
    P = mmul(P, h)
check("A3.4 one-particle level, 21-site chain: (h^n)_{x0} = 0 for n < |x|, = 1 at n = |x| (|x| <= 10)", okc)
eps = [F(1), F(2), F(3), F(5), F(7)]
H0 = {}
for x in range(L):
    H0 = add(H0, scl(eps[x], mul(V[x], W[x], SC)))
check("A3.5 no hop: [H_0, a_x] = -eps_x a_x, so {a_x(t), a_y*} = e^{-i eps_x t} delta_xy: the mode never leaves its site (ultralocal)",
      all(eq(comm(H0, W[x], SC), scl(-eps[x], W[x])) for x in range(L)))

# --- A4. Twistor attachment: helicity-s kernels --------------------------------------
# chart coordinates M^{BA'} (B unprimed row, A' primed column): variables m00, m01, m10, m11.
m00, m01, m10, m11 = (Poly.var(i) for i in range(4))
Mv = [[m00, m01], [m10, m11]]
idx = [[0, 1], [2, 3]]
D = m00 * m11 - m01 * m10
mu = [F(2), F(3)]
chi = [Mv[0][a] * mu[0] + Mv[1][a] * mu[1] for a in range(2)]      # chi^{A'} = mu_B M^{BA'}


def kernel_eq_numerators(m, contraction):
    """Numerators (over D^(m+2)) of the field equation for the helicity m/2 kernel
    phi^{A'_1..A'_m} = chi^{A'_1}..chi^{A'_m} / D^(m+1)."""
    outs = []
    for B in range(2):
        for rest in product(range(2), repeat=m - 1):
            Pi = Poly.const(F(1))
            for c in rest:
                Pi = Pi * chi[c]
            tot = Poly()
            for A in range(2):
                if contraction == "trace":
                    der_var, comp, sgn = idx[B][A], A, F(1)
                else:   # epsilon contraction eps^{A'B'} d_{BB'} phi^{A'...}
                    Bp = 1 - A
                    der_var, comp, sgn = idx[B][Bp], A, F(1) if A == 0 else F(-1)
                num = chi[comp] * Pi
                term = num.deriv(der_var) * D - (num * D.deriv(der_var)) * F(m + 1)
                tot = tot + term * sgn
            outs.append(tot)
    return outs


box = (D.deriv(0).deriv(3) - D.deriv(1).deriv(2))
# second derivative numerator of 1/D: d_i d_j D^-1 = (2 d_iD d_jD - D d_i d_j D)/D^3
lap_num = ((D.deriv(0) * D.deriv(3)) * F(2) - D * D.deriv(0).deriv(3)) - \
          ((D.deriv(1) * D.deriv(2)) * F(2) - D * D.deriv(1).deriv(2))
check("A4.1 s = 0: 1/det solves the chart wave equation (d00 d11 - d01 d10)(1/D) = 0", lap_num.is_zero())
for m in (1, 2, 3, 4):
    tr = kernel_eq_numerators(m, "trace")
    ep = kernel_eq_numerators(m, "eps")
    check("A4.2 s = %s: the kernel solves d_{BA'} phi^{A'...} = 0 identically (all components)" %
          (F(m, 2)), all(p.is_zero() for p in tr))
    check("A4.3 s = %s: control, the epsilon contraction of the same kernel does not vanish" %
          (F(m, 2)), any(not p.is_zero() for p in ep))
for m in range(0, 5):
    num = Poly.const(F(1))
    for _ in range(m):
        num = num * chi[0]
    check("A4.4 2s = %d: exchange parity, numerator(-x) = (-1)^%d numerator(x) and D(-x) = D(x)" % (m, m),
          (num.subst_neg() - num * F((-1) ** m)).is_zero() and (D.subst_neg() - D).is_zero())
# a rational spacelike Minkowski point: x = (x0, x1, x2, x3) = (1, 2, 1, 1)
x0, x1, x2, x3 = F(1), F(2), F(1), F(1)
pt = [QI(x0 + x3), QI(x1, -x2), QI(x1, x2), QI(x0 - x3)]   # Hermitian M = x0 + x.sigma
Dv = D.ev(pt)
check("A4.5 at x = (1,2,1,1): det M = x^2 = -5, real and negative (spacelike)", Dv == QI(-5))
okp = True
for m in range(0, 5):
    num = Poly.const(F(1))
    for _ in range(m):
        num = num * chi[0]
    Wx = num.ev(pt) / qpow(Dv, m + 1)
    Wmx = num.ev([-p for p in pt]) / qpow(D.ev([-p for p in pt]), m + 1)
    okp = okp and (Wmx == Wx * ((-1) ** m)) and Wx != 0
check("A4.6 at the spacelike point the kernels satisfy W(-x) = (-1)^{2s} W(x), W != 0, for 2s = 0..4", okp)

# --- A5. The palatial storey's ladder module --------------------------------------
# operators on polynomials in y1..y4 (a1*, a2*, b1*, b2*); Z = (y1, y2, d3, d4),
# Zbar = (-d1, -d2, y3, y4), hbar = 1.
NV = 4


def mono_basis(deg):
    out = []
    for e in product(range(deg + 1), repeat=NV):
        if sum(e) <= deg:
            out.append(Poly({e: F(1)}, NV))
    return out


def op_Z(al):
    if al < 2:
        return lambda p: Poly.var(al, NV) * p
    return lambda p: p.deriv(al)


def op_Zb(be):
    if be < 2:
        return lambda p: -p.deriv(be)
    return lambda p: Poly.var(be, NV) * p


basis3 = mono_basis(3)
okccr = True
for al in range(4):
    for be in range(4):
        for p in basis3:
            c = op_Z(al)(op_Zb(be)(p)) - op_Zb(be)(op_Z(al)(p))
            target = p if al == be else Poly(n=NV)
            if not (c - target).is_zero():
                okccr = False
        for p in basis3:
            if not (op_Z(al)(op_Z(be)(p)) - op_Z(be)(op_Z(al)(p))).is_zero():
                okccr = False
            if not (op_Zb(al)(op_Zb(be)(p)) - op_Zb(be)(op_Zb(al)(p))).is_zero():
                okccr = False
check("A5.1 the oscillator realisation satisfies the palatial relations [Z^a, Zbar_b] = delta (degree <= 3)",
      okccr)


def fock_ip(p, q):
    tot = F(0)
    for k, v in p.d.items():
        if k in q.d:
            w = q.d[k]
            f = 1
            for e in k:
                f *= factorial(e)
            tot += v * w * f
    return tot


okadj = True
Sig = [F(-1), F(-1), F(1), F(1)]
for al in range(4):
    for p in basis3:
        for q in basis3:
            # <p, Zbar_al q> = Sigma_al <Z^al p, q>  (Zbar is the Sigma-adjoint of Z)
            lhs = fock_ip(p, op_Zb(al)(q))
            rhs = Sig[al] * fock_ip(op_Z(al)(p), q)
            if lhs != rhs:
                okadj = False
check("A5.2 in the Fock inner product Zbar_a = Sigma_aa (Z^a)^dagger with Sigma = diag(-1,-1,1,1), "
      "signature (2,2): the twistor form", okadj)


def qM(Mm):
    def f(p):
        tot = Poly(n=NV)
        for al in range(4):
            for be in range(4):
                c = Mm[be][al]
                if c != 0:
                    t = op_Z(al)(op_Zb(be)(p)) + op_Zb(be)(op_Z(al)(p))
                    tot = tot + t * (c / 2)
        return tot
    return f


Idm = [[F(int(i == j)) for j in range(4)] for i in range(4)]
SigM = [[Sig[i] if i == j else F(0) for j in range(4)] for i in range(4)]
qid, qsig = qM(Idm), qM(SigM)
okhe = True
for p in mono_basis(4):
    (k, _), = p.d.items()
    Na, Nb = k[0] + k[1], k[2] + k[3]
    if not (qid(p) * F(1, 2) - p * F(Nb - Na, 2)).is_zero():
        okhe = False
    if not (qsig(p) * F(1, 2) - p * (F(Na + Nb, 2) + 1)).is_zero():
        okhe = False
check("A5.3 helicity q(id)/2 = (N_b - N_a)/2 and energy q(Sigma)/2 = (N_a + N_b)/2 + 1 on all monomials "
      "of degree <= 4", okhe)
okmult = True
okpos = True
tally = {}
for e in product(range(13), repeat=4):
    Na, Nb = e[0] + e[1], e[2] + e[3]
    if Na + Nb <= 12:
        key = (Nb - Na, F(Na + Nb, 2) + 1)
        tally[key] = tally.get(key, 0) + 1
for twos in range(-4, 5):
    for n in range(0, 5):
        cnt = tally.get((twos, F(abs(twos), 2) + 1 + n), 0)
        if cnt != (n + 1) * (n + abs(twos) + 1):
            okmult = False
for e in product(range(7), repeat=4):
    Na, Nb = e[0] + e[1], e[2] + e[3]
    if F(Na + Nb, 2) + 1 < F(abs(Nb - Na), 2) + 1:
        okpos = False
check("A5.4 helicity-s module: energies |s| + 1 + n with multiplicity (n+1)(n+2|s|+1), 2s = -4..4, n <= 4",
      okmult)
check("A5.5 positive energy: E >= |s| + 1 on every Fock monomial (degree <= 24)", okpos)

# --- A6. Floors versus the limit -----------------------------------------------------
zeta = QI(F(3, 5), F(4, 5))          # e^{i chi}, cos chi = 3/5
zsp = QI(F(24, 25), F(7, 25))        # e^{i t}, cos t = 24/25 (t < chi: spacelike)
ztl = QI(F(7, 25), F(24, 25))        # e^{i t}, cos t = 7/25 (t > chi: timelike)


def im(z):
    return z.im


def re(z):
    return z.re


def sin_n(z, n):
    return im(qpow(z, n))


def cos_n(z, n):
    return re(qpow(z, n))


check("A6.0 the sample points: cos t = 24/25 > cos chi = 3/5 (spacelike), cos t = 7/25 < 3/5 (timelike)",
      re(zsp) > re(zeta) and re(ztl) < re(zeta))
partial = [sum((sin_n(zsp, n) * sin_n(zeta, n) for n in range(1, N + 1)), F(0)) for N in range(1, 13)]
check("A6.1 ESU conformal scalar: every energy truncation N = 1..12 of the commutator sum is nonzero at "
      "the spacelike point", all(p != 0 for p in partial))


def g_re(w):
    return (w / (QI(1) - w)).re


def g_im(w):
    return (w / (QI(1) - w)).im


for lab, z in (("spacelike", zsp), ("timelike", ztl)):
    wm = z * zeta.conj()
    wp = z * zeta
    comm_full = F(1, 4) * (g_re(wm) - g_re(wp))
    check("A6.2 completed (Abel) commutator sum sum sin(nt) sin(n chi) = 0 at the %s point "
          "(Re w/(1-w) = -1/2 on the circle; Huygens)" % lab,
          comm_full == 0 and g_re(wm) == F(-1, 2) and g_re(wp) == F(-1, 2))
acomm_full = F(1, 2) * (g_im(zeta * zsp) + g_im(zeta * zsp.conj()))
check("A6.3 the completed anticommutator sum sum cos(nt) sin(n chi) is nonzero at the spacelike point "
      "(a CAR scalar is not local)", acomm_full != 0)
p = QI(F(3, 5), F(-4, 5))            # e^{-iu/2}
pinv = p.conj()
ns_full = p / (QI(1) - p * p) + pinv / (QI(1) - pinv * pinv)
check("A6.4 2D chiral CAR field, half-odd modes (NS): completed anticommutator sum_{n in Z+1/2} e^{-inu} "
      "is exactly 0 off u = 0", ns_full == QI(0))
ns_part = [sum((qpow(p, 2 * k + 1) + qpow(pinv, 2 * k + 1) for k in range(K + 1)), QI(0))
           for K in range(0, 10)]
check("A6.5 its truncations K = 0..9 are all nonzero at the same u", all(x != QI(0) for x in ns_part))
wq = p * p                           # e^{-iu}
cur = wq / ((QI(1) - wq) * (QI(1) - wq))
check("A6.6 integer-spin chiral field (weight 1) under CAR: completed anticommutator 2 Re w/(1-w)^2 != 0 "
      "off u = 0, while the commutator (Im part) is 0", cur.re != 0 and cur.im == 0)

# ===========================================================================
# PART B. Lorentz invariance as a test (item 3)
# ===========================================================================
print("=" * 72)
print("PART B. Lorentz invariance as a test (item 3)")
print("=" * 72)

S1 = (1, -1)                                   # the atom Cl(1,1): e0, e1
va = add(scl(F(1, 2), gen(0)), scl(F(1, 2), gen(1)))      # T07 Prop mode: v (annihilates)
vs = add(scl(F(1, 2), gen(0)), scl(F(-1, 2), gen(1)))     # v^* (creates)
sig_ = sub(mul(vs, va, S1), mul(va, vs, S1))
check("B1.0 sigma = v* v - v v* = e0 e1, sigma^2 = 1, star(v) = v*",
      eq(sig_, mul(gen(0), gen(1), S1)) and eq(mul(sig_, sig_, S1), sc(1)) and eq(star(va, S1), vs))
R = add(sc(F(5, 4)), scl(F(3, 4), sig_))      # e^{lambda/2} = 2
Ri = add(sc(F(5, 4)), scl(F(-3, 4), sig_))
Adv = mul(mul(R, va, S1), Ri, S1)
Advs = mul(mul(R, vs, S1), Ri, S1)
check("B1.1 real rapidity (e^lambda = 4): Ad(R) v = v/4, Ad(R) v* = 4 v*, and the CAR is preserved",
      eq(Adv, scl(F(1, 4), va)) and eq(Advs, scl(F(4), vs)) and eq(acomm(Adv, Advs, S1), sc(1)))
check("B1.2 ... but Ad(R) is not a *-map: star(Ad(R) v) = v*/4 != Ad(R)(star v) = 4 v*",
      not eq(star(Adv, S1), Advs))
check("B1.3 R is self-adjoint and not unitary: R* = R, R* R = R^2 != 1",
      eq(star(R, S1), R) and not eq(mul(star(R, S1), R, S1), sc(1)))
# uniform boost on k planes, Fock matrices: creators c_j^dagger scale by 4
okn = True
for k in range(1, 5):
    C = jw_ops(k)
    Cd = [mdag(c) for c in C]
    Bm = mid(2 ** k)
    for j in range(k):
        Bm = mmul(Bm, Cd[j])
    BB = mmul(mdag(Bm), Bm)
    Pp = BB
    okn = okn and meq(mmul(Pp, Pp), Pp) and mtrace(Pp) == 1           # norm-one partial isometry
    Bimg = mscal(F(4) ** k, Bm)
    BBi = mmul(mdag(Bimg), Bimg)
    okn = okn and meq(BBi, mscal(F(16) ** k, Pp))                      # norm 4^k
check("B1.4 uniform real boost on k = 1..4 planes: c_1*..c_k* (norm 1) goes to 4^k c_1*..c_k* (norm 4^k); "
      "no bounded extension to the CAR C*-algebra", okn)
# imaginary rapidity: R_{i phi} = cos(phi/2) + i sin(phi/2) sigma, (cos, sin) = (3/5, 4/5)
Rc = {(): QI(F(3, 5))}
Rc[(0, 1)] = QI(0, F(4, 5))
Rci = {(): QI(F(3, 5)), (0, 1): QI(0, F(-4, 5))}
vaq = {b: QI(c) for b, c in va.items()}
vsq = {b: QI(c) for b, c in vs.items()}
Adq = mul(mul(Rc, vaq, S1), Rci, S1)
emiphi = QI(F(3, 5), F(-4, 5)) * QI(F(3, 5), F(-4, 5))
check("B1.5 imaginary rapidity: R_{i phi} is unitary (R* = R^-1) and Ad(R_{i phi}) v = e^{-i phi} v",
      eq(star(Rc, S1), Rci) and eq(mul(Rc, Rci, S1), {(): QI(1)}) and eq(Adq, scl(emiphi, vaq)))
check("B1.6 ... and is a *-map: star(Ad v) = Ad(star v)",
      eq(star(Adq, S1), mul(mul(Rc, vsq, S1), Rci, S1)))
Nq = mul(vsq, vaq, S1)
eiphi = emiphi.conj()
G = add({(): QI(1)}, scl(eiphi - QI(1), Nq))   # e^{i phi N}
check("B1.7 R_{i phi} = e^{-i phi/2} e^{i phi N}: the imaginary-rapidity rotor is the gauge flow of N",
      eq(Rc, scl(QI(F(3, 5), F(-4, 5)), G)))

Nr = mul(vs, va, S1)
check("B1.8 the real rotor is R_lambda = e^{-lambda/2} e^{lambda N} (e^{lambda/2} = 2: R = (1 + 3N)/2): the number "
      "operator's imaginary-time evolution, i.e. the KMS-strip map of the unitary flow of B1.7",
      eq(R, scl(F(1, 2), add(sc(1), scl(F(3), Nr)))))

# --- B2. su(2,2) on the attached field preserves the positive-energy module --------
okB2 = True
energy = lambda k: F(k[0] + k[1] + k[2] + k[3], 2) + 1
for al in range(4):
    for be in range(4):
        Em = [[F(int(i == be and j == al)) for j in range(4)] for i in range(4)]
        qe = qM(Em)
        for pp in mono_basis(3):
            (k0, _), = pp.d.items()
            img = qe(pp)
            # commutes with helicity
            if not (qid(img) - qe(qid(pp))).is_zero():
                okB2 = False
            for k1 in img.d:
                if energy(k1) - energy(k0) not in (F(-1), F(0), F(1)):
                    okB2 = False
                if F(k1[0] + k1[1] + k1[2] + k1[3], 2) + 1 < F(abs(k1[2] + k1[3] - k1[0] - k1[1]), 2) + 1:
                    okB2 = False
check("B2.1 every q(E_ab), a basis of u(2,2)_C, commutes with helicity, moves the energy by -1, 0 or +1 and "
      "stays in the positive-energy Fock module", okB2)

# --- B3. Thermofield Bogoliubov: HS norm = number --------------------------------------
angs = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(8, 17), F(15, 17))]
kk = len(angs)
Cops = jw_ops(2 * kk)                          # modes: a_j = 2j, atilde_j = 2j+1
Cd = [mdag(c) for c in Cops]
dim = 2 ** (2 * kk)
vac = [[F(int(i == 0))] for i in range(dim)]
psi = vac
for j, (c, s) in enumerate(angs):
    Op = madd(mscal(c, mid(dim)), mscal(s, mmul(Cd[2 * j], Cd[2 * j + 1])))
    psi = mmul(Op, psi)
norm = mmul(mdag(psi), psi)[0][0]
okann = True
for j, (c, s) in enumerate(angs):
    b = madd(mscal(c, Cops[2 * j]), mscal(-s, Cd[2 * j + 1]))
    bt = madd(mscal(c, Cops[2 * j + 1]), mscal(s, Cd[2 * j]))
    okann = okann and all(x[0] == 0 for x in mmul(b, psi)) and all(x[0] == 0 for x in mmul(bt, psi))
    okann = okann and meq(madd(mmul(b, mdag(b)), mmul(mdag(b), b)), mid(dim))
Ntot = mzero(dim)
for j in range(2 * kk):
    Ntot = madd(Ntot, mmul(Cd[j], Cops[j]))
Nexp = mmul(mdag(psi), mmul(Ntot, psi))[0][0]
HS2 = 2 * sum((s * s for (c, s) in angs), F(0))
check("B3.1 thermofield vector of 3 pairs: norm 1, annihilated by the Bogoliubov modes b_j, btilde_j "
      "(which satisfy the CAR)", norm == 1 and okann)
check("B3.2 <N_total> = 2 sum s_j^2 = Hilbert-Schmidt norm^2 of the off-diagonal Bogoliubov block",
      Nexp == HS2)
oneside = [mmul(mdag(psi), mmul(mmul(Cd[2 * j], Cops[2 * j]), psi))[0][0] for j in range(kk)]
check("B3.3 one-sided occupancy n_j = s_j^2, and n_j/(1-n_j) = (s_j/c_j)^2 is the Gibbs ratio",
      all(oneside[j] == angs[j][1] ** 2 and oneside[j] / (1 - oneside[j]) == (angs[j][1] / angs[j][0]) ** 2
          for j in range(kk)))

# --- B4. Real-time reading of the linear spectrum -------------------------------------
iS = {(0, 1): QI(0, 1)}                        # R_{i pi} = i sigma (sigma = e0 e1 in the atom)
iSi = {(0, 1): QI(0, -1)}
check("B4.1 R_{i pi} = i sigma is unitary and Ad(R_{i pi}) v = -v (the half-turn is the parity)",
      eq(mul(iS, iSi, S1), {(): QI(1)}) and eq(mul(mul(iS, vaq, S1), iSi, S1), scl(QI(-1), vaq)))
okB4 = True
for k in range(0, 6):
    Rk = {(): QI(1)}
    for _ in range(2 * k):
        Rk = mul(Rk, iS, S1)
    Rki = {(): QI(1)}
    for _ in range(2 * k):
        Rki = mul(Rki, iSi, S1)
    okB4 = okB4 and eq(mul(mul(Rk, vaq, S1), Rki, S1), vaq)          # weight k: one period is the identity
    Rh = mul(Rk, iS, S1)
    Rhi = mul(Rki, iSi, S1)
    okB4 = okB4 and eq(mul(mul(Rh, vaq, S1), Rhi, S1), scl(QI(-1), vaq))  # weight k + 1/2: the parity
check("B4.2 weight k (omega_k = kappa k): the flow over one period 2 pi/kappa is the identity on the mode; "
      "weight k + 1/2: it is the parity (k = 0..5)", okB4)
pc = QI(F(5, 13), F(-12, 13))                # e^{-i kappa v}, v not a multiple of the period
comb = QI(1) + pc / (QI(1) - pc) + pc.conj() / (QI(1) - pc.conj())
check("B4.3 the horizon anticommutator sum_{k in Z} e^{-i kappa k v} is 0 off v in (2 pi/kappa) Z",
      comb == QI(0))
check("B4.4 at v = 2 pi/kappa every phase is 1: the truncations equal 2K + 1 (the comb's tooth), so "
      "psi(v + 2 pi/kappa) = psi(v) term by term",
      all(sum((qpow(QI(1), abs(k)) for k in range(-K, K + 1)), QI(0)) == QI(2 * K + 1) for K in range(6)))

# ===========================================================================
# PART C. The odd-charge limit: the reading for T14's towers (item 4)
# ===========================================================================
print("=" * 72)
print("PART C. The odd-charge limit, the reading for T14's towers (item 4)")
print("=" * 72)

for (p_, q_) in ((2, 1), (1, 2), (1, 4), (4, 1)):
    n = p_ + q_
    Sg = tuple([1] * p_ + [-1] * q_ + [1, -1])
    e_, f_ = n, n + 1
    vv, ww = pair(e_, f_)
    om0 = sc(1)
    for i in range(n):
        om0 = mul(om0, gen(i), Sg)
    om1 = mul(mul(om0, gen(e_), Sg), gen(f_), Sg)
    pi1 = mul(gen(e_), gen(f_), Sg)
    Pi = sub(sc(1), scl(F(2), mul(vv, ww, Sg)))
    central = all(commutes(om1, gen(i), Sg) for i in range(n + 2))
    sq = mul(om1, om1, Sg)
    lemma = eq(om0, mul(om1, pi1, Sg)) and eq(pi1, Pi)
    if eq(sq, sc(1)):
        Pp = scl(F(1, 2), add(sc(1), om1))
        Pm = scl(F(1, 2), sub(sc(1), om1))
        ok = eq(mul(om0, Pp, Sg), mul(Pi, Pp, Sg)) and eq(mul(om0, Pm, Sg), neg(mul(Pi, Pm, Sg)))
        kind = "split: omega_0 = +-(-1)^N on the two summands"
    else:
        om1q = {b: QI(c) for b, c in om1.items()}
        Pp = scl(QI(F(1, 2)), add({(): QI(1)}, scl(QI(0, -1), om1q)))   # omega_1 = +i here
        Pm = scl(QI(F(1, 2)), add({(): QI(1)}, scl(QI(0, 1), om1q)))    # omega_1 = -i here
        om0q = {b: QI(c) for b, c in om0.items()}
        Piq = {b: QI(c) for b, c in Pi.items()}
        ok = (eq(mul(om1q, Pp, Sg), scl(QI(0, 1), Pp)) and
              eq(mul(om0q, Pp, Sg), scl(QI(0, 1), mul(Piq, Pp, Sg))) and
              eq(mul(om0q, Pm, Sg), scl(QI(0, -1), mul(Piq, Pm, Sg))))
        kind = "complex: omega_0 = +-i(-1)^N on the two complex summands"
    check("C1 ground Cl(%d,%d) + one plane: omega_1 central, omega_0 = omega_1 pi_1, pi_1 = 1 - 2vw = (-1)^N, "
          "and %s" % (p_, q_, kind), central and lemma and ok)

# ===========================================================================
# PART D. The path integral (item 1)
# ===========================================================================
print("=" * 72)
print("PART D. The path integral (item 1)")
print("=" * 72)

# --- D1. Grassmann variables inside the tower ----------------------------------------
ST = tuple([1, -1] * 5)                       # five planes: plane 0 the physical mode
vp, wp = pair(0, 1)
us = [pair(2 * j, 2 * j + 1)[0] for j in range(1, 5)]   # creation vectors of four further rungs
okg = all(is_zero(mul(u, u, ST)) for u in us)
okg = okg and all(anticommutes(us[i], us[j], ST) for i in range(4) for j in range(i + 1, 4))
okg = okg and all(anticommutes(u, x, ST) for u in us for x in (vp, wp))
top = sc(1)
for u in us:
    top = mul(top, u, ST)
check("D1.1 four further rungs' creation vectors square to 0, anticommute pairwise and with the physical "
      "pair, and their top product is nonzero (a faithful Grassmann algebra on 4 generators)",
      okg and not is_zero(top))

# --- D2. Exact finite slicing -----------------------------------------------------------


def grass_sig(n):
    return tuple([0] * n)


def action(M, t, eta, base=0):
    """S = sum_m psibar_m psi_m - t psibar_m psi_{m-1}, psi_0 = eta psi_M; generators
    psibar_m = base + 2(m-1), psi_m = base + 2(m-1) + 1."""
    Sx = {}
    for m in range(1, M + 1):
        pb = gen(base + 2 * (m - 1))
        ps = gen(base + 2 * (m - 1) + 1)
        Sx = add(Sx, {tuple(sorted((base + 2 * (m - 1), base + 2 * (m - 1) + 1))): F(1)})
        if m >= 2:
            prev = gen(base + 2 * (m - 2) + 1)
            c = -t
        else:
            prev = gen(base + 2 * (M - 1) + 1)
            c = -t * eta
        Sx = add(Sx, scl(c, mul(pb, prev, grass_sig(1000))))
    return Sx


def berezin(x, ngen):
    """Integral over prod_m dpsibar_m dpsi_m: (-1)^(ngen/2) times the top coefficient, the
    convention with int dpsibar dpsi exp(-a psibar psi) = a."""
    topb = tuple(range(ngen))
    return F((-1) ** (ngen // 2)) * x.get(topb, F(0))


def diff_matrix(M, t, eta):
    A = mid(M)
    for m in range(1, M):
        A[m][m - 1] = -t
    A[0][M - 1] = A[0][M - 1] + (-t * eta)
    return A


okD2 = True
okD2tr = True
for M in range(1, 6):
    for delta in (F(1, 3), F(2, 7), F(5, 4)):
        t = 1 - delta
        for eta in (-1, 1):
            Sx = action(M, t, eta)
            Z = berezin(exp_nil(neg(Sx), grass_sig(2 * M), 2 * M), 2 * M)
            dA = mdet(diff_matrix(M, t, eta))
            closed = 1 - eta * t ** M
            T = [[F(1), F(0)], [F(0), 1 - delta]]          # 1 - delta N on the mode (N = diag(0,1))
            TM = mid(2)
            for _ in range(M):
                TM = mmul(TM, T)
            Gam = [[F(1), F(0)], [F(0), F(-1)]]
            trace = mtrace(TM) if eta == -1 else mtrace(mmul(Gam, TM))
            okD2 = okD2 and Z == dA == closed
            okD2tr = okD2tr and Z == trace
check("D2.1 Berezin integral of exp(-S) = det(A) = 1 - eta (1-delta)^M for M = 1..5, delta = 1/3, 2/7, 5/4, "
      "both closures", okD2)
check("D2.2 antiperiodic closure = Tr (1 - delta N)^M, periodic closure = Tr Gamma (1 - delta N)^M, exactly at "
      "every M", okD2tr)
okfac = True
for M in (2, 3):
    t1, t2 = F(2, 3), F(5, 7)
    S1x = action(M, t1, -1, 0)
    S2x = action(M, t2, -1, 2 * M)
    Z12 = berezin(exp_nil(neg(add(S1x, S2x)), grass_sig(4 * M), 4 * M), 4 * M)
    okfac = okfac and Z12 == (1 + t1 ** M) * (1 + t2 ** M)
check("D2.3 two modes factorise: Z_12 = Z_1 Z_2 (M = 2, 3)", okfac)
# the same integral computed inside the tower (M = 2, Grassmann generators = rung vectors)
ws = [pair(2 * j, 2 * j + 1)[1] for j in range(1, 5)]
P0 = sc(1)
for j in range(4):
    P0 = mul(P0, mul(ws[j], us[j], ST), ST)    # vacuum projector of the four rungs


def tower_berezin(x):
    y = x
    for j in range(4):
        y = mul(ws[j], y, ST)
    y = mul(y, P0, ST)
    # y = c P0; read c off a blade of P0
    b0, c0 = next(iter(P0.items()))
    c = y.get(b0, F(0)) / c0
    return c if eq(y, scl(c, P0)) else None


def to_tower(x):
    out = {}
    for b, c in x.items():
        term = sc(c)
        for g in b:
            term = mul(term, us[g], ST)
        out = add(out, term)
    return out


calib = tower_berezin(to_tower(exp_nil(neg(action(2, F(1, 2), 0)), grass_sig(4), 4)))
abst = berezin(exp_nil(neg(action(2, F(1, 2), 0)), grass_sig(4), 4), 4)
sgn = calib / abst
okT = sgn in (F(1), F(-1))
for t in (F(2, 3), F(-1, 4)):
    for eta in (-1, 1):
        xx = exp_nil(neg(action(2, t, eta)), grass_sig(4), 4)
        okT = okT and tower_berezin(to_tower(xx)) == sgn * (1 - eta * t ** 2)
check("D2.4 inside the tower (rung vectors as Grassmann variables, Berezin = w...w x P0): the same values "
      "1 - eta t^2 at M = 2, one overall sign fixed once", okT)
# the finite-slicing two-point function: the Matsubara dichotomy in its quoted (two-point) form
okG = True
okper = True
for M in (2, 3, 4):
    for t in (F(2, 3), F(-1, 4)):
        for eta in (-1, 1):
            Sx = action(M, t, eta)
            ex = exp_nil(neg(Sx), grass_sig(2 * M), 2 * M)
            Z = berezin(ex, 2 * M)
            T = [[F(1), F(0)], [F(0), t]]
            a = [[F(0), F(1)], [F(0), F(0)]]
            ad = [[F(0), F(0)], [F(1), F(0)]]
            Gam = [[F(1), F(0)], [F(0), F(-1)]] if eta == 1 else mid(2)
            Tp = [mid(2)]
            for _ in range(M):
                Tp.append(mmul(Tp[-1], T))
            Zop = mtrace(mmul(Gam, Tp[M]))
            Gby = {}
            for m in range(1, M + 1):
                for n in range(1, M + 1):
                    ins = mul(gen(2 * (m - 1) + 1), gen(2 * (n - 1)), grass_sig(2 * M))   # psi_m psibar_n
                    G = berezin(mul(ins, ex, grass_sig(2 * M)), 2 * M) / Z
                    j = m - n
                    if j >= 0:
                        op = mtrace(mmul(Gam, mmul(Tp[M - j], mmul(a, mmul(Tp[j], ad))))) / Zop
                    else:   # fermionic time ordering: the creator acts first, one sign
                        op = -mtrace(mmul(Gam, mmul(Tp[M + j], mmul(ad, mmul(Tp[-j], a))))) / Zop
                    okG = okG and G == op
                    if j in Gby:
                        okG = okG and Gby[j] == G           # depends on m - n only
                    Gby[j] = G
            for j in range(1, M):
                okper = okper and Gby[j - M] == eta * Gby[j]
check("D2.7 two-point form: <psi_m psibar_n> from the Berezin integral depends on m - n only and equals the "
      "time-ordered operator function (Gamma inserted for the periodic closure, one ordering sign for "
      "m < n), M = 2..4", okG)
check("D2.8 from the computed values, G(j - M) = eta G(j) for 0 < j < M: antiperiodic for the trace, periodic "
      "for the supertrace, the Matsubara dichotomy in the two-point form T05 Rem. rem:spinstructure quotes", okper)

# finite-M occupancy and the limit
okocc = True
for M in (1, 2, 5, 10):
    for x in (F(1), F(3, 2)):
        t = 1 - x / M
        T = [[F(1), F(0)], [F(0), t]]
        TM = mid(2)
        for _ in range(M):
            TM = mmul(TM, T)
        Nn = [[F(0), F(0)], [F(0), F(1)]]
        n_tr = mtrace(mmul(Nn, TM)) / mtrace(TM)
        okocc = okocc and n_tr == t ** M / (1 + t ** M)
check("D2.5 finite-M occupancy <N>_M = t^M/(1 + t^M), t = 1 - beta eps/M (M = 1, 2, 5, 10)", okocc)
# bracket e^{-1} by alternating partial sums and check 1/(e+1) against n_M at M = 1000
lo = sum((F((-1) ** k, factorial(k)) for k in range(0, 14)), F(0))   # ends on a negative term
hi = sum((F((-1) ** k, factorial(k)) for k in range(0, 13)), F(0))
tM = (1 - F(1, 1000)) ** 1000
check("D2.6 e^{-1} bracketed exactly, lo < hi, and (1 - 1/M)^M lies in [lo (1 - 1/M), hi] at M = 1000 "
      "(the standard bound e^{-x}(1 - x^2/M) <= (1-x/M)^M <= e^{-x})",
      lo < hi and lo * (1 - F(1, 1000)) <= tM <= hi)

# --- D3. Antiperiodicity is the parity; the full turn does not supply the sign ----------
Gq = sub(sc(1), scl(F(2), mul(vs, va, S1)))   # Gamma = 1 - 2N, N = v* v
check("D3.1 Gamma = 1 - 2 v* v = -sigma (T05 Prop. prop:statistics) and Gamma anticommutes with v, v*",
      eq(Gq, neg(sig_)) and anticommutes(Gq, va, S1) and anticommutes(Gq, vs, S1))
R2 = mul(iS, iS, S1)
check("D3.2 the full Euclidean turn R_{2 pi i} = (i sigma)^2 = -1 on the module, and Ad(R_{2 pi i}) v = v: "
      "the turn fixes the mode operators", eq(R2, {(): QI(-1)}) and eq(mul(mul(R2, vaq, S1), {(): QI(-1)}, S1), vaq))
okD3 = True
for xg in (F(9, 16), F(1, 3)):
    Zu = 1 + xg
    Zg = 1 - xg
    okD3 = okD3 and Zu == mtrace([[F(1), F(0)], [F(0), xg]]) and Zg == mtrace([[F(1), F(0)], [F(0), -xg]])
check("D3.3 the two closures are T05's two functionals: Z = 1 + x (ungraded, the state) and Z_Gamma = 1 - x "
      "(graded, twisted), consistent with D2.2 in the limit t^M -> x", okD3)

# --- D4. The circle fixes the Matsubara set, not the spectrum ----------------------------
okS = True
okchar = True
okdet = True
X = RF.var()
for M in range(1, 7):
    for eta in (-1, 1):
        Sm = mzero(M)
        for m in range(1, M):
            Sm[m][m - 1] = F(1)
        Sm[0][M - 1] = F(eta)
        SM = mid(M)
        for _ in range(M):
            SM = mmul(SM, Sm)
        okS = okS and meq(SM, mscal(F(eta), mid(M)))
        XI = [[(X if i == j else RF.const(0)) - RF.const(Sm[i][j]) for j in range(M)] for i in range(M)]
        cp = rf_mat_det(XI)
        target = RF([F(-eta)] + [F(0)] * (M - 1) + [F(1)])
        okchar = okchar and cp.eqrf(target)
        IA = [[RF.const(int(i == j)) - X * RF.const(Sm[i][j]) for j in range(M)] for i in range(M)]
        dt = rf_mat_det(IA)
        target2 = RF([F(1)] + [F(0)] * (M - 1) + [F(-eta)])
        okdet = okdet and dt.eqrf(target2)
check("D4.1 the one-step shift with closure eta satisfies S^M = eta (M = 1..6): its spectrum is the M-th roots "
      "of eta, and S contains no energy", okS)
check("D4.2 det(x - S) = x^M - eta exactly (M = 1..6): the antiperiodic set is zeta^M = -1", okchar)
check("D4.3 det(1 - t S) = 1 - eta t^M as a polynomial identity in t: the energy enters only through t, "
      "never through the Matsubara set", okdet)
z2 = [QI(0, 1), QI(0, -1)]
check("D4.4 M = 2 explicitly: the antiperiodic roots are +-i and (1 - t i)(1 + t i) = 1 + t^2 at t = 2/3",
      (QI(1) - QI(F(2, 3)) * z2[0]) * (QI(1) - QI(F(2, 3)) * z2[1]) == QI(1 + F(4, 9)))

# ---------------------------------------------------------------------------
print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f in FAILURES:
        print("  " + f)
    sys.exit(1)
print("ALL CHECKS PASSED")
