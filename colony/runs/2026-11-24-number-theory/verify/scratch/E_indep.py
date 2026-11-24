from fractions import Fraction as F
from math import gcd
def B2(x): return x*x-x+F(1,6)
def legendre(a,p): a%=p; return 0 if a==0 else (1 if pow(a,(p-1)//2,p)==1 else -1)
def chi(D,a):
    # explicit real characters from their definitions
    if D==-4: return [0,1,0,-1][a%4]
    if D==8: return {1:1,3:-1,5:-1,7:1}.get(a%8,0)
    if D==-8: return {1:1,3:1,5:-1,7:-1}.get(a%8,0)
    if D==12: return {1:1,5:-1,7:-1,11:1}.get(a%12,0)
    if D in (-3,5,13,-11,-7,-23):  # prime |D|: Legendre symbol (a/|D|) is chi_D for D = 1 mod 4 in sign sense
        p=abs(D); return legendre(a,p)
    if D==-20: return chi(-4,a)*legendre(a,5) if a%2 and a%5 else 0
    if D==-15: return legendre(a,3)*legendre(a,5)
def sums(D,M):
    f=2*M; tw=[(2*j+1, F(2*j+1,f)) for j in range(M)]
    c=[chi(D,a) if gcd(a,f)==1 else 0 for a,_ in tw]
    return sum(ci*(1-2*d) for ci,(a,d) in zip(c,tw)), sum(ci*B2(d) for ci,(a,d) in zip(c,tw))
for D,M in [(-4,2),(-8,4),(-20,10),(-3,3),(-11,11),(-7,7),(-15,15),(-23,23),(8,4),(12,6),(5,5),(13,13)]:
    print(D,M,sums(D,M))
