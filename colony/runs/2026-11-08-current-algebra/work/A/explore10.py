import sys, importlib.util
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
spec = importlib.util.spec_from_file_location('ck', 'synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split/check.py')
ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
so = ck._so10(); D = ck._dual(so)
n = 16
def tensor(B, Dd):
    C = {}
    for M, Md in zip(B, Dd):
        sM = [(i, j, c) for i, r in enumerate(M) for j, c in enumerate(r) if c]
        sD = [(i, j, c) for i, r in enumerate(Md) for j, c in enumerate(r) if c]
        for a, c_, x in sD:
            for b, d, y in sM:
                C[(a, c_, b, d)] = C.get((a, c_, b, d), 0) + x * y
    return C
C = tensor(so, D)
# Casimir in the 16
K = {}
for (a, c, b, d), v in C.items():
    if c == b:
        K[(a, d)] = K.get((a, d), 0) + v
print('Casimir in 16 scalar:', set(v for (a, d), v in K.items() if a == d), all(v == 0 for (a, d), v in K.items() if a != d))
def A(T, a, b, c, d):
    return T.get((a, c, b, d), 0) - T.get((a, d, b, c), 0)
bad = 0
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                an = F(1, 16) * ((a == c) * (b == d) - (a == d) * (b == c))
                if A(C, a, b, c, d) + 3 * an != 0: bad += 1
print('A_so + 3 A_N nonzero entries:', bad)
# u(5) part only (first 25 generators) for comparison
u5 = so[:25]; Du5 = ck._dual(u5); C5 = tensor(u5, Du5)
vals = set()
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                an = F(1, 16) * ((a == c) * (b == d) - (a == d) * (b == c))
                if an: vals.add(A(C5, a, b, c, d) / an)
                elif A(C5, a, b, c, d): vals.add('off')
print('u5 ratios', vals)
