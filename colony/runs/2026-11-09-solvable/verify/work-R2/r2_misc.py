"""R2 own-route recomputations for the thickness, residue, Georgi-Jarlskog and D-term proposals (exact Fractions).

Thickness: 8/(3 pi) bracketed by a Machin enclosure of pi; the licensed charge branch T = 1 + 4/eps and the eps that
  reproduces the observed 5.364.
Residue: p(16) and partitions of 16 into 8 parts by a generating-function recursion (not by enumeration);
  s(pi) and S_0 by rational exponential enclosures.
GJ: the lepton/quark ratio from the stored GJ entries; the three models; the bottom reading; h_mu on a random
  rational model with a 120.
D-term: the critical level by differentiating V along the lift family by hand (closed form), compared at both frames.
"""
import random
import sys
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA  # noqa: E402,F401  (house rule: checks import GA)

ok_all = True


def rep(msg, ok):
    global ok_all
    ok_all = ok_all and ok
    print(("OK  " if ok else "BAD ") + msg)


# ---------------- pi and exp enclosures
def atan_b(x, terms):
    s = sum(F((-1) ** k) * x ** (2 * k + 1) / (2 * k + 1) for k in range(terms))
    t = x ** (2 * terms + 1) / (2 * terms + 1)
    return s - t, s + t


a, b = atan_b(F(1, 5), 10), atan_b(F(1, 239), 4)
PI = (16 * a[0] - 4 * b[1], 16 * a[1] - 4 * b[0])


def exp_b(x, terms=40):          # x >= 0 rational: partial sum < e^x < partial sum + 2 * next term (x small enough)
    s, t = F(0), F(1)
    for k in range(terms):
        s += t
        t = t * x / (k + 1)
    return s, s + 2 * t


# ---------------- thickness
f5 = (F(8, 3) / PI[1], F(8, 3) / PI[0])
rep(f"8/(3 pi) in ({float(f5[0]):.6f}, {float(f5[1]):.6f}) within (5/6, 8/9)", F(5, 6) < f5[0] and f5[1] < F(8, 9))
lam = (F(3, 8) * PI[0], F(3, 8) * PI[1])
rep(f"licensed lambda = 3 pi/8 in ({float(lam[0]):.6f},{float(lam[1]):.6f}) within (9/8, 6/5)", F(9, 8) < lam[0] and lam[1] < F(6, 5))
T_obs = F(5364, 1000)
eps = 4 / (T_obs - 1)
rep(f"charge branch T = 1 + 4/eps equals the observed 5.364 at eps = {float(eps):.4f} (0 < eps <= 1)", 0 < eps <= 1)
print(f"    and equal filling (share 1 for all odd towers) gives T = 5, {(F(5364,1000)-5)/F(65,1000):.1f} sigma below 5.364 +- 0.065")


# ---------------- residue
def partitions_count(n, k=None):
    # p(n) and p(n, exactly k parts) by the recursion p(n, k) = p(n - 1, k - 1) + p(n - k, k)
    memo = {}

    def pk(n, k):
        if n == 0 and k == 0:
            return 1
        if n <= 0 or k <= 0:
            return 0
        if (n, k) not in memo:
            memo[(n, k)] = pk(n - 1, k - 1) + pk(n - k, k)
        return memo[(n, k)]
    return sum(pk(n, j) for j in range(1, n + 1)) if k is None else pk(n, k)


rep(f"p(16) = {partitions_count(16)}, into 8 parts = {partitions_count(16, 8)}", partitions_count(16) == 231 and partitions_count(16, 8) == 22)
# s(x) = ln(1 + e^-x) + x/(e^x + 1) < e^-x + x e^-x ; e^pi > e^{PI_lo}
epi_lo = exp_b(PI[0])[0]
s_pi_hi = (1 + PI[1]) / epi_lo
rep(f"s(pi) < {float(s_pi_hi):.5f} < ln 2", s_pi_hi < F(69, 100))
# ln 2 enclosure
ln2_lo = sum(F(1, k * 2 ** k) for k in range(1, 40))
# S_0 = ln 2 + 2 sum_{k>=1} s(2 pi k) > ln 2 + 2 * [x/(e^x + 1)] at x = 2 pi (lower bound, one term)
e2pi_hi = exp_b(2 * PI[1])[1]
S0_lo = ln2_lo + 2 * (2 * PI[0]) / (e2pi_hi + 1)
rep(f"S_0 > {float(S0_lo):.5f} > ln 2 (offset-0 array exceeds the capacity)", S0_lo > ln2_lo + F(1, 100))


# ---------------- GJ
# stored: GJ form = 1/3 (quarks), -1 (leptons) in units of the 10; w4 P4 = -(3/32) T_GJ
def ratio(a_, b_):
    quark = a_ + b_ * F(-3, 32) * F(1, 3)
    lep = a_ + b_ * F(-3, 32) * F(-1)
    return lep / quark


rep("lepton/quark = (32a + 3b)/(32a - b) at three weights; 3 at b/a = 32/3",
    all(ratio(F(x), F(y)) == (32 * F(x) + 3 * F(y)) / (32 * F(x) - F(y)) for x, y in ((1, 0), (1, 5), (2, -7)))
    and ratio(F(3), F(32)) == 3)


def diag_model(vd, wd):
    Y = [F(-1, 10), F(-1), F(3)]
    f = [F(1, 10), F(1), F(1)]
    Md = [vd * y + wd * x for y, x in zip(Y, f)]
    Me = [vd * y - 3 * wd * x for y, x in zip(Y, f)]
    Mu = [y + x for y, x in zip(Y, f)]
    Mn = [y - 3 * x for y, x in zip(Y, f)]
    return Mu, Mn, Md, Me


A, B, C = diag_model(F(1), F(1, 3)), diag_model(F(1), F(1, 5)), diag_model(F(47, 45), F(1, 5))
rep("models: factors 3, 2, 37/19; same M_u, M_nu", A[3][1] / A[2][1] == 3 and B[3][1] / B[2][1] == 2
    and C[3][1] / C[2][1] == F(37, 19) and A[0] == B[0] == C[0] and A[1] == B[1] == C[1])
rep("A and C share sigma_1(M_d) = 10/3", max(map(abs, A[2])) == max(map(abs, C[2])) == F(10, 3))
mt = A[0][2]
N = [x / F(1) - (1 if i == 2 else 0) for i, x in enumerate([F(1, 10), F(1), F(1)])]
sig1N = max(map(abs, N))
rep(f"top reading sigma_1(N) = {sig1N} = 1 holds; bottom reading needs m_b/m_t = {F(10,3)/mt} (fails in A and C alike)",
    sig1N == 1 and F(10, 3) / mt != sig1N)
# h_mu invariance on a random rational model with a 120
random.seed(7)


def rnd():
    return F(random.randint(-9, 9), random.randint(1, 9))


def matsym():
    m_ = [[rnd() for _ in range(3)] for _ in range(3)]
    return [[(m_[i][j] + m_[j][i]) / 2 for j in range(3)] for i in range(3)]


def matanti():
    m_ = [[rnd() for _ in range(3)] for _ in range(3)]
    return [[(m_[i][j] - m_[j][i]) / 2 for j in range(3)] for i in range(3)]


Y_, f_, h_ = matsym(), matsym(), matanti()
vu, vd, wu, wd = rnd(), rnd(), rnd(), rnd()
cu, cn, cd, ce = rnd(), rnd(), rnd(), rnd()
comb = lambda *ts: [[sum(c * M[i][j] for c, M in ts) for j in range(3)] for i in range(3)]
okh = True
for mu in (F(1), F(3, 7), F(-5, 2)):
    Mu = comb((vu, Y_), (wu, f_), (cu, h_))
    Mn = comb((vu, Y_), (-3 * wu, f_), (cn, h_))
    Md = comb((vd, Y_), (mu * wd, f_), (cd, h_))
    Me = comb((vd, Y_), (-3 * mu * wd, f_), (ce, h_))
    D = comb((1, Md), (-1, Me))
    symD = [[(D[i][j] + D[j][i]) / 2 for j in range(3)] for i in range(3)]
    okh = okh and symD == comb((4 * mu * wd, f_))
    if mu == 1:
        Mu0, Mn0 = Mu, Mn
    okh = okh and Mu == Mu0 and Mn == Mn0
rep("random model with a 120: h_mu fixes M_u, M_nu and scales Sym(M_d - M_e) = 4 mu w_d f", okh)

# ---------------- D-term: critical level by hand
g, gp, kap, H2 = F(2, 3), F(1, 2), F(1, 5), F(1)
for lam_ in (F(1, 3), F(1, 5)):
    Nn = (H2 ** 2 / lam_ ** 2 + lam_ ** 2) / 2
    m = (H2 ** 2 / lam_ ** 2 - lam_ ** 2) / 2
    dm = -(H2 ** 2 / lam_ ** 3 + lam_)
    dN = -(H2 ** 2 / lam_ ** 3 - lam_)
    # V = 1/2 (g^2 m^2/4 + g'^2 (m/2 - z)^2) + kap N^2;  dV/dlam = 0 is linear in z
    c0 = (g * g * m * dm / 2 + gp * gp * (m / 2) * dm) / 2 + 2 * kap * Nn * dN   # d/dlam of (1/2)(g^2 m^2/4) is g^2 m m'/4
    c1 = -(gp * gp * dm) / 2          # coefficient of z in dV/dlam
    z = -c0 / c1
    xi = 2 * z
    rep(f"frame {lam_}: hand-derived critical level xi = {xi} equals m(g^2 + g'^2 + 8 kappa)/g'^2",
        xi == m * (g * g + gp * gp + 8 * kap) / (gp * gp))
print("ALL OK" if ok_all else "SOME FAILED")
