"""Own route for P2 (ii)(c): the error bound, by an independent route. One block = two fermion modes in a
4-dim Fock matrix representation (Jordan-Wigner), with J represented by the complex i (exploration only;
the identification is used only to evaluate numbers). omega_N(prod_j W_N(x_j)) = omega(Z)^N by (a);
compare with e^{-c} and with the stated bound. The norms ||y||_1 are computed exactly in GA."""
import sys, cmath, math
from fractions import Fraction as F
import numpy as np
from scipy.linalg import expm
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

# ---- exact GA side: blade norms of the centred fields in Cl(2,2) (block, no kernel needed for ||.||_1;
# pi = J(b* - b) has the same blade norm as b* - b since J times a blade is +- a blade)
s = (1, -1, 1, -1)
mul = lambda x, y: GA.mul(x, y, s)
v = [GA.scal(F(1, 2), GA.add(GA.gen(2 * k), GA.gen(2 * k + 1))) for k in range(2)]
w = [GA.scal(F(1, 2), GA.sub(GA.gen(2 * k), GA.gen(2 * k + 1))) for k in range(2)]
n = [mul(v[k], w[k]) for k in range(2)]
def star(x):
    out = {}
    for b, c in x.items():
        g = len(b); sg = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if s[i] == -1)
        out[b] = sg * c
    return out
b = mul(v[0], w[1])
phi = GA.add(b, star(b)); pim = GA.sub(star(b), b)
norm1 = lambda x: sum(abs(c) for c in x.values())
p1, p2 = F(3, 4), F(1, 5)

# ---- matrix side: Jordan-Wigner for two modes, basis |n1 n2>
a1 = np.kron(np.array([[0, 1], [0, 0]]), np.eye(2))
Z = np.diag([1, -1])
a2 = np.kron(Z, np.array([[0, 1], [0, 0]]))
N1, N2 = a1.conj().T @ a1, a2.conj().T @ a2
bm = a1.conj().T @ a2            # v_1 w_2 = a_1^* a_2
phim = bm + bm.conj().T
pim_m = 1j * (bm.conj().T - bm)
rho = np.kron(np.diag([1 - float(p1), float(p1)]), np.diag([1 - float(p2), float(p2)]))
om = lambda X: np.trace(rho @ X)

def run(name, xs_m, norms):
    ys = [x - om(x) * np.eye(4) for x in xs_m]
    r = sum(norms)
    c = 0.5 * om(sum(ys) @ sum(ys)) + 0.5 * sum(om(ys[j] @ ys[l] - ys[l] @ ys[j]) for j in range(len(ys)) for l in range(j + 1, len(ys)))
    print(f"{name}: r = {r:.4f}, c = {c:.6f}")
    for N in (1, 4, 16, 64, 256, 1024, 10**4, 10**6):
        Zm = np.eye(4, dtype=complex)
        for y in ys:
            Zm = Zm @ expm(1j * y / math.sqrt(N))
        val = om(Zm) ** N
        err = abs(val - cmath.exp(-c))
        bound = r ** 3 / 6 * math.exp(r / math.sqrt(N)) / math.sqrt(N) + r ** 4 / 8 * math.exp(r ** 2 / (2 * N)) / N
        print(f"  N={N:>8}: err={err:.3e}  bound={bound:.3e}  ok={err <= bound}  sqrtN*err={err*math.sqrt(N):.5f}")

# n_1 - p1: ||y||_1 exactly
yn = GA.sub(n[0], GA.sc(p1)); print("||n_1 - p1||_1 =", norm1(yn), " predicted |kappa_3|/6 e^{-c} =",
      float(abs(p1 * (1 - p1) * (1 - 2 * p1)) / 6) * math.exp(-float(p1 * (1 - p1)) / 2))
run("x = n_1", [N1], [float(norm1(yn))])
# phi, n_1, pi (noncommuting list); omega(phi) = omega(pi) = 0
run("x = (phi, n_1, pi)", [phim, N1, pim_m], [float(norm1(phi)), float(norm1(yn)), float(norm1(pim))])
