import sys
sys.path.insert(0,'/home/claude/phys-graph/store/claims/synthesis.kerr-ring-count-misses-area-law'); sys.path.insert(0,'/home/claude/phys-graph/lib')
import types; tp=types.ModuleType('tp_premise'); tp.premise=lambda x:None; sys.modules['tp_premise']=tp
from check import metric, det, gram, pyth
from fractions import Fraction as F
import math
# level-set determinant in u-coordinates: surface r=R(u), R^2 = rho^2 - a^2 u^2
ok=True
for (M,a,rho) in [(F(50),F(2),F(4)),(F(500),F(3),F(10)),(F(9),F(1),F(3)),(F(40),F(7,5),F(13,4))]:
    for (m,n) in [(7,1),(9,1),(12,1),(8,-1),(15,2)]:
        c,s=pyth(m,n)   # R = rho c, a u = rho s
        R=rho*c; u=rho*s/a
        if abs(u)>=1: continue
        g=metric(M,a,R,u)
        Rp=-a*a*u/R
        d=det(gram(g,[[F(1),0,0,0],[F(0),Rp,F(1),F(0)],[F(0),0,0,F(1)]]))
        B=R*(2*M-R)-a*a-(1-u*u)*a**4*u*u/(R*R)
        ok&=(d==rho*rho*B); 
        assert B<=R*(2*M-rho) and B>0
        # constant r slice
        d2=det(gram(g,[[F(1),0,0,0],[F(0),0,F(1),F(0)],[F(0),0,0,F(1)]]))
        S=R*R+a*a*u*u
        ok&=(d2==-S*(R*R-2*M*R+a*a))
print(ok)
# numeric V'
def V(M,a,rho,n=20000):
    tot=0
    for i in range(n):
        u=-1+(i+.5)*2/n
        R=math.sqrt(rho*rho-a*a*u*u)
        B=R*(2*M-R)-a*a-(1-u*u)*a**4*u*u/(R*R)
        tot+=math.sqrt(rho*rho*B)*2/n
    return 2*math.pi*tot
for M in (500.,4000.,1e6):
    rho=(2*M)**(1/3)
    for e in (0.1,0.5,1):
        a=e*rho/2*1; a=math.sqrt(e)*rho/2
        eps=a*a/rho/rho
        V0=4*math.pi*rho**1.5*math.sqrt(2*M-rho)
        print(M,eps, V(M,a,rho)/V0, 1-eps/12, 1-eps/3, (V(M,a,rho)/V0)/math.sqrt(1-a*a/M/M))
