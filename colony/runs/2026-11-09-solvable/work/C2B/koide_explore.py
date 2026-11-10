from fractions import Fraction as F
SC=10**12
def isqrt(n):
    x=int(n)
    if x==0: return 0
    r=1<<((x.bit_length()+1)//2)
    while True:
        y=(r+x//r)//2
        if y>=r: return r
        r=y
def sb(q):
    n=(F(q)*SC*SC).__floor__(); lo=isqrt(n); return F(lo,SC),F(lo+1,SC)
def gt(m):
    hi=sum(sb(x)[1] for x in m); return 3*sum(m)>2*hi*hi
def lt(m):
    lo=sum(sb(x)[0] for x in m); return 3*sum(m)<2*lo*lo
def qf(m):
    s=[float(sb(x)[0]) for x in m]; return sum(m)/sum(s)**2
sets={'down':[F('0.00470'),F('0.0935'),F('4.18')],'downMZ':[F('0.00290'),F('0.055'),F('2.89')],
 'up':[F('0.00216'),F('1.2730'),F('172.57')],'upMZ':[F('0.00127'),F('0.619'),F('171.7')]}
for k,m in sets.items():
    print(k,'Q=',float(qf(m)))
    for name,f in [('R1',lambda R:[R*m[0],m[1],m[2]]),('R2',lambda R:[m[0],R*m[1],m[2]]),('R12',lambda R:[R*m[0],R*m[1],m[2]])]:
        lo,hi=F(1),F(10**5)
        for _ in range(80):
            mid=(lo+hi)/2
            if gt(f(mid)): lo=mid
            else: hi=mid
        print('  ',name,float(lo), 'Rm1<=m3/9?', float(lo*m[0]), float(m[2]/9), float(lo*m[1]) if name!='R1' else '')
    r=m[1]/m[2]; print('  m2/m3=',float(r),' t*^2=',17/2-6*2**0.5, ' below?', 72 < (F(17,2)-r)**2 and r< F(17,2)-r*0)
print('---- corrected')
for k,m in sets.items():
    for name,f in [('R1',lambda R:[R*m[0],m[1],m[2]]),('R2',lambda R:[m[0],R*m[1],m[2]]),('R12',lambda R:[R*m[0],R*m[1],m[2]])]:
        hi=None; R=F(1)
        while R<10**6:
            if lt(f(R)): hi=R; break
            R=R*F(11,10)
        if hi is None: print(k,name,'no Koide'); continue
        lo=F(1)
        for _ in range(60):
            mid=(lo+hi)/2
            if gt(f(mid)): lo=mid
            else: hi=mid
        print(k,name,float(lo), 'R m1 vs m3/9', float(lo*m[0]), float(m[2]/9), float(lo*m[1]))
