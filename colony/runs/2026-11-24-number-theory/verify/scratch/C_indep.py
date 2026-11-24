# Independent route for C(ii)/(iv): work in the truncated ring Z[s]/(s^(n+1)), s = chi - 1, where the ideal (f),
# f = (1+s)^N - 1, is the Z-span of f s^i; membership of 2^m (1 - chi^(N/2)) is a triangular divisibility problem.
from math import comb
def order(N, n, cap=200):
    f=[comb(N,k) for k in range(N+1)]; f[0]=0          # f = N s + ...
    w=[comb(N//2,k) for k in range(N//2+1)]; w[0]=0    # chi^(N/2) - 1
    for m in range(cap):
        t=[0]*(n+1)
        for k,c in enumerate(w):
            if k<=n: t[k]=(2**m)*c
        # eliminate with f s^i, whose lowest term is N s^(i+1)
        ok=True
        for pos in range(1,n+1):
            c=t[pos]
            if c % N: ok=False; break
            q=c//N; i=pos-1
            for k,fc in enumerate(f):
                if i+k<=n: t[i+k]-=q*fc
        if ok and not any(t): return m
    return None
ceil=lambda a,b:-(-a//b)
bad=[(N,n) for N in (2,4,8,16) for n in range(1,61) if order(N,n)!=ceil(2*n,N)]
print("mismatches:",bad)
print([order(4,n) for n in range(1,15)])
