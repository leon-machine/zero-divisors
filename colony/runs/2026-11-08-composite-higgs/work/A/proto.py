import sys, time
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import combinations
import GA

def ann(i, st, m):
    return GA.ext_contract([F(1) if j == i else F(0) for j in range(m)], st)

def addin(out, x, c):
    for k, v in x.items():
        out[k] = out.get(k, 0) + c * v

def pairsum(Om, f, g, st):
    m = 3 * Om; out = {}
    for b in range(Om):
        y = ann(3*b+g, st, m); y = ann(3*b+f, y, m)       # w_f w_g |st>
        for c in range(Om):
            z = GA.ext_wedge(3*c+g, GA.ext_wedge(3*c+f, y))   # v_g v_f ... (sum_c w_f w_g)* = sum v_g v_f
            addin(out, z, 1)
    return {k: v for k, v in out.items() if v != 0}

def sector(Om, nums):
    m = 3*Om
    return [frozenset(S) for k in range(m+1) for S in combinations(range(m), k)
            if tuple(sum(1 for j in S if j % 3 == f) for f in range(3)) == nums]

def matrix(Om, nums, coeffs):
    basis = sector(Om, nums); idx = {S: i for i, S in enumerate(basis)}
    M = [[F(0)]*len(basis) for _ in basis]
    for j, S in enumerate(basis):
        for (f, g), c in coeffs.items():
            for T, v in pairsum(Om, f, g, {S: F(1)}).items():
                M[idx[T]][j] += c * v
    return M

def inertia(M):
    """negative-eigenvalue count etc. by sparse symmetric elimination with zero-pivot repair"""
    n = len(M)
    A = [{j: x for j, x in enumerate(r) if x != 0} for r in M]
    alive = list(range(n)); pos = neg = zer = 0
    alive_set = set(alive)
    while alive_set:
        piv = next((i for i in alive_set if A[i].get(i, 0) != 0), None)
        if piv is None:
            found = None
            for i in alive_set:
                for j, x in A[i].items():
                    if j != i and j in alive_set and x != 0:
                        found = (i, j); break
                if found: break
            if found is None:
                zer += len(alive_set); break
            i, j = found
            # row/col i += row/col j
            for k, x in list(A[j].items()):
                A[i][k] = A[i].get(k, 0) + x
            for k in list(alive_set):
                if j in A[k]:
                    A[k][i] = A[k].get(i, 0) + A[k][j]
            A[i][i] = A[i].get(i, 0)  # already updated via column pass
            continue
        d = A[piv][piv]
        if d > 0: pos += 1
        else: neg += 1
        alive_set.discard(piv)
        rowp = {k: x for k, x in A[piv].items() if k in alive_set and x != 0}
        for i, xi in rowp.items():
            f = xi / d
            Ai = A[i]
            for k, xk in rowp.items():
                v = Ai.get(k, 0) - f * xk
                if v: Ai[k] = v
                else: Ai.pop(k, None)
    return pos, neg, zer

if __name__ == '__main__':
    Om, s = int(sys.argv[1]), int(sys.argv[2])
    t = time.time()
    Wm = matrix(Om, (s, s+1, 1), {(0,1):1, (0,2):1, (1,2):1})
    print('dim', len(Wm), 'build', round(time.time()-t,2))
    for a in range(0, 3*Om):
        t = time.time()
        Mm = [[(F(a) if i == j else 0) - Wm[i][j] for j in range(len(Wm))] for i in range(len(Wm))]
        p, ng, z = inertia(Mm)
        print('a', a, '#eig>a', ng, 'zero', z, round(time.time()-t, 2))
