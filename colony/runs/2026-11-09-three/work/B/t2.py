from fractions import Fraction as F
# polynomials in r: list of Fractions, index = power
def trim(p):
    p=list(p)
    while p and p[-1]==0: p.pop()
    return p
def padd(p,q):
    n=max(len(p),len(q)); return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(n)])
def pmul(p,q):
    if not p or not q: return []
    o=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): o[i+j]+=a*b
    return trim(o)
def pder(p): return trim([i*p[i] for i in range(1,len(p))])
def peval(p,x): return sum(c*x**i for i,c in enumerate(p))
class R:  # rational function
    def __init__(s,n,d=None): s.n=trim([F(c) for c in n]); s.d=trim([F(c) for c in (d or [1])])
    def __add__(s,o): return R(padd(pmul(s.n,o.d),pmul(o.n,s.d)),pmul(s.d,o.d))
    def __neg__(s): return R([-c for c in s.n],s.d)
    def __sub__(s,o): return s+(-o)
    def __mul__(s,o): return R(pmul(s.n,o.n),pmul(s.d,o.d))
    def inv(s): return R(s.d,s.n)
    def der(s): return R(padd(pmul(pder(s.n),s.d),[-c for c in pmul(s.n,pder(s.d))]),pmul(s.d,s.d))
    def iszero(s): return not s.n
    def __eq__(s,o): return (s-o).iszero()
    def at(s,x): return peval(s.n,x)/peval(s.d,x)
def c(a): return R([a])
r=R([0,1])
def setup(M,l):
    f=R([-2*M,1],[0,1])
    lam=F((l-1)*(l+2),2)
    Wm=(c(l*(l+1))*r.inv()*r.inv()-c(6*M)*r.inv()*r.inv()*r.inv()); Vm=f*Wm
    den=(c(lam)*r+c(3*M))
    Wp=c(2)*(c(lam*lam*(lam+1))*r*r*r+c(3*lam*lam*M)*r*r+c(9*lam*M*M)*r+c(9*M**3))*(r*r*r*den*den).inv(); Vp=f*Wp
    ft=f*(c(2)*r*den).inv()
    beta=6*M; kap=4*lam*(lam+1)
    return f,lam,Vm,Vp,ft,beta,kap,den,Wm,Wp
for M in (F(1),F(3,7)):
  for l in range(0,7):
    f,lam,Vm,Vp,ft,beta,kap,den,Wm,Wp=setup(M,l)
    ds=lambda g: f*g.der()
    ok1 = (Vp-Vm)==c(2*beta)*ds(ft)
    ok2 = (Vp+Vm)==c(2*beta*beta)*ft*ft+c(2*kap)*ft
    k=F(kap,1)/(2*beta)
    w=c(beta)*ft+c(k)
    ok3 = Vm==(w*w-ds(w)-c(k*k)) and Vp==(w*w+ds(w)-c(k*k))
    hm=Wm.at(2*M)
    try: hp=Wp.at(2*M)
    except ZeroDivisionError: hp='pole'
    print(M,l,ok1,ok2,ok3,'k=',k,'k*12M=',k*12*M,'Vm/f@h *4M^2=',hm*4*M*M,'Vp/f@h*4M^2=',hp*4*M*M if hp!='pole' else hp, 'den root r=',(-3*M/lam if lam else None))
# l=1: static mode 1/r in kernel of RW
M=F(1); f,lam,Vm,Vp,ft,beta,kap,den,Wm,Wp=setup(M,1)
ds=lambda g: f*g.der()
Z=r.inv(); print('l=1 static 1/r solves RW at omega=0:', (ds(ds(Z))-Vm*Z).iszero(), ' in kernel of d+w:', (ds(Z)+ (c(beta)*ft)*Z).iszero())
# sign of Vm for l=1 between 2M and 3M
print('l=1 Vm at 5M/2:',Vm.at(F(5,2)), ' Vp(l=1)==f*2M/r^3:', Vp==f*c(2*M)*r.inv()*r.inv()*r.inv())
