"""synthesis.lowest-causal-residues-zero-four-content: exact checks.

Signatures (p, q): p generators of square +1, q of square -1. A causal signature has
min(p, q) = 1 and its time is the minority-sign generator. T14c's definitions
(obj.dark-tower-matter.ideals-fields-momentum): f = (1 + e_t e_a)/2, spinor ideal
S = Cl0(V) f, momentum j(psi) = <psi e_t rev(psi)>_1, squared mass m^2 = Q(e_t) Q(P).
In dimension six f is multiplied by the chiral projector (1 + I)/2, I the pseudoscalar,
to make it primitive. The check:
  (a) along every (1,1)-tower with ground of dimension <= 12 there is exactly one causal
      floor, the residue is constant, and the lowest causal dimension of residue r is
      min(r, 8 - r) + 2 (r = 0 gives 2);
  (b) at (1,1): Cl0 = R + R, S is one-dimensional, j(S) lies on one null ray, so every total
      momentum from S is null; the complementary ideal gives the opposite ray and one
      constituent from each has m^2 = 1;
  (c) at (1,5) and (5,1): S has dimension 8, its corner algebra dimension 4, Q(j(psi)) vanishes
      identically as a quartic form, and two constituents reach m^2 = 1/4;
  (d) the same machinery reproduces T14c's onsets at (1,3), (2,1) (two) and (1,4) (one);
  (e) unit-ball sums with pi bounded by 333/106 < pi < 355/113: P3's value lies inside
      5.364 +- 0.065, and adding the r = 4 lowest-causal term V3/V5 = 5/(2 pi) puts it between
      6.160 and 6.161, 12 to 13 standard errors above 5.364.
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from GA import mul, add, sub, scal, sc, gen, reverse, rank_of_vectors, all_blades
from tp_premise import premise


def squares(p, q):
    return tuple([1] * p + [-1] * q)


def setup(p, q, chiral=0):
    n = p + q
    s = squares(p, q)
    t = 0 if p == 1 else p
    a = 1 if t == 0 else 0
    f = scal(F(1, 2), add(sc(1), mul(gen(t), gen(a), s)))
    if chiral:
        vol = {tuple(range(n)): F(1)}
        f = mul(f, scal(F(1, 2), add(sc(1), scal(chiral, vol))), s)
    assert mul(f, f, s) == f
    blades = all_blades(n)
    even = [B for B in blades if len(B) % 2 == 0]
    rows, S = [], []
    for B in even:
        g = mul({B: F(1)}, f, s)
        cand = rows + [[g.get(C, F(0)) for C in blades]]
        if g and rank_of_vectors(cand) == len(cand):
            rows, S = cand, S + [g]
    corner = rank_of_vectors([[mul(mul(f, {B: F(1)}, s), f, s).get(C, F(0)) for C in blades]
                              for B in even])
    return dict(n=n, s=s, t=t, f=f, S=S, corner=corner, even=even)


def quaternion_units(D):
    """Two elements u, v of the corner fCl0f with u^2 = v^2 = -f and uv = -vu."""
    s, f = D["s"], D["f"]
    units = []
    for B in D["even"]:
        g = mul(mul(f, {B: F(1)}, s), f, s)
        if not g:
            continue
        g2 = mul(g, g, s)
        lam = g2.get((), F(0)) / f[()]
        if lam < 0 and g2 == scal(lam, f):
            units.append(scal(F(1), g))
    for u in units:
        for v in units:
            if add(mul(u, v, D["s"]), mul(v, u, D["s"])) == {}:
                return True
    return False


def mom(psi, D):
    x = mul(mul(psi, gen(D["t"]), D["s"]), reverse(psi), D["s"])
    return {B: c for B, c in x.items() if len(B) == 1}


def qv(u, v, s):
    return sum(c * v.get(B, F(0)) * s[B[0]] for B, c in u.items())


def single_null_identically(D):
    """Coefficients of the quartic form Q(j(sum_i x_i S_i)) all vanish."""
    S, s, k = D["S"], D["s"], len(D["S"])
    Jp = {}
    for i in range(k):
        for l in range(i, k):
            x = mul(mul(S[i], gen(D["t"]), s), reverse(S[l]), s)
            if i != l:
                x = add(x, mul(mul(S[l], gen(D["t"]), s), reverse(S[i]), s))
            Jp[(i, l)] = {B: c for B, c in x.items() if len(B) == 1}
    coef = {}
    for x in Jp:
        for y in Jp:
            mono = tuple(sorted(x + y))
            coef[mono] = coef.get(mono, F(0)) + qv(Jp[x], Jp[y], s)
    return all(c == 0 for c in coef.values())


def pair_mass(D, i, l):
    P = add(mom(D["S"][i], D), mom(D["S"][l], D))
    return D["s"][D["t"]] * qv(P, P, D["s"])


def check_lowest_causal_residues_zero_four_content():
    premise("dark-tower-matter.h1-momentum")
    premise("dark-tower-matter.where-mass-begins")
    premise("dark-tower-matter.constituents-field")
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    premise("dark-matter.towers-are-residues-single-clock-filter")
    premise("dark-matter.unit-ball-rule")

    # (a) one causal floor per tower; lowest causal dimension per residue
    lowest = {}
    for m in range(0, 13):
        for ground in ((m, 0), (0, m)):
            floors = [(ground[0] + k, ground[1] + k) for k in range(0, 9)]
            causal = [fl for fl in floors if min(fl) == 1]
            assert len(causal) == 1 and causal[0] == (ground[0] + 1, ground[1] + 1)
            assert len({(fl[0] - fl[1]) % 8 for fl in floors}) == 1
            r = (ground[0] - ground[1]) % 8
            d = sum(causal[0])
            lowest[r] = min(lowest.get(r, d), d)
    assert lowest == {r: min(r, 8 - r) + 2 for r in range(8)}
    assert lowest[0] == 2 and lowest[4] == 6 and lowest[6] == 4 and lowest[1] == 3

    # (b) residue 0 at (1,1): one ideal, one null ray, no mass; two ideals give mass
    D = setup(1, 1)
    assert len(D["S"]) == 1 and D["corner"] == 1
    j1 = mom(D["f"], D)
    assert j1 and qv(j1, j1, D["s"]) == 0
    assert pair_mass(D, 0, 0) == 0
    fbar = sub(sc(1), D["f"])
    j2 = mom(fbar, D)
    assert qv(j2, j2, D["s"]) == 0 and j2 != j1
    P = add(j1, j2)
    assert D["s"][D["t"]] * qv(P, P, D["s"]) == 1

    # (c) residue 4 at (1,5) and (5,1): mass begins at two
    for (p, q) in ((1, 5), (5, 1)):
        for chi in (1, -1):
            D = setup(p, q, chiral=chi)
            assert len(D["S"]) == 8 and D["corner"] == 4 and quaternion_units(D)
            assert single_null_identically(D)
            assert pair_mass(D, 0, 1) == F(1, 4)

    # (d) reproduce T14c's onsets
    D = setup(1, 3)
    assert len(D["S"]) == 4 and single_null_identically(D) and pair_mass(D, 0, 1) == 1
    D = setup(2, 1)
    assert len(D["S"]) == 2 and single_null_identically(D) and pair_mass(D, 0, 1) == 1
    D = setup(1, 4)
    assert len(D["S"]) == 8 and not single_null_identically(D)

    # (e) unit-ball sums, pi in (333/106, 355/113)
    lo, hi = F(333, 106), F(355, 113)
    obs, sig = F(5364, 1000), F(65, 1000)
    p3_lo, p3_hi = F(11, 3) + F(16, 3) / hi, F(11, 3) + F(16, 3) / lo
    assert obs - sig < p3_lo and p3_hi < obs + sig
    with_r4_lo = F(11, 3) + F(47, 6) / hi
    with_r4_hi = F(11, 3) + F(47, 6) / lo
    assert F(6160, 1000) < with_r4_lo and with_r4_hi < F(6161, 1000)
    assert obs + 12 * sig < with_r4_lo and with_r4_hi < obs + 13 * sig
    # 16/(3 pi) + 5/(2 pi) = 47/(6 pi)
    assert F(16, 3) + F(5, 2) == F(47, 6)
    return True
