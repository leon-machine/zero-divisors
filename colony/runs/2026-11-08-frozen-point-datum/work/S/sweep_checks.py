#!/usr/bin/env python3
"""Exact checks behind the class B and C rows of findings/sweep.md (run 2026-11-08-frozen-point-datum).

Run:  python3 colony/runs/2026-11-08-frozen-point-datum/work/S/sweep_checks.py
Exact arithmetic only (Fractions, lib/GA.py). Each sw_* function names the sweep rows it confirms. For every B row the
pattern is: the clause as written fails over Q at some Lambda with Lambda/3 not a square (Lambda = 7/3 or 6, and 9 for
the group labels), and holds over Q once Lambda = 3H^2 with H rational. Quadratic extensions are span{1, u}, u = f1 f2,
the product of two extra generators of squares 1 and -delta (u^2 = delta, central on the blades of Cl(2,4)); no
imaginary unit is used.
"""
import sys
from fractions import Fraction as F
from itertools import product

sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA  # noqa: E402
from GA import mul, add, sub, scal, sc, gen, eq  # noqa: E402

SQ6 = (1, -1, -1, -1, 1, -1)
U = {(6, 7): F(1)}
RESULTS = []


def ext(delta):
    return SQ6 + (1, -F(delta))


def isqrt(n):
    lo, hi = 0, 1
    while hi * hi <= n:
        hi *= 2
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if mid * mid <= n:
            lo = mid
        else:
            hi = mid - 1
    return lo


def is_sq(q):
    q = F(q)
    return q >= 0 and isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator


def rt(q):
    q = F(q)
    assert is_sq(q)
    return F(isqrt(q.numerator), isqrt(q.denominator))


def dot(a, b, sq):
    return add(mul(a, b, sq), mul(b, a, sq)).get((), F(0)) / 2


def frame(L):
    n0 = scal(F(1, 2), add(gen(4), gen(5)))
    ninf = sub(gen(4), gen(5))
    return n0, ninf, add(ninf, scal(F(L) / 6, n0)), sub(ninf, scal(F(L) / 6, n0))


def prod_all(vs, sq):
    out = sc(1)
    for v in vs:
        out = mul(out, v, sq)
    return out


def lift(x, sq):
    n0, ninf, _, _ = frame(0)
    Qx = dot(x, x, sq) if x else F(0)
    return add(n0, x, scal(-Qx / 2, ninf)), Qx


def sum_of_two_squares_witness(q, box=30):
    """A rational pair (a, b) with a^2 + b^2 = q, searched with denominators up to box, or None."""
    q = F(q)
    for den in range(1, box + 1):
        t = q * den * den
        if t.denominator != 1:
            continue
        t = t.numerator
        for a in range(0, isqrt(t) + 1):
            r = t - a * a
            if is_sq(r):
                return F(a, den), rt(r) / den
    return None


def report(name, rows):
    RESULTS.append(name)
    print("PASS  %-36s rows: %s" % (name, ", ".join(rows)))


BAD = [F(7, 3), F(6), F(1)]          # Lambda/3 = 7/9, 2, 1/3: not rational squares
GOOD_H = [F(1), F(1, 2), F(3, 7)]


def sw_static_boost():
    """static boost (iii): unit boost u = B/H, e_W = W/H, R_h = 1/H, kappa = H, horizon point (2/H) e1."""
    sq = SQ6
    for L in BAD:
        d = L / 3
        _, _, I, W = frame(L)
        B = mul(gen(0), W, sq)
        assert eq(mul(B, B, sq), sc(d)) and not is_sq(d) and not is_sq(1 / d) and not is_sq(4 / d)
    for H in GOOD_H:
        L = 3 * H * H
        _, _, I, W = frame(L)
        B = mul(gen(0), W, sq)
        u = scal(1 / H, B)
        assert eq(mul(u, u, sq), sc(1)) and dot(scal(1 / H, W), scal(1 / H, W), sq) == -1
        X, Qx = lift(scal(2 / H, gen(1)), sq)
        assert Qx == -12 / L and dot(X, I, sq) == 2 and (2 / H) / 2 == 1 / H
    report("sw_static_boost", ["synthesis.de-sitter-static-boost-frozen-point (iii), technical"])


def sw_completed_pair():
    """completed pair (v) and (iv) wording: a pair over K exists iff Lambda/3 is a nonzero square."""
    sq = SQ6
    for L in BAD + [F(-3)]:
        d = L / 3
        _, _, _, W = frame(L)
        # Q(a e0 + b W) = a^2 - d b^2 on a grid: zero only at (0, 0)
        for a, b in product(range(-6, 7), repeat=2):
            z = add(scal(a, gen(0)), scal(b, W))
            assert dot(z, z, sq) == a * a - d * b * b
            assert (a * a - d * b * b == 0) == (a == 0 and b == 0)
    for H in GOOD_H:
        L = 3 * H * H
        _, _, _, W = frame(L)
        eW = scal(1 / H, W)
        v, vs = scal(F(1, 2), add(gen(0), eW)), scal(F(1, 2), sub(gen(0), eW))
        assert dot(v, v, sq) == 0 == dot(vs, vs, sq) and eq(add(mul(v, vs, sq), mul(vs, v, sq)), sc(1))
        # endpoints x = -+ (2/H) e0 = -+ sqrt(12/Lambda) e0
        assert (2 / H) ** 2 == 12 / L
    # Lambda = 7/3 over span{1, u}, u^2 = 7: H = u/3 gives the pair
    sqk = ext(7)
    _, _, _, W = frame(F(7, 3))
    Hk = scal(F(1, 3), U)
    Hinv = scal(F(3, 7), U)
    assert eq(mul(Hk, Hinv, sqk), sc(1))
    eW = mul(Hinv, W, sqk)
    v = scal(F(1, 2), add(gen(0), eW))
    assert mul(v, v, sqk) == {}
    report("sw_completed_pair", ["synthesis.cosmological-horizon-completed-pair (v), (iv) and one-liner wording",
                                 "obj.synthesis.cosmological-horizon-boundary-modes"])


def sw_unit_stelle_west_and_cl14():
    """e_5 = V/|V| = H V (Q(V) = -3/Lambda), Cl(I-perp) = Cl(1,4) doubled, mirror Cl(4,1)."""
    sq = SQ6
    rev = tuple(-s for s in sq)
    for L in BAD:
        d = L / 3
        QV = -3 / L
        assert not is_sq(-QV)                    # no rational |V|
        _, _, _, W = frame(L)
        om = prod_all([gen(0), gen(1), gen(2), gen(3), W], sq)
        assert eq(mul(om, om, sq), sc(d)) and not is_sq(d)          # centre a field, not doubled
        omr = prod_all([gen(0), gen(1), gen(2), gen(3), W], rev)
        assert eq(mul(omr, omr, rev), sc(-d)) and not is_sq(d)      # mirror centre not that of Cl(4,1)
    for H in GOOD_H:
        L = 3 * H * H
        QV = -3 / L
        assert QV * H * H == -1                  # e_5 = H V has square -1
        _, _, _, W = frame(L)
        e5 = scal(1 / H, W)                      # W = V / Q(V) is parallel to V; W/H is the unit
        basis = [gen(0), gen(1), gen(2), gen(3), e5]
        om = prod_all(basis, sq)
        assert eq(mul(om, om, sq), sc(1))
        e = scal(F(1, 2), add(sc(1), om))
        assert eq(mul(e, e, sq), e) and all(GA.commutes(e, g, sq) for g in basis)
        # e_5 acts as +-omega' on the two summands: e_5 = om * (e0 e1 e2 e3)^{-1} up to sign
        om4 = prod_all(basis[:4], sq)
        assert eq(mul(om4, om4, sq), sc(-1))
        assert eq(mul(scal(-1, om4), om, sq), e5) or eq(mul(om4, om, sq), e5) or \
            eq(mul(om, scal(-1, om4), sq), e5) or eq(mul(om, om4, sq), e5)
        omr = prod_all(basis, rev)
        assert eq(mul(omr, omr, rev), sc(-1))
    report("sw_unit_stelle_west_and_cl14",
           ["odd-extensions.two-towers-one-curved-universe (i)-(iii)", "synthesis.mirror-extensions-causal-convention (v)",
            "odd-extensions.are-ascents-pair-signed", "odd-extensions.belongs-tower (iii)",
            "odd-extensions.translation-bivectors-frozen-point (i)", "odd-extensions.cosmological-constant-deforms-wall",
            "odd-extensions.two-readings-which-which", "odd-extensions.not-coupling-between-towers (technical)",
            "dark-energy.imported-macdowell-mansouri-theorem-stelle-west", "notes"])


def sw_anti_de_sitter_unit():
    """Lambda < 0: e_5 = H' V with Q = +1 and Cl(I-perp) = Cl(2,3) need -Lambda/3 = H'^2."""
    sq = SQ6
    for L in (F(-1), F(-6), F(-7, 3)):
        assert not is_sq(-L / 3) and not is_sq(-3 / L)
    for Hp in (F(1), F(2, 5)):
        L = -3 * Hp * Hp
        _, _, _, W = frame(L)
        e5 = scal(1 / Hp, W)
        assert dot(e5, e5, sq) == 1
        om = prod_all([gen(0), gen(1), gen(2), gen(3), e5], sq)
        assert eq(mul(om, om, sq), sc(-1))
    report("sw_anti_de_sitter_unit", ["odd-extensions.translation-bivectors-frozen-point (ii)",
                                      "odd-extensions.are-ascents-pair-signed (Lambda < 0)",
                                      "odd-extensions.two-towers-one-curved-universe (i), anti-de Sitter half",
                                      "odd-extensions.cosmological-constant-deforms-wall (Lambda < 0)"])


def similarity(q, sig_last):
    """Similarity of <1,-1,-1,-1, sig_last*q> onto <1,-1,-1,-1, sig_last> of factor q, from q = a^2 + b^2."""
    w = sum_of_two_squares_witness(q)
    if w is None:
        return None
    a, b = w
    f = [gen(i) for i in range(5)]
    T = [add(scal((1 + q) / 2, f[0]), scal((1 - q) / 2, f[1])), add(scal((1 - q) / 2, f[0]), scal((1 + q) / 2, f[1])),
         add(scal(a, f[2]), scal(b, f[3])), add(scal(-b, f[2]), scal(a, f[3])), scal(q, f[4])]
    return T


def sw_group_labels():
    """SO(I-perp) = SO(1,4) by a similarity iff Lambda/3 is a sum of two squares; SO(2,3) iff -Lambda/3 is."""
    for d, expect in ((F(2), True), (F(5, 9), True), (F(3), False), (F(7, 9), False), (F(1, 3), False), (F(1), True)):
        for sgn, std in ((-1, (1, -1, -1, -1, -1)), (1, (1, -1, -1, -1, 1))):
            src_sq = (1, -1, -1, -1, sgn * d)
            T = similarity(d, sgn)
            if expect:
                assert T is not None
                G1 = [[dot(x, y, src_sq) for y in [gen(i) for i in range(5)]] for x in [gen(i) for i in range(5)]]
                G2 = [[dot(x, y, std) for y in T] for x in T]
                assert G2 == [[d * g for g in row] for row in G1]
            else:
                assert T is None
    # the failures are exact: 3 and 7 are not sums of two rational squares (residues mod 3 and mod 4 / 8)
    assert [(x, y) for x, y in product(range(3), repeat=2) if (x * x + y * y) % 3 == 0] == [(0, 0)]
    assert [(x, y) for x, y in product(range(4), repeat=2) if (x * x + y * y) % 4 == 3] == []
    assert sum_of_two_squares_witness(F(7, 9)) is None and 7 % 4 == 3
    # with H the label holds: d = H^2 = H^2 + 0^2
    for H in GOOD_H:
        assert similarity(H * H, -1) is not None
    report("sw_group_labels",
           ["SO(1,4), so(1,4), SO(2,3), so(2,3) labels: dark-energy.frozen-point-makes-stelle-west-vector",
            "dark-energy.imported-frozen-point-geometry", "dark-matter.imported-frozen-point-de-sitter-radius",
            "interior.non-null-stabilisers-section-they-act", "interior.schwarzschild-de-sitter-weighted-limit",
            "interior.stabiliser-rotates-parabolic-reductive", "mass.casimir-form-join", "mass.five-broken-generators",
            "mass.imported-frozen-point-tractor-connection", "odd-extensions.imported-frozen-point",
            "standard-model.imported-grip-area-casimir-form", "synthesis.curvature-only-tractor-actions-are-macdowell-mansouri",
            "synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation",
            "proof and note wording"])


def sw_radius_and_scales():
    """ell = 1/H, rho_Lambda = 2 ell = 2/H, R_h = 1/H: rational iff Lambda/3 is a rational square."""
    for L in BAD:
        assert not is_sq(3 / L) and not is_sq(12 / L)
    for H in GOOD_H:
        L = 3 * H * H
        assert (1 / H) ** 2 == 3 / L and (2 / H) ** 2 == 12 / L
        # tube point: N(rho) = rho / sigma, sigma = 1 + L rho^2 / 12, kappa = H: 1 - kappa N = (1 - H rho/2)^2 / sigma
        for rho in (F(1), F(3, 4), F(5), 2 / H):
            sigma = 1 + L * rho * rho / 12
            assert 1 - H * rho / sigma == (1 - H * rho / 2) ** 2 / sigma
        rho_max = 2 / H
        assert 1 - H * rho_max / (1 + L * rho_max ** 2 / 12) == 0
    report("sw_radius_and_scales", ["synthesis.de-sitter-field-fixes-the-observer-tube-point",
                                    "synthesis.positive-structure-and-natural-scale-actions-do-not-select-the-almost-einstein-scale",
                                    "dark-matter.imported-frozen-point-de-sitter-radius (radius)",
                                    "odd-extensions.two-readings-which-which (norm ell)",
                                    "odd-extensions.exceptional-algebra-residue-completion-both-sides (ii)"])


def sw_sheaf_rescaling():
    """exceptional algebra (i): W/sqrt|L| has square -sgn(L)/3; Cl(1,3) + <+-1/3> = Cl(2,3), Cl(1,4) needs sqrt 3."""
    sq = SQ6
    std = [gen(0), gen(1), gen(2), gen(3)]
    for H in GOOD_H:
        L = 3 * H * H
        assert not is_sq(L)                      # sqrt|Lambda| = sqrt(3) H is not rational
        _, _, _, W = frame(L)
        assert dot(scal(1 / H, W), scal(1 / H, W), sq) == -1
    for L in (F(1), F(-1), F(4), F(-4)):
        _, _, _, W = frame(L)
        w = scal(1 / rt(abs(L)), W)
        t = -L / abs(L)
        assert dot(w, w, sq) == t / 3
        om = prod_all(std + [w], sq)
        assert eq(mul(om, om, sq), sc(-t / 3)) and not is_sq(F(1, 3))
    sq3 = ext(3)
    _, _, _, W = frame(F(1))
    uw = mul(U, W, sq3)
    assert eq(mul(uw, uw, sq3), sc(-1))
    report("sw_sheaf_rescaling", ["odd-extensions.exceptional-algebra-residue-completion-both-sides (i), technical, one-liner, check (class C)"])


def sw_line_tame_wall_gauge():
    """line-tame-wall (iii): the gauge a = b has a^2 = Lambda/6; with Lambda = 3H^2 this is H^2/2: needs sqrt 2."""
    for H in GOOD_H + [F(2), F(5, 3)]:
        L = 3 * H * H
        assert L / 6 == H * H / 2 and not is_sq(L / 6)
    for s in (F(1), F(2, 3)):
        L = 6 * s * s
        assert is_sq(L / 6) and not is_sq(L / 3)   # where the gauge is rational, H is not
    # over span{1, u}, u^2 = 2: a = u H / 2 has a^2 = H^2/2
    sq = ext(2)
    for H in GOOD_H:
        a = scal(H / 2, U)
        assert eq(mul(a, a, sq), sc(H * H / 2))
    report("sw_line_tame_wall_gauge", ["odd-extensions.line-tame-wall (iii) and proof (class C)"])


def sw_operator_join():
    """operator join (2), (3): lambda = H^2/2, sqrt(lambda) = H/sqrt 2: needs sqrt 2 besides H."""
    sq = ext(2)
    for H in GOOD_H:
        lam = H * H / 2
        assert not is_sq(lam)
        r = scal(H / 2, U)                       # sqrt(lambda) = u H / 2
        assert eq(mul(r, r, sq), sc(lam))
        s2 = scal(1 / H, U)                      # s^2 = 1/sqrt(lambda) = u / H
        assert eq(mul(mul(s2, s2, sq), sc(lam), sq), sc(1))
    for L, rl in ((F(6), F(1)), (F(3, 2), F(1, 2))):
        assert rl * rl == L / 6 and not is_sq(L / 3)
    report("sw_operator_join", ["synthesis.operator-join-point-spectrum-on-positive-energy-modules (2), (3), check (class C)"])


def sw_weight_nu():
    """weight polynomial: w = -3/2 +- I4 nu with nu^2 = m^2/H^2 - 9/4; nu in K is a condition on m/H, not on H."""
    for x, ok in ((F(5, 2), True), (F(2), False), (F(15, 8), True), (F(3), False)):
        nu2 = x * x - F(9, 4)
        assert is_sq(nu2) == ok
    # the dictionary itself is rational: m^2/H^2 = -w(w+3) = 9/4 + nu^2 for w = -3/2 +- I4 nu (I4^2 = -1)
    for nu in (F(2), F(1, 3), F(7, 5)):
        sq = (-1,)
        I4 = gen(0)
        w = add(sc(F(-3, 2)), scal(nu, I4))
        val = scal(-1, mul(w, add(w, sc(3)), sq))
        assert eq(val, sc(F(9, 4) + nu * nu))
    report("sw_weight_nu", ["mass.weight-polynomial-two-series (class C: nu in K)"])


def sw_complement_window():
    """complement window (iii): the standard (1,4) and (4,1) are admitted over Q iff Lambda/3 is a square."""
    sq = SQ6
    for L in BAD:
        d = L / 3
        _, _, _, W = frame(L)
        # a standard (1,4) subspace of the five-dimensional I-perp is all of it; isometry needs omega^2 = d a square
        om = prod_all([gen(0), gen(1), gen(2), gen(3), W], sq)
        assert eq(mul(om, om, sq), sc(d)) and not is_sq(d)
    for H in GOOD_H:
        _, _, _, W = frame(3 * H * H)
        basis = [gen(0), gen(1), gen(2), gen(3), scal(1 / H, W)]
        assert [dot(b, b, sq) for b in basis] == [1, -1, -1, -1, -1]
    report("sw_complement_window", ["synthesis.frozen-point-complement-window-lowest-causal (iii), (iv), read over Q"])


if __name__ == "__main__":
    for name in sorted(n for n in dir() if n.startswith("sw_")):
        globals()[name]()
    print("%d sweep checks passed" % len(RESULTS))
