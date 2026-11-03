"""dark-matter.superselected-hence-dark-exactly-stable: exact checks of the algebraic steps.

Step (2), the ascent stays in its tower: for every (p,q) with p + q <= 6, adjoining a null pair
(Gram block [[0,1],[1,0]] beside diag(+1 x p, -1 x q)) gives congruence signature (p+1, q+1), so
p - q is preserved exactly, not only mod 8, and no sequence of ascents joins two residues; adjoining
a definite plane ((2,0) or (0,2)) instead moves the residue by +-2 (control). The completion is
Mat_2 of the old algebra: in Cl(p+1, q+1) the elements e_i e_+ e_- (old generators times the unit
square of the new pair) satisfy the relations of Cl(p,q), commute with e_+ and e_-, and with them
span all 2^(n+2) dimensions (n <= 4), so Cl(p+1, q+1) = Cl(p,q) (x) Cl(1,1) = Mat_2(Cl(p,q)).
Step (1), the soldering obstruction for the six populated representatives (1,3), (3,1), (2,1),
(1,2), (4,1), (1,4): a map carrying one generating subspace onto another and respecting v^2 = g(v,v)
is an isometry of the Gram forms, and the congruence signatures (also after a rational change of
basis) differ for every pair of distinct residues, so no such map exists.
Not computable here: the sector decomposition itself, the wall-sequence theorem's analysis, and the
acoustic no-go behind the darkness clause.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

POPULATED = [(1, 3), (3, 1), (2, 1), (1, 2), (4, 1), (1, 4)]
BASIS_CHANGE = [[1, 2, 0, 0, 1], [0, 1, 0, 3, 0], [0, 3, 1, 0, 0], [1, 0, 0, 1, 2], [0, 0, 1, 0, 1]]


def gram_diag(p, q):
    n = p + q
    return [[F(0) if i != j else F(1 if i < p else -1) for j in range(n)] for i in range(n)]


def adjoin(G, block):
    n = len(G)
    out = [row + [F(0), F(0)] for row in G] + [[F(0)] * n + [F(x) for x in r] for r in block]
    return out


def check_ascent_preserves_residue():
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    count = 0
    for n in range(0, 7):
        for p in range(n + 1):
            q = n - p
            G = gram_diag(p, q)
            up = GA.congruence_signature(adjoin(G, [[0, 1], [1, 0]]))
            assert up == (p + 1, q + 1, 0)
            assert (up[0] - up[1]) == p - q
            sp = GA.congruence_signature(adjoin(G, [[1, 0], [0, 1]]))
            tm = GA.congruence_signature(adjoin(G, [[-1, 0], [0, -1]]))
            assert (sp[0] - sp[1] - (p - q)) % 8 == 2 and (tm[0] - tm[1] - (p - q)) % 8 == 6
            count += 1
    assert count == 28
    return True


def span_rank(elems, n):
    bl = GA.all_blades(n)
    return GA.rank_of_vectors([[x.get(b, F(0)) for b in bl] for x in elems])


def check_completion_is_matrix_amplification():
    premise("dark-matter.imported-eight-towers-mod-8-clock")
    for n in range(1, 5):
        for p in range(n + 1):
            q = n - p
            sq = GA.sig(p + 1, q + 1)          # old generators: indices 0..p-1 (+), p+1..p+q (-)
            plus, minus = p, p + q + 1          # the adjoined pair: e_+ at index p, e_- at the end
            old = [i for i in range(p + q + 2) if i not in (plus, minus)]
            unit = GA.mul(GA.gen(plus), GA.gen(minus), sq)
            assert GA.eq(GA.mul(unit, unit, sq), GA.sc(1))
            f = [GA.mul(GA.gen(i), unit, sq) for i in old]
            for a, i in enumerate(old):
                assert GA.eq(GA.mul(f[a], f[a], sq), GA.sc(sq[i]))
                assert GA.commutes(f[a], GA.gen(plus), sq) and GA.commutes(f[a], GA.gen(minus), sq)
            for a, b in combinations(range(len(f)), 2):
                assert GA.anticommutes(f[a], f[b], sq)
            words = []
            for k in range(len(f) + 1):
                for S in combinations(range(len(f)), k):
                    w = GA.sc(1)
                    for a in S:
                        w = GA.mul(w, f[a], sq)
                    for m in (GA.sc(1), GA.gen(plus), GA.gen(minus), unit):
                        words.append(GA.mul(w, m, sq))
            assert span_rank(words, p + q + 2) == 2 ** (n + 2)
    return True


def check_no_soldered_map_between_residues():
    premise("dark-matter.residue-soldered-invariant-not-algebraic-one")
    sigs = {}
    for p, q in POPULATED:
        n = p + q
        T = [row[:n] for row in BASIS_CHANGE[:n]]
        G = gram_diag(p, q)
        G2 = [[sum(F(T[i][k]) * G[k][l] * T[j][l] for k in range(n) for l in range(n))
               for j in range(n)] for i in range(n)]
        s = GA.congruence_signature(G2)
        assert s == (p, q, 0)
        sigs[(p - q) % 8] = s
    assert sorted(sigs) == [1, 2, 3, 5, 6, 7]
    assert len(set(sigs.values())) == 6
    return True
