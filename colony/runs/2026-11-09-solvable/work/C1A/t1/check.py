"""Two rungs need the doubled dying line stably trivial: exact checks.

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
  (6) the comparison wall: an orthogonal sum h + A with A negative definite of rank four keeps the corank-one
      wall, the restriction property and nondegeneracy, adding (0,4) to every signature.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, gen, sc, reverse, congruence_signature, check
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
    return [(-a if i % 2 else a) for i, a in enumerate(x)]


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
    for m in (2, 3):
        n = 2 * m + 2
        Jm = J_matrix(m)
        I = ident(n)
        minusI = [[-a for a in r] for r in I]
        check("J^2 = -1 (m=%d)" % m, matmul(Jm, Jm) == minusI)
        check("J orthogonal (m=%d)" % m, matmul(transpose(Jm), Jm) == I)
        # c anticommutes with J: c(Jv) = -J c(v) on a basis
        ok = True
        for i in range(n):
            e = [F(int(k == i)) for k in range(n)]
            if c_map(apply(Jm, e)) != [-a for a in apply(Jm, c_map(e))]:
                ok = False
        check("c J = -J c (m=%d): x -> c(x) is a section of L (x) E" % m, ok)
        for p in POINTS[m]:
            x = [F(a) for a in p]
            cx = c_map(x)
            check("c(x) != 0", any(a != 0 for a in cx))
            Jx = apply(Jm, x)
            # c(Jx) = -J c(x): the line through c(x) is carried to the line through c(Jx) by J
            check("c(Jx) = -J c(x)", c_map(Jx) == [-a for a in apply(Jm, cx)])
            pi = projector(cx)
            piJ = projector(c_map(Jx))
            check("pi(Jx) = J pi(x) J^T", piJ == matmul(matmul(Jm, pi), transpose(Jm)))
            for t in (F(1, 2), F(-1, 3), F(0), F(2)):
                Gind = [[t * pi[i][j] - (I[i][j] - pi[i][j]) for j in range(n)] for i in range(n)]
                Gdef = [[I[i][j] - (1 - t) * pi[i][j] for j in range(n)] for i in range(n)]
                check("det G_ind = -t", det(Gind) == -t)
                check("det G_def = t", det(Gdef) == t)
                sgi = congruence_signature(Gind)
                sgd = congruence_signature(Gdef)
                if t > 0:
                    check("indefinite physical side (1, 2m+1)", sgi == (1, n - 1, 0))
                    check("definite physical side (2m+2, 0)", sgd == (n, 0, 0))
                elif t < 0:
                    check("far side of the indefinite wall (0, 2m+2)", sgi == (0, n, 0))
                    check("far side of the definite wall (2m+1, 1)", sgd == (n - 1, 1, 0))
                else:
                    check("corank one at the wall", sgi == (0, n - 1, 1) and sgd == (n - 1, 0, 1))
                    check("radical c(x) (indefinite)", apply(Gind, cx) == [F(0)] * n)
                    check("radical c(x) (definite)", apply(Gdef, cx) == [F(0)] * n)


def check_spin_lift_of_doubled_line():
    premise("std-algebra.spin-double-cover")
    premise("sheaf.imported-real-line-bundles")
    sq = (1, 1)
    e12 = {(0, 1): F(1)}
    check("(e1e2)^2 = -1", mul(e12, e12, sq) == {(): F(-1)})
    for i in range(2):
        v = gen(i)
        rot = mul(mul(e12, v, sq), reverse(e12), sq)
        check("e1e2 v (e1e2)~ = -v: the half turn, holonomy of L + L", rot == scal(-1, v))
    # the quarter turn of the plane, J2(v) = v . e12
    J2 = lambda v: scal(F(1, 2), sub(mul(v, e12, sq), mul(e12, v, sq)))
    check("J2(e1) = e2", J2(gen(0)) == gen(1))
    check("J2(e2) = -e1", J2(gen(1)) == scal(-1, gen(0)))
    check("J2^2 = -1", all(J2(J2(gen(i))) == scal(-1, gen(i)) for i in range(2)))
    # rotor isomorphism exp(e12 phi) -> rot(phi) on the order-4 subgroups: e12 = exp(e12 pi/2) -> J2;
    # the double cover R -> (v -> R v R~) sends e12 to the half turn = J2^2.
    for i in range(2):
        v = gen(i)
        check("double cover of e12 = J2^2",
              mul(mul(e12, v, sq), reverse(e12), sq) == J2(J2(v)))
    m3 = mul(mul(e12, e12, sq), e12, sq)
    check("the other lift -e12 = (e1e2)^3", m3 == scal(-1, e12))


def poly_mod(coeffs, modulus, top):
    """Truncate a polynomial in y below degree top+1 and reduce coefficients (degree >= 1) mod modulus."""
    out = [0] * (top + 1)
    for d, c in enumerate(coeffs):
        if d <= top:
            out[d] = c % modulus if d >= 1 else c
    return out


def pmul_int(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def check_spin_class_of_doubled_line_on_lens_spaces():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("sheaf.imported-real-line-bundles")
    # universal case, H^*(BSpin(2); Z) = Z[a]: e = 2a, p1 = e^2, q1 = p1 / 2
    e = [0, 2]
    p1 = pmul_int(e, e)
    check("p1 = 4 a^2 on BSpin(2)", p1 == [0, 0, 4])
    q1 = [c // 2 for c in p1]
    check("q1 = 2 a^2 (H^4 torsion-free, so p1/2 is exact)", all(c % 2 == 0 for c in p1) and q1 == [0, 0, 2])
    for m in (1, 2, 3):
        # H^{even}(L^{2m+1}(4); Z) = Z[y] / (4y, y^{m+1}); the two spin structures give a = y, 3y
        for a in ([0, 1], [0, 3]):
            a2 = poly_mod(pmul_int(a, a), 4, m)
            q1L = poly_mod([2 * c for c in a2], 4, m)
            p1L = poly_mod([4 * c for c in a2], 4, m)
            check("p1(L + L) = 0 in H^4 (m=%d)" % m, all(c == 0 for c in p1L[1:]))
            if m >= 2:
                check("q1(L + L) = 2 y^2 != 0 (m=%d)" % m, q1L[2] == 2)
            else:
                check("q1 = 0 on L(4,1): H^4 = 0 (m=1)", all(c == 0 for c in q1L[1:]))
        # mod 2: H^*(;Z_2) = Lambda[x] (x) Z_2[u]/(u^{m+1}); x^2 = 0 since 4 = 0 mod 4 lifts x to Z_4
        w = [1]
        for _ in range(m + 1):
            w = pmul_int(w, [1, 1])
        w = [c % 2 for c in w[:m + 1]]
        if m in (1, 3):
            check("w(T Sigma) = 1 (m=%d)" % m, w == [1] + [0] * m)
        else:
            check("w(T Sigma) != 1 (m=2)", w != [1] + [0] * m)


def in_ideal(m, v, q=4):
    """Is the vector v (coefficients of s^1..s^m) in the Z-span of s^k ((1+s)^q - 1), truncated at s^{m+1}?"""
    from math import comb
    f = [comb(q, j) for j in range(1, m + 1)]
    rows = []
    for sh in range(m):
        r = [0] * m
        for j in range(m):
            if j + sh < m:
                r[j + sh] = f[j]
        rows.append(r)
    v = list(v)
    for i in range(m):
        piv = rows[i][i]
        if v[i] % piv:
            return False
        cc = v[i] // piv
        v = [a - cc * b for a, b in zip(v, rows[i])]
    return all(a == 0 for a in v)


def check_k_theory_cross_check():
    premise("sheaf.imported-real-line-bundles")
    from math import comb
    for m in (1, 2, 3):
        # c(L + L) - 2 = 2(eta^2 - 1) = 2((1+s)^2 - 1) = 4s + 2s^2
        x = [2 * comb(2, j) for j in range(1, m + 1)]
        if m == 3:
            check("2(eta^2 - 1) != 0 in K(L^7(4))", not in_ideal(m, x))
            check("4(eta^2 - 1) = 0 in K(L^7(4))", in_ideal(m, [2 * a for a in x]))
        else:
            check("2(eta^2 - 1) = 0 in K(L^%d(4))" % (2 * m + 1), in_ideal(m, x))


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
    M = [coords(mul(b, B, E3)) for b in basis]          # rows: images of basis elements
    Mt = transpose(M)
    check("right multiplication by e2e3 is orthogonal", matmul(transpose(Mt), Mt) == ident(4))
    check("and squares to -1 (a complex structure on H, hence on H^2)",
          matmul(Mt, Mt) == [[-a for a in r] for r in ident(4)])
    samples = [(1, 2, 0, 1), (2, -1, 1, 3), (0, 1, 1, 1), (3, 1, -2, 0), (1, 0, 0, 0)]
    for s in samples:
        R = rotor(*s)
        RB = mul(R, B, E3)
        v = mul(mul(R, gen(1), E3), reverse(R), E3)
        vB = mul(mul(RB, gen(1), E3), reverse(RB), E3)
        check("R e2 R~ is a vector", all(len(k) == 1 for k in v))
        check("odd under R -> R e2e3", vB == scal(-1, v))
        n2 = mul(R, reverse(R), E3).get((), F(0))
        vv = mul(v, v, E3).get((), F(0))
        check("|R e2 R~|^2 = (R R~)^2", vv == n2 * n2)
    for s1, s2 in [((1, 2, 0, 1), (0, 0, 0, 0)), ((0, 0, 0, 0), (2, -1, 1, 3)), ((1, 1, 1, 1), (3, 1, -2, 0))]:
        R1, R2 = rotor(*s1), rotor(*s2)
        v1 = mul(mul(R1, gen(1), E3), reverse(R1), E3)
        v2 = mul(mul(R2, gen(1), E3), reverse(R2), E3)
        tot = mul(v1, v1, E3).get((), F(0)) + mul(v2, v2, E3).get((), F(0))
        n1 = mul(R1, reverse(R1), E3).get((), F(0))
        n2 = mul(R2, reverse(R2), E3).get((), F(0))
        check("|F|^2 = |R1|^4 + |R2|^4 > 0", tot == n1 * n1 + n2 * n2 and tot > 0)


def check_comparison_wall_product():
    premise("synthesis.lens-space-wall-rung-count-sees-the-integral-twist")
    premise("sheaf.tameness")
    # a block h (signature (P,Q)) and A = -I_4: h + A has signature (P, Q + 4), det h * det A, and the
    # wall cometric G + A keeps corank one with the same radical
    h = [[0, 1, 0], [1, 0, 0], [0, 0, -1]]                 # sample nondegenerate block, signature (1,2)
    A = [[-1 if i == j else 0 for j in range(4)] for i in range(4)]
    S = [[F(0)] * 7 for _ in range(7)]
    for i in range(3):
        for j in range(3):
            S[i][j] = F(h[i][j])
    for i in range(4):
        S[3 + i][3 + i] = F(A[i][i])
    check("signature adds (0,4)", congruence_signature(S) == (1, 6, 0))
    check("det multiplies", det(S) == det(h) * det(A))
    G0 = [[F(0), F(0)], [F(0), F(-1)]]                     # corank-one wall block, radical e_1
    W = [[F(0)] * 6 for _ in range(6)]
    for i in range(2):
        for j in range(2):
            W[i][j] = G0[i][j]
    for i in range(4):
        W[2 + i][2 + i] = F(-1)
    check("product wall stays corank one", congruence_signature(W) == (0, 5, 1))
