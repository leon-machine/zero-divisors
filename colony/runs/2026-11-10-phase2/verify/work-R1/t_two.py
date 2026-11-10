from own import *
import random
# Cl(2,2): e1=0,f1=1,e2=2,f2=3
A=Alg((1,-1,1,-1)); e1,f1,e2,f2=[A.g(i) for i in range(4)]
p1=A.mul(f1,e1); p2=A.mul(f2,e2); G=A.mul(p1,p2)
X1,Z1,X2,Z2=e1,p1,A.mul(e2,p1),p2
U=A.mul(X1,X2); V=A.mul(Z1,Z2); K=A.mul(e1,f2)
def CH(a1,a2,b1,b2): return L((1,A.mul(a1,L((1,b1),(1,b2)))),(1,A.mul(a2,L((1,b1),(-1,b2)))))
def even(x): return {b:c for b,c in x.items() if not par(b)}
def fn(rho): return lambda x: tau(A.mul(rho,x))
print('--- effects (v) / records (iv)')
B1=L((F(3,5),X2),(F(4,5),Z2)); B2=L((F(4,5),X2),(F(-3,5),Z2))
C=CH(X1,Z1,B1,B2); u=A.mul(e2,f1)
print('U==e2f1',U==u,' E(C)==7/5(u+G)?',even(C)==L((F(7,5),u),(F(7,5),G)))
rho=A.mul(L((1,ONE),(1,U)),L((1,ONE),(1,V)))
print('even state value',fn(rho)(C),' rho even:',all(not par(b) for b in rho),' rho=R R+/4:',A.mul(rho,A.dag(rho))==L((4,rho)))
# record map of B1 on omega, value on X1 Z2
Ea=lambda a,x: L((F(1,2),x),(F(1,2),A.P(a,x,a)))
print('omega∘E_B1 (X1Z2)=',fn(rho)(Ea(B1,A.mul(X1,Z2))),' parity of X1Z2 odd:',all(par(b) for b in A.mul(X1,Z2)))
print('--- records (iii): 256 homogeneous settings')
mx=0
for a1,a2,b1,b2 in iprod(*[[(s,o) for s in (1,-1) for o in range(2)]]*4):
    AA=[X1,Z1];BB=[X2,Z2]
    Cc=CH(L((a1[0],AA[a1[1]])),L((a2[0],AA[a2[1]])),L((b1[0],BB[b1[1]])),L((b2[0],BB[b2[1]])))
    ev=even(Cc); assert set(ev)<=set(U)|set(V)
    mu=sum(abs(c) for c in ev.values()); mx=max(mx,mu)
print('max |mu|+|nu| =',mx)
print('--- records (ii): random mixed observable a = x X1 + z Z1 twisted by conj; find even state made non-even')
# general observables: conjugate a blade observable by a random invertible "rotor" exp-like: a = g s g^-1 need self-adjoint; use a = cos-like combos
tests=[L((F(3,5),X1),(F(4,5),Z1)), L((F(5,13),A.mul(X1,Z2)),(F(12,13),V)), L((F(3,5),U),(F(4,5),V)), L((F(3,5),X2),(F(4,5),A.mul(X1,X2)))]
evs=[b for b in range(16) if not par(b) and A.bm(b,b)[0]==1 and b]
for a in tests:
    sa=A.dag(a)==a and A.mul(a,a)==ONE
    hom= all(par(b) for b in a) or all(not par(b) for b in a)
    breaks=False
    for s in evs:
        for sg in (1,-1):
            r=L((1,ONE),(sg,{s:F(1)}))
            for o in [b for b in range(16) if par(b)]:
                if fn(r)(Ea(a,{o:F(1)}))!=0: breaks=True
    print('observable',sa,'homogeneous',hom,'breaks evenness',breaks)
print('--- local weights')
C0=CH(X1,Z1,X2,Z2); box=L((1,ONE),(1,C0))
b=L((F(3,5),X2),(F(4,5),Z2))
print('box(C0)',fn(box)(C0),'box(X1 b)',fn(box)(A.mul(X1,b)),'weight',fn(box)(L((F(1,4),A.mul(L((1,ONE),(1,X1)),L((1,ONE),(-1,b)))))))
print('UV==-K',A.mul(U,V)==L((-1,K)),'VU==UV',A.mul(U,V)==A.mul(V,U),' K = -(X1Z1)(X2Z2):',K==L((-1,A.P(X1,Z1,X2,Z2))))
loc=[A.mul(s,t) for s in (ONE,X1,Z1) for t in (ONE,X2,Z2)]
for c in (F(-1),F(0),F(1),F(5,7),F(-3)):
    M=L((1,ONE),(-1,U),(-1,V),(c,K)); lam=fn(M)
    vals=[lam(x) for x in loc]
    tab={(uu,vv):lam(L((F(1,4),A.mul(L((1,ONE),(uu,U)),L((1,ONE),(vv,V)))))) for uu in (1,-1) for vv in (1,-1)}
    # positivity: Gram matrix of (x,y)->lam(x y+) minimal check via negative table entry or psd by exact LDL
    Gm=[[lam(A.mul({i:F(1)},A.dag({j:F(1)}))) for j in range(16)] for i in range(16)]
    def psd(Mx):
        Mx=[r[:] for r in Mx]; n=len(Mx)
        for i in range(n):
            if Mx[i][i]<0: return False
            if Mx[i][i]==0:
                if any(Mx[i][j]!=0 for j in range(n)): return False
                continue
            for j in range(i+1,n):
                f_=Mx[j][i]/Mx[i][i]
                if f_!=0: Mx[j]=[a-f_*b_ for a,b_ in zip(Mx[j],Mx[i])]
            for j in range(i+1,n): Mx[j][i]=0
        return True
    sym=all(Gm[i][j]==Gm[j][i] for i in range(16) for j in range(16))
    odd0=all(lam({o:F(1)})==0 for o in range(16) if par(o))
    # (L) on rational directions
    okL=True
    for s_ in range(-6,7):
        for t_ in range(-6,7):
            xa,za=F(1-s_*s_,1+s_*s_),F(2*s_,1+s_*s_); xb,zb=F(1-t_*t_,1+t_*t_),F(2*t_,1+t_*t_)
            a=L((xa,X1),(za,Z1)); bb=L((xb,X2),(zb,Z2))
            for sa_ in (1,-1):
              for sb_ in (1,-1):
                w=lam(L((F(1,4),A.mul(L((1,ONE),(sa_,a)),L((1,ONE),(sb_,bb))))))
                okL&=(w>=0) and w==F(1,4)*(1-sa_*sb_*(xa*xb+za*zb))
    print('c=',c,'local vals',vals,'lam(K)',lam(K),'table',list(tab.values()),'Gram symmetric',sym,'PSD(P)',psd(Gm),'even',odd0,'(L)',okL)
print('box Gram PSD?',psd([[fn(box)(A.mul({i:F(1)},A.dag({j:F(1)}))) for j in range(16)] for i in range(16)]))
# descents
def EN(x):
    return L(*[(F(1,4),A.P(g,x,g)) for g in (ONE,p1,p2,G)])
def ET(x): return L((F(1,2),x),(F(1,2),A.P(G,x,G)))
for nm,M in [('box',box)]+[('c=%s'%c,L((1,ONE),(-1,U),(-1,V),(c,K))) for c in (F(-1),F(2))]:
    # functional lam∘E_N has density E_N(M) (E_N self-dual for tau)
    print(nm,'E_N density',EN(M)==L((1,ONE),(-1,V)),' E_T density',ET(M))
y=L((F(1,4),A.mul(L((1,ONE),(-1,U)),L((1,ONE),(1,V)))))
print('box∘E on y:',tau(A.mul(ET(box),y)),' y proj:',A.mul(y,y)==y and A.dag(y)==y)
print('--- PM square')
sq=[[X1,X2,U],[Z2,Z1,V],[A.mul(X1,Z2),A.mul(Z1,X2),A.mul(U,V)]]
print('rows',[A.P(*r) for r in sq],'cols',[A.P(sq[0][t],sq[1][t],sq[2][t]) for t in range(3)])
print('commute rows/cols',all(A.mul(a,b)==A.mul(b,a) for t in range(3) for a in sq[t] for b in sq[t]) and all(A.mul(sq[i][t],sq[j][t])==A.mul(sq[j][t],sq[i][t]) for t in range(3) for i in range(3) for j in range(3)), 'sa sq1',all(A.dag(o)==o and A.mul(o,o)==ONE for r in sq for o in r))
