"""synthesis.clausius-heat-exceeds-created-modes-killing-energy: exact checks.

Windows are finite sets of fermionic modes with fixed Killing weights; in the occupation basis
|n_1 ... n_k> the boost Hamiltonian is diagonal and e^{-beta omega_j} =: q_j is taken rational, so
e^{-beta H_F} is a rational diagonal matrix. Logarithms of rationals are carried as exact coefficient
vectors over the primes 2, 3, 5 (a formal Q-linear combination of ln 2, ln 3, ln 5), compared through
the rational numbers they are logarithms of.

  check_kms_unique_on_window:   for a two-mode window with q = (1/3, 1/5), the KMS equations
                                G rho E_ij G^{-1} = E_ij rho (G = e^{beta H}, all 16 matrix units)
                                have a one-dimensional solution space, spanned by e^{-beta H}.
  check_exchange_leaves_kms:    a resonant number-conserving exchange (rotation with cos 3/5, sin 4/5
                                on the one-particle sector) between a window mode at q = 1/3 (n = 1/4)
                                and an occupied matter mode conserves total occupation (5/4) and leaves
                                the window mode at n = 73/100, so its state is no longer the unique KMS
                                state: Killing energy moved into a fixed window takes it off (R_loc).
  check_created_mode_ledger:    the Gibbs state of a window plus one created mode factorises exactly;
                                per created mode at e^{x} = 3 the entropy is 2 ln 2 - (3/4) ln 3, the
                                Killing energy over T is (1/4) ln 3, and the Clausius heat over T minus
                                the Killing energy over T is ln(4/3) > 0; at zero weight (e^x = 1) the
                                entropy is ln 2, the Killing energy 0, the deficit all of the heat; at a
                                common weight the deficit scales with the net number of created modes.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

PRIMES = (2, 3, 5)


def lg(r):
    """exact prime-log vector of a positive rational r (ln r = sum c_p ln p)."""
    r = F(r)
    out = []
    for p in PRIMES:
        c = 0
        num, den = r.numerator, r.denominator
        while num % p == 0:
            num //= p
            c += 1
        while den % p == 0:
            den //= p
            c -= 1
        out.append(F(c))
        r = F(num, den)
    assert r == 1
    return out


def vadd(u, v):
    return [a + b for a, b in zip(u, v)]


def vscale(c, u):
    return [c * a for a in u]


def exp_of(v):
    """the positive rational whose logarithm is the integer prime-log vector v."""
    out = F(1)
    for c, p in zip(v, PRIMES):
        assert c.denominator == 1
        out *= F(p) ** int(c)
    return out


def diag(xs):
    n = len(xs)
    return [[xs[i] if i == j else F(0) for j in range(n)] for i in range(n)]


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]


def gibbs(qs):
    """occupation basis of len(qs) modes, index bits: bit k = occupation of mode k."""
    dim = 2 ** len(qs)
    w = []
    for idx in range(dim):
        x = F(1)
        for k, q in enumerate(qs):
            if (idx >> k) & 1:
                x *= q
        w.append(x)
    Z = sum(w)
    return [x / Z for x in w], w


def check_kms_unique_on_window():
    premise("singularity.kms-uniqueness-factor")
    premise("synthesis.boundary-mode-first-law-of-entanglement")
    qs = [F(1, 3), F(1, 5)]
    _, w = gibbs(qs)
    G = diag([1 / x for x in w])
    Gi = diag(w)
    dim = 4
    rows = []
    for i in range(dim):
        for j in range(dim):
            E = [[F(1) if (a, b) == (i, j) else F(0) for b in range(dim)] for a in range(dim)]
            # unknown rho: coordinates r[a*dim+b]; equation G rho E Gi - E rho = 0, entrywise
            for a in range(dim):
                for b in range(dim):
                    row = [F(0)] * (dim * dim)
                    for c in range(dim):
                        for d in range(dim):
                            row[c * dim + d] += G[a][c] * matmul(E, Gi)[d][b]
                            row[c * dim + d] -= E[a][c] if d == b else F(0)
                    rows.append(row)
    ker = GA.field_kernel(rows)
    assert len(ker) == 1
    k = ker[0]
    lam = k[0] / w[0]
    for a in range(dim):
        for b in range(dim):
            assert k[a * dim + b] == (lam * w[a] if a == b else F(0))
    assert GA.field_rank(rows) == 15
    return True


def check_exchange_leaves_kms():
    premise("singularity.kms-uniqueness-factor")
    premise("synthesis.boundary-mode-thermal-entropy")
    q = F(1, 3)
    n_w = q / (1 + q)
    assert n_w == F(1, 4)
    # basis |n_w n_m>: index = n_w + 2 n_m ; matter mode occupied with certainty
    rho = diag([F(0), F(0), 1 - n_w, n_w])           # |00>,|10>,|01>,|11>
    c, s = F(3, 5), F(4, 5)
    U = [[F(1), F(0), F(0), F(0)],
         [F(0), c, -s, F(0)],
         [F(0), s, c, F(0)],
         [F(0), F(0), F(0), F(1)]]
    Ut = [[U[j][i] for j in range(4)] for i in range(4)]
    for i in range(4):          # U is orthogonal
        for j in range(4):
            assert sum(U[i][k] * U[j][k] for k in range(4)) == (1 if i == j else 0)
    r2 = matmul(matmul(U, rho), Ut)
    Nw = diag([F(0), F(1), F(0), F(1)])
    Nm = diag([F(0), F(0), F(1), F(1)])
    tr = lambda A: sum(A[i][i] for i in range(4))
    nw2 = tr(matmul(r2, Nw))
    nm2 = tr(matmul(r2, Nm))
    assert nw2 == F(73, 100)
    assert nw2 + nm2 == n_w + 1 == F(5, 4)
    # the window's reduced state: diag(1 - nw2, nw2) (off-diagonal terms cancel in the partial trace)
    red01 = r2[0][1] + r2[2][3]
    assert red01 == 0
    # the unique KMS marginal has n = q/(1+q); the new marginal does not
    assert nw2 != n_w
    assert nw2 / (1 - nw2) != q
    return True


def check_created_mode_ledger():
    premise("synthesis.boundary-mode-thermal-entropy")
    premise("singularity.kms-uniqueness-factor")
    # factorisation: Gibbs state of window (q1, q2) plus created mode q3 = product
    q1, q2, q3 = F(1, 3), F(1, 5), F(1, 3)
    big, _ = gibbs([q1, q2, q3])
    small, _ = gibbs([q1, q2])
    one, _ = gibbs([q3])
    for idx in range(8):
        assert big[idx] == small[idx & 3] * one[idx >> 2]
    # per-mode ledger at e^x = r: n = 1/(r+1), s = ln(1 + 1/r) + n ln r, Killing energy / T = n ln r
    for r, s_expect, e_expect, d_expect in (
            (F(3), [F(2), F(-3, 4), F(0)], [F(0), F(1, 4), F(0)], [F(2), F(-1), F(0)]),
            (F(1), [F(1), F(0), F(0)], [F(0), F(0), F(0)], [F(1), F(0), F(0)])):
        n = 1 / (r + 1)
        s = vadd(lg(1 + 1 / r), vscale(n, lg(r)))
        e = vscale(n, lg(r))
        assert s == s_expect and e == e_expect
        deficit = [a - b for a, b in zip(s, e)]          # (Clausius heat - Killing energy) / T
        assert deficit == d_expect == lg(1 + 1 / r)
        assert exp_of(deficit) > 1                        # strictly positive
        assert (1 - n) / n == r                          # the marginal is the KMS one at weight x
    # common weight, net number dm of created modes: deficit = dm ln(1 + 1/r), zero iff dm = 0
    r = F(3)
    for dm in (F(2), F(-1), F(0)):
        n = 1 / (r + 1)
        dS = vscale(dm, vadd(lg(1 + 1 / r), vscale(n, lg(r))))
        dE = vscale(dm, vscale(n, lg(r)))
        d = [a - b for a, b in zip(dS, dE)]
        assert d == vscale(dm, lg(F(4, 3)))
        assert (d == [F(0)] * 3) == (dm == 0)
    return True


if __name__ == "__main__":
    for f in (check_kms_unique_on_window, check_exchange_leaves_kms, check_created_mode_ledger):
        print(f.__name__, f())
