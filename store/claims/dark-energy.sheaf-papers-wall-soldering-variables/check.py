"""dark-energy.sheaf-papers-wall-soldering-variables: exact checks of (i)-(iii) and of the two computable
cases of (iv).

(i) Tame collar models (frame (k, m_1, m_2, m_3) of T*M; G(k, k) = lambda(tau), lambda(0) = 0,
    lambda'(0) = T != 0, G(k, m_i) = b_i(tau) with b(0) = 0, tau-dependent G1): G^{-1} is computed exactly
    (GA.rf_mat_inverse); tau G^{-1} at tau = 0 is the rank-one k-dual (x) k-dual / T, every other entry 0, and
    G^{-1}(v, v) for k(v) = 1 has a simple pole. Hence no coframe with eta_ab e^a e^b = G^{-1} is regular
    (it would make G^{-1} regular); in the diagonal model, with sigma^2 = tau, the coframe e^0 = sigma^{-1}
    theta^0 realises it: a half-power pole along k.
(ii) In the weighted frame (e^0 = k, e^i = m_i) the internal cometric eta^{ab}(tau) = G(e^a, e^b) is regular
    with eta(0) = diag(0, G1(0)), G1(0) nondegenerate (three models). The stabiliser {A : A eta + eta A^T = 0}
    in gl(4) of eta = diag(0, -1, -1, -1) has dimension 7 with u = 0 (no rotation of k into the m_i), and
    contains so(3), the three null rotations m_i -> m_i + v_i k and the dilation k -> alpha k; for the
    Lorentzian eta = diag(1, -1, -1, -1) the dimension is 6: one new generator.
(iii) Ambient fibre on (k, m_1, m_2, m_3, k*, w) with <k, k*> = 1, <m_i, m_j> = -delta_ij, <w, w> = 1:
    signature (2, 4); k and k* null, k* orthogonal to the m_i. The subalgebra of so(h) preserving
    P = span(k, m) has dimension 8 and restricts onto the 7-dimensional algebra of (ii) (rank 7, kernel 1).
    The element k -> k, k* -> -k*, fixing m and w, is in it and restricts to the dilation; exponentiated,
    k -> c k, k* -> k*/c is an isometry of h (c = 2, 3/5, -4): the boost of the ladder plane.
(iv) Through the premise's exported equations: an invertible soldering form gives the connection equation
    full rank 24; a regular corank-one one gives rank 18 and 12 free connection components. The case at the
    sheaf paper's wall (a pole) is stated open and not checked.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

R = GA.RF.const
T = GA.RF.var()
Z = GA.RF0
CS = [F(2), F(3, 5), F(-4)]


def model(i):
    if i == 0:
        lam, b = T + R(2) * T * T, [R(3) * T, T * T, Z]
        G1 = [[R(-1), Z, Z], [Z, R(-1), Z], [Z, Z, R(-1) + T]]
    elif i == 1:
        lam, b = R(3) * T - T * T, [T, Z, R(2) * T]
        G1 = [[R(-1), R(F(1, 2)), Z], [R(F(1, 2)), R(-2) + T * T, Z], [Z, Z, R(-1)]]
    else:
        lam, b = R(F(-1, 2)) * T, [Z, Z, Z]
        G1 = [[R(-1), Z, Z], [Z, R(-1), Z], [Z, Z, R(-1)]]
    G = [[lam] + b] + [[b[i]] + G1[i] for i in range(3)]
    return G, lam, G1


def check_soldering_form_acquires_half_power_pole():
    premise("sheaf.tameness")
    premise("sheaf.metrics-residue-square-root-twist")
    for i in range(3):
        G, lam, G1 = model(i)
        Tk = lam.deriv().eval(0)
        assert Tk != 0 and lam.eval(0) == 0
        Ginv = GA.rf_mat_inverse(G)
        res = [[(T * Ginv[a][c]).eval(0) for c in range(4)] for a in range(4)]
        assert res[0][0] == 1 / Tk
        assert all(res[a][c] == 0 for a in range(4) for c in range(4) if (a, c) != (0, 0))
        g00 = Ginv[0][0]
        g00_den_at0 = GA.peval(g00.den, F(0))
        assert g00_den_at0 == 0 and (T * g00).eval(0) != 0          # simple pole at tau = 0
    sigma = GA.RF.var()
    e0 = GA.RF1 / sigma                                             # e^0 = sigma^{-1} theta^0
    assert (e0 * e0).eqrf(GA.RF1 / (sigma * sigma))                 # = G^{-1}(theta-dual) with tau = sigma^2
    assert GA.peval(e0.den, F(0)) == 0


def stabiliser(eta):
    rows = []
    for a in range(4):
        for b in range(a, 4):
            row = [F(0)] * 16
            for i in range(4):
                for j in range(4):
                    if i == a:
                        row[4 * i + j] += eta[j][b]
                    if i == b:
                        row[4 * i + j] += eta[a][j]
            rows.append(row)
    return GA.field_kernel(rows)


def in_span(vec, basis):
    return GA.rank_of_vectors(basis + [vec]) == GA.rank_of_vectors(basis)


def check_weighted_chart_and_seven_dim_stabiliser():
    premise("sheaf.tameness")
    for i in range(3):
        G, lam, G1 = model(i)
        eta0 = [[G[a][c].eval(0) for c in range(4)] for a in range(4)]
        assert eta0[0] == [0, 0, 0, 0] and all(eta0[a][0] == 0 for a in range(4))
        assert GA.mat_rank([row[1:] for row in eta0[1:]]) == 3
    eta_deg = [[F(0)] * 4 for _ in range(4)]
    for i in (1, 2, 3):
        eta_deg[i][i] = F(-1)
    eta_lor = [[F(0)] * 4 for _ in range(4)]
    eta_lor[0][0] = F(1)
    for i in (1, 2, 3):
        eta_lor[i][i] = F(-1)
    stab = stabiliser(eta_deg)
    assert len(stab) == 7 and len(stabiliser(eta_lor)) == 6
    assert all(v[4 * 0 + j] == 0 for v in stab for j in (1, 2, 3))
    unit = lambda i, j: [F(int(4 * i + j == t)) for t in range(16)]
    dil = unit(0, 0)
    nulls = [unit(i, 0) for i in (1, 2, 3)]
    rots = [[x - y for x, y in zip(unit(i, j), unit(j, i))] for (i, j) in ((1, 2), (1, 3), (2, 3))]
    for v in [dil] + nulls + rots:
        assert in_span(v, stab)
    assert GA.rank_of_vectors([dil] + nulls + rots) == 7


def ambient():
    hh = [[F(0)] * 6 for _ in range(6)]
    hh[0][4] = hh[4][0] = F(1)
    for i in (1, 2, 3):
        hh[i][i] = F(-1)
    hh[5][5] = F(1)
    return hh


def check_dilation_lifts_to_ladder_boost():
    premise("sheaf.localised-transport")
    premise("dark-energy.stelle-west-vector-frozen-point")
    hh = ambient()
    assert GA.congruence_signature(hh) == (2, 4, 0)
    assert hh[0][0] == 0 and hh[4][4] == 0 and hh[0][4] == 1 and all(hh[4][i] == 0 for i in (1, 2, 3))
    rows = []
    for a in range(6):
        for b in range(a, 6):
            row = [F(0)] * 36
            for i in range(6):
                for j in range(6):
                    if j == a:
                        row[6 * i + j] += hh[i][b]
                    if j == b:
                        row[6 * i + j] += hh[a][i]
            rows.append(row)
    for i in (4, 5):
        for j in range(4):
            row = [F(0)] * 36
            row[6 * i + j] = F(1)
            rows.append(row)
    stab6 = GA.field_kernel(rows)
    assert len(stab6) == 8
    restr = [[v[6 * i + j] for i in range(4) for j in range(4)] for v in stab6]
    assert GA.rank_of_vectors(restr) == 7
    lift = [[F(0)] * 6 for _ in range(6)]
    lift[0][0], lift[4][4] = F(1), F(-1)
    flat = [lift[i][j] for i in range(6) for j in range(6)]
    assert GA.rank_of_vectors(stab6 + [flat]) == 8
    assert [flat[6 * i + j] for i in range(4) for j in range(4)] == [F(int(i == j == 0)) for i in range(4) for j in range(4)]
    for c in CS:
        Lc = [[F(int(i == j)) for j in range(6)] for i in range(6)]
        Lc[0][0], Lc[4][4] = c, 1 / c
        img = GA.mat_mul(GA.mat_mul([list(r) for r in zip(*Lc)], hh), Lc)
        assert img == hh


def check_dichotomy_cases_through_the_free_sector():
    ex = premise("dark-energy.walls-free-sector")
    tm, conn, ker = ex["torsion_matrix"], ex["conn_eq_on_omega"], ex["kernel"]
    assert GA.rank_of_vectors(tm(ex["E_INV"])) == 24
    assert GA.rank_of_vectors(tm(ex["E_LOR"])) == 18
    rows = conn(ex["E_LOR"])
    assert GA.rank_of_vectors(rows) == 12 and len(ker(rows)) == 12
    assert GA.rank_of_vectors(conn(ex["E_INV"])) == 24
