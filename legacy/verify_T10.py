#!/usr/bin/env python3
# Copyright (c) 2026 Leon Butler. Released under the MIT License; see LICENSE-CODE.txt.
"""
verify_T10.py: exact-arithmetic verification of the computational identities of
"Dark Energy and the Action of Gravity: MacDowell-Mansouri, the Frozen Point,
and One Way to Grip" (Transport Papers, T10), printed version 1.1.

Imports the series' shared exact-arithmetic library GA.py (deposited alongside
this script).  Everything is exact: rational arithmetic and rational functions
in a formal cosmological constant throughout, no floating point anywhere.
Statement tags refer to the compiled paper.

Five parts.  A: the frozen point and the Stelle-West vector (lem:sw,
thm:action, prop:goldstone).  B: the wall's free sector (thm:wallfree),
including the check that the withdrawn radical-vanishing claim fails; the
sheaf paper's wall in soldering variables (prop:whichwall); the Kasner wall
(prop:kasnerwall, prop:lambdacorr, prop:counterterm, lem:varexp).  C: the two
kinds of action and the norm of the scale tractor off the Einstein region
(thm:twokinds, prop:w); the thm:twokinds checks are the trace identities the
proof uses, algebraic identities rather than tests, and are labelled so.
D: symmetry orthogonality on a six-mode window (prop:nogo), including the
checks that both hypotheses are necessary.  E: the norm as a parameter of the
laws (prop:parameter): the free-Lambda constraint count, the norm mode
against the gauge images, and its identification with the tangent of the
rescaling family.
"""

from fractions import Fraction
from itertools import combinations, permutations
import GA as g

# ---------------------------------------------------------------------------
# the flat model R^{2,4}: slots (sigma, mu_0..mu_3, rho), form
# <u,v> = eta(mu,mu') + sigma rho' + rho sigma', eta = diag(+,-,-,-)
# ---------------------------------------------------------------------------

G = [[Fraction(x) for x in row] for row in [
    [0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0],
    [0, 0, -1, 0, 0, 0],
    [0, 0, 0, -1, 0, 0],
    [0, 0, 0, 0, -1, 0],
    [1, 0, 0, 0, 0, 0],
]]


def ip(u, v):
    return sum(u[i] * G[i][j] * v[j] for i in range(6) for j in range(6))


def basis(k):
    return [Fraction(1) if i == k else Fraction(0) for i in range(6)]


def biv_action(a, b, w):
    """(a ^ b) w = <b,w> a - <a,w> b."""
    ca, cb = ip(b, w), ip(a, w)
    return [ca * a[i] - cb * b[i] for i in range(6)]


def biv_matrix(a, b):
    """6x6 matrix of the bivector a ^ b acting on the fibre."""
    cols = [biv_action(a, b, basis(k)) for k in range(6)]
    return [[cols[k][i] for k in range(6)] for i in range(6)]


PAIRS = [(i, j) for i in range(6) for j in range(i + 1, 6)]

# rational-function versions of the same objects, in formal Lambda
Lam = g.RF.var()
R0, R1 = g.RF0, g.RF1


def rfc(c):
    return g.RF.const(Fraction(c))


def rf_vec(entries):
    return [e if isinstance(e, g.RF) else rfc(e) for e in entries]


G_rf = [[rfc(G[i][j]) for j in range(6)] for i in range(6)]


def ip_rf(u, v):
    tot = R0
    for i in range(6):
        for j in range(6):
            if G[i][j] != 0:
                tot = tot + u[i] * G_rf[i][j] * v[j]
    return tot


def biv_action_rf(a, b, w):
    ca, cb = ip_rf(b, w), ip_rf(a, w)
    return [ca * a[i] - cb * b[i] for i in range(6)]


def rf_vec_zero(v):
    return all(x.is_zero() for x in v)


def rf_vec_eq(u, v):
    return all(u[i].eqrf(v[i]) for i in range(6))


# ---------------------------------------------------------------------------
# Part A: the frozen point and the Stelle-West vector
# ---------------------------------------------------------------------------

I_rf = rf_vec([1, 0, 0, 0, 0, Lam / rfc(6)])
X_rf = rf_vec([0, 0, 0, 0, 0, 1])
normI = ip_rf(I_rf, I_rf)
g.check("thm:action/fact:frozen: <I,I> = Lambda/3 as a rational-function "
        "identity for I = (1,0,0,0,0,Lambda/6)", normI.eqrf(Lam / rfc(3)))

inv_norm = R1 / normI
g.check("thm:action(2): the prefactor 1/<I,I> = 3/Lambda has a simple pole at "
        "Lambda = 0 and nowhere else",
        inv_norm.eqrf(rfc(3) / Lam) and len(inv_norm.den) == 2
        and inv_norm.den[0] == 0)

# lem:sw (i): X null, <X,I> = 1, V = X - (3/Lambda) I orthogonal to I with
# norm -3/Lambda
three_over_L = rfc(3) / Lam
V_rf = [X_rf[i] - three_over_L * I_rf[i] for i in range(6)]
g.check("lem:sw(i): <X,X> = 0 and <X,I> = 1 for the canonical tractor X",
        ip_rf(X_rf, X_rf).is_zero() and ip_rf(X_rf, I_rf).eqrf(R1))
g.check("lem:sw(i): V = X - (3/Lambda) I satisfies <V,I> = 0 and "
        "<V,V> = -3/Lambda as rational-function identities",
        ip_rf(V_rf, I_rf).is_zero()
        and ip_rf(V_rf, V_rf).eqrf(-(rfc(3) / Lam)))

# W = V/<V,V> = (1,0,0,0,0,-Lambda/6)
W_rf = [V_rf[i] / ip_rf(V_rf, V_rf) for i in range(6)]
g.check("lem:sw: W = V/<V,V> = (1,0,0,0,0,-Lambda/6)",
        rf_vec_eq(W_rf, rf_vec([1, 0, 0, 0, 0, -(Lam / rfc(6))])))

# lem:sw (ii),(iii): the model connection bivector e_a ^ W annihilates I,
# sends X and V to e_a, and agrees with eq:conn on every basis tractor.
# eq:conn with P = (Lambda/6) eta, on a constant tractor (sigma, mu, rho), in
# contravariant mu-components:
#   sigma-slot -mu_a, mu^b-slot delta^b_a (rho - (Lambda/6) sigma),
#   rho-slot (Lambda/6) mu_a, where mu_a = eta_ab mu^b.
eta = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1)]


def conn_display(a, u):
    """Non-derivative part of eq:conn, in formal Lambda, for frame index a."""
    sigma, mu, rho = u[0], u[1:5], u[5]
    mu_a = rfc(eta[a]) * mu[a]
    out = [R0] * 6
    out[0] = -mu_a
    out[1 + a] = rho - (Lam / rfc(6)) * sigma
    out[5] = (Lam / rfc(6)) * mu_a
    return out


def e_vec_rf(a):
    # e_a = (0, g_ab, 0): covariant mu-slot g_ab, i.e. contravariant
    # components mu^b = delta^b_a: the unit vector of the a-th mu slot
    return rf_vec(basis(1 + a))


ok_I = ok_X = ok_V = ok_disp = True
for a in range(4):
    ea = e_vec_rf(a)
    ok_I = ok_I and rf_vec_zero(biv_action_rf(ea, W_rf, I_rf))
    ok_X = ok_X and rf_vec_eq(biv_action_rf(ea, W_rf, X_rf), ea)
    ok_V = ok_V and rf_vec_eq(biv_action_rf(ea, W_rf, V_rf), ea)
    for k in range(6):
        u = rf_vec(basis(k))
        ok_disp = ok_disp and rf_vec_eq(biv_action_rf(ea, W_rf, u),
                                        conn_display(a, u))
g.check("lem:sw(iii)/fact:frozen: the connection bivector e_a ^ W annihilates "
        "the frozen point I for every a (I is parallel in the model)", ok_I)
g.check("lem:sw(ii): (e_a ^ W) X = e_a: the derivative of the canonical "
        "tractor is the soldering form", ok_X)
g.check("lem:sw(ii): (e_a ^ W) V = e_a: the derivative of the Stelle-West "
        "vector is the soldering form", ok_V)
g.check("lem:sw(iii): e_a ^ W agrees with the display eq:conn (P = Lambda/6 "
        "eta) on all six basis tractors and all four a", ok_disp)

# lem:sw (iv): [e_a ^ W, e_b ^ W] = (Lambda/3) e_a ^ e_b as 6x6 matrices
def biv_matrix_rf(a, b):
    cols = [biv_action_rf(a, b, rf_vec(basis(k))) for k in range(6)]
    return [[cols[k][i] for k in range(6)] for i in range(6)]


def mmul_rf(A, B):
    out = [[R0] * 6 for _ in range(6)]
    for i in range(6):
        for j in range(6):
            tot = R0
            for k in range(6):
                tot = tot + A[i][k] * B[k][j]
            out[i][j] = tot
    return out


ok_br = True
for a in range(4):
    for b in range(4):
        if a == b:
            continue
        Ma = biv_matrix_rf(e_vec_rf(a), W_rf)
        Mb = biv_matrix_rf(e_vec_rf(b), W_rf)
        AB, BA = mmul_rf(Ma, Mb), mmul_rf(Mb, Ma)
        Eab = biv_matrix_rf(e_vec_rf(a), e_vec_rf(b))
        for i in range(6):
            for j in range(6):
                lhs = AB[i][j] - BA[i][j]
                rhs = (Lam / rfc(3)) * Eab[i][j]
                ok_br = ok_br and lhs.eqrf(rhs)
g.check("lem:sw(iv): [e_a ^ W, e_b ^ W] = (Lambda/3) e_a ^ e_b as a matrix "
        "identity in formal Lambda: the sign of the e^e term in F", ok_br)

# thm:action(iii): the slot count.  eps_6(I, ., B1, B2) is a fibre VECTOR
# (nonzero for generic bivectors); eps_6(I, V, B1, B2) = eps_6(I, X, B1, B2)
# is a scalar.  Rational instance Lambda = 3.
LAM = Fraction(3)
I_vec = [Fraction(1), 0, 0, 0, 0, LAM / 6]
I_vec = [Fraction(x) for x in I_vec]
X_vec = basis(5)
V_vec = [X_vec[i] - (3 / LAM) * I_vec[i] for i in range(6)]
g.check("fact:frozen: at Lambda = 3 the instance I = (1,0,0,0,0,1/2) has "
        "<I,I> = 1 = Lambda/3 exactly", ip(I_vec, I_vec) == Fraction(1))


def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def eps6_contract(vecs, bivs):
    """Contract the 6-form eps_{ABCDEF} with the given vectors (each a 6-list)
    and bivectors (each a dict {(i,j): coeff}, i<j); returns a dict over the
    remaining free multi-index (tuple), so a full contraction is {(): value}."""
    nfree = 6 - len(vecs) - 2 * len(bivs)
    out = {}
    for p in permutations(range(6)):
        s = perm_sign(p)
        coeff = Fraction(s)
        pos = 0
        for v in vecs:
            coeff *= v[p[pos]]
            pos += 1
            if coeff == 0:
                break
        if coeff == 0:
            continue
        for B in bivs:
            i, j = p[pos], p[pos + 1]
            pos += 2
            if i < j:
                coeff *= B.get((i, j), Fraction(0))
            else:
                coeff *= -B.get((j, i), Fraction(0))
            if coeff == 0:
                break
        if coeff == 0:
            continue
        free = tuple(p[pos:])
        out[free] = out.get(free, Fraction(0)) + coeff
    return {k: v for k, v in out.items() if v != 0}


B1 = {(1, 2): Fraction(2), (2, 3): Fraction(-1), (1, 4): Fraction(3),
      (3, 4): Fraction(1)}
B2 = {(1, 3): Fraction(1), (2, 4): Fraction(2), (1, 2): Fraction(-3),
      (0, 5): Fraction(1)}
# restrict the test bivectors to Lambda^2 I-perp is not needed for the slot
# count; the point is the free index.
vec_form = eps6_contract([I_vec], [B1, B2])
scalar_V = eps6_contract([I_vec, V_vec], [B1, B2])
scalar_X = eps6_contract([I_vec, X_vec], [B1, B2])
g.check("thm:action(iii): eps(I, ., B1, B2) with one vector slot filled is a "
        "nonzero fibre vector, not a scalar (an integrand eps_I<F^F> with one slot "
        "open is not a scalar)",
        len(vec_form) > 0 and all(len(k) == 1 for k in vec_form))
g.check("thm:action(iii): eps(I, V, B1, B2) is a scalar and equals "
        "eps(I, X, B1, B2) exactly (the I-component of V drops by "
        "antisymmetry)",
        list(scalar_V.keys()) in ([()], []) and scalar_V == scalar_X
        and scalar_X.get((), 0) != 0)

# stabiliser and Goldstone counting (prop:goldstone) at Lambda = 3
images = []
for (i, j) in PAIRS:
    images.append(biv_action(basis(i), basis(j), I_vec))
rankA = g.rank_of_vectors([list(v) for v in images])
g.check("prop:goldstone: the bivector algebra's image on the non-null I has "
        "rank exactly 5 (= dim I-perp), so the stabiliser has dimension "
        "15 - 5 = 10", rankA == 5)
g.check("prop:goldstone: every image vector is orthogonal to I (the broken "
        "generators map into the tangent space I-perp)",
        all(ip(v, I_vec) == 0 for v in images))

perp_rows = []
for k in range(6):
    e = basis(k)
    lam = ip(e, I_vec) / ip(I_vec, I_vec)
    perp_rows.append([e[i] - lam * I_vec[i] for i in range(6)])
rankP = g.rank_of_vectors([r[:] for r in perp_rows])
g.check("prop:goldstone: I-perp has dimension exactly 5, so the broken-to-"
        "tangent map is bijective by rank (5 onto 5, kernel = stabiliser cap "
        "complement = 0)", rankP == 5)

sel = []
for r in perp_rows:
    trial = sel + [r]
    if g.rank_of_vectors([t[:] for t in trial]) == len(trial):
        sel.append(r)
    if len(sel) == 5:
        break
Gram_perp = [[ip(a, b) for b in sel] for a in sel]
sig = g.congruence_signature(Gram_perp)
g.check("fact:frozen: the induced form on I-perp has signature (1,4): the de "
        "Sitter stabiliser SO(1,4) for Lambda > 0", sig == (1, 4, 0))


def perp_signature(vecs):
    """Signature of the induced form on the orthogonal complement of vecs."""
    rows = []
    for k in range(6):
        e = basis(k)
        for u in vecs:
            lam = ip(e, u) / ip(u, u)
            e = [e[i] - lam * u[i] for i in range(6)]
        rows.append(e)
    sel = []
    for r in rows:
        trial = sel + [r]
        if g.rank_of_vectors([t[:] for t in trial]) == len(trial):
            sel.append(r)
    Gram = [[ip(a, b) for b in sel] for a in sel]
    return len(sel), g.congruence_signature(Gram)


LAM_ADS = Fraction(-3)
I_ads = [Fraction(1), 0, 0, 0, 0, LAM_ADS / 6]
I_ads = [Fraction(x) for x in I_ads]
V_ads = [X_vec[i] - (3 / LAM_ADS) * I_ads[i] for i in range(6)]
g.check("thm:action(i) [anti-de Sitter branch, Lambda = -3]: <I,I> = -1 = Lambda/3, "
        "<V,V> = 1 = -3/Lambda, <I,V> = 0, and I-perp has signature (2,3)",
        ip(I_ads, I_ads) == -1 and ip(V_ads, V_ads) == 1 and ip(I_ads, V_ads) == 0
        and perp_signature([I_ads]) == (5, (2, 3, 0)))
g.check("thm:action(ii): {I,V}-perp has signature (1,3) on both branches "
        "(Lambda = 3 and Lambda = -3): the Lorentz fibre, so the stabiliser of the "
        "pair is so(1,3) either way",
        perp_signature([I_vec, V_vec]) == (4, (1, 3, 0))
        and perp_signature([I_ads, V_ads]) == (4, (1, 3, 0)))
# thm:action(iii) field-space clause: the I-leg components of an unconstrained
# ambient connection enter the curvature's Lorentz block quadratically:
# [I^u, I^v] = -<I,I> u^v for u, v orthogonal to I, and eps(I, V, u^v, B) != 0.
u_vec = basis(1)
w_vec = basis(2)
Mu = biv_matrix(I_vec, u_vec)
Mw = biv_matrix(I_vec, w_vec)
comm6 = [[sum(Mu[i][k] * Mw[k][j] - Mw[i][k] * Mu[k][j] for k in range(6)) for j in range(6)]
         for i in range(6)]
target = [[-ip(I_vec, I_vec) * x for x in row] for row in biv_matrix(u_vec, w_vec)]
uw = {(1, 2): Fraction(1)}
g.check("thm:action(iii) [field space]: [I^u, I^v] = -<I,I> u^v for u, v in I-perp, "
        "and eps(I, V, u^v, B1) != 0: the I-leg components nabla I of an unconstrained "
        "ambient connection would enter the Lorentz block of the curvature "
        "quadratically, which is why the field space is the connections with "
        "nabla I = 0",
        comm6 == target
        and eps6_contract([I_vec, V_vec], [uw, B1]).get((), Fraction(0)) != 0)

# prop:goldstone: the three-argument functional.  Joint action of the bivector
# algebra on the pair (I, V), and the one-argument failure with xi = I ^ V.
joint = [biv_action(basis(i), basis(j), I_vec) + biv_action(basis(i), basis(j), V_vec)
         for (i, j) in PAIRS]
g.check("prop:goldstone: the joint action xi -> (xi.I, xi.V) of the fifteen basis "
        "bivectors has rank exactly 9, so the stabiliser of the pair (I,V) has "
        "dimension 15 - 9 = 6 (the Lorentz algebra of {I,V}-perp)",
        g.rank_of_vectors(joint) == 9)
cons = []
for k in range(12):
    dI = basis(k) if k < 6 else [Fraction(0)] * 6
    dV = basis(k - 6) if k >= 6 else [Fraction(0)] * 6
    cons.append([ip(dI, I_vec), ip(dV, I_vec) + ip(V_vec, dI), ip(dV, V_vec)])
cons_T = [[cons[k][r] for k in range(12)] for r in range(3)]
g.check("prop:goldstone: the three linearised Stelle-West constraints are "
        "independent, so the constrained (I,V) fluctuation space has dimension "
        "12 - 3 = 9 = the number of broken generators", g.rank_of_vectors(cons_T) == 3)
xi_I = biv_action(I_vec, V_vec, I_vec)
xi_X = biv_action(I_vec, V_vec, X_vec)
g.check("prop:goldstone: with xi = I ^ V, xi.I = -(Lambda/3) V (a tangential "
        "fluctuation) and xi.X = -(3/Lambda) I - V",
        xi_I == [-(LAM / 3) * v for v in V_vec]
        and xi_X == [-(3 / LAM) * I_vec[i] - V_vec[i] for i in range(6)])
one_arg = eps6_contract([I_vec, xi_X], [B1, B2]).get((), Fraction(0))
full = eps6_contract([I_vec, V_vec], [B1, B2]).get((), Fraction(0))
# invariance of eps(I, V, B1, B2) under rational elements of SO(2,4): the
# null-pair scaling (sigma, rho) -> (3 sigma, rho/3) in the hyperbolic plane and a rotation
# (cos, sin) = (3/5, 4/5) in the definite plane (mu_1, mu_2), and their product


def apply_mat(Mx, u):
    return [sum(Mx[i][j] * u[j] for j in range(6)) for i in range(6)]


def apply_biv(Mx, B):
    """Push a bivector dict {(i,j): c} through the linear map Mx."""
    out = {}
    for (i, j), c in B.items():
        ui = [Mx[r][i] for r in range(6)]
        uj = [Mx[r][j] for r in range(6)]
        for r in range(6):
            for t in range(r + 1, 6):
                val = c * (ui[r] * uj[t] - ui[t] * uj[r])
                if val != 0:
                    out[(r, t)] = out.get((r, t), Fraction(0)) + val
    return {k: val for k, val in out.items() if val != 0}


boost = [[Fraction(1) if i == j else Fraction(0) for j in range(6)] for i in range(6)]
# in the (sigma, rho) plane with <sigma, rho> pairing: (sigma, rho) -> (a sigma, rho / a)
boost[0][0], boost[5][5] = Fraction(3), Fraction(1, 3)
rot = [[Fraction(1) if i == j else Fraction(0) for j in range(6)] for i in range(6)]
rot[2][2], rot[2][3], rot[3][2], rot[3][3] = Fraction(3, 5), Fraction(-4, 5), Fraction(4, 5), Fraction(3, 5)
prod = [[sum(boost[i][k] * rot[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
ok_inv = True
for Mx in (boost, rot, prod):
    # isometry check
    for i in range(6):
        for j in range(6):
            ok_inv = ok_inv and ip(apply_mat(Mx, basis(i)), apply_mat(Mx, basis(j))) == G[i][j]
    val = eps6_contract([apply_mat(Mx, I_vec), apply_mat(Mx, V_vec)],
                        [apply_biv(Mx, B1), apply_biv(Mx, B2)]).get((), Fraction(0))
    ok_inv = ok_inv and val == full
g.check("prop:goldstone: eps(gI, gV, gB1, gB2) = eps(I, V, B1, B2) for rational "
        "elements g of SO(2,4) (a boost, a rotation, their product; each confirmed "
        "an isometry): the integrand is invariant under the ambient group acting on "
        "all three arguments", ok_inv)
g.check("prop:goldstone: the one-argument version fails: eps(I, xi.X, B1, B2) = "
        "-eps(I, V, B1, B2) != 0, so acting on nabla and I with X held fixed is "
        "not a symmetry of the functional", one_arg == -full and full != 0)

# ---------------------------------------------------------------------------
# Part B: the wall's free sector (thm:wallfree)
# ---------------------------------------------------------------------------


def eps4(a, b, c, d):
    p = (a, b, c, d)
    if len(set(p)) < 4:
        return 0
    return perm_sign(p)


TRIPLES = list(combinations(range(4), 3))
PAIRS4 = [(m, n) for m in range(4) for n in range(m + 1, 4)]


def wedge_1_2(one, two):
    """(alpha ^ beta)_{mnr} for a 1-form alpha[m] and 2-form beta[(m,n)]
    (antisymmetric dict on ordered pairs m<n)."""
    def b(m, n):
        if m == n:
            return Fraction(0)
        return two.get((m, n), Fraction(0)) if m < n else -two.get((n, m), Fraction(0))
    out = {}
    for (m, n, r) in TRIPLES:
        out[(m, n, r)] = one[m] * b(n, r) - one[n] * b(m, r) + one[r] * b(m, n)
    return out


def torsion_matrix(e):
    """Rows: components (a<b, triple) of eps_{abcd} e^c ^ T^d; columns: the 24
    torsion components T^d_{mn}, m<n."""
    cols_idx = [(d, mn) for d in range(4) for mn in PAIRS4]
    rows = []
    for (a, b) in PAIRS4:
        for tri in TRIPLES:
            row = []
            for (d0, mn0) in cols_idx:
                T = {mn0: Fraction(1)}
                tot = Fraction(0)
                for c in range(4):
                    s = eps4(a, b, c, d0)
                    if s == 0:
                        continue
                    tot += s * wedge_1_2(e[c], T)[tri]
                row.append(tot)
            rows.append(row)
    return rows


def frame_matrix(e):
    """Rows: components (a, triple) of eps_{abcd} e^b ^ F^{cd}; columns: the
    36 curvature components F^{cd}_{mn}, c<d, m<n."""
    cols_idx = [(cd, mn) for cd in PAIRS4 for mn in PAIRS4]
    rows = []
    for a in range(4):
        for tri in TRIPLES:
            row = []
            for ((c0, d0), mn0) in cols_idx:
                F = {mn0: Fraction(1)}
                tot = Fraction(0)
                for b in range(4):
                    s = eps4(a, b, c0, d0)
                    if s == 0:
                        continue
                    # F^{cd} antisymmetric in cd: eps already carries the
                    # sign; both orderings of (c,d) sum to twice one of them
                    tot += 2 * s * wedge_1_2(e[b], F)[tri]
                row.append(tot)
            rows.append(row)
    return rows


def zero_rows(M):
    return sum(1 for r in M if all(x == 0 for x in r))


e_inv = [[Fraction(1) if m == a else Fraction(0) for m in range(4)] for a in range(4)]

# The three corank-one normal forms of the proof of thm:wallfree, by the type
# of the wall's tangent space (the image of e): Lorentzian (e^3 = 0),
# Riemannian (e^0 = 0) and null (e^0 = e^1 = dx^0).  Each entry is
# (name, e, dying frame index D, radical coordinate, Q), where e = Q f for an
# adapted frame f in which the dying frame direction is the single covector
# f^D = 0; Q is the identity for the first two and the null rotation
# e^0 = f^0 + f^1, e^1 = f^0 - f^1 for the third.  The torsion-level checks
# below are metric-free (only eps_{abcd} and e enter), so the adapted frame
# is a change of basis of rows (E_{ab}) and columns (T^d) by Q, under which
# the ranks are invariant and the vacated components become visible.
e_lor = [[Fraction(1) if (m == a and a < 3) else Fraction(0) for m in range(4)] for a in range(4)]
e_rie = [[Fraction(1) if (m == a and a > 0) else Fraction(0) for m in range(4)] for a in range(4)]
e_nul = [[Fraction(0)] * 4 for _ in range(4)]
e_nul[0][0] = Fraction(1); e_nul[1][0] = Fraction(1); e_nul[2][2] = Fraction(1); e_nul[3][3] = Fraction(1)
Q_id = [[Fraction(1) if i == j else Fraction(0) for j in range(4)] for i in range(4)]
Q_nul = [[Fraction(1), Fraction(1), Fraction(0), Fraction(0)],
         [Fraction(1), Fraction(-1), Fraction(0), Fraction(0)],
         [Fraction(0), Fraction(0), Fraction(1), Fraction(0)],
         [Fraction(0), Fraction(0), Fraction(0), Fraction(1)]]
FORMS = [("Lorentzian image, e^3 = 0", e_lor, 3, 3, Q_id),
         ("Riemannian image, e^0 = 0", e_rie, 0, 0, Q_id),
         ("null image, e^0 = e^1 = dx^0", e_nul, 1, 1, Q_nul)]
# sanity on the null adaptation: f = Q^{-1} e has f^1 = 0 and f^0 = dx^0
_f = [[(e_nul[0][m] - e_nul[1][m]) / 2 if a == 1 else
       ((e_nul[0][m] + e_nul[1][m]) / 2 if a == 0 else e_nul[a][m]) for m in range(4)] for a in range(4)]
assert all(_f[1][m] == 0 for m in range(4)) and _f[0][0] == 1


def adapt_rows(rows, Q, pairs=True):
    """Rows indexed by (frame pair a<b, triple) or (frame index a, triple):
    re-express them in the adapted frame f (e = Q f), E'_{a'b'} = Q^a_{a'} Q^b_{b'} E_{ab}."""
    nt = len(TRIPLES)
    out = []
    if pairs:
        for (a1, b1) in PAIRS4:
            for t in range(nt):
                acc = [Fraction(0)] * len(rows[0])
                for pi, (a, b) in enumerate(PAIRS4):
                    c = Q[a][a1] * Q[b][b1] - Q[b][a1] * Q[a][b1]
                    if c != 0:
                        acc = [x + c * y for x, y in zip(acc, rows[pi * nt + t])]
                out.append(acc)
    else:
        for a1 in range(4):
            for t in range(nt):
                acc = [Fraction(0)] * len(rows[0])
                for a in range(4):
                    if Q[a][a1] != 0:
                        acc = [x + Q[a][a1] * y for x, y in zip(acc, rows[a * nt + t])]
                out.append(acc)
    return out


def adapt_cols(rows, Q):
    """Columns T^d_{mn}: T = Q T', so the column of T'^{d'}_{mn} is sum_d Q^d_{d'} col(T^d_{mn})."""
    npairs = len(PAIRS4)
    out = []
    for r in rows:
        new = []
        for d1 in range(4):
            for pi in range(npairs):
                new.append(sum(Q[d][d1] * r[d * npairs + pi] for d in range(4)))
        out.append(new)
    return out


Tinv, Finv = torsion_matrix(e_inv), frame_matrix(e_inv)
g.check("thm:wallfree(a): on the invertible normal form the connection "
        "equation has rank 24 (torsion forced to vanish) and the frame "
        "equation has rank 16",
        g.rank_of_vectors(Tinv) == 24 and g.rank_of_vectors(Finv) == 16)
ok_18 = ok_vac = ok_16 = ok_inj = ok_3 = True
for (name, e_nf, D, rad, Q) in FORMS:
    Tw = adapt_cols(adapt_rows(torsion_matrix(e_nf), Q), Q)
    Fw = adapt_rows(frame_matrix(e_nf), Q, pairs=False)
    ok_18 = ok_18 and g.rank_of_vectors(Tw) == 18
    ok_vac = ok_vac and zero_rows(Tw) == 3
    ok_16 = ok_16 and g.rank_of_vectors(Fw) == 16 and zero_rows(Fw) == 0
    # the freed torsion components are tangential: in the adapted frame the
    # kernel lies in the span of T'^d_{mn} with d != D and rad not in {m, n}
    cols_idx = [(d, mn) for d in range(4) for mn in PAIRS4]
    tangential = [k for k, (d, (m, n)) in enumerate(cols_idx) if d != D and rad not in (m, n)]
    nontan = [k for k in range(24) if k not in tangential]
    Tsub = [[row[k] for k in nontan] for row in Tw]
    ok_inj = ok_inj and g.rank_of_vectors(Tsub) == len(nontan) == 15 and len(tangential) == 9
    Ttan = [[row[k] for k in tangential] for row in Tw]
    ok_3 = ok_3 and g.rank_of_vectors(Ttan) == 3
g.check("thm:wallfree(a): at each of the three corank-one normal forms "
        "(Lorentzian, Riemannian, null image) the connection equation has rank "
        "exactly 18: six torsion components freed", ok_18)
g.check("thm:wallfree(a): at each normal form exactly 3 of the 24 components of "
        "the wall connection equation are identities 0 = 0 (vacated; in the "
        "frame adapted to the dying direction)", ok_vac and zero_rows(Tinv) == 0)
g.check("thm:wallfree(a): at each normal form the frame equation keeps rank 16 "
        "and no component is identically zero", ok_16)
g.check("thm:wallfree(a): at each normal form the wall connection equation is "
        "injective on the 15 non-tangential torsion components (radical-leg and "
        "cokernel components all forced to zero), so the 6 freed components are "
        "tangential", ok_inj)
g.check("thm:wallfree(a): at each normal form, on the 9 tangential components "
        "the wall connection equation imposes exactly 3 conditions", ok_3)
e_wall = e_lor

# the withdrawn claim: radical components of the frame equation vanish.
# Explicit integer instance: they do not.
Fint = {}
seed = 7
for cd in PAIRS4:
    for mn in PAIRS4:
        seed = (seed * 31 + 11) % 17
        Fint[(cd, mn)] = Fraction(seed - 8)


def E_component(a, tri, e, F):
    tot = Fraction(0)
    for b in range(4):
        for (c, d) in PAIRS4:
            s = eps4(a, b, c, d)
            if s == 0:
                continue
            Fcd = {mn: F[((c, d), mn)] for mn in PAIRS4}
            tot += 2 * s * wedge_1_2(e[b], Fcd)[tri]
    return tot


radical_nonzero = 0
for a in range(4):
    for tri in TRIPLES:
        if 3 in tri:  # components with the radical leg d/dx^3
            if E_component(a, tri, e_wall, Fint) != 0:
                radical_nonzero += 1
cokernel_nonzero = sum(1 for tri in TRIPLES
                       if E_component(3, tri, e_wall, Fint) != 0)
g.check("thm:wallfree(a): the withdrawn radical-vanishing claim fails: for an explicit "
        "integer curvature the radical components E_a(d_3, ., .) are nonzero "
        "(%d of 12) and so are cokernel components E_3 (%d of 4)"
        % (radical_nonzero, cokernel_nonzero),
        radical_nonzero > 0 and cokernel_nonzero > 0)


# --- connection level, propagation, and the Hamiltonian component
# (thm:wallfree (b), (c), (d)); run for all three types of dying direction

ETA4 = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1)]
OMEGA_IDX = [(p, mu) for p in PAIRS4 for mu in range(4)]      # 24 components


def om_get(om, a, b, mu):
    """omega^{ab}_mu with antisymmetry in (a, b)."""
    if a == b:
        return Fraction(0)
    if a < b:
        return om.get(((a, b), mu), Fraction(0))
    return -om.get(((b, a), mu), Fraction(0))


def om_mixed(om, a, b, mu):
    """omega^a_b mu = omega^{ac}_mu eta_cb."""
    return om_get(om, a, b, mu) * ETA4[b]


def torsion_of(om, e):
    """T^a_{mn} = omega^a_{b m} e^b_n - omega^a_{b n} e^b_m (de = 0)."""
    T = {}
    for a in range(4):
        for m in range(4):
            for n in range(4):
                T[(a, m, n)] = sum(om_mixed(om, a, b, m) * e[b][n]
                                   - om_mixed(om, a, b, n) * e[b][m]
                                   for b in range(4))
    return T


def conn_eq_on_omega(e):
    rows = []
    for (a, b) in PAIRS4:
        for (m, n, r) in TRIPLES:
            row = []
            for u in OMEGA_IDX:
                T = torsion_of({u: Fraction(1)}, e)
                tot = Fraction(0)
                for c in range(4):
                    for d in range(4):
                        s4 = eps4(a, b, c, d)
                        if s4 == 0:
                            continue
                        tot += s4 * (e[c][m] * T[(d, n, r)] - e[c][n] * T[(d, m, r)]
                                     + e[c][r] * T[(d, m, n)])
                row.append(tot)
            rows.append(row)
    return rows


def kernel_basis(rows, ncols):
    """Exact kernel basis by row reduction over Fraction."""
    M = [r[:] for r in rows]
    piv_cols, rk = [], 0
    for c in range(ncols):
        piv = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        M[rk] = [x / M[rk][c] for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        piv_cols.append(c)
        rk += 1
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncols
        v[f] = Fraction(1)
        for i, p in enumerate(piv_cols):
            v[p] = -M[i][f]
        basis.append(v)
    return basis


def frame_symbol(e, direction):
    """Principal part of eps_{abcd} e^b ^ d omega^{cd} with d -> dx^dir d_dir:
    rows (a, triple), columns the 24 components d_dir omega^{cd}_nu."""
    rows = []
    for a in range(4):
        for (m, n, r) in TRIPLES:
            row = []
            for ((c, d), nu) in OMEGA_IDX:
                two = {}
                if direction != nu:
                    key = (min(direction, nu), max(direction, nu))
                    two[key] = Fraction(1 if direction < nu else -1)
                tot = Fraction(0)
                for b in range(4):
                    for (cc, dd) in ((c, d), (d, c)):
                        s4 = eps4(a, b, cc, dd)
                        if s4 == 0:
                            continue
                        sg = 1 if (cc, dd) == (c, d) else -1
                        w = wedge_1_2(e[b], {k: sg * v for k, v in two.items()})
                        tot += s4 * w[(m, n, r)]
                row.append(tot)
            rows.append(row)
    return rows


def frame_full_const(om, e, lam_over_3=Fraction(0)):
    """Full frame equation for constant omega (d omega = 0):
    eps_{abcd} e^b ^ (omega^c_f ^ omega^{fd} + lam e^c ^ e^d)."""
    Rt = {}
    for c in range(4):
        for d in range(4):
            for m in range(4):
                for n in range(4):
                    v = sum(om_mixed(om, c, f, m) * om_get(om, f, d, n)
                            - om_mixed(om, c, f, n) * om_get(om, f, d, m)
                            for f in range(4))
                    v += lam_over_3 * (e[c][m] * e[d][n] - e[c][n] * e[d][m])
                    Rt[(c, d, m, n)] = v
    out = {}
    for a in range(4):
        for (m, n, r) in TRIPLES:
            tot = Fraction(0)
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        s4 = eps4(a, b, c, d)
                        if s4 == 0:
                            continue
                        tot += s4 * (e[b][m] * Rt[(c, d, n, r)] - e[b][n] * Rt[(c, d, m, r)]
                                     + e[b][r] * Rt[(c, d, m, n)])
            out[(a, (m, n, r))] = tot
    return out


def lin_comb(vecs, coeffs):
    om = {}
    for v, c in zip(vecs, coeffs):
        for k in range(24):
            if v[k] != 0:
                om[OMEGA_IDX[k]] = om.get(OMEGA_IDX[k], Fraction(0)) + c * v[k]
    return om


def sigma2p(A):
    tr = sum(A[i][i] for i in range(3))
    return tr * tr - sum(A[i][j] * A[j][i] for i in range(3) for j in range(3))


# the normal forms FORMS are defined with the torsion-level checks above

seedval = 5


def pseudo(n):
    global seedval
    seedval = (seedval * 1103515245 + 12345) % (2 ** 31)
    return Fraction((seedval >> 8) % (2 * n + 1) - n)


for (name, e_nf, D, rad, Q) in FORMS:
    rows = conn_eq_on_omega(e_nf)
    Kb = kernel_basis(rows, 24)
    g.check("thm:wallfree(b) [%s]: the connection equation has rank 12 on the "
            "24 components of omega: 12 free" % name,
            g.rank_of_vectors(rows) == 12 and len(Kb) == 12)
    # symbols on the free sector
    ranks = []
    for d in range(4):
        S = frame_symbol(e_nf, d)
        Kmat = [[sum(row[k] * v[k] for k in range(24)) for v in Kb] for row in S]
        ranks.append(g.rank_of_vectors(Kmat))
    tang = [ranks[d] for d in range(4) if d != rad]
    g.check("thm:wallfree(c) [%s]: the frame equation's principal symbol on "
            "the 12 free components has rank 6 in the radical direction and 3 "
            "in each tangential direction (six components never differentiated)"
            % name, ranks[rad] == 6 and tang == [3, 3, 3])
    # quadratic frame equation on the free sector: one component only
    om1 = lin_comb(Kb, [pseudo(4) for _ in Kb])
    om2 = lin_comb(Kb, [pseudo(4) for _ in Kb])
    E1 = frame_full_const(om1, e_nf)
    nz = [k for k, v in E1.items() if v != 0]
    tang_triple = tuple(i for i in range(4) if i != rad)
    # the cokernel covector n (n_a e^a = 0) picks out the one surviving
    # component n^a E_a; for the null form n = (1,-1,0,0) and E_0 = -E_1
    one_comp = (len(nz) >= 1 and all(k[1] == tang_triple for k in nz)
                and len({k[0] for k in nz}) <= 2)
    if not name.startswith("null"):
        one_comp = one_comp and len(nz) == 1 and nz[0][0] == rad
    else:
        one_comp = one_comp and {k[0] for k in nz} == {0, 1} \
            and E1[(0, tang_triple)] == -E1[(1, tang_triple)]
    g.check("thm:wallfree(d) [%s]: on the free sector the quadratic frame "
            "equation has exactly one surviving component, the cokernel "
            "component on the three tangential directions" % name, one_comp)

# The K/M description of thm:wallfree(b), (d) at the two normal forms whose
# wall metric is nondegenerate (Lorentzian and Riemannian images).  With D the
# dying frame index and W the three wall indices: K^a_b = omega^a_{D b} (the
# boost components into the dying direction, a, b in W, b a tangential leg)
# and M_{c mu} = 1/2 eps_{c a b D} omega^{ab}_mu (the dualised tangential
# connection), indices raised and lowered with the wall metric eta|_W.  At
# the null image the wall metric is degenerate (the dying direction lies in
# the wall) and the free sector does not split as K (+) M; there the script
# confirms the counts (rank 12, symbols, one surviving component) above and
# the cosmological coefficient below, and nothing more.


def eps3(a, b, c):
    return eps4(a, b, c, 3)


def K_mixed(om, D=3):      # K^a_b = omega^a_{D b}, a, b in W
    W = [a for a in range(4) if a != D]
    return [[om_mixed(om, a, D, b) for b in W] for a in W]


def M_lower(om, D=3):      # M_{c mu} = 1/2 eps_{c a b D} omega^{ab}_mu
    W = [a for a in range(4) if a != D]
    return [[sum(eps4(c, a, b, D) * om_get(om, a, b, mu) for a in W for b in W) / 2
             for mu in W] for c in W]


def M_mixed(om, D=3):      # M^c_mu = eta^{cc} M_{c mu}
    W = [a for a in range(4) if a != D]
    Ml = M_lower(om, D)
    return [[ETA4[W[c]] * Ml[c][mu] for mu in range(3)] for c in range(3)]


ok_sym = ok_rad = ok_12 = ok_66 = ok_h = True
lam_sign = {}
for (name, e_nf, D, rad, Q) in FORMS:
    W = [a for a in range(4) if a != D]
    tri = tuple(W)
    if name.startswith("null"):
        # the surviving pair E_0 = -E_1 on the tangential triple carries the
        # cosmological term with coefficient 6 * (Lambda/3) and -6 * (Lambda/3)
        E0 = frame_full_const({}, e_nf, Fraction(1))[(0, tri)]
        E1 = frame_full_const({}, e_nf, Fraction(1))[(1, tri)]
        lam_sign[name] = (E0, E1)
        continue
    rows = conn_eq_on_omega(e_nf)
    Kb = kernel_basis(rows, 24)
    for v in Kb:
        om = lin_comb([v], [Fraction(1)])
        Km = K_mixed(om, D)
        Kl = [[ETA4[W[a]] * Km[a][b] for b in range(3)] for a in range(3)]
        Ml = M_lower(om, D)
        ok_sym = ok_sym and all(Kl[a][b] == Kl[b][a] for a in range(3) for b in range(3)) \
            and all(Ml[a][b] == Ml[b][a] for a in range(3) for b in range(3))
        ok_rad = ok_rad and all(om.get((p, rad), Fraction(0)) == 0 for p in PAIRS4)
    ok_12 = ok_12 and len(Kb) == 12
    Kc = [v for v in Kb if any(v[k] != 0 and D in OMEGA_IDX[k][0] for k in range(24))]
    Mc = [v for v in Kb if all(D not in OMEGA_IDX[k][0] for k in range(24) if v[k] != 0)]
    ok_66 = ok_66 and len(Kc) == 6 and len(Mc) == 6
    for trial in range(4):
        omK = lin_comb(Kc, [pseudo(4) for _ in Kc])
        omM = lin_comb(Mc, [pseudo(4) for _ in Mc])
        both = dict(omK)
        for k, v in omM.items():
            both[k] = both.get(k, Fraction(0)) + v
        EK = frame_full_const(omK, e_nf)[(D, tri)]
        EM = frame_full_const(omM, e_nf)[(D, tri)]
        EB = frame_full_const(both, e_nf)[(D, tri)]
        ok_h = ok_h and EK == -sigma2p(K_mixed(omK, D)) and EM == sigma2p(M_mixed(omM, D)) \
            and EB == EK + EM
    lam_sign[name] = frame_full_const({}, e_nf, Fraction(1))[(D, tri)]
g.check("thm:wallfree(b) [Lorentzian and Riemannian images]: every free connection "
        "component has K_{ab} and M_{c mu} symmetric and no radial-leg component "
        "omega^{ab}_r", ok_sym and ok_rad)
# dimension count: the symmetric parts are 6 + 6 = 12 = kernel dimension
g.check("thm:wallfree(b) [Lorentzian and Riemannian images]: the free sector is "
        "exactly Sym^2 (+) Sym^2, 6 + 6 = 12 components", ok_12)
g.check("thm:wallfree(b) [Lorentzian and Riemannian images]: the kernel splits as "
        "6 boost components (K) and 6 tangential components (M)", ok_66)
g.check("thm:wallfree(d) [Lorentzian and Riemannian images]: E_D(tangential triple) "
        "= sigma_2'(M) - sigma_2'(K) exactly on the free sector, with vanishing "
        "cross term (D the dying frame index)", ok_h)
g.check("thm:wallfree(d): the cosmological term contributes -6 * (Lambda/3) = "
        "-2 Lambda to the Hamiltonian component E_3 at the Lorentzian image; at the "
        "Riemannian image E_0 carries +6 * (Lambda/3), so there the constraint reads "
        "sigma_2'(K) - sigma_2'(M) - 2 Lambda = 0; at the null image the surviving "
        "pair carries E_0 = +6 * (Lambda/3) = -E_1",
        lam_sign["Lorentzian image, e^3 = 0"] == -6
        and lam_sign["Riemannian image, e^0 = 0"] == 6
        and lam_sign["null image, e^0 = e^1 = dx^0"] == (6, -6))


# --- prop:whichwall: the sheaf paper's wall in soldering variables

# (ii) stabiliser of the degenerate internal cometric eta = diag(0, -1, -1, -1)
eta_deg = [[Fraction(0)] * 4 for _ in range(4)]
for i in (1, 2, 3):
    eta_deg[i][i] = Fraction(-1)
rows = []
for a in range(4):
    for b in range(a, 4):
        row = [Fraction(0)] * 16
        for i in range(4):
            for j in range(4):
                if i == a:
                    row[4 * i + j] += eta_deg[j][b]
                if i == b:
                    row[4 * i + j] += eta_deg[a][j]
        rows.append(row)
stab4 = kernel_basis(rows, 16)
g.check("prop:whichwall(ii): the stabiliser algebra of the degenerate internal "
        "cometric diag(0, eta_3) in gl(4) has dimension 7 (Lorentz 6 -> 7: one "
        "new generator)", len(stab4) == 7)
# the new generator: u = 0 forced, alpha free
ok_u = all(all(v[4 * 0 + j] == 0 for j in (1, 2, 3)) for v in stab4)
ok_alpha = any(v[0] != 0 for v in stab4)
g.check("prop:whichwall(ii): the stabiliser has u = 0 (no rotation of the "
        "dying direction into the surviving ones) and contains the dilation "
        "alpha of the dying line", ok_u and ok_alpha)

# (iii) ambient: basis (k, m1, m2, m3, k*, w); <k,k*> = 1, <m_i,m_j> = -delta,
# <w,w> = +1: signature (2,4).  Elements of so(h) preserving P = span(k, m).
hh = [[Fraction(0)] * 6 for _ in range(6)]
hh[0][4] = hh[4][0] = Fraction(1)
for i in (1, 2, 3):
    hh[i][i] = Fraction(-1)
hh[5][5] = Fraction(1)
g.check("prop:whichwall(iii): the ambient form on (k, m, k*, w) has signature "
        "(2,4)", g.congruence_signature(hh) == (2, 4, 0))
rows = []
for a in range(6):
    for b in range(a, 6):
        row = [Fraction(0)] * 36
        for i in range(6):
            for j in range(6):
                if j == a:
                    row[6 * i + j] += hh[i][b]
                if j == b:
                    row[6 * i + j] += hh[a][i]
        rows.append(row)
for i in (4, 5):
    for j in range(4):
        row = [Fraction(0)] * 36
        row[6 * i + j] = Fraction(1)
        rows.append(row)
stab6 = kernel_basis(rows, 36)
g.check("prop:whichwall(iii): the subalgebra of so(2,4) preserving the "
        "degenerate four-plane P has dimension 8", len(stab6) == 8)
restr = [[v[6 * i + j] for i in range(4) for j in range(4)] for v in stab6]
g.check("prop:whichwall(iii): its restriction to P is the full 7-dimensional "
        "stabiliser of (ii) (surjective, one-dimensional kernel)",
        g.rank_of_vectors(restr) == 7)
# lift of the dilation: solve for the element restricting to diag(1,0,0,0)
target = [Fraction(1) if (i == 0 and j == 0) else Fraction(0)
          for i in range(4) for j in range(4)]
aug = [[restr[l][t] for l in range(len(stab6))] + [target[t]] for t in range(16)]
# solve by elimination
Mx = [r[:] for r in aug]
piv_cols, rk = [], 0
for c in range(len(stab6)):
    piv = next((i for i in range(rk, len(Mx)) if Mx[i][c] != 0), None)
    if piv is None:
        continue
    Mx[rk], Mx[piv] = Mx[piv], Mx[rk]
    Mx[rk] = [x / Mx[rk][c] for x in Mx[rk]]
    for i in range(len(Mx)):
        if i != rk and Mx[i][c] != 0:
            f = Mx[i][c]
            Mx[i] = [x - f * y for x, y in zip(Mx[i], Mx[rk])]
    piv_cols.append(c)
    rk += 1
sol = [Fraction(0)] * len(stab6)
for i, pc in enumerate(piv_cols):
    sol[pc] = Mx[i][-1]
consistent = all(all(x == 0 for x in Mx[i][:-1]) <= (Mx[i][-1] == 0) for i in range(len(Mx)))
Alift = [[sum(sol[l] * stab6[l][6 * i + j] for l in range(len(stab6))) for j in range(6)]
         for i in range(6)]
expect = [[Fraction(0)] * 6 for _ in range(6)]
expect[0][0] = Fraction(1)
expect[4][4] = Fraction(-1)
g.check("prop:whichwall(iii): the dilation of the dying line lifts to "
        "k -> k, k* -> -k*, surviving directions and w fixed: the so(1,1) "
        "boost of the ladder plane, the rescaling k -> ck, k* -> k*/c of the "
        "sheaf paper's residue theorem", consistent and Alift == expect)


# --- prop:kasnerwall: the frozen-point datum at a Kasner wall.  Exact in the
# variable s with tau = s^N and p_i = n_i/N, so that every power is integral.

RFs = g.RF.var()
RF1, RF0 = g.RF1, g.RF0


def rfk(x):
    return g.RF.const(Fraction(x))


def spow(n):
    r = RF1
    for _ in range(abs(n)):
        r = r * RFs
    return r if n >= 0 else RF1 / r


def kasner_data(N, np_):
    """Orthonormal coframe e^0 = dtau = N s^{N-1} ds, e^i = s^{n_i} dx^i;
    returns (torsion-free ok, curvature formulas ok, Ricci diagonal entries * tau^2
    as RFs, Gauss-Bonnet density check ok)."""
    eta = [1, -1, -1, -1]
    tau = spow(N)
    e = [{0: rfk(N) * spow(N - 1)}] + [{i + 1: spow(np_[i])} for i in range(3)]

    def d1(f):
        return {(0, k): v.deriv() for k, v in f.items() if k != 0}

    def w11(a, b):
        out = {}
        for ka, va in a.items():
            for kb, vb in b.items():
                if ka == kb:
                    continue
                key = (min(ka, kb), max(ka, kb))
                sg = RF1 if ka < kb else -RF1
                out[key] = out.get(key, RF0) + sg * va * vb
        return out

    def add2(a, b):
        return {k: a.get(k, RF0) + b.get(k, RF0) for k in set(a) | set(b)}

    om = {}
    for i in range(1, 4):
        om[(i, 0)] = {k: v * rfk(Fraction(np_[i - 1], N)) / tau for k, v in e[i].items()}
        om[(0, i)] = {k: -v for k, v in om[(i, 0)].items()}

    def omega(a, b):
        return om.get((a, b), {})

    ok_t = True
    for a in range(4):
        T = d1(e[a])
        for b in range(4):
            T = add2(T, w11({k: v * rfk(eta[b]) for k, v in omega(a, b).items()}, e[b]))
        ok_t = ok_t and all(v.is_zero() for v in T.values())
    R = {}
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            cur = d1(omega(a, b))
            for cc in range(4):
                cur = add2(cur, w11({k: v * rfk(eta[cc]) for k, v in omega(a, cc).items()},
                                    omega(cc, b)))
            R[(a, b)] = cur

    def comp(two, a, b):
        f = rfk(N) * spow(N - 1) * spow(np_[b - 1]) if a == 0 else spow(np_[a - 1] + np_[b - 1])
        return two.get((a, b), RF0) / f

    p = [Fraction(x, N) for x in np_]
    ok_R = True
    for i in range(1, 4):
        ok_R = ok_R and comp(R[(i, 0)], 0, i).eqrf(rfk(p[i - 1] * (p[i - 1] - 1)) / (tau * tau))
        for j in range(i + 1, 4):
            ok_R = ok_R and comp(R[(i, j)], i, j).eqrf(-rfk(p[i - 1] * p[j - 1]) / (tau * tau))

    def Rabcd(a, b, cc, d):
        if a == b or cc == d:
            return RF0
        sg = RF1
        if cc > d:
            cc, d, sg = d, cc, -RF1
        return sg * comp(R[(a, b)], cc, d)

    # Ricci in the convention of T6 (de Sitter has Ric = +Lambda g in the
    # mostly-minus signature, so that P = (Lambda/6) g and I is parallel):
    # Ric_{bd} = - sum_a R^a_{b a d}, with R^a_{bcd} = R^{ae}_{cd} eta_{eb}.
    ric = [[RF0] * 4 for _ in range(4)]
    for b in range(4):
        for d in range(4):
            tot = RF0
            for a in range(4):
                tot = tot - Rabcd(a, b, a, d) * rfk(eta[b])
            ric[b][d] = tot
    offdiag = all(ric[a][b].is_zero() for a in range(4) for b in range(4) if a != b)
    gb = RF0
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    sg = eps4(a, b, cc, d)
                    if sg == 0:
                        continue
                    tot = RF0
                    for (m, n) in PAIRS4:
                        pq = [x for x in range(4) if x not in (m, n)]
                        tot = tot + rfk(eps4(m, n, pq[0], pq[1])) * Rabcd(a, b, m, n) \
                            * Rabcd(cc, d, pq[0], pq[1])
                    gb = gb + rfk(sg) * tot
    volcoef = rfk(N) * spow(N - 1) * spow(sum(np_))
    S1, S2 = sum(p), sum(x * x for x in p)
    # GB density claim uses sum(p_i - 1) = -2 only on Kasner; general form:
    claim = rfk(8 * p[0] * p[1] * p[2] * (S1 - 3)) / (tau ** 4 if False else (tau * tau * tau * tau)) \
        * rfk(N) * spow(N - 1) * spow(sum(np_))
    ok_gb = (gb * volcoef).eqrf(claim)
    ric_tau2 = [ric[i][i] * tau * tau for i in range(4)]
    return ok_t, ok_R, offdiag, ric_tau2, ok_gb, p, S1, S2


for (N, np_) in ((3, (-1, 2, 2)), (7, (-2, 3, 6))):
    ok_t, ok_R, offdiag, rt, ok_gb, p, S1, S2 = kasner_data(N, np_)
    g.check("prop:kasnerwall(i) [p = %s]: omega^{i0} = (p_i/tau) e^i is torsion-free and "
            "its curvature is R^{i0} = p_i(p_i-1) tau^-2 e^0 e^i, R^{ij} = -p_i p_j "
            "tau^-2 e^i e^j, exactly" % (tuple(str(x) for x in p),), ok_t and ok_R)
    g.check("prop:kasnerwall(ii) [p = %s]: Kasner relations hold and the Ricci tensor "
            "vanishes identically (vacuum), off-diagonal included"
            % (tuple(str(x) for x in p),),
            S1 == 1 and S2 == 1 and offdiag and all(x.is_zero() for x in rt))
    g.check("prop:kasnerwall(iii) [p = %s]: eps_{abcd} R^{ab} ^ R^{cd} = -16 p1 p2 p3 "
            "tau^-3 dtau d^3x exactly (= %s tau^-3)"
            % (tuple(str(x) for x in p), str(-16 * p[0] * p[1] * p[2])), ok_gb)
# non-Kasner point: Ricci formulas hold and are nonzero
ok_t, ok_R, offdiag, rt, ok_gb, p, S1, S2 = kasner_data(5, (1, 1, 2))
g.check("prop:kasnerwall(ii) [non-Kasner p = (1/5,1/5,2/5)]: tau^2 R_00 = S2 - S1 "
        "and tau^2 R_ii = -p_i (S1 - 1) in T6's convention (de Sitter Ric = +Lambda g), "
        "nonzero, off-diagonal zero: the field equations at the wall are the Kasner "
        "relations",
        ok_t and ok_R and offdiag and rt[0].eqrf(rfk(S2 - S1))
        and all(rt[i].eqrf(rfk(-p[i - 1] * (S1 - 1))) for i in range(1, 4))
        and not rt[0].is_zero())
# the degenerate Kasner point (1,0,0), excluded by prop:kasnerwall's hypothesis
# p1 p2 p3 != 0: every curvature coefficient and the Gauss-Bonnet density vanish
ok_t, ok_R, offdiag, rt, ok_gb, p, S1, S2 = kasner_data(1, (1, 0, 0))
g.check("prop:kasnerwall [excluded point p = (1,0,0)]: a Kasner point with "
        "p1 p2 p3 = 0 is flat Milne: Ricci zero, the displayed curvature "
        "coefficients zero and the Gauss-Bonnet density zero, so the hypothesis "
        "p1 p2 p3 != 0 is needed for (i) and (iii)",
        S1 == 1 and S2 == 1 and ok_t and ok_R and all(x.is_zero() for x in rt)
        and ok_gb and p[0] * p[1] * p[2] == 0)
g.check("prop:kasnerwall(iii) [arithmetic of the printed constant]: -16 p1 p2 p3 at "
        "(-1/3, 2/3, 2/3) equals 64/27",
        -16 * Fraction(-1, 3) * Fraction(2, 3) * Fraction(2, 3) == Fraction(64, 27))
# B_w = sum_i p_i e_0 ^ e_i as a 4x4 matrix in the Lorentz fibre (eta = +,-,-,-),
# (a^b) w = <b,w> a - <a,w> b; B_w^2 should be (sum p_i^2) = 1 on the boost plane
# span(e_0, p_hat) and 0 on its orthogonal complement.


def unit_boost_check(p):
    ETA4L = [Fraction(1), Fraction(-1), Fraction(-1), Fraction(-1)]

    def ip4(u, w):
        return sum(ETA4L[i] * u[i] * w[i] for i in range(4))

    def e4(k):
        return [Fraction(1) if i == k else Fraction(0) for i in range(4)]

    def Bw(w):
        out = [Fraction(0)] * 4
        for i in range(3):
            a, b = e4(0), e4(i + 1)
            ca, cb = ip4(b, w), ip4(a, w)
            for r in range(4):
                out[r] += p[i] * (ca * a[r] - cb * b[r])
        return out
    phat = [Fraction(0)] + list(p)
    ok = True
    for w in (e4(0), phat):
        ww = Bw(Bw(w))
        s2 = sum(x * x for x in p)
        ok = ok and ww == [s2 * x for x in w]
    # a spatial vector orthogonal to p_hat is annihilated
    # two independent spatial vectors orthogonal to p_hat span its complement
    for q in ([Fraction(0), p[1], -p[0], Fraction(0)], [Fraction(0), p[2], Fraction(0), -p[0]]):
        ok = ok and Bw(q) == [Fraction(0)] * 4
    return ok


g.check("prop:kasnerwall(ii): the residue bivector B_w = sum p_i e_0^e_i squares to "
        "(sum p_i^2) = 1 on its boost plane and to 0 on the orthogonal spatial "
        "directions, formed exactly at both rational Kasner points: a unit boost",
        all(unit_boost_check([Fraction(x, N) for x in np_])
            for (N, np_) in ((3, (-1, 2, 2)), (7, (-2, 3, 6)))))


# --- prop:counterterm: the Chern-Simons primitive on the Kasner connection,
# and prop:lambdacorr: the Bianchi I series with Lambda.

def forms_kasner(N, np_):
    """Exact differential-form algebra on coords (s,x,y,z) with coefficients
    rational in s; returns the Kasner connection omega and curvature R as
    dicts of forms (keys: sorted coordinate tuples)."""
    eta = [1, -1, -1, -1]
    tau = spow(N)

    def wedge(a, b):
        out = {}
        for ka, va in a.items():
            for kb, vb in b.items():
                if set(ka) & set(kb):
                    continue
                arr = list(ka) + list(kb)
                sg = 1
                for i in range(len(arr)):
                    for j in range(len(arr) - 1 - i):
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                            sg = -sg
                key = tuple(arr)
                out[key] = out.get(key, RF0) + rfk(sg) * va * vb
        return out

    def dform(a):
        out = {}
        for k, v in a.items():
            if 0 in k:
                continue
            key = (0,) + k
            out[key] = out.get(key, RF0) + v.deriv()
        return out

    def add(a, b, sb=RF1):
        return {k: a.get(k, RF0) + sb * b.get(k, RF0) for k in set(a) | set(b)}

    def scal(a, f):
        return {k: v * f for k, v in a.items()}

    e = [{(0,): rfk(N) * spow(N - 1)}] + [{(i + 1,): spow(np_[i])} for i in range(3)]
    om = {}
    for i in range(1, 4):
        om[(i, 0)] = scal(e[i], rfk(Fraction(np_[i - 1], N)) / tau)
        om[(0, i)] = scal(om[(i, 0)], -RF1)

    def W(a, b):
        return om.get((a, b), {})

    R = {}
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            cur = dform(W(a, b))
            for cc in range(4):
                cur = add(cur, wedge(scal(W(a, cc), rfk(eta[cc])), W(cc, b)))
            R[(a, b)] = cur
    GB = {}
    Q = {}
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    sg = eps4(a, b, cc, d)
                    if not sg:
                        continue
                    GB = add(GB, wedge(R[(a, b)], R[(cc, d)]), rfk(sg))
                    t1 = wedge(W(a, b), dform(W(cc, d)))
                    t2 = {}
                    for ee in range(4):
                        t2 = add(t2, wedge(wedge(W(a, b), scal(W(cc, ee), rfk(eta[ee]))), W(ee, d)))
                    Q = add(Q, add(t1, scal(t2, rfk(Fraction(2, 3)))), rfk(sg))
    dQ = dform(Q)
    diff = add(GB, dQ, -RF1)
    return all(v.is_zero() for v in diff.values()), Q.get((1, 2, 3), RF0), tau


for (N, np_) in ((3, (-1, 2, 2)), (7, (-2, 3, 6))):
    ok_trans, q_slice, tau = forms_kasner(N, np_)
    p = [Fraction(x, N) for x in np_]
    g.check("prop:counterterm(i) [p = %s]: dQ = eps_{abcd} R^{ab} ^ R^{cd} holds "
            "identically for the Chern-Simons form of the Kasner connection"
            % (tuple(str(x) for x in p),), ok_trans)
    g.check("prop:counterterm(ii) [p = %s]: Q restricted to the slice tau = const "
            "equals 8 p1 p2 p3 tau^-2 d^3x exactly" % (tuple(str(x) for x in p),),
            q_slice.eqrf(rfk(8 * p[0] * p[1] * p[2]) / (tau * tau)))


def transgression_generic():
    """dQ = eps R^R for a generic so(1,3) connection with all six components
    nonzero, coefficients polynomial in s, legs in all four coordinate
    directions (mu = 0..3), so that omega^omega^omega^omega is a genuine
    four-form and the quartic step eps(omega^2, omega^2) = 0 is exercised,
    unlike on Kasner."""
    eta = [1, -1, -1, -1]

    def wedge(a, b):
        out = {}
        for ka, va in a.items():
            for kb, vb in b.items():
                if set(ka) & set(kb):
                    continue
                arr = list(ka) + list(kb)
                sg = 1
                for i in range(len(arr)):
                    for j in range(len(arr) - 1 - i):
                        if arr[j] > arr[j + 1]:
                            arr[j], arr[j + 1] = arr[j + 1], arr[j]
                            sg = -sg
                key = tuple(arr)
                out[key] = out.get(key, RF0) + rfk(sg) * va * vb
        return out

    def dform(a):
        out = {}
        for k, vv in a.items():
            if 0 in k:
                continue
            key = (0,) + k
            out[key] = out.get(key, RF0) + vv.deriv()
        return out

    def add(a, b, sb=RF1):
        return {k: a.get(k, RF0) + sb * b.get(k, RF0) for k in set(a) | set(b)}

    def scal(a, f):
        return {k: vv * f for k, vv in a.items()}

    seed = [3]

    def coef():
        seed[0] = (seed[0] * 7 + 5) % 11
        c0, c1 = seed[0] - 5, (seed[0] * 3) % 7 - 3
        return rfk(c0) + rfk(c1) * RFs + rfk(c1 * c0 % 5) * RFs * RFs
    om = {}
    for (a, b) in PAIRS4:
        om[(a, b)] = {(mu,): coef() for mu in range(4)}
        om[(b, a)] = scal(om[(a, b)], -RF1)

    def W(a, b):
        return om.get((a, b), {})
    R = {}
    for a in range(4):
        for b in range(4):
            if a == b:
                continue
            cur = dform(W(a, b))
            for cc in range(4):
                cur = add(cur, wedge(scal(W(a, cc), rfk(eta[cc])), W(cc, b)))
            R[(a, b)] = cur
    GB, Q = {}, {}
    for a in range(4):
        for b in range(4):
            for cc in range(4):
                for d in range(4):
                    sg = eps4(a, b, cc, d)
                    if not sg:
                        continue
                    GB = add(GB, wedge(R[(a, b)], R[(cc, d)]), rfk(sg))
                    t1 = wedge(W(a, b), dform(W(cc, d)))
                    t2 = {}
                    for ee in range(4):
                        t2 = add(t2, wedge(wedge(W(a, b), scal(W(cc, ee), rfk(eta[ee]))), W(ee, d)))
                    Q = add(Q, add(t1, scal(t2, rfk(Fraction(2, 3)))), rfk(sg))
    diff = add(GB, dform(Q), -RF1)
    nontrivial = any(not vv.is_zero() for vv in GB.values())
    return all(vv.is_zero() for vv in diff.values()) and nontrivial


g.check("prop:counterterm(i): dQ = eps_{abcd} R^{ab} ^ R^{cd} holds identically for a "
        "generic so(1,3) connection with all six components nonzero and legs in all "
        "four directions (the quartic step eps(omega^2, omega^2) = 0 exercised; "
        "eps R^R itself nonzero)", transgression_generic())


def bianchi_series(p, Lam, order):
    H = [{-1: p[i]} for i in range(3)]
    for n in range(1, order + 1):
        k = 2 * n - 1
        known = []
        for i in range(3):
            tot = Fraction(0)
            for a, ca in H[i].items():
                for j in range(3):
                    for b, cb in H[j].items():
                        if a + b == k - 1:
                            tot += ca * cb
            known.append(tot)
        rhs = [(Lam if k == 1 else Fraction(0)) - known[i] for i in range(3)]
        Hn = sum(rhs) / (k + 2)
        for i in range(3):
            H[i][k] = (rhs[i] - p[i] * Hn) / (k + 1)
    return H


def bianchi_residuals(H, Lam, maxpow):
    res = []
    for i in range(3):
        r = {}
        for a, ca in H[i].items():
            if a != 0:
                r[a - 1] = r.get(a - 1, Fraction(0)) + a * ca
            for j in range(3):
                for b, cb in H[j].items():
                    r[a + b] = r.get(a + b, Fraction(0)) + ca * cb
        r[0] = r.get(0, Fraction(0)) - Lam
        res.append({k: v for k, v in r.items() if v != 0 and k <= maxpow})
    C = {}
    for i in range(3):
        for j in range(i + 1, 3):
            for a, ca in H[i].items():
                for b, cb in H[j].items():
                    C[a + b] = C.get(a + b, Fraction(0)) + ca * cb
    C[0] = C.get(0, Fraction(0)) - Lam
    return res, {k: v for k, v in C.items() if v != 0 and k <= maxpow}


for (p, Lam) in (([Fraction(-1, 3), Fraction(2, 3), Fraction(2, 3)], Fraction(3)),
                 ([Fraction(-2, 7), Fraction(3, 7), Fraction(6, 7)], Fraction(5, 2))):
    H = bianchi_series(p, Lam, 3)
    res, C = bianchi_residuals(H, Lam, 4)
    # at the Schwarzschild exponents with Lambda = 3 the paper quotes
    # h_{i,1} = (2, 1/2, 1/2) and h_{i,2} = (-33/20, -3/40, -3/40)
    quoted_ok = True
    if Lam == 3 and p[0] == Fraction(-1, 3):
        quoted_ok = ([H[i][1] for i in range(3)] == [Fraction(2), Fraction(1, 2), Fraction(1, 2)]
                     and [H[i][3] for i in range(3)]
                     == [Fraction(-33, 20), Fraction(-3, 40), Fraction(-3, 40)])
    g.check("prop:lambdacorr [p = %s, Lambda = %s]: first correction h_{i,1} = "
            "Lambda (1 - p_i)/2 exactly%s" % (tuple(str(x) for x in p), Lam,
            "; at these Schwarzschild exponents h_{i,1} = (2, 1/2, 1/2) and "
            "h_{i,2} = (-33/20, -3/40, -3/40) as quoted" if Lam == 3 else ""),
            all(H[i][1] == Lam * (1 - p[i]) / 2 for i in range(3)) and quoted_ok)
    g.check("prop:lambdacorr [p = %s, Lambda = %s]: with the series solved to tau^5 "
            "the evolution equations and the constraint have vanishing residual "
            "through order tau^4 (constraint preserved automatically)"
            % (tuple(str(x) for x in p), Lam),
            all(len(r) == 0 for r in res) and len(C) == 0)


# --- lem:varexp: the displayed connection is torsion-free as an identity of
# the exterior algebra.  Structure coefficients (p_i/tau) -> a_i and
# (d_j p_i) log(tau) tau^{-p_j} -> L[j][i] replaced by independent rationals;
# de^i = a_i e^0 e^i + sum_j L[j][i] e^j e^i ; the e^a are the basis.


def varexp_torsion(a, L, sign):
    """Torsion of omega^{i0} = a_i e^i, omega^{ij} = sign*(L[i][j] e^j - L[j][i] e^i)
    against de^i = a_i e^0^e^i + sum_j L[j][i] e^j^e^i, de^0 = 0.  True iff all
    four torsion two-forms vanish.  Indices 0..3, spatial i = 1..3."""
    ETA = [1, -1, -1, -1]

    def two(m, n):
        if m == n:
            return {}
        return {(m, n): Fraction(1)} if m < n else {(n, m): Fraction(-1)}

    def add(x, y, c=Fraction(1)):
        out = dict(x)
        for k, vv in y.items():
            out[k] = out.get(k, Fraction(0)) + c * vv
        return {k: vv for k, vv in out.items() if vv != 0}

    def om(p, q):
        if p == q:
            return {}
        if q == 0 and p > 0:
            return {p: a[p - 1]}
        if p == 0 and q > 0:
            return {q: -a[q - 1]}
        i, j = p, q
        return {j: sign * L[i - 1][j - 1], i: -sign * L[j - 1][i - 1]}

    ok = True
    for i0 in range(4):
        de = {}
        if i0 > 0:
            de = add(de, two(0, i0), a[i0 - 1])
            for j in range(1, 4):
                if j != i0:
                    de = add(de, two(j, i0), L[j - 1][i0 - 1])
        T = dict(de)
        for b in range(4):
            for leg, coeff in om(i0, b).items():
                T = add(T, two(leg, b), coeff * ETA[b])
        ok = ok and len(T) == 0
    return ok


a_pl = [Fraction(2), Fraction(-3), Fraction(5)]
L_pl = [[Fraction(x) for x in row] for row in [[0, 7, -2], [3, 0, 4], [-5, 6, 0]]]
g.check("lem:varexp: the displayed connection (boost block a_i e^i, tangential "
        "block L_ij e^j - L_ji e^i) is torsion-free as an identity of the exterior "
        "algebra with independent placeholder coefficients",
        varexp_torsion(a_pl, L_pl, Fraction(1)))
g.check("lem:varexp: the connection with the opposite tangential sign is NOT "
        "torsion-free (the sign is not a convention)",
        not varexp_torsion(a_pl, L_pl, Fraction(-1)))

# ---------------------------------------------------------------------------
# Part C: the two kinds (thm:twokinds) and the scale tractor off the Einstein
# region (prop:w)
# ---------------------------------------------------------------------------


def mat3(rows):
    return [[Fraction(x) for x in r] for r in rows]


def mm3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)]
            for i in range(3)]


def tr3(A):
    return A[0][0] + A[1][1] + A[2][2]


X3 = mat3([[1, 2, 0], [3, -1, 1], [0, 4, 0]])
Y3 = mat3([[0, 1, 5], [2, 2, -3], [1, 0, -2]])
Z3 = mat3([[3, 0, 1], [-1, 1, 0], [2, 2, -4]])
comm = lambda A, B: [[mm3(A, B)[i][j] - mm3(B, A)[i][j] for j in range(3)]
                     for i in range(3)]
g.check("thm:twokinds(1) [identity, not a test]: trace cyclicity tr(XY) = tr(YX) and the derivation "
        "identity tr([X,Y]Z) + tr(Y[X,Z]) = 0 on exact integer instances",
        tr3(mm3(X3, Y3)) == tr3(mm3(Y3, X3))
        and tr3(mm3(comm(X3, Y3), Z3)) + tr3(mm3(Y3, comm(X3, Z3))) == 0)

# tr(alpha ^ beta) = tr(beta ^ alpha) for matrix-valued 2-forms in 4D:
# alpha = X3 dx^0 dx^1 + Y3 dx^2 dx^3, beta = Z3 dx^0 dx^1 + X3 dx^2 dx^3
# (alpha ^ beta)_{0123} = X3 X3 + Y3 Z3 (as dx^0dx^1dx^2dx^3 coefficient,
# the 2-forms commuting); the trace comparison is the whole content.
lhs = tr3(mm3(X3, X3)) + tr3(mm3(Y3, Z3))
rhs = tr3(mm3(Z3, Y3)) + tr3(mm3(X3, X3))
g.check("thm:twokinds(1) [identity, not a test]: tr(alpha ^ beta) = tr(beta ^ alpha) for matrix-"
        "valued two-forms on an exact instance, the commutation the Bianchi "
        "cancellation d tr(F^F) = 2 tr(DF ^ F) uses", lhs == rhs)

# prop:w(ii): I_g = (1, 0, J/4) has norm J/2 in formal J, and the mu-slot of
# nabla I_g from eq:conn is (J/4) g - P, the trace-free Schouten tensor.
Jf = g.RF.var()
Ig = rf_vec([1, 0, 0, 0, 0, Jf / rfc(4)])
g.check("prop:w(ii): <I_g, I_g> = J/2 (= R/12) as a rational-function "
        "identity for I_g = (1, 0, J/4)",
        ip_rf(Ig, Ig).eqrf(Jf / rfc(2)))
# eq:conn applied to I_g = (1, 0, J/4) with a Schouten tensor P_a^b = diag(P_a)
# (mixed components) and J := sum_a P_a^a:
#   sigma-slot: d sigma - mu_a = 0 - 0 ;  mu-slot: d mu_b + g_ab rho - P_ab sigma
#   = (J/4) g_ab - P_ab ;  rho-slot: d rho + P_a^b mu_b = d(J/4) + 0.
# For constant P (the algebraic slots) d sigma = d mu = d rho = 0.


def eq_conn_on_Ig(P_diag):
    J = sum(P_diag)
    sigma, mu, rho = Fraction(1), [Fraction(0)] * 4, J / 4
    sigma_slot = [Fraction(0) - mu[a] for a in range(4)]
    mu_slot = [(J / 4) - P_diag[a] for a in range(4)]          # mixed (J/4) delta - P_a^b, times sigma = 1
    rho_slot = [Fraction(0) + sum(P_diag[a] * mu[b] if a == b else 0 for b in range(4))
                for a in range(4)]
    return sigma_slot, mu_slot, rho_slot


P_diag = [Fraction(2), Fraction(-1), Fraction(-1), Fraction(3)]   # non-Einstein
sig_s, mu_s, rho_s = eq_conn_on_Ig(P_diag)
J_inst = sum(P_diag)
g.check("prop:w(ii): eq:conn applied to I_g = (1, 0, J/4) with a non-Einstein "
        "Schouten tensor gives sigma-slot 0, mu-slot (J/4) g - P (the trace-free "
        "Schouten tensor: traceless and nonzero), and rho-slot P_a^b mu_b = 0 for the "
        "algebraic part (the derivative part is (1/4) d_a J, checked next)",
        sig_s == [0] * 4 and all(mu_s[a] == -(P_diag[a] - J_inst / 4) for a in range(4))
        and sum(mu_s) == 0 and any(x != 0 for x in mu_s) and rho_s == [0] * 4)
P_ein = [Fraction(1, 2)] * 4   # Einstein: P = (Lambda/6) g with Lambda = 3
sig_e, mu_e, rho_e = eq_conn_on_Ig(P_ein)
g.check("prop:w(i): on an Einstein instance (P = Lambda/6 g, Lambda = 3) eq:conn "
        "applied to I_g gives all three slots zero and J/4 = Lambda/6 = 1/2: "
        "I_g = (1,0,Lambda/6) is parallel",
        sig_e == [0] * 4 and mu_e == [0] * 4 and rho_e == [0] * 4 and sum(P_ein) / 4 == Fraction(1, 2))

# rho slot of nabla I_g, derived from eq:conn itself: the covariant derivative
# along a coordinate s is the ordinary derivative of the slots plus the
# algebraic action of eq:conn with the Schouten tensor P(s), here diagonal
# (mixed components P_a^b = diag(P_a(s))) and non-constant in s.  With
# I_g(s) = (1, 0, J(s)/4), J = sum_a P_a(s), eq:conn gives
#   sigma-slot: d_s 1 - mu_s = 0;  mu-slot: d_s 0 + rho g - P sigma = (J/4) g - P;
#   rho-slot: d_s(J/4) + P_s^b mu_b = (1/4) J'(s).
# Nothing is differentiated by hand: the derivative of every slot is taken
# by the rational-function class and the algebraic part is eq:conn's.


def conn_alg_rf(P_diag_rf, a, u):
    """Algebraic part of eq:conn along frame direction a, for a diagonal
    Schouten tensor P_a^b = diag(P) of rational functions, on a tractor u =
    (sigma, mu^b, rho) of rational functions (contravariant mu)."""
    sigma, mu, rho = u[0], u[1:5], u[5]
    mu_a = rfk(eta[a]) * mu[a]
    out = [rfk(0)] * 6
    out[0] = rfk(0) - mu_a
    out[1 + a] = rho - P_diag_rf[a] * sigma
    out[5] = P_diag_rf[a] * mu_a
    return out


def nabla_Ig(P_diag_rf, a):
    """nabla_a I_g for I_g(s) = (1, 0, J(s)/4), J = sum P_a(s), the direction
    a carrying the coordinate s: d/ds of the slots plus eq:conn's algebraic part."""
    J = P_diag_rf[0] + P_diag_rf[1] + P_diag_rf[2] + P_diag_rf[3]
    Ig_s = [rfk(1), rfk(0), rfk(0), rfk(0), rfk(0), J / rfk(4)]
    dIg = [x.deriv() for x in Ig_s]
    alg = conn_alg_rf(P_diag_rf, a, Ig_s)
    return [dIg[k] + alg[k] for k in range(6)], J


# instance: P_a(s) = (2 + s^2, -1 + s^2, -1, 3 + s^2), J(s) = 3 + 3 s^2,
# so (1/4) J'(s) = (3/2) s; the direction a = 0 carries s
P_s = [rfk(2) + RFs * RFs, rfk(-1) + RFs * RFs, rfk(-1), rfk(3) + RFs * RFs]
nabs = [nabla_Ig(P_s, a) for a in range(4)]
J_s = nabs[0][1]
mu_mixed = [nabs[a][0][1 + a] for a in range(4)]       # (nabla_a I_g)^{mu^a}: (J/4) - P_a^a
off_diag = all(nabs[a][0][1 + b].is_zero() for a in range(4) for b in range(4) if a != b)
trace_mu = sum(mu_mixed, rfk(0))
ein = [nabla_Ig([rfk(Fraction(1, 2))] * 4, a)[0] for a in range(4)]
g.check("prop:w(ii): nabla_a I_g computed from eq:conn (slot derivatives by the "
        "rational-function class plus eq:conn's algebraic part, P_a^b = diag(2+s^2, "
        "-1+s^2, -1, 3+s^2)) has sigma-slot 0, mu-slot (J/4) delta - P (trace-free, "
        "nonzero) and rho-slot exactly (1/4) J'(s) = (3/2) s in every direction, "
        "nonzero because J is not constant; on the Einstein instance P = (1/2) "
        "diag(1,1,1,1) every slot is zero",
        all(nabs[a][0][0].is_zero() for a in range(4))
        and all((mu_mixed[a] - (J_s / rfk(4) - P_s[a])).is_zero() for a in range(4))
        and off_diag and trace_mu.is_zero() and any(not x.is_zero() for x in mu_mixed)
        and all((nabs[a][0][5] - (J_s / rfk(4)).deriv()).is_zero() for a in range(4))
        and nabs[0][0][5].eqrf(rfk(Fraction(3, 2)) * RFs)
        and all(x.is_zero() for a in range(4) for x in ein[a]))

# ---------------------------------------------------------------------------
# Part D: symmetry orthogonality on a six-mode window (prop:nogo)
# ---------------------------------------------------------------------------

NW = 6
# mode labels: index 0,1,2 -> particles k = 1,2,3 ; index 3,4,5 -> antiparticles
# k = -1,-2,-3.  Energy |k|, charge +1 / -1.
energy = [1, 2, 3, 1, 2, 3]
charge = [1, 1, 1, -1, -1, -1]


def popcount(m):
    return bin(m).count("1")


def diag_state_expect(func, occ):
    """Expectation of a diagonal function func(occupation bitstring) in the
    product state with occupancies occ."""
    tot = Fraction(0)
    for s in range(1 << NW):
        w = Fraction(1)
        for k in range(NW):
            w *= occ[k] if (s >> k) & 1 else (1 - occ[k])
        tot += w * func(s)
    return tot


def H_of(s):
    return Fraction(sum(energy[k] for k in range(NW) if (s >> k) & 1))


def Q_of(s):
    return Fraction(sum(charge[k] for k in range(NW) if (s >> k) & 1))


def covariance(occ):
    return (diag_state_expect(lambda s: H_of(s) * Q_of(s), occ)
            - diag_state_expect(H_of, occ) * diag_state_expect(Q_of, occ))


x = Fraction(1, 2)
# C-symmetric window state: n(antiparticle k) = n(particle k).  Dictionary to
# the array of T5: the antiparticle mode is the hole at -k, n_array(-k) =
# 1 - n_anti(k), so this is the criterion n_{-k} = 1 - n_k of prop:nogo.
occ_sym = [x ** e / (1 + x ** e) for e in energy]
occ_mu = [x ** e / (1 + x ** e) if charge[k] > 0 else x ** (e + 1) / (1 + x ** (e + 1))
          for k, e in enumerate(energy)]                        # chemical potential
cov_sym, cov_mu = covariance(occ_sym), covariance(occ_mu)
g.check("prop:nogo: energy-charge covariance <HQ> - <H><Q> vanishes exactly "
        "in the charge-conjugation-symmetric window state (n_anti(k) = n(k), i.e. "
        "n_{-k} = 1 - n_k in the array's symbols)", cov_sym == 0)
g.check("prop:nogo: the hypothesis is necessary: at nonzero chemical "
        "potential the covariance is exactly nonzero (%s)" % cov_mu, cov_mu != 0)


def psi_dag_psi(a, b, statevec):
    out = {}
    for s, c in statevec.items():
        if not (s >> b) & 1:
            continue
        sgn1 = -1 if popcount(s & ((1 << b) - 1)) % 2 else 1
        s1 = s & ~(1 << b)
        if (s1 >> a) & 1:
            continue
        sgn2 = -1 if popcount(s1 & ((1 << a) - 1)) % 2 else 1
        out[s1 | (1 << a)] = out.get(s1 | (1 << a), Fraction(0)) + Fraction(sgn1 * sgn2) * c
    return {s: c for s, c in out.items() if c != 0}


# charged case: the overlap <H psi^dag_a psi_b> of a charge-changing bilinear
# with the diagonal flow generator, (1) in the gauge-invariant diagonal state
# and (2) in a pure state superposing two charge sectors (which breaks U(1))


def expect_pure(vec, a, b):
    """<vec| H psi^dag_a psi_b |vec> with H = sum |k| N_k, vec unnormalised."""
    out = Fraction(0)
    for s0, c0 in vec.items():
        for st, c in psi_dag_psi(a, b, {s0: c0}).items():
            out += vec.get(st, Fraction(0)) * c * H_of(st)
    return out


ok_diag = True
ok_super = False
for a in range(NW):
    for b in range(NW):
        if charge[a] == charge[b]:
            continue
        tot = Fraction(0)
        for s0 in range(1 << NW):
            w = Fraction(1)
            for k in range(NW):
                w *= occ_sym[k] if (s0 >> k) & 1 else (1 - occ_sym[k])
            tot += w * expect_pure({s0: Fraction(1)}, a, b)
        ok_diag = ok_diag and tot == 0
        for s0 in range(1 << NW):
            img = psi_dag_psi(a, b, {s0: Fraction(1)})
            if not img:
                continue
            s1 = next(iter(img))
            if expect_pure({s0: Fraction(1), s1: Fraction(1)}, a, b) != 0:
                ok_super = True
g.check("prop:nogo [identity, not a test]: in a diagonal state the overlap of the "
        "flow generator with every charge-changing bilinear vanishes, because an "
        "operator that changes the occupation has no diagonal matrix element", ok_diag)
g.check("prop:nogo: the U(1) hypothesis is necessary: in a pure state superposing "
        "two charge sectors the same overlap is exactly nonzero", ok_super)

# ---------------------------------------------------------------------------
# Part E: the norm as a parameter of the laws (prop:parameter), at the same
# rational instance Lambda = 3 as the prop:goldstone checks, with the Lambda
# dependence of N^2 as a rational-function identity in formal Lambda.
# ---------------------------------------------------------------------------

# (ii): N^2 = 3 M_P^2 / Lambda, in units M_P = 1 throughout Part E, so the
# paper's -3 M_P^2/Lambda^2 reads -3/Lambda^2 here; d(N^2)/dLambda as an RF
# identity, and the same rational function evaluated at two members of the
# family to unequal values.
LamE = g.RF.var()
Nsq = rfc(3) / LamE
g.check("prop:parameter(ii): d(N^2)/dLambda = -3/Lambda^2 (M_P = 1) as a "
        "rational-function identity (N^2 = 3 M_P^2/Lambda from H^2 = <I,I> = "
        "Lambda/3): N is not dynamically fixed across the family",
        Nsq.deriv().eqrf(-(rfc(3) / (LamE * LamE))) and not Nsq.deriv().is_zero())
g.check("prop:parameter(ii): the rational function N^2 evaluated at Lambda = 3 "
        "and at Lambda = 12 gives 1 and 1/4, unequal: across the family the norm "
        "varies, with ratio s^2 = 4 (N -> N/s)",
        Nsq.eval(Fraction(3)) == 1 and Nsq.eval(Fraction(12)) == Fraction(1, 4)
        and Nsq.eval(Fraction(3)) / Nsq.eval(Fraction(12)) == 4)

# the free case: variables (dI, dV, dLambda) in R^13.  The linearised constraints
# d<I,I> - dLambda/3 = 0, d<I,V> = 0, d<V,V> + (3/Lambda^2) dLambda = 0
# (from <V,V> = -3/Lambda, d<V,V> = +(3/Lambda^2) dLambda), so the dLambda
# columns of the rows 2<dI,I>, ..., 2<dV,V> are -1/3 and -3/Lambda^2.
# (cons_T carries <dI,I>, <dV,I> + <V,dI>, <dV,V> without the factors 2, so the
# dLambda columns are halved: -1/6 and -3/(2 Lambda^2).)
cons_free_T = [cons_T[0] + [Fraction(-1, 6)],
               cons_T[1] + [Fraction(0)],
               cons_T[2] + [Fraction(-3, 2) / LAM ** 2]]
g.check("prop:parameter (free case): three independent constraints on thirteen "
        "components, constrained space of dimension 13 - 3 = 10",
        g.rank_of_vectors([r[:] for r in cons_free_T]) == 3)
joint_ext = [v + [Fraction(0)] for v in joint]
g.check("prop:parameter (free case): the fifteen gauge images extended by a zero "
        "dLambda-component still have rank 9 (bivectors do not move a norm), so "
        "exactly one non-gauge direction remains: 10 - 9 = 1",
        g.rank_of_vectors([v[:] for v in joint_ext]) == 9)
norm_mode = ([x / (2 * LAM) for x in I_vec] + [-x / (2 * LAM) for x in V_vec]
             + [Fraction(1)])
def dot(r, v):
    return sum(r[k] * v[k] for k in range(len(v)))
g.check("prop:parameter (free case): the norm mode (I/2Lambda, -V/2Lambda, 1) "
        "satisfies all three free constraints and violates the fixed ones (its "
        "(dI, dV) part changes <I,I> and <V,V>)",
        all(dot(r, norm_mode) == 0 for r in cons_free_T)
        and dot(cons_T[0], norm_mode[:12]) != 0 and dot(cons_T[2], norm_mode[:12]) != 0
        and dot(cons_T[1], norm_mode[:12]) == 0)
g.check("prop:parameter (free case): the norm mode is not a gauge direction and "
        "spans the complement: the gauge images together with it have rank 10 "
        "= the full constrained space",
        g.rank_of_vectors([v[:] for v in joint_ext] + [norm_mode[:]]) == 10)
# the norm mode is the tangent of the rescaling family (sI, V/s, s^2 Lambda) at
# s = 1.  The family is built as a 13-vector of rational functions in a formal s,
# differentiated componentwise in s, and the derivative evaluated at s = 1 is
# compared with 2 Lambda * norm_mode; the constraints on the family are checked
# as identities in s (numerators cleared), not at sampled values.
sE = g.RF.var()
fam = ([sE * rfc(x) for x in I_vec] + [rfc(x) / sE for x in V_vec]
       + [sE * sE * rfc(LAM)])
fam_deriv_at_1 = [c.deriv().eval(Fraction(1)) for c in fam]
Is_rf, Vs_rf, Ls_rf = fam[:6], fam[6:12], fam[12]
fam_ok = (ip_rf(Is_rf, Is_rf).eqrf(Ls_rf / rfc(3))
          and ip_rf(Vs_rf, Vs_rf).eqrf(-(rfc(3) / Ls_rf))
          and ip_rf(Is_rf, Vs_rf).is_zero())
g.check("prop:parameter (free case): the componentwise s-derivative at s = 1 of the "
        "rescaling family (sI, V/s, s^2 Lambda), built as rational functions of a "
        "formal s, equals 2 Lambda times the norm mode (I/2Lambda, -V/2Lambda, 1), "
        "and the family satisfies <I_s,I_s> = s^2 Lambda/3, <V_s,V_s> = -3/(s^2 "
        "Lambda), <I_s,V_s> = 0 as identities in s",
        fam_deriv_at_1 == [2 * LAM * x for x in norm_mode] and fam_ok)

# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

print()
if g.FAILURES:
    print("FAILURES (%d):" % len(g.FAILURES))
    for f in g.FAILURES:
        print("  " + f)
    raise SystemExit(1)
print("All checks pass.")
