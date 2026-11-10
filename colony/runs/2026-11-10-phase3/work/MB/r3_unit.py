"""Adversarial test of the sibling's density-law clause: which length is R3's unit when R2 fails?
Exact: quantities are c * pi^k, sums kept as {k: Fraction}. Family (E-preserving): m_r = s_r m,
nu_r = 1/(s_r V_D d^D). Three readings of R3's unit: (a) the length d of (E); (b) this tower's Wigner-Seitz radius
d s_6^(1/3); (c) the tower's own Wigner-Seitz radius d s_r^(1/D_r). To stay rational take s_r = k_r^(D_r) for (c)
and s_6 = k_6^3 for (b)."""
from fractions import Fraction as F

def V(D):                      # unit ball volume as (coefficient, power of pi): V_D = 2 pi V_{D-2} / D
    c, k = (F(1), 0) if D % 2 == 0 else (F(2), 0)
    for d in range(2 + D % 2, D + 1, 2):
        c, k = c * 2 / d, k + 1
    return c, k

def ratio(a, b):
    return (a[0] / b[0], a[1] - b[1])

def total(k2, k4, k6, reading):
    """k_r: s_r = k_r^(D_r). Returns {power of pi: coefficient} for T (mirror term 1; two towers of each odd kind)."""
    out = {0: F(1)}
    base3 = ratio(V(3), V(2)); base5 = ratio(V(3), V(4))
    if reading == 'a':
        u3 = u5 = F(1)                        # thickness d
    elif reading == 'b':
        u3 = u5 = F(k6)                       # thickness d k_6
    else:
        u3, u5 = F(k2), F(k4)                 # own cell radius d k_r
    # share = (m nu)_r/(m nu)_6 * thickness^(+1 or -1) ; (m nu)_r = m/(V_D d^D) for every member of the family
    f3 = (base3[0] / u3, base3[1]); f5 = (base5[0] * u5, base5[1])
    for c, k in (f3, f5):
        out[k] = out.get(k, F(0)) + 2 * c
    return out

rule = {0: F(1) + F(8, 3), -1: F(16, 3)}
assert V(2) == (F(1), 1) and V(3) == (F(4, 3), 1) and V(4) == (F(1, 2), 2) and V(5) == (F(8, 15), 2)
assert total(1, 1, 1, 'a') == total(1, 1, 1, 'b') == total(1, 1, 1, 'c') == rule
assert total(3, 2, 1, 'a') == rule                       # (E)-length reading: shares kept for every s
assert total(3, 2, 1, 'b') == rule                       # our-cell reading: kept when s_6 = 1
assert total(3, 2, 2, 'b') == {0: F(1) + F(4, 3), -1: F(32, 3)}   # our-cell reading with s_6 = 8: moved
assert total(1, 2, 1, 'c') == {0: F(1) + F(8, 3), -1: F(32, 3)}   # own-cell reading, s_5D = 16: 1 + 8/3 + 32/(3 pi)
assert total(2, 1, 1, 'c') == {0: F(1) + F(4, 3), -1: F(16, 3)}   # own-cell reading, s_3D = 4: 1 + 4/3 + 16/(3 pi)
lo, hi = F(333, 106), F(355, 113)
t = F(11, 3) + F(32, 3) / hi, F(11, 3) + F(32, 3) / lo
assert F(706, 100) < t[0] and t[1] < F(707, 100)
# joint D, R1, R2: equal quanta per ball of radius ell and one quantum per ball of radius a in dimensions 2, 3, 4
# need (ell/a)^2 = (ell/a)^3 = (ell/a)^4, so ell/a = 1 (the only positive root of x^2 = x^3)
assert [x for x in (F(1, 2), F(1), F(2), F(3)) if x ** 2 == x ** 3 == x ** 4] == [F(1)]
print('ok: own-cell reading moves the total to', float(t[0]))
