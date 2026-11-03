"""sheaf.one-sided-completion: exact checks.

Collar models for every (p, q) with p >= 1, p + q <= 5: on the covector frame (k, m_1, ..., m_(n-1)) the
cometric G(tau) has lambda = G(k, k) = tau + tau^2, cross terms b(tau) = O(tau) nonzero and a
tau-dependent non-orthogonal block G1(tau) of signature (p - 1, q) at tau = 0, so G has signature (p, q) on
the physical side tau > 0 near the wall (checked). e = evaluation at the transversal u (k(u) = 1, nonzero
tangential parts). h = G + H + beta kappa with kappa(alpha, n0) = nu alpha(u), kappa(alpha, ninf) = mu alpha(u).
(1) With mu nu > 0 ((2, 3) and (1/2, 1)): at the wall (tau = 0, beta = 1) h has signature (p + 1, q + 1); at the
    physical collar samples tau = 1/5, 1/20, 1/100 and every bump value beta in {0, 1/4, 1/2, 1},
    s = G^-1(e, e) > 0, F = 1 + 2 mu nu beta^2 s >= 1, det h = det G (-F) exactly, and the signature of h is
    (p + 1, q + 1); with beta = 0 (outside the collar) h = G + H.
(2) Control: with mu nu < 0 the completion is not one-sided-good: at tau = 1/100 (beta = 1) the signature of h
    is (p, q + 2), not (p + 1, q + 1).
(3) The fibres: Cl(T, h) at the wall and at a collar point has 2^(n+2) independent blades in the exterior
    model (rank 2^(n+2), the locally free rank), and the physical fibre Cl(2, 4) is Mat_4(H): its centre is R
    (only the scalar blade commutes with every generator), f = (1 + e0e2)(1 + e1e3)/4 is an idempotent with
    dim A f = 16 and dim f A f = 4, and f A f = span(f, e4 f, e5 f, e4 e5 f) with (e4 f)^2 = (e5 f)^2 = -f
    anticommuting: the quaternions, so A = End_H(A f) = Mat_4(H).
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

SIGS = [(p, n - p) for n in range(1, 6) for p in range(1, n + 1)]
TAUS = [F(1, 5), F(1, 20), F(1, 100)]
BETAS = [F(0), F(1, 4), F(1, 2), F(1)]
GOOD = [(F(2), F(3)), (F(1, 2), F(1))]
# control couplings with mu nu < 0
BAD = [(F(-2), F(3)), (F(1, 2), F(-1))]
# bump value at the wall and at the control point
BETA_FULL = F(1)
# collar point for the mu nu < 0 control
TAU_CONTROL = TAUS[-1]
# signatures (p, q) whose fibres are tested for local freeness, and the points: the wall and a collar point
FIBRE_SIGS = [(1, 1), (2, 1), (1, 3)]
FIBRE_TAUS = (F(0), TAUS[0])
FIBRE_COUPLING = GOOD[0]


def blade_el(b):
    """The basis blade e_b as a multivector."""
    return {b: F(1)}


def _det(M):
    A = [list(r) for r in M]
    n = len(A)
    d = F(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if A[r][c] != 0), None)
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            f = A[r][c] / A[c][c]
            A[r] = [a - f * b for a, b in zip(A[r], A[c])]
    return d


def collar_gram(p, q, tau):
    """Cometric G(tau) on the frame (k, m_1..m_(n-1)): lambda = tau + tau^2, b = O(tau) nonzero,
    G1(tau) nondegenerate of signature (p - 1, q) at tau = 0, non-orthogonal and tau-dependent."""
    n = p + q
    tau = F(tau)
    G = [[F(0)] * n for _ in range(n)]
    G[0][0] = tau + tau * tau
    for i in range(1, n):
        G[0][i] = G[i][0] = tau * (i % 2 + 1) - tau * tau * i
        for j in range(1, n):
            base = (F(1) if i < p else F(-1)) if i == j else (F(1, 3) if abs(i - j) == 1 else F(0))
            G[i][j] = base + tau * F((i * j) % 3, 2)
    return G


def evaluation(n):
    """e = evaluation at the transversal u, in the covector frame: k(u) = 1, tangential parts nonzero."""
    return [F(1)] + [F(1, i + 1) for i in range(1, n)]


def ambient(G, e, beta, mu, nu):
    n = len(G)
    h = [[F(0)] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            h[i][j] = G[i][j]
        h[i][n] = h[n][i] = nu * beta * e[i]
        h[i][n + 1] = h[n + 1][i] = mu * beta * e[i]
    h[n][n + 1] = h[n + 1][n] = F(-1)
    return h


def s_of(G, e):
    x = GA.field_solve(G, e)
    return sum((a * b for a, b in zip(e, x)), F(0))


def check_signature_constant_on_physical_side():
    premise("sheaf.wall-gram")
    premise("sheaf.determinant-identity-blow-up-expansion")
    premise("sheaf.tameness")
    ok = True
    points = 0
    for (p, q) in SIGS:
        n = p + q
        e = evaluation(n)
        for mu, nu in GOOD:
            ok = ok and GA.congruence_signature(ambient(collar_gram(p, q, 0), e, F(1), mu, nu)) == (p + 1, q + 1, 0)
            for tau in TAUS:
                G = collar_gram(p, q, tau)
                ok = ok and GA.congruence_signature(G) == (p, q, 0)
                s = s_of(G, e)
                ok = ok and s > 0
                for beta in BETAS:
                    h = ambient(G, e, beta, mu, nu)
                    Fv = 1 + 2 * mu * nu * beta * beta * s
                    ok = ok and Fv >= 1 and _det(h) == _det(G) * (-Fv) and _det(h) != 0
                    ok = ok and GA.congruence_signature(h) == (p + 1, q + 1, 0)
                    points += 1
    _tp_rv = (ok and points == 15 * 2 * 3 * 4); assert _tp_rv is not False, "check_signature_constant_on_physical_side"; return _tp_rv


def check_wrong_coupling_sign_fails():
    premise("sheaf.wall-gram")
    ok = True
    for (p, q) in SIGS:
        n = p + q
        e = evaluation(n)
        for mu, nu in BAD:
            h = ambient(collar_gram(p, q, TAU_CONTROL), e, BETA_FULL, mu, nu)
            ok = ok and GA.congruence_signature(h) == (p, q + 2, 0)
            ok = ok and GA.congruence_signature(ambient(collar_gram(p, q, 0), e, BETA_FULL, mu, nu)) == (p, q + 2, 0)
    _tp_rv = (ok); assert _tp_rv is not False, "check_wrong_coupling_sign_fails"; return _tp_rv


def check_fibres_locally_free_and_physical_type():
    premise("sheaf.local-freeness-constant-rank")
    ok = True
    for (p, q) in FIBRE_SIGS:
        n = p + q
        e = evaluation(n)
        for tau in FIBRE_TAUS:
            h = ambient(collar_gram(p, q, tau), e, BETA_FULL, *FIBRE_COUPLING)
            N = n + 2
            blades = GA.all_blades(N)
            rows = []
            for I in blades:
                st = GA.ext_sigma_blade(I, h, N)
                rows.append([st.get(frozenset(J), F(0)) for J in blades])
            ok = ok and GA.rank_of_vectors(rows) == 2 ** N
    sq = GA.sig(2, 4)
    one = {(): F(1)}

    def bl(*idx):
        x = dict(one)
        for i in idx:
            x = GA.mul(x, GA.gen(i), sq)
        return x
    blades = GA.all_blades(len(sq))
    centre = [b for b in blades if all(GA.commutes(blade_el(b), GA.gen(i), sq) for i in range(len(sq)))]
    ok = ok and centre == [()]
    f = GA.scal(F(1, 4), GA.mul(GA.add(one, bl(0, 2)), GA.add(one, bl(1, 3)), sq))
    ok = ok and GA.eq(GA.mul(f, f, sq), f)

    def dim(xs):
        bs = sorted({b for x in xs for b in x})
        return GA.rank_of_vectors([[x.get(b, F(0)) for b in bs] for x in xs])
    ok = ok and dim([GA.mul(blade_el(b), f, sq) for b in blades]) == 16
    corner = [GA.mul(GA.mul(f, blade_el(b), sq), f, sq) for b in blades]
    ok = ok and dim(corner) == 4
    i_, j_ = GA.mul(bl(4), f, sq), GA.mul(bl(5), f, sq)
    ok = ok and dim(corner + [i_, j_, GA.mul(i_, j_, sq)]) == 4 == dim([f, i_, j_, GA.mul(i_, j_, sq)])
    ok = ok and GA.eq(GA.mul(i_, i_, sq), GA.neg(f)) and GA.eq(GA.mul(j_, j_, sq), GA.neg(f))
    ok = ok and GA.eq(GA.mul(i_, j_, sq), GA.neg(GA.mul(j_, i_, sq)))
    _tp_rv = (ok); assert _tp_rv is not False, "check_fibres_locally_free_and_physical_type"; return _tp_rv
