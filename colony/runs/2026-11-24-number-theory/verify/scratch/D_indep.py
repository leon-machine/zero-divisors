import math
def T(d):
    r2=1-12*(d-0.5)**2; r=math.sqrt(r2); lam=2*math.pi/r
    s=-r2/24
    for k in range(40):
        for a in (k+d, k+1-d):
            x=lam*a
            s+= a*math.exp(-x)/(1+math.exp(-x))
    return s
lo=0.5-1/math.sqrt(12)
for d in [0.215,0.23,0.245,0.25,0.27,0.29,0.31,1/3,0.36,0.40,0.45,0.49,0.5]:
    print(round(d,4), "%.6e"%T(d))
N=200000; prev=None; ch=[]
for i in range(1,N+1):
    d=lo+(0.5-lo)*i/N; v=T(d)
    if prev is not None and (v>0)!=(prev>0): ch.append(round(d,6))
    prev=v
print("sign changes:",ch)
h=1e-4
for d in (0.25,1/3):
    print("T'(%.4f)"%d, (T(d+h)-T(d-h))/(2*h))
print("T''(1/2)", (T(0.5+h)-2*T(0.5)+T(0.5-h))/h**2)
print("max |T| on (0.2145,0.5):", max(abs(T(0.2145+(0.5-0.2145)*i/2000)) for i in range(2001)))
