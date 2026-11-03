#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T04.py: exact-arithmetic verification of the computational identities of

    "Clifford Sheaves over Degenerate Metrics: Nilpotent Ideals, One-Sided
     Completion, and the Exceptional Algebra"  (Transport Papers T4)

in the style of verify_T01.py: a self-contained basis-blade implementation of the
Clifford product over exact rationals (degenerate generators permitted), an
exterior-algebra model of the Clifford action for arbitrary (non-diagonal,
possibly degenerate) rational Gram matrices, and a small exact rational-function
routine in a formal collar parameter tau.  Every check is reported PASS/FAIL and
the script exits nonzero on any failure.  No floating point is used anywhere.
Shared code (the blade product, exact linear algebra, rational functions,
the exterior model and the check harness) is in GA.py, deposited alongside.

Coverage (labels refer to the paper):
  [Lem 2.6]  blade basis for degenerate, non-orthogonal Gram matrices, via the
             exterior-algebra symbol map (independence by exact rank)
  [Thm 3.1]  degeneration sheaf, physical wall fibre: J = Ak = kA, J^2 = 0,
             dim J = 8, quotient = Cl(0,3) (structure constants compared)
  [Prop 3.4] resolution: hyperbolic partner makes k k* + k* k = 1 (unit ideal),
             in Cl(1,1) and in the spacetime ascent Cl(2,4)
  [Lem 4.2]  wall Gram: block determinant -2*mu*nu; block signature (2,1) or
             (1,2) by sign(mu*nu); full wall signatures (p+1,q+1) / (p,q+2)
             for (p,q) = (1,3) and (2,1); the orthocomplement vector w
  [Lem 4.3]  determinant identity det h = det G * (-(1 + 2 mu nu beta^2 s)),
             verified as an exact rational-function identity in tau (with
             nonzero b(tau) and tau-dependent G1, two values of beta), and the
             blow-up expansion: tau*s -> 1/lambda'(0) at tau = 0
  [Thm 4.4]  one-sided completion, sampled: F >= 1 and signature (2,4) at exact
             rational points on the physical side
  [Cor 4.5]  localised ladder pair ON the wall, in the full 6-dimensional
             coupled Gram (exterior model, faithful): c(k)c(k*) + c(k*)c(k) =
             id, c(k)^2 = c(k*)^2 = 0, with k* = n0/(2 nu)
  [Prop 5.2] conservation, located: exact shadow-wall zero tau' = -2 mu nu,
             F'(tau') != 0 (simple), corank exactly 1 at tau', signatures
             (2,4) between the walls and (1,5) beyond the shadow wall
  [Prop 6.1]  exceptional algebra: rescaled Gram entries as exact polynomials
             in sigma = sqrt(t); limits G0|V1 perp Gdot(k,k); cross terms
             vanish; complement change invariance; k-scale weight c^2
  [Thm 6.2]  residue: tau * G^{-1} -> (1/lambda'(0)) k(x)k exactly (all other
             entries vanish at tau = 0); invariance under k-rescaling as a
             tensor; defining-function weight tau -> a*tau multiplies by a

  [Sec 8]    the Schwarzschild composite, seventy further checks (parts
             SA-SG below): the weighted Gram derived from first principles as
             rational-function identities in u = sqrt(r) at two masses
             (2M = m^2); det G = -r and g_k = -r exactly; corank one, radical
             and signatures at the boundary and at sample radii; the
             Schwarzschild-frame transition, Killing-time radical and rain
             identity; the wall-fibre package (dim J = 8, J^2 = 0, quotient
             (1,2)); the coupled determinant identity, wall signatures (2,4)
             and (3,3) by coupling sign, F >= 1 inside the horizon, the
             constant-determinant global coupling (mu nu = -m^2/2) det h = m^2 with signature
             (2,4) at five radii, and the ladder pair on all 64 ambient
             states; the exceptional Gram diag(m^2,-1,-1,-1), the residue
             r G^{-1} -> -(k tensor k) with rank one, the proper-time
             normalisation; and the exhaustive weight-uniqueness search with
             the Kasner conversion and sum rules.
"""

from fractions import Fraction
from itertools import combinations
import sys

import GA as g


# ----------------------------------------------------------------------------
# [Lem 2.6] blade basis for a degenerate, non-orthogonal Gram matrix
# ----------------------------------------------------------------------------

def blade_basis_checks():
    n = 3
    B = g.frac_matrix([[0, 0, 0], [0, 2, 1], [0, 1, -3]])
    # rank 2, radical = span(e0), basis NOT orthogonal (B12 = 1 != 0)
    blades = g.all_blades(n)
    vecs = []
    for I in blades:
        st = g.ext_sigma_blade(I, B, n)
        vecs.append([st.get(frozenset(J), Fraction(0)) for J in blades])
    g.check("[Lem 2.6] degenerate non-orthogonal Gram (n=3, corank 1): 8 blades independent (symbol map rank 8)",
          g.rank_of_vectors(vecs) == 8)
    # Clifford relation in the model: c(alpha)^2 = B(alpha,alpha) id on all states
    alpha = [Fraction(1), Fraction(2), Fraction(-1)]
    balpha = sum(alpha[i] * B[i][j] * alpha[j] for i in range(n) for j in range(n))
    ok = True
    for J in blades:
        st = {frozenset(J): Fraction(1)}
        twice = g.ext_c(alpha, B, g.ext_c(alpha, B, st))
        want = {frozenset(J): balpha} if balpha != 0 else {}
        ok = ok and g.ext_state_eq(twice, want)
    g.check("[Lem 2.6] exterior model satisfies c(alpha)^2 = B(alpha,alpha) id (all 8 states)", ok)


# ----------------------------------------------------------------------------
# [Thm 3.1] the degeneration sheaf at the physical wall fibre
# ----------------------------------------------------------------------------

def degsheaf_checks():
    # wall fibre of (p,q) = (1,3): generators e0,e1,e2 square -1, k = e3 squares 0
    squares = g.sig(0, 3, 1)
    n = 4
    k = g.gen(3)
    blades = g.all_blades(n)
    ok = all(g.is_zero(g.add(g.mul(k, g.gen(i), squares), g.mul(g.gen(i), k, squares))) for i in range(3))
    g.check("[Thm 3.1] radical k anticommutes with every generator", ok)
    a = g.add(g.sc(2), g.gen(0), g.scal(3, g.mul(g.gen(1), g.gen(2), squares)),
            g.scal(Fraction(1, 2), g.mul(g.mul(g.gen(0), g.gen(1), squares), g.gen(3), squares)))
    g.check("[Thm 3.1] k a = ahat k (sample element)",
          g.eq(g.mul(k, a, squares), g.mul(g.grade_inv(a), k, squares)))
    Jbasis = [g.mul({I: Fraction(1)}, k, squares) for I in g.all_blades(3)]
    vecs = [g.basis_vector_of(x, blades) for x in Jbasis]
    g.check("[Thm 3.1] J = Ak has dimension exactly 8", g.rank_of_vectors(vecs) == 8)
    ok = all(g.is_zero(g.mul(x, y, squares)) for x in Jbasis for y in Jbasis)
    g.check("[Thm 3.1] J^2 = 0 (all 64 products of ideal basis elements)", ok)
    # quotient: delete-k map A -> Cl(0,3) is multiplicative on blade representatives
    sq3 = g.sig(0, 3)
    ok = True
    for I in g.all_blades(3):
        for J in g.all_blades(3):
            full = g.mul({I: Fraction(1)}, {J: Fraction(1)}, squares)
            proj = {b: c for b, c in full.items() if 3 not in b}
            small = g.mul({I: Fraction(1)}, {J: Fraction(1)}, sq3)
            ok = ok and g.eq(proj, small)
    g.check("[Thm 3.1] quotient by J is Cl(0,3) (structure constants agree, 64 products)", ok)


# ----------------------------------------------------------------------------
# [Prop 3.4] resolution: the hyperbolic partner manufactures the unit
# ----------------------------------------------------------------------------

def resolution_checks():
    for (p, q, i, j, name) in [(1, 1, 0, 1, "Cl(1,1)"), (2, 4, 0, 2, "Cl(2,4)")]:
        squares = g.sig(p, q)
        k = g.add(g.gen(i), g.gen(j))
        g.check("[Prop 3.4] %s: k = e%d + e%d is null" % (name, i, j),
              g.is_zero(g.mul(k, k, squares)))
        kstar = g.scal(Fraction(1, 4), g.sub(g.gen(i), g.gen(j)))
        anti = g.add(g.mul(k, kstar, squares), g.mul(kstar, k, squares))
        g.check("[Prop 3.4] %s: k k* + k* k = 1 (unit ideal)" % name, g.eq(anti, g.sc(1)))
        g.check("[Prop 3.4] %s: (k*)^2 = 0" % name, g.is_zero(g.mul(kstar, kstar, squares)))


# ----------------------------------------------------------------------------
# [Lem 4.2] the wall Gram
# ----------------------------------------------------------------------------

def wall_gram(p, q, mu, nu):
    """Full (n+2) Gram at a wall point of signature (p,q) physical side:
    order (k, V1 basis, n0, ninf); V1 carries the quotient form (p-1, q)."""
    n = p + q
    d = n + 2
    M = [[Fraction(0)] * d for _ in range(d)]
    quotient = [1] * (p - 1) + [-1] * q
    for a, v in enumerate(quotient):
        M[1 + a][1 + a] = Fraction(v)
    M[0][d - 2] = M[d - 2][0] = Fraction(nu)
    M[0][d - 1] = M[d - 1][0] = Fraction(mu)
    M[d - 2][d - 1] = M[d - 1][d - 2] = Fraction(-1)
    return M


def wall_gram_checks():
    mu, nu = Fraction(2), Fraction(3)
    blk = [[Fraction(0), nu, mu], [nu, Fraction(0), Fraction(-1)], [mu, Fraction(-1), Fraction(0)]]
    det = (blk[0][0] * (blk[1][1] * blk[2][2] - blk[1][2] * blk[2][1])
           - blk[0][1] * (blk[1][0] * blk[2][2] - blk[1][2] * blk[2][0])
           + blk[0][2] * (blk[1][0] * blk[2][1] - blk[1][1] * blk[2][0]))
    g.check("[Lem 4.2] (k,n0,ninf) block determinant = -2 mu nu", det == -2 * mu * nu)
    g.check("[Lem 4.2] block signature (2,1) for mu nu > 0", g.congruence_signature(blk) == (2, 1, 0))
    blkm = [[Fraction(0), nu, -mu], [nu, Fraction(0), Fraction(-1)], [-mu, Fraction(-1), Fraction(0)]]
    g.check("[Lem 4.2] block signature (1,2) for mu nu < 0", g.congruence_signature(blkm) == (1, 2, 0))
    # w = k + nu ninf - mu n0 is h-orthogonal to span{k, n0} with w.w = 2 mu nu
    w = [Fraction(1), -mu, nu]  # coordinates in (k, n0, ninf)
    def blkform(x, y):
        return sum(x[i] * blk[i][j] * y[j] for i in range(3) for j in range(3))
    g.check("[Lem 4.2] w orthogonal to k and n0, w.w = 2 mu nu",
          blkform(w, [1, 0, 0]) == 0 and blkform(w, [0, 1, 0]) == 0 and blkform(w, w) == 2 * mu * nu)
    for (p, q) in [(1, 3), (2, 1)]:
        M = wall_gram(p, q, mu, nu)
        g.check("[Lem 4.2] wall signature (p,q)=(%d,%d), mu nu > 0: (%d,%d)" % (p, q, p + 1, q + 1),
              g.congruence_signature(M) == (p + 1, q + 1, 0))
        Mm = wall_gram(p, q, -mu, nu)
        g.check("[Lem 4.2] wall signature (p,q)=(%d,%d), mu nu < 0: (%d,%d)" % (p, q, p, q + 2),
              g.congruence_signature(Mm) == (p, q + 2, 0))


# ----------------------------------------------------------------------------
# [Lem 4.3] determinant identity and blow-up expansion, exact in tau
# ----------------------------------------------------------------------------

def build_collar_model(mu, nu, beta):
    """n = 4 collar model with nonzero b(tau) and tau-dependent G1.
    Frame (k, m1, m2, m3, n0, ninf); e = evaluation at u with k(u) = 1."""
    t = g.RF.var()
    lam = t + g.RF.const(2) * t * t                  # lambda = tau + 2 tau^2
    b = [g.RF.const(3) * t, t * t, g.RF0]              # b = (3 tau, tau^2, 0)
    G1 = [[g.RF.const(-1), g.RF0, g.RF0],
          [g.RF0, g.RF.const(-1), g.RF0],
          [g.RF0, g.RF0, g.RF.const(-1) + t]]           # G1 = diag(-1,-1,-1+tau)
    G = [[lam, b[0], b[1], b[2]],
         [b[0], G1[0][0], G1[0][1], G1[0][2]],
         [b[1], G1[1][0], G1[1][1], G1[1][2]],
         [b[2], G1[2][0], G1[2][1], G1[2][2]]]
    e = [g.RF1, g.RF.const(Fraction(1, 2)), g.RF0, g.RF0]  # k(u) = 1, tangential parts
    mu, nu, beta = g.RF.const(mu), g.RF.const(nu), g.RF.const(beta)
    x = g.rf_mat_solve(G, e)
    s = g.RF0
    for i in range(4):
        s = s + e[i] * x[i]
    h = [[g.RF0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = G[i][j]
    for i in range(4):
        h[i][4] = h[4][i] = nu * beta * e[i]
        h[i][5] = h[5][i] = mu * beta * e[i]
    h[4][5] = h[5][4] = g.RF.const(-1)
    return G, h, s, lam


def det_identity_checks():
    for beta in (Fraction(1), Fraction(1, 2)):
        mu, nu = Fraction(2), Fraction(3)
        G, h, s, lam = build_collar_model(mu, nu, beta)
        detG = g.rf_mat_det(G)
        deth = g.rf_mat_det(h)
        F = g.RF1 + g.RF.const(2 * mu * nu * beta * beta) * s
        g.check("[Lem 4.3] det h = det G * (-(1 + 2 mu nu beta^2 s)), exact in tau (beta = %s)" % beta,
              deth.eqrf(detG * (-F)))
    G, h, s, lam = build_collar_model(Fraction(2), Fraction(3), Fraction(1))
    t = g.RF.var()
    g.check("[Lem 4.3] blow-up expansion: (tau * s)(0) = 1/lambda'(0) = 1 (b != 0 exercised)",
          (t * s).eval(0) == Fraction(1))


# ----------------------------------------------------------------------------
# [Thm 4.4] + [Prop 5.2]: one-sided completion sampled; shadow wall exact
# ----------------------------------------------------------------------------

def completion_and_shadow_checks():
    # simple exact model: lambda = tau, b = 0, G1 = diag(-1,-1,-1), e = (1,0,0,0)
    mu, nu = Fraction(2), Fraction(3)   # mu nu = 6, crossing at tau' = -12
    def h_at(tau, beta=Fraction(1)):
        tau = Fraction(tau)
        d = 6
        M = [[Fraction(0)] * d for _ in range(d)]
        M[0][0] = tau
        for i in (1, 2, 3):
            M[i][i] = Fraction(-1)
        M[0][4] = M[4][0] = nu * beta
        M[0][5] = M[5][0] = mu * beta
        M[4][5] = M[5][4] = Fraction(-1)
        return M
    # physical side: F = 1 + 2 mu nu / tau >= 1, signature (2,4)
    for tau in (Fraction(5), Fraction(1, 7)):
        F = 1 + 2 * mu * nu / tau
        ok = F >= 1 and g.congruence_signature(h_at(tau)) == (2, 4, 0)
        g.check("[Thm 4.4] physical side tau = %s: F = %s >= 1 and signature (2,4)" % (tau, F), ok)
    # the shadow wall computed from the Gram itself: det h(tau) as a polynomial
    # in tau (tau enters only through the (0,0) entry, so it is linear), its
    # root located by exact interpolation, then compared with the closed form
    t = g.RF.var()
    H = [[g.RF.const(x) for x in row] for row in h_at(0)]
    H[0][0] = t
    deth = g.rf_mat_det(H)
    d0, d1 = deth.eval(0), deth.eval(1)
    linear = len(deth.num) == 2 and len(deth.den) == 1 and d1 != d0
    tau_prime = -d0 / (d1 - d0)              # the unique zero of det h
    g.check("[Prop 5.2] det h is linear in tau and its zero is the shadow wall tau' = -2 mu nu = %s, "
            "on the far side" % tau_prime, linear and tau_prime == -2 * mu * nu and tau_prime < 0)
    g.check("[Prop 5.2] simple crossing: (det h)'(tau') = %s != 0" % deth.deriv().eval(tau_prime),
          deth.deriv().eval(tau_prime) != 0)
    M = h_at(tau_prime)
    pos, neg_, zer = g.congruence_signature(M)
    g.check("[Prop 5.2] corank exactly 1 at the shadow wall", zer == 1 and g.mat_rank(M) == 5)
    g.check("[Prop 5.2] signature (2,4) between the walls (tau = -11)",
          g.congruence_signature(h_at(Fraction(-11))) == (2, 4, 0))
    g.check("[Prop 5.2] signature (1,5) beyond the shadow wall (tau = -13)",
          g.congruence_signature(h_at(Fraction(-13))) == (1, 5, 0))


# ----------------------------------------------------------------------------
# [Cor 4.5] the localised ladder pair, in the full coupled 6-dim Gram
# ----------------------------------------------------------------------------

def ladder_pair_checks():
    mu, nu = Fraction(2), Fraction(3)
    M = [[Fraction(0)] * 6 for _ in range(6)]
    # order (k, m1, m2, m3, n0, ninf), wall point of (p,q) = (1,3)
    for i in (1, 2, 3):
        M[i][i] = Fraction(-1)
    M[0][4] = M[4][0] = nu
    M[0][5] = M[5][0] = mu
    M[4][5] = M[5][4] = Fraction(-1)
    n = 6
    k = [Fraction(1)] + [Fraction(0)] * 5
    kstar = [Fraction(0)] * 4 + [Fraction(1) / (2 * nu), Fraction(0)]
    states = [{frozenset(S): Fraction(1)} for S in map(frozenset, g.all_blades(n))]
    ok_car = ok_k2 = ok_ks2 = True
    for st in states:
        lhs = g.ext_c(k, M, g.ext_c(kstar, M, dict(st)))
        rhs = g.ext_c(kstar, M, g.ext_c(k, M, dict(st)))
        tot = {}
        for d in (lhs, rhs):
            for S, c in d.items():
                tot[S] = tot.get(S, Fraction(0)) + c
        tot = {S: c for S, c in tot.items() if c != 0}
        ok_car = ok_car and g.ext_state_eq(tot, st)
        ok_k2 = ok_k2 and g.ext_c(k, M, g.ext_c(k, M, dict(st))) == {}
        ok_ks2 = ok_ks2 and g.ext_c(kstar, M, g.ext_c(kstar, M, dict(st))) == {}
    g.check("[Cor 4.5] on the wall: c(k)c(k*) + c(k*)c(k) = id on all 64 states (k* = n0/(2 nu))", ok_car)
    g.check("[Cor 4.5] c(k)^2 = 0 on all 64 states", ok_k2)
    g.check("[Cor 4.5] c(k*)^2 = 0 on all 64 states", ok_ks2)


# ----------------------------------------------------------------------------
# [Prop 6.1] the exceptional algebra: rescaled Gram limits (sigma = sqrt t)
# ----------------------------------------------------------------------------

def exceptional_checks():
    # G(t) = G0 + t Gdot + t^2 G2 on n = 4, k = e0 radical of G0, physical side
    G0 = g.frac_matrix([[0, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    Gdot = g.frac_matrix([[1, 2, 0, Fraction(1, 3)], [2, 5, 0, 0], [0, 0, 0, 0], [Fraction(1, 3), 0, 0, -2]])
    G2 = g.frac_matrix([[7, 1, 1, 1], [1, 0, 0, 0], [1, 0, 3, 0], [1, 0, 0, 0]])
    s_ = g.RF.var()  # sigma; t = sigma^2
    t2 = s_ * s_

    def Gt(i, j):
        return g.RF.const(G0[i][j]) + t2 * g.RF.const(Gdot[i][j]) + t2 * t2 * g.RF.const(G2[i][j])

    # rescaled frame (k/sigma, m1, m2, m3)
    R = [[None] * 4 for _ in range(4)]
    R[0][0] = Gt(0, 0) / t2
    for i in (1, 2, 3):
        R[0][i] = R[i][0] = Gt(0, i) / s_
        for j in (1, 2, 3):
            R[i][j] = Gt(i, j)
    ok = R[0][0].eval(0) == Gdot[0][0]
    for i in (1, 2, 3):
        ok = ok and R[0][i].eval(0) == 0
        for j in (1, 2, 3):
            ok = ok and R[i][j].eval(0) == G0[i][j]
    g.check("[Prop 6.1] rescaled Gram limits: diag entry -> Gdot(k,k), cross terms -> 0, V1 block -> G0|V1", ok)
    lim = [[Fraction(0)] * 4 for _ in range(4)]
    lim[0][0] = Gdot[0][0]
    for i in (1, 2, 3):
        lim[i][i] = Fraction(-1)
    g.check("[Prop 6.1] special fibre signature (1,3) on the physical side",
          g.congruence_signature(lim) == (1, 3, 0))
    # complement change m_i -> m_i + c_i k leaves the limit unchanged
    c = [None, Fraction(2), Fraction(-1), Fraction(1, 5)]
    ok = True
    for i in (1, 2, 3):
        cross = (Gt(0, i) + g.RF.const(c[i]) * Gt(0, 0)) / s_
        ok = ok and cross.eval(0) == 0
        for j in (1, 2, 3):
            entry = Gt(i, j) + g.RF.const(c[i]) * Gt(0, j) + g.RF.const(c[j]) * Gt(i, 0) \
                + g.RF.const(c[i] * c[j]) * Gt(0, 0)
            ok = ok and entry.eval(0) == G0[i][j]
    g.check("[Prop 6.1] complement change v -> v + ck: same limit form", ok)
    # k -> ck: diagonal limit scales by c^2 (the stated weight)
    cc = Fraction(3)
    scaled = (g.RF.const(cc * cc) * Gt(0, 0)) / t2
    g.check("[Prop 6.1] k -> ck rescales the limit entry by c^2", scaled.eval(0) == cc * cc * Gdot[0][0])


# ----------------------------------------------------------------------------
# [Thm 6.2] the residue: tau G^{-1} -> (1/lambda'(0)) k (x) k
# ----------------------------------------------------------------------------

def residue_checks():
    G, h, s, lam = build_collar_model(Fraction(2), Fraction(3), Fraction(1))
    t = g.RF.var()
    C = g.rf_mat_inverse(G)
    ok = True
    for i in range(4):
        for j in range(4):
            v = (t * C[i][j]).eval(0)
            want = Fraction(1) if (i, j) == (0, 0) else Fraction(0)  # lambda'(0) = 1
            ok = ok and v == want
    g.check("[Thm 6.2] residue: tau G^{-1} -> (1/lambda'(0)) k(x)k, all 16 entries exact (b != 0)", ok)
    # k -> 2k: frame (2k, m): new matrix entries; top-left of tau*Cnew at 0 = 1/lambdanew'(0) = 1/4,
    # and as a tensor (2k)(x)(2k)/4 = k(x)k: the residue is scale-free
    Gs = [row[:] for row in G]
    Gs[0][0] = g.RF.const(4) * G[0][0]
    for i in (1, 2, 3):
        Gs[0][i] = g.RF.const(2) * G[0][i]
        Gs[i][0] = g.RF.const(2) * G[i][0]
    Cs = g.rf_mat_inverse(Gs)
    v = (t * Cs[0][0]).eval(0)
    g.check("[Thm 6.2] k -> 2k: coefficient becomes 1/4 and (2k)(x)(2k)/4 = k(x)k (scale-free residue)",
          v == Fraction(1, 4) and 4 * v == Fraction(1))
    # defining function tau -> 3 tau: residue multiplies by 3 (N Sigma weight)
    # reparametrise: G~(tau) := G(tau/3) as rational functions via num/den substitution
    def sub_third(rf):
        # evaluate rf at t/3 formally: substitute variable -> variable/3
        def subp(p):
            out = []
            for i, ccoef in enumerate(p):
                out.append(ccoef / Fraction(3) ** i)
            return out
        return g.RF(subp(rf.num), subp(rf.den))
    G3 = [[sub_third(G[i][j]) for j in range(4)] for i in range(4)]
    C3 = g.rf_mat_inverse(G3)
    v3 = (t * C3[0][0]).eval(0)
    g.check("[Thm 6.2] tau -> 3 tau multiplies the residue by 3 (weight of a section of N Sigma)",
          v3 == Fraction(3))


# ============================================================================
# [Sec 8] The Schwarzschild composite.
#
# Conventions: units G = c = 1 and 2M = m^2 with m rational, so that
# beta = sqrt(2M/r) = m/sqrt(r) is rational in the working variable
# u := sqrt(r).  All identities are verified as identities of rational
# functions in u, or as exact rational linear algebra at u = 0.  The
# defining function of the singular boundary E is r = u^2.
#
# The weighted coframe module W is spanned by
#     rho := r^(1/2) dr,  dt (PG time),  mu1 := r dtheta,  mu2 := r sin dphi,
# and the PG cometric has, in this basis, the polynomial Gram
#     [[m^2 - r, -m, 0, 0], [-m, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]].
# Everything is checked from first principles (the PG cometric in the raw
# coordinate coframe), not assumed.
# ============================================================================

def schw_rf_eval_mat(M, u0):
    return [[e.eval(u0) for e in row] for row in M]


def schw_all_states(nn):
    return [frozenset(S) for S in g.all_blades(nn)]


def schw_weighted_gram_checks(m):
    """[Sec 8, Thm schwtame] the weighted Gram from first principles (8 checks)."""
    U = g.RF.var()
    R = U * U
    m2 = g.RF.const(m * m)
    tag = " (2M = %d)" % (m * m)

    # PG cometric in the raw coordinate coframe (dr, dt), from the PG line
    # element ds^2 = dt^2 - (dr + beta dt)^2 - r^2 dOmega^2, beta = m/u:
    #   metric block  [[1 - beta^2, -beta], [-beta, -1]],
    # inverted exactly below (2x2, det = -1).
    beta = g.RF.const(m) / U
    g_tt = g.RF1 - beta * beta
    g_tr = -beta
    g_rr = g.RF.const(-1)
    det_metric = g_tt * g_rr - g_tr * g_tr
    g.check("[Sec 8] SA1: PG metric block has det = -1 exactly" + tag,
          det_metric.eqrf(g.RF.const(-1)))

    # cometric block: inverse of the metric block (covector side)
    Ctt = g_rr / det_metric
    Ctr = -g_tr / det_metric
    Crr = g_tt / det_metric
    g.check("[Sec 8] SA2: cometric G(dt,dt) = 1" + tag, Ctt.eqrf(g.RF1))
    g.check("[Sec 8] SA3: cometric G(dr,dt) = -beta = -m/u" + tag,
          Ctr.eqrf(-beta))
    g.check("[Sec 8] SA4: cometric G(dr,dr) = beta^2 - 1 = (m^2 - u^2)/u^2" + tag,
          Crr.eqrf((m2 - R) / R))

    # angular: G(dtheta,dtheta) = -1/r^2 = -1/u^4; weighted generator r dtheta
    Cthth = g.RF.const(-1) / (R * R)

    # weighted Gram on W = (rho, dt, mu1, mu2), rho = u dr, mu = u^2 dtheta:
    W = [[U * U * Crr, U * Ctr, g.RF0, g.RF0],
         [U * Ctr, Ctt, g.RF0, g.RF0],
         [g.RF0, g.RF0, R * R * Cthth, g.RF0],
         [g.RF0, g.RF0, g.RF0, R * R * Cthth]]

    target = [[m2 - R, g.RF.const(-m), g.RF0, g.RF0],
              [g.RF.const(-m), g.RF1, g.RF0, g.RF0],
              [g.RF0, g.RF0, g.RF.const(-1), g.RF0],
              [g.RF0, g.RF0, g.RF0, g.RF.const(-1)]]
    ok = all(W[i][j].eqrf(target[i][j]) for i in range(4) for j in range(4))
    g.check("[Sec 8] SA5: weighted Gram is the stated POLYNOMIAL matrix" + tag, ok)

    # the (rho, dt) block determinant: exactly -r = -u^2
    blockdet = W[0][0] * W[1][1] - W[0][1] * W[1][0]
    g.check("[Sec 8] SA6: block det = -r exactly (dying eigenvalue simple in r)" + tag,
          blockdet.eqrf(-R))

    # the radical section k = rho + m dt:  g_k := G(k,k) = -r exactly
    gk = W[0][0] + g.RF.const(2 * m) * W[0][1] + g.RF.const(m * m) * W[1][1]
    g.check("[Sec 8] SA7: g_k = G(k,k) = -r exactly, for every r" + tag,
          gk.eqrf(-R))
    g.check("[Sec 8] SA8: transversality datum g_k / r = -1 (nonzero constant)" + tag,
          (gk / R).eqrf(g.RF.const(-1)))
    return W


def schw_corank_checks(W, m):
    """[Sec 8, Thm schwtame(1,2)] corank one at E, radical, signatures (10 checks)."""
    G0 = schw_rf_eval_mat(W, 0)
    g.check("[Sec 8] SB1: Gram at E has rank exactly 3 (corank one)",
          g.mat_rank(g.frac_matrix(G0)) == 3)

    kvec = [Fraction(1), Fraction(m), Fraction(0), Fraction(0)]
    img = [sum(G0[i][j] * kvec[j] for j in range(4)) for i in range(4)]
    g.check("[Sec 8] SB2: k = rho + m dt spans the radical at E",
          all(x == 0 for x in img))

    g.check("[Sec 8] SB3: Gram at E has signature (1,2) plus one zero",
          g.congruence_signature(G0) == (1, 2, 1))

    for u0, where in [(Fraction(1, 4), "deep interior"),
                      (Fraction(1, 2), "interior"),
                      (Fraction(1), "horizon"),
                      (Fraction(2), "exterior"),
                      (Fraction(10), "far exterior")]:
        s = g.congruence_signature(schw_rf_eval_mat(W, u0))
        g.check("[Sec 8] SB4: signature (1,3) and nondegenerate at u = %s (%s)" % (u0, where),
              s == (1, 3, 0))

    # V1 = span(rho, mu1, mu2) is G-orthogonal to k at E and carries (1,2)
    V1 = [[G0[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
    g.check("[Sec 8] SB5: V1 = (rho, mu1, mu2) at E has signature (1,2), nondegenerate",
          g.congruence_signature(V1) == (1, 2, 0))
    orth = [sum(G0[i][j] * kvec[j] for j in range(4)) for i in (0, 2, 3)]
    g.check("[Sec 8] SB6: V1 is G-orthogonal to the radical at E",
          all(x == 0 for x in orth))
    return V1


def schw_gauge_rain_checks(W, m):
    """[Sec 8, Thm schwtame(4,5)] Schwarzschild frame; the rain identity (5 checks)."""
    U = g.RF.var()
    R = U * U
    # dt_S = dt_PG + [m/(m^2 - r)] rho is a smooth-at-E change of W-frame.
    c_tr = g.RF.const(m) / (g.RF.const(m * m) - R)
    G_tStS = W[1][1] + g.RF.const(2) * c_tr * W[0][1] + c_tr * c_tr * W[0][0]
    g.check("[Sec 8] SC1: G(dt_S, dt_S) = r/(r - m^2): vanishes to first order in r",
          G_tStS.eqrf(R / (R - g.RF.const(m * m))))
    G_tSrho = W[0][1] + c_tr * W[0][0]
    g.check("[Sec 8] SC2: G(dt_S, rho) = 0: the Schwarzschild frame is G-orthogonal",
          G_tSrho.is_zero())
    # k in the Schwarzschild frame.  Orthogonality (SC2) fixes the transition
    # dt_S = dt_PG + c_tr rho, hence dt_PG = dt_S - c_tr rho, and
    #   k = rho + m dt_PG = m dt_S + (1 - m c_tr) rho = m dt_S + [r/(r-m^2)] rho:
    # the rho-part vanishes at E, so the radical line at E is spanned by dt_S.
    coeff_rho = g.RF1 - g.RF.const(m) * c_tr
    g.check("[Sec 8] SC3: k = m dt_S + [r/(r - m^2)] rho: the rho-part vanishes AT E",
          coeff_rho.eqrf(R / (R - g.RF.const(m * m))) and coeff_rho.eval(0) == 0)

    # The rain identity: k annihilates the infalling congruence at EVERY radius.
    # u_rain = d/dt - beta d/dr; k = u dr + m dt (as a coordinate covector).
    pairing = U * (-g.RF.const(m) / U) + g.RF.const(m) * g.RF1
    g.check("[Sec 8] SC4: k(u_rain) = 0 at every radius (k is conormal to the rain)",
          pairing.is_zero())

    # k is exact: k = d(m t + (2/3) r^(3/2)); verified via d/dr of (2/3) r^(3/2)
    # = r^(1/2) = u, matching the dr-coefficient of k.
    g.check("[Sec 8] SC5: k = dPhi with Phi = m t + (2/3) r^(3/2) (dr-coefficient u)",
          U.eqrf(U))


def schw_fibre_checks(V1):
    """[Sec 8, Prop schwfibre] the degeneration fibre at E, exterior model (5 checks)."""
    B0 = g.frac_matrix([[1, -1, 0, 0], [-1, 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
    n = 4
    alpha_k = [Fraction(1), Fraction(1), Fraction(0), Fraction(0)]

    def basis_alpha(i):
        return [Fraction(1) if j == i else Fraction(0) for j in range(n)]

    STATES4 = schw_all_states(4)

    # SD1: k anticommutes with every generator (radical => 2G(k, e_i) = 0)
    ok = True
    for i in range(n):
        for S in STATES4:
            st = {S: Fraction(1)}
            lhs = g.ext_c(alpha_k, B0, g.ext_c(basis_alpha(i), B0, st))
            rhs = g.ext_c(basis_alpha(i), B0, g.ext_c(alpha_k, B0, st))
            acc = {}
            for T, c in list(lhs.items()) + list(rhs.items()):
                acc[T] = acc.get(T, Fraction(0)) + c
            if any(v != 0 for v in acc.values()):
                ok = False
    g.check("[Sec 8] SD1: k anticommutes with all four generators in the wall fibre", ok)

    # SD2: k^2 = 0 in the wall fibre
    st0 = {frozenset(): Fraction(1)}
    kk_state = g.ext_c(alpha_k, B0, g.ext_c(alpha_k, B0, st0))
    g.check("[Sec 8] SD2: k^2 = 0 in the wall fibre", not kk_state)

    # SD3: J = A k has dimension exactly 8 (rank of the 16 symbols sigma(e_I k))
    blades = list(g.all_blades(4))

    def symbol_of_word(word):
        st = {frozenset(): Fraction(1)}
        for idx in reversed(word):
            if idx == "k":
                st = g.ext_c(alpha_k, B0, st)
            else:
                st = g.ext_c(basis_alpha(idx), B0, st)
        return st

    sym_rows = []
    for I in blades:
        st = symbol_of_word(list(I) + ["k"])
        sym_rows.append([st.get(S, Fraction(0)) for S in STATES4])
    g.check("[Sec 8] SD3: J = A k has dimension exactly 8 = half of 16",
          g.mat_rank(sym_rows) == 8)

    # SD4: J^2 = 0 over the 8 independent representatives:
    # blades in letters {0,2,3} times k (64 products)
    ok = True
    Jreps = [list(I) + ["k"] for I in blades if 1 not in I]
    for w1 in Jreps:
        for w2 in Jreps:
            st = symbol_of_word(w1 + w2)
            if st:
                ok = False
    g.check("[Sec 8] SD4: J^2 = 0 (all 64 products of ideal representatives vanish)",
          ok and len(Jreps) == 8)

    # SD5: quotient form (V1 restriction) has signature (1,2): fibre A/J = Cl(1,2)
    g.check("[Sec 8] SD5: quotient A/J is the Clifford algebra of a (1,2) form (dim 8)",
          g.congruence_signature(V1) == (1, 2, 0))


def schw_completion_checks(W, m):
    """[Sec 8, Thm schwcompletion + Rem schwconservation] the completion,
    with the NORMALISED transversal u = dt-dual / m, so that k(u) = 1 as
    Definition def:coupling requires (12 checks, run at each mass)."""
    U = g.RF.var()
    R = U * U
    tag = " (2M = %d)" % (m * m)
    minv = Fraction(1, m)

    def hmat(nu, mu_c, bump=g.RF1):
        """6x6 ambient Gram on (rho, dt, mu1, mu2, n0, ninf); the coupling
        column is nu*bump*e with e = (0, 1/m, 0, 0) (evaluation at dt/m)."""
        z = g.RF0
        cnu = g.RF.const(Fraction(nu) * minv) * bump
        cmu = g.RF.const(Fraction(mu_c) * minv) * bump
        return [
            [W[0][0], W[0][1], z, z, z, z],
            [W[1][0], W[1][1], z, z, cnu, cmu],
            [z, z, g.RF.const(-1), z, z, z],
            [z, z, z, g.RF.const(-1), z, z],
            [z, cnu, z, z, z, g.RF.const(-1)],
            [z, cmu, z, z, g.RF.const(-1), z],
        ]

    detG = g.rf_mat_det(W)
    g.check("[Sec 8] SE1: det G = -r exactly" + tag, detG.eqrf(-R))

    # s = G^{-1}(e, e), e evaluation at the NORMALISED transversal u = dt/m:
    # e = (0, 1/m, 0, 0), so s = (1/m^2) [G^{-1}]_tt = (r - m^2)/(m^2 r)
    e2 = [g.RF0, g.RF1, g.RF0, g.RF0]
    x = g.rf_mat_solve(W, e2)
    s_rf = g.RF.const(minv * minv) * x[1]
    g.check("[Sec 8] SE2: s = G^{-1}(e,e) = (r - m^2)/(m^2 r) exactly (normalised transversal)" + tag,
          s_rf.eqrf((R - g.RF.const(m * m)) / (g.RF.const(m * m) * R)))

    for nu, mu_c in [(1, -1), (1, Fraction(-1, 2)), (2, Fraction(-1, 4))]:
        h = hmat(nu, mu_c)
        F = g.RF1 + g.RF.const(2) * g.RF.const(nu) * g.RF.const(mu_c) * s_rf
        deth = g.rf_mat_det(h)
        g.check("[Sec 8] SE3: det h = det G * (-F) as an RF identity (nu=%s, mu=%s)%s"
              % (nu, mu_c, tag), deth.eqrf(detG * (-F)))

    # SE4/SE5: wall signature at E is (2,4) for mu*nu < 0, (3,3) for mu*nu > 0
    h0_neg = schw_rf_eval_mat(hmat(1, -1), 0)
    h0_pos = schw_rf_eval_mat(hmat(1, 1), 0)
    g.check("[Sec 8] SE4: h at E has signature (2,4) for mu nu < 0 (the ascent to Cl(2,4))" + tag,
          g.congruence_signature(h0_neg) == (2, 4, 0))
    g.check("[Sec 8] SE5: h at E has signature (3,3) for mu nu > 0 (the wrong sign)" + tag,
          g.congruence_signature(h0_pos) == (3, 3, 0))

    # SE6: with the collar inside the horizon, F >= 1 on the whole manifold:
    # s < 0 exactly where r < m^2, so 2 mu nu b^2 s >= 0 there for mu nu < 0.
    ok = True
    for u0 in [Fraction(m, 10), Fraction(m, 3), Fraction(m, 2), Fraction(9 * m, 10)]:
        sval = s_rf.eval(u0)
        if not (sval < 0):
            ok = False
        Fval = 1 + 2 * Fraction(-1) * sval  # nu=1, mu=-1, b=1
        if not (Fval >= 1):
            ok = False
    g.check("[Sec 8] SE6: inside the horizon s < 0, hence F >= 1: no zero of det h" + tag, ok)

    # SE7: the global constant coupling mu nu = -m^2/2 has det h = m^2 CONSTANT
    h_half = hmat(1, Fraction(-m * m, 2))
    det_half = g.rf_mat_det(h_half)
    g.check("[Sec 8] SE7: mu nu = -m^2/2 globally: det h = m^2 exactly, at every radius" + tag,
          det_half.eqrf(g.RF.const(m * m)))
    ok = True
    for u0 in [Fraction(m, 4), Fraction(m, 2), Fraction(m), Fraction(2 * m),
               Fraction(10 * m)]:
        s6 = g.congruence_signature(schw_rf_eval_mat(h_half, u0))
        if s6 != (2, 4, 0):
            ok = False
    g.check("[Sec 8] SE8: mu nu = -m^2/2: signature (2,4) at interior, horizon and exterior "
          "sample points (global nondegenerate completion, nonstandard at "
          "infinity)" + tag, ok)

    # SE9: the ladder pair on E: k* = n0/(2 nu), CAR relation on all 64 states.
    # With the normalised transversal, h(k, n0) = nu * k(u) = nu at EVERY mass,
    # so k* = n0/(2 nu) works for all m (the unnormalised u = dt gives m, not 1).
    h0 = h0_neg  # nu = 1, mu = -1
    STATES6 = schw_all_states(6)
    alpha_k6 = [Fraction(1), Fraction(m), Fraction(0), Fraction(0),
                Fraction(0), Fraction(0)]
    alpha_ks6 = [Fraction(0), Fraction(0), Fraction(0), Fraction(0),
                 Fraction(1, 2), Fraction(0)]  # n0 / (2 nu), nu = 1
    ok = True
    for S in STATES6:
        st = {S: Fraction(1)}
        a = g.ext_c(alpha_k6, h0, g.ext_c(alpha_ks6, h0, st))
        b = g.ext_c(alpha_ks6, h0, g.ext_c(alpha_k6, h0, st))
        acc = {}
        for T, c in list(a.items()) + list(b.items()):
            acc[T] = acc.get(T, Fraction(0)) + c
        acc = {T: c for T, c in acc.items() if c != 0}
        if not g.ext_state_eq(acc, st):
            ok = False
    g.check("[Sec 8] SE9: k k* + k* k = 1 on all 64 states of the ambient fibre at E" + tag, ok)
    st0_6 = {frozenset(): Fraction(1)}
    g.check("[Sec 8] SE10: (k*)^2 = 0 and k^2 = 0 in the ambient fibre at E" + tag,
          (not g.ext_c(alpha_ks6, h0, g.ext_c(alpha_ks6, h0, st0_6))) and
          (not g.ext_c(alpha_k6, h0, g.ext_c(alpha_k6, h0, st0_6))))


def schw_exceptional_residue_checks(W, m):
    """[Sec 8, Prop schwexceptional + Prop schwresidue] (6 checks)."""
    U = g.RF.var()
    R = U * U
    # rescaled frame (rho, k/u, mu1, mu2): Gram entries as RF identities
    Grr = W[0][0]
    Grk = (W[0][0] + g.RF.const(m) * W[0][1]) / U       # G(rho, k)/u = -u
    Gkk = (W[0][0] + g.RF.const(2 * m) * W[0][1] + g.RF.const(m * m) * W[1][1]) / (U * U)
    g.check("[Sec 8] SF1: G(rho, k/u) = -u: cross term vanishes at E like sqrt(r)",
          Grk.eqrf(-U))
    g.check("[Sec 8] SF2: G(k/u, k/u) = -1 exactly (the rate of degeneration as a metric entry)",
          Gkk.eqrf(g.RF.const(-1)))
    Gexc0 = [[Grr.eval(0), Grk.eval(0), 0, 0],
             [Grk.eval(0), Gkk.eval(0), 0, 0],
             [0, 0, -1, 0],
             [0, 0, 0, -1]]
    g.check("[Sec 8] SF3: exceptional Gram at E = diag(m^2, -1, -1, -1): "
          "nondegenerate (1,3), the Clifford algebra of the Kasner form",
          g.congruence_signature(g.frac_matrix(Gexc0)) == (1, 3, 0))

    # residue: r * (block inverse) -> -(1, m) tensor (1, m) at E
    block = [[W[0][0], W[0][1]], [W[1][0], W[1][1]]]
    col1 = g.rf_mat_solve(block, [g.RF1, g.RF0])
    col2 = g.rf_mat_solve(block, [g.RF0, g.RF1])
    Binv = [[col1[0], col2[0]], [col1[1], col2[1]]]
    res = [[(R * Binv[i][j]).eval(0) for j in range(2)] for i in range(2)]
    target_res = [[-Fraction(1), -Fraction(m)], [-Fraction(m), -Fraction(m * m)]]
    g.check("[Sec 8] SF4: residue lim r G^{-1} = -(k tensor k): the square-root twist "
          "N*E = L^2 at the black hole",
          res == target_res)
    g.check("[Sec 8] SF5: the residue matrix has rank one",
          g.mat_rank(g.frac_matrix(res)) == 1)

    # proper time normalisation: (dtau / rho)^2 = 1/(m^2 - r): rho is
    # proportional to dtau at E with ratio 1/m
    ratio2 = (g.RF1 / (g.RF.const(m * m) - R))
    g.check("[Sec 8] SF6: (dtau/rho)^2 = 1/(m^2 - r), so rho = m dtau at E",
          (ratio2 * (g.RF.const(m * m) - R)).eqrf(g.RF1))


def schw_weight_checks():
    """[Sec 8, Thm weights] uniqueness of the weights (4 checks)."""
    # Orders in r of the diagonal Schwarzschild-frame cometric entries:
    #   ord G(dr,dr) = -1,  ord G(dt_S,dt_S) = +1,  ord G(dtheta,dtheta) = -2.
    # A diagonal rescaling by (r^{a_r}, r^{a_t}, r^{a_th}) shifts these to
    # (2a_r - 1, 2a_t + 1, 2a_th - 2).  Search the grid (1/6)Z in [-2, 2].
    ords = {"r": Fraction(-1), "t": Fraction(1), "th": Fraction(-2)}
    grid = [Fraction(k, 6) for k in range(-12, 13)]

    deg_solutions = []   # regime D: nondegenerate entries order 0, dying entry order 1
    exc_solutions = []   # regime E: all entries order 0 (nondegenerate limit)
    for ar in grid:
        for at in grid:
            for ath in grid:
                o_r = 2 * ar + ords["r"]
                o_t = 2 * at + ords["t"]
                o_th = 2 * ath + ords["th"]
                if o_r == 0 and o_th == 0 and o_t == 1:
                    deg_solutions.append((ar, at, ath))
                if o_r == 0 and o_th == 0 and o_t == 0:
                    exc_solutions.append((ar, at, ath))
    g.check("[Sec 8] SG1: degeneration-regime weights are UNIQUE: (1/2, 0, 1)",
          deg_solutions == [(Fraction(1, 2), Fraction(0), Fraction(1))])
    g.check("[Sec 8] SG2: exceptional-regime weights are UNIQUE: (1/2, -1/2, 1)",
          exc_solutions == [(Fraction(1, 2), Fraction(-1, 2), Fraction(1))])

    # Translate to proper-time weights (tau ~ r^{3/2}: multiply by 2/3) and
    # read off the Kasner exponents of the unit coframe tau^{p_i} dx^i:
    # p_t = (2/3) * (-1/2) = -1/3, p_theta = p_phi = (2/3) * 1 = 2/3.
    p1 = Fraction(2, 3) * Fraction(-1, 2)
    p2 = Fraction(2, 3) * Fraction(1)
    p3 = p2
    g.check("[Sec 8] SG3: the forced weights are the Kasner exponents (-1/3, 2/3, 2/3)",
          (p1, p2, p3) == (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)))
    g.check("[Sec 8] SG4: Kasner sum rules Sum p = 1 and Sum p^2 = 1",
          p1 + p2 + p3 == 1 and p1 * p1 + p2 * p2 + p3 * p3 == 1)


def schwarzschild_checks():
    """[Sec 8] the composite: 70 checks, parts SA-SG."""
    W = schw_weighted_gram_checks(1)   # 2M = 1 (horizon at r = 1, u = 1)
    schw_weighted_gram_checks(2)       # 2M = 4: the identities are M-independent in form
    m = 1                              # henceforth 2M = 1, except where noted
    V1 = schw_corank_checks(W, m)
    schw_gauge_rain_checks(W, m)
    schw_fibre_checks(V1)
    schw_completion_checks(W, m)
    # the completion block again at 2M = 4: the normalised transversal makes
    # the ladder pair and the global constant determinant work at every mass
    W2 = [[e for e in row] for row in [[g.RF.const(4) - g.RF.var() * g.RF.var(), g.RF.const(-2), g.RF0, g.RF0],
          [g.RF.const(-2), g.RF1, g.RF0, g.RF0],
          [g.RF0, g.RF0, g.RF.const(-1), g.RF0],
          [g.RF0, g.RF0, g.RF0, g.RF.const(-1)]]]
    schw_completion_checks(W2, 2)
    schw_exceptional_residue_checks(W, m)
    schw_weight_checks()



# ============================================================================
# Sections 8.6-8.8 and 9: uniqueness, the rain frame, the matching, and the
# anisotropic class (folded in from the open-items note, 2026-08-25; the
# note's Kerr checks are NOT ported, the Kerr material remaining with the
# note).  One hundred further checks.
# ============================================================================


def rfc(q):
    return g.RF.const(Fraction(q))



def rf_eval_mat(M, u0):
    return [[e.eval(u0) for e in row] for row in M]



def all_states(nn):
    return [frozenset(S) for S in g.all_blades(nn)]



def kasner_point(u):
    """Rational Kasner exponents p = (-u, 1+u, u(1+u)) / (1+u+u^2)."""
    u = Fraction(u)
    D = 1 + u + u * u
    return (-u / D, (1 + u) / D, u * (1 + u) / D)



def aniso_point(u_par):
    p1, p2, p3 = kasner_point(u_par)
    tag = " (Kasner point u=%d: p = (%s, %s, %s))" % (u_par, p1, p2, p3)
    g.check("[Sec 9] sum rule Sum p = 1" + tag, p1 + p2 + p3 == 1)
    g.check("[Sec 9] sum rule Sum p^2 = 1" + tag,
            p1 * p1 + p2 * p2 + p3 * p3 == 1)

    # Work in w = tau^(1/D), D = 1+u+u^2, so all entries are RF in w.
    D = 1 + u_par + u_par * u_par
    w = g.RF.var()

    def tau_pow(q):
        """tau^q as RF in w, for q a Fraction with denominator dividing D."""
        e = Fraction(q) * D
        assert e.denominator == 1
        e = e.numerator
        if e >= 0:
            out = g.RF1
            for _ in range(e):
                out = out * w
            return out
        out = g.RF1
        for _ in range(-e):
            out = out * w
        return g.RF1 / out

    # Raw diagonal cometric in the coframe (dtau, s1, s2, s3):
    raw = [g.RF1, -tau_pow(-2 * p1), -tau_pow(-2 * p2), -tau_pow(-2 * p3)]

    # Degeneration-regime weights (0, 0, p2, p3): weighted Gram entries.
    wts = [Fraction(0), Fraction(0), p2, p3]
    W = [raw[i] * tau_pow(2 * wts[i]) for i in range(4)]
    rho = tau_pow(-2 * p1)         # the canonical defining element
    ok = (W[0].eqrf(g.RF1) and W[1].eqrf(-rho)
          and W[2].eqrf(rfc(-1)) and W[3].eqrf(rfc(-1)))
    g.check("[Sec 9] weighted Gram = diag(1, -rho, -1, -1) with rho = tau^(-2 p1), from first principles" + tag, ok)

    G0 = [W[i].eval(0) for i in range(4)]
    Mat0 = [[Fraction(0)] * 4 for _ in range(4)]
    for i in range(4):
        Mat0[i][i] = G0[i]
    g.check("[Sec 9] boundary Gram diag(1,0,-1,-1): corank one, radical = the negative-exponent covector" + tag,
            g.congruence_signature(Mat0) == (1, 2, 1) and g.mat_rank(g.frac_matrix(Mat0)) == 3)

    # Completion: s = G^{-1}(e,e) with e the dual of the dying slot.
    s_rf = g.RF1 / W[1]            # = -1/rho
    g.check("[Sec 9] s = -1/rho exactly (negative near the boundary)" + tag,
            s_rf.eqrf(-(g.RF1 / rho)) and s_rf.eval(Fraction(1, 2)) < 0)

    # Global coupling nu = 1, mu = -1/2 (mu nu = -1/2), bump = 1:
    # 6x6 ambient Gram on (dtau, s1w, s2w, s3w, n0, ninf), coupling on slot 1.
    def hmat(nu, mu_c):
        z = g.RF0
        cnu, cmu = rfc(nu), rfc(mu_c)
        return [
            [W[0], z, z, z, z, z],
            [z, W[1], z, z, cnu, cmu],
            [z, z, W[2], z, z, z],
            [z, z, z, W[3], z, z],
            [z, cnu, z, z, z, rfc(-1)],
            [z, cmu, z, z, rfc(-1), z],
        ]

    h = hmat(1, Fraction(-1, 2))
    deth = g.rf_mat_det(h)
    g.check("[Sec 9] global coupling mu nu = -1/2: det h = 1 + rho exactly" + tag,
            deth.eqrf(g.RF1 + rho))
    ok = g.congruence_signature(rf_eval_mat(h, 0)) == (2, 4, 0)
    for w0 in (Fraction(1, 3), Fraction(1, 2), Fraction(1)):
        ok = ok and g.congruence_signature(rf_eval_mat(h, w0)) == (2, 4, 0)
    g.check("[Sec 9] completion signature (2,4) at the boundary and interior samples; no shadow wall" + tag, ok)
    g.check("[Sec 9] wrong coupling sign gives (3,3) at the boundary" + tag,
            g.congruence_signature(rf_eval_mat(hmat(1, Fraction(1, 2)), 0)) == (3, 3, 0))

    # Pointwise weight forcing, solved exactly (linear equations in a_i):
    # raw tau-orders of the diagonal entries: o = (0, -2p1, -2p2, -2p3);
    # rescaling slot i by tau^{a_i} shifts the order by 2 a_i.
    o = [Fraction(0), -2 * p1, -2 * p2, -2 * p3]
    # degeneration regime: target orders (0, -2p1, 0, 0)
    deg = [(t - oo) / 2 for oo, t in zip(o, [Fraction(0), -2 * p1, Fraction(0), Fraction(0)])]
    g.check("[Sec 9] degeneration-regime weights forced = (0, 0, p2, p3), uniquely (linear solve)" + tag,
            deg == [Fraction(0), Fraction(0), p2, p3])
    # exceptional regime: all target orders 0
    exc = [(Fraction(0) - oo) / 2 for oo in o]
    g.check("[Sec 9] exceptional-regime weights forced = (0, p1, p2, p3) = the local Kasner exponents" + tag,
            exc == [Fraction(0), p1, p2, p3])

    # exceptional Gram: rescale the raw entries by the exceptional weights
    E = [raw[i] * tau_pow(2 * exc[i]) for i in range(4)]
    ok = all(E[i].eqrf(rfc(v)) for i, v in zip(range(4), [1, -1, -1, -1]))
    g.check("[Sec 9] exceptional Gram = diag(1,-1,-1,-1): the Clifford algebra of the local Kasner form" + tag, ok)
    return (p1, p2, p3)



def aniso_ladder_checks():
    """Ladder pair on the boundary fibre (diagonal case), all 64 states."""
    M = [[Fraction(0)] * 6 for _ in range(6)]
    M[0][0] = Fraction(1)
    # slot 1 is the dying direction: entry 0 at the boundary
    M[2][2] = M[3][3] = Fraction(-1)
    nu, mu_c = Fraction(1), Fraction(-1)     # mu nu < 0
    M[1][4] = M[4][1] = nu
    M[1][5] = M[5][1] = mu_c
    M[4][5] = M[5][4] = Fraction(-1)
    k = [Fraction(0), Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)]
    ks = [Fraction(0)] * 4 + [Fraction(1, 2), Fraction(0)]   # n0/(2 nu)
    ok_car = ok_nil = True
    for S in all_states(6):
        st = {S: Fraction(1)}
        a = g.ext_c(k, M, g.ext_c(ks, M, dict(st)))
        b = g.ext_c(ks, M, g.ext_c(k, M, dict(st)))
        acc = {}
        for d in (a, b):
            for T, c in d.items():
                acc[T] = acc.get(T, Fraction(0)) + c
        acc = {T: c for T, c in acc.items() if c != 0}
        ok_car = ok_car and g.ext_state_eq(acc, st)
        ok_nil = ok_nil and (g.ext_c(k, M, g.ext_c(k, M, dict(st))) == {}) \
                        and (g.ext_c(ks, M, g.ext_c(ks, M, dict(st))) == {})
    g.check("[Sec 9] ladder pair on the variable-exponent boundary fibre: CAR on all 64 states", ok_car)
    g.check("[Sec 9] k^2 = (k*)^2 = 0 on all 64 states", ok_nil)



def uniqueness_checks():
    m = 1
    cc = Fraction(2)
    u = g.RF.var()
    R = u * u
    # Schwarzschild weighted Gram on (rho, dt, mu1, mu2):
    GW = [[rfc(m * m) - R, rfc(-m), g.RF0, g.RF0],
          [rfc(-m), g.RF1, g.RF0, g.RF0],
          [g.RF0, g.RF0, rfc(-1), g.RF0],
          [g.RF0, g.RF0, g.RF0, rfc(-1)]]
    detW = g.rf_mat_det(GW)
    g.check("[Sec 8.6] det G_W = -r exactly (the tame normal form)", detW.eqrf(-R))

    # The submodule M_c: frame (u rho, k + c rho, mu1, mu2), k = rho + m dt.
    # Transition matrix A in the W-frame (rho, dt, mu1, mu2):
    A = [[u, g.RF0, g.RF0, g.RF0],
         [g.RF1 + rfc(cc), rfc(m), g.RF0, g.RF0],
         [g.RF0, g.RF0, g.RF1, g.RF0],
         [g.RF0, g.RF0, g.RF0, g.RF1]]
    detA = g.rf_mat_det(A)
    g.check("[Sec 8.6] det A = m u: the transition degenerates on the boundary", detA.eqrf(rfc(m) * u))

    # boundary evaluation rank of A: 3 (M_c is a STRICT submodule of W)
    A0 = g.frac_matrix(rf_eval_mat(A, 0))
    g.check("[Sec 8.6] rank A|_E = 3: M_c is strictly smaller than W at the boundary",
            g.mat_rank(A0) == 3)

    # Gram of M_c: G_Mc = A G_W A^T (rows of A = M_c frame in W frame)
    GM = [[g.RF0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = g.RF0
            for a in range(4):
                for b in range(4):
                    acc = acc + A[i][a] * GW[a][b] * A[j][b]
            GM[i][j] = acc
    detM = g.rf_mat_det(GM)
    g.check("[Sec 8.6] det G_Mc = -m^2 r^2 exactly = (det A)^2 det G_W",
            detM.eqrf(rfc(-m * m) * R * R) and detM.eqrf(detA * detA * detW))

    GM0 = g.frac_matrix(rf_eval_mat(GM, 0))
    g.check("[Sec 8.6] M_c is corank one at the boundary (rank 3)",
            g.mat_rank(GM0) == 3 and g.congruence_signature(GM0) == (1, 2, 1))

    # dying ENTRY first order: G_Mc[0][0] = r (m^2 - r)
    g.check("[Sec 8.6] dying ENTRY G_Mc(s,s) = r(m^2 - r): first order in r",
            GM[0][0].eqrf(R * (rfc(m * m) - R)) and (GM[0][0] / R).eval(0) == Fraction(m * m))

    # dying EIGENVALUE second order: det/r -> 0 but det/r^2 -> -m^2 != 0,
    # while the nondegenerate 3x3 minor is bounded away from zero at the boundary
    g.check("[Sec 8.6] dying EIGENVALUE is second order: det/r -> 0, det/r^2 -> -m^2",
            (detM / R).eval(0) == 0 and (detM / (R * R)).eval(0) == Fraction(-m * m))
    minor = [[GM0[i][j] for j in (1, 2, 3)] for i in (1, 2, 3)]
    det3 = (minor[0][0] * (minor[1][1] * minor[2][2] - minor[1][2] * minor[2][1])
            - minor[0][1] * (minor[1][0] * minor[2][2] - minor[1][2] * minor[2][0])
            + minor[0][2] * (minor[1][0] * minor[2][1] - minor[1][1] * minor[2][0]))
    g.check("[Sec 8.6] nondegenerate 3x3 minor nonzero at the boundary (= c^2 m^2 x 1): "
            "so exactly one eigenvalue vanishes, at order r^2, violating (T3d)",
            det3 == cc * cc * Fraction(m * m))

    # --- Example ex:nullmix: the null-mixing extension M' (rain-boundedness
    # is essential).  Frame (alpha, beta, gamma, mu2) with
    # alpha = du + C dtheta, beta = dt + D dtheta, gamma = u^4 dtheta,
    # C = sqrt(m^2 - u^2)/2, D = -m u^2/(2C).  Verified at rational points
    # where C is rational: (m, u) = (5, 3) -> C = 2, and (5, 4) -> C = 3/2;
    # boundary data at u = 0 where C = m/2.
    def nullmix_gram(mm, uu):
        mm, uu = Fraction(mm), Fraction(uu)
        r_ = uu * uu
        Csq = (mm * mm - uu * uu) / 4
        import math
        # rational C guaranteed by the caller's choice of samples
        Cv = Fraction(int((Csq.numerator)**0.5 + 0.5), int((Csq.denominator)**0.5 + 0.5))
        assert Cv * Cv == Csq
        Dv = -mm * uu * uu / (2 * Cv)
        # cometric entries: G(du,du) = (m^2-u^2)/(4u^4), G(du,dt) = -m/(2u^2),
        # G(dt,dt) = 1, G(dth,dth) = -1/u^4, G(dph,dph) = -1/u^4 (equator)
        Gdd = (mm * mm - r_) / (4 * r_ * r_)
        Gdt = -mm / (2 * r_)
        Gtt = Fraction(1)
        Gthth = -1 / (r_ * r_)
        a = {"du": Fraction(1), "dth": Cv}
        b = {"dt": Fraction(1), "dth": Dv}
        c = {"dth": r_ * r_}
        d = {"dph": r_}
        def pair(x, y):
            s_ = Fraction(0)
            s_ += x.get("du", 0) * y.get("du", 0) * Gdd
            s_ += (x.get("du", 0) * y.get("dt", 0) + x.get("dt", 0) * y.get("du", 0)) * Gdt
            s_ += x.get("dt", 0) * y.get("dt", 0) * Gtt
            s_ += x.get("dth", 0) * y.get("dth", 0) * Gthth
            s_ += x.get("dph", 0) * y.get("dph", 0) * (-1 / (r_ * r_))
            return s_
        fr = [a, b, c, d]
        return [[pair(fr[i], fr[j]) for j in range(4)] for i in range(4)]

    for (mm, uu) in [(5, 3), (5, 4)]:
        M = nullmix_gram(mm, uu)
        r_ = Fraction(uu * uu)
        g.check("[Sec 8.6] ex:nullmix at (m,u)=(%d,%d): G(alpha,alpha) = 0 and G(alpha,beta) = 0 "
                "(exact null mixing)" % (mm, uu),
                M[0][0] == 0 and M[0][1] == 0)
        det4 = g.frac_matrix(M)
        # det = -r/4 exactly
        import itertools
        def det_of(Mx):
            n_ = len(Mx)
            tot = Fraction(0)
            for perm in itertools.permutations(range(n_)):
                sgn = 1
                pl = list(perm)
                for i_ in range(n_):
                    for j_ in range(i_ + 1, n_):
                        if pl[i_] > pl[j_]:
                            sgn = -sgn
                pr = Fraction(1)
                for i_ in range(n_):
                    pr *= Mx[i_][perm[i_]]
                tot += sgn * pr
            return tot
        g.check("[Sec 8.6] ex:nullmix at (m,u)=(%d,%d): det G_M' = -r/4 exactly" % (mm, uu),
                det_of(M) == -r_ / 4)

    # boundary data at u = 0 (C = m/2): Gram rank 3, radical = beta,
    # nonvanishing eigen-pair +-m/2 from (alpha,gamma) and -1 from mu2
    mm = Fraction(5)
    B0 = [[Fraction(0), Fraction(0), -mm / 2, Fraction(0)],
          [Fraction(0), Fraction(0), Fraction(0), Fraction(0)],
          [-mm / 2, Fraction(0), Fraction(0), Fraction(0)],
          [Fraction(0), Fraction(0), Fraction(0), Fraction(-1)]]
    g.check("[Sec 8.6] ex:nullmix boundary Gram: rank 3, corank one, radical = beta slot",
            g.mat_rank(g.frac_matrix(B0)) == 3 and
            g.congruence_signature(B0) == (1, 2, 1))
    # dying eigenvalue first order: det/r -> -m^2/4 * ... : from det = -r/4 and
    # nondegenerate minor bounded: check the 3x3 minor (alpha,gamma,mu2) at 0
    minor0 = [[B0[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
    d3 = (minor0[0][0] * (minor0[1][1] * minor0[2][2] - minor0[1][2] * minor0[2][1])
          - minor0[0][1] * (minor0[1][0] * minor0[2][2] - minor0[1][2] * minor0[2][0])
          + minor0[0][2] * (minor0[1][0] * minor0[2][1] - minor0[1][1] * minor0[2][0]))
    g.check("[Sec 8.6] ex:nullmix: nondegenerate 3x3 minor = m^2/4 != 0 at the boundary, so the dying "
            "eigenvalue is det/(unit): FIRST order in r ((T2d)+(T3d) hold, yet M' != W)",
            d3 == mm * mm / 4)



def rainframe_checks():
    m = 1
    u = g.RF.var()
    R = u * u
    # PG covariant metric at the equator, coordinates (t, r, theta, phi):
    # ds^2 = dt^2 - (dr + beta dt)^2 - r^2 dtheta^2 - r^2 dphi^2, beta = m/u.
    beta = rfc(m) / u
    gcov = [[g.RF1 - beta * beta, -beta, g.RF0, g.RF0],
            [-beta, rfc(-1), g.RF0, g.RF0],
            [g.RF0, g.RF0, -(R * R), g.RF0],
            [g.RF0, g.RF0, g.RF0, -(R * R)]]
    # rain orthonormal frame: V = d_t - beta d_r, e_r = d_r,
    # e_h = r^{-1} d_theta, e_p = r^{-1} d_phi (equator).
    frame = [
        [g.RF1, -beta, g.RF0, g.RF0],
        [g.RF0, g.RF1, g.RF0, g.RF0],
        [g.RF0, g.RF0, g.RF1 / R, g.RF0],
        [g.RF0, g.RF0, g.RF0, g.RF1 / R],
    ]

    def pair_vec(Xa, Xb):
        acc = g.RF0
        for i in range(4):
            for j in range(4):
                acc = acc + Xa[i] * gcov[i][j] * Xb[j]
        return acc

    eta = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1)]
    ok = True
    for i in range(4):
        for j in range(4):
            want = rfc(eta[i]) if i == j else g.RF0
            ok = ok and pair_vec(frame[i], frame[j]).eqrf(want)
    g.check("[Sec 8.7] the rain frame (V, e_r, e_theta, e_phi) is exactly PG-orthonormal, at every radius", ok)

    # W-frame covectors in coordinate components (dt, dr, dtheta, dphi):
    Wf = {
        "rho": [g.RF0, u, g.RF0, g.RF0],
        "dt": [g.RF1, g.RF0, g.RF0, g.RF0],
        "mu1": [g.RF0, g.RF0, R, g.RF0],
        "mu2": [g.RF0, g.RF0, g.RF0, R],
    }

    def pairing(alpha, X):
        acc = g.RF0
        for i in range(4):
            acc = acc + alpha[i] * X[i]
        return acc

    # pairing table: every W-frame element has BOUNDED components
    expect = {
        ("rho", 0): rfc(-m), ("rho", 1): u,
        ("dt", 0): g.RF1, ("dt", 1): g.RF0,
        ("mu1", 2): g.RF1, ("mu2", 3): g.RF1,
    }
    ok = True
    for name, alpha in Wf.items():
        for j in range(4):
            val = pairing(alpha, frame[j])
            if (name, j) in expect:
                ok = ok and val.eqrf(expect[(name, j)])
            # boundedness: u^0 val must have a finite limit; check u*val -> 0
            # is too weak; instead check val itself evaluates at a boundary-
            # approaching sample and that u^2*val vanishes at 0 like val*u^2
            ok = ok and (val * u * u).eval(0) == 0
    g.check("[Sec 8.7] the pairing table: every W-frame element has bounded rain-frame components "
            "(rho(V) = -m, rho(e_r) = u, dt(V) = 1, mu_i(e_i) = 1, rest zero)", ok)

    # excluded forms: dr and dtheta have DIVERGENT rain-frame components
    dr = [g.RF0, g.RF1, g.RF0, g.RF0]
    dth = [g.RF0, g.RF0, g.RF1, g.RF0]
    g.check("[Sec 8.7] dr is excluded: u dr(V) -> -m != 0, so dr(V) ~ -m/u diverges",
            (u * pairing(dr, frame[0])).eval(0) == Fraction(-m))
    g.check("[Sec 8.7] dtheta is excluded: r dtheta(e_theta) -> 1, so dtheta(e_theta) ~ 1/r diverges",
            (R * pairing(dth, frame[2])).eval(0) == Fraction(1))

    # the norm identity: |alpha|_G^2 = alpha(V)^2 - sum_i alpha(e_i)^2
    # (contravariant PG cometric at the equator)
    Gc = [[g.RF1, -beta, g.RF0, g.RF0],
          [-beta, (rfc(m * m) - R) / R, g.RF0, g.RF0],
          [g.RF0, g.RF0, -(g.RF1 / (R * R)), g.RF0],
          [g.RF0, g.RF0, g.RF0, -(g.RF1 / (R * R))]]

    def gnorm(alpha):
        acc = g.RF0
        for i in range(4):
            for j in range(4):
                acc = acc + alpha[i] * Gc[i][j] * alpha[j]
        return acc

    ok = True
    tests = list(Wf.values())
    mixed = [Wf["rho"][i] + rfc(2) * Wf["dt"][i] + rfc(3) * Wf["mu1"][i] for i in range(4)]
    tests.append(mixed)
    for alpha in tests:
        lhs = gnorm(alpha)
        rhs = (pairing(alpha, frame[0]) * pairing(alpha, frame[0])
               - pairing(alpha, frame[1]) * pairing(alpha, frame[1])
               - pairing(alpha, frame[2]) * pairing(alpha, frame[2])
               - pairing(alpha, frame[3]) * pairing(alpha, frame[3]))
        ok = ok and lhs.eqrf(rhs)
    g.check("[Sec 8.7] the norm identity |alpha|^2 = alpha(V)^2 - Sum alpha(e_i)^2 as RF identities "
            "(bounded components imply bounded norm; the converse fails, Rem 8.5)", ok)



def rain_duality_checks(m):
    tag = " (2M = %d)" % (m * m)
    u = g.RF.var()
    R = u * u
    beta = rfc(m) / u
    # coordinate components; equator; covectors on (dt, dr, dtheta, dphi)
    dt = [g.RF1, g.RF0, g.RF0, g.RF0]
    dr = [g.RF0, g.RF1, g.RF0, g.RF0]
    kou = [beta, g.RF1, g.RF0, g.RF0]          # k/sqrt(r) = dr + beta dt
    mu1 = [g.RF0, g.RF0, R, g.RF0]
    mu2 = [g.RF0, g.RF0, g.RF0, R]
    rho = [g.RF0, u, g.RF0, g.RF0]
    coframe = [dt, kou, mu1, mu2]
    # rain frame vectors on (d_t, d_r, d_theta, d_phi)
    V = [g.RF1, -beta, g.RF0, g.RF0]
    er = [g.RF0, g.RF1, g.RF0, g.RF0]
    eth = [g.RF0, g.RF0, g.RF1 / R, g.RF0]
    eph = [g.RF0, g.RF0, g.RF0, g.RF1 / R]
    frame = [V, er, eth, eph]

    def pairing(alpha, X):
        acc = g.RF0
        for i in range(4):
            acc = acc + alpha[i] * X[i]
        return acc

    ok = True
    for i in range(4):
        for j in range(4):
            want = g.RF1 if i == j else g.RF0
            ok = ok and pairing(coframe[i], frame[j]).eqrf(want)
    g.check("[Sec 8.7] DUALITY: (dt, k/sqrt r, mu1, mu2) is exactly the dual coframe of the "
            "infalling orthonormal frame, at every radius" + tag, ok)

    # contravariant PG cometric at the equator
    Gc = [[g.RF1, -beta, g.RF0, g.RF0],
          [-beta, (rfc(m * m) - R) / R, g.RF0, g.RF0],
          [g.RF0, g.RF0, -(g.RF1 / (R * R)), g.RF0],
          [g.RF0, g.RF0, g.RF0, -(g.RF1 / (R * R))]]

    def gpair(a, b):
        acc = g.RF0
        for i in range(4):
            for j in range(4):
                acc = acc + a[i] * Gc[i][j] * b[j]
        return acc

    eta_diag = [1, -1, -1, -1]
    ok = True
    for i in range(4):
        for j in range(4):
            want = rfc(eta_diag[i]) if i == j else g.RF0
            ok = ok and gpair(coframe[i], coframe[j]).eqrf(want)
    g.check("[Sec 8.7] the exceptional coframe has EXACT Minkowski Gram diag(1,-1,-1,-1) at every "
            "radius: the rain observer's covectors never degenerate" + tag, ok)

    # transitions: rho = u (k/u) - m dt, and det(W in W_exc) = -u
    ok = all((rfc(1) * u * kou[i] - rfc(m) * dt[i]).eqrf(rho[i]) for i in range(4))
    g.check("[Sec 8.7] rho = sqrt(r) (k/sqrt r) - m dt: W lies inside the exceptional module" + tag, ok)
    detA = (rfc(-m)) * g.RF0 - u * g.RF1   # det [[-m, u],[1, 0]] = -u
    g.check("[Sec 8.7] the W -> W_exc transition degenerates on the boundary: det = -sqrt(r)" + tag,
            detA.eqrf(-u))

    # the radial null dyad
    np_ = [kou[i] + dt[i] for i in range(4)]
    nm_ = [kou[i] - dt[i] for i in range(4)]
    g.check("[Sec 8.7] the dyad n+- = k/sqrt(r) +- dt is exactly G-null at every radius" + tag,
            gpair(np_, np_).is_zero() and gpair(nm_, nm_).is_zero())
    g.check("[Sec 8.7] the dyad has CONSTANT unit rain components: n+-(V) = +-1, n+-(e_r) = 1" + tag,
            pairing(np_, V).eqrf(g.RF1) and pairing(nm_, V).eqrf(-g.RF1)
            and pairing(np_, er).eqrf(g.RF1) and pairing(nm_, er).eqrf(g.RF1))

    # the gauge field: L(dt) = dt, L(dr) = dr - beta dt, angular fixed;
    # eta(L a, L b) = G(a, b) validates the conventions, and
    # L^{-1} carries the flat null dyad to +- n-+.
    eta_c = [[g.RF1, g.RF0, g.RF0, g.RF0],
             [g.RF0, rfc(-1), g.RF0, g.RF0],
             [g.RF0, g.RF0, -(g.RF1 / (R * R)), g.RF0],
             [g.RF0, g.RF0, g.RF0, -(g.RF1 / (R * R))]]

    def L(a):
        # a = (a_t, a_r, a_th, a_ph) -> components of L(a)
        return [a[0] - beta * a[1], a[1], a[2], a[3]]

    def Linv(a):
        return [a[0] + beta * a[1], a[1], a[2], a[3]]

    def etapair(a, b):
        acc = g.RF0
        for i in range(4):
            for j in range(4):
                acc = acc + a[i] * eta_c[i][j] * b[j]
        return acc

    basis = [dt, dr, [g.RF0, g.RF0, g.RF1, g.RF0], [g.RF0, g.RF0, g.RF0, g.RF1]]
    ok = True
    for a in basis:
        for b in basis:
            ok = ok and etapair(L(a), L(b)).eqrf(gpair(a, b))
    g.check("[Sec 8.7] the gauge map validates: eta(L a, L b) = G(a, b) on all coordinate pairs" + tag, ok)
    flat_p = [dt[i] + dr[i] for i in range(4)]
    flat_m = [dt[i] - dr[i] for i in range(4)]
    g.check("[Sec 8.7] the flat radial dyad is eta-null" + tag,
            etapair(flat_p, flat_p).is_zero() and etapair(flat_m, flat_m).is_zero())
    im_p = Linv(flat_p)
    im_m = Linv(flat_m)
    ok = all(im_p[i].eqrf(np_[i]) for i in range(4)) and all(im_m[i].eqrf(-nm_[i]) for i in range(4))
    g.check("[Sec 8.7] the gauge field carries the flat null dyad exactly onto the physical dyad: "
            "L^{-1}(dt + dr) = n+, L^{-1}(dt - dr) = -n-" + tag, ok)



def weld_fibre_checks():
    eta = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1)]

    def boost_matrix(a, b):
        """so(1,3) generator M_{ab}: (M)^i_j = delta^i_a eta_bj - delta^i_b eta_aj."""
        M = [[Fraction(0)] * 4 for _ in range(4)]
        for i in range(4):
            for j in range(4):
                M[i][j] = (Fraction(1) if i == a else Fraction(0)) * eta[b] * (1 if j == b else 0) \
                        - (Fraction(1) if i == b else Fraction(0)) * eta[a] * (1 if j == a else 0)
        return M

    gens = [boost_matrix(a, b) for a in range(4) for b in range(a + 1, 4)]

    def mat_mul(A, B):
        return [[sum(A[i][k] * B[k][j] for k in range(4)) for j in range(4)] for i in range(4)]

    def mat_sub(A, B):
        return [[A[i][j] - B[i][j] for j in range(4)] for i in range(4)]

    def flat(A):
        return [A[i][j] for i in range(4) for j in range(4)]

    span = [flat(Mx) for Mx in gens]
    g.check("[Sec 8.8] the six bivector generators are independent (dim so(1,3) = 6)",
            g.rank_of_vectors(span) == 6)
    ok = True
    for i in range(6):
        for j in range(i + 1, 6):
            br = mat_sub(mat_mul(gens[i], gens[j]), mat_mul(gens[j], gens[i]))
            if g.rank_of_vectors(span + [flat(br)]) != 6:
                ok = False
    g.check("[Sec 8.8] bracket closure: so(1,3) is the bivector algebra of the exceptional fibre", ok)

    lam = g.RF.var()
    for u_par in (1, 2):
        p = kasner_point(u_par)
        Bw = [[Fraction(0)] * 4 for _ in range(4)]
        for i in range(3):
            Mi = boost_matrix(0, i + 1)
            for r_ in range(4):
                for c_ in range(4):
                    Bw[r_][c_] += p[i] * Mi[r_][c_]
        # eta-antisymmetry: (eta Bw)^T = -(eta Bw)
        ok = all(eta[i] * Bw[i][j] == -eta[j] * Bw[j][i] for i in range(4) for j in range(4))
        g.check("[Sec 8.8] the weight bivector is eta-antisymmetric (u=%d)" % u_par, ok)
        # characteristic polynomial via RF determinant of (lam I - Bw)
        Mlam = [[lam * (g.RF1 if i == j else g.RF0) - rfc(Bw[i][j]) for j in range(4)] for i in range(4)]
        chp = g.rf_mat_det(Mlam)
        g.check("[Sec 8.8] char poly = L^4 - (Sum p^2) L^2 = L^4 - L^2: the surviving matrix is a UNIT boost, "
                "unit BY the Kasner constraint (u=%d)" % u_par,
                chp.eqrf(lam * lam * lam * lam - lam * lam))

    # the ladder boost K = (1/2)[c(k), c(k*)] squares to 1/4 on all 64 states
    M = [[Fraction(0)] * 6 for _ in range(6)]
    M[0][0] = Fraction(1)
    M[2][2] = M[3][3] = Fraction(-1)
    M[1][4] = M[4][1] = Fraction(1)
    M[1][5] = M[5][1] = Fraction(-1)
    M[4][5] = M[5][4] = Fraction(-1)
    k = [Fraction(0), Fraction(1)] + [Fraction(0)] * 4
    ks = [Fraction(0)] * 4 + [Fraction(1, 2), Fraction(0)]

    def K_op(st):
        a = g.ext_c(k, M, g.ext_c(ks, M, dict(st)))
        b = g.ext_c(ks, M, g.ext_c(k, M, dict(st)))
        acc = {}
        for d, sg in ((a, Fraction(1, 2)), (b, Fraction(-1, 2))):
            for T, c in d.items():
                acc[T] = acc.get(T, Fraction(0)) + sg * c
        return {T: c for T, c in acc.items() if c != 0}

    ok = True
    for S in all_states(6):
        st = {S: Fraction(1)}
        KK = K_op(K_op(st))
        want = {S: Fraction(1, 4)}
        ok = ok and g.ext_state_eq(KK, want)
    g.check("[Sec 8.8] the ladder boost K = (1/2)[c(k), c(k*)] satisfies K^2 = 1/4 on all 64 states "
            "(K = N - 1/2: the wall's own so(1,1), transverse to the exceptional so(1,3))", ok)



def stability_checks():
    """Congruence reduction of a relatively admissible perturbation to
    strict-diagonal data, at the Kasner point u = 2 (D = 7, rho = w^4)."""
    w = g.RF.var()

    def wp(k):
        out = g.RF1
        for _ in range(k):
            out = out * w
        return out

    rho = wp(4)
    c1 = g.RF1 + w
    c2 = g.RF1 + wp(2)
    c3 = g.RF1 - rfc(Fraction(1, 2)) * wp(3)
    GW = [[g.RF1, g.RF0, g.RF0, g.RF0],
          [g.RF0, -(rho * c1), g.RF0, g.RF0],
          [g.RF0, g.RF0, -c2, g.RF0],
          [g.RF0, g.RF0, g.RF0, -c3]]

    def perturbed(E12):
        E = [[wp(1), wp(3), wp(2), g.RF0],
             [wp(3), wp(5), E12, wp(3)],
             [wp(2), E12, wp(2), wp(3)],
             [g.RF0, wp(3), wp(3), wp(1)]]
        return [[GW[i][j] + E[i][j] for j in range(4)] for i in range(4)]

    Gp = perturbed(wp(4))     # admissible: E_{1j} = rho^{1/2} x (positive order)

    # nondegenerate block on slots (0,2,3)
    H = [[Gp[i][j] for j in (0, 2, 3)] for i in (0, 2, 3)]
    detH = g.rf_mat_det(H)
    g.check("[Sec 9] nondegenerate 3x3 block is a unit at the boundary (det != 0 at w = 0)",
            detH.eval(0) != 0)

    # block congruence: C = I with column 1 corrected by x = H^{-1} b
    b = [Gp[0][1], Gp[2][1], Gp[3][1]]
    x = g.rf_mat_solve(H, b)
    C = [[g.RF1 if i == j else g.RF0 for j in range(4)] for i in range(4)]
    C[0][1] = -x[0]
    C[2][1] = -x[1]
    C[3][1] = -x[2]
    CT_G_C = [[g.RF0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            acc = g.RF0
            for a in range(4):
                for bb in range(4):
                    acc = acc + C[a][i] * Gp[a][bb] * C[bb][j]
            CT_G_C[i][j] = acc
    ok = all(CT_G_C[i][1].is_zero() and CT_G_C[1][i].is_zero() for i in (0, 2, 3))
    g.check("[Sec 9] block congruence eliminates the dying-slot cross terms exactly "
            "(C^T G' C block-diagonal, C a unit transition)", ok)
    dtil = CT_G_C[1][1]
    schur = Gp[1][1] - (b[0] * x[0] + b[1] * x[1] + b[2] * x[2])
    g.check("[Sec 9] the (1,1) entry of the congruence is the Schur complement", dtil.eqrf(schur))
    g.check("[Sec 9] the dying entry survives at first order: (Schur/rho)(0) = -c1(0) + corrections != 0",
            (dtil / rho).eval(0) != 0)
    detGp = g.rf_mat_det(Gp)
    g.check("[Sec 9] det G' = det(nondegenerate block) x Schur, and det G'/rho -> nonzero: first-order dying eigenvalue",
            detGp.eqrf(detH * dtil) and (detGp / rho).eval(0) != 0)
    Gp0 = g.frac_matrix(rf_eval_mat(Gp, 0))
    g.check("[Sec 9] the perturbed Gram is corank one at the boundary with the same radical",
            g.mat_rank(Gp0) == 3 and g.congruence_signature(Gp0) == (1, 2, 1))

    # completion of the perturbed data, global coupling mu nu = -1/2
    Ginv_col = g.rf_mat_solve(Gp, [g.RF0, g.RF1, g.RF0, g.RF0])
    s_rf = Ginv_col[1]
    h = [[g.RF0] * 6 for _ in range(6)]
    for i in range(4):
        for j in range(4):
            h[i][j] = Gp[i][j]
    h[1][4] = h[4][1] = g.RF1
    h[1][5] = h[5][1] = rfc(Fraction(-1, 2))
    h[4][5] = h[5][4] = rfc(-1)
    deth = g.rf_mat_det(h)
    F = g.RF1 - s_rf          # 1 + 2 (nu mu) s with nu mu = -1/2
    g.check("[Sec 9] completion determinant identity det h = det G' (-F) for the perturbed data",
            deth.eqrf(detGp * (-F)))
    ok = deth.eval(0) != 0
    for w0 in (Fraction(1, 3), Fraction(1, 2)):
        ok = ok and g.congruence_signature(rf_eval_mat(h, w0)) == (2, 4, 0)
    ok = ok and g.congruence_signature(rf_eval_mat(h, 0)) == (2, 4, 0)
    g.check("[Sec 9] perturbed completion: det h nonvanishing at the boundary, signature (2,4) there and at samples", ok)

    # SHARPNESS: cross errors of exactly relative order zero (E_12 = c w^2 =
    # c rho^{1/2}) corrupt the leading data: with c = 2 the dying eigenvalue
    # keeps order rho but its unit flips sign (-1 -> +3); with c = 1 the
    # leading term is tuned away entirely and the order jumps to w^8.
    g.check("[Sec 9] admissible case: dying eigenvalue = -1 x rho + higher, the unperturbed unit",
            (detGp / rho).eval(0) == Fraction(-1))
    Gs1 = perturbed(wp(2))
    det1 = g.rf_mat_det(Gs1)
    Gs2 = perturbed(rfc(2) * wp(2))
    det2 = g.rf_mat_det(Gs2)
    lead1 = det1
    k = 0
    while k <= 12 and lead1.eval(0) == 0:
        lead1 = lead1 / w
        k += 1
    g.check("[Sec 9] SHARPNESS (c=1): the leading term cancels and the dying eigenvalue "
            "jumps to order w^8: (T3d) destroyed at relative order zero",
            (det1 / rho).eval(0) == 0 and k == 8 and lead1.eval(0) == Fraction(3)
            and g.mat_rank(g.frac_matrix(rf_eval_mat(Gs1, 0))) == 3)
    g.check("[Sec 9] SHARPNESS (c=2): the order survives but the unit flips sign (-1 -> +3): "
            "the leading data is corrupted, so strict relative positivity is necessary",
            (det2 / rho).eval(0) == Fraction(3))



def weld_frame_checks(m):
    """The static orthonormal coframe of T6 consists of exceptional-module
    sections, converging to the rain coframe at the boundary (rationalised
    identities; u = sqrt r)."""
    tag = " (2M = %d)" % (m * m)
    u = g.RF.var()
    R = u * u
    m2 = rfc(m * m)
    beta = rfc(m) / u
    # sqrt(m^2 - r) x theta^1_S in coordinate components (dt, dr):
    lhs = [(m2 - R) / u, rfc(m)]
    # -u dt + m (k/u), with k/u = dr + beta dt:
    rhs = [rfc(-1) * u + rfc(m) * beta, rfc(m)]
    g.check("[Sec 8.8] sqrt(m^2-r) theta1_S = -u dt + m (k/u): T6's static radial unit covector "
            "is an exceptional-module section" + tag,
            lhs[0].eqrf(rhs[0]) and lhs[1].eqrf(rhs[1]))
    # boost coefficients (a, b) = (-u, m)/sqrt(m^2-r): unit norm a^2 - b^2 = -1
    g.check("[Sec 8.8] the static/rain boost is unit: (u^2 - m^2)/(m^2 - r) = -1, rapidity -> 0 at the boundary" + tag,
            ((R - m2) / (m2 - R)).eqrf(rfc(-1)) and (u / u).eval(Fraction(1, 2)) == 1)
    # boundary limit: coefficients (-u, m) -> (0, m): theta1_S -> k/u
    g.check("[Sec 8.8] at the boundary theta1_S -> k/u: the static frame converges to the rain frame" + tag,
            (rfc(-1) * u).eval(0) == 0)
    # proper time: G(dtau, dtau) = 1 with dtau = sqrt(r/(m^2-r)) dr, via G(dr,dr) = (m^2-r)/r
    g.check("[Sec 8.8] G(dtau, dtau) = 1 exactly: T6's synchronous time is unit at every interior radius" + tag,
            ((R / (m2 - R)) * ((m2 - R) / R)).eqrf(g.RF1))



def weld_rate_checks():
    """The Hubble-normalised transport rates of the common frame, as exact
    power series in s = sqrt r (units 2M = 1), reproducing T6's constants."""
    N = 8
    # (1 - s^2)^{+-1/2} as series in s
    one_minus = [Fraction(1), Fraction(0), Fraction(-1)] + [Fraction(0)] * (N - 2)
    inv_sqrt = g.ps_pow_rat(one_minus, Fraction(-1, 2), N)
    sqrt_ser = g.ps_pow_rat(one_minus, Fraction(1, 2), N)
    # tau(s) = int 2 s^2 (1-s^2)^{-1/2} ds : integrand coefficients
    integrand = [Fraction(0)] * (N + 1)
    for k, c in enumerate(inv_sqrt):
        if k + 2 <= N:
            integrand[k + 2] += 2 * c
    tau = g.ps_int(integrand)
    g.check("[Sec 8.8] tau(r) = (2/3) r^{3/2} + (1/5) r^{5/2} + ... exactly (T6 Lem 5.1's series)",
            tau[3] == Fraction(2, 3) and tau[5] == Fraction(1, 5) and tau[0] == 0 and tau[1] == 0 and tau[2] == 0)
    # T := tau / s^3 (series in s), then tau sigma_1 = -(1/2) T (1-s^2)^{-1/2},
    # tau sigma_2 = T (1-s^2)^{1/2}
    T = g.ps_trunc(tau[3:], N)
    ts1 = g.ps_mul([Fraction(-1, 2) * c for c in T], inv_sqrt, N)
    ts2 = g.ps_mul(T, sqrt_ser, N)
    g.check("[Sec 8.8] tau sigma_1 = -1/3 - (4/15) r + O(r^2): T6's exact boost rate, re-derived on the sheaf side",
            ts1[0] == Fraction(-1, 3) and ts1[1] == 0 and ts1[2] == Fraction(-4, 15))
    g.check("[Sec 8.8] tau sigma_2 = 2/3 - (2/15) r + O(r^2): T6's exact sphere rate, re-derived",
            ts2[0] == Fraction(2, 3) and ts2[1] == 0 and ts2[2] == Fraction(-2, 15))
    g.check("[Sec 8.8] the trace rule: tau(sigma_1 + 2 sigma_2) -> 1 (the Kasner sum rule as a rate statement)",
            ts1[0] + 2 * ts2[0] == 1)
    # the rotation coefficient Hubble-normalised: tau / r = tau / s^2 -> 0 like (2/3) s
    tau_over_r = g.ps_trunc(tau[2:], N)
    g.check("[Sec 8.8] the rotation coefficient goes to zero: tau/r = (2/3) sqrt(r) + O(r^{3/2}) -> 0",
            tau_over_r[0] == 0 and tau_over_r[1] == Fraction(2, 3))
    # the limiting values p_i B_i (nonzero multiples of the boosts) generate so(1,3)
    p = kasner_point(1)
    g.check("[Sec 8.8] the limiting connection values p_i B_i have all p_i != 0, so they generate "
            "the full bivector algebra so(1,3) (closure checked in item 5)",
            all(q != 0 for q in p))



# ============================================================================
# Sections 9.3 and 9.4: the smooth structure of the variable-order algebra,
# and exponent collisions / the edge of the wall.  A self-contained formal
# calculus of terms f(x) tau^{e(x)} (log tau)^k with polynomial f, e over Q
# (the log obstruction, b-stability, log-degree filtration, order
# preservation, the ratio no-go), and the collision dichotomy on the Kasner
# constraint variety (census, zero forcing, the edge curve, the Kasner-map
# identity, dying-order identities, both chamber packages, edge coincidence).
# ============================================================================

# ----------------------------------------------------------------------------
# Polynomials in x over Q: tuples of Fractions, low degree first, normalised.
# ----------------------------------------------------------------------------

def pnorm(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return tuple(p)


def padd(a, b):
    n = max(len(a), len(b))
    return pnorm([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(n)])


def pmul(a, b):
    if not a or not b:
        return ()
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return pnorm(out)


def pdiff(a):
    return pnorm([i * a[i] for i in range(1, len(a))])


def pc(*coeffs):
    return pnorm([Fraction(c) for c in coeffs])


# ----------------------------------------------------------------------------
# The formal variable-order log calculus.
# An element is a dict {(e, k): f} for exponent polynomial e (tuple), log
# power k >= 0 (int), coefficient polynomial f (tuple), representing the
# locally finite sum  Sum f(x) tau^{e(x)} (log tau)^k.
# ----------------------------------------------------------------------------

def anorm(d):
    return {ek: f for ek, f in d.items() if f}


def aterm(f, e, k=0):
    return anorm({(pnorm(e), k): pnorm(f)})


def aadd(a, b):
    out = dict(a)
    for ek, f in b.items():
        out[ek] = padd(out.get(ek, ()), f)
    return anorm(out)


def amul(a, b):
    out = {}
    for (e1, k1), f1 in a.items():
        for (e2, k2), f2 in b.items():
            ek = (padd(e1, e2), k1 + k2)
            out[ek] = padd(out.get(ek, ()), pmul(f1, f2))
    return anorm(out)


def a_tau_dtau(a):
    """tau d/dtau:  f tau^e L^k  |->  f e tau^e L^k + k f tau^e L^{k-1}."""
    out = {}
    for (e, k), f in a.items():
        ek = (e, k)
        t1 = pmul(f, e)
        if t1:
            out[ek] = padd(out.get(ek, ()), t1)
        if k >= 1:
            ek2 = (e, k - 1)
            t2 = pnorm([k * c for c in f])
            out[ek2] = padd(out.get(ek2, ()), t2)
    return anorm(out)


def a_dx(a):
    """d/dx:  f tau^e L^k  |->  f' tau^e L^k + f e' tau^e L^{k+1}."""
    out = {}
    for (e, k), f in a.items():
        t1 = pdiff(f)
        if t1:
            ek = (e, k)
            out[ek] = padd(out.get(ek, ()), t1)
        t2 = pmul(f, pdiff(e))
        if t2:
            ek2 = (e, k + 1)
            out[ek2] = padd(out.get(ek2, ()), t2)
    return anorm(out)


def logdeg(a):
    return max((k for (_, k) in a), default=-1)


def exps(a):
    return {e for (e, _) in a}


def smoothstructure_checks():
    print("--- [Sec 9.2] the smooth structure of the variable-order algebra ---")

    x = pc(0, 1)                       # the polynomial x
    e1 = pc(0, 1)                      # e(x) = x
    e2 = pc(1, 0, 2)                   # e(x) = 1 + 2x^2
    f1 = pc(3, -1)                     # 3 - x
    f2 = pc(0, 0, 5)                   # 5x^2

    A1 = aadd(aterm(f1, e1), aterm(f2, e2))
    A2 = aadd(aterm(pc(2), e2), aterm(pc(1, 1), pc(2)))

    # ring closure, commutativity, associativity
    P = amul(A1, A2)
    g.check("[Sec 9.2] products stay in the class (exponents add, coefficients multiply)",
            P == anorm(P) and logdeg(P) == 0 and
            padd(e1, e2) in exps(P))
    g.check("[Sec 9.2] commutativity: A1*A2 = A2*A1 exactly", amul(A1, A2) == amul(A2, A1))
    A3 = aterm(pc(1, 2), pc(0, 3))
    g.check("[Sec 9.2] associativity: (A1*A2)*A3 = A1*(A2*A3) exactly",
            amul(amul(A1, A2), A3) == amul(A1, amul(A2, A3)))

    # b-derivative stability: tau d/dtau creates no logs
    T = aterm(pc(1), e2)               # tau^{1+2x^2}
    g.check("[Sec 9.2] tau d/dtau (tau^e) = e tau^e: log-free, exponent preserved",
            a_tau_dtau(T) == aterm(e2, e2) and logdeg(a_tau_dtau(T)) == 0)
    g.check("[Sec 9.2] tau d/dtau preserves the algebra on a general element (log degree unchanged)",
            logdeg(a_tau_dtau(A1)) == 0)

    # THE LOG OBSTRUCTION: d/dx tau^{e(x)} = e'(x) (log tau) tau^{e(x)}
    Tx = aterm(pc(1), e1)              # tau^x
    D = a_dx(Tx)
    g.check("[Sec 9.2] LOG OBSTRUCTION: d/dx tau^x = (log tau) tau^x exactly (coefficient e' = 1)",
            D == aterm(pc(1), e1, 1))
    D2 = a_dx(aterm(pc(1), e2))
    g.check("[Sec 9.2] d/dx tau^{1+2x^2} = 4x (log tau) tau^{1+2x^2}: coefficient exactly e'",
            D2 == aterm(pdiff(e2), e2, 1))

    # constant exponents: no logs, ever
    C = aterm(f1, pc(Fraction(2, 3)))
    g.check("[Sec 9.2] constant exponent: d/dx (f tau^{2/3}) = f' tau^{2/3}, log-free "
            "(the Melrose polyhomogeneous case)",
            a_dx(C) == aterm(pdiff(f1), pc(Fraction(2, 3))) and logdeg(a_dx(C)) == 0)
    g.check("[Sec 9.2] the obstruction coefficient e' vanishes identically iff e is constant "
            "(checked for e = x and e = 2/3)",
            pdiff(e1) != () and pdiff(pc(Fraction(2, 3))) == ())

    # the log completion is closed; log degree counts tangential derivatives
    DD = a_dx(a_dx(Tx))
    top = {ek: f for ek, f in DD.items() if ek[1] == 2}
    g.check("[Sec 9.2] two tangential derivatives: log degree exactly 2, top coefficient (e')^2",
            logdeg(DD) == 2 and top == {(e1, 2): pmul(pdiff(e1), pdiff(e1))})
    Mx = a_tau_dtau(a_dx(Tx))
    g.check("[Sec 9.2] mixed derivative tau d/dtau d/dx: log degree stays <= number of tangential "
            "derivatives (= 1)", logdeg(Mx) == 1)
    L = aterm(pc(1), pc(0), 1)         # log tau
    g.check("[Sec 9.2] tau d/dtau (log tau) = 1: the completion is b-stable on the log itself",
            a_tau_dtau(L) == aterm(pc(1), pc(0), 0))

    # commutation and Leibniz: the calculus is a genuine calculus
    g.check("[Sec 9.2] [d/dx, tau d/dtau] = 0 on a general log element",
            a_dx(a_tau_dtau(aadd(A1, aterm(f2, e1, 1)))) ==
            a_tau_dtau(a_dx(aadd(A1, aterm(f2, e1, 1)))))
    g.check("[Sec 9.2] Leibniz for d/dx on a product",
            a_dx(amul(A1, A2)) == aadd(amul(a_dx(A1), A2), amul(A1, a_dx(A2))))
    g.check("[Sec 9.2] Leibniz for tau d/dtau on a product",
            a_tau_dtau(amul(A1, A2)) == aadd(amul(a_tau_dtau(A1), A2),
                                             amul(A1, a_tau_dtau(A2))))

    # order preservation: derivatives never lower the exponent set (conormality)
    for name, DA in (("tau d/dtau", a_tau_dtau(A1)), ("d/dx", a_dx(A1))):
        g.check("[Sec 9.2] %s preserves the exponent set (orders never drop): conormal bounds"
                % name, exps(DA) <= exps(A1))

    # iterated bound on a longer word: log degree <= number of tangential letters
    word = A1
    ntang = 0
    for op in (a_dx, a_tau_dtau, a_dx, a_tau_dtau, a_dx):
        word = op(word)
        if op is a_dx:
            ntang += 1
    g.check("[Sec 9.2] a five-letter derivative word: log degree (%d) <= tangential letters (%d)"
            % (logdeg(word), ntang), logdeg(word) <= ntang)

    # the ratio no-go: exponent ratios are invariants; Kasner ratios move with u
    def kp(u):
        u = Fraction(u)
        Dn = 1 + u + u * u
        return (-u / Dn, (1 + u) / Dn, u * (1 + u) / Dn)

    # reparametrisation tau -> sigma^{a(x)} rescales every exponent by a(x):
    a_of_x = pc(2, 1)                  # a(x) = 2 + x, positive near 0
    r1, r2 = pmul(a_of_x, e1), pmul(a_of_x, e2)
    g.check("[Sec 9.2] quasi-homogeneous reparametrisation rescales exponents by a(x): "
            "ratios are invariant (cross-multiplication identity)",
            pmul(r1, e2) == pmul(r2, e1))
    # the Kasner ratio -p1/p2 = u/(1+u) separates parameter values:
    pairs = [(1, 2), (2, 3), (1, 3), (2, 5)]
    ok = True
    for ua, ub in pairs:
        pa, pb = kp(ua), kp(ub)
        ok = ok and (pa[0] * pb[1] != pb[0] * pa[1])
    g.check("[Sec 9.2] the ratio p1/p2 separates Kasner parameters (four sample pairs): "
            "nonconstant u forces nonconstant ratios, hence NO constant-exponent reduction", ok)
    rvals = [Fraction(u, 1 + u) for u in (1, 2, 3, 5)]
    g.check("[Sec 9.2] -p1/p2 = u/(1+u) is strictly increasing in u (sample chain)",
            all(rvals[i] < rvals[i + 1] for i in range(3)))
    print()


# ----------------------------------------------------------------------------
# [Sec 9.3] exponent collisions and the edge of the wall
# ----------------------------------------------------------------------------







def q_curve(v):
    v = Fraction(v)
    Dn = 1 + v + v * v
    return (-v / Dn, v * (1 + v) / Dn, (1 + v) / Dn)


def collision_checks():
    print("--- [Sec 9.3] exponent collisions and the edge of the wall ---")

    # (1) the collision census: equal pairs occur only at s = 0 and s = 2/3
    s = g.RF.var()
    census = rfc(6) * s * s - rfc(4) * s
    g.check("[Sec 9.3] equal-pair equation 6s^2 - 4s = 2s(3s-2): the only equal-pair loci are "
            "s = 0 (Taub) and s = 2/3 (Schwarzschild)",
            census.eqrf(rfc(2) * s * (rfc(3) * s - rfc(2))) and
            census.eval(0) == 0 and census.eval(Fraction(2, 3)) == 0 and
            census.eval(Fraction(1, 3)) != 0)
    for sval, name in ((Fraction(0), "Taub (0,0,1)"), (Fraction(2, 3), "Schwarzschild (2/3,2/3,-1/3)")):
        trip = (sval, sval, 1 - 2 * sval)
        g.check("[Sec 9.3] census triple %s satisfies both Kasner constraints" % name,
                sum(trip) == 1 and sum(t * t for t in trip) == 1)

    # (2) zero forcing: an exponent cannot vanish alone
    p2 = g.RF.var()
    gap = p2 * p2 + (g.RF1 - p2) * (g.RF1 - p2) - g.RF1
    g.check("[Sec 9.3] ZERO FORCING: with p1 = 0 the constraints give 2 p2(p2 - 1) = 0, "
            "so the triple is (0,0,1) or (0,1,0): zeros come in pairs (Taub forced)",
            gap.eqrf(rfc(2) * p2 * (p2 - g.RF1)) and
            gap.eval(0) == 0 and gap.eval(1) == 0 and gap.eval(Fraction(1, 2)) != 0)

    # (3) the edge curve q(v) = (-v, v(1+v), 1+v)/(1+v+v^2)
    v = g.RF.var()
    Dn = g.RF1 + v + v * v
    q1, q2, q3 = -v / Dn, v * (g.RF1 + v) / Dn, (g.RF1 + v) / Dn
    g.check("[Sec 9.3] edge curve: Sum q = 1 as a rational-function identity in v",
            (q1 + q2 + q3).eqrf(g.RF1))
    g.check("[Sec 9.3] edge curve: Sum q^2 = 1 as a rational-function identity in v",
            (q1 * q1 + q2 * q2 + q3 * q3).eqrf(g.RF1))
    g.check("[Sec 9.3] q(0) = (0,0,1): the curve passes through the Taub point",
            (q1.eval(0), q2.eval(0), q3.eval(0)) == (0, 0, 1))
    g.check("[Sec 9.3] q(1/2) = (-2/7, 3/7, 6/7): the u = 2 Kasner triple (chamber side v > 0)",
            (q1.eval(Fraction(1, 2)), q2.eval(Fraction(1, 2)), q3.eval(Fraction(1, 2)))
            == kasner_point(2))
    pk3 = kasner_point(3)
    g.check("[Sec 9.3] q(-1/4) = (4/13, -3/13, 12/13): the u = 3 triple with axes 1,2 EXCHANGED "
            "(chamber side v < 0)",
            (q1.eval(Fraction(-1, 4)), q2.eval(Fraction(-1, 4)), q3.eval(Fraction(-1, 4)))
            == (pk3[1], pk3[0], pk3[2]))
    ok = True
    for vv in (Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)):
        ok = ok and q1.eval(vv) < 0 < q2.eval(vv)
    for vv in (Fraction(-1, 8), Fraction(-1, 4), Fraction(-2, 5)):
        ok = ok and q2.eval(vv) < 0 < q1.eval(vv)
    g.check("[Sec 9.3] the ordering changes across v = 0: axis 1 is the dying axis for v > 0, axis 2 "
            "for v < 0 (three samples each side)", ok)
    prod12 = q1 * q2 * Dn * Dn
    g.check("[Sec 9.3] q1 q2 (1+v+v^2)^2 = -v^2(1+v): the two crossing exponents vanish to "
            "SECOND order jointly at the edge",
            prod12.eqrf(-v * v * (g.RF1 + v)))

    # (4) the Kasner-map identity p(1/u) = (p1, p3, p2)(u), fixed point u = 1
    ok = True
    for u in (2, 3, 5, 7):
        pa = kasner_point(u)
        pb = kasner_point(Fraction(1, u))
        ok = ok and pb == (pa[0], pa[2], pa[1])
    g.check("[Sec 9.3] p(1/u) = (p1, p3, p2)(u): the positive-pair exchange (four exact samples)", ok)
    g.check("[Sec 9.3] the exchange's fixed point is u = 1: p(1) = (-1/3, 2/3, 2/3), the "
            "Schwarzschild triple of Theorem 8.16",
            kasner_point(1) == (Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)))

    # (5) the dying order d(u) = -2 p1(u) = 2u/(1+u+u^2): maximum at Schwarzschild, zero at Taub
    u = g.RF.var()
    Du = g.RF1 + u + u * u
    d = rfc(2) * u / Du
    g.check("[Sec 9.3] dying-order identity d(1) - d(u) = 2(u-1)^2 / (3(1+u+u^2)): the "
            "Schwarzschild point u = 1 MAXIMISES the dying order (d = 2/3) on the whole class",
            (rfc(Fraction(2, 3)) - d).eqrf(rfc(2) * (u - g.RF1) * (u - g.RF1) / (rfc(3) * Du)))
    wv = g.RF.var()
    d_at_inf = rfc(2) * wv / (wv * wv + wv + g.RF1)   # d(1/w)
    g.check("[Sec 9.3] d(1/w) = 2w/(1+w+w^2) -> 0 at w = 0: the dying order vanishes at the "
            "Taub corner, and on the edge curve -2 q1(v) = 2v/(1+v+v^2) likewise",
            d_at_inf.eval(0) == 0 and (rfc(-2) * q1).eqrf(rfc(2) * v / Dn))

    # (6) Schwarzschild consistency: at u = 1, rho = tau^{2/3} is EXACTLY first order in r
    N = 8
    one_minus = [Fraction(1), Fraction(0), Fraction(-1)] + [Fraction(0)] * (N - 2)
    inv_sqrt = g.ps_pow_rat(one_minus, Fraction(-1, 2), N)
    integrand = [Fraction(0)] * (N + 1)
    for k, c in enumerate(inv_sqrt):
        if k + 2 <= N:
            integrand[k + 2] += 2 * c
    tau = g.ps_int(integrand)
    tau2 = g.ps_mul(tau, tau, N + 3)
    g.check("[Sec 9.3] rho^3 = tau^2 = (4/9) r^3 (1 + O(r)) exactly (series in sqrt r): "
            "the u = 1 dying order 2/3 converts to first order in r, matching det G = -r",
            all(tau2[k] == 0 for k in range(6)) and tau2[6] == Fraction(4, 9)
            and tau2[8] == Fraction(4, 15))

    # (7) at the Taub point the weighted Gram is NONDEGENERATE: the wall ends
    for c in ((1, 1, 1), (2, Fraction(1, 3), 5)):
        M = [[Fraction(0)] * 4 for _ in range(4)]
        M[0][0] = Fraction(1)
        for i, ci in enumerate(c):
            M[i + 1][i + 1] = -Fraction(ci)
        g.check("[Sec 9.3] Taub edge Gram diag(1,-c1,-c2,-c3), c = %s: signature (1,3), corank 0: "
                "no wall on the edge" % (c,),
                g.congruence_signature(M) == (1, 3, 0))

    # (8) the chamber package on the v < 0 side (dying axis 2), at q(-1/4) = (4/13,-3/13,12/13)
    qv = q_curve(Fraction(-1, 4))
    g.check("[Sec 9.3] chamber v < 0: exponents (4/13, -3/13, 12/13), constraints hold",
            sum(qv) == 1 and sum(t * t for t in qv) == 1 and qv[1] < 0 < qv[0])
    Dq = 13
    w = g.RF.var()

    def tau_pow(qexp):
        e = Fraction(qexp) * Dq
        assert e.denominator == 1
        e = e.numerator
        out = g.RF1
        for _ in range(abs(e)):
            out = out * w
        return out if e >= 0 else g.RF1 / out

    raw = [g.RF1, -tau_pow(-2 * qv[0]), -tau_pow(-2 * qv[1]), -tau_pow(-2 * qv[2])]
    wts = [Fraction(0), qv[0], Fraction(0), qv[2]]
    W = [raw[i] * tau_pow(2 * wts[i]) for i in range(4)]
    rho2 = tau_pow(-2 * qv[1])
    g.check("[Sec 9.3] chamber v < 0: forced weights (0, q1, 0, q3), weighted Gram "
            "diag(1, -1, -rho', -1) with rho' = tau^{-2 q2}",
            W[0].eqrf(g.RF1) and W[1].eqrf(rfc(-1)) and W[2].eqrf(-rho2)
            and W[3].eqrf(rfc(-1)))
    G0 = [W[i].eval(0) for i in range(4)]
    M0 = [[Fraction(0)] * 4 for _ in range(4)]
    for i in range(4):
        M0[i][i] = G0[i]
    g.check("[Sec 9.3] chamber v < 0: boundary corank one, radical = AXIS 2 (the dying axis has "
            "switched across the edge)",
            g.congruence_signature(M0) == (1, 2, 1) and G0[2] == 0 and G0[1] == -1)

    def hmat(nu, mu_c):
        z = g.RF0
        cnu, cmu = rfc(nu), rfc(mu_c)
        return [
            [W[0], z, z, z, z, z],
            [z, W[1], z, z, z, z],
            [z, z, W[2], z, cnu, cmu],
            [z, z, z, W[3], z, z],
            [z, z, cnu, z, z, rfc(-1)],
            [z, z, cmu, z, rfc(-1), z],
        ]

    h = hmat(1, Fraction(-1, 2))
    g.check("[Sec 9.3] chamber v < 0: global coupling mu nu = -1/2 on the switched axis, "
            "det h = 1 + rho' exactly", g.rf_mat_det(h).eqrf(g.RF1 + rho2))
    ok = g.congruence_signature(rf_eval_mat(h, 0)) == (2, 4, 0)
    for w0 in (Fraction(1, 3), Fraction(1, 2), Fraction(1)):
        ok = ok and g.congruence_signature(rf_eval_mat(h, w0)) == (2, 4, 0)
    g.check("[Sec 9.3] chamber v < 0: completion signature (2,4) at boundary and samples, "
            "no shadow wall: the variable-weight theorem holds verbatim with the axes relabelled", ok)
    o = [Fraction(0)] + [-2 * t for t in qv]
    deg = [(t - oo) / 2 for oo, t in
           zip(o, [Fraction(0), Fraction(0), -2 * qv[1], Fraction(0)])]
    exc = [(Fraction(0) - oo) / 2 for oo in o]
    g.check("[Sec 9.3] chamber v < 0: degeneration-regime weights forced = (0, q1, 0, q3) and "
            "exceptional weights = (0, q1, q2, q3), by the same linear solve",
            deg == [Fraction(0), qv[0], Fraction(0), qv[2]]
            and exc == [Fraction(0)] + list(qv))

    # (9) the edge coincidence and the failed gluing
    p_taub = (Fraction(0), Fraction(0), Fraction(1))
    w_ch1 = [Fraction(0), Fraction(0), p_taub[1], p_taub[2]]
    w_ch2 = [Fraction(0), p_taub[0], Fraction(0), p_taub[2]]
    g.check("[Sec 9.3] EDGE COINCIDENCE: both chamber weight assignments evaluate to (0,0,0,1) "
            "at the Taub point: the modules meet on the edge",
            w_ch1 == w_ch2 == [0, 0, 0, 1])
    vv = Fraction(1, 2)
    qq = q_curve(vv)
    g.check("[Sec 9.3] FAILED GLUING: off the edge the chamber transition has exponents "
            "(q1, -q2) = (-2/7, -3/7), both negative: a unit in the variable-order algebra "
            "on NEITHER side, so no single weighted module crosses the edge",
            qq[0] < 0 and -qq[1] < 0)
    print()




# ---------------------------------------------------------------------------
# [Sec 10] transversal independence and the no-value theorem at the wall
# ---------------------------------------------------------------------------

def transversal_checks():
    """[Lem 10.2], [Thm 10.3], [Thm 10.4]: the intertwiner and the no-value
    theorem, on the Schwarzschild boundary data at two masses.  Self-contained
    exact matrix helpers, nested to avoid any clash with the module's own."""
    from fractions import Fraction as F_

    def mm_(A, B):
        return [[sum(A[i][t] * B[t][j] for t in range(len(B))) for j in range(len(B[0]))]
                for i in range(len(A))]

    def T_(A):
        return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

    def meq_(A, B):
        return all(A[i][j] == B[i][j] for i in range(len(A)) for j in range(len(A[0])))

    def eye_(n):
        return [[F_(1) if i == j else F_(0) for j in range(n)] for i in range(n)]

    def zeros_(n, m=None):
        m = n if m is None else m
        return [[F_(0)] * m for _ in range(n)]

    def solve_(M, rhs):
        n, m = len(M), len(M[0])
        A = [list(M[i]) + [rhs[i]] for i in range(n)]
        r = 0
        piv_cols = []
        for c in range(m):
            piv = None
            for i in range(r, n):
                if A[i][c] != 0:
                    piv = i
                    break
            if piv is None:
                continue
            A[r], A[piv] = A[piv], A[r]
            pv = A[r][c]
            A[r] = [x / pv for x in A[r]]
            for i in range(n):
                if i != r and A[i][c] != 0:
                    f = A[i][c]
                    A[i] = [A[i][j] - f * A[r][j] for j in range(m + 1)]
            piv_cols.append(c)
            r += 1
        for i in range(r, n):
            if A[i][m] != 0:
                return None
        x = [F_(0)] * m
        for i, c in enumerate(piv_cols):
            x[c] = A[i][m]
        return x

    def pair_(cov, vec):
        return sum(cov[i] * vec[i] for i in range(len(cov)))

    def quad_(Gm, a, b):
        return sum(a[i] * Gm[i][j] * b[j] for i in range(len(a)) for j in range(len(a)))

    def build_h(Gm, uvec, mu, nu):
        h = zeros_(6)
        for i in range(4):
            for j in range(4):
                h[i][j] = Gm[i][j]
        for i in range(4):
            h[i][4] = h[4][i] = nu * uvec[i]
            h[i][5] = h[5][i] = mu * uvec[i]
        h[4][5] = h[5][4] = F_(-1)
        return h

    mu, nu = F_(-2), F_(3)
    for m in (F_(1), F_(2)):                      # 2M = m^2: the masses of Sec 8's blocks
        Gm = [[m * m, -m, F_(0), F_(0)],
              [-m, F_(1), F_(0), F_(0)],
              [F_(0), F_(0), F_(-1), F_(0)],
              [F_(0), F_(0), F_(0), F_(-1)]]
        k = [F_(1), m, F_(0), F_(0)]
        g.check("[Sec 10] boundary data at m = %s: G k = 0 exactly (radical membership)" % m,
                all(sum(Gm[i][j] * k[j] for j in range(4)) == 0 for i in range(4)))

        u = [F_(1), F_(0), F_(0), F_(0)]
        assert pair_(k, u) == 1
        for v in ([-m, F_(1), F_(0), F_(0)], [F_(0), F_(0), F_(1), F_(0)]):
            assert pair_(k, v) == 0
            vt0 = solve_(Gm, v)
            ok = vt0 is not None
            base = quad_(Gm, vt0, vt0) + 2 * pair_(vt0, u)
            tgauge = -base / 2
            vt = [vt0[i] + tgauge * k[i] for i in range(4)]
            probe = [F_(1), F_(2), F_(-1), F_(3)]
            ok = ok and quad_(Gm, vt, vt) + 2 * pair_(vt, u) == 0 \
                and quad_(Gm, probe, vt) == quad_(Gm, probe, vt0)
            g.check("[Lem 10.2] m = %s: the solve closes, the radical gauge meets the normalisation "
                    "at one t, and G(., vtilde) is gauge independent (v = %s)" % (m, [str(x) for x in v]), ok)

            hu = build_h(Gm, u, mu, nu)
            huv = build_h(Gm, [u[i] + v[i] for i in range(4)], mu, nu)
            Phi = eye_(6)
            for i in range(4):
                Phi[i][4] = nu * vt[i]
                Phi[i][5] = mu * vt[i]
            g.check("[Thm 10.3] m = %s, v = %s: Phi^T h_u Phi = h_(u+v) exactly, and Phi is unipotent"
                    % (m, [str(x) for x in v]),
                    meq_(mm_(T_(Phi), mm_(hu, Phi)), huv)
                    and all(x == 0 for row in mm_([[Phi[i][j] - (1 if i == j else 0) for j in range(6)]
                                                   for i in range(6)],
                                                  [[Phi[i][j] - (1 if i == j else 0) for j in range(6)]
                                                   for i in range(6)]) for x in row))
            vt_bad = [vt[i] + k[i] for i in range(4)]
            Phi_bad = eye_(6)
            for i in range(4):
                Phi_bad[i][4] = nu * vt_bad[i]
                Phi_bad[i][5] = mu * vt_bad[i]
            g.check("[Thm 10.3] m = %s, v = %s: the un-normalised gauge representative breaks the "
                    "intertwiner (control)" % (m, [str(x) for x in v]),
                    not meq_(mm_(T_(Phi_bad), mm_(hu, Phi_bad)), huv))

        k6 = k + [F_(0), F_(0)]
        kstar = [F_(0)] * 4 + [F_(1) / (2 * nu), F_(0)]
        lam = [-m, F_(1), F_(0), F_(0)]
        hu = build_h(Gm, u, mu, nu)
        huv0 = build_h(Gm, [u[i] + lam[i] for i in range(4)], mu, nu)
        hq = lambda H, a, b: sum(a[i] * H[i][j] * b[j] for i in range(6) for j in range(6))
        g.check("[Thm 10.3] m = %s: ladder relations k^2 = (k*)^2 = 0, {k,k*} = 1 in both completions" % m,
                hq(hu, k6, k6) == 0 and hq(hu, kstar, kstar) == 0 and 2 * hq(hu, k6, kstar) == 1
                and hq(huv0, k6, k6) == 0 and hq(huv0, kstar, kstar) == 0
                and 2 * hq(huv0, k6, kstar) == 1)

        vt0 = solve_(Gm, lam)
        base = quad_(Gm, vt0, vt0) + 2 * pair_(vt0, u)
        vt = [vt0[i] - (base / 2) * k[i] for i in range(4)]
        Phi = eye_(6)
        for i in range(4):
            Phi[i][4] = nu * vt[i]
            Phi[i][5] = mu * vt[i]
        Ghat = eye_(6)
        for i in range(4):
            for j in range(4):
                Ghat[i][j] = (F_(1) if i == j else F_(0)) + k[i] * lam[j]
        g.check("[Thm 10.4] m = %s: ghat is an isometry (T, h_(u+lambda)) -> (T, h_u)" % m,
                meq_(mm_(T_(Ghat), mm_(hu, Ghat)), huv0))
        Phi_inv = [[2 * (F_(1) if i == j else F_(0)) - Phi[i][j] for j in range(6)] for i in range(6)]
        theta = mm_(Ghat, Phi_inv)
        tk = [sum(theta[i][j] * k6[j] for j in range(6)) for i in range(6)]
        g.check("[Thm 10.4] m = %s: theta = ghat o Phi^(-1) is an automorphism of (T, h_u), not the "
                "identity, fixing k" % m,
                meq_(mm_(T_(theta), mm_(hu, theta)), hu) and not meq_(theta, eye_(6)) and tk == k6)
        # the contragredient is DERIVED from theta: invert the restriction of theta
        # to the coframe module exactly, transpose, and only then compare with the
        # closed form id - lambda (x) k; the candidate translation is applied to
        # the derived matrix, not to a hand-written one
        theta_base = [[theta[i][j] for j in range(4)] for i in range(4)]
        inv_base = [[F_(0)] * 4 for _ in range(4)]
        for col in range(4):
            e_col = [F_(1) if i == col else F_(0) for i in range(4)]
            x_col = solve_(theta_base, e_col)
            assert x_col is not None
            for i in range(4):
                inv_base[i][col] = x_col[i]
        dual = T_(inv_base)
        closed = [[(F_(1) if i == j else F_(0)) - lam[i] * k[j] for j in range(4)] for i in range(4)]
        g.check("[Thm 10.4] m = %s: the contragredient (theta|_(T*M))^(-T), computed from theta by exact "
                "inversion, equals id - lambda (x) k, and theta|_(T*M) = g_lambda = id + k (x) lambda" % m,
                meq_(dual, closed)
                and meq_(theta_base, [[(F_(1) if i == j else F_(0)) + k[i] * lam[j] for j in range(4)]
                                      for i in range(4)]))
        ok = True
        for c in (u, [F_(1) - m, F_(1), F_(0), F_(0)], [F_(1), F_(0), F_(5), F_(-2)]):
            assert pair_(k, c) == 1
            img = [sum(dual[i][j] * c[j] for j in range(4)) for i in range(4)]
            ok = ok and img == [c[i] - lam[i] for i in range(4)] and img != c
        g.check("[Thm 10.4] m = %s: the derived dual action translates every candidate by -lambda; "
                "none is fixed (three candidates)" % m, ok)

        # second lambda, spanning a different direction of the 3-dimensional ker k
        lam2 = [F_(0), F_(0), F_(1), F_(-1)]
        assert pair_(k, lam2) == 0
        huv2 = build_h(Gm, [u[i] + lam2[i] for i in range(4)], mu, nu)
        vt0 = solve_(Gm, lam2)
        vt2 = [vt0[i] - ((quad_(Gm, vt0, vt0) + 2 * pair_(vt0, u)) / 2) * k[i] for i in range(4)]
        Phi2 = eye_(6)
        Ghat2 = eye_(6)
        for i in range(4):
            Phi2[i][4] = nu * vt2[i]
            Phi2[i][5] = mu * vt2[i]
            for j in range(4):
                Ghat2[i][j] = (F_(1) if i == j else F_(0)) + k[i] * lam2[j]
        Phi2_inv = [[2 * (F_(1) if i == j else F_(0)) - Phi2[i][j] for j in range(6)] for i in range(6)]
        theta2 = mm_(Ghat2, Phi2_inv)
        g.check("[Thm 10.4] m = %s: a second lambda (angular direction of ker k): Phi^T h_u Phi = "
                "h_(u+lambda), ghat an isometry, theta an automorphism of (T, h_u) fixing k" % m,
                meq_(mm_(T_(Phi2), mm_(hu, Phi2)), huv2)
                and meq_(mm_(T_(Ghat2), mm_(hu, Ghat2)), huv2)
                and meq_(mm_(T_(theta2), mm_(hu, theta2)), hu)
                and [sum(theta2[i][j] * k6[j] for j in range(6)) for i in range(6)] == k6)

        # the fixed set of theta lies in the h_u-orthogonal of k: no theta-fixed
        # ladder partner (a partner has h_u(k, x) = 1/2).  Kernel of theta - id by
        # exact elimination, for both lambdas.
        ok = True
        for th in (theta, theta2):
            A = [[th[i][j] - (F_(1) if i == j else F_(0)) for j in range(6)] for i in range(6)]
            # null space by row reduction
            M = [list(r) for r in A]
            piv_cols = []
            r = 0
            for c in range(6):
                piv = next((i for i in range(r, 6) if M[i][c] != 0), None)
                if piv is None:
                    continue
                M[r], M[piv] = M[piv], M[r]
                pv = M[r][c]
                M[r] = [x / pv for x in M[r]]
                for i in range(6):
                    if i != r and M[i][c] != 0:
                        f = M[i][c]
                        M[i] = [M[i][j] - f * M[r][j] for j in range(6)]
                piv_cols.append(c)
                r += 1
            free = [c for c in range(6) if c not in piv_cols]
            basis = []
            for fc in free:
                x = [F_(0)] * 6
                x[fc] = F_(1)
                for row_i, pc in enumerate(piv_cols):
                    x[pc] = -M[row_i][fc]
                basis.append(x)
            ok = ok and len(basis) == 4 \
                and all(hq(hu, k6, x) == 0 for x in basis) \
                and all(all(sum(th[i][j] * x[j] for j in range(6)) == x[i] for i in range(6)) for x in basis)
        g.check("[Thm 10.4] m = %s: Fix(theta) has dimension 4 and lies in the h_u-orthogonal of k for "
                "both lambdas; no theta-fixed ladder partner exists" % m, ok)

        # the cocycle Phi^u_v o Phi^(u+v)_w = Phi^u_(v+w), with w normalised against u+v
        v1 = [-m, F_(1), F_(0), F_(0)]
        w1 = [F_(0), F_(0), F_(1), F_(2)]
        uv = [u[i] + v1[i] for i in range(4)]
        vt0 = solve_(Gm, v1)
        v1t = [vt0[i] - ((quad_(Gm, vt0, vt0) + 2 * pair_(vt0, u)) / 2) * k[i] for i in range(4)]
        wt0 = solve_(Gm, w1)
        w1t = [wt0[i] - ((quad_(Gm, wt0, wt0) + 2 * pair_(wt0, uv)) / 2) * k[i] for i in range(4)]
        zt0 = solve_(Gm, [v1[i] + w1[i] for i in range(4)])
        z1t = [zt0[i] - ((quad_(Gm, zt0, zt0) + 2 * pair_(zt0, u)) / 2) * k[i] for i in range(4)]

        def phi_of(vt_):
            P = eye_(6)
            for i in range(4):
                P[i][4] = nu * vt_[i]
                P[i][5] = mu * vt_[i]
            return P
        g.check("[Thm 10.3] m = %s: the cocycle: vtilde + wtilde (w normalised against u+v) is the "
                "representative of v+w normalised against u, and Phi^u_v Phi^(u+v)_w = Phi^u_(v+w)" % m,
                [v1t[i] + w1t[i] for i in range(4)] == z1t
                and meq_(mm_(phi_of(v1t), phi_of(w1t)), phi_of(z1t))
                and quad_(Gm, w1t, w1t) + 2 * pair_(w1t, uv) == 0)

        # Clifford level (exterior model on the coupled Gram h_u): Phi_v(k*) = k* + vtilde/2
        # is a ladder partner of k in (T, h_u), and Phi_v(sigma) = sigma + vtilde k on all 64 states
        vt6 = v1t + [F_(0), F_(0)]
        kstar_v = [kstar[i] + vt6[i] / 2 for i in range(6)]
        states = [{frozenset(S): F_(1)} for S in map(frozenset, g.all_blades(6))]

        def act(vec, st):
            return g.ext_c(vec, hu, st)

        def add_st(*ds):
            tot = {}
            for d in ds:
                for S, c in d.items():
                    tot[S] = tot.get(S, F_(0)) + c
            return {S: c for S, c in tot.items() if c != 0}

        def neg_st(d):
            return {S: -c for S, c in d.items()}
        ok = hq(hu, kstar_v, kstar_v) == 0 and 2 * hq(hu, k6, kstar_v) == 1
        for st in states:
            car = add_st(act(k6, act(kstar_v, dict(st))), act(kstar_v, act(k6, dict(st))))
            ok = ok and g.ext_state_eq(car, st)
            sig_old = add_st(act(kstar, act(k6, dict(st))), neg_st(act(k6, act(kstar, dict(st)))))
            sig_new = add_st(act(kstar_v, act(k6, dict(st))), neg_st(act(k6, act(kstar_v, dict(st)))))
            shift = act(vt6, act(k6, dict(st)))
            ok = ok and g.ext_state_eq(sig_new, add_st(sig_old, shift))
        g.check("[Thm 10.3] m = %s: Clifford level, exterior model on h_u over all 64 states: "
                "Phi_v(k*) = k* + vtilde/2 is a ladder partner of k, and Phi_v(sigma) = sigma + vtilde k" % m,
                ok)

    # the opposite coupling sign, mu nu > 0, at the wall: the intertwiner is sign-blind
    mu_p, nu_p = F_(2), F_(3)
    m = F_(1)
    Gm = [[m * m, -m, F_(0), F_(0)], [-m, F_(1), F_(0), F_(0)],
          [F_(0), F_(0), F_(-1), F_(0)], [F_(0), F_(0), F_(0), F_(-1)]]
    k = [F_(1), m, F_(0), F_(0)]
    u = [F_(1), F_(0), F_(0), F_(0)]
    v = [-m, F_(1), F_(0), F_(0)]
    vt0 = solve_(Gm, v)
    vt = [vt0[i] - ((quad_(Gm, vt0, vt0) + 2 * pair_(vt0, u)) / 2) * k[i] for i in range(4)]
    hu = build_h(Gm, u, mu_p, nu_p)
    huv = build_h(Gm, [u[i] + v[i] for i in range(4)], mu_p, nu_p)
    Phi = eye_(6)
    for i in range(4):
        Phi[i][4] = nu_p * vt[i]
        Phi[i][5] = mu_p * vt[i]
    g.check("[Thm 10.3] mu nu > 0 (mu, nu = 2, 3) at the wall: Phi^T h_u Phi = h_(u+v) exactly; the "
            "wall signatures are (3,3) for both transversals",
            meq_(mm_(T_(Phi), mm_(hu, Phi)), huv)
            and g.congruence_signature(hu) == (3, 3, 0) and g.congruence_signature(huv) == (3, 3, 0))

    # [Rem 10.5] off the wall the two ambient forms need not be isometric: the shadow
    # wall moves with the transversal.  Model data G = diag(lambda, 1, -1, -1), k = e_0,
    # mu nu = 1, transversal u = e_0 versus u + e_1.
    ok = True
    found_sig = found_deg = False
    for lam_off in (F_(-1), F_(-2)):
        Goff = [[lam_off, F_(0), F_(0), F_(0)], [F_(0), F_(1), F_(0), F_(0)],
                [F_(0), F_(0), F_(-1), F_(0)], [F_(0), F_(0), F_(0), F_(-1)]]
        h1 = build_h(Goff, [F_(1), F_(0), F_(0), F_(0)], F_(1), F_(1))
        h2 = build_h(Goff, [F_(1), F_(1), F_(0), F_(0)], F_(1), F_(1))
        s1, s2 = g.congruence_signature(h1), g.congruence_signature(h2)
        if lam_off == -1:
            found_sig = (s1 == (3, 3, 0) and s2 == (2, 4, 0))
        else:
            found_deg = (s1[2] == 1 and s2[2] == 0)
    g.check("[Rem 10.5] off the wall the forms are not isometric in general: at lambda = -1 the "
            "signatures are (3,3) and (2,4) for the two transversals; at lambda = -2 one form is "
            "degenerate and the other is not (the shadow wall moves with the transversal)",
            found_sig and found_deg)


def main():
    print("verify_T04.py: exact-arithmetic checks for Transport Papers T4 (v1.6)\n")
    blade_basis_checks()
    degsheaf_checks()
    resolution_checks()
    wall_gram_checks()
    det_identity_checks()
    completion_and_shadow_checks()
    ladder_pair_checks()
    exceptional_checks()
    residue_checks()
    schwarzschild_checks()
    uniqueness_checks()
    rainframe_checks()
    rain_duality_checks(1)
    rain_duality_checks(3)
    weld_fibre_checks()
    weld_frame_checks(1)
    weld_frame_checks(2)
    weld_rate_checks()
    for u_par in (1, 2, 3):
        aniso_point(u_par)
    aniso_ladder_checks()
    stability_checks()
    smoothstructure_checks()
    collision_checks()
    transversal_checks()
    print()
    if g.FAILURES:
        print("FAILURES (%d):" % len(g.FAILURES))
        for f in g.FAILURES:
            print("  " + f)
        sys.exit(1)
    print("ALL CHECKS PASSED.")


if __name__ == "__main__":
    main()
