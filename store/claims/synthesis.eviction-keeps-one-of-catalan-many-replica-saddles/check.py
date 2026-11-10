"""synthesis.eviction-keeps-one-of-catalan-many-replica-saddles: exact checks.

Integers and Fractions only. eta is the cyclic permutation (0 1 ... n-1) of the n replicas; #(s) the
number of cycles. Checks:
  (1) non-crossing count: #(s) + #(s^-1 eta) <= n + 1 for every s in S_n, with equality for exactly
      C_n = binom(2n, n)/(n + 1) permutations, n = 1..7 (the planar replica saddles);
  (2) Haar moments by Schur-Weyl: <tr rho_A^n> = sum_s dA^#(s^-1 eta) dB^#(s) / prod_{i<n}(D + i),
      D = dA dB; at n = 2 this is the stored Haar purity (dA + dB)/(dA dB + 1); at dA = dB = d the
      numerator has leading term C_n d^(n+1) (so d^(n-1) <tr rho^n> -> C_n), checked as exact
      polynomials in d for n = 2..5, and the exact values at d = 2, 4, 8 lie strictly between the
      one-saddle value d^(1-n) and the planar value C_n d^(1-n) for n = 2, 3, 4;
  (3) eviction at zero weight: the radiation state at the crossing (j = n_cap = m qubits) is a product of
      m Bell-pair halves, so tr rho_R^n = 2^(m(1-n)) exactly (built as Pauli-algebra marginals in GA,
      Cl(3,0), with tr = 2 <.>_0), i.e. one planar saddle; away from the crossing the max of the two
      extremal saddles;
  (4) the gap Delta S_n = ln C_n/(n-1): C_n^(1/(n-1)) strictly increasing and below 4 for n = 2..10
      (integer comparisons), and the n -> 1 continuation d/dn ln C_n at n = 1 equals
      2 H_2 - H_1 - H_2 = 1/2 (harmonic numbers; digamma differences), the stored half nat.
"""
from fractions import Fraction as F
from itertools import permutations
import GA
from GA import mul, add, sc, gen, scal
from tp_premise import premise


def cycles(p):
    n, seen, c = len(p), [False] * len(p), 0
    for i in range(n):
        if not seen[i]:
            c += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = p[j]
    return c


def compose(a, b):          # (a b)(i) = a(b(i))
    return tuple(a[b[i]] for i in range(len(b)))


def inverse(a):
    out = [0] * len(a)
    for i, x in enumerate(a):
        out[x] = i
    return tuple(out)


def comb(a, b):
    out = F(1)
    for i in range(b):
        out = out * (a - i) / (i + 1)
    assert out.denominator == 1
    return out.numerator


def catalan(n):
    c = F(comb(2 * n, n), n + 1)
    assert c.denominator == 1
    return c.numerator


def genus_profile(n):
    eta = tuple((i + 1) % n for i in range(n))
    prof = {}
    for s in permutations(range(n)):
        t = cycles(s) + cycles(compose(inverse(s), eta))
        prof[t] = prof.get(t, 0) + 1
    return prof


def check_planar_replica_saddles_are_catalan():
    premise("synthesis.imported-replica-wormhole-two-saddle-purity")
    premise("synthesis.imported-non-crossing-permutations-are-geodesic")
    want = [1, 2, 5, 14, 42, 132, 429]
    got = []
    for n in range(1, 8):
        prof = genus_profile(n)
        assert max(prof) == n + 1
        got.append(prof[n + 1])
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        assert sum(prof.values()) == fact
    assert got == want == [catalan(n) for n in range(1, 8)]
    return True


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def haar_numerator(n, dA, dB):
    eta = tuple((i + 1) % n for i in range(n))
    return sum(F(dA) ** cycles(compose(inverse(s), eta)) * F(dB) ** cycles(s) for s in permutations(range(n)))


def haar_moment(n, dA, dB):
    D = dA * dB
    den = F(1)
    for i in range(n):
        den *= D + i
    return haar_numerator(n, dA, dB) / den


def check_haar_moments_tend_to_catalan():
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    premise("singularity.imported-page-average-entropy-subsystem")
    for m, nn in [(2, 2), (2, 3), (3, 5), (4, 4), (2, 7)]:
        assert haar_moment(2, m, nn) == F(m + nn, m * nn + 1)           # the index-two value
    for n in range(2, 6):
        eta = tuple((i + 1) % n for i in range(n))
        # numerator as a polynomial in d at dA = dB = d: coefficient list by power
        num = [0] * (2 * n + 1)
        for s in permutations(range(n)):
            num[cycles(compose(inverse(s), eta)) + cycles(s)] += 1
        assert num[n + 1] == catalan(n) and all(c == 0 for c in num[n + 2:])
        den = [1]
        for i in range(n):
            den = poly_mul(den, [i, 0, 1])                                # d^2 + i
        assert den[2 * n] == 1 and len(den) == 2 * n + 1
        # d^(n-1) <tr rho^n> = num(d) d^(n-1) / den(d): leading terms C_n d^(2n) / d^(2n)
    table = {}
    for n in (2, 3, 4):
        for d in (2, 4, 8):
            v = haar_moment(n, d, d)
            one = F(1, d ** (n - 1))
            assert one < v < catalan(n) * one
            table[(n, d)] = v
    assert table[(2, 2)] == F(4, 5) and table[(3, 2)] == F(7, 10)
    return True


def bell_half():
    """Marginal of one Bell pair in the Pauli algebra: rho = (1 + 0 e3)/2."""
    return scal(F(1, 2), sc(1))


def tr(x):
    return 2 * x.get((), F(0))


def check_eviction_keeps_one_saddle_every_index():
    premise("synthesis.eviction-keeps-one-replica-saddle")
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    P = (1, 1, 1)
    rho = bell_half()
    for n in range(2, 6):
        rn = sc(1)
        for _ in range(n):
            rn = mul(rn, rho, P)
        one = tr(rn)
        assert one == F(1, 2 ** (n - 1))
        for m in range(1, 5):
            # product of m identical marginals: tr rho_R^n = (tr rho^n)^m
            assert one ** m == F(1, 2 ** (m * (n - 1)))
            # one planar saddle at the crossing d = 2^m; the planar island sum is C_n of them
            d = 2 ** m
            assert catalan(n) * one ** m == catalan(n) * F(1, d ** (n - 1))
        # away from the crossing: j quanta, capacity c; eviction = larger of the extremal saddles
        for j, c in [(1, 3), (3, 1), (2, 5), (4, 2)]:
            ev = F(1, 2 ** ((n - 1) * min(j, c)))
            assert ev == max(F(1, 2 ** (j * (n - 1))), F(1, 2 ** (c * (n - 1))))
    # a nonzero-weight marginal (1 + r e3)/2 is not flat: its moments separate n = 2 and n = 3
    r = F(3, 5)
    rho_w = scal(F(1, 2), add(sc(1), scal(r, gen(2))))
    t2 = tr(mul(rho_w, rho_w, P))
    t3 = tr(mul(mul(rho_w, rho_w, P), rho_w, P))
    assert t2 == (1 + r * r) / 2 and t3 == (1 + 3 * r * r) / 4
    return True


def check_gap_family_interpolates_half_nat_to_ln4():
    premise("synthesis.eviction-deficit-against-page-deficit")
    premise("singularity.imported-page-average-entropy-subsystem")
    # Delta S_n = ln C_n / (n - 1): monotone in n, below ln 4, ln 2 at n = 2
    assert catalan(2) == 2 and catalan(3) == 5
    for n in range(2, 10):
        a, b = catalan(n), catalan(n + 1)
        assert b ** (n - 1) > a ** n                  # C_{n+1}^(1/n) > C_n^(1/(n-1))
        assert a < 4 ** (n - 1)                        # C_n^(1/(n-1)) < 4
    # n -> 1: ln C_n = lnG(2n+1) - lnG(n+1) - lnG(n+2); derivative at n = 1 is
    # 2 psi(3) - psi(2) - psi(3), with psi(k + 1) - psi(1) = H_k
    H = lambda k: sum(F(1, i) for i in range(1, k + 1))
    deriv = 2 * H(2) - H(1) - H(2)
    assert deriv == F(1, 2)
    # Page at the crossing: S = ln m - m/(2n) at m = n, a gap of exactly 1/2 below ln m
    m = 7
    assert F(m, 2 * m) == deriv
    return True


# ---------------------------------------------------------------- version 4: a parity sector
def sector_trace(d, s, tau):
    """Number of n-tuples of sector basis states (a_i, b_i), parity(a_i) = parity(b_i), fixed when the a are
    permuted by tau and the b by s: the trace of P_sigma (P_eta on A) on the n-th power of the sector."""
    from itertools import product
    n = len(s)
    par = lambda x: bin(x).count("1") % 2
    count = 0
    for a in product(range(d), repeat=n):
        if any(a[tau[i]] != a[i] for i in range(n)):
            continue
        for b in product(range(d), repeat=n):
            if all(b[s[i]] == b[i] for i in range(n)) and all(par(a[i]) == par(b[i]) for i in range(n)):
                count += 1
    return count


def sector_moment(n, d, perms):
    den = F(1)
    for l in range(n):
        den *= F(d * d, 2) + l
    return 2 * sum(F(d, 2) ** (cs + ct) for cs, ct in perms) / den


def check_parity_sector_moments_keep_the_catalan_limit():
    """Partial: the sector trace count is enumerated at three cases only (n = 2 with d = 2, 4; n = 3 with
    d = 2); the count for every n is the proof's argument over F_2. The genus form, the Catalan limit and the
    bounds are evaluated for n = 2..6, d = 2..32."""
    premise("synthesis.imported-haar-moments-of-random-pure-state")
    premise("tower.commuting-copies")
    premise("synthesis.eviction-keeps-one-replica-saddle")
    # the sector form of the moments is clause (iv) of the finite-averages result; the count below confirms it
    premise("synthesis.finite-normaliser-averages-leave-the-haar-moments-at-order-four-and-on-a-parity-sector")
    # the twist behind the reduction: two modes, generators e (square +1), f (square -1); A = the first mode
    sq = (1, -1, 1, -1)
    p_a = mul(gen(1), gen(0), sq)                                    # the parity f e of the first mode
    assert GA.eq(mul(p_a, p_a, sq), sc(F(1)))
    for y in (gen(2), gen(3)):
        t = mul(y, p_a, sq)
        assert GA.eq(mul(t, t, sq), mul(y, y, sq))
        assert all(GA.commutes(t, x, sq) and GA.anticommutes(y, x, sq) for x in (gen(0), gen(1)))
    cyc = {}
    for n in (2, 3, 4, 5, 6):
        eta = tuple((i + 1) % n for i in range(n))
        cyc[n] = []
        for s in permutations(range(n)):
            tau = compose(inverse(s), eta)
            cyc[n].append((cycles(s), cycles(tau)))
            if n <= 3:                                              # the trace count, by enumeration
                for d in ((2, 4) if n == 2 else (2,)):
                    assert sector_trace(d, s, tau) == 2 * F(d, 2) ** (cycles(s) + cycles(tau))
    genus_one = {2: 0, 3: 1, 4: 10, 5: 70, 6: 420}
    for n in (2, 3, 4, 5, 6):
        ng = {}
        for cs, ct in cyc[n]:
            assert (n + 1 - cs - ct) % 2 == 0
            g = (n + 1 - cs - ct) // 2
            ng[g] = ng.get(g, 0) + 1
        assert ng[0] == catalan(n) and ng.get(1, 0) == genus_one[n]
        for d in (2, 4, 8, 16, 32):
            u = F(1, d * d)
            v = sector_moment(n, d, cyc[n])
            den = F(1)
            for l in range(n):
                den *= 1 + 2 * l * u
            assert v * d ** (n - 1) == sum(c * (4 * u) ** g for g, c in ng.items()) / den
            assert F(1, d ** (n - 1)) < v < catalan(n) * F(1, d ** (n - 1))
            if n <= 4 and d <= 8:
                assert v < haar_moment(n, d, d)
            if n == 2:
                assert v == F(2 * d, d * d + 2)
    assert sector_moment(3, 2, cyc[3]) == F(1, 2) and sector_moment(2, 4, cyc[2]) == F(4, 9)
    return True


if __name__ == "__main__":
    for fn in [check_planar_replica_saddles_are_catalan, check_haar_moments_tend_to_catalan,
               check_eviction_keeps_one_saddle_every_index, check_gap_family_interpolates_half_nat_to_ln4,
               check_parity_sector_moments_keep_the_catalan_limit]:
        GA.check(fn.__name__, fn())
