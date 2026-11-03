"""singularity.rate-discharge-hypothesis-iii: exact checks.

(1) The gluing condition of (R) at period p on a diagonal marginal diag(1 - n, n), e^{p omega} n = 1 - n,
    written with x = e^{-p omega}: n = x (1 - n). As a linear equation in n with coefficient 1 + x it has the
    unique solution n = x/(1 + x) = (e^{p omega} + 1)^{-1}, an identity of rational functions in x; for every
    x > 0 sampled, 0 < n < 1, and the boundary values n = 0, 1/2, 1 fail it. The marginal it fixes,
    diag(1 - n, n) = diag(1, x)/(1 + x), is the unique solution of the single-mode KMS system for
    e^{-pK} = diag(1, x) (kernel computed): the Gibbs state of K_k at beta = p.
(2) Faithful, hence cyclic and separating: at x = 9/16 (n = 9/25, sqrt(1 - n) = 4/5, sqrt(n) = 3/5) the
    purification Omega = (4/5)|00> + (3/5)|11> gives an injective map A -> (A (x) 1) Omega (separating) whose
    image is all of C^4 (cyclic), both by rank 4; at the unfaithful n = 0 the rank drops to 2.
(3) The temperature: in GTG (PG gauge, GTG-sign Omega(e_t) = (M/r^2) sigma_r, sigma_r = e_r e_t) the
    Killing field K = hb^{-1}(e_t) satisfies (K . D)K = kappa K at r = 2M with kappa = 1/(4M), for four
    masses; beta = 2 pi/kappa = 8 pi M and T = kappa/(2 pi) = 1/(8 pi M) (pi cancelled: beta kappa/pi = 2,
    T beta = 1).
(4) Same beta at every mode, with no joint condition: for weights omega_k = 1, 2, 1/2 at one period
    (x_k = y^omega_k, y = 4/9), each glued marginal is Gibbs at the same beta (n_k/(1 - n_k) = y^omega_k), and
    an even correlated joint state with exactly those marginals (diagonal, not a product) exists.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise

S13 = GA.sig(1, 3)
ET, ER = GA.gen(0), GA.gen(1)
SIG = GA.mul(ER, ET, S13)
XS = [F(9, 16), F(1, 3), F(4), F(7, 2), F(1, 100)]


def check_gluing_fixes_fermi_dirac_gibbs_marginal():
    premise("singularity.r-regularity-fixed-locus")
    premise("singularity.ascended-marginals-are-diagonal")
    premise("singularity.descended-form-state-independent")
    premise("singularity.modular-structure-completed-pair")
    x = GA.RF.var()
    one = GA.RF.const(1)
    n = x / (one + x)
    ok = n.eqrf(x * (one - n)) and (one / n - one).eqrf(one / x)     # e^{p omega} n = 1 - n
    for xv in XS:
        nv = xv / (1 + xv)
        ok = ok and nv == n.eval(xv) and 0 < nv < 1
        # linear in n with nonzero coefficient 1 + x: unique solution
        ok = ok and (1 + xv) != 0 and nv == xv / (1 + xv)
        for m in (F(0), F(1, 2), F(1)):
            ok = ok and (xv * (1 - m) == m) == (m == nv)
        # KMS for diag(1, x): unknown density r (r00, r01, r10, r11), omega(E_ab) = r_ba
        w = [F(1), xv]
        rows = []
        for s1 in range(2):
            for t1 in range(2):
                for s2 in range(2):
                    for t2 in range(2):
                        c = [F(0)] * 4
                        if t1 == s2:
                            c[2 * t2 + s1] += 1
                        if t2 == s1:
                            c[2 * t1 + s2] -= w[s1] / w[t1]
                        if any(c):
                            rows.append(c)
        ker = GA.field_kernel(rows)
        ok = ok and len(ker) == 1
        k = ker[0]
        t = k[0] + k[3]
        ok = ok and [v / t for v in k] == [1 - nv, F(0), F(0), nv]
    _tp_rv = (ok); assert _tp_rv is not False, "check_gluing_fixes_fermi_dirac_gibbs_marginal"; return _tp_rv


def check_faithful_marginal_cyclic_separating():
    ok = True
    for amps, want in (((F(4, 5), F(3, 5)), 4), ((F(1), F(0)), 2)):
        a0, a1 = amps
        ok = ok and a0 * a0 + a1 * a1 == 1
        Omega = [a0, F(0), F(0), a1]                       # basis |ij> at index 2 i + j
        cols = []
        for a in range(2):
            for b in range(2):
                # (E_ab (x) 1) Omega
                v = [F(0)] * 4
                for j in range(2):
                    v[2 * a + j] += Omega[2 * b + j]
                cols.append(v)
        ok = ok and GA.rank_of_vectors(cols) == want
    ok = ok and F(9, 25) == F(3, 5) ** 2 and F(16, 25) == F(4, 5) ** 2 and F(9, 16) == F(9, 25) / F(16, 25)
    _tp_rv = (ok); assert _tp_rv is not False, "check_faithful_marginal_cyclic_separating"; return _tp_rv


def check_hawking_temperature_from_the_connection():
    premise("singularity.computed")
    premise("singularity.plane-rate")
    ok = True
    for M in (F(1), F(1, 2), F(3), F(7, 4)):
        beta_pg = F(1)                                     # horizon: beta^2 = 2M/r = 1
        r = 2 * M
        K = GA.add(ET, GA.scal(beta_pg, ER))               # hb^{-1}(e_t)
        hbK = GA.sub(K, GA.scal(beta_pg * GA.dot(K, ET, S13), ER))
        ok = ok and GA.eq(hbK, ET) and GA.dot(K, K, S13) == 0
        Om = GA.scal(M / (r * r), SIG)                     # Omega(e_t)
        KDK = GA.scal(F(1, 2), GA.sub(GA.mul(Om, K, S13), GA.mul(K, Om, S13)))
        kappa = F(1) / (4 * M)
        ok = ok and GA.eq(KDK, GA.scal(kappa, K))
        beta_over_pi = 2 / kappa
        T_times_pi = kappa / 2
        ok = ok and beta_over_pi == 8 * M and T_times_pi * 8 * M == 1 and T_times_pi * beta_over_pi == 1
    _tp_rv = (ok); assert _tp_rv is not False, "check_hawking_temperature_from_the_connection"; return _tp_rv


def check_one_beta_at_every_mode():
    premise("singularity.p-univalence")
    y = F(4, 9)
    xk = {F(1): y, F(2): y * y, F(1, 2): F(2, 3)}
    ok = xk[F(1, 2)] ** 2 == y
    ns = {}
    for om, x in xk.items():
        n = x / (1 + x)
        ns[om] = n
        ok = ok and n / (1 - n) == x and x * (1 - n) == n
    # a correlated joint state on modes (1, 2) with these marginals: shift eps between diagonal entries
    n1, n2 = ns[F(1)], ns[F(2)]
    eps = F(1, 200)
    joint = [(1 - n1) * (1 - n2) + eps, (1 - n1) * n2 - eps, n1 * (1 - n2) - eps, n1 * n2 + eps]
    ok = ok and all(p > 0 for p in joint) and sum(joint) == 1
    ok = ok and joint[2] + joint[3] == n1 and joint[1] + joint[3] == n2
    ok = ok and joint[3] != n1 * n2
    _tp_rv = (ok); assert _tp_rv is not False, "check_one_beta_at_every_mode"; return _tp_rv
