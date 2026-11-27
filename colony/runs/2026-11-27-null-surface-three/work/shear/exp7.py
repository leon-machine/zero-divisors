import sys, time
sys.path.insert(0, 'colony/runs/2026-11-27-null-surface-three/work/shear')
from pw import *
x0 = (F(1, 2), F(1, 3), F(-1, 4), F(1, 5))
ORDER = 8
n = ORDER - 1
# (b2) area parameter, generic S0 with nonzero expansion, vacuum and with matter (tr w != 0)
profiles = {
 "vacuum": [[[F(3), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(-2), F(-1)]]],
 "matter": [[[F(1), F(2), F(1)], [F(5, 2), F(-1)]], [[F(5, 2), F(-1)], [F(-3), F(1), F(-2)]]],
}
S0 = [[F(2, 3), F(-1, 5)], [F(-1, 5), F(3, 7)]]
for name, w in profiles.items():
    W_ = Wave(w, S0, x0, ORDER, analytic=True)
    th = W_.theta(); Sig = W_.trB2() - F(1, 2) * th * th; r4 = W_.rho4()
    trw = u_series(series_jet(w[0][0], W_.du) + series_jet(w[1][1], W_.du), n)
    th, Sig, r4 = u_series(th, n), u_series(Sig, n), u_series(r4, n + 1)
    rho = s_pow(r4, F(1, 4), n + 1)
    p = s_der(rho)                                 # to du^7
    ok_a = s_der(p)[:n] == s_scal(F(-1, 2), s_mul(s_add(Sig, s_scal(-1, trw)), rho, n))[:n]
    # (b2): d(p^2)/d rho = -rho Sigma_rho p^2 + rho KRK ; as u-series: (p^2)' = -rho Sigma p + rho KRK p
    p2 = s_mul(p, p, n)
    lhs = s_der(p2)
    rhs = s_add(s_scal(-1, s_mul(s_mul(rho, Sig, n), p, n)), s_mul(s_mul(rho, trw, n), p, n))
    ok_b2 = lhs[:n] == rhs[:n]
    # integrated form vacuum: ln(p/p0) = -1/2 int rho Sigma / p du
    if name == "vacuum":
        pn = s_scal(1 / p[0], p)
        Xi = s_scal(F(1, 2), s_int(s_mul(s_mul(rho, Sig, n), s_inv(p, n), n)))
        ok_int = s_log(pn, n)[:n + 1] == s_scal(-1, Xi)[:n + 1]
        # lambda - lambda0 = (1/p0) int e^Xi d rho = (1/p0) int e^Xi p du ; e^Xi = p0/p
    else:
        # p^2 = e^{-2 Xi}[p0^2 + int e^{2 Xi} rho KRK d rho]
        ok_int = None
    # (b1) with e0 != 0 and matter: e = 2p ; de/ds = -Sig_s + rho^2 KRK ; s' = 1/rho
    e = s_scal(2, p)
    ok_b1 = s_mul(rho, s_der(e), n - 1)[:n] == s_mul(s_mul(rho, rho, n), s_add(s_scal(-1, Sig), trw), n)[:n]
    print(name, "p0", p[0], "theta0", th[0], ok_a, ok_b2, ok_int, ok_b1)

# exact power-law waves: qbar = diag(rho^a, rho^-a)
for a in (F(1), F(3), F(1, 2), F(-2), F(10)):
    den = 1 + a * a / 4
    p1, p2 = (1 + a / 2) / den, (1 - a / 2) / den
    c1, c2 = p1 * (p1 - 1), p2 * (p2 - 1)
    u0 = F(2)
    xx = (u0 + F(1, 5), F(1, 3), F(-1, 4), F(1, 5))
    # Taylor coefficients of c/u^2 about u0: c * (-1)^k (k+1) / u0^(k+2)
    K_ = 6
    inv2 = [(-1) ** k * (k + 1) / u0 ** (k + 2) for k in range(K_)]
    w = [[[c1 * x for x in inv2], []], [[], [c2 * x for x in inv2]]]
    W_ = Wave(w, [[p1 / u0, 0], [0, p2 / u0]], xx, 2)
    fld = W_.fld
    Rop = gtg.as_op(fld.curvature())
    th = W_.theta(); Sig = W_.trB2() - F(1, 2) * th * th
    dth = W_.along(th)
    q = (dth.v / 2 + th.v ** 2 / 4) / (th.v ** 2 / 4)      # rho rho''/rho'^2
    print("a =", a, "p1,p2", p1, p2, "c", c1, c2, "vacuum", gtg.ricci_flat(Rop, S), fld.torsion_free(),
          "Q(K)", jet_zero(W_.QK(), 2), "theta*u", th.v * u0, "P", p1 + p2,
          "rho rho''/rho'^2 =", q, "pred", -a * a / 4, "Sig/theta^2", Sig.v / th.v ** 2, "pred", a * a / 8,
          "2/(u theta)", 2 / (u0 * th.v), "pred", den)
