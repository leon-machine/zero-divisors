"""mass.de-sitter-scale-frozen-point: exact checks in Gauge Theory Gravity.

Spacetime vectors: e_0..e_3 with squares (+1, -1, -1, -1); ambient space Cl(2,4) in GA.py with squares
(e_0, e_1, e_2, e_3, e_+, e_-) = (+1, -1, -1, -1, +1, -1), n_inf = e_+ + e_-, n_0 = (e_+ - e_-)/2 (null,
<n_inf, n_0> = 1, both orthogonal to spacetime), X(x) = n_0 + x - Q(x)/2 n_inf. sigma(x) = 1 - Lambda Q/12
for Lambda in {3, -6/5, 1/2}. Derivatives of the polynomial sigma (degree 2) are exact central
differences; derivatives of rational fields are exact first-order jets.
(1) The scale tractor (premises: Thomas operator at w = 1, J = 0; flat tractor connection, P = 0):
    I_sigma = sigma n_inf + grad sigma - (Box sigma)/4 n_0 equals (1 - Lambda Q/12) n_inf - (Lambda/6) x +
    (Lambda/6) n_0 at sample points; it is parallel for the tractor gauge field of the flat scale,
    a.grad I + Omega_T(a) x I = 0 with Omega_T(a) = -n_inf ^ a, for every frame direction a; and
    <I_sigma, I_sigma> = Lambda/3. Einstein, computed from the gauge fields themselves: for hb(a) = sigma a
    the rotation-gauge field Omega(a) = -(a ^ grad sigma)/sigma solves the torsion condition
    D_mu g_nu = D_nu g_mu (g_mu = e_mu/sigma), uniquely (torsion map of rank 24), and the store's curvature
    calR(B) = -R(hb(B)) equals (Lambda/3) B on all six frame planes: de Sitter, R(a) = Lambda a (DICTIONARY C6).
(2) <X(x), n_inf + lam n_0> = 1 - lam Q(x)/2 and <X(x), n_0 + lam n_inf> = lam - Q(x)/2 at sample points;
    X(x) is null; the six points 0, e_0..e_3, 2 e_0 give X's of rank 6, and solving <X(x_k), V> = sigma(x_k)
    on them returns exactly V = n_inf + (Lambda/6) n_0.
(3) <I_Lambda, I_Lambda> = Lambda/3 (GA.dot); at Lambda = 0 it is n_inf, null; nonzero norm (non-simple
    as a bivector, by the imported simplicity criterion) exactly when Lambda != 0.
"""
import itertools
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
S13 = gtg.S13
ETA = gtg.ETA
NINF = GA.add(GA.gen(4), GA.gen(5))
N0 = GA.scal(F(1, 2), GA.sub(GA.gen(4), GA.gen(5)))
LAMS = [F(3), F(-6, 5), F(1, 2)]
XS = [[F(1, 2), F(1), F(0), F(-1, 3)], [F(2), F(0), F(1), F(1)], [F(0), F(1, 3), F(-2), F(1, 2)]]


def Q(x):
    return sum(ETA[i] * x[i] * x[i] for i in range(4))


vec = gtg.vec                            # sum x[i] e_i, zero entries dropped


def X(x):
    return GA.add(N0, vec(x), GA.scal(-Q(x) / 2, NINF))


def shift(x, i, h):
    y = list(x)
    y[i] += h
    return y


def d1(f, x, i):
    return (f(shift(x, i, 1)) - f(shift(x, i, -1))) / 2


def d2(f, x, i, j):
    if i == j:
        return f(shift(x, i, 1)) - 2 * f(x) + f(shift(x, i, -1))
    return (f(shift(shift(x, i, 1), j, 1)) - f(shift(shift(x, i, 1), j, -1))
            - f(shift(shift(x, i, -1), j, 1)) + f(shift(shift(x, i, -1), j, -1))) / 4


# jets and jet multivectors: lib/gtg.py
J = gtg.J
m_add = gtg.m_add
m_scal = gtg.m_scal
m_comm = gtg.comm                         # (xy - yx)/2
m_val = gtg.m_val


def gauge_fields(lam, x):
    """Jets at x of sigma, of g_mu = e_mu/sigma and of Omega(e_mu) = -(e_mu ^ grad sigma)/sigma."""
    def sigma(y):
        return 1 - lam * Q(y) / 12
    sg = J(sigma(x), [d1(sigma, x, i) for i in range(4)])
    dsg = [J(d1(sigma, x, i), [d2(sigma, x, i, j) for j in range(4)]) for i in range(4)]
    inv = sg.inv()
    g = [{(m,): inv} for m in range(4)]
    grad = {(i,): dsg[i] * ETA[i] for i in range(4)}          # grad sigma = e^mu d_mu sigma
    Om = []
    for m in range(4):
        wedge = m_comm({(m,): J(1)}, grad)                     # e_m ^ grad sigma (vectors: x = wedge)
        Om.append(m_scal(-inv, wedge))
    return sg, g, Om


d = gtg.m_d                              # derivative along label i of a jet multivector


def check_scale_tractor_parallel_with_norm():
    premise("mass.imported-thomas-operator")
    premise("mass.imported-frozen-point-tractor-connection")
    for lam in LAMS:
        def sigma(y):
            return 1 - lam * Q(y) / 12

        def I_at(y):
            grad = {(i,): d1(sigma, y, i) * ETA[i] for i in range(4)}
            box = sum(ETA[i] * d2(sigma, y, i, i) for i in range(4))
            return GA.add(GA.scal(sigma(y), NINF), {b: c for b, c in grad.items() if c != 0},
                          GA.scal(-box / 4, N0))
        for x in XS:
            I = I_at(x)
            want = GA.add(GA.scal(1 - lam * Q(x) / 12, NINF), GA.scal(-lam / 6, vec(x)),
                          GA.scal(lam / 6, N0))
            assert GA.eq(I, want)
            assert GA.dot(I, I, SQ) == lam / 3
            for a in range(4):
                ea = GA.gen(a)
                dI = GA.scal(F(1, 2), GA.sub(I_at(shift(x, a, 1)), I_at(shift(x, a, -1))))
                OmT = GA.neg(GA.scal(F(1, 2), GA.sub(GA.mul(NINF, ea, SQ), GA.mul(ea, NINF, SQ))))
                act = GA.scal(F(1, 2), GA.sub(GA.mul(OmT, I, SQ), GA.mul(I, OmT, SQ)))
                assert GA.is_zero(GA.add(dI, act)), (lam, x, a)
    return True


def bv_act(B, v):
    """B . v = (Bv - vB)/2 for the unit frame bivector with blade B acting on a vector v."""
    Bm = {B: F(1)}
    return GA.scal(F(1, 2), GA.sub(GA.mul(Bm, v, S13), GA.mul(v, Bm, S13)))


def vec_coords(t, dims):
    """Frame components of a vector t."""
    return [t.get((i,), F(0)) for i in dims]


def check_gauge_field_sigma_is_de_sitter():
    for lam in LAMS:
        for x in XS:
            sg, g, Om = gauge_fields(lam, x)
            assert sg.v, "sigma vanishes at the sample point"
            dims = range(len(g))
            pairs = list(itertools.combinations(dims, 2))
            for m, n in pairs:
                tor = m_add(d(g[n], m), m_scal(-1, d(g[m], n)), m_comm(Om[m], g[n]),
                            m_scal(-1, m_comm(Om[n], g[m])))
                assert m_val(tor) == {}
            # uniqueness: the torsion map on bivector-valued Omega has rank 24 at the point
            # (4 directions x 6 bivectors unknowns, 6 planes x 4 components equations: full rank)
            gv = [m_val(t) for t in g]
            cols = []
            for mu in dims:
                for B in pairs:
                    col = []
                    for a, b in pairs:
                        t = {}
                        if a == mu:
                            t = GA.add(t, bv_act(B, gv[b]))
                        if b == mu:
                            t = GA.sub(t, bv_act(B, gv[a]))
                        col.extend(vec_coords(t, dims))
                    cols.append(col)
            assert GA.rank_of_vectors(cols) == 24
            # store curvature calR(e_m ^ e_n) = -sigma^2 R(e_m ^ e_n) (hb(g_m ^ g_n) = e_m ^ e_n)
            for m, n in pairs:
                R = m_val(m_add(d(Om[n], m), m_scal(-1, d(Om[m], n)), m_comm(Om[m], Om[n])))
                calR = GA.scal(-sg.v * sg.v, R)
                assert GA.eq(calR, GA.scal(lam / 3, GA.mul(GA.gen(m), GA.gen(n), S13))), (lam, x, m, n)
    return True


def check_frozen_point_unique_constant_vector():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    for x in XS + [[F(0)] * 4]:
        Xx = X(x)
        assert GA.dot(Xx, Xx, SQ) == 0
        for lm in (F(1, 2), F(-1), F(3)):
            assert GA.dot(Xx, GA.add(NINF, GA.scal(lm, N0)), SQ) == 1 - lm * Q(x) / 2
            assert GA.dot(Xx, GA.add(N0, GA.scal(lm, NINF)), SQ) == lm - Q(x) / 2
    pts = [[F(0)] * 4] + [[F(1 if i == a else 0) for i in range(4)] for a in range(4)] + [[F(2), 0, 0, 0]]
    rows = [[GA.dot(X(p), GA.gen(i), SQ) for i in range(6)] for p in pts]
    assert GA.rank_of_vectors(rows) == 6
    # V = sum v_i e_i; <X(p), V> = sum_i <X(p), e_i> v_i = sigma(p): solve the 6 x 6 system
    for lam in LAMS:
        rhs = [1 - lam * Q(p) / 12 for p in pts]
        v = GA.field_solve([[F(c) for c in r] for r in rows], rhs)
        V = {(i,): v[i] for i in range(6) if v[i] != 0}
        assert GA.eq(V, GA.add(NINF, GA.scal(lam / 6, N0)))
    return True


def check_frozen_point_norm_and_null_limit():
    premise("mass.imported-flat-model-twistor-chart-infinity")
    for lam in LAMS + [F(0)]:
        I = GA.add(NINF, GA.scal(lam / 6, N0))
        nrm = GA.dot(I, I, SQ)
        assert nrm == lam / 3
        assert (nrm == 0) == (lam == 0)
    assert GA.dot(NINF, N0, SQ) == 1 and GA.dot(NINF, NINF, SQ) == 0 and GA.dot(N0, N0, SQ) == 0
    return True
