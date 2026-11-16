"""R3: new statements of the B - L proposal, from my own charge table.

Kill conditions (before running):
 K1 if tr_16(B-L) != 0, tr_15(B-L) != -1, tr(B-L)^3 differ from (0, -1), or tr Y^2(B-L), tr Y(B-L)^2 nonzero on
    sixteen or fifteen, clause (i) as revised is wrong.
 K2 if the symmetric-phase Gram ratio with N_H = 1 + eps differs from 28/79 - 48 eps/(79(79 + 13 eps)) at any
    rational eps, the sensitivity formula is wrong.
 K3 if the bound (250/81)(1 - 2^-18)^-2 e^(-72/5) is not below 2e-6, or the resulting shift not below 2e-8, the
    numerical statement of (vii) is wrong.
"""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as Fr
import GA  # noqa: F401  (exact library; Fractions used directly)

# (name, multiplicity, Y, B-L, T3 list for the components)
species = [("Q", 6, Fr(1, 6), Fr(1, 3)), ("u^c", 3, Fr(-2, 3), Fr(-1, 3)), ("d^c", 3, Fr(1, 3), Fr(-1, 3)),
           ("L", 2, Fr(-1, 2), Fr(-1)), ("e^c", 1, Fr(1), Fr(1)), ("nu^c", 1, Fr(0), Fr(1))]
def tr(f, drop_singlet):
    return sum(m * f(Y, X) for n, m, Y, X in species if not (drop_singlet and n == "nu^c"))
for lab, ds in (("sixteen", False), ("fifteen", True)):
    print(lab, "tr(B-L) =", tr(lambda Y, X: X, ds), " tr(B-L)^3 =", tr(lambda Y, X: X ** 3, ds),
          " tr Y^2(B-L) =", tr(lambda Y, X: Y * Y * X, ds), " tr Y(B-L)^2 =", tr(lambda Y, X: Y * X * X, ds),
          " tr Y =", tr(lambda Y, X: Y, ds), " tr Y^3 =", tr(lambda Y, X: Y ** 3, ds))

# Gram ratio in the symmetric phase from states: per family on the fifteen; N_H doublets of Y = 1/2, weight 2
def chi(a, b, NH, Nf=3):
    fer = Nf * sum(m * a(Y, X) * b(Y, X) for n, m, Y, X in species if n != "nu^c")
    bos = 2 * NH * 2 * a(Fr(1, 2), Fr(0)) * b(Fr(1, 2), Fr(0))      # two complex components per doublet
    return fer + bos
Yc = lambda Y, X: Y
BL = lambda Y, X: X
nB = lambda Y, X: X if X in (Fr(1, 3), Fr(-1, 3)) else Fr(0)     # quarks: n_B = B - L there
def gram(NH):
    num = chi(nB, BL, NH) * chi(Yc, Yc, NH) - chi(nB, Yc, NH) * chi(Yc, BL, NH)
    den = chi(BL, BL, NH) * chi(Yc, Yc, NH) - chi(Yc, BL, NH) ** 2
    return num / den
print("c_sym(N_H=1) =", gram(1), " c_sym(N_H=2) =", gram(2))
bad = [e for e in (Fr(0), Fr(1, 7), Fr(1), Fr(-1, 3), Fr(5, 2), Fr(10) ** -6)
       if gram(1 + e) != Fr(28, 79) - 48 * e / (79 * (79 + 13 * e))]
print("sensitivity formula mismatches:", bad)

# K3: exact upper bound on e^(-72/5): 1/e^(72/5) <= 1/partial sum of the exponential series of 72/5
x = Fr(72, 5); s = Fr(0); term = Fr(1)
for k in range(60):
    s += term; term = term * x / (k + 1)
ub_exp = 1 / s
w = Fr(250, 81) / (1 - Fr(1, 2 ** 18)) ** 2 * ub_exp
shift = 48 * w / (79 * 79)
print("weight bound < 2e-6:", w < Fr(2, 10 ** 6), " shift bound < 2e-8:", shift < Fr(2, 10 ** 8),
      " shift > 1e-8 (only an upper bound, so this is not implied):", shift > Fr(1, 10 ** 8))
print("2500/134 >= 18:", Fr(2500, 134) >= 18)
