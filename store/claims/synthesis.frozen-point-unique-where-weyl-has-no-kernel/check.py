"""synthesis.frozen-point-unique-where-weyl-has-no-kernel: exact checks.

All tensors are arrays of Fractions in an orthonormal frame with eta = diag(1, -1, -1, -1), the series' mostly-minus convention.
The Weyl tensor of a vacuum region is assembled from its electric and magnetic parts,
W_{0i0j} = E_ij, W_{0ijk} = eps_{jkm} B_{mi}, W_{ijkl} = -eps_{ijm} eps_{kln} E_mn, and its
algebraic symmetries (antisymmetry, pair symmetry, first Bianchi, tracelessness) are verified
before use. Ranks are exact (Gaussian elimination over Fractions).

  (1) Schwarzschild (E = (M/r^3) diag(-2, 1, 1), B = 0, at M/r^3 = 1 and 2/5): W_{abcd} v^d = 0
      has only v = 0 (rank 4); a type N wave (E, B transverse and traceless) has the null
      propagation vector in its kernel, so the hypothesis is not automatic.
  (2) On the tractor fibre (sigma, mu_0..mu_3, rho), the curvature of the connection in an Einstein
      scale acts as the Weyl tensor on the mu slot and kills the other two: at the Schwarzschild
      point the common kernel of the six Omega_ab is two-dimensional, spanned by the sigma and
      rho slots; at the type N point it is three-dimensional.
  (3) A tractor with vanishing mu slot on an open set is parallel only if rho = (Lambda/6) sigma
      with sigma constant: I_r = sigma_r I, <I_r, I_r> = sigma_r^2 Lambda/3, at Lambda = 3/7.
  (4) The proof's GTG route (lib/gtg.py): the tractor field strength of the static Schwarzschild-de Sitter
      field is -W on the physical planes with no n0 or ninf block; the Weyl map has rank-four kernel map
      (no kernel vector); a type N Weyl map has its null direction as a kernel vector; the algebraic step
      on sigma ninf + rho n0.
"""
from fractions import Fraction as F
from itertools import product
import GA  # noqa: F401  (house rule; the computation is tensor algebra over Fractions)
from tp_premise import premise
import gtg

ETA = [F(1), F(-1), F(-1), F(-1)]


def eps3(i, j, k):
    if len({i, j, k}) < 3:
        return 0
    return 1 if (i, j, k) in ((0, 1, 2), (1, 2, 0), (2, 0, 1)) else -1


def weyl(E, B):
    W = {}
    for a, b, c, d in product(range(4), repeat=4):
        W[a, b, c, d] = F(0)
    for i, j in product(range(3), repeat=2):
        for (a, b, c, d), s in (((0, i + 1, 0, j + 1), 1), ((i + 1, 0, 0, j + 1), -1),
                                ((0, i + 1, j + 1, 0), -1), ((i + 1, 0, j + 1, 0), 1)):
            W[a, b, c, d] += s * E[i][j]
    for i, j, k in product(range(3), repeat=3):
        val = sum(eps3(j, k, m) * B[m][i] for m in range(3))
        if val:
            for (a, b, c, d), s in (((0, i + 1, j + 1, k + 1), 1), ((i + 1, 0, j + 1, k + 1), -1),
                                    ((j + 1, k + 1, 0, i + 1), 1), ((j + 1, k + 1, i + 1, 0), -1)):
                W[a, b, c, d] += s * val
    for i, j, k, l in product(range(3), repeat=4):
        W[i + 1, j + 1, k + 1, l + 1] = -sum(eps3(i, j, m) * eps3(k, l, n) * E[m][n]
                                             for m in range(3) for n in range(3))
    return W


def is_weyl(W):
    for a, b, c, d in product(range(4), repeat=4):
        if W[a, b, c, d] != -W[b, a, c, d] or W[a, b, c, d] != W[c, d, a, b]:
            return False
        if W[a, b, c, d] + W[a, c, d, b] + W[a, d, b, c] != 0:
            return False
    for b, d in product(range(4), repeat=2):
        if sum(ETA[a] * W[a, b, a, d] for a in range(4)) != 0:
            return False
    return True


def rank(rows):
    M = [list(r) for r in rows]
    rk, col, ncol = 0, 0, len(M[0]) if M else 0
    while rk < len(M) and col < ncol:
        piv = next((r for r in range(rk, len(M)) if M[r][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        rk += 1
        col += 1
    return rk


def kernel_rows(W):
    """rows of the linear map v -> (W_abcd v^d), v^d with index raised by eta"""
    return [[W[a, b, c, d] * ETA[d] for d in range(4)] for a, b, c in product(range(4), repeat=3)]


def omega(W, a, b):
    """6x6 action on (sigma, mu_0..mu_3, rho): mu_c -> W_{ab c}^{d} mu_d, other slots killed"""
    O = [[F(0)] * 6 for _ in range(6)]
    for c, d in product(range(4), repeat=2):
        O[1 + c][1 + d] = W[a, b, c, d] * ETA[d]
    return O


def common_kernel_dim(W):
    rows = []
    for a in range(4):
        for b in range(a + 1, 4):
            rows.extend(omega(W, a, b))
    return 6 - rank(rows)


def schwarzschild(m):
    return [[-2 * m, F(0), F(0)], [F(0), m, F(0)], [F(0), F(0), m]], [[F(0)] * 3 for _ in range(3)]


def type_n(a, b):
    E = [[F(0)] * 3, [F(0), a, b], [F(0), b, -a]]
    B = [[F(0)] * 3, [F(0), -b, a], [F(0), a, b]]
    return E, B


def apply(W, v):
    return [sum(W[a, b, c, d] * ETA[d] * v[d] for d in range(4)) for a, b, c in product(range(4), repeat=3)]


def check_weyl_kernel_schwarzschild_and_type_n():
    premise("dark-energy.imported-frozen-point-geometry")
    for m in (F(1), F(2, 5)):
        W = weyl(*schwarzschild(m))
        assert is_weyl(W)
        assert rank(kernel_rows(W)) == 4
        assert W[0, 1, 0, 1] == -2 * m and W[2, 3, 2, 3] == 2 * m
    E, B = type_n(F(1), F(1, 3))
    W = weyl(E, B)
    assert is_weyl(W)
    k = [F(1), F(1), F(0), F(0)]
    kk = [F(1), F(-1), F(0), F(0)]
    assert any(x != 0 for x in apply(W, kk))
    assert all(x == 0 for x in apply(W, k))
    assert rank(kernel_rows(W)) == 3


def check_tractor_curvature_common_kernel():
    premise("dark-energy.imported-frozen-point-geometry")
    W = weyl(*schwarzschild(F(1)))
    assert common_kernel_dim(W) == 2
    rows = []
    for a in range(4):
        for b in range(a + 1, 4):
            rows.extend(omega(W, a, b))
    for v in ([F(1), F(0), F(0), F(0), F(0), F(0)], [F(0), F(0), F(0), F(0), F(0), F(1)]):
        assert all(sum(r[i] * v[i] for i in range(6)) == 0 for r in rows)
    E, B = type_n(F(1), F(1, 3))
    assert common_kernel_dim(weyl(E, B)) == 3
    zero = {key: F(0) for key in product(range(4), repeat=4)}
    assert common_kernel_dim(zero) == 6


def tractor_ip(X, Y):
    """<(s, m, r), (s', m', r')> = s r' + r s' + eta(m, m')"""
    return X[0] * Y[5] + X[5] * Y[0] + sum(ETA[i] * X[1 + i] * Y[1 + i] for i in range(4))


def connection_algebraic_part(I, lam):
    """the parts of nabla_a I that survive when sigma, mu, rho are locally constant and mu = 0:
    top: -mu_a; middle: g_ab rho - P_ab sigma with P = (lam/6) g; bottom: P_a^b mu_b."""
    s, mu, r = I[0], I[1:5], I[5]
    top = [-mu[a] for a in range(4)]
    mid = [[(ETA[a] if a == b else F(0)) * (r - lam / 6 * s) for b in range(4)] for a in range(4)]
    bot = [lam / 6 * mu[a] for a in range(4)]
    return top, mid, bot


def check_parallel_tractors_are_multiples_of_I():
    premise("dark-energy.imported-frozen-point-geometry")
    lam = F(3, 7)
    I = [F(1), F(0), F(0), F(0), F(0), lam / 6]
    assert tractor_ip(I, I) == lam / 3
    top, mid, bot = connection_algebraic_part(I, lam)
    assert all(x == 0 for x in top + bot) and all(x == 0 for row in mid for x in row)
    # with mu = 0 on an open set the middle slot is linear in (sigma, rho): rank one, kernel (1, lam/6)
    cols = []
    for v in ([F(1), F(0)], [F(0), F(1)]):
        top, mid, bot = connection_algebraic_part([v[0], F(0), F(0), F(0), F(0), v[1]], lam)
        cols.append([x for row in mid for x in row])
    rows = [[cols[0][i], cols[1][i]] for i in range(16)]
    assert rank(rows) == 1
    assert all(r[0] * 1 + r[1] * (lam / 6) == 0 for r in rows)
    assert any(r[0] * 1 + r[1] * (lam / 5) != 0 for r in rows)
    # Lambda = 0: null frozen point, Ricci-flat scale, kernel (1, 0)
    I0 = [F(1), F(0), F(0), F(0), F(0), F(0)]
    assert tractor_ip(I0, I0) == 0
    cols0 = []
    for v in ([F(1), F(0)], [F(0), F(1)]):
        top, mid, bot = connection_algebraic_part([v[0], F(0), F(0), F(0), F(0), v[1]], F(0))
        cols0.append([x for row in mid for x in row])
    rows0 = [[cols0[0][i], cols0[1][i]] for i in range(16)]
    assert rank(rows0) == 1 and all(r[0] == 0 for r in rows0) and any(r[1] != 0 for r in rows0)
    for c in (F(2), F(-3, 5)):
        Ir = [c * x for x in I]
        assert tractor_ip(Ir, Ir) == c * c * lam / 3


# ---- the proof's GTG route (lib/gtg.py): tractor field strength of the stored static fields ----
GTG_POINTS = [(F(3, 7), F(1), F(1, 2), F(3, 5), F(4, 5)), (F(0), F(3), F(1, 2), F(4, 5), F(3, 5))]   # (Lambda, r, sqrt f, sin, cos)


ALG_A = GA.add(GA.gen(0), GA.scal(F(2), GA.gen(3)))
ALG_S = F(2)
ALG_OFF = (F(1), F(5))


def _kernel_rank(Wop, sq):
    """Rank of v -> (W(e_a ^ e_b) . v)_{a<b} on the four spacetime vectors."""
    rows = []
    for a in range(4):
        for b in range(a + 1, 4):
            Wab = Wop(gtg.biv(a, b, sq))
            for k in range(4):
                rows.append([gtg.bdot(Wab, GA.gen(m), sq).get((k,), F(0)) for m in range(4)])
    return GA.rank_of_vectors([list(c) for c in zip(*rows)])


def check_gtg_tractor_field_strength_is_minus_weyl():
    """On the Einstein region the tractor gauge field is Omega(a) + u ^ hb^{-1}(a), u = (Lambda/6) n0 - ninf; its
    field strength (computed by the library from the static Schwarzschild-de Sitter field on exact jets) is
    F_T(e_mu ^ e_nu) = -W(g_mu ^ g_nu): spacetime bivectors only (no n0 or ninf block); the Weyl map has no
    kernel vector (rank four); type N has its null direction as a kernel vector; the algebraic step: on
    sigma ninf + rho n0 the connection's algebraic part is -(u . V) A, zero exactly on the line of I, and
    Q(c I) = c^2 Lambda/3."""
    premise("synthesis.imported-gtg-dictionary")
    premise("synthesis.gtg-tractor-gauge-field-reproduces-tractor-connection")
    premise("dark-energy.imported-frozen-point-geometry")
    ok = True
    sq = gtg.S13
    sqc = gtg.S24
    n0, ni = gtg.null_pair(sqc)
    for lam, r0, w, s0, c0 in GTG_POINTS:
        M = gtg.mass_for_root(r0, w, lam)
        ok = ok and M > 0
        fld = gtg.static_field(r0, s0, c0, gtg.f_static(M, lam), order=2)
        Rc = fld.curvature()
        ok = ok and all(GA.eq(gtg.ricci(Rc, GA.gen(m)), GA.scal(lam, GA.gen(m))) for m in range(fld.d))
        W = gtg.weyl_op(Rc)
        k = M / r0 ** 3
        sig_r = GA.mul(GA.gen(1), GA.gen(0), sq)
        ok = ok and all(GA.eq(W[pl], gtg.op_type_d(k / 2, sig_r)(gtg.biv(*pl))) for pl in W)
        u = GA.sub(GA.scal(lam / 6, n0), ni)
        ok = ok and gtg.vdot(u, u, sqc) == -lam / 3
        for mu in range(fld.d):
            for nu in range(mu + 1, fld.d):
                FT = gtg.tractor_strength(fld, mu, nu)
                gmn = gtg.wedge(fld.hb_inv(GA.gen(mu)), fld.hb_inv(GA.gen(nu)), sq)
                ok = ok and GA.eq(FT, GA.neg(gtg.apply_op(W, gmn)))
                ok = ok and all(max(bl) < 4 for bl in FT)
        ok = ok and _kernel_rank(lambda X: gtg.apply_op(W, X), sq) == 4
        # algebraic step with mu' = 0: D^T_a (s ninf + p n0) has algebraic part -(u . V) A
        A = ALG_A
        for s_, p_ in ((ALG_S, ALG_S * lam / 6), ALG_OFF):
            V = GA.add(GA.scal(s_, ni), GA.scal(p_, n0))
            alg = gtg.comm(gtg.wedge(u, A, sqc), V, sqc)
            ok = ok and GA.eq(alg, GA.scal(-gtg.vdot(u, V, sqc), A))
            ok = ok and ((alg == {}) == (p_ == lam * s_ / 6))
        I = gtg.scale_tractor(lam)
        ok = ok and gtg.vdot(GA.scal(3, I), GA.scal(3, I), sqc) == 9 * lam / 3
    # type N: W(X) = (X . N) N - (X . I N) I N, N = k ^ e2, k = e0 + e1: a Weyl map with k in its kernel
    I4 = gtg.pseudoscalar(sq)
    kv = GA.add(GA.gen(0), GA.gen(1))
    N = gtg.wedge(kv, GA.gen(2), sq)
    IN = GA.mul(I4, N, sq)

    def WN(X):
        return GA.sub(GA.scal(gtg.sp(GA.mul(X, N, sq)), N), GA.scal(gtg.sp(GA.mul(X, IN, sq)), IN))
    ok = ok and all(gtg.ricci(WN, GA.gen(m)) == {} for m in range(4))
    ok = ok and _kernel_rank(WN, sq) == 3
    ok = ok and all(gtg.bdot(WN(gtg.biv(a, b, sq)), kv, sq) == {} for a in range(4) for b in range(a + 1, 4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_gtg_tractor_field_strength_is_minus_weyl"; return _tp_rv
