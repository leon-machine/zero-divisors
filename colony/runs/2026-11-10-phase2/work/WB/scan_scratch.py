# SCRATCH (floats; not evidence). K-W1 and K-W2 scans.
import math
pi=math.pi
def P(y,N=200):  # sum (k+1/2)/(e^{2 pi y (k+1/2)}+1)
    return sum((k+0.5)/(math.exp(min(2*pi*y*(k+0.5),700))+1) for k in range(N))
# K-W1: D(x)*12L/pi = 48 P(1/x) - x^2 ; x = L/beta (window length / thermal length), L fixed
print("K-W1: D(x) in units pi/(12 L)")
for x in [0.05,0.2,0.5,0.8,0.95,1.0,1.05,1.5,2,4,10]:
    d1=48*P(1/x)-x*x; d2=1-48*x*x*P(x)
    print(x, d1, d2)
# Clausius integral: S_arr(x) = lnZ + beta E ; check int beta dD from x=0 (ground) to 1 equals ln2/2 - pi/6
# beta = L/x ; D = (pi/(12L)) d(x) ; beta dD = (pi/(12 x)) d'(x) dx
def d(x): return 1-48*x*x*P(x) if x>0.3 else 48*P(1/x)-x*x
def integral(a,b,n=20000):
    s=0
    h=(b-a)/n
    for i in range(n):
        x0=a+i*h; x1=x0+h; xm=(x0+x1)/2
        s+= (pi/(12*xm))*(d(x1)-d(x0))
    return s
print("Clausius integral 0->1:", integral(1e-6,1.0), " target", 0.5*math.log(2)-pi/6)
# K-W2: tests in (r, delta). units kappa=1, beta=2pi. array weights (k+delta)/r.
def B2(a): return a*a-a+1/6
def Eexc(r,dl,N=400):
    s=0
    for k in range(N):
        for w in ((k+dl)/r,(k+1-dl)/r):
            if w>0: s+= w/(math.exp(min(2*pi*w,700))+1)
            # w==0 contributes 0
    return s
def Sarr(r,dl,N=400):
    s=0
    for k in range(N):
        for w in ((k+dl)/r,(k+1-dl)/r):
            x=2*pi*w
            if x>600: continue
            s+= math.log(1+math.exp(-x))+x/(math.exp(x)+1)
    return s
def G(r,dl): return B2(dl)/(2*r)+r/24      # ground test (zero iff match)
def T(r,dl): return B2(dl)/(2*r)+Eexc(r,dl) # thermal test: symmetric-ordered energy at Hawking T (target 0)
print("K-W2: along ground-test curve delta=1/2-sqrt((1-r^2)/12): thermal test value")
import itertools
prev=None
for i in range(1,201):
    r=i/200
    dl=0.5-math.sqrt(max(0,(1-r*r)/12))
    t=T(r,dl)
    if prev is not None and (prev[1]*t<0 or abs(t)<1e-12): print("  sign change/zero near r=",prev[0],r,prev[1],t)
    prev=(r,t)
    if i%20==0: print(r,dl,t,Sarr(r,dl), "S per thermal period", Sarr(r,dl)/r)
print("check (1/2,1/4):",G(.5,.25),T(.5,.25),Sarr(.5,.25), math.log(2)/4)
print("check (1,1/2):",G(1,.5),T(1,.5),Sarr(1,.5))
# r>1: no real delta from ground test. thermal test alone zero set:
print("thermal-only zeros at delta=1/2 for r in:")
for r in [0.5,0.8,1,1.5,2,3]: print(r,T(r,.5),G(r,.5),Sarr(r,.5)-pi*r/6)
print("delta=0 (periodic), r=1: S=",Sarr(1,1e-12)+0, "T=",T(1,1e-12),"G=",G(1,0.0))
print("variance beta^2 Var per array r=1:", sum(2*(2*pi*(k+.5))**2*math.exp(2*pi*(k+.5))/(math.exp(2*pi*(k+.5))+1)**2 for k in range(50)), pi/6)
