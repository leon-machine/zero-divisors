"""dark-energy.gravity-pre-metric-forces-degenerate-exactly: exact checks of the computable content
(widening the trace identities of legacy verify_T10.py, thm:twokinds).

  (1) Star-free quadratic invariants are topological: for a gl(2)-valued connection A with polynomial
      components on R^4 (exact multivariate polynomials), F = dA + A ^ A, the identity
      tr(F ^ F) = d tr(A ^ dA + (2/3) A ^ A ^ A) holds coefficient by coefficient, and the Bianchi identity
      eps^{mu nu rho sigma} D_nu F_{rho sigma} = 0 (which is the Euler-Lagrange expression of tr(F ^ F), so
      no field equations) holds identically; an abelian and a nonabelian sample.
  (2) The Hodge star on 2-forms in four dimensions depends on the conformal class only: for derived metrics
      g = hb^{-T} eta hb^{-1} of sample gauge fields (rational matrices, sqrt|g| = |det hb^{-1}| exact), the
      6x6 matrix of star is unchanged under g -> c^2 g, changes under a non-conformal change of hb, and
      squares to -1 (Lorentzian).
  (3) At a corank-one wall (the soldering form with a simple pole in one leg, hb^{-1}(e_1) = e_1/s, so the
      cometric g^{11} = -s^2 acquires a radical and the metric a pole as s -> 0): the star entries grow
      like 1/s (no limit), and the bounded rescaling s star tends to a map of rank 3 of 6 (degenerate); tr(F ^ F)
      in (1) used no metric and is unaffected.
Clause (1)'s first route (no invariant eps(I, ., F_i, F_i) because I is an internal singlet) is structural
and is not tested.
"""
from fractions import Fraction as F
from itertools import permutations

import GA
from tp_premise import premise

ETA = [1, -1, -1, -1]


# ---- exact polynomials in (x0, x1, x2, x3): dict {exponent tuple: Fraction} --------------------------
def padd(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def pscal(c, p):
    return {k: c * v for k, v in p.items()} if c != 0 else {}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = out.get(k, F(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def pder(p, mu):
    out = {}
    for k, v in p.items():
        if k[mu]:
            kk = list(k)
            kk[mu] -= 1
            out[tuple(kk)] = out.get(tuple(kk), F(0)) + v * k[mu]
    return {k: v for k, v in out.items() if v != 0}


def mono(c, e):
    return {tuple(e): F(c)}


# ---- 2x2 matrices of polynomials ------------------------------------------------------------------------
def madd(*Ms):
    return [[padd(*[M[i][j] for M in Ms]) for j in range(2)] for i in range(2)]


def mscal(c, M):
    return [[pscal(c, M[i][j]) for j in range(2)] for i in range(2)]


def mmul(A, B):
    return [[padd(pmul(A[i][0], B[0][j]), pmul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def mder(M, mu):
    return [[pder(M[i][j], mu) for j in range(2)] for i in range(2)]


def tr(M):
    return padd(M[0][0], M[1][1])


def psign(p):
    s = 1
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def curvature(A):
    return {(m, n): madd(mder(A[n], m), mscal(-1, mder(A[m], n)), mmul(A[m], A[n]), mscal(-1, mmul(A[n], A[m])))
            for m in range(4) for n in range(4)}


Z = {}
ABELIAN = [[[mono(1, (0, 1, 0, 0)), Z], [Z, Z]], [[mono(2, (1, 0, 0, 1)), Z], [Z, Z]],
           [[mono(-1, (0, 0, 0, 2)), Z], [Z, Z]], [[mono(3, (0, 1, 1, 0)), Z], [Z, Z]]]
NONABELIAN = [[[mono(1, (0, 1, 0, 0)), mono(1, (0, 0, 1, 0))], [Z, mono(-1, (0, 1, 0, 0))]],
              [[Z, mono(2, (1, 0, 0, 0))], [mono(1, (0, 0, 0, 1)), Z]],
              [[mono(1, (0, 0, 0, 1)), Z], [mono(-1, (1, 1, 0, 0)), mono(-1, (0, 0, 0, 1))]],
              [[Z, mono(1, (0, 0, 1, 0))], [mono(1, (0, 0, 0, 0)), Z]]]


def check_star_free_invariant_is_topological():
    ok = True
    for A in (ABELIAN, NONABELIAN):
        Fc = curvature(A)
        lhs, rhs, bianchi = {}, {}, {}
        for p in permutations(range(4)):
            s = psign(p)
            m, n, r, t = p
            lhs = padd(lhs, pscal(F(s, 4), tr(mmul(Fc[(m, n)], Fc[(r, t)]))))
            cs = padd(tr(mmul(A[n], mder(A[t], r))), pscal(F(2, 3), tr(mmul(mmul(A[n], A[r]), A[t]))))
            rhs = padd(rhs, pscal(F(s), pder(cs, m)))
        for mu in range(4):
            for i in range(2):
                for j in range(2):
                    tot = {}
                    for p in permutations(range(4)):
                        if p[0] != mu:
                            continue
                        s = psign(p)
                        _, n, r, t = p
                        DF = madd(mder(Fc[(r, t)], n), mmul(A[n], Fc[(r, t)]), mscal(-1, mmul(Fc[(r, t)], A[n])))
                        tot = padd(tot, pscal(F(s), DF[i][j]))
                    ok = ok and tot == {}
        ok = ok and lhs == rhs and lhs != {}
    GA.check("tr(F ^ F) = d CS identically; Bianchi: no field equations", ok)
    assert ok


def metric_of(hinv):
    """g_{mu nu} = hb^{-1}(e_mu) . hb^{-1}(e_nu) with columns of hinv the images; returns g, sqrt|g|."""
    g = [[sum(ETA[k] * hinv[k][m] * hinv[k][n] for k in range(4)) for n in range(4)] for m in range(4)]
    return g, abs(det(hinv))


def det(M):
    if len(M) == 1:
        return M[0][0]
    return sum(((-1) ** c) * M[0][c] * det([r[:c] + r[c + 1:] for r in M[1:]]) for c in range(len(M)) if M[0][c])


def inverse(M):
    n = len(M)
    cols = []
    for c in range(n):
        A = [[F(M[i][j]) for j in range(n)] + [F(1 if i == c else 0)] for i in range(n)]
        for col in range(n):
            piv = next(r for r in range(col, n) if A[r][col] != 0)
            A[col], A[piv] = A[piv], A[col]
            pv = A[col][col]
            A[col] = [x / pv for x in A[col]]
            for r in range(n):
                if r != col and A[r][col] != 0:
                    f = A[r][col]
                    A[r] = [x - f * y for x, y in zip(A[r], A[col])]
        cols.append([A[i][n] for i in range(n)])
    return [[cols[j][i] for j in range(n)] for i in range(n)]


PL = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def star(g, vol):
    gi = inverse(g)
    M = []
    for (a, b) in PL:                      # output component (*w)_{ab}
        row = []
        for (c, d) in PL:                  # input w_{cd} (w_{cd} = -w_{dc})
            tot = F(0)
            for al in range(4):
                for be in range(4):
                    if len({al, be, a, b}) < 4:
                        continue
                    e = psign((al, be, a, b))
                    tot += F(1, 2) * vol * e * (gi[al][c] * gi[be][d] - gi[al][d] * gi[be][c])
            row.append(tot)
        M.append(row)
    return M


H1 = [[2, 1, 0, 0], [0, 1, 0, 1], [1, 0, 3, 0], [0, 0, 1, 1]]
H2 = [[1, 0, 0, 0], [1, 2, 0, 0], [0, 0, 1, 0], [0, 1, 0, 3]]


def check_hodge_star_depends_on_conformal_class_only():
    ok = True
    stars = []
    for H in (H1, H2):
        hinv = [[F(x) for x in r] for r in H]
        g, vol = metric_of(hinv)
        ok = ok and det(g) < 0
        S0 = star(g, vol)
        for c in (F(2), F(1, 3)):
            g2, vol2 = metric_of([[c * x for x in r] for r in hinv])
            ok = ok and star(g2, vol2) == S0
        S2 = [[sum(S0[i][k] * S0[k][j] for k in range(6)) for j in range(6)] for i in range(6)]
        ok = ok and S2 == [[F(-1) if i == j else F(0) for j in range(6)] for i in range(6)]
        stars.append(S0)
    ok = ok and stars[0] != stars[1]
    GA.check("the star on 2-forms depends only on the conformal class", ok)
    assert ok


def check_star_degenerates_at_corank_one_wall():
    premise("dark-energy.imported-walls-sphere-theorem")
    ok = True
    maxima = []
    for s in (F(1, 10), F(1, 100), F(1, 1000)):
        hinv = [[F(1), 0, 0, 0], [0, 1 / s, 0, 0], [0, 0, F(1), 0], [0, 0, 0, F(1)]]
        g, vol = metric_of(hinv)
        gi = inverse(g)
        ok = ok and gi[1][1] == -s * s and g[1][1] == -1 / (s * s)
        S0 = star(g, vol)
        maxima.append(max(abs(x) for r in S0 for x in r))
        sS = [[s * x for x in r] for r in S0]
        lim = [[x if abs(x) >= F(1, 2) else F(0) for x in r] for r in sS]   # drop the O(s^2) entries
        ok = ok and GA.rank_of_vectors(lim) == 3
        ok = ok and (len(sS) == len(lim) and all(len(r1) == len(r2) for r1, r2 in zip(sS, lim)) and all(abs(x - y) <= s * s for r1, r2 in zip(sS, lim) for x, y in zip(r1, r2)))
    ok = ok and maxima == [F(10), F(100), F(1000)]
    GA.check("at a corank-one wall the star diverges like 1/s and s*star tends to rank 3", ok)
    assert ok
