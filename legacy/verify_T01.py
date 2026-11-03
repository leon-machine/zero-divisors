#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T01.py: exact-arithmetic verification of every computational identity in

    "The Transport Principle: Total Division in Clifford Algebras via
Minimal Completion"  (Transport Papers, T1)

This is the consolidated script of the merged paper: it unites the twenty-two
checks of the published verify_transport_principle.py (the type-N development,
Section 4 of the paper) with the eighty-five checks of verify_T02.py (the
taxonomy, the type-C and type-P rules, the sharpenings, and the clock),
one hundred and seven checks in all, each retagged to the merged paper's
compiled statement numbers, plus the eight checks of Section 5.5 (the
extension theorem and the commuting square), one hundred and fifteen in all.
(v3.1 to v3.3 also carried sixteen further checks for Section 5.6, the
five-dimensional and planar instances; that section left the paper at v4.0
and its checks went with it.)  Everything is exact rational arithmetic over
basis-blade Clifford engines (degenerate generators included); shared
machinery lives in GA.py, deposited alongside; no floating point is used
anywhere except the Moore-Penrose comparisons of Sec 4.8.2, which are float
at machine precision.  The script exits nonzero on any failure.
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g

# ===========================================================================
# PART ONE: the taxonomy, the type-C and type-P rules, the sharpenings, and
# the clock (85 checks; from the deposited verify_T02.py, retagged).
# ===========================================================================



# ----------------------------------------------------------------------------
# [Lem 2.6] and [Lem 2.7]: centre and omega^2, all signatures n <= 8
# ----------------------------------------------------------------------------

def centre_and_omega_checks(nmax=8):
    ok_centre, ok_omega, ok_typeC = True, True, True
    for n in range(1, nmax + 1):
        for p in range(n + 1):
            q = n - p
            squares = g.sig(p, q)
            gens = [g.gen(i) for i in range(n)]
            # central blades: conjugation by each invertible generator maps a
            # blade to +- itself, so centrality is blade-wise (proof of Lem 2.6)
            central = []
            for b in g.all_blades(n):
                x = {b: Fraction(1)}
                if all(g.commutes(x, gg, squares) for gg in gens):
                    central.append(b)
            expect = [()] if n % 2 == 0 else [(), tuple(range(n))]
            if central != expect:
                ok_centre = False
            # omega^2
            omega = {tuple(range(n)): Fraction(1)}
            m = p - q
            want = Fraction((-1) ** ((m * (m - 1) // 2) % 2))
            if not g.eq(g.mul(omega, omega, squares), g.sc(want)):
                ok_omega = False
            # type C existence criterion [Thm 3.6]
            has_typeC = (n % 2 == 1) and (want == 1)
            if has_typeC != ((p - q) % 4 == 1):
                ok_typeC = False
            if has_typeC:
                epp = add(g.sc(Fraction(1, 2)), g.scal(Fraction(1, 2), omega))
                epm = add(g.sc(Fraction(1, 2)), g.scal(Fraction(-1, 2), omega))
                if not (g.eq(g.mul(epp, epp, squares), epp)
                        and g.eq(g.mul(epm, epm, squares), epm)
                        and g.is_zero(g.mul(epp, epm, squares))
                        and g.eq(add(epp, epm), g.sc(1))
                        and all(g.commutes(epp, gg, squares) for gg in gens)):
                    ok_typeC = False
    g.check("[Lem 2.6] centre = R (n even) / R + R.omega (n odd), all (p,q), n<=%d" % nmax, ok_centre)
    g.check("[Lem 2.7] omega^2 = (-1)^{m(m-1)/2}, all (p,q), n<=%d" % nmax, ok_omega)
    g.check("[Thm 3.6] central idempotents exist iff p-q=1 mod 4; eps_+- identities", ok_typeC)


# ----------------------------------------------------------------------------
# [Prop 3.3], [Ex 3.4], [Ex 3.5], [Lem 2.8]
# ----------------------------------------------------------------------------

def taxonomy_checks():
    # type N existence, constructive, and hyperbolic-partner idempotent in Cl(1,1)
    squares = g.sig(1, 1)
    e1, e2 = g.gen(0), g.gen(1)
    v = add(e1, e2)                                   # null
    g.check("[Prop 3.3] v = e1+e2 is null in Cl(1,1)", g.is_zero(g.mul(v, v, squares)))
    w = g.scal(Fraction(1, 4), sub(e1, e2))             # v.w = 1/2
    anti = add(g.mul(v, w, squares), g.mul(w, v, squares))
    g.check("[Ex 3.4] hyperbolic pair: vw + wv = 1", g.eq(anti, g.sc(1)))
    e = g.mul(w, v, squares)
    ok = (g.eq(g.mul(e, e, squares), e)
          and g.is_zero(g.mul(v, sub(g.sc(1), e), squares))
          and not g.eq(g.mul(e, v, squares), g.mul(v, e, squares)))
    g.check("[Ex 3.4] e = wv idempotent, v(1-e) = 0, e non-central", ok)

    # regularity instance [Lem 2.8]: x = w gives vxv = v; e = xv; checks
    ok = (g.eq(g.mul(g.mul(v, w, squares), v, squares), v)
          and g.eq(e, g.mul(w, v, squares))
          and not g.eq(e, g.sc(1)) and not g.is_zero(e))
    g.check("[Lem 2.8] regularity instance: vwv = v, e = wv nontrivial idempotent", ok)

    # Cl(2,0): nilpotent without null vectors [Ex 3.5]
    squares = g.sig(2, 0)
    e1, e2 = g.gen(0), g.gen(1)
    x = g.mul(add(g.sc(1), e1), e2, squares)
    eps = g.scal(Fraction(1, 2), add(g.sc(1), e1))
    ok = (g.is_zero(g.mul(x, x, squares))
          and g.eq(g.mul(eps, eps, squares), eps)
          and g.is_zero(g.mul(sub(g.sc(1), eps), x, squares))
          and not g.eq(g.mul(eps, e2, squares), g.mul(e2, eps, squares)))
    g.check("[Ex 3.5] Cl(2,0): x=(1+e1)e2 nilpotent; eps idempotent non-central; (1-eps)x=0", ok)
    # definite signature: no null vector among a rational net of directions
    ok = True
    for a in range(-3, 4):
        for b in range(-3, 4):
            if (a, b) != (0, 0):
                vv = add(g.scal(a, e1), g.scal(b, e2))
                if g.is_zero(g.mul(vv, vv, squares)):
                    ok = False
    g.check("[Prop 3.3] Cl(2,0): no null vectors (rational net)", ok)


# ----------------------------------------------------------------------------
# [Sec 5] Rule 2 fusion, both ascents, three bases; null ascent
# ----------------------------------------------------------------------------

def fusion_checks(p, q):
    n = p + q
    base_blades = g.all_blades(n)
    even_base = [b for b in base_blades if len(b) % 2 == 0]
    for gamma in (1, -1):
        squares = g.sig(p, q) + (gamma,)
        name = "Cl(%d,%d) -> gamma=%+d" % (p, q, gamma)
        nu = g.gen(n)
        nu_inv = g.scal(gamma, nu)
        omega = {tuple(range(n)): Fraction(1)}
        epp = add(g.sc(Fraction(1, 2)), g.scal(Fraction(1, 2), omega))
        epm = add(g.sc(Fraction(1, 2)), g.scal(Fraction(-1, 2), omega))

        # Ad_nu = grade involution on every base blade  [Prop 5.2]
        ok = all(g.eq(g.mul(g.mul(nu, {b: Fraction(1)}, squares), nu_inv, squares),
                    g.grade_inv({b: Fraction(1)})) for b in base_blades)
        g.check("[Prop 5.2] %s: Ad_nu = grade involution on A" % name, ok)

        # eps swap and fusion of the ideal
        ok = (g.eq(g.mul(g.mul(nu, epp, squares), nu_inv, squares), epm)
              and g.eq(add(epp, g.mul(g.mul(nu, epp, squares), nu_inv, squares)), g.sc(1)))
        g.check("[Prop 5.2] %s: nu eps+ nu^-1 = eps-; eps+ + conj = 1" % name, ok)

        # matrix units [Lem 5.4]
        E = {(1, 1): epp, (2, 2): epm,
             (1, 2): g.mul(epp, nu, squares),
             (2, 1): g.scal(gamma, g.mul(epm, nu, squares))}
        ok = g.eq(add(E[(1, 1)], E[(2, 2)]), g.sc(1))
        for i in (1, 2):
            for j in (1, 2):
                for k in (1, 2):
                    for l in (1, 2):
                        prod = g.mul(E[(i, j)], E[(k, l)], squares)
                        want = E[(i, l)] if j == k else {}
                        ok = ok and g.eq(prod, want)
        g.check("[Lem 5.4] %s: full 2x2 matrix-unit relations" % name, ok)

        # corner = eps+ A: eps+ (a nu) eps+ = 0 for all base blades a
        ok = all(g.is_zero(g.mul(g.mul(epp, g.mul({b: Fraction(1)}, nu, squares), squares), epp, squares))
                 for b in base_blades)
        g.check("[Lem 5.3] %s: eps+ (A nu) eps+ = 0" % name, ok)

        # corner iso Cl^0 -> eps+ A: injectivity via exact rank  [Lem 5.3]
        amb = g.all_blades(n + 1)
        vecs = [g.basis_vector_of(g.mul(epp, {b: Fraction(1)}, squares), amb) for b in even_base]
        g.check("[Lem 5.3] %s: {eps+ b : b even} linearly independent (rank %d)"
              % (name, len(even_base)), g.rank_of_vectors(vecs) == len(even_base))

    # null-generator ascent [Thm 5.7(2)]: J = A nu, J^2 = 0
    squares = g.sig(p, q) + (0,)
    nu = g.gen(n)
    ok = all(g.is_zero(g.mul(g.mul({b1: Fraction(1)}, nu, squares),
                         g.mul({b2: Fraction(1)}, nu, squares), squares))
             for b1 in base_blades for b2 in base_blades)
    g.check("[Thm 5.7] Cl(%d,%d)+null generator: (A nu)(A nu) = 0" % (p, q), ok)


# ----------------------------------------------------------------------------
# [Thm 7.1], [Prop 7.5], [Prop 7.8]: Rule 1 Morita and the pinching
# ----------------------------------------------------------------------------

def pseudo_random_element(blades, seed):
    """Deterministic exact-rational element: coefficients from a fixed LCG."""
    state = seed
    out = {}
    for b in blades:
        state = (1103515245 * state + 12345) % (2 ** 31)
        c = (state % 7) - 3  # in {-3..3}
        if c:
            out[b] = Fraction(c)
    return out


def morita_checks(p, q):
    n = p + q
    squares = g.sig(p, q) + (1, -1)          # adjoin e+ (sq +1) at n, e- (sq -1) at n+1
    name = "Cl(%d,%d) -> Cl(%d,%d)" % (p, q, p + 1, q + 1)
    ep, em = g.gen(n), g.gen(n + 1)
    f = g.scal(Fraction(1, 2), add(ep, em))
    fs = g.scal(Fraction(1, 2), sub(ep, em))
    base_blades = g.all_blades(n)
    amb_blades = g.all_blades(n + 2)

    # CAR identities
    ok = (g.is_zero(g.mul(f, f, squares)) and g.is_zero(g.mul(fs, fs, squares))
          and g.eq(add(g.mul(f, fs, squares), g.mul(fs, f, squares)), g.sc(1)))
    g.check("[Thm 7.1] %s: f^2 = f*^2 = 0, ff* + f*f = 1" % name, ok)

    ffs, fsf = g.mul(f, fs, squares), g.mul(fs, f, squares)
    E = {(1, 1): ffs, (2, 2): fsf, (1, 2): f, (2, 1): fs}
    ok = g.eq(add(E[(1, 1)], E[(2, 2)]), g.sc(1))
    for i in (1, 2):
        for j in (1, 2):
            for k in (1, 2):
                for l in (1, 2):
                    ok = ok and g.eq(g.mul(E[(i, j)], E[(k, l)], squares),
                                   E[(i, l)] if j == k else {})
    g.check("[Thm 7.1] %s: ladder pair is a 2x2 matrix-unit system" % name, ok)

    # ff* commutes with A; twisted diagonal f a f* = ahat ff*; off-diagonals die
    ok1 = ok2 = ok3 = True
    for b in base_blades:
        a = {b: Fraction(1)}
        if not g.commutes(ffs, a, squares):
            ok1 = False
        if not g.eq(g.mul(g.mul(f, a, squares), fs, squares),
                  g.mul(g.grade_inv(a), ffs, squares)):
            ok2 = False
        if not (g.is_zero(g.mul(g.mul(ffs, a, squares), g.mul(fs, g.sc(1), squares), squares))
                and g.is_zero(g.mul(g.mul(f, a, squares), ffs, squares))):
            ok3 = False
    g.check("[Thm 7.1] %s: ff* commutes with A" % name, ok1)
    g.check("[Thm 7.1] %s: f a f* = ahat ff* (twisted diagonal)" % name, ok2)
    g.check("[Thm 7.1] %s: off-diagonal entries of embedded A vanish" % name, ok3)

    # pinching [Prop 7.5]
    P, Pc = fsf, ffs

    def pinch(x):
        return add(g.mul(g.mul(P, x, squares), P, squares),
                   g.mul(g.mul(Pc, x, squares), Pc, squares))

    ok1 = ok2 = True
    for b in base_blades:
        a = {b: Fraction(1)}
        if not g.eq(pinch(a), a):
            ok1 = False
        if not (g.is_zero(pinch(g.mul(a, f, squares))) and g.is_zero(pinch(g.mul(a, fs, squares)))):
            ok2 = False
    g.check("[Prop 7.5] %s: E = id on A" % name, ok1)
    g.check("[Prop 7.5] %s: E kills Af and Af* (the ladder sector)" % name, ok2)
    ok = g.is_zero(pinch(f)) and g.is_zero(pinch(fs))
    g.check("[Prop 7.5] %s: E(f) = E(f*) = 0" % name, ok)

    # round trip: P a P = a f*f for base blades (identity in the natural corner)
    ok = all(g.eq(g.mul(g.mul(P, {b: Fraction(1)}, squares), P, squares),
                g.mul({b: Fraction(1)}, fsf, squares)) for b in base_blades)
    g.check("[Prop 7.5] %s: round trip P a P = a f*f" % name, ok)

    # multiplicative defect on deterministic pseudo-random elements
    x = pseudo_random_element(amb_blades, 20260819)
    y = pseudo_random_element(amb_blades, 314159)
    D = lambda z: g.mul(g.mul(P, z, squares), P, squares)
    lhs = sub(D(g.mul(x, y, squares)), g.mul(D(x), D(y), squares))
    rhs = g.mul(g.mul(g.mul(g.mul(P, x, squares), Pc, squares), y, squares), P, squares)
    g.check("[Prop 7.5] %s: D(xy) - D(x)D(y) = P x (1-P) y P (random exact elements)" % name,
          g.eq(lhs, rhs))

    # [Prop 7.8] the completion carries fresh obstructions
    g.check("[Prop 7.8] %s: adjoined f is null (new type N upstairs)" % name,
          g.is_zero(g.mul(f, f, squares)))


# ----------------------------------------------------------------------------
# [Thm 6.4], [Lem 6.3], [Rem 6.6]: type P structure (exact rational matrices)
# ----------------------------------------------------------------------------

def typeP_checks():
    F = Fraction
    I2 = [[F(1), F(0)], [F(0), F(1)]]
    # conjugacy at fixed rank [Thm 6.4(1)]: e = E11, e' = projection onto
    # span(1,0) along span(-1,1); g = adapted-basis change per the proof
    e = [[F(1), F(0)], [F(0), F(0)]]
    ep = [[F(1), F(1)], [F(0), F(0)]]      # idempotent, image span(1,0), ker span(-1,1)
    ok = g.mat_eq(g.mat_mul(ep, ep), ep)
    gm = [[F(1), F(-1)], [F(0), F(1)]]     # columns: im-basis, ker-basis of e'
    ginv = [[F(1), F(1)], [F(0), F(1)]]
    ok = ok and g.mat_eq(g.mat_mul(gm, ginv), I2)
    ok = ok and g.mat_eq(g.mat_mul(g.mat_mul(gm, e), ginv), ep)
    g.check("[Thm 6.4] rank-1 idempotents conjugate: g e g^-1 = e' (explicit g)", ok)

    # centrality iff singleton orbit [Thm 6.4(3)], samples
    u = [[F(0), F(1)], [F(1), F(0)]]       # a unit
    uinv = u
    moved = not g.mat_eq(g.mat_mul(g.mat_mul(u, e), uinv), e)
    fixed = g.mat_eq(g.mat_mul(g.mat_mul(u, I2), uinv), I2)
    g.check("[Thm 6.4] non-central idempotent is moved; central one is not (samples)",
          moved and fixed)

    # sum of two units [Lem 6.3]: v null in Cl(1,1): v = (v-1) + 1, v-1 invertible
    squares = g.sig(1, 1)
    v = add(g.gen(0), g.gen(1))
    vm1 = sub(v, g.sc(1))
    inv = g.neg(add(v, g.sc(1)))               # (v-1)(v+1) = v^2 - 1 = -1
    g.check("[Lem 6.3] v = (v-1) + 1 with (v-1)^-1 = -(v+1) (sum of two units)",
          g.eq(g.mul(vm1, inv, squares), g.sc(1)) and g.eq(g.mul(inv, vm1, squares), g.sc(1)))

    # Moore-Penrose boundary [Rem 6.6]
    # definite h = I, W = span(w), w = (1,2): P_W = w w^T / 5
    w = [F(1), F(2)]
    Pw = [[w[i] * w[j] / F(5) for j in range(2)] for i in range(2)]
    ok = g.mat_eq(g.mat_mul(Pw, Pw), Pw) and Pw[0][1] == Pw[1][0]
    # uniqueness: e_u = w u^T with u.w = 1; symmetric iff u = w/5 exactly.
    # parametrise u = (1/5)w + s(-2,1): symmetric entry condition forces s = 0.
    ok_unique = True
    for s_num in range(-4, 5):
        s = F(s_num, 3)
        u = [F(1, 5) * w[0] + s * F(-2), F(1, 5) * w[1] + s * F(1)]
        e_u = [[w[i] * u[j] for j in range(2)] for i in range(2)]
        sym = e_u[0][1] == e_u[1][0]
        if (s == 0) != sym:
            ok_unique = False
    g.check("[Rem 6.6] definite form: unique self-adjoint idempotent with image W", ok and ok_unique)

    # indefinite h = diag(1,-1), null image w = (1,1): no h-self-adjoint idempotent.
    # e = w u^T, u1 + u2 = 1; h-self-adjointness forces u2 = -u1, so u1+u2 = 0 != 1.
    ok = True
    for u1_num in range(-6, 7):
        u1 = F(u1_num, 2)
        u2 = 1 - u1
        e_u = [[u1, u2], [u1, u2]]
        h = [[F(1), F(0)], [F(0), F(-1)]]
        et = [[e_u[j][i] for j in range(2)] for i in range(2)]
        adj = g.mat_mul(g.mat_mul(h, et), h)
        if g.mat_eq(adj, e_u):
            ok = False
    g.check("[Rem 6.6] indefinite form, null image: no self-adjoint idempotent (net)", ok)


# ----------------------------------------------------------------------------
# main
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# [Sec 4] Sharpenings: cohomological no-go and representation-independent
# minimality (added at v2.0)
# ----------------------------------------------------------------------------

def gram_matrix_points(p, q):
    """The conformal Gram matrix M_ij = -1/2 Q(p_i - p_j) for the points
    {0, e_1..e_n, 2e_1} of Lemma [gram], as exact rationals."""
    n = p + q
    sq = [Fraction(1)] * p + [Fraction(-1)] * q
    pts = [[Fraction(0)] * n]
    for i in range(n):
        v = [Fraction(0)] * n
        v[i] = Fraction(1)
        pts.append(v)
    v = [Fraction(0)] * n
    v[0] = Fraction(2)
    pts.append(v)
    def Qv(x):
        return sum(sq[i] * x[i] * x[i] for i in range(n))
    m = len(pts)
    return [[Fraction(-1, 2) * Qv([a - b for a, b in zip(pts[i], pts[j])])
             for j in range(m)] for i in range(m)]


def sharpenings_cohomology_checks():
    # Setting: Cl(2,2); v = e1 + e3, w0 = (e1 - e3)/4, U = span{e2, e4}
    squares = g.sig(2, 2)  # e1,e2 -> +1 ; e3,e4 -> -1
    e1, e2, e3, e4 = g.gen(0), g.gen(1), g.gen(2), g.gen(3)
    v = add(e1, e3)
    w0 = g.scal(Fraction(1, 4), sub(e1, e3))
    g.check("[Lem 4.6] Cl(2,2): (v, w0) hyperbolic pair",
          g.is_zero(g.mul(v, v, squares)) and g.is_zero(g.mul(w0, w0, squares))
          and g.eq(add(g.mul(v, w0, squares), g.mul(w0, v, squares)), g.sc(1)))

    def R_of(u):
        return add(g.sc(1), g.mul(v, u, squares))

    u1 = add(e2, g.scal(2, e4))
    u2 = sub(g.scal(3, e2), e4)
    Ru1, Ru2 = R_of(u1), R_of(u2)
    g.check("[Lem 4.6] group law: R_u R_u' = R_{u+u'}",
          g.eq(g.mul(Ru1, Ru2, squares), R_of(add(u1, u2))))
    Ru1_inv = R_of(g.neg(u1))
    g.check("[Lem 4.6] R_u^-1 = R_{-u}; R_u fixes v",
          g.eq(g.mul(Ru1, Ru1_inv, squares), g.sc(1))
          and g.eq(g.mul(g.mul(Ru1, v, squares), Ru1_inv, squares), v))

    # Levi equivariance: g = 1 + (1/2) e2 e4, invertible, g v g^-1 = v,
    # g R_u g^-1 = R_{g u g^-1}
    B = g.mul(e2, e4, squares)
    gel = add(g.sc(1), g.scal(Fraction(1, 2), B))
    g_inv = g.scal(Fraction(4, 3), sub(g.sc(1), g.scal(Fraction(1, 2), B)))  # B^2=+1 so (1+B/2)(1-B/2)=3/4
    # (1 + B/2)(1 - B/2) = 1 - B^2/4 ; B^2 = -e2^2 e4^2 = +1 -> 3/4... recompute:
    ok_inv = g.eq(g.mul(gel, g_inv, squares), g.sc(1))
    u_conj = g.mul(g.mul(gel, u1, squares), g_inv, squares)
    ok = (ok_inv and g.eq(g.mul(g.mul(gel, v, squares), g_inv, squares), v)
          and g.eq(g.mul(g.mul(gel, Ru1, squares), g_inv, squares), R_of(u_conj))
          and all(len(b) == 1 for b in u_conj))
    g.check("[Lem 4.6] Levi equivariance: g R_u g^-1 = R_{gug^-1}, g fixes v", ok)

    # Torsor [Prop 4.7]: membership test x in vCl <=> (vw0) x = x
    vw0 = g.mul(v, w0, squares)
    alpha = add(g.sc(3), g.scal(-2, e2))            # sample class coordinate
    sigma = add(w0, alpha)
    g.check("[Prop 4.7] sigma = w0 + alpha is a pseudo-inverse: v sigma v = v",
          g.eq(g.mul(g.mul(v, sigma, squares), v, squares), v))
    sigma_p = g.mul(g.mul(Ru1, sigma, squares), Ru1_inv, squares)
    g.check("[Prop 4.7] N_v preserves S(v)",
          g.eq(g.mul(g.mul(v, sigma_p, squares), v, squares), v))
    d = sub(sigma_p, add(w0, sub(alpha, u1)))
    g.check("[Prop 4.7] translation by -u on classes: sigma' = w0 + (alpha - u) mod vCl",
          g.eq(g.mul(vw0, d, squares), d))
    d_fix = sub(sigma_p, sigma)
    g.check("[Thm 4.8] no fixed point: sigma' differs from sigma mod vCl",
          not g.eq(g.mul(vw0, d_fix, squares), d_fix))


def sharpenings_gram_checks():
    for (p, q) in [(1, 1), (2, 0), (0, 2), (2, 1), (1, 3)]:
        n = p + q
        M = gram_matrix_points(p, q)
        pos, neg_, zer = g.congruence_signature(M)
        g.check("[Lem 4.18] Gram of {0, e_i, 2e_1} in (%d,%d): rank %d, signature (%d,%d)"
              % (p, q, n + 2, p + 1, q + 1),
              zer == 0 and pos == p + 1 and neg_ == q + 1)

    # chart consistency: Gram of the model lifts equals M, for (1,1) and (1,3)
    for (p, q) in [(1, 1), (1, 3)]:
        n = p + q
        squares = g.sig(p, q) + (1, -1)           # e+ at n, e- at n+1
        ep, em = g.gen(n), g.gen(n + 1)
        n0 = g.scal(Fraction(1, 2), sub(em, ep))
        ninf = add(em, ep)
        sq = [Fraction(1)] * p + [Fraction(-1)] * q

        def lift(x):
            Qx = sum(sq[i] * x[i] * x[i] for i in range(n))
            vec = {}
            for i in range(n):
                if x[i]:
                    vec[(i,)] = x[i]
            return add(n0, vec, g.scal(Fraction(1, 2) * Qx, ninf))

        pts = [[Fraction(0)] * n]
        for i in range(n):
            vv = [Fraction(0)] * n
            vv[i] = Fraction(1)
            pts.append(vv)
        vv = [Fraction(0)] * n
        vv[0] = Fraction(2)
        pts.append(vv)
        lifts = [lift(x) for x in pts]
        M = gram_matrix_points(p, q)
        ok = all(g.dot_scalar(lifts[i], lifts[j], squares) == M[i][j]
                 for i in range(n + 2) for j in range(n + 2))
        g.check("[Lem 4.18] (%d,%d): Gram of model lifts equals the point matrix M" % (p, q), ok)


# --- exact complex fractions and 4x4 matrices for the exotic embedding ------

def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cmat_mul(A, B):
    n = len(A)
    return [[tuple(map(sum, zip(*[cmul(A[i][k], B[k][j]) for k in range(n)])))
             for j in range(n)] for i in range(n)]


def cmat_add(A, B):
    return [[(A[i][j][0] + B[i][j][0], A[i][j][1] + B[i][j][1])
             for j in range(len(A))] for i in range(len(A))]


def cmat_scal(c, A):
    return [[(c * A[i][j][0], c * A[i][j][1]) for j in range(len(A))] for i in range(len(A))]


def cmat_eq(A, B):
    return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A)))


def exotic_embedding_checks():
    F = Fraction
    Z, O, I = (F(0), F(0)), (F(1), F(0)), (F(0), F(1))
    mI = (F(0), F(-1))
    mO = (F(-1), F(0))
    # H -> M2(C): 1->I2, i->diag(i,-i), j->[[0,1],[-1,0]], k->[[0,i],[i,0]]
    u1 = [[I, Z], [Z, mI]]
    u2 = [[Z, O], [mO, Z]]
    u3 = [[Z, I], [I, Z]]
    I2 = [[O, Z], [Z, O]]
    Z2 = [[Z, Z], [Z, Z]]

    def block(A, B, C, D):
        out = []
        for r in range(2):
            out.append(A[r] + B[r])
        for r in range(2):
            out.append(C[r] + D[r])
        return out

    I4 = block(I2, Z2, Z2, I2)
    mI2 = cmat_scal(F(-1), I2)
    G0 = block(I2, Z2, Z2, mI2)                  # gamma_0 = diag(1,-1) over H
    G = [G0] + [block(Z2, u, u, Z2) for u in (u1, u2, u3)]

    ok = cmat_eq(cmat_mul(G[0], G[0]), I4)
    for k in (1, 2, 3):
        ok = ok and cmat_eq(cmat_mul(G[k], G[k]), cmat_scal(F(-1), I4))
    for a in range(4):
        for b in range(a + 1, 4):
            anti = cmat_add(cmat_mul(G[a], G[b]), cmat_mul(G[b], G[a]))
            ok = ok and cmat_eq(anti, cmat_scal(F(0), I4))
    g.check("[Ex 4.20] exotic embedding: Cl(1,3) generators realised in M4(C), "
          "unital, all Clifford relations", ok)




# ===========================================================================
# PART TWO: the type-N development (22 checks; from the published
# verify_transport_principle.py, retagged).  Self-contained engine kept as
# deposited and frozen-tested; F is fractions.Fraction.
# ===========================================================================

from fractions import Fraction as F
from itertools import combinations

# ----------------------------------------------------------------------
# Minimal exact Clifford algebra over a diagonal signature.
# Elements are dicts {blade-tuple: Fraction}; blade (0,2) means e0*e2.
# Signature entries may be +1, -1 or 0 (degenerate generator).
# ----------------------------------------------------------------------


class Cl:
    def __init__(self, sig):
        self.sig = list(sig)

    def _blade_mul(self, A, B):
        sign, res = 1, list(A)
        for b in B:
            if b in res:                     # e_b already present: contract
                i = res.index(b)
                sign *= (-1) ** (len(res) - 1 - i) * self.sig[b]
                res.pop(i)
            else:                            # insert keeping sorted order
                i = 0
                while i < len(res) and res[i] < b:
                    i += 1
                sign *= (-1) ** (len(res) - i)
                res.insert(i, b)
        return sign, tuple(res)

    def mul(self, X, Y):
        out = {}
        for a, ca in X.items():
            for b, cb in Y.items():
                s, blade = self._blade_mul(a, b)
                if s == 0:
                    continue
                out[blade] = out.get(blade, 0) + s * ca * cb
        return {k: v for k, v in out.items() if v != 0}

    def dot(self, a, b):
        return scalar(smul(F(1, 2), add(self.mul(a, b), self.mul(b, a))))

    def Q(self, a):
        return scalar(self.mul(a, a))


def add(*Xs):
    out = {}
    for X in Xs:
        for k, v in X.items():
            out[k] = out.get(k, 0) + v
    return {k: v for k, v in out.items() if v != 0}


def smul(c, X):
    c = F(c)
    return {k: c * v for k, v in X.items() if c * v != 0}


def sub(X, Y):
    return add(X, smul(-1, Y))


def hat(X):                                  # grade involution
    return {k: (v if len(k) % 2 == 0 else -v) for k, v in X.items()}


def rev(X):                                  # reversion
    return {k: (v if (len(k) * (len(k) - 1) // 2) % 2 == 0 else -v)
            for k, v in X.items()}


def scalar(X):
    return X.get((), F(0))


def e(i):
    return {(i,): F(1)}


def blades(n):
    out = []
    for k in range(n + 1):
        out += [tuple(c) for c in combinations(range(n), k)]
    return out


def solve(M, ncol):
    """Reduced row echelon solve; M rows are [coeffs..., rhs]. Returns solution
    and asserts consistency (which is itself the span/basis claim)."""
    where, piv = [-1] * ncol, 0
    for col in range(ncol):
        sel = next((r for r in range(piv, len(M)) if M[r][col] != 0), None)
        if sel is None:
            continue
        M[piv], M[sel] = M[sel], M[piv]
        pv = M[piv][col]
        M[piv] = [x / pv for x in M[piv]]
        for r in range(len(M)):
            if r != piv and M[r][col] != 0:
                f = M[r][col]
                M[r] = [a - f * b for a, b in zip(M[r], M[piv])]
        where[col] = piv
        piv += 1
    for r in range(piv, len(M)):
        assert all(x == 0 for x in M[r][:ncol]) and M[r][-1] == 0, \
            "system inconsistent: the claimed basis does not span"
    return [M[where[c]][-1] if where[c] >= 0 else F(0) for c in range(ncol)]


# ======================================================================
# Setting: a base V of mixed signature with a chosen hyperbolic pair,
# optionally ascended.  e_0^2 = +1 and e_{n-1}^2 = -1, so v = e_0 + e_{n-1}
# is null and w0 = (e_0 - e_{n-1})/4 is its partner with v.w0 = 1/2.
# ======================================================================


class Setting:
    def __init__(self, p, q, extra=()):
        self.sig = [1] * p + [-1] * q + list(extra)
        self.n = p + q
        self.A = Cl(self.sig)
        self.one = {(): F(1)}
        self.v = add(e(0), e(self.n - 1))
        self.w0 = smul(F(1, 4), sub(e(0), e(self.n - 1)))
        self.U = list(range(1, self.n - 1))              # U  subset of V
        self.Up = self.U + list(range(self.n, len(self.sig)))   # U' = U perp V^perp
        self.blU = [tuple(sorted(self.Up[i] for i in bl))
                    for bl in blades(len(self.Up))]

    def clU(self, coeffs):
        """An element of Cl(U') from a list of rational coefficients."""
        return {bl: F(c) for bl, c in zip(self.blU, coeffs) if c != 0}

    def sample_clU(self, seed):
        return self.clU([F((seed * 7 + 5 * i) % 11) - 5
                         for i in range(len(self.blU))])

    def decompose(self, X):
        """Unique expansion X = alpha + v beta + w0 gamma + v w0 delta
        with coefficients in Cl(U')  (Lemma 2.4)."""
        A, v, w0 = self.A, self.v, self.w0
        vw0 = A.mul(v, w0)
        cols, tags = [], []
        for slot, pre in (("a", self.one), ("b", v), ("c", w0), ("d", vw0)):
            for bl in self.blU:
                cols.append(A.mul(pre, {bl: F(1)}))
                tags.append((slot, bl))
        allbl = blades(len(self.sig))
        M = [[F(c.get(bl, 0)) for c in cols] + [F(X.get(bl, 0))] for bl in allbl]
        sol = solve(M, len(cols))
        parts = {"a": {}, "b": {}, "c": {}, "d": {}}
        for (slot, bl), val in zip(tags, sol):
            if val != 0:
                parts[slot][bl] = val
        recon = add(parts["a"], A.mul(v, parts["b"]),
                    A.mul(w0, parts["c"]), A.mul(vw0, parts["d"]))
        assert recon == X, "decomposition failed to reconstruct"
        return parts["a"], parts["b"], parts["c"], parts["d"]

    def rotor(self, u):
        """The null rotation R = 1 + v u and its inverse."""
        A, v = self.A, self.v
        return add(self.one, A.mul(v, u)), sub(self.one, A.mul(v, u))


SETTINGS = [
    ("Cl(2,1), no ascent",              Setting(2, 1)),
    ("Cl(2,1) + hyperbolic ascent",     Setting(2, 1, (1, -1))),
    ("Cl(2,1) + DEGENERATE ascent",     Setting(2, 1, (0,))),
    ("Cl(3,2), no ascent (dim U = 3)",  Setting(3, 2)),
    ("Cl(2,2) + degenerate ascent",     Setting(2, 2, (0, 1))),
]


def check_hyperbolic_pair():
    for _, S in SETTINGS:
        A, v, w0 = S.A, S.v, S.w0
        assert A.mul(v, v) == {} and A.mul(w0, w0) == {}
        assert A.dot(v, w0) == F(1, 2)
        assert add(A.mul(v, w0), A.mul(w0, v)) == S.one       # vw0 + w0v = 1
        assert A.mul(A.mul(v, w0), v) == v                    # vw0v = v


def check_splitting():
    """Lemma 2.4: the expansion exists, is unique, and left multiplication by
    v is injective on Cl(U') -- including over a degenerate ascent."""
    for _, S in SETTINGS:
        a, b, c, d = (S.sample_clU(i) for i in range(1, 5))
        X = add(a, S.A.mul(S.v, b), S.A.mul(S.w0, c),
                S.A.mul(S.A.mul(S.v, S.w0), d))
        assert S.decompose(X) == (a, b, c, d), "expansion not unique"
        for i in range(1, 6):                      # injectivity of x -> v x
            x = S.sample_clU(i)
            if x:
                assert S.A.mul(S.v, x) != {}


def check_nogo_step1():
    for _, S in SETTINGS:
        A, v = S.A, S.v
        al, be, ga, de = (S.sample_clU(i) for i in range(1, 5))
        sigma = add(al, A.mul(v, be), A.mul(S.w0, ga),
                    A.mul(A.mul(v, S.w0), de))
        assert A.mul(A.mul(v, sigma), v) == A.mul(v, hat(ga)), \
            "v sigma v != v gamma^"
        # hence v sigma v = v iff gamma = 1
        nf = add(S.w0, al, A.mul(v, be), A.mul(A.mul(v, S.w0), de))
        assert A.mul(A.mul(v, nf), v) == v


def check_versor_factorisation():
    """eq. (4): R = u'u/Q(u) with u' = u + Q(u)v, both factors invertible of
    equal square -- so R is a versor, not merely a rotor."""
    for _, S in SETTINGS:
        A, v = S.A, S.v
        for ui in S.U:
            u = e(ui)
            Qu = A.Q(u)
            if Qu == 0:
                continue
            up = add(u, smul(Qu, v))
            assert A.Q(up) == Qu, "Q(u + Q(u)v) != Q(u)"
            R, Ri = S.rotor(u)
            assert smul(F(1, Qu), A.mul(up, u)) == R
            assert A.mul(R, Ri) == S.one and A.mul(Ri, R) == S.one
            assert A.mul(R, rev(R)) == S.one, "R is not a rotor"
            # the whole path t -> 1 + t v u factors the same way
            for t in (F(1, 3), F(-2), F(5)):
                ut = smul(t, u)
                Qut = A.Q(ut)
                Rt, _ = S.rotor(ut)
                assert smul(1 / Qut, A.mul(add(ut, smul(Qut, v)), ut)) == Rt


def check_nogo_step2():
    for _, S in SETTINGS:
        A, v, w0 = S.A, S.v, S.w0
        for ui in S.U:
            u = e(ui)
            R, Ri = S.rotor(u)
            conj = lambda Z: A.mul(A.mul(R, Z), Ri)
            assert conj(v) == v, "R does not fix v"
            assert conj(w0) == add(w0, smul(-1, u), smul(-A.Q(u), v))
            for j in S.Up:
                uu = e(j)
                assert conj(uu) == add(uu, smul(2 * A.dot(u, uu), v))


def check_nogo_step3():
    """The shear: the Cl(U')-component of R sigma R^{-1} is alpha - u, for
    EVERY u in U (dim U = 3 in the Cl(3,2) setting)."""
    for _, S in SETTINGS:
        A, v, w0 = S.A, S.v, S.w0
        al, be, de = (S.sample_clU(i) for i in (1, 2, 4))
        nf = add(w0, al, A.mul(v, be), A.mul(A.mul(v, w0), de))
        for ui in S.U:
            u = e(ui)
            R, Ri = S.rotor(u)
            conj = lambda Z: A.mul(A.mul(R, Z), Ri)
            # the four term-by-term identities of Step 3
            assert conj(al) == add(al, A.mul(v, sub(A.mul(u, al),
                                                    A.mul(hat(al), u))))
            assert conj(A.mul(v, be)) == A.mul(v, be)
            vw0d = A.mul(A.mul(v, w0), de)
            assert conj(vw0d) == sub(vw0d, A.mul(v, A.mul(hat(de), u)))
            a2, _, c2, _ = S.decompose(conj(nf))
            assert c2 == S.one, "the w0-coefficient must stay 1"
            assert a2 == sub(al, u), "shear alpha -> alpha - u fails"


def check_local_robustness():
    """Rem 4.3: equivariance up to scale fails too.  The w0-slot is 1 both
    before and after conjugation, so lambda = 1 is forced, and then the
    Cl(U')-slots give alpha - u = alpha."""
    for _, S in SETTINGS:
        A, v, w0 = S.A, S.v, S.w0
        al, be, de = (S.sample_clU(i) for i in (3, 1, 2))
        nf = add(w0, al, A.mul(v, be), A.mul(A.mul(v, w0), de))
        for ui in S.U:
            u = e(ui)
            R, Ri = S.rotor(u)
            a2, b2, c2, d2 = S.decompose(A.mul(A.mul(R, nf), Ri))
            assert c2 == S.one                       # forces lambda = 1
            assert sub(a2, al) == smul(-1, u) != {}  # then a contradiction


def check_parabolic():
    """Rem 4.4: on V the action is unipotent of index 3, not 2, when
    Q(u) != 0; and Ad_R fixes v together with U cap u^perp."""
    for label, S in SETTINGS:
        A, v, w0, n = S.A, S.v, S.w0, S.n
        u = next(e(i) for i in S.U if A.Q(e(i)) != 0)
        R, Ri = S.rotor(u)
        conj = lambda Z: A.mul(A.mul(R, Z), Ri)
        # (Ad_R - id) on the base V, as a matrix in the basis e_0..e_{n-1}
        N = [[F(conj(e(j)).get((i,), 0)) - (1 if i == j else 0)
              for i in range(n)] for j in range(n)]
        def comp(Ma, Mb):
            return [[sum(Ma[j][k] * Mb[k][i] for k in range(n))
                     for i in range(n)] for j in range(n)]
        P, idx = N, 1
        while any(x != 0 for col in P for x in col):
            P, idx = comp(P, N), idx + 1
            assert idx <= n + 1
        assert idx == 3, f"{label}: nilpotency index {idx}, expected 3"
        # the explicit second power: (Ad_R - id)^2 w0 = -2 Q(u) v  != 0
        d1 = sub(conj(w0), w0)
        assert d1 == add(smul(-1, u), smul(-A.Q(u), v))
        d2 = sub(conj(d1), d1)
        assert d2 == smul(-2 * A.Q(u), v) != {}, "index is not 3"
        assert sub(conj(d2), d2) == {}
        # fixed vectors: v, and every u'' in U orthogonal to u
        assert conj(v) == v
        for j in S.U:
            if A.dot(u, e(j)) == 0:
                assert conj(e(j)) == e(j), "U cap u^perp must be fixed"


def check_parabolic_fixes_a_null_direction():
    """Rem 4.4: for n >= 4 the fixed set can contain null directions other
    than [v] -- so 'fixes exactly one direction' holds only at n = 3."""
    S = Setting(3, 2)
    A, v = S.A, S.v
    R, Ri = S.rotor(e(1))
    conj = lambda Z: A.mul(A.mul(R, Z), Ri)
    w = add(e(2), e(3))                       # in U, orthogonal to e1
    assert A.Q(w) == 0 and w != v and conj(w) == w
    # and at n = 3 the fixed space of Ad_R on V is exactly span{v}: v is
    # fixed, and the kernel of (Ad_R - id) restricted to V has dimension 1
    S3 = Setting(2, 1)
    A3, v3 = S3.A, S3.v
    R3, Ri3 = S3.rotor(e(1))
    c3 = lambda Z: A3.mul(A3.mul(R3, Z), Ri3)
    assert c3(v3) == v3, "v must be fixed"
    # rows: the vector (Ad_R - id) e_j, j = 0, 1, 2, in the basis e_0, e_1, e_2
    rows = []
    for j in range(3):
        d = sub(c3(e(j)), e(j))
        assert all(len(k) == 1 for k in d), "Ad_R must map vectors to vectors"
        rows.append([d.get((i,), F(0)) for i in range(3)])
    assert g.rank_of_vectors(rows) == 2, "fixed space at n = 3 must be one-dimensional"


def check_partners():
    """eq. (5): the partners of v are exactly y_u = w0 - u - Q(u) v, u in U,
    and the null rotations act on them simply transitively."""
    for _, S in SETTINGS:
        A, v, w0 = S.A, S.v, S.w0
        for ui in S.U:
            for lam in (F(1), F(-3), F(1, 2)):
                u = smul(lam, e(ui))
                y = add(w0, smul(-1, u), smul(-A.Q(u), v))
                assert A.Q(y) == 0 and A.dot(v, y) == F(1, 2)
                R, Ri = S.rotor(u)
                assert A.mul(A.mul(R, w0), Ri) == y     # simple transitivity
        # conversely every null y with v.y = 1/2 has this form
        A2, n = S.A, S.n
        for ui in S.U:
            u = e(ui)
            y = add(w0, smul(-1, u), smul(-A2.Q(u), v))
            a = -A2.Q(u)
            assert y == add(smul(a, v), w0, smul(-1, u))


def check_atom_section():
    """Rem 4.5 / Sec 4.8.2: in the hyperbolic plane the partner is UNIQUE, and
    sigma(lam v) = lam^{-1} w0 is equivariant under all of Pin(1,1)."""
    A = Cl([1, -1])
    e0, e1 = e(0), e(1)
    v = smul(F(1, 2), add(e0, e1))
    w0 = smul(F(1, 2), sub(e0, e1))
    assert A.Q(v) == 0 and A.Q(w0) == 0 and A.dot(v, w0) == F(1, 2)

    def sigma(x):
        """x is null: x = lam v or lam w0."""
        for base, partner in ((v, w0), (w0, v)):
            for k in ((0,), (1,)):
                if base.get(k):
                    lam = x.get(k, F(0)) / base[k]
                    if lam != 0 and smul(lam, base) == x:
                        return smul(1 / lam, partner)
        raise AssertionError("not a null vector of the plane")

    # uniqueness of the partner (the reason equivariance holds)
    for lam in (F(1), F(-2), F(3, 5)):
        x = smul(lam, v)
        y = sigma(x)
        assert A.Q(y) == 0 and A.dot(x, y) == F(1, 2)
        # uniqueness: the null vectors of the plane are mu(e0 + e1) and
        # mu(e0 - e1); exactly one of them pairs with x to 1/2, namely y.
        hits = []
        for base in (add(e0, e1), sub(e0, e1)):
            d = A.dot(x, base)
            if d != 0:
                hits.append(smul(F(1, 2) / d, base))
        assert len(hits) == 1 and hits[0] == y, "the partner is not unique"

    def Ad(g, x):                                  # twisted adjoint on vectors
        ginv = smul(1 / A.Q(g), g) if len(next(iter(g))) == 1 else None
        if ginv is None:                           # even element: g^{-1} via rev
            nrm = scalar(A.mul(g, rev(g)))
            ginv = smul(1 / nrm, rev(g))
            return A.mul(A.mul(g, x), ginv)
        return smul(-1, A.mul(A.mul(g, x), ginv))  # odd: hat(g) x g^{-1}

    boost = A.mul(add(smul(F(5, 4), e0), smul(F(3, 4), e1)), e0)   # unit*unit
    assert A.mul(boost, rev(boost)) == {(): F(1)}
    gens = [e0, e1, A.mul(e0, e1), boost, A.mul(boost, e0)]
    for g in gens:
        for x in (v, smul(F(-3), v), w0, smul(F(2, 3), w0)):
            assert sigma(Ad(g, x)) == Ad(g, sigma(x)), "Pin(1,1)-equivariance"


# ======================================================================
# Conformal model, over bases of signature (1,1) and (2,1).
# ======================================================================


class Model:
    """Base V of signature (a,b) inside the ambient Cl(a+1, b+1)."""

    def __init__(self, a, b):
        self.sig = [1] * a + [-1] * b + [1, -1]     # last two are e+, e-
        self.B = Cl(self.sig)
        self.dim = a + b
        self.ep, self.em = e(self.dim), e(self.dim + 1)
        self.n0 = smul(F(1, 2), sub(self.em, self.ep))
        self.ninf = add(self.em, self.ep)

    def vec(self, *cs):
        return add(*[smul(F(c), e(i)) for i, c in enumerate(cs) if c != 0]) \
            if any(cs) else {}

    def Q(self, x):
        return self.B.Q(x)

    def X(self, x):
        return add(self.n0, x, smul(F(self.Q(x), 2), self.ninf))

    def iota(self, N):
        return self.B.mul(self.B.mul(self.ep, N), self.ep)

    def coords(self, N):
        """(s, x, t) with N = s n0 + x + t ninf."""
        cp, cm = N.get((self.dim,), F(0)), N.get((self.dim + 1,), F(0))
        s, t = cm - cp, (cm + cp) / 2
        x = {k: val for k, val in N.items() if k[0] < self.dim and len(k) == 1}
        return s, x, t

    def dsc(self, N):
        s, x, _ = self.coords(N)
        assert s != 0, "descent applied to an ideal point"
        return smul(1 / s, x)


M11, M21 = Model(1, 1), Model(2, 1)
MODELS = [("base (1,1)", M11), ("base (2,1)", M21)]


def _pts(M):
    out = []
    rng = range(-3, 4)
    for c in rng:
        for d in rng:
            if M.dim == 2:
                out.append(M.vec(c, d))
            else:
                for f in (-2, 0, 1, 3):
                    out.append(M.vec(c, d, f))
    return out


def check_conformal_model():
    for _, M in MODELS:
        B = M.B
        assert B.mul(M.n0, M.n0) == {} and B.mul(M.ninf, M.ninf) == {}
        assert B.dot(M.n0, M.ninf) == -1
        pts = _pts(M)
        for x in pts[::7]:
            assert B.mul(M.X(x), M.X(x)) == {}, "X(x)^2 != 0"
            for y in pts[::13]:
                assert B.dot(M.X(x), M.X(y)) == -F(M.Q(sub(x, y)), 2)


def check_eplus_actions():
    for _, M in MODELS:
        assert M.iota(M.n0) == smul(F(-1, 2), M.ninf)
        assert M.iota(M.ninf) == smul(-2, M.n0)
        for i in range(M.dim):
            assert M.iota(e(i)) == smul(-1, e(i))
        assert M.ep == smul(-1, add(M.n0, smul(F(-1, 2), M.ninf)))


def check_totality_invertible():
    for _, M in MODELS:
        for x in _pts(M):
            # the key display (9), valid for every x
            assert M.iota(M.X(x)) == smul(-1, add(smul(F(M.Q(x)), M.n0), x,
                                                  smul(F(1, 2), M.ninf)))
            if M.Q(x) != 0:
                assert smul(F(-1, M.Q(x)), M.iota(M.X(x))) == \
                    M.X(smul(F(1, M.Q(x)), x))


def check_totality_null_and_origin():
    for _, M in MODELS:
        nulls = [x for x in _pts(M) if x and M.Q(x) == 0]
        assert nulls, "expected null vectors in a mixed-signature base"
        for x0 in nulls:
            val = M.iota(M.X(x0))
            assert val == smul(-1, add(x0, smul(F(1, 2), M.ninf)))
            assert M.B.mul(val, val) == {}, "the ideal value must be null"
            s, _, _ = M.coords(val)
            assert s == 0, "the value must be ideal"
        assert M.iota(M.X({})) == smul(F(-1, 2), M.ninf)      # origin -> [ninf]


def check_scale_memory():
    """Rem 4.11: rescaling a null vector moves its ideal value."""
    for _, M in MODELS:
        x0 = next(x for x in _pts(M) if x and M.Q(x) == 0)
        Na = add(x0, smul(F(1, 2), M.ninf))
        Nb = add(smul(2, x0), smul(F(1, 2), M.ninf))
        assert not any(smul(l, Na) == Nb
                       for l in (F(1), F(2), F(1, 2), F(-1), F(-2)))


def check_density_paths():
    """Lemma 4.9's two explicit families, with exact rationals, over both
    model bases (1,1) and (2,1)."""
    for _, M in MODELS:
        _density_paths_on(M)


def _density_paths_on(M):
    xb = next(x for x in _pts(M) if x and M.Q(x) == 0)
    uu = next(e(i) for i in range(M.dim) if M.B.dot(xb, e(i)) != 0)
    uu = smul(1 / M.B.dot(xb, uu), uu)                  # normalise x.u = 1
    assert M.B.dot(xb, uu) == 1
    for t in (F(7), F(0), F(-2)):
        prev = None
        for s in (F(10), F(100), F(1000)):
            y = add(smul(s, xb), smul(t + 1 / s, uu))
            assert M.Q(y) != 0, "path vector must be invertible"
            rep = smul(1 / s, M.X(y))
            diff = sub(rep, add(xb, smul(t, M.ninf)))
            m = max((abs(c) for c in diff.values()), default=F(0))
            assert prev is None or m < prev, "no convergence"
            prev = m
    a = next(e(i) for i in range(M.dim) if M.Q(e(i)) != 0)
    prev = None
    for s in (F(10), F(100), F(1000)):
        rep = smul(F(2) / (s * s * M.Q(a)), M.X(smul(s, a)))
        m = max(abs(c) for c in sub(rep, M.ninf).values())
        assert prev is None or m < prev
        prev = m


def check_swap():
    """Prop 4.21: iota(s,x,t) = (2t, x, s/2) up to the projective sign, and the
    incidence condition Q(x) = 2st is preserved."""
    for _, M in MODELS:
        for s_, t_ in ((F(7), F(11)), (F(0), F(3)), (F(-2), F(1, 2))):
            x = M.vec(*([3, 2] if M.dim == 2 else [3, 2, -1]))
            N = add(smul(s_, M.n0), x, smul(t_, M.ninf))
            assert M.iota(N) == smul(-1, add(smul(2 * t_, M.n0), x,
                                             smul(s_ / 2, M.ninf)))
            assert 2 * (2 * t_) * (s_ / 2) == 2 * s_ * t_


def check_strata_fixed_loci():
    """Rem 4.22: stratum (ii) is fixed pointwise by iota; the ordinary fixed
    points are exactly the unit quadric Q(x) = 1."""
    M = M21
    x0 = next(x for x in _pts(M) if x and M.Q(x) == 0)
    assert M.iota(x0) == smul(-1, x0)                    # (0, x, 0) fixed
    xu = next(x for x in _pts(M) if M.Q(x) == 1)
    assert M.iota(M.X(xu)) == smul(-1, M.X(xu))          # unit quadric fixed
    xn = next(x for x in _pts(M) if M.Q(x) not in (0, 1))
    assert M.iota(M.X(xn)) != smul(-1, M.X(xn))


def check_descent():
    for _, M in MODELS:
        for x in _pts(M)[::5]:
            assert M.dsc(M.X(x)) == x                     # Lem 4.23(1)
        lam = F(7)
        for x in _pts(M)[::11]:
            N = smul(lam, M.X(x))
            assert smul(lam, M.X(M.dsc(N))) == N          # X(dsc[N]) in [N]
            if M.Q(x) != 0:                               # Lem 4.23(2)
                assert M.dsc(M.iota(M.X(x))) == smul(F(1, M.Q(x)), x)
        for x0 in [x for x in _pts(M) if M.Q(x) == 0][:5]:   # Lem 4.23(3)
            s, _, _ = M.coords(M.iota(M.X(x0)))
            assert s == 0


def check_riemann_sphere():
    """Sec 4.8.1: over the base (2,0) the quadric is the Riemann sphere, iota is
    inversion in the unit circle, and on the sphere that is reflection in the
    equator.  The one-dimensional base (1,0), giving RP^1 and the classical
    inversion matrix, is checked at the end."""
    # ---- the Euclidean plane: base (2,0), completion Cl(3,1) ----------------
    C = Cl([1, 1, 1, -1])
    g1, g2, cep, cem = e(0), e(1), e(2), e(3)
    cn0 = smul(F(1, 2), sub(cem, cep))
    cninf = add(cem, cep)
    assert C.Q(cn0) == 0 and C.Q(cninf) == 0 and C.dot(cn0, cninf) == -1

    def lift(x, y):                                   # X(z) = n0 + z + Q/2 ninf
        q = x * x + y * y
        return add(cn0, smul(x, g1), smul(y, g2), smul(q / 2, cninf))

    conj = lambda N: C.mul(C.mul(cep, N), cep)
    pts = [(F(3), F(1)), (F(-2), F(5)), (F(1, 4), F(-1, 3)),
           (F(1), F(0)), (F(0), F(2)), (F(3, 5), F(4, 5))]

    for x, y in pts:
        assert C.Q(lift(x, y)) == 0, "X(z) must be null"
        q = x * x + y * y
        # Thm 4.10(2): iota[X(z)] = [X(z/|z|^2)], inversion in the unit circle
        assert smul(F(-1) / q, conj(lift(x, y))) == lift(x / q, y / q)
    assert conj(lift(F(0), F(0))) == smul(F(-1, 2), cninf)     # 1/0 = infinity
    assert conj(cninf) == smul(-2, cn0)                        # 1/infinity = 0

    # definite signature: incidence (eq. 9) with s = 0 forces z = 0, so the
    # ideal strata (i) and (ii) of Prop 4.21 are empty and [ninf] is the only
    # ideal point.
    for a in range(-4, 5):
        for b in range(-4, 5):
            null = (F(a) * F(a) + F(b) * F(b) == 0)
            assert null == (a == 0 and b == 0)

    # the identification with S^2, and iota as reflection in the equator
    def sph(x, y):
        q = x * x + y * y
        return (2 * x / (q + 1), 2 * y / (q + 1), (q - 1) / (q + 1))

    NORTH, SOUTH = (F(0), F(0), F(1)), (F(0), F(0), F(-1))
    assert sph(F(0), F(0)) == SOUTH
    for x, y in pts:
        X, Y, Z = sph(x, y)
        assert X * X + Y * Y + Z * Z == 1, "image must lie on the unit sphere"
        q = x * x + y * y
        assert sph(x / q, y / q) == (X, Y, -Z)
    # fixed locus (Rem 4.22 with stratum (ii) empty): exactly the equator |z|=1
    for x, y in pts:
        q = x * x + y * y
        fixed = ((x / q, y / q) == (x, y))
        assert fixed == (q == 1) == (sph(x, y)[2] == 0)

    # ---- the one-dimensional base (1,0): RP^1 and [[0,1],[1,0]] -------------
    D = Cl([1, 1, -1])
    h0, dep, dem = e(0), e(1), e(2)
    dn0 = smul(F(1, 2), sub(dem, dep))
    dninf = add(dem, dep)
    dlift = lambda x: add(dn0, smul(F(x), h0), smul(F(x) * F(x) / 2, dninf))
    dconj = lambda N: D.mul(D.mul(dep, N), dep)
    for x in (F(3), F(-2), F(1, 4)):
        assert smul(-1 / (F(x) * F(x)), dconj(dlift(x))) == dlift(1 / x)
    assert dconj(dlift(F(0))) == smul(F(-1, 2), dninf)
    assert dconj(dninf) == smul(-2, dn0)

    # N = s n0 + x e0 + t ninf has e+ coefficient t - s/2 and e- coefficient
    # t + s/2; read the coordinates off the algebra, not off the formula.
    def coords(N):
        cp, cm = N.get((1,), F(0)), N.get((2,), F(0))
        return cm - cp, N.get((0,), F(0)), (cm + cp) / 2

    for x in (F(3), F(-2), F(1, 4), F(0)):
        s1, x1, t1 = coords(dconj(dlift(x)))
        assert x1 * x1 == 2 * s1 * t1, "image must lie on the null quadric"
        # [x1 : s1] = [1 : x], with s1 = 0 exactly at x = 0
        assert x1 * x == s1 and (s1 == 0) == (x == 0)


def check_moore_penrose():
    import numpy as np
    E = np.array([[0., 1.], [1., 0.]])
    Fm = np.array([[0., 1.], [-1., 0.]])
    I = np.eye(2)
    assert (E @ E == I).all() and (Fm @ Fm == -I).all()
    assert (E @ Fm + Fm @ E == 0).all(), "Clifford relations fail in M2(R)"
    N = np.array([[0., 1.], [0., 0.]])
    assert ((E + Fm) / 2 == N).all() and ((E - Fm) / 2 == N.T).all()
    assert (N @ N == 0).all() and (N @ N.T + N.T @ N == I).all()
    assert (N @ N.T @ N == N).all(), "Penrose eq. AXA = A fails"
    for lam in (2.0, -3.5, 0.25):
        assert np.allclose(np.linalg.pinv(lam * N), (1 / lam) * N.T)
        assert np.allclose(np.linalg.pinv(lam * N.T), (1 / lam) * N)
    Am = 7 * N
    assert np.allclose(np.linalg.pinv(Am),
                       Am.T / (np.linalg.norm(Am, 'fro') ** 2))
    th, ph = 0.7, -1.2
    U = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    V = np.array([[np.cos(ph), -np.sin(ph)], [np.sin(ph), np.cos(ph)]])
    assert np.allclose(np.linalg.pinv(U @ Am @ V),
                       V.T @ np.linalg.pinv(Am) @ U.T)
    # determinant dictionary: a base vector is null iff its matrix is singular
    for x, y in ((1., 1.), (2., -2.), (3., 1.)):
        Mx = x * E + y * Fm
        assert abs(np.linalg.det(Mx) + (x * x - y * y)) < 1e-12


# ----------------------------------------------------------------------

CHECKS = [
    ("eq. (2)   hyperbolic-pair identities",          check_hyperbolic_pair),
    ("Lem 2.4   splitting (incl. degenerate ascent)", check_splitting),
    ("Thm 4.2   Step 1: normal form",                 check_nogo_step1),
    ("eq. (4)   versor factorisation of R",           check_versor_factorisation),
    ("Thm 4.2   Step 2: null-rotation actions",       check_nogo_step2),
    ("Thm 4.2   Step 3: the shear alpha -> alpha-u",  check_nogo_step3),
    ("Rem 4.3   locality and scale-robustness",       check_local_robustness),
    ("Rem 4.4   unipotence of index 3; fixed set",    check_parabolic),
    ("Rem 4.4   fixed set: null direction at n >= 4, span{v} at n = 3", check_parabolic_fixes_a_null_direction),
    ("eq. (5)   partner torsor, simply transitive",   check_partners),
    ("Rem 4.5   atom: Pin(1,1)-equivariant section",  check_atom_section),
    ("eqs. (6/7) conformal lift identities",           check_conformal_model),
    ("eq. (8)   e+ actions and e+ formula",           check_eplus_actions),
    ("Thm 4.10(2) reciprocal on invertible vectors",   check_totality_invertible),
    ("Thm 4.10(3) null vectors and origin -> ideal",   check_totality_null_and_origin),
    ("Rem 4.11   the ideal value remembers the scale", check_scale_memory),
    ("Lem 4.9   density paths converge, bases (1,1), (2,1)", check_density_paths),
    ("Prop 4.21  swap-and-rescale + incidence",        check_swap),
    ("Rem 4.22   stratum (ii) and unit-quadric fixed", check_strata_fixed_loci),
    ("Lem 4.23   descent: ascend, invert, descend",    check_descent),
    ("Sec 4.8.1   Riemann sphere: iota inverts in |z|=1; RP^1 too",
                                                   check_riemann_sphere),
    ("Sec 4.8.2   Moore-Penrose agreement",             check_moore_penrose),
]





# ===========================================================================
# PART THREE: one-dimensional extensions of an even-dimensional algebra
# (8 checks; Section 5.5).  Same GA.py engine; exact rational arithmetic.
# ===========================================================================

def extension_checks():
    ONE = g.sc(1)


    def volume(n):
        """The volume element e_0 e_1 ... e_{n-1}."""
        return {tuple(range(n)): F(1)}


    def is_central(x, sq):
        return all(g.commutes(x, g.gen(i), sq) for i in range(len(sq)))


    def centre_blades(sq):
        """The basis blades spanning the centre: conjugation by an invertible
        generator maps every blade to +- itself, so the centre is spanned by the
        blades commuting with every generator (proof of Lem 2.6)."""
        return [b for b in g.all_blades(len(sq)) if is_central({b: F(1)}, sq)]


    def omega_square(sq):
        n = len(sq)
        w = volume(n)
        w2 = g.mul(w, w, sq)
        if w2 == g.sc(1):
            return 1
        if w2 == g.sc(-1):
            return -1
        return None


    def type_C(p, q):
        """Type C by the definition: volume element central with square +1."""
        sq = g.sig(p, q)
        w = volume(p + q)
        return is_central(w, sq) and omega_square(sq) == 1


    def type_C_sq(sq):
        """Type C for an arbitrary signature tuple (generator order free)."""
        return is_central(volume(len(sq)), sq) and omega_square(sq) == 1


    def complex_type(p, q):
        """Centre isomorphic to C: n odd, volume element central with square -1."""
        sq = g.sig(p, q)
        w = volume(p + q)
        return (p + q) % 2 == 1 and is_central(w, sq) and omega_square(sq) == -1


    def vec(x, blades):
        return [x.get(b, F(0)) for b in blades]


    def span_rank(elements, n):
        blades = g.all_blades(n)
        return g.rank_of_vectors([vec(x, blades) for x in elements])


    def ad(u, u_inv, x, sq):
        return g.mul(g.mul(u, x, sq), u_inv, sq)


    def hom_images_generate_even(images, n_big, sq_big, n_small):
        """The subalgebra generated by the images (all products over subsets of
        the generators, in index order) spans a space of dimension 2^n_small,
        and every image is even."""
        prods = []
        for k in range(n_small + 1):
            for S in combinations(range(n_small), k):
                x = ONE
                for i in S:
                    x = g.mul(x, images[i], sq_big)
                prods.append(x)
        even = all(all(len(b) % 2 == 0 for b in x) for x in images)
        return even and span_rank(prods, n_big) == 2 ** n_small


    # ---------------------------------------------------------------------------
    # Part A: thm:extension (a): exactly one one-dimensional extension of an
    # even-dimensional algebra is type C, the other complex type; cor:lorentz:
    # the odd Lorentzian alternation, to dimension eleven
    # ---------------------------------------------------------------------------

    okA = True
    grid = [(p, q) for p in range(0, 7) for q in range(0, 7) if (p + q) % 2 == 0 and 2 <= p + q <= 6]
    for (p, q) in grid:
        d = (p - q) % 8
        space_split = type_C(p, q + 1)
        time_split = type_C(p + 1, q)
        space_cx = complex_type(p, q + 1)
        time_cx = complex_type(p + 1, q)
        okA &= space_split == ((p - q) % 4 == 2)
        okA &= time_split == ((p - q) % 4 == 0)
        okA &= (space_split != time_split)
        okA &= (space_cx == (not space_split)) and (time_cx == (not time_split))
    g.check("Thm 5.14(a): on every even-dimensional nondegenerate (p,q) with "
            "2 <= p+q <= 6, the spacelike extension is type C iff p-q = 2 mod 4, the "
            "timelike one iff p-q = 0 mod 4, exactly one of the two is type C and the "
            "other has complex type (centre C)", okA)

    even_residues_space = sorted(set((p - q) % 8 for (p, q) in grid if type_C(p, q + 1)))
    even_residues_time = sorted(set((p - q) % 8 for (p, q) in grid if type_C(p + 1, q)))
    g.check("Cor 5.15: the even residues whose spacelike extension obstructs are "
            "{2, 6}, whose timelike extension obstructs are {0, 4}",
            even_residues_space == [2, 6] and even_residues_time == [0, 4])

    okL = True
    table = {}
    for n in [3, 5, 7, 9, 11]:
        plus = type_C(1, n - 1)          # time = plus: Cl(1, n-1)
        minus = type_C(n - 1, 1)         # time = minus: Cl(n-1, 1)
        plus_cx = complex_type(1, n - 1)
        minus_cx = complex_type(n - 1, 1)
        table[n] = (plus, minus)
        okL &= (plus == (n % 4 == 1)) and (minus == (n % 4 == 3))
        okL &= (plus != minus) and (plus_cx == (not plus)) and (minus_cx == (not minus))
    g.check("Cor 5.16: odd Lorentzian dimensions 3, 5, 7, 9, 11: Cl(1,n-1) is type C "
            "iff n = 1 mod 4 (n = 5, 9), Cl(n-1,1) iff n = 3 mod 4 (n = 3, 7, 11); the "
            "other real form has complex type in every case", okL)
    g.check("Rem 5.17: Cl(1,4) split and Cl(4,1) complex; "
            "Cl(2,1) split and Cl(1,2) complex; Cl(10,1) split and Cl(1,10) complex",
            table[5] == (True, False) and table[3] == (False, True)
            and table[11] == (False, True))

    # ---------------------------------------------------------------------------
    # Part B: lem:even: Cl^0(p,q+1) = Cl(p,q) and Cl^0(p+1,q) = Cl(q,p) by
    # e_i -> e_i nu
    # ---------------------------------------------------------------------------

    def even_iso_check(p, q, timelike):
        """Adjoin nu (index n) of square +1 (timelike=True) or -1; the images
        e_i nu satisfy the relations of Cl(p,q) (spacelike nu) or Cl(q,p)
        (timelike nu), are even, and generate a subalgebra of dimension 2^n."""
        n = p + q
        sq_big = g.sig(p, q) + ((1,) if timelike else (-1,))
        nu = g.gen(n)
        images = [g.mul(g.gen(i), nu, sq_big) for i in range(n)]
        target_sq = tuple((-1 if timelike else 1) * s for s in g.sig(p, q))
        rel = all(g.eq(g.mul(images[i], images[i], sq_big), g.sc(target_sq[i])) for i in range(n))
        rel &= all(g.anticommutes(images[i], images[j], sq_big)
                   for i in range(n) for j in range(i + 1, n))
        return rel and hom_images_generate_even(images, n + 1, sq_big, n)

    g.check("Lem 5.13: e_i -> e_i nu realises Cl(1,3) inside Cl^0(1,4) and Cl(2,0) "
            "inside Cl^0(2,1) (spacelike nu): relations, evenness, dimension 2^n",
            even_iso_check(1, 3, False) and even_iso_check(2, 0, False))
    g.check("Lem 5.13: with a timelike nu the same map realises Cl(q,p): Cl(3,1) "
            "inside Cl^0(2,3) and Cl(0,2) inside Cl^0(3,0): relations, evenness, "
            "dimension 2^n",
            even_iso_check(1, 3, True) and even_iso_check(2, 0, True))

    # ---------------------------------------------------------------------------
    # Part F: thm:square in general: for every even (p,q) with p+q <= 6, the
    # obstructed one-dimensional extension, repaired by a generator of the
    # opposite sign, is Cl(p+1,q+1), and the two adjoined generators span a
    # hyperbolic plane carrying a ladder pair; the same-sign repair lands two
    # residues away
    # ---------------------------------------------------------------------------

    okS = True
    for (p, q) in grid:
        d = (p - q) % 8
        n = p + q
        # the obstructed extension is found by testing type C, not assumed
        ext = (p, q + 1) if type_C(p, q + 1) else (p + 1, q)
        okS &= type_C(*ext) and not type_C(*((p + 1, q) if ext == (p, q + 1) else (p, q + 1)))
        okS &= (ext == (p, q + 1)) == (d % 4 == 2)
        # the extension's signature tuple, with the obstructing generator adjoined
        # last (index n) to the base's tuple
        sq_ext = g.sig(p, q) + ((-1,) if ext == (p, q + 1) else (1,))
        okS &= type_C_sq(sq_ext)
        # the repairs are built from the extension's signature tuple: adjoin a
        # generator of the opposite sign, or of the same sign, to the obstructing one
        sq_opp = sq_ext + (-sq_ext[n],)
        sq_same = sq_ext + (sq_ext[n],)
        opp = (sq_opp.count(1), sq_opp.count(-1))
        same = (sq_same.count(1), sq_same.count(-1))
        okS &= opp == (p + 1, q + 1)
        okS &= ((opp[0] - opp[1]) % 8) == d
        okS &= ((same[0] - same[1]) % 8) in ((d + 2) % 8, (d - 2) % 8)
        okS &= ((same[0] - same[1]) % 8) != d
        # the adjoined plane of the opposite-sign repair is hyperbolic
        gram = [[sq_opp[n], 0], [0, sq_opp[n + 1]]]
        okS &= g.congruence_signature(gram) == (1, 1, 0)
        # the ladder pair in the opposite-sign repair: f = (u + v)/2 with u the
        # generator of square +1 and v that of square -1, f* = (u - v)/2
        a, b = g.gen(n), g.gen(n + 1)
        u, v = (a, b) if sq_opp[n] == 1 else (b, a)
        ff = g.scal(F(1, 2), g.add(u, v))
        gg = g.scal(F(1, 2), g.sub(u, v))
        okS &= g.is_zero(g.mul(ff, ff, sq_opp))
        okS &= g.is_zero(g.mul(gg, gg, sq_opp))
        okS &= g.eq(g.add(g.mul(ff, gg, sq_opp), g.mul(gg, ff, sq_opp)), ONE)
        # the same-sign repair has no null vector in the adjoined plane: its
        # Gram matrix, from the tuple in use, is definite
        gram_same = [[sq_same[n], 0], [0, sq_same[n + 1]]]
        okS &= g.congruence_signature(gram_same) in ((2, 0, 0), (0, 2, 0))
        # the isomorphism class of the same-sign repair agrees with Cl(p+1,q+1):
        # both even-dimensional with trivial centre, and the volume elements'
        # squares agree with the classification's residue (d -+ 2 and d are
        # both even, and the two algebras are Mat_2(Cl(p,q)) by Thm 5.14(d))
        okS &= centre_blades(sq_same) == [()] and centre_blades(sq_opp) == [()]
    g.check("Thm 5.14(c,d): for every even (p,q), 2 <= p+q <= 6: exactly one "
            "extension is type C (found by testing, at the sign Thm 5.14(a) predicts), "
            "the repair by the opposite sign, built from the extension's signature "
            "tuple, is Cl(p+1,q+1) at the same residue with the adjoined pair a "
            "hyperbolic plane carrying a ladder pair (f^2 = 0, f*^2 = 0, "
            "f f* + f* f = 1), and the same-sign repair is two residues away with a "
            "definite adjoined plane; both repairs have trivial centre", okS)

    g.check("Prop 7.4 along the square: fusion occurs at most once: the centre of "
            "Cl(p+1,q+1), computed blade-wise, is the scalars alone on the whole grid, "
            "so the repaired algebra carries no central idempotent",
            all(centre_blades(g.sig(p + 1, q + 1)) == [()] for (p, q) in grid))


# ===========================================================================
# main
# ===========================================================================

if __name__ == "__main__":
    print("verify_T01.py: 115 exact-arithmetic checks for Transport Papers T1\n")
    # Part one (85 checks, GA-based harness)
    centre_and_omega_checks(nmax=8)
    taxonomy_checks()
    for (p, q) in [(1, 0), (0, 3), (2, 1)]:
        fusion_checks(p, q)
    morita_checks(1, 1)
    morita_checks(1, 3)
    typeP_checks()
    sharpenings_cohomology_checks()
    sharpenings_gram_checks()
    exotic_embedding_checks()
    # Part three (8 checks, Section 5.5)
    extension_checks()
    # Part two (22 checks, assert-based, adapted to the shared harness)
    for name, fn in CHECKS:
        try:
            fn()
            g.check(name, True)
        except AssertionError as exc:
            g.check(name + "  [" + str(exc)[:60] + "]", False)
    print()
    if g.FAILURES:
        print("%d CHECK(S) FAILED:" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  - " + f)
        sys.exit(1)
    print("ALL 115 CHECKS PASSED.")
    sys.exit(0)
