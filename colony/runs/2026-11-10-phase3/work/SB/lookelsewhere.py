from fractions import Fraction as F
def window(ns, sig, n=3):
    lo, hi = (1-ns) - n*sig, (1-ns) + n*sig   # 1 - n_s in [lo, hi]
    return lo, hi
data = {"Planck2018": (F("0.9649"), F("0.0042")), "P-ACT-LB2": (F("0.9752"), F("0.0030")), "SPA": (F("0.9684"), F("0.0030")), "SPT+Planck": (F("0.9647"), F("0.0037"))}
for name, (ns, sig) in data.items():
    for n in (1, 3):
        lo, hi = window(ns, sig, n)
        nulo, nuhi = F(3,2) + lo/2, F(3,2) + hi/2
        # smallest denominator rational nu in window
        best = None
        for b in range(1, 200):
            a0 = -(-nulo*b // 1)
            if F(a0, b) <= nuhi:
                best = F(a0, b); break
        # integer power-law exponents p with 1-ns = 2/(p-1) (expanding) in window
        ps = [p for p in range(2, 400) if lo <= F(2, p-1) <= hi]
        # xi window: 3 - sqrt(6 xi) = -(1-ns) -> xi = (3 + t)^2/6
        xlo, xhi = (3+lo)**2/6, (3+hi)**2/6
        xr = sorted({F(a, b) for b in range(1, 13) for a in range(0, 2*b+1) if xlo <= F(a, b) <= xhi})
        allr = {F(a, b) for b in range(1, 13) for a in range(0, 2*b+1)}
        print(name, n, "sigma: 1-ns in [%s,%s]; nu in [%.5f,%.5f]; least-denominator nu %s; integer p %s..%s (%d); xi in [%.4f,%.4f], rationals den<=12: %s; sig from scale-inv %.2f; expected count %.2f" % (
            float(lo), float(hi), nulo, nuhi, best, ps[0] if ps else None, ps[-1] if ps else None, len(ps), xlo, xhi, xr, float((1-ns)/sig), len(allr)*float(xhi-xlo)/2))
# wands dual: contraction w for measured tilt: n-1 = -12 w/(1+... ) exact: p = 2/(3(1+w)), nu = 3/2 + 1/(p-1)
for ns in (F("0.9649"),):
    t = 1 - ns   # 3 - 2|nu| = -t -> |nu| = 3/2 + t/2
    # expanding branch nu = 3/2 + t/2: 1/(p-1) = t/2
    p = 1 + 2/t; w = F(2,3)/p - 1; print("expanding p", p, float(p), "w", w, float(w), "r=16/p", float(16/p))
    # contracting: nu = -(3/2 + t/2): 1/(p-1) = -3 - t/2
    p = 1 + 1/(-3 - t/2); w = F(2,3)/p - 1; print("contracting p", p, float(p), "w", w, float(w), "r=24(1+w)", float(24*(1+w)))
    print("running for dust+const:", float(6*t), "sigma off", float((6*t + F("0.0045"))/F("0.0067")))
# one-loop: factor needed
print("min factor (xi-1/6) from 1/2:", float((F("1.522584375")-F(1,6))/(F(1,2)-F(1,6))), float((F("1.548079215")-F(1,6))/(F(1,2)-F(1,6))))
# de sitter: P_T/P_Phi
print("P_T/P_Phi(lambda=1) =", F(16)/F(2))
