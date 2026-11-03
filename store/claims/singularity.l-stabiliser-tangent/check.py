"""singularity.l-stabiliser-tangent: exact checks of the stabiliser/tangent split of so(2 nu).

Fock space of nu = 2, 3, 4 modes (Jordan-Wigner signs), operators as sparse rational matrices.
The quadratic elements: hops v_i* v_j (i != j) and Cartan elements v_i* v_i - 1/2, pair annihilations
v_j v_i (the adjoints of the creations) and pair creations v_i* v_j* (i < j).
(1) Counts nu^2, nu(nu-1)/2, nu(nu-1)/2 with nu^2 + nu(nu-1) = nu(2 nu - 1); the elements are linearly
    independent (rank nu(2 nu - 1)) and closed under the bracket (all commutators in their span). The
    raw elements (no -1/2) have the same rank, are not closed ([v_0* v_1*, v_1 v_0] leaves their span),
    and together with the identity span a space of dimension nu(2 nu - 1) + 1 closed under the bracket,
    the same as the corrected elements with the identity.
(2) On |0>: every off-diagonal hop and every pair annihilation gives 0, every Cartan element gives
    -1/2 |0>. The pair creations applied to |0> are linearly independent (rank nu(nu-1)/2); the images
    X|0> of all generators span rank 1 + nu(nu-1)/2, and modulo |0> rank nu(nu-1)/2.
(3) nu = 4: for every pair of modes the hop generator v_i* v_j - v_j* v_i and the pairing generator
    v_i* v_j* - v_j v_i satisfy G^3 = -G, so exp(theta G) = 1 + sin G + (1 - cos) G^2 exactly at
    (cos, sin) = (3/5, 4/5); these rotations are orthogonal and nontrivial, every hop rotation fixes |0>
    and every pairing rotation moves it. The pairing rotation on modes (0, 1) sends |0> to
    3/5 |0> + 4/5 |11>, the witness of the envelope corollary. A hop rotation does entangle off the
    vacuum: on |10> it gives a superposition of |10> and |01> with mode-0 population 9/25.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
import fock
from tp_premise import premise  # noqa: F401 (the claim has no premises)


def _basis(nu):
    """Basis subsets in the fock LSB bitmask order: allb[s] = the modes set in s, idx[S] = s."""
    allb = [frozenset(k for k in range(nu) if s >> k & 1) for s in range(2 ** nu)]
    return allb, {S: s for s, S in enumerate(allb)}


mmul = fock.mm


def madd(A, B, c=1):
    return fock.madd(A, fock.msc(c, B))


def mvec(A, v, dim):
    out = [F(0)] * dim
    for (i, k), a in A.items():
        out[i] += a * v[k]
    return out


def srank(rows):
    piv, rank = {}, 0
    for r in rows:
        r = dict(r)
        while r:
            k = min(r)
            if k in piv:
                p = piv[k]
                f = r[k] / p[k]
                for kk, vv in p.items():
                    nv = r.get(kk, F(0)) - f * vv
                    if nv:
                        r[kk] = nv
                    else:
                        r.pop(kk, None)
            else:
                piv[k] = r
                rank += 1
                break
    return rank


def generators(nu):
    allb, idx = _basis(nu)
    dim = len(allb)
    half = {(i, i): F(1, 2) for i in range(dim)}
    C = [fock.cre(i, nu) for i in range(nu)]
    A = [fock.ann(i, nu) for i in range(nu)]
    raw_hops = {(i, j): fock.mm(C[i], A[j]) for i in range(nu) for j in range(nu)}
    pairs = list(combinations(range(nu), 2))
    anns = {(i, j): fock.mm(A[j], A[i]) for (i, j) in pairs}
    cres = {(i, j): fock.mm(C[i], C[j]) for (i, j) in pairs}
    hops = {ij: (madd(H, half, -1) if ij[0] == ij[1] else H) for ij, H in raw_hops.items()}
    return allb, idx, dim, raw_hops, hops, anns, cres


def check_so2nu_split_and_closure():
    for nu in (2, 3, 4):
        allb, idx, dim, raw_hops, hops, anns, cres = generators(nu)
        assert (len(hops), len(anns), len(cres)) == (nu * nu, nu * (nu - 1) // 2, nu * (nu - 1) // 2)
        gens = list(hops.values()) + list(anns.values()) + list(cres.values())
        raw = list(raw_hops.values()) + list(anns.values()) + list(cres.values())
        n = nu * (2 * nu - 1)
        assert len(gens) == n and srank(gens) == n and srank(raw) == n
        brackets = [madd(mmul(X, Y), mmul(Y, X), -1) for a, X in enumerate(gens) for Y in gens[a + 1:]]
        assert srank(gens + brackets) == n
        ident = {(i, i): F(1) for i in range(dim)}
        rb = madd(mmul(cres[(0, 1)], anns[(0, 1)]), mmul(anns[(0, 1)], cres[(0, 1)]), -1)
        assert srank(raw + [rb]) == n + 1 and srank(raw + [ident, rb]) == n + 1
        raw_brackets = [madd(mmul(X, Y), mmul(Y, X), -1) for a, X in enumerate(raw) for Y in raw[a + 1:]]
        assert srank(raw + [ident] + raw_brackets) == n + 1 == srank(gens + [ident])


def check_vacuum_stabiliser_and_tangent():
    for nu in (2, 3, 4):
        allb, idx, dim, raw_hops, hops, anns, cres = generators(nu)
        vac = [F(0)] * dim
        vac[idx[frozenset()]] = F(1)
        zero = [F(0)] * dim
        for (i, j), H in hops.items():
            img = mvec(H, vac, dim)
            assert img == (zero if i != j else [x * F(-1, 2) for x in vac])
        for A in anns.values():
            assert mvec(A, vac, dim) == zero
        m = nu * (nu - 1) // 2
        cre_imgs = [mvec(C, vac, dim) for C in cres.values()]
        assert GA.rank_of_vectors(cre_imgs) == m
        imgs = [mvec(X, vac, dim) for X in list(hops.values()) + list(anns.values()) + list(cres.values())]
        assert GA.rank_of_vectors(imgs) == 1 + m
        assert GA.rank_of_vectors(imgs + [vac]) - 1 == m


def check_rotations_fix_or_move_the_vacuum():
    nu = 4
    allb, idx, dim, raw_hops, hops, anns, cres = generators(nu)
    c, s = F(3, 5), F(4, 5)
    ident = {(i, i): F(1) for i in range(dim)}
    vac = [F(0)] * dim
    vac[idx[frozenset()]] = F(1)

    def rot(G):
        G2 = mmul(G, G)
        assert mmul(G2, G) == madd({}, G, -1)
        return madd(madd(ident, G, s), G2, 1 - c)

    def orthogonal(R):
        RT = {(j, i): v for (i, j), v in R.items()}
        return mmul(RT, R) == ident

    hop_R = {ij: rot(madd(raw_hops[ij], raw_hops[(ij[1], ij[0])], -1)) for ij in anns}
    pair_R = {ij: rot(madd(cres[ij], anns[ij], -1)) for ij in anns}
    assert len(hop_R) == len(pair_R) == 6
    for R in list(hop_R.values()) + list(pair_R.values()):
        assert orthogonal(R) and R != ident
    assert all(mvec(R, vac, dim) == vac for R in hop_R.values())
    assert all(mvec(R, vac, dim) != vac for R in pair_R.values())
    target = [F(0)] * dim
    target[idx[frozenset()]] = F(3, 5)
    target[idx[frozenset((0, 1))]] = F(4, 5)
    assert mvec(pair_R[(0, 1)], vac, dim) == target
    ket10 = [F(0)] * dim
    ket10[idx[frozenset((0,))]] = F(1)
    out = mvec(hop_R[(0, 1)], ket10, dim)
    support = {allb[k] for k in range(dim) if out[k] != 0}
    p0 = sum((out[k] * out[k] for k in range(dim) if 0 in allb[k]), F(0))
    assert support == {frozenset((0,)), frozenset((1,))} and p0 == F(9, 25)
