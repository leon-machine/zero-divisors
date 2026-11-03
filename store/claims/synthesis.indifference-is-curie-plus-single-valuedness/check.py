"""synthesis.indifference-is-curie-plus-single-valuedness: exact checks.

Finite group actions on finite sets, with exact rational weights.

  (1) The reversal (p, q) -> (q, p) acts on residues r = p - q mod 8 as r -> -r, computed from
      the signatures (p, q) with p, q <= 4 (GA's signature tuples): five orbits {0}, {4}, {1,7}, {2,6}, {3,5}.
      The invariant weight assignments are the functions constant on orbits (dimension five, the
      image of the averaging projection); for every pair x, y in different orbits the indicator of
      the orbit of x is invariant and separates them, so invariance licenses no equality across orbits.
  (2) Haar on an orbit: the only invariant probability on {2, 6} is (1/2, 1/2); the averaging
      projection is idempotent and equivariant.
  (3) Maximum entropy over all eight residues (the uniform distribution) is invariant but equates
      residues of different orbits; at fixed orbit totals the invariant assignment is unique.
  (4) A many-valued construction: under the swap of {2, 6} the outcome set {(1, 0), (0, 1)} is
      invariant and contains no invariant element; a single-valued equivariant construction
      (here: the average of any invariant outcome set) is invariant.
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise


def residue(p, q):
    return (p - q) % 8


def reversal_orbits():
    seen, orbits = set(), []
    for p, q in product(range(5), repeat=2):
        sq = GA.sig(p, q)
        r = residue(sq.count(1), sq.count(-1))
        rr = residue(sq.count(-1), sq.count(1))
        if r not in seen:
            orb = sorted({r, rr})
            seen.update(orb)
            orbits.append(orb)
    return sorted(orbits)


def act(f):
    """reversal on a weight vector indexed by residue"""
    return [f[(-r) % 8] for r in range(8)]


def average(f):
    g = act(f)
    return [(a + b) / 2 for a, b in zip(f, g)]


def rank(rows):
    M = [list(r) for r in rows]
    rk, col = 0, 0
    while rk < len(M) and col < len(M[0]):
        piv = next((i for i in range(rk, len(M)) if M[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for i in range(len(M)):
            if i != rk and M[i][col] != 0:
                fac = M[i][col] / M[rk][col]
                M[i] = [x - fac * y for x, y in zip(M[i], M[rk])]
        rk += 1
        col += 1
    return rk


def check_orbits_and_invariant_assignments():
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    premise("dark-tower-matter.mirrors-temperature-p2")
    orbits = reversal_orbits()
    assert orbits == [[0], [1, 7], [2, 6], [3, 5], [4]]
    basis = [[F(int(r == s)) for s in range(8)] for r in range(8)]
    images = [average(e) for e in basis]
    assert rank(images) == 5
    for f in images:
        assert act(f) == f and average(f) == f
    orbit_of = {r: tuple(o) for o in orbits for r in o}
    for x, y in product(range(8), repeat=2):
        ind = [F(int(s in orbit_of[x])) for s in range(8)]
        assert act(ind) == ind
        if orbit_of[x] != orbit_of[y]:
            assert ind[x] != ind[y]
        else:
            assert all(g[x] == g[y] for g in images)


def check_haar_on_orbit_and_maxent_overreach():
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    premise("dark-tower-matter.mirrors-temperature-p2")
    # invariant probabilities supported on {2, 6}: w2 = w6 and w2 + w6 = 1
    sols = [(a, F(1) - a) for a in (F(k, 8) for k in range(9))]
    inv = [s for s in sols if act([F(0), F(0), s[0], F(0), F(0), F(0), s[1], F(0)])
           == [F(0), F(0), s[0], F(0), F(0), F(0), s[1], F(0)]]
    assert inv == [(F(1, 2), F(1, 2))]
    uni = [F(1, 8)] * 8
    assert act(uni) == uni and uni[0] == uni[2]
    # at fixed orbit totals the invariant assignment is unique (Haar on each orbit)
    totals = {(0,): F(1, 10), (1, 7): F(1, 5), (2, 6): F(2, 5), (3, 5): F(1, 5), (4,): F(1, 10)}
    w = [F(0)] * 8
    for orb, t in totals.items():
        for r in orb:
            w[r] = t / len(orb)
    assert act(w) == w and sum(w) == 1 and w[2] == w[6] == F(1, 5) and w[0] != w[2]


def check_many_valued_outcome_has_no_invariant_member():
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    premise("dark-tower-matter.mirrors-temperature-p2")

    def swap(v):
        return (v[1], v[0])
    outcomes = {(F(1), F(0)), (F(0), F(1))}
    assert {swap(v) for v in outcomes} == outcomes
    assert all(swap(v) != v for v in outcomes)
    # a single-valued equivariant construction on the same data: the barycentre
    bary = tuple(sum(v[i] for v in outcomes) / len(outcomes) for i in range(2))
    assert swap(bary) == bary and bary == (F(1, 2), F(1, 2))
    # the temperature datum on the reversal orbit {2, 6}: a single-valued covariant outcome forces
    # T_2 = T_6 (xi = 1, the value the record excludes); a cold mirror needs a many-valued outcome
    xi = F(1, 3)
    temps = {(F(1), xi), (xi, F(1))}
    assert {swap(v) for v in temps} == temps and all(swap(v) != v for v in temps)
    single = [(a, b) for a, b in product([F(k, 3) for k in range(1, 4)], repeat=2) if swap((a, b)) == (a, b)]
    assert all(a == b for a, b in single) and len(single) == 3
    # three-element case: the cyclic group on three labels, outcome set of three selections
    cyc = [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))]

    def rot(v):
        return (v[2], v[0], v[1])
    assert {rot(v) for v in cyc} == set(cyc)
    assert all(rot(v) != v for v in cyc)
