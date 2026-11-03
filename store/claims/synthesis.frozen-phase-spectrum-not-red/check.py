"""synthesis.frozen-phase-spectrum-not-red: exact checks.

Ambient Cl(2,4) with generators e0..e3 (spacetime, +,-,-,-), e4 = e_+ (+1), e5 = e_- (-1);
n0 = (e_+ + e_-)/2, ninf = e_+ - e_-, <n0, ninf> = 1, X(x) = n0 + x - Q(x)/2 ninf, the
conventions of mass.de-sitter-scale-frozen-point. All arithmetic is over Fractions.

(1) The flat-slicing frozen point I_fs = H e0 has <I,I> = H^2 = Lambda/3 and scale function
    sigma(x) = <X(x), I_fs> = H x0; it is carried to the chart frozen point
    I_Lambda = ninf + (Lambda/6) n0 by an explicit ambient rotation (two reflections).
(2) The ten bivectors orthogonal to e0 (rotations, translations, special conformal maps,
    dilatation of the chart) commute with I_fs; the seven that preserve the null ray of ninf
    (rotations, spatial translations, dilatation) form the slicing's symmetry group; time
    translation does not fix I_fs.
(3) The dilatation rotor R = 5/4 + (3/4) n0^ninf (rapidity ln 4) maps X(x) to 4 X(x/4),
    and spatial translation rotors map X(x) to X(x + a), both fixing e0.
(4) The dictionary weight solves the Klein-Gordon indicial equation Delta^2 - 3 Delta + m^2/H^2 = 0 at
    Delta = -w (real and principal-series weights); the scaling lemma P(lam k) = lam^(-3-2w) P(k) is
    tested exactly on regulated homogeneous G = |x|^(2n); a weight-w boundary two-point function forces
    Delta^2(k) proportional to k^(-2w);
    with the dictionary m^2 = -w(w+3) H^2, the leading late-time weight of every scalar in the
    principal, complementary or massless series gives n_s - 1 = -2 w_lead >= 0, the exceptional
    series' shadows give n_s - 1 = -2k <= -2, and the measured n_s = 0.9649 needs w = 351/20000,
    m^2/H^2 = -21183201/400000000 < 0.
"""
from fractions import Fraction as F
from GA import mul, add, sub, scal, sc, gen, reverse, eq, commutes, QI
from tp_premise import premise

SQ = (1, -1, -1, -1, 1, -1)
HS = [F(1), F(1, 2), F(3), F(2, 7)]


def dot(a, b):
    return add(mul(a, b, SQ), mul(b, a, SQ)).get((), F(0)) / 2


def wedge(a, b):
    return scal(F(1, 2), sub(mul(a, b, SQ), mul(b, a, SQ)))


def sandwich(R, v):
    return mul(mul(R, v, SQ), reverse(R), SQ)


n0 = scal(F(1, 2), add(gen(4), gen(5)))
ninf = sub(gen(4), gen(5))
E = [gen(i) for i in range(4)]


def vec(x):
    out = {}
    for i, c in enumerate(x):
        out = add(out, scal(F(c), E[i]))
    return out


def Q(x):
    return x[0] * x[0] - x[1] * x[1] - x[2] * x[2] - x[3] * x[3]


def X(x):
    return add(add(n0, vec(x)), scal(-Q(x) / 2, ninf))


POINTS = [(F(1), F(0), F(0), F(0)), (F(2), F(1), F(-3), F(1, 2)), (F(-1, 3), F(5), F(2), F(7)),
          (F(3, 4), F(-1, 2), F(0), F(1))]


def check_frozen_point_and_slicing():
    premise("mass.de-sitter-scale-frozen-point")
    premise("dark-matter.imported-frozen-point-de-sitter-radius")
    assert dot(n0, ninf) == 1 and dot(n0, n0) == 0 and dot(ninf, ninf) == 0
    for h in HS:
        L = 3 * h * h
        Ifs = scal(h, E[0])
        IL = add(ninf, scal(L / 6, n0))
        assert dot(Ifs, Ifs) == h * h == dot(IL, IL)
        for x in POINTS:
            assert dot(X(x), X(x)) == 0
            assert dot(X(x), Ifs) == h * x[0]               # sigma = H x0: the flat slicing
        # explicit rotation carrying I_Lambda to I_fs: reflect in u = I_Lambda - I_fs, then in e1
        u = sub(IL, Ifs)
        assert dot(u, u) == 2 * h * h
        uinv = scal(1 / dot(u, u), u)
        refl_u = lambda v: scal(F(-1), mul(mul(u, v, SQ), uinv, SQ))
        e1inv = scal(F(-1), E[1])                            # e1^2 = -1
        refl_e1 = lambda v: scal(F(-1), mul(mul(E[1], v, SQ), e1inv, SQ))
        assert eq(refl_e1(refl_u(IL)), Ifs)
        # the composite is a rotation (two reflections) and an isometry on a basis
        basis = [gen(i) for i in range(6)]
        for a in basis:
            for b in basis:
                assert dot(refl_e1(refl_u(a)), refl_e1(refl_u(b))) == dot(a, b)
    return True


def check_stabiliser_contains_slicing_group():
    premise("dark-matter.imported-frozen-point-de-sitter-radius")
    e0 = E[0]
    rot = [wedge(E[i], E[j]) for i in (1, 2, 3) for j in (1, 2, 3) if i < j]
    trans = [wedge(ninf, E[i]) for i in (1, 2, 3)]
    special = [wedge(n0, E[i]) for i in (1, 2, 3)]
    dil = wedge(n0, ninf)
    gens = rot + trans + special + [dil]
    assert len(gens) == 10
    for g in gens:
        assert commutes(g, e0, SQ)                           # all ten fix I_fs = H e0
    # the null ray of ninf (the slicing): preserved by rotations, translations, dilatation
    def bracket(g, v):
        return sub(mul(g, v, SQ), mul(v, g, SQ))
    for g in rot + trans:
        assert bracket(g, ninf) == {}
    b = bracket(dil, ninf)
    assert eq(b, scal(F(2), ninf)) or eq(b, scal(F(-2), ninf))  # scales the ray
    for g in special:
        bb = bracket(g, ninf)
        assert bb != {} and dot(bb, n0) == 0 and dot(bb, ninf) == 0   # moves the ray off itself
    # time translation does not fix I_fs: the slicing selects a time
    assert not commutes(wedge(ninf, e0), e0, SQ)
    return True


def check_dilatation_and_translation_rotors():
    premise("mass.de-sitter-scale-frozen-point")
    N = wedge(n0, ninf)
    assert mul(N, N, SQ) == sc(F(1))                         # unit boost in the (n0, ninf) plane
    for sgn in (F(1), F(-1)):
        R = add(sc(F(5, 4)), scal(sgn * F(3, 4), N))        # cosh(s/2), sinh(s/2) at e^s = 4
        assert mul(R, reverse(R), SQ) == sc(F(1))
        assert eq(sandwich(R, E[0]), E[0])                   # fixes the frozen point H e0
        lam = None
        for cand in (F(4), F(1, 4)):
            if all(eq(sandwich(R, X(x)), scal(cand, X(tuple(c / cand for c in x)))) for x in POINTS):
                lam = cand
        assert lam is not None                               # X(x) -> lam X(x/lam): dilatation
        # sigma scales with the point: H x0 -> H x0 / lam, and g = eta / sigma^2 is invariant
        for x in POINTS:
            for v in POINTS:
                if x[0] != 0:
                    y = tuple(c / lam for c in x)
                    w_ = tuple(c / lam for c in v)
                    assert Q(w_) / (y[0] * y[0]) == Q(v) / (x[0] * x[0])
    for a in [(F(0), F(1), F(2), F(-1)), (F(0), F(1, 3), F(0), F(5))]:
        T = add(sc(F(1)), scal(F(1, 2), mul(ninf, vec(a), SQ)))
        assert mul(T, reverse(T), SQ) == sc(F(1))
        assert eq(sandwich(T, E[0]), E[0])
        for x in POINTS:
            xa = tuple(x[i] + a[i] for i in range(4))
            assert eq(sandwich(T, X(x)), X(xa)) or eq(sandwich(reverse(T), X(x)), X(xa))
    return True


def check_index_from_weight():
    premise("standard-model.imported-frozen-point-dictionary")
    premise("mass.weight-polynomial-two-series")
    premise("mass.imported-unitary-representations-de-sitter-group")
    mu = lambda w: -w * (w + 3)                              # m^2 / H^2
    # (a) the dictionary weight is the late-time falloff exponent: substituting phi = x0^Delta into
    # phi'' - (2/x0) phi' + (mu/x0^2) phi = 0 (flat slicing, k -> 0) gives the coefficient
    # Delta(Delta-1) - 2 Delta + mu, which must vanish exactly at Delta = -w for both dictionary roots
    def indicial(D, m2):
        return D * (D - 1) - 2 * D + m2
    for w in [F(k, 7) for k in range(-25, 8)]:
        m2 = mu(w)
        for root in (w, -3 - w):
            D = -root
            assert indicial(D, m2) == D * D - 3 * D + m2 == 0
        assert indicial(-w + F(1, 3), m2) != 0                # a shifted exponent is not a root
    for nu in (F(0), F(1, 2), F(7, 3), F(40)):                   # principal series, w = -3/2 + i nu
        for s in (1, -1):
            w = QI(F(-3, 2), s * nu)
            m2 = -(w * (w + 3))
            assert m2.im == 0 and m2.re == F(9, 4) + nu * nu
            D = -w
            assert D * (D - 1) - 2 * D + m2 == QI(0)
            assert D.re == F(3, 2)                               # both roots share Re Delta = 3/2
    # (b) the scaling lemma with w in the exponent, tested exactly on G(x) = |x|^(2n) (weight w = n):
    # G(x/lam) = lam^(-2n) G(x), and with a Gaussian regulator e^(-a|x|^2) the 3D Fourier transform is
    # P_a(k) = (pi/a)^(3/2) p_n(s) e^(-s/4a), s = k^2, p_0 = 1, p_(n+1) = -Lap(p_n) with the radial
    # Laplacian Lap = 4 s d^2/ds^2 + 6 d/ds acting on p e^(-s/4a). The substitution x = y/lam gives
    # P_a(lam k) = lam^(-3-2n) P_(a/lam^2)(k); after cancelling the common exponential and
    # (pi/a)^(3/2) lam^3 = (pi lam^2/a)^(3/2) this is the polynomial identity
    # p_n^(a)(lam^2 s) = lam^(-2n) p_n^(a/lam^2)(s), checked coefficient by coefficient.
    def pderiv_(p):
        return [i * p[i] for i in range(1, len(p))] or [F(0)]
    def padd_(p, q):
        n = max(len(p), len(q))
        return [(p[i] if i < len(p) else 0) + (q[i] if i < len(q) else 0) for i in range(n)]
    def pscal_(c, p):
        return [c * x for x in p]
    def shift_(p):                                               # multiply by s
        return [F(0)] + list(p)
    def lap(p, a):
        c = F(-1) / (4 * a)
        d1 = padd_(pderiv_(p), pscal_(c, p))                     # (p' + c p)
        d2 = padd_(padd_(pderiv_(pderiv_(p)), pscal_(2 * c, pderiv_(p))), pscal_(c * c, p))
        return padd_(shift_(pscal_(F(4), d2)), pscal_(F(6), d1))
    def pn(n, a):
        p = [F(1)]
        for _ in range(n):
            p = pscal_(F(-1), lap(p, a))
        return p
    def trim(p):
        p = list(p)
        while len(p) > 1 and p[-1] == 0:
            p.pop()
        return p
    for n in range(0, 5):
        for x in ((F(1), F(2), F(-3)), (F(1, 2), F(0), F(5, 3))):
            G = lambda y: (y[0] ** 2 + y[1] ** 2 + y[2] ** 2) ** n
            for lam in (F(2), F(3, 5)):
                assert G(tuple(c / lam for c in x)) == lam ** (-2 * n) * G(x)
        for a in (F(1), F(2, 3), F(5)):
            for lam in (F(2), F(3, 5), F(7, 4)):
                lhs = [c * lam ** (2 * i) for i, c in enumerate(pn(n, a))]   # p_n^(a)(lam^2 s)
                rhs = pscal_(lam ** (-2 * n), pn(n, a / lam ** 2))
                assert trim(lhs) == trim(rhs)
                wrong = pscal_(lam ** (-2 * n - 1), pn(n, a / lam ** 2))      # exponent off by one
                assert trim(lhs) != trim(wrong)                  # the test discriminates the exponent
        # Delta^2 = k^3 P: lam^3 * lam^(-3-2n) = lam^(-2n), so n_s - 1 = -2w with w = n
    # sanity of the regulated transform at n = 1: -Lap(e^(-s/4a)) = (3/(2a) - s/(4a^2)) e^(-s/4a)
    a = F(2, 3)
    assert trim(pn(1, a)) == [F(3) / (2 * a), F(-1) / (4 * a * a)]
    # real weights: leading late-time root is the larger one, w_lead in [-3/2, 0] iff 0 <= m^2 <= 9/4
    for k in range(0, 151):
        w = F(-k, 100)                                       # w_lead from 0 down to -3/2
        m2 = mu(w)
        shadow = -3 - w
        assert mu(shadow) == m2 and shadow <= w
        assert 0 <= m2 <= F(9, 4)
        assert -2 * w >= 0                                   # n_s - 1 >= 0: never red
    # principal series: Re w = -3/2 on both roots, n_s - 1 = 3
    assert -2 * F(-3, 2) == 3
    # a red tilt needs w_lead > 0, which forces m^2 < 0
    for k in range(1, 200):
        w = F(k, 1000)
        assert mu(w) < 0
    # exceptional series at Delta = 3 + k (m^2 = -k(k+3) H^2): weights -3-k and its shadow k
    for k in range(1, 6):
        assert mu(F(-3 - k)) == -k * (k + 3) == mu(F(k))
        assert -2 * F(k) <= -2                               # n_s - 1 = -2k: far too red
    # the measured value, Planck 2018: n_s = 0.9649 +- 0.0042
    ns, sd = F(9649, 10000), F(42, 10000)
    w_req = (1 - ns) / 2
    assert w_req == F(351, 20000)
    assert mu(w_req) == F(-21183201, 400000000) and mu(w_req) < 0
    for nsx in (ns - 2 * sd, ns + 2 * sd):                   # the whole 2-sigma band is tachyonic
        assert mu((1 - nsx) / 2) < 0
    # distance of the dilatation-invariant floor n_s = 1 from the measurement, in sigma
    z = (1 - ns) / sd
    assert F(83, 10) < z < F(84, 10)
    return True
