"""synthesis.c-loc-entropy-clause-curvature-independent-density: exact checks.

Tangent Minkowski space as the vector part of GA with squares (-1, 1, 1, 1). Reference horizon data at
p: the null ray of l0 = e0 + e1, its partner n0 = e0 - e1, and the edge plane P0 = span(e2, e3).
check_lorentz_transitive_on_horizon_data: for future null l, n with rational components (Pythagorean
quadruples, and two positive multiples of l0), at most two reflections in spacelike vectors,
v1 = l0 - l (skipped when l is a positive multiple of l0, where v1 would be null) and v2 = n0' - mu n,
map l0 to a positive multiple of l and n0 to mu n with mu > 0, composed with the reflection in e2 when
only one is used; the images of e2, e3 are orthonormal and orthogonal to l and n, and e0 goes to a
future timelike vector. All 70 ordered non-parallel pairs, 14 of them with l a multiple of l0.
check_boost_rescales_ray_fixes_plane: two reflections in the timelike unit vectors e0 and
c e0 + s e1 give a boost that rescales l0 by (c + s)^2 and n0 by (c - s)^2 and fixes e2 and e3.
check_eta_from_temperature: kappa(M) from f'(2M)/2 as a rational function, 1/T = 2 pi/kappa = 8 pi M,
S = 4 pi M^2 with dS/dM = 1/T and S(0) = 0, A = 16 pi M^2, S/A = 1/4 identically; a period c times the
regular one gives c/4 (control); de Sitter pi N^2/(4 pi N^2) = 1/4; a Kerr case with rational r_+;
eta = 4 pi nu <s> equals 1/4 iff 16 pi nu <s> = 1 (pi formal).
check_clausius_forces_constant_density: order counting in the affine extent of the patch.
"""
from fractions import Fraction as F
import GA
from GA import RF
from tp_premise import premise

SQ = (-1, 1, 1, 1)
# Sample patch data (eta(0) = e, g = k.grad(eta), area curvature c, heat q, temperature T) for (iv).
CLAUSIUS_SAMPLES = [(F(1, 4), F(2), F(3), F(5, 7), F(1, 3)), (F(1, 4), F(0), F(-1), F(2), F(1, 2))]
# Sample null vectors (t, x, y, z) for the spanning argument in (iv).
SPAN_NULLS = [[1, 1, 0, 0], [1, -1, 0, 0], [1, 0, 1, 0], [1, 0, 0, 1]]


def setup_lorentz():
    premise("synthesis.imported-jacobson-clausius-1995")


def setup_values():
    premise("synthesis.quarter-from-temperature")
    premise("synthesis.de-sitter-entropy-pi-n-squared")
    premise("synthesis.imported-kerr-surface-gravity-entropy")
    premise("synthesis.clausius-route-newton-constant-is-residue")


def vec(c):
    return {(i,): F(c[i]) for i in range(4) if c[i] != 0}


def comps(x):
    return [x.get((i,), F(0)) for i in range(4)]


def ip(x, y):
    return GA.dot(x, y, SQ)


def reflect(v, x):
    """Reflection of x in the hyperplane orthogonal to the non-null vector v."""
    return GA.sub(x, GA.scal(2 * ip(x, v) / ip(v, v), v))


L0 = vec([1, 1, 0, 0])
N0 = vec([1, -1, 0, 0])
E0, E2, E3 = vec([1, 0, 0, 0]), vec([0, 0, 1, 0]), vec([0, 0, 0, 1])

# future null vectors from Pythagorean quadruples t^2 = x^2 + y^2 + z^2, and two positive multiples of
# l0 (the case in which the first reflection would be in a null vector and is skipped)
NULLS = [[3, 2, 2, 1], [7, 2, 3, 6], [9, 4, 4, 7], [15, 2, 5, 14], [3, -1, 2, -2], [11, -2, 6, 9],
         [9, -8, 1, 4], [2, 2, 0, 0], [3, 3, 0, 0]]


def positive_multiple(x, y):
    """x = c y with c > 0 (y nonzero)."""
    cx, cy = comps(x), comps(y)
    i = next(j for j in range(4) if cy[j] != 0)
    c = cx[i] / cy[i]
    return c > 0 and all(cx[j] == c * cy[j] for j in range(4))


def check_lorentz_transitive_on_horizon_data():
    setup_lorentz()
    GA.check("reference data: l0, n0 null, l0.n0 = -2",
             ip(L0, L0) == 0 and ip(N0, N0) == 0 and ip(L0, N0) == -2)
    count = 0
    skipped_first = 0
    for a in NULLS:
        for b in NULLS:
            l, n = vec(a), vec(b)
            if ip(l, n) == 0:
                continue                      # parallel rays: not a horizon pair
            GA.check("null inputs", ip(l, l) == 0 and ip(n, n) == 0)
            x = [L0, N0, E2, E3, E0]
            nref = 0
            if ip(L0, l) != 0:
                v1 = GA.sub(L0, l)
                GA.check("v1 spacelike", ip(v1, v1) > 0)
                x = [reflect(v1, y) for y in x]
                nref += 1
                GA.check("l0 goes to l exactly", GA.eq(x[0], l))
            else:
                skipped_first += 1
            GA.check("l0 goes to a positive multiple of l", positive_multiple(x[0], l))
            mu = ip(x[1], l) / ip(n, l)
            GA.check("mu > 0 (future to future)", mu > 0)
            v2 = GA.sub(x[1], GA.scal(mu, n))
            if not GA.is_zero(v2):
                GA.check("v2 orthogonal to l", ip(v2, l) == 0)
                GA.check("v2 spacelike", ip(v2, v2) > 0)
                x = [reflect(v2, y) for y in x]
                nref += 1
            if nref == 1:
                # compose with the reflection in e2 applied first (it fixes l0, n0 and the plane
                # <e2, e3> as a set), so that the map is a product of two spacelike reflections
                x = [x[0], x[1], GA.neg(x[2]), x[3], x[4]]
            GA.check("ray of l kept by the second reflection", positive_multiple(x[0], l))
            GA.check("n0 goes to mu n", GA.eq(x[1], GA.scal(mu, n)))
            f2, f3 = x[2], x[3]
            GA.check("edge plane orthonormal",
                     ip(f2, f2) == 1 and ip(f3, f3) == 1 and ip(f2, f3) == 0)
            GA.check("edge plane orthogonal to l and n",
                     all(ip(f, g) == 0 for f in (f2, f3) for g in (l, n)))
            GA.check("time orientation kept", ip(x[4], x[4]) == -1 and comps(x[4])[0] > 0)
            count += 1
    GA.check("all 70 ordered non-parallel pairs mapped", count == 70)
    GA.check("14 pairs with l a positive multiple of l0", skipped_first == 14)
    return True


def check_boost_rescales_ray_fixes_plane():
    setup_lorentz()
    for (c, s) in ((F(5, 4), F(3, 4)), (F(13, 12), F(5, 12)), (F(17, 8), F(-15, 8))):
        u = vec([c, s, 0, 0])
        GA.check("unit timelike", ip(u, u) == -1)
        def boost(y):
            return reflect(u, reflect(E0, y))
        GA.check("l0 rescaled by (c + s)^2", GA.eq(boost(L0), GA.scal((c + s) ** 2, L0)))
        GA.check("n0 rescaled by (c - s)^2", GA.eq(boost(N0), GA.scal((c - s) ** 2, N0)))
        GA.check("edge plane fixed pointwise", GA.eq(boost(E2), E2) and GA.eq(boost(E3), E3))
        GA.check("ray rescaling nontrivial", (c + s) ** 2 != 1)
    return True


def kappa_of(m):
    r = RF.var()
    f = RF.const(1) - RF.const(2 * m) / r
    GA.check("horizon at 2M", f.eval(2 * m) == 0)
    return f.deriv().eval(2 * m) / 2


def check_eta_from_temperature():
    setup_values()
    M = RF.var()
    GA.check("kappa at M = 1, 5/2, 7/3", [kappa_of(m) for m in (F(1), F(5, 2), F(7, 3))]
             == [F(1, 4), F(1, 10), F(3, 28)])
    # kappa as a rational function of M: f'(r) = 2M/r^2 at r = 2M, halved
    kappaM = (RF.const(2) * M / ((RF.const(2) * M) * (RF.const(2) * M))) / RF.const(2)
    GA.check("kappa(M) = 1/(4M)", kappaM.eqrf(RF.const(1) / (RF.const(4) * M)))
    invT = RF.const(2) / kappaM                  # 1/T = 2 pi/kappa: coefficient of pi
    GA.check("1/T = 8 pi M", invT.eqrf(RF.const(8) * M))
    S = RF.const(4) * M * M                      # candidate antiderivative, coefficient of pi
    GA.check("dS/dM = 1/T", S.deriv().eqrf(invT))
    GA.check("S(0) = 0", S.eval(F(0)) == 0)
    A = RF.const(16) * M * M                     # A = 4 pi (2M)^2, coefficient of pi
    ratio = S / A
    GA.check("S(5/2) = 25 pi, A(5/2) = 100 pi", S.eval(F(5, 2)) == 25 and A.eval(F(5, 2)) == 100)
    GA.check("S/A = 1/4 along the family", ratio.eqrf(RF.const(F(1, 4))))
    # control: a period p = c (2 pi/kappa) in place of the regular one gives S/A = c/4
    for c in (F(1, 2), F(3)):
        Sc = RF.const(4 * c) * M * M
        GA.check("control: dS/dM = c/T", Sc.deriv().eqrf(RF.const(c) * invT))
        GA.check("control ratio c/4", (Sc / A).eqrf(RF.const(c / 4)))
    # de Sitter: S = pi N^2 and A = 4 pi N^2, coefficients of pi N^2
    for Nh in (F(3), F(10), F(7, 2)):
        S_dS = Nh * Nh                           # pi N^2, coefficient of pi
        A_dS = 4 * Nh * Nh                       # 4 pi R_h^2 with R_h = N Planck lengths
        GA.check("de Sitter ratio 1/4", S_dS / A_dS == F(1, 4))
    GA.check("de Sitter at N = 3: S = 9 pi, A = 36 pi", (F(3) ** 2, 4 * F(3) ** 2) == (9, 36))
    # Kerr (imported S = A_+/4): M = 5, a = 3 gives r_+ = M + sqrt(M^2 - a^2) = 9 and
    # A_+ = 4 pi (r_+^2 + a^2) = 360 pi, S = 90 pi
    Mk, ak = F(5), F(3)
    rp = Mk + 4                                  # sqrt(25 - 9) = 4
    GA.check("r_+ solves r^2 - 2Mr + a^2 = 0", rp * rp - 2 * Mk * rp + ak * ak == 0)
    Ap = 4 * (rp * rp + ak * ak)
    GA.check("Kerr A_+ = 360 pi and S/A_+ = 1/4", Ap == 360 and (Ap / 4) / Ap == F(1, 4))
    # count form: eta = 4 pi nu <s>; with nu = a/pi (1-nat) and <s> = b: eta = 4ab
    for a in (F(1, 16), F(1, 8)):
        for b in (F(1), F(1, 2)):
            GA.check("eta = 1/4 iff 16 pi nu <s> = 1", (4 * a * b == F(1, 4)) == (16 * a * b == 1))
    return True


def check_clausius_forces_constant_density():
    """(iv): polynomials in the affine extent l0 of the patch (GA.RF in l0). Per unit area at p:
    area factor 1 + c l0^2 (zero expansion at p), heat q l0^2 (second order), density
    eta(l0) = e + g l0 with g = k.grad(eta). T dS - dQ has first-order coefficient -T g, so the
    Clausius relation at first order forces g = 0; four null vectors whose components are
    linearly independent then force grad(eta) = 0."""
    premise("synthesis.imported-jacobson-clausius-1995")
    lam = RF.var()
    for (e, g, c, q, T) in CLAUSIUS_SAMPLES:
        area = RF.const(1) + RF.const(c) * lam * lam
        eta = RF.const(e) + RF.const(g) * lam
        dS = RF.const(e) - eta * area             # entropy at 0 minus entropy at l0
        dQ = RF.const(q) * lam * lam
        defect = RF.const(T) * dS - dQ
        GA.check("no zeroth-order term", defect.eval(F(0)) == 0)
        GA.check("first-order coefficient is -T g", defect.deriv().eval(F(0)) == -T * g)
    # null vectors (t, x, y, z) with t^2 = x^2 + y^2 + z^2 spanning R^4: k.grad = 0 for all => grad = 0
    ks = SPAN_NULLS
    GA.check("the spanning vectors are null", all(sum(s * v * v for s, v in zip(SQ, k)) == 0 for k in ks))
    GA.check("four null vectors span (rank 4)", GA.mat_rank([[F(v) for v in k] for k in ks]) == 4)
    return True
