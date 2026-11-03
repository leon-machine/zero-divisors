"""synthesis.infinity-vacuum-incidence-is-a-property-of-the-scale: exact checks.

Tractors in the splitting of a scale g of signature (1,3), eta = diag(1,-1,-1,-1), written
(sigma, mu_b, rho) with mu lower-index; tractor form <x,y> = sigma rho' + rho sigma' + eta^{bc} mu_b mu'_c.
At a point, in a frame, the non-Levi part of the tractor connection (interior.imported-tractor-connection)
acts along v as omega(v)(sigma, mu, rho) = (-mu(v), v_flat rho - P(v,.) sigma, P(v, mu)); along an
affinely parametrised null geodesic with tangent l the Levi-Civita part annihilates X = (0,0,1),
I_g = (1,0,0) and L = (0, l_flat, 0), so nabla_l acts on them by omega(l) alone. Complex numbers are
GA.QI; Fock states are GA exterior-model states.
"""
from fractions import Fraction as F
import GA
from GA import QI
from tp_premise import premise

ETA = [1, -1, -1, -1]
Z = QI(0)


def _gram():
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][5] = G[5][0] = F(1)
    for a in range(4):
        G[1 + a][1 + a] = F(ETA[a])
    return G


G = _gram()
I_G = [QI(1), Z, Z, Z, Z, Z]
X_T = [Z, Z, Z, Z, Z, QI(1)]
NULLS = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1],
         [1, F(3, 5), F(4, 5), 0], [1, 0, F(3, 5), F(4, 5)], [1, F(4, 5), 0, F(3, 5)],
         [1, F(-3, 5), F(4, 5), 0], [1, F(2, 3), F(2, 3), F(1, 3)]]
GENERIC_P = [[F(2), F(1, 3), F(-1), F(0)], [F(1, 3), F(-5), F(1, 2), F(3)],
             [F(-1), F(1, 2), F(7), F(-2, 3)], [F(0), F(3), F(-2, 3), F(4)]]


def ip(x, y):
    return sum((QI(G[i][j]) * QI(x[i]) * QI(y[j]) for i in range(6) for j in range(6)), Z)


def omega(v, P):
    M = [[QI(0)] * 6 for _ in range(6)]
    for b in range(4):
        M[0][1 + b] = M[0][1 + b] - QI(v[b])
        M[1 + b][5] = M[1 + b][5] + QI(ETA[b]) * QI(v[b])
        M[1 + b][0] = M[1 + b][0] - sum((QI(v[a]) * QI(P[a][b]) for a in range(4)), Z)
        M[5][1 + b] = M[5][1 + b] + sum((QI(v[a]) * QI(P[a][b]) for a in range(4)), Z) * QI(ETA[b])
    return M


def act(M, x):
    return [sum((M[i][j] * QI(x[j]) for j in range(6)), Z) for i in range(6)]


def tangent(u):
    return [Z] + [QI(ETA[b]) * QI(u[b]) for b in range(4)] + [Z]


def gform(u, w):
    return sum((QI(ETA[a]) * QI(u[a]) * QI(w[a]) for a in range(4)), Z)


def pform(P, u, w):
    return sum((QI(P[a][b]) * QI(u[a]) * QI(w[b]) for a in range(4) for b in range(4)), Z)


def lin(c1, x, c2, y):
    return [QI(c1) * a + QI(c2) * b for a, b in zip(x, y)]


def in_span(vecs, x):
    return GA.field_rank(vecs + [x]) == GA.field_rank(vecs)


def trace(P):
    return sum(F(ETA[a]) * P[a][a] for a in range(4))


def companion(l):
    axis = [k for k in range(1, 4) if l[k] != 0][0]
    rest = [k for k in range(1, 4) if k != axis]
    m = [Z, Z, Z, Z]
    m[rest[0]] = QI(1)
    m[rest[1]] = QI(0, 1)
    return m


def fock_vacuum(W):
    st = {frozenset(): QI(1)}
    for w in reversed(W):
        st = GA.ext_c(list(w), G, st)
    return st


def killed(x, st):
    return all(not c for c in GA.ext_c(list(x), G, st).values())


def check_ray_closure():
    premise("interior.imported-tractor-connection")
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    einstein = [[F(ETA[a]) * F(1, 2) if a == b else F(0) for b in range(4)] for a in range(4)]
    for l in NULLS:
        L = tangent(l)
        assert gform(l, l) == Z
        for P in (GENERIC_P, einstein):
            M = omega(l, P)
            # point line: nabla_l X = L, nabla_l L = P(l,l) X; span(X, L) closed in every metric
            assert act(M, X_T) == L
            assert act(M, L) == [QI(x) * pform(P, l, l) for x in X_T]
            assert in_span([X_T, L], act(M, X_T)) and in_span([X_T, L], act(M, L))
        # infinity line: closed for the Einstein Schouten tensor, not for the generic one
        Me = omega(l, einstein)
        assert act(Me, I_G) == [QI(F(-1, 2)) * x for x in L] and act(Me, L) == [Z] * 6
        Mg = omega(l, GENERIC_P)
        assert not (in_span([I_G, L], act(Mg, I_G)) and in_span([I_G, L], act(Mg, L)))
    # Fock form, one real null direction: the vacuum of span(X, l, m) and of span(I_g, l, m)
    l = [1, 1, 0, 0]
    m = companion(l)
    L, Mt = tangent(l), tangent(m)
    up = fock_vacuum([X_T, L, Mt])
    ui = fock_vacuum([I_G, L, Mt])
    assert any(up.values()) and any(ui.values())
    for P in (GENERIC_P, einstein):
        M = omega(l, P)
        assert killed(act(M, X_T), up) and killed(act(M, L), up)       # point vacuum stays one
    Me, Mg = omega(l, einstein), omega(l, GENERIC_P)
    assert killed(act(Me, I_G), ui) and killed(act(Me, L), ui)          # Einstein: infinity stays
    assert not killed(act(Mg, I_G), ui) or not killed(act(Mg, L), ui)   # generic: it leaves
    return True


def ricci_at_origin(H):
    """Ricci tensor (R^a_{bad}, R^a_{bcd} = d_c Gamma^a_{db} - d_d Gamma^a_{cb} + ...) at the origin of
    g = f eta, f = 1 + (1/2) x^T H x, where g = eta and d g = 0, so Gamma = 0 and only d Gamma enters:
    d_d Gamma^a_{bc} = (1/2) eta^{aa} (H_db eta_ac + H_dc eta_ab - H_da eta_bc)."""
    def dG(d, a, b, c):
        e = lambda i, j: F(ETA[i]) if i == j else F(0)
        return F(1, 2) * F(ETA[a]) * (H[d][b] * e(a, c) + H[d][c] * e(a, b) - H[d][a] * e(b, c))
    Ric = [[F(0)] * 4 for _ in range(4)]
    for b in range(4):
        for d in range(4):
            Ric[b][d] = sum(dG(a, a, d, b) - dG(d, a, a, b) for a in range(4))
    return Ric


def schouten_store(Ric_std):
    # store convention: Ric_store = -Ric_std (Ric = Lambda g for de Sitter in signature (1,3))
    Ric = [[-x for x in r] for r in Ric_std]
    R = trace(Ric)
    return [[F(1, 2) * (Ric[a][b] - R * (F(ETA[a]) if a == b else F(0)) * F(1, 6)) for b in range(4)]
            for a in range(4)]


def check_conformal_blindness():
    premise("interior.imported-tractor-connection")
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    a = F(3)
    Hbad = [[F(0)] * 4 for _ in range(4)]
    Hbad[1][1] = 2 * a                                   # f = 1 + a x1^2
    for k in (F(1), F(-2, 3)):                            # f ~ (1 + (k/4) Q(x))^{-2}: H = -k eta
        Hc = [[-k * F(ETA[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
        P = schouten_store(ricci_at_origin(Hc))
        J = trace(P)
        assert all(P[i][j] == (J / 4) * (F(ETA[i]) if i == j else F(0)) for i in range(4) for j in range(4))
        assert J != 0 and P[0][0] == -k / 2 and P[2][2] == k / 2
        assert J in (F(-2), F(4, 3))
        for l in NULLS:
            assert pform(P, l, l) == Z
    P = schouten_store(ricci_at_origin(Hbad))
    J = trace(P)
    tf_nonzero = any(P[i][j] != (J / 4) * (F(ETA[i]) if i == j else F(0)) for i in range(4) for j in range(4))
    assert tf_nonzero
    assert P[1][1] == a and J == -a and P[0][0] == 0 and P[2][2] == 0
    assert P[1][1] == F(3) and Hbad[1][1] == F(6)
    l = [1, 1, 0, 0]
    assert pform(P, l, l) == QI(a)                            # own-ray class -P(l,l) != 0 for f eta
    P0 = [[F(0)] * 4 for _ in range(4)]                   # eta itself
    assert pform(P0, l, l) == Z
    # at the origin d f = 0, so the splittings of eta and f eta agree there: the same X, the same
    # I_g, the same Fock vacua; only the first-order germ of the field of infinity vacua differs
    m = companion(l)
    ui = fock_vacuum([I_G, tangent(l), tangent(m)])
    assert killed(I_G, ui)
    assert killed(act(omega(l, P0), I_G), ui)             # eta: unexcited along its own ray
    assert not killed(act(omega(l, P), I_G), ui)          # f eta: excited, same vacuum, same point
    return True


def check_frozen_point_decomposition():
    premise("correspondence.imported-vacuum-equations-scale-tractor")
    premise("mass.imported-frozen-point-tractor-connection")
    premise("one-relation.imported-pure-spinors-incidence-chart")
    P = GENERIC_P
    J = trace(P)
    Ip = lin(1, I_G, J / 4, X_T)                          # I' = I_g + (J/4) X
    assert ip(Ip, X_T) == QI(1) and ip(Ip, Ip) == QI(J / 2)
    Qp = ip(Ip, Ip)
    assert lin(1, Ip, -(Qp.re) / 2, X_T) == I_G           # I_g = I' - (1/2) Q(I') X, null
    assert ip(I_G, I_G) == Z
    # the point embedding has the same shape: v - (1/2) Q(v) n is null when <v, n> = 1, n null
    v = [QI(1), QI(2), QI(-1), QI(F(1, 2)), QI(3), QI(F(1, 3))]
    assert ip(v, X_T) == QI(1)
    w = lin(1, v, -(ip(v, v).re) / 2, X_T)
    assert ip(w, w) == Z
    for l in NULLS:
        M = omega(l, P)
        # own-ray class of infinity vacua = own-ray component of nabla I' (the X part is the point class)
        assert ip(act(M, Ip), tangent(l)) == ip(act(M, I_G), tangent(l)) == -pform(P, l, l)
    # middle slot of omega(v) I' is (J/4) v_flat - P(v,.) = minus the trace-free Schouten tensor
    for vv in ([1, 0, 0, 0], [0, 1, 0, 0], [F(1, 2), 3, -1, 2]):
        mid = act(omega(vv, P), Ip)[1:5]
        for b in range(4):
            tf = sum(QI(vv[c]) * QI(P[c][b]) for c in range(4)) - QI(J / 4) * QI(ETA[b]) * QI(vv[b])
            assert mid[b] == -tf
    einstein = [[F(ETA[i]) * F(1, 2) if i == j else F(0) for j in range(4)] for i in range(4)]
    Je = trace(einstein)
    Ipe = lin(1, I_G, Je / 4, X_T)
    for vv in ([1, 0, 0, 0], [0, 1, 0, 0], [F(1, 2), 3, -1, 2]):
        assert act(omega(vv, einstein), Ipe) == [Z] * 6       # parallel frozen point (Lambda = 3)
    assert Je / 4 * 6 == 3                                    # rho = Lambda/6
    return True


def check_matter_sources_frozen_point():
    premise("synthesis.einstein-condition-is-infinity-vacuum-incidence")
    premise("mass.imported-frozen-point-tractor-connection")
    for kappa, lam in ((F(3), F(2, 5)), (F(1, 7), F(-3))):     # kappa = 4 pi G
        g = [[F(ETA[a]) if a == b else F(0) for b in range(4)] for a in range(4)]
        T = [[F(5), F(1, 2), F(-1), F(0)], [F(1, 2), F(2), F(1, 3), F(-2)],
             [F(-1), F(1, 3), F(7, 4), F(1)], [F(0), F(-2), F(1), F(3)]]
        tau = trace(T)
        Ric = [[(lam + kappa * tau) * g[a][b] - 2 * kappa * T[a][b] for b in range(4)] for a in range(4)]
        R = trace(Ric)
        P = [[(Ric[a][b] - R * g[a][b] * F(1, 6)) * F(1, 2) for b in range(4)] for a in range(4)]
        J = trace(P)
        # middle slot of nabla I': -(P - (J/4) g) = kappa (T - (tau/4) g)
        for a in range(4):
            for b in range(4):
                assert -(P[a][b] - J / 4 * g[a][b]) == kappa * (T[a][b] - tau / 4 * g[a][b])
        # rho slot: J/4 = Lambda/6 + kappa tau/12, so d(J/4) = (kappa/12) d tau and Lambda = 6(J/4) - kappa tau/2
        assert J / 4 == lam / 6 + kappa * tau / 12
        assert tau == F(-7, 4) and J / 4 in (F(-89, 240), F(-25, 48))
        assert 6 * (J / 4) - kappa * tau / 2 == lam
        for l in NULLS:
            Ip = lin(1, I_G, J / 4, X_T)
            assert ip(act(omega(l, P), Ip), tangent(l)) == QI(kappa) * pform(T, l, l)
    return True
