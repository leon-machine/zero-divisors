"""synthesis.positive-energy-selects-rule-2-sign: exact checks (Fractions, GA engine).

For a real Clifford algebra Cl(p,q) the bivectors e_i e_j (i < j) span so(p,q) under the commutator.
A bivector whose two factors square alike squares to -1 (a rotation, compact); one whose factors
square oppositely squares to +1 (a boost).  The rotations span the maximal compact subalgebra k and
the boosts its complement p (the Cartan decomposition).  The checks compute the centre of k and the
action of a central element on p, for the two Rule 2 repairs of the obstructed extension of the
spacetime algebra, in both signature conventions.
"""
from fractions import Fraction as F
from itertools import combinations
from tp_premise import premise
import GA


def bivectors(n):
    return [(i, j) for i, j in combinations(range(n), 2)]


def setup(p, q):
    s = GA.sig(p, q)
    n = p + q
    blades = bivectors(n)
    B = [{b: F(1)} for b in blades]
    K = [x for x in B if GA.mul(x, x, s) == GA.sc(-1)]
    P = [x for x in B if GA.mul(x, x, s) == GA.sc(1)]
    return s, blades, K, P


def bracket(x, y, s):
    return GA.sub(GA.mul(x, y, s), GA.mul(y, x, s))


def centre_dim(p, q):
    """dim of the centre of k = span of the rotation bivectors, by exact linear algebra."""
    s, blades, K, P = setup(p, q)
    rows = []
    for kj in K:
        cols = [GA.basis_vector_of(bracket(ki, kj, s), blades) for ki in K]
        for r in range(len(blades)):
            rows.append([cols[i][r] for i in range(len(K))])
    return len(K) - GA.mat_rank(rows), len(K), len(P)


def obstructed_side(p, q):
    """rule2 (a): for even n = p + q, the spacelike extension Cl(p, q+1) is obstructed iff
    p - q = 2 mod 4, the timelike Cl(p+1, q) iff p - q = 0 mod 4."""
    return "s" if (p - q) % 4 == 2 else "t"


def repairs(p, q):
    """the opposite-sign and same-sign Rule 2 repairs of the obstructed extension (rule2 (c), (d))."""
    if obstructed_side(p, q) == "s":                 # extension squares -1
        return (p + 1, q + 1), (p, q + 2)
    return (p + 1, q + 1), (p + 2, q)


def check_repairs_and_centres():
    """For the base Cl(1,3) and its mirror Cl(3,1) the obstructed extension is the spacelike one;
    the opposite-sign repair is Cl(2,4) (resp. Cl(4,2)), the same-sign one Cl(1,5) (resp. Cl(3,3)).
    The compact part k has a one-dimensional centre for the opposite-sign repairs and none for the
    same-sign ones; dim k = 7 for (2,4), matching SO(2) x SO(4)."""
    premise("synthesis.imported-invariant-cone-classification")
    premise("rule2.where-obstruction-sits-commuting-square")
    premise("standard-model.imported-maximal-compact-subgroups")
    assert obstructed_side(1, 3) == "s" and obstructed_side(3, 1) == "s"
    assert repairs(1, 3) == ((2, 4), (1, 5))
    assert repairs(3, 1) == ((4, 2), (3, 3))
    out = {}
    for base in ((1, 3), (3, 1)):
        opp, same = repairs(*base)
        out[opp] = centre_dim(*opp)
        out[same] = centre_dim(*same)
    assert out[(2, 4)] == (1, 7, 8) and out[(4, 2)] == (1, 7, 8)
    assert out[(1, 5)] == (0, 10, 5) and out[(3, 3)] == (0, 6, 9)
    # the base itself (Lorentz algebra) has no centre in k either: positive energy is not a
    # Lorentz-group property, which is why it can discriminate only after the completion
    assert centre_dim(1, 3) == (0, 3, 3)


def check_central_element_is_fused_time_plane():
    """In Cl(2,4), with e_0 the time generator of Cl(1,3) and nu the opposite-sign repair generator
    (both squaring +1), Z = e_0 nu spans the centre of k, Z^2 = -1, ad(Z) vanishes on k and
    ad(Z)^2 = -4 on p: (1/2) ad(Z) is a complex structure on p (Hermitian type).  In Cl(1,5) the
    same plane (e_0 with the same-sign nu, nu^2 = -1) gives Z^2 = +1, a boost, not a rotation."""
    premise("synthesis.imported-invariant-cone-classification")
    premise("rule2.where-obstruction-sits-commuting-square")
    premise("field-theory.twistor-attachment")
    # generator order in GA.sig(2, 4): e_0, nu square +1; e_1, e_2, e_3 and the extension e_4 square -1
    s, blades, K, P = setup(2, 4)
    Z = GA.mul(GA.gen(0), GA.gen(1), s)
    assert GA.mul(Z, Z, s) == GA.sc(-1)
    for k in K:
        assert bracket(Z, k, s) == {}
    for x in P:
        assert bracket(Z, bracket(Z, x, s), s) == GA.scal(-4, x)
    # the extension e_4 and nu span a hyperbolic plane (rule2 (c)): (e_4 nu)^2 = +1, and the null
    # vectors (nu +- e_4)/2 square to zero
    w = GA.mul(GA.gen(5), GA.gen(1), s)
    assert GA.mul(w, w, s) == GA.sc(1)
    f = GA.scal(F(1, 2), GA.add(GA.gen(1), GA.gen(5)))
    assert GA.mul(f, f, s) == {}
    # mirror: GA.sig(4, 2) has e_1, e_2, e_3 and nu squaring +1 (indices 0-3) and the base time
    # direction and the extension squaring -1 (indices 4, 5); the central rotation is their product,
    # and time times nu is a boost there
    s4, blades4, K4, P4 = setup(4, 2)
    Zm = GA.mul(GA.gen(4), GA.gen(5), s4)
    assert GA.mul(Zm, Zm, s4) == GA.sc(-1)
    for k in K4:
        assert bracket(Zm, k, s4) == {}
    for x in P4:
        assert bracket(Zm, bracket(Zm, x, s4), s4) == GA.scal(-4, x)
    tn = GA.mul(GA.gen(4), GA.gen(3), s4)
    assert GA.mul(tn, tn, s4) == GA.sc(1)
    # same-sign repair: GA.sig(1, 5) has e_0 squaring +1 and nu among the -1 generators
    s2, blades2, K2, P2 = setup(1, 5)
    Z2 = GA.mul(GA.gen(0), GA.gen(5), s2)
    assert GA.mul(Z2, Z2, s2) == GA.sc(1)
    # and no rotation of Cl(1,5) is central in its k: each fails to commute with some rotation
    for k in K2:
        assert any(bracket(k, k2, s2) != {} for k2 in K2)


EXPORTS = {}
