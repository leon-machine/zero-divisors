import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA, time
def mk(L, kernel=False):
    s = tuple(([-1,-1] if kernel else []) + [1,-1]*L); o = 2 if kernel else 0
    mul = lambda x,y: GA.mul(x,y,s)
    v=[GA.add(GA.scal(F(1,2),GA.gen(o+2*j)),GA.scal(F(1,2),GA.gen(o+2*j+1))) for j in range(L)]
    w=[GA.add(GA.scal(F(1,2),GA.gen(o+2*j)),GA.scal(F(-1,2),GA.gen(o+2*j+1))) for j in range(L)]
    n=[mul(v[j],w[j]) for j in range(L)]
    return s,mul,v,w,n
for L in range(1,7):
    t=time.time()
    s,mul,v,w,n=mk(L)
    T={}
    for q in range(1,L):
        rq=GA.add(*[mul(v[j],w[j+q]) for j in range(L-q)])
        rqs=GA.add(*[mul(v[j+q],w[j]) for j in range(L-q)])
        T=GA.add(T,mul(rqs,rq))
    Nn=GA.add(*n) if n else {}
    rhs=GA.sub(GA.add(*[GA.scal(j,n[j]) for j in range(L)]), GA.scal(F(1,2),mul(Nn,GA.sub(Nn,GA.sc(1)))))
    print(L, GA.eq(T,rhs), round(time.time()-t,2))
