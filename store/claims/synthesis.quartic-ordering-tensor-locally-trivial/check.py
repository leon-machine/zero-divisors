"""synthesis.quartic-ordering-tensor-locally-trivial: exact checks.

sl(4) = sl(CS) in the matrix basis E_ij (i != j), H_k = E_kk - E_(k+1)(k+1).
(1) The Chevalley-Eilenberg complex of sl4 with adjoint coefficients, restricted to torus weight
    zero (the other weights are acyclic: on them the Cartan formula L_H = d i_H + i_H d inverts d up
    to the nonzero weight), has dimensions 3, 21, 87, 273 and ranks 3, 18, 69, d d = 0, so
    H^1(sl4, sl4) = H^2(sl4, sl4) = 0 exactly.
(2) Chirality blocks: g+ = sl2 on the first two twistor coordinates, g- = sl2 on the last two;
    [g+, g-] = 0. A map phi equal to a spin-2 map S on g+ (S(f) = e, weight +4, Killing-symmetric)
    and zero on g- and on the rest has coboundary d(phi) vanishing on (g-, g-) and (g-, g+) and
    nonzero on (g+, g+) with values in g+: a first-order deformation of the quadratic bracket that
    passes the anti-self-dual consistency check and puts a spin-2 tensor in the googly slot, and is
    a coboundary (removed by q -> q o (1 + hbar phi)).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from pyutil import get_or_set
from GA import mat_rank
from tp_premise import premise

n = 4


def E(i, j):
    M = [[F(0)] * n for _ in range(n)]
    M[i][j] = F(1)
    return M


mm = GA.mat_mul


def msub(A, B):
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]


def msc(c, A):
    return [[c * A[i][j] for j in range(n)] for i in range(n)]


def br(A, B):
    return msub(mm(A, B), mm(B, A))


ZERO = [[F(0)] * n for _ in range(n)]


def basis_sl4():
    B, W = [], []
    for i in range(n):
        for j in range(n):
            if i != j:
                B.append(E(i, j))
                w = [0] * n
                w[i] += 1
                w[j] -= 1
                W.append(tuple(w))
    for k in range(n - 1):
        B.append(msub(E(k, k), E(k + 1, k + 1)))
        W.append((0,) * n)
    return B, W


def coords(M):
    c = [M[i][j] for i in range(n) for j in range(n) if i != j]
    s = F(0)
    for k in range(n - 1):
        s += M[k][k]
        c.append(s)
    return c


def ce_matrix(k, B, W):
    """Chevalley-Eilenberg d: weight-zero k-cochains -> weight-zero (k+1)-cochains, adjoint values."""
    D = len(B)
    BR = [[coords(br(B[i], B[j])) for j in range(D)] for i in range(D)]

    def wsum(I):
        return tuple(sum(W[i][c] for i in I) for c in range(n))

    def unknowns(kk):
        U = {}
        for I in combinations(range(D), kk):
            for m in range(D):
                if W[m] == wsum(I):
                    U[(I, m)] = len(U)
        return U
    Uk, Uk1 = unknowns(k), unknowns(k + 1)
    byI = {}
    for (I, m), u in Uk.items():
        get_or_set(byI, I, []).append((m, u))
    M = [[F(0)] * len(Uk) for _ in range(len(Uk1))]
    for (J, o), r in Uk1.items():
        for a in range(k + 1):
            rest = J[:a] + J[a + 1:]
            for (m, u) in byI.get(rest, []):
                M[r][u] += (-1) ** a * BR[J[a]][m][o]
        for a in range(k + 1):
            for b in range(a + 1, k + 1):
                rest = J[:a] + J[a + 1:b] + J[b + 1:]
                for p, coef in enumerate(BR[J[a]][J[b]]):
                    if coef == 0 or p in rest:
                        continue
                    arg = (p,) + rest
                    srt = tuple(sorted(arg))
                    perm = [arg.index(x) for x in srt]
                    inv = sum(1 for x in range(len(perm)) for y in range(x + 1, len(perm)) if perm[x] > perm[y])
                    if (srt, o) in Uk:
                        M[r][Uk[(srt, o)]] += (-1) ** (a + b) * coef * (-1) ** inv
    return M, len(Uk), len(Uk1)


def check_h2_sl4_vanishes():
    premise("correspondence.spin-representation")
    premise("correspondence.symmetrised-quadratics-palatial-algebra")
    B, W = basis_sl4()
    assert len(B) == 15
    # weight-zero complex 0 -> 1 -> 2 -> 3 (nonzero torus weights are acyclic by the Cartan formula)
    d0, a0, b0 = ce_matrix(0, B, W)
    d1, a1, b1 = ce_matrix(1, B, W)
    d2, a2, b2 = ce_matrix(2, B, W)
    assert (a0, a1, a2, b2) == (3, 21, 87, 273)
    r0, r1, r2 = mat_rank(d0), mat_rank(d1), mat_rank(d2)
    assert (r0, r1, r2) == (3, 18, 69)
    # d d = 0
    for i in range(len(d2)):
        for j in range(a1):
            assert sum(d2[i][k] * d1[k][j] for k in range(a2)) == 0
    assert a1 - r1 - r0 == 0                              # H^1(sl4, sl4) = 0: derivations are inner
    assert a2 - r2 - r1 == 0                              # H^2(sl4, sl4) = 0: the bracket is rigid
    return True


def blocks():
    hp, ep, fp = msub(E(0, 0), E(1, 1)), E(0, 1), E(1, 0)
    hm, em, fm = msub(E(2, 2), E(3, 3)), E(2, 3), E(3, 2)
    return (hp, ep, fp), (hm, em, fm)


def phi(M):
    """Spin-2 map S(f+) = e+ on g+, zero on g-, on the Cartan complement and off the Lorentz blocks."""
    (hp, ep, fp), _ = blocks()
    # component of M along f+ is the (1,0) entry; S sends it to e+
    return msc(M[1][0], ep)


def dphi(M, N):
    return msub(msub(br(M, phi(N)), br(N, phi(M))), phi(br(M, N)))


def in_block(M, lo, hi):
    return all(M[i][j] == 0 for i in range(n) for j in range(n) if not (lo <= i < hi and lo <= j < hi))


def check_spin_two_coboundary_in_googly_slot():
    premise("correspondence.chirality-split-ordering-insensitivity-asd-sector")
    premise("correspondence.ordering-filtration")
    gp, gm = blocks()
    for x in gp:
        for y in gm:
            assert br(x, y) == ZERO                       # [g+, g-] = 0
    hp, ep, fp = gp
    assert br(hp, ep) == msc(F(2), ep) and br(hp, fp) == msc(F(-2), fp) and br(ep, fp) == hp
    # S is a weight-4 vector of End(g+): ad_h S - S ad_h = 4 S on g+
    for x in gp:
        lhs = msub(br(hp, phi(x)), phi(br(hp, x)))
        assert lhs == msc(F(4), phi(x))
    # Killing-symmetric on g+: K(S x, y) = K(x, S y), with K proportional to tr(xy)
    tr = lambda A: sum(A[i][i] for i in range(n))
    for x in gp:
        for y in gp:
            assert tr(mm(phi(x), y)) == tr(mm(x, phi(y)))
    # anti-self-dual words see nothing; mixed words see nothing
    for x in gm:
        for y in gm:
            assert dphi(x, y) == ZERO
        for y in gp:
            assert dphi(x, y) == ZERO and dphi(y, x) == ZERO
    # self-dual words: nonzero, valued in g+
    vals = [dphi(x, y) for x in gp for y in gp]
    assert any(v != ZERO for v in vals)
    assert all(in_block(v, 0, 2) for v in vals)
    assert dphi(hp, fp) == msc(F(4), ep)                  # [h, S f] - [f, S h] - S[h, f] = 2e + 2e
    # the complement p of g+ + g-: off-block E_ij and diag(1,1,-1,-1)
    pp = [E(i, j) for i in range(2) for j in range(2, 4)] + [E(i, j) for i in range(2, 4) for j in range(2)]
    pp.append(msub(madd(E(0, 0), E(1, 1)), madd(E(2, 2), E(3, 3))))
    assert len(pp) == 9
    for x in gm:
        for y in pp:
            assert dphi(x, y) == ZERO                     # never touches the anti-self-dual factor
    assert any(dphi(x, y) != ZERO for x in gp for y in pp)        # (g+, p): nonzero
    assert any(dphi(x, y) != ZERO for x in pp for y in pp)        # (p, p): nonzero
    # an explicit (p, p) value: E_12 and E_20 lie in p, phi vanishes on both, [E_12, E_20] = E_10 = f+
    assert dphi(E(1, 2), E(2, 0)) == msc(F(-1), ep)       # d phi = -phi(f+) = -e+
    # S is not a derivation of g+ (derivations are inner, Killing-antisymmetric): d(phi) != 0 on g+
    # the deformed bracket [M,N] + t d(phi)(M,N) is the transport of [ , ] by (1 + t phi) to first order
    t = F(1, 7)
    for M in gp:
        for N in gp:
            rhs_first = madd(br(M, N), msc(t, dphi(M, N)))
            full = br(madd(M, msc(t, phi(M))), madd(N, msc(t, phi(N))))
            # (1 + t phi)[M,N]' = [(1+t phi)M, (1+t phi)N] up to order t^2
            diff = msub(madd(rhs_first, msc(t, phi(rhs_first))), full)
            second = msc(t * t, msub(br(phi(M), phi(N)), phi(dphi(M, N))))
            assert diff == msc(F(-1), second)
    return True
