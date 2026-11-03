"""synthesis.tameness-splits-regularity-and-order: exact checks.

Polynomials in the transversal parameter tau are coefficient lists over Fractions; matrices
of polynomials have determinants by permutation expansion. Inertia of a rational symmetric
matrix is exact: characteristic polynomial by Faddeev-LeVerrier, then Descartes' sign count
(exact because every root is real), the multiplicity of 0 split off first.

  (1) Jacobi at corank one: for G(tau) = G0 + tau G1 + tau^2 G2 with radical k = e_0 of G0, the
      tau-coefficient of det G is det(G0 restricted to k-complement) * G1(k,k); so det G has a
      simple zero exactly when (T3) holds, and a zero of order >= 2 when G1(k,k) = 0;
      at corank two the tau-coefficient vanishes for every G1.
  (2) A wild wall in the physical case: Schur complement S = tau^3, G1 negative definite, so
      (T3) fails (the tau-coefficient of g_k = G(k,k) is 0) and det G has a triple zero; the
      exact identity s = (1-c)^2/S + e'^T G1^{-1} e' holds at rational points; the completed
      form h (coupling mu, nu with mu nu > 0, beta = 1) has signature (2,4) at the wall and at
      every sampled physical point; det h is a polynomial in tau whose zeros are all simple
      (gcd(P, P') = 1) with a far-side zero between -1/4 and -1/5, signature (2,4)
      between wall and shadow wall and (1,5) beyond: the shadow wall is a
      simple zero, hence first order.
  (3) Even order: S = tau^2 gives the same signature on both sides (no signature change).
"""
from fractions import Fraction as F
from itertools import permutations
import GA  # noqa: F401  (house rule; the computation is matrix algebra over Fractions)
from tp_premise import premise


# ---------- polynomials ----------
def ptrim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def padd(p, q):
    n = max(len(p), len(q))
    return ptrim([(p[i] if i < len(p) else F(0)) + (q[i] if i < len(q) else F(0)) for i in range(n)])


def pmul(p, q):
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a:
            for j, b in enumerate(q):
                r[i + j] += a * b
    return ptrim(r)


def pscale(c, p):
    return ptrim([c * a for a in p])


def peval(p, x):
    v = F(0)
    for a in reversed(p):
        v = v * x + a
    return v


def pderiv(p):
    return ptrim([i * p[i] for i in range(1, len(p))] or [F(0)])


def pval(p):
    """order of vanishing at 0"""
    for i, a in enumerate(p):
        if a != 0:
            return i
    return None


def pdivmod(p, q):
    p = ptrim(p)
    q = ptrim(q)
    out = [F(0)] * max(1, len(p) - len(q) + 1)
    r = list(p)
    while len(r) >= len(q) and any(r):
        c = r[-1] / q[-1]
        k = len(r) - len(q)
        out[k] = c
        for i, b in enumerate(q):
            r[i + k] -= c * b
        r = ptrim(r)
        if len(r) < len(q) or (len(r) == 1 and r[0] == 0):
            break
    return ptrim(out), ptrim(r)


def pgcd(p, q):
    p, q = ptrim(p), ptrim(q)
    while not (len(q) == 1 and q[0] == 0):
        _, r = pdivmod(p, q)
        p, q = q, r
    return p


def pdet(M):
    n = len(M)
    total = [F(0)]
    for perm in permutations(range(n)):
        sgn = 1
        seen = [False] * n
        for i in range(n):
            if not seen[i]:
                j, L = i, 0
                while not seen[j]:
                    seen[j] = True
                    j = perm[j]
                    L += 1
                if L % 2 == 0:
                    sgn = -sgn
        term = [F(sgn)]
        for i in range(n):
            term = pmul(term, M[i][perm[i]])
            if term == [F(0)]:
                break
        total = padd(total, term)
    return total


# ---------- rational matrices ----------
def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


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
    n = len(A)
    c = [F(1)]
    I = [[F(int(i == j)) for j in range(n)] for i in range(n)]
    Mk = I
    for k in range(1, n + 1):
        if k > 1:
            Mk = [[x + c[-1] * y for x, y in zip(r1, r2)] for r1, r2 in zip(mat_mul(A, Mk), I)]
        AM = mat_mul(A, Mk)
        c.append(-sum(AM[i][i] for i in range(n)) / k)
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
    return (pos, neg, zero)


def at(PM, x):
    return [[peval(p, x) for p in row] for row in PM]


# ---------- model builders ----------
def quad_family(G0, G1, G2):
    n = len(G0)
    return [[ptrim([G0[i][j], G1[i][j], G2[i][j]]) for j in range(n)] for i in range(n)]


def wild_wall(m, G1, b1):
    """Gram [[lam, b^T],[b, G1]] with b = tau b1, lam = tau^m + tau^2 b1^T G1^{-1} b1, so S = tau^m."""
    n = len(G1) + 1
    Gi = inv(G1)
    q = sum(b1[i] * Gi[i][j] * b1[j] for i in range(n - 1) for j in range(n - 1))
    lam = [F(0)] * (max(m, 2) + 1)
    lam[m] += 1
    lam[2] += q
    M = [[[F(0)] for _ in range(n)] for _ in range(n)]
    M[0][0] = ptrim(lam)
    for i in range(1, n):
        M[0][i] = M[i][0] = ptrim([F(0), b1[i - 1]])
        for j in range(1, n):
            M[i][j] = [G1[i - 1][j - 1]]
    return M


def completed(PM, e, mu, nu):
    """h = G (+) H + kappa with beta = 1: kappa(alpha, n_O) = nu alpha(u), kappa(alpha, n_inf) = mu alpha(u)."""
    n = len(PM)
    Z = [F(0)]
    h = [[Z for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            h[i][j] = PM[i][j]
        h[i][n] = h[n][i] = [nu * e[i]]
        h[i][n + 1] = h[n + 1][i] = [mu * e[i]]
    h[n][n + 1] = h[n + 1][n] = [F(-1)]
    return h


G1_PHYS = [[F(-2), F(1), F(0)], [F(1), F(-3), F(1, 2)], [F(0), F(1, 2), F(-1)]]
B1 = [F(1), F(-2), F(3, 2)]
E = [F(1), F(1, 3), F(-1, 2), F(2)]


# ---------- checks ----------
def check_jacobi_corank_one_simple_zero():
    premise("sheaf.invariant-form-t3")
    premise("sheaf.determinant-identity-blow-up-expansion")
    low = [[F(-2), F(1), F(0)], [F(1), F(-3), F(1, 2)], [F(0), F(1, 2), F(-1)]]
    G0 = [[F(0)] * 4] + [[F(0)] + row for row in low]
    G2 = [[F(i + j - 3, 2) for j in range(4)] for i in range(4)]
    dlow = det(low)
    assert dlow == F(-9, 2)
    for g00 in (F(3), F(-5, 2), F(0)):
        G1 = [[F(1, 1 + i + j) for j in range(4)] for i in range(4)]
        G1[0][0] = g00
        P = pdet(quad_family(G0, G1, G2))
        assert P[0] == 0
        assert P[1] == dlow * g00
        assert (pval(P) == 1) == (g00 != 0)
    # corank two: radical span(e0, e1); the linear coefficient vanishes for every G1
    low2 = [[F(-1), F(1, 3)], [F(1, 3), F(2)]]
    G0b = [[F(0)] * 4, [F(0)] * 4] + [[F(0), F(0)] + row for row in low2]
    for s in (1, 2, 3):
        G1 = [[F(s * (i + 1) * (j + 2) - 5, 7) for j in range(4)] for i in range(4)]
        G1 = [[(G1[i][j] + G1[j][i]) / 2 for j in range(4)] for i in range(4)]
        P = pdet(quad_family(G0b, G1, G2))
        assert P[0] == 0 and P[1] == 0
        assert pval(P) == 2
        # second order: det of the complementary block times det of G1 on the radical
        assert P[2] == det(low2) * (G1[0][0] * G1[1][1] - G1[0][1] * G1[1][0])
    assert det(low2) == F(-19, 9)


def check_wild_wall_completion_and_shadow():
    premise("sheaf.determinant-identity-blow-up-expansion")
    premise("sheaf.invariant-form-t3")
    mu, nu = F(1, 10), F(1, 2)
    PM = wild_wall(3, G1_PHYS, B1)
    # (T3) fails: g_k = lam has zero tau-coefficient; det G has a triple zero
    assert pval(PM[0][0]) == 2
    dG = pdet(PM)
    assert pval(dG) == 3 and dG[3] == det(G1_PHYS)
    # the exact identity for s = G^{-1}(e,e)
    Gi1 = inv(G1_PHYS)
    for tau in (F(1, 7), F(-1, 5), F(1, 40), F(-1, 33)):
        Gt = at(PM, tau)
        s = sum(E[i] * inv(Gt)[i][j] * E[j] for i in range(4) for j in range(4))
        b = [tau * x for x in B1]
        c = sum(b[i] * Gi1[i][j] * E[j + 1] for i in range(3) for j in range(3))
        B = sum(E[i + 1] * Gi1[i][j] * E[j + 1] for i in range(3) for j in range(3))
        assert s == (1 - c) ** 2 / tau ** 3 + B
    # completed form: wall and physical side signature (2,4)
    H = completed(PM, E, mu, nu)
    assert inertia(at(PM, F(1, 10))) == (1, 3, 0) and inertia(at(PM, F(-1, 10))) == (0, 4, 0)
    assert inertia(at(H, F(0))) == (2, 4, 0)
    for k in range(1, 41):
        assert inertia(at(H, F(k, 400))) == (2, 4, 0)
    # det h is a polynomial; every zero is simple; one lies on the far side between -1/4 and -1/5
    P = pdet(H)
    assert P[0] != 0 and len(P) == 4
    g = pgcd(P, pderiv(P))
    assert len(g) == 1
    assert peval(P, F(-1, 4)) * peval(P, F(-1, 5)) < 0
    # between the wall and the shadow wall the signature stays (2,4); beyond it, (1,5)
    assert inertia(at(H, F(-1, 100))) == (2, 4, 0) and inertia(at(H, F(-1, 2))) == (1, 5, 0)
    # identity det h = det G * (-(1 + 2 mu nu s)) at a far-side point
    tau = F(-1, 9)
    Gt = at(PM, tau)
    s = sum(E[i] * inv(Gt)[i][j] * E[j] for i in range(4) for j in range(4))
    assert peval(P, tau) == det(Gt) * (-(1 + 2 * mu * nu * s))


def check_even_order_keeps_signature():
    premise("sheaf.invariant-form-t3")
    premise("sheaf.determinant-identity-blow-up-expansion")
    PM2 = wild_wall(2, G1_PHYS, [F(0), F(0), F(0)])
    assert inertia(at(PM2, F(1, 10))) == inertia(at(PM2, F(-1, 10))) == (1, 3, 0)
    PM3 = wild_wall(3, G1_PHYS, [F(0), F(0), F(0)])
    assert inertia(at(PM3, F(1, 10))) == (1, 3, 0) and inertia(at(PM3, F(-1, 10))) == (0, 4, 0)
