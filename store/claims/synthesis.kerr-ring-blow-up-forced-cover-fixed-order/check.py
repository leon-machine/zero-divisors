"""synthesis.kerr-ring-blow-up-forced-cover-fixed-order: exact checks.

Signature (+,-,-,-), eta = diag(1,-1,-1,-1). Kerr-Schild data at rational points: c = cos(theta) and
sin(theta) rational (c = (1 - q^2)/(1 + q^2)), cos(phi), sin(phi) rational, x + i y = (r + i a) sin(theta) e^{i phi},
Z = r c; the covector k = (1, -(r x + a y)/(r^2 + a^2), -(r y - a x)/(r^2 + a^2), -Z/r), raised with eta to
k^mu = (1, v) with |v| = 1. On the double cover z = r - i a c. The stored exact inverse metric is
g^{-1} = eta^{-1} + 2 H k k with H = M r^3/(r^4 + a^2 Z^2) = M Re(1/z).

  check_boost_identity:  at several rational points (including near the ring) k is eta-null, l = (1, -v)/2
                         is eta-null with eta(k, l) = 1, the boost B (k -> lam k, l -> l/lam, identity on the
                         complement) preserves eta^{-1}, and B g^{-1} B^T = eta^{-1} + 2 H lam^2 k k exactly;
                         det(eta^{-1} + s k k) = det(eta^{-1}) for every s; H |z|^2 = M r.
  check_forced_weights:  search over all weight vectors in {-1,-1/2,0,1/2,1}^4 for the diagonal rescaling of
                         the null frame (entries multiplied by rho^(a_A + a_B)), with the cometric entries
                         computed as rational functions of s = rho^(1/2) from H = M cos(psi)/rho: exactly
                         one vector, (1/2, -1/2, 0, 0), gives a finite nondegenerate limit keeping the
                         Kerr term.
  check_downstairs_sign: the limit coefficient H |z| has the sign of r = Re z; the deck map z -> -z,
                         (r, c) -> (-r, -c), fixes the base point (x^2 + y^2, Z) and reverses the sign of
                         H |z|^2, so the downstairs limit coefficient 2 M cos(arg(w)/2) takes opposite values
                         at the two ends of a loop round the ring.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

ETA = [1, -1, -1, -1]
POINTS = [  # (a, r, q, cos phi, sin phi, M)
    (F(1), F(1, 7), F(1, 3), F(3, 5), F(4, 5), F(2)),
    (F(2), F(-1, 5), F(2, 5), F(5, 13), F(12, 13), F(3)),
    (F(1, 2), F(1, 100), F(1, 9), F(8, 17), F(15, 17), F(1)),
    (F(3), F(-2, 3), F(1, 2), F(-3, 5), F(4, 5), F(5)),
]


def ks_data(a, r, q, cphi, sphi):
    c = (1 - q * q) / (1 + q * q)
    s = 2 * q / (1 + q * q)
    x = s * (r * cphi - a * sphi)
    y = s * (r * sphi + a * cphi)
    Z = r * c
    den = r * r + a * a
    k_low = [F(1), -(r * x + a * y) / den, -(r * y - a * x) / den, -Z / r]
    k_up = [ETA[i] * k_low[i] for i in range(4)]
    return c, x, y, Z, k_up


def eta_ip(u, w):
    return sum(ETA[i] * u[i] * w[i] for i in range(4))


def outer(u, w):
    return [[u[i] * w[j] for j in range(4)] for i in range(4)]


def madd(A, B, s=F(1)):
    return [[A[i][j] + s * B[i][j] for j in range(4)] for i in range(4)]


def transpose(A):
    return [[A[j][i] for j in range(4)] for i in range(4)]


def boost(k, l, lam):
    """B v = v + (lam - 1) eta(v, l) k + (1/lam - 1) eta(v, k) l, as a matrix acting on vectors."""
    B = [[F(1) if i == j else F(0) for j in range(4)] for i in range(4)]
    for j in range(4):
        e = [F(1) if i == j else F(0) for i in range(4)]
        cl, ck = eta_ip(e, l), eta_ip(e, k)
        for i in range(4):
            B[i][j] += (lam - 1) * cl * k[i] + (F(1) / lam - 1) * ck * l[i]
    return B


def det4(A):
    M = [[GA.RF.const(A[i][j]) for j in range(4)] for i in range(4)]
    return GA.rf_mat_det(M).eval(0)


def check_boost_identity():
    premise("interior.unipotency-across-kerr-family")
    premise("interior.imported-kerr-schild-form-kerr-gauge")
    premise("synthesis.kerr-ring-double-cover-data")
    eta_inv = [[F(ETA[i]) if i == j else F(0) for j in range(4)] for i in range(4)]
    for (a, r, q, cphi, sphi, M) in POINTS:
        c, x, y, Z, k = ks_data(a, r, q, cphi, sphi)
        assert eta_ip(k, k) == 0
        l = [F(1, 2)] + [-k[i] * F(1, 2) for i in range(1, 4)]
        assert eta_ip(l, l) == 0 and eta_ip(k, l) == 1
        H = M * r ** 3 / (r ** 4 + a * a * Z * Z)
        zz = r * r + a * a * c * c                       # |z|^2
        assert H * zz == M * r
        ginv = madd(eta_inv, outer(k, k), 2 * H)
        for lam in (F(1, 2), F(3), F(2, 7)):
            B = boost(k, l, lam)
            assert GA.mat_mul(GA.mat_mul(B, eta_inv), transpose(B)) == eta_inv
            lhs = GA.mat_mul(GA.mat_mul(B, ginv), transpose(B))
            assert lhs == madd(eta_inv, outer(k, k), 2 * H * lam * lam)
        for s in (F(5), F(-7, 3)):
            assert det4(madd(eta_inv, outer(k, k), s)) == det4(eta_inv) == -1
    return True


def _ord_lead(r):
    """order at s = 0 and leading coefficient of a nonzero rational function of s."""
    def low(p):
        return next(i for i, x in enumerate(p) if x != 0)
    n, d = low(r.num), low(r.den)
    return n - d, r.num[n] / r.den[d]


def check_forced_weights():
    premise("synthesis.kerr-ring-double-cover-data")
    premise("interior.unipotency-across-kerr-family")
    M, cpsi = F(2), F(3, 5)
    s = GA.RF.var()                                   # s = rho^(1/2)
    one = GA.RF.const(1)
    H = GA.RF.const(M * cpsi) / (s * s)               # H = M cos(psi) / rho
    # cometric components in the null frame (k, l, e1, e2): eta^-1 + 2 H k k
    G = [[GA.RF.const(2) * H, one, None, None], [one, None, None, None],
         [None, None, GA.RF.const(-1), None], [None, None, None, GA.RF.const(-1)]]
    halves = [F(-1), F(-1, 2), F(0), F(1, 2), F(1)]
    found = []
    for ak in halves:
        for al in halves:
            for a1 in halves:
                for a2 in halves:
                    w = [ak, al, a1, a2]
                    lim = [[F(0)] * 4 for _ in range(4)]
                    ok = True
                    for A in range(4):
                        for B in range(4):
                            if G[A][B] is None:
                                continue
                            e = 2 * (w[A] + w[B])             # rho^(a_A + a_B) = s^(2(a_A + a_B))
                            pw = one
                            for _ in range(abs(int(e))):
                                pw = pw * s
                            ent = G[A][B] * pw if e >= 0 else G[A][B] / pw
                            o, c = _ord_lead(ent)
                            if o < 0:
                                ok = False
                            elif o == 0:
                                lim[A][B] = c
                    if ok and lim[0][0] != 0 and GA.mat_rank(lim) == 4:
                        found.append(w)
    assert found == [[F(1, 2), F(-1, 2), F(0), F(0)]]
    return True


def check_downstairs_sign():
    premise("synthesis.kerr-ring-double-cover-data")
    for (a, r, q, cphi, sphi, M) in POINTS:
        c = (1 - q * q) / (1 + q * q)
        rho2 = (r * r + a * a) * (1 - c * c)
        Z = r * c
        rho2_d = ((-r) * (-r) + a * a) * (1 - c * c)
        Z_d = (-r) * (-c)
        assert rho2_d == rho2 and Z_d == Z               # same base point
        zz = r * r + a * a * c * c
        Hz2 = M * r ** 3 / (r ** 4 + a * a * Z * Z) * zz
        Hz2_d = M * (-r) ** 3 / ((-r) ** 4 + a * a * Z_d * Z_d) * zz
        assert Hz2 == M * r
        assert Hz2_d == -Hz2 != 0                        # coefficient changes sign between the sheets
    return True


if __name__ == "__main__":
    for f in (check_boost_identity, check_forced_weights, check_downstairs_sign):
        print(f.__name__, f())
