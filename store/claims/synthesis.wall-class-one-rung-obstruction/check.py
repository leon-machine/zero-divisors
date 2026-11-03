"""synthesis.wall-class-one-rung-obstruction: exact checks.

All matrices are Gram matrices over Fractions. Inertia is computed exactly: the characteristic
polynomial by Faddeev-LeVerrier, then Descartes' sign count, exact for a real symmetric matrix
(all roots real), with the multiplicity of the root 0 split off first.

  (1) the rung-relaxed construction of clause (iii): det h = det G * 2 * (-2 sig - mu^2 beta^2 s)
      (Schur complement), on fixed (deterministically generated) rational data; and along a model transversal through the wall
      on which s = G^{-1}(e,e) changes sign inside the collar, with a good coupling (mu^2 S < 2),
      h is nondegenerate of signature (p+1, q+1) at every sampled point, equal to G + H on the
      physical exterior and to G + (positive definite) on the far exterior; with mu^2 S >= 2
      (mu = 1, 8) the same construction degenerates (negative control for the coupling bound);
  (2) at the wall the block (k, a, b) has determinant -2 mu^2 for every value of the interpolating
      function, and the total signature is (p+1, q+1);
  (3) the local mechanism of the necessity proof: inertia(G) = inertia(G|_Q) + sign(Schur complement),
      so the far-side negative bundle is N(G|_Q) plus the dying line;
  (4) the doubling of clause (ii): [[S, b 1], [b 1, -S]]^2 = (S^2 + b^2) (+) (S^2 + b^2), signature
      (n, n), for symmetric S including singular ones;
  (5) the isotropic-line step: a nondegenerate rank-3 form of signature (2,1) containing an isotropic
      line L has negative line projecting isomorphically onto P/L (never meets L), on instances.
"""
from fractions import Fraction as F
import GA  # noqa: F401  (house rule; the computation is matrix algebra over Fractions)
from tp_premise import premise


class Det:
    """Deterministic integer sequence (linear congruential, exact integers only) supplying fixed
    rational test points; replaces pseudo-random sampling so the check is reproducible and exact."""

    def __init__(self, seed):
        self.x = seed

    def _next(self):
        self.x = (self.x * 1103515245 + 12345) % 2147483648
        return self.x // 65536

    def randint(self, lo, hi):
        return lo + self._next() % (hi - lo + 1)

    def choice(self, seq):
        return seq[self._next() % len(seq)]

    def sample(self, seq, k):
        pool = list(seq)
        out = []
        for _ in range(k):
            out.append(pool.pop(self._next() % len(pool)))
        return out


def mat_mul(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def det(A):
    A = [row[:] for row in A]
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
            if f:
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return d


def inv(A):
    n = len(A)
    M = [row[:] + [F(int(i == j)) for j in range(n)] for i, row in enumerate(A)]
    for c in range(n):
        piv = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[piv] = M[piv], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [row[n:] for row in M]


def charpoly(A):
    """Faddeev-LeVerrier: coefficients c[0..n] of det(x - A) = sum c[k] x^(n-k), c[0] = 1."""
    n = len(A)
    c = [F(1)]
    Mk = [[F(0)] * n for _ in range(n)]
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(1, n + 1):
        Mk = [[x + c[-1] * y for x, y in zip(r1, r2)] for r1, r2 in zip(mat_mul(A, Mk), I)] if k > 1 else I
        AM = mat_mul(A, Mk)
        ck = -sum(AM[i][i] for i in range(n)) / k
        c.append(ck)
    return c


def inertia(A):
    c = charpoly(A)
    n = len(A)
    while c and c[-1] == 0:
        c = c[:-1]
    zero = n + 1 - len(c)

    def var(seq):
        s = [x for x in seq if x != 0]
        return sum(1 for a, b in zip(s, s[1:]) if (a > 0) != (b > 0))
    pos = var(c)
    deg = len(c) - 1
    neg = var([x * (-1) ** (deg - i) for i, x in enumerate(c)])
    assert pos + neg + zero == n
    return (pos, neg, zero)


def rnd(rng, lo=-5, hi=5):
    return F(rng.randint(lo, hi), rng.randint(1, 6))


def gram_h(G, e, mu, beta, sig):
    """h on T*M (+) R^2, basis of the plane (a, b) with a = n_O + n_inf, b = n_O - n_inf:
    H = diag(-2, 2) there; K_sig = diag(-2 sig, 2); coupling kappa(alpha, a) = mu beta alpha(u)."""
    n = len(G)
    h = [[F(0)] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            h[i][j] = G[i][j]
        h[i][n] = h[n][i] = mu * beta * e[i]
    h[n][n] = -2 * sig
    h[n + 1][n + 1] = F(2)
    return h


def check_rung_relaxed_construction():
    premise("sheaf.conservation-degeneracy-absolute-form")
    premise("sheaf.tameness")
    premise("sheaf.determinant-identity-blow-up-expansion")
    premise("sheaf.one-sided-completion")
    premise("sheaf.tame-wall-induction")
    rng = Det(20261022)
    # (1a) the Schur identity on fixed rational data, n = 3 and 4
    for n in (3, 4):
        for _ in range(40):
            G = [[F(0)] * n for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    G[i][j] = G[j][i] = rnd(rng)
            if det(G) == 0:
                continue
            e = [F(1)] + [rnd(rng) for _ in range(n - 1)]
            mu, beta, sig = rnd(rng) or F(1), rnd(rng), rnd(rng)
            Gi = inv(G)
            s = sum(e[i] * Gi[i][j] * e[j] for i in range(n) for j in range(n))
            assert det(gram_h(G, e, mu, beta, sig)) == det(G) * 2 * (-2 * sig - mu * mu * beta * beta * s)
    # (1b) a model transversal: physical signature (p, q) = (2, 1), coframe (k, m1, m2),
    # G(tau) = [[tau, tau/3, 0], [tau/3, 1, 1/5], [0, 1/5, -1]], u with e = (1, 1/2, 3). The O(1) part
    # of s = G^{-1}(e, e) is about -7.8, so s = 1/lambda + O(1) CHANGES SIGN inside the collar on the
    # physical side (near tau = 0.13): the good-coupling bound on mu is genuinely exercised.
    def G_of(t):
        return [[t, t / 3, F(0)], [t / 3, F(1), F(1, 5)], [F(0), F(1, 5), F(-1)]]
    e = [F(1), F(1, 2), F(3)]

    def beta_of(t):          # 1 on |t| <= 1/2, linear to 0 at |t| = 1
        a = abs(t)
        return F(1) if a <= F(1, 2) else (F(0) if a >= 1 else 2 * (1 - a))

    def s_of(t):
        Gi = inv(G_of(t))
        return sum(e[i] * Gi[i][j] * e[j] for i in range(3) for j in range(3))
    grid = [F(k, 128) for k in range(-160, 161) if k != 0]
    assert any(t > 0 and t < 1 and s_of(t) < 0 for t in grid), "s must change sign on the physical side"
    # Z: the thin neighbourhood inside {beta = 1} on which s has the sign of the side
    zw = max(z for z in [F(k, 128) for k in range(1, 65)]
             if all((s_of(t) > 0) == (t > 0) for t in grid if abs(t) < z))
    assert 0 < zw <= F(1, 2)
    S = max(abs(s_of(t)) for t in grid if zw <= abs(t) < 1)       # sup |s| on supp(beta) minus Z

    def run(mu):
        """Build h along the transversal; return the list of (t, inertia) failures."""
        thin = 2 / (mu * mu)
        inner = [abs(t) for t in grid if abs(t) < zw and abs(s_of(t)) <= thin]
        t0 = min(inner) if inner else zw
        # Z' = Sigma u ({|s| > 2/mu^2} cut with Z) contains every sample with |t| < t0
        assert all(abs(s_of(t)) > thin for t in grid if abs(t) < t0)

        def sig_of(t):
            if abs(t) >= t0:
                return F(1) if t > 0 else F(-1)
            return t / t0                  # interpolation only inside Z'
        bad = []
        for t in grid + [F(0)]:
            h = gram_h(G_of(t), e, mu, beta_of(t), sig_of(t))
            if det(h) == 0 or inertia(h) != (3, 2, 0):
                bad.append(t)
            if t >= 1:
                assert beta_of(t) == 0 and sig_of(t) == 1 and inertia(G_of(t)) == (2, 1, 0)
            if t <= -1:
                assert beta_of(t) == 0 and sig_of(t) == -1 and inertia(G_of(t)) == (1, 2, 0)
        return bad, t0
    mu = F(1)
    while mu * mu * S >= 2:
        mu /= 2
    bad, t0 = run(mu)
    assert not bad, bad                                    # a good coupling: nondegenerate, (p+1, q+1)
    assert t0 < zw                                         # the interpolation zone is exercised
    for big in (F(1), F(8)):                               # mu^2 S >= 2: the construction breaks
        assert big * big * S >= 2
        bad_big, _ = run(big)
        assert bad_big, big
    # (2) at the wall: block (k, a, b) and full signature for several interpolation values
    for sg in (F(-1), F(-1, 3), F(0), F(1, 2), F(1)):
        h = gram_h(G_of(F(0)), e, mu, F(1), sg)
        blk = [[h[0][0], h[0][3], h[0][4]], [h[3][0], h[3][3], h[3][4]], [h[4][0], h[4][3], h[4][4]]]
        assert det(blk) == -2 * mu * mu
        assert inertia(h) == (3, 2, 0)
    return True


def check_far_side_negative_bundle_contains_dying_line():
    premise("sheaf.degeneration-sheaf")
    premise("sheaf.metrics-residue-square-root-twist")
    rng = Det(7)
    for _ in range(60):
        n = rng.choice((3, 4, 5))
        G1 = [[F(0)] * (n - 1) for _ in range(n - 1)]
        for i in range(n - 1):
            for j in range(i, n - 1):
                G1[i][j] = G1[j][i] = rnd(rng)
        if det(G1) == 0:
            continue
        b = [rnd(rng) for _ in range(n - 1)]
        lam = rnd(rng)
        G = [[lam] + b] + [[b[i]] + G1[i] for i in range(n - 1)]
        G1i = inv(G1)
        schur = lam - sum(b[i] * G1i[i][j] * b[j] for i in range(n - 1) for j in range(n - 1))
        p1, q1, z1 = inertia(G1)
        expect = (p1 + (schur > 0), q1 + (schur < 0), int(schur == 0))
        assert inertia(G) == expect
    return True


def check_doubling_is_never_obstructed():
    premise("sheaf.conservation-degeneracy-absolute-form")
    # worked example: S = [[1, 2], [2, 4]] is singular (a wall point), beta = 1.
    S0 = [[F(1), F(2)], [F(2), F(4)]]
    assert det(S0) == 0
    D0 = [[F(1), F(2), F(1), F(0)], [F(2), F(4), F(0), F(1)],
          [F(1), F(0), F(-1), F(-2)], [F(0), F(1), F(-2), F(-4)]]
    assert charpoly(D0) == [F(1), F(0), F(-27), F(0), F(26)]   # x^4 - (tr S^2 + 2) x^2 + det(S^2 + 1)
    assert det(D0) == 26 and inertia(D0) == (2, 2, 0)
    assert mat_mul(D0, D0)[0][:2] == [F(6), F(10)] and mat_mul(D0, D0)[1][:2] == [F(10), F(21)]
    rng = Det(11)
    for _ in range(40):
        n = rng.choice((2, 3, 4))
        S = [[F(0)] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                S[i][j] = S[j][i] = rnd(rng)
        if rng.randint(0, 1) == 0:                       # force a corank-one S (a wall point)
            S[n - 1] = [x + y for x, y in zip(S[0], S[1])] if n > 2 else [S[0][0], S[0][1]]
            for i in range(n):
                S[i][n - 1] = S[n - 1][i]
            if n == 2:
                S = [[F(1), F(2)], [F(2), F(4)]]
        for bt in (F(1), F(1, 3), F(-2)):
            D = [[F(0)] * (2 * n) for _ in range(2 * n)]
            for i in range(n):
                for j in range(n):
                    D[i][j] = S[i][j]
                    D[n + i][n + j] = -S[i][j]
                D[i][n + i] = D[n + i][i] = bt
            D2 = mat_mul(D, D)
            S2 = mat_mul(S, S)
            for i in range(n):
                for j in range(n):
                    tgt = S2[i][j] + (bt * bt if i == j else 0)
                    assert D2[i][j] == tgt and D2[n + i][n + j] == tgt
                    assert D2[i][n + j] == 0 and D2[n + i][j] == 0
            assert det(D) != 0 and inertia(D) == (n, n, 0)
    return True


def check_isotropic_line_in_rank_three():
    premise("sheaf.wall-gram")
    premise("sheaf.imported-real-line-bundles")
    premise("sheaf.infinite-wall-sequence")
    # W = span(k, n_O, n_inf) at the wall with the Gram of sheaf.wall-gram, mu nu > 0: signature (2,1),
    # k isotropic. The negative line never meets L = R k, so it maps isomorphically onto W / L^perp-type
    # quotient; here: for the negative eigenline v, h(v, k) != 0 (v pairs with L), the pairing that
    # identifies the negative line with L^*.
    for mu, nu in ((F(1), F(1)), (F(1, 2), F(3)), (F(-2), F(-1, 5))):
        W = [[F(0), nu, mu], [nu, F(0), F(-1)], [mu, F(-1), F(0)]]
        assert det(W) == -2 * mu * nu and inertia(W) == (2, 1, 0)
        # every vector x with h(x, k) = 0 has h(x, x) >= 0: L^perp = span(k, w), w^2 = 2 mu nu > 0
        w = [F(1), -mu, nu]          # w = k + nu n_inf - mu n_O in the order (k, n_O, n_inf)
        hw = sum(w[i] * W[i][j] * w[j] for i in range(3) for j in range(3))
        assert hw == 2 * mu * nu and hw > 0
        assert sum(w[i] * W[i][0] for i in range(3)) == 0
        # so a negative vector is never in L^perp: it pairs nondegenerately with L
    return True
