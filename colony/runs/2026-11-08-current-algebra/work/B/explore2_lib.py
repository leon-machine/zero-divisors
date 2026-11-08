from fock import *
from fractions import Fraction as F
def setup(n,L):
    M=n*L
    idx=lambda x,j: x*L+j
    CD={(x,j):cdag(idx(x,j),M) for x in range(n) for j in range(L)}
    C={(x,j):c(idx(x,j),M) for x in range(n) for j in range(L)}
    def jcur(x,y,q):
        out={}
        for j in range(L):
            if 0<=j+q<L: out=add(out,mul(CD[(x,j)],C[(y,j+q)]))
        return out
    return M,idx,CD,C,jcur
def solve(names,rows,rhs):
    m=[ [F(v) for v in r]+[F(b)] for r,b in zip(rows,rhs)]
    ncol=len(rows[0]); piv=[]; r=0
    for col in range(ncol):
        p=next((i for i in range(r,len(m)) if m[i][col]!=0),None)
        if p is None: continue
        m[r],m[p]=m[p],m[r]
        pv=m[r][col]; m[r]=[v/pv for v in m[r]]
        for i in range(len(m)):
            if i!=r and m[i][col]!=0:
                f=m[i][col]; m[i]=[a-f*b for a,b in zip(m[i],m[r])]
        piv.append(col); r+=1
    incons=any(all(v==0 for v in row[:-1]) and row[-1]!=0 for row in m)
    return incons,{names[c]:m[i][-1] for i,c in enumerate(piv)}
