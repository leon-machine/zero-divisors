#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_GRV.py: exact checks for "GA matter fields as the source of gravity in the element reading" (16 October 2026).
Preregistration: preregistration_GRV_2026-10-16.md. Findings: GRV_findings_2026-10-16.md.

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


def comm(x, y, S):
    return sub(mul(x, y, S), mul(y, x, S))


def planes(n):
    out = []
    for q in range(n):
        e_, f_ = 4 + 2 * q, 5 + 2 * q
        out.append((add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))),
                    add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))))
    return out


def vacuum(pl, S):
    vac = {(): F(1)}
    for (v, w) in pl:
        vac = mul(vac, mul(w, v, S), S)
    return vac


def coeff_on(Y, X, S):
    """z in span{1, I4} with Y = z X exactly, or None (X fixed and nonzero)."""
    if is_zero(Y):
        return QI(0)
    IX = mul(I4, X, S)
    keys = sorted(set(X) | set(IX))
    for b1 in keys:
        for b2 in keys:
            a11, a12, a21, a22 = X.get(b1, F(0)), IX.get(b1, F(0)), X.get(b2, F(0)), IX.get(b2, F(0))
            det = a11 * a22 - a12 * a21
            if det != 0:
                r1, r2 = Y.get(b1, F(0)), Y.get(b2, F(0))
                z = QI((r1 * a22 - a12 * r2) / det, (a11 * r2 - a21 * r1) / det)
                return z if eq(Y, mul(qmv(z), X, S)) else None
    return None


# ===========================================================================
print("=" * 72)
print("G1. The stress tensor of the GA fields with i = I4")
print("=" * 72)
okG1 = True
for k in [(5, 3, 4, 0), (3, 2, 1, 2), (9, 1, 4, 8), (7, 2, 3, 6)]:
    f = spinor(k)
    J = cur(f, f)
    c = J[0] * QI(F(1) / F(k[0]))
    okG1 = okG1 and all(J[mu] == c * QI(k[mu]) for mu in range(4)) and c.im == 0 and c.re > 0
    # with I4 d^nu on exp(-I4 k.x) f giving k^nu: T^{mu nu} = J^mu k^nu, symmetric because J ~ k
    T = [[J[mu] * QI(k[nu]) for nu in range(4)] for mu in range(4)]
    okG1 = okG1 and all(T[m][n] == T[n][m] for m in range(4) for n in range(4))
    kl = [k[0], -k[1], -k[2], -k[3]]
    okG1 = okG1 and all(sum((QI(kl[m]) * T[m][n] for m in range(4)), QI(0)) == QI(0) for n in range(4))
    okG1 = okG1 and T[0][0] == J[0] * QI(k[0]) and T[0][0].re > 0
check("G1.1 massless chi_+ modes (four momenta): J(f, f) = c k with c > 0; T^{mu nu} = J^mu k^nu (the definition, with "
      "I4 d^nu giving k^nu on exp(-I4 k.x) f) is symmetric and conserved, T^00 = J^0 k^0 > 0: energy per quantum k^0", okG1)
okG1b = True
for (p, m) in (((5, 3, 0, 0), 4), ((13, 5, 0, 0), 12), ((5, 0, 3, 0), 4), ((10, 6, 0, 0), 8), ((7, 2, 3, 6), 0)):
    if m == 0:
        continue                                     # (7; 2, 3, 6) is null: no rest frame, skipped
    pv = kvec(p)
    psi0 = add(sc(F(m)), mul(pv, G0, S4))
    okG1b = okG1b and eq(mul(pv, psi0, S4), scl(F(m), mul(psi0, G0, S4)))     # Dirac-Hestenes, p psi = m psi g0
    Jv = mul(mul(psi0, G0, S4), reverse(psi0), S4)
    # Jv must be a vector proportional to p (contravariant components p^mu gamma_mu)
    lam = Jv.get((0,), F(0)) / F(p[0])
    okG1b = okG1b and eq(Jv, scl(lam, pv)) and lam > 0
check("G1.2 massive Dirac-Hestenes plane waves psi_0 = m + p gamma_0 (p psi_0 = m psi_0 gamma_0): the current "
      "psi_0 gamma_0 psi_0~ is a positive multiple of p, so T^{mu nu} is proportional to p^mu p^nu and "
      "T^00 / J^0 = p^0, the mass at rest", okG1b)

# ===========================================================================
print("=" * 72)
print("G2-G3. The energy of a massive mode is a quasi-particle number")
print("=" * 72)
ST2 = tuple(list(S4) + [1, -1, 1, -1])
(va, wa), (vc, wc) = planes(2)


def block_H(K, mu):
    H = add(scl(F(K), mul(va, wa, ST2)), scl(F(K), mul(vc, wc, ST2)))
    return add(H, mul(qmv(mu), mul(wa, wc, ST2), ST2), mul(qmv(mu.conj()), mul(vc, va, ST2), ST2))


okG2 = okG3 = okG3b = True
for (K, mu) in ((3, QI(4)), (3, QI(F(12, 5), F(16, 5))), (5, QI(12)), (0, QI(1)), (0, QI(F(3, 5), F(4, 5)))):
    H = block_H(K, mu)
    m2 = mu.re ** 2 + mu.im ** 2
    E = F(math.isqrt(int(F(K) ** 2 + m2)))
    assert E * E == F(K) ** 2 + m2
    al = QI(2)
    be = al * QI(F(K) - E) * mu.conj() * QI(1 / m2)          # beta = (K - E) alpha / mu
    alp = QI(2)
    bep = alp * QI(E - F(K)) * mu.conj() * QI(1 / m2)        # beta' = (E - K) alpha' / mu
    ga = add(mul(qmv(al), wa, ST2), mul(qmv(be), vc, ST2))
    gc = add(mul(qmv(alp), wc, ST2), mul(qmv(bep), va, ST2))
    okG2 = okG2 and eq(comm(H, ga, ST2), scl(-E, ga)) and eq(comm(H, gc, ST2), scl(-E, gc))
    nrm_a = al.re ** 2 + al.im ** 2 + be.re ** 2 + be.im ** 2
    nrm_c = alp.re ** 2 + alp.im ** 2 + bep.re ** 2 + bep.im ** 2
    okG2 = okG2 and eq(add(mul(ga, star(ga, ST2), ST2), mul(star(ga, ST2), ga, ST2)), sc(nrm_a))
    Na = scl(1 / nrm_a, mul(star(ga, ST2), ga, ST2))
    Nc = scl(1 / nrm_c, mul(star(gc, ST2), gc, ST2))
    okG2 = okG2 and eq(H, add(scl(E, add(Na, Nc)), sc(F(K) - E)))
    na, nc = mul(va, wa, ST2), mul(vc, wc, ST2)
    okG3 = okG3 and is_zero(comm(Na, Nc, ST2)) and is_zero(comm(H, Na, ST2)) and is_zero(comm(H, Nc, ST2))
    okG3 = okG3 and is_zero(comm(na, nc, ST2)) and not is_zero(comm(H, na, ST2)) and not is_zero(comm(H, nc, ST2))
    # massive vacuum: annihilated by both gammas, with <n_a> != 0
    P0 = vacuum([(va, wa), (vc, wc)], ST2)
    lam = F(K) - E
    p = QI(0) - mu * QI(1 / lam)
    Om = add(mul(qmv(p), P0, ST2), mul(mul(va, vc, ST2), P0, ST2))
    okG3 = okG3 and is_zero(mul(ga, Om, ST2)) and is_zero(mul(gc, Om, ST2))
    nrm = coeff_on(mul(mul(P0, star(add(qmv(p), mul(va, vc, ST2)), ST2), ST2), Om, ST2), P0, ST2)
    nav = coeff_on(mul(mul(P0, star(add(qmv(p), mul(va, vc, ST2)), ST2), ST2), mul(na, Om, ST2), ST2), P0, ST2)
    okG3 = okG3 and nav is not None and nav != QI(0) and nav.im == 0
    # G3b: conserved numbers inside the rung algebra: the charge Q = n_a - n_c
    Q = sub(na, nc)
    okG3b_l = is_zero(comm(H, Q, ST2)) and eq(Q, sub(Na, Nc)) and is_zero(mul(Q, Om, ST2))
    # one quantum: the rung state v_a P0 is an eigenstate of H (energy K = (K - E) + E) with N_a = 1, N_c = 0
    one = mul(va, P0, ST2)
    okG3b_l = okG3b_l and eq(mul(H, one, ST2), scl(F(K), one)) and eq(mul(Na, one, ST2), one) and is_zero(mul(Nc, one, ST2))
    okG3b = okG3b and okG3b_l
    print("    K = %s, mu = %s: E = %s, <n_a> in the massive vacuum = %s" % (K, mu, E, nav * QI(1 / nrm.re)))
check("G2 on the mass block H = K(n_a + n_c) + mu w_a w_c + mu^* v_c v_a (five cases, mu complex included, K = 0 at "
      "rest): gamma_a = alpha w_a + beta v_c and gamma_c = alpha' w_c + beta' v_a satisfy [H, gamma] = -E gamma, and "
      "H = E (N_a + N_c) + (K - E) exactly, N = gamma^* gamma / {gamma, gamma^*}: the energy (T^00) of a massive mode "
      "is E times a quasi-particle number", okG2)
check("G3 the quasi-particle numbers commute with each other and with H; the single rung numbers n_a, n_c commute "
      "with each other but not with H when mu != 0; the massive vacuum is annihilated by both gammas and has "
      "<n_a> != 0", okG3)
check("G3b (added after review) the rung algebra does contain conserved numbers: the charge Q = n_a - n_c commutes "
      "with H, equals N_a - N_c exactly and vanishes on the massive vacuum; and one massive quantum is the rung state "
      "v_a P0 itself (energy K, N_a = 1, N_c = 0): the pairing only mixes the empty and doubly occupied states", okG3b)

# ===========================================================================
print("=" * 72)
print("G4-G5. The operator Newtonian coupling, and no self-gravity between branches")
print("=" * 72)
LAYOUTS = {"parallel (d = 4, separation 3)": (F(4), F(4), F(5), F(5)),
           "collinear (D = 10, separation 2)": (F(10), F(10), F(12), F(8)),
           "collinear (D = 7, separation 3)": (F(7), F(7), F(10), F(4))}
G_, MA, MB = F(1), F(2), F(3)
ST4 = tuple(list(S4) + [1, -1] * 4)
PL = planes(4)                     # 0 = A1, 1 = A2, 2 = B1, 3 = B2
N4 = [mul(v, w, ST4) for (v, w) in PL]
VAC4 = vacuum(PL, ST4)
okG4 = okG4c = okG5 = okG5c = True
for name, (r11, r22, r12, r21) in LAYOUTS.items():
    R = {(0, 2): r11, (1, 3): r22, (0, 3): r12, (1, 2): r21}
    HN = {}
    for (i, j), r in R.items():
        HN = add(HN, scl(-G_ * MA * MB / r, mul(N4[i], N4[j], ST4)))
    okG4 = okG4 and eq(star(HN, ST4), HN) and all(is_zero(comm(HN, n, ST4)) for n in N4)
    E = {}
    for (a, b) in ((0, 2), (0, 3), (1, 2), (1, 3)):
        st = mul(mul(PL[a][0], PL[b][0], ST4), VAC4, ST4)
        z = coeff_on(mul(HN, st, ST4), st, ST4)
        okG4 = okG4 and z is not None and z.im == 0
        E[(a, b)] = z.re
    # relative phase arg(c11 c22 / (c12 c21)) under exp(-I4 H t) is -(E11 + E22 - E12 - E21) t
    dE = E[(0, 2)] + E[(1, 3)] - E[(0, 3)] - E[(1, 2)]
    Phi_rate = G_ * MA * MB * (1 / r11 + 1 / r22 - 1 / r12 - 1 / r21)
    okG4 = okG4 and -dE == Phi_rate and Phi_rate != 0
    print("    %s: Phi / t = %s" % (name, Phi_rate))
    # mean-field (Schrodinger-Newton) control: the source is <N> = 1/2 for every branch mode, including the body's own
    RA = {(0, 1): F(5) if "parallel" in name else (F(2) if "D = 10" in name else F(3))}
    RB = {(2, 3): RA[(0, 1)]}
    allR = dict(R)
    allR.update(RA)
    allR.update(RB)
    Mass = [MA, MA, MB, MB]
    HSN = {}
    for (i, j), r in allR.items():
        HSN = add(HSN, scl(-G_ * Mass[i] * Mass[j] * F(1, 2) / r, add(N4[i], N4[j])))
    ESN = {}
    for (a, b) in ((0, 2), (0, 3), (1, 2), (1, 3)):
        st = mul(mul(PL[a][0], PL[b][0], ST4), VAC4, ST4)
        ESN[(a, b)] = coeff_on(mul(HSN, st, ST4), st, ST4).re
    okG5c = okG5c and ESN[(0, 2)] + ESN[(1, 3)] - ESN[(0, 3)] - ESN[(1, 2)] == 0
    # the self term: the same mean-field source without the body's own other branch
    HSN0 = {}
    for (i, j), r in R.items():
        HSN0 = add(HSN0, scl(-G_ * Mass[i] * Mass[j] * F(1, 2) / r, add(N4[i], N4[j])))
    for (a, b) in ((0, 2), (1, 3)):
        st = mul(mul(PL[a][0], PL[b][0], ST4), VAC4, ST4)
        e0 = coeff_on(mul(HSN0, st, ST4), st, ST4).re
        selfterm = ESN[(a, b)] - e0
        okG5c = okG5c and selfterm == -G_ * F(1, 2) * (MA * MA / RA[(0, 1)] + MB * MB / RB[(2, 3)]) and selfterm != 0
# G4c: the determinant factorises as c12 c21 (u - 1) with u the phase ratio; exact on rational unit phases
for (x, y) in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(1), F(0))):
    u = QI(x, y)
    c12, c21 = QI(F(1, 2)), QI(F(1, 2))
    c11, c22 = QI(F(1, 2)) * u, QI(F(1, 2))
    det = c11 * c22 - c12 * c21
    okG4c = okG4c and (det == QI(0)) == (u == QI(1))
check("G4 H_N = -G sum M_i M_j N_i N_j / r_ij (three layouts) is self-adjoint, commutes with every number (no matter "
      "quanta created or moved, by construction), has the branch states as eigenstates, and gives the relative phase arg(c11 c22 / (c12 c21)) = "
      "+Phi = (G M_A M_B / hbar)(1/r11 + 1/r22 - 1/r12 - 1/r21) t: the registration's phase with its sign", okG4)
check("G4c (algebraic identity) the entangling determinant is c12 c21 (u - 1), u = exp(I4 Phi): zero exactly when the "
      "phase ratio is 1, for an initial product state (three rational unit phases)", okG4c)
# G5: no self-gravity: N_A1 N_A2 = 0 on one-body states
for a in (0, 1):
    for b in (2, 3):
        st = mul(mul(PL[a][0], PL[b][0], ST4), VAC4, ST4)
        okG5 = okG5 and is_zero(mul(mul(N4[0], N4[1], ST4), st, ST4)) and is_zero(mul(mul(N4[2], N4[3], ST4), st, ST4))
check("G5 N_A1 N_A2 and N_B1 N_B2 annihilate every state with one body A and one body B: the operator source "
      "gives no gravitational interaction between a body's own branches", okG5)
check("G5c control: the mean-field (Schrodinger-Newton) source <N> gives branch energies whose combination "
      "E11 + E22 - E12 - E21 vanishes (no entanglement from a product state), and each branch carries a self term "
      "-G M^2 <N_other branch> / r from the body's own other branch, absent from the operator coupling", okG5c)

# G4m: massive bodies at rest, quasi-particle numbers (K = 0 blocks), parallel layout
print("    massive bodies at rest: four mass blocks (eight tower planes)")
ST8 = tuple(list(S4) + [1, -1] * 8)
PL8 = planes(8)
blocks = [(PL8[2 * b], PL8[2 * b + 1]) for b in range(4)]       # block b: (chi plane, eta plane)
Om8 = {(): F(1)}
gam = []
Hfree = {}
mrest = F(1)
for ((v1, w1), (v2, w2)) in blocks:
    P0b = mul(mul(w1, v1, ST8), mul(w2, v2, ST8), ST8)
    Om8 = mul(Om8, add(P0b, mul(mul(v1, v2, ST8), P0b, ST8)), ST8)
    g = sub(w1, v2)                                              # K = 0, mu = m = 1: gamma_a = w_a - v_c
    gam.append(g)
    Hb = add(mul(w1, w2, ST8), mul(v2, v1, ST8))
    Hfree = add(Hfree, scl(mrest, Hb))
Nq = [scl(F(1, 2), mul(star(g, ST8), g, ST8)) for g in gam]
okG4m = all(is_zero(mul(g, Om8, ST8)) for g in gam)
Qn = []
for ((v1, w1), (v2, w2)) in blocks:
    Qn.append(sub(mul(v1, w1, ST8), mul(v2, w2, ST8)))       # the charge of each block
okG4mq = True
for name, (r11, r22, r12, r21) in LAYOUTS.items():
    R = {(0, 2): r11, (1, 3): r22, (0, 3): r12, (1, 2): r21}
    for (src, okname) in ((Nq, "N"), (Qn, "Q")):
        HN8 = {}
        for (i, j), r in R.items():
            HN8 = add(HN8, scl(-G_ * MA * MB / r, mul(src[i], src[j], ST8)))
        okl = all(is_zero(comm(HN8, n, ST8)) for n in Nq) and all(is_zero(comm(Hfree, n, ST8)) for n in Nq)
        E8 = {}
        for (a, b) in ((0, 2), (0, 3), (1, 2), (1, 3)):
            st = mul(mul(star(gam[a], ST8), star(gam[b], ST8), ST8), Om8, ST8)
            zN = coeff_on(mul(HN8, st, ST8), st, ST8)
            zF = coeff_on(mul(Hfree, st, ST8), st, ST8)
            okl = okl and zN is not None and zF is not None
            E8[(a, b)] = (zN.re, zF.re)
        okl = okl and len(set(v[1] for v in E8.values())) == 1
        dE8 = E8[(0, 2)][0] + E8[(1, 3)][0] - E8[(0, 3)][0] - E8[(1, 2)][0]
        okl = okl and -dE8 == G_ * MA * MB * (1 / r11 + 1 / r22 - 1 / r12 - 1 / r21)
        if okname == "N":
            okG4m = okG4m and okl
        else:
            okG4mq = okG4mq and okl
check("G4m (the G4 model in the quasi-particle basis) massive bodies at rest, K = 0 mass blocks on the massive "
      "vacuum, three layouts: the branch states gamma_a^* gamma_b^* Omega are eigenstates of H_free and H_N, the free "
      "energies are branch-independent, and the relative phase is again +Phi", okG4m)
check("G4q (added after review) the same with the block charges Q = n_a - n_c, which lie in the rung algebra, as the "
      "source: same eigenstates, same +Phi at all three layouts", okG4mq)

# ===========================================================================
print("=" * 72)
print("G6. Composite rigid bodies: toward (P-iv)")
print("=" * 72)


def composite_phase(a, D, sep):
    """Two bodies of two constituents each (mass 1), collinear: A at 0 or sep, B at D or D + sep; constituents at
    +-a/2 about the body centre. Returns (Phi rate from the operator coupling, internal terms cancel?)."""
    ST_ = tuple(list(S4) + [1, -1] * 8)
    P = planes(8)
    # mode index: body (A=0,B=1), branch (0,1), constituent (0,1)
    idx = lambda body, br, c: 4 * body + 2 * br + c
    pos = {}
    for br in (0, 1):
        for c in (0, 1):
            off = (-a / 2) if c == 0 else (a / 2)
            pos[idx(0, br, c)] = (F(0) if br == 0 else sep) + off
            pos[idx(1, br, c)] = (D if br == 0 else D + sep) + off
    N = [mul(v, w, ST_) for (v, w) in P]
    H = {}
    for i in range(8):
        for j in range(i + 1, 8):
            same_body = (i // 4) == (j // 4)
            same_branch = ((i // 2) % 2) == ((j // 2) % 2)
            if same_body and not same_branch:
                continue                                  # never both occupied; omitted, then checked below
            H = add(H, scl(-F(1) / abs(pos[i] - pos[j]), mul(N[i], N[j], ST_)))
    vac = vacuum(P, ST_)
    Hint = {}
    for i in range(8):
        for j in range(i + 1, 8):
            if (i // 4) == (j // 4) and ((i // 2) % 2) == ((j // 2) % 2):
                Hint = add(Hint, scl(-F(1) / abs(pos[i] - pos[j]), mul(N[i], N[j], ST_)))
    E = {}
    Eint = set()
    okomit = True
    for ba in (0, 1):
        for bb in (0, 1):
            ops = [P[idx(0, ba, 0)][0], P[idx(0, ba, 1)][0], P[idx(1, bb, 0)][0], P[idx(1, bb, 1)][0]]
            st = vac
            for o in reversed(ops):
                st = mul(o, st, ST_)
            E[(ba, bb)] = coeff_on(mul(H, st, ST_), st, ST_).re
            Eint.add(coeff_on(mul(Hint, st, ST_), st, ST_).re)
            for i in range(8):
                for j in range(i + 1, 8):
                    if (i // 4) == (j // 4) and ((i // 2) % 2) != ((j // 2) % 2):
                        okomit = okomit and is_zero(mul(mul(N[i], N[j], ST_), st, ST_))
    dE = E[(0, 0)] + E[(1, 1)] - E[(0, 1)] - E[(1, 0)]
    return -dE, len(Eint) == 1, okomit


okG6 = True
D, sep = F(20), F(4)
mono = F(2) * F(2) * (1 / D + 1 / D - 1 / (D + sep) - 1 / (D - sep))
diffs = []
for a in (F(2), F(1)):
    ph, int_same, omit_ok = composite_phase(a, D, sep)
    okG6 = okG6 and int_same and omit_ok
    diffs.append(ph - mono)
    print("    a = %s: Phi/t = %s, monopole (M = 2) = %s" % (a, ph, mono))
ratio = diffs[0] / diffs[1]
okG6 = okG6 and diffs[1] != 0 and F(7, 2) < ratio < F(9, 2)
check("G6 composite rigid bodies (two constituents each, collinear, D = 20, separation 4): the internal terms are "
      "branch-independent and cancel from Phi; Phi equals the single-rung phase of mass M = 2m up to a correction "
      "that scales as a^2 (ratio %s on halving a): (P-iv) at monopole order, derived" % ratio, okG6)

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f_ in FAILURES:
        print("  " + f_)
    sys.exit(1)
print("ALL CHECKS PASSED")
