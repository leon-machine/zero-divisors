from fractions import Fraction as F
from itertools import product, combinations
# components (n,k): dims dim2 x dim3, Y
def dim2(n): return [1,2,1][n]
def dim3(k): return [1,3,3,1][k]
def Y(n,k): return F(3*n-2*k,6)
# weights: T3 values for slot states, H8 = diag(1,1,-2)/? use pair weights; build weight lists by subsets
states=[S for r in range(6) for S in combinations(range(5),r)]
def wt(S):
    n=sum(1 for i in S if i<2); k=len(S)-n
    t3=sum(F(1,2) if i==0 else F(-1,2) for i in S if i<2)
    h={2:F(1),3:F(1),4:F(-2)}
    h8=sum(h[i] for i in S if i>=2)
    h3=sum({2:F(1,2),3:F(-1,2),4:F(0)}[i] for i in S if i>=2)
    return n,k,t3,h3,h8,Y(n,k)
comps={}
for S in states:
    n,k,*_=wt(S); comps.setdefault((n,k),[]).append(S)
pairs=[((1,0),(1,3)),((2,0),(0,3)),((0,1),(2,2)),((1,1),(1,2)),((2,1),(0,2))]
res=[]
for signs in product([0,1],repeat=5):
    Vp=list(comps[(0,0)])
    for s,(a,b) in zip(signs,pairs): Vp+=comps[a if s==0 else b]
    W=[wt(S) for S in Vp]
    lv=(sum(t3*t3 for _,_,t3,_,_,_ in W), sum(h3*h3 for _,_,_,h3,_,_ in W), sum(y*y for *_,y in W))
    an=(sum(y for *_,y in W), sum(y**3 for *_,y in W), sum(y*t3*t3 for _,_,t3,_,_,y in W), sum(y*h3*h3 for _,_,_,h3,_,y in W), sum(h8**3 for _,_,_,_,h8,_ in W))
    res.append((signs,lv,an,len(Vp)))
print(set(r[1] for r in res))
for r in res:
    if all(a==0 for a in r[2]): print('anomaly-free',r)
print(sum(1 for r in res if all(a==0 for a in r[2])))
# even-parity check
