"""synthesis.einstein-condition-is-infinity-vacuum-incidence: exact checks.

Tractors in the splitting of a scale g of signature (1,3), eta = diag(1,-1,-1,-1), written
(sigma, mu_b, rho) with mu lower-index; tractor form <x,y> = sigma rho' + rho sigma' + eta^{bc} mu_b mu'_c.
At a point, in a frame, the non-Levi part of the tractor connection of interior.imported-tractor-connection
acts along v as
    omega(v)(sigma, mu, rho) = (-mu(v), v_flat rho - P(v,.) sigma, P(v, mu)),
the Levi-Civita part annihilating I_g = (1,0,0) and X = (0,0,1) in this splitting. Complex numbers are GA.QI
(exact Gaussian rationals). The pairing class of a field W of isotropic 3-planes along v is
<nabla_v w, w'> on W; for w = I_g or X it is <omega(v) w, w'>.

  check_classes:        omega(v) preserves the tractor form; on W = span(I_g, l, m) the classes
                        (I_g, l), (I_g, m) are -P(v,l), -P(v,m); on span(X, l, m) the classes (X, .) are
                        g(v, .), which vanish along v = l for every P (incidence of point vacua).
  check_own_ray:        P(l,l) = 0 for the listed real null l has solution space span(eta) (rank 9 of 10);
                        adding the (I_g, m) own-ray equations leaves rank 9; P = (Lambda/6) eta gives
                        classes -(Lambda/6) g(v, w) and zero own-ray classes.
  check_fixed_vacuum:   for one W = span(I_g, l, m) the conditions P(v,l) = P(v,m) = 0 for all v have
                        real solution space span(l_flat l_flat), trace-free.
  check_fock:           in the exterior model of Cl(V_C) (GA.ext_c) the Fock vacuum of W is annihilated
                        by c(I_g), c(l), c(m), and by c(nabla_v I_g) exactly when both (I_g, .) classes
                        along v vanish (generic P: never; P = l l: always; P = eta: only along l);
                        the spinor module is 8-dimensional and c(I_g), c(X) each have a 4-dimensional
                        kernel with zero intersection.
  check_matter_and_bianchi: with kappa = 4 pi G and Lambda rational stand-ins and a rational symmetric T,
                        the store-convention Einstein tensor Ric = (Lambda + kappa tau) g - 2 kappa T has
                        own-ray classes -P(l,l) = kappa T(l,l), trace 4 Lambda + 2 kappa tau, and equals
                        Lambda g at T = 0; the Bianchi linear system (dh - dR/2 = 0, dR - 4 dh = -2 kappa
                        dtau) forces dh = kappa dtau, and at T = 0 (vacuum, h = R/4) forces dR = 0.
  check_real_direction: the totally null plane span(l, m) meets its conjugate in the real line of l:
                        l, m, conj(m) are independent over Q(i) for each listed l.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from GA import QI
from tp_premise import premise

ETA = [1, -1, -1, -1]
Z = QI(0)
PAIRS = [(a, b) for a in range(4) for b in range(a, 4)]


def _gram():
    G = [[F(0)] * 6 for _ in range(6)]
    G[0][5] = G[5][0] = F(1)
    for a in range(4):
        G[1 + a][1 + a] = F(ETA[a])
    return G


G = _gram()
I_G = [QI(1), Z, Z, Z, Z, Z]
X_T = [Z, Z, Z, Z, Z, QI(1)]


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
    """the tractor (0, u_flat, 0) of an upper-index tangent vector u."""
    return [Z] + [QI(ETA[b]) * QI(u[b]) for b in range(4)] + [Z]


def gform(u, w):
    return sum((QI(ETA[a]) * QI(u[a]) * QI(w[a]) for a in range(4)), Z)


def pform(P, u, w):
    return sum((QI(P[a][b]) * QI(u[a]) * QI(w[b]) for a in range(4) for b in range(4)), Z)


def row(u, w):
    """coefficients of P(u, w) in the unknowns P_ab (a <= b) of a symmetric P."""
    return [QI(u[a]) * QI(w[b]) + (QI(u[b]) * QI(w[a]) if a != b else Z) for (a, b) in PAIRS]


def basis4():
    return [[1 if b == a else 0 for b in range(4)] for a in range(4)]


def companion(l):
    """m = e + i f with e, f unit spatial vectors orthogonal to the unit spatial part of l and to each
    other; only used for l along a coordinate axis, where e and f are coordinate vectors."""
    axis = [k for k in range(1, 4) if l[k] != 0][0]
    rest = [k for k in range(1, 4) if k != axis]
    m = [Z, Z, Z, Z]
    m[rest[0]] = QI(1)
    m[rest[1]] = QI(0, 1)
    return m


def check_classes():
    premise("interior.imported-tractor-connection")
    premise("interior.covariant-form-vacuum-equations")
    P = [[F(2), F(1, 3), F(-1), F(0)], [F(1, 3), F(-5), F(1, 2), F(3)],
         [F(-1), F(1, 2), F(7), F(-2, 3)], [F(0), F(3), F(-2, 3), F(4)]]
    v = [F(1, 2), F(3), F(-1), F(2)]
    l = [1, 1, 0, 0]
    m = [0, 0, QI(1), QI(0, 1)]
    M = omega(v, P)
    E = [[QI(1) if i == j else Z for i in range(6)] for j in range(6)]
    for x in E:
        for y in E:
            assert ip(act(M, x), y) + ip(x, act(M, y)) == Z
    W = [I_G, tangent(l), tangent(m)]
    for a in W:
        for b in W:
            assert ip(a, b) == Z
    assert ip(act(M, I_G), tangent(l)) == -pform(P, v, l)
    assert ip(act(M, I_G), tangent(m)) == -pform(P, v, m)
    assert ip(act(M, I_G), tangent(l)) == QI(F(19, 3))
    assert ip(act(M, X_T), tangent(l)) == gform(v, l)
    assert ip(act(M, X_T), tangent(m)) == gform(v, m)
    assert ip(X_T, I_G) == QI(1)
    Ml = omega(l, P)                                   # along the point vacuum's own ray
    assert ip(act(Ml, X_T), tangent(l)) == Z and ip(act(Ml, X_T), tangent(m)) == Z
    assert ip(act(Ml, I_G), tangent(l)) == -pform(P, l, l) != Z
    return True




def check_own_ray():
    premise("interior.covariant-form-vacuum-equations")
    premise("interior.metric-parallelism-trace-schouten-condition")
    nulls = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1],
             [1, F(3, 5), F(4, 5), 0], [1, 0, F(3, 5), F(4, 5)], [1, F(4, 5), 0, F(3, 5)],
             [1, F(-3, 5), F(4, 5), 0], [1, F(2, 3), F(2, 3), F(1, 3)]]
    for l in nulls:
        assert gform(l, l) == Z
    rows = [row(l, l) for l in nulls]
    assert GA.field_rank(rows) == 9
    ker = GA.field_kernel(rows)
    assert len(ker) == 1
    eta_coords = [QI(ETA[a]) if a == b else Z for (a, b) in PAIRS]
    k = ker[0]
    lam = k[0] / eta_coords[0]
    assert all(k[i] == lam * eta_coords[i] for i in range(10))
    rows2 = rows + [row(l, companion(l)) for l in nulls[:6]]
    assert GA.field_rank(rows2) == 9
    # Lambda case: P = (Lambda/6) eta with Lambda = 3
    Pl = [[F(1, 2) * ETA[a] if a == b else F(0) for b in range(4)] for a in range(4)]
    v = [F(2), F(-1), F(1, 3), F(5)]
    for l in nulls[:6]:
        m = companion(l)
        Ml, Mv = omega(l, Pl), omega(v, Pl)
        assert ip(act(Ml, I_G), tangent(l)) == Z and ip(act(Ml, I_G), tangent(m)) == Z
        assert ip(act(Mv, I_G), tangent(l)) == -QI(F(1, 2)) * gform(v, l) != Z
    return True


def check_fixed_vacuum():
    premise("interior.covariant-form-vacuum-equations")
    premise("interior.metric-parallelism-trace-schouten-condition")
    l = [1, 1, 0, 0]
    m = [0, 0, QI(1), QI(0, 1)]
    assert gform(l, l) == Z and gform(m, m) == Z and gform(l, m) == Z
    rows = []
    for va in basis4():
        rows.append(row(va, l))
        r = row(va, m)
        rows.append([QI(x.re) for x in r])
        rows.append([QI(x.im) for x in r])
    ker = GA.field_kernel(rows)
    assert len(ker) == 1
    lf = [ETA[a] * l[a] for a in range(4)]
    ll = [QI(lf[a] * lf[b]) for (a, b) in PAIRS]
    k = ker[0]
    c = k[0] / ll[0]
    assert all(k[i] == c * ll[i] for i in range(10))
    trace = sum((QI(ETA[a]) * ll[PAIRS.index((a, a))] for a in range(4)), Z)
    assert trace == Z
    return True


GENERIC_P = [[F(2), F(1, 3), F(-1), F(0)], [F(1, 3), F(-5), F(1, 2), F(3)],
             [F(-1), F(1, 2), F(7), F(-2, 3)], [F(0), F(3), F(-2, 3), F(4)]]
L_FOCK = [1, 1, 0, 0]
M_FOCK = [0, 0, QI(1), QI(0, 1)]
N_FOCK = [1, -1, 0, 0]
MBAR_FOCK = [0, 0, QI(1), QI(0, -1)]


def _cvec(x, st):
    return GA.ext_c(list(x), G, st)


def _is0(st):
    return all(not c for c in st.values())


def check_fock():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    premise("interior.covariant-form-vacuum-equations")
    l, m = L_FOCK, M_FOCK
    W = [I_G, tangent(l), tangent(m)]
    partners = [X_T, tangent(N_FOCK), tangent(MBAR_FOCK)]
    for i in range(3):
        for j in range(3):
            assert (ip(W[i], partners[j]) == Z) == (i != j)
    psi = {frozenset(): QI(1)}
    for w in reversed(W):
        psi = _cvec(w, psi)
    assert not _is0(psi)
    assert all(_is0(_cvec(w, psi)) for w in W)

    def nabla_I(P, v):
        return [Z] + [-sum((QI(v[a]) * QI(P[a][b]) for a in range(4)), Z) for b in range(4)] + [Z]

    generic = GENERIC_P
    lf = [ETA[a] * l[a] for a in range(4)]
    radiation = [[F(lf[a] * lf[b]) for b in range(4)] for a in range(4)]
    einstein = [[F(ETA[a]) if a == b else F(0) for b in range(4)] for a in range(4)]
    dirs = basis4() + [l]
    for P, expect in ((generic, [False] * 5), (radiation, [True] * 5),
                      (einstein, [False, False, False, False, True])):
        for v, e in zip(dirs, expect):
            killed = _is0(_cvec(nabla_I(P, v), psi))
            classes_zero = (ip(act(omega(v, P), I_G), tangent(l)) == Z
                            and ip(act(omega(v, P), I_G), tangent(m)) == Z)
            assert killed == e == classes_zero
    module = []
    for k in range(4):
        for S in combinations(range(3), k):
            st = psi
            for i in reversed(S):
                st = _cvec(partners[i], st)
            module.append(st)
    keys = sorted({s for st in module for s in st}, key=lambda s: (len(s), sorted(s)))

    def coords(st):
        return [st.get(s, Z) for s in keys]

    assert GA.field_rank([coords(st) for st in module]) == 8
    rI = GA.field_rank([coords(_cvec(I_G, st)) for st in module])
    rX = GA.field_rank([coords(_cvec(X_T, st)) for st in module])
    assert rI == 4 and rX == 4
    # common kernel of c(I_g) and c(X): stack both images per basis state
    both = [coords(_cvec(I_G, st)) + coords(_cvec(X_T, st)) for st in module]
    assert GA.field_rank(both) == 8
    return True


def check_real_direction():
    premise("one-relation.imported-pure-spinors-incidence-chart")
    for l in ([1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, -1]):
        m = companion(l)
        mbar = [x.conj() if isinstance(x, QI) else x for x in m]
        assert gform(l, l) == Z and gform(m, m) == Z and gform(l, m) == Z
        assert gform(m, mbar) != Z
        assert GA.field_rank([[QI(x) for x in l], [QI(x) for x in m], [QI(x) for x in mbar]]) == 3
    return True


def check_matter_and_bianchi():
    premise("interior.metric-parallelism-trace-schouten-condition")
    premise("interior.covariant-form-vacuum-equations")
    kappa, lam = F(3), F(2, 5)
    g = [[F(ETA[a]) if a == b else F(0) for b in range(4)] for a in range(4)]
    T = [[F(5), F(1, 2), F(-1), F(0)], [F(1, 2), F(2), F(1, 3), F(-2)],
         [F(-1), F(1, 3), F(7, 4), F(1)], [F(0), F(-2), F(1), F(3)]]
    tau = sum(F(ETA[a]) * T[a][a] for a in range(4))
    for TT, tt in ((T, tau), ([[F(0)] * 4 for _ in range(4)], F(0))):
        h = lam + kappa * tt
        Ric = [[h * g[a][b] - 2 * kappa * TT[a][b] for b in range(4)] for a in range(4)]
        R = sum(F(ETA[a]) * Ric[a][a] for a in range(4))
        assert R == 4 * lam + 2 * kappa * tt
        assert R + 2 * kappa * tt == 4 * h
        P = [[(Ric[a][b] - R * g[a][b] * F(1, 6)) * F(1, 2) for b in range(4)] for a in range(4)]
        nulls = [[1, 1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1], [1, -1, 0, 0], [1, 0, -1, 0], [1, 0, 0, -1],
                 [1, F(3, 5), F(4, 5), 0], [1, 0, F(3, 5), F(4, 5)], [1, F(4, 5), 0, F(3, 5)],
                 [1, F(-3, 5), F(4, 5), 0], [1, F(2, 3), F(2, 3), F(1, 3)]]
        for l in nulls:
            assert gform(l, l) == Z
            assert -pform(P, l, l) == QI(kappa) * pform(TT, l, l)
    # T = 0: de Sitter normalisation of the store convention, Ric = Lambda g
    Ric0 = [[lam * g[a][b] for b in range(4)] for a in range(4)]
    assert Ric0[0][0] == lam and Ric0[1][1] == -lam
    # Bianchi step with matter: unknowns (dh, dR); dh - dR/2 = 0 and dR - 4 dh = -2 kappa dtau
    dtau = F(7)
    sol = GA.field_solve([[F(1), F(-1, 2)], [F(-4), F(1)]], [F(0), -2 * kappa * dtau])
    assert sol == [kappa * dtau, 2 * kappa * dtau]
    # vacuum (Schur): h = R/4, so d(R/4) - dR/2 = 0 has only dR = 0
    assert GA.mat_rank([[F(1, 4) - F(1, 2)]]) == 1
    return True


if __name__ == "__main__":
    for f in (check_classes, check_own_ray, check_fixed_vacuum, check_fock, check_real_direction, check_matter_and_bianchi):
        print(f.__name__, f())
