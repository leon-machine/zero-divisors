from fractions import Fraction as F
# fermionic Fock space on modes indexed 0..M-1, states bitmasks; operator = dict {(out,in): coeff} sparse matrix
def cdag(i,M):
    op={}
    for s in range(1<<M):
        if not s>>i &1:
            sign=(-1)**bin(s & ((1<<i)-1)).count('1')
            op[(s|1<<i,s)]=sign
    return op
def c(i,M):
    return {(b,a):v for (a,b),v in cdag(i,M).items()}
def mul(A,B):
    Bi={}
    for (o,i),v in B.items(): Bi.setdefault(o,[]).append((i,v))
    out={}
    for (o,m),v in A.items():
        for (i,w) in Bi.get(m,[]):
            out[(o,i)]=out.get((o,i),0)+v*w
    return {k:v for k,v in out.items() if v!=0}
def add(*As,coeffs=None):
    out={}
    for t,A in enumerate(As):
        cf=1 if coeffs is None else coeffs[t]
        for k,v in A.items(): out[k]=out.get(k,0)+cf*v
    return {k:v for k,v in out.items() if v!=0}
def scal(a,A): return {k:a*v for k,v in A.items() if a*v!=0}
def comm(A,B): return add(mul(A,B),mul(B,A),coeffs=[1,-1])
def dag(A): return {(i,o):v for (o,i),v in A.items()}  # real coefficients only
def ident(M): return {(s,s):1 for s in range(1<<M)}
