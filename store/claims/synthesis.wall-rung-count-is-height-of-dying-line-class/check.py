"""synthesis.wall-rung-count-is-height-of-dying-line-class: exact checks.

Matrices over Fractions, Clifford products with GA. Checks:
  (1) wall block: a nondegenerate form W of rank 2k+1, signature (k+1, k), with an isotropic vector l has
      inertia In(W) = (1, 1) + In(l^perp / l): the negative space is one line paired with l plus the
      negative space of l^perp/l (rank k - 1), for k = 1, 2, 3 on rational instances;
  (2) Whitney algebra: in Z2[x]/(x^(n+1)), w(N) = (1 + x)^(-1) = sum x^j; a bundle N of rank r with this
      total class exists only if x^j = 0 for j > r, so on RP^n (x^n != 0) the rank is at least n and the
      rung count at least n + 1; on the torus (exterior algebra, x^2 = 0) w(N) = 1 + x, rank one;
  (3) the two-rung completion of the stored Moebius torus wall with the twist confined to the collar:
      the dying line l = c a1 + s a2 and its complement n = -s a1 + c a2 inside the trivial null plane
      V = span(a1, a2) of H + H; the form h on T*M + R^4 is single valued under (c, s) -> (-c, -s),
      restricts to G on T*M, equals G + H + H where beta = 0, has det h = 2 mu nu beta^2 - t, signature
      (4, 3) on the physical side and on the wall, and at the shadow wall t = 2 mu nu beta^2 its radical
      has cotangent part along theta = c dpsi + s dt and rung part along (c, s) in V: the new dying line is
      again a copy of L; l ^ n = a1 ^ a2 (GA), so L + N is the trivial V with a global oriented frame;
  (4) clause (c): in Cl(1,1) built on l (x) e0, l (x) e1 the primitive idempotent f = (1 + l0 l1)/2 is fixed
      by the joint sign flip l -> -l, so Cl(L (x) R^{1,1}) has a global spinor module and is Morita trivial;
      with the torus frame, Cl(L (+) N, negative) has the global pseudoscalar a1 a2 squaring to -1.
"""
from fractions import Fraction as F
import GA
from GA import congruence_signature, mat_rank, mat_mul, mul, add, sc, gen, scal, eq
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


def transpose(A):
    return [list(r) for r in zip(*A)]


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


def bil(M, u, v):
    return sum(u[i] * M[i][j] * v[j] for i in range(len(u)) for j in range(len(v)))


def kernel(M):
    """Exact basis of the right kernel of a rational matrix."""
    A = [list(map(F, r)) for r in M]
    rows, cols = len(A), len(A[0])
    piv = []
    r = 0
    for c in range(cols):
        p = next((i for i in range(r, rows) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    free = [c for c in range(cols) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * cols
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        out.append(v)
    return out


def block(P, R):
    n, m = len(P), len(R)
    out = [[F(0)] * (n + m) for _ in range(n + m)]
    for i in range(n):
        for j in range(n):
            out[i][j] = F(P[i][j])
    for i in range(m):
        for j in range(m):
            out[n + i][n + j] = F(R[i][j])
    return out


S_MIX = [[1, 2, 0, -1, 1, 0, 3], [0, 1, 1, 0, -2, 1, 0], [1, 0, 1, 1, 0, 0, -1], [2, -1, 0, 1, 1, 1, 0],
         [0, 0, 1, -1, 1, 2, 1], [1, 1, 0, 0, 0, 1, 2], [0, 3, -1, 1, 0, 0, 1]]


def check_wall_block_negative_bundle():
    premise("synthesis.wall-class-one-rung-obstruction")
    premise("sheaf.wall-gram")
    premise("sheaf.degeneration-sheaf")
    want = {1: (2, 3), 2: (-24, -16), 3: (147, 60)}
    cases = {1: [[2]], 2: [[1, 1, 0], [1, -3, 2], [0, 2, 5]],
             3: [[3, 1, 0, 0, 1], [1, -2, 1, 0, 0], [0, 1, 4, -1, 0], [0, 0, -1, -1, 2], [1, 0, 0, 2, 1]]}
    for k, R0 in cases.items():
        n = 2 * k + 1
        P = [[0, 1], [1, 3]]                      # isotropic first vector, signature (1, 1)
        W0 = block(P, R0)
        S = [[F(S_MIX[i][j]) for j in range(n)] for i in range(n)]
        assert (det(R0), det(S)) == want[k]
        assert det(W0) == -det(R0)
        W = mat_mul(mat_mul(transpose(S), W0), S)  # W = S^T W0 S
        # l with S l = e_0, solved exactly
        e0 = [F(1)] + [F(0)] * (n - 1)
        aug = [S[i] + [e0[i]] for i in range(n)]
        sol = kernel(aug)
        v = [x for x in sol if x[n] != 0][0]
        l = [-x / v[n] for x in v[:n]]
        assert matvec(S, l) == e0 and bil(W, l, l) == 0
        perp = kernel([matvec(transpose(W), l)])  # l^perp, rank 2k, contains l
        assert len(perp) == 2 * k
        Gperp = [[bil(W, a, b) for b in perp] for a in perp]
        pw, nw, zw = congruence_signature(W)
        pr, nr, zr = congruence_signature(Gperp)
        assert (pw, nw, zw) == (k + 1, k, 0)
        assert zr == 1 and (pr, nr) == (k, k - 1)
        assert (pw, nw) == (1 + pr, 1 + nr)
        assert det(W) == det(S) ** 2 * det(W0)
        e1 = [F(0), F(1)] + [F(0)] * (n - 2)
        v1 = [x for x in kernel([S[i] + [e1[i]] for i in range(n)]) if x[n] != 0][0]
        m = [-x / v1[n] for x in v1[:n]]
        assert bil(W, l, m) == 1 and bil(W, m, m) == 3   # l pairs with a partner line: P is (1, 1)
        assert congruence_signature(R0)[:2] == (k, k - 1)
    return True


def z2_mul(a, b, n):
    out = [0] * (n + 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if i + j <= n and x and y:
                out[i + j] ^= 1
    return out


def check_whitney_inverse_forces_height():
    premise("sheaf.imported-real-line-bundles")
    premise("synthesis.wall-class-one-rung-obstruction")
    for n in range(1, 8):
        one_plus_x = [1, 1] + [0] * (n - 1)
        inv = [1] * (n + 1)
        assert z2_mul(one_plus_x, inv, n) == [1] + [0] * n
        # a rank-r bundle has w_j = 0 for j > r; w_j(N) = x^j != 0 for j <= n on RP^n
        ranks = [r for r in range(0, n + 2) if all(inv[j] == 0 for j in range(r + 1, n + 1))]
        assert min(ranks) == n
        assert min(ranks) + 1 == n + 1                # rung count at least n + 1 on RP^n
    # torus T^2: H*(T^2; Z2) exterior on (x, y); x = w1(L) pulled back from the phi circle, x^2 = 0
    def ext_mul(a, b):
        out = {}
        for ka, va in a.items():
            for kb, vb in b.items():
                if set(ka) & set(kb):
                    continue
                key = tuple(sorted(ka + kb))
                out[key] = out.get(key, 0) ^ (va & vb)
        return {k: v for k, v in out.items() if v}
    one = {(): 1}
    x = {(0,): 1}
    assert ext_mul(x, x) == {}
    w_inv = {(): 1, (0,): 1}                          # (1 + x)^(-1) = 1 + x since x^2 = 0
    assert ext_mul({(): 1, (0,): 1}, w_inv) == one
    return True


def moebius(c, sn, t):
    Kv = [F(0), c, sn]
    Mv = [F(0), -sn, c]
    Pv = [F(1), F(0), F(0)]
    return [[-Pv[i] * Pv[j] + t * Kv[i] * Kv[j] + Mv[i] * Mv[j] for j in range(3)] for i in range(3)]


def two_rung(c, sn, t, mu, nu, b):
    """Form on T*M + R^4 in the global frame (dphi, dpsi, dt; a1, a2, b1, b2), H(a_i, b_j) = delta_ij."""
    G = moebius(c, sn, t)
    u = [F(0), c, sn]
    h = [[F(0)] * 7 for _ in range(7)]
    for i in range(3):
        for j in range(3):
            h[i][j] = G[i][j]
    for a in range(2):
        h[3 + a][5 + a] = h[5 + a][3 + a] = F(1)
    lcoef = [c, sn]
    for i in range(3):
        for a in range(2):
            h[i][3 + a] = h[3 + a][i] = b * mu * lcoef[a] * u[i]
            h[i][5 + a] = h[5 + a][i] = b * nu * lcoef[a] * u[i]
    return h


def check_torus_two_rung_completion():
    premise("sheaf.tameness")
    premise("sheaf.one-sided-completion")
    premise("sheaf.tame-wall-induction")
    premise("synthesis.twisted-wall-induction-conserves-dying-line-class")
    mu, nu = F(-1, 3), F(1)
    for x in (F(0), F(1, 2), F(2), F(-3), F(7, 5)):
        c = (1 - x * x) / (1 + x * x)
        sn = 2 * x / (1 + x * x)
        assert c * c + sn * sn == 1
        for b in (F(1), F(1, 2), F(0)):
            for t in (F(0), F(1, 4), F(1), F(3), F(-1, 5)):
                h = two_rung(c, sn, t, mu, nu, b)
                assert h == two_rung(-c, -sn, t, mu, nu, b)          # single valued on the torus
                assert [r[:3] for r in h[:3]] == moebius(c, sn, t)    # restricts to G on T*M
                assert det(h) == 2 * mu * nu * b * b - t
                if b == 0:
                    assert all(h[i][j] == 0 for i in range(3) for j in range(3, 7))
                if t >= 0 and b != 0:
                    assert congruence_signature(h) == (4, 3, 0)
            if b != 0:
                tw = 2 * mu * nu * b * b
                h = two_rung(c, sn, tw, mu, nu, b)
                assert mat_rank(h) == 6
                K = kernel(h)
                assert len(K) == 1
                v = K[0]
                theta = [F(0), c, sn]
                assert v[1] * theta[2] == v[2] * theta[1]
                assert v[0] == 0 and v[1] * sn == v[2] * c and (v[1], v[2]) != (0, 0)
                assert v[3] * sn == v[4] * c and v[5] * sn == v[6] * c
        # global oriented frame of L + N = V: l ^ n = a1 ^ a2
        sq = (1, 1)
        l = add(scal(c, gen(0)), scal(sn, gen(1)))
        nn = add(scal(-sn, gen(0)), scal(c, gen(1)))
        ln = mul(l, nn, sq)
        assert eq(ln, mul(gen(0), gen(1), sq))
    # untwisted one rung on the same wall (store): w1(L) != 0 obstructs; two rungs suffice here
    return True


def check_twisted_hyperbolic_plane_morita_trivial():
    premise("sheaf.imported-real-line-bundles")
    premise("synthesis.wall-class-one-rung-obstruction")
    sq = (1, -1)
    for eps in (1, -1):
        l0 = scal(F(eps), gen(0))
        l1 = scal(F(eps), gen(1))
        f = scal(F(1, 2), add(sc(1), mul(l0, l1, sq)))
        assert eq(mul(f, f, sq), f)
        assert not eq(f, sc(1)) and not GA.is_zero(f)
        assert eq(f, scal(F(1, 2), add(sc(1), mul(gen(0), gen(1), sq))))  # fixed by l -> -l
    sqn = (-1, -1)
    I = mul(gen(0), gen(1), sqn)
    assert eq(mul(I, I, sqn), sc(-1))
    return True
