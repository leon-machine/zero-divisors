"""R3: the restated quarter-turn sign rule of the determinant-phase proposal, by direct 3x3 determinants.

Kill condition (before running): at the quarter turn (t_d real, t_u = I tau) the exact determinant
det M_u det M_d must be real and of sign -sgn(c_u c_d R_u R_d), R_q = (p_q - 2 r_q)^2 + delta_q p_q^2, on every
case; R_q = 0 must give det M_q = 0 (a massless quark). Any exception kills the restated clause (iv).
Also: the closed form Theta = (c_u c_d)^3 (d_u d_d)^2 (t_u t_d)^2 R_u R_d at generic complex t.
"""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
from itertools import product
from GA import QI

def det3(M):
    a = M
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))

def stage(c, d, t, p, r):
    # J + d (E + t S), S real symmetric P12-odd: S11 = -S22 = p, S13 = S31 = r, S23 = S32 = -r, S12 = 0
    S = [[p, 0, r], [0, -p, -r], [r, -r, 0]]
    M = []
    for i in range(3):
        row = []
        for j in range(3):
            e = QI(1) + QI(d) * (QI(1 if (i == 2 and j == 2) else 0) + t * QI(S[i][j]))
            row.append(QI(c) * e)
        M.append(row)
    return M

def sgn(x): return (x > 0) - (x < 0)
R = lambda d, p, r: (p - 2 * r) ** 2 + d * p * p

fails = 0; n = 0; seen = set()
deltas = [Fr(1, 3), Fr(2), Fr(-5), Fr(-1, 2), Fr(-7), Fr(-3, 4)]
for cu, cd, du, dd, pu, ru, pd, rd in product([Fr(1), Fr(-2, 3)], [Fr(3, 2), Fr(-1)], deltas, deltas[:3] + [Fr(-9)],
                                              [Fr(2), Fr(1, 2)], [Fr(-1), Fr(1, 3)], [Fr(1)], [Fr(2), Fr(-1, 2)]):
    tau, td = Fr(3, 7), Fr(5, 2)
    Ru, Rd = R(du, pu, ru), R(dd, pd, rd)
    Th = det3(stage(cu, du, QI(0, tau), pu, ru)) * det3(stage(cd, dd, QI(td), pd, rd))
    n += 1
    if Ru == 0 or Rd == 0:
        ok = Th == QI(0)
    else:
        ok = Th.im == 0 and sgn(Th.re) == -sgn(cu * cd * Ru * Rd)
        seen.add((sgn(cu * cd), sgn(Ru * Rd), sgn(Th.re)))
    if not ok:
        fails += 1; print("FAIL", cu, cd, du, dd, pu, ru, pd, rd, Th)
print("quarter-turn sign rule: %d cases, %d failures; sign patterns (sgn c_u c_d, sgn R_u R_d, sgn Theta): %s"
      % (n, fails, sorted(seen)))

# the referee's case: delta_u = -5, p = 2, r = -1, R_u = -4
print("R_u(-5, 2, -1) =", R(Fr(-5), Fr(2), Fr(-1)))
# degenerate R_q = 0: delta = -(p - 2r)^2 / p^2, e.g. p = 1, r = 1: R = 1 + delta -> delta = -1
for (d, p, r) in [(Fr(-1), Fr(1), Fr(1)), (Fr(-9, 4), Fr(2), Fr(-1, 2)), (Fr(-25, 4), Fr(2), Fr(-3, 2))]:
    print("R = %s, det M = %s" % (R(d, p, r), det3(stage(Fr(1), d, QI(0, Fr(1)), p, r))))
# closed form at generic complex t
bad = 0
for cu, cd, du, dd, tu, td, pu, ru, pd, rd in [
        (Fr(1), Fr(2), Fr(1, 3), Fr(-5), QI(Fr(3, 5), Fr(4, 5)), QI(Fr(1), Fr(-2)), Fr(2), Fr(-1), Fr(1), Fr(3)),
        (Fr(-1, 2), Fr(1), Fr(-7), Fr(1, 2), QI(Fr(-7, 25), Fr(24, 25)), QI(Fr(2), Fr(1, 3)), Fr(1, 2), Fr(1), Fr(-1), Fr(0))]:
    Th = det3(stage(cu, du, tu, pu, ru)) * det3(stage(cd, dd, td, pd, rd))
    cf = QI((cu * cd) ** 3 * (du * dd) ** 2 * R(du, pu, ru) * R(dd, pd, rd)) * (tu * td) * (tu * td)
    bad += Th != cf
print("closed form at generic complex t: mismatches", bad)
# both a quarter turn: real, sign +sgn(c_u c_d R_u R_d)
Th = det3(stage(Fr(1), Fr(-5), QI(0, Fr(1)), Fr(2), Fr(-1))) * det3(stage(Fr(1), Fr(2), QI(0, Fr(3)), Fr(1), Fr(1)))
print("both quarter turns:", Th)
