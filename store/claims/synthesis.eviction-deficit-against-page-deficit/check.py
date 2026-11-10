"""synthesis.eviction-deficit-against-page-deficit: exact checks.

All arithmetic is over Fractions.  ln 2 is enclosed by the rational partial sums of
ln 2 = sum_j 1/(j 2^j) with the tail bound 1/((N+1) 2^N); exp(157/25) is bounded below by a
Taylor partial sum (all terms positive) and 2 pi > 157/25.

(i)   Page's average entropy <S> = H_{mn} - H_n - (m-1)/(2n) (imported) for m = 2^w <= n = 2^r:
      the deficit ln m - <S> lies strictly between (m-1)/(2n) and (m-1)/(2n) + (m-1)/(mn+1),
      so it is positive at every stage, below 1 nat, and above 2/5 at the crossing m = n >= 4;
      On a parity sector the mean entropy is sum_{k=n/2+1}^{mn/2} 1/k - (m-2)/(2n) (the weight term plus Page's
      average on a block); its deficit lies between (m-2)/(2n) + 2(m-1)/(2mn+m+1) and m/(2n) - 1/(mn) < 1/2,
      is above (m-1)/(2n) for m >= 4 and below it at m = 2, and differs from the abstract deficit by a rational;
(ii)  zero weight: occupation 1/2 has zero Pinsker bound, mode entropy s(0) = ln 2 (computed, in units of
      ln 2) and hence zero deficit sum (ln 2 - h_k) for windows of 1 to 5 members;
(iii) general weights: with E = e^{x_*} at four sample values, the Pinsker bound per member equals
      (1/2) tanh^2(x_*/2), and the smallest |W| above 2/tanh^2(x_*/2) puts the bound above 1 nat.
      (Q) weights: e^{2 pi} > 500, so a mode of weight kappa*k, k != 0, has p < 1/501; Pinsker
      gives > 49/100 per member, and H(p) < 8/501 gives > 1/2, so two members exceed 1 nat.
"""
from fractions import Fraction as F
import GA
from GA import peval
from tp_premise import premise


def ln2_bounds(N):
    lo = sum(F(1, j * 2 ** j) for j in range(1, N + 1))
    return lo, lo + F(1, (N + 1) * 2 ** N)


def harmonic(a, b):
    """sum_{k=a+1}^{b} 1/k"""
    return sum(F(1, k) for k in range(a + 1, b + 1))


def check_page_deficit_bounds():
    premise("synthesis.imported-pinsker-inequality")
    premise("singularity.imported-page-average-entropy-subsystem")
    premise("singularity.assembled-page-curve-up-typicality")
    lo2, hi2 = ln2_bounds(60)
    assert F(6931, 10000) < lo2 and hi2 < F(6932, 10000)
    assert harmonic(2, 4) - F(1, 4) == F(1, 3)                       # m = n = 2
    assert harmonic(4, 16) - F(3, 8) == F(664789, 720720)            # m = n = 4
    for w in range(1, 6):
        m = 2 ** w
        for r in range(w, w + 4):
            n = 2 ** r
            page = harmonic(n, m * n) - F(m - 1, 2 * n)
            d_lo, d_hi = w * lo2 - page, w * hi2 - page
            low = F(m - 1, 2 * n)
            assert low < d_lo
            assert d_hi < low + F(m - 1, m * n + 1)
            assert 0 < d_lo and d_hi < 1
            if r == w and w >= 2:
                assert d_lo > F(2, 5)
    return True


def sector_mean(m, n):
    """Mean entropy of the m-dimensional side on a parity sector of C^m x C^n, m <= n powers of two."""
    return harmonic(n // 2, m * n // 2) - F(m - 2, 2 * n)


def check_sector_deficit_bounds():
    premise("singularity.imported-page-average-entropy-subsystem")
    lo2, hi2 = ln2_bounds(60)
    ok = sector_mean(2, 2) == F(1, 2) and sector_mean(2, 4) == F(7, 12) and sector_mean(4, 4) == F(271, 280)
    ok = ok and sector_mean(4, 4) - (harmonic(4, 16) - F(3, 8)) == F(6553, 144144)
    for w in range(1, 6):
        m = 2 ** w
        for r in range(w, w + 4):
            n = 2 ** r
            page = harmonic(n, m * n) - F(m - 1, 2 * n)
            sec = sector_mean(m, n)
            # block decomposition: the weight term plus Page's average on a block of dimensions m/2, n/2
            block = harmonic(n // 2, m * n // 4) - F(m // 2 - 1, n) if m > 2 else F(0)
            ok = ok and sec == harmonic(m * n // 4, m * n // 2) + block
            # the rational difference from the abstract value and its bounds
            diff = sec - page
            ok = ok and F(1, 2 * m * n) < diff < F(1, 2 * (m * n + 1)) + F(1, 2 * n * (n + 1))
            # the sector deficit ln m - sec, enclosed through the enclosure of ln 2
            d_lo, d_hi = w * lo2 - sec, w * hi2 - sec
            ok = ok and F(m - 2, 2 * n) + F(2 * (m - 1), 2 * m * n + m + 1) < d_lo
            ok = ok and d_hi < F(m, 2 * n) - F(1, m * n) < F(1, 2)
            old_bound = F(m - 1, 2 * n)
            ok = ok and (d_lo > old_bound if m >= 4 else d_hi < old_bound)
            if r == w and w >= 2:
                ok = ok and F(2, 5) < d_lo and d_hi < F(1, 2)
    GA.check("sector mean entropy 1/2, 7/12, 271/280; block decomposition; rational difference from the abstract "
             "value within its bounds; sector deficit within its bounds, below 1/2, above (m-1)/(2n) for m >= 4 "
             "and below it at m = 2; in (2/5, 1/2) at the crossing from m = 4", ok)
    return ok


def exp_lower(x, terms):
    s, t = F(0), F(1)
    for j in range(terms):
        s += t
        t = t * x / (j + 1)
    return s


def check_eviction_deficits():
    premise("synthesis.imported-pinsker-inequality")
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("synthesis.boundary-mode-thermal-entropy")
    # zero weight: occupation 1/2, Pinsker bound 2 (p - 1/2)^2 = 0, deficit 0 at every stage
    p0 = 1 / (1 + peval([F(1)], 0))                 # 1/(e^0 + 1)
    assert p0 == F(1, 2) and 2 * (p0 - F(1, 2)) ** 2 == 0

    def log2_exact(p):
        """log_2 p for p a power of 2 (ln p = log_2 p * ln 2), found by search."""
        return next(e for e in range(-8, 9) if F(2) ** e == p)
    # mode entropy s(0) = -p ln p - (1 - p) ln(1 - p) at p = p0, in units of ln 2
    h0 = -(p0 * log2_exact(p0) + (1 - p0) * log2_exact(1 - p0))
    assert h0 == 1
    for size in range(1, 6):
        assert sum(1 - h0 for _ in range(size)) == 0          # delta_ev = sum (ln 2 - h_k) = 0
    # weights bounded away from zero: with E = e^{x_*}, p = 1/(E + 1) and 1/2 - p = tanh(x_*/2)/2, so the
    # Pinsker bound 2 (p - 1/2)^2 per member is (1/2) tanh^2(x_*/2); above 1 nat once |W| > 2/tanh^2(x_*/2)
    for E in (F(3), F(11, 2), F(40), F(501)):
        pE = 1 / (E + 1)
        t2 = ((E - 1) / (E + 1)) ** 2
        assert 2 * (pE - F(1, 2)) ** 2 == t2 / 2
        size = int(2 / t2) + 1
        assert size * t2 / 2 > 1 and (size - 1) * t2 / 2 <= 1
    # (Q) weights: x = 2 pi |k| >= 2 pi > 157/25 and exp(157/25) > 500
    assert exp_lower(F(157, 25), 40) > 500
    eta = F(1, 2) - F(1, 501)
    assert eta == F(499, 1002)
    per_member = 2 * eta ** 2                       # Pinsker lower bound, nats per member
    assert per_member > F(49, 100)
    page_upper = F(1)                               # from check_page_deficit_bounds
    assert 3 * per_member > page_upper and 2 * per_member < page_upper
    # sharper bound: H(p) < (ln 501 + 1)/501 < 8/501 for p < 1/501, since e^7 > 501
    assert exp_lower(F(7), 40) > 501
    lo2, hi2 = ln2_bounds(60)
    sharp = lo2 - F(8, 501)                         # nats per member with k != 0
    assert sharp > F(1, 2) and 2 * sharp > page_upper
    # the bound is linear in the number of nonzero-weight members
    for size in (3, 10, 100):
        assert size * per_member > F(size, 2) - F(size, 100)
    return True


if __name__ == "__main__":
    print(check_page_deficit_bounds(), check_eviction_deficits(), check_sector_deficit_bounds())
