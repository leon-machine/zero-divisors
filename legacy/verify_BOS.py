#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_BOS.py: exact checks for "Bosons for the GA field theory with i = I4" (16 October 2026).
Preregistration: preregistration_BOS_2026-10-16.md. Findings: BOS_findings_2026-10-16.md.

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


# ===========================================================================
print("=" * 72)
print("S. Composite scalars: the NJL channel in the tower")
print("=" * 72)

DIRS = [(3, 0, 0, 3), (5, 3, 4, 0), (3, 2, 1, 2), (9, 1, 4, 8), (7, 2, 3, 6), (5, 0, -3, 4)]
cvals = set()
okS1 = True
for k in DIRS:
    km = (k[0], -k[1], -k[2], -k[3])
    f, g = spinor(k), spinor(km)
    okS1 = okS1 and B(f, f) == QI(0) and B(g, g) == QI(0)
    mu = B(f, g)
    cvals.add((mu.re ** 2 + mu.im ** 2) / (alpha(f, f) * alpha(g, g)))
check("S1.1 (immediate from INT M1, antisymmetry) B_N(f(k), f(k)) = 0; with the modelling assumption that the "
      "creation and annihilation parts at k carry the same spinor f(k), the mass acts only through pair terms", okS1)
check("S1.2 the normalised pairing |B(f(k), f(-k))|^2 / (alpha alpha) is one constant c = %s over six directions "
      "of k: the pair mass is isotropic" % sorted(cvals), len(cvals) == 1)
cB = next(iter(cvals))

# tower: two planes a (chi particle at k) and c (eta particle at -k)
ST = tuple(list(S4) + [1, -1, 1, -1])


def plane(q):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    v = add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_)))
    w = add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))
    return v, w


(va, wa), (vc, wc) = plane(0), plane(1)


def qmv(z):
    return add(sc(z.re), scl(z.im, I4))


def block_H(K, mu):
    H = add(scl(F(K), mul(va, wa, ST)), scl(F(K), mul(vc, wc, ST)))
    H = add(H, mul(qmv(mu), mul(wa, wc, ST), ST), mul(qmv(mu.conj()), mul(vc, va, ST), ST))
    return H


def ad(H, x):
    return sub(mul(H, x, ST), mul(x, H, ST))


okS1b = True
for (K, mu) in ((3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(7, 24)), (2, QI(F(1, 2), F(-3, 4)))):
    H = block_H(K, mu)
    E2 = F(K) ** 2 + mu.re ** 2 + mu.im ** 2
    okS1b = okS1b and all(eq(ad(H, ad(H, x)), scl(E2, x)) for x in (wa, va, wc, vc))
    okS1b = okS1b and eq(star(H, ST), H)
check("S1.3 the block Hamiltonian H = K(n_a + n_c) + mu w_a w_c + mu^* v_c v_a (mu in span{1, I4}) is self-adjoint "
      "and ad_H^2 = K^2 + |mu|^2 on all four mode operators (four cases): quasiparticle energy E = sqrt(K^2 + |mu|^2); with "
      "mu = m B the dispersion is E^2 = K^2 + c m^2, isotropic by S1.2", okS1b)
# block energies, computed on the pair sector {P0, s1 = v_a v_c P0}
P0 = mul(mul(wa, va, ST), mul(wc, vc, ST), ST)
s1 = mul(mul(va, vc, ST), P0, ST)
okS2 = True
for (K, mu) in ((3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(F(60, 13), F(144, 13)))):
    H = block_H(K, mu)
    # H P0 = -mu^* s1 and H s1 = -mu P0 + 2K s1: the matrix [[0, -mu], [-mu^*, 2K]]
    okS2 = okS2 and eq(mul(H, P0, ST), neg(mul(qmv(mu.conj()), s1, ST)))
    okS2 = okS2 and eq(mul(H, s1, ST), add(neg(mul(qmv(mu), P0, ST)), scl(F(2 * K), s1)))
    E = math.isqrt(int(F(K) ** 2 + mu.re ** 2 + mu.im ** 2))
    lam = F(K - E)
    p = QI(0) - mu * QI(1 / lam)                          # ground vector p P0 + s1
    u = add(mul(qmv(p), P0, ST), s1)
    okS2 = okS2 and eq(mul(H, u, ST), scl(lam, u)) and not is_zero(u)
    for o in (mul(va, P0, ST), mul(vc, P0, ST)):          # odd sectors: one quasiparticle, energy K
        okS2 = okS2 and eq(mul(H, o, ST), scl(F(K), o)) and not is_zero(o)
check("S2.1 the full block: the odd states v_a vacuum, v_c vacuum have energy K; the pair sector {vacuum, v_a v_c vacuum} is invariant: H acts as [[0, -mu], [-mu^*, 2K]], with the "
      "exact ground vector -(mu/(K - E)) vacuum + v_a v_c vacuum of energy K - E, E = sqrt(K^2 + |mu|^2); spectrum {K - E, K, K, K + E} "
      "(3-4-5 point: K - E = -2; also K = 5, mu = (60 + 144 I4)/13, |mu| = 12, energy -8)", okS2)
# S2.5 an explicit tower four-fermion operator: H_4 = sum_b K(n_a + n_c) - G P* P, P = sum_b w_a w_c
def pairing_model(nbk, K, G):
    STm = tuple(list(S4) + [1, -1] * (2 * nbk))
    pl = [plane(j) for j in range(2 * nbk)]
    Pop = {}
    Hk = {}
    for b in range(nbk):
        (v1, w1), (v2, w2) = pl[2 * b], pl[2 * b + 1]
        Pop = add(Pop, mul(w1, w2, STm))
        Hk = add(Hk, scl(F(K), add(mul(v1, w1, STm), mul(v2, w2, STm))))
    Pst = star(Pop, STm)
    H4 = sub(Hk, scl(F(G), mul(Pst, Pop, STm)))
    Ntot = add(*[mul(v, w, STm) for (v, w) in pl])
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = mul(vac, mul(w, v, STm), STm)
    ok = eq(star(H4, STm), H4) and eq(mul(H4, Ntot, STm), mul(Ntot, H4, STm))
    st = vac
    energies = []
    for n in range(nbk + 1):
        En = F(2 * K * n) - F(G) * n * (nbk - n + 1)
        ok = ok and not is_zero(st) and eq(mul(H4, st, STm), scl(En, st))
        energies.append(En)
        st = mul(Pst, st, STm)                           # unnormalised symmetric n-pair state
    return ok, energies


okS20 = True
for (nbk, K_, G) in ((2, 3, 2), (2, 3, 4), (3, 3, 1), (3, 3, 3)):
    ok, en = pairing_model(nbk, K_, G)
    Gc = F(2 * K_, nbk)
    okS20 = okS20 and ok and ((min(en) < 0) == (G > Gc))
    print('    n_b = %d, K = %d, G = %s (2K/n_b = %s): pair-state energies %s' % (nbk, K_, G, Gc, [str(e) for e in en]))
check("S2.5 the interaction is a tower element: H_4 = sum_b K(n_a + n_c) - G P*P with P = sum_b w_a w_c is "
      "self-adjoint, conserves the axial number, and has exact symmetric pair states of energy "
      "2Kn - G n(n_b - n + 1); pairs enter the ground state exactly when G > 2K/n_b (n_b = 2, 3)", okS20)
# one shell: 2N momenta (N antipodal pairs); a Dirac field has 4 modes per momentum (chi and eta, particle and
# antiparticle), and the mass pairs them into n_b = 4N blocks. Mean field: E_tot = n_b(K - E) + Delta^2/G.
Ndir, K = 6, F(3)
nb = 4 * Ndir


def E_tot(x, G):                                         # x = Delta^2, chosen so that K^2 + c x is a square
    E = math.isqrt(int(K ** 2 + cB * x))
    assert F(E) ** 2 == K ** 2 + cB * x
    return nb * (K - E) + x / G


# d E_tot / d x = -n_b c / (2E) + 1/G: stationary at E = n_b c G / 2 = 2NcG; -sqrt is convex, so E_tot is convex in x
G_c = 2 * K / (nb * cB)
G_star = F(2 * 5) / (nb * cB)                             # stationary point at E = 5, x = 16
vals = [(x, E_tot(x, G_star)) for x in (F(0), F(7), F(16), F(27), F(40))]
okS22 = min(vals, key=lambda t: t[1])[0] == 16 and E_tot(F(16), G_star) < 0 and G_star > G_c
check("S2.2 mean field, one shell, N = 6, n_b = 4N = 24 blocks: E_tot = n_b(K - sqrt(K^2 + c Delta^2)) + Delta^2/G "
      "(convex in Delta^2, analytic) is stationary at sqrt(K^2 + c Delta^2) = 2NcG; at G = %s > G_c = %s it is %s at "
      "Delta^2 = 16, below its values %s at Delta^2 = 0, 7, 27, 40 (sampled)" %
      (G_star, G_c, E_tot(F(16), G_star), [str(v) for (x, v) in vals if x != 16]), okS22)
okS23 = all(E_tot(x, G) > 0 for G in (G_c, G_c * F(9, 10)) for x in (F(7), F(16), F(27), F(40)))
check("S2.3 for G <= G_c = 2K/(n_b c) = K/(2Nc) the slope at Delta = 0 is -n_b c/(2K) + 1/G >= 0, so Delta = 0 is the "
      "minimum (the same threshold as S2.5, the exact operator); sampled at G = G_c and 0.9 G_c", okS23)
# S2.4 the pair expectation in the exact block ground state: |<w_a w_c>| = |mu|/(2E)
def coeff_P0(Y):
    z = QI(4 * Y.get((), F(0)), 4 * Y.get((0, 1, 2, 3), F(0)))
    return z, eq(Y, mul(qmv(z), P0, ST))


okS24 = True
for (K_, mu) in ((3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(F(60, 13), F(144, 13)))):
    H = block_H(K_, mu)
    E = math.isqrt(int(F(K_) ** 2 + mu.re ** 2 + mu.im ** 2))
    lam = F(K_ - E)
    U = add(qmv(QI(0) - mu * QI(1 / lam)), mul(va, vc, ST))
    nrm, ok1 = coeff_P0(mul(mul(P0, star(U, ST), ST), mul(U, P0, ST), ST))
    pr, ok2 = coeff_P0(mul(mul(P0, star(U, ST), ST), mul(mul(wa, wc, ST), mul(U, P0, ST), ST), ST))
    z = pr * QI(1 / nrm.re)
    okS24 = okS24 and ok1 and ok2 and nrm.im == 0 and z.re ** 2 + z.im ** 2 == (mu.re ** 2 + mu.im ** 2) / (4 * E * E)
    okS24 = okS24 and (z * mu).im == 0
    print('    block K=%s mu=%s: <w_a w_c> = %s, z mu = %s' % (K_, mu, z, z * mu))
Dlt = F(4)                                                  # the stationary Delta of S2.2 (Delta^2 = 16, E = 5)
okS24 = okS24 and G_star * nb * Dlt / (2 * 5) == Dlt and nb == 24
check("S2.4 in the exact block ground state the pair amplitude <w_a w_c> has modulus |mu|/(2E) and is aligned with "
      "mu^* (z mu real): with mu = Delta, n_b blocks and stationarity E = NcG, Delta = G sum_blocks |<w_a w_c>| "
      "(at the S2.2 point: 4 = (5/12)(24)(4/10); this is the Hellmann-Feynman form of S2.2's stationarity), "
      "the fermion mass is G times the condensate (T16's 'the mass is the condensate')", okS24)
# S3 the axial phase: an inner unitary of the tower; flat direction of the mean-field energy
zq = QI(F(3, 5), F(4, 5))
zm = qmv(zq)
na, nc = mul(va, wa, ST), mul(vc, wc, ST)
U = mul(add(sc(1), mul(sub(zm, sc(1)), na, ST)), add(sc(1), mul(sub(zm, sc(1)), nc, ST)), ST)
okS3 = eq(mul(U, star(U, ST), ST), sc(1)) and eq(mul(star(U, ST), U, ST), sc(1))
zinv2 = zq.conj() * zq.conj()
for (K_, mu) in ((3, QI(4)), (5, QI(F(60, 13), F(144, 13))), (2, QI(F(1, 2), F(-3, 4)))):
    okS3 = okS3 and eq(mul(mul(U, block_H(K_, mu), ST), star(U, ST), ST), block_H(K_, mu * zinv2))
f, g = spinor(DIRS[1]), spinor((5, -3, -4, 0))
okS3 = okS3 and B(mul(zm, f, S4), mul(zm, g, S4)) == B(f, g) * (zq * zq)
check("S3 the axial phase is an inner unitary of the tower: U = exp(theta I4 (n_a + n_c)) is unitary and "
      "U H(mu) U* = H(mu exp(-2 theta I4)); the field phase multiplies B by exp(2 theta I4). So the spectrum depends "
      "on |mu| only and the mean-field E_tot has an exactly flat phase direction for G > G_c (mean field; the "
      "massless pole itself is the imported NJL random-phase result)", okS3)

# ===========================================================================
print("=" * 72)
print("V. Composite gauge bosons")
print("=" * 72)


def re_im_vectors(J):
    a = add(*[scl(J[mu].re, gen(mu)) for mu in range(4) if J[mu].re != 0]) if any(J[mu].re for mu in range(4)) else {}
    b = add(*[scl(J[mu].im, gen(mu)) for mu in range(4) if J[mu].im != 0]) if any(J[mu].im for mu in range(4)) else {}
    return a, b


def lower(J):
    return [J[0], -J[1], -J[2], -J[3]]


Rb = add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1))))
Rr = add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2))))
rotors = [Rb, Rr, add(sc(F(13, 5)), scl(F(12, 5), blade((0, 2)))), mul(Rb, Rr, S4)]
others = [gen(1), add(sc(1), scl(F(1, 3), I4)), add(blade((0, 1)), blade((2, 3)), blade((1, 3)))]
okV = True
for R in rotors:
    for (k1, k3) in (((5, 3, 4, 0), (3, 2, 1, 2)), ((9, 1, 4, 8), (7, 2, 3, 6))):
        f1, f3 = spinor(k1), spinor(k3)
        J = cur(f3, f1)
        Jr = cur(mul(R, f3, S4), mul(R, f1, S4))
        # components J^mu are upper; the vector is J^mu gamma_mu
        a, b = re_im_vectors(J)
        ar, br = re_im_vectors(Jr)
        okV = okV and eq(ar, mul(mul(R, a, S4), reverse(R), S4)) and eq(br, mul(mul(R, b, S4), reverse(R), S4))
okVo = True
for S_ in others:
    f1, f3 = spinor((5, 3, 4, 0)), spinor((3, 2, 1, 2))
    a, b = re_im_vectors(cur(f3, f1))
    ar, br = re_im_vectors(cur(mul(S_, f3, S4), mul(S_, f1, S4)))
    okVo = okVo and eq(ar, mul(mul(S_, a, S4), reverse(S_), S4)) and eq(br, mul(mul(S_, b, S4), reverse(S_), S4))
S_ = add(sc(1), gen(0))
f1, f3 = spinor((5, 3, 4, 0)), spinor((3, 2, 1, 2))
a, b = re_im_vectors(cur(f3, f1))
ar, br = re_im_vectors(cur(mul(S_, f3, S4), mul(S_, f1, S4)))
okVc = not (eq(ar, mul(mul(S_, a, S4), reverse(S_), S4)) and eq(br, mul(mul(S_, b, S4), reverse(S_), S4)))
check("V2 (near-immediate) J(S f, S g) = S J(f, g) S~ for four rotors (two boosts, a rotation, and boost x rotation in "
      "non-commuting planes) and, as an identity of the bilinear, for three non-rotor elements of definite parity; "
      "control: it fails for the mixed-parity 1 + g0. A nonzero <J> picks a direction: the Bjorken route breaks "
      "Lorentz invariance", okV and okVo and okVc)

# ===========================================================================
print("=" * 72)
print("E. Elementary gauge bosons")
print("=" * 72)


def mdot(J1, J2):
    return J1[0] * J2[0] - J1[1] * J2[1] - J1[2] * J2[2] - J1[3] * J2[3]


# exact kinematics: k1 + k2 = k3 + k4, all null, k1 not collinear with k3, k2 not with k4, |q| rational
pick = [((3, 3, 0, 0), (5, 0, 3, -4), (5, 3, 0, -4), (3, 0, 3, 0)),
        ((3, 0, 0, -3), (5, 3, 4, 0), (5, 0, 4, -3), (3, 3, 0, 0)),
        ((4, 0, 4, 0), (5, 4, 0, -3), (5, 0, 4, -3), (4, 4, 0, 0)),
        ((3, 3, 0, 0), (5, -3, -4, 0), (5, 3, -4, 0), (3, -3, 0, 0)),
        ((4, 0, 0, 4), (2, -2, 0, 0), (3, -1, 2, 2), (3, -1, -2, 2)),
        ((4, 0, -4, 0), (5, 0, 4, 3), (3, 0, 0, -3), (6, 0, 0, 6)),
        ((4, 0, 0, -4), (3, -2, 1, 2), (3, 2, 1, -2), (4, -4, 0, 0)),
        ((5, 4, 0, -3), (4, -4, 0, 0), (6, 0, 0, -6), (3, 0, 0, 3)),
        ((3, 1, -2, 2), (3, 2, 2, -1), (3, 1, 2, 2), (3, 2, -2, -1)),
        ((5, 3, -4, 0), (5, 0, 4, 3), (5, 3, 4, 0), (5, 0, -4, 3))]


def collinear(x, y):
    return (x[2] * y[3] - x[3] * y[2], x[3] * y[1] - x[1] * y[3], x[1] * y[2] - x[2] * y[1]) == (0, 0, 0)


okE0 = True
cfg = []
for (k1, k2, k3, k4) in pick:
    okE0 = okE0 and all(k[0] > 0 and k[0] ** 2 == k[1] ** 2 + k[2] ** 2 + k[3] ** 2 for k in (k1, k2, k3, k4))
    okE0 = okE0 and all(k1[i] + k2[i] == k3[i] + k4[i] for i in range(4))
    okE0 = okE0 and not collinear(k1, k3) and not collinear(k2, k4) and k3 != k2
    q = [k1[i] - k3[i] for i in range(4)]
    Q2 = q[1] ** 2 + q[2] ** 2 + q[3] ** 2
    Qr = math.isqrt(Q2)
    okE0 = okE0 and Qr * Qr == Q2 and q[0] ** 2 != Q2
    JA, JB = cur(spinor(k3), spinor(k1)), cur(spinor(k4), spinor(k2))
    okE0 = okE0 and JA[0] * JB[0] != QI(0)                  # nondegenerate: the Coulomb term is present
    cfg.append((k1, k2, k3, k4, q, Qr))
pick = cfg
nq0 = sum(1 for c in pick if c[4][0] != 0)
check("E0 kinematics: %d exact non-collinear configurations with rational |q| (%d with q_0 != 0, %d with q along an "
      "axis), every one with J_A^0 J_B^0 != 0" % (len(pick), nq0,
      sum(1 for c in pick if sum(1 for x in c[4][1:] if x != 0) == 1)), okE0 and len(pick) == 10)
okE1 = True
for (k1, k2, k3, k4, q, Qr) in pick:
    for (ka, kb) in ((k1, k3), (k2, k4)):
        fa, fb = spinor(ka), spinor(kb)
        J = cur(fb, fa)
        qq = [kb[i] - ka[i] for i in range(4)]
        okE1 = okE1 and (J[0] * QI(qq[0]) - J[1] * QI(qq[1]) - J[2] * QI(qq[2]) - J[3] * QI(qq[3])) == QI(0)
check("E1 current conservation: (k_out - k_in) . J(out, in) = 0 exactly for every GA transition current used", okE1)
# E2 photon polarisations as GA vectors with span{1, I4} coefficients on the left (i = I4)
def gavec(J):                                            # J^mu gamma_mu, complex coefficients on the left
    return add(*[mul(qmv(J[mu]), gen(mu), S4) for mu in range(4) if J[mu] != QI(0)])


def comm_half(Bv, x):
    return scl(F(1, 2), sub(mul(Bv, x, S4), mul(x, Bv, S4)))


def frame(qs, Qr):
    """A rational right-handed orthonormal frame (t1, t2, n) with n = qs/|qs|: a reflection taking e3 to n."""
    n = [F(x, Qr) for x in qs]
    E = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    if n == E[2]:
        return E[0], E[1], n
    if n == [F(0), F(0), F(-1)]:
        return E[1], E[0], n
    m = [n[0], n[1], n[2] - 1]
    mm = sum(x * x for x in m)
    R = lambda x: [x[i] - 2 * sum(x[j] * m[j] for j in range(3)) * m[i] / mm for i in range(3)]
    return R(E[1]), R(E[0]), n                           # reflection reverses handedness, so swap e1 and e2


def svec(t):
    return add(*[scl(t[i], gen(1 + i)) for i in range(3) if t[i] != 0])


def cross(x, y):
    return [x[1] * y[2] - x[2] * y[1], x[2] * y[0] - x[0] * y[2], x[0] * y[1] - x[1] * y[0]]


okE2a = okE2ac = okE2b = okE2c = okE2d = okE3 = okE3g = okfr = True
for (k1, k2, k3, k4, q, Qr) in pick:
    t1, t2, n = frame(q[1:], Qr)
    okfr = okfr and cross(t1, t2) == n and all(sum(x * y for x, y in zip(u, v)) == (1 if u is v else 0)
                                               for u in (t1, t2, n) for v in (t1, t2, n))
    # B_q = n1 g2g3 + n2 g3g1 + n3 g1g2 (g3g1 = -g1g3)
    Bq = add(scl(n[0], blade((2, 3))), scl(-n[1], blade((1, 3))), scl(n[2], blade((1, 2))))
    T1, T2 = svec(t1), svec(t2)
    eps = {}
    for h in (1, -1):
        eps[h] = sub(T1, scl(F(h), mul(I4, T2, S4)))
        okE2a = okE2a and eq(comm_half(Bq, eps[h]), scl(F(h), mul(I4, eps[h], S4)))
        wrongh = add(T1, scl(F(h), mul(I4, T2, S4)))
        okE2ac = okE2ac and not eq(comm_half(Bq, wrongh), scl(F(h), mul(I4, wrongh, S4)))
    JA, JB = cur(spinor(k3), spinor(k1)), cur(spinor(k4), spinor(k2))
    gA, gB = gavec(JA), gavec(JB)
    for h in (1, -1):
        epsc = [QI(0)] + [QI(t1[i], h * t2[i]) for i in range(3)]      # conj of t1 - h I4 t2
        okE2b = okE2b and to_q(proj(mul(gA, eps[h], S4))) == mdot(JA, epsc)
        okE2b = okE2b and to_q(proj(mul(gB, eps[h], S4))) == mdot(JB, epsc)
    Q2 = F(Qr) ** 2
    dotAB = JA[1] * JB[1] + JA[2] * JB[2] + JA[3] * JB[3]
    qA = JA[1] * QI(q[1]) + JA[2] * QI(q[2]) + JA[3] * QI(q[3])
    qB = JB[1] * QI(q[1]) + JB[2] * QI(q[2]) + JB[3] * QI(q[3])
    perp = dotAB - qA * qB * QI(1 / Q2)
    hs = hs_naive = QI(0)
    for h in (1, -1):
        hs = hs + to_q(proj(mul(gA, eps[h], S4))) * to_q(proj(mul(gB, eps[-h], S4))) * QI(F(1, 2))
        hs_naive = hs_naive + to_q(proj(mul(gA, eps[h], S4))) * to_q(proj(mul(gB, eps[h], S4))) * QI(F(1, 2))
    okE2c = okE2c and hs == perp
    okE2d = okE2d and hs_naive != perp
    # E3: Coulomb-gauge old-fashioned perturbation theory
    q0 = F(q[0])
    t = q0 * q0 - Q2
    den = QI(F(1) / (2 * Qr)) * (QI(1 / (q0 - Qr)) + QI(1 / (-q0 - Qr)))   # two time orderings, 1/(2|q|)
    T_coul = JA[0] * JB[0] * QI(1 / Q2)
    cov = mdot(JA, JB) * QI(-1 / t)
    okE3 = okE3 and (perp * den + T_coul) == cov
    okE3g = okE3g and (hs * den + T_coul) == cov                            # transverse sum from GA polarisations
nax = sum(1 for c in pick if sum(1 for x in c[4][1:] if x != 0) == 1)
check("E2.0 rational right-handed orthonormal frames (t1, t2, q/|q|) at all %d configurations (%d off the axes)" %
      (len(pick), len(pick) - nax), okfr)
check("E2.1 helicity in GA with i = I4: eps_h = t1 - h I4 t2 satisfies B_q . eps_h = h I4 eps_h, B_q the rotation "
      "bivector about q (dual of q/|q|), at all configurations; h is the I4-eigenvalue of B_q, and under the chi_+ "
      "convention (positive frequency exp(-I4 E t)) the physical helicity is -h", okE2a)
check("E2.1c control: the opposite-handed t1 + h I4 t2 fails the eigen-equation", okE2ac)
check("E2.2 the GA product of complex vectors is sesquilinear: proj(J eps) = J . conj(eps), the conjugation coming "
      "from I4 anticommuting with vectors (both currents, all configurations)", okE2b)
check("E2.3 the helicity sum (1/2) sum_h proj(J_A eps_h) proj(J_B eps_-h) equals the transverse product "
      "J_A_perp . J_B_perp at all configurations: in the GA product the absorbed photon carries the opposite label", okE2c)
check("E2.4 control: pairing each helicity with itself, (1/2) sum_h proj(J_A eps_h) proj(J_B eps_h), does not give "
      "the transverse product", okE2d)
check("E3 (arithmetic, conditional on E1) one-photon exchange in Coulomb gauge (two time orderings with energy "
      "denominators, plus the instantaneous Coulomb term) equals the covariant -J_A . J_B / t at all %d "
      "configurations, %d with q_0 != 0, with the analytic transverse projector" %
      (len(pick), sum(1 for c in pick if c[4][0] != 0)), okE3)
check("E3g the same with the transverse sum built from the GA polarisations of E2.3: the GA polarisations give the "
      "projector, on and off the axes", okE3g)
okE3b = True
okE3c = True
nonc = 0
for (k1, k2, k3, k4, q, Qr) in pick:
    if q[0] == 0:
        continue
    JA, JB = cur(spinor(k3), spinor(k1)), cur(spinor(k4), spinor(k2))
    Q2 = F(Qr) ** 2
    q0 = F(q[0])
    t = q0 * q0 - Q2
    den = QI(F(1) / (2 * Qr)) * (QI(1 / (q0 - Qr)) + QI(1 / (-q0 - Qr)))
    dotAB = JA[1] * JB[1] + JA[2] * JB[2] + JA[3] * JB[3]
    wrong = dotAB * den + JA[0] * JB[0] * QI(1 / Q2)          # no transverse projection
    nonc += 1
    okE3b = okE3b and wrong != mdot(JA, JB) * QI(-1 / t)
    # fake, non-conserved current: add a time component
    JF = [JA[0] + QI(1)] + JA[1:]
    qF = JF[1] * QI(q[1]) + JF[2] * QI(q[2]) + JF[3] * QI(q[3])
    qB = JB[1] * QI(q[1]) + JB[2] * QI(q[2]) + JB[3] * QI(q[3])
    perpF = JF[1] * JB[1] + JF[2] * JB[2] + JF[3] * JB[3] - qF * qB * QI(1 / Q2)
    okE3c = okE3c and perpF * den + JF[0] * JB[0] * QI(1 / Q2) != mdot(JF, JB) * QI(-1 / t)
check("E3b control: dropping the transverse projection (keeping longitudinal photons) breaks the equality when "
      "q_0 != 0 (all %d such configurations)" % nonc, okE3b and nonc > 0)
check("E3c control: for a non-conserved current (J_A^0 shifted by 1) the Coulomb-gauge sum differs from the covariant "
      "form at all %d q_0 != 0 configurations: E3 tests current conservation" % nonc, okE3c)
# E4 massive vector: contact limit
MV2 = F(10) ** 6
okE4 = True
for (k1, k2, k3, k4, q, Qr) in pick[:3]:
    JA, JB = cur(spinor(k3), spinor(k1)), cur(spinor(k4), spinor(k2))
    t = F(q[0]) ** 2 - F(Qr) ** 2
    massive = mdot(JA, JB) * QI(-1 / (t - MV2))
    contact = mdot(JA, JB) * QI(1 / MV2)
    okE4 = okE4 and (massive - contact) == contact * QI(t / (MV2 - t)) and contact != QI(0)
    qq = [QI(x) for x in q]
    okE4 = okE4 and mdot(JA, qq) == QI(0) and mdot(JB, qq) == QI(0)    # the Proca q_mu q_nu / M^2 term drops
check("E4 massive vector exchange -J.J/(t - M^2) = (J.J/M^2)(1 + t/(M^2 - t)) exactly: INT's contact term with "
      "G = e^2/M^2 plus a correction of relative size t/(M^2 - t) (M^2 = 10^6); the Proca q_mu q_nu/M^2 term drops "
      "because q . J = 0 at both vertices", okE4)

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f_ in FAILURES:
        print("  " + f_)
    sys.exit(1)
print("ALL CHECKS PASSED")
