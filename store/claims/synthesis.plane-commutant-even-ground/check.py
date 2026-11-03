"""synthesis.plane-commutant-even-ground: the relative commutant of the tower's planes."""
from fractions import Fraction as F
import GA
from tp_premise import premise


def floor_squares(p, q, k):
    return tuple([1] * p + [-1] * q + [1, -1] * k)


def commutant_blades(sq, gens):
    return [B for B in GA.all_blades(len(sq))
            if all(GA.commutes({B: F(1)}, GA.gen(g), sq) for g in gens)]


def even_relations(sq):
    n = len(sq)
    u = [GA.mul(GA.gen(i), GA.gen(n - 1), sq) for i in range(n - 1)]
    squares = [GA.mul(a, a, sq) for a in u]
    anti = all(GA.anticommutes(u[i], u[j], sq) for i in range(n - 1) for j in range(i + 1, n - 1))
    return squares, anti


def test_plane_commutant():
    premise("tower.algebraic-limit-even-charge")
    premise("tower.commuting-copies")
    premise("tower.volume-elements-planes")
    premise("tower.rigidity-clock-frozen")
    premise("transport.classification-real-clifford-algebras")   # the table of types read in Step 3
    SIGS = [(1, 0), (0, 1), (2, 1), (1, 2), (3, 0), (0, 0), (1, 1), (2, 0), (0, 2), (1, 3), (3, 1)]
    for (p, q) in SIGS:
        n = p + q
        even_ground = sorted(B for B in GA.all_blades(n) if len(B) % 2 == 0)
        for k in range(3):
            sq1 = floor_squares(p, q, k + 1)
            if len(sq1) > 9:
                continue
            planes = list(range(n, n + 2 * (k + 1)))
            inside = sorted(B for B in commutant_blades(sq1, planes) if all(i < n + 2 * k for i in B))
            assert inside == even_ground
            if k >= 1:
                sq = floor_squares(p, q, k)
                assert len(commutant_blades(sq, list(range(n, n + 2 * k)))) == 2 ** n
    GA.check("the elements commuting with every plane generator are exactly Cl^0(p,q)", True)
    for (p, q) in [(1, 3), (2, 4), (1, 2), (3, 0), (2, 1), (4, 1), (1, 4), (2, 3)]:
        sq = floor_squares(p, q, 0)
        rev = tuple(-c for c in sq)
        assert even_relations(sq) == even_relations(rev) and even_relations(sq)[1]
    for (p, q), want in [((1, 1), 1), ((2, 2), 1), ((0, 4), 1), ((4, 0), 1), ((1, 5), 1),
                         ((2, 0), -1), ((0, 2), -1), ((1, 3), -1), ((3, 1), -1), ((2, 4), -1)]:
        sq = floor_squares(p, q, 0)
        n = p + q
        ev = [B for B in GA.all_blades(n) if len(B) % 2 == 0]
        Z = [B for B in ev if all(GA.commutes({B: F(1)}, {C: F(1)}, sq) for C in ev if len(C) == 2)]
        assert sorted(Z) == sorted([(), tuple(range(n))])
        om = {tuple(range(n)): F(1)}
        assert GA.mul(om, om, sq) == GA.sc(want)
    for (p, q) in [(1, 0), (0, 1), (2, 1), (1, 2), (3, 0), (0, 3), (2, 3), (3, 2)]:
        sq = floor_squares(p, q, 0)
        n = p + q
        ev = [B for B in GA.all_blades(n) if len(B) % 2 == 0]
        assert [B for B in ev if all(GA.commutes({B: F(1)}, {C: F(1)}, sq) for C in ev if len(C) == 2)] == [()]
    GA.check("Cl^0 has one presentation for r and -r; its centre separates the parity and, for even "
             "charge, {2, 6} from {0} and {4}", True)
