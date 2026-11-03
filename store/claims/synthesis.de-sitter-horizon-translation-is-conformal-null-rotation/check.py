"""The de Sitter horizon's affine translation is a conformal null rotation: exact checks in Cl(2,4).

Generators e0 (+1), e1, e2, e3 (-1), nu (+1), e- (-1); n_inf = nu + e-, n0 = (nu - e-)/2, <n0, n_inf> = 1,
X(x) = n0 + x - Q(x)/2 n_inf, P_a = (1/2) a n_inf. De Sitter: I = n_inf + (L/6) n0, sigma = <X, I> = 1 - L Q/12,
g = sigma^-2 eta. Future null n = e0 + e1, its partner m = (e0 - e1)/2, W = n_inf - (L/6) n0.
(1) n is a boundary point (<n, I> = 0); its light cone in the chart is the null plane N = {<x, n> = 0}; sigma is
    constant along each generator x0 + s n and equals 1 + L|x_perp|^2/12 there.
(2) The boost n^m is a de Sitter isometry (commutes with I), fixes the ray of n and the transverse plane, so N is
    a sheet of its Killing horizon; the static-patch rotations e2e3, e2W, e3W fix I, n and n^m and preserve
    lambda = s/sigma(x0) (tabulated images).
(3) T_a = 1 + (a/2) n I is a rotor and maps X(x0 + s n) to a multiple of X(x0 + (s + a sigma(x0)) n): lambda -> lambda + a
    on every generator; (1/2) n I = P_n + (L/12) n n0.
(4) Cone steps: rho^2 Ad(D_rho) Z - rho^4 P_e0 = e0 n0 (tabulated) and (2/rho^2) Ad(B_rho)(e0 n0) - l n0 =
    rho^-4 (e0 - e1) n0, l = e0 + e1 = n.
(5) Covariance: the rotor 1 - e1 e_W (L = 3, e_W = W) fixes I and carries n to 2 v*, v* = (e0 - e_W)/2 = X(2 e0)/4,
    the null vector of the store's static observer at x = 0.
(7) Gauge Theory Gravity on the flat background Cl(1,3): for the de Sitter field R(B) = (L/3)B the Ricci contraction
    is 3c b and the Weyl part vanishes; for the Schwarzschild field R = -(M/r^3)(1 - 3 Pi) the contraction vanishes and
    the Weyl part is R, nonzero, still after a rotation gauge; on N_n, Omega(n).n = 0 for Omega(a) = -(a ^ grad sigma)/sigma,
    so the lines are free-fall null worldlines, with a tabulated control off the plane.
(6) Controls: a non-null n gives a sigma that varies along the line; P_n alone shifts lambda by a/sigma, not uniformly;
    at L < 0 the coefficient of n n0 is negative.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
E = [GA.gen(i) for i in range(6)]
NINF = GA.add(E[4], E[5])
N0 = GA.scal(F(1, 2), GA.sub(E[4], E[5]))
NV = GA.add(E[0], E[1])
MV = GA.scal(F(1, 2), GA.sub(E[0], E[1]))


def _m(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ)
    return out


def _sand(R, x):
    return _m(R, x, GA.reverse(R))


def _ip(a, b):
    return GA.dot(a, b, SQ)


def _vec(c0, c1, c2, c3):
    return GA.add(GA.scal(c0, E[0]), GA.scal(c1, E[1]), GA.scal(c2, E[2]), GA.scal(c3, E[3]))


def _X(x):
    return GA.add(N0, x, GA.scal(-F(1, 2) * _ip(x, x), NINF))


def _I(L):
    return GA.add(NINF, GA.scal(L / 6, N0))


def _W(L):
    return GA.sub(NINF, GA.scal(L / 6, N0))


def _sigma(L, x):
    return 1 - L * _ip(x, x) / 12


def _decode(Y):
    """Y = lam X(y) for a point y: return (lam, y)."""
    lam = _ip(Y, NINF)
    y = {k: c / lam for k, c in Y.items() if k[0] < 4}
    GA.check("image is a multiple of a chart point", GA.eq(GA.scal(1 / lam, Y), _X(y)))
    return lam, y


def _on_generator(y, x0):
    """y = x0 + s n with the same transverse part: return s, else None."""
    s = y.get((0,), F(0))
    return s if GA.eq(GA.sub(y, GA.scal(s, NV)), x0) else None


BASES = [(F(2), F(1, 2)), (F(-3), F(4, 3)), (F(0), F(5))]   # transverse points (y2, y3)


def _x0(y2, y3):
    return _vec(F(0), F(0), y2, y3)


def check_boundary_point_and_null_plane():
    premise("mass.de-sitter-scale-frozen-point")
    table = {F(3): [F(33, 16), F(133, 36), F(29, 4)], F(3, 7): [F(129, 112), F(349, 252), F(53, 28)],
             F(12): [F(21, 4), F(106, 9), F(26)]}
    for L, sig in table.items():
        I = _I(L)
        GA.check("n is null and <n, I> = 0", _ip(NV, NV) == 0 and _ip(NV, I) == 0)
        for (y2, y3), sv in zip(BASES, sig):
            GA.check("sigma on the generator (tabulated)", _sigma(L, _x0(y2, y3)) == sv)
            x0 = _x0(y2, y3)
            GA.check("x0 on the plane", _ip(x0, NV) == 0)
            r2 = y2 * y2 + y3 * y3
            for s in [F(0), F(1), F(-7, 2)]:
                x = GA.add(x0, GA.scal(s, NV))
                GA.check("<X(x), n> = <x, n> = 0 on the generator", _ip(_X(x), NV) == 0)
                GA.check("<X(x), I> = sigma(x)", _ip(_X(x), I) == _sigma(L, x))
                GA.check("sigma constant on the generator, 1 + L r^2/12",
                         _sigma(L, x) == 1 + L * r2 / 12 and _sigma(L, x) > 0)
    return True


def check_killing_horizon_and_rotation_invariant_parameter():
    premise("synthesis.de-sitter-static-boost-frozen-point")
    L = F(3, 7)
    I, W = _I(L), _W(L)
    K = _m(NV, MV)
    GA.check("the boost n^m commutes with I", GA.eq(_m(K, I), _m(I, K)))
    rho = F(3)
    B = GA.add(GA.sc((rho + 1 / rho) / 2), GA.scal((rho - 1 / rho) / 2, _m(E[0], E[1])))
    GA.check("the boost rescales n", GA.eq(_sand(B, NV), GA.scal(F(1, 9), NV)))
    GA.check("the boost fixes the transverse directions", GA.eq(_sand(B, E[2]), E[2]) and GA.eq(_sand(B, E[3]), E[3]))
    GA.check("W orthogonal to I with Q(W) = -L/3", _ip(W, I) == 0 and _ip(W, W) == -L / 3)
    # Cayley-type rotors in the static-patch rotation planes (e2,e3), (e2,W), (e3,W)
    tabulated, moved = [], []
    e2w_images = [(F(7168, 6401), F(17878, 6401), F(3584, 6401)), (F(16128, 18241), F(-40362, 18241), F(21504, 18241)),
                  (F(1792, 1789), F(126, 1789), F(8960, 1789))]
    for (a, b) in [(E[2], E[3]), (E[2], W), (E[3], W)]:
        is_e2w = GA.eq(b, W) and GA.eq(a, E[2])
        Bv = _m(a, b)
        GA.check("rotation bivector commutes with I and with n^m", GA.eq(_m(Bv, I), _m(I, Bv)) and GA.eq(_m(Bv, K), _m(K, Bv)))
        R = GA.add(GA.sc(1), GA.scal(F(1, 3), Bv))
        nr = _m(R, GA.reverse(R))
        GA.check("R R~ is a positive scalar", set(nr) <= {()} and nr[()] > 0)
        c = nr[()]
        GA.check("the rotation fixes n", GA.eq(GA.scal(1 / c, _sand(R, NV)), NV))
        for (y2, y3) in BASES:
            x0 = _x0(y2, y3)
            lam0, x0p = _decode(GA.scal(1 / c, _sand(R, _X(x0))))
            GA.check("the bifurcation surface s = 0 goes to itself", _ip(x0p, NV) == 0 and x0p.get((0,), F(0)) == 0)
            moved.append(not GA.eq(x0p, x0))
            for s in [F(1), F(5, 2)]:
                lam, y = _decode(GA.scal(1 / c, _sand(R, _X(GA.add(x0, GA.scal(s, NV))))))
                base = GA.sub(y, GA.scal(y.get((0,), F(0)), NV))
                sp = y.get((0,), F(0))
                if is_e2w and s == 1:
                    want = e2w_images[BASES.index((y2, y3))]
                    GA.check("(e2, W) rotation image at s = 1 (tabulated)",
                             (sp, y.get((2,), F(0)), y.get((3,), F(0))) == want)
                GA.check("generators go to generators", _ip(base, NV) == 0 and GA.eq(GA.sub(y, GA.scal(sp, NV)), base))
                GA.check("lambda = s/sigma is preserved", sp / _sigma(L, base) == s / _sigma(L, x0))
                tabulated.append(sp / _sigma(L, base) == s / _sigma(L, x0))
    GA.check("the rotations move generators (the invariance test is not vacuous)", sum(moved) >= 6)
    return all(tabulated)


def check_uniform_translation_is_null_rotation():
    premise("mass.de-sitter-scale-frozen-point")
    premise("std-algebra.bivector-exponential")
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    shifts = {(F(3), F(2, 5)): [F(33, 40), F(133, 90), F(29, 10)], (F(3), F(-3)): [F(-99, 16), F(-133, 12), F(-87, 4)],
              (F(3, 7), F(2, 5)): [F(129, 280), F(349, 630), F(53, 70)], (F(3, 7), F(-3)): [F(-387, 112), F(-349, 84), F(-159, 28)]}
    for L in [F(3), F(3, 7)]:
        I = _I(L)
        nI = _m(NV, I)
        GA.check("n I = n^I is nilpotent", GA.is_zero(_m(nI, nI)))
        GA.check("n null and orthogonal to I, so n I is a pure bivector with zero square",
                 _ip(NV, NV) == 0 and _ip(NV, I) == 0 and _ip(I, I) != 0
                 and all(len(b) == 2 for b, cf in nI.items() if cf != 0) and not GA.is_zero(nI))
        GA.check("(1/2) n I = P_n + (L/12) n n0",
                 GA.eq(GA.scal(F(1, 2), nI), GA.add(GA.scal(F(1, 2), _m(NV, NINF)), GA.scal(L / 12, _m(NV, N0)))))
        for a in [F(2, 5), F(-3)]:
            T = GA.add(GA.sc(1), GA.scal(a / 2, nI))
            GA.check("T_a is a rotor", GA.eq(_m(T, GA.reverse(T)), GA.sc(1)))
            for (y2, y3) in BASES:
                x0 = _x0(y2, y3)
                for s in [F(0), F(7, 3)]:
                    lam, y = _decode(_sand(T, _X(GA.add(x0, GA.scal(s, NV)))))
                    sp = _on_generator(y, x0)
                    GA.check("T_a maps the generator to itself", sp is not None)
                    GA.check("lambda -> lambda + a uniformly", (sp - s) / _sigma(L, x0) == a)
                    GA.check("shift in s is a sigma (tabulated)", sp - s == shifts[(L, a)][BASES.index((y2, y3))])
    return True


def check_cone_reaches_the_conformal_null_rotation():
    premise("synthesis.positive-conformal-energy-gives-positive-null-translations")
    premise("mass.chart-form-spin-isomorphism")
    Z = _m(E[0], E[4])
    e0n0 = _m(E[0], N0)
    Pe0 = GA.scal(F(1, 2), _m(E[0], NINF))
    for rho, c4 in [(F(1, 2), F(1, 16)), (F(1, 4), F(1, 256)), (F(3), F(81))]:
        D = GA.add(GA.sc((rho + 1 / rho) / 2), GA.scal((rho - 1 / rho) / 2, _m(E[5], E[4])))
        GA.check("D_rho is a rotor", GA.eq(_m(D, GA.reverse(D)), GA.sc(1)))
        lhs = GA.sub(GA.scal(rho * rho, _sand(D, Z)), GA.scal(c4, Pe0))
        GA.check("rho^2 Ad(D) Z - rho^4 P_e0 = e0 n0 (rho^4 tabulated)", GA.eq(lhs, e0n0))
    for rho in [F(2), F(3)]:
        B = GA.add(GA.sc((rho + 1 / rho) / 2), GA.scal((rho - 1 / rho) / 2, _m(E[1], E[0])))
        GA.check("the boost fixes n0", GA.eq(_sand(B, N0), N0))
        rem = GA.sub(GA.scal(2 / (rho * rho), _sand(B, e0n0)), _m(NV, N0))
        GA.check("(2/rho^2) Ad(B) e0 n0 - n n0 = rho^-4 (e0 - e1) n0",
                 GA.eq(rem, GA.scal(1 / rho ** 4, _m(GA.sub(E[0], E[1]), N0))))
    return True


def check_covariance_to_the_static_observer_at_the_origin():
    premise("synthesis.cosmological-horizon-completed-pair")
    L = F(3)
    I, eW = _I(L), _W(L)
    GA.check("at L = 3, e_W = W is a unit vector of square -1", _ip(eW, eW) == -1)
    R = GA.sub(GA.sc(1), _m(E[1], eW))
    nr = _m(R, GA.reverse(R))
    GA.check("R R~ = 2", GA.eq(nr, GA.sc(2)))
    GA.check("R fixes I", GA.eq(GA.scal(F(1, 2), _sand(R, I)), I))
    vstar = GA.scal(F(1, 2), GA.sub(E[0], eW))
    img = GA.scal(F(1, 2), _sand(R, NV))
    GA.check("R carries n to 2 v* of the origin's static patch", GA.eq(img, GA.scal(2, vstar)))
    GA.check("v* is the future endpoint: v* = X(2 e0)/4", GA.eq(vstar, GA.scal(F(1, 4), _X(GA.scal(2, E[0])))))
    return True


def check_controls():
    premise("mass.de-sitter-scale-frozen-point")
    L = F(3, 7)
    I = _I(L)
    nb = _vec(F(1), F(2), F(0), F(0))           # timelike-ish, not null
    x0 = _vec(F(2), F(1), F(1), F(0))
    GA.check("control: for a non-null direction sigma varies along the line (tabulated 13/14, 29/28)",
             _sigma(L, x0) == F(13, 14) and _sigma(L, GA.add(x0, nb)) == F(29, 28))
    T = GA.add(GA.sc(1), GA.scal(F(1, 2), _m(NV, NINF)))     # P_n alone
    vals = []
    for (y2, y3) in BASES:
        x = _x0(y2, y3)
        lam, y = _decode(_sand(T, _X(x)))
        vals.append(_on_generator(y, x) / _sigma(L, x))
    GA.check("control: P_n alone shifts lambda by 1/sigma (tabulated), not uniformly",
             vals == [F(112, 129), F(252, 349), F(28, 53)])
    Lneg = F(-3)
    GA.check("control: at L < 0 the n n0 coefficient L/12 is negative", Lneg / 12 < 0)
    return True


# ---- Gauge Theory Gravity checks on the flat background Cl(1,3) ----
SQ4 = (1, -1, -1, -1)
G4 = [GA.gen(i) for i in range(4)]
RECIP4 = [G4[0], GA.neg(G4[1]), GA.neg(G4[2]), GA.neg(G4[3])]
PAIRS4 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def _m4(*xs):
    out = xs[0]
    for y in xs[1:]:
        out = GA.mul(out, y, SQ4)
    return out


def _wedge4(a, b):
    return GA.scal(F(1, 2), GA.sub(_m4(a, b), _m4(b, a)))


def _grade(x, k):
    return {b: c for b, c in x.items() if len(b) == k}


def _contract(R, b):
    """d_a . R(a ^ b) in the orthonormal frame."""
    out = {}
    for mu in range(4):
        out = GA.add(out, _grade(_m4(RECIP4[mu], R(_wedge4(G4[mu], b))), 1))
    return out


def _weyl(R, a, b):
    """W(a^b) = R(a^b) - Sch(a)^b - a^Sch(b), Sch(a) = (R(a) - a R/6)/2 (Fact (v))."""
    scal_curv = sum((_grade(_m4(RECIP4[mu], _contract(R, G4[mu])), 0).get((), F(0)) for mu in range(4)), F(0))
    def sch(v):
        return GA.scal(F(1, 2), GA.sub(_contract(R, v), GA.scal(scal_curv / 6, v)))
    return GA.sub(R(_wedge4(a, b)), GA.add(_wedge4(sch(a), b), _wedge4(a, sch(b))))


def _proj_radial(B):          # onto span{e0e1, e2e3} = span{sigma_r, I sigma_r}
    return {k: c for k, c in B.items() if k in [(0, 1), (2, 3)]}


def check_dilation_field_against_schwarzschild_field():
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("singularity.curvature-gauge-field-exact-shape-decoupling")
    premise("mass.de-sitter-scale-frozen-point")
    # de Sitter: R(B) = (L/3) B; contraction 3c b (tabulated), Weyl part zero
    for L, three_c in [(F(3), F(3)), (F(3, 7), F(3, 7))]:
        c = L / 3
        R = lambda B, c=c: GA.scal(c, B)
        GA.check("de Sitter Ricci contraction is 3c b (tabulated)",
                 all(GA.eq(_contract(R, b), GA.scal(three_c, b)) for b in G4))
        GA.check("de Sitter Weyl part vanishes",
                 all(GA.is_zero(_weyl(R, G4[i], G4[j])) for (i, j) in PAIRS4))
    # Schwarzschild: R = -(M/r^3) S, S = 1 - 3 Pi; at M/r^3 = 2/5
    k = F(2, 5)
    S = lambda B: GA.sub(B, GA.scal(3, _proj_radial(B)))
    R = lambda B: GA.scal(-k, S(B))
    GA.check("Schwarzschild Ricci contraction vanishes", all(GA.is_zero(_contract(R, b)) for b in G4))
    eig = {(0, 1): F(-2), (2, 3): F(-2), (0, 2): F(1), (0, 3): F(1), (1, 2): F(1), (1, 3): F(1)}
    for (i, j), ev in eig.items():
        Bv = _wedge4(G4[i], G4[j])
        GA.check("S eigenvalue on e%d e%d (tabulated)" % (i, j), GA.eq(S(Bv), GA.scal(ev, Bv)))
        GA.check("Schwarzschild Weyl part equals R and is nonzero",
                 GA.eq(_weyl(R, G4[i], G4[j]), R(Bv)) and not GA.is_zero(R(Bv)))
    # rotation gauge covariance of the Weyl part's vanishing: conjugate by a rotor
    U = GA.add(GA.sc(F(5, 4)), GA.scal(F(3, 4), _m4(G4[0], G4[2])))   # U U~ = 25/16 - 9/16 = 1
    GA.check("U is a rotor", GA.eq(_m4(U, GA.reverse(U)), GA.sc(1)))
    RU = lambda B: _m4(U, R(_m4(GA.reverse(U), B, U)), GA.reverse(U))
    GA.check("the gauge-transformed Schwarzschild Weyl part is still nonzero",
             not GA.is_zero(_weyl(RU, G4[0], G4[1])) and GA.is_zero(_contract(RU, G4[3])))
    return True


def check_free_fall_lines_on_the_horizon():
    premise("synthesis.imported-gtg-dictionary")
    premise("mass.de-sitter-scale-frozen-point")
    L = F(3, 7)
    n4 = GA.add(G4[0], G4[1])
    def grad_sigma(x):
        return GA.scal(-L / 6, x)
    def omega_dot(x, a, v):      # Omega(a).v with Omega(a) = -(a ^ grad sigma)/sigma
        sig = 1 - L * GA.dot(x, x, SQ4) / 12
        B = GA.scal(-1 / sig, _wedge4(a, grad_sigma(x)))
        return GA.scal(F(1, 2), GA.sub(_m4(B, v), _m4(v, B)))
    on = [GA.add(GA.scal(F(2), G4[2]), GA.scal(F(1, 2), G4[3])), GA.add(GA.scal(F(-3), G4[2]), GA.scal(F(5), n4))]
    for x in on:
        GA.check("x on the plane", GA.dot(x, n4, SQ4) == 0)
        GA.check("Omega(n).n = 0 on the plane, so the lines are free-fall null worldlines",
                 GA.is_zero(omega_dot(x, n4, n4)))
    off = GA.add(G4[0], GA.scal(F(2), G4[2]))     # <x, n> = 1 off the plane
    sig = 1 - L * GA.dot(off, off, SQ4) / 12
    GA.check("control: off the plane Omega(n).n = (L/6)<n,x>/sigma n (tabulated 1/14 / sigma)",
             GA.eq(omega_dot(off, n4, n4), GA.scal(F(1, 14) / sig, n4)))
    # torsion-free: sum_mu e^mu ^ D_{e_mu}(sigma b) = 0 for constant b, D_a v = (a.grad sigma) b + sigma Omega(a).b
    def torsion(x, extra=None):
        sig = 1 - L * GA.dot(x, x, SQ4) / 12
        g = grad_sigma(x)
        for b in G4:
            tot = _wedge4(g, b)
            for mu in range(4):
                B = GA.scal(-1 / sig, _wedge4(G4[mu], g))
                if extra is not None:
                    B = GA.add(B, extra(G4[mu]))
                Bb = GA.scal(F(1, 2), GA.sub(_m4(B, b), _m4(b, B)))
                tot = GA.add(tot, _wedge4(RECIP4[mu], GA.scal(sig, Bb)))
            GA.check("torsion-free for b = basis vector", GA.is_zero(tot))
    for x in on + [off]:
        torsion(x)
    bad = lambda a: _wedge4(a, G4[2])
    sig = 1 - L * GA.dot(on[0], on[0], SQ4) / 12
    tot = {}
    for mu in range(4):
        B = GA.add(GA.scal(-1 / sig, _wedge4(G4[mu], grad_sigma(on[0]))), bad(G4[mu]))
        Bb = GA.scal(F(1, 2), GA.sub(_m4(B, G4[0]), _m4(G4[0], B)))
        tot = GA.add(tot, _wedge4(RECIP4[mu], GA.scal(sig, Bb)))
    tot = GA.add(tot, _wedge4(grad_sigma(on[0]), G4[0]))
    GA.check("control: adding a torsion term a ^ e2 to Omega breaks the torsion condition", not GA.is_zero(tot))
    # the parameter lambda = s/sigma: finite difference of x(lambda) = x_perp + sigma lambda n, read through hb^-1
    xp = on[0]
    s_perp = 1 - L * GA.dot(xp, xp, SQ4) / 12
    for lam in [F(0), F(3, 2)]:
        x1 = GA.add(xp, GA.scal(s_perp * lam, n4))
        x2 = GA.add(xp, GA.scal(s_perp * (lam + 1), n4))
        dx = GA.sub(x2, x1)
        sig_here = 1 - L * GA.dot(x1, x1, SQ4) / 12
        GA.check("hb^-1(dx/dlambda) = n with sigma evaluated at the point", GA.eq(GA.scal(1 / sig_here, dx), n4))
    return True
