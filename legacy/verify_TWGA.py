#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_TWGA.py: exact checks for "The twistor route in geometric algebra" (16 October 2026).
Preregistration: preregistration_TWGA_2026-10-16.md. Findings: TWGA_findings_2026-10-16.md.

Real Clifford algebras only (GA.py, Fraction coefficients); no complex numbers are used in any
construction. Gaussian rationals (GA.QI) appear only in E4.2, to produce exact cosines and sines
at rational points of the unit circle, which are then used as real coefficients.

Parts: E1 twistors in Cl(2,4) with their own i; E2 massless fields in the spacetime algebra;
E3 the field's complex structure; E4 the CAR in geometric algebra.
"""

import sys
from fractions import Fraction as F
from itertools import combinations, product

import GA
from GA import (FAILURES, mul, add, neg, sub, sc, gen, reverse, eq, is_zero, commutes,
                anticommutes, all_blades, congruence_signature, rank_of_vectors, blade_mul, QI)

NCHECKS = [0]


def check(label, ok):
    NCHECKS[0] += 1
    GA.check(label, ok)


def scl(c, x):
    c = F(c)
    return {b: c * v for b, v in x.items()} if c != 0 else {}


def comm(x, y, s):
    return sub(mul(x, y, s), mul(y, x, s))


def blade(t):
    return {tuple(t): F(1)}


def star(x, s):
    """T03 Lemma lem:cstar on real elements: x* = x (square +1), x* = -x (square -1) on frame
    generators, extended as an antiautomorphism."""
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


# --- exact linear algebra over Q ------------------------------------------------

def nullspace(rows, ncols):
    """Basis of {c : M c = 0}, M given as a list of rows (Fraction)."""
    m = [list(r) for r in rows]
    piv_cols = []
    row = 0
    for col in range(ncols):
        piv = next((r for r in range(row, len(m)) if m[r][col] != 0), None)
        if piv is None:
            continue
        m[row], m[piv] = m[piv], m[row]
        pv = m[row][col]
        m[row] = [a / pv for a in m[row]]
        for r in range(len(m)):
            if r != row and m[r][col] != 0:
                f = m[r][col]
                m[r] = [a - f * b for a, b in zip(m[r], m[row])]
        piv_cols.append(col)
        row += 1
        if row == len(m):
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -m[i][fc]
        basis.append(v)
    return basis


def vec(x, blades):
    return [x.get(b, F(0)) for b in blades]


def from_vec(c, elems):
    out = {}
    for ci, e in zip(c, elems):
        if ci != 0:
            out = add(out, scl(ci, e))
    return out


def solve_coords(y, elems, blades):
    """Coordinates of y in the span of elems (exact), or None."""
    cols = [vec(e, blades) for e in elems]
    n = len(elems)
    rows = [[cols[j][i] for j in range(n)] + [-y.get(blades[i], F(0))] for i in range(len(blades))]
    ns = nullspace(rows, n + 1)
    for v in ns:
        if v[n] != 0:
            return [a / v[n] for a in v[:n]]
    return None


def span_rank(elems, blades):
    return rank_of_vectors([vec(e, blades) for e in elems]) if elems else 0


# ===========================================================================
# E1. Twistors in Cl(2,4), with their own i
# ===========================================================================
print("=" * 72)
print("E1. Twistors in Cl(2,4), with their own i")
print("=" * 72)

S4 = (1, -1, -1, -1)
S6 = (1, -1, -1, -1, 1, -1)                 # gamma_0..3, e_+, e_-
I4 = blade((0, 1, 2, 3))
Ebv = blade((4, 5))
I6 = blade((0, 1, 2, 3, 4, 5))


def even_blades(n):
    return [b for b in all_blades(n) if len(b) % 2 == 0]


def centre_of_even(n, s):
    eb = even_blades(n)
    gens = [blade(b) for b in eb if len(b) == 2]
    rows = []
    for B in gens:
        imgs = [comm(blade(b), B, s) for b in eb]
        allb = sorted({bb for im in imgs for bb in im})
        for bb in allb:
            rows.append([im.get(bb, F(0)) for im in imgs])
    ns = nullspace(rows, len(eb))
    return [from_vec(v, [blade(b) for b in eb]) for v in ns]


Z4 = centre_of_even(4, S4)
check("E1.1 the centre of Cl+(1,3) is 2-dimensional and contains 1 and I4; I4^2 = -1",
      len(Z4) == 2 and span_rank(Z4 + [sc(1), I4], [(), (0, 1, 2, 3)]) == 2
      and eq(mul(I4, I4, S4), sc(-1)))
Z6 = centre_of_even(6, S6)
check("E1.2a the centre of Cl+(2,4) is 2-dimensional, spanned by 1 and I6; I6^2 = -1",
      len(Z6) == 2 and span_rank(Z6 + [sc(1), I6], [(), (0, 1, 2, 3, 4, 5)]) == 2
      and eq(mul(I6, I6, S6), sc(-1)))
check("E1.2b I6 = I4 E, with E = e+ e- the ascent plane's bivector, E^2 = +1, [I4, E] = 0",
      eq(I6, mul(I4, Ebv, S6)) and eq(mul(Ebv, Ebv, S6), sc(1)) and commutes(I4, Ebv, S6))

# --- E1.3 the twistor ideal ---
EB6 = even_blades(6)
ALLB6 = all_blades(6)
g4 = [blade(b) for b in EB6 if len(b) == 4 and eq(mul(blade(b), blade(b), S6), sc(1))]
P = None
for Q1, Q2 in combinations(g4, 2):
    if not commutes(Q1, Q2, S6):
        continue
    PP = mul(scl(F(1, 2), add(sc(1), Q1)), scl(F(1, 2), add(sc(1), Q2)), S6)
    if eq(mul(PP, PP, S6), PP) and eq(reverse(PP), PP):
        ideal = [mul(blade(b), PP, S6) for b in EB6]
        if span_rank(ideal, ALLB6) == 8:
            P, Q1s, Q2s = PP, Q1, Q2
            break
check("E1.3a a reversion-invariant idempotent P = (1 + Q1)(1 + Q2)/4 (commuting 4-blades) has an "
      "8-dimensional even left ideal S = Cl+(2,4) P", P is not None)
# a basis of S
cand = [mul(blade(b), P, S6) for b in EB6]
Sb = []
for c in cand:
    if span_rank(Sb + [c], ALLB6) > len(Sb):
        Sb.append(c)
check("E1.3b S is I6-stable (complex dimension 4 with i = I6)",
      len(Sb) == 8 and all(solve_coords(mul(I6, z, S6), Sb, ALLB6) is not None for z in Sb))


def lmat(a):
    """8 x 8 matrix of left multiplication by even a on S (columns = images of basis)."""
    cols = [solve_coords(mul(a, z, S6), Sb, ALLB6) for z in Sb]
    return [[cols[j][i] for j in range(8)] for i in range(8)]


Lmats = [lmat(blade(b)) for b in EB6]
flat = [[x for r in M for x in r] for M in Lmats]
check("E1.3c Cl+(2,4) acts faithfully on S: the 32 even blades give 32 independent 8 x 8 matrices "
      "(Cl+(2,4) = M_4(C), S = C^4)", rank_of_vectors(flat) == 32)
gensM = [lmat(blade(b)) for b in EB6 if len(b) == 2]
rows = []
for G in gensM:
    for i in range(8):
        for j in range(8):
            # (C G - G C)_{ij} = sum_k C_ik G_kj - G_ik C_kj ; unknown C_{ab} at index 8a + b
            r = [F(0)] * 64
            for k in range(8):
                r[8 * i + k] += G[k][j]
                r[8 * k + j] -= G[i][k]
            rows.append(r)
comm_basis = nullspace(rows, 64)
LI6 = lmat(I6)
Id8 = [[F(int(i == j)) for j in range(8)] for i in range(8)]
check("E1.3d the commutant of the twistor action on S is 2-dimensional, spanned by 1 and left I6: "
      "every complex structure on S commuting with it is +-I6",
      len(comm_basis) == 2 and rank_of_vectors(comm_basis + [[x for r in Id8 for x in r],
                                                              [x for r in LI6 for x in r]]) == 2)

# --- E1.4 the twistor form ---
PCP = [mul(mul(P, blade(b), S6), P, S6) for b in EB6]
check("E1.4a P Cl+ P is 2-dimensional, spanned by P and I6 P", span_rank(PCP, ALLB6) == 2 and
      span_rank(PCP + [P, mul(I6, P, S6)], ALLB6) == 2)
I6P = mul(I6, P, S6)


def h(z1, z2):
    c = solve_coords(mul(reverse(z1), z2, S6), [P, I6P], ALLB6)
    return c                                   # [a, b]: h = a + b i, i = I6


H = [[h(Sb[i], Sb[j]) for j in range(8)] for i in range(8)]
herm = all(H[i][j][0] == H[j][i][0] and H[i][j][1] == -H[j][i][1] for i in range(8) for j in range(8))
check("E1.4b h is Hermitian: Re h symmetric, Im h antisymmetric", herm)
okses = True
for i in range(8):
    for j in range(8):
        a, b = h(mul(I6, Sb[i], S6), Sb[j])
        a0, b0 = H[i][j]
        okses = okses and (a, b) == (b0, -a0)            # h(i Z1, Z2) = -i h(Z1, Z2)
check("E1.4c h is antilinear in the first slot for i = I6 (reversion negates I6)", okses)
ReH = [[H[i][j][0] for j in range(8)] for i in range(8)]
sigH = congruence_signature(ReH)
check("E1.4d the real form Re h has signature (4,4,0): h has complex signature (2,2), the twistor form",
      sigH == (4, 4, 0))
rotors = [add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1)))),          # a boost
          add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2)))),          # a rotation
          add(sc(F(5, 4)), scl(F(3, 4), blade((0, 4)))),          # an e+ plane rotation (square -1?)
          add(sc(F(1)), scl(F(1, 2), mul(add(gen(4), gen(5)), gen(1), S6)))]   # a translation
rotors = [R for R in rotors if eq(mul(R, reverse(R), S6), sc(1))]
okinv = all(h(mul(R, Sb[i], S6), mul(R, Sb[j], S6)) == H[i][j]
            for R in rotors for i in range(8) for j in range(8))
check("E1.4e h is invariant under %d sample Spin(2,4) rotors (boost, rotation, translation)" % len(rotors),
      okinv and len(rotors) >= 3)

# --- E1.5 lines ---
ninf = add(gen(4), gen(5))
n0 = scl(F(1, 2), sub(gen(5), gen(4)))
check("E1.5a n_inf, n_0 null with n_0 . n_inf = -1",
      is_zero(mul(ninf, ninf, S6)) and is_zero(mul(n0, n0, S6))
      and eq(scl(F(1, 2), add(mul(n0, ninf, S6), mul(ninf, n0, S6))), sc(-1)))


def xvec(x):
    return add(*[scl(x[m], gen(m)) for m in range(4)])


def sq4(x):
    return x[0] ** 2 - x[1] ** 2 - x[2] ** 2 - x[3] ** 2


def Xpt(x):
    return add(n0, xvec(x), scl(sq4(x) / 2, ninf))


def Tx(x):
    return add(sc(1), scl(F(1, 2), mul(ninf, xvec(x), S6)))


xs = [(F(1), F(2), F(3), F(1)), (F(2), F(1, 3), F(-1), F(1, 2)), (F(1), F(0), F(0), F(0))]
check("E1.5b T_x = 1 + n_inf x/2 is a rotor and T_x n_0 T_x~ = X(x) = n_0 + x + x^2 n_inf/2 (null)",
      all(eq(mul(Tx(x), reverse(Tx(x)), S6), sc(1)) and eq(mul(mul(Tx(x), n0, S6), reverse(Tx(x)), S6), Xpt(x))
          and is_zero(mul(Xpt(x), Xpt(x), S6)) for x in xs))


def kernel_in_S(Y):
    imgs = [mul(Y, z, S6) for z in Sb]
    allb = sorted({bb for im in imgs for bb in im})
    rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, Sb) for v in nullspace(rws, 8)] if rws else list(Sb)


L0 = kernel_in_S(n0)
Linf = kernel_in_S(ninf)
okl = len(L0) == 4 and len(Linf) == 4
for x in xs:
    Lx = kernel_in_S(Xpt(x))
    TL0 = [mul(Tx(x), z, S6) for z in L0]
    okl = okl and len(Lx) == 4 and span_rank(Lx + TL0, ALLB6) == 4
check("E1.5c every line L_x = ker X(x) in S has real dimension 4 (complex 2) and L_x = T_x L_0", okl)
check("E1.5d control: a non-null vector (e_+) annihilates nothing in S", kernel_in_S(gen(4)) == [])
okinc = True
for x in xs:
    for p in L0:
        Z = mul(Tx(x), p, S6)
        om = sub(Z, p)
        okinc = okinc and eq(om, scl(F(1, 2), mul(mul(ninf, xvec(x), S6), p, S6))) and is_zero(mul(ninf, om, S6))
check("E1.5e GA incidence: Z = T_x pi = pi + omega with omega = (n_inf x/2) pi in L_inf; no explicit i",
      okinc)

# --- E1.6 the two halves ---
eps = None
okE = True
for z in L0:
    Ez = mul(Ebv, z, S6)
    if eq(Ez, z):
        e_ = 1
    elif eq(Ez, neg(z)):
        e_ = -1
    else:
        okE = False
        e_ = 0
    eps = e_ if eps is None else eps
    okE = okE and e_ == eps
okEinf = all(eq(mul(Ebv, z, S6), scl(-eps, z)) for z in Linf)
check("E1.6a left E is a fixed sign eps = %s on L_0 and -eps on L_inf" % eps, okE and okEinf)
check("E1.6b S = L_0 (+) L_inf", span_rank(L0 + Linf, ALLB6) == 8)
lor = [add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1)))), add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2))))]
check("E1.6c L_0 and L_inf are Lorentz-invariant (Spin(1,3) rotors preserve both kernels)",
      all(is_zero(mul(n0, mul(R, z, S6), S6)) for R in lor for z in L0) and
      all(is_zero(mul(ninf, mul(R, z, S6), S6)) for R in lor for z in Linf))
check("E1.6d I6 = eps I4 on L_0 and I6 = -eps I4 on L_inf: the twistor's i is the spacetime "
      "pseudoscalar on the spinors at a point, with opposite signs on the two halves",
      all(eq(mul(I6, z, S6), scl(eps, mul(I4, z, S6))) for z in L0) and
      all(eq(mul(I6, z, S6), scl(-eps, mul(I4, z, S6))) for z in Linf))

# --- E1.7 the factor i ---
iso = all(h(a, b) == [F(0), F(0)] for a in L0 for b in L0) and \
      all(h(a, b) == [F(0), F(0)] for a in Linf for b in Linf)
check("E1.7a L_0 and L_inf are h-isotropic (null halves of the twistor form)", iso)
oka = True
sigs = {}
for lab, x in (("timelike", (F(1), F(0), F(0), F(0))), ("timelike2", (F(3), F(1), F(2), F(1))),
               ("null", (F(1), F(1), F(0), F(0))), ("spacelike", (F(0), F(1), F(0), F(0)))):
    W = scl(F(1, 2), mul(ninf, xvec(x), S6))
    q = [[h(mul(W, L0[i], S6), L0[j]) for j in range(4)] for i in range(4)]
    oka = oka and all(q[i][j][0] == -q[j][i][0] and q[i][j][1] == q[j][i][1] for i in range(4) for j in range(4))
    sigs[lab] = congruence_signature([[q[i][j][1] for j in range(4)] for i in range(4)])
check("E1.7b q_x(pi1, pi2) = h((n_inf x/2) pi1, pi2) is anti-Hermitian on L_0 for real x: q_x = i H_x "
      "with H_x Hermitian, i = I6 (Penrose's i in omega = i x pi)", oka)
check("E1.7c H_x is definite for timelike x, rank 2 (complex 1) for null x, indefinite for spacelike x: "
      "%s" % sigs,
      sigs["timelike"] in ((4, 0, 0), (0, 4, 0)) and sigs["timelike2"] in ((4, 0, 0), (0, 4, 0))
      and sigs["null"][2] == 2 and sigs["spacelike"] == (2, 2, 0))


def det_q(M):
    A = [list(r) for r in M]
    n = len(A)
    d = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


ratios = []
for x in ((F(1), F(0), F(0), F(0)), (F(3), F(1), F(2), F(1)), (F(1), F(2), F(1, 2), F(-1)), (F(2), F(-1), F(1, 3), F(1))):
    W = scl(F(1, 2), mul(ninf, xvec(x), S6))
    Hm = [[h(mul(W, L0[i], S6), L0[j])[1] for j in range(4)] for i in range(4)]
    ratios.append(det_q(Hm) / sq4(x) ** 2)
check("E1.7d det of the real 4 x 4 matrix of H_x is a fixed constant times (x^2)^2 (constant %s at four "
      "points): H_x is Penrose's Hermitian x^{AA'} with det x^{AA'} proportional to x^2, so the incidence form "
      "is the numerator of the spin-1/2 two-point kernel of E2.1" % ratios[0],
      len(set(ratios)) == 1 and ratios[0] != 0)

# ===========================================================================
# E2. Massless fields in the spacetime algebra
# ===========================================================================
print("=" * 72)
print("E2. Massless fields in the spacetime algebra")
print("=" * 72)


class Poly(object):
    def __init__(self, d=None):
        self.d = {k: v for k, v in (d or {}).items() if v != 0}

    @staticmethod
    def var(i):
        e = [0, 0, 0, 0]
        e[i] = 1
        return Poly({tuple(e): F(1)})

    @staticmethod
    def const(c):
        return Poly({(0, 0, 0, 0): F(c)})

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, F(0)) + v
        return Poly(d)

    def __neg__(self):
        return Poly({k: -v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        if not isinstance(o, Poly):
            return Poly({k: o * v for k, v in self.d.items()})
        d = {}
        for k1, v1 in self.d.items():
            for k2, v2 in o.d.items():
                k = tuple(a + b for a, b in zip(k1, k2))
                d[k] = d.get(k, F(0)) + v1 * v2
        return Poly(d)

    def deriv(self, i):
        d = {}
        for k, v in self.d.items():
            if k[i]:
                kk = list(k)
                kk[i] -= 1
                d[tuple(kk)] = d.get(tuple(kk), F(0)) + v * k[i]
        return Poly(d)

    def neg_arg(self):
        return Poly({k: v * (-1) ** sum(k) for k, v in self.d.items()})

    def zero(self):
        return not self.d


# multivector-valued polynomials: {blade: Poly}
def mvp_from_mv(a):
    return {b: Poly.const(c) for b, c in a.items()}


def mvp_add(*xs):
    out = {}
    for x in xs:
        for b, p in x.items():
            out[b] = out.get(b, Poly()) + p
    return {b: p for b, p in out.items() if not p.zero()}


def mvp_mul(x, y, s=S4):
    out = {}
    for b1, p1 in x.items():
        for b2, p2 in y.items():
            c, b = blade_mul(b1, b2, s)
            if c != 0:
                out[b] = out.get(b, Poly()) + (p1 * p2) * c
    return {b: p for b, p in out.items() if not p.zero()}


def mvp_scale(x, p):
    return {b: q * p for b, q in x.items() if not (q * p).zero()}


def mvp_deriv(x, i):
    return {b: p.deriv(i) for b, p in x.items() if not p.deriv(i).zero()}


def mvp_zero(x):
    return all(p.zero() for p in x.values())


def mvp_neg_arg(x):
    return {b: p.neg_arg() for b, p in x.items()}


xv = {(m,): Poly.var(m) for m in range(4)}                    # x = x^mu gamma_mu
Dq = Poly.var(0) * Poly.var(0) - Poly.var(1) * Poly.var(1) - Poly.var(2) * Poly.var(2) - Poly.var(3) * Poly.var(3)
recip = [F(1), F(-1), F(-1), F(-1)]                            # gamma^mu = recip_mu gamma_mu


def nabla_kernel_numerator(N, k):
    """Numerator over D^(k+1) of nabla (N / D^k), nabla = gamma^mu d_mu acting from the left."""
    tot = {}
    for m in range(4):
        term = mvp_add(mvp_scale(mvp_deriv(N, m), Dq), mvp_scale(N, Dq.deriv(m) * F(-k)))
        tot = mvp_add(tot, mvp_mul({(m,): Poly.const(recip[m])}, term))
    return tot


psi0 = {(): F(2), (0, 1): F(-1), (1, 3): F(3), (2, 3): F(1, 2), (0, 1, 2, 3): F(5)}
Nw = mvp_mul(xv, mvp_from_mv(psi0))
check("E2.1 nabla (x psi_0 / (x^2)^2) = 0 for a generic constant even psi_0 (massless spin 1/2)",
      mvp_zero(nabla_kernel_numerator(Nw, 2)))
Nw_even = mvp_mul(Nw, {(0,): Poly.const(1)})
check("E2.1b (post-review) x psi_0 is odd; the Hestenes (even) form is x psi_0 gamma_0 / (x^2)^2, even and "
      "also a solution", all(len(b) % 2 == 1 for b in Nw) and all(len(b) % 2 == 0 for b in Nw_even)
      and mvp_zero(nabla_kernel_numerator(Nw_even, 2)))
Bc = {(0, 1): F(1), (0, 2): F(-2), (1, 2): F(3), (2, 3): F(1, 3), (1, 3): F(-1, 2), (0, 3): F(2)}
Nm = mvp_mul(mvp_mul(xv, mvp_from_mv(Bc)), xv)
okgr = all(len(b) == 2 for b in Nm)
res3 = mvp_zero(nabla_kernel_numerator(Nm, 3))
res2 = mvp_zero(nabla_kernel_numerator(Nm, 2))
check("E2.2 x B x is a bivector and nabla (x B x / (x^2)^3) = 0 for a generic constant bivector B "
      "(massless spin 1); exponent 2 fails (control)", okgr and res3 and not res2)
Ns = {(): Poly.const(1)}
d1 = nabla_kernel_numerator(Ns, 1)                     # numerator over D^2 of nabla(1/D)
d2 = nabla_kernel_numerator(d1, 2)                     # nabla of (d1 / D^2)
check("E2.3a s = 0: nabla^2 (1/x^2) = 0 off the cone (the wave equation, as nabla twice)",
      mvp_zero(d2))
check("E2.3b exchange parity: N(-x) = -N for x psi_0 (s = 1/2), +N for x B x (s = 1), and x^2 even: "
      "the spin-s propagator carries 2s factors of the separation vector",
      mvp_zero(mvp_add(mvp_neg_arg(Nw), Nw)) and mvp_zero(mvp_add(mvp_neg_arg(Nm), {b: -p for b, p in Nm.items()}))
      and (Dq.neg_arg() - Dq).zero())
okj = all(eq(mul(mul(I4, gen(m), S4), neg(I4), S4), neg(gen(m))) for m in range(4))
okjb = all(eq(mul(mul(I4, blade(b), S4), neg(I4), S4), blade(b)) for b in combinations(range(4), 2))
check("E2.4a x -> -x is Ad(I4) on vectors (I4^-1 = -I4), and Ad(I4) fixes every bivector", okj and okjb)
Rj = add(sc(F(3, 5)), scl(F(4, 5), I4))
Rji = add(sc(F(3, 5)), scl(F(-4, 5), I4))
img = mul(mul(Rj, gen(1), S4), Rji, S4)
cj, sj = F(3, 5), F(4, 5)
a_, b_ = cj * cj - sj * sj, 2 * cj * sj
ph = QI(a_, b_) * QI(a_, b_)
check("E2.4b PREREGISTERED CLAIM REFUTED (review): Ad(c + s I4) multiplies every vector by the phase "
      "(c^2 - s^2) - 2cs I4, so it rescales z.z by %s (not 1): a complex dilation, not a complex Lorentz "
      "transformation, hence not Jost's path" % ph,
      eq(img, add(scl(a_, gen(1)), scl(-b_, mul(gen(1), I4, S4)))) and ph != QI(1))
# corrected path, in Cl+(2,4) acting on twistor space (post-review)
Pi_ = scl(F(1, 2), sub(sc(1), Ebv))
B12 = blade((1, 2))
check("E2.4c (post-review) Pi = (1 - E)/2 is an idempotent commuting with gamma_1 gamma_2, and it is the "
      "projector onto L_inf in S (zero on L_0)",
      eq(mul(Pi_, Pi_, S6), Pi_) and commutes(Pi_, B12, S6) and all(is_zero(mul(Pi_, z, S6)) for z in L0)
      and all(eq(mul(Pi_, z, S6), z) for z in Linf))


def Rpath(c, s_):
    return add(sub(sc(1), Pi_), mul(Pi_, add(sc(c), scl(s_, B12)), S6))


check("E2.4d (post-review) the path R(theta) = (1 - Pi) + Pi exp(theta gamma_1 gamma_2), a 2 pi rotation of "
      "one chirality only, ends at R(pi) = E, the ascent plane's bivector",
      eq(Rpath(F(-1), F(0)), Ebv))
okPT = all(eq(mul(mul(Ebv, Xpt(x), S6), Ebv, S6), neg(Xpt(tuple(-t for t in x)))) for x in xs)
check("E2.4e (post-review) Ad(E) X(x) = -X(-x): on the conformal model the total inversion x -> -x is "
      "conjugation by E", okPT)
okJ = True
for x in xs[:2]:
    R_ = Rpath(cj, sj)
    Ri_ = Rpath(cj, -sj)
    W = scl(F(1, 2), mul(ninf, xvec(x), S6))
    xp = mul(add(sc(cj), scl(sj, B12)), xvec(x), S6)            # x' = (c + s gamma_1 gamma_2) x
    for p in L0:
        lhs = mul(mul(mul(R_, W, S6), Ri_, S6), p, S6)
        rhs = scl(F(1, 2), mul(mul(ninf, xp, S6), p, S6))
        okJ = okJ and eq(lhs, rhs)
    u = {b: c for b, c in xp.items() if len(b) == 1}
    t = {b: c for b, c in xp.items() if len(b) == 3}
    w = neg(mul(I4, t, S4))                                      # t = I4 w
    okJ = okJ and all(len(b) == 1 for b in w) and not is_zero(w) and eq(add(u, mul(I4, w, S4)), xp)
    uu = mul(u, u, S4).get((), F(0))
    ww = mul(w, w, S4).get((), F(0))
    uw = (scl(F(1, 2), add(mul(u, w, S4), mul(w, u, S4)))).get((), F(0))
    okJ = okJ and uu - ww == sq4(x) and uw == 0
check("E2.4f (post-review) at an intermediate point of the path the incidence operator of x goes to that of "
      "x' = (c + s gamma_1 gamma_2) x = u + I4 w with w != 0: a complex point (off the real points) with "
      "u^2 - w^2 = x^2 and u.w = 0, so z.z is preserved: Jost's complex Lorentz path", okJ)

# ===========================================================================
# E3. The field's complex structure is the pseudoscalar
# ===========================================================================
print("=" * 72)
print("E3. The field's complex structure is the pseudoscalar")
print("=" * 72)

kk = add(gen(0), gen(3))                                 # null, along gamma_3
B4 = [blade(b) for b in combinations(range(4), 2)]
EV4 = [blade(b) for b in all_blades(4) if len(b) % 2 == 0]
ALL4 = all_blades(4)


def ker_left(k, basis):
    imgs = [mul(k, b, S4) for b in basis]
    allb = sorted({bb for im in imgs for bb in im})
    rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, basis) for v in nullspace(rws, len(basis))]


Kf = ker_left(kk, B4)
check("E3.1a the null bivectors annihilated by k = gamma_0 + gamma_3 form a 2-dimensional space, "
      "stable under I4 (so V_k = {(f, g)} has real dimension 4)",
      len(Kf) == 2 and all(solve_coords(mul(I4, f, S4), Kf, ALL4) is not None for f in Kf))
# sectors: J(f,g) = (-g, f); D(f,g) = (I4 f, I4 g)
okJD = True
for f in Kf:
    g = neg(mul(I4, f, S4))                              # sector J = D: g = -I4 f
    Jfg = (neg(g), f)
    Dfg = (mul(I4, f, S4), mul(I4, g, S4))
    okJD = okJD and eq(Jfg[0], Dfg[0]) and eq(Jfg[1], Dfg[1])
    g2 = mul(I4, f, S4)                                  # sector J = -D: g = I4 f
    Jfg2 = (neg(g2), f)
    Dfg2 = (mul(I4, f, S4), mul(I4, g2, S4))
    okJD = okJD and eq(Jfg2[0], neg(Dfg2[0])) and eq(Jfg2[1], neg(Dfg2[1]))
check("E3.1b V_k splits as {g = -I4 f} (J = D) plus {g = I4 f} (J = -D), each of real dimension 2", okJD)
c, s = F(3, 5), F(4, 5)
Rr = add(sc(c), scl(s, blade((1, 2))))                  # rotation about gamma_3
Rri = add(sc(c), scl(-s, blade((1, 2))))
cth, sth = c * c - s * s, 2 * c * s
hsign = None
okh = True
for f in Kf:
    rf = mul(mul(Rr, f, S4), Rri, S4)
    for hs in (1, -1):
        if eq(rf, add(scl(cth, f), scl(hs * sth, mul(I4, f, S4)))):
            hsign = hs if hsign is None else hsign
            okh = okh and hs == hsign
            break
    else:
        okh = False
check("E3.1c a rotation about the propagation direction acts on every null f as cos(theta) + h sin(theta) "
      "I4 with one sign h = %s: exp(h theta J) on the sector J = D and exp(-h theta J) on J = -D, the "
      "two helicities" % hsign, okh and hsign is not None)
Kp = ker_left(kk, EV4)
okR = all(eq(mul(blade((1, 2)), p, S4), neg(mul(I4, p, S4))) for p in Kp)
check("E3.2a even phi with k phi = 0: a 4-dimensional space on which the rotation bivector gamma_1 gamma_2 "
      "acts as -I4", len(Kp) == 4 and okR)
Is3 = {(1, 2): F(-1)}                                    # gamma_2 gamma_1 = I sigma_3 (T16)
check("E3.2b I sigma_3 = gamma_2 gamma_1 = I4 gamma_3 gamma_0 squares to -1 and commutes with gamma_0",
      eq(Is3, mul(I4, mul(gen(3), gen(0), S4), S4)) and eq(mul(Is3, Is3, S4), sc(-1)) and commutes(Is3, gen(0), S4))
okH = True
for p in Kp:
    chi = neg(mul(p, Is3, S4))                         # Hestenes positive frequency: (phi, -phi I s3)
    J = (neg(chi), p)
    Rt = (mul(p, Is3, S4), mul(chi, Is3, S4))
    okH = okH and eq(J[0], Rt[0]) and eq(J[1], Rt[1]) and is_zero(mul(kk, chi, S4))
check("E3.2c on Hestenes' positive-frequency solutions phi exp(-I sigma_3 k.x), J is right multiplication "
      "by I sigma_3", okH)
# chiral subspaces: I4 phi = +- phi I s3
def chiral(sign):
    rws = []
    imgs = [sub(mul(I4, p, S4), scl(sign, mul(p, Is3, S4))) for p in Kp]
    allb = sorted({bb for im in imgs for bb in im})
    rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, Kp) for v in nullspace(rws, len(Kp))]


Cp, Cm = chiral(1), chiral(-1)
okC = len(Cp) == 2 and len(Cm) == 2 and span_rank(Cp + Cm, ALL4) == 4
for sign, Cs in ((1, Cp), (-1, Cm)):
    for p in Cs:
        chi = neg(mul(p, Is3, S4))
        J = (neg(chi), p)
        D = (mul(I4, p, S4), mul(I4, chi, S4))
        okC = okC and eq(J[0], scl(sign, D[0])) and eq(J[1], scl(sign, D[1]))
check("E3.2d the subspaces J = +I4 and J = -I4 are the chiral subspaces I4 phi = +phi I sigma_3 and "
      "I4 phi = -phi I sigma_3, two and two: on a massless chiral field Hestenes' i, the pseudoscalar and J "
      "agree up to the chirality sign", okC)
okrot = True
for sign, Cs in ((1, Cp), (-1, Cm)):
    for p in Cs:
        rp = mul(Rr, p, S4)
        okrot = okrot and eq(rp, sub(scl(c, p), scl(s, mul(I4, p, S4))))   # (c - s I4) phi = exp(-theta/2 I4)
check("E3.2e the rotation acts on both chiral sectors as (c - s I4) = exp(-(theta/2) I4) = exp(-+(theta/2) J): "
      "helicity -+1/2 tied to chirality", okrot)
C_mass = mul(I4, gen(3), S4)
check("E3.2f consistency with T16 Lemma lem:onedatum: I4 anticommutes with a mass datum C = I4 gamma_3, "
      "so a mass term removes the pseudoscalar as complex structure", anticommutes(I4, C_mass, S4))

# ===========================================================================
# E4. The CAR in geometric algebra
# ===========================================================================
print("=" * 72)
print("E4. The CAR in geometric algebra")
print("=" * 72)

NP = 3
ST = tuple(list(S4) + [1, -1] * NP)                      # Cl(1,3) + three tower planes
e_ = [gen(4 + 2 * j) for j in range(NP)]
f_ = [gen(5 + 2 * j) for j in range(NP)]
w_ = [scl(F(1, 2), sub(e_[j], f_[j])) for j in range(NP)]
v_ = [scl(F(1, 2), add(e_[j], f_[j])) for j in range(NP)]
g_ = [mul(I4, f_[j], ST) for j in range(NP)]
check("E4.1a I4 commutes with every plane vector and I4* = -I4 (T03's *)",
      all(commutes(I4, x, ST) for x in e_ + f_) and eq(star(I4, ST), neg(I4)))
maj = e_ + g_
okmaj = all(eq(mul(m, m, ST), sc(1)) for m in maj) and \
    all(anticommutes(maj[a], maj[b], ST) for a in range(len(maj)) for b in range(a + 1, len(maj))) and \
    all(eq(star(m, ST), m) for m in maj)
check("E4.1b e_j and g_j = I4 f_j are self-adjoint, square to +1 and anticommute pairwise: a Euclidean "
      "(Majorana) Clifford system of 6", okmaj)
check("E4.1c the ladder pairs are w_j = (e_j + I4 g_j)/2 and v_j = (e_j - I4 g_j)/2: complex combinations of "
      "two Hermitian Majoranas with i = I4",
      all(eq(w_[j], scl(F(1, 2), add(e_[j], mul(I4, g_[j], ST)))) and
          eq(v_[j], scl(F(1, 2), sub(e_[j], mul(I4, g_[j], ST)))) for j in range(NP)))
check("E4.1d control: f_j itself squares to -1 and is anti-self-adjoint, so the split form needs the I4",
      all(eq(mul(f, f, ST), sc(-1)) and eq(star(f, ST), neg(f)) for f in f_))


def cs_n(z, n):
    zn = QI(1)
    for _ in range(n):
        zn = zn * z
    return zn.re, zn.im


def field(z, second):
    out = {}
    for j in range(NP):
        cn, sn = cs_n(z, j + 1)
        out = add(out, scl(cn, e_[j]), scl(sn, second[j]))
    return out


def anti(a, b):
    r = add(mul(a, b, ST), mul(b, a, ST))
    return r


zA = QI(F(3, 5), F(4, 5))
zB = QI(F(5, 13), F(12, 13))
pairs = [(zA, QI(1)), (zA * zB, zB)]                    # same u - y, different u + y
vals_E = [anti(field(u, g_), field(y, g_)) for (u, y) in pairs]
vals_S = [anti(field(u, f_), field(y, f_)) for (u, y) in pairs]
closed = 2 * sum((cs_n(zA, n)[0] for n in range(1, NP + 1)), F(0))
check("E4.2a Euclidean form (g_n = I4 f_n): {Psi(u), Psi(y)} is the scalar 2 sum cos n(u - y), equal at two "
      "pairs with the same u - y", all(set(v) <= {()} for v in vals_E) and vals_E[0] == vals_E[1] == sc(closed))
check("E4.2b split form (the tower's f_n used directly): the anticommutator differs between the two pairs "
      "(it is 2 sum cos n(u + y)): not translation-invariant", not eq(vals_S[0], vals_S[1]))
okS = True
for (u, y), v in zip(pairs, vals_S):
    target = 2 * sum((cs_n(u * y, n)[0] for n in range(1, NP + 1)), F(0))
    okS = okS and eq(v, sc(target))
check("E4.2c ... and equals 2 sum cos n(u + y) exactly", okS)
ue = {(): F(1), (0, 1): F(2), (1, 2): F(-1), (0, 1, 2, 3): F(3)}
okb = all(commutes(I4, blade(b), ST) for b in all_blades(4) if len(b) % 2 == 0) and \
    all(eq(mul(mul(I4, ue, ST), w_[j], ST), mul(ue, mul(I4, w_[j], ST), ST)) for j in range(NP))
check("E4.3 I4 commutes with the even spacetime algebra and with the modes, so (I4 u) w = u (I4 w): a field "
      "sum_j u_j(x) w_j is complex-bilinear for the single i = I4", okb)

Ej = mul(e_[0], f_[0], ST)
Ru = add(sc(F(3, 5)), scl(F(4, 5), mul(I4, Ej, ST)))
Rui = add(sc(F(3, 5)), scl(F(-4, 5), mul(I4, Ej, ST)))
ph2 = (F(3, 5) ** 2 - F(4, 5) ** 2, 2 * F(3, 5) * F(4, 5))
check("E4.4 (post-review) on a tower plane, exp(phi I4 e_j f_j) is unitary for T03's * and acts on w_j as the "
      "phase exp(2 phi I4): the plane's boost continued with i = I4 is the physical flow (tower planes only; "
      "not T05's radial atom, where I4 anticommutes with the plane)",
      eq(mul(star(Ru, ST), Ru, ST), sc(1)) and
      eq(mul(mul(Ru, w_[0], ST), Rui, ST), add(scl(ph2[0], w_[0]), scl(ph2[1], mul(I4, w_[0], ST)))))
check("E4.2d (post-review) control on the reading: the split-form field of E4.2b is not self-adjoint, so it was "
      "never a real field", not eq(star(field(zA, f_), ST), field(zA, f_)) and eq(star(field(zA, g_), ST), field(zA, g_)))

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f in FAILURES:
        print("  " + f)
    sys.exit(1)
print("ALL CHECKS PASSED")
