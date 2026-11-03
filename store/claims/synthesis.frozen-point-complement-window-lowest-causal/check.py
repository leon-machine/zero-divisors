"""synthesis.frozen-point-complement-window-lowest-causal: exact checks.

check_complement_signature: in the tractor space R^{2,4} (generators e0, e1 squaring +1, e2..e5
  squaring -1), the orthogonal complement of a vector I has signature (1,4) when Q(I) > 0, (2,3)
  when Q(I) < 0, and (1,3) plus a one-dimensional radical when Q(I) = 0: computed by exact
  nullspace and congruence diagonalisation of the Gram matrix built from GA products, for basis and
  non-basis rational I.
check_inertia_bound: a nondegenerate (a, b) sits in (P, Q) only if a <= P and b <= Q. Exhaustive over
  every plane spanned by two vectors with entries in {-1, 0, 1} of R^{1,4}: no positive-definite
  plane; and coordinate subspaces realise every (a, b) with a <= P, b <= Q.
check_window_census: the causal signatures (min(p, q) = 1) admitted up to overall sign by (1,4),
  for all p + q <= 16, are exactly (1,1), (2,1), (1,2), (3,1), (1,3), (4,1), (1,4): one per residue
  r != 4, the lowest causal member of that residue (dimension min(r, 8 - r) + 2, from an independent
  enumeration), none of residue 4; the tractor space (2,4) admits the same causal set; (2,3) and the
  degenerate (1,3,1) admit the set without residues 3 and 5. The admitted set is closed under
  (p, q) -> (q, p).
"""
from fractions import Fraction as F
from itertools import product
import GA
from tp_premise import premise


def gram(vectors, squares):
    return [[GA.dot(u, v, squares) for v in vectors] for u in vectors]


def vec(coeffs):
    out = {}
    for i, c in enumerate(coeffs):
        if c != 0:
            out[(i,)] = F(c)
    return out


def complement_basis(I, squares):
    """Exact basis of {v : <v, I> = 0} in R^n (n = len(squares))."""
    n = len(squares)
    row = [GA.dot(GA.gen(i), I, squares) for i in range(n)]
    piv = next(i for i in range(n) if row[i] != 0) if any(row) else None
    basis = []
    for j in range(n):
        if j == piv:
            continue
        c = [F(0)] * n
        c[j] = F(1)
        if piv is not None:
            c[piv] = -row[j] / row[piv]
        basis.append(vec(c))
    return basis


def check_complement_signature():
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    sq = GA.sig(2, 4)
    cases = [([1, 0, 0, 0, 0, 0], (1, 4, 0)),
             ([2, 1, 1, 0, 0, 0], (1, 4, 0)),          # Q = 4 + 1 - 1 = 4 > 0
             ([0, 0, 1, 0, 0, 0], (2, 3, 0)),
             ([1, 0, 1, 1, 0, 0], (2, 3, 0)),          # Q = 1 - 1 - 1 = -1 < 0
             ([1, 0, 1, 0, 0, 0], (1, 3, 1)),          # null: Q = 0
             ([1, 1, 1, 1, 0, 0], (1, 3, 1))]
    for coeffs, expected in cases:
        I = vec(coeffs)
        Q = GA.dot(I, I, sq)
        B = complement_basis(I, sq)
        assert len(B) == 5
        assert all(GA.dot(b, I, sq) == 0 for b in B)
        s = GA.congruence_signature(gram(B, sq))
        assert s == expected
        assert (Q > 0) == (s == (1, 4, 0)) and (Q < 0) == (s == (2, 3, 0)) and (Q == 0) == (s[2] == 1)
    # the de Sitter complement (1,4) is the residue-5 signature: 1 - 4 = -3 = 5 mod 8
    assert (1 - 4) % 8 == 5 and (2 - 3) % 8 == 7
    GA.check("frozen point complement in R^{2,4}: (1,4) for Q(I) > 0, (2,3) for Q(I) < 0, (1,3)+radical for Q(I) = 0", True)
    return True


def check_inertia_bound():
    premise("std-algebra.sylvester-inertia")
    sq = GA.sig(1, 4)
    vals = (-1, 0, 1)
    vecs = [vec(c) for c in product(vals, repeat=5) if any(c)]
    count = 0
    for i, u in enumerate(vecs):
        quu = GA.dot(u, u, sq)
        if quu <= 0:
            continue
        for v in vecs[i + 1:]:
            qvv = GA.dot(v, v, sq)
            if qvv <= 0:
                continue
            quv = GA.dot(u, v, sq)
            det = quu * qvv - quv * quv
            assert det <= 0          # never positive definite: a plane of type (2,0) does not exist
            count += 1
    assert count > 0
    # coordinate subspaces realise every (a, b) with a <= 1, b <= 4
    for a in range(0, 2):
        for b in range(0, 5):
            B = [GA.gen(i) for i in range(a)] + [GA.gen(1 + j) for j in range(b)]
            assert GA.congruence_signature(gram(B, sq)) == (a, b, 0) if B else True
    GA.check("inertia bound in R^{1,4}: no positive-definite plane; coordinate subspaces realise a <= 1, b <= 4", True)
    return True


def admitted(P, Q, nmax=16):
    """Causal (p, q), p + q <= nmax, embeddable up to overall sign in a nondegenerate (P, Q)."""
    out = []
    for p in range(0, nmax + 1):
        for q in range(0, nmax + 1 - p):
            if p + q < 2 or min(p, q) != 1:
                continue
            if (p <= P and q <= Q) or (q <= P and p <= Q):
                out.append((p, q))
    return sorted(out)


def lowest_causal(nmax=16):
    """Independent enumeration: for each residue the causal signatures of least dimension."""
    best = {}
    for p in range(0, nmax + 1):
        for q in range(0, nmax + 1 - p):
            if p + q < 2 or min(p, q) != 1:
                continue
            r = (p - q) % 8
            n = p + q
            if r not in best or n < best[r][0]:
                best[r] = (n, [(p, q)])
            elif n == best[r][0]:
                best[r][1].append((p, q))
    return best


def check_window_census():
    premise("std-algebra.sylvester-inertia")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    W = admitted(1, 4)
    assert W == [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (3, 1), (4, 1)]
    assert sorted((q, p) for p, q in W) == W                     # closed under reversal (P2 orbit)
    by_res = {}
    for p, q in W:
        by_res.setdefault((p - q) % 8, []).append((p, q))
    assert sorted(by_res) == [0, 1, 2, 3, 5, 6, 7]
    assert all(len(v) == 1 for v in by_res.values())
    low = lowest_causal()
    for r in range(8):
        assert low[r][0] == min(r, 8 - r) + 2
    for r, v in by_res.items():
        assert v[0] in low[r][1] and low[r][0] == sum(v[0])
    assert sorted(low[4][1]) == [(1, 5), (5, 1)] and 4 not in by_res
    # this world (1,3) is residue 6, the mirror (3,1) residue 2, the five-dimensional towers 3 and 5
    assert by_res[6] == [(1, 3)] and by_res[2] == [(3, 1)] and by_res[3] == [(4, 1)] and by_res[5] == [(1, 4)]
    # the whole tractor space (2,4) admits the same causal set
    assert admitted(2, 4) == W
    # Lambda < 0: complement (2,3); Lambda = 0: nondegenerate part (1,3); residues 3 and 5 drop out
    W23 = admitted(2, 3)
    assert W23 == admitted(1, 3) == [(1, 1), (1, 2), (1, 3), (2, 1), (3, 1)]
    assert sorted({(p - q) % 8 for p, q in W23}) == [0, 1, 2, 6, 7]
    # without the single-clock filter (W) also admits definite signatures, residue 4's (0,4), (4,0)
    fits = [(p, q) for p in range(0, 6) for q in range(0, 6)
            if 0 < p + q and ((p <= 1 and q <= 4) or (q <= 1 and p <= 4))]
    definite = [s for s in fits if min(s) == 0]
    assert (0, 4) in definite and (4, 0) in definite and (2, 0) in definite
    assert sorted(s for s in definite if (s[0] - s[1]) % 8 == 4) == [(0, 4), (4, 0)]
    assert all(min(s) == 1 for s in W) and not any(min(s) == 0 for s in W)
    # a larger ambient would admit a residue-4 member: (1,5) needs five directions of one sign
    assert (1, 5) in admitted(1, 5) and (1, 5) not in W
    GA.check("window under (W): one causal signature per residue r != 4, the lowest; none at r = 4; "
             "same for the tractor space; Lambda <= 0 drops residues 3 and 5", True)
    return True


def check_residue_zero_member():
    premise("synthesis.residues-zero-four-real-chirality-anomaly")
    premise("std-algebra.sylvester-inertia")
    # the admitted residue-0 member is (1,1), causal, and P3's (2,2) is not causal
    W = admitted(1, 4)
    zero = [s for s in W if (s[0] - s[1]) % 8 == 0]
    assert zero == [(1, 1)] and min(2, 2) != 1
    # at (1,1) the pseudoscalar I = e0 e1 squares to +1 and commutes with the even algebra:
    # the really chiral case of the anomaly theorem (n = 2 = 2 mod 4)
    sq = GA.sig(1, 1)
    I = GA.mul(GA.gen(0), GA.gen(1), sq)
    assert GA.eq(GA.mul(I, I, sq), GA.sc(1))
    for x in (GA.sc(3), I, GA.add(GA.sc(2), GA.scal(F(5, 7), I))):
        assert GA.commutes(I, x, sq)
    # whereas at this world's (1,3) the pseudoscalar squares to -1
    sq4 = GA.sig(1, 3)
    I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq4), GA.mul(GA.gen(2), GA.gen(3), sq4), sq4)
    assert GA.eq(GA.mul(I4, I4, sq4), GA.sc(-1))
    GA.check("residue 0 under (W): (1,1), pseudoscalar of square +1 central in the even algebra", True)
    return True
