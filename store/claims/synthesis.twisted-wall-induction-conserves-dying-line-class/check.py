"""synthesis.twisted-wall-induction-conserves-dying-line-class: exact checks.

Matrices over Fractions. The ambient form in a local frame is
  h = [[G, b nu e, b mu e], [b nu e^T, 0, 1], [b mu e^T, 1, 0]]
on T*M + plane (frame n_o, n_inf, hyperbolic H(n_o, n_inf) = 1), e = components of the transversal u,
s = e^T G^{-1} e. Checks:
  (1) det h = -det G (1 - 2 mu nu b^2 s) at fixed rational data (several (mu, nu));
  (2) at a zero of F = 1 - 2 mu nu b^2 s the kernel of h is spanned by K = (-G^{-1}e, b mu s, b nu s),
      whose T*M part is nonzero; h has corank exactly one there;
  (3) twist equivariance: with D = diag(1_n, -1, -1), D h(e) D = h(-e) and K(-e) = -D K(e): flipping the
      transversal together with the plane frame (the twisted coupling's monodromy) preserves h and
      flips the T*M part of the kernel, so the shadow wall's radical line is a copy of Lambda;
  (4) the explicit Moebius wall on T^2 x R: cometric G = -d_phi d_phi + t K K + M M with
      K = c d_psi + s d_t, M = -s d_psi + c d_t, (c, s) = (cos phi/2, sin phi/2) at rational points of the
      circle (c, s) = ((1 - x^2)/(1 + x^2), 2x/(1 + x^2)); radical at t = 0 is span(k), k = c dpsi + s dt;
      det h = t - 2 mu nu (beta = 1); at t = 2 mu nu the radical of h projects onto span(k); and
      (c, s) -> (-c, -s) leaves G fixed while flipping k and u (the Moebius monodromy).
"""
from fractions import Fraction as F
import GA
from GA import mat_mul, mat_rank, frac_matrix
from tp_premise import premise


def det(M):
    M = [list(map(F, r)) for r in M]
    n = len(M)
    d = F(1)
    for i in range(n):
        p = next((r for r in range(i, n) if M[r][i] != 0), None)
        if p is None:
            return F(0)
        if p != i:
            M[i], M[p] = M[p], M[i]
            d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            M[r] = [M[r][j] - f * M[i][j] for j in range(n)]
    return d


def inv(M):
    n = len(M)
    A = [list(map(F, r)) + [F(1) if i == j else F(0) for j in range(n)] for i, r in enumerate(M)]
    for i in range(n):
        p = next(r for r in range(i, n) if A[r][i] != 0)
        A[i], A[p] = A[p], A[i]
        piv = A[i][i]
        A[i] = [x / piv for x in A[i]]
        for r in range(n):
            if r != i and A[r][i] != 0:
                f = A[r][i]
                A[r] = [A[r][j] - f * A[i][j] for j in range(2 * n)]
    return [r[n:] for r in A]


def ambient(G, e, mu, nu, b):
    n = len(G)
    h = [[F(G[i][j]) for j in range(n)] + [b * nu * e[i], b * mu * e[i]] for i in range(n)]
    h.append([b * nu * e[j] for j in range(n)] + [F(0), F(1)])
    h.append([b * mu * e[j] for j in range(n)] + [F(1), F(0)])
    return h


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def svalue(G, e):
    Gi = inv(G)
    return sum(e[i] * Gi[i][j] * e[j] for i in range(len(e)) for j in range(len(e)))


def kernel_vec(G, e, mu, nu, b):
    Gi = inv(G)
    s = svalue(G, e)
    a = matvec(Gi, e)
    return [-x for x in a] + [b * mu * s, b * nu * s]


G0 = [[F(-3), F(1), F(0), F(2)], [F(1), F(2), F(1), F(0)], [F(0), F(1), F(1), F(1)], [F(2), F(0), F(1), F(-1)]]
E0 = [F(1), F(-2), F(3), F(1)]


def check_determinant_identity():
    premise("sheaf.tame-wall-induction")
    premise("sheaf.determinant-identity-blow-up-expansion")
    s = svalue(G0, E0)
    assert s == F(50, 3) and det(G0) == 3
    for (mu, nu, b, want) in ((F(1), F(2), F(1), F(197)), (F(-3, 2), F(1, 3), F(1, 2), F(-31, 2)),
                              (F(5), F(-1), F(2, 3), F(-2027, 9))):
        h = ambient(G0, E0, mu, nu, b)
        assert det(h) == -det(G0) * (1 - 2 * mu * nu * b * b * s) == want
    return True


def check_kernel_at_shadow_wall():
    premise("sheaf.tame-wall-induction")
    premise("synthesis.wall-class-one-rung-obstruction")
    s = svalue(G0, E0)
    for (nu, b) in ((F(1), F(1)), (F(-2), F(1, 2))):
        mu = F(1) / (2 * nu * b * b * s)
        h = ambient(G0, E0, mu, nu, b)
        assert det(h) == 0
        assert mat_rank(h) == len(h) - 1
        K = kernel_vec(G0, E0, mu, nu, b)
        assert all(x == 0 for x in matvec(h, K))
        assert any(x != 0 for x in K[:4])
    return True


def check_twist_equivariance():
    premise("synthesis.wall-class-one-rung-obstruction")
    premise("sheaf.imported-real-line-bundles")
    s = svalue(G0, E0)
    nu, b = F(3), F(1)
    mu = F(1) / (2 * nu * b * b * s)
    D = [[F(1) if (i == j and i < 4) else (F(-1) if i == j else F(0)) for j in range(6)] for i in range(6)]
    hp = ambient(G0, E0, mu, nu, b)
    hm = ambient(G0, [-x for x in E0], mu, nu, b)
    assert mat_mul(mat_mul(D, hp), D) == hm
    Kp = kernel_vec(G0, E0, mu, nu, b)
    Km = kernel_vec(G0, [-x for x in E0], mu, nu, b)
    assert Km == [-x for x in matvec(D, Kp)]
    assert Km[:4] == [-x for x in Kp[:4]] and Km[4:] == Kp[4:]
    return True


def moebius(c, sn, t):
    """Cometric on T^2 x R in the coordinate coframe (dphi, dpsi, dt)."""
    Kv = [F(0), c, sn]
    Mv = [F(0), -sn, c]
    Pv = [F(1), F(0), F(0)]
    return [[-Pv[i] * Pv[j] + t * Kv[i] * Kv[j] + Mv[i] * Mv[j] for j in range(3)] for i in range(3)]


def check_moebius_wall():
    premise("sheaf.tameness")
    premise("sheaf.one-sided-completion")
    premise("sheaf.infinite-wall-sequence")
    premise("sheaf.imported-real-line-bundles")
    mu, nu = F(-1, 3), F(1)
    tw = 2 * mu * nu
    for x in (F(0), F(1, 2), F(2), F(-3), F(7, 5)):
        c = (1 - x * x) / (1 + x * x)
        sn = 2 * x / (1 + x * x)
        k = [F(0), c, sn]
        u = [F(0), c, sn]
        assert sum(k[i] * u[i] for i in range(3)) == 1
        G = moebius(c, sn, F(0))
        assert mat_rank(G) == 2 and all(v == 0 for v in matvec(G, k))
        assert moebius(-c, -sn, F(1, 2)) == moebius(c, sn, F(1, 2))
        for t in (F(1), F(1, 4), F(-1, 5), F(3)):
            assert det(ambient(moebius(c, sn, t), u, mu, nu, F(1))) == t - tw
        assert det(ambient(moebius(c, sn, F(0)), u, mu, nu, F(1))) == -tw
        h = ambient(moebius(c, sn, tw), u, mu, nu, F(1))
        assert det(h) == 0 and mat_rank(h) == 4
        K = kernel_vec(moebius(c, sn, tw), u, mu, nu, F(1))
        assert all(v == 0 for v in matvec(h, K))
        assert [K[i] * tw for i in range(3)] == [-v for v in k]
    return True
