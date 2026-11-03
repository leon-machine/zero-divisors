"""synthesis.vacuum-field-stress-tensor-is-einstein-tensor-or-trace: exact checks.

Signature (1,3), eta = diag(1,-1,-1,-1); symmetric tensors P_ab are coordinatised by the ten pairs
a <= b. Tractors (sigma, mu_b, rho) in the splitting of g, form <x,y> = sigma rho' + rho sigma' +
eta^{bc} mu_b mu'_c, and the non-Levi part of the connection of interior.imported-tractor-connection
along v, omega(v)(sigma, mu, rho) = (-mu(v), v_flat rho - P(v,.) sigma, P(v, mu)), as in the checks of
synthesis.einstein-condition-is-infinity-vacuum-incidence. kappa stands for 4 pi G (a rational
stand-in: every step is linear in kappa).

  check_first_order_data:  the classes of I_g and X along v are -P(v,w) and g(v,w) for a generic P;
                           a tensor read linearly off them is a linear function of P plus a multiple
                           of g (the X classes do not depend on P).
  check_schur:             the linear maps of Sym^2 commuting with a rational boost, two rational
                           rotations and two reflections form a space of dimension exactly 2, spanned
                           by the identity and P -> tr(P) eta.
  check_dichotomy:         for Theta = a P + b J g + c g the own-ray matter clause
                           -P(l,l) = kappa Theta(l,l) on eleven real null l: with 1 + kappa a != 0 its
                           solution space in P is span(eta) (rank 9), where Theta(l,l) = 0 and the
                           trace-free part of Theta vanishes; with a = -1/kappa every row vanishes.
  check_conservation:      on a metric with vanishing first derivatives at the origin and generic
                           second and third derivatives, the contracted Bianchi identity
                           div P = dJ holds exactly at the origin; hence div Theta = (a + b) dJ, and
                           the conserved tautological tensor (a = -1/kappa, b = 1/kappa) is
                           -(Ric - R g/2)/(2 kappa), for which Ric + 2 kappa Theta = h g holds
                           identically with h = R/2 + 2 kappa c.
"""
from fractions import Fraction as F
import GA
from GA import QI
from tp_premise import premise

ETA = [1, -1, -1, -1]
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]
NULLS = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1],
         [1, F(3, 5), F(4, 5), 0], [1, 0, F(3, 5), F(4, 5)], [1, F(4, 5), 0, F(3, 5)],
         [1, F(-3, 5), F(4, 5), 0], [1, F(2, 3), F(2, 3), F(1, 3)]]
GENERIC_P = [[F(2), F(1, 3), F(-1), F(0)], [F(1, 3), F(-5), F(1, 2), F(3)],
             [F(-1), F(1, 2), F(7), F(-2, 3)], [F(0), F(3), F(-2, 3), F(4)]]


def gram():
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][5] = G[5][0] = F(1)
    for a in range(4):
        G[1 + a][1 + a] = F(ETA[a])
    return G


GR = gram()


def ip(x, y):
    return sum(GR[i][j] * x[i] * y[j] for i in range(6) for j in range(6))


def omega(v, P):
    M = [[F(0)] * 6 for _ in range(6)]
    for b in range(4):
        M[0][1 + b] -= F(v[b])
        M[1 + b][5] += ETA[b] * F(v[b])
        M[1 + b][0] -= sum(F(v[a]) * P[a][b] for a in range(4))
        M[5][1 + b] += sum(F(v[a]) * P[a][b] for a in range(4)) * ETA[b]
    return M


def act(M, x):
    return [sum(M[i][j] * x[j] for j in range(6)) for i in range(6)]


def tangent(u):
    return [F(0)] + [ETA[b] * F(u[b]) for b in range(4)] + [F(0)]


def pform(P, u, w):
    return sum(P[a][b] * F(u[a]) * F(w[b]) for a in range(4) for b in range(4))


def gform(u, w):
    return sum(ETA[a] * F(u[a]) * F(w[a]) for a in range(4))


def to_vec(P):
    return [P[a][b] for (a, b) in PAIRS]


def to_mat(x):
    P = [[F(0)] * 4 for _ in range(4)]
    for k, (a, b) in enumerate(PAIRS):
        P[a][b] = P[b][a] = x[k]
    return P


def trace(P):
    return sum(ETA[a] * P[a][a] for a in range(4))


def eta_mat():
    return [[F(ETA[a]) if a == b else F(0) for b in range(4)] for a in range(4)]


def check_first_order_data():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("interior.imported-tractor-connection")
    I_g = [F(1), F(0), F(0), F(0), F(0), F(0)]
    X = [F(0), F(0), F(0), F(0), F(0), F(1)]
    vs = [[F(1, 2), F(3), F(-1), F(2)], [F(0), F(1), F(1), F(0)], [F(2), F(-1, 3), F(0), F(5, 7)]]
    ws = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    for v in vs:
        M = omega(v, GENERIC_P)
        M0 = omega(v, [[F(0)] * 4 for _ in range(4)])
        for w in ws:
            assert ip(act(M, I_g), tangent(w)) == -pform(GENERIC_P, v, w)
            assert ip(act(M, X), tangent(w)) == gform(v, w)
            assert ip(act(M0, X), tangent(w)) == ip(act(M, X), tangent(w))
    assert ip(act(omega(vs[0], GENERIC_P), I_g), tangent(ws[0])) == F(-3)
    return True


def rep_matrix(L):
    """matrix of P -> L^T P L on Sym^2 in the PAIRS coordinates."""
    cols = []
    for k in range(10):
        e = [F(0)] * 10
        e[k] = F(1)
        P = to_mat(e)
        Q = [[sum(L[c][a] * P[c][d] * L[d][b] for c in range(4) for d in range(4)) for b in range(4)]
             for a in range(4)]
        cols.append(to_vec(Q))
    return [[cols[j][i] for j in range(10)] for i in range(10)]


def lorentz_generators():
    def eye():
        return [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
    boost = eye()
    boost[0][0] = boost[1][1] = F(5, 4)
    boost[0][1] = boost[1][0] = F(3, 4)
    rot12 = eye()
    rot12[1][1] = rot12[2][2] = F(3, 5)
    rot12[1][2], rot12[2][1] = F(-4, 5), F(4, 5)
    rot23 = eye()
    rot23[2][2] = rot23[3][3] = F(5, 13)
    rot23[2][3], rot23[3][2] = F(-12, 13), F(12, 13)
    tref = eye()
    tref[0][0] = F(-1)
    pref = eye()
    pref[1][1] = F(-1)
    gens = [boost, rot12, rot23, tref, pref]
    for L in gens:     # each preserves eta
        for a in range(4):
            for b in range(4):
                assert sum(L[c][a] * ETA[c] * L[c][b] for c in range(4)) == (ETA[a] if a == b else 0)
    return gens


def check_schur():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    gens = lorentz_generators()
    rows = []
    for L in gens:
        R = rep_matrix(L)
        # unknown K (10x10, index K[i][j] -> 10 i + j): (K R - R K)[i][j] = 0
        for i in range(10):
            for j in range(10):
                row = [F(0)] * 100
                for k in range(10):
                    row[10 * i + k] += R[k][j]
                    row[10 * k + j] -= R[i][k]
                rows.append(row)
    ker = GA.field_kernel(rows)
    assert len(ker) == 2
    ident = [F(1) if i == j else F(0) for i in range(10) for j in range(10)]
    eta_v = to_vec(eta_mat())
    tr_row = [ETA[a] if a == b else 0 for (a, b) in PAIRS]
    trmap = [eta_v[i] * tr_row[j] for i in range(10) for j in range(10)]
    assert GA.field_rank(ker + [ident]) == 2 and GA.field_rank(ker + [trmap]) == 2
    assert GA.field_rank([ident, trmap]) == 2
    return True


def check_dichotomy():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("interior.metric-parallelism-trace-schouten-condition")
    kappa = F(3)
    for l in NULLS:
        assert gform(l, l) == 0
    eta_v = to_vec(eta_mat())
    for a, b, c in ((F(1, 2), F(-7), F(2)), (F(0), F(1), F(-1, 5)), (F(-2), F(1, 3), F(0))):
        assert 1 + kappa * a != 0
        # row of (1 + kappa a) P(l,l) in the unknown P (Theta(l,l) = a P(l,l): g(l,l) = 0)
        rows = [[(1 + kappa * a) * (F(l[p]) * F(l[q]) * (1 if p == q else 2)) for (p, q) in PAIRS]
                for l in NULLS]
        assert GA.field_rank(rows) == 9
        ker = GA.field_kernel(rows)
        assert len(ker) == 1
        lam = ker[0][0] / eta_v[0]
        assert all(ker[0][i] == lam * eta_v[i] for i in range(10))
        P = to_mat(ker[0])
        J = trace(P)
        Theta = [[a * P[p][q] + (b * J + c) * ETA[p] * (1 if p == q else 0) for q in range(4)]
                 for p in range(4)]
        for l in NULLS:
            assert pform(Theta, l, l) == 0
        tr = trace(Theta)
        tf = [[Theta[p][q] - tr * ETA[p] * (1 if p == q else 0) / 4 for q in range(4)] for p in range(4)]
        assert all(x == 0 for r in tf for x in r)
    a = -1 / kappa
    rows = [[(1 + kappa * a) * F(l[p]) * F(l[q]) for (p, q) in PAIRS] for l in NULLS]
    assert GA.field_rank(rows) == 0
    for l in NULLS:      # the clause then holds for the generic P
        assert -pform(GENERIC_P, l, l) == kappa * a * pform(GENERIC_P, l, l)
    return True


# metric g = eta + h, h_ab = 1/2 A_abcd x^c x^d + 1/6 B_abcde x^c x^d x^e (symmetric in the derivative
# slots); first derivatives vanish at 0, so Gamma(0) = 0 and the Gamma-Gamma part of the Riemann
# tensor has vanishing value and first derivative there.
def _sym_coeff(seed, idx):
    a, b = sorted(idx[:2])
    der = tuple(sorted(idx[2:]))
    h = (seed * (7 * a + 3 * b + 1) + sum((k + 2) * (d + 1) * (d + 3) for k, d in enumerate(der))) % 11
    return F(h - 5, 1 + (a + b + len(der)) % 3)


def d2g(a, b, c, d):
    return _sym_coeff(3, (a, b, c, d))


def d3g(a, b, c, d, e):
    return _sym_coeff(5, (a, b, c, d, e))


def riem(a, b, c, d, e=None):
    """R_abcd at 0 (e None) or its e-derivative at 0, sphere-positive convention."""
    if e is None:
        f = d2g
        return (f(a, d, b, c) + f(b, c, a, d) - f(a, c, b, d) - f(b, d, a, c)) / 2
    f = d3g
    return (f(a, d, b, c, e) + f(b, c, a, d, e) - f(a, c, b, d, e) - f(b, d, a, c, e)) / 2


def check_conservation():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("interior.imported-tractor-connection")
    eta = eta_mat()

    def ric(e=None):     # store convention: minus the sphere-positive Ricci tensor
        return [[-sum(ETA[a] * riem(a, b, a, d, e) for a in range(4)) for d in range(4)] for b in range(4)]

    def sch(e=None):
        Rc = ric(e)
        R = trace(Rc)
        return [[(Rc[a][b] - R * eta[a][b] / 6) / 2 for b in range(4)] for a in range(4)], R

    dP = [sch(e)[0] for e in range(4)]
    dJ = [trace(dP[e]) for e in range(4)]
    assert any(x != 0 for x in dJ)
    for b in range(4):
        div = sum(ETA[a] * dP[a][a][b] for a in range(4))
        assert div == dJ[b]
    # div Theta = (a + b) dJ for Theta = a P + b J g + c g
    for (ca, cb) in ((F(2), F(-2)), (F(1, 3), F(5))):
        for b in range(4):
            divT = sum(ETA[a] * (ca * dP[a][a][b] + cb * dJ[a] * eta[a][b]) for a in range(4))
            assert divT == (ca + cb) * dJ[b]
    # the conserved tautological tensor is the store-convention Einstein tensor
    kappa, c = F(3), F(2, 7)
    P0, R0 = sch()
    Rc0 = ric()
    J0 = trace(P0)
    assert J0 == R0 / 6
    Theta = [[-(P0[a][b] - J0 * eta[a][b]) / kappa + c * eta[a][b] for b in range(4)] for a in range(4)]
    for a in range(4):
        for b in range(4):
            assert Theta[a][b] == -(Rc0[a][b] - R0 * eta[a][b] / 2) / (2 * kappa) + c * eta[a][b]
            assert Rc0[a][b] + 2 * kappa * Theta[a][b] == (R0 / 2 + 2 * kappa * c) * eta[a][b]
    for l in NULLS:
        assert -pform(P0, l, l) == kappa * pform(Theta, l, l)
    return True


if __name__ == "__main__":
    for f in (check_first_order_data, check_schur, check_dichotomy, check_conservation):
        print(f.__name__, f())
