"""synthesis.gauge-algebra-by-tower: one rule, six causal towers, T12's row recovered.

Every input of the rule is recomputed in exact arithmetic where the geometric
algebra allows it, and the automorphism algebras are computed as exact ranks:
  (a) the onset count a: 2 if the reversion pairing on S = Cl^0(V) f is
      alternating, 1 if not (the criterion of T14c Thm 3.5);
  (F) the field F = f Cl^0(V) f, classified by dimension and commutativity
      (T14c Thm 3.2 and the ladder's F);
  (b) the pair count: real ladder pairs of the conformal space built and
      checked against the canonical relations; complex index floor((n+2)/2);
  (K) the pairs' scalars: R when the two indices agree, otherwise the
      centraliser in F of a unit u of F (U3), and the slot algebra of one
      quaternionic constituent cut to the circle commuting with u;
  (g) the image of g(a,K) + g(b,K), acting as X (x) 1 + 1 (x) Y on the real
      form of K^a (x) K^b: its dimension, centre and derived algebra.
The table must give T12's 12 and 17 and T14c's 2 and 9, and the mirror row
must equal this tower's (T14 Thm 4.3(i)); wrong inputs must give other numbers.
"""
from fractions import Fraction as Fr
from itertools import combinations
import GA
from tp_premise import premise

ZERO, ONE = Fr(0), Fr(1)
HALF = Fr(1, 2)

# The six causal towers of T14 and T14c: residue r = p - q mod 8, signature
# (p, q) of the tower; the field column is T14c Thm 3.2's, recomputed below.
TOWERS = [(6, (1, 3), "C"), (2, (3, 1), "C"), (1, (2, 1), "R"),
          (7, (1, 2), "R"), (3, (4, 1), "H"), (5, (1, 4), "H")]
# the numbers the theorems state
T12_ROW = 12          # standard-model.gauge-algebra-minimal-massive-composite
T12_MAXIMAL = 17      # C^3 (x) C^3, same theorem
T14C_THREE = 2        # dark-tower-matter.gauge-algebras (i)
T14C_FIVE = 9         # dark-tower-matter.gauge-algebras (ii)


# ---------------------------------------------------------------- the algebra side
def squares(p, q):
    return GA.sig(p, q)


def even_blades(n):
    return [B for B in GA.all_blades(n) if len(B) % 2 == 0]


def idempotent(sq):
    """f = (1 + b)/2 with b = e_i e_j, Q(e_i) = +1, Q(e_j) = -1, so Q-square b^2 = +1."""
    i = sq.index(1)
    j = sq.index(-1)
    b = GA.mul(GA.gen(i), GA.gen(j), sq)
    assert GA.eq(GA.mul(b, b, sq), GA.sc(1))
    f = GA.add(GA.sc(HALF), GA.scal(HALF, b))
    assert GA.eq(GA.mul(f, f, sq), f)
    return f


def onset_count(p, q):
    """2 if the reversion pairing on S = Cl^0 f is alternating, else 1."""
    sq = squares(p, q)
    f = idempotent(sq)
    gens = [GA.mul({B: ONE}, f, sq) for B in even_blades(p + q)]
    alternating = True
    for x, y in combinations(range(len(gens)), 2):
        s = GA.add(GA.mul(GA.reverse(gens[x]), gens[y], sq),
                   GA.mul(GA.reverse(gens[y]), gens[x], sq))
        if not GA.is_zero(s):
            alternating = False
            break
    if alternating:
        alternating = all(GA.is_zero(GA.mul(GA.reverse(g), g, sq)) for g in gens)
    return 2 if alternating else 1


def span_basis(elems, n):
    blades = GA.all_blades(n)
    out, vecs = [], []
    for e in elems:
        v = GA.basis_vector_of(e, blades)
        if GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            out.append(e)
    return out


def field_of(p, q):
    """F = f Cl^0(V) f: its type, a basis, and the idempotent (its unit)."""
    sq, n = squares(p, q), p + q
    f = idempotent(sq)
    F = span_basis([GA.mul(GA.mul(f, {B: ONE}, sq), f, sq) for B in even_blades(n)], n)
    comm = all(GA.commutes(x, y, sq) for x in F for y in F)
    kind = {1: "R", 2: "C" if comm else None, 4: "H" if not comm else None}.get(len(F))
    return kind, F, f, sq


def unit_in(F, f, sq):
    """An element u of F with u^2 = -c f, c > 0 (a complex unit up to scale), or None."""
    for x in F:
        if GA.eq(x, f):
            continue
        # the basis elements are blade sandwiches f e_K f; a unit is one whose square is -c f
        x2 = GA.mul(x, x, sq)
        for c in (Fr(k, 4) for k in range(1, 17)):
            if GA.eq(x2, GA.scal(-c, f)):
                return x
    return None


def centraliser_dim(u, F, sq, n):
    """dim of {y in F : uy = yu}, exactly (linear algebra over the basis F)."""
    blades = GA.all_blades(n)
    cols = [GA.basis_vector_of(GA.sub(GA.mul(u, y, sq), GA.mul(y, u, sq)), blades) for y in F]
    return len(F) - GA.rank_of_vectors(cols)


def commutator_space(F, sq, n):
    return span_basis([GA.sub(GA.mul(x, y, sq), GA.mul(y, x, sq)) for x in F for y in F], n)


def real_pairs_ok(p, q):
    """Build min(p+1, q+1) real ladder pairs in the conformal Cl(p+1, q+1) and
    check the canonical anticommutation relations."""
    sq = squares(p + 1, q + 1)
    pos = [i for i, s in enumerate(sq) if s == 1]
    neg = [i for i, s in enumerate(sq) if s == -1]
    k = min(len(pos), len(neg))
    W = [GA.scal(HALF, GA.add(GA.gen(pos[t]), GA.gen(neg[t]))) for t in range(k)]
    Vv = [GA.scal(HALF, GA.sub(GA.gen(pos[t]), GA.gen(neg[t]))) for t in range(k)]
    for s in range(k):
        for t in range(k):
            ww = GA.add(GA.mul(W[s], W[t], sq), GA.mul(W[t], W[s], sq))
            vv = GA.add(GA.mul(Vv[s], Vv[t], sq), GA.mul(Vv[t], Vv[s], sq))
            wv = GA.add(GA.mul(W[s], Vv[t], sq), GA.mul(Vv[t], W[s], sq))
            if not (GA.is_zero(ww) and GA.is_zero(vv) and GA.eq(wv, GA.sc(1 if s == t else 0))):
                return k, False
    return k, True


def even_centre(p, q):
    sq, n = squares(p, q), p + q
    ev = even_blades(n)
    return [B for B in ev if all(GA.commutes({B: ONE}, {C: ONE}, sq) for C in ev if len(C) == 2)], sq


def full_field_dim(p, q):
    """Dimension of f A f for the full Clifford algebra A = Cl(p,q), with f the
    smallest product of commuting idempotents (1 + B)/2 found (B blades of square +1)."""
    sq, n = squares(p, q), p + q
    cand = [B for B in GA.all_blades(n) if B and GA.eq(GA.mul({B: ONE}, {B: ONE}, sq), GA.sc(1))]
    best = None
    for r in (1, 2):
        for Bs in combinations(cand, r):
            if not all(GA.commutes({x: ONE}, {y: ONE}, sq) for x, y in combinations(Bs, 2)):
                continue
            f = GA.sc(1)
            for B in Bs:
                f = GA.mul(f, GA.add(GA.sc(HALF), {B: HALF}), sq)
            if GA.is_zero(f):
                continue
            F = span_basis([GA.mul(GA.mul(f, {B: ONE}, sq), f, sq) for B in GA.all_blades(n)], n)
            comm = all(GA.commutes(x, y, sq) for x in F for y in F)
            if best is None or len(F) < best[0]:
                best = (len(F), comm)
    return best


# ---------------------------------------------------------------- the matrix side
def cm(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def zeros(N):
    return [[(ZERO, ZERO) for _ in range(N)] for _ in range(N)]


def unit_mat(N, j, k, z):
    M = zeros(N)
    M[j][k] = z
    return M


def madd(A, B):
    return [[(a[0] + b[0], a[1] + b[1]) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def kron(A, B):
    m, k = len(A), len(B)
    return [[cm(A[i // k][j // k], B[i % k][j % k]) for j in range(m * k)] for i in range(m * k)]


def ident(N):
    return [[(ONE, ZERO) if i == j else (ZERO, ZERO) for j in range(N)] for i in range(N)]


def lie_basis(a, K, traceless=False):
    """o(a) for K = R; u(a) (or su(a)) for K = C, as complex matrices."""
    out = []
    for j in range(a):
        for k in range(j + 1, a):
            out.append(madd(unit_mat(a, j, k, (ONE, ZERO)), unit_mat(a, k, j, (-ONE, ZERO))))
            if K == "C":
                out.append(madd(unit_mat(a, j, k, (ZERO, ONE)), unit_mat(a, k, j, (ZERO, ONE))))
    if K == "C":
        if traceless:
            for j in range(a - 1):
                out.append(madd(unit_mat(a, j, j, (ZERO, ONE)), unit_mat(a, j + 1, j + 1, (ZERO, -ONE))))
        else:
            for j in range(a):
                out.append(unit_mat(a, j, j, (ZERO, ONE)))
    return out


def realify(M, K):
    N = len(M)
    if K == "R":
        assert all(z[1] == 0 for row in M for z in row)
        return [[z[0] for z in row] for row in M]
    R = [[ZERO] * (2 * N) for _ in range(2 * N)]
    for i in range(N):
        for j in range(N):
            x, y = M[i][j]
            R[2 * i][2 * j], R[2 * i][2 * j + 1] = x, -y
            R[2 * i + 1][2 * j], R[2 * i + 1][2 * j + 1] = y, x
    return R


def rmul(A, B):
    return GA.mat_mul(A, B)


def rbr(A, B):
    P, Q = rmul(A, B), rmul(B, A)
    return [[x - y for x, y in zip(r, s)] for r, s in zip(P, Q)]


def flat(M):
    return [x for row in M for x in row]


def independent(mats):
    out, vecs = [], []
    for M in mats:
        v = flat(M)
        if GA.rank_of_vectors(vecs + [v]) > len(vecs):
            vecs.append(v)
            out.append(M)
    return out


def automorphism_algebra(K, a, b):
    """Image of g(a,K) + g(b,K) on the real form of K^a (x) K^b, acting as
    X (x) 1 + 1 (x) Y.  Returns (dim, centre dim, derived dim, dim of the image of
    su(a), dim of the image of su(b)), all exact ranks."""
    Ia, Ib = ident(a), ident(b)
    A = [realify(kron(X, Ib), K) for X in lie_basis(a, K)]
    B = [realify(kron(Ia, Y), K) for Y in lie_basis(b, K)]
    img = independent(A + B)
    d = len(img)
    for M in img:  # every image element preserves the real inner product
        assert all(M[i][j] == -M[j][i] for i in range(len(M)) for j in range(len(M)))
    if K == "C":   # and is complex-linear: it commutes with J
        N = 2 * a * b
        J = [[ZERO] * N for _ in range(N)]
        for i in range(a * b):
            J[2 * i + 1][2 * i], J[2 * i][2 * i + 1] = ONE, -ONE
        assert all(GA.mat_eq(rmul(M, J), rmul(J, M)) for M in img)
    # centre: c with [sum c_k M_k, M_j] = 0 for all j
    rows = [[x for Mj in img for x in flat(rbr(Mk, Mj))] for Mk in img]
    centre = d - GA.rank_of_vectors(rows) if d else 0
    derived = GA.rank_of_vectors([flat(rbr(img[i], img[j]))
                                  for i in range(d) for j in range(i + 1, d)]) if d > 1 else 0
    if K == "C":
        sa = GA.rank_of_vectors([flat(realify(kron(X, Ib), K)) for X in lie_basis(a, K, True)]) if a > 1 else 0
        sb = GA.rank_of_vectors([flat(realify(kron(Ia, Y), K)) for Y in lie_basis(b, K, True)]) if b > 1 else 0
    else:
        sa = sb = 0
    return d, centre, derived, sa, sb


def formula(K, a, b):
    if K == "R":
        return a * (a - 1) // 2 + b * (b - 1) // 2
    return a * a + b * b - 1


# ---------------------------------------------------------------- the rule
def tower_row(r, pq, F_stated):
    p, q = pq
    n = p + q
    a = onset_count(p, q)
    F_kind, F, f, sq = field_of(p, q)
    real_index, ok = real_pairs_ok(p, q)
    b = (n + 2) // 2
    if real_index == b:
        K = "R"                       # no unit needed (T14c Prop 4.1(i))
    else:
        u = unit_in(F, f, sq)         # U3: the unit lies in the constituent's field
        assert u is not None, f"r={r}: the pairs need a unit and F has none"
        assert centraliser_dim(u, F, sq, n) == 2   # span{f, u}: a copy of C
        K = "C"
        if F_kind == "H":
            # the slot algebra of one quaternionic constituent is [F, F] = Im H (sp(1));
            # only the circle generated by u commutes with the pair algebra (T14c Thm 5.1(ii))
            imH = commutator_space(F, sq, n)
            assert len(imH) == 3
            assert centraliser_dim(u, imH, sq, n) == 1
    return dict(r=r, n=n, F=F_kind, F_stated=F_stated, a=a, b=b, real_index=real_index,
                pairs_ok=ok, K=K)


def test_gauge_algebra_by_tower():
    for pid in ("standard-model.gauge-algebra-minimal-massive-composite",
                "standard-model.four-dimensions-forces-converse",
                "standard-model.pair-count-dimension",
                "standard-model.internal-symmetry-ladder",
                "mass.mass-symplectic-area-two-twistor-formula",
                "dark-tower-matter.gauge-algebras",
                "dark-tower-matter.where-mass-begins",
                "dark-tower-matter.constituents-field",
                "dark-tower-matter.pairs",
                "dark-tower-matter.ladder",
                "dark-tower-matter.third-pairs-unit-five-dimensions",
                "dark-tower-matter.mirror-algebra",
                "dark-tower-matter.h2-identification",
                "dark-tower-matter.u-transposition-rule",
                "dark-tower-matter.h1-momentum"):
        premise(pid)

    # 1. the automorphism algebras, exact, against the dimension formula
    cache = {}
    for K in ("R", "C"):
        for a in (1, 2, 3):
            for b in (1, 2, 3):
                cache[(K, a, b)] = automorphism_algebra(K, a, b)
                assert cache[(K, a, b)][0] == formula(K, a, b), (K, a, b, cache[(K, a, b)])
    GA.check("image of g(a,K)+g(b,K): dim = a^2+b^2-1 over C, a(a-1)/2+b(b-1)/2 over R, a,b <= 3", True)
    d, z, der, sa, sb = cache[("C", 2, 3)]
    GA.check("C^2 (x) C^3: dim 12, centre 1, derived 11 = 3 + 8 (su(2)+su(3)+u(1))",
             (d, z, der, sa, sb) == (T12_ROW, 1, 11, 3, 8) and sa + sb == der)
    d, z, der, sa, sb = cache[("C", 3, 3)]
    GA.check("C^3 (x) C^3: dim 17, centre 1, derived 16 = 8 + 8", (d, z, der, sa, sb) == (T12_MAXIMAL, 1, 16, 8, 8))
    d, z, der, sa, sb = cache[("C", 1, 3)]
    GA.check("C^1 (x) C^3: dim 9, centre 1, derived 8 (u(3))", (d, z, der, sb) == (T14C_FIVE, 1, 8, 8))
    d, z, der, sa, sb = cache[("R", 2, 2)]
    GA.check("R^2 (x) R^2: dim 2, abelian (so(2)+so(2))", (d, z, der) == (T14C_THREE, 2, 0))

    # 2. the rule's inputs in each causal tower, recomputed
    rows = [tower_row(r, pq, Fs) for r, pq, Fs in TOWERS]
    for row in rows:
        GA.check(f"r={row['r']}: field {row['F']} = T14c's {row['F_stated']}", row["F"] == row["F_stated"])
        GA.check(f"r={row['r']}: {row['real_index']} real pairs obey the canonical relations",
                 row["pairs_ok"] and row["real_index"] == 2)
    want = {6: ("C", 2, 3, 12), 2: ("C", 2, 3, 12), 1: ("R", 2, 2, 2),
            7: ("R", 2, 2, 2), 3: ("C", 1, 3, 9), 5: ("C", 1, 3, 9)}
    table = {}
    for row in rows:
        dim = cache[(row["K"], row["a"], row["b"])][0]
        table[row["r"]] = (row["K"], row["a"], row["b"], dim)
        GA.check(f"r={row['r']} (n={row['n']}): {row['K']}^{row['a']} (x) {row['K']}^{row['b']}, dim {dim}",
                 table[row["r"]] == want[row["r"]])

    # 3. the four-dimensional row is T12's theorem; the odd rows are T14c's
    GA.check("r = 6: the rule returns T12 Thm 4.1's C^2 (x) C^3 and 12", table[6] == ("C", 2, 3, T12_ROW))
    GA.check("r = 1, 7: T14c Thm 5.1(i)'s 2; r = 3, 5: T14c Thm 5.1(ii)'s 9",
             table[1][3] == table[7][3] == T14C_THREE and table[3][3] == table[5][3] == T14C_FIVE)

    # 4. the mirror: same row (T14 Thm 4.3(i)); even algebras isomorphic (T14c Thm 8.1)
    GA.check("mirror r = 2 row equals this tower's r = 6 row", table[2] == table[6])
    for (p, q) in ((1, 3), (2, 4)):
        s1 = squares(p, q)
        s2 = tuple(-x for x in s1)    # every Q(e_a) negated: signature (q, p)
        ev = even_blades(p + q)
        phi = lambda x: {B: c * (-1 if (len(B) // 2) % 2 else 1) for B, c in x.items()}
        ok = all(GA.eq(phi(GA.mul({K1: ONE}, {L1: ONE}, s1)),
                       GA.mul(phi({K1: ONE}), phi({L1: ONE}), s2)) for K1 in ev for L1 in ev)
        GA.check(f"e_K -> (-1)^(|K|/2) e_K is an isomorphism Cl^0({p},{q}) -> Cl^0({q},{p})", ok)
    for (p, q) in ((2, 4), (4, 2)):
        cen, sq = even_centre(p, q)
        I6 = {tuple(range(6)): ONE}
        GA.check(f"centre of Cl^0({p},{q}) is span(1, I6), Q-square I6^2 = -1",
                 sorted(cen) == sorted([(), tuple(range(6))]) and GA.eq(GA.mul(I6, I6, sq), GA.sc(-1)))
    # the rejected reading (commutant of the full Clifford module, T14c Remark 'why U'):
    # H for (1,3) and R for (3,1), so the mirror's row would differ from ours
    full_ours, full_mirror = full_field_dim(1, 3), full_field_dim(3, 1)
    GA.check("full-module commutant: H (dim 4, noncommutative) for (1,3), R (dim 1) for (3,1)",
             full_ours == (4, False) and full_mirror == (1, True))

    # 5. wrong inputs give other numbers
    GA.check("wrong a (three constituents): 17, not 12", cache[("C", 3, 3)][0] != T12_ROW)
    GA.check("wrong b (two pairs): 7, not 12", cache[("C", 2, 2)][0] == 7 != T12_ROW)
    GA.check("wrong field (real pairs, R^2 (x) R^3): 4, not 12", cache[("R", 2, 3)][0] == 4 != T12_ROW)
    GA.check("one constituent in dimension four (C^1 (x) C^3): 9, not 12", cache[("C", 1, 3)][0] != T12_ROW)
    return True


if __name__ == "__main__":
    test_gauge_algebra_by_tower()
    print("failures:", GA.FAILURES)
