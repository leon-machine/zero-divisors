import sys
sys.argv=['x','2','1','1']
exec(open('explore.py').read().split("nb=int(sys.argv[1])")[0])
import sympy as sp
def gs(nb,K,G):
    best=None
    for n1 in range(nb+1):
      for n2 in range(nb+1):
        for ns in range(nb+1):
          ev=spectrum(nb,K,G,n1,n2,ns)
          e=min(ev.keys(), key=lambda t: float(t))
          if best is None or float(e)<float(best[0]): best=(e,(n1,n2,ns))
    band=min((2*K*p-G*p*(nb-p+1),p) for p in range(nb+1))
    return best, band
for nb in (2,3):
  for K,G in [(3,1),(1,2),(1,1),(0,1),(sp.Rational(1,2),sp.Rational(5,3)),(3,4),(2,1)]:
    K=sp.Rational(K);G=sp.Rational(G)
    print(nb,K,G,gs(nb,K,G))
