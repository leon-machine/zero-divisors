"""synthesis.array-capacity-in-charge-sector-one-channel: exact checks.

The (Q) array on the window k = -L..L, weights kappa*k (units of kappa), sea filled below k = 0.
A configuration is a set of occupied sites; its charge relative to the sea is
Q = #(occupied k >= 0) - #(empty k < 0) and its energy E = sum of k over occupied k >= 0
plus sum of |k| over empty k < 0.  Everything is integer counting.

(i)   for every E <= L the number of configurations of charge Q and energy E equals
      p(E - Q(Q-1)/2) (partitions; zero when negative): the window's Fock space is charge
      sectors with ground energies Q(Q-1)/2 tensored with one bosonic oscillator tower;
(ii)  the zero-energy configurations are exactly two, of charges 0 and 1 (the zero-mode doublet);
      with the sea between sites (weights k + 1/2) the ground energies are Q^2/2, the tower is
      the same, and the zero-energy configuration is unique;
(iii) the currents a_m preserve the charge: on Jordan-Wigner matrices for 5 sites,
      [N_tot, a_m] = 0, and a_m has no matrix element between the two doublet states;
(iv)  one oscillator tower, not two: the charge-0 level counts 1, 1, 2, 3, 5, 7 are p(E), and
      the count at E = 1 is 1, whereas two independent towers (both helicities) give 2.
"""
from fractions import Fraction as F
from itertools import product
import GA
from GA import pmul, ptrim
from tp_premise import premise


def partitions(nmax):
    """p(0..nmax) from the generating function prod 1/(1-q^m), via GA polynomial products."""
    series = [F(1)] + [F(0)] * nmax
    for m in range(1, nmax + 1):
        geo = [F(0)] * (nmax + 1)
        for j in range(0, nmax + 1, m):
            geo[j] = F(1)
        series = (pmul(series, geo) + [F(0)] * (nmax + 1))[:nmax + 1]
    return [int(x) for x in series]


def configs(L):
    sites = list(range(-L, L + 1))
    for occ in product((0, 1), repeat=len(sites)):
        q = 0
        e = 0
        for k, o in zip(sites, occ):
            if k >= 0 and o:
                q += 1
                e += k
            if k < 0 and not o:
                q -= 1
                e += -k
        yield q, e


def counts(L):
    table = {}
    for q, e in configs(L):
        table[(q, e)] = table.get((q, e), 0) + 1
    return table


def counts_between_sites(L):
    """Sea between sites: weights k + 1/2; returns counts keyed by (Q, 2E)."""
    sites = list(range(-L, L))
    table = {}
    for occ in product((0, 1), repeat=len(sites)):
        q = 0
        e2 = 0
        for k, o in zip(sites, occ):
            if k >= 0 and o:
                q += 1
                e2 += 2 * k + 1
            if k < 0 and not o:
                q -= 1
                e2 += -2 * k - 1
        table[(q, e2)] = table.get((q, e2), 0) + 1
    return table


def check_charge_times_oscillator():
    premise("synthesis.imported-jacobi-triple-product")
    premise("singularity.bosonisation-bridge-s-wave-sector")
    premise("hawking.imported-s-wave-bosonic-sector")
    L = 6
    p = partitions(L)
    table = counts(L)
    for e in range(0, L + 1):
        for q in range(-L - 1, L + 2):
            g = q * (q - 1) // 2
            want = p[e - g] if e - g >= 0 else 0
            assert table.get((q, e), 0) == want
    # the zero-mode doublet: two zero-energy configurations, charges 0 and 1
    zero = sorted(q for (q, e), c in table.items() if e == 0 for _ in range(c))
    assert zero == [0, 1]
    # the other particle-hole symmetric offset (sea between sites): ground energies Q^2/2,
    # the same tower, and a unique zero-energy configuration
    tb = counts_between_sites(L)
    for e2 in range(0, 2 * L + 1):
        for q in range(-L - 1, L + 2):
            rest = e2 - q * q
            want = p[rest // 2] if rest >= 0 and rest % 2 == 0 else 0
            assert tb.get((q, e2), 0) == want
    zero_b = [q for (q, e2), c in tb.items() if e2 == 0 for _ in range(c)]
    assert zero_b == [0]
    return True


def zeros(n):
    return [[F(0)] * n for _ in range(n)]


def mm(a, b):
    n = len(a)
    out = zeros(n)
    for i in range(n):
        for t in range(n):
            if a[i][t]:
                for j in range(n):
                    if b[t][j]:
                        out[i][j] += a[i][t] * b[t][j]
    return out


def check_currents_blind_to_doublet():
    premise("synthesis.imported-jacobi-triple-product")
    premise("hawking.current-commutator-exactly-edge-split")
    premise("synthesis.residue-from-mode-entropy")
    L = 5                       # sites k = -2..2, bit i <-> site i - 2
    dim = 2 ** L
    cs = []
    for k in range(L):
        c = zeros(dim)
        for s in range(dim):
            if (s >> k) & 1:
                sign = -1 if bin(s & ((1 << k) - 1)).count("1") % 2 else 1
                c[s ^ (1 << k)][s] = F(sign)
        cs.append(c)
    cd = [[[c[j][i] for j in range(dim)] for i in range(dim)] for c in cs]
    ntot = zeros(dim)
    for s in range(dim):
        ntot[s][s] = F(bin(s).count("1"))
    sea = 0b00011                # sites -2, -1 filled
    up = sea | (1 << 2)          # plus the zero mode k = 0
    for m in (1, 2, 3):
        a = zeros(dim)
        for k in range(L - m):
            t = mm(cd[k], cs[k + m])
            for i in range(dim):
                for j in range(dim):
                    a[i][j] += t[i][j]
        comm = [[x - y for x, y in zip(r1, r2)] for r1, r2 in zip(mm(ntot, a), mm(a, ntot))]
        assert all(x == 0 for row in comm for x in row)
        for b in (a, [[a[j][i] for j in range(dim)] for i in range(dim)]):
            assert b[up][sea] == 0 and b[sea][up] == 0
    # the charge current a_0 (the charge) reads the doublet without connecting it
    assert ntot[up][up] - ntot[sea][sea] == 1 and ntot[up][sea] == 0 and ntot[sea][up] == 0
    # the zero mode itself is reached by a fermion, not by a current
    assert cd[2][up][sea] != 0
    return True


def check_one_tower_not_two():
    premise("synthesis.imported-jacobi-triple-product")
    premise("hawking.helicity-lift-joints-itemised")
    premise("synthesis.capacity-per-mode-independent-of-helicity")
    L = 6
    table = counts(L)
    level = [table.get((0, e), 0) for e in range(L + 1)]
    assert level == [1, 1, 2, 3, 5, 7, 11]
    # two independent oscillator towers (one per helicity): coefficients of prod 1/(1-q^m)^2
    p = partitions(L)
    two = [sum(p[i] * p[e - i] for i in range(e + 1)) for e in range(L + 1)]
    assert two == [1, 2, 5, 10, 20, 36, 65]
    assert level[1] == 1 and two[1] == 2
    assert all(level[e] < two[e] for e in range(1, L + 1))
    return True


if __name__ == "__main__":
    print(partitions(8))
    for f in (check_charge_times_oscillator, check_currents_blind_to_doublet, check_one_tower_not_two):
        print(f.__name__, f())
