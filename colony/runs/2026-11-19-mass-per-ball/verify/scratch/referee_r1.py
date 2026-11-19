"""Referee R1 scratch: exact arithmetic in Q(pi) as Laurent polynomials {k: c} = sum c pi^k."""
from fractions import Fraction as F

def lp(c, k=0): return {k: F(c)} if c != 0 else {}
def mul(*xs):
    out = {0: F(1)}
    for b in xs:
        new = {}
        for k1, c1 in out.items():
            for k2, c2 in b.items():
                new[k1+k2] = new.get(k1+k2, F(0)) + c1*c2
        out = {k: c for k, c in new.items() if c != 0}
    return out
def inv(a):
    (k, c), = a.items(); return {-k: 1/c}
def add(*xs):
    out = {}
    for x in xs:
        for k, c in x.items(): out[k] = out.get(k, F(0)) + c
    return {k: c for k, c in out.items() if c != 0}
# unit-ball volumes by Gamma-free closed forms, independent of the stored recursion
V = {2: lp(1, 1), 3: lp(F(4, 3), 1), 4: lp(F(1, 2), 2), 5: lp(F(8, 15), 2)}
PI_LO, PI_HI = F(314159265358, 10**11), F(314159265359, 10**11)
def bounds(x):
    lo = hi = F(0)
    for k, c in x.items():
        u, v = c*PI_LO**k, c*PI_HI**k; lo += min(u, v); hi += max(u, v)
    return lo, hi

# 1. key numbers
f3, f5, f6 = mul(V[3], inv(V[2])), mul(V[3], inv(V[4])), mul(V[3], inv(V[5]))
T = add(lp(1), mul(lp(2), f3), mul(lp(2), f5))
print("V3/V2 =", f3, " V3/V4 =", f5, " V3/V5 =", f6)
print("T =", T, [float(b) for b in bounds(T)])
T4 = add(T, f6); print("T with residue 4 at D=5:", T4, [float(b) for b in bounds(T4)])
print("share 16x five-dim (own cell):", add(lp(1), mul(lp(2), f3), mul(lp(4), f5)))

# 2. (iii) converse with a mirror of density 2 rho_3: the three conditions of the iff hold, E fails
d = F(49, 50); rho3 = lp(F(3, 7), -1)
rho2 = mul(f3, lp(d), rho3); rho4 = mul(f5, rho3, lp(1/d)); rho_mirror = mul(lp(2), rho3)
mpb = lambda rho, D, L: mul(rho, V[D], lp(L**D))
assert mpb(rho2, 2, d) == mpb(rho3, 3, d) == mpb(rho4, 4, d)       # s = t = d, both shares hold
assert all(mpb(rho_mirror, 3, L) != mpb(rho3, 3, L) for L in (d, F(1), F(2)))
print("mirror counterexample: shares and s = t hold, mirror mass per ball is twice ours at every length -> E fails")
# two sheet towers with unequal densities whose mean share is 4/3: the summed total is unchanged, E fails
rho2a, rho2b = mul(lp(F(1, 2)), rho2), mul(lp(F(3, 2)), rho2)
sh = lambda r: mul(r, inv(mul(lp(d), rho3)))
assert add(sh(rho2a), sh(rho2b)) == mul(lp(2), f3) and mpb(rho2a, 2, d) != mpb(rho3, 3, d)
print("pair counterexample: total kept, E fails for each sheet tower")

# 3. contact mechanism (iv) on own cells, three-dimensional towers: downward count uses OUR quanta's cells a6
mu = F(938, 7)
for a6, ar in [(d, 2*d), (2*d, d), (3*d, 5*d)]:
    rho_us = lp(mu/d**3) ; rho_us = mul(rho_us, inv(V[3]))
    rho_sheet = mul(lp(mu/d**2), inv(V[2]))                 # E for the sheet tower
    per_area_us = mul(rho_us, lp(a6))                        # our matter whose own cell (radius a6) meets the plane, one side
    ratio_on_sheet = mul(per_area_us, inv(rho_sheet))        # rho_us/rho_3D read on the sheet
    # O: rho_3D/rho_us read on our space, sheets s apart: rho_sheet/(s rho_us) = 1/ratio_on_sheet  => s
    s = mul(rho_sheet, inv(rho_us), ratio_on_sheet)
    assert s == {0: a6}
    share = mul(rho_sheet, inv(mul(lp(s[0]), rho_us)))
    assert share == mul(f3, lp(d/a6))
    stated = mul(f3, lp(d/ar))                               # entity (iv): (V3/V2)(a_r/d)^(-1)
    print(f"a6={a6}, a_r={ar}: mechanism gives s = a6, share = (V3/V2)(d/a6); stated (iv) equals it: {share == stated}")

# 4. R3 v3 own-cell formula under E reduces to (V3/V_D)(a_r/d)^(D-3) (independent of a6)
for D in (2, 4):
    for a6, ar in [(F(1), F(2)), (F(3), F(5, 7))]:
        m_r, m_6 = mu*(ar/d)**D, mu*(a6/d)**3            # E with one quantum per own cell
        lhs = mul(lp(m_r/m_6), V[3], inv(V[D]), lp((a6/ar)**3))
        rhs = mul(V[3], inv(V[D]), lp((ar/d)**(D-3)))
        assert lhs == rhs
print("R3 v3 formula (m_r/m_6)(V3/V_D)(a6/a_r)^3 = (V3/V_D)(a_r/d)^(D-3) under E: ok")

# 5. epoch (v): d_sheet ~ rho2/rho3 ~ a, d_five ~ rho3/rho4 ~ b
for a in (F(2), F(3)):
    for beta in (0, 1, 2):
        b = a**beta
        r2, r3, r4 = 1/a**2, 1/a**3, 1/(a**3*b)
        assert r2/r3 == a and r3/r4 == b
print("epoch exponents: ok")
# 6. (iv) one length: (k)^2 = (k)^3 forces k = 1 for positive rationals sampled
assert all((k**2 == k**3) == (k == 1) for k in (F(1,2), F(1), F(2), F(7,3)))
print("all referee checks done")
