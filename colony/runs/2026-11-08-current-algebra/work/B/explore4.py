from explore2_lib import *
import sys
n,L=int(sys.argv[1]),int(sys.argv[2])
M,idx,CD,C,jcur=setup(n,L)
num={k:mul(CD[k],C[k]) for k in CD}
N=add(*[num[k] for k in num])
def ec(s,d):
    return all((s>>idx(x,j)&1) and not (s>>idx(x,L-1-j)&1) for x in range(n) for j in range(d))
B={}
for q in range(1,L):
    J0=add(*[jcur(x,x,q) for x in range(n)]); B=add(B,mul(dag(J0),J0))
for q in range(1,L):
    for which,Ja in (('j01_q',jcur(0,1,q)),('j01_q*',dag(jcur(0,1,q))),('j00-j11_q',add(jcur(0,0,q),jcur(1,1,q),coeffs=[1,-1]))):
        cm=comm(B,Ja)
        out=[]
        for d in range(0,L//2+1):
            bad=sum(1 for (o,i),v in cm.items() if ec(i,d))
            out.append((d,bad))
        print(q,which,out)
