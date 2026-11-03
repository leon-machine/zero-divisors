#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_SMC.py: exact checks for "T12's chiral assignments under i = I4" (16 October 2026).
Preregistration: preregistration_SMC_2026-10-16.md. Findings: SMC_findings_2026-10-16.md.

Real Clifford algebras (GA.py, Fraction coefficients). Gaussian rationals (GA.QI) are used for the
2 x 2 and 3 x 3 gauge matrices of C4, with i read as I4. Exact arithmetic throughout.

Parts: C1 the two chirality halves against the Lorentz chiralities; C2 the twistor's unit against
the field's; C3 T12's spectrum and its anomalies under the listings; C4 the gauge representations
seen by I4-linear fields; C5 the internal grading against the spacetime chirality.
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



S4 = (1, -1, -1, -1)
S6 = (1, -1, -1, -1, 1, -1)                 # gamma_0..3, e_+, e_-
I4 = blade((0, 1, 2, 3))
Ebv = blade((4, 5))
I6 = blade((0, 1, 2, 3, 4, 5))
EB6 = [b for b in all_blades(6) if len(b) % 2 == 0]
OB6 = [b for b in all_blades(6) if len(b) % 2 == 1]
ALLB6 = all_blades(6)

# ===========================================================================
print("=" * 72)
print("C1. The two chirality halves of the twistor module against the Lorentz chiralities")
print("=" * 72)
g4 = [blade(b) for b in EB6 if len(b) == 4 and eq(mul(blade(b), blade(b), S6), sc(1))]
P = None
for Q1, Q2 in combinations(g4, 2):
    if not commutes(Q1, Q2, S6):
        continue
    PP = mul(scl(F(1, 2), add(sc(1), Q1)), scl(F(1, 2), add(sc(1), Q2)), S6)
    if eq(mul(PP, PP, S6), PP) and eq(reverse(PP), PP):
        if span_rank([mul(blade(b), PP, S6) for b in EB6], ALLB6) == 8:
            P = PP
            break


def basis_of(blist):
    out = []
    for b in blist:
        c = mul(blade(b), P, S6)
        if span_rank(out + [c], ALLB6) > len(out):
            out.append(c)
    return out


T = basis_of(EB6)                            # the even half (twistor space)
Tp = basis_of(OB6)                           # the odd half
okC1 = len(T) == 8 and len(Tp) == 8 and span_rank(T + Tp, ALLB6) == 16


def eig_space(basis, op, sign):
    imgs = [sub(mul(op, z, S6), scl(sign, z)) for z in basis]
    allb = sorted({bb for im in imgs for bb in im})
    rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, basis) for v in nullspace(rws, len(basis))] if rws else list(basis)


rotors = [add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1)))), add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2)))),
          mul(add(sc(F(5, 4)), scl(F(3, 4), blade((0, 2)))), add(sc(F(3, 5)), scl(F(4, 5), blade((2, 3)))), S6)]
halves = {}
for name, B in (("T", T), ("T'", Tp)):
    Lp, Lm = eig_space(B, Ebv, 1), eig_space(B, Ebv, -1)
    halves[name] = (Lp, Lm)
    okC1 = okC1 and len(Lp) == 4 and len(Lm) == 4
    for R in rotors:
        for (L, sgn) in ((Lp, 1), (Lm, -1)):
            for z in L:
                Rz = mul(R, z, S6)
                okC1 = okC1 and eq(mul(Ebv, Rz, S6), scl(sgn, Rz)) and span_rank(B + [Rz], ALLB6) == 8
        # I6 = +I4 on E = +1 and -I4 on E = -1
    okC1 = okC1 and all(eq(mul(I6, z, S6), mul(I4, z, S6)) for z in Lp)
    okC1 = okC1 and all(eq(mul(I6, z, S6), neg(mul(I4, z, S6))) for z in Lm)
# boost = -I4 x rotation as an algebra identity (every module)
okC1b = eq(blade((0, 1)), neg(mul(I4, blade((2, 3)), S4))) and eq(blade((0, 2)), mul(I4, blade((1, 3)), S4)) \
    and eq(blade((0, 3)), neg(mul(I4, blade((1, 2)), S4)))
check("C1 the even half T and the odd half T' of the Cl(2,4) spinor module are each preserved by Lorentz rotors and "
      "each splits into E = +1 and E = -1 doublets (real dimension 4 each), Lorentz-invariant, with I6 = +I4 on E = +1 "
      "and I6 = -I4 on E = -1", okC1)
check("C1b the boosts are -I4 (resp. +I4) times the dual rotations: g0g1 = -I4 g2g3, g0g2 = I4 g1g3, g0g3 = -I4 g1g2; "
      "so on a doublet where I4 = s i the boosts are -s i times rotations, and the sign s with respect to the module's "
      "complex unit i = I6 decides (1/2, 0) against (0, 1/2): each of T and T' contains both Lorentz chiralities", okC1b)

# ===========================================================================
print("=" * 72)
print("C2. The twistor's complex unit and the field's agree on one doublet only")
print("=" * 72)
ca, sa = F(4, 5), F(3, 5)                    # half angle alpha; rotation angle 2 alpha
okC2 = True
phases = {}


def kvec6(k):
    return add(*[scl(F(k[i]), gen(i)) for i in range(4) if k[i] != 0])


def frame(n):
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


for n in [(F(0), F(0), F(1)), (F(3, 5), F(4, 5), F(0)), (F(2, 3), F(1, 3), F(2, 3)), (F(1, 9), F(-4, 9), F(-8, 9))]:
    k = add(gen(0), svec(n))                 # null k = g0 + n
    t1, t2 = frame(n)
    T1, T2 = svec(t1), svec(t2)
    R = None
    for s_ in (1, -1):
        Rc = add(sc(ca), scl(F(s_) * sa, mul(T1, T2, S6)))
        if eq(mul(mul(Rc, T1, S6), reverse(Rc), S6), add(scl(ca * ca - sa * sa, T1), scl(2 * sa * ca, T2))):
            R = Rc
    for name in ("T", "T'"):
        for (L, Ename) in ((halves[name][0], "E=+1"), (halves[name][1], "E=-1")):
            # the massless spinors of momentum k in this doublet: ker(k) inside L
            imgs = [mul(k, z, S6) for z in L]
            allb = sorted({bb for im in imgs for bb in im})
            rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
            ker = [from_vec(v, L) for v in nullspace(rws, len(L))]
            okC2 = okC2 and len(ker) == 2
            lam4 = lam6 = None
            for s_ in (1, -1):
                if all(eq(mul(R, z, S6), add(scl(ca, z), scl(F(s_) * sa, mul(I4, z, S6)))) for z in ker):
                    lam4 = s_
                if all(eq(mul(R, z, S6), add(scl(ca, z), scl(F(s_) * sa, mul(I6, z, S6)))) for z in ker):
                    lam6 = s_
            okC2 = okC2 and lam4 is not None and lam6 is not None
            phases.setdefault((name, Ename), set()).add((lam4, lam6))
print("    rotation phases R z = (cos a + lam sin a X) z on ker(k), as (lam for X = I4, lam for X = I6):")
for key, v in sorted(phases.items()):
    print("      %s %s: %s" % (key[0], key[1], sorted(v)))
# controls: the reversed rotation sense, and a rotation about an axis perpendicular to k, fail the eigen-relation
okC2c = True
n = (F(3, 5), F(4, 5), F(0))
k = add(gen(0), svec(n))
t1, t2 = frame(n)
T1, T2 = svec(t1), svec(t2)
Rrev = add(sc(ca), scl(-sa, mul(T1, T2, S6)))
Rperp = add(sc(ca), scl(sa, mul(svec(n), T1, S6)))
for (L, _) in ((halves["T"][0], 1), (halves["T"][1], -1)):
    imgs = [mul(k, z, S6) for z in L]
    allb = sorted({bb for im in imgs for bb in im})
    ker = [from_vec(v, L) for v in nullspace([[im.get(bb, F(0)) for im in imgs] for bb in allb], len(L))]
    for Rx in (Rrev, Rperp):
        okC2c = okC2c and not all(eq(mul(Rx, z, S6), add(scl(ca, z), scl(-sa, mul(I4, z, S6)))) for z in ker)
uniform = all(len(v) == 1 for v in phases.values())
lam4s = {next(iter(v))[0] for v in phases.values()}
okC2 = okC2 and uniform and lam4s == {-1}
okC2 = okC2 and all(next(iter(phases[(nm, "E=+1")]))[1] == -next(iter(phases[(nm, "E=-1")]))[1] for nm in ("T", "T'"))
check("C2 (near-immediate: it holds in any Cl(1,3) module) on the massless spinors ker(k) in each doublet (four "
      "directions of k), the rotation about k acts as exp(-I4 alpha) in every doublet of both halves: with i = I4 "
      "every one is helicity +1/2 at positive frequency; with left I6 the E = +1 and E = -1 doublets carry opposite "
      "helicities", okC2)
check("C2c (added after review) controls: the reversed rotation sense and a rotation about an axis perpendicular to k "
      "fail the relation", okC2c)

# ===========================================================================
print("=" * 72)
print("C6. The Clifford-linear twistor unit, and where the orientation goes (added after review)")
print("=" * 72)
n0 = scl(F(1, 2), sub(gen(5), gen(4)))
ninf = add(gen(4), gen(5))


def rI6(z):
    return mul(z, I6, S6)


okC6a = True
for z in T:
    okC6a = okC6a and eq(rI6(z), mul(I6, z, S6)) and span_rank(T + [rI6(z)], ALLB6) == 8
for z in Tp:
    okC6a = okC6a and eq(rI6(z), neg(mul(I6, z, S6))) and span_rank(Tp + [rI6(z)], ALLB6) == 8
okC6a = okC6a and all(eq(mul(gen(i), rI6(z), S6), rI6(mul(gen(i), z, S6))) for i in range(6) for z in T[:2])
check("C6a the Clifford-linear twistor unit is J = right multiplication by I6: it commutes with the left action of "
      "every vector (which maps T to T'), preserves T and T', and equals +left I6 on T and -left I6 on T'", okC6a)


def kern(Bas, Y):
    imgs = [mul(Y, z, S6) for z in Bas]
    allb = sorted({bb for im in imgs for bb in im})
    rws = [[im.get(bb, F(0)) for im in imgs] for bb in allb]
    return [from_vec(v, Bas) for v in nullspace(rws, len(Bas))] if rws else list(Bas)


K0T, K0Tp = kern(T, n0), kern(Tp, n0)
okC6b = len(K0T) == 4 and len(K0Tp) == 4
okC6b = okC6b and all(eq(mul(Ebv, z, S6), z) for z in K0T + K0Tp)
okC6b = okC6b and all(eq(rI6(z), mul(I4, z, S6)) for z in K0T) and all(eq(rI6(z), neg(mul(I4, z, S6))) for z in K0Tp)
check("C6b the momentum doublet ker(n_0), which carries the incidence spinor pi, is the E = +1 doublet in both halves; "
      "on it J = +I4 in T and J = -I4 in T': with J as the twistor's unit and i = I4 as the field's, T's momentum "
      "spinors are I4-linear and T''s are I4-conjugate", okC6b)


def intertwiners(src, dst, extra_src, extra_dst):
    """Real-linear maps M: span(src) -> span(dst) commuting with the 15 bivectors and with the given unit."""
    gens = [blade(b) for b in all_blades(6) if len(b) == 2]
    ops = [(lambda z, g=g: mul(g, z, S6), lambda z, g=g: mul(g, z, S6)) for g in gens] + [(extra_src, extra_dst)]
    nd = len(dst)
    unknowns = len(src) * nd
    rows = []
    for (A_src, A_dst) in ops:
        # M A_src z_j = A_dst M z_j for every basis z_j; M z_j = sum_i m_ij d_i
        Acols_src = [solve_coords(A_src(z), src, ALLB6) for z in src]
        Acols_dst = [solve_coords(A_dst(d), dst, ALLB6) for d in dst]
        for j in range(len(src)):
            for r in range(nd):
                row = [F(0)] * unknowns
                for i in range(len(src)):
                    row[r * len(src) + i] += Acols_src[j][i]          # (M A z_j)_r = sum_i m_ri a_ij
                for i in range(nd):
                    row[i * len(src) + j] -= Acols_dst[i][r]          # (A M z_j)_r = sum_i A_ri m_ij
                rows.append(row)
    return len(nullspace(rows, unknowns))


dimJ = intertwiners(T, Tp, rI6, rI6)
dimL = intertwiners(T, Tp, lambda z: mul(I6, z, S6), lambda z: mul(I6, z, S6))
check("C6c with J the two halves are inequivalent complex so(2,4)-modules (intertwiner space dimension %d, twistors "
      "and dual twistors); with left I6 on both they are equivalent (dimension %d)" % (dimJ, dimL), dimJ == 0 and dimL == 2)
ep = gen(4)
okC6d = all(span_rank(Tp + [mul(ep, z, S6)], ALLB6) == 8 for z in T) and span_rank([mul(ep, z, S6) for z in T], ALLB6) == 8
okC6d = okC6d and commutes(ep, I4, S6) and all(commutes(ep, R, S6) for R in rotors) and anticommutes(ep, Ebv, S6)
check("C6d (the review's R4) left multiplication by e_+ maps T onto T', commutes with I4 and with Lorentz rotors, and "
      "swaps the E-doublets: Lorentz symmetry and i = I4 alone do not tell T from T'", okC6d)
# C6e: the sign of the twistor unit. With -J in place of J, the I4-linear momentum doublet moves to T'
okC6e = all(eq(neg(rI6(z)), mul(I4, z, S6)) for z in K0Tp) and all(eq(neg(rI6(z)), neg(mul(I4, z, S6))) for z in K0T)
check("C6e the commutant fixes the twistor's unit only up to sign (twistor run E1.3): with -J the I4-linear momentum "
      "doublet is T''s: which half is I4-linear is the relative sign of the twistor's unit and the field's", okC6e)

# ===========================================================================
print("=" * 72)
print("C3. T12's spectrum, its anomalies, and the listings")
print("=" * 72)
# one generation in T12's listing (a): (SU(2) dim, SU(3) rep label, Y)
LIST_A = [("Q", 2, "3", F(1, 6)), ("L", 2, "1", F(-1, 2)), ("uc", 1, "3b", F(-2, 3)), ("dc", 1, "3b", F(1, 3)),
          ("ec", 1, "1", F(1)), ("nuc", 1, "1", F(0))]
dim3 = {"1": 1, "3": 3, "3b": 3}


def conj(lst):
    return [(n + "bar", d, {"3": "3b", "3b": "3", "1": "1"}[c], -Y) for (n, d, c, Y) in lst]


def su3cubed(lst, sign=None):
    sg = sign or [1] * len(lst)
    return sum(s * d * {"3": 1, "3b": -1, "1": 0}[c] for s, (n, d, c, Y) in zip(sg, lst))


def anomalies(lst, sign=None):
    """The four anomaly sums for left-handed Weyl fields (sign: +1 per field, or a per-field list of +-1 for
    right-handed entries counted with -1)."""
    sg = sign or [1] * len(lst)
    su3 = sum(s * d * Y for s, (n, d, c, Y) in zip(sg, lst) if c != "1")
    su2 = sum(s * dim3[c] * Y for s, (n, d, c, Y) in zip(sg, lst) if d == 2)
    grav = sum(s * d * dim3[c] * Y for s, (n, d, c, Y) in zip(sg, lst))
    cub = sum(s * d * dim3[c] * Y ** 3 for s, (n, d, c, Y) in zip(sg, lst))
    return su3, su2, grav, cub


A = anomalies(LIST_A)
Bc = anomalies(conj(LIST_A))
mixed = anomalies(conj(LIST_A[:2]) + LIST_A[2:])
okC3 = A == (0, 0, 0, 0) and Bc == (0, 0, 0, 0) and (mixed[0], mixed[3]) == (F(-2, 3), F(4, 9))
# with i = I4 the I4-particles are right-handed; listing (a) read as left-handed enters conjugated: the
# I4-linear content is conj(LIST_A), all right-handed; as right-handed fields their anomaly contributions carry -1
RH = anomalies(conj(LIST_A), sign=[-1] * len(LIST_A))
okC3 = okC3 and RH == (0, 0, 0, 0) and su3cubed(LIST_A) == 0 and su3cubed(conj(LIST_A)) == 0
okC3 = okC3 and su3cubed(conj(LIST_A[:2]) + LIST_A[2:]) == -4
# all 64 conjugation patterns: which are anomaly-free (five conditions)?
free = []
for mask in range(64):
    lst = [conj([f])[0] if (mask >> i) & 1 else f for i, f in enumerate(LIST_A)]
    if anomalies(lst) == (0, 0, 0, 0) and su3cubed(lst) == 0:
        free.append(mask)
okC3 = okC3 and len(free) == 4 and all(((m ^ 63) & 31) == 0 or (m & 31) == 0 for m in free)
print("    anomaly-free conjugation patterns: %s (bit i conjugates %s)" % (free, [f[0] for f in LIST_A]))
check("C3 T12's listing (a) and its conjugate (b) both satisfy the four anomaly conditions; the mixed listing (doublets "
      "conjugated, singlets not) gives [SU(3)]^2 U(1) = %s, cubic = %s and [SU(3)]^3 = -4; of the 64 conjugation "
      "patterns exactly four are anomaly-free, (a) and (b) each with nu^c either way (nu^c is self-conjugate): every "
      "multiplet except nu^c must enter with the same status" % (mixed[0], mixed[3]), okC3)

# ===========================================================================
print("=" * 72)
print("C4. The gauge representations seen by I4-linear fields")
print("=" * 72)
I = QI(0, 1)
Z, O = QI(0), QI(1)


def mm(A_, B_):
    n = len(A_)
    return [[sum((A_[i][k] * B_[k][j] for k in range(n)), QI(0)) for j in range(n)] for i in range(n)]


def mconj(A_):
    return [[z.conj() for z in r] for r in A_]


def mscal(c, A_):
    return [[c * z for z in r] for r in A_]


half = QI(F(1, 2))
sig = [[[Z, O], [O, Z]], [[Z, QI(0, -1)], [I, Z]], [[O, Z], [Z, QI(-1)]]]
X2 = [mscal(I * half, s) for s in sig]                              # su(2) generators i sigma/2
eps = [[Z, O], [QI(-1), Z]]
epsinv = [[Z, QI(-1)], [O, Z]]
okC4a = all(mm(mm(eps, mconj(X), ), epsinv) == X for X in X2)
# su(3): i lambda_a / 2
lam = []
def M3(entries):
    m = [[QI(0)] * 3 for _ in range(3)]
    for (i, j, z) in entries:
        m[i][j] = z
    return m
lam.append(M3([(0, 1, O), (1, 0, O)]))
lam.append(M3([(0, 1, QI(0, -1)), (1, 0, I)]))
lam.append(M3([(0, 0, O), (1, 1, QI(-1))]))
lam.append(M3([(0, 2, O), (2, 0, O)]))
lam.append(M3([(0, 2, QI(0, -1)), (2, 0, I)]))
lam.append(M3([(1, 2, O), (2, 1, O)]))
lam.append(M3([(1, 2, QI(0, -1)), (2, 1, I)]))
lam8 = M3([(0, 0, O), (1, 1, O), (2, 2, QI(-2))])                   # times 1/sqrt3: irrelevant for intertwining
lam.append(lam8)
X3 = [mscal(I * half, l) for l in lam]
# solve M X^* = X M for all a: 9 complex = 18 real unknowns
unk = []
for i in range(3):
    for j in range(3):
        for part in (0, 1):
            unk.append((i, j, part))
rows = []
for X in X3:
    Xc = mconj(X)
    for i in range(3):
        for j in range(3):
            # (M Xc - X M)_{ij} = sum_k M_ik Xc_kj - X_ik M_kj ; real and imaginary parts
            re_row, im_row = [F(0)] * 18, [F(0)] * 18
            for kk in range(3):
                for (src, coef) in (((i, kk), Xc[kk][j]), ((kk, j), QI(0) - X[i][kk])):
                    idx_re = unk.index((src[0], src[1], 0))
                    idx_im = unk.index((src[0], src[1], 1))
                    # (a + b i)(c + d i) = (ac - bd) + (ad + bc) i, with M entry a + b i
                    re_row[idx_re] += coef.re
                    re_row[idx_im] += -coef.im
                    im_row[idx_re] += coef.im
                    im_row[idx_im] += coef.re
            rows.append(re_row)
            rows.append(im_row)
ns3 = nullspace(rows, 18)
okC4b = len(ns3) == 0
# the same solve for su(2) finds the epsilon intertwiner (a one-complex-dimensional space)
unk2 = [(i, j, p) for i in range(2) for j in range(2) for p in (0, 1)]
rows2 = []
for X in X2:
    Xc = mconj(X)
    for i in range(2):
        for j in range(2):
            re_row, im_row = [F(0)] * 8, [F(0)] * 8
            for kk in range(2):
                for (src, coef) in (((i, kk), Xc[kk][j]), ((kk, j), QI(0) - X[i][kk])):
                    ir, ii = unk2.index((src[0], src[1], 0)), unk2.index((src[0], src[1], 1))
                    re_row[ir] += coef.re
                    re_row[ii] += -coef.im
                    im_row[ir] += coef.im
                    im_row[ii] += coef.re
            rows2.append(re_row)
            rows2.append(im_row)
okC4a = okC4a and len(nullspace(rows2, 8)) == 2
check("C4 (standard, computed) with numbers span{1, I4}: the conjugate of the SU(2) doublet is equivalent to it "
      "through epsilon (intertwiner space of complex dimension 1), while the conjugate of the SU(3) triplet admits no "
      "intertwiner: a multiplet read I4-antilinearly is an SU(2) doublet, an antitriplet, of opposite hypercharge", okC4a and okC4b)

# ===========================================================================
print("=" * 72)
print("C5. The internal grading against the spacetime chirality")
print("=" * 72)
NP = 5
ST = tuple(list(S4) + [1, -1] * NP)
pl = []
for q in range(NP):
    e_, f_ = 4 + 2 * q, 5 + 2 * q
    pl.append((add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_))), add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))))
Pi = sc(1)
for (v, w) in pl:
    Pi = mul(Pi, sub(sc(1), scl(F(2), mul(v, w, ST))), ST)          # internal parity (-1)^N
IS3 = {(1, 2): F(-1)}


def chi(e_, p):
    return scl(F(1, 2), sub(p, scl(F(e_), mul(mul(I4, p, ST), IS3, ST))))


okC5 = eq(mul(Pi, Pi, ST), sc(1)) and commutes(Pi, I4, ST)
lor4 = [add(sc(F(5, 4)), scl(F(3, 4), blade((0, 1)))), add(sc(F(3, 5)), scl(F(4, 5), blade((1, 2))))]
okC5 = okC5 and all(commutes(Pi, R, ST) for R in lor4)
# chirality projection (left I4, right I sigma_3 on the ground value) commutes with the internal parity on states
vac = sc(1)
for (v, w) in pl:
    vac = mul(vac, mul(w, v, ST), ST)
states = [vac, mul(pl[0][0], vac, ST), mul(mul(pl[1][0], pl[3][0], ST), vac, ST)]
vals = [blade(b) for b in all_blades(4) if len(b) % 2 == 0]
for s_ in states:
    for u in vals:
        x = mul(u, s_, ST)
        for e_ in (1, -1):
            okC5 = okC5 and eq(chi(e_, mul(Pi, x, ST)), mul(Pi, chi(e_, x), ST))
# both identifications are Lorentz-invariant and I4-linear: the projectors (1 +- Pi)/2 (x) chi_e commute with rotors
for sgn in (1, -1):
    Proj = scl(F(1, 2), add(sc(1), scl(F(sgn), Pi)))
    okC5 = okC5 and all(commutes(Proj, R, ST) for R in lor4) and commutes(Proj, I4, ST)
check("C5 (true by construction) in S (x) H (ground values, five internal modes of the label copy): the internal parity "
      "(-1)^N squares to 1 and commutes with I4, with Lorentz rotors and with the chirality projections: the label "
      "copy's grading is independent of spacetime chirality, which is why T12 needs (S) to tie them", okC5)

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f_ in FAILURES:
        print("  " + f_)
    sys.exit(1)
print("ALL CHECKS PASSED")
