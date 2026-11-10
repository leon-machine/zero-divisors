# scratch (floats allowed here; not evidence)
import math as m
pi=m.pi
def s(x): return m.log1p(m.exp(-x))+x/(m.exp(x)+1) if x<700 else 0.0
def nF(x): return 1/(m.exp(x)+1) if x<700 else 0.0
def arr(r,d,K=400):
    S=E=V=lnZa=0.0
    for k in range(-K,K):
        x=2*pi*(k+d)/r; ax=abs(x)
        if ax==0: S+=m.log(2); lnZa+=m.log(2); continue
        S+=s(ax); E+=ax*nF(ax); V+=ax*ax*nF(ax)*(1-nF(ax)); lnZa+=m.log1p(m.exp(-ax)) if ax<700 else 0
    B2=d*d-d+1/6
    sea=(pi/r)*B2 if d>0 else (2*pi/r)/12
    return lnZa-sea, E, E+sea, S, V
for r in [.25,.5,1,2,3,4,8]:
    lnZ,Ea,Es,S,V=arr(r,.5)
    dual=2*sum(m.log1p(m.exp(-2*pi*r*(n-.5)))-2*pi*r*(n-.5)*nF(2*pi*r*(n-.5)) for n in range(1,60))
    print('r',r,'lnZ %.12f Ea-pi r/12 %.3e Esym %.10f S-pi r/6 %.12f dual %.12f V %.10f V-pi r/6 %.3e'%(lnZ,Ea-pi*r/12,Es,S-pi*r/6,dual,V,V-pi*r/6), 'lead %.6f'%(-2*(pi*r-1)*m.exp(-pi*r)))
print('closed var', pi**4/(24*m.gamma(.75)**8), 'half ln2',m.log(2)/2, 'lnZ(2) closed', -m.log(2)/8+m.log(2+m.sqrt(2))/2)
def th(r):
    q=m.exp(-pi*r)
    t3=sum(q**(n*n) for n in range(-40,41)); t4=sum((-1)**n*q**(n*n) for n in range(-40,41)); t2=sum(q**((n+.5)**2) for n in range(-40,41))
    return t2,t3,t4
for r in [.5,1,2,3]:
    t2,t3,t4=th(r); print('theta E %.12f direct %.12f'%(pi*r/12*(t4**4-t2**4), arr(r,.5)[2]))
def simpson(f,a,b,n=400):
    h=(b-a)/n; return h/3*(f(a)+f(b)+4*sum(f(a+(2*i-1)*h) for i in range(1,n//2+1))+2*sum(f(a+2*i*h) for i in range(1,n//2)))
for r in [1,2,.5]:
    for i,name,target in [(3,'S',pi*r/6),(1,'Eabove',pi*r/12),(4,'Var',pi*r/6),(2,'Esym',pi*r/12)]:
        val=simpson(lambda d:arr(r,d if d>0 else 1e-12,80)[i],0,1)
        print('r',r,name,'%.10f %.10f'%(val,target))
for d in [1e-9,.1,.2,.25,.3,.4,.5]:
    a=arr(1,d); print(d, 'S %.8f Eabove %.8f Esym %.8f Var %.6f'%(a[3],a[1],a[2],a[4]))
lo,hi=.2,.3
for _ in range(60):
    mid=(lo+hi)/2
    if arr(1,mid)[3]>pi/6: lo=mid
    else: hi=mid
print('twist with S=pi/6 at r=1:',lo)
print('thirdnum', m.log(m.sinh(pi)/pi)/6, 'pi/6',pi/6,'3/(4pi)',3/(4*pi),'1/(4ln2)',1/(4*m.log(2)),'6ln2/pi',6*m.log(2)/pi)
