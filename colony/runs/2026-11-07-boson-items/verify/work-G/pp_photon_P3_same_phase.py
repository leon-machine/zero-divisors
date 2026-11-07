"""synthesis.null-plane-photon-data-and-the-pair-currents-of-the-generators: exact checks.

Spacetime side: Cl(1,3), gamma_0^2 = 1, gamma_i^2 = -1, I4 = g0 g1 g2 g3, a null plane with generators along
n = g0 + g3, second null direction m = g0 - g3, transverse g1, g2, J = g1 g2. Fields are polynomials in the four
coordinates with multivector coefficients (exact Fractions); nabla = sum_mu gamma^mu d_mu.
(1) div(F1.A2 - F2.A1) = (div F1).A2 - (div F2).A1, F = nabla ^ A, F.A = <F A>_1, for generic polynomial A1, A2.
(2) In the gauge n.A = 0: n.F = d_n A and n.omega = d_n A1perp . A2perp - d_n A2perp . A1perp identically; F is
    unchanged by A -> A + nabla chi.
(3) For a generic constant bivector F: n.(n.F) = 0, n.F = alpha n + Eperp, n.T(n) = -Eperp^2 > 0 with
    T(a) = -1/2 F a F; I4 (n ^ a) = (n ^ a) J = n ^ (a J) for transverse a; eps = g1 Eperp lies in span{1, J} and the
    rotation about the generator multiplies it by a phase.
Tower side: plane j has e = gen(2j) (square +1), f = gen(2j + 1) (square -1), c*_j = (e + f)/2, c_j = (e - f)/2; the
kernel plane gen(2M), gen(2M + 1) (squares -1) gives J = gen(2M) gen(2M + 1); * reverses and flips the sign of
each negative-square generator. Generators g, channels a = 0 (+), 1 (-), levels k = 1..L;
J^{ab}_m = sum_k c*_{a,k} c_{b,k+m} on one generator.
(4) The u(2) window identity for all a, b, c, d and |m|, |n| <= 1 at L = 3; central value m on edge-clean basis states.
(5) The rotation U = prod (1 + (z_a - 1) n_{a,k}), z_+ = (3 + 4J)/5, z_- = (3 - 4J)/5: unitary; densities invariant;
    J^{+-} and J^{-+} multiplied by z_+^2 and z_-^2.
(6) Flip-current defect in the bottom-filled window: one generator: ||[J^+_m, J^-_n] Omega||^2 = 2|m + n|;
    N = 2 generators with weight matrices M (M_gh pairs channel + of generator g with channel - of h):
    ||D Omega||^2 = 2 |q| ||M M*||_F^2, central value tr(M M*), bound 2|q| tr^2 / N with equality only for M = 1;
    N = 3 generators with M = 1: ||D Omega||^2 = 6 = 2 tr^2 / 3. The window Hamiltonian H = sum k n_k shifts every
    current: [H, J^{ab}_m] = -m J^{ab}_m.
"""
import itertools
from fractions import Fraction as F

import GA
from tp_premise import premise

# ------------------------------------------------------------------ spacetime algebra helpers
_SQ = (1, -1, -1, -1)


def _m4(x, y):
    return GA.mul(x, y, _SQ)


def _grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def _g(i):
    return GA.gen(i)


def _vdot(a, b):
    return _grade(_m4(a, b), 0).get((), F(0))


def _padd(*fs):
    out = {}
    for f in fs:
        for e, mv in f.items():
            out[e] = GA.add(out.get(e, {}), mv)
    return {e: mv for e, mv in out.items() if mv}


def _pneg(f):
    return {e: GA.neg(mv) for e, mv in f.items()}


def _pmul(f, h):
    out = {}
    for e1, m1 in f.items():
        for e2, m2 in h.items():
            e = tuple(a + b for a, b in zip(e1, e2))
            out[e] = GA.add(out.get(e, {}), _m4(m1, m2))
    return {e: mv for e, mv in out.items() if mv}


def _pconst(mv):
    return {(0, 0, 0, 0): mv} if mv else {}


def _pgrade(f, k):
    return {e: _grade(mv, k) for e, mv in f.items() if _grade(mv, k)}


def _pd(f, mu):
    out = {}
    for e, mv in f.items():
        if e[mu]:
            e2 = list(e)
            e2[mu] -= 1
            out[tuple(e2)] = GA.add(out.get(tuple(e2), {}), GA.scal(e[mu], mv))
    return {e: mv for e, mv in out.items() if mv}


def _nabla(f):
    return _padd(*[_pmul(_pconst(GA.scal(F(1, _SQ[mu]), _g(mu))), _pd(f, mu)) for mu in range(4)])


def _pdn(f, n):
    return _padd(*[{e: GA.scal(n.get((mu,), 0), mv) for e, mv in _pd(f, mu).items()}
                   for mu in range(4) if n.get((mu,), 0)])


def _poly_vec(seed, deg):
    out = {}
    mons = [e for e in itertools.product(range(deg + 1), repeat=4) if sum(e) <= deg]
    for j, e in enumerate(mons):
        mv = {}
        for mu in range(4):
            c = F(((seed * 7 + j * 3 + mu * 5) % 11) - 5, 1 + (j + mu + seed) % 3)
            if c:
                mv = GA.add(mv, GA.scal(c, _g(mu)))
        if mv:
            out[e] = mv
    return out


def _gauge_vec(seed, deg, n):
    out = {}
    for e, mv in _poly_vec(seed, deg).items():
        x = GA.add(GA.scal(mv.get((0,), F(0)), n), GA.scal(mv.get((1,), F(0)), _g(1)),
                   GA.scal(mv.get((2,), F(0)), _g(2)))
        if x:
            out[e] = x
    return out


def _perp(f):
    out = {}
    for e, mv in f.items():
        x = GA.add(GA.scal(mv.get((1,), 0), _g(1)), GA.scal(mv.get((2,), 0), _g(2)))
        if x:
            out[e] = x
    return out


def _symp(F1, A2, F2, A1):
    return _padd(_pgrade(_pmul(F1, A2), 1), _pneg(_pgrade(_pmul(F2, A1), 1)))


# ------------------------------------------------------------------ tower helpers
class _Tower(object):
    def __init__(self, nm):
        self.n = nm
        self.sq = tuple([1, -1] * nm + [-1, -1])
        self.J = GA.mul(GA.gen(2 * nm), GA.gen(2 * nm + 1), self.sq)
        self.c = [GA.add(GA.scal(F(1, 2), GA.gen(2 * j)), GA.scal(F(-1, 2), GA.gen(2 * j + 1))) for j in range(nm)]
        self.cd = [GA.add(GA.scal(F(1, 2), GA.gen(2 * j)), GA.scal(F(1, 2), GA.gen(2 * j + 1))) for j in range(nm)]

    def m(self, *xs):
        out = GA.sc(1)
        for x in xs:
            out = GA.mul(out, x, self.sq)
        return out

    def num(self, p):
        return self.m(self.cd[p], self.c[p])

    def bil(self, p, q):
        return self.m(self.cd[p], self.c[q])

    def comm(self, x, y):
        return GA.sub(self.m(x, y), self.m(y, x))

    def star(self, x):
        out = {}
        for b, c in x.items():
            g = len(b)
            s = (-1) ** (g * (g - 1) // 2)
            for i in b:
                if self.sq[i] == -1:
                    s = -s
            out[b] = s * c
        return {b: c for b, c in out.items() if c != 0}

    def proj(self, occ):
        P = GA.sc(1)
        for p, o in enumerate(occ):
            P = self.m(P, self.num(p) if o else GA.sub(GA.sc(1), self.num(p)))
        return P

    def omega(self, P, X):
        s = F(0)
        for b, c in P.items():
            d = X.get(b)
            if d is not None:
                sg, _ = GA.blade_mul(b, b, self.sq)
                s += c * d * sg
        return (2 ** self.n) * s


def _current(T, idx, L, a, b, m):
    out = {}
    for k in range(1, L + 1):
        if 1 <= k + m <= L:
            out = GA.add(out, T.bil(idx(a, k), idx(b, k + m)))
    return out


# ------------------------------------------------------------------ test data (module level: any choice must pass)
_GAUGE_SEEDS = (3, 4)
_GAUGE_FREE_SEED = 1
_CHI = {(1, 1, 0, 0): GA.sc(3), (0, 2, 1, 0): GA.sc(-2), (2, 0, 0, 1): GA.sc(5)}


# ------------------------------------------------------------------ checks
def check_maxwell_symplectic_current_identity():
    A1, A2 = _poly_vec(1, 2), _poly_vec(2, 2)
    F1, F2 = _pgrade(_nabla(A1), 2), _pgrade(_nabla(A2), 2)
    lhs = _pgrade(_nabla(_symp(F1, A2, F2, A1)), 0)
    d1, d2 = _pgrade(_nabla(F1), 1), _pgrade(_nabla(F2), 1)
    rhs = _padd(_pgrade(_pmul(d1, A2), 0), _pneg(_pgrade(_pmul(d2, A1), 0)))
    GA.check("div(F1.A2 - F2.A1) = (div F1).A2 - (div F2).A1", _padd(lhs, _pneg(rhs)) == {})
    GA.check("the test fields are not free (div F1 != 0), so the identity is not vacuous", d1 != {})
    # the symmetric term F1 . F2 that cancels is nonzero for these fields
    GA.check("the cancelled term <F1 F2>_0 is nonzero", _pgrade(_pmul(F1, F2), 0) != {})
    return True


def check_null_flux_has_only_transverse_data():
    n = GA.add(_g(0), _g(3))
    B1, B2 = _gauge_vec(_GAUGE_SEEDS[0], 2, n), _gauge_vec(_GAUGE_SEEDS[1], 2, n)
    GA.check("n.A = 0 identically for the gauge fields", all(_vdot(n, mv) == 0 for f in (B1, B2) for mv in f.values()))
    G1, G2 = _pgrade(_nabla(B1), 2), _pgrade(_nabla(B2), 2)
    flux = _pgrade(_pmul(_pconst(n), _symp(G1, B2, G2, B1)), 0)
    tr = _padd(_pgrade(_pmul(_perp(_pdn(B1, n)), _perp(B2)), 0), _pneg(_pgrade(_pmul(_perp(_pdn(B2, n)), _perp(B1)), 0)))
    GA.check("n.omega = d_n A1perp . A2perp - d_n A2perp . A1perp identically", _padd(flux, _pneg(tr)) == {} and flux != {})
    GA.check("n.F = d_n A identically in this gauge", _padd(_pgrade(_pmul(_pconst(n), G1), 1), _pneg(_pdn(B1, n))) == {})
    # the longitudinal coefficient a of A = a n + Aperp is present and drops out
    GA.check("the gauge fields have a nonzero n-component", any(_vdot(GA.sub(_g(0), _g(3)), mv) != 0 for mv in B1.values()))
    A1 = _poly_vec(_GAUGE_FREE_SEED, 2)
    GA.check("F is unchanged by A -> A + nabla chi", _pgrade(_nabla(_padd(A1, _pgrade(_nabla(_CHI), 1))), 2) == _pgrade(_nabla(A1), 2))
    return True


def check_null_energy_duality_and_helicity_phase():
    n, mn = GA.add(_g(0), _g(3)), GA.sub(_g(0), _g(3))
    I4 = _m4(_m4(_g(0), _g(1)), _m4(_g(2), _g(3)))
    J = _m4(_g(1), _g(2))
    ok = True
    for seed in range(3):
        Fb = {}
        for j, b in enumerate(itertools.combinations(range(4), 2)):
            c = F((j * 5 + 3 + seed * 2) % 7 - 3, 1 + (j + seed) % 2)
            if c:
                Fb[b] = c
        nF = _grade(_m4(n, Fb), 1)
        Ep = GA.add(GA.scal(nF.get((1,), 0), _g(1)), GA.scal(nF.get((2,), 0), _g(2)))
        Tn = GA.scal(F(-1, 2), _m4(_m4(Fb, n), Fb))
        ok = ok and _vdot(n, nF) == 0 and GA.eq(nF, GA.add(GA.scal(F(1, 2) * _vdot(mn, nF), n), Ep))
        ok = ok and _vdot(n, Tn) == -_vdot(Ep, Ep) and _vdot(n, Tn) > 0
    GA.check("n.(n.F) = 0, n.F = alpha n + Eperp, n.T(n) = -Eperp^2 > 0 (three bivectors)", ok)
    ok = True
    for a in (_g(1), _g(2), GA.add(GA.scal(3, _g(1)), GA.scal(-2, _g(2)))):
        f = _grade(_m4(n, a), 2)
        ok = ok and GA.eq(_m4(I4, f), _m4(f, J)) and GA.eq(_m4(f, J), _grade(_m4(n, _grade(_m4(a, J), 1)), 2))
        ok = ok and GA.eq(_m4(J, f), GA.neg(_m4(f, J)))
    GA.check("I4 (n ^ a) = (n ^ a) J = n ^ (a J) = -J (n ^ a) for transverse a", ok)
    R = GA.add(GA.sc(2), J)
    Rt = GA.reverse(R)
    E = GA.add(GA.scal(3, _g(1)), GA.scal(-2, _g(2)))
    eps = _m4(_g(1), E)
    GA.check("eps = g1 Eperp lies in span{1, J}", set(eps) <= {(), (1, 2)})
    GA.check("R Eperp R~ gives eps (R~)^2: the rotation about the generator is a phase on eps",
             GA.eq(_m4(_g(1), _m4(_m4(R, E), Rt)), _m4(eps, _m4(Rt, Rt))) and GA.eq(_m4(R, Rt), GA.sc(5)))
    return True


def check_two_channel_currents_on_a_window():
    premise("field-theory.imported-tower-limit")
    premise("hawking.current-commutator-exactly-edge-split")
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    L = 3
    T = _Tower(2 * L)
    idx = lambda a, k: a * L + (k - 1)
    Jc = lambda a, b, m: _current(T, idx, L, a, b, m)

    def rhs(a, b, c, d, m, n):
        out = {}
        if b == c:
            for k in range(1, L + 1):
                if 1 <= k + m <= L and 1 <= k + m + n <= L:
                    out = GA.add(out, T.bil(idx(a, k), idx(d, k + m + n)))
        if a == d:
            for l in range(1, L + 1):
                if 1 <= l + n <= L and 1 <= l + n + m <= L:
                    out = GA.sub(out, T.bil(idx(c, l), idx(b, l + n + m)))
        return out
    ok = all(GA.eq(T.comm(Jc(a, b, m), Jc(c, d, n)), rhs(a, b, c, d, m, n))
             for a, b, c, d in itertools.product((0, 1), repeat=4) for m in (-1, 0, 1) for n in (-1, 0, 1))
    GA.check("[J^ab_m, J^cd_n] = window identity, all a, b, c, d, |m|, |n| <= 1, L = 3", ok)
    # edge-clean basis states at depth 1 (level 1 filled, level 3 empty, level 2 free, in each channel)
    vals = []
    for s0, s1 in itertools.product((0, 1), repeat=2):
        P = T.proj([1, s0, 0, 1, s1, 0])
        for a, b in itertools.product((0, 1), repeat=2):
            X = T.comm(Jc(a, b, 1), Jc(b, a, -1))
            extra = GA.sub(Jc(a, a, 0), Jc(b, b, 0)) if a != b else {}
            vals.append(GA.eq(T.m(X, P), GA.add(P, T.m(extra, P))))
    GA.check("on the 4 edge-clean basis states [J^ab_1, J^ba_-1] = 1 + J^aa_0 - J^bb_0 (level one)", all(vals) and len(vals) == 16)
    # distinct generators: pair currents of disjoint modes commute
    GA.check("pair currents of disjoint channels commute", GA.is_zero(T.comm(Jc(0, 0, 1), Jc(1, 1, -1))))
    return True


def check_densities_are_helicity_zero_and_flips_helicity_one():
    premise("synthesis.light-ray-good-part-of-a-spinor-is-two-chirality-arrays")
    premise("field-theory.imported-tower-limit")
    L = 2
    T = _Tower(2 * L)
    idx = lambda a, k: a * L + (k - 1)
    Jc = lambda a, b, m: _current(T, idx, L, a, b, m)
    z = {0: GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), T.J)), 1: GA.add(GA.sc(F(3, 5)), GA.scal(F(4, 5), T.J))}
    U, Ui = GA.sc(1), GA.sc(1)
    for a in (0, 1):
        for k in range(1, L + 1):
            nn = T.num(idx(a, k))
            U = T.m(U, GA.add(GA.sc(1), T.m(GA.sub(z[a], GA.sc(1)), nn)))
            Ui = T.m(Ui, GA.add(GA.sc(1), T.m(GA.sub(T.star(z[a]), GA.sc(1)), nn)))
    GA.check("U is unitary: U U^-1 = 1, U* = U^-1", GA.eq(T.m(U, Ui), GA.sc(1)) and GA.eq(T.star(U), Ui))
    Ad = lambda X: T.m(U, X, Ui)
    GA.check("densities rho_+, rho_- (m = 1, 0) are invariant: helicity 0",
             all(GA.eq(Ad(Jc(a, a, m)), Jc(a, a, m)) for a in (0, 1) for m in (0, 1)))
    zz = T.m(z[0], z[0])
    GA.check("z_+^2 = (-7 + 24 J)/25", GA.eq(zz, GA.add(GA.sc(F(-7, 25)), GA.scal(F(24, 25), T.J))))
    GA.check("J^{+-}_m -> z_+^2 J^{+-}_m and J^{-+}_m -> z_-^2 J^{-+}_m (helicity +1, -1), m = -1, 0, 1",
             all(GA.eq(Ad(Jc(0, 1, m)), T.m(zz, Jc(0, 1, m))) and GA.eq(Ad(Jc(1, 0, m)), T.m(T.star(zz), Jc(1, 0, m)))
                 for m in (-1, 0, 1)))
    return True


def check_flip_defect_and_the_generator_bound():
    premise("field-theory.imported-tower-limit")
    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("synthesis.fluctuation-forms-of-the-tower-and-density-wave-bosons-of-the-null-vacuum")
    premise("synthesis.bulk-hadamard-states-restrict-to-the-generator-condition-on-flat-null-planes")
    # one copy, L = 3, bottom level filled
    L = 3
    T = _Tower(2 * L)
    idx = lambda a, k: a * L + (k - 1)
    Jc = lambda a, b, m: _current(T, idx, L, a, b, m)
    P = T.proj([1, 0, 0, 1, 0, 0])
    X = T.comm(Jc(0, 1, 0), Jc(1, 0, -1))
    GA.check("[J^{+-}_0, J^{-+}_-1] = J^{++}_-1 - J^{--}_-1 = 2 J^3_-1", GA.eq(X, GA.sub(Jc(0, 0, -1), Jc(1, 1, -1))))
    GA.check("one copy: ||[J^+_0, J^-_-1] Omega||^2 = 2", T.omega(P, T.m(T.star(X), X)) == 2)
    L4 = 4
    T4 = _Tower(2 * L4)
    i4 = lambda a, k: a * L4 + (k - 1)
    J4 = lambda a, b, m: _current(T4, i4, L4, a, b, m)
    P4 = T4.proj([1, 1, 0, 0, 1, 1, 0, 0])
    nr = []
    for m, n in ((1, -2), (0, -2), (-1, -1)):
        X2 = T4.comm(J4(0, 1, m), J4(1, 0, n))
        nr.append(T4.omega(P4, T4.m(T4.star(X2), X2)))
    GA.check("one copy, L = 4, depth 2: ||[J^+_m, J^-_n] Omega||^2 = 2|m + n| = 2, 4, 4", nr == [2, 4, 4])
    # N generators, L = 2: modes (g, a, k); M[g][h] weights c*_{g,+,k} c_{h,-,k+m}
    def run(Nf, Ms):
        L2 = 2
        T2 = _Tower(Nf * 2 * L2)
        ix = lambda f, a, k: (f * 2 + a) * L2 + (k - 1)
        P2 = T2.proj([1 if k == 1 else 0 for f in range(Nf) for a in (0, 1) for k in range(1, L2 + 1)])

        def flip(M, a, b, m):
            out = {}
            for f in range(Nf):
                for g in range(Nf):
                    if M[f][g]:
                        for k in range(1, L2 + 1):
                            if 1 <= k + m <= L2:
                                out = GA.add(out, GA.scal(M[f][g], T2.bil(ix(f, a, k), ix(g, b, k + m))))
            return out
        res = []
        for M in Ms:
            Mt = [[M[g][f] for g in range(Nf)] for f in range(Nf)]
            MMt = [[sum(M[f][h] * M[g][h] for h in range(Nf)) for g in range(Nf)] for f in range(Nf)]
            tr = sum(MMt[f][f] for f in range(Nf))
            fro = sum(MMt[f][g] ** 2 for f in range(Nf) for g in range(Nf))
            D = T2.comm(flip(M, 0, 1, 0), flip(Mt, 1, 0, -1))
            nrm = T2.omega(P2, T2.m(T2.star(D), D))
            cen = T2.omega(P2, T2.comm(flip(M, 0, 1, 1), flip(Mt, 1, 0, -1)))
            ident = all(M[f][g] == (1 if f == g else 0) for f in range(Nf) for g in range(Nf))
            res.append((nrm, fro, tr, cen, ident))
        return res
    r2 = run(2, ([[1, 0], [0, 1]], [[1, 1], [0, 1]], [[2, 0], [1, 1]]))
    GA.check("two generators: ||D Omega||^2 = 2 ||M M*||_F^2, central value tr(M M*), bound 2 tr^2 / 2 attained only at M = 1",
             all(n == 2 * fr and c == t and n * 2 >= 2 * t * t and ((n * 2 == 2 * t * t) == i) for n, fr, t, c, i in r2)
             and [x[0] for x in r2] == [4, 14, 56])
    r3 = run(3, ([[1, 0, 0], [0, 1, 0], [0, 0, 1]],))
    GA.check("three generators, uniform: ||D Omega||^2 = 6, central value 3: normalised defect 2/3", r3[0][0] == 6 and r3[0][3] == 3)
    # null translations along the generator: H = sum_k k n_{a,k}
    H = {}
    for a in (0, 1):
        for k in range(1, L + 1):
            H = GA.add(H, GA.scal(k, T.num(idx(a, k))))
    GA.check("[H, J^ab_m] = -m J^ab_m for all a, b and m = -2..2 (linear dispersion along the generator)",
             all(GA.eq(T.comm(H, Jc(a, b, m)), GA.scal(-m, Jc(a, b, m))) for a in (0, 1) for b in (0, 1) for m in range(-2, 3)))
    return True
