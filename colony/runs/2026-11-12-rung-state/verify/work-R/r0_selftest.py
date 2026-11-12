"""Self-test of the matrix route: Clifford relations, transpose = (P) adjoint, faithfulness size."""
from myalg import *
for n in (1, 2, 3):
    es, fs = jw(n)
    I = SM.eye(2 ** n)
    ok = True
    for i in range(n):
        ok &= es[i] * es[i] == I and fs[i] * fs[i] == I.sc(-1)
        ok &= es[i].T() == es[i] and fs[i].T() == fs[i].sc(-1)
        for j in range(n):
            ok &= (es[i] * fs[j] + fs[j] * es[i]).d == {}
            if i != j:
                ok &= (es[i] * es[j] + es[j] * es[i]).d == {} and (fs[i] * fs[j] + fs[j] * fs[i]).d == {}
    # faithfulness: the 4^n blade matrices are linearly independent
    gens = es + fs
    mats = []
    for r in range(2 * n + 1):
        for c in combinations(range(2 * n), r):
            m = I
            for g in c:
                m = m * gens[g]
            mats.append([m.d.get((a, b), F(0)) for a in range(2 ** n) for b in range(2 ** n)])
    ok &= rank(mats) == 4 ** n
    print("n =", n, "relations, adjoint = transpose, faithful:", ok)
