#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_PHO.py: exact checks for "The photon's Fock space in GA with i = I4, coupled to the tower" (16 October 2026).
Preregistration: preregistration_PHO_2026-10-16.md. Findings: PHO_findings_2026-10-16.md.

Real Clifford algebra (GA.py, Fraction). Complex numbers are the span{1, I4} parts of elements,
handled as GA elements or, for bookkeeping, as GA.QI with i read as I4.
"""

import sys
import math
from fractions import Fraction as F
from itertools import product

import GA
from GA import FAILURES, mul, add, neg, sub, sc, gen, reverse, eq, is_zero, commutes, all_blades, QI

NCHECKS = [0]


def check(label, ok):
    NCHECKS[0] += 1
    GA.check(label, ok)


def scl(c, x):
    out = {}
    for b, v in x.items():
        w = c * v
        if w != 0:
            out[b] = w
    return out


def blade(t):
    return {tuple(t): F(1)}


def star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sign = (-1) ** (g * (g - 1) // 2)
        for i in b:
            if s[i] == -1:
                sign = -sign
        out[b] = sign * c
    return {b: c for b, c in out.items() if c != 0}


S4 = (1, -1, -1, -1)
I4 = blade((0, 1, 2, 3))
IS3 = {(1, 2): F(-1)}
G0 = gen(0)
ALL4 = all_blades(4)
EVEN = [blade(b) for b in ALL4 if len(b) % 2 == 0]
GUP = [gen(0), neg(gen(1)), neg(gen(2)), neg(gen(3))]
NB = blade((0, 1))                          # the pairing's right factor (INT M1)


def chi(e, p):
    return scl(F(1, 2), sub(p, scl(F(e), mul(mul(I4, p, S4), IS3, S4))))


def proj(x):
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (0, 1, 2, 3):
            out[b] = c
    return out


def kvec(k):
    return add(*[scl(F(k[i]), gen(i)) for i in range(4) if k[i] != 0])


def Lam(k, phi):
    return scl(F(1) / (2 * F(k[0])), mul(mul(kvec(k), G0, S4), phi, S4))


def spinor(k):
    for b in EVEN:
        f = Lam(k, chi(1, b))
        if not is_zero(f):
            return f


def alpha(a, b):
    return mul(star(a, S4), b, S4).get((), F(0))


def to_q(x):
    return QI(x.get((), F(0)), x.get((0, 1, 2, 3), F(0)))


def B(a, b):
    return to_q(proj(mul(mul(reverse(a), b, S4), NB, S4)))


def cur(a, b):
    return [to_q(proj(mul(mul(mul(star(a, S4), G0, S4), GUP[mu], S4), b, S4))) for mu in range(4)]



def qmv(z):
    return add(sc(z.re), scl(z.im, I4))


def mdot(J1, J2):
    return J1[0] * J2[0] - J1[1] * J2[1] - J1[2] * J2[2] - J1[3] * J2[3]


# ===========================================================================
print("=" * 72)
print("F. The bosonic Fock space (Bargmann-Fock, coefficients span{1, I4})")
print("=" * 72)


def p_a(m, p):          # annihilation d/dz_m on a polynomial {exps: QI}
    out = {}
    for e, c in p.items():
        if e[m] > 0:
            e2 = e[:m] + (e[m] - 1,) + e[m + 1:]
            out[e2] = out.get(e2, QI(0)) + c * QI(e[m])
    return {e: c for e, c in out.items() if c != QI(0)}


def p_ad(m, p):         # creation z_m
    out = {}
    for e, c in p.items():
        e2 = e[:m] + (e[m] + 1,) + e[m + 1:]
        out[e2] = out.get(e2, QI(0)) + c
    return out


def p_sub(p, q):
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, QI(0)) - c
    return {e: c for e, c in out.items() if c != QI(0)}


def p_eq(p, q):
    return p_sub(p, q) == {}


def ip(p, q):           # <p, q>, antilinear in p
    tot = QI(0)
    for e, c in p.items():
        if e in q:
            w = 1
            for n in e:
                w *= math.factorial(n)
            tot = tot + c.conj() * q[e] * QI(w)
    return tot


NM = 4
monos = [e for e in product(range(7), repeat=NM) if sum(e) <= 6]
okF1 = True
zc = QI(F(2, 3), F(-5, 7))
for e in monos:
    p = {e: zc}
    for m in range(NM):
        for n in range(NM):
            lhs = p_sub(p_a(m, p_ad(n, p)), p_ad(n, p_a(m, p)))
            okF1 = okF1 and p_eq(lhs, p if m == n else {})
            okF1 = okF1 and p_eq(p_a(m, p_a(n, p)), p_a(n, p_a(m, p)))
            okF1 = okF1 and p_eq(p_ad(m, p_ad(n, p)), p_ad(n, p_ad(m, p)))
check("F1.1 CCR [a_m, a_n*] = delta_mn, [a_m, a_n] = [a_m*, a_n*] = 0 exactly on all %d monomials of degree <= 6 in "
      "%d modes, with a span{1, I4} coefficient" % (len(monos), NM), okF1)
okF12 = True
sample = monos[::7]
for e1 in sample:
    for e2 in sample:
        p, q = {e1: QI(1, 2)}, {e2: QI(F(-1, 3), 1)}
        for m in range(NM):
            okF12 = okF12 and ip(p_ad(m, p), q) == ip(p, p_a(m, q))
    okF12 = okF12 and ip({e1: QI(1)}, {e1: QI(1)}).re > 0
check("F1.2 a_m* is the adjoint of a_m for <z^n, z^n'> = n! delta (sesquilinear over span{1, I4}); the form is "
      "positive", okF12)
# F2: coupled states: GA element x polynomial; photon operators act on the polynomial index only
SPACE = tuple(list(S4) + [1, -1] * 4)


def tplane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    return (add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))), add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_))))


TP = [tplane(j) for j in range(4)]
VAC = {(): F(1)}
for (v, w) in TP:
    VAC = mul(VAC, mul(w, v, SPACE), SPACE)


def s_apply(X, op, st):
    """Apply X (GA element) times a Fock word op (None, ('a', m) or ('ad', m)) to a coupled state."""
    out = {}
    for e, Y in st.items():
        if op is None:
            items = [(e, F(1))]
        elif op[0] == 'a':
            m = op[1]
            items = [(e[:m] + (e[m] - 1,) + e[m + 1:], F(e[m]))] if e[m] > 0 else []
        else:
            m = op[1]
            items = [(e[:m] + (e[m] + 1,) + e[m + 1:], F(1))]
        for (e2, c) in items:
            Z = scl(c, mul(X, Y, SPACE))
            out[e2] = add(out.get(e2, {}), Z)
    return {e: Y for e, Y in out.items() if not is_zero(Y)}


def s_add(*sts):
    out = {}
    for st in sts:
        for e, Y in st.items():
            out[e] = add(out.get(e, {}), Y)
    return {e: Y for e, Y in out.items() if not is_zero(Y)}


st0 = {(0, 0, 0, 0): mul(mul(TP[0][0], TP[1][0], SPACE), VAC, SPACE)}
okF2 = True
for X in (gen(1), I4, TP[2][0], mul(TP[0][1], TP[3][0], SPACE)):
    for m in range(4):
        for kind in ('a', 'ad'):
            lhs = s_apply(X, None, s_apply(sc(1), (kind, m), s_apply(sc(1), ('ad', (m + 1) % 4), st0)))
            rhs = s_apply(sc(1), (kind, m), s_apply(X, None, s_apply(sc(1), ('ad', (m + 1) % 4), st0)))
            okF2 = okF2 and s_add(lhs, {e: neg(Y) for e, Y in rhs.items()}) == {}
check("F2 (true by construction; a smoke test of the code) on coupled states (tower element x polynomial) photon operators commute with ground "
      "vectors, I4 and tower mode operators", okF2)

# ===========================================================================
print("=" * 72)
print("M. Maxwell modes with i = I4")
print("=" * 72)
BIV = [blade(b) for b in ALL4 if len(b) == 2]
NDIRS = [(F(1), F(0), F(0)), (F(0), F(0), F(-1)), (F(3, 5), F(4, 5), F(0)), (F(2, 3), F(1, 3), F(2, 3)),
         (F(-6, 9), F(-6, 9), F(3, 9)), (F(1, 9), F(-4, 9), F(-8, 9))]


def frame(n):
    """Rational right-handed orthonormal (t1, t2) with t1 x t2 = n, by a reflection taking e3 to n."""
    E = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    n = list(n)
    if n == E[2]:
        return E[0], E[1]
    if n == [F(0), F(0), F(-1)]:
        return E[1], E[0]
    m = [n[0], n[1], n[2] - 1]
    mm = sum(x * x for x in m)
    R = lambda x: [x[i] - 2 * sum(x[j] * m[j] for j in range(3)) * m[i] / mm for i in range(3)]
    return R(E[1]), R(E[0])


def svec(t):
    return add(*[scl(F(t[i]), gen(1 + i)) for i in range(3) if t[i] != 0])


def cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


okM1 = True
okM2a = True
okM2b = True
okM2f = True
okM2e = True
nM2e = 0
sig_set, lam_set, mu_set = set(), set(), set()
ca, sa = F(4, 5), F(3, 5)                       # half angle alpha; theta = 2 alpha
ct, st_ = ca * ca - sa * sa, 2 * sa * ca
for n in NDIRS:
    assert sum(x * x for x in n) == 1
    t1, t2 = frame(n)
    assert cross(t1, t2) == list(n)
    kv = add(gen(0), svec(n))                    # k = gamma_0 + n (omega = 1)
    cols = [mul(kv, b, S4) for b in BIV]
    keys = sorted(set(k for c in cols for k in c))
    M = [[c.get(k, F(0)) for c in cols] for k in keys]
    rk = GA.mat_rank(M)
    T1, T2 = svec(t1), svec(t2)
    f = mul(kv, T2, S4)                          # k t2, a bivector since k . t2 = 0
    g = mul(kv, T1, S4)
    okM1 = okM1 and 6 - rk == 2 and is_zero(mul(kv, f, S4)) and is_zero(mul(kv, mul(I4, f, S4), S4))
    okM1 = okM1 and not is_zero(f) and all(len(b) == 2 for b in f) and not eq(mul(I4, f, S4), f)
    # M2a: A = t1 c + t2 s  =>  F = (k t2) c - (k t1) s = f (c - sigma I4 s) with k t1 = sigma I4 (k t2)
    sig = None
    for s_ in (1, -1):
        if eq(g, scl(F(s_), mul(I4, f, S4))):
            sig = s_
    okM2a = okM2a and sig is not None
    sig_set.add(sig)
    # M2b: rotor about n by theta; R t1 R~ = cos t1 + sin t2
    Bn = mul(T1, T2, S4)
    R = None
    for s_ in (1, -1):
        Rc = add(sc(ca), scl(F(s_) * sa, Bn))
        if eq(mul(mul(Rc, T1, S4), reverse(Rc), S4), add(scl(ct, T1), scl(st_, T2))):
            R = Rc
    okM2b = okM2b and R is not None
    lam = None
    for s_ in (1, -1):
        if eq(mul(mul(R, f, S4), reverse(R), S4), add(scl(ct, f), scl(F(s_) * st_, mul(I4, f, S4)))):
            lam = s_
    okM2b = okM2b and lam is not None
    lam_set.add(lam)
    # fermion: chi_+ spinor in ker k, R phi = (cos alpha + mu sin alpha I4) phi
    phi = spinor((1, n[0], n[1], n[2]))
    mu = None
    for s_ in (1, -1):
        if eq(mul(R, phi, S4), add(scl(ca, phi), scl(F(s_) * sa, mul(I4, phi, S4)))):
            mu = s_
    okM2f = okM2f and mu is not None
    mu_set.add(mu)
    # chi_- spinors in ker k: the same left-I4 rotation phase (the result is structural, not a chirality choice)
    for b in EVEN:
        pm = Lam((1, n[0], n[1], n[2]), chi(-1, b))
        if not is_zero(pm):
            okM2e = okM2e and eq(mul(R, pm, S4), add(scl(ca, pm), scl(F(mu) * sa, mul(I4, pm, S4))))
            nM2e += 1
check("M1 for null k (six directions, four off the axes) the bivectors f with k f = 0 form a real 2-dimensional, "
      "I4-stable space: one I4-complex mode per momentum", okM1)
sigma = next(iter(sig_set))
check("M2a geometric: A = t1 cos(k.x) + t2 sin(k.x) (helicity +1, t1 x t2 = n) has F = grad A = "
      "f (cos - sigma I4 sin)(k.x) = f exp(-sigma I4 k.x) with f = k t2 and sigma = %s in every direction" % sigma,
      okM2a and len(sig_set) == 1)
lam = next(iter(lam_set))
check("M2b rotor: rotation by theta about n acts on the mode space as cos theta + (%s) sin theta I4 = exp(-I4 theta), "
      "the same in every direction; read as exp(-i J theta) with i = I4 this is J = +1, the helicity M2a found for "
      "f exp(-I4 k.x): the two routes agree" % lam, okM2b and len(lam_set) == 1 and lam == -sigma)
# M2d the BOS polarisation eps_h = t1 - h I4 t2 with positive frequency exp(-I4 k.x) = c - I4 s (left factor):
# its vector part is t1 c - h t2 s, a real circular potential of physical helicity -h
okM2d = True
for n in NDIRS:
    t1, t2 = frame(n)
    T1, T2 = svec(t1), svec(t2)
    for h in (1, -1):
        eps = sub(T1, scl(F(h), mul(I4, T2, S4)))
        cpart, spart = eps, neg(mul(I4, eps, S4))
        v = lambda x: {b: c for b, c in x.items() if len(b) == 1}
        okM2d = okM2d and eq(v(cpart), T1) and eq(v(spart), scl(F(-h), T2))
check("M2d the polarisation eps_h = t1 - h I4 t2 of BOS E2, carried by exp(-I4 k.x) on the left, has vector part "
      "t1 cos - h t2 sin: physical helicity -h, confirming the BOS convention note through M2a", okM2d)
# M3 the field operator with i = I4. For a real wave F = X c + Y s (c, s = cos, sin of k.x), the quantised field is
# N[(X + iY)(c - i s) a + (X - iY)(c + i s) a*]; with i = I4 (one complex unit for values and Fock space) the
# coefficients become (X + I4 Y)(c - I4 s) and (X - I4 Y)(c + I4 s).
okM31 = True
for n in NDIRS:
    t1, t2 = frame(n)
    kv = add(gen(0), svec(n))
    T1, T2 = svec(t1), svec(t2)
    for hel in (1, -1):
        # A = t1 c + hel t2 s;  grad A = -k t1 s + hel k t2 c
        X, Y = scl(F(hel), mul(kv, T2, S4)), neg(mul(kv, T1, S4))
        ann = add(X, mul(I4, Y, S4))                 # coefficient of a (times exp(-I4 k.x))
        cre = sub(X, mul(I4, Y, S4))                 # coefficient of a* (times exp(+I4 k.x))
        if hel == 1:
            okM31 = okM31 and is_zero(cre) and not is_zero(ann)
        else:
            okM31 = okM31 and is_zero(ann) and not is_zero(cre)
check("M3.1 with i = I4 the helicity +1 mode keeps only its annihilation term 2X exp(-I4 k.x) a_+ and the helicity -1 "
      "mode only its creation term 2X exp(+I4 k.x) a_-*: the field operator is the Riemann-Silberstein form "
      "F = sum N 2X [exp(-I4 k.x) a_+ + exp(+I4 k.x) a_-*], in all six directions", okM31)
okM32 = True
for b in BIV:
    elec = next(iter(b))[0] == 0
    okM32 = okM32 and eq(star(b, S4), b if elec else neg(b))
check("M3.2 (near-immediate; six basis blades, then linearity) on bivectors T03's * is +1 on the electric (g_k g_0) and "
      "-1 on the magnetic (g_i g_j) blades, so for any state <(F + F*)/2> and <(F - F*)/2> are the electric and magnetic parts of <F>: E = (F + F*)/2 is a self-adjoint "
      "field with geometric electric expectation values", okM32)
mu_ = next(iter(mu_set))
check("M2e (added after review) every massless even spinor, chi_- included (%d spinors), has the same left-I4 rotation "
      "phase exp(-I4 alpha): helicity +1/2 with respect to left I4. So M2c is structural: left I4 as the complex unit "
      "makes positive frequency equal positive helicity for every massless even field" % nM2e, okM2e and nM2e > 0)
Jf = F(-mu_, 2)
Jph = sigma            # helicity of the exp(-I4 k.x) (positive-frequency for i = I4) photon mode
print("    photon mode exp(-I4 k.x) has helicity %s; chi_+ fermion: R phi = exp(%s I4 alpha) phi, J = %s" %
      (Jph, mu_, Jf))
check("M2c registered prediction (structural, see findings): with i = I4 the positive-frequency photon (helicity %s) and "
      "the chi_+ fermion (helicity %s) have the same sign of helicity" % (Jph, Jf), okM2f and len(mu_set) == 1 and Jph * Jf > 0)


def coeff_f(Y, X):
    """z in span{1, I4} with Y = z X exactly, or None."""
    if is_zero(Y):
        return QI(0)
    IX = mul(I4, X, SPACE)
    keys = sorted(set(X) | set(IX))
    for b1 in keys:
        for b2 in keys:
            a11, a12 = X.get(b1, F(0)), IX.get(b1, F(0))
            a21, a22 = X.get(b2, F(0)), IX.get(b2, F(0))
            det = a11 * a22 - a12 * a21
            if det != 0:
                r1, r2 = Y.get(b1, F(0)), Y.get(b2, F(0))
                z = QI((r1 * a22 - a12 * r2) / det, (a11 * r2 - a21 * r1) / det)
                return z if eq(Y, mul(qmv(z), X, SPACE)) else None
    return None

# ===========================================================================
print("=" * 72)
print("C. The coupled system: tower fermions and Fock-space photons")
print("=" * 72)
CONFIGS = [((6, 0, 0, 6), (7, 2, 6, -3), (9, 6, 6, 3), (4, -4, 0, 0)),
           ((7, 3, 2, 6), (9, -3, 6, -6), (10, 6, 8, 0), (6, -6, 0, 0)),
           ((9, 0, 0, -9), (9, 4, 8, -1), (12, 8, 4, -8), (6, -4, 4, -2)),
           ((9, 9, 0, 0), (12, -8, 8, 4), (12, 8, 4, 8), (9, -7, 4, -4)),
           ((5, -3, 0, 4), (9, 1, 8, 4), (12, -4, 8, 8), (2, 2, 0, 0)),
           ((6, 2, -4, -4), (12, -8, -8, 4), (9, 1, -8, 4), (9, -7, -4, -4)),
           ((3, 3, 0, 0), (5, 0, 3, -4), (5, 3, 0, -4), (3, 0, 3, 0)),
           ((3, 0, 0, -3), (5, 3, 4, 0), (5, 0, 4, -3), (3, 3, 0, 0)),
           ((3, 1, -2, 2), (3, 2, 2, -1), (3, 1, 2, 2), (3, 2, -2, -1))]
# fermion planes: 0 = A at k1, 1 = B at k2, 2 = A at k3, 3 = B at k4.  photon modes: 0,1 = (q, h = +-1), 2,3 = (-q, h)
SPECIES = {0: 'A', 2: 'A', 1: 'B', 3: 'B'}


def build(cfg, vertex='component'):
    k = list(cfg)
    q = [k[0][i] - k[2][i] for i in range(4)]
    Q2 = q[1] ** 2 + q[2] ** 2 + q[3] ** 2
    Q = math.isqrt(Q2)
    assert Q * Q == Q2 and math.isqrt(4 * Q) ** 2 == 4 * Q
    Nm = F(1, math.isqrt(4 * Q))                 # 1/sqrt(2|q|) times 1/|eps| (|eps|^2 = 2)
    n = [F(x, Q) for x in q[1:]]
    t1, t2 = frame(n)
    pq = [(q, t1, t2), ([-x for x in q], t2, t1)]  # right-handed frames about q and -q
    modes = []
    for (qq, a1, a2) in pq:
        for h in (1, -1):
            eps = [QI(0)] + [QI(a1[i], -h * a2[i]) for i in range(3)]       # t1 - h I4 t2
            modes.append((qq, h, eps))
    u = [spinor(kk) for kk in k]
    Jm = {(j, l): cur(u[j], u[l]) for j in range(4) for l in range(4) if SPECIES[j] == SPECIES[l]}
    terms = []                                   # (GA coefficient x tower operator, fock word)
    for (j, l), J in Jm.items():
        if j == l:
            continue
        dk = [k[j][i] - k[l][i] for i in range(1, 4)]                      # out j, in l
        for m, (qq, h, eps) in enumerate(modes):
            epsc = [z.conj() for z in eps]
            gaJ = add(*[mul(qmv(J[mu]), gen(mu), S4) for mu in range(4) if J[mu] != QI(0)])
            for (kind, sgn) in (('a', 1), ('ad', -1)):                     # absorb q: k_j = k_l + q; emit: k_j + q = k_l
                if dk != [sgn * x for x in qq[1:]]:
                    continue
                if vertex == 'component':
                    c = mdot(J, eps if kind == 'a' else epsc)
                else:                                                      # GA product proj(J_GA A_GA)
                    gav = add(*[mul(qmv(z), gen(mu), S4) for mu, z in enumerate(eps if kind == 'a' else epsc)
                                if z != QI(0)])
                    c = to_q(proj(mul(gaJ, gav, S4)))
                X = mul(qmv(c * QI(Nm)), mul(TP[j][0], TP[l][1], SPACE), SPACE)
                terms.append((X, (kind, m)))
    H0 = add(*[scl(F(k[j][0]), mul(TP[j][0], TP[j][1], SPACE)) for j in range(4)])
    rho = {s: {} for s in 'AB'}                 # rho_s(p) for the two momentum transfers present
    HC = {}
    for (j, l), J in Jm.items():
        if j != l:
            dk = tuple(k[j][i] - k[l][i] for i in range(1, 4))
            rho[SPECIES[j]][dk] = add(rho[SPECIES[j]].get(dk, {}), mul(qmv(J[0]), mul(TP[j][0], TP[l][1], SPACE), SPACE))
    for p, rA in rho['A'].items():
        mp = tuple(-x for x in p)
        if mp in rho['B']:
            HC = add(HC, scl(F(1, Q2), mul(rA, rho['B'][mp], SPACE)))
    return dict(k=k, q=q, Q=Q, Qm=[F(Q)] * 4, modes=modes, terms=terms, H0=H0, HC=HC, Jm=Jm)


def apply_terms(terms, st):
    return s_add(*[s_apply(X, op, st) for (X, op) in terms]) if terms else {}


def H0_apply(sys_, st):
    """The free Hamiltonian as an operator on coupled states: fermion part sum E_j v_j w_j (a GA element)
    plus the photon part sum_m |q_m| a_m* a_m (Fock operators)."""
    out = s_apply(sys_['H0'], None, st)
    for m, Qm in enumerate(sys_['Qm']):
        out = s_add(out, s_apply(sc(Qm), ('ad', m), s_apply(sc(1), ('a', m), st)))
    return out


def energy(sys_, e, Y):
    """H_0 eigenvalue of the coupled basis state Y (x) z^e, read off the operator H_0 and verified."""
    res = H0_apply(sys_, {e: Y})
    HY = res[e]
    for b, c in Y.items():
        if c != 0:
            E = HY.get(b, F(0)) / c
            break
    assert set(res) == {e} and eq(HY, scl(E, Y)), "not an eigenstate"
    return E


def adjoint_terms(terms):
    flip = {'a': 'ad', 'ad': 'a'}
    return [(star(X, SPACE), (flip[op[0]], op[1])) for (X, op) in terms]


def same_operator(t1_, t2_):
    d1, d2 = {}, {}
    for (X, op) in t1_:
        d1[op] = add(d1.get(op, {}), X)
    for (X, op) in t2_:
        d2[op] = add(d2.get(op, {}), X)
    keys = set(d1) | set(d2)
    return all(eq(d1.get(o, {}), d2.get(o, {})) for o in keys)


okC1 = okC1q = True
okC2 = okC3 = okC3h = okC2c = True
nconf = 0
for cfg in CONFIGS:
    S_ = build(cfg)
    S2 = build(cfg, vertex='ga')
    k = S_['k']
    # C1 self-adjoint, charge-conserving, photon number +-1
    okC1 = okC1 and same_operator(S_['terms'], adjoint_terms(S_['terms']))
    okC1 = okC1 and same_operator(S2['terms'], adjoint_terms(S2['terms']))
    okC1 = okC1 and eq(S_['HC'], star(S_['HC'], SPACE))
    QA = add(mul(TP[0][0], TP[0][1], SPACE), mul(TP[2][0], TP[2][1], SPACE))
    QB = add(mul(TP[1][0], TP[1][1], SPACE), mul(TP[3][0], TP[3][1], SPACE))
    for (X, op) in S_['terms']:
        okC1q = okC1q and eq(mul(X, QA, SPACE), mul(QA, X, SPACE)) and eq(mul(X, QB, SPACE), mul(QB, X, SPACE))
    # C2: second-order amplitude on the coupled state space
    ini = {(0, 0, 0, 0): mul(mul(TP[0][0], TP[1][0], SPACE), VAC, SPACE)}
    Ff, Fi = mul(TP[2][0], TP[3][0], SPACE), mul(TP[0][0], TP[1][0], SPACE)
    fin = mul(Ff, VAC, SPACE)

    def braket(Fx, Y):
        return coeff_f(mul(mul(VAC, star(Fx, SPACE), SPACE), Y, SPACE), VAC)
    Ei = energy(S_, (0, 0, 0, 0), ini[(0, 0, 0, 0)])
    amps = {}
    for tag, SS in (('comp', S_), ('ga', S2)):
        mid = apply_terms(SS['terms'], ini)
        mid2 = {}
        for e, Y in mid.items():
            assert sum(e) == 1
            mid2[e] = scl(1 / (Ei - energy(SS, e, Y)), Y)
        out = s_add(apply_terms(SS['terms'], mid2), s_apply(SS['HC'], None, ini))
        Yf = out.get((0, 0, 0, 0), {})
        # the <f| component; the remainder is the forward (self-energy) part along |i>
        z = braket(Ff, Yf) * QI(1 / braket(Ff, fin).re)
        zi = braket(Fi, Yf) * QI(1 / braket(Fi, ini[(0, 0, 0, 0)]).re)
        rest = sub(sub(Yf, mul(qmv(z), fin, SPACE)), mul(qmv(zi), ini[(0, 0, 0, 0)], SPACE))
        amps[tag] = (z, mid, is_zero(rest))
    JA, JB = S_['Jm'][(2, 0)], S_['Jm'][(3, 1)]
    q = S_['q']
    t = F(q[0]) ** 2 - F(S_['Q']) ** 2
    cov = mdot(JA, JB) * QI(-1 / t)
    okC2 = okC2 and amps['comp'][0] == cov and cov != QI(0) and amps['comp'][2]
    okC3 = okC3 and amps['ga'][0] == cov
    # C3h: the GA-product vertex puts the intermediate photon in the opposite helicity mode
    m1, m2 = amps['comp'][1], amps['ga'][1]
    swap = {0: 1, 1: 0, 2: 3, 3: 2}
    for e, Y in m1.items():
        m = e.index(1)
        e2 = tuple(1 if i == swap[m] else 0 for i in range(4))
        okC3h = okC3h and e2 in m2 and eq(m2[e2], Y)
    # controls: without the Coulomb operator, or with one helicity only, the amplitude is wrong
    for drop in ('coulomb', 'helicity'):
        mid = apply_terms(S_['terms'], ini)
        mid2 = {}
        for e, Y in mid.items():
            if drop == 'helicity' and e.index(1) in (1, 3):
                continue
            mid2[e] = scl(1 / (Ei - energy(S_, e, Y)), Y)
        out = apply_terms(S_['terms'], mid2)
        if drop == 'helicity':
            out = s_add(out, s_apply(S_['HC'], None, ini))
        zc_ = braket(Ff, out.get((0, 0, 0, 0), {})) * QI(1 / braket(Ff, fin).re)
        okC2c = okC2c and zc_ != cov
    nconf += 1
    print("    q = %s, |q| = %d: amplitude %s = -J_A.J_B/t" % (q, S_['Q'], amps['comp'][0]))
noff = sum(1 for c in CONFIGS if sum(1 for i in range(1, 4) if c[0][i] - c[2][i] != 0) == 3)
check("C1 H_int = e sum J^mu A_mu (component vertex) and H_int' = e proj(J_GA A_GA) (GA-product vertex) are "
      "self-adjoint for the combined adjoint (T03's * on the tower, a <-> a*); the Coulomb operator e^2 rho_A rho_B/|q|^2 "
      "is self-adjoint", okC1)
check("C1q every vertex term commutes with both fermion charges Q_A and Q_B (each term changes photon number by one by "
      "construction)", okC1q)
check("C2 (BOS E3 in operator form) second order on the coupled state space, H_int (E_i - H_0)^-1 H_int + H_C, with "
      "H_0 = sum E_j v_j w_j + sum |q_m| a_m* a_m applied as an operator: the <f| component equals -e^2 J_A(3,1) . J_B(4,2)/t exactly at %d configurations (%d with q off the "
      "axes; %d with q_0 != 0); the remainder of the vacuum-photon component lies along |i> (forward terms)" %
      (nconf, noff, sum(1 for c in CONFIGS if c[0][0] != c[2][0])), okC2)
check("C2c controls: dropping the Coulomb operator, or keeping one photon helicity only, gives a different amplitude "
      "at every configuration", okC2c)
check("C3 the GA-product vertex gives the same amplitude at every configuration", okC3)
check("C3h (near-immediate given BOS E2.2) with the GA-product vertex each intermediate one-photon state is exactly "
      "the component-vertex state with the helicity label swapped: proj(J eps_h) = J . conj(eps_h) = J . eps_-h", okC3h)


# C4 identical fermions: one species, four modes k1 k2 -> k3 k4, photons at q = k1 - k3 and q' = k1 - k4 (both signs,
# both helicities: eight modes). The mode normalisation N_m = 1/sqrt(4|q_m|) is carried symbolically: every
# second-order path creates and destroys one photon in the same mode, so the factor N_m^2 = 1/(4|q_m|) is applied
# exactly at the energy-denominator step; the Coulomb operator (1/2) sum_p rho(p) rho(-p)/|p|^2 has no N.
C4CONF = [((8, 0, 0, -8), (7, -6, -3, 2), (9, -6, 3, -6), (6, 0, -6, 0)),
          ((9, 0, -9, 0), (9, -4, 7, 4), (9, -8, -1, -4), (9, 4, -1, 8)),
          ((9, 4, -1, 8), (9, 4, -1, -8), (13, 12, -5, 0), (5, -4, 3, 0)),
          ((9, 4, 4, -7), (9, 4, -8, -1), (9, 0, 0, -9), (9, 8, -4, 1))]


def build_same(k):
    pl = {0: 0, 1: 1, 2: 2, 3: 3}                  # plane j holds k[j]; one species
    qs = []
    for (a, b) in ((0, 2), (0, 3)):
        p = [k[a][i] - k[b][i] for i in range(4)]
        qs += [p, [-x for x in p]]
    modes = []
    for p in qs:
        Q2 = p[1] ** 2 + p[2] ** 2 + p[3] ** 2
        Q = math.isqrt(Q2)
        assert Q * Q == Q2
        t1, t2 = frame([F(x, Q) for x in p[1:]])
        for h in (1, -1):
            modes.append((p, Q, [QI(0)] + [QI(t1[i], -h * t2[i]) for i in range(3)]))
    u = [spinor(kk) for kk in k]
    Jm = {(j, l): cur(u[j], u[l]) for j in range(4) for l in range(4)}
    terms = []
    for (j, l), J in Jm.items():
        if j == l:
            continue
        dk = [k[j][i] - k[l][i] for i in range(1, 4)]
        for m, (p, Q, eps) in enumerate(modes):
            for (kind, sgn) in (('a', 1), ('ad', -1)):
                if dk == [sgn * x for x in p[1:]]:
                    c = mdot(J, eps if kind == 'a' else [z.conj() for z in eps])
                    terms.append((mul(qmv(c), mul(TP[j][0], TP[l][1], SPACE), SPACE), (kind, m)))
    rho = {}
    for (j, l), J in Jm.items():
        if j != l:
            p = tuple(k[j][i] - k[l][i] for i in range(1, 4))
            rho[p] = add(rho.get(p, {}), mul(qmv(J[0]), mul(TP[j][0], TP[l][1], SPACE), SPACE))
    HC = {}
    for p, r in rho.items():
        mp = tuple(-x for x in p)
        if mp in rho:
            HC = add(HC, scl(F(1, 2) / sum(x * x for x in p), mul(r, rho[mp], SPACE)))
    H0 = add(*[scl(F(k[j][0]), mul(TP[j][0], TP[j][1], SPACE)) for j in range(4)])
    return dict(k=k, modes=modes, terms=terms, H0=H0, HC=HC, Jm=Jm, Qm=[F(md[1]) for md in modes])


okC4 = okC4c = okC4s = True
for cfg in C4CONF:
    S_ = build_same(list(cfg))
    k = S_['k']
    okC4s = okC4s and same_operator(S_['terms'], adjoint_terms(S_['terms'])) and eq(S_['HC'], star(S_['HC'], SPACE))
    e0 = (0,) * 8
    ini = {e0: mul(mul(TP[0][0], TP[1][0], SPACE), VAC, SPACE)}
    Ff = mul(TP[2][0], TP[3][0], SPACE)
    fin = mul(Ff, VAC, SPACE)
    Ei = energy(S_, e0, ini[e0])
    mid = apply_terms(S_['terms'], ini)
    mid2 = {}
    for e, Y in mid.items():
        m = e.index(1)
        mid2[e] = scl(F(1, 4 * S_['modes'][m][1]) / (Ei - energy(S_, e, Y)), Y)
    out = s_add(apply_terms(S_['terms'], mid2), s_apply(S_['HC'], None, ini))
    z = coeff_f(mul(mul(VAC, star(Ff, SPACE), SPACE), out.get(e0, {}), SPACE), VAC)
    z = z * QI(1 / coeff_f(mul(mul(VAC, star(Ff, SPACE), SPACE), fin, SPACE), VAC).re)
    J31, J42, J41, J32 = S_['Jm'][(2, 0)], S_['Jm'][(3, 1)], S_['Jm'][(3, 0)], S_['Jm'][(2, 1)]
    q, qp = [k[0][i] - k[2][i] for i in range(4)], [k[0][i] - k[3][i] for i in range(4)]
    t = F(q[0] ** 2 - q[1] ** 2 - q[2] ** 2 - q[3] ** 2)
    uu = F(qp[0] ** 2 - qp[1] ** 2 - qp[2] ** 2 - qp[3] ** 2)
    direct, exch = mdot(J31, J42) * QI(-1 / t), mdot(J41, J32) * QI(-1 / uu)
    okC4 = okC4 and z == direct - exch and direct != QI(0) and exch != QI(0)
    okC4c = okC4c and z != direct + exch
    print("    identical fermions, |q| = %d, |q'| = %d: amplitude %s = -(J31.J42/t - J41.J32/u)" %
          (S_['modes'][0][1], S_['modes'][4][1], z))
check("C4 (added after review) identical fermions k1 k2 -> k3 k4 in one species, eight photon modes: H_int and the full "
      "Coulomb operator (1/2) sum_p rho(p) rho(-p)/|p|^2 are self-adjoint, and the operator amplitude equals "
      "-e^2 (J31.J42/t - J41.J32/u) exactly at %d configurations with q and q' off the axes" % len(C4CONF),
      okC4 and okC4s)
check("C4c control: the bosonic combination -(J31.J42/t + J41.J32/u) is not obtained: C4 tests the fermionic "
      "ordering of the tower", okC4c)


def plane_n(qq):
    e_, f_ = 4 + 2 * qq, 5 + 2 * qq
    return (add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))), add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_))))


# ===========================================================================
print("=" * 72)
print("T. How close the tower comes to the CCR")
print("=" * 72)
okT1 = okT2 = okT3 = True
for npair in (1, 2, 3):
    STn = tuple(list(S4) + [1, -1] * (2 * npair))
    pl = [plane_n(j) for j in range(2 * npair)]
    Bp = add(*[mul(pl[2 * j][1], pl[2 * j + 1][1], STn) for j in range(npair)])
    Bd = star(Bp, STn)
    Nn = add(*[mul(v, w, STn) for (v, w) in pl])
    K3 = scl(F(1, 2), sub(Nn, sc(npair)))
    comm = sub(mul(Bp, Bd, STn), mul(Bd, Bp, STn))
    okT1 = okT1 and eq(comm, sub(sc(npair), Nn))
    okT2 = okT2 and eq(sub(mul(K3, Bd, STn), mul(Bd, K3, STn)), Bd)
    okT2 = okT2 and eq(sub(mul(K3, Bp, STn), mul(Bp, K3, STn)), neg(Bp)) and eq(comm, scl(F(-2), K3))
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = mul(vac, mul(w, v, STn), STn)
    stk = vac
    for kk in range(npair + 1):
        # <k|[b, b*]|k> = 1 - 2k/n with b = B/sqrt(n): [B, B*] |k> = (n - 2k) |k>
        okT3 = okT3 and not is_zero(stk) and eq(mul(comm, stk, STn), scl(F(npair - 2 * kk), stk))
        stk = mul(Bd, stk, STn)
    okT3 = okT3 and is_zero(stk)                 # the ladder stops after n pairs: su(2), not the CCR
check("T1 for n = 1, 2, 3 tower pairs, B = sum_j w_cj w_dj gives [B, B*] = n - (N_c + N_d) exactly: b = B/sqrt(n) obeys "
      "[b, b*] = 1 - (N_c + N_d)/n", okT1)
check("T2 with K3 = (N_c + N_d - n)/2: [K3, B*] = B*, [K3, B] = -B, [B, B*] = -2 K3: the tower's pair bosons are an "
      "su(2) quasi-spin", okT2)
check("T3 on the symmetric k-pair states [b, b*] = 1 - 2k/n exactly, and (B*)^(n+1) annihilates the vacuum: a finite "
      "ladder of n + 1 states; the CCR is the n -> infinity (Inonu-Wigner) contraction of su(2), and b converges to a "
      "boson only on bounded-k states, not in norm", okT3)

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f_ in FAILURES:
        print("  " + f_)
    sys.exit(1)
print("ALL CHECKS PASSED")
