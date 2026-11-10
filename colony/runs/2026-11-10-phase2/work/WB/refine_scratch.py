# SCRATCH (floats). refine third root of thermal test on the ground-test curve
import math
from scan_scratch import T,Sarr,pi
def f(r):
    dl=0.5-math.sqrt((1-r*r)/12); return T(r,dl)
a,b=0.81,0.83
for _ in range(60):
    m=(a+b)/2
    if f(a)*f(m)<=0: b=m
    else: a=m
r=(a+b)/2; dl=0.5-math.sqrt((1-r*r)/12)
print("r*",r,"sqrt(2/3)",math.sqrt(2/3),"delta*",dl,"S",Sarr(r,dl),"S per period",Sarr(r,dl)/r,"cont",pi/6)
print("f at sqrt(2/3):",f(math.sqrt(2/3)))
# derivative sign at r=1 and r=1/2: are they simple roots?
for r0 in (0.5,1.0-1e-9):
    h=1e-4
    print(r0,(f(min(r0+h,1.0))-f(r0-h))/(min(r0+h,1.0)-(r0-h)))
