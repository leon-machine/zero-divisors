"""dark-matter.flag-bit-exists-exactly-tower-dimension: exact checks.

Fock model in GA.py on the split form of the ambient dimension 2m (e_0..e_{m-1} square +1,
e_m..e_{2m-1} square -1, plus one extra generator ell of square +1 in odd dimension 2m+1): null pairs
w_i = (e_i + e_{m+i})/2, v_i = (e_i - e_{m+i})/2, W = span(w), W' = span(v), f = w_1...w_m (pure spinor
of W), top = v_1...v_m f (pure spinor of W'), I = e_0...e_{2m-1} (chirality, I^2 = 1).
Even ambient (m = 1..4, tower dimension n = 2m - 2 = 0, 2, 4, 6): the chirality of every Fock state
v_S f is (-1)^|S| times that of f, so the pure spinors of W and W' (grades 0 and m) have opposite
chirality iff m is odd; the isometry negating the partners e_m..e_{2m-1} carries W to W' and has
determinant (-1)^m (so for m even W and W' lie in one SO(2m, C) orbit). With the premise that versors of
the connected group keep chirality (two-families-are-two-chiralities), the choice of W against W' is a
bit iff m is odd iff n = 0 mod 4 (checked for n = 0, 2, 4, 6, 8, 10 through m = (n + 2)/2).
(i) Odd ambient 2m + 1 (m = 1, 2, 3): omega is central; a determinant +1 isometry carries W to W'; the
spin-algebra element ell v_1 sends the grade-0 state f P (P = (1 + omega)/2) to a multiple of the grade-1
state v_1 f P; and p - q is odd iff p + q is odd, so every signature of an odd residue is odd-dimensional.
(ii) Under P3 the even residues are represented in dimension four (m = 3: bit); the causal
representatives (1,1) of r = 0 and (1,5) of r = 4 of the other windows have n = 2, 6 (m = 2, 4: no bit).
"""
from fractions import Fraction as F
from itertools import combinations
import GA
from tp_premise import premise


def fock(m, extra=0):
    sq = tuple([1] * m + [-1] * m + [1] * extra)
    w = [GA.scal(F(1, 2), GA.add(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    v = [GA.scal(F(1, 2), GA.sub(GA.gen(i), GA.gen(m + i))) for i in range(m)]
    f = GA.sc(1)
    for x in w:
        f = GA.mul(f, x, sq)
    I = GA.sc(1)
    for i in range(2 * m):
        I = GA.mul(I, GA.gen(i), sq)
    return sq, w, v, f, I


def state(S, v, f, sq):
    y = f
    for i in reversed(S):
        y = GA.mul(v[i], y, sq)
    return y


def eigen(I, psi, sq):
    for lam in (1, -1):
        if GA.eq(GA.mul(I, psi, sq), GA.scal(lam, psi)):
            return lam
    return None


def det(M):
    M = [row[:] for row in M]
    n, d = len(M), F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            M[c], M[p] = M[p], M[c]
            d = -d
        d *= M[c][c]
        for r in range(c + 1, n):
            t = M[r][c] / M[c][c]
            M[r] = [a - t * b for a, b in zip(M[r], M[c])]
    return d


def isometry_data(sq, signs, m):
    """Diagonal map with the given signs: (preserves the form, carries W to W', determinant)."""
    n = len(sq)
    keeps = all(signs[i] * signs[i] == 1 for i in range(n))
    to_wp = all(signs[i] == 1 and signs[m + i] == -1 for i in range(m))
    D = [[F(signs[i]) if i == j else F(0) for j in range(n)] for i in range(n)]
    return keeps, to_wp, det(D)


def flips(m):
    """True iff the pure spinors of W and W' have opposite chirality (computed in the Fock model)."""
    sq, w, v, f, I = fock(m)
    return eigen(I, f, sq) == -eigen(I, state(tuple(range(m)), v, f, sq), sq)


def check_bit_iff_tower_dimension_zero_mod_four():
    premise("dark-matter.two-families-are-two-chiralities")
    ok = True
    flip = {}
    for m in range(1, 5):
        sq, w, v, f, I = fock(m)
        ok = ok and GA.eq(GA.mul(I, I, sq), GA.sc(1))
        lam = eigen(I, f, sq)
        ok = ok and all(GA.is_zero(GA.mul(x, f, sq)) for x in w)
        top = state(tuple(range(m)), v, f, sq)
        ok = ok and all(GA.is_zero(GA.mul(x, top, sq)) for x in v) and not GA.is_zero(top)
        for k in range(m + 1):
            for S in combinations(range(m), k):
                ok = ok and eigen(I, state(S, v, f, sq), sq) == lam * (-1) ** k
        flip[m] = flips(m)
        keeps, to_wp, d = isometry_data(sq, [1] * m + [-1] * m, m)
        ok = ok and keeps and to_wp and d == (-1) ** m
    ok = ok and flip == {1: True, 2: False, 3: True, 4: False}
    bit = {2 * m - 2: flip[m] for m in flip}
    ok = ok and bit == {0: True, 2: False, 4: True, 6: False}
    ok = ok and all(((n + 2) // 2) % 2 == (1 if n % 4 == 0 else 0) for n in range(0, 12, 2))
    GA.check("thm:paritybit: f and the top state have opposite chirality iff m is odd (m = 1..4), the "
             "partner-negating isometry has det (-1)^m; the bit exists iff n = 0 mod 4", ok)
    return ok


def check_odd_ambient_no_bit():
    premise("dark-matter.two-families-are-two-chiralities")
    ok = True
    for m in (1, 2, 3):
        sq, w, v, f, Gam = fock(m, 1)
        n = 2 * m + 1
        ell = GA.gen(2 * m)
        om = GA.mul(Gam, ell, sq)
        ok = ok and all(GA.commutes(om, GA.gen(i), sq) for i in range(n))
        signs = [1] * m + [-1] * m + [(-1) ** m]
        keeps, to_wp, d = isometry_data(sq, signs, m)
        ok = ok and keeps and to_wp and d == 1
        P = GA.scal(F(1, 2), GA.add(GA.sc(1), om))
        fP = GA.mul(f, P, sq)
        v1fP = GA.mul(v[0], fP, sq)
        img = GA.mul(GA.mul(ell, v[0], sq), fP, sq)
        ok = ok and not GA.is_zero(img) and (GA.eq(img, v1fP) or GA.eq(img, GA.neg(v1fP)))
        ok = ok and eigen(Gam, fP, sq) == -eigen(Gam, v1fP, sq)
    ok = ok and all(((p - q) % 2 == 1) == ((p + q) % 2 == 1) for p in range(12) for q in range(12))
    GA.check("thm:paritybit(i): odd ambient (m = 1, 2, 3): omega central, a det +1 isometry carries W to W', "
             "ell v_1 mixes Fock grades 0 and 1; odd residues are odd-dimensional", ok)
    return ok


def check_even_residues_at_p3_and_other_windows():
    premise("dark-matter.p3-nearest-dimension-representatives")
    premise("dark-matter.two-families-are-two-chiralities")
    sigs = [(p, q) for p in range(7) for q in range(7) if 1 <= p + q <= 6]
    p3 = {r: sorted(s for s in sigs if sum(s) == 4 and (s[0] - s[1]) % 8 == r) for r in (0, 2, 4, 6)}
    ok = p3 == {0: [(2, 2)], 2: [(3, 1)], 4: [(0, 4), (4, 0)], 6: [(1, 3)]}
    carries = {r: all(flips((p + q + 2) // 2) for p, q in p3[r]) for r in p3}
    ok = ok and carries == {0: True, 2: True, 4: True, 6: True}
    alt = {(1, 1): flips(2), (1, 5): flips(4)}
    ok = ok and alt == {(1, 1): False, (1, 5): False}
    ok = ok and (1 - 1) % 8 == 0 and (1 - 5) % 8 == 4
    GA.check("thm:paritybit(ii): the P3 representatives of r = 0, 2, 4, 6 (dimension four) carry the bit; "
             "(1,1) and (1,5) do not", ok)
    return ok
