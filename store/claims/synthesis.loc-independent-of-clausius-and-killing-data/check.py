"""synthesis.loc-independent-of-clausius-and-killing-data: exact checks.

A model of every premise except (Loc): the local-horizon entropy density 1/4 (1 + c S_ab S^ab), S the
tracefree Ricci tensor. Curvatures are computed from the metrics with exact truncated Taylor jets.
(1) On Schwarzschild-de Sitter and de Sitter (Lambda-vacuum) S = 0, so the density is 1/4: every Killing-horizon
datum is the general-relativistic one. (2) The Einstein static universe with dust, metric
-dt^2 + 4a^2 |dx|^2/(1 + |x|^2)^2: Ric(e_t, e_t) = 0, Ric(e_i, e_j) = (2/a^2) delta_ij, S_ab S^ab = 3/a^4 at two
points; for several rational null k the Clausius defect T(k,k) - (eta/2 pi) Ric(k,k) of the stored theorem
vanishes with eta = 1/4 (1 + 3c/a^4) and 8 pi rho = 2(1 + 3c/a^4)/a^2; the dust is conserved (Gamma^b_tt = 0,
Gamma^a_at = 0) and the integration constant is Lambda_J = 1/a^2. (3) eta differs between the two spacetimes,
so it depends on the curvature at the point. pi is carried as a formal factor (mu = 8 pi rho is rational).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise

NV = 4
D = 3
SQ = [-1, 1, 1, 1]          # orthonormal frame (t, r, theta, phi), signature (-,+,+,+)


# ---- exact truncated Taylor jets in the four coordinate displacements --------------------------
def jconst(c):
    return {(0, 0, 0, 0): F(c)} if c != 0 else {}


def jvar(i):
    e = [0, 0, 0, 0]
    e[i] = 1
    return {tuple(e): F(1)}


def jadd(a, b, s=1):
    out = dict(a)
    for e, v in b.items():
        out[e] = out.get(e, F(0)) + s * v
    return {e: v for e, v in out.items() if v != 0}


def jscal(c, a):
    return {e: c * v for e, v in a.items() if c * v != 0}


def jmul(a, b, d):
    out = {}
    for e1, v1 in a.items():
        for e2, v2 in b.items():
            e = tuple(x + y for x, y in zip(e1, e2))
            if sum(e) <= d:
                out[e] = out.get(e, F(0)) + v1 * v2
    return {e: v for e, v in out.items() if v != 0}


def jinv(a, d):
    c0 = a.get((0, 0, 0, 0), F(0))
    assert c0 != 0
    x = jscal(-1 / c0, jadd(a, jconst(c0), -1))
    term, out = jconst(1), jconst(1)
    for _ in range(d):
        term = jmul(term, x, d)
        out = jadd(out, term)
    return jscal(1 / c0, out)


def jderiv(a, i):
    out = {}
    for e, v in a.items():
        if e[i] > 0:
            ee = list(e)
            ee[i] -= 1
            out[tuple(ee)] = out.get(tuple(ee), F(0)) + v * e[i]
    return out


def jval(a):
    return a.get((0, 0, 0, 0), F(0))


def jdr(a):
    return a.get((0, 1, 0, 0), F(0))


def christoffel(g):
    ginv = [jinv(g[a], D) for a in range(NV)]
    G = {}
    for a, b, c in product(range(NV), repeat=3):
        s = {}
        if a == c:
            s = jadd(s, jderiv(g[a], b))
        if a == b:
            s = jadd(s, jderiv(g[a], c))
        if b == c:
            s = jadd(s, jderiv(g[b], a), -1)
        if s:
            G[(a, b, c)] = jscal(F(1, 2), jmul(ginv[a], s, D - 1))
    return G


def riemann(g):
    """lowered R_{abcd} = g_aa (d_c G^a_db - d_d G^a_cb + G^a_ce G^e_db - G^a_de G^e_cb)"""
    G = christoffel(g)
    Rl = {}
    for a, b, c, d in product(range(NV), repeat=4):
        if c >= d:
            continue
        s = jadd(jderiv(G.get((a, d, b), {}), c), jderiv(G.get((a, c, b), {}), d), -1)
        for e in range(NV):
            s = jadd(s, jmul(G.get((a, c, e), {}), G.get((e, d, b), {}), D - 2))
            s = jadd(s, jmul(G.get((a, d, e), {}), G.get((e, c, b), {}), D - 2), -1)
        low = jmul(g[a], s, D - 2)
        if low:
            Rl[(a, b, c, d)] = low
            Rl[(a, b, d, c)] = jscal(-1, low)
    return Rl, G


def R4(Rl, a, b, c, d):
    return jval(Rl.get((a, b, c, d), {}))


def ricci(g, Rl):
    return {(b, d): sum(R4(Rl, a, b, a, d) / jval(g[a]) for a in range(NV)) for b in range(NV) for d in range(NV)}


def tracefree_square(g, Ric):
    """S_ab S^ab for a diagonal metric, S = Ric - (R/4) g"""
    gi = [1 / jval(g[a]) for a in range(NV)]
    Rs = sum(gi[a] * Ric[(a, a)] for a in range(NV))
    S = {(a, b): Ric[(a, b)] - (Rs / 4 * jval(g[a]) if a == b else 0) for a in range(NV) for b in range(NV)}
    return sum(gi[a] * gi[b] * S[(a, b)] ** 2 for a in range(NV) for b in range(NV)), Rs


def sds(M, Lam, r0):
    r = jadd(jconst(r0), jvar(1))
    r2 = jmul(r, r, D)
    f = jadd(jadd(jconst(1), jscal(-2 * M, jinv(r, D))), jscal(-Lam / 3, r2))
    z = jvar(2)
    omz = jadd(jconst(1), jmul(z, z, D), -1)
    return [jscal(-1, f), jinv(f, D), jmul(r2, jinv(omz, D), D), jmul(r2, omz, D)]


def esu(a, x0):
    """-dt^2 + A (dx^2 + dy^2 + dz^2), A = 4 a^2 / (1 + |x|^2)^2, about (0, x0)"""
    rho2 = jconst(0)
    for i in range(3):
        xi = jadd(jconst(x0[i]), jvar(i + 1))
        rho2 = jadd(rho2, jmul(xi, xi, D))
    den = jadd(jconst(1), rho2)
    A = jscal(4 * a * a, jinv(jmul(den, den, D), D))
    return [jconst(-1), A, A, A]


def eta_model(c, S2):
    return F(1, 4) * (1 + c * S2)


C_MODEL = F(5, 3)
SQ = [-1, 1, 1, 1]


def check_vacuum_density_is_one_quarter():
    premise("synthesis.black-hole-data-do-not-fix-field-equations")
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    premise("synthesis.sds-clausius-fixes-area-constant")
    for (M, Lam, r0) in ((F(1), F(3, 100), F(3)), (F(1, 2), F(1, 10), F(7, 5)), (F(0), F(1, 10), F(2))):
        g = sds(M, Lam, r0)
        Rl, G = riemann(g)
        Ric = ricci(g, Rl)
        S2, Rs = tracefree_square(g, Ric)
        GA.check("Lambda-vacuum: R = 4 Lambda, S = 0", Rs == 4 * Lam and S2 == 0)
        GA.check("model density 1/4 on vacuum patches", eta_model(C_MODEL, S2) == F(1, 4))
        anchors = {F(3): (F(3, 25), F(227, 2700)), F(7, 5): (F(2, 5), F(4093, 10290)), F(2): (F(2, 5), F(1, 30))}
        K = R4(Rl, 2, 3, 2, 3) / (jval(g[2]) * jval(g[3]))
        GA.check("anchor R and K_edge", (Rs, K) == anchors[r0])


def check_einstein_static_universe_model():
    premise("synthesis.einstein-equations-from-c-loc-and-clausius")
    premise("synthesis.c-loc-entropy-clause-curvature-independent-density")
    for a in (F(2), F(3, 2)):
        Ge = 1 / (1 + 3 * C_MODEL / a ** 4)                 # Newton coupling of the model in ESU
        eta = eta_model(C_MODEL, 3 / a ** 4)
        GA.check("eta = 1/(4 G_e) != 1/4", eta == 1 / (4 * Ge) and eta != F(1, 4))
        mu = 2 / (Ge * a ** 2)                              # mu = 8 pi rho
        anchors = {F(2): (F(21, 64), F(21, 32)), F(3, 2): (F(161, 324), F(1288, 729))}
        GA.check("anchor eta, 8 pi rho", (eta, mu) == anchors[a])
        for x0 in ((F(0), F(0), F(0)), (F(1, 2), F(1, 3), F(-1, 5))):
            g = esu(a, x0)
            Rl, G = riemann(g)
            Ric = ricci(g, Rl)
            S2, Rs = tracefree_square(g, Ric)
            A0 = jval(g[1])
            GA.check("Ric(e_t, e_t) = 0, Ric(e_i, e_j) = (2/a^2) delta_ij",
                     Ric[(0, 0)] == 0 and all(Ric[(i, j)] == (2 / a ** 2 * A0 if i == j else 0)
                                              for i in range(1, 4) for j in range(1, 4))
                     and all(Ric[(0, i)] == 0 for i in range(1, 4)))
            GA.check("S_ab S^ab = 3/a^4, R = 6/a^2", S2 == 3 / a ** 4 and Rs == 6 / a ** 2)
            GA.check("model density uses the computed curvature", eta_model(C_MODEL, S2) == eta)
            # dust at rest is conserved: Gamma^b_tt = 0 and Gamma^a_at = 0
            GA.check("u = d_t geodesic and expansion-free",
                     all(jval(G.get((b, 0, 0), {})) == 0 for b in range(NV))
                     and sum(jval(G.get((b, b, 0), {})) for b in range(NV)) == 0)
            for n in ((F(1), F(0), F(0)), (F(3, 5), F(4, 5), F(0)), (F(2, 7), F(3, 7), F(6, 7)), (F(1, 3), F(-2, 3), F(2, 3))):
                kon = {(0,): F(1)}
                for i in range(3):
                    if n[i]:
                        kon[(i + 1,)] = n[i]
                GA.check("k null (GA)", GA.dot(kon, kon, SQ) == 0)
                # coordinate components: k = e_t + n^i e_i, e_i = d_i / sqrt(A0); Ric(k,k) via the orthonormal frame
                ric_kk = Ric[(0, 0)] + sum(n[i] * n[j] * Ric[(i + 1, j + 1)] / A0 for i in range(3) for j in range(3))
                T_kk_8pi = mu                                   # 8 pi T(k,k) = 8 pi rho (u.k)^2, u.k = -1
                # stored defect: T(k,k) - (eta/2 pi) Ric(k,k) = 0  <=>  8 pi T(k,k) = 4 eta Ric(k,k)
                GA.check("Clausius balance with the model density", T_kk_8pi == 4 * eta * ric_kk)
                GA.check("same balance fails with eta = 1/4", T_kk_8pi != 4 * F(1, 4) * ric_kk)
            # integration constant: G_tt + Lambda_J g_tt = 8 pi G_e T_tt
            G_tt = Ric[(0, 0)] - Rs / 2 * jval(g[0])
            Lam_J = G_tt - Ge * mu
            GA.check("Lambda_J = 1/a^2", Lam_J == 1 / a ** 2)
            G_xx = Ric[(1, 1)] - Rs / 2 * A0
            GA.check("spatial equations: G_ij + Lambda_J g_ij = 0", G_xx + Lam_J * A0 == 0)
