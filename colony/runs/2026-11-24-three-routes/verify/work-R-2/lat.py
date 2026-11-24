# independent reimplementation from the formal text of clause (2)/(8); exact Fractions in object arrays
import numpy as np, sys
from fractions import Fraction as Fr
PAIRS=[(0,1),(0,2),(1,2)]  # components 3,4,5
def comp(i,j):
    if i==j: return i
    return 3+PAIRS.index((min(i,j),max(i,j)))
def s(a,i): return np.roll(a,-1,axis=i)-a
def b(a,i): return a-np.roll(a,1,axis=i)
def Dl(a,i): return b(s(a,i),i)
def G(h):
    out=[None]*6
    for i in range(3):
        j,k=[m for m in range(3) if m!=i]
        out[i]=Fr(1,2)*(Dl(h[j],k)+Dl(h[k],j)) - b(b(h[comp(j,k)],j),k)
    for (i,j) in PAIRS:
        k=3-i-j
        out[comp(i,j)]=Fr(1,2)*(-Dl(h[comp(i,j)],k)+s(b(h[comp(j,k)],k),i)+s(b(h[comp(i,k)],k),j)-s(s(h[k],j),i))
    return out
def D(h):
    r=0
    for (i,j) in PAIRS: r=r+2*b(b(h[comp(i,j)],j),i)
    for i in range(3):
        for k in range(3):
            if k!=i: r=r-Dl(h[i],k)
    return r
def zeros(L): return np.full((L,L,L),Fr(0),dtype=object)
def pmap(pi):
    tr=pi[0]+pi[1]+pi[2]
    return [pi[c]-(Fr(1,2)*tr if c<3 else 0) for c in range(6)]
def step(h,pi,tau=Fr(1,2)):
    g=G(h); pi2=[pi[c]-tau*g[c] for c in range(6)]
    p=pmap(pi2); return [h[c]+2*tau*p[c] for c in range(6)],pi2
