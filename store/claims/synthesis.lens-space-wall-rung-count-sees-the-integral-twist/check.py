"""synthesis.lens-space-wall-rung-count-sees-the-integral-twist: exact checks.

Rational rotors in Cl(3,0) (GA), matrices over Fractions. Sigma = L(4,1) = S^3 / <B>, B = e2 e3 acting on
unit rotors by left multiplication (B^2 = -1, so <B> has order four). Checks:
  (1) the adjoint frame: O(R)_{ab} = <e_a, R e_b R~> / (R R~) is orthogonal with det 1 and O(BR) = D O(R),
      D = diag(1, -1, -1); so row 1 of O is a global section of the trivial line and rows 2, 3 are sections
      of the Moebius line L twisted by B: an explicit global frame of R + L + L over L(4,1), and an
      explicit embedding of L (row 2) in the trivial R^3;
  (2) the indefinite wall: with theta = row 2 . sigma (left-invariant coframe sigma), the cometric
      G_0 = (I - l l^T) + (-dt^2) is degenerate with radical theta and signature (2,1) on a complement; the
      wall form h_0 on T*M + R^4 (rung basis a1, a2, b1, b2) built from the adjoint frame of the rungs is
      single valued (h_0(BR) = h_0(R)), restricts to G_0 on T*M, has signature (5,3) like G_1 + H + H, and
      its maximal negative subspace span(dt, theta - g2, g3) carries the single-valued frame
      f_a = sum_b O_{ba} n_b with negative definite Gram: the negative bundle at the wall is trivial;
  (3) the definite wall: G_t = I_4 - (1 - t) l l^T on T*Sigma + R; three rungs with the dying line embedded as
      row 2 in the null space of H + H + H give the stored twisted-coupling form, single valued, restricting
      to G on T*M, with det h = 2 mu nu beta^2 - t and signature (7,3) for t >= 0 (wall included);
  (4) the comparison wall T^3 with x pulled back from a circle: the half-angle frame (c, s) embeds L in the
      trivial R^2, the definite two-rung form is single valued with det h = t - 2 mu nu beta^2 and signature
      (6,2) for t >= 0: same mod-2 data (x != 0 = x^2), two rungs, against three on L(4,1).
"""
from fractions import Fraction as F
import GA
from GA import congruence_signature, mul, add, gen, sc, scal, reverse
from tp_premise import premise

E3 = (1, 1, 1)


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


def rotor(w, x, y, z):
    """w + x e2e3 + y e3e1 + z e1e2 in Cl(3,0); generators 0, 1, 2 are e1, e2, e3."""
    return add(sc(w), scal(x, {(1, 2): F(1)}), scal(-y, {(0, 2): F(1)}), scal(z, {(0, 1): F(1)}))


B = {(1, 2): F(1)}                                   # e2 e3


def adjoint(R):
    n2 = mul(R, reverse(R), E3)
    r = n2.get((), F(0))
    assert set(n2) <= {()} and r > 0
    O = [[F(0)] * 3 for _ in range(3)]
    for b in range(3):
        v = mul(mul(R, gen(b), E3), reverse(R), E3)
        assert all(len(k) == 1 for k in v)            # a vector
        for a in range(3):
            O[a][b] = v.get((a,), F(0)) / r
    return O


SAMPLES = [(1, 0, 0, 0), (1, 2, 0, 1), (2, -1, 1, 3), (0, 1, 1, 1), (3, 1, -2, 0), (1, 1, 2, -3), (0, 0, 1, 2)]
D = [1, -1, -1]


def check_adjoint_frame_twisted_by_half_turn():
    premise("std-algebra.spin-double-cover")
    premise("sheaf.imported-real-line-bundles")
    BB = mul(B, B, E3)
    assert BB == {(): F(-1)}                          # B has order four: the half-turn rotor squares to -1
    for s in SAMPLES:
        R = rotor(*s)
        O = adjoint(R)
        OB = adjoint(mul(B, R, E3))
        assert all(OB[a][b] == D[a] * O[a][b] for a in range(3) for b in range(3))
        assert all(sum(O[a][c] * O[b][c] for c in range(3)) == (1 if a == b else 0)
                   for a in range(3) for b in range(3))
        assert det(O) == 1
        # -R gives the same frame (the double cover), so the frame lives on S^3/<B> = SO(3)/<D>
        assert adjoint(scal(-1, R)) == O
    return True


def h1_matrix():
    h = [[F(0)] * 8 for _ in range(8)]
    for i in range(3):
        h[i][i] = F(1)
    h[3][3] = F(-1)
    for i in range(2):
        h[4 + i][6 + i] = h[6 + i][4 + i] = F(1)     # a_i . b_i = 1
    return h


def wall_form(O):
    """h_0 on (sigma1, sigma2, sigma3, dt, r1..r4), r = (a1, a2, b1, b2)."""
    l = O[1]
    h = [[F(0)] * 8 for _ in range(8)]
    for c in range(3):
        for d in range(3):
            h[c][d] = (1 if c == d else 0) - l[c] * l[d]
    h[3][3] = F(-1)
    h[4][4] = F(1)                                    # r1 positive
    for b in range(3):
        for d in range(3):
            h[5 + b][5 + d] = O[0][b] * O[0][d] - O[2][b] * O[2][d]   # g1 positive, g2 null, g3 negative
    for c in range(3):
        for b in range(3):
            h[c][5 + b] = h[5 + b][c] = l[c] * O[1][b]                # theta pairs with g2
    return h


def bil(M, u, v):
    return sum(u[i] * M[i][j] * v[j] for i in range(len(u)) for j in range(len(v)))


def check_indefinite_lens_wall_form_has_trivial_negative_bundle():
    premise("sheaf.tameness")
    premise("sheaf.degeneration-sheaf")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("std-algebra.spin-double-cover")
    h1 = h1_matrix()
    assert congruence_signature(h1) == (5, 3, 0)
    for s in SAMPLES:
        R = rotor(*s)
        O, OB = adjoint(R), adjoint(mul(B, R, E3))
        h0 = wall_form(O)
        assert wall_form(OB) == h0                    # single valued on L(4,1)
        assert all(h0[i][j] == h0[j][i] for i in range(8) for j in range(8))
        theta = list(O[1]) + [F(0)] * 5
        G0 = [row[:4] for row in h0[:4]]
        # restriction to T*M is the wall cometric: theta in its radical, signature (2,1) on a complement
        assert all(bil(G0, theta[:4], [F(1) if j == i else F(0) for j in range(4)]) == 0 for i in range(4))
        assert congruence_signature(G0) == (2, 1, 1)
        assert det(h0) != 0 and congruence_signature(h0) == (5, 3, 0)
        # negative subspace span(dt, theta - g2, g3) and its single-valued frame f_a = sum_b O_ba n_b
        dt = [F(0)] * 3 + [F(1)] + [F(0)] * 4
        g2 = [F(0)] * 5 + list(O[1])
        g3 = [F(0)] * 5 + list(O[2])
        n = [dt, [theta[i] - g2[i] for i in range(8)], g3]
        assert [[bil(h0, x, y) for y in n] for x in n] == [[-1, 0, 0], [0, -2, 0], [0, 0, -1]]
        nB = [dt, [OB[1][i] if i < 3 else (-OB[1][i - 5] if i >= 5 else F(0)) for i in range(8)],
              [F(0)] * 5 + list(OB[2])]
        f = [[sum(O[b][a] * n[b][i] for b in range(3)) for i in range(8)] for a in range(3)]
        fB = [[sum(OB[b][a] * nB[b][i] for b in range(3)) for i in range(8)] for a in range(3)]
        assert f == fB                                # the frame descends: N(h_0) is trivial
        gram = [[bil(h0, x, y) for y in f] for x in f]
        assert congruence_signature(gram) == (0, 3, 0)
    return True


def coupled_form(G, l, k, beta, mu, nu):
    """G on T*M (size m, dying covector direction l padded), plus H_k on (a_1..a_k, b_1..b_k), coupled by
    h(alpha, a_i) = beta mu l_i alpha(u), h(alpha, b_i) = beta nu l_i alpha(u), alpha(u) = lpad . alpha."""
    m = len(G)
    lpad, lr = l[0], l[1]
    N = m + 2 * k
    h = [[F(0)] * N for _ in range(N)]
    for i in range(m):
        for j in range(m):
            h[i][j] = G[i][j]
    for i in range(k):
        h[m + i][m + k + i] = h[m + k + i][m + i] = F(1)
    for c in range(m):
        for i in range(k):
            h[c][m + i] = h[m + i][c] = beta * mu * lr[i] * lpad[c]
            h[c][m + k + i] = h[m + k + i][c] = beta * nu * lr[i] * lpad[c]
    return h


def check_definite_lens_wall_three_rungs():
    premise("synthesis.wall-class-one-rung-obstruction")
    premise("sheaf.tameness")
    premise("sheaf.one-sided-completion")
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    mu, nu = F(-1, 3), F(1)
    for s in SAMPLES[:5]:
        R = rotor(*s)
        O, OB = adjoint(R), adjoint(mul(B, R, E3))
        for t in [F(0), F(1, 5), F(1), F(-1, 2)]:
            for beta in [F(1), F(1, 2)]:
                def build(OO):
                    l = OO[1]
                    lpad = list(l) + [F(0)]
                    G = [[(1 if i == j else 0) - (1 - t) * lpad[i] * lpad[j] for j in range(4)] for i in range(4)]
                    return coupled_form(G, (lpad, list(l)), 3, beta, mu, nu), G
                h, G = build(O)
                assert build(OB)[0] == h                  # single valued
                assert [row[:4] for row in h[:4]] == G    # restricts to G on T*M
                assert det(h) == 2 * mu * nu * beta ** 2 - t
                if t >= 0:
                    assert congruence_signature(h) == (7, 3, 0)
                    assert congruence_signature(G)[:2] == ((4, 0) if t > 0 else (3, 0))
    return True


def check_torus_comparison_two_rungs_definite():
    premise("synthesis.wall-rung-count-is-height-of-dying-line-class")
    premise("sheaf.one-sided-completion")
    premise("synthesis.wall-class-one-rung-obstruction")
    mu, nu = F(-1, 3), F(1)
    cs, dets = [], []
    for u in [F(0), F(1, 2), F(2), F(-3), F(1, 7)]:
        c, s = (1 - u * u) / (1 + u * u), 2 * u / (1 + u * u)   # half-angle point (cos phi/2, sin phi/2)
        assert c * c + s * s == 1
        cs.append((c, s))
        for t in [F(0), F(1, 3), F(2)]:
            def build(cc, ss):
                lpad = [cc, ss, F(0), F(0)]               # theta = c dpsi + s dchi on T^3, plus dt
                G = [[(1 if i == j else 0) - (1 - t) * lpad[i] * lpad[j] for j in range(4)] for i in range(4)]
                return coupled_form(G, (lpad, [cc, ss]), 2, F(1), mu, nu)
            h = build(c, s)
            assert build(-c, -s) == h                     # monodromy phi -> phi + 2 pi
            assert det(h) == t - 2 * mu * nu
            assert congruence_signature(h) == (6, 2, 0)
            assert h[0][4] == mu * c * c and h[1][6] == nu * s * c   # the coupling is quadratic in (c, s)
            dets.append(det(h))
    assert cs == [(1, 0), (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)), (F(-4, 5), F(-3, 5)), (F(24, 25), F(7, 25))]
    assert dets[:3] == [F(2, 3), F(1), F(8, 3)]
    return True


if __name__ == "__main__":
    for fn in [check_adjoint_frame_twisted_by_half_turn,
               check_indefinite_lens_wall_form_has_trivial_negative_bundle,
               check_definite_lens_wall_three_rungs, check_torus_comparison_two_rungs_definite]:
        GA.check(fn.__name__, fn())
