"""synthesis.two-frozen-points-conformally-flat: exact checks.

Flat scale on conformal Minkowski space, eta = diag(1, -1, -1, -1). A tractor is (sigma, mu, rho)
with tractor form Q = eta(mu, mu) + 2 sigma rho; the tractor connection in the flat scale is
nabla_a (sigma, mu_b, rho) = (d_a sigma - mu_a, d_a mu_b + eta_ab rho, d_a rho). Parallel
tractors are labelled by constants (s, m, r): sigma = s + m.x - (r/2) eta(x, x), mu_b = d_b sigma,
rho = r. Polynomials in x are dicts {exponent 4-tuple: Fraction}.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

ETA = [1, -1, -1, -1]
# two frozen points of equal norm Lambda/3 = 2 (Lambda = 6), and a third of another norm
I_A = (F(1), (F(0), F(0), F(0), F(0)), F(1))
I_B = (F(1), (F(1), F(0), F(0), F(0)), F(1, 2))
I_C = (F(2), (F(0), F(1), F(0), F(0)), F(3, 4))
I_D = (F(1), (F(0), F(0), F(0), F(0)), F(5, 2))          # same point, other norm
PTS = [(F(0), F(0), F(0), F(0)), (F(1, 3), F(1, 5), F(0), F(-1, 7)), (F(1, 2), F(0), F(1, 4), F(0))]


PAIRINGS = [F(3, 2), F(11, 4), F(7, 4)]


def _premises():
    premise("dark-energy.imported-frozen-point-geometry")
    premise("dark-energy.point-infinity-has-no-physical-fluctuation")


def padd(p, q, c=F(1)):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + c * v
    return {k: v for k, v in out.items() if v != 0}


def pmul(p, q):
    out = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            out[k] = out.get(k, F(0)) + v1 * v2
    return {k: v for k, v in out.items() if v != 0}


def pconst(c):
    return {(0, 0, 0, 0): F(c)} if c != 0 else {}


def pvar(a):
    e = [0, 0, 0, 0]
    e[a] = 1
    return {tuple(e): F(1)}


def pdiff(p, a):
    out = {}
    for k, v in p.items():
        if k[a] > 0:
            e = list(k)
            e[a] -= 1
            out[tuple(e)] = out.get(tuple(e), F(0)) + v * k[a]
    return {k: v for k, v in out.items() if v != 0}


def peval(p, x):
    tot = F(0)
    for k, v in p.items():
        term = v
        for a in range(4):
            term *= x[a] ** k[a]
        tot += term
    return tot


def qform():
    """eta(x, x) as a polynomial."""
    out = {}
    for a in range(4):
        out = padd(out, pmul(pvar(a), pvar(a)), F(ETA[a]))
    return out


def scale_tractor(I):
    """The parallel tractor field of constants (s, m, r) in the flat scale."""
    s, m, r = I
    sigma = pconst(s)
    for a in range(4):
        sigma = padd(sigma, pvar(a), F(ETA[a]) * m[a])      # m . x = eta(m, x)
    sigma = padd(sigma, qform(), -r / 2)
    mu = [pdiff(sigma, a) for a in range(4)]                  # lower-index mu_a = d_a sigma
    return sigma, mu, pconst(r)


def tractor_form(T1, T2):
    """Q(T1, T2) = eta^{ab} mu1_a mu2_b + sigma1 rho2 + rho1 sigma2, as a polynomial."""
    s1, m1, r1 = T1
    s2, m2, r2 = T2
    out = padd(pmul(s1, r2), pmul(r1, s2))
    for a in range(4):
        out = padd(out, pmul(m1[a], m2[a]), F(ETA[a]))
    return out


def is_parallel(T):
    sigma, mu, rho = T
    ok = all(padd(pdiff(sigma, a), mu[a], F(-1)) == {} for a in range(4))
    for a in range(4):
        for b in range(4):
            term = pdiff(mu[b], a)
            if a == b:
                term = padd(term, pmul(pconst(ETA[a]), rho))
            ok = ok and term == {}
    ok = ok and all(pdiff(rho, a) == {} for a in range(4))
    return ok


def gram6():
    """The tractor form on constant tractors (s, m^0..m^3, r) at x = 0."""
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][5] = G[5][0] = F(1)
    for a in range(4):
        G[1 + a][1 + a] = F(ETA[a])
    return G


def vec(I):
    s, m, r = I
    return [s] + [F(ETA[a]) * m[a] for a in range(4)] + [r]   # mu_a(0) = eta_aa m^a


def stabiliser_dim(vectors):
    """dim of {A in so(Q) : A v = 0 for v in vectors}, by exact linear algebra on 6x6 matrices."""
    G = gram6()
    rows = []
    n = 6
    idx = [(i, j) for i in range(n) for j in range(n)]
    # A^T G + G A = 0
    for p in range(n):
        for q in range(n):
            row = [F(0)] * (n * n)
            for k, (i, j) in enumerate(idx):
                # (A^T G)_{pq} = sum_i A_{ip} G_{iq}; (G A)_{pq} = sum_j G_{pj} A_{jq}
                if j == p:
                    row[k] += G[i][q]
                if j == q:
                    row[k] += G[p][i]
            rows.append(row)
    for v in vectors:
        for p in range(n):
            row = [F(0)] * (n * n)
            for k, (i, j) in enumerate(idx):
                if i == p:
                    row[k] += v[j]
            rows.append(row)
    return n * n - GA.rank_of_vectors(rows)


def check_parallel_frozen_points_and_norms():
    """Each (s, m, r) gives a parallel tractor; its norm is constant, 2 r s + eta(m, m)."""
    _premises()
    norms = []
    for I in (I_A, I_B, I_C, I_D):
        T = scale_tractor(I)
        assert is_parallel(T)
        N = tractor_form(T, T)
        s, m, r = I
        expect = 2 * r * s + sum(ETA[a] * m[a] * m[a] for a in range(4))
        assert N == pconst(expect)
        norms.append(expect)
    # A, B, C have the same norm Lambda / 3 = 2; D has another
    assert norms[0] == norms[1] == norms[2] == 2 and norms[3] != 2
    # the tractor form has signature (2, 4)
    assert GA.congruence_signature(gram6()) == (2, 4, 0)
    return True


def check_two_frozen_points_give_two_metrics():
    """Equal-norm frozen points A, B: the scales are not proportional, so g_A = sigma_A^{-2} eta
    and g_B = sigma_B^{-2} eta are distinct Einstein metrics of the same Lambda; the pairing
    Q(I_A, I_B) is constant and is not +-Q(I_A, I_A)."""
    _premises()
    TA, TB, TC = scale_tractor(I_A), scale_tractor(I_B), scale_tractor(I_C)
    for (T1, T2), want in zip(((TA, TB), (TA, TC), (TB, TC)), PAIRINGS):
        s1, s2 = T1[0], T2[0]
        keys = sorted(set(s1) | set(s2))
        assert GA.rank_of_vectors([[s1.get(k, F(0)) for k in keys],
                                   [s2.get(k, F(0)) for k in keys]]) == 2
        pair = tractor_form(T1, T2)
        assert len(pair) <= 1 and set(pair) <= {(0, 0, 0, 0)}     # constant
        c = pair.get((0, 0, 0, 0), F(0))
        assert c == want and c * c != tractor_form(T1, T1)[(0, 0, 0, 0)] ** 2
    # both metrics are defined and Lorentzian near x = 0, with conformal factors that differ
    for x in PTS:
        a, b = peval(TA[0], x), peval(TB[0], x)
        assert a != 0 and b != 0
    ratios = {peval(TA[0], x) / peval(TB[0], x) for x in PTS}
    assert len(ratios) > 1
    return True


def check_pair_has_one_gauge_invariant():
    """so(2,4) has dimension 15; the stabiliser of one non-null frozen point has dimension 10;
    of an equal-norm pair spanning a nondegenerate plane, 6. Each point ranges over a
    five-dimensional quadric, so pairs form a 10-dimensional space with 15 - 6 = 9 dimensional
    orbits: one gauge invariant, the pairing Q(I, I')."""
    _premises()
    assert stabiliser_dim([]) == 15
    assert stabiliser_dim([vec(I_A)]) == 10
    assert stabiliser_dim([vec(I_A), vec(I_B)]) == 6
    # the plane spanned by A and B is nondegenerate
    G = gram6()
    va, vb = vec(I_A), vec(I_B)
    q = lambda u, w: sum(u[i] * G[i][j] * w[j] for i in range(6) for j in range(6))
    assert q(va, va) * q(vb, vb) - q(va, vb) ** 2 != 0
    orbit = 15 - stabiliser_dim([va, vb])
    pairs = 2 * (6 - 1)
    assert pairs - orbit == 1
    return True
