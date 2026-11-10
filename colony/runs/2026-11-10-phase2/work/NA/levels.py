"""Scratch: exponential reading against the proved tower. Exact (GA.py, Fractions)."""
import sys, time
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from itertools import combinations
import GA

def pairs(k):
    """Cl(k,k): generators e_0..e_{k-1} (+1), f_0..f_{k-1} (-1); v_j=(e_j+f_j)/2, w_j=(e_j-f_j)/2."""
    sq = GA.sig(k, k)
    v = [GA.scal(F(1, 2), GA.add(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    w = [GA.scal(F(1, 2), GA.sub(GA.gen(j), GA.gen(k + j))) for j in range(k)]
    return sq, v, w

def car_ok(sq, v, w):
    k = len(v)
    for i in range(k):
        for j in range(k):
            if not GA.is_zero(GA.add(GA.mul(v[i], v[j], sq), GA.mul(v[j], v[i], sq))): return False
            if not GA.is_zero(GA.add(GA.mul(w[i], w[j], sq), GA.mul(w[j], w[i], sq))): return False
            if not GA.eq(GA.add(GA.mul(v[i], w[j], sq), GA.mul(w[j], v[i], sq)), GA.sc(1 if i == j else 0)): return False
    return True

def vacuum(sq, v, w):
    P = GA.sc(1)
    for j in range(len(v)):
        P = GA.mul(P, GA.mul(w[j], v[j], sq), sq)
    return P

def ideal_dim(k):
    sq, v, w = pairs(k)
    P = vacuum(sq, v, w)
    assert GA.eq(GA.mul(P, P, sq), P)
    blades = GA.all_blades(2 * k)
    vecs = []
    for b in blades:
        x = GA.mul({b: F(1)}, P, sq)
        vecs.append(GA.basis_vector_of(x, blades))
    return GA.rank_of_vectors(vecs)

t = time.time()
for k in (1, 2, 3, 4):
    sq, v, w = pairs(k)
    print("k", k, "CAR", car_ok(sq, v, w), "dim left ideal Cl(k,k)P =", ideal_dim(k), "2^k =", 2 ** k, round(time.time() - t, 1))

# level two of E-fock: Cl(8,8), pairs indexed by the 8 subsets of {0,1,2}
sq8, V, W = pairs(8)
print("Cl(8,8) 8 state-indexed pairs CAR as vectors:", car_ok(sq8, V, W), round(time.time() - t, 1))

# second-quantised lift for k = 2 (Cl(4,4)) and k = 3 (Cl(8,8))
def subsets(k):
    return [frozenset(c) for r in range(k + 1) for c in combinations(range(k), r)]

def wedge(j, S):
    if j in S: return None
    return frozenset(S | {j}), (-1) ** len([i for i in S if i < j])

def contract(j, S):
    if j not in S: return None
    return frozenset(S - {j}), (-1) ** len([i for i in S if i < j])

def lift(k):
    st = subsets(k)
    ix = {S: n for n, S in enumerate(st)}
    d = len(st)
    sq, V, W = pairs(d)
    def dG(op, j):
        out = {}
        for S in st:
            r = op(j, S)
            if r is None: continue
            T, s = r
            out = GA.add(out, GA.scal(s, GA.mul(V[ix[T]], W[ix[S]], sq)))
        return out
    a = [dG(wedge, j) for j in range(k)]
    b = [dG(contract, j) for j in range(k)]
    num = {}
    for n in range(d):
        num = GA.add(num, GA.mul(V[n], W[n], sq))
    res = {}
    res["a0^2 zero"] = GA.is_zero(GA.mul(a[0], a[0], sq))
    ac = GA.add(GA.mul(a[0], b[0], sq), GA.mul(b[0], a[0], sq))
    res["{a0,b0} = 1"] = GA.eq(ac, GA.sc(1))
    res["{a0,b0} = number op"] = GA.eq(ac, num)
    cm = GA.sub(GA.mul(a[0], b[0], sq), GA.mul(b[0], a[0], sq))
    # [v,w] on F: v w - w v = 2 v w - 1 : diag +1 on S containing 0, -1 otherwise
    dcomm = {}
    for S in st:
        s = 1 if 0 in S else -1
        dcomm = GA.add(dcomm, GA.scal(s, GA.mul(V[ix[S]], W[ix[S]], sq)))
    res["[dG v, dG w] = dG[v,w] (Lie)"] = GA.eq(cm, dcomm)
    if k > 1:
        res["{a0,a1} zero"] = GA.is_zero(GA.add(GA.mul(a[0], a[1], sq), GA.mul(a[1], a[0], sq)))
        res["[a0,a1] = dG[v0,v1]"] = None
    res["terms a0^2"] = len(GA.mul(a[0], a[0], sq))
    return res

for k in (1, 2, 3):
    print("lift k =", k, lift(k), round(time.time() - t, 1))
