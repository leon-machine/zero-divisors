"""synthesis.nondiagonal-kasner-residue-weighted-shear: exact checks (Fractions; GA imported).

Metric g = dtau^2 - sum_l tau^{2 p_l} (theta^l)^2, theta = G(tau) theta0, at the rational Kasner point
p = (-2/7, 3/7, 6/7); tau = t^7 so tau^{p_l} = t^{-2}, t^3, t^6. Derivatives are exact (dual numbers in t);
log tau is an independent symbol ell with d ell/dt = 7/t, tested at two rational stand-ins (the identities are
polynomial in ell).
(a) For G = exp(c log(tau) N) with N triangular in either direction (so Omega = c N), at three values of t and
    two stand-ins: with E = Delta G theta0 the orthonormal coframe matrix (e^l = E^l_i dx^i), the coefficient of
    dtau ^ e^m in de^l, times tau, is (tau d_tau E) E^{-1} = B = P + Delta Omega Delta^{-1} entrywise; the
    mixed second fundamental form tau K = (1/2) h^{-1} tau d_tau h, computed from the coordinate metric
    h = E^T E and carried to the orthonormal frame (E tau K E^{-1}), equals sym(B) entrywise, so tau K is
    similar to sym(B) (their characteristic polynomials are also compared). By Cartan's first structure
    equation (argued, not computed) this is the boost block omega^{l0} = tau^{-1} sym(B)_lm e^m with the
    e^0-leg of the rotation block tau^{-1} times the antisymmetric part of B. With G = 1 it is P (the diagonal
    lemma's boost block).
(b) tr sym(B)^2 = sum p^2 + (c^2/2) sum_{l != m} N_lm^2 tau^{2(p_l - p_m)}: pinned values, decreasing to 1 for a
    shear in the order of the weights, increasing without bound against it.
(c) G = 1 + tau^{3/7} E_12 tends to the identity and rotates at rate o(1/tau), yet
    tr (tau K)^2 = 1 + (9/98) tau^{-4/7}.
(d) The residue relations only (the field-equation step that yields them is not computed): for R = P,
    tr R = tr R^2 = (tr R)^2 = 1, and an off-circle control violates both.
"""
from fractions import Fraction as F
import GA
from GA import field_rank
from tp_premise import premise

EXP = (-2, 3, 6)          # tau^{p_l} = t^{EXP_l}, tau = t^7


class D:
    """Dual number over Q: exact first derivative in t."""
    def __init__(s, v, d=0):
        s.v, s.d = F(v), F(d)

    def _c(s, o):
        return o if isinstance(o, D) else D(o, 0)

    def __add__(s, o):
        o = s._c(o)
        return D(s.v + o.v, s.d + o.d)
    __radd__ = __add__

    def __sub__(s, o):
        o = s._c(o)
        return D(s.v - o.v, s.d - o.d)

    def __mul__(s, o):
        o = s._c(o)
        return D(s.v * o.v, s.v * o.d + s.d * o.v)
    __rmul__ = __mul__

    def __truediv__(s, o):
        o = s._c(o)
        return D(s.v / o.v, (s.d * o.v - s.v * o.d) / (o.v * o.v))


def tpow(t, k):
    return D(t ** k, k * t ** (k - 1))


def mm(A, B):
    n = len(A)
    return [[sum((A[i][k] * B[k][j] for k in range(n)), D(0)) for j in range(n)] for i in range(n)]


def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A))]


def inv(A):
    n = len(A)
    M = [row[:] + [D(1 if i == j else 0) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c].v != 0)
        M[c], M[p] = M[p], M[c]
        piv = M[c][c]
        M[c] = [x / piv for x in M[c]]
        for r in range(n):
            if r != c:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [row[n:] for row in M]


def charpoly(M):
    t1 = M[0][0] + M[1][1] + M[2][2]
    t2 = sum(M[i][i] * M[j][j] - M[i][j] * M[j][i] for i in range(3) for j in range(i + 1, 3))
    t3 = (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
          + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))
    return (t1, t2, t3)


def weights():
    return [F(e, 7) for e in EXP]


def tauK_coord(t, G, theta0):
    """tau K^i_j = (1/2) h^{-1} tau d_tau h, h = theta0^T G^T D G theta0; tau d/dtau = (t/7) d/dt."""
    Dm = [[tpow(t, 2 * EXP[i]) if i == j else D(0) for j in range(3)] for i in range(3)]
    T0 = [[D(x) for x in row] for row in theta0]
    h = mm(mm(transpose(T0), mm(mm(transpose(G), Dm), G)), T0)
    hv = [[D(x.v) for x in row] for row in inv(h)]
    hd = [[D(x.d * t / 7) for x in row] for row in h]
    return [[x.v / 2 for x in row] for row in mm(hv, hd)]


def symB(t, Omega):
    P = weights()
    B = [[(P[i] if i == j else F(0)) + Omega[i][j] * t ** (EXP[i] - EXP[j]) for j in range(3)] for i in range(3)]
    return [[(B[i][j] + B[j][i]) / 2 for j in range(3)] for i in range(3)]


def fullB(t, Omega):
    P = weights()
    return [[(P[i] if i == j else F(0)) + Omega[i][j] * t ** (EXP[i] - EXP[j]) for j in range(3)] for i in range(3)]


def frame_data(t, G, theta0):
    """E = Delta G theta0 (dual numbers in t): returns ((tau d_tau E) E^{-1}, E, E^{-1}) as Fractions."""
    Dm = [[tpow(t, EXP[i]) if i == j else D(0) for j in range(3)] for i in range(3)]
    T0 = [[D(x) for x in row] for row in theta0]
    E = mm(mm(Dm, G), T0)
    Ev = [[D(x.v) for x in row] for row in E]
    Einv = inv(Ev)
    Ed = [[D(x.d * t / 7) for x in row] for row in E]
    rate = [[x.v for x in row] for row in mm(Ed, Einv)]
    return rate, [[x.v for x in row] for row in E], [[x.v for x in row] for row in Einv]


def fmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), F(0)) for j in range(3)] for i in range(3)]


def exp_shear(t, c, N, ell0):
    ell = D(ell0, F(7) / t)
    Nd = [[D(x) for x in row] for row in N]
    N2 = mm(Nd, Nd)
    return [[D(1 if i == j else 0) + c * ell * Nd[i][j] + (c * c / 2) * ell * ell * N2[i][j]
             for j in range(3)] for i in range(3)]


def trsq(S):
    return sum(S[i][j] * S[j][i] for i in range(3) for j in range(3))


def check_boost_block_identity():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    premise("synthesis.diagonal-kasner-momentum-constraint")
    theta0 = [[1, 2, 0], [0, 1, -1], [1, 0, 3]]
    assert field_rank([[F(x) for x in r] for r in theta0]) == 3
    c = F(3, 5)
    cases = 0
    for N in ([[0, 0, 0], [1, 0, 0], [2, -1, 0]], [[0, 1, 2], [0, 0, -1], [0, 0, 0]]):
        for ell0 in (F(-5, 2), F(7, 3)):
            for t in (F(1, 2), F(1, 3), F(2, 7)):
                G = exp_shear(t, c, N, ell0)
                Om = [[c * N[i][j] for j in range(3)] for i in range(3)]
                Kc = tauK_coord(t, G, theta0)
                assert charpoly(Kc) == charpoly(symB(t, Om))
                rate, E, Einv = frame_data(t, G, theta0)
                assert rate == fullB(t, Om)                      # (tau d_tau E) E^{-1} = B entrywise
                assert fmul(fmul(E, Kc), Einv) == symB(t, Om)     # tau K in the orthonormal frame = sym(B)
                cases += 1
    assert cases == 12
    # pinned value at one point: the shear in the order of the weights, t = 1/2, log stand-in -5/2
    t = F(1, 2)
    Kc = tauK_coord(t, exp_shear(t, c, [[0, 0, 0], [1, 0, 0], [2, -1, 0]], F(-5, 2)), theta0)
    assert charpoly(Kc) == (1, F(-2457, 1638400), F(-588011931, 5619712000))
    # G = 1: the diagonal boost block P, whatever theta0
    t = F(1, 3)
    I3 = [[D(1 if i == j else 0) for j in range(3)] for i in range(3)]
    assert charpoly(tauK_coord(t, I3, theta0)) == (1, 0, F(-36, 343))
    return True


def check_weighted_criterion():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    c = F(3, 5)
    allowed = [[0, 0, 0], [1, 0, 0], [2, -1, 0]]      # N_lm != 0 only for p_l > p_m
    against = [[0, 1, 2], [0, 0, -1], [0, 0, 0]]
    ts = (F(1, 2), F(1, 4), F(1, 8), F(1, 16))
    va, vb = [], []
    for t in ts:
        for N, out in ((allowed, va), (against, vb)):
            S = symB(t, [[c * N[i][j] for j in range(3)] for i in range(3)])
            pred = 1 + (c * c / 2) * sum(N[i][j] ** 2 * t ** (2 * (EXP[i] - EXP[j]))
                                         for i in range(3) for j in range(3) if i != j)
            assert trsq(S) == pred
            out.append(trsq(S))
    assert va[0] == F(821657, 819200) and vb[0] == F(1184569, 25)
    assert all(a > b > 1 for a, b in zip(va, va[1:]))
    assert all(b > a for a, b in zip(vb, vb[1:]))
    # in the order of the weights the off-diagonal entries of sym(B) vanish in the limit: at t = 1/16
    S = symB(F(1, 16), [[c * allowed[i][j] for j in range(3)] for i in range(3)])
    assert max(abs(S[i][j]) for i in range(3) for j in range(3) if i != j) < F(1, 10 ** 3)
    return True


def check_counterexample_rate():
    premise("dark-energy.variable-exponents-residue-pointwise-corrections-are")
    theta0 = [[1, 2, 0], [0, 1, -1], [1, 0, 3]]
    vals = []
    for t in (F(1, 2), F(1, 4), F(1, 8), F(1, 16)):
        f = tpow(t, 3)                                  # tau^{3/7}
        G = [[D(1), f, D(0)], [D(0), D(1), D(0)], [D(0), D(0), D(1)]]
        Kc = tauK_coord(t, G, theta0)
        Om = [[F(0), F(3, 7) * t ** 3, F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(0)]]
        assert charpoly(Kc) == charpoly(symB(t, Om))
        assert trsq(Kc) == 1 + F(9, 98) * t ** -4
        assert f.v == t ** 3                            # G -> 1 as t -> 0
        vals.append(trsq(Kc))
    assert vals == [F(121, 49), F(1201, 49), F(18481, 49), F(294961, 49)]
    return True


def check_residue_relations_on_kasner_circle():
    premise("dark-energy.frozen-point-datum-kasner-wall")
    premise("dark-energy.cosmological-constant-does-not-change-residue")
    P = weights()
    trR = sum(P)
    trR2 = sum(x * x for x in P)
    assert trR == 1 and trR2 == 1 and trR * trR == trR2
    # off the circle the two leading equations disagree (control)
    Q = [F(-1, 7), F(3, 7), F(6, 7)]
    assert sum(Q) - sum(x * x for x in Q) == F(10, 49)
    assert sum(Q) ** 2 - sum(x * x for x in Q) == F(18, 49)
    assert trR - trR2 == 0 and trR ** 2 - trR2 == 0 and P[0] * P[1] * P[2] == F(-36, 343)
    return True
