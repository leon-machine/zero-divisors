"""odd-extensions.imported-tame-walls-exceptional-algebra-residue: exact checks on model walls.

Families over a line with defining function t (Sigma = {t = 0}), Gram matrices with polynomial
entries handled as GA.RF rational functions: G(t) = P(t)^T diag(h, lambda(t)) P(t) with P(t) a
polynomial matrix of determinant 1 (so the frame is not adapted), lambda(t) = delta t + c t^2, h a
constant nondegenerate form; plus the Schwarzschild wall Gram [[m^2 - r, -m, 0, 0], [-m, 1, 0, 0],
0, 0, diag(-1, -1)] in t = r (m = 2), which is not of that shape.
(T1)-(T3): det G vanishes at t = 0 and not at nearby sample points; rank n - 1 at t = 0 with a
one-dimensional radical spanned by k (computed as a kernel); delta(k (x) k) = d/dt G(k, k) at 0 is
nonzero, scales by s^2 under k -> s k and by phi'(0) under t = phi(s).
Signatures on the two sides (t = +-1/100) differ by one unit, (p,q) where G(k,k) > 0.
Exceptional algebra: in the adapted frame P^-1 the dying entry rescaled by |t|^-1 tends to +-delta
(t -> 0+-) with zero cross terms; the special fibre h (+) <+-delta> has the signature of the side
approached; equivalently sig(G(0) on a complement of k) plus the sign of the rate.
Residue: lim t G(t)^-1 = k (x) k / delta(k (x) k) (as matrices), independent of the scale of k, and
it rescales with the defining function as stated.
Conservation: G (+) K with K constant nondegenerate has det of opposite signs on the two sides, so it
degenerates in between; a completion whose complement switches signature (the hyperbolic model
diag(h) (+) [[0,1],[1,0]] containing span(f, u + t v/2)) is nondegenerate for every t.
Smoothness of Sigma and of the line bundle, and the global sheaf statements, are not finite
computations and are represented by these local models only.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RF, RF0, RF1 = GA.RF, GA.RF0, GA.RF1
T = RF.var()


def c(x):
    return RF.const(x)


def rmat(A):
    return [[c(x) if not isinstance(x, RF) else x for x in row] for row in A]


def rmul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    out = [[RF0] * p for _ in range(n)]
    for i in range(n):
        for j in range(p):
            acc = RF0
            for k in range(m):
                acc = acc + A[i][k] * B[k][j]
            out[i][j] = acc
    return out


def rtrans(A):
    return [list(r) for r in zip(*A)]


def ev(A, t):
    return [[x.eval(t) for x in row] for row in A]


def model(h, delta, cc, P):
    n = len(h) + 1
    D = [[RF0] * n for _ in range(n)]
    for i in range(n - 1):
        D[i][i] = c(h[i])
    D[n - 1][n - 1] = c(delta) * T + c(cc) * T * T
    return rmul(rmul(rtrans(P), D), P), D, P


P4 = [[RF1, T, RF0, c(2)], [RF0, RF1, c(-1), T], [RF0, RF0, RF1, T * T], [RF0, RF0, RF0, RF1]]
P3 = [[RF1, c(3), T], [RF0, RF1, c(F(1, 2)) * T], [RF0, RF0, RF1]]
FAMILIES = [model([1, -1, -1], F(-1), F(0), P4),
            model([1, 1, -1], F(2), F(3), P4),
            model([-1, -1], F(1, 3), F(-1), P3),
            model([1, -1], F(-5), F(1, 2), P3)]
M_SCH = 2
SCHW = rmat([[c(M_SCH * M_SCH) - T, c(-M_SCH), 0, 0], [c(-M_SCH), 1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
EPS = F(1, 100)
NEAR = (F(1, 100), F(-1, 100), F(1, 7), F(-2, 9))


def radical(G0):
    ker = GA.field_kernel([[F(x) for x in row] for row in G0])
    return ker


def gk(G, k):
    acc = RF0
    for i in range(len(k)):
        for j in range(len(k)):
            acc = acc + c(k[i]) * G[i][j] * c(k[j])
    return acc


def check_tameness_conditions():
    premise("sheaf.tameness")
    ok = True
    for G in [f[0] for f in FAMILIES] + [SCHW]:
        n = len(G)
        det = GA.rf_mat_det(G)
        ok = ok and det.eval(F(0)) == 0 and all(det.eval(t) != 0 for t in NEAR)
        G0 = ev(G, F(0))
        ok = ok and GA.mat_rank(G0) == n - 1
        ker = radical(G0)
        ok = ok and len(ker) == 1
        k = ker[0]
        delta = gk(G, k).deriv().eval(F(0))
        ok = ok and gk(G, k).eval(F(0)) == 0 and delta != 0
        # invariance: k -> 3k scales delta by 9; t = 2s scales it by 2
        ok = ok and gk(G, [3 * x for x in k]).deriv().eval(F(0)) == 9 * delta
        scaled = [[_subst_2s(x) for x in row] for row in G]
        ok = ok and gk(scaled, k).deriv().eval(F(0)) == 2 * delta
    # the Schwarzschild wall: k = rho + m dt, delta = -1 (g_k = -r)
    k = radical(ev(SCHW, F(0)))[0]
    k = [x / k[0] for x in k]
    ok = ok and k == [F(1), F(M_SCH), F(0), F(0)] and gk(SCHW, k).eqrf(-T)
    GA.check("tame walls: (T1) det vanishes only at the wall, (T2) corank one, (T3) delta(k (x) k) != 0", ok)
    return ok


def _subst_2s(x):
    """x(t) with t = 2s, as a rational function of s."""
    def sub(p):
        return [coef * (2 ** i) for i, coef in enumerate(p)]
    return RF(sub(x.num), sub(x.den))


def sig(M):
    return GA.congruence_signature([[F(x) for x in row] for row in M])


def check_signatures_and_exceptional_fibre():
    premise("sheaf.tameness")
    ok = True
    for G, D, P in FAMILIES:
        n = len(G)
        k = radical(ev(G, F(0)))[0]
        delta = gk(G, k).deriv().eval(F(0))
        plus, minus = sig(ev(G, EPS)), sig(ev(G, -EPS))
        ok = ok and plus[2] == minus[2] == 0
        ok = ok and abs(plus[0] - minus[0]) == 1 and plus[0] + plus[1] == minus[0] + minus[1] == n
        pos_side = plus if gk(G, k).eval(EPS) > 0 else minus
        neg_side = minus if pos_side == plus else plus
        ok = ok and pos_side[0] == neg_side[0] + 1
        # adapted frame: D(t); the rescaled dying entry lambda(t)/t -> delta, cross terms zero
        lam_over_t = D[n - 1][n - 1] / T
        ok = ok and lam_over_t.eval(F(0)) == delta
        ok = ok and all(D[i][j].is_zero() for i in range(n) for j in range(n) if i != j)
        h = [D[i][i].eval(F(0)) for i in range(n - 1)]
        for side, s in ((plus, 1), (minus, -1)):
            fibre = [[(h[i] if i < n - 1 else s * delta) if i == j else F(0) for j in range(n)] for i in range(n)]
            ok = ok and sig(fibre) == side
        # the surviving form: G(0) on a complement of k, plus the sign of the rate
        G0 = ev(G, F(0))
        j = next(i for i in range(n) if k[i] != 0)
        comp = [i for i in range(n) if i != j]          # coordinate complement of span(k)
        sub = [[G0[a][b] for b in comp] for a in comp]
        ok = ok and sig(sub) == (sum(1 for x in h if x > 0), sum(1 for x in h if x < 0), 0)
    GA.check("tame walls: signatures differ by one unit; the exceptional fibre has the signature of its side", ok)
    return ok


K_SCALES = (F(1), F(3), F(-1, 2))


def check_residue_is_inverse_transversality_datum():
    premise("sheaf.tameness")
    ok = True
    for G in [f[0] for f in FAMILIES] + [SCHW]:
        n = len(G)
        inv = GA.rf_mat_inverse(G)
        O = [[(T * x).eval(F(0)) for x in row] for row in inv]
        for s in K_SCALES:
            k = [s * x for x in radical(ev(G, F(0)))[0]]
            delta = gk(G, k).deriv().eval(F(0))
            ok = ok and O == [[k[i] * k[j] / delta for j in range(n)] for i in range(n)]
        ok = ok and any(x != 0 for row in O for x in row)
        # with the defining function tau = 2t: lim tau G^-1 = 2 O, and delta_tau = delta / 2
        O2 = [[(c(2) * T * x).eval(F(0)) for x in row] for row in inv]
        ok = ok and O2 == [[2 * x for x in row] for row in O]
    # by hand at the Schwarzschild wall (m = 2): k = (1, 2, 0, 0), delta = -1, so O = -k k^T
    inv = GA.rf_mat_inverse(SCHW)
    O = [[(T * x).eval(F(0)) for x in row] for row in inv]
    ok = ok and O == [[F(-1), F(-2), 0, 0], [F(-2), F(-4), 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    GA.check("tame walls: lim t G^-1 = k (x) k / delta(k (x) k): the residue is the inverse datum", ok)
    return ok


def check_conservation_needs_constant_complement():
    premise("sheaf.tameness")
    ok = True
    for G, D, P in FAMILIES:
        for K in ([F(1)], [F(-1), F(1)], [F(2), F(5)]):
            dets = []
            for t in (EPS, -EPS):
                Gt = ev(G, t)
                n = len(Gt)
                full = [[Gt[i][j] if i < n and j < n else (K[i - n] if i == j else F(0))
                         for j in range(n + len(K))] for i in range(n + len(K))]
                dets.append(GA.rf_mat_det(rmat(full)).eval(F(0)))
            ok = ok and dets[0] * dets[1] < 0
    # the hyperbolic completion: diag(h) (+) [[0,1],[1,0]] contains span(f, u + t v/2) with induced
    # form diag(h, t) and complement u - t v/2 of norm -t (switching sign): nondegenerate for all t
    for h in ([1, -1, -1], [-1, -1]):
        n = len(h)
        whole = [[F(h[i]) if i == j and i < n else F(0) for j in range(n + 2)] for i in range(n + 2)]
        whole[n][n + 1] = whole[n + 1][n] = F(1)
        for t in (F(-1), F(0), F(1, 3)):
            x = [F(0)] * n + [F(1), t / 2]
            y = [F(0)] * n + [F(1), -t / 2]
            q = lambda a, b: sum(a[i] * whole[i][j] * b[j] for i in range(n + 2) for j in range(n + 2))
            ok = ok and q(x, x) == t and q(y, y) == -t and q(x, y) == 0
        ok = ok and GA.mat_rank(whole) == n + 2
    GA.check("tame walls: a standard completion with constant K degenerates; a switching one need not", ok)
    return ok
