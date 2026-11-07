"""Exact checks: the window Sugawara identity, linear dispersion, the phase flow with the kernel unit,
the band compression of the null momentum, and the Luttinger normal modes.

Tower planes: plane j has e_j = gen(o + 2j) (square +1), f_j = gen(o + 2j + 1) (square -1); v_j = (e_j + f_j)/2
creator, w_j = (e_j - f_j)/2 annihilator, n_j = v_j w_j (the convention of the fluctuation-forms result).
With the kernel (o = 2), g1 = gen(0), g2 = gen(1) square -1 and J = g1 g2. On a window of L modes
rho_q = sum_j v_j w_{j+q} lowers the level index by q, T = sum_{q=1}^{L-1} rho_q* rho_q, Nhat = sum_j n_j.
"""
from fractions import Fraction as F
from itertools import product

import GA
from tp_premise import premise

WINDOWS = (1, 2, 3, 4, 5, 6)


def _modes(L, kernel=False):
    o = 2 if kernel else 0
    s = tuple(([-1, -1] if kernel else []) + [1, -1] * L)
    mul = lambda x, y: GA.mul(x, y, s)
    v = [GA.add(GA.scal(F(1, 2), GA.gen(o + 2 * j)), GA.scal(F(1, 2), GA.gen(o + 2 * j + 1))) for j in range(L)]
    w = [GA.add(GA.scal(F(1, 2), GA.gen(o + 2 * j)), GA.scal(F(-1, 2), GA.gen(o + 2 * j + 1))) for j in range(L)]
    n = [mul(v[j], w[j]) for j in range(L)]
    return s, mul, v, w, n


def _star(x, s):
    out = {}
    for b, c in x.items():
        g = len(b)
        sg = (-1) ** (g * (g - 1) // 2)
        for k in b:
            if s[k] == -1:
                sg = -sg
        out[b] = sg * c
    return {b: c for b, c in out.items() if c != 0}


def _rho(mul, v, w, idx, q):
    """sum over the window idx of v_{idx[j]} w_{idx[j+q]}: moves a particle q steps down idx."""
    return GA.add(*[mul(v[idx[j]], w[idx[j + q]]) for j in range(len(idx) - q)])


def _comm(mul, x, y):
    return GA.sub(mul(x, y), mul(y, x))


def _number(n):
    return GA.add(*n)


def _vac(mul, v, w):
    out = GA.sc(1)
    for j in range(len(v)):
        out = mul(out, mul(w[j], v[j]))
    return out


def _basis(mul, v, vac, occ):
    st = vac
    for j in reversed(range(len(occ))):
        if occ[j]:
            st = mul(v[j], st)
    return st


def check_window_sugawara_identity_holds_as_an_algebra_identity():
    premise("std-algebra.witt-basis-car")
    premise("hawking.current-commutator-exactly-edge-split")
    ok = True
    for L in WINDOWS:
        s, mul, v, w, n = _modes(L)
        idx = list(range(L))
        T = GA.add(*[mul(_star(_rho(mul, v, w, idx, q), s), _rho(mul, v, w, idx, q)) for q in range(1, L)])
        Nh = _number(n)
        rhs = GA.sub(GA.add(*[GA.scal(j, n[j]) for j in range(L)]), GA.scal(F(1, 2), mul(Nh, GA.sub(Nh, GA.sc(1)))))
        ok = ok and GA.eq(T, rhs)
        # sea form: modes k = j - L/2 with weight k + 1/2, sea k < 0 filled, Q = Nhat - L/2:
        # sum_k (k + 1/2) n_k + L^2/8 = Q^2/2 + T
        if L % 2 == 0:
            Mh = L // 2
            H = GA.add(*[GA.scal(F(2 * (j - Mh) + 1, 2), n[j]) for j in range(L)], GA.sc(F(Mh * Mh, 2)))
            Q = GA.sub(Nh, GA.sc(Mh))
            ok = ok and GA.eq(H, GA.add(GA.scal(F(1, 2), mul(Q, Q)), T))
        # the quartic part: sum_q sum (rho_q* rho_q - its quadratic part) = -Nhat(Nhat - 1)/2 needs the linear weights;
        # with weights j^2 the same T does not reproduce the energy
        if L >= 3:
            curved = GA.add(*[GA.scal(j * j, n[j]) for j in range(L)])
            ok = ok and not GA.eq(curved, GA.add(T, GA.scal(F(1, 2), mul(Nh, GA.sub(Nh, GA.sc(1))))))
    GA.check("sum_q rho_q* rho_q = sum_j j n_j - Nhat(Nhat - 1)/2 on windows of 1..6 modes; sea form Q^2/2 + T", ok)
    return ok


def check_linear_dispersion_and_the_phase_flow_with_the_kernel_unit():
    premise("hawking.current-commutator-exactly-edge-split")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    ok = True
    for L in (2, 3, 4):
        s, mul, v, w, n = _modes(L, kernel=True)
        J = mul(GA.gen(0), GA.gen(1))
        idx = list(range(L))
        H = GA.add(*[GA.scal(F(2 * j + 1, 2), n[j]) for j in range(L)])
        u = GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), J))          # e^{J t / 2}
        U = GA.sc(1)
        for j in range(L):
            uj = GA.sc(1)
            for _ in range(2 * j + 1):
                uj = mul(uj, u)                                     # e^{J t (j + 1/2)}
            U = mul(U, GA.add(GA.sc(1), mul(GA.sub(uj, GA.sc(1)), n[j])))
        ok = ok and GA.eq(mul(U, _star(U, s)), GA.sc(1))
        for q in range(1, L):
            rq = _rho(mul, v, w, idx, q)
            rqs = _star(rq, s)
            ok = ok and GA.eq(_comm(mul, H, rqs), GA.scal(q, rqs)) and GA.eq(_comm(mul, H, rq), GA.scal(-q, rq))
            uq = GA.sc(1)
            for _ in range(2 * q):
                uq = mul(uq, u)                                     # e^{J q t}
            ok = ok and GA.eq(mul(mul(U, rqs), _star(U, s)), mul(uq, rqs))
        if L >= 3:
            curved = GA.add(*[GA.scal(j * j, n[j]) for j in range(L)])
            r1s = _star(_rho(mul, v, w, idx, 1), s)
            c = _comm(mul, curved, r1s)
            ok = ok and not any(GA.eq(c, GA.scal(k, r1s)) for k in range(-2 * L, 2 * L))
    GA.check("[H, rho_q*] = q rho_q* for H = sum (j + 1/2) n_j; e^{JtH} rho_q* e^{-JtH} = e^{Jqt} rho_q*", ok)
    return ok


def check_band_compression_of_the_null_momentum_has_half_integer_weights():
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    ok = True
    # h_k has P-spectral wave function Delta^{-1/2} on [k Delta, (k + 1) Delta); <h_k, P h_l> = delta_kl Delta (k + 1/2)
    for Delta in (F(1), F(2, 3), F(5, 7)):
        for k in range(-4, 4):
            lo, hi = k * Delta, (k + 1) * Delta
            mean = (hi * hi - lo * lo) / 2 / Delta                  # Delta^{-1} int p dp over the band
            ok = ok and mean == Delta * (k + F(1, 2))
            occ = 1 if hi <= 0 else 0                                # band average of chi(P < 0)
            ok = ok and occ == (1 if k < 0 else 0)
    # on the window k = -2 .. 1 the null vacuum is the sea: ground state of the compressed energy, Q = 0, rho_q sea = 0
    s, mul, v, w, n = _modes(4)
    vac = _vac(mul, v, w)
    sea = _basis(mul, v, vac, [1, 1, 0, 0])
    idx = list(range(4))
    H = GA.add(*[GA.scal(F(2 * (j - 2) + 1, 2), n[j]) for j in range(4)], GA.sc(2))
    ok = ok and GA.is_zero(mul(H, sea)) and not GA.is_zero(sea)
    for q in range(1, 4):
        ok = ok and GA.is_zero(mul(_rho(mul, v, w, idx, q), sea))
    GA.check("band compression of P: weights Delta (k + 1/2); the null vacuum's window sea has energy 0", ok)
    return ok


def check_luttinger_normal_modes_on_edge_clean_vectors():
    premise("hawking.current-commutator-exactly-edge-split")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    ok = True
    L = 4
    s, mul, v, w, n = _modes(2 * L)
    Rb, Lb = list(range(L)), list(range(L, 2 * L))
    Lrev = list(reversed(Lb))                 # the left branch: energy decreases up the window
    vac = _vac(mul, v, w)
    H0 = GA.add(*[GA.scal(F(2 * j + 1, 2) - 2, n[Rb[j]]) for j in range(L)],
                *[GA.scal(2 - F(2 * j + 1, 2), n[Lb[j]]) for j in range(L)])
    g4, g2 = F(1, 2), F(9, 10)
    rR, rL = _rho(mul, v, w, Rb, 1), _rho(mul, v, w, Lrev, 1)
    rRs, rLs = _star(rR, s), _star(rL, s)
    V = GA.add(GA.scal(g4, GA.add(mul(rRs, rR), mul(rLs, rL))), GA.scal(g2, GA.add(mul(rR, rL), mul(rLs, rRs))))
    H = GA.add(H0, V)
    beta = GA.add(rRs, GA.scal(F(1, 3), rL))  # r = 1/3 solves g2 r^2 - 2(1 + g4) r + g2 = 0
    C = _comm(mul, H, beta)
    omega = F(6, 5)                           # sqrt((1 + g4)^2 - g2^2)
    ok = ok and g2 * F(1, 9) - 2 * (1 + g4) * F(1, 3) + g2 == 0 and omega * omega == (1 + g4) ** 2 - g2 ** 2
    count = 0
    for mid in product((0, 1), repeat=4):
        occ = [1, mid[0], mid[1], 0, 0, mid[2], mid[3], 1]   # both branches edge-clean at depth 1
        psi = _basis(mul, v, vac, occ)
        ok = ok and GA.eq(mul(C, psi), GA.scal(omega, mul(beta, psi)))
        count += 1
    ok = ok and count == 16
    # off the edge-clean subspace the relation fails: the top right mode filled
    psi = _basis(mul, v, vac, [1, 1, 0, 1, 0, 0, 1, 1])
    ok = ok and not GA.eq(mul(C, psi), GA.scal(omega, mul(beta, psi)))
    GA.check("Luttinger q = 1: [H, beta*] = (6/5) beta* on all 16 depth-1 edge-clean vectors, not off them", ok)
    return ok
