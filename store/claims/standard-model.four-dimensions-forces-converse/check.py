"""standard-model.four-dimensions-forces-converse: exact checks.

The automorphism algebra of a two-factor hierarchy C^m (x) C^k is computed, not assumed: the real Lie algebra
u(m) + u(k) acts on C^m (x) C^k by X (x) 1 + 1 (x) Y (maps of the form A (x) B only, so the swap of factors is
excluded by definition, also at m = k), and its image is the automorphism algebra.
(1) Pair count: in spacetime dimension n (n even) the complexified ambient space C^(n+2) of signature (2, n) has
    an explicit totally isotropic subspace U of dimension (n+2)/2 with U^perp = U (so it is maximal); for each even
    n in 2..8 the image algebra of C^2 (x) C^((n+2)/2) has real dimension 4 + ((n+2)/2)^2 - 1, and it is the
    Standard Model algebra (dimension 12, derived algebra of dimension 11 split 3 + 8, centre of dimension 1)
    exactly at n = 4.
(2) Converse: for every 1 <= m, k <= 4 the image has dimension m^2 + k^2 - 1 (one-dimensional kernel, the
    diagonal phase), and m^2 + k^2 - 1 = 12 forces m^2 + k^2 = 13, so m, k <= 3 and the complete list of
    solutions is (2, 3), (3, 2). Given m = 2 the pair count is 3 and (n+2)/2 = 3 gives n = 4; given n = 4 the
    pair count is 3 and m = 2. The hypotheses of part (1) (the gauge-algebra reading, mass at two constituents
    away from n = 4) are declared premises, not computed.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

QI = GA.QI


def _basis_u(n):
    """Real basis of u(n): i E_kk, E_jk - E_kj, i(E_jk + E_kj), as sparse {(r, c): QI}."""
    out = []
    for k in range(n):
        out.append({(k, k): QI(0, 1)})
    for j in range(n):
        for k in range(j + 1, n):
            out.append({(j, k): QI(1), (k, j): QI(-1)})
            out.append({(j, k): QI(0, 1), (k, j): QI(0, 1)})
    return out


def _act(X, Y, m, k):
    """X (x) 1 + 1 (x) Y on C^m (x) C^k, index a*k + b."""
    M = {}
    for (a, c), z in X.items():
        for b in range(k):
            key = (a * k + b, c * k + b)
            M[key] = M.get(key, QI(0)) + z
    for (b, d), z in Y.items():
        for a in range(m):
            key = (a * k + b, a * k + d)
            M[key] = M.get(key, QI(0)) + z
    return {kk: v for kk, v in M.items() if v}


def _real_row(M, N):
    row = [F(0)] * (2 * N * N)
    for (r, c), z in M.items():
        row[r * N + c] = z.re
        row[N * N + r * N + c] = z.im
    return row


def _mmul(A, B):
    out = {}
    for (r, c), z in A.items():
        for (c2, d), w in B.items():
            if c == c2:
                out[(r, d)] = out.get((r, d), QI(0)) + z * w
    return {kk: v for kk, v in out.items() if v}


def _comm(A, B):
    out = dict(_mmul(A, B))
    for kk, v in _mmul(B, A).items():
        out[kk] = out.get(kk, QI(0)) - v
    return {kk: v for kk, v in out.items() if v}


def _image(m, k):
    zm, zk = {}, {}
    A = [_act(X, zk, m, k) for X in _basis_u(m)]
    B = [_act(zm, Y, m, k) for Y in _basis_u(k)]
    return A, B


def _rank(mats, N):
    return GA.rank_of_vectors([_real_row(M, N) for M in mats]) if mats else 0


def _derived_ranks(m, k):
    """Ranks of [g, g], of the A-side and B-side derived ideals, and the centre dimension of the image."""
    A, B = _image(m, k)
    N = m * k
    gens = A + B
    comms = [_comm(gens[i], gens[j]) for i in range(len(gens)) for j in range(i + 1, len(gens))]
    dA = _rank([_comm(A[i], A[j]) for i in range(len(A)) for j in range(i + 1, len(A))], N)
    dB = _rank([_comm(B[i], B[j]) for i in range(len(B)) for j in range(i + 1, len(B))], N)
    # centre: real combinations sum c_i g_i commuting with every g_j, modulo the kernel of the action
    rows = []
    for j in range(len(gens)):
        cols = [_real_row(_comm(g, gens[j]), N) for g in gens]
        rows.extend([[cols[i][r] for i in range(len(gens))] for r in range(2 * N * N)])
    cent_coeffs = GA.field_kernel(rows)
    cent = [{kk: v for kk, v in _sum_scaled(gens, c).items() if v} for c in cent_coeffs]
    return _rank(comms, N), dA, dB, _rank(cent, N)


def _sum_scaled(gens, coeffs):
    out = {}
    for g, c in zip(gens, coeffs):
        if c:
            for kk, z in g.items():
                out[kk] = out.get(kk, QI(0)) + z * QI(c)
    return out


def _isotropic_half(N):
    """Diagonal form diag(+1, +1, -1, ..., -1) of signature (2, N - 2) on Q(i)^N; vectors e_a + i e_b
    (equal squares) or e_a + e_b (opposite squares), pairs (0,1), (2,3), ...; returns (U basis, Gram)."""
    sq = [1, 1] + [-1] * (N - 2)
    U = []
    for j in range(N // 2):
        a, b = 2 * j, 2 * j + 1
        v = [QI(0)] * N
        v[a] = QI(1)
        v[b] = QI(0, 1) if sq[a] == sq[b] else QI(1)
        U.append(v)
    return U, sq


def _bil(x, y, sq):
    return sum((QI(s) * a * b for s, a, b in zip(sq, x, y)), QI(0))


def check_pair_count_and_even_dimensions():
    premise("standard-model.pair-count-dimension")
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    ok = True
    sm_dims = []
    for n in range(2, 10, 2):
        N = n + 2
        U, sq = _isotropic_half(N)
        iso = all(_bil(x, y, sq) == QI(0) for x in U for y in U)
        # U^perp: kernel of the N/2 x N matrix (B(u_i, e_c)); maximal iff its dimension is N/2
        perp = GA.field_kernel([[QI(sq[c]) * u[c] for c in range(N)] for u in U])
        rkU = GA.field_rank(U)
        pc = rkU
        ok = ok and iso and rkU == len(perp) and 2 * pc == n + 2
        A, B = _image(2, pc)
        dim = _rank(A + B, 2 * pc)
        ok = ok and dim == 3 + pc * pc
        if dim == 12:
            sm_dims.append(n)
    ok = ok and sm_dims == [4]
    der, dA, dB, cen = _derived_ranks(2, 3)
    ok = ok and (der, dA, dB, cen) == (11, 3, 8, 1)
    GA.check("pair count (n+2)/2 from a maximal isotropic subspace; dim aut(C^2 x C^pc) = 12 only at n = 4, "
             "where it is su(2) + su(3) + u(1)", ok)
    return ok


def check_converse_two_by_three():
    premise("standard-model.gauge-algebra-minimal-massive-composite")
    premise("standard-model.pair-count-dimension")
    ok = True
    hits = []
    for m in range(1, 5):
        for k in range(1, 5):
            A, B = _image(m, k)
            dim = _rank(A + B, m * k)
            ok = ok and dim == m * m + k * k - 1 and len(A) + len(B) - dim == 1
            if dim == 12:
                hits.append((m, k))
    # m^2 + k^2 = 13 bounds m, k by 3, so the box 1..4 is exhaustive
    sols = [(m, k) for m in range(1, 5) for k in range(1, 5) if m * m + k * k == 13]
    ok = ok and hits == sols == [(2, 3), (3, 2)]
    # the 2 x 2 hierarchy (n = 2): su(2) + su(2) + u(1), dimension 7, not 12
    der, dA, dB, cen = _derived_ranks(2, 2)
    ok = ok and (der, dA, dB, cen) == (6, 3, 3, 1)
    # ordering: m = 2 forces k = 3 and n = 2k - 2 = 4; n = 4 forces k = 3 and m = 2
    ok = ok and [k for (m, k) in hits if m == 2] == [3] and [2 * k - 2 for (m, k) in hits if m == 2] == [4]
    ok = ok and [m for (m, k) in hits if k == 3] == [2]
    GA.check("aut(C^m x C^k) has dimension m^2 + k^2 - 1 for m, k <= 4; equals 12 only at {2, 3}", ok)
    return ok
