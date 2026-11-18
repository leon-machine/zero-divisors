import sys
sys.path.insert(0,'/home/claude/phys-graph/lib')
from fractions import Fraction as F
from itertools import product
import GA
from GA import mul, add, sub, scal, gen, dot
S=GA.sig(1,3); eta=[1,-1,-1,-1]
e=[gen(i) for i in range(4)]
I4=mul(mul(mul(e[0],e[1],S),e[2],S),e[3],S)
def vec(c): return {(i,):F(x) for i,x in enumerate(c) if x}
def d(a,b): return dot(a,b,S)
def s0(x): return x.get((),F(0))
def comp(T):  # T: vector->vector ; components T_{mu nu} = e_mu . T(e_nu)
    return [[d(e[m],T(e[n])) for n in range(4)] for m in range(4)]
def Tscalar(p,q,xi=F(0)):
    k=add(p,q); k2=d(k,k)
    return comp(lambda a: add(scal(-d(a,q),p),scal(-d(a,p),q),scal(d(p,q),a),scal(2*xi*d(a,k),k),scal(-2*xi*k2,a)))
def wedge(a,b): return scal(F(1,2),sub(mul(a,b,S),mul(b,a,S)))
def Tvec(F1,F2):
    def T(a):
        x=add(mul(mul(F1,a,S),F2,S),mul(mul(F2,a,S),F1,S))
        return {b:-c/2 for b,c in x.items() if len(b)==1}
    return comp(T)
def reduce_(T):  # R = T - 1/2 eta tr T (lower indices)
    tr=sum(eta[m]*T[m][m] for m in range(4))
    return [[T[m][n]-F(1,2)*(eta[m] if m==n else 0)*tr for n in range(4)] for m in range(4)]
def con(A,B): return sum(eta[m]*eta[n]*A[m][n]*B[m][n] for m in range(4) for n in range(4))
# source "density" of a pair state: list of (T, weight) for real pieces, plus for Weyl the S and A tensors
def scalar_pair(p,q,xi=F(0)): return ('real',[Tscalar(p,q,xi)])
def vector_pair(p,q):
    # polarisations: e2 and the unit vector in the 1-3 plane orthogonal to p's spatial direction
    pc=[d(e[m],p)*eta[m] for m in range(4)]   # contravariant components
    n=vec([0,pc[3],0,-pc[1]])
    assert d(n,p)==0 and d(n,q)==0 and d(n,n)==-1
    pol=(n,e[2])
    return ('real',[Tvec(wedge(p,a1),wedge(q,a2)) for a1 in pol for a2 in pol])
def weyl_pair(p,q):
    dd=sub(p,q); dc=[d(e[m],dd) for m in range(4)]
    XS=[[2*s0(mul(mul(mul(q,e[m],S),p,S),e[r],S)) for r in range(4)] for m in range(4)]
    XA=[[2*s0(mul(mul(mul(mul(q,e[m],S),p,S),e[r],S),I4,S)) for r in range(4)] for m in range(4)]
    return ('weyl',dc,XS,XA)
def sumsq(src1,src2,sign=1):
    # returns sum over polarisations of |T1 : R2|^2
    if src1[0]=='real' and src2[0]=='real':
        return sum(con(T1,reduce_(T2))**2 for T1 in src1[1] for T2 in src2[1])
    if src1[0]=='weyl' and src2[0]=='real':
        _,dc,XS,XA=src1; tot=0
        for T2 in src2[1]:
            R=reduce_(T2)
            # M = 1/4 * 2 * vbar gamma^mu u * R_{mu nu} d^nu  -> w_mu = R_{mu nu} d^nu (index raised on d)
            w=[sum(R[m][n]*eta[n]*dc[n] for n in range(4)) for m in range(4)]
            tot+=F(1,4)*sum(eta[m]*eta[r]*w[m]*w[r]*XS[m][r] for m in range(4) for r in range(4))
        return tot
    if src1[0]=='real' and src2[0]=='weyl':
        return sumsq(src2,src1)
    # weyl-weyl: M = (1/16) sum over sym structures; T1_{mu nu}=1/4 (g_mu d_nu + g_nu d_mu), same for 2
    _,d1,S1,A1=src1; _,d2,S2,A2=src2
    # T1:R2 with T2 traceless: = (1/16) * [ 2 (d1.d2) g1.g2 + 2 (g1.d2)(g2.d1) ] = 1/8[(d1.d2) g1.g2 + g1.d2 g2.d1]
    d1d2=sum(eta[m]*d1[m]*d2[m] for m in range(4))
    up=lambda v:[eta[m]*v[m] for m in range(4)]
    d1u,d2u=up(d1),up(d2)
    def quad(X1,X2):
        # sum_{mu,rho,alpha,beta} C^{mu alpha} C^{rho beta} X1_{mu rho} X2_{alpha beta}, with C^{mu alpha}= d1d2 eta^{mu alpha} + d2^mu d1^alpha
        tot=0
        Cm=[[d1d2*(eta[m] if m==a else 0)+d2u[m]*d1u[a] for a in range(4)] for m in range(4)]
        for m in range(4):
            for a in range(4):
                if Cm[m][a]==0: continue
                for r in range(4):
                    for b in range(4):
                        if Cm[r][b]==0: continue
                        tot+=Cm[m][a]*Cm[r][b]*X1[m][r]*X2[a][b]
        return tot
    return F(1,64)*(quad(S1,S2)-sign*quad(A1,A2))
def kin(c,s_):
    return vec([1,0,0,1]),vec([1,0,0,-1]),vec([1,s_,0,c]),vec([1,-s_,0,-c])
pts=[(F(3,5),F(4,5)),(F(5,13),F(12,13)),(F(-7,25),F(24,25)),(F(-8,17),F(15,17)),(F(20,29),F(21,29)),(F(-12,37),F(35,37)),(F(9,41),F(40,41))]
def fit_and_integrate(vals):
    # vals: list of (c, value); fit polynomial of degree len-1 and integrate over [-1,1]
    n=len(vals)
    M=[[c**k for k in range(n)] for c,_ in vals]; rhs=[v for _,v in vals]
    for i in range(n):
        piv=next(r for r in range(i,n) if M[r][i]!=0); M[i],M[piv]=M[piv],M[i]; rhs[i],rhs[piv]=rhs[piv],rhs[i]
        for r in range(n):
            if r!=i and M[r][i]!=0:
                f=M[r][i]/M[i][i]; M[r]=[a-f*b for a,b in zip(M[r],M[i])]; rhs[r]-=f*rhs[i]
    co=[rhs[i]/M[i][i] for i in range(n)]
    integ=sum(co[k]*(F(2,k+1) if k%2==0 else 0) for k in range(n))
    return co,integ
kinds={'s':lambda p,q:scalar_pair(p,q),'w':weyl_pair,'v':vector_pair}
cw={'s':1,'w':3,'v':12}; sym={'s':F(1,2),'w':F(1),'v':F(1,2)}
for a in 'swv':
    for b in 'swv':
        for sign in ((1,-1) if a==b=='w' else (1,)):
            vals=[]
            for (c,s_) in pts:
                p1,p2,p3,p4=kin(c,s_)
                vals.append((c,sumsq(kinds[a](p1,p2),kinds[b](p3,p4),sign)/F(4)**4))  # s=4 -> divide by s^4
            co,integ=fit_and_integrate(vals)
            W=integ*2*sym[a]*sym[b]   # times pi
            pred=F(cw[a]*cw[b],180)+(F(5,180) if a==b=='s' else 0)
            print(a,b,sign,'coeffs',[str(x) for x in co],' W/pi=',W,' pred',pred, W==pred)
