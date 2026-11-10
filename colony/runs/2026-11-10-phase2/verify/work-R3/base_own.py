from decimal import Decimal as D, getcontext
getcontext().prec=60
def pi():
    # Chudnovsky-free: Gauss-Legendre
    a=D(1);b=D(1)/D(2).sqrt();t=D(1)/4;p=D(1)
    for _ in range(8):
        an=(a+b)/2;b=(a*b).sqrt();t-=p*(a-an)**2;a=an;p*=2
    return (a+b)**2/(4*t)
PI=pi(); LN2=D(2).ln()
def modes(r,K=400):
    return [2*PI*(D(k)+D(1)/2)/D(r) for k in range(K) if 2*PI*(D(k)+D(1)/2)/D(r)<160]
def lg(x): return (1+(-x).exp()).ln()
def n(x): return 1/(x.exp()+1)
def f(r): return PI/(12*D(r))+2*sum(lg(x) for x in modes(r))
def e(r): return 2*sum(x*n(x) for x in modes(r))
def S(r): return 2*sum(lg(x)+x*n(x) for x in modes(r))
def v(r): return 2*sum(x*x*n(x)*(1-n(x)) for x in modes(r))
print('pi',PI)
print('1/24 series', sum(D(2*k-1)/(((2*k-1)*PI).exp()+1) for k in range(1,60)) - D(1)/24)
for r in ['2','4','0.5','0.8','0.3']:
    print('dual f',r, f(D(r))-f(1/D(r)))
print('f(1)-ln2/2',f(1)-LN2/2,' c(1)',f(1)-PI/12)
for r in ['1','2','4','8','0.5','0.25']:
    r=D(r); print('r',r,'Delta',S(r)-PI*r/6,' esym',e(r)-PI/(12*r),' D',e(r)-PI*r/12,' v-pi r/6',v(r)-PI*r/6, 'v',v(r))
print('Delta1 closed',LN2/2-PI/6)
for r in [1,2,4]:
    r=D(r); rem=(S(r)-PI*r/6)+2*(PI*r-1)*(-PI*r).exp(); print('rem',r,rem, 3*PI*r*(-2*PI*r).exp())
# variance crossing
lo,hi=D('0.3'),D(1)
for _ in range(60):
    m=(lo+hi)/2
    if v(m)-PI*m/6>0: hi=m
    else: lo=m
print('variance equals continuum at r*=',lo, v(lo)-PI*lo/6)
# Delta monotonic? sample
for r in ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9','1','1.5']:
    r=D(r); print(r, float(S(r)-PI*r/6), float(v(r)-PI*r/6), float((e(r)-PI*r/12)))
print(1/(4*LN2),3/(4*PI),3/(2*PI),3*LN2/PI,6*LN2/PI, 2/(4*S(2)), PI/LN2)
# closed form variance
