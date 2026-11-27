import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
from pw import *
x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
w1 = [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]]
ORDER = 8
def run(eps, S0):
    w = [[[eps * c for c in w1[i][j]] for j in range(2)] for i in range(2)]
    W_ = Wave(w, S0, x0, ORDER, analytic=True)
    th = W_.theta()
    Sig = W_.trB2() - F(1, 2) * th * th
    r4 = W_.rho4()
    n = ORDER - 1
    only_u = all(e[1] == 0 and e[2] == 0 for j in (th, Sig, r4) for e in j.c)
    return u_series(th, n), u_series(Sig, n), u_series(r4, n + 1), only_u, jet_zero(W_.QK(), ORDER)

t0 = time.time()
Z = [[0, 0], [0, 0]]
res = {}
for eps in (F(1), F(-2), F(3, 2), F(5), F(-1, 3), F(7, 4)):
    th, Sig, r4, only_u, qk = run(eps, Z)
    n = ORDER - 1
    rho = s_pow(r4, F(1, 4), n + 1)              # to du^8
    # (a) rho' = theta rho / 2, rho'' = -1/2 Sigma rho
    d1 = s_der(rho)                               # to du^7
    ok1 = d1[:n + 1] == s_scal(F(1, 2), s_mul(th, rho, n))[:n + 1]
    d2 = s_der(d1)                                # to du^6
    ok2 = d2[:n] == s_scal(F(-1, 2), s_mul(Sig, rho, n))[:n]
    # (b1) s = int du / rho; ln rho^2 = - int_0^u (s(u) - s(u')) rho Sigma du'
    sser = s_int(s_inv(rho, n))                   # to du^8
    rs = s_mul(rho, Sig, n)                       # to du^7
    A = s_int(rs)                                 # to du^8
    Bq = s_int(s_mul(sser, rs, n))
    rhs = s_add(s_mul(sser, A, n + 1), s_scal(-1, Bq))
    lhs = s_log(s_mul(rho, rho, n + 1), n + 1)
    ok3 = lhs[:n + 2] == s_scal(-1, rhs)[:n + 2]
    res[eps] = (th, Sig, rho, lhs)
    print(eps, only_u, qk, ok1, ok2, ok3, "theta:", th[:5], "rho:", rho[:6])
print("time", time.time() - t0)

# interpolate in eps
def lagrange(xs, ys):
    """coefficients of the interpolating polynomial through (xs, ys)."""
    n = len(xs)
    coef = [F(0)] * n
    for i in range(n):
        num = [F(1)]
        den = F(1)
        for j in range(n):
            if j != i:
                num = polymul(num, [-xs[j], F(1)], n)
                den *= xs[i] - xs[j]
        for k in range(len(num)):
            if k < n:
                coef[k] += ys[i] * num[k] / den
    return coef
xs = list(res)
for name, idx in (("theta", 0), ("Sigma", 1), ("rho", 2), ("ln rho^2", 3)):
    print(name)
    for k in range(len(res[xs[0]][idx])):
        c = lagrange(xs, [res[e][idx][k] for e in xs])
        print("  du^%d:" % k, [str(x) for x in c])
