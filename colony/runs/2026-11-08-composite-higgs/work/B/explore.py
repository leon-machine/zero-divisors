# exploratory: doublet-singlet floor, exact spectrum by sectors (sympy-free, Fractions)
from fractions import Fraction as F
from itertools import combinations
import sys
sys.path.insert(0,'/home/claude/phys-graph/lib')
import sympy as sp

def ann(i, S):
    if i not in S: return None
    sgn = (-1)**sum(1 for j in S if j < i)
    return sgn, S - {i}
def cre(i, S):
    if i in S: return None
    sgn = (-1)**sum(1 for j in S if j < i)
    return sgn, S | {i}
def apply(ops, vec):
    # ops: list of ('a'|'c', i) applied right to left
    for kind, i in reversed(ops):
        out = {}
        for S, c in vec.items():
            r = (ann if kind=='a' else cre)(i, S)
            if r is None: continue
            s, T = r
            out[T] = out.get(T, 0) + s*c
        vec = {k:v for k,v in out.items() if v != 0}
    return vec
def add(a,b,c=1):
    out=dict(a)
    for k,v in b.items(): out[k]=out.get(k,0)+c*v
    return {k:v for k,v in out.items() if v!=0}

def mode(b, ch): return 3*b+ch   # ch 0,1 doublet, 2 singlet
def H(nb, K, G, vec):
    out = {}
    for b in range(nb):
        for ch in range(3):
            out = add(out, apply([('c',mode(b,ch)),('a',mode(b,ch))], vec), K)
    for a in range(2):
        Pv = {}
        for b in range(nb):
            Pv = add(Pv, apply([('a',mode(b,a)),('a',mode(b,2))], vec))
        PPv = {}
        for b in range(nb):
            PPv = add(PPv, apply([('c',mode(b,2)),('c',mode(b,a))], Pv))
        out = add(out, PPv, -G)
    return out

def spectrum(nb,K,G,n1,n2,ns):
    m=3*nb
    basis=[frozenset(S) for k in range(m+1) for S in combinations(range(m),k)
           if sum(1 for j in S if j%3==0)==n1 and sum(1 for j in S if j%3==1)==n2 and sum(1 for j in S if j%3==2)==ns]
    idx={S:i for i,S in enumerate(basis)}
    M=sp.zeros(len(basis))
    for j,S in enumerate(basis):
        for T,v in H(nb,K,G,{S:1}).items(): M[idx[T],j]+=v
    return M.eigenvals()

nb=int(sys.argv[1]); K=sp.Rational(sys.argv[2]); G=sp.Rational(sys.argv[3])
allev={}
for n1 in range(nb+1):
  for n2 in range(nb+1):
    for ns in range(nb+1):
      ev=spectrum(nb,K,G,n1,n2,ns)
      allev[(n1,n2,ns)]=ev
      print((n1,n2,ns), sorted(ev.items(), key=lambda t: float(t[0])))
gs=min(min(float(e) for e in ev) for ev in allev.values())
print('ground', gs)
