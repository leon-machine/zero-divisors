"""tower.compatibility-connecting-maps-transported: exact checks.

GA.py blade engine. Floor T_k over the ground A = Cl(p,q) (p - q even): ground generators at
0..n-1, plane j at n+2(j-1) (e_j, +1), n+2j-1 (f_j, -1); v_j = (e_j+f_j)/2, w_j = (e_j-f_j)/2;
matrix units of plane j labelled as in Fact transport.rule-1-morita-trivial: E11 = v w, E12 = v,
E21 = w, E22 = w v. Omega_k = omega_1...omega_k. The identification phi_k^{-1} : A (x) Mat_{2^k} -> T_k
of tower.commuting-copies, planes nested in order with plane k carrying the outer index:
    phi_k^{-1}(a (x) E_{I,J}) = E_k[i_k,1] ( ... E_1[i_1,1] alpha_k(a) E_1[1,j_1] ... ) E_k[1,j_k],
alpha_k(a) = a on even blades and a Omega_k on odd blades (the twisted ground copy). A matrix over
A is a dict {(I, J): ground element}, I and J tuples (outer index first).
(1) The data: phi_k^{-1} is multiplicative on matrix units and sends 1 (x) Omega-bar_k (the diagonal
    with entry prod_j s(i_j), s(1) = -1, s(2) = +1) to Omega_k, and u_A (x) Omega-bar_k to the floor's
    volume element u_{T_k}; V_k is invertible (V_k V_k^-1 = 1, u_A^2 = +-1).
(2) The lemma: phi_{k+1}^{-1}(Ad(V_k) theta_k(z)) = phi_k^{-1}(z) (computed in T_{k+1}) for EVERY
    basis element z = a (x) E_{I,J} (a a ground blade), for the grounds Cl(0,0), Cl(1,1), Cl(2,0),
    Cl(0,2) at k = 1, 2 and Cl(1,3), Cl(3,1), Cl(2,2) at k = 1, with
    V_k = diag(u_A (x) 1, 1 (x) Omega-bar_k).
(3) The naive transported single-step corrector diag(1, u_A (x) Omega-bar_k) (the image of
    diag(1, u_{T_k})) fails on some basis element for every ground with n >= 2 here; for the trivial
    ground n = 0 (u_A = 1) it coincides with V_k. The labelling matters: with vw and wv exchanged for
    the new plane, V_k fails, the bare exchange of corners diag(1 (x) Omega-bar_k, u_A (x) 1) fails too,
    and the corrector that works is diag(1, u_A (x) Omega-bar_k), the transported single-step one
    (reported: the statement's "exchanges the two corners of V_k" is not what the computation gives).
EXPORTS: Tower (phi_k^{-1}, alpha_k, the matrix units), idx, omega_bar, theta, corrector, conj_diag.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

CASES = [((0, 0), 1), ((0, 0), 2), ((1, 1), 1), ((1, 1), 2), ((2, 0), 1), ((2, 0), 2), ((0, 2), 1),
         ((0, 2), 2), ((1, 3), 1), ((3, 1), 1), ((2, 2), 1)]


class Tower(object):
    def __init__(self, p, q, kmax, swap=()):
        self.n = n = p + q
        self.S = tuple([1] * p + [-1] * q + [1, -1] * kmax)
        S = self.S
        self.E = []
        self.om = []
        for j in range(kmax):
            e, f = GA.gen(n + 2 * j), GA.gen(n + 2 * j + 1)
            v, w = GA.scal(F(1, 2), GA.add(e, f)), GA.scal(F(1, 2), GA.sub(e, f))
            if j in swap:
                v, w = w, v
            self.E.append({(1, 1): GA.mul(v, w, S), (1, 2): v, (2, 1): w, (2, 2): GA.mul(w, v, S)})
            self.om.append(GA.mul(e, f, S))
        self.uA = {tuple(range(n)): F(1)}

    def mul(self, *xs):
        out = GA.sc(1)
        for x in xs:
            out = GA.mul(out, x, self.S)
        return out

    def Om(self, k):
        return self.mul(*self.om[:k])

    def alpha(self, a, k):
        Om = self.Om(k)
        out = {}
        for b, c in a.items():
            piece = {b: c} if len(b) % 2 == 0 else GA.mul({b: c}, Om, self.S)
            out = GA.add(out, piece)
        return out

    def phi_inv(self, M, k):
        out = {}
        for (I, J), a in M.items():
            x = self.alpha(a, k)
            for lvl in range(k):          # inner plane first: index k-1-lvl of the tuples
                j = lvl
                i_, l_ = I[k - 1 - lvl], J[k - 1 - lvl]
                x = self.mul(self.E[j][(i_, 1)], x, self.E[j][(1, l_)])
            out = GA.add(out, x)
        return out


def idx(k):
    return list(product((1, 2), repeat=k))


def omega_bar(I):
    s = 1
    for i in I:
        s *= -1 if i == 1 else 1
    return F(s)


def conj_diag(Vd, Vinv, N, S):
    out = {}
    for (K, L), a in N.items():
        z = GA.mul(GA.mul(Vd[K], a, S), Vinv[L], S)
        if z:
            out[(K, L)] = z
    return out


def theta(M):
    return {((o,) + I, (o,) + J): a for (I, J), a in M.items() for o in (1, 2)}


def inv_pm1(u, S):
    return u if GA.eq(GA.mul(u, u, S), GA.sc(1)) else GA.neg(u)


def corrector(T, k, first_ground):
    """diag(u_A (x) 1, 1 (x) Omega-bar_k) if first_ground, else diag(1 (x) Omega-bar_k, u_A (x) 1)."""
    S = T.S
    uinv = inv_pm1(T.uA, S)
    V, Vi = {}, {}
    for o in (1, 2):
        for I in idx(k):
            K = (o,) + I
            ground_corner = (o == 1) == first_ground
            V[K] = T.uA if ground_corner else GA.sc(omega_bar(I))
            Vi[K] = uinv if ground_corner else GA.sc(omega_bar(I))
    return V, Vi


def naive(T, k):
    S = T.S
    uinv = inv_pm1(T.uA, S)
    V, Vi = {}, {}
    for o in (1, 2):
        for I in idx(k):
            K = (o,) + I
            V[K] = GA.sc(1) if o == 1 else GA.scal(omega_bar(I), T.uA)
            Vi[K] = GA.sc(1) if o == 1 else GA.scal(omega_bar(I), uinv)
    return V, Vi


def basis(T, k):
    for a in GA.all_blades(T.n):
        for I in idx(k):
            for J in idx(k):
                yield {(I, J): {a: F(1)}}


def holds(T, k, V, Vi):
    for z in basis(T, k):
        lhs = T.phi_inv(z, k)
        rhs = T.phi_inv(conj_diag(V, Vi, theta(z), T.S), k + 1)
        if not GA.eq(lhs, rhs):
            return False
    return True


EXPORTS = {"Tower": Tower, "idx": idx, "omega_bar": omega_bar, "theta": theta,
           "corrector": corrector, "conj_diag": conj_diag}


def check_identification_data():
    premise("tower.commuting-copies")
    premise("tower.volume-elements-planes")
    for (p, q), k in CASES:
        T = Tower(p, q, k + 1)
        S = T.S
        units = [(I, J) for I in idx(k) for J in idx(k)]
        for (I, J) in units:
            for (K, L) in units:
                prod_ = GA.mul(T.phi_inv({(I, J): GA.sc(1)}, k), T.phi_inv({(K, L): GA.sc(1)}, k), S)
                want = T.phi_inv({(I, L): GA.sc(1)}, k) if J == K else {}
                assert GA.eq(prod_, want)
        Ob = {(I, I): GA.sc(omega_bar(I)) for I in idx(k)}
        assert GA.eq(T.phi_inv(Ob, k), T.Om(k))
        uT = {tuple(range(T.n + 2 * k)): F(1)}
        assert GA.eq(T.phi_inv({(I, I): GA.scal(omega_bar(I), T.uA) for I in idx(k)}, k), uT)
        u2 = GA.mul(T.uA, T.uA, S)
        assert GA.eq(u2, GA.sc(1)) or GA.eq(u2, GA.sc(-1))
        V, Vi = corrector(T, k, True)
        assert all(GA.eq(GA.mul(V[K], Vi[K], S), GA.sc(1)) for K in V)
    return True


def check_transported_connecting_map_is_ad_v_theta():
    premise("tower.grade-twist-when-it-inner")
    premise("transport.rule-1-morita-trivial")
    for (p, q), k in CASES:
        assert (p - q) % 2 == 0
        T = Tower(p, q, k + 1)
        V, Vi = corrector(T, k, True)
        assert holds(T, k, V, Vi), ((p, q), k)
    return True


# grounds on which the exchanged labelling of the outer plane is also tested
SWAP_GROUNDS = ((1, 1), (2, 0), (1, 3))


def tower_to_next_floor(p, q, k, **kw):
    """The tower through floor k + 1, where the connecting map at rung k lands."""
    return Tower(p, q, k + 1, **kw)


def check_naive_corrector_and_labelling_convention():
    for (p, q), k in CASES:
        T = tower_to_next_floor(p, q, k)
        V, Vi = naive(T, k)
        if p + q == 0:
            assert holds(T, k, V, Vi)
        else:
            assert not holds(T, k, V, Vi), ((p, q), k)
        if (p, q) in SWAP_GROUNDS:
            # exchange vw and wv for the outer (new) plane: the ground volume moves to the second
            # corner, where it joins the planes' volume; the bare exchange of corners fails
            Ts = tower_to_next_floor(p, q, k, swap=(k,))
            Vn, Vni = naive(Ts, k)
            assert holds(Ts, k, Vn, Vni)
            Vx, Vxi = corrector(Ts, k, False)
            assert not holds(Ts, k, Vx, Vxi)
            V0, V0i = corrector(Ts, k, True)
            assert not holds(Ts, k, V0, V0i)
    return True
