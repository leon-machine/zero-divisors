import sys, itertools
sys.path.insert(0,'lib')
from fractions import Fraction as F
import GA, numpy as np
# 1. (2,3)_Q: Hilbert symbol at 3 via Legendre symbol, and brute search of norm form
leg = pow(2,(3-1)//2,3); print("Legendre (2/3) residue:", leg, "(2 == -1 mod 3 -> nonsplit at 3)")
N=12; zeros=[t for t in itertools.product(range(-N,N+1),repeat=4) if any(t) and t[0]**2-2*t[1]**2-3*t[2]**2+6*t[3]**2==0]
print("nontrivial zeros of a^2-2b^2-3c^2+6d^2 with |.|<=12:", len(zeros))
# contrast: squares 2 and 7 -> (2,7)_Q; 2 is a square mod 7 (3^2=9=2), find zero
z=[t for t in itertools.product(range(-6,7),repeat=4) if any(t) and t[0]**2-2*t[1]**2-7*t[2]**2+14*t[3]**2==0][:1]; print("squares 2,7 zero example:", z)
# 2. Sylvester by eigenvalues (independent of rejection) for the six Grams
G={"hyperbolic":[[0,1],[1,0]],"plane":[[2,0],[0,3]],"mixed":[[1,2,0],[2,1,0],[0,0,-3]],"deg":[[1,1,0],[1,1,0],[0,0,0]],
"npr":[[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,5]],"lsk":[[1,1,1,1],[1,0,1,1],[1,1,-1,1],[1,1,1,-2]]}
for k,g in G.items():
    ev=np.linalg.eigvalsh(np.array(g,float)); print(k,(int((ev>1e-9).sum()),int((ev<-1e-9).sum()),int((abs(ev)<=1e-9).sum())))
# 3. E_{I,I} closed form for k=2
k=2; sq=GA.sig(k,k)
v=[GA.scal(F(1,2),GA.add(GA.gen(i),GA.gen(k+i))) for i in range(k)]
w=[GA.scal(F(1,2),GA.sub(GA.gen(i),GA.gen(k+i))) for i in range(k)]
def pr(xs):
    o=GA.sc(1)
    for x in xs: o=GA.mul(o,x,sq)
    return o
f=pr([GA.mul(v[i],w[i],sq) for i in range(k)])
ok=True
for m in range(k+1):
  for I in itertools.combinations(range(k),m):
    E=pr([w[i] for i in I]+[f]+[v[j] for j in reversed(I)])
    cf=pr([GA.mul(w[i],v[i],sq) if i in I else GA.mul(v[i],w[i],sq) for i in range(k)])
    ok &= GA.eq(E,cf)
print("E_II closed form k=2:",ok)
# 4. Cl(0,3): e123 central, square +1
sq3=GA.sig(0,3); u=pr.__globals__  # dummy
e=[GA.gen(i) for i in range(3)]
t=GA.mul(GA.mul(e[0],e[1],sq3),e[2],sq3); print("e123^2 in Cl(0,3):",GA.mul(t,t,sq3), "central:",all(GA.commutes(t,x,sq3) for x in e))
