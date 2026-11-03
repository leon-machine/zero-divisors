"""synthesis.mirror-extensions-causal-convention: exact checks.

Signatures (p, q): p generators of square +1, q of square -1. The mirror of (p, q) is (q, p),
the metric reversal g -> -g. T14's causal convention reads the time direction of a causal
signature (min(p, q) = 1) as its minority sign; T14a's uniform convention reads time as the
plus sign in both towers. The check recomputes, in GA.py, the central volume element of every
odd signature up to dimension nine, the four single extensions of (1,3) and (3,1) under both
conventions, the obstructed extensions of the even residues, and the de Sitter added direction
in the tractor signatures (2,4) and (4,2).
"""
from fractions import Fraction as F
from itertools import product
import GA
from GA import mul, add, sub, scal, sc, gen, commutes
from tp_premise import premise

THIS = (1, 3)
MIRROR = (3, 1)


def squares(p, q):
    return tuple([1] * p + [-1] * q)


def omega(n):
    return {tuple(range(n)): F(1)}


def omega_sq(p, q):
    n = p + q
    w = omega(n)
    w2 = mul(w, w, squares(p, q))
    assert set(w2) <= {()}
    return w2.get((), F(0))


def is_central_omega(p, q):
    n = p + q
    w = omega(n)
    sq = squares(p, q)
    return all(commutes(w, gen(i), sq) for i in range(n))


def residue(p, q):
    return (p - q) % 8


def time_sign(sig, convention):
    p, q = sig
    if convention == "causal":
        assert min(p, q) == 1
        return 1 if p == 1 else -1          # the minority sign carries time
    return 1                                 # uniform: time = plus in both towers


def extend(sig, sign):
    p, q = sig
    return (p + 1, q) if sign == 1 else (p, q + 1)


def ext(sig, kind, convention):
    t = time_sign(sig, convention)
    return extend(sig, t if kind == "time" else -t)


def kind_of(omega2):
    return "doubled" if omega2 == 1 else "complex"


def space_dim(sig, convention):
    p, q = sig
    t = time_sign(sig, convention) if convention == "uniform" or min(p, q) == 1 else None
    return q if t == 1 else p


def check_mirror_extensions_causal_convention():
    premise("odd-extensions.volume-element-odd-dimension")
    premise("odd-extensions.doubling-or-complexification")
    premise("odd-extensions.four-extensions-oriented-pair")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    premise("dark-matter.nesting")
    premise("rule2.where-obstruction-sits-commuting-square")
    premise("rule2.which-residues-obstruct-which-way")
    premise("rule2.rule-2-plane")
    premise("odd-extensions.two-towers-one-curved-universe")

    # (i) odd dimension: omega central, omega^2 = (-1)^{n(n-1)/2 + q}, reversal flips it
    for n in (1, 3, 5, 7, 9):
        for p in range(n + 1):
            q = n - p
            assert is_central_omega(p, q)
            w2 = omega_sq(p, q)
            assert w2 == F(-1) ** (n * (n - 1) // 2 + q)
            assert omega_sq(q, p) == -w2                       # reversal swaps the type
            assert (residue(p, q) + residue(q, p)) % 8 == 0
            assert (w2 == 1) == (residue(p, q) % 4 == 1)        # doubled iff r = 1, 5
    # doubled case: (1 +- omega)/2 are complementary nonzero central idempotents
    for (p, q) in ((1, 4), (3, 2)):
        sq = squares(p, q)
        w = omega(5)
        e_plus = scal(F(1, 2), add(sc(1), w))
        e_minus = scal(F(1, 2), sub(sc(1), w))
        assert mul(e_plus, e_plus, sq) == e_plus and mul(e_minus, e_minus, sq) == e_minus
        assert mul(e_plus, e_minus, sq) == {} and add(e_plus, e_minus) == sc(1)

    # (ii) causal convention: the four extensions, with type and residue
    table = {}
    for world, sig in (("this", THIS), ("mirror", MIRROR)):
        for kind in ("space", "time"):
            e = ext(sig, kind, "causal")
            table[(world, kind)] = (e, residue(*e), kind_of(omega_sq(*e)))
    assert table[("this", "space")] == ((1, 4), 5, "doubled")
    assert table[("this", "time")] == ((2, 3), 7, "complex")
    assert table[("mirror", "time")] == ((3, 2), 1, "doubled")
    assert table[("mirror", "space")] == ((4, 1), 3, "complex")
    for kind in ("space", "time"):
        (a, ra, ka), (b, rb, kb) = table[("this", kind)], table[("mirror", kind)]
        assert b == (a[1], a[0])                    # mirror + X is the reversal of this + X
        assert (ra + rb) % 8 == 0 and ka != kb       # a reversal pair, opposite types
    # convention-free: a generator of square -1 doubles, of square +1 complexifies
    for sig in (THIS, MIRROR):
        assert kind_of(omega_sq(*extend(sig, -1))) == "doubled"
        assert kind_of(omega_sq(*extend(sig, 1))) == "complex"
    # causal reading: every causal signature has exactly one time and n - 1 space directions
    for sig in (THIS, MIRROR, (2, 1), (1, 2), (4, 1), (1, 4)):
        assert space_dim(sig, "causal") == sum(sig) - 1

    # (iii) uniform convention (T14a Cor 2.4): no reversal pair
    uni = {(w, k): ext(s, k, "uniform") for (w, s) in (("this", THIS), ("mirror", MIRROR))
           for k in ("space", "time")}
    assert uni[("mirror", "space")] == (3, 2) and uni[("mirror", "time")] == (4, 1)
    for kind in ("space", "time"):
        ra, rb = residue(*uni[("this", kind)]), residue(*uni[("mirror", kind)])
        assert (ra + rb) % 8 != 0
        assert uni[("mirror", kind)] != (uni[("this", kind)][1], uni[("this", kind)][0])
    # under it the mirror (3,1) has three time directions and one space direction
    assert min(MIRROR) == 1                      # still causal by min(p, q) = 1
    assert space_dim(MIRROR, "uniform") == 1 and MIRROR[0] == 3
    assert [space_dim(s, "uniform") for s in ((2, 1), (4, 1))] == [1, 1]

    # (iv) even residues: the obstructed (doubled) one-dimensional extension
    for n in (2, 4, 6, 8):
        for p in range(n + 1):
            q = n - p
            d = residue(p, q)
            minus_doubled = omega_sq(p, q + 1) == 1
            plus_doubled = omega_sq(p + 1, q) == 1
            assert minus_doubled != plus_doubled                # exactly one obstructs
            assert minus_doubled == (d % 4 == 2)                # minus extension at d = 2, 6
    # at residue 6 (time = plus) the minus extension is space: the KK direction obstructs
    assert ext(THIS, "space", "causal") == (1, 4) and omega_sq(1, 4) == 1
    # at residue 2 (time = minus) the minus extension is time; the KK direction is complex
    assert ext(MIRROR, "time", "causal") == (3, 2) and omega_sq(3, 2) == 1
    assert ext(MIRROR, "space", "causal") == (4, 1) and omega_sq(4, 1) == -1
    # the Rule 2 plane reads Cl(3,1) from Cl(2,1) by a plus generator, "a third spatial direction"
    assert extend((2, 1), 1) == MIRROR and time_sign((2, 1), "causal") == -1

    # (v) de Sitter: the frozen point in conformal-model form I = n_inf + (Lambda/6) n_0 with
    # n_0 = (e4 + e5)/2, n_inf = e4 - e5 (as in the store's de Sitter checks). V spans the
    # orthogonal complement of I in span(e4, e5). Each world's space sign is read as the MAJORITY
    # sign of its Lorentz frame (independently of time_sign), and I-perp's signature is computed.
    for L in (F(3), F(1, 2), F(7)):                                # Lambda > 0
        for world, base in (("this", (1, -1, -1, -1, 1, -1)), ("mirror", (-1, 1, 1, 1, -1, 1))):
            n0 = scal(F(1, 2), add(gen(4), gen(5)))
            ninf = sub(gen(4), gen(5))
            I = add(ninf, scal(L / 6, n0))
            a, b = I.get((4,), F(0)), I.get((5,), F(0))
            V = add(scal(b * base[5], gen(4)), scal(-a * base[4], gen(5)))   # <I, V> = 0
            assert add(mul(I, V, base), mul(V, I, base)) == {}
            II = mul(I, I, base)
            VV = mul(V, V, base)
            assert set(II) <= {()} and set(VV) <= {()}
            II, VV = II.get((), F(0)), VV.get((), F(0))
            frame = tuple(base[:4])
            assert all(add(mul(gen(i), V, base), mul(V, gen(i), base)) == {} for i in range(4))
            space_sign = 1 if frame.count(1) == 3 else -1                     # majority sign
            assert frame.count(space_sign) == 3 and frame.count(-space_sign) == 1
            vsign = 1 if VV > 0 else -1
            p = frame.count(1) + (1 if VV > 0 else 0)
            q = frame.count(-1) + (1 if VV < 0 else 0)
            assert II * VV < 0
            if world == "this":
                assert II == L / 3 and (p, q) == (1, 4) and omega_sq(p, q) == 1
            else:
                assert II == -L / 3 and (p, q) == (4, 1) and omega_sq(p, q) == -1
            assert vsign == space_sign                                  # V is spacelike in both
            # the uniform reading calls V time in the mirror: its time sign is +1 there
            if world == "mirror":
                assert vsign == time_sign(MIRROR, "uniform")
    return True
