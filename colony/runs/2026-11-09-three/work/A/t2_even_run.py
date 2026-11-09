import sys, time
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
from t2_even import functionals
t0 = time.time()
for (r0, w, s0, c0, l) in [(F(3), F(1,2), F(3,5), F(4,5), 2), (F(5), F(2,3), F(5,13), F(12,13), 3)]:
    cols = []; zer = []
    for fn in range(4):
        for i in range(4):
            for j in range(4 - i):
                rows, Psi, VZ, fj = functionals(r0, w, s0, c0, l, fn, (i, j))
                Zv = (Psi.d(0).d(0) - fj * (fj * Psi.d(1)).d(1) + VZ * Psi).v
                cols.append(rows); zer.append(Zv)
    n = len(cols)
    Mrows = [[cols[c][k] for c in range(n)] for k in range(len(cols[0]))]
    Mrows = [r for r in Mrows if any(r)]
    rk = GA.field_rank(Mrows); rk2 = GA.field_rank(Mrows + [zer])
    print(l, 'rows', len(Mrows), 'rank', rk, 'with Zerilli', rk2, 'zer nonzero', any(zer), time.time() - t0)
    # control: wrong potential
    zer_bad = list(zer)
