import random
from poly import *
random.seed(11)
t, x, y, z = X

def rpoly(deg, nterms=6):
    f = ZJ
    for _ in range(nterms):
        m = ONE
        for i in range(D):
            m = m * X[i] ** random.randint(0, deg)
        f = f + m * F(random.randint(-4, 4), random.randint(1, 3))
    return f

def rsym(deg):
    H = zeros()
    for m in range(D):
        for k in range(m, D):
            H[m][k] = H[k][m] = rpoly(deg)
    return H

def outerc(xu, yu):
    return [[xu[m] * yu[k] + yu[m] * xu[k] for k in range(D)] for m in range(D)]
Nu = [1, 0, 0, 1]; M1u = [0, 1, 0, 0]; M2u = [0, 0, 1, 0]; NBu = [1, 0, 0, -1]
GB = [outerc(a, b) for a, b in ((Nu, Nu), (Nu, M1u), (Nu, M2u), (M1u, M1u), (M1u, M2u), (M2u, M2u))]
def rgauge(deg):
    H = zeros()
    for Bm in GB:
        f = rpoly(deg)
        H = [[H[m][k] + f * Bm[m][k] for k in range(D)] for m in range(D)]
    return H

xiB = [z, ZJ, ZJ, t]
nvec = [ONE, ZJ, ZJ, ONE]
def ndot(v):   # n . v
    return v[0] - v[3]
def dn(f):
    return f.d(0) + f.d(3)
def onN(f):
    return subst_N(f)
def eqN(f, g):
    return subst_N(f - g) == {}

H = rsym(2)
K = superpotential(H, xiB)
# K . n : vector; (K.n)^j = sum_i K^{ji} n_i(lower) ... compute generally: K.n = -n.K ; (n.K)^j = sum_i n_i K^{ij}, n_i lower = eta_i n^i
def comp(K, i, j):
    if i < j: return K[(i, j)]
    if i > j: return K[(j, i)] * (-1)
    return ZJ
def vdotK(v, K):   # v . K (vector) for constant-or-field v (upper comps)
    return [sum((v[i] * ETA[i] * comp(K, i, j) for i in range(D)), ZJ) for j in range(D)]
Kn = vscal(-1, vdotK(nvec, K))        # K . n
lhs = ndot(bdiv(K))
rhs = dn(K[(0, 3)] * (-1)) + Kn[1].d(1) + Kn[2].d(2)
print("n.(div K) = d_lam(-B.K) + div_perp (K.n)_perp on N:", eqN(lhs, rhs), "(even off N:", (lhs - rhs) == 0, ")")
# coefficient of n in K.n is -B.K ?
print("K.n = alpha n + perp with alpha = -B.K:", (Kn[0] - Kn[3]) == 0, (Kn[0] + K[(0, 3)]) == 0)

# light-cone gauge
Hg = rgauge(2)
print("h(n)=0:", all(not bool(c) for c in papply(Hg, nvec)))
Kg = superpotential(Hg, xiB)
tau = ptrace(Hg)
lam_dn_tau = dn(tau)   # on N multiply by lam: use t as lam (t = z = lam on N)
diff = Kg[(0, 3)] * (-1) - (tau - t * dn(tau))
print("-B.K = tau - lam d_n tau on N in gauge:", subst_N(diff) == {})
print("remainder on N:", subst_N(diff))
