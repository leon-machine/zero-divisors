"""Referee F1 (blind), run 2026-11-07-consistency: independent exact recomputations.

Written from the proofs' statements, not from the entities' check functions. Uses lib/GA.py (products of
multivectors) and lib/gtg.py (the jet engine and the torsion solver for fields), Fractions throughout.
Each section prints PASS/FAIL lines; a FAIL marked 'expected' is a mutation or a disproved line of a proof.
"""
import sys
from fractions import Fraction as F
from itertools import permutations

sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA  # noqa: E402
import gtg  # noqa: E402

RESULTS = []


def rep(label, ok, expect=True):
    tag = "PASS" if ok == expect else "FAIL"
    RESULTS.append(tag)
    print(tag, label, "" if expect else "(expected False)")


S13 = (1, -1, -1, -1)
ETA = [1, -1, -1, -1]


def m(x, y, sq=S13):
    return GA.mul(x, y, sq)


def vec(c):
    return {(i,): F(v) for i, v in enumerate(c) if v}


def wedge(a, b, sq=S13):
    return {k: v for k, v in GA.scal(F(1, 2), GA.sub(m(a, b, sq), m(b, a, sq))).items() if v}


def dotv(a, b, sq=S13):
    r = GA.dot(a, b, sq)
    return r.get((), F(0)) if isinstance(r, dict) else F(r)


def bvdot(B, a, sq=S13):
    """B . a for a bivector B and vector a: (Ba - aB)/2."""
    return {k: v for k, v in GA.scal(F(1, 2), GA.sub(m(B, a, sq), m(a, B, sq))).items() if v}


def comm(A, B, sq=S13):
    return {k: v for k, v in GA.scal(F(1, 2), GA.sub(m(A, B, sq), m(B, A, sq))).items() if v}


def sp(x):
    return x.get((), F(0))


def perm_sign(p):
    p = list(p)
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0)) for j in range(len(B[0]))] for i in range(len(A))]


def matinv(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)] + [F(1 if i == k else 0) for k in range(n)] for i in range(n)]
    for c in range(n):
        p = next(r for r in range(c, n) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for r in range(n):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    return [row[n:] for row in A]


def det(M):
    n = len(M)
    return sum((perm_sign(p) * _prod(M[i][p[i]] for i in range(n)) for p in permutations(range(n))), F(0))


def _prod(xs):
    out = F(1)
    for x in xs:
        out *= x
    return out


# ============================================================================
# E1. dark-energy.gravity-pre-metric-forces-degenerate-exactly
#     star_g F = |det hb|^-1 I G(F), G = hb hb^T; star^2 = -1; scale and boost invariance; wall limit.
# ============================================================================
I4 = m(m(GA.gen(0), GA.gen(1)), m(GA.gen(2), GA.gen(3)))
PLANES = [(a, b) for a in range(4) for b in range(a + 1, 4)]


def lin(M):
    """Background linear map with matrix M: e_j -> sum_i M[i][j] e_i."""
    return lambda a: GA.add(*[GA.scal(c * M[i][j], GA.gen(i)) for (j,), c in a.items() for i in range(4) if M[i][j]]) if a else {}


def outer2(f, B):
    """Outermorphism of f on a bivector B."""
    out = {}
    for (a, b), c in B.items():
        out = GA.add(out, GA.scal(c, wedge(f(GA.gen(a)), f(GA.gen(b)))))
    return {k: v for k, v in out.items() if v}


def adjoint(M):
    """a . f^T(b) = f(a) . b for the flat product: (f^T)[i][j] = eta_i M[j][i] eta_j."""
    return [[F(ETA[i]) * M[j][i] * ETA[j] for j in range(4)] for i in range(4)]


def recip(i):
    return GA.scal(F(ETA[i]), GA.gen(i))


def two_form(c, d):
    """the background bivector e^c ^ e^d (the unit two-form with w_cd = 1)."""
    return wedge(recip(c), recip(d))


def comps(X):
    """X = sum_{a<b} X_ab e^a ^ e^b: X_ab = <(e_b ^ e_a) X>."""
    return [sp(m(wedge(GA.gen(b), GA.gen(a)), X)) for a, b in PLANES]


def ga_star_matrix(hinv, Gfun=None, use_abs=True):
    hb = matinv(hinv)
    d = det(hb)
    G = matmul(hb, adjoint(hb)) if Gfun is None else Gfun(hb)
    cols = []
    for c, dd in PLANES:
        X = outer2(lin(G), two_form(c, dd))
        X = GA.scal(1 / (abs(d) if use_abs else d), m(I4, X))
        cols.append(comps(X))
    return [[cols[j][i] for j in range(6)] for i in range(6)]


def component_star(hinv):
    """(*w)_ab = (1/2) sqrt|g| eps_abcd g^ce g^df w_ef, eps_0123 = +1, g_{mu nu} = sum_k eta_k h_k mu h_k nu."""
    g = [[sum((ETA[k] * hinv[k][mu] * hinv[k][nu] for k in range(4)), F(0)) for nu in range(4)] for mu in range(4)]
    gi = matinv(g)
    vol = abs(det(hinv))
    M = []
    for a, b in PLANES:
        row = []
        for e, f in PLANES:
            tot = F(0)
            for c in range(4):
                for dd in range(4):
                    if len({a, b, c, dd}) < 4:
                        continue
                    eps = perm_sign((a, b, c, dd))
                    # w_ef = 1, w_fe = -1
                    tot += F(1, 2) * vol * eps * (gi[c][e] * gi[dd][f] - gi[c][f] * gi[dd][e])
            row.append(tot)
        M.append(row)
    return M


def mat6sq(S):
    return matmul(S, S)


ID6 = [[F(1 if i == j else 0) for j in range(6)] for i in range(6)]
NEGID6 = [[-x for x in r] for r in ID6]

HINVS = [[[F(x) for x in r] for r in H] for H in (
    [[3, 1, 0, -1], [0, 2, 1, 0], [1, 0, 1, 2], [0, -1, 1, 1]],
    [[1, 0, 2, 0], [1, 1, 0, 0], [0, 3, 1, -1], [2, 0, 0, 5]],
    [[F(1, 2), 1, 0, 0], [0, 1, F(-1, 3), 0], [0, 0, 2, 1], [1, 0, 0, -1]])]

for k, hinv in enumerate(HINVS):
    dh = det(matinv(hinv))
    S_ga = ga_star_matrix(hinv)
    S_c = component_star(hinv)
    rep(f"E1 field {k} (det hb = {dh}): |det hb|^-1 I G(F) equals the component Hodge star", S_ga == S_c)
    rep(f"E1 field {k}: star^2 = -1", mat6sq(S_ga) == NEGID6)
    # inverse adjoint: hb^{-T}(X) = I hb(I^{-1} X)/det hb on a bivector X
    hb = matinv(hinv)
    X = GA.add(two_form(0, 2), GA.scal(F(5), two_form(1, 3)), GA.scal(F(-2), two_form(2, 3)))
    hbinvT = adjoint(hinv)         # (hb^{-1})^T = (hb^T)^{-1}
    I4inv = GA.scal(F(-1), I4)
    lhs = outer2(lin(hbinvT), X)
    rhs = GA.scal(1 / dh, m(I4, outer2(lin(hb), m(I4inv, X))))
    rep(f"E1 field {k}: hb^-T(X) = I hb(I^-1 X)/det hb", GA.eq(lhs, rhs))
    # physical duality read back: hb^{-T}(I hb^T(F)) = sgn(det hb) * star(F)
    Fb = X
    back = outer2(lin(hbinvT), m(I4, outer2(lin(adjoint(hb)), Fb)))
    st = GA.scal(1 / abs(dh), m(I4, outer2(lin(matmul(hb, adjoint(hb))), Fb)))
    sgn = 1 if dh > 0 else -1
    rep(f"E1 field {k}: physical dual read back = sgn(det hb) |det hb|^-1 I G(F)", GA.eq(back, GA.scal(F(sgn), st)))
    # scale: hb -> lam hb
    for lam in (F(3), F(2, 5)):
        rep(f"E1 field {k}: invariant under hb -> {lam} hb", ga_star_matrix([[x / lam for x in r] for r in hinv]) == S_ga)
    # rotation gauge: hb -> hb o L with L a Lorentz transformation (boost along e2 with ch = 13/12 ... use 5/3,4/3)
    ch, shh = F(5, 3), F(4, 3)
    L = [[ch, 0, shh, 0], [0, 1, 0, 0], [shh, 0, ch, 0], [0, 0, 0, 1]]
    rep(f"E1 field {k}: invariant under the rotation gauge hb -> hb L", ga_star_matrix(matinv(matmul(hb, L))) == S_ga)
    # mutations
    rep(f"E1 field {k} mutation G = hb^T hb", ga_star_matrix(hinv, Gfun=lambda h: matmul(adjoint(h), h)) == S_c, expect=False)
    if dh < 0:
        rep(f"E1 field {k} mutation det hb in place of |det hb|", ga_star_matrix(hinv, use_abs=False) == S_c, expect=False)
rep("E1 star depends on [g]: two non-conformal fields differ", ga_star_matrix(HINVS[0]) != ga_star_matrix(HINVS[1]))

# wall: hb_s = C diag(1, s, 1, 1) D, non-diagonal; G_s -> G_0 of rank 3, det hb_s = s det C det D -> 0
C = [[F(x) for x in r] for r in ([1, 0, 0, 0], [2, 1, 0, 0], [0, 1, 1, 0], [1, 0, 3, 1])]
D = [[F(x) for x in r] for r in ([1, 2, 0, 1], [0, 1, 3, 0], [0, 0, 1, 2], [0, 0, 0, 1])]
G0 = matmul(matmul(C, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), matmul(D, adjoint(matmul(matmul(C, [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), D))))
G0 = [[F(x) for x in r] for r in G0]
rk = GA.rank_of_vectors([[x for x in r] for r in G0])
rep("E1 wall: the limiting cometric G_0 has rank 3", rk == 3)
IG0 = []
for c, dd in PLANES:
    IG0.append(comps(m(I4, outer2(lin(G0), two_form(c, dd)))))
IG0 = [[IG0[j][i] for j in range(6)] for i in range(6)]
rep("E1 wall: I G_0 has rank 3 on the six bivectors", GA.rank_of_vectors(IG0) == 3)
errs, maxes = [], []
for s in (F(1, 10), F(1, 100), F(1, 1000)):
    hb_s = matmul(matmul(C, [[1, 0, 0, 0], [0, s, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]), D)
    hinv_s = matinv(hb_s)
    St = ga_star_matrix(hinv_s)
    rep(f"E1 wall s = {s}: GA star = component star", St == component_star(hinv_s))
    dd_ = abs(det(hb_s))
    resc = [[x * dd_ for x in r] for r in St]
    errs.append(max(abs(x - y) for r1, r2 in zip(resc, IG0) for x, y in zip(r1, r2)))
    maxes.append(max(abs(x) for r in St for x in r))
print("   wall errors", [float(e) for e in errs], "max entries", [float(x) for x in maxes])
rep("E1 wall: |det hb_s| star - I G_0 = O(s)", errs[1] < errs[0] / 5 and errs[2] < errs[1] / 5)
rep("E1 wall: star entries diverge (grow by about 10 per decade of s)", maxes[1] > 5 * maxes[0] and maxes[2] > 5 * maxes[1])

# variation sign of (1): d tr(dA ^ F) = tr(D dA ^ F) - tr(dA ^ DF) for a one-form dA (graded Leibniz), so
# tr(D dA ^ F) = d tr(dA ^ F) + tr(dA ^ DF): the new proof's '+' is right (the old proof wrote '-').
# Checked here on Grassmann forms with commuting scalar values (the sign is the form grading alone).


# (the sign is elementary: d(alpha ^ beta) = d alpha ^ beta - alpha ^ d beta for a one-form alpha; checked by hand
#  in the report rather than numerically.)

# ============================================================================
# E2. dark-energy.stelle-west-vector-frozen-point: slots of Omega_T, V, W, Theta = A ^ W, D X = A, bracket.
# ============================================================================
S24 = (1, -1, -1, -1, 1, -1)
E6 = [GA.gen(i) for i in range(6)]
N0 = GA.scal(F(1, 2), GA.add(E6[4], E6[5]))
NI = GA.sub(E6[4], E6[5])


def d6(a, b):
    return dotv(a, b, S24)


def w6(a, b):
    return wedge(a, b, S24)


def act(B, Y):
    return bvdot(B, Y, S24)


rep("E2 n0, ninf null, n0 . ninf = 1", d6(N0, N0) == 0 and d6(NI, NI) == 0 and d6(N0, NI) == 1)
for lam in (F(3, 4), F(-5, 2), F(12)):
    I = GA.add(NI, GA.scal(lam / 6, N0))
    X = N0
    V = GA.sub(X, GA.scal(d6(X, I) / d6(I, I), I))
    W = GA.scal(1 / d6(V, V), V)
    ok = d6(I, I) == lam / 3 and d6(X, I) == 1 and d6(V, I) == 0 and d6(V, V) == -3 / lam
    ok = ok and GA.eq(V, GA.add(GA.scal(-3 / lam, NI), GA.scal(F(1, 2), N0)))
    ok = ok and GA.eq(W, GA.sub(NI, GA.scal(lam / 6, N0)))
    rep(f"E2 Lambda = {lam}: (i) Q(X) = 0, <X,I> = 1, <V,I> = 0, Q(V) = -3/Lambda, slots of V and W", ok)
    A = vec([2, -1, 3, F(1, 2)])
    B2 = vec([0, 1, F(-2, 3), 4])
    theta = GA.add(GA.scal(F(-1), w6(NI, A)), w6(N0, GA.scal(lam / 6, A)))
    rep(f"E2 Lambda = {lam}: Theta(A) = -ninf ^ A + (Lambda/6) n0 ^ A = A ^ W", GA.eq(theta, w6(A, W)))
    rep(f"E2 Lambda = {lam}: (A ^ W) . n0 = A (D X = soldering form)", GA.eq(act(w6(A, W), N0), A))
    rep(f"E2 Lambda = {lam}: (A ^ W) . I = 0 (I parallel)", act(w6(A, W), I) == {} or GA.is_zero(act(w6(A, W), I)))
    rep(f"E2 Lambda = {lam}: [A ^ W, B ^ W] = (Lambda/3) A ^ B", GA.eq(comm(w6(A, W), w6(B2, W), S24), GA.scal(lam / 3, w6(A, B2))))
    # mutation: the opposite sign of the soldering term gives D X = -A
    theta_bad = GA.add(w6(NI, A), w6(N0, GA.scal(lam / 6, A)))
    rep(f"E2 Lambda = {lam} mutation +ninf ^ A: D X = A", GA.eq(act(theta_bad, N0), A), expect=False)
# slots for a generic P and Omega: compare with the Fact's display (sigma - mu_a, D mu + g rho - P sigma, rho + P mu)
Pm = [[F(x) for x in r] for r in ([1, 0, 2, -1], [3, -2, 0, 1], [0, 1, 1, 0], [2, 0, -1, 4])]


def Pmap(a):
    return GA.add(*[GA.scal(Pm[i][j] * c, E6[i]) for (j,), c in a.items() for i in range(4) if Pm[i][j]])


Om = GA.add(w6(E6[0], E6[2]), GA.scal(F(3), w6(E6[1], E6[3])))
A = vec([1, F(1, 3), -2, 0])
for (sg, mu, rho) in ((F(2), vec([1, 0, -1, 2]), F(-3)), (F(-1, 2), vec([0, 2, 1, 1]), F(5))):
    Y = GA.add(GA.scal(sg, NI), mu, GA.scal(rho, N0))
    Z = act(GA.add(Om, GA.scal(F(-1), w6(NI, A)), w6(N0, Pmap(A))), Y)
    sig_slot, rho_slot = d6(Z, N0), d6(Z, NI)
    mid = {k: v for k, v in Z.items() if k and max(k) < 4}
    ok = sig_slot == -d6(A, mu) and rho_slot == d6(Pmap(A), mu)
    ok = ok and GA.eq(mid, GA.add(act(Om, mu), GA.scal(rho, A), GA.scal(-sg, Pmap(A))))
    rep("E2 Omega_T slots equal the Fact's display (generic P, Omega)", ok)

# ============================================================================
# E3. synthesis.black-hole-data-do-not-fix-field-equations: the Wald direction and its sign.
# ============================================================================
SIG = wedge(GA.gen(1), GA.gen(0))        # sigma = gamma_1 gamma_0


def S_sigma(B):
    return GA.scal(-sp(m(B, SIG)), SIG)


# (a) Riem^o of S_sigma (C11: Riem^o(u,v,w,z) = (w ^ z) . calR(u ^ v)) against the statement's tensor eps_ab eps_cd
#     in (-,+,+,+) (eps_tr = 1, eps_ab eps^ab = -2), using C7 (all-down Riemann changes sign with the signature).
eps = [[F(0)] * 4 for _ in range(4)]
eps[0][1], eps[1][0] = F(1), F(-1)
ok = True
for u in range(4):
    for v in range(4):
        for w in range(4):
            for z in range(4):
                Ro = sp(m(wedge(GA.gen(w), GA.gen(z)), S_sigma(wedge(GA.gen(u), GA.gen(v))))) if u != v and w != z else F(0)
                # Riem_(-+++) = -Riem^o_(+---) on the same frame
                ok = ok and (-Ro) == eps[u][v] * eps[w][z]
rep("E3 S_sigma is exactly the curvature operator whose (-,+,+,+) Riemann tensor is eps_ab eps_cd (C11, C7)", ok)
gmp = [-1, 1, 1, 1]
rep("E3 eps_ab eps^ab = -2 in (-,+,+,+)", sum((eps[a][b] ** 2 * gmp[a] * gmp[b] for a in range(4) for b in range(4)), F(0)) == -2)
# (b) Ricci map of S_sigma (calR(b) = d_a . calR(a ^ b)) is -P_sigma, scalar -2
ric = []
for b in range(4):
    out = {}
    for a in range(4):
        if a == b:
            continue
        out = GA.add(out, GA.scal(F(1), GA.scal(F(-1), bvdot(S_sigma(wedge(GA.gen(a), GA.gen(b))), recip(a)))))
    ric.append({k: v for k, v in out.items() if v})
ok = all(GA.eq(ric[b], GA.scal(F(-1 if b < 2 else 0), GA.gen(b))) for b in range(4))
rep("E3 Ricci map of S_sigma = -P_sigma", ok)
rep("E3 scalar of S_sigma = -2 (Einstein term: E.eps.eps = -1/(8 pi G), S = A/4G)",
    sum((dotv(recip(b), ric[b]) for b in range(4)), F(0)) == -2)
# (c) component side of the Wald contraction for L = beta R_ab R^ab, numerically, in (-,+,+,+) with mixed Ricci
#     diag(Rt, Rr, Rth, Rph): d/dt L(R + t eps eps) where delta R_ab = g^cd eps_ca eps_db
ginv = [F(-1), F(1), F(1), F(1)]
for (Rt, Rr, Rth, Rph) in ((F(-5, 4), F(-5, 4), F(5, 4), F(5, 4)), (F(2), F(-3), F(1, 2), F(7))):
    dR = [[sum((ginv[c] * eps[c][a] * eps[c][b] for c in range(4)), F(0)) for b in range(4)] for a in range(4)]
    dmix = [ginv[a] * dR[a][a] for a in range(4)]
    mixed = [Rt, Rr, Rth, Rph]
    dL = 2 * sum((mixed[a] * dmix[a] for a in range(4)), F(0))
    rep(f"E3 component Wald contraction for R_ab R^ab = -2 (R^t_t + R^r_r) at {mixed[:2]}", dL == -2 * (Rt + Rr))
# (d) Reissner-Nordstrom Ricci map from the PG gauge field (engine torsion solver), store sign
Mr, Q2 = F(3, 2), F(5, 4)
for r0 in (F(5, 2), F(9, 2)):
    beta = lambda r: (2 * Mr / r - Q2 / (r * r)).pw(F(1, 2))  # noqa: E731
    fld = gtg.pg_field(r0, F(3, 5), F(4, 5), beta)
    Rc = fld.curvature()
    q = Q2 / r0 ** 4
    ok = fld.torsion_free()
    for a, want in enumerate([-q, -q, q, q]):
        ok = ok and GA.eq(gtg.m_val(gtg.ricci(Rc, gtg.e(a))), GA.scal(want, GA.gen(a)))
    # entropy shift / (pi beta A) = 4 (R^t_t + R^r_r) = -8 Q^2/r^4
    ok = ok and 4 * (-q - q) == -8 * Q2 / r0 ** 4
    rep(f"E3 RN at r = {r0}: store Ricci map (-q, -q, q, q), q = Q^2/r^4; R^t_t = gamma^0 . calR(gamma_0)", ok)
rep("E3 RN r_+ = 5/2 is the horizon: 1 - 2M/r + Q^2/r^2 = 0", 1 - 2 * Mr / F(5, 2) + Q2 / F(25, 4) == 0)
# (e) Schwarzschild curvature operator and Kretschmann from the field
for Ms, r0 in ((F(1), F(8)), (F(3, 2), F(12))):
    fld = gtg.schwarzschild_pg(Ms, r0, F(3, 5), F(4, 5))
    Rc = fld.curvature()
    ok = all(GA.eq(gtg.m_val(Rc[pl]), GA.scal(Ms / (2 * r0 ** 3), GA.add(gtg.biv(*pl), GA.scal(F(3), m(m(SIG, gtg.biv(*pl)), SIG)))))
             for pl in Rc)
    ok = ok and gtg.kretschmann(Rc) == 48 * Ms ** 2 / r0 ** 6 and gtg.ricci_flat(Rc)
    rep(f"E3 Schwarzschild M = {Ms}, r = {r0}: calR = (M/2r^3)(B + 3 s B s), Ricci flat, K = 48 M^2/r^6", ok)

# ============================================================================
# E4. synthesis.collapsing-hole-flux-...: k = (g1 - g0)/(1 + beta) is D-parallel along x' = e_r - e_t/(1 + beta).
# ============================================================================
for Ms, r0 in ((F(1), F(8)), (F(3, 2), F(3)), (F(1), F(2))):
    fld = gtg.schwarzschild_pg(Ms, r0, F(3, 5), F(4, 5))
    b = (2 * Ms / r0) ** 0  # placeholder
    rj = gtg.Jet.var(1, r0, 4, 2)
    bj = (2 * Ms / rj).pw(F(1, 2))
    b0, db0 = bj.v, bj.d(1).v
    # by hand: Omega(e_t) = (M/r^2) s_r, Omega(e_r) = -beta' s_r, s_r = g1 g0
    Om_t, Om_r = GA.scal(Ms / r0 ** 2, SIG), GA.scal(-db0, SIG)
    okO = GA.eq(gtg.m_val(fld.Omega(0)), Om_t) and GA.eq({k: v for k, v in gtg.m_val(fld.Omega(1)).items() if k == (0, 1)}, Om_r)
    Om_x = GA.add(Om_r, GA.scal(-1 / (1 + b0), Om_t))
    okO = okO and GA.eq(Om_x, GA.scal(b0 / (2 * r0 * (1 + b0)), SIG))
    kvec = GA.scal(1 / (1 + b0), GA.sub(GA.gen(1), GA.gen(0)))
    dk_dr = GA.scal(-db0 / (1 + b0) ** 2, GA.sub(GA.gen(1), GA.gen(0)))
    Dk = GA.add(dk_dr, bvdot(Om_x, kvec))
    # physical velocity of x' through hb^{-1}(a) = a + beta (a.e_t) e_r
    xp = vec([-1 / (1 + b0), 1, 0, 0])
    hk = GA.add(xp, GA.scal(b0 * dotv(xp, GA.gen(0)), GA.gen(1)))
    rep(f"E4 M = {Ms}, r = {r0}: Omega values, hb^-1(x') = k, D_x' k = 0 (by hand)",
        okO and GA.eq(hk, kvec) and GA.is_zero(Dk) and dotv(kvec, kvec) == 0)
    # the control as it should be: along the t-parametrised ray the physical velocity is g0 - g1, not D-parallel
    xt = vec([1, -1 - b0, 0, 0])
    kt = GA.add(xt, GA.scal(b0 * dotv(xt, GA.gen(0)), GA.gen(1)))
    rep(f"E4 M = {Ms}, r = {r0}: hb^-1(e_t - (1 + beta) e_r) = g0 - g1 (the check's control uses e_t - (1+beta) e_r instead)",
        GA.eq(kt, GA.sub(GA.gen(0), GA.gen(1))))
    Om_xt = GA.add(Om_t, GA.scal(-1 - b0, Om_r))
    rep(f"E4 M = {Ms}, r = {r0}: D_{{x_t}}(g0 - g1) != 0 (t is not affine)", not GA.is_zero(bvdot(Om_xt, kt)))
    if r0 == 2 * Ms:
        K = GA.add(GA.gen(0), GA.scal(b0, GA.gen(1)))
        rep(f"E4 M = {Ms}: (K.D)K = Omega(e_t) . K = K/4M at r = 2M", GA.eq(bvdot(Om_t, K), GA.scal(1 / (4 * Ms), K)))

# ============================================================================
# E5 and E10. Dilation fields hb^{-1}(a) = a/sigma: Omega(a) = (grad sigma ^ a)/sigma and calR(B) = Q(I) B for
#     every sigma = s + m.x - (r/2) Q(x) (general case: R(a ^ b) = -(2 r sigma + Q(grad sigma))/sigma^2 a ^ b).
# ============================================================================


def dilation_field(s, mv, r, x0):
    def rows(X):
        qx = X[0] * X[0] - X[1] * X[1] - X[2] * X[2] - X[3] * X[3]
        mx = mv[0] * X[0] - mv[1] * X[1] - mv[2] * X[2] - mv[3] * X[3]
        inv = (s + mx - (r / 2) * qx).inv()
        return [[inv if a == mu else F(0) for a in range(4)] for mu in range(4)]
    return gtg.field_from_hbinv(rows, x0)


for (s, mv, r, x0) in ((F(1), [0, 0, 0, 0], F(1, 8), (F(1, 3), F(-1, 4), F(1, 5), F(0))),
                       (F(1), [1, 0, 0, 0], F(1, 2), (F(1, 7), F(1, 2), F(0), F(-1, 3))),
                       (F(2), [0, 1, F(1, 2), 0], F(3, 4), (F(-1, 5), F(0), F(1, 4), F(2, 9))),
                       (F(-1), [F(1, 3), 0, 0, 2], F(-2), (F(1, 6), F(1, 5), F(-1, 7), F(0)))):
    x = vec(list(x0))
    mvv = vec(mv)
    sig = s + dotv(mvv, x) - (r / 2) * dotv(x, x)
    grad = GA.sub(mvv, GA.scal(r, x))
    QI = 2 * r * s + dotv(mvv, mvv)
    fld = dilation_field(s, mv, r, x0)
    ok = fld.torsion_free()
    ok = ok and all(GA.eq(gtg.m_val(fld.Omega(mu)), GA.scal(1 / sig, wedge(grad, GA.gen(mu)))) for mu in range(4))
    ok = ok and all(GA.eq(gtg.m_val(fld.strength(p, q)), GA.scal(-(2 * r * sig + dotv(grad, grad)) / sig ** 2, wedge(GA.gen(p), GA.gen(q))))
                    for p in range(4) for q in range(p + 1, 4))
    ok = ok and 2 * r * sig + dotv(grad, grad) == QI
    Rc = fld.curvature()
    ok = ok and all(GA.eq(gtg.m_val(Rc[pl]), GA.scal(QI, gtg.biv(*pl))) for pl in Rc)
    rep(f"E5/E10 sigma = {s} + m.x - ({r}/2)Q(x): Omega = grad sigma ^ a/sigma, R = -Q(I)/sigma^2, calR = Q(I) B (Q(I) = {QI})", ok)
# E5 special case sigma = 1 - Lambda Q/12: Q(I) = Lambda/3 (s = 1, m = 0, r = Lambda/6)
rep("E5 sigma = 1 - Lambda Q/12 is (s, m, r) = (1, 0, Lambda/6), Q(I) = Lambda/3", 2 * (F(3, 4) / 6) * 1 == F(3, 4) / 3)
# C11 reading: Riem^o(a,b,c,d) = -(Lambda/3)(g_ac g_bd - g_ad g_bc) for calR = (Lambda/3) id
lamv = F(3, 4)
ok = True
for a in range(4):
    for b in range(4):
        for c in range(4):
            for d in range(4):
                if a == b or c == d:
                    continue
                Ro = sp(m(wedge(GA.gen(c), GA.gen(d)), GA.scal(lamv / 3, wedge(GA.gen(a), GA.gen(b)))))
                want = -(lamv / 3) * (ETA[a] * (a == c) * ETA[b] * (b == d) - ETA[a] * (a == d) * ETA[b] * (b == c))
                ok = ok and Ro == want
rep("E5 Riem^o of (Lambda/3) id is -(Lambda/3)(g_ac g_bd - g_ad g_bc) in (+,-,-,-)", ok)

# ============================================================================
# E6. synthesis.frozen-point-reduces-...: the contractions listed in (i) of the proof.
# ============================================================================
a = vec([1, 2, 0, -1])
sv = vec([0, 1, 3, 1])
rep("E6 (ninf ^ a) . ninf = 0", GA.is_zero(act(w6(NI, a), NI)))
rep("E6 (ninf ^ a) . n0 = -a", GA.eq(act(w6(NI, a), N0), GA.scal(F(-1), a)))
rep("E6 (n0 ^ s) . ninf = -s", GA.eq(act(w6(N0, sv), NI), GA.scal(F(-1), sv)))
rep("E6 (n0 ^ s) . n0 = 0", GA.is_zero(act(w6(N0, sv), N0)))
rep("E6 proof's line (ninf ^ n0) . ninf = -n0", GA.eq(act(w6(NI, N0), NI), GA.scal(F(-1), N0)), expect=False)
rep("E6 correct value (ninf ^ n0) . ninf = +ninf", GA.eq(act(w6(NI, N0), NI), NI))
rep("E6 proof's line (ninf ^ n0) . n0 = ninf", GA.eq(act(w6(NI, N0), N0), NI), expect=False)
rep("E6 correct value (ninf ^ n0) . n0 = -n0", GA.eq(act(w6(NI, N0), N0), GA.scal(F(-1), N0)))
for rho in (F(3, 7), F(-2, 5)):
    I = GA.add(NI, GA.scal(rho, N0))
    Sa = vec([2, 0, -1, 1])
    bet = F(5, 3)
    OT = GA.add(w6(E6[1], E6[2]), GA.scal(F(-1), w6(NI, a)), w6(N0, Sa), GA.scal(bet, w6(NI, N0)))
    DI = act(OT, I)
    DX = act(OT, N0)
    rep(f"E6 rho = {rho}: DI(a) = rho a - S(a) + beta (ninf - rho n0) (the statement's formula)",
        GA.eq(DI, GA.add(GA.scal(rho, a), GA.scal(F(-1), Sa), GA.scal(bet, GA.sub(NI, GA.scal(rho, N0))))))
    rep(f"E6 rho = {rho}: DX(a) = a - beta n0", GA.eq(DX, GA.sub(a, GA.scal(bet, N0))))

# ============================================================================
# E7. synthesis.killing-horizon-value-factor-...: (K.D)K = beta(r_h) f'(r_h)/2 K, signs per chart.
# ============================================================================


def kappa_at(beta_fn, rh):
    fld = gtg.pg_field(rh, F(3, 5), F(4, 5), beta_fn)
    rj = gtg.Jet.var(1, rh, 4, 2)
    bj = beta_fn(rj)
    K = {(0,): gtg.Jet.const(1, 4), (1,): bj}
    Kv = gtg.m_val(K)
    DK = gtg.m_val(fld.cov(0, K))
    # (K.D)K = D_{e_t} K since hb(K) = e_t
    if dotv(Kv, Kv) != 0:
        return None, bj.v
    # read kappa from DK = kappa K
    kap = DK.get((0,), F(0)) / Kv[(0,)]
    return (kap if GA.eq(DK, GA.scal(kap, Kv)) else "not prop"), bj.v


H = F(2, 3)
k1, b1 = kappa_at(lambda r: H * r, 1 / H)
rep(f"E7 de Sitter beta = +rH: beta(r_h) = {b1}, kappa = {k1} = -H", k1 == -H and b1 == 1)
k2, b2 = kappa_at(lambda r: -H * r, 1 / H)
rep(f"E7 de Sitter beta = -rH (expanding): beta(r_h) = {b2}, kappa = {k2} = +H", k2 == H and b2 == -1)
# in the beta = +rH chart the stuck radial null ray at r_h is the outgoing one (dr/dt = +1 - beta = 0): the past
# horizon is generated by outgoing rays; in the expanding chart the ingoing one (dr/dt = -1 - beta = 0)
rep("E7 beta = +rH: outgoing ray stuck at r_h; beta = -rH: ingoing ray stuck", (1 - b1) == 0 and (-1 - b2) == 0)
Ms, H2 = F(3, 7), F(1, 7)
fS = lambda r: 1 - 2 * Ms / r - H2 * r * r  # noqa: E731
rep("E7 SdS f(1) = f(2) = 0", fS(F(1)) == 0 and fS(F(2)) == 0)
for rh, want in ((F(1), F(2, 7)), (F(2), F(-5, 28))):
    kk, bb = kappa_at(lambda r: (2 * Ms / r + H2 * r * r).pw(F(1, 2)), rh)
    rep(f"E7 SdS r_h = {rh}: beta = {bb}, kappa = {kk} (want {want})", kk == want and bb == 1)
k3, _ = kappa_at(lambda r: (2 / r).pw(F(1, 2)), F(2))
rep(f"E7 Schwarzschild M = 1: kappa = {k3} = 1/4", k3 == F(1, 4))
# Omega(e_t) = -beta beta' sigma_r for a general beta (the label chart of the engine), no angular part
for (b, db, r0) in ((F(1, 3), F(-2, 5), F(3)), (F(-7, 4), F(5, 9), F(2, 7))):
    fld = gtg.pg_field(r0, F(5, 13), F(12, 13), lambda r, b=b, db=db, r0=r0: b + db * (r - r0))
    rep(f"E7 beta = {b}, beta' = {db}: Omega(e_t) = -beta beta' sigma_r exactly",
        GA.eq(gtg.m_val(fld.Omega(0)), GA.scal(-b * db, SIG)) and fld.torsion_free())
    # the angular components of the closed form are the label chart's (they carry the polar frame's rotation)
    om2 = gtg.m_val(fld.omega(2))
    rep(f"E7 beta = {b}: omega(gamma_2) = (beta g0 + g1) ^ g2 / r (label chart)",
        GA.eq(om2, GA.scal(1 / r0, wedge(GA.add(GA.scal(b, GA.gen(0)), GA.gen(1)), GA.gen(2)))))


# E7 (iv) at a horizon with beta = 1: k = e_t + e_r, m = (e_t - e_r)/2, k . m = 1, k ^ m = sigma_r, and with
# Omega(e_t) = (f'/2) sigma_r the Killing bivector F_K = -Omega(e_t) = -kappa k ^ m, kappa = f'/2
kk_ = GA.add(GA.gen(0), GA.gen(1))
mm_ = GA.scal(F(1, 2), GA.sub(GA.gen(0), GA.gen(1)))
rep("E7 k . m = 1 and k ^ m = sigma_r", dotv(kk_, mm_) == 1 and GA.eq(wedge(kk_, mm_), SIG))
for fp2 in (F(1, 4), F(-2, 3), F(2, 7)):
    FK = GA.scal(-fp2, SIG)
    rep(f"E7 kappa = {fp2}: K . F_K = kappa K and F_K^2 = kappa^2", GA.eq(GA.scal(F(-1), bvdot(FK, kk_)), GA.scal(fp2, kk_)) and GA.eq(m(FK, FK), {(): fp2 ** 2}))
    rep(f"E7 kappa = {fp2}: (K.D)K = Omega(e_t) . K = kappa K", GA.eq(bvdot(GA.scal(fp2, SIG), kk_), GA.scal(fp2, kk_)) and GA.eq(m(FK, FK), {(): fp2 ** 2}))

# ============================================================================
# E8. synthesis.macdowell-mansouri-...: the 'outer product of Cl(1,4)' form product equals the Grassmann
#     product for every signature, so the new check cannot distinguish the reading it is meant to test.
# ============================================================================


def fprod(X, Y, sig):
    out = {}
    for a_, A in X.items():
        for b_, B in Y.items():
            s, g = GA.blade_mul(a_, b_, sig)
            if s != 0 and len(g) == len(a_) + len(b_):
                out[g] = GA.add(out.get(g, {}), GA.scal(s, GA.mul(A, B, S24)))
    return {g: v for g, v in out.items() if v}


Xf = {(0,): E6[1], (2,): GA.add(E6[0], E6[4]), (4,): E6[5]}
Yf = {(1, 3): w6(E6[2], E6[3]), (0, 4): w6(E6[0], E6[5]), (2,): E6[3]}
prods = [fprod(Xf, Yf, sig) for sig in ((1, -1, -1, -1, -1), (0, 0, 0, 0, 0), (1, 1, 1, 1, 1), (-1, 2, 3, -5, 7))]
rep("E8 the grade-additive part of the Clifford product of background blades is signature independent",
    all(p == prods[0] for p in prods[1:]))

# ============================================================================
# E9. synthesis.nondiagonal-kasner-residue-weighted-shear: torsion solution vs the closed form, a shear not in the check.
# ============================================================================
P = [F(-2, 7), F(3, 7), F(6, 7)]
TH0 = [[F(1), F(1, 2), F(0)], [F(0), F(1), F(-1, 3)], [F(2), F(0), F(1)]]


def kasner_case(c, q, N):
    """G = 1 + c tau^q N, tau0 = 1; rows of hb^{-1}: hb^{-1}(e_tau) = g0, hb^{-1}(e_i) = sum_l E_li g_l, E = Delta G TH0."""
    def rows(X):
        tau = X[0]
        Dl = [tau.pw(p) for p in P]
        tq = tau.pw(q)
        G = [[(F(1) if i == j else F(0)) + c * tq * N[i][j] for j in range(3)] for i in range(3)]
        E = [[sum((Dl[l] * G[l][k] * TH0[k][i] for k in range(3)), F(0) * tau) for i in range(3)] for l in range(3)]
        out = [[gtg.Jet.const(1, 4), F(0), F(0), F(0)]]
        for i in range(3):
            out.append([F(0)] + [E[l][i] for l in range(3)])
        return out
    fld = gtg.field_from_hbinv(rows, (F(1), F(0), F(0), F(0)))
    # B at tau = 1: Omega = tau G' G^{-1} = c q N (G = 1 at tau = 1, G' = c q N), Delta = 1
    Bm = [[(P[i] if i == j else F(0)) + c * q * N[i][j] for j in range(3)] for i in range(3)]
    return fld, Bm


for (c, q, N) in ((F(2), F(1, 3), [[0, 1, 0], [0, 0, 0], [0, 0, 0]]),
                  (F(-1, 2), F(5, 7), [[0, 0, 0], [0, 0, 0], [1, 0, 0]]),
                  (F(3), F(1), [[0, 0, 0], [0, 0, 1], [0, 0, 0]])):
    N = [[F(x) for x in r] for r in N]
    fld, Bm = kasner_case(c, q, N)
    sym = [[(Bm[i][j] + Bm[j][i]) / 2 for j in range(3)] for i in range(3)]
    asy = [[(Bm[i][j] - Bm[j][i]) / 2 for j in range(3)] for i in range(3)]
    ok = fld.torsion_free()
    for mm in range(3):
        w = gtg.m_val(fld.omega(mm + 1))
        ok = ok and all(w.get((0, l + 1), F(0)) == -sym[l][mm] for l in range(3))
    w0 = gtg.m_val(fld.omega(0))
    ok = ok and GA.eq(w0, {(l + 1, j + 1): asy[l][j] for l in range(3) for j in range(l + 1, 3) if asy[l][j]})
    ok = ok and any(asy[l][j] for l in range(3) for j in range(3))
    # second fundamental form (g_m . D) g0 = sum_l sym(B)_lm g_l
    for mm in range(3):
        A = [0] + [1 if k == mm else 0 for k in range(3)]
        Dg0 = gtg.m_val(fld.cov_phys(A, {(0,): gtg.Jet.const(1, 4)}))
        ok = ok and GA.eq(Dg0, vec([0] + [sym[l][mm] for l in range(3)]))
    rep(f"E9 shear c = {c}, q = {q}: omega(g_m) boost = -sym(B)/tau, omega(g0) = antisym(B)/tau, tau K = sym(B)", ok)
    # mutation: the opposite boost sign
    w = gtg.m_val(fld.omega(1))
    rep(f"E9 shear c = {c} mutation boost +sym(B)", all(w.get((0, l + 1), F(0)) == sym[l][0] for l in range(3)), expect=False)

print()
print("total", len(RESULTS), "PASS", RESULTS.count("PASS"), "FAIL", RESULTS.count("FAIL"))
