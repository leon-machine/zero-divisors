#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_GA2Q.py: exact checks for "Second quantisation of multivector-valued fields in GA"
(16 October 2026). Preregistration: preregistration_GA2Q_2026-10-16.md.
Findings: GA2Q_findings_2026-10-16.md.

Real Clifford algebra only (GA.py, Fraction coefficients). Gaussian rationals (GA.QI) are used
only as bookkeeping for the expected complex numbers and to produce rational points on the unit
circle; every field-theoretic construction is done in the real algebra of the ground Cl(1,3) and
the tower planes.
"""

import sys
from fractions import Fraction as F
from itertools import combinations

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


# ---------------------------------------------------------------------------
# the ground: Cl(1,3); values are even elements
# ---------------------------------------------------------------------------
S4 = (1, -1, -1, -1)
I4 = blade((0, 1, 2, 3))
IS3 = {(1, 2): F(-1)}                       # I sigma_3 = gamma_2 gamma_1
G0 = gen(0)
EVEN = [blade(b) for b in all_blades(4) if len(b) % 2 == 0]


def dag(phi, s=S4):
    return star(phi, s)


def alpha(phi, u):
    return mul(dag(phi), u, S4).get((), F(0))


def J(phi):
    return mul(phi, IS3, S4)


def cpair(phi, u):
    """<phi, u> = alpha(phi, u) + i alpha(phi J, u): antilinear in phi, linear in u, i = right I sigma_3."""
    return QI(alpha(phi, u), alpha(J(phi), u))


def chi(eps, phi):
    return scl(F(1, 2), sub(phi, scl(F(eps), mul(mul(I4, phi, S4), IS3, S4))))


def rphase(u, z):
    """u times the unit complex number z, i acting as right I sigma_3."""
    return add(scl(z.re, u), scl(z.im, J(u)))


def kvec(k):
    return add(*[scl(F(k[m]), gen(m)) for m in range(4) if k[m] != 0])


def Lam(k, phi):
    return scl(F(1, 2 * k[0]), mul(mul(kvec(k), G0, S4), phi, S4))


phis = [{(): F(1), (0, 1): F(2), (1, 3): F(-1), (0, 1, 2, 3): F(1, 2)},
        {(0, 2): F(1), (2, 3): F(3), (): F(-2)},
        {(1, 2): F(1), (0, 3): F(-1, 3), (0, 1, 2, 3): F(2)}]

# ===========================================================================
print("=" * 72)
print("Q1. The pairing is the projection onto span{1, I4}")
print("=" * 72)

ok_chi = all(eq(chi(e, chi(e, b)), chi(e, b)) for e in (1, -1) for b in EVEN) and \
    all(eq(mul(I4, chi(e, b), S4), scl(F(e), mul(chi(e, b), IS3, S4))) for e in (1, -1) for b in EVEN)
check("Q1.0 chi_eps(phi) = (phi - eps I4 phi I sigma_3)/2 is idempotent with I4 u = eps u I sigma_3 on its range",
      ok_chi)


def proj14(x):
    """Projection onto the ground's span{1, I4}, tower parts carried along."""
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (0, 1, 2, 3):
            out[b] = c
    return out


def cnum_to_mv(z, eps):
    return add(sc(z.re), scl(F(eps) * z.im, I4))


okq1 = True
for eps in (1, -1):
    for b in EVEN:
        u = chi(eps, b)
        if is_zero(u):
            continue
        for phi in EVEN + phis:
            okq1 = okq1 and eq(proj14(mul(dag(phi), u, S4)), cnum_to_mv(cpair(phi, u), eps))
check("Q1.1 for chiral u (both signs) and every even phi tested, <phi, u> = projection of phi^dagger u onto "
      "span{1, I4}, with i read as eps I4", okq1)
nonchiral = add(chi(1, blade(())), chi(-1, blade((0, 1))))
fails = {e: any(not eq(proj14(mul(dag(phi), nonchiral, S4)), cnum_to_mv(cpair(phi, nonchiral), e))
                for phi in EVEN + phis) for e in (1, -1)}
check("Q1.2 control (added, not preregistered): for a non-chiral u the projection fails to be the pairing for "
      "some test spinor, for either reading of the sign", fails[1] and fails[-1])

# ===========================================================================
print("=" * 72)
print("Q2. Lambda(k) = k gamma_0 / 2k_0 is the projector onto ker k; GA completeness")
print("=" * 72)

KS = [(1, 0, 0, 1), (5, 3, 4, 0), (3, 2, 1, 2)]


def mat_of(op):
    """8 x 8 real matrix of a linear map on the even algebra (columns = images of EVEN)."""
    eb = [b for b in all_blades(4) if len(b) % 2 == 0]
    cols = [op(blade(b)) for b in eb]
    return [[cols[j].get(eb[i], F(0)) for j in range(8)] for i in range(8)]


def rank(M):
    return GA.rank_of_vectors([list(r) for r in M])


okL = True
for k in KS:
    kv = kvec(k)
    okL = okL and is_zero(mul(kv, kv, S4))
    for b in EVEN:
        lb = Lam(k, b)
        okL = okL and eq(Lam(k, lb), lb)                                  # idempotent
        okL = okL and is_zero(mul(kv, lb, S4))                            # range in ker k
        okL = okL and eq(Lam(k, J(b)), J(lb))                             # C-linear
        if is_zero(mul(kv, b, S4)):
            okL = okL and eq(lb, b)                                       # identity on ker k
    for b1 in EVEN:
        for b2 in EVEN:
            okL = okL and alpha(Lam(k, b1), b2) == alpha(b1, Lam(k, b2))  # self-adjoint
    okL = okL and rank(mat_of(lambda p: Lam(k, p))) == 4
check("Q2.1 for three null k, Lambda(k) is idempotent, self-adjoint for alpha, C-linear, the identity on ker k, "
      "with range ker k of rank 4: the orthogonal projector onto ker k", okL)
check("Q2.2 Lambda(k) commutes with chi_eps (both signs)",
      all(eq(Lam(k, chi(e, b)), chi(e, Lam(k, b))) for k in KS for e in (1, -1) for b in EVEN))
F_ = {}
okF = True
for k in KS:
    for eps in (1, -1):
        f = None
        for b in EVEN:
            c = Lam(k, chi(eps, b))
            if not is_zero(c):
                f = c
                break
        F_[(k, eps)] = f
        a_ = alpha(f, f)
        for phi in EVEN + phis:
            lhs = rphase(f, cpair(f, phi))                               # f <f, phi>
            rhs = scl(a_, Lam(k, chi(eps, phi)))
            okF = okF and eq(lhs, rhs)
        okF = okF and rank(mat_of(lambda p, k=k, eps=eps: Lam(k, chi(eps, p)))) == 2
check("Q2.3 GA completeness: for f in ker k of chirality eps, f <f, phi> = alpha(f, f) Lambda(k) chi_eps(phi) for "
      "every phi tested; Lambda(k) chi_eps has real rank 2 (complex 1)", okF)

# ===========================================================================
print("=" * 72)
print("Q3. The field in the single algebra: anticommutator = GA propagator")
print("=" * 72)

NM = len(KS)
NPL = 4 * NM                                     # planes: particle and antiparticle, two chiralities
SB = tuple(list(S4) + [1, -1] * NPL)


def plane(p):
    e_, f_ = 4 + 2 * p, 5 + 2 * p
    v = add(scl(F(1, 2), gen(e_)), scl(F(1, 2), gen(f_)))
    w = add(scl(F(1, 2), gen(e_)), scl(F(-1, 2), gen(f_)))
    return v, w                                  # v creates, w annihilates (T03)


PL = [plane(p) for p in range(NPL)]
# phases e^{-i k_j . x} at two points x and y (rational points of the unit circle)
PX = [QI(F(3, 5), F(-4, 5)), QI(F(5, 13), F(12, 13)), QI(F(-8, 17), F(15, 17))]
PY = [QI(F(7, 25), F(24, 25)), QI(F(-3, 5), F(-4, 5)), QI(F(20, 29), F(21, 29))]


def field(phase, chiralities):
    """Psi = sum_j [ f_j p_j w_(particle plane) + f_j conj(p_j) v_(antiparticle plane) ] in the single algebra."""
    out = {}
    for j, k in enumerate(KS):
        for ci, eps in enumerate(chiralities):
            f = F_[(k, eps)]
            pp = 4 * j + 2 * ci
            ap = pp + 1
            up = rphase(f, phase[j])
            vm = rphase(f, phase[j].conj())
            out = add(out, mul(up, PL[pp][1], SB), mul(vm, PL[ap][0], SB))
    return out


def comp(phi, Psi):
    return proj14(mul(dag(phi, SB), Psi, SB))


def anti(a, b):
    return add(mul(a, b, SB), mul(b, a, SB))


def expected(phi1, phi2, chiralities, conj_for=()):
    tot = QI(0)
    for j, k in enumerate(KS):
        for eps in chiralities:
            f = F_[(k, eps)]
            term = QI(0)
            for (px, py) in ((PX[j], PY[j]), (PX[j].conj(), PY[j].conj())):
                term = term + cpair(phi1, rphase(f, px)) * cpair(rphase(f, py), phi2)
            tot = tot + (term.conj() if eps in conj_for else term)
    return tot


PsiX = field(PX, (1,))
PsiY = field(PY, (1,))
okQ3 = True
okNoTower = True
for phi1 in phis:
    for phi2 in phis:
        A = anti(comp(phi1, PsiX), star(comp(phi2, PsiY), SB))
        okNoTower = okNoTower and all(max(b) < 4 if b else True for b in A)
        okQ3 = okQ3 and eq(A, cnum_to_mv(expected(phi1, phi2, (1,)), 1))
check("Q3.1 the anticommutator {Psi(x; phi_1), Psi(y; phi_2)^*}, computed in the single algebra (ground plus 12 "
      "planes), has no tower part", okNoTower)
check("Q3.2 ... and equals <phi_1, (S_+ + S_-)(x, y) phi_2> with i -> I4 (eps = +1), for all pairs of test spinors",
      okQ3)
okcos = True
for phi1 in phis:
    for phi2 in phis:
        tot = QI(0)
        for j, k in enumerate(KS):
            f = F_[(k, 1)]
            ph = PX[j] * PY[j].conj()
            cosv = ph.re
            tot = tot + QI(2 * alpha(f, f) * cosv) * cpair(phi1, Lam(k, chi(1, phi2)))
        okcos = okcos and tot == expected(phi1, phi2, (1,))
check("Q3.3 the GA form of the kernel: S_+ + S_- = sum_j 2 alpha_j cos(k_j . (x - y)) Lambda(k_j) chi_+, real "
      "(no complex unit needed)", okcos)

# ===========================================================================
print("=" * 72)
print("Q4. Locality (assembly)")
print("=" * 72)

okk = all(eq(scl(F(2 * k[0]), Lam(k, sc(1))), mul(kvec(k), G0, S4)) for k in KS)
check("Q4.1 2 k_0 Lambda(k) = k gamma_0: the kernel is sum_j (alpha_j/k_j0) cos(k_j . xi) k_j gamma_0, which is "
      "nabla[sum_j (alpha_j/k_j0) sin(k_j . xi)] gamma_0 (nabla sin(k.xi) = k cos(k.xi)); the bracket is the "
      "scalar commutator function in the continuum (import)", okk)

# ===========================================================================
print("=" * 72)
print("Q5. Bilinears are the second-quantisation functor")
print("=" * 72)


def particle_field(phase, eps):
    out = {}
    for j, k in enumerate(KS):
        f = F_[(k, eps)]
        out = add(out, mul(rphase(f, phase[j]), PL[4 * j][1], SB))
    return out


Psi_p = particle_field(PX, 1)
Ms = [("1 (density)", sc(1)), ("gamma_0 gamma_1 (a current component)", blade((0, 1))),
      ("gamma_1 gamma_2 (spin)", blade((1, 2)))]
for lab, M in Ms:
    lhs = proj14(mul(mul(star(Psi_p, SB), M, SB), Psi_p, SB))
    rhs = {}
    for c, kc in enumerate(KS):
        uc = rphase(F_[(kc, 1)], PX[c])
        for d, kd in enumerate(KS):
            ud = rphase(F_[(kd, 1)], PX[d])
            z = cpair(uc, mul(M, ud, S4))
            rhs = add(rhs, mul(cnum_to_mv(z, 1), mul(PL[4 * c][0], PL[4 * d][1], SB), SB))
    check("Q5 M = %s: projection of Psi^* M Psi onto span{1, I4} = sum_cd <u_c, M u_d> a_c^* a_d, i -> I4" % lab,
          eq(lhs, rhs))

# ===========================================================================
print("=" * 72)
print("Q6. Mixed chirality")
print("=" * 72)

PsiXm = field(PX, (1, -1))
PsiYm = field(PY, (1, -1))
bad = False
okconj = True
for phi1 in phis:
    for phi2 in phis:
        A = anti(comp(phi1, PsiXm), star(comp(phi2, PsiYm), SB))
        if not eq(A, cnum_to_mv(expected(phi1, phi2, (1, -1)), 1)):
            bad = True
        okconj = okconj and eq(A, cnum_to_mv(expected(phi1, phi2, (1, -1), conj_for=(-1,)), 1))
check("Q6.1 with both chiralities in one field the anticommutator is NOT <phi_1, S phi_2> (i -> I4)", bad)
check("Q6.2 ... it is <phi_1, S_R phi_2> + conj <phi_1, S_L phi_2>: the other chirality enters as its complex "
      "conjugate (its charge conjugate)", okconj)

# post-review: the same mixed field read through Hestenes' projection onto span{1, I sigma_3}


def projq(x):
    out = {}
    for b, c in x.items():
        g = tuple(i for i in b if i < 4)
        if g == () or g == (1, 2):
            out[b] = c
    return out


def cnum_to_q(z, sgn):
    return add(sc(z.re), scl(F(sgn) * z.im, IS3))


check("Q6.3 (post-review) I sigma_3 commutes with every tower vector, so it is also available as the operator i",
      all(commutes(IS3, gen(i), SB) for i in range(4, 4 + 2 * NPL)))
res = {}
for sgn in (1, -1):
    okq = True
    for phi1 in phis:
        for phi2 in phis:
            A = anti(projq(mul(dag(phi1, SB), PsiXm, SB)), star(projq(mul(dag(phi2, SB), PsiYm, SB)), SB))
            okq = okq and eq(A, cnum_to_q(expected(phi1, phi2, (1, -1)), sgn))
    res[sgn] = okq
check("Q6.4 (post-review) the two-chirality field read through the projection onto span{1, I sigma_3}, with "
      "operator i = %s I sigma_3, reproduces <phi_1, S phi_2> for both chiralities at once: no splitting is "
      "needed with Hestenes' i" % ("+" if res[1] else "-"), res[1] or res[-1])
okeps = True
PsiXn = field(PX, (-1,))
PsiYn = field(PY, (-1,))
for phi1 in phis:
    for phi2 in phis:
        A = anti(comp(phi1, PsiXn), star(comp(phi2, PsiYn), SB))
        okeps = okeps and eq(A, cnum_to_mv(expected(phi1, phi2, (-1,)), -1))
check("Q3.4 (post-review) the single-chirality construction also works for eps = -1, with i -> -I4", okeps)

# ===========================================================================
print("=" * 72)
print("Q7. Control: the projection is needed")
print("=" * 72)

raw = anti(mul(dag(phis[0], SB), PsiX, SB), star(mul(dag(phis[1], SB), PsiY, SB), SB))
check("Q7 without the projection the anticommutator has ground components outside span{1, I4}",
      any(tuple(i for i in b if i < 4) not in ((), (0, 1, 2, 3)) for b in raw))

print("=" * 72)
print("%d checks" % NCHECKS[0])
if FAILURES:
    print("FAILURES (%d):" % len(FAILURES))
    for f in FAILURES:
        print("  " + f)
    sys.exit(1)
print("ALL CHECKS PASSED")
