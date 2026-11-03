"""one-relation.two-capacities-three-consequences: exact checks.

Quadratic spaces R^{p,q} with the diagonal form of GA.sig(p,q); complex vectors as Gaussian-rational
coordinate lists (GA.QI). Real null pairs (e_i +- e_{p+i})/2 for i < min(p,q); on the remaining definite
part, complex pairs (e + i e')/2, -(e - i e')/2 on consecutive blocks.
(1) Real capacity: for every (p,q) with p, q <= 5 the min(p,q) real pairs are pairwise anticommuting
    ladder pairs (complex-bilinear pairings: <w_i, w_j> = <wb_i, wb_j> = 0, <w_i, wb_j> = delta_ij/2), and
    the form on W-perp/W (W their real span) is definite of dimension |p - q|, so no real isotropic
    subspace contains W properly; by Witt's theorem (premise) all maximal ones have this dimension.
(2) Complex capacity: floor(d/2) pairs (real ones plus complex ones) with the same pairings; the
    isotropic U they span has dim U^perp = d - dim U (nondegenerate), U in U^perp, and for d odd the
    quotient U^perp/U is spanned by a vector of nonzero square, so U is maximal: 2 dim U <= d is attained.
(3) The capacities agree iff |p - q| <= 1 on the grid p, q <= 8; (1,3) gives (1, 2) and (2,4) gives (2, 3);
    each (1,1) ascent raises both by exactly one.
(4) Consequence 1: the complement of the boost plane in (1,3) is negative definite (congruence signature
    (0, 2)); the complex reading of Cl(1,3) has a Fock module of dimension 2^2 = 4 (computed in Cl(1,3)
    with Q(i) coefficients), the Dirac spinor.
(5) Consequence 3: r_C(2,4) = 3 = (n + 2)/2 at n = 4, and r_R(2,4) = 2: the third pair is complex only.
"""
from fractions import Fraction as F
from functools import reduce
from itertools import combinations, product

import GA
from tp_premise import premise

QI = GA.QI
GRID5 = [(p, q) for p in range(6) for q in range(6) if p + q >= 1]


def r_real(p, q):
    return min(p, q)


def r_cplx(p, q):
    return (p + q) // 2


def pairs(p, q):
    """(w, wbar) as complex coordinate lists, real pairs first."""
    n = p + q
    S = GA.sig(p, q)
    out = []
    k = min(p, q)
    for i in range(k):
        w = [QI(0)] * n
        wb = [QI(0)] * n
        w[i], w[p + i] = QI(F(1, 2)), QI(F(1, 2))
        wb[i], wb[p + i] = QI(F(1, 2)), QI(F(-1, 2))
        out.append((w, wb))
    rest = list(range(k, p)) + list(range(p + k, n))
    for j in range(0, len(rest) - 1, 2):
        a, b = rest[j], rest[j + 1]
        s = S[a]
        w = [QI(0)] * n
        wb = [QI(0)] * n
        w[a], w[b] = QI(F(1, 2)), QI(0, F(1, 2))
        wb[a], wb[b] = QI(F(s, 2)), QI(0, F(-s, 2))
        out.append((w, wb))
    return out, rest


def bil(u, v, S):
    return sum((u[i] * v[i] * S[i] for i in range(len(S))), QI(0))


def check_real_capacity_is_min_pq():
    premise("tower.witt-index-quantum-capacity")
    premise("one-relation.imported-witts-extension-theorem")
    ok = True
    for p, q in GRID5:
        S = GA.sig(p, q)
        n = p + q
        P, rest = pairs(p, q)
        k = r_real(p, q)
        real = P[:k]
        ok = ok and all(x.im == 0 for w, wb in real for x in w + wb)
        for i in range(k):
            for j in range(k):
                ok = ok and bil(real[i][0], real[j][0], S) == 0 and bil(real[i][1], real[j][1], S) == 0
                ok = ok and bil(real[i][0], real[j][1], S) == (QI(F(1, 2)) if i == j else QI(0))
        # W-perp / W: the generators outside the real pairs; the form there is diagonal and definite
        sig = GA.congruence_signature([[F(S[a]) if a == b else F(0) for b in rest] for a in rest]) if rest else (0, 0, 0)
        ok = ok and len(rest) == abs(p - q) and (sig[0] == 0 or sig[1] == 0) and sig[2] == 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_real_capacity_is_min_pq"; return _tp_rv


def check_complex_capacity_is_floor_half_d():
    premise("one-relation.two-presentations")
    ok = True
    for p, q in GRID5:
        S = GA.sig(p, q)
        n = p + q
        P, rest = pairs(p, q)
        ok = ok and len(P) == r_cplx(p, q)
        r = len(P)
        for i in range(r):
            for j in range(r):
                ok = ok and bil(P[i][0], P[j][0], S) == 0 and bil(P[i][1], P[j][1], S) == 0
                ok = ok and bil(P[i][0], P[j][1], S) == (QI(F(1, 2)) if i == j else QI(0))
        U = [w for w, wb in P]
        rows = [[u[i] * S[i] for i in range(n)] for u in U]
        perp = GA.field_kernel(rows) if rows else [[QI(1 if i == j else 0) for i in range(n)] for j in range(n)]
        ok = ok and len(perp) == n - r and GA.field_rank(rows) == r
        ok = ok and all(GA.field_rank(perp + [u]) == len(perp) for u in U)
        if n % 2 == 1:
            # one generator is left over; its square is nonzero, so U^perp/U is anisotropic
            used = {i for w, wb in P for i in range(n) if w[i] != 0}
            left = [i for i in range(n) if i not in used]
            ok = ok and len(left) == 1 and S[left[0]] != 0
    _tp_rv = (ok); assert _tp_rv is not False, "check_complex_capacity_is_floor_half_d"; return _tp_rv


def check_agreement_locus_and_increments():
    premise("tower.witt-index-quantum-capacity")
    ok = True
    for p in range(9):
        for q in range(9):
            ok = ok and (r_real(p, q) == r_cplx(p, q)) == (abs(p - q) <= 1)
            ok = ok and r_real(p + 1, q + 1) == r_real(p, q) + 1 and r_cplx(p + 1, q + 1) == r_cplx(p, q) + 1
            if p + q >= 1 and p <= 5 and q <= 5:
                P, rest = pairs(p, q)
                ok = ok and len(P) == r_cplx(p, q) and sum(1 for w, wb in P if all(x.im == 0 for x in w)) >= r_real(p, q)
    ok = ok and (r_real(1, 3), r_cplx(1, 3)) == (1, 2) and (r_real(2, 4), r_cplx(2, 4)) == (2, 3)
    _tp_rv = (ok); assert _tp_rv is not False, "check_agreement_locus_and_increments"; return _tp_rv


# Sample coefficient pairs (a, b) for vectors a e + b e' in the complement of the boost plane.
COMPLEMENT_SAMPLES = ((F(1), F(2)), (F(-3), F(1, 2)), (F(0), F(5)))


def coords_qi(x, blades):
    """Coordinate row of a Q(i)-coefficient multivector on the given blades."""
    return [x.get(b, QI(0)) for b in blades]


def check_boost_qubit_and_dirac_fock_space():
    premise("tower.witt-index-quantum-capacity")
    S = GA.sig(1, 3)
    n = len(S)
    ok = GA.congruence_signature([[GA.dot(GA.gen(i), GA.gen(j), S) for j in range(n)] for i in range(n)]) == (1, 3, 0)
    P, rest = pairs(1, 3)
    # the pairs live in the same space as S; one real pair (r_R(1,3) = 1), complex capacity two in all
    ok = ok and all(len(c) == n for pr in P for c in pr)
    ok = ok and sum(all(x.im == 0 for c in pr for x in c) for pr in P) == 1 and len(P) == 2
    # the complement of the boost plane is negative definite of dimension n - 2
    G = [[GA.dot(GA.gen(i), GA.gen(j), S) for j in rest] for i in rest]
    ok = ok and len(rest) == n - 2 and GA.congruence_signature(G) == (0, n - 2, 0)
    for a, b in COMPLEMENT_SAMPLES:
        x = GA.add(GA.scal(a, GA.gen(rest[0])), GA.scal(b, GA.gen(rest[1])))
        ok = ok and GA.mul(x, x, S)[()] == -(a * a + b * b)

    def mv(c):
        return {(i,): c[i] for i in range(len(c)) if c[i] != 0}
    Om = reduce(lambda x, y: GA.mul(x, y, S), [mv(wb) for w, wb in P])
    states = []
    for mask in product((False, True), repeat=len(P)):
        x = Om
        for (w, wb), on in zip(P, mask):
            if on:
                x = GA.mul(mv(w), x, S)
        states.append(x)
    bl = GA.all_blades(n)
    ok = ok and Om != {} and GA.field_rank([coords_qi(s, bl) for s in states]) == 4
    _tp_rv = (ok); assert _tp_rv is not False, "check_boost_qubit_and_dirac_fock_space"; return _tp_rv


def check_ascended_capacity_three_complex_two_real():
    premise("tower.witt-index-quantum-capacity")
    P, rest = pairs(2, 4)
    ok = len(P) == 3 == (4 + 2) // 2
    nreal = sum(1 for w, wb in P if all(x.im == 0 for x in w + wb))
    ok = ok and nreal == 2 == r_real(2, 4)
    ok = ok and rest == [4, 5] and GA.sig(2, 4)[4] == GA.sig(2, 4)[5] == -1
    # the pair count (n + 2)/2 of ambient signature (2, n), n even, is the computed complex capacity
    for n in (2, 4, 6, 8):
        ok = ok and len(pairs(2, n)[0]) == r_cplx(2, n) == (n + 2) // 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_ascended_capacity_three_complex_two_real"; return _tp_rv
