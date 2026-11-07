# plain Fock exploration (not evidence): window modes k = -M..M-1, index i = k + M
from fractions import Fraction as F
import itertools
def apply_hop(state, i, j):
    """a*_i a_j on basis state (tuple of 0/1) -> (sign, newstate) or None"""
    s = list(state)
    if s[j] == 0: return None
    sign = (-1) ** sum(s[:j]); s[j] = 0
    if s[i] == 1: return None
    sign *= (-1) ** sum(s[:i]); s[i] = 1
    return sign, tuple(s)
def op_rho(q, L):  # rho_q = sum_k a*_k a_{k+q}
    return [(k, k + q) for k in range(L - q)]
def apply(terms, vec, coef=1):
    out = {}
    for st, c in vec.items():
        for (i, j) in terms:
            r = apply_hop(st, i, j)
            if r: out[r[1]] = out.get(r[1], 0) + c * r[0] * coef
    return {k: v for k, v in out.items() if v != 0}
def addv(a, b, cb=1):
    o = dict(a)
    for k, v in b.items(): o[k] = o.get(k, 0) + cb * v
    return {k: v for k, v in o.items() if v != 0}
def check(M):
    L = 2 * M
    bad = []; good = 0
    for st in itertools.product((0, 1), repeat=L):
        Q = sum(st) - M
        E = sum((F(2 * i - L + 1, 2)) for i in range(L) if st[i]) + F(M * M, 2)  # sum (k+1/2) n_k + M^2/2
        T = {}
        for q in range(1, L):
            r = apply(op_rho(q, L), {st: 1})
            r = {k: F(v) for k, v in r.items()}
            rr = {}
            for st2, c in r.items():
                for (i, j) in op_rho(q, L):
                    x = apply_hop(st2, j, i)
                    if x: rr[x[1]] = rr.get(x[1], 0) + c * x[0]
            T = addv(T, {k: v for k, v in rr.items()})
        T = addv(T, {st: F(Q * Q, 2)})
        exact = (T == ({st: E} if E != 0 else {}))
        # depth: number of filled modes at the bottom, empty at the top
        db = 0
        while db < L and st[db] == 1: db += 1
        dt = 0
        while dt < L and st[L - 1 - dt] == 0: dt += 1
        if exact: good += 1
        bad.append((exact, E, Q, db, dt, st))
    return bad
for M in (2, 3, 4):
    res = check(M)
    # criterion guess: exact iff E (excitation energy) satisfies something with depths
    ex = [r for r in res if r[0]]
    nonex = [r for r in res if not r[0]]
    print("M", M, "exact", len(ex), "not", len(nonex))
    # print min over non-exact of (E - Q^2/2) and depth
    for r in sorted(ex, key=lambda r: (r[1]))[:0]: print(r)
    mins = {}
    for r in nonex:
        key = r[2]
        mins.setdefault(key, []).append(r[1] - F(r[2] ** 2, 2))
    print("  non-exact min boson energy E - Q^2/2 per charge:", {k: min(v) for k, v in sorted(mins.items())})
    maxs = {}
    for r in ex:
        maxs.setdefault(r[2], []).append(r[1] - F(r[2] ** 2, 2))
    print("  exact max boson energy per charge:", {k: max(v) for k, v in sorted(maxs.items())})
print("debug")
M=4; L=8
for st in [(1,1,1,0,1,0,0,0),(1,1,1,1,0,1,0,0)]:
    T={}
    for q in range(1,L):
        r=apply(op_rho(q,L),{st:1})
        rr={}
        for st2,c in r.items():
            for (i,j) in op_rho(q,L):
                x=apply_hop(st2,j,i)
                if x: rr[x[1]]=rr.get(x[1],0)+F(c*x[0],q)
        T=addv(T,rr)
    print(st,T)
print("fails")
res=check(4)
for r in res:
    if not r[0] and r[1]-F(r[2]**2,2)==2: print(r)
print("T on")
st=(1,1,1,0,0,1,0,0); L=8
for q in range(1,L):
    r=apply(op_rho(q,L),{st:1})
    rr={}
    for st2,c in r.items():
        for (i,j) in op_rho(q,L):
            x=apply_hop(st2,j,i)
            if x: rr[x[1]]=rr.get(x[1],0)+F(c*x[0],q)
    print(q, r, {k:v for k,v in rr.items() if v})
