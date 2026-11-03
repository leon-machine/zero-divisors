"""dark-tower-matter.mirror-algebra: exact checks.

(i)   phi(e_K) = (-1)^(|K|/2) e_K on even basis blades is multiplicative from Cl^0(p,q) to
      Cl^0(q,p) (the same generators with every square negated), on every pair of even blades, for
      every signature with 1 <= p + q <= 6, so in particular Cl^0(3,1) = Cl^0(1,3) and
      Cl^0(4,2) = Cl^0(2,4); phi is diagonal with entries +-1, hence bijective. Control: the naive
      map e_K -> e_K is not multiplicative between Cl^0(3,1) and Cl^0(1,3).
(ii)  phi(I4') = +I4 and phi(I6') = -I6 (pseudoscalars as even blades), and phi carries the squares
      correctly (I'^2 computed in the mirror equals phi(I')^2 computed in the reversed algebra).
(iii) The full algebras differ: a primitive idempotent of Cl(1,3) (and of Cl(3,1)) is found by a
      search over commuting blades of square +1; on the minimal left ideal the left-multiplication
      matrices of the generators are computed, and their commutant (an exact kernel) is H on an
      8-dimensional module for Cl(1,3) and R on a 4-dimensional module for Cl(3,1).
      (Fact imported-clifford-structure (iii): the commutant of a minimal left ideal is a division
      algebra; the type is computed here from the commutant's trace-free part.)
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def phi(x):
    return {b: c * (-1) ** (len(b) // 2) for b, c in x.items()}


def even_blades(n):
    return [b for b in GA.all_blades(n) if len(b) % 2 == 0]


def multiplicative(p, q, mapping):
    Sm = GA.sig(p, q)
    So = tuple(-s for s in Sm)
    ev = even_blades(p + q)
    for a in ev:
        for b in ev:
            lhs = mapping(GA.mul({a: F(1)}, {b: F(1)}, Sm))
            rhs = GA.mul(mapping({a: F(1)}), mapping({b: F(1)}), So)
            if not GA.eq(lhs, rhs):
                return False
    return True


# ---- minimal left ideals and commutants -------------------------------------------------

def primitive_idempotent(S, n):
    blades = GA.all_blades(n)

    def dim(f):
        return GA.rank_of_vectors([[GA.mul({K: F(1)}, f, S).get(b, F(0)) for b in blades] for K in blades])
    f, d, chosen = GA.sc(1), 2 ** n, []
    for b in blades:
        if not b or GA.mul({b: F(1)}, {b: F(1)}, S) != {(): F(1)}:
            continue
        if not all(GA.commutes({b: F(1)}, {c: F(1)}, S) for c in chosen):
            continue
        f2 = GA.mul(f, GA.add(GA.sc(F(1, 2)), {b: F(1, 2)}), S)
        d2 = dim(f2)
        if 0 < d2 < d:
            f, d, chosen = f2, d2, chosen + [b]
    return f, d


def left_matrices(S, n, f, xs):
    blades = GA.all_blades(n)
    reps, vecs = [], []
    for K in blades:
        v = GA.mul({K: F(1)}, f, S)
        row = [v.get(b, F(0)) for b in blades]
        if GA.rank_of_vectors(vecs + [row]) > len(vecs):
            vecs.append(row)
            reps.append(v)
    N = len(reps)
    # pivot coordinates where the representative matrix is invertible
    piv = []
    for i, b in enumerate(blades):
        if GA.rank_of_vectors([[vecs[r][c] for c in piv + [i]] for r in range(N)]) > len(piv):
            piv.append(i)
        if len(piv) == N:
            break
    Msq = [[vecs[r][c] for r in range(N)] for c in piv]     # rows: pivot coords, cols: reps
    out = []
    for x in xs:
        cols = []
        for v in reps:
            w = GA.mul(x, v, S)
            rhs = [w.get(blades[c], F(0)) for c in piv]
            cols.append(GA.field_solve(Msq, rhs))
        out.append([[cols[j][i] for j in range(N)] for i in range(N)])
    return out, N


mm = GA.mat_mul                         # dense matrix product


def commutant(mats, N):
    rows = []
    for G in mats:
        for i in range(N):
            for j in range(N):
                r = [F(0)] * (N * N)
                for k in range(N):
                    r[i * N + k] += G[k][j]
                    r[k * N + j] -= G[i][k]
                rows.append(r)
    ker = GA.field_kernel(rows)
    return [[[v[i * N + j] for j in range(N)] for i in range(N)] for v in ker]


def division_type(basis):
    N = len(basis[0])
    if len(basis) == 1:
        return 'R'
    pure = []
    for B in basis:
        t = sum(B[i][i] for i in range(N)) / N
        P = [[B[i][j] - (t if i == j else 0) for j in range(N)] for i in range(N)]
        if any(x for r in P for x in r):
            pure.append(P)
    G = []
    for P in pure:
        row = []
        for Qm in pure:
            A, B = mm(P, Qm), mm(Qm, P)
            Sx = [[(A[i][j] + B[i][j]) / 2 for j in range(N)] for i in range(N)]
            if any(Sx[i][j] != (Sx[0][0] if i == j else 0) for i in range(N) for j in range(N)):
                return None
            row.append(Sx[0][0])
        G.append(row)
    pos, neg, zer = GA.congruence_signature(G)
    if pos == 0 and zer == 0 and GA.rank_of_vectors([[x for r in P for x in r] for P in pure]) == neg:
        return {1: 'C', 3: 'H'}.get(neg)
    return None


def check_even_isomorphism_reversed_signature():
    premise("dark-tower-matter.imported-clifford-structure")
    pairs = 0
    for n in range(1, 7):
        for p in range(n + 1):
            assert multiplicative(p, n - p, phi)
            pairs += 1
    assert pairs == 27
    # the stated instances, and phi is +-1 on every blade (bijective)
    assert multiplicative(3, 1, phi) and multiplicative(4, 2, phi)
    assert all(abs(phi({b: F(1)})[b]) == 1 for b in even_blades(6))
    # control: the identity on blades is not multiplicative between Cl0(3,1) and Cl0(1,3)
    assert not multiplicative(3, 1, lambda x: dict(x))
    return True


def check_pseudoscalars():
    I4 = {(0, 1, 2, 3): F(1)}
    I6 = {(0, 1, 2, 3, 4, 5): F(1)}
    assert GA.eq(phi(I4), I4)
    assert GA.eq(phi(I6), GA.scal(-1, I6))
    for (p, q), I in (((3, 1), I4), ((4, 2), I6)):
        Sm = GA.sig(p, q)
        So = tuple(-s for s in Sm)
        assert GA.eq(phi(GA.mul(I, I, Sm)), GA.mul(phi(I), phi(I), So))
    # the squares themselves: I4'^2 = I4^2 = -1, I6'^2 = I6^2 = -1
    assert GA.mul(I4, I4, GA.sig(3, 1)) == {(): F(-1)} and GA.mul(I4, I4, GA.sig(1, 3)) == {(): F(-1)}
    assert GA.mul(I6, I6, GA.sig(4, 2)) == {(): F(-1)} and GA.mul(I6, I6, GA.sig(2, 4)) == {(): F(-1)}
    return True


def check_full_algebras_differ():
    premise("dark-tower-matter.imported-clifford-structure")
    found = {}
    for (p, q) in ((1, 3), (3, 1)):
        S = GA.sig(p, q)
        f, d = primitive_idempotent(S, 4)
        mats, N = left_matrices(S, 4, f, [GA.gen(a) for a in range(4)])
        assert N == d
        # the generators act faithfully with the Clifford relations
        for a in range(4):
            sq = mm(mats[a], mats[a])
            assert sq == [[F(S[a]) if i == j else F(0) for j in range(N)] for i in range(N)]
        C = commutant(mats, N)
        found[(p, q)] = (N, len(C), division_type(C))
    assert found == {(1, 3): (8, 4, 'H'), (3, 1): (4, 1, 'R')}
    return True
