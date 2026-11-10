"""synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial: exact checks.

Sigma_m = L^{2m+1}(4) = S^{2m+1} / <J>, J the quarter turn v -> v . B in every coordinate plane of R^{2m+2}
(B = e_1e_2 + e_3e_4 + ..., GA). The dying line L is the flat line of holonomy -1 under J. Checks:
  (1) the action and the walls: J^2 = -1 and J orthogonal (a free Z_4 action on the unit sphere); the map c
      negating e_2, e_4, ... anticommutes with J, so x -> c(x) is a nowhere-zero section of L (x) (T*Sigma + R)
      and embeds L in T*M along the wall; the cometrics G_t = t pi - (1 - pi) (physical side t > 0 of
      signature (1, 2m+1)) and G_t = 1 - (1 - t) pi (definite) are J-equivariant, corank one at t = 0 with
      radical c(x), det = -t, respectively t, for m = 2, 3;
  (2) the spin lift of the doubled line: in Cl(2,0) the rotor e_1e_2 squares to -1 and acts on the plane as
      the half turn, the holonomy of L + L; it is the image of the quarter turn under the rotor isomorphism
      exp(e_1e_2 phi) -> rotation by phi, so the spin structures of L + L have Spin(2) holonomy +-e_1e_2;
  (3) the spin class: universally on BSpin(2) e = 2a, p1 = e^2 = 4a^2, q1 = p1/2 = 2a^2; on Sigma_m with
      a = y or 3y (the two spin structures), q1(L + L) = 2y^2 != 0 in H^4(Sigma_m; Z) = Z_4 exactly when
      m >= 2, while p1 = 4a^2 = 0; mod 2, x^2 = 0 and w(T Sigma_m) = (1 + u)^{m+1} equals 1 for m = 1, 3
      and not for m = 2;
  (4) cross-check in complex K-theory, dimension seven: 2(eta^2 - 1) is not in the ideal
      ((1 + s)^4 - 1, s^{m+1}) of Z[s] for m = 3, and is in it for m = 1, 2;
  (5) the upper bound on L^7(4): in the quaternion model H^2 = (Cl^0(3,0))^2 with J' = right multiplication
      by e_2e_3 (an orthogonal complex structure), R -> R e_2 R~ is odd under J' and |R e_2 R~| = R R~,
      so (R_1 e_2 R_1~, R_2 e_2 R_2~) embeds L in the trivial R^6: e(L) <= 6;
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen, sc, reverse, congruence_signature
from tp_premise import premise


def euclid(n):
    return tuple([1] * n)


def bivector_B(m):
    B = {}
    for j in range(m + 1):
        B[(2 * j, 2 * j + 1)] = F(1)
    return B


def vec(cs):
    return {(i,): F(c) for i, c in enumerate(cs) if c != 0}


def comps(v, n):
    assert all(len(b) == 1 for b in v)
    return [v.get((i,), F(0)) for i in range(n)]


def J_of(v, B, sq):
    """v . B = (vB - Bv)/2 for a vector v and bivector B."""
    return scal(F(1, 2), sub(mul(v, B, sq), mul(B, v, sq)))


def J_matrix(m):
    n = 2 * m + 2
    sq = euclid(n)
    B = bivector_B(m)
    cols = [comps(J_of(gen(i), B, sq), n) for i in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def matmul(A, Bm):
    return [[sum(A[i][k] * Bm[k][j] for k in range(len(Bm))) for j in range(len(Bm[0]))] for i in range(len(A))]


def transpose(A):
    return [list(r) for r in zip(*A)]


def apply(A, v):
    return [sum(A[i][j] * v[j] for j in range(len(v))) for i in range(len(A))]


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


def c_map(x):
    return [a for i, a in enumerate(x)]


def projector(v):
    n2 = sum(a * a for a in v)
    return [[v[i] * v[j] / n2 for j in range(len(v))] for i in range(len(v))]


def ident(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


POINTS = {
    2: [(1, 0, 0, 0, 0, 0), (1, 2, 0, -1, 3, 1), (0, 1, 1, 2, -2, 1), (2, -1, 3, 0, 1, 1)],
    3: [(1, 0, 0, 0, 0, 0, 0, 0), (1, 2, 0, -1, 3, 1, 0, 2), (0, 1, 1, 2, -2, 1, 1, -1), (3, -1, 2, 0, 1, 1, -2, 1)],
}


def check_lens_action_and_walls():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("sheaf.tameness")
    premise("sheaf.imported-real-line-bundles")
    for m, n in ((2, 6), (3, 8)):
        assert n == 2 * m + 2
        Jm = J_matrix(m)
        I = ident(n)
        minusI = [[-a for a in r] for r in I]
        assert matmul(Jm, Jm) == minusI                     # J^2 = -1: free Z_4 action
        assert matmul(transpose(Jm), Jm) == I               # J orthogonal
        assert Jm[1][0] == 1 and Jm[0][1] == -1             # quarter turn e1 -> e2 -> -e1
        for i in range(n):                                  # c J = -J c
            e = [F(int(k == i)) for k in range(n)]
            assert c_map(apply(Jm, e)) == [-a for a in apply(Jm, c_map(e))]
        for p in POINTS[m]:
            x = [F(a) for a in p]
            cx = c_map(x)
            assert any(a != 0 for a in cx)
            Jx = apply(Jm, x)
            assert c_map(Jx) == [-a for a in apply(Jm, cx)]  # c(Jx) = -J c(x): a section of L (x) E
            pi = projector(cx)
            assert projector(c_map(Jx)) == matmul(matmul(Jm, pi), transpose(Jm))
            table = [(F(1, 2), F(-1, 2), F(1, 2), (1, n - 1, 0), (n, 0, 0)),
                     (F(-1, 3), F(1, 3), F(-1, 3), (0, n, 0), (n - 1, 1, 0)),
                     (F(2), F(-2), F(2), (1, n - 1, 0), (n, 0, 0)),
                     (F(0), F(0), F(0), (0, n - 1, 1), (n - 1, 0, 1))]
            for t, d_ind, d_def, s_ind, s_def in table:
                Gind = [[t * pi[i][j] - (I[i][j] - pi[i][j]) for j in range(n)] for i in range(n)]
                Gdef = [[I[i][j] - (1 - t) * pi[i][j] for j in range(n)] for i in range(n)]
                assert det(Gind) == d_ind and det(Gdef) == d_def
                assert congruence_signature(Gind) == s_ind
                assert congruence_signature(Gdef) == s_def
                if t == 0:
                    assert apply(Gind, cx) == [F(0)] * n and apply(Gdef, cx) == [F(0)] * n


def check_spin_lift_of_doubled_line():
    premise("std-algebra.spin-double-cover")
    premise("sheaf.imported-real-line-bundles")
    sq = (1, 1)
    e12 = {(0, 1): F(1)}
    assert mul(e12, e12, sq) == {(): F(-1)}                 # the rotor squares to -1
    J2 = lambda v: scal(F(1, 2), sub(mul(v, e12, sq), mul(e12, v, sq)))
    assert J2(gen(0)) == gen(1) and J2(gen(1)) == {(0,): F(-1)}
    for i in range(2):
        v = gen(i)
        cover = mul(mul(e12, v, sq), reverse(e12), sq)
        assert cover == scal(-1, v)                         # the half turn, holonomy of L + L
        assert cover == J2(J2(v))                           # = (quarter turn)^2
    assert mul(mul(e12, e12, sq), e12, sq) == {(0, 1): F(-1)}   # the other lift -e12 = (e1e2)^3
    assert mul(mul(e12, e12, sq), mul(e12, e12, sq), sq) == {(): F(1)}  # order four


def pmul_int(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def trunc_mod(c, modulus, top):
    out = [0] * (top + 1)
    for d, v in enumerate(c):
        if d <= top:
            out[d] = v % modulus if d >= 1 else v
    return out


def check_spin_class_of_doubled_line_on_lens_spaces():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("sheaf.imported-real-line-bundles")
    e = [0, 2]                                              # BSpin(2): e = 2a
    p1 = pmul_int(e, e)
    assert p1 == [0, 0, 4]
    q1 = [c // 2 for c in p1]
    assert all(c % 2 == 0 for c in p1) and q1 == [0, 0, 2]
    expected_q1 = {1: [0, 0], 2: [0, 0, 2], 3: [0, 0, 2, 0]}
    expected_w = {1: [1, 0], 2: [1, 1, 1], 3: [1, 0, 0, 0]}
    for m in (1, 2, 3):
        for a in ([0, 1], [0, 3]):                          # the two spin structures, a = y and 3y
            a2 = pmul_int(a, a)
            q1L = trunc_mod([2 * c for c in a2], 4, m)
            p1L = trunc_mod([4 * c for c in a2], 4, m)
            eL = trunc_mod([2 * c for c in a], 4, m)
            assert q1L == expected_q1[m]
            assert all(c == 0 for c in p1L)
            assert eL[1] == 2                               # beta x = e(L + L) = 2y != 0
        w = [1]
        for _ in range(m + 1):
            w = pmul_int(w, [1, 1])
        assert [c % 2 for c in w[:m + 1]] == expected_w[m]


def binom(n, k):
    out = 1
    for j in range(k):
        out = out * (n - j) // (j + 1)
    return out


def reduce_mod_ideal(m, v, q):
    """Reduce v (coefficients of s^1..s^m) by the triangular Z-basis s^k((1+s)^q - 1), k = 0..m-1."""
    f = [binom(q, j) for j in range(1, m + 1)]
    v = list(v)
    for i in range(m):
        row = [0] * m
        for j in range(m):
            if j + i < m:
                row[j + i] = f[j]
        cc = v[i] // row[i]
        v = [a - cc * b for a, b in zip(v, row)]
    return v


def check_k_theory_cross_check():
    premise("sheaf.imported-real-line-bundles")
    expected = {1: [0], 2: [0, 0], 3: [0, 0, 2]}
    for m in (1, 2, 3):
        x = [2 * binom(2, j) for j in range(1, m + 1)]       # 2(eta^2 - 1) = 4s + 2s^2
        r = reduce_mod_ideal(m, x, 4)
        assert r == expected[m]
    r4 = reduce_mod_ideal(3, [8, 4, 0], 4)
    assert r4 == [0, 0, 0]                                   # 4(eta^2 - 1) = 0 on L^7(4)
    assert binom(4, 1) == 4 and binom(4, 2) == 6 and binom(4, 3) == 4


def rotor(w, x, y, z):
    return add(sc(w), scal(x, {(1, 2): F(1)}), scal(-y, {(0, 2): F(1)}), scal(z, {(0, 1): F(1)}))


def check_quaternionic_odd_map_bounds_embedding_rank():
    premise("std-algebra.spin-double-cover")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    E3 = (1, 1, 1)
    B = {(1, 2): F(1)}
    basis = [rotor(1, 0, 0, 0), rotor(0, 1, 0, 0), rotor(0, 0, 1, 0), rotor(0, 0, 0, 1)]
    keys = [(), (1, 2), (0, 2), (0, 1)]
    sgn = [1, 1, -1, 1]

    def coords(R):
        return [R.get(k, F(0)) * s for k, s in zip(keys, sgn)]
    Mt = transpose([coords(mul(b, B, E3)) for b in basis])
    assert Mt == [[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 0, -1], [0, 0, 1, 0]]
    assert matmul(transpose(Mt), Mt) == ident(4)
    assert matmul(Mt, Mt) == [[-a for a in r] for r in ident(4)]
    for s, nn in [((1, 2, 0, 1), 6), ((2, -1, 1, 3), 15), ((0, 1, 1, 1), 3), ((3, 1, -2, 0), 14), ((1, 0, 0, 0), 1)]:
        R = rotor(*s)
        RB = mul(R, B, E3)
        v = mul(mul(R, gen(1), E3), reverse(R), E3)
        vB = mul(mul(RB, gen(1), E3), reverse(RB), E3)
        assert all(len(k) == 1 for k in v)
        assert vB == scal(-1, v)                             # odd under R -> R e2e3
        n2 = mul(R, reverse(R), E3).get((), F(0))
        assert n2 == nn and mul(v, v, E3).get((), F(0)) == nn * nn
    for s1, s2, tot in [((1, 2, 0, 1), (0, 0, 0, 0), 36), ((0, 0, 0, 0), (2, -1, 1, 3), 225),
                        ((1, 1, 1, 1), (3, 1, -2, 0), 212)]:
        R1, R2 = rotor(*s1), rotor(*s2)
        v1 = mul(mul(R1, gen(1), E3), reverse(R1), E3)
        v2 = mul(mul(R2, gen(1), E3), reverse(R2), E3)
        assert mul(v1, v1, E3).get((), F(0)) + mul(v2, v2, E3).get((), F(0)) == tot
