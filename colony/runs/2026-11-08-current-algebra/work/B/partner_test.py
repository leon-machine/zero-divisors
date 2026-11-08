from fractions import Fraction as F
from itertools import combinations
STATES=[S for r in range(6) for S in combinations(range(5),r)]
def a(j,S):
    if j not in S: return None
    p=S.index(j); return (-1)**p, tuple(x for x in S if x!=j)
def ad(i,S):
    if i in S: return None
    p=sum(1 for x in S if x<i); return (-1)**p, tuple(sorted(S+(i,)))
def act(t,S):  # t: {(i,j):coef real}
    out={}
    for (i,j),c in t.items():
        r=a(j,S)
        if r is None: continue
        s1,S1=r; r2=ad(i,S1)
        if r2 is None: continue
        s2,S2=r2; out[S2]=out.get(S2,0)+c*s1*s2
    return out
def comp(S): return tuple(x for x in range(5) if x not in S)
def eps(S):
    s=1; T=S
    for i in comp(S):  # apply a†_{S^c} after a†_S ... order: a†_S a†_{S^c}|0> means a†_{s1}..a†_{sr} a†_{c1}..|0>
        pass
    # compute sign of permutation (S, S^c) -> sorted
    seq=list(S)+list(comp(S)); inv=sum(1 for i in range(5) for j in range(i+1,5) if seq[i]>seq[j])
    return (-1)**inv
import random
def nk(S): n=sum(1 for x in S if x<2); return n,len(S)-n
comps={}
for S in STATES: comps.setdefault(nk(S),[]).append(S)
gens=[{(0,1):1,(1,0):-1},{(0,1):1,(1,0):1},{(0,0):1,(1,1):-1},{(2,3):1,(3,2):-1},{(2,4):1},{(3,3):1,(4,4):-1},{(0,0):F(1,2),(1,1):F(1,2),(2,2):F(-1,3),(3,3):F(-1,3),(4,4):F(-1,3)}]
ok=True
for A,B in [((1,0),(1,3)),((2,0),(0,3)),((0,1),(2,2)),((1,1),(1,2)),((2,1),(0,2))]:
    for t in gens:
        for S in comps[A]:
            for R in comps[A]:
                mA=act(t,S).get(R,0)        # <R|t|S>
                # partner: <S^c| t | R^c> with signs
                mB=act(t,comp(R)).get(comp(S),0)*eps(S)*eps(R)
                # want M_B[x,y] = -M_A[y,x]: x=S^c?? M_B[S^c,R^c] = <S^c|t|R^c> eps eps ; M_A[R,S]=<R|t|S>
                if mB != -mA: ok=False; print(A,t,S,R,mA,mB)
print(ok)
