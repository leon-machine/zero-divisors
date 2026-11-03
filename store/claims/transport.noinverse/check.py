"""transport.noinverse: exact checks.

A null vector v != 0 has no left or right inverse in Cl(p,q), nor in any associative unital algebra
containing Cl(p,q). Tested in GA.py on every mixed signature with 2 <= n <= 5, with null vectors
e_i +- e_j (one positive, one negative generator) and Pythagorean ones 3e_a + 4e_b + 5e_c where the
signature allows:
  (1) v^2 = 0 exactly and v != 0.
  (2) Inside Cl(p,q): left and right multiplication by v have rank exactly 2^(n-1), half the
      dimension, so neither is surjective and v has no one-sided inverse there.
  (3) The extension argument: in the larger algebra Cl(p+1, q+1) (and in Cl(p,q) with one adjoined
      degenerate generator) v^2 is still 0, so v (v w) = 0 and (w v) v = 0 for every sample w;
      if v w = 1 then v = v (v w) = 0, a contradiction. The multiplication maps by v keep half rank
      in the larger algebra.
No premises: the claim has no uses.
"""
from fractions import Fraction as F

import GA

SIGS = [(p, n - p) for n in range(2, 6) for p in range(1, n)]
SAMPLE_W = [((), 2), ((0,), -1), ((1,), 3), ((0, 1), 5)]


def nulls(p, q):
    n = p + q
    out = []
    for i in range(p):
        for j in range(p, n):
            out.append(GA.add(GA.gen(i), GA.gen(j)))
            out.append(GA.sub(GA.gen(i), GA.gen(j)))
    if p >= 2:
        out.append(GA.add(GA.scal(3, GA.gen(0)), GA.scal(4, GA.gen(1)), GA.scal(5, GA.gen(p))))
    if q >= 2:
        out.append(GA.add(GA.scal(5, GA.gen(0)), GA.scal(3, GA.gen(p)), GA.scal(-4, GA.gen(p + 1))))
    return out


def mult_rank(v, sq, n, side):
    blades = GA.all_blades(n)
    rows = []
    for b in blades:
        x = {b: F(1)}
        y = GA.mul(v, x, sq) if side == "left" else GA.mul(x, v, sq)
        rows.append([y.get(c, F(0)) for c in blades])
    return GA.field_rank(rows)


def sample_w(n):
    return GA.add(*[GA.scal(c, {tuple(i for i in b if i < n): F(1)}) for b, c in SAMPLE_W])


def check_null_vector_squares_to_zero_and_multiplication_has_half_rank():
    ok = True
    count = 0
    for p, q in SIGS:
        n = p + q
        sq = GA.sig(p, q)
        for v in nulls(p, q):
            ok = ok and GA.is_zero(GA.mul(v, v, sq)) and not GA.is_zero(v)
            half = 2 ** (n - 1)
            ok = ok and mult_rank(v, sq, n, "left") == half and mult_rank(v, sq, n, "right") == half
            count += 1
    # 2pq sign pairs per signature plus the Pythagorean extras: 2 + 10 + 24 + 46 by hand
    ok = ok and count == 82
    GA.check("null v: v^2 = 0, and v x, x v have rank 2^(n-1) on Cl(p,q) (no one-sided inverse), 82 cases", ok)
    return ok


# Sample extensions: a hyperbolic pair (Cl(p+1, q+1)) and one degenerate generator; rank of the
# multiplication maps checked in both extensions for bases with n <= 3.
EXTENSIONS = ((1, -1), (0,))
MAX_N_RANK = 3


def probe_w(m):
    """Sample w in the extended algebra on m generators, involving the last adjoined generator."""
    return GA.add(sample_w(m), GA.gen(m - 1))


def check_no_inverse_in_larger_algebras():
    ok = True
    rank_cases = 0
    for p, q in SIGS:
        n = p + q
        for extra in EXTENSIONS:
            sq = GA.sig(p, q) + extra
            m = n + len(extra)
            for v in nulls(p, q):
                ok = ok and GA.is_zero(GA.mul(v, v, sq))
                w = probe_w(m)
                # v (v w) = v^2 w = 0 and (w v) v = 0, so v w = 1 or w v = 1 would force v = 0
                ok = ok and GA.is_zero(GA.mul(v, GA.mul(v, w, sq), sq))
                ok = ok and GA.is_zero(GA.mul(GA.mul(w, v, sq), v, sq))
                if n <= MAX_N_RANK:
                    rank_cases += 1
                    ok = ok and mult_rank(v, sq, m, "left") == 2 ** (m - 1)
                    ok = ok and mult_rank(v, sq, m, "right") == 2 ** (m - 1)
    # by hand: the null vectors with n <= 3 are 2 (for (1,1)) + 5 + 5 (for (1,2), (2,1)) = 12, in each
    # of the two extensions
    ok = ok and rank_cases == 24
    GA.check("in Cl(p+1,q+1) and with an adjoined degenerate generator v^2 = 0 persists: v(vw) = (wv)v = 0", ok)
    return ok
