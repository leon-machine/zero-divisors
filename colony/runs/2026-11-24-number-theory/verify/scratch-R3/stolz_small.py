"""m = 1, 2 cases of the Stolz import by explicit maps (exact integer arithmetic)."""
import itertools
def qm(a, b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
conj=lambda a:(a[0],-a[1],-a[2],-a[3]); I=(0,1,0,0); Jq=(0,0,1,0)
F=lambda v: qm(qm(conj(v),Jq),v)
ok=True
for v in itertools.product(range(-3,4),repeat=4):
    if v==(0,0,0,0): continue
    f=F(v); fi=F(qm(I,v)); n=sum(x*x for x in v)
    ok &= f[0]==0 and fi==tuple(-x for x in f) and sum(x*x for x in f)==n*n
print("m=2: F(v)= conj(v) j v is pure, odd under left mult by i (quarter turn in planes (1,i),(j,k)), |F|=|v|^2:", ok)
# m=1: z -> z^2 on the circle, odd under z -> iz, two components
ok=all(((x*x-y*y),(2*x*y))==tuple(-c for c in ((-y)*(-y)-x*x, 2*(-y)*x)) for x in range(-5,6) for y in range(-5,6))
print("m=1: z^2 odd under quarter turn (so s(1) <= 2; = 2 since S^1 is connected):", ok)
