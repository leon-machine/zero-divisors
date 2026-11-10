"""Invariant bilinear forms on the Fock module of Cl(k,k), and the pair counts they give a next level.

Everything is computed in GA.py inside B_k = Cl(k,k), generators e_j (square +1) and f_j (square -1),
null pairs v_j = (e_j + f_j)/2, w_j = (e_j - f_j)/2, vacuum idempotent P = prod_j w_j v_j, Fock module
F_k = B_k P with basis v_S P (S a subset of the k rungs), Omega = v_1 ... v_k. For tau the reverse
(eps = +1) or the reverse composed with the grade involution (eps = -1), the form beta_eps is read off
tau(psi) phi = beta_eps(psi, phi) Omega. Exact rational arithmetic throughout.

check_forms_are_invariant_and_unique (k = 1, 2, 3): w_j P = 0, Omega P = Omega, the 2^k states are
    independent, every tau(psi) phi is a multiple of Omega, the matrices of the generators (read through
    the vacuum coefficient P w_T x) satisfy A^T G = eps G A, and the space of ALL bilinear forms with that
    adjoint property has dimension exactly one for each eps.
check_symmetry_law_neutral_signature_and_parity_pairing (k = 1..4): beta_eps is symmetric or antisymmetric
    by the sign eps^k (-1)^(k(k-1)/2), nonzero only between a state and its complement (grades s, k - s),
    of full rank; when symmetric its signature is (2^(k-1), 2^(k-1)).
check_counts_at_three_and_the_two_iterations: at k = 3 one form is antisymmetric and the other symmetric of
    signature (4, 4) with both parity halves totally null; the bivectors of B_3 annihilate no state of F_3 and
    commute with the new pair of B_4 (the count 4 = 3 + 1 is not the ascent); at k = 2 both are antisymmetric; 2^(k-1) = k + 1
    only at k = 3 (scanned, with the induction in the proof); the iteration k -> 2^(k-1) from three, its
    residues mod 4 and state counts, and where the bracket 2^407 < |J| < 2^408 quoted in the stored base
    result falls in it. The rule k -> 2^k is the base result's and is not recomputed.
Not computed: the statements for every k (the proof's), the isometry with the next rung's vector space
(equal signature, by the Witt decomposition), and the audit that no stored result selects either rule.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

KS_FULL = (1, 2, 3)
KS_GRAM = (1, 2, 3, 4)
K_SCAN = 64
OLD_GENS, NEW_GENS = (0, 1, 2, 4, 5, 6), (3, 7)     # generators of B_3 inside B_4, and the new pair's
LIMIT = 300        # no power 2^n with n above this is ever formed (the fourth doubling is 2^(2^256))


def next_by_forms(k):
    assert k <= LIMIT
    return 2 ** (k - 1)


def next_by_doubling(k):
    assert k <= LIMIT
    return 2 ** k


def setup(k):
    sq = tuple([1] * k + [-1] * k)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    P = GA.sc(1)
    for j in range(k):
        P = GA.mul(P, GA.mul(w[j], v[j], sq), sq)
    return sq, v, w, P


def subsets(k):
    return [S for r in range(k + 1) for S in combinations(range(k), r)]


def word(vs, S, sq):
    x = GA.sc(1)
    for j in S:
        x = GA.mul(x, vs[j], sq)
    return x


def tau_of(eps):
    if eps == 1:
        return GA.reverse
    return lambda x: GA.reverse(GA.grade_inv(x))


def multiple_of(z, ref):
    """The rational c with z = c ref, or None."""
    if z == {}:
        return F(0)
    b = next(iter(ref))
    c = z.get(b, F(0)) / ref[b]
    return c if GA.eq(z, GA.scal(c, ref)) else None


def gram(k, eps):
    sq, v, w, P = setup(k)
    tau = tau_of(eps)
    S_all = subsets(k)
    st = [GA.mul(word(v, S, sq), P, sq) for S in S_all]
    omega = word(v, tuple(range(k)), sq)
    G = []
    for x in st:
        row = []
        for y in st:
            c = multiple_of(GA.mul(tau(x), y, sq), omega)
            assert c is not None
            row.append(c)
        G.append(row)
    return S_all, st, G


def symmetry_sign(G):
    n = len(G)
    if all(G[i][j] == G[j][i] for i in range(n) for j in range(n)):
        return 1
    if all(G[i][j] == -G[j][i] for i in range(n) for j in range(n)):
        return -1
    return 0


def operator_matrix(k, a, st, S_all):
    """Matrix of left multiplication by a on the basis v_S P, through P w_T x = (coefficient) P."""
    sq, v, w, P = setup(k)
    A = [[F(0)] * len(st) for _ in st]
    for s, x in enumerate(st):
        ax = GA.mul(a, x, sq)
        for t, T in enumerate(S_all):
            wT = word(w, tuple(reversed(T)), sq)
            c = multiple_of(GA.mul(P, GA.mul(wT, ax, sq), sq), P)
            assert c is not None
            A[t][s] = c
    return A


def check_forms_are_invariant_and_unique():
    premise("tower.fock-module-one-qubit-per-rung")
    premise("std-algebra.fock-representation")       # the left ideal on the vacuum idempotent, families exchanged
    for k in KS_FULL:
        sq, v, w, P = setup(k)
        n = 2 ** k
        omega = word(v, tuple(range(k)), sq)
        assert GA.eq(GA.mul(P, P, sq), P)
        assert all(GA.is_zero(GA.mul(w[j], P, sq)) for j in range(k))
        assert GA.eq(GA.mul(omega, P, sq), omega) and not GA.is_zero(omega)
        gens = [GA.gen(i) for i in range(2 * k)]
        mats = None
        for eps in (1, -1):
            S_all, st, G = gram(k, eps)
            blades = GA.all_blades(2 * k)
            assert len(st) == n and GA.rank_of_vectors([GA.basis_vector_of(x, blades) for x in st]) == n
            if mats is None:
                mats = [operator_matrix(k, a, st, S_all) for a in gens]
                for i, A in enumerate(mats):          # a module of B_k: squares +1, -1
                    assert GA.mat_eq(GA.mat_mul(A, A), [[F(sq[i]) * (r == c) for c in range(n)] for r in range(n)])
            rows = []
            for A in mats:
                At = [list(r) for r in zip(*A)]
                assert GA.mat_eq(GA.mat_mul(At, G), [[eps * z for z in r] for r in GA.mat_mul(G, A)])
                # all forms X with A^T X = eps X A: one linear equation per entry (i, j)
                for i in range(n):
                    for j in range(n):
                        row = [F(0)] * (n * n)
                        for u in range(n):
                            row[u * n + j] += A[u][i]
                            row[i * n + u] -= eps * A[u][j]
                        rows.append(row)
            assert n * n - GA.mat_rank(rows) == 1
    return True


def check_symmetry_law_neutral_signature_and_parity_pairing():
    premise("tower.fock-module-one-qubit-per-rung")
    premise("std-algebra.chevalley-pairing")         # eps = +1: the stored symmetry law and grade pairing
    seen = []
    for k in KS_GRAM:
        n = 2 ** k
        for eps in (1, -1):
            S_all, st, G = gram(k, eps)
            law = eps ** k * (-1) ** (k * (k - 1) // 2)
            assert symmetry_sign(G) == law
            seen.append((k, eps, law))
            assert GA.mat_rank(G) == n
            for i, S in enumerate(S_all):
                for j, T in enumerate(S_all):
                    complementary = sorted(S + T) == list(range(k))
                    assert (G[i][j] != 0) == complementary
                    if complementary:
                        assert G[i][j] * G[i][j] == 1 and len(S) + len(T) == k
            if law == 1:
                assert GA.congruence_signature(G) == (2 ** (k - 1), 2 ** (k - 1), 0)
    assert [(k, e) for k, e, s in seen if s == 1] == [(1, 1), (3, -1), (4, 1), (4, -1)]
    assert [(k, e) for k, e, s in seen if s == -1] == [(1, -1), (2, 1), (2, -1), (3, 1)]
    return True


def check_counts_at_three_and_the_two_iterations():
    premise("tower.fock-module-one-qubit-per-rung")
    premise("tower.witt-index-quantum-capacity")
    premise("synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent")
    # the base supplies the first rule (3, 8, 256, 2^256), the ascent's four and the bracket 2^407 < |J| < 2^408
    S_all, st, G_rev = gram(3, 1)
    _, _, G_con = gram(3, -1)
    assert symmetry_sign(G_rev) == -1 and GA.mat_rank(G_rev) == 8
    assert symmetry_sign(G_con) == 1 and GA.congruence_signature(G_con) == (4, 4, 0)
    witt_index = min(GA.congruence_signature(G_con)[:2])
    assert witt_index == 3 + 1                       # the pair count of the next rung of the tower
    for parity in (0, 1):                            # each parity half is totally null, of dimension four
        idx = [i for i, S in enumerate(S_all) if len(S) % 2 == parity]
        assert len(idx) == 4 and all(G_con[i][j] == 0 for i in idx for j in idx)
    # not the ascent: the 15 bivectors of B_3 have common kernel zero on F_3 (rank 8 of the stacked matrices),
    # while on the vector space of B_4 they commute with the new pair
    mats = [operator_matrix(3, GA.gen(i), st, S_all) for i in range(6)]
    stacked = [row for i in range(6) for j in range(i + 1, 6) for row in GA.mat_mul(mats[i], mats[j])]
    assert len(stacked) == 15 * 8 and GA.mat_rank(stacked) == 8
    sq4 = tuple([1] * 4 + [-1] * 4)
    assert all(GA.commutes(GA.mul(GA.gen(i), GA.gen(j), sq4), GA.gen(n), sq4)
               for i in OLD_GENS for j in OLD_GENS if i < j for n in NEW_GENS)
    assert all(symmetry_sign(gram(2, eps)[2]) == -1 for eps in (1, -1))
    assert [k for k in range(1, K_SCAN + 1) if 2 ** (k - 1) == k + 1] == [3]
    forms = [3]
    for _ in range(4):
        forms.append(next_by_forms(forms[-1]))
    assert forms == [3, 4, 8, 128, 2 ** 127]
    assert all(x % 4 == 0 for x in forms[1:])        # a symmetric invariant form exists at every later level
    assert [next_by_doubling(x) for x in forms[:4]] == [8, 16, 256, 2 ** 128]     # the state counts
    assert 3 * 10 ** 38 < 2 ** 128 < 4 * 10 ** 38
    # given the base's bracket 2^407 < |J| < 2^408: between the terms 2^127 and 2^(2^127 - 1) of this rule
    assert forms[4] < 2 ** 407 and 408 < forms[4] - 1
    return True
