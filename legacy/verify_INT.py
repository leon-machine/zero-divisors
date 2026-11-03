#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_INT.py: exact checks for "Interactions for the GA field with i = I4" (16 October 2026).
Preregistration: preregistration_INT_2026-10-16.md. Findings: INT_findings_2026-10-16.md.

Real Clifford algebra only (GA.py, Fraction). Complex numbers appear only as the span{1, I4} parts
of elements, read off as pairs (a, b) for |M|^2.
"""

import sys
from fractions import Fraction as F
from itertools import combinations

import GA
from GA import FAILURES, mul, add, neg, sub, sc, gen, reverse, eq, is_zero, commutes, all_blades, rank_of_vectors

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
IS3 = {(1, 2): F(-1)}                      # I sigma_3 = gamma_2 gamma_1
G0 = gen(0)
ALL4 = all_blades(4)
EVEN = [blade(b) for b in ALL4 if len(b) % 2 == 0]


def chi(e, p):
    return scl(F(1, 2), sub(p, scl(F(e), mul(mul(I4, p, S4), IS3, S4))))


def proj(x):
    """span{1, I4} part over the ground, tower parts carried along."""
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (0, 1, 2, 3):
            out[b] = c
    return out


def vecmv(x):
    return [x.get(b, F(0)) for b in ALL4]


def basis_of(elems):
    out = []
    for c in elems:
        if c and rank_of_vectors([vecmv(x) for x in out + [c]]) > len(out):
            out.append(c)
    return out


Cp = basis_of([chi(1, b) for b in EVEN])
Cm = basis_of([chi(-1, b) for b in EVEN])

# ===========================================================================
print("=" * 72)
print("M. Mass with i = I4")
print("=" * 72)


def BN(a, b, N):
    return proj(mul(mul(reverse(a), b, S4), N, S4))


Ns = [blade(t) for t in ((0, 1), (0, 2), (1, 3), (2, 3))]
okM1 = True
for N in Ns:
    vals = [[BN(a, b, N) for b in Cp] for a in Cp]
    okM1 = okM1 and any(v for r in vals for v in r)
    okM1 = okM1 and all(eq(vals[i][j], neg(vals[j][i])) for i in range(4) for j in range(4))
    okM1 = okM1 and all(eq(BN(mul(I4, a, S4), b, N), mul(I4, BN(a, b, N), S4)) and
                        eq(BN(a, mul(I4, b, S4), N), mul(I4, BN(a, b, N), S4)) for a in Cp for b in Cp)
    okM1 = okM1 and all(eq(mul(N, IS3, S4), neg(mul(IS3, N, S4))) for _ in [0])
check("M1.1 for N in {g0g1, g0g2, g1g3, g2g3} (the even basis right factors anticommuting with I sigma_3), "
      "B_N(psi, phi) = proj(psi~ phi N) is nonzero, antisymmetric and C-bilinear (i = I4) on chi_+", okM1)
none_other = True
for t in ALL4:
    if blade(t) in Ns:
        continue
    vals = [proj(mul(mul(reverse(a), b, S4), blade(t), S4)) for a in Cp for b in Cp]
    if any(vals):
        none_other = False
check("M1.2 no other basis right factor gives a nonzero pairing on chi_+ (in particular N = 1 gives zero: "
      "psi~ psi has no span{1, I4} part on one chirality)", none_other)
lor = [add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1)))), add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2)))),
       add(sc(F(13, 5)), scl(F(12, 5), blade((0, 3))))]
lor = [R for R in lor if eq(mul(R, reverse(R), S4), sc(1))]
okinv = all(eq(BN(mul(R, a, S4), mul(R, b, S4), Ns[0]), BN(a, b, Ns[0])) for R in lor for a in Cp for b in Cp)
check("M1.3 B_N is invariant under %d Lorentz rotors (left action)" % len(lor), okinv and len(lor) == 3)
# charge 2 under the common phase exp(theta I4) = c + s I4
c_, s_ = F(3, 5), F(4, 5)
ph = add(sc(c_), scl(s_, I4))
ph2 = mul(ph, ph, S4)
okch = all(eq(BN(mul(ph, a, S4), mul(ph, b, S4), Ns[0]), mul(ph2, BN(a, b, Ns[0]), S4)) for a in Cp for b in Cp)
phc = add(sc(c_), scl(-s_, I4))
okch0 = all(eq(BN(mul(ph, a, S4), mul(phc, b, S4), Ns[0]), BN(a, b, Ns[0])) for a in Cp for b in Cp)
check("M1.4 under a common phase exp(theta I4) the pairing picks up exp(2 theta I4) (charge 2); with opposite "
      "charges on the two fields it is invariant", okch and okch0)
# nondegenerate: as a 2 x 2 complex antisymmetric form, nonzero means nondegenerate; check rank of real form
realM = [[BN(a, b, Ns[0]).get((), F(0)) for b in Cp] for a in Cp]
check("M1.5 the real part of B_N on chi_+ has rank 4 (nondegenerate): the 2-spinor epsilon pairing",
      rank_of_vectors(realM) == 4)

# --- M2 massive Dirac plane wave ---
p = add(scl(F(5), gen(0)), scl(F(3), gen(1)))
m = F(4)
check("M2.0 p = 5 g0 + 3 g1 has p^2 = 16 = m^2", eq(mul(p, p, S4), sc(16)))
rows = []
imgs = [sub(mul(p, b, S4), scl(m, mul(b, G0, S4))) for b in EVEN]
allb = sorted({bb for im in imgs for bb in im})
ns = GA_ns = None


def nullspace(rows_, ncols):
    mm = [list(r) for r in rows_]
    piv = []
    row = 0
    for col in range(ncols):
        pr = next((r for r in range(row, len(mm)) if mm[r][col] != 0), None)
        if pr is None:
            continue
        mm[row], mm[pr] = mm[pr], mm[row]
        pv = mm[row][col]
        mm[row] = [a / pv for a in mm[row]]
        for r in range(len(mm)):
            if r != row and mm[r][col] != 0:
                f = mm[r][col]
                mm[r] = [a - f * b for a, b in zip(mm[r], mm[row])]
        piv.append(col)
        row += 1
        if row == len(mm):
            break
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * ncols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -mm[i][fc]
        out.append(v)
    return out


sol = nullspace([[im.get(bb, F(0)) for im in imgs] for bb in allb], len(EVEN))
psis = [add(*[scl(v[i], EVEN[i]) for i in range(len(EVEN)) if v[i] != 0]) for v in sol]
check("M2.1 the positive-energy Dirac-Hestenes amplitudes (p psi_0 = m psi_0 g0) form a 4-dimensional space "
      "(complex 2: two spin states)", len(psis) == 4)
okM2 = True
for N in Ns:
    Ninv = scl(F(1) / mul(N, N, S4).get((), F(1)), N)
    for ps in psis:
        chp, chm = chi(1, ps), chi(-1, ps)
        eta = mul(chm, N, S4)
        in_plus = eq(chi(1, eta), eta)
        # mass equations: p chi = m eta N^-1 g0 and p eta = m chi g0 N
        e1 = eq(mul(p, chp, S4), scl(m, mul(mul(eta, Ninv, S4), G0, S4)))
        e2 = eq(mul(p, eta, S4), scl(m, mul(mul(chp, G0, S4), N, S4)))
        # opposite charges: right phase exp(theta I sigma_3) on psi acts on chi as exp(theta I4) and on eta as exp(-theta I4)
        phr = add(sc(c_), scl(s_, IS3))
        psr = mul(ps, phr, S4)
        q1 = eq(chi(1, psr), mul(ph, chp, S4))
        q2 = eq(mul(chi(-1, psr), N, S4), mul(phc, eta, S4))
        okM2 = okM2 and in_plus and e1 and e2 and q1 and q2 and not is_zero(chp) and not is_zero(eta)
check("M2.2 for each N of M1 and each massive amplitude: eta = psi_- N lies in chi_+; the Dirac equation is "
      "p chi = m eta N^-1 g0 and p eta = m chi g0 N (the mass couples the two right-handed fields); the Dirac "
      "phase gives chi charge +1 and eta charge -1 under exp(theta I4)", okM2)
okmt = True
for ps in psis:
    chp, chm = chi(1, ps), chi(-1, ps)
    N = Ns[0]
    eta = mul(chm, N, S4)
    Ninv = scl(F(1) / mul(N, N, S4).get((), F(1)), N)
    lhs = proj(mul(reverse(ps), ps, S4))
    rhs = scl(F(2), proj(mul(reverse(chp), chm, S4)))
    okmt = okmt and eq(lhs, rhs) and eq(proj(mul(reverse(chp), chm, S4)), BN(chp, eta, Ninv))
check("M2.3 the Dirac mass density proj(psi~ psi) is 2 proj(chi~ psi_-) = 2 B_{N^-1}(chi, eta): purely the "
      "cross pairing of the two right-handed fields", okmt)

# ===========================================================================
print("=" * 72)
print("B. No bosons in the tower")
print("=" * 72)

NPL_B = 3
SBB = tuple(list(S4) + [1, -1] * NPL_B)
import random
random.seed(7)
okB = True
gens_ = list(range(4 + 2 * NPL_B))
for _ in range(6):
    X = {tuple(sorted(random.sample(gens_, random.randint(0, 4)))): F(random.randint(-3, 3)) for _ in range(5)}
    Y = {tuple(sorted(random.sample(gens_, random.randint(0, 4)))): F(random.randint(-3, 3)) for _ in range(5)}
    X = {b: c for b, c in X.items() if c}
    Y = {b: c for b, c in Y.items() if c}
    cm = sub(mul(X, Y, SBB), mul(Y, X, SBB))
    okB = okB and cm.get((), F(0)) == 0
check("B1 the scalar part of every commutator vanishes (the scalar part is a trace on each floor), while "
      "<1>_0 = 1: no floor contains a pair with [a, a*] = 1 (checked on random elements of a floor)", okB)

# ===========================================================================
print("=" * 72)
print("C. Contact interactions in the tower")
print("=" * 72)


def kvec(k):
    return add(*[scl(F(k[i]), gen(i)) for i in range(4) if k[i] != 0])


def Lam(k, phi):
    return scl(F(1) / (2 * F(k[0])), mul(mul(kvec(k), G0, S4), phi, S4))


def spinor(k):
    for b in EVEN:
        f = Lam(k, chi(1, b))
        if not is_zero(f):
            return f


GUP = [gen(0), neg(gen(1)), neg(gen(2)), neg(gen(3))]       # gamma^mu


def current(a, b):
    """GA current between spinor values: J^mu(a, b) = proj(a^dagger g0 g^mu b), elements of span{1, I4}."""
    return [proj(mul(mul(mul(star(a, S4), G0, S4), GUP[mu], S4), b, S4)) for mu in range(4)]


def cdot(J1, J2):
    """Minkowski product J1 . J2 with upper-index components: J1^0 J2^0 - sum J1^i J2^i."""
    tot = mul(J1[0], J2[0], S4)
    for i in range(1, 4):
        tot = sub(tot, mul(J1[i], J2[i], S4))
    return tot


# tower: four planes, modes A k1 (0), B k2 (1), A k3 (2), B k4 (3)
NPL = 4
ST = tuple(list(S4) + [1, -1] * NPL)


def plane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    v = add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_)))
    w = add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))
    return v, w


PL = [plane(q) for q in range(NPL)]


def build_H(k1, k2, k3, k4, g=F(1)):
    u = [spinor(k1), spinor(k2), spinor(k3), spinor(k4)]
    PsiA = add(mul(u[0], PL[0][1], ST), mul(u[2], PL[2][1], ST))
    PsiB = add(mul(u[1], PL[1][1], ST), mul(u[3], PL[3][1], ST))
    JA = [proj(mul(mul(mul(star(PsiA, ST), G0, ST), GUP[mu], ST), PsiA, ST)) for mu in range(4)]
    JB = [proj(mul(mul(mul(star(PsiB, ST), G0, ST), GUP[mu], ST), PsiB, ST)) for mu in range(4)]
    H = mul(JA[0], JB[0], ST)
    for i in range(1, 4):
        H = sub(H, mul(JA[i], JB[i], ST))
    return scl(g, H), u


K1, K2, K3, K4 = (5, 3, 4, 0), (5, -3, -4, 0), (5, 0, 0, 5), (5, 0, 0, -5)
H, u = build_H(K1, K2, K3, K4)
check("C1.1 H = J_A . J_B is self-adjoint for T03's *", eq(star(H, ST), H))
QA = add(mul(PL[0][0], PL[0][1], ST), mul(PL[2][0], PL[2][1], ST))
QB = add(mul(PL[1][0], PL[1][1], ST), mul(PL[3][0], PL[3][1], ST))
check("C1.2 H commutes with both charges Q_A and Q_B (gauge invariance of the contact term)",
      commutes(H, QA, ST) and commutes(H, QB, ST))
tgrades = {len([i for i in b if i >= 4]) for b in H}
check("C1.3 H has tower components of grade 4 (it is not quasi-free); grades present %s" % sorted(tgrades),
      4 in tgrades)
adw = sub(mul(H, PL[0][1], ST), mul(PL[0][1], H, ST))
check("C1.4 [H, w_1] has tower components of grade 3: a single mode operator is carried to cubic terms "
      "(Majorana degree grows, T08 successor item 3)", any(len([i for i in b if i >= 4]) == 3 for b in adw))

# vacuum projector of the four planes
P0 = sc(1)
for q in range(NPL):
    P0 = mul(P0, mul(PL[q][1], PL[q][0], ST), ST)


def amplitude(H_):
    X = mul(mul(mul(mul(mul(mul(P0, PL[3][1], ST), PL[2][1], ST), H_, ST), PL[0][0], ST), PL[1][0], ST), P0, ST)
    b0, c0 = next(iter(P0.items()))
    a_ = X.get(b0, F(0)) / c0
    # I4 part: coefficient on blade (0,1,2,3) + P0's blade
    rest = sub(X, scl(a_, P0))
    bI = None
    I4P0 = mul(I4, P0, ST)
    bb, cc = next(iter(I4P0.items()))
    b_ = rest.get(bb, F(0)) / cc
    ok = eq(X, add(scl(a_, P0), scl(b_, I4P0)))
    return (a_, b_), ok


def ga_amp(u_):
    JA = current(u_[2], u_[0])
    JB = current(u_[3], u_[1])
    z = cdot(JA, JB)
    return (z.get((), F(0)), z.get((0, 1, 2, 3), F(0)))


amp, okform = amplitude(H)
gaa = ga_amp(u)
sign = None
if amp == gaa:
    sign = 1
elif amp == (-gaa[0], -gaa[1]):
    sign = -1
check("C2.1 the tower vacuum matrix element <A3 B4|H|A1 B2> is a complex number in span{1, I4} and equals "
      "%s J_A(3,1) . J_B(4,2) computed from the GA spinor currents" % ("+" if sign == 1 else "-"),
      okform and sign is not None)


def norm_c(k, f):
    J = current(f, f)
    # J^mu = c k^mu
    c = J[0].get((), F(0)) / F(k[0])
    okc = all(eq(J[mu], sc(c * F(k[mu]))) for mu in range(4))
    return c, okc


def ratio(k1, k2, k3, k4):
    us = [spinor(k1), spinor(k2), spinor(k3), spinor(k4)]
    a, b = ga_amp(us)
    cs = []
    okc = True
    for k, f in zip((k1, k2, k3, k4), us):
        c, o = norm_c(k, f)
        cs.append(c)
        okc = okc and o
    ssum = [k1[i] + k2[i] for i in range(4)]
    s = ssum[0] ** 2 - ssum[1] ** 2 - ssum[2] ** 2 - ssum[3] ** 2
    return (a * a + b * b) / (cs[0] * cs[1] * cs[2] * cs[3] * F(s) ** 2), okc


configs = [
    ((5, 3, 4, 0), (5, -3, -4, 0), (5, 0, 0, 5), (5, 0, 0, -5)),
    ((5, 3, 4, 0), (5, -3, -4, 0), (5, 4, 0, 3), (5, -4, 0, -3)),
    ((5, 3, 4, 0), (5, -3, -4, 0), (5, 0, 3, 4), (5, 0, -3, -4)),
    ((5, 3, 4, 0), (5, -3, -4, 0), (5, -3, 4, 0), (5, 3, -4, 0)),
    ((13, 5, 12, 0), (13, -5, -12, 0), (13, 12, 0, 5), (13, -12, 0, -5)),
    ((3, 1, 2, 2), (3, -1, -2, -2), (3, 2, 2, 1), (3, -2, -2, -1)),
]
for cf in configs:
    for t in range(4):
        assert cf[0][t] + cf[1][t] == cf[2][t] + cf[3][t]
rats = [ratio(*cf) for cf in configs]
check("C2.2 the spinor currents are J(f, f) = c k for each momentum (normalisation read off exactly)",
      all(o for _, o in rats))
vals = sorted({r for r, _ in rats})
check("C2.3 the normalised |M|^2 / s^2 is one constant (%s) over six configurations (three distinct angles "
      "at energy 10, three energies): same-chirality current-current scattering is isotropic, proportional to s^2" % vals,
      len(vals) == 1 and vals[0] != 0)
# C2.4 (post-review, replaces the first control): the other species as antiparticles, in the tower.
# Psi_B = g_2 v_B2 + g_4 v_B4 (creators of antiparticles, values in ker k and chi_+); state |A1, Bbar2>.


def build_H_anti(k1, k2, k3, k4):
    uA = [spinor(k1), spinor(k3)]
    gB = [spinor(k2), spinor(k4)]
    PsiA = add(mul(uA[0], PL[0][1], ST), mul(uA[1], PL[2][1], ST))
    PsiB = add(mul(gB[0], PL[1][0], ST), mul(gB[1], PL[3][0], ST))
    JA = [proj(mul(mul(mul(star(PsiA, ST), G0, ST), GUP[mu], ST), PsiA, ST)) for mu in range(4)]
    JB = [proj(mul(mul(mul(star(PsiB, ST), G0, ST), GUP[mu], ST), PsiB, ST)) for mu in range(4)]
    Hx = mul(JA[0], JB[0], ST)
    for i in range(1, 4):
        Hx = sub(Hx, mul(JA[i], JB[i], ST))
    return Hx, uA, gB


rat_anti = set()
ok_cross = True
for cf in configs:
    Hx, uA, gB = build_H_anti(*cf)
    (a_, b_), okf = amplitude(Hx)
    # GA crossing: amplitude is -J_A(3,1) . J_B(2,4) (spinor order of B swapped)
    z = cdot(current(uA[1], uA[0]), current(gB[0], gB[1]))
    ok_cross = ok_cross and okf and (a_, b_) == (-z.get((), F(0)), -z.get((0, 1, 2, 3), F(0)))
    cs = [current(f, f)[0].get((), F(0)) / F(k[0]) for k, f in zip((cf[0], cf[2], cf[1], cf[3]), (uA[0], uA[1], gB[0], gB[1]))]
    uv = [cf[0][i] - cf[3][i] for i in range(4)]
    uu = uv[0] ** 2 - uv[1] ** 2 - uv[2] ** 2 - uv[3] ** 2
    rat_anti.add((a_ * a_ + b_ * b_) / (cs[0] * cs[1] * cs[2] * cs[3] * F(uu) ** 2))
check("C2.4 (post-review) in the tower, with the second species' quanta as antiparticles of a right-handed "
      "field, the amplitude is the crossed -J_A(3,1) . J_B(2,4), and |M|^2/u^2 is one constant %s over the six "
      "configurations: the textbook opposite-helicity u^2 law, with no step done by hand" % sorted(rat_anti),
      ok_cross and len(rat_anti) == 1)

# C3 boost of a whole configuration
R = add(sc(F(5, 4)), scl(F(3, 4), blade((0, 3))))
Rt = reverse(R)


def boost_k(k):
    kv = mul(mul(R, kvec(k), S4), Rt, S4)
    return tuple(kv.get((i,), F(0)) for i in range(4))


cf = configs[1]
bk = [boost_k(k) for k in cf]
us_b = [mul(R, spinor(k), S4) for k in cf]
a0, b0 = ga_amp([spinor(k) for k in cf])
a1, b1 = ga_amp(us_b)
okboost = (a0 * a0 + b0 * b0 == a1 * a1 + b1 * b1) and all(eq(chi(1, f), f) for f in us_b)
okker = all(is_zero(mul(kvec(k), f, S4)) for k, f in zip(bk, us_b))
s0 = sum(((cf[0][i] + cf[1][i]) * (1 if i == 0 else -1) * (cf[0][i] + cf[1][i]) for i in range(4)), F(0))
s1 = sum(((bk[0][i] + bk[1][i]) * (1 if i == 0 else -1) * (bk[0][i] + bk[1][i]) for i in range(4)), F(0))
check("C3 a boost of the whole configuration keeps the boosted spinors chiral and in ker k', and leaves |M|^2 "
      "and s unchanged (boosted momentum %s)" % (bk[0],), okboost and okker and s0 == s1)

rb = ratio(*bk)
check("C3b (post-review) with fresh spinors built in the boosted (non-centre-of-mass) frame, the normalised "
      "|M|^2/s^2 is again %s" % (rb[0],), rb[0] == vals[0] and rb[1])

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f in FAILURES:
        print("  " + f)
    sys.exit(1)
print("ALL CHECKS PASSED")
