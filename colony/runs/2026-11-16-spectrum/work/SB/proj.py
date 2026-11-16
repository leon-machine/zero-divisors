# Projection of slice data on the exact radiation-era solutions (exact rational Laurent series in x = k eta).
from fractions import Fraction as F
N=6
# Laurent series as dict power->coeff
def add(a,b,s=1):
    r=dict(a)
    for k,v in b.items(): r[k]=r.get(k,0)+s*v
    return {k:v for k,v in r.items() if v!=0}
def mul(a,b,cut=8):
    r={}
    for i,u in a.items():
        for j,v in b.items():
            if i+j<=cut: r[i+j]=r.get(i+j,0)+u*v
    return {k:v for k,v in r.items() if v!=0}
def scal(a,c): return {k:v*c for k,v in a.items()}
def xd(a): return {k:v*k for k,v in a.items() if k!=0}  # x d/dx
# growing: sum a_n x^(2n), decaying: sum b_n x^(2n-3)
g={0:F(1)}; a=F(1)
for n in range(1,N):
    a=-a/(3*(2*n)*(2*n+3)); g[2*n]=a
d={-3:F(1)}; b=F(1)
for n in range(1,N):
    b=-b/(3*(2*n-3)*(2*n)); d[2*n-3]=b
def check_ode(p):
    # x^2 P'' + 4 x P' + x^2 P/3 = 0
    xdp=xd(p); x2pp=add(xd(xdp),xdp,-1)
    res=add(add(x2pp,scal(xdp,4)),mul({2:F(1,3)},p))
    return {k:v for k,v in res.items() if k<2*N-4}
print('ode residual g',check_ode(g),'d',check_ode(d))
def R(p): return add(p,scal(add(xd(p),p),F(1,2)))
def D(p): return mul({2:F(-2,3)},p)
Rg,Dg,Rd,Dd=R(g),D(g),R(d),D(d)
def show(n,s): print(n,{k:str(v) for k,v in sorted(s.items()) if k<=3})
show('Phi_g',g);show('Phi_d',d);show('R_g',Rg);show('Delta_g',Dg);show('R_d',Rd);show('Delta_d',Dd)
show('R_g+Delta_g/4',add(Rg,scal(Dg,F(1,4))))
show('R_d+Delta_d/4',add(Rd,scal(Dd,F(1,4))))
# exact projection: A*Rg + c*Rd = Rdat ; A*Dg + c*Dd = Ddat ; A = (Rdat*Dd - Ddat*Rd)/(Rg*Dd - Dg*Rd)
W=add(mul(Rg,Dd),mul(Dg,Rd),-1); show('Wronskian-like det',W)
show('coefficient of Rdat in A*det: Dd',Dd); show('coefficient of Ddat in A*det: -Rd',scal(Rd,-1))
