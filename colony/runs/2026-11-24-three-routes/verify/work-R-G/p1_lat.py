# Independent implementation of proposal 1's stencils (referee R-G). Exact: integers / dyadic floats / mod-p.
import numpy as np, itertools
COMP = [(0,0),(1,1),(2,2),(0,1),(0,2),(1,2)]
CI = {c:i for i,c in enumerate(COMP)}
def ci(i,j): return CI[(min(i,j),max(i,j))]
def T(f,i,s=1): return np.roll(f,-s,axis=i)          # (T_i f)(x) = f(x+e_i)
def s_(f,i): return T(f,i)-f
def b_(f,i): return f-T(f,i,-1)
def Dl(f,i): return b_(s_(f,i),i)
def other(i,j): return 3-i-j
def G2(h):   # returns 2*G[h]
    out=[None]*6
    for i in range(3):
        j,k=[m for m in range(3) if m!=i]
        out[ci(i,i)] = Dl(h[ci(j,j)],k)+Dl(h[ci(k,k)],j) - 2*b_(b_(h[ci(j,k)],j),k)
    for (i,j) in [(0,1),(0,2),(1,2)]:
        k=other(i,j)
        out[ci(i,j)] = -Dl(h[ci(i,j)],k) + s_(b_(h[ci(j,k)],k),i) + s_(b_(h[ci(i,k)],k),j) - s_(s_(h[ci(k,k)],j),i)
    return out
def D(h):
    r = 0
    for (i,j) in [(0,1),(0,2),(1,2)]:
        r = r + 2*b_(b_(h[ci(i,j)],i),j)
    for i in range(3):
        for k in range(3):
            if k!=i: r = r - Dl(h[ci(i,i)],k)
    return r
def C(pi):
    return [s_(pi[ci(i,i)],i) + sum(b_(pi[ci(i,j)],j) for j in range(3) if j!=i) for i in range(3)]
def disp(xi):
    out=[None]*6
    for i in range(3): out[ci(i,i)] = 2*b_(xi[i],i)
    for (i,j) in [(0,1),(0,2),(1,2)]: out[ci(i,j)] = s_(xi[j],i)+s_(xi[i],j)
    return out
def pair(a,b):
    return sum((a[c]*b[c]).sum()*(1 if c<3 else 2) for c in range(6))
