"""synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side: exact checks.

Sigma_n = L^{2n+1}(4) = S^{2n+1} / <J>, J the quarter turn v -> v . B in every coordinate plane. The dying line L
is the flat line on which J acts by -1; Z^x is the integer coefficient system twisted by x = w_1(L). Checks:
  (1) in Cl(6,0): the map c negating e_2, e_4, e_6 anticommutes with the quarter turn, so the line of c(v) has
      holonomy -1 and the coefficient system of a plane bundle N with w_1(N) = x is the sign character;
  (2) the twisted cochain complex of the equivariant cell structure (one free cell per dimension, boundary
      (g - 1) for odd cells and N for even cells), the generator acting by -1 on the coefficients: cohomology
      Z_2 in odd degrees and 0 in even degrees; controls with the group of order two (projective spaces);
  (3) Whitney: w(N) = (1 + x)^{-1} = 1 + x in the mod-2 ring of the lens space, the class of L + 1;
  (4) the complex K-ring Z[s]/((1+s)^4 - 1, s^{n+1}), s = chi - 1: 2(1 - chi^2) is not zero for 3 <= n <= 12 and
      is zero for n = 1, 2; 4(1 - chi^2) is zero for n = 3, 4 (so the stored lambda bound gives only three there);
  (5) dimension five: the spin class 2a^2 of L + L for a = y, 3y in H^4 = Z_4.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

ORDER = 4                 # order of the quarter turn
TOP_N = 6                 # lens spaces L^{2n+1}(4), n = 1 .. TOP_N, in the cochain check
K_TOP = 12                # K-ring checked up to n = K_TOP


def check_dying_line_has_sign_holonomy():
    premise("synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial")
    premise("sheaf.imported-real-line-bundles")
    sq = GA.sig(6, 0)
    B = GA.add(GA.mul(GA.gen(0), GA.gen(1), sq), GA.mul(GA.gen(2), GA.gen(3), sq), GA.mul(GA.gen(4), GA.gen(5), sq))

    def J(v):
        return {k: c for k, c in GA.mul(v, B, sq).items() if len(k) == 1}

    def c(v):
        out = {}
        for k, val in v.items():
            out[k] = -val if k[0] % 2 == 1 else val
        return out

    vs = [GA.add(GA.scal(F(1 + i), GA.gen(i)), GA.scal(F(3 - 2 * i), GA.gen((i + 1) % 6)), GA.gen((i + 4) % 6))
          for i in range(6)]
    for v in vs:
        assert GA.eq(J(J(v)), GA.neg(v))                       # J^2 = -1: order four
        assert GA.eq(c(J(v)), GA.neg(J(c(v))))                 # c J = -J c: the line of c(v) has holonomy -1
        assert GA.mul(c(v), c(v), sq) == GA.mul(v, v, sq)      # c(v) is nowhere zero on the sphere
        assert not GA.eq(c(J(v)), J(c(v)))
    return True


def boundary_coefficient(k, m, character):
    """Value on the boundary of the cell e_k of the cochain dual to e_{k-1}, the generator acting on the
    coefficients by `character` (1: untwisted, -1: twisted by the sign character)."""
    if k % 2 == 1:
        return character - 1                                   # boundary (g - 1) e_{k-1}
    return sum(character ** a for a in range(m))               # boundary N e_{k-1}


def twisted_cohomology(top, m, character):
    """Orders of the cohomology groups H^0 .. H^top of the complex Z -> Z -> ... (cells e_0 .. e_top):
    0 for an infinite group is returned as the string 'Z', otherwise the order."""
    d = [boundary_coefficient(k, m, character) for k in range(1, top + 1)]      # d[j]: C^j -> C^{j+1}
    out = []
    for j in range(top + 1):
        kernel_all = (j == top) or d[j] == 0
        incoming = abs(d[j - 1]) if j >= 1 else 0
        if not kernel_all:
            out.append(1)
        elif incoming == 0:
            out.append('Z')
        else:
            out.append(incoming)
    return out


def check_twisted_cochain_complex_of_lens_spaces():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    for n in range(1, TOP_N + 1):
        top = 2 * n + 1
        tw = twisted_cohomology(top, ORDER, -1)
        assert tw == [2 if j % 2 == 1 else 1 for j in range(top + 1)]          # Z_2 odd, 0 even
        assert tw[2] == 1                                                       # twisted H^2 = 0
        un = twisted_cohomology(top, ORDER, 1)
        assert un[0] == 'Z' and un[top] == 'Z' and all(un[j] == (ORDER if j % 2 == 0 else 1) for j in range(1, top))
    # controls, the group of order two: projective plane has twisted H^2 = Z (its tangent bundle is not L + 1),
    # projective spaces of dimension three and more have twisted H^2 = 0
    assert twisted_cohomology(2, 2, -1)[2] == 'Z'
    assert twisted_cohomology(3, 2, -1)[2] == 1 and twisted_cohomology(5, 2, -1)[2] == 1
    return True


def check_whitney_class_of_the_rank_two_complement():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("synthesis.imported-whitney-product-formula-and-projective-space")
    # mod-2 ring of the lens space in degrees up to two: 1, x, u with x^2 = 0; classes as (c0, cx, cu)
    def times(a, b):
        return (a[0] * b[0] % 2, (a[0] * b[1] + a[1] * b[0]) % 2, (a[0] * b[2] + a[2] * b[0]) % 2)   # x^2 = 0
    one_plus_x = (1, 1, 0)
    w_N = one_plus_x                                            # candidate inverse of 1 + x
    assert times(one_plus_x, w_N) == (1, 0, 0)                  # (1 + x)(1 + x) = 1: w(N) = 1 + x
    assert w_N[1] == 1 and w_N[2] == 0                          # w_1(N) = x, w_2(N) = 0, the classes of L + 1
    # on projective space x^2 = u is not zero and (1 + x)^{-1} has a degree-two part: no such collapse
    def times_proj(a, b):
        return (a[0] * b[0] % 2, (a[0] * b[1] + a[1] * b[0]) % 2, (a[0] * b[2] + a[2] * b[0] + a[1] * b[1]) % 2)
    assert times_proj(one_plus_x, (1, 1, 1)) == (1, 0, 0)
    return True


def binom(n, k):
    out = 1
    for i in range(k):
        out = out * (n - i) // (i + 1)
    return out


def in_ideal(v, n):
    """Is the polynomial v (coefficients of s^1 .. s^n) in the ideal of Z[s]/(s^{n+1}) generated by
    (1 + s)^4 - 1 = 4s + 6s^2 + 4s^3 + s^4?  The translates s^j ((1+s)^4 - 1) are a triangular basis of the
    ideal with diagonal 4, so greedy reduction from the lowest degree decides membership."""
    v = (list(v) + [0] * n)[:n]                                 # truncate at s^n: s^{n+1} = 0
    rel = [4, 6, 4, 2]        # 4, 6, 4, 1
    for j in range(n):
        if v[j] % rel[0]:
            return False
        q = v[j] // rel[0]
        for i, r in enumerate(rel):
            if j + i < n:
                v[j + i] -= q * r
    return not any(v)


def check_doubled_line_in_the_k_ring():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    premise("synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height")
    one_minus_chi2 = [-2, -1]                                   # 1 - (1 + s)^2 = -2s - s^2
    for n in range(1, K_TOP + 1):
        twice = in_ideal([2 * a for a in one_minus_chi2], n)
        assert twice == (n <= 2)                                # 2(1 - chi^2) = 0 only for n = 1, 2
        assert not in_ideal(one_minus_chi2, n)                  # 1 - chi^2 itself is never zero
    for n in (3, 4):
        assert in_ideal([4 * a for a in one_minus_chi2], n)     # the lambda bound 2^{k-1}(1 - xi) allows k = 3
    assert not in_ideal([4 * a for a in one_minus_chi2], 5)
    return True


def check_spin_class_in_dimension_five():
    premise("synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial")
    for a in (1, 3):                                            # the two spin structures: a = y, 3y
        assert (2 * a) % ORDER == 2                             # 2a = e(L + L) = 2y
        assert (2 * a * a) % ORDER == 2                         # q_1 = 2a^2 = 2y^2, not zero in Z_4 (n >= 2)
        assert (4 * a * a) % ORDER == 0                         # p_1 = 0
    return True


def check_gaussian_image_for_every_dimension():
    premise("synthesis.cohomology-of-the-quarter-turn-lens-spaces-from-the-equivariant-cell-structure")
    # the ring map chi -> I = e1e2 (GA unit bivector of the plane, I^2 = -1) sends chi - 1 to I - 1, 1 - chi^2 to 2
    sq = GA.sig(2, 0)
    I = GA.mul(GA.gen(0), GA.gen(1), sq)
    one = GA.sc(F(1))
    assert GA.eq(GA.mul(I, I, sq), GA.neg(one))
    t = GA.sub(one, I)                                           # 1 - I, the image of 1 - chi
    t2 = GA.mul(t, t, sq)
    t4 = GA.mul(t2, t2, sq)
    assert GA.eq(GA.sub(one, GA.mul(I, I, sq)), GA.sc(F(2)))     # 1 - chi^2 -> 2
    assert GA.eq(t4, GA.sc(F(-4)))                               # (1 - I)^4 = -4: the image of 2(1 - chi^2) is -(1 - I)^4
    t5 = GA.mul(t4, t, sq)
    # 4 / (1 - I)^5 = -(1 + I)/2 is not a Gaussian integer: 4 is not in the ideal ((1 - I)^{n+1}) for n >= 4
    quotient = GA.scal(F(-1, 2), GA.add(one, I))
    assert GA.eq(GA.mul(quotient, t5, sq), GA.sc(F(4)))
    assert any(c.denominator != 1 for c in quotient.values())
    return True
