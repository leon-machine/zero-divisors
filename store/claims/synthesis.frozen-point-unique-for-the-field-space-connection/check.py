"""synthesis.frozen-point-unique-for-the-field-space-connection: exact checks.

A_rho = Omega - u ^ E, u = nInf - rho nO, E = hb^{-1}(a), in Cl(2,4) with nO.nInf = 1.
  (1) the pointwise action of A_rho on the three parts of a tractor, and the norms (clause (i));
  (2) the field strength of A_rho computed from fields (jets, lib/gtg.py) on de Sitter, six isotropic fluid
      instants and Schwarzschild in Kerr-Schild form, against -(calR - 2 rho id); kernel dimensions
      (clauses (i), (iii), (iv));
  (3) the torsion counter-model of clause (v);
  (4) the reversed-signature Remark.
The derivative step and the passage from a neighbourhood to the connected region are the proof's.
"""
from fractions import Fraction as F

import GA
import gtg
from gtg import S24, comm, m_add, m_d, m_neg, m_scal, m_sub, m_val
from tp_premise import premise

S42 = tuple(-s for s in S24)
N0, NINF = gtg.null_pair(S24)
e = GA.gen
RHOS = [F(0), F(1, 3), F(-5, 2), F(7)]


def vec(*c):
    return {(i,): F(x) for i, x in enumerate(c) if x}


def lorentz_biv(cs):
    out, k = {}, 0
    for i in range(4):
        for j in range(i + 1, 4):
            if cs[k]:
                out = GA.add(out, GA.scal(cs[k], GA.mul(e(i), e(j), S24)))
            k += 1
    return out


def u_of(rho):
    return GA.sub(NINF, GA.scal(rho, N0))


def i_of(rho):
    return GA.add(NINF, GA.scal(rho, N0))


def a_rho(om, frame, rho, sq=S24):
    return GA.sub(om, comm(u_of(rho), frame, sq))      # u ^ E = u x E since u . E = 0


OM = lorentz_biv([F(3, 7), F(-2), F(5, 3), F(1, 4), F(-6, 5), F(2)])
AVEC = vec(2, F(-1, 3), F(5, 2), 7)
BVEC = vec(F(-4, 9), 1, 0, F(3, 2))
MU = vec(F(1, 5), 3, F(-2), F(7, 3))


def check_pointwise_action_of_the_field_space_connection():
    premise("synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation")
    assert GA.dot(N0, NINF, S24) == 1
    for rho in RHOS:
        u, big_i = u_of(rho), i_of(rho)
        lhs = comm(comm(u, AVEC, S24), comm(u, BVEC, S24), S24)
        assert GA.eq(lhs, GA.scal(2 * rho, comm(AVEC, BVEC, S24)))
        a = a_rho(OM, AVEC, rho)
        assert GA.is_zero(comm(a, big_i, S24))
        sgm, tau = F(5, 3), F(-2, 7)
        w = GA.add(GA.scal(sgm, NINF), GA.scal(tau, N0))
        assert GA.eq(comm(a, w, S24), GA.scal(tau - rho * sgm, AVEC))
        expect = GA.sub(comm(OM, MU, S24), GA.scal(GA.dot(AVEC, MU, S24), u))
        assert GA.eq(comm(a, MU, S24), expect)
        assert GA.dot(big_i, big_i, S24) == 2 * rho and GA.dot(u, u, S24) == -2 * rho
        assert GA.dot(u, big_i, S24) == 0
        assert GA.dot(N0, GA.scal(F(9, 4), big_i), S24) == F(9, 4)
    return True


def fs_strength_frame(fld, rho):
    """F(hb(gamma_a) ^ hb(gamma_b)) of A_rho on the frame planes, computed from the field's jets."""
    u = u_of(rho)
    conn = [m_sub(fld.Om[m], comm(u, fld.g[m], S24)) for m in range(4)]
    raw = {}
    for m in range(4):
        for n in range(m + 1, 4):
            raw[(m, n)] = m_val(m_add(m_d(conn[n], m), m_neg(m_d(conn[m], n)), comm(conn[m], conn[n], S24)))
    hi = fld.hb_matrix()
    out = {}
    for a in range(4):
        for b in range(a + 1, 4):
            acc = {}
            for (m, n), fm in raw.items():
                c = hi[m][a] * hi[n][b] - hi[n][a] * hi[m][b]
                if c and fm:
                    acc = m_add(acc, m_scal(c, fm))
            out[(a, b)] = acc
    return out


def kernel_dim(op, n):
    """dimension of {v among the first n generators' span : op(X) x v = 0 for all frame planes X}."""
    blades = GA.all_blades(6)
    rows = []
    for i in range(n):
        col = []
        for k in sorted(op):
            col += GA.basis_vector_of(comm(op[k], e(i), S24), blades)
        rows.append(col)
    return n - GA.rank_of_vectors(rows)


def matches_lorentz_block(fld, rho):
    fop = fs_strength_frame(fld, rho)
    curv = {k: m_val(v) for k, v in fld.curvature().items()}
    ok = True
    for (a, b), fv in fop.items():
        plane = GA.mul(e(a), e(b), S24)
        assert GA.eq(fv, m_neg(m_sub(curv[(a, b)], m_scal(2 * rho, plane))))
    return ok, fop, curv


def check_field_strength_and_kernels_on_de_sitter_fluid_and_schwarzschild_fields():
    premise("synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation")
    premise("synthesis.frozen-point-unique-where-weyl-has-no-kernel")
    # de Sitter, flat slicing, H = 1/2: Lambda = 3/4, rho = 1/8; F vanishes and all six directions are flat
    hub = F(1, 2)
    ds = gtg.de_sitter_flat(hub, F(1), order=2)
    ok, fds, _ = matches_lorentz_block(ds, hub * hub / 2)
    assert ok and all(GA.is_zero(v) for v in fds.values()) and kernel_dim(fds, 6) == 6
    ok2, fds2, _ = matches_lorentz_block(ds, F(1, 3))
    assert ok2 and kernel_dim(fds2, 4) == 0
    assert fds2[(0, 1)] == {(0, 1): F(5, 12)} and fds2[(2, 3)] == {(2, 3): F(5, 12)}     # 2 rho - Lambda/3
    # isotropic fluid instants from the two Friedmann equations: H = 1, Lambda = 3/2, kappa rho_m = 3/2
    h0, lam = F(1), F(3, 2)
    krho = 3 * h0 ** 2 - lam
    # (w, kernel dimension, pinned factor of L on time-space bivectors); on space-space bivectors it is -1/2
    for w, want, ts in ((F(0), 0, F(1, 4)), (F(1, 3), 0, F(1, 2)), (F(1), 0, F(1)), (F(-1, 3), 1, F(0)),
                        (F(-1), 0, F(-1, 2)), (F(-2, 3), 0, F(-1, 4))):
        addot = -krho * (1 + 3 * w) / 6 + lam / 3
        okw, fop, _ = matches_lorentz_block(gtg.flrw_flat(1, h0, addot), lam / 6)
        assert okw and kernel_dim(fop, 4) == want and kernel_dim(fop, 6) == 2 + want
        assert fop[(0, 1)] == ({(0, 1): ts} if ts else {}) and fop[(2, 3)] == {(2, 3): F(-1, 2)}
    # Schwarzschild, Kerr-Schild form, M = 1 at a rational point with r = 13, rho = 0: F = -Weyl, no kernel
    sch = gtg.schwarzschild_ks(F(1), (F(0), F(3), F(4), F(12)), order=2)
    oks, fsch, curv = matches_lorentz_block(sch, F(0))
    weyl = {k: m_neg(m_val(v)) for k, v in gtg.weyl_op(curv).items()}
    assert oks and all(GA.eq(fsch[k], weyl[k]) for k in fsch)
    assert kernel_dim(fsch, 4) == 0 and kernel_dim(fsch, 6) == 2
    assert fsch[(0, 1)][(0, 1)] == F(142, 371293) and fsch[(2, 3)][(1, 3)] == F(36, 371293)
    return True


def check_torsion_counter_model():
    premise("synthesis.frozen-point-field-space-is-the-gtg-pair-and-its-omega-equation-is-the-torsion-equation")
    h0, lam = F(1), F(3, 2)
    krho = 3 * h0 ** 2 - lam
    rho = lam / 6
    lop = fs_strength_frame(gtg.flrw_flat(1, h0, -krho / 6 + lam / 3), rho)     # dust: no kernel vector
    mu0 = vec(1, F(1, 2), F(-1, 3), 2)
    sgm, c = F(2), F(1)
    v0 = GA.add(mu0, GA.scal(sgm, NINF), GA.scal(c + rho * sgm, N0))
    assert kernel_dim(lop, 4) == 0
    # pinned values of the dust instant: L = 1/4 on time-space and -1/2 on space-space bivectors
    assert rho == F(1, 4)
    assert GA.eq(lop[(0, 1)], GA.scal(F(1, 4), GA.mul(e(0), e(1), S24)))
    assert GA.eq(lop[(2, 3)], GA.scal(F(-1, 2), GA.mul(e(2), e(3), S24)))
    assert GA.eq(comm(lop[(1, 3)], mu0, S24), vec(0, 1, 0, F(-1, 4)))
    assert GA.dot(N0, v0, S24) == 2 and GA.dot(NINF, v0, S24) == F(3, 2)
    assert GA.dot(u_of(rho), v0, S24) == 1
    for lk in lop.values():
        tk = GA.scal(F(-1) / c, comm(lk, mu0, S24))                             # T = -(L . mu0)/c
        fk = GA.sub(lk, comm(u_of(rho), tk, S24))                                # F = L - u ^ T
        assert GA.is_zero(comm(fk, v0, S24))
        assert not GA.is_zero(comm(lk, v0, S24))                            # without T, V0 is not in the kernel
    return True


def check_reversed_signature_reading():
    bgen = GA.add(OM, GA.scal(F(2, 3), GA.mul(e(1), e(4), S24)), GA.scal(F(-5), GA.mul(e(4), e(5), S24)),
                  GA.scal(F(1, 7), GA.mul(e(0), e(5), S24)))
    vgen = GA.add(vec(1, 2, -3, F(1, 2)), GA.scal(F(4), e(4)), GA.scal(F(-1, 3), e(5)))
    assert GA.eq(comm(bgen, vgen, S42), GA.neg(comm(bgen, vgen, S24)))
    rho = F(3, 5)
    a = a_rho(OM, AVEC, rho)
    # pinned value of the covariant derivative's algebraic part on the sample tractor
    pinned = GA.add(vec(F(-207, 70), F(167, 1260), F(89, 12), F(13, 2)), GA.scal(F(-14, 3), e(4)),
                    GA.scal(F(26, 3), e(5)))
    assert GA.eq(comm(a, vgen, S24), pinned)
    # keep X = nO, reverse nInf: rho' = -rho, Omega' = -Omega
    ninf_b = GA.neg(NINF)
    u_b = GA.sub(ninf_b, GA.scal(-rho, N0))
    a_b = GA.sub(GA.neg(OM), comm(u_b, AVEC, S42))
    i_b = GA.add(ninf_b, GA.scal(-rho, N0))
    assert GA.dot(N0, ninf_b, S42) == 1
    assert GA.eq(a_b, GA.neg(a)) and GA.eq(comm(a_b, vgen, S42), comm(a, vgen, S24))
    assert GA.eq(i_b, GA.neg(i_of(rho))) and GA.dot(N0, i_b, S42) == 1
    assert GA.dot(i_b, i_b, S42) == -2 * rho == F(-6, 5)
    # keep nInf, reverse nO: u and I_rho unchanged as vectors; the form is Ad(I4) A_rho, not A_rho
    n0_a = GA.neg(N0)
    u_a = GA.sub(NINF, GA.scal(-rho, n0_a))
    assert GA.dot(n0_a, NINF, S42) == 1 and GA.eq(u_a, u_of(rho))
    assert GA.eq(GA.add(NINF, GA.scal(-rho, n0_a)), i_of(rho))
    a_a = GA.sub(GA.neg(OM), comm(u_a, AVEC, S42))
    flipped = GA.add(OM, comm(u_of(rho), AVEC, S24))                             # A_rho with E -> -E
    assert not GA.eq(comm(a_a, vgen, S42), comm(a, vgen, S24))
    assert GA.eq(comm(a_a, vgen, S42), comm(flipped, vgen, S24))
    i4 = GA.mul(GA.mul(e(0), e(1), S24), GA.mul(e(2), e(3), S24), S24)
    conj = GA.mul(GA.mul(i4, a, S24), GA.neg(i4), S24)
    assert GA.eq(conj, flipped)
    assert GA.eq(GA.mul(GA.mul(i4, i_of(rho), S24), GA.neg(i4), S24), i_of(rho))
    return True
