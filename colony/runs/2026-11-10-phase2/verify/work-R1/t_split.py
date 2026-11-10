from own import *
def inv2(Am):
    n=len(Am); M=[list(map(F,r))+[F(int(i==j)) for j in range(n)] for i,r in enumerate(Am)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[a/pv for a in M[c]]
        for i in range(n):
            if i!=c and M[i][c]!=0:
                f_=M[i][c]; M[i]=[a-f_*b for a,b in zip(M[i],M[c])]
    return [r[n:] for r in M]
def setup(l):
    A=Alg(tuple([1,-1]*l)); e=[A.g(2*j) for j in range(l)]; f=[A.g(2*j+1) for j in range(l)]
    v=[L((F(1,2),e[j]),(F(1,2),f[j])) for j in range(l)]; w=[L((F(1,2),e[j]),(F(-1,2),f[j])) for j in range(l)]
    return A,e,f,v,w
def adjoint_map(l,Gm):
    """split with form g(v_i,v_j)=Gm (positive definite symmetric): M v_i = sum_k Gm_ik w_k, M w_k = sum_i Ginv_ki v_i"""
    A,e,f,v,w=setup(l); Gi=inv2(Gm)
    Mv=[L(*[(Gm[i][k],w[k]) for k in range(l)]) for i in range(l)]
    Mw=[L(*[(Gi[k][i],v[i]) for i in range(l)]) for k in range(l)]
    Mg={}
    for j in range(l):
        Mg[2*j]=L((1,Mv[j]),(1,Mw[j])); Mg[2*j+1]=L((1,Mv[j]),(-1,Mw[j]))
    def adj(x):
        r={}
        for b,c in x.items():
            t=ONE
            for i in range(2*l):
                if b>>i&1: t=A.mul(Mg[i],t)   # reversed order
            r=L((1,r),(c,t))
        return r
    return A,adj,Mg
# l=1: g(v,v)=G. Proposal: frame t has v'=t v with g(v',v')=1, so g(v,v)=t^-2.
A,e,f,v,w=setup(1)
for t in (F(4),F(2),F(1,3)):
    A_,adj,Mg=adjoint_map(1,[[1/(t*t)]])
    ep=L((t,v[0]),(1/t,w[0])); fp=L((t,v[0]),(-1/t,w[0]))
    print('t=',t,"e'=",ep,"adj fixes e'",adj(ep)==ep,"negates f'",adj(fp)==L((-1,fp)),"e'^2",A.mul(ep,ep),"f'e'==fe",A.mul(fp,ep)==A.mul(f[0],e[0]))
# non-square scale over Q: g=2 gives a split with no rational orthonormal frame
A_,adj,Mg=adjoint_map(1,[[F(2)]])
vp=L((1,v[0]),(1,adj(v[0]))); print('g=2: V+ vector',vp,'Q=',A.mul(vp,vp),'(not a rational square -> no rational unit vector)')
# stored adjoint is G=identity
for l in (1,2):
    A_,adj,Mg=adjoint_map(l,[[F(int(i==j)) for j in range(l)] for i in range(l)])
    print('l=',l,'G=1 gives blade inverse:',all(adj({b:F(1)})==A_.dag({b:F(1)}) for b in range(1<<(2*l))))
# l=2: my own correspondence check: for random positive definite G, adj is an anti-automorphism, involutive, maps W->W', splits V orthogonally
import random; random.seed(3)
A,e,f,v,w=setup(2)
def realdim(l,Gs):
    rows=[]; n=1<<(2*l)
    for Gm in Gs:
        A_,adj,Mg=adjoint_map(l,Gm)
        for b in range(n):
            d=L((1,adj({b:F(1)})),(-1,{b:F(1)}))
            if d: rows.append([d.get(k,0) for k in range(n)])
    return n-rank(rows), rows
Gs=[[[1,0],[0,1]],[[2,1],[1,3]],[[5,-2],[-2,1]],[[F(1,3),0],[0,7]]]
for Gm in Gs:
    A_,adj,Mg=adjoint_map(2,Gm)
    x={3:F(2),4:F(1),9:F(-1)}; y={1:F(1),14:F(3),6:F(5)}
    print('G',Gm,'anti-aut',adj(A.mul(x,y))==A.mul(adj(y),adj(x)),'involution',adj(adj(x))==x,
          'N self-adj',adj(L((1,A.mul(w[0],v[0])),(1,A.mul(w[1],v[1]))))==L((1,A.mul(w[0],v[0])),(1,A.mul(w[1],v[1]))),
          'Mg squares',[A.mul(Mg[i],Mg[i]) == A.mul(A.g(i),A.g(i)) for i in range(4)])
d,rows=realdim(2,Gs); print('l=2 dim of functionals real for my 4 splits:',d)
# is the solution space the span of tau(N^j .)?  functional omega(x)=tau(h x): reality <=> rows . omega =0 where omega coords = omega(blade)
N=L((1,A.mul(w[0],v[0])),(1,A.mul(w[1],v[1])))
for h in (ONE,N,A.mul(N,N)):
    om=[tau(A.mul(h,{b:F(1)})) for b in range(16)]
    print(' N-power functional satisfies all conditions:',all(sum(a*b for a,b in zip(r,om))==0 for r in rows))
print('rank of 1,N,N^2:',rank([[h.get(k,0) for k in range(16)] for h in (ONE,N,A.mul(N,N))]))
d1,_=realdim(2,[[[1,0],[0,1]],[[4,0],[0,1]],[[1,0],[0,9]]]); print('l=2 diagonal splits only: dim',d1,'(claimed 2^l=4)')
d3,_=realdim(3,[[[1,0,0],[0,1,0],[0,0,1]],[[2,1,0],[1,3,1],[0,1,2]],[[1,0,0],[0,4,0],[0,0,9]],[[3,-1,1],[-1,2,0],[1,0,5]]]); print('l=3 dim',d3)
# pair state
c,s=F(3,5),F(4,5); r=c*c-s*s; p=[A.mul(f[j],e[j]) for j in range(2)]
rho=L((F(1,4),A.mul(L((1,ONE),(1,A.mul(p[0],p[1]))),L((1,ONE),(r,p[0])))),(c*s,A.mul(w[0],w[1])),(c*s,A.mul(v[1],v[0])))
print('rho pure proj:',A.mul(rho,rho)==rho, A.dag(rho)==rho, tau(rho))
# split v1'=2 v1: g(v1',v1')=1 -> g(v1,v1)=1/4
A_,adj,Mg=adjoint_map(2,[[F(1,4),0],[0,1]])
ww=A.mul(w[0],w[1])
print('values',4*tau(A.mul(rho,ww)),4*tau(A.mul(rho,adj(ww))))
# positivity failure too? value on x x^{dag_s} for some x
import itertools
neg=None
for _ in range(3000):
    x={b:F(random.randint(-3,3)) for b in random.sample(range(16),4)}
    val=tau(A.mul(rho,A.mul(x,adj(x))))
    if val<0: neg=(x,val);break
print('pair state negative on some x x^{dag_s}:',neg)
