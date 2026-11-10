from decimal import Decimal as D, getcontext
import math
getcontext().prec=50
def pi():
    a=D(1);b=D(1)/D(2).sqrt();t=D(1)/4;p=D(1)
    for _ in range(8):
        an=(a+b)/2;b=(a*b).sqrt();t-=p*(a-an)**2;a=an;p*=2
    return (a+b)**2/(4*t)
PI=pi(); LN2=D(2).ln()
def s(x):
    x=abs(x)
    if x>110: return D(0)
    return (1+(-x).exp()).ln()+x/(x.exp()+1)
def S(d,r,K=80): return sum(s(2*PI*(D(k)+d)/r) for k in range(-K,K))
def Ex(d,r,K=80):  # sum |x| n(|x|)
    t=D(0)
    for k in range(-K,K):
        x=abs(2*PI*(D(k)+d)/r)
        if 0<x<110: t+=x/(x.exp()+1)
    return t
def B2(a): return a*a-a+D(1)/6
for d in ['0','0.24','0.25','0.5']:
    print('S_delta(1)',d,S(D(d),D(1)))
print('S_1/6',S(D(1)/6,D(1)),' pi/6',PI/6)
# twist 1/3
r=(D(2)/3).sqrt(); d=D(1)/3
print('S(1/3,sqrt(2/3))',S(d,r),' per period',S(d,r)/r,' ln2/S',LN2/S(d,r))
for (rr,dd) in [(D(1),D('0.5')),(D('0.5'),D('0.25')),(r,d)]:
    print('thermal test beta*E_sym', Ex(dd,rr)+PI/rr*B2(dd), ' ground', B2(dd)/(2*rr)+rr/24, 'S',S(dd,rr))
# eta-quotient check of Phi_1/3 invariance, float
def lneta(t): # tau = i t
    q=math.exp(-2*math.pi*t); return -2*math.pi*t/24+sum(math.log(1-q**n) for n in range(1,200))
def lnPhi3(sg): return lneta(2*sg)+lneta(3*sg)-lneta(sg)-lneta(6*sg)
for sg in (0.2,0.5,1/math.sqrt(6)): print('Phi_1/3 fricke',lnPhi3(sg)-lnPhi3(1/(6*sg)), lnPhi3(sg))
# scan along conic (float)
def tval(r):
    dl=0.5-math.sqrt((1-r*r)/12)
    t=0.5*(dl*dl-dl+1/6)
    for k in range(60):
        for w in (k+dl,k+1-dl):
            a=2*math.pi*w/r
            if a<700: t+=w/(math.exp(a)+1)
    return t
prev=None; zs=[]
N=20000
for i in range(1,N):
    r=i/N; v=tval(r)
    if prev is not None and (v==0 or prev*v<0): zs.append(r)
    prev=v
print('sign changes on conic near r=',zs, ' tval(0.999)',tval(0.999),'tval(0.9)',tval(0.9),'tval(0.7)',tval(0.7),'tval(0.3)',tval(0.3),'tval(0.05)',tval(0.05))
# monotonic S_delta(1) on [0,1/2]
vals=[float(S(D(i)/200,D(1),K=20)) for i in range(0,101)]
print('monotone decreasing on [0,1/2]:',all(vals[i]>vals[i+1] for i in range(100)), vals[0],vals[-1])
