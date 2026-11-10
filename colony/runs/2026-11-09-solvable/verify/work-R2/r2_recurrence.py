"""R2 independent recomputation for the two recurrence proposals (exact arithmetic, lib/GA.py).

(a) On a window of L = 6 planes (beyond the proposal's L = 2, 4): Gamma_win = (-1)^M prod_j (1 - 2 n_j) built from
    the Witt pairs equals (-1)^M prod_j e_j f_j, squares to 1, anticommutes with every v_j, w_j, and is +1 on the sea.
    Spectrum route: every occupation eigenvalue h of H satisfies h - Q/2 in Z, so e^{2 pi J h} = (-1)^Q.
(b) The sea constant by the closed Bernoulli form zeta(-1, a) = -B_2(a)/2 (not by series inversion):
    symmetric CAR sea at delta = 1/2 is -1/24; real CCR at delta = 0 is -1/24.
(c) The table c = 16 n_g + 2 n_V + n_s + 2 eps: verdicts for n_h = 0, 1, 2, with and without the graviton, and the
    J3 'currents' reading (bosons not added: c = 16 n_g) for comparison.
(d) Grading sign ambiguity: U = +-Gamma iff 12 | n; for 16 n_g that is again 3 | n_g.
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA  # noqa: E402

ok_all = True


def rep(msg, ok):
    global ok_all
    ok_all = ok_all and ok
    print(("OK  " if ok else "BAD ") + msg)


# (a)
L = 6
M = L // 2
s = tuple([-1, -1] + [1, -1] * L)
mul = lambda x, y: GA.mul(x, y, s)
e = [GA.gen(2 + 2 * j) for j in range(L)]
f = [GA.gen(3 + 2 * j) for j in range(L)]
v = [GA.scal(F(1, 2), GA.add(e[j], f[j])) for j in range(L)]
w = [GA.scal(F(1, 2), GA.sub(e[j], f[j])) for j in range(L)]
n = [mul(v[j], w[j]) for j in range(L)]
J = mul(GA.gen(0), GA.gen(1))
G1 = GA.sc((-1) ** M)
G2 = GA.sc((-1) ** M)
for j in range(L):
    G1 = mul(G1, GA.sub(GA.sc(1), GA.scal(F(2), n[j])))
    G2 = mul(G2, mul(e[j], f[j]))
rep("L=6: (-1)^M prod(1 - 2 n_j) = (-1)^M prod e_j f_j", GA.eq(G1, G2))
rep("L=6: Gamma^2 = 1", GA.eq(mul(G1, G1), GA.sc(1)))
rep("L=6: Gamma anticommutes with all v_j, w_j", all(GA.anticommutes(G1, x, s) for x in v + w))
rep("L=6: Gamma commutes with J", GA.commutes(G1, J, s))
vac = GA.sc(1)
for j in range(L):
    vac = mul(vac, mul(w[j], v[j]))
sea = vac
for j in reversed(range(M)):
    sea = mul(v[j], sea)
rep("L=6: Gamma = +1 on the sea", GA.eq(mul(G1, sea), sea))
okh = True
for m_ in range(2 ** L):
    occ = [(m_ >> j) & 1 for j in range(L)]
    h = F(M * M, 2) + sum(F(2 * (j - M) + 1, 2) * occ[j] for j in range(L))
    Q = sum(occ) - M
    okh = okh and (h - F(Q, 2)).denominator == 1
rep("L=6: every eigenvalue h has h - Q/2 integer (so e^{2 pi J h} = (-1)^Q)", okh)


# (b)
def B2(a):
    return a * a - a + F(1, 6)


def hz(a):            # zeta(-1, a) = -B_2(a)/2
    return -B2(a) / 2


car_sea = -(hz(F(1, 2)) + hz(F(1, 2))) / 2
rep(f"CAR symmetric sea at delta=1/2 = {car_sea} (want -1/24)", car_sea == F(-1, 24))
ccr_real = hz(F(1)) / 2   # (1/2) sum_{m>=1} m = zeta(-1)/2
rep(f"real CCR at delta=0: {ccr_real} (want -1/24)", ccr_real == F(-1, 24))
car_zero = -(hz(F(1)) + 0) / 2 * 2   # delta = 0: towers m >= 1 and m >= 0 (zero mode weight 0)
print(f"    note: CAR at delta=0 symmetric sea (towers k>=1 and k>=0 with zero weight) = {-(hz(F(1)) + hz(F(1)))/2} = +1/12")


# (c)
def c_of(ng, nV, ns, eps, per=16):
    return per * ng + 2 * nV + ns + 2 * eps


def verdict(nh, eps, window):
    mod = 24 if window == 1 else 12
    return [g for g in range(1, 10) if c_of(g, 12, 4 * nh, eps) % mod == 0]


rep("n_h=2, eps=0, one-window passes [1,4,7]", verdict(2, 0, 1) == [1, 4, 7])
rep("n_h=2: n_g=3 fails, c=80", c_of(3, 12, 8, 0) == 80 and 80 % 24 != 0 and 80 % 12 != 0)
rep("n_h=1, eps=0: one-window never, two-window [2,5,8]", verdict(1, 0, 1) == [] and verdict(1, 0, 2) == [2, 5, 8])
rep("eps=1: nothing passes for n_h < 12", all(verdict(h, 1, 1) == [] and verdict(h, 1, 2) == [] for h in range(12)))
rep("J3 currents reading (c = 16 n_g): passes [3,6,9]", [g for g in range(1, 10) if (16 * g) % 24 == 0] == [3, 6, 9])
# consistency of the two proposals: proposal-1 (iv) with c_B = 24 + 4 n_h + 2 eps
cons = True
for nh in range(12):
    for eps in (0, 1):
        cb = 24 + 4 * nh + 2 * eps
        p1 = [g for g in range(1, 13) if cb % 8 == 0 and (g - cb // 8) % 3 == 0]
        p2 = [g for g in range(1, 13) if eps == 0 and (nh - 2 * g) % 6 == 0]
        cons = cons and p1 == p2
rep("proposal 1 (iv) and proposal 2 (iii) agree on every (n_h, eps)", cons)
# (d)
rep("U = +-Gamma (12 | 16 n_g) iff 3 | n_g", [g for g in range(1, 13) if (16 * g) % 12 == 0] == [3, 6, 9, 12])
print("ALL OK" if ok_all else "SOME FAILED")
