# Clause (1): stored first-order Einstein map in gauge h(e0)=0 vs leading symbols of the stencils. Own route, GA.py.
import sys, random, itertools
sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/lib')
import GA
from fractions import Fraction as F
SQ=(1,-1,-1,-1); e=[GA.gen(i) for i in range(4)]
def dot(a,b): return GA.mul(GA.add(GA.mul(a,b,SQ),GA.mul(b,a,SQ)),GA.sc(F(1,2)),SQ)
def num(x): return x.get((),F(0)) if isinstance(x,dict) else GA.scal(1,x)
def sc_of(x):
    # scalar part
    for k,v in x.items():
        pass
    return x.get((),0) if isinstance(x,dict) else 0
def S(x): 
    d=dict(x) if isinstance(x,dict) else x
    return d.get((),F(0))
random.seed(5)
H=[[0]*3 for _ in range(3)]
for m in range(3):
    for n in range(m,3):
        H[m][n]=H[n][m]=F(random.randint(-5,5))
def hmap(a):  # h(a) = sum H_mn (a.e_m) e_n over spatial m,n (h(e0)=0)
    r=GA.sc(0)
    for m in range(3):
        am=S(dot(a,e[m+1]))
        for n in range(3):
            r=GA.add(r,GA.scal(H[m][n]*am,e[n+1]))
    return r
trh=sum(S(dot(hmap(e[a]),e[a]))*SQ[a] for a in range(4))   # tr h = sum h(e_a).e^a, e^a = e_a/e_a^2
def Gk(k,a):
    u=hmap(k); Q=S(GA.mul(k,k,SQ))
    t1=GA.add(GA.scal(S(dot(a,k)),GA.sub(u,GA.scal(trh,k))),GA.scal(-Q,hmap(a)),GA.scal(S(dot(a,u)),k))
    return GA.add(GA.scal(F(-1,2),t1),GA.scal(F(1,2)*(S(dot(k,u))-Q*trh),a))
def comp(v,n): return -S(dot(v,e[n+1]))      # v = sum v_n e_n
# lattice symbols: s_i,b_i -> kappa_i, product -> -kappa_i kappa_j
for trial in range(3):
    kap=[F(random.randint(-4,4)) for _ in range(3)]; w=F(random.randint(1,4))
    k=GA.add(GA.scal(w,e[0]),*[GA.scal(kap[i],e[i+1]) for i in range(3)])
    # D symbol
    Dsym=sum(-2*kap[i]*kap[j]*H[i][j] for i in range(3) for j in range(i+1,3)) + sum(kap[kk]**2*H[i][i] for i in range(3) for kk in range(3) if kk!=i)
    tt=S(dot(Gk(k,e[0]),e[0]))
    trH=H[0][0]+H[1][1]+H[2][2]
    Pi=[[F(1,2)*(H[m][n]-(trH if m==n else 0)) for n in range(3)] for m in range(3)]
    Csym=[kap[i]*Pi[i][i]+sum(kap[j]*Pi[i][j] for j in range(3) if j!=i) for i in range(3)]
    G0=Gk(k,e[0]); ts=[comp(G0,n) for n in range(3)]
    # G symbol
    def Gs(i,j):
        if i==j:
            jj,kk=[m for m in range(3) if m!=i]
            return F(1,2)*(-kap[kk]**2*H[jj][jj]-kap[jj]**2*H[kk][kk]) + kap[jj]*kap[kk]*H[jj][kk]
        kk=3-i-j
        return F(1,2)*(kap[kk]**2*H[i][j]-kap[i]*kap[kk]*H[j][kk]-kap[j]*kap[kk]*H[i][kk]+kap[i]*kap[j]*H[kk][kk])
    ss=[[comp(Gk(k,e[a+1]),n) for n in range(3)] for a in range(3)]
    print('tt',tt,'vs -D/2 sym',-Dsym/2,'| ts',ts,'vs w C',[w*c for c in Csym],
          '| ss ok (matrix convention, = -component)?', all(-ss[a][n]==w*w*Pi[a][n]-Gs(a,n) for a in range(3) for n in range(3)),
          [ (ss[a][n], w*w*Pi[a][n]-Gs(a,n)) for a,n in [(0,0),(0,1)]])
