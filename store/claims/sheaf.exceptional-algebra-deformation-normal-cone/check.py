"""sheaf.exceptional-algebra-deformation-normal-cone: exact checks.

Transversal families G(t) = G0 + t Gdot + t^2 G2 on n = 2, 3, 4 in an adapted frame (k, v_1, ..., v_(n-1)):
k spans the radical of G0, G0|V1 is a general nondegenerate form of signature (p - 1, q) (non-orthogonal,
G1 = P^T diag P), Gdot and G2 are general symmetric matrices (all cross terms nonzero), and
Gdot(k, k) = T > 0 (the physical side; T < 0 as a control). With sigma = sqrt(t) as the exact variable
(GA.RF), the rescaled frame (k/sigma, v_i) has Gram R(sigma).
(1) Every entry of R(sigma) is a polynomial in sigma (continuity through t = 0), R(0) is block diagonal
    G0|V1 + Gdot(k, k), the cross terms are O(sigma) (R_0i/sigma is again a polynomial), and the limit is
    nondegenerate of signature (p, q) for T > 0 and (p - 1, q + 1) for T < 0; for every (p, q), p >= 1, n <= 4.
(2) The special fibre: in the exterior model with Gram R(s) at s = 0 and at sample s, c(a)^2 = R(s)(a, a)
    on all basis states and the 2^n blades are a basis; at s = 0 every structure constant
    c(e_i) c(e_j) |0> agrees with the one built from G0|V1 + Gdot(k, k) assembled directly.
(3) Independence of choices: a complement change v_i -> v_i + c_i k leaves the limit form literally equal;
    k -> c k multiplies the limit entry by c^2 and diag(c, 1, ...) is an isometry of the two limit forms;
    t -> a t (a = 4, 9/4) multiplies the entry by a and k -> k/sqrt(a) is the isometry back; k -> -k is a
    second isometry fixing V1 (canonical means choice-free, not unique).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

RF = GA.RF
SIGMA = RF.var()
SIGS = [(p, n - p) for n in (2, 3, 4) for p in range(1, n + 1)]
S_SAMPLES = [F(1, 2), F(-1, 3)]
# the special fibre s = 0 and the sample general fibres, on which the exterior model is tested
FIBRE_POINTS = [F(0)] + S_SAMPLES
# sample Gdot(k, k) on the physical side (T > 0)
T_PHYSICAL = F(3)
# sample vector a (truncated to n) for c(a)^2 = R(s)(a, a)
SAMPLE_A = [F(1), F(2), F(3), F(4)]
# the vacuum state |0> of the exterior model
VACUUM = {frozenset(): F(1)}


def unit(i, n):
    """The i-th standard basis vector of length n."""
    return [F(1) if t == i else F(0) for t in range(n)]


def _mm(A, B):
    return [[sum((A[i][t] * B[t][j] for t in range(len(B))), F(0)) for j in range(len(B[0]))]
            for i in range(len(A))]


def family(p, q, T):
    """(G0, Gdot, G2) on the adapted frame (k, v_1..v_(n-1))."""
    n = p + q
    m = n - 1
    D = [[F(0)] * m for _ in range(m)]
    for i in range(m):
        D[i][i] = F(1) if i < p - 1 else F(-1)
    P = [[F(1) if i == j else (F(i - j + 1) if j > i else F(0)) for j in range(m)] for i in range(m)]
    G1 = _mm([list(r) for r in zip(*P)], _mm(D, P))
    G0 = [[F(0)] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            G0[i + 1][j + 1] = G1[i][j]
    Gd = [[F((i * 3 + j * 3 + i * j) % 7 - 3) for j in range(n)] for i in range(n)]
    G2 = [[F((i + j) % 4 + 1) for j in range(n)] for i in range(n)]
    Gd[0][0] = T
    return G0, Gd, G2


def gram_t(G0, Gd, G2, i, j, a=F(1)):
    """G(a t)(i, j) as a polynomial in sigma, t = sigma^2."""
    t = SIGMA * SIGMA * RF.const(a)
    return RF.const(G0[i][j]) + t * RF.const(Gd[i][j]) + t * t * RF.const(G2[i][j])


def rescaled(G0, Gd, G2, a=F(1)):
    n = len(G0)
    R = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            e = gram_t(G0, Gd, G2, i, j, a)
            if i == 0:
                e = e / SIGMA
            if j == 0:
                e = e / SIGMA
            R[i][j] = e
    return R


def hat(G0, Gd):
    n = len(G0)
    H = [[F(0)] * n for _ in range(n)]
    H[0][0] = Gd[0][0]
    for i in range(1, n):
        for j in range(1, n):
            H[i][j] = G0[i][j]
    return H


def check_rescaled_limit_and_signature():
    premise("sheaf.tameness")              # Gdot(k, k) != 0 (T3)
    premise("sheaf.degeneration-sheaf")    # G0 | V1 nondegenerate of signature (p - 1, q)
    ok = True
    for (p, q) in SIGS:
        for T in (F(3), F(-2)):
            G0, Gd, G2 = family(p, q, T)
            n = p + q
            ok = ok and GA.congruence_signature([r[1:] for r in G0[1:]]) == (p - 1, q, 0)
            R = rescaled(G0, Gd, G2)
            ok = ok and all(len(R[i][j].den) == 1 for i in range(n) for j in range(n))
            lim = [[R[i][j].eval(0) for j in range(n)] for i in range(n)]
            ok = ok and lim == hat(G0, Gd)
            ok = ok and all(R[0][i].eval(0) == 0 and len((R[0][i] / SIGMA).den) == 1 for i in range(1, n))
            ok = ok and any(not R[0][i].is_zero() for i in range(1, n))
            want = (p, q, 0) if T > 0 else (p - 1, q + 1, 0)
            ok = ok and GA.congruence_signature(lim) == want
    _tp_rv = (ok); assert _tp_rv is not False, "check_rescaled_limit_and_signature"; return _tp_rv


def check_special_fibre_is_the_limit_algebra():
    premise("sheaf.blade-basis-degenerate-forms-included")
    ok = True
    for (p, q) in SIGS:
        G0, Gd, G2 = family(p, q, T_PHYSICAL)
        n = p + q
        R = rescaled(G0, Gd, G2)
        Hh = hat(G0, Gd)
        vac = VACUUM
        for s in FIBRE_POINTS:
            Rs = [[R[i][j].eval(s) for j in range(n)] for i in range(n)]
            blades = GA.all_blades(n)
            rows = []
            for I in blades:
                st = GA.ext_sigma_blade(I, Rs, n)
                rows.append([st.get(frozenset(J), F(0)) for J in blades])
            ok = ok and GA.rank_of_vectors(rows) == 2 ** n
            a = SAMPLE_A[:n]
            raa = sum((a[i] * Rs[i][j] * a[j] for i in range(n) for j in range(n)), F(0))
            for J in blades:
                st = {frozenset(J): F(1)}
                ok = ok and GA.ext_state_eq(GA.ext_c(a, Rs, GA.ext_c(a, Rs, st)), {frozenset(J): raa} if raa else {})
        # the special fibre (s = 0): every c(e_i) c(e_j) |0> agrees with the one built from G0|V1 + Gdot(k, k)
        R0 = [[R[i][j].eval(0) for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                ei, ej = unit(i, n), unit(j, n)
                lhs = GA.ext_c(ei, R0, GA.ext_c(ej, R0, vac))
                rhs = GA.ext_c(ei, Hh, GA.ext_c(ej, Hh, vac))
                ok = ok and GA.ext_state_eq(lhs, rhs)
    _tp_rv = (ok); assert _tp_rv is not False, "check_special_fibre_is_the_limit_algebra"; return _tp_rv


def check_limit_independent_of_choices():
    premise("sheaf.tameness")
    ok = True
    for (p, q) in SIGS:
        G0, Gd, G2 = family(p, q, F(3))
        n = p + q
        H = hat(G0, Gd)
        # complement change v_i -> v_i + c_i k
        c = [None] + [F(2 - i, i + 1) for i in range(1, n)]
        for i in range(1, n):
            cross = (gram_t(G0, Gd, G2, 0, i) + RF.const(c[i]) * gram_t(G0, Gd, G2, 0, 0)) / SIGMA
            ok = ok and cross.eval(0) == 0 and len(cross.den) == 1
            for j in range(1, n):
                e = (gram_t(G0, Gd, G2, i, j) + RF.const(c[i]) * gram_t(G0, Gd, G2, 0, j)
                     + RF.const(c[j]) * gram_t(G0, Gd, G2, i, 0) + RF.const(c[i] * c[j]) * gram_t(G0, Gd, G2, 0, 0))
                ok = ok and e.eval(0) == H[i][j]
        # k -> c k
        for cc in (F(3), F(-2), F(1, 2)):
            e = RF.const(cc * cc) * gram_t(G0, Gd, G2, 0, 0) / (SIGMA * SIGMA)
            Hc = [row[:] for row in H]
            Hc[0][0] = e.eval(0)
            ok = ok and Hc[0][0] == cc * cc * Gd[0][0]
            Dm = [[(cc if i == 0 else F(1)) if i == j else F(0) for j in range(n)] for i in range(n)]
            ok = ok and _mm(Dm, _mm(H, Dm)) == Hc
        # t -> a t, with sqrt(a) rational
        for a, ra in ((F(4), F(2)), (F(9, 4), F(3, 2))):
            Ra = rescaled(G0, Gd, G2, a)
            Ha = [[Ra[i][j].eval(0) for j in range(n)] for i in range(n)]
            ok = ok and Ha[0][0] == a * Gd[0][0] and all(Ha[i][j] == H[i][j] for i in range(1, n) for j in range(1, n))
            Dm = [[(1 / ra if i == 0 else F(1)) if i == j else F(0) for j in range(n)] for i in range(n)]
            ok = ok and _mm(Dm, _mm(Ha, Dm)) == H
        # k -> -k: a second isometry fixing V1
        Dm = [[(F(-1) if i == 0 else F(1)) if i == j else F(0) for j in range(n)] for i in range(n)]
        ok = ok and _mm(Dm, _mm(H, Dm)) == H and Dm != [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    _tp_rv = (ok); assert _tp_rv is not False, "check_limit_independent_of_choices"; return _tp_rv
