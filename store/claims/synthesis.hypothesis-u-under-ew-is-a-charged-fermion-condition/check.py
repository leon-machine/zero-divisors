"""synthesis.hypothesis-u-under-ew-is-a-charged-fermion-condition: exact checks.

Family matrices are 3x3 over Q (complex entries as pairs of Fractions where needed).
(a) Consistency re-derivation of the stored elimination, Clebsch structure with (EW): for rational symmetric 10 coupling Y and 126 coupling f, with
    w_u fixed by 4 w_u f_33 = (M_u)_33 and M_u rank one along e3, M_nu = m_t (e3 e3^T - fhat),
    fhat = (M_d - M_e)/(M_d - M_e)_33, and (M_nu)_33 = 0.
(b) Rank-one fhat = w w^T, w = (0, eps, 1): N = fhat - e3 e3^T has trace eps^2 and determinant
    -eps^2 on its 2-3 block (a polynomial identity, checked at more points than its degree), so its
    nonzero eigenvalues solve l^2 - eps^2 l - eps^2 = 0. eps^2 = 1/2 gives eigenvalues 1, -1/2
    (top reading); eps^2 = r^2/(1+r) gives r and -r/(1+r) (bottom reading, r = m_b/m_t);
    eps = 0 gives N = 0.
(c) Diagonal order: N = diag(d1/d3, d2/d3, 0) with d_k = m_d,k u_k - m_e,k v_k, |u_k| = |v_k| = 1.
    At the M_I masses of the stored fits, (m_mu - m_s)/(m_b + m_tau) > m_b/m_t and
    max(m_d + m_e, m_s + m_mu)/(m_tau - m_b) < 1, so neither reading is met at any phases;
    sampled rational phases (Pythagorean points) confirm both bounds.
(d) Rank-one witness: fhat = e3 e3^T + mu e2 e2^T, built through the Clebsch construction, gives
    M_nu = -mu m_t e2 e2^T (rank one) at mu = 1 and mu = m_b/m_t.
"""
from fractions import Fraction as F
import GA
from GA import mat_mul
from tp_premise import premise

# masses at M_I in GeV used by the stored coupling sets (T12, obs:anglefits)
MT, MB, MTAU = F(9245, 100), F(13651, 10000), F(1764, 1000)
MS, MMU = F(261, 10000), F(1037, 10000)
MD, ME = F(130, 100000), F(502, 1000000)


def e33():
    return [[F(0)] * 3 for _ in range(2)] + [[F(0), F(0), F(1)]]


def madd(A, B, c=F(1)):
    return [[A[i][j] + c * B[i][j] for j in range(3)] for i in range(3)]


def mscal(c, A):
    return [[c * A[i][j] for j in range(3)] for i in range(3)]


def outer(u, v):
    return [[u[i] * v[j] for j in range(3)] for i in range(3)]


def check_ew_elimination_rank_one_up():
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    premise("standard-model.premise-ew-equal-weight")
    premise("standard-model.hyp-s-slot-statistics")
    samples = [
        ([[F(1, 3), F(2), F(-1)], [F(2), F(5), F(1, 7)], [F(-1), F(1, 7), F(4)]], F(3, 2), F(-2, 5)),
        ([[F(-2), F(1, 2), F(0)], [F(1, 2), F(1, 9), F(3)], [F(0), F(3), F(7, 3)]], F(-5, 4), F(7, 3)),
    ]
    for idx, (f, wd, zscale) in enumerate(samples):
        mt = MT
        Mu = mscal(mt, e33())                               # leading-order rank one
        wu = mt / (4 * f[2][2])                             # (EW): 4 w_u f_33 = m_t
        Y = madd(Mu, f, -wu)                                # M_u = Y + w_u f
        Mnu = madd(Y, f, -3 * wu)                           # M_nu = Y - 3 w_u f
        Z = [[zscale * (i + 2 * j + 1) * (j + 2 * i + 1) for j in range(3)] for i in range(3)]
        Md, Me = madd(Z, f, wd), madd(Z, f, -3 * wd)
        D = madd(Md, Me, F(-1))
        assert D == mscal(4 * wd, f)
        fhat = mscal(F(1) / D[2][2], D)
        assert Mnu == mscal(mt, madd(e33(), fhat, F(-1)))
        assert Mnu[2][2] == 0
        if idx == 0:                                        # pinned values of the first sample
            assert (Mnu[1][2], Mnu[0][0], Mnu[1][1]) == (F(-1849, 560), F(-1849, 240), F(-1849, 16))


def block_char(N):
    tr = N[1][1] + N[2][2]
    det = N[1][1] * N[2][2] - N[1][2] * N[2][1]
    return tr, det


def check_rank_one_readings():
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    premise("standard-model.premise-ew-equal-weight")
    for eps in [F(0), F(1), F(-2), F(1, 3), F(5, 7)]:
        w = [F(0), eps, F(1)]
        N = madd(outer(w, w), e33(), F(-1))
        assert all(N[0][j] == 0 and N[j][0] == 0 for j in range(3))
        tr, det = block_char(N)
        assert tr == eps * eps and det == -eps * eps
        if eps == 0:
            assert N == [[F(0)] * 3 for _ in range(3)]      # aligned: M_nu = 0
    def roots_ok(e2, big, small):
        # big and small are the roots of l^2 - e2 l - e2 and |small| < |big|
        assert big + small == e2 and big * small == -e2 and abs(small) < abs(big)
    roots_ok(F(1, 2), F(1), F(-1, 2))                        # top reading: |l| = 1
    r = MB / MT
    roots_ok(r * r / (1 + r), r, -r / (1 + r))               # bottom reading: |l| = r
    assert r * r / (1 + r) < F(1, 4000)


def check_diagonal_order_excludes_both_readings():
    premise("standard-model.fits-record-level")
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    premise("standard-model.premise-ew-equal-weight")
    r = MB / MT
    low = (MMU - MS) / (MB + MTAU)
    assert low > r                                            # bottom reading out
    high = max(MD + ME, MS + MMU) / (MTAU - MB)
    assert high < 1                                           # top reading out
    assert low == F(776, 31291) and low > F(247, 10000) and r < F(148, 10000) and high < F(326, 1000)
    phases = [(F(1), F(0)), (F(3, 5), F(4, 5)), (F(-5, 13), F(12, 13)), (F(0), F(-1)),
              (F(-8, 17), F(-15, 17)), (F(-1), F(0))]
    def absq(z):
        return z[0] * z[0] + z[1] * z[1]
    def diff(a, u, b, v):
        return (a * u[0] - b * v[0], a * u[1] - b * v[1])
    for u2 in phases:
        for v2 in phases:
            d2 = absq(diff(MS, u2, MMU, v2))
            for u3 in phases:
                for v3 in phases:
                    d3 = absq(diff(MB, u3, MTAU, v3))
                    assert d2 >= low * low * d3                # |d2/d3| >= low > r
                    assert d2 <= high * high * d3              # |d2/d3| <= high < 1



def check_rank_one_witness():
    premise("standard-model.neutrino-dirac-matrix-charged-fermions")
    premise("standard-model.premise-ew-equal-weight")
    mt = MT
    for mu in (F(1), MB / MT):
        fhat = madd(e33(), [[F(0)] * 3, [F(0), mu, F(0)], [F(0)] * 3])
        f = mscal(F(5, 2), fhat)                            # any 126 coupling proportional to fhat
        Mu = mscal(mt, e33())
        wu = mt / (4 * f[2][2])
        Y = madd(Mu, f, -wu)
        Mnu = madd(Y, f, -3 * wu)
        assert Mnu[2][2] == 0
        assert Mnu == [[F(0)] * 3, [F(0), -mu * mt, F(0)], [F(0)] * 3]     # rank one, sigma1 = mu m_t
    assert MB / MT == F(13651, 924500)


EXPORTS = {}
