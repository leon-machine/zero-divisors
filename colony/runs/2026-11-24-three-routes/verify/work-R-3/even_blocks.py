import sys; sys.path.insert(0,'/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import combinations
import GA
def M(x,y,sq): return GA.mul(x,y,sq)
def inv_dag(x,sq):
    # adjoint = linear extension of blade inverse, computed as rev(b)/(b rev(b))
    out={}
    for b,c in x.items():
        r=GA.reverse({b:F(1)}); s=M({b:F(1)},r,sq)[()]
        for bb,cc in r.items(): out[bb]=out.get(bb,F(0))+c*cc/s
    return {b:c for b,c in out.items() if c}
def rank(rows):
    rows=[list(r) for r in rows]; rk=0; ncol=len(rows[0]) if rows else 0
    for c in range(ncol):
        p=next((i for i in range(rk,len(rows)) if rows[i][c]!=0),None)
        if p is None: continue
        rows[rk],rows[p]=rows[p],rows[rk]
        for i in range(len(rows)):
            if i!=rk and rows[i][c]!=0:
                f=rows[i][c]/rows[rk][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[rk])]
        rk+=1
    return rk
def run(l):
    sq=tuple([1,-1]*l); one={():F(1)}
    e=[GA.gen(2*j) for j in range(l)]; f=[GA.gen(2*j+1) for j in range(l)]
    v=[GA.scal(F(1,2),GA.add(e[j],f[j])) for j in range(l)]
    w=[GA.scal(F(1,2),GA.sub(e[j],f[j])) for j in range(l)]
    P0=one
    for j in range(l): P0=M(P0,M(w[j],v[j],sq),sq)
    subs=[s for k in range(l+1) for s in combinations(range(l),k)]
    S=[]
    for I in subs:
        x=one
        for j in I: x=M(x,v[j],sq)
        S.append(M(x,P0,sq))
    G=one
    for j in range(l): G=M(G,M(e[j],f[j],sq),sq)
    assert GA.eq(M(G,G,sq),one) and GA.eq(inv_dag(G,sq),G)
    blades=GA.all_blades(2*l)
    # commutant of G: kernel of x -> Gx - xG
    img=[GA.basis_vector_of(GA.sub(M(G,{b:F(1)},sq),M({b:F(1)},G,sq)),blades) for b in blades]
    kdim=len(blades)-rank(img)
    evens=[b for b in blades if len(b)%2==0]
    assert all(GA.eq(M(G,{b:F(1)},sq),M({b:F(1)},G,sq)) for b in evens)
    assert kdim==len(evens)==2*4**(l-1), (kdim,len(evens))
    for i,I in enumerate(subs): assert GA.eq(M(G,S[i],sq),GA.scal((-1)**len(I),S[i]))
    def mat(x):
        return [[ (M(M(inv_dag(S[i],sq),x,sq),S[j],sq).get((),F(0))/P0[()]) for j in range(len(S))] for i in range(len(S))]
    # check s_I^dag x s_J is exactly that multiple of P0
    allm=[]
    for b in blades:
        x={b:F(1)}; m=mat(x)
        for i in range(len(S)):
            for j in range(len(S)):
                assert GA.eq(M(M(inv_dag(S[i],sq),x,sq),S[j],sq),GA.scal(m[i][j],P0))
        md=mat(inv_dag(x,sq))
        assert all(md[i][j]==m[j][i] for i in range(len(S)) for j in range(len(S)))
        par=len(b)%2
        for i,I in enumerate(subs):
            for j,J in enumerate(subs):
                if (len(I)+len(J))%2!=par: assert m[i][j]==0
        allm.append([c for row in m for c in row])
    assert rank(allm)==4**l
    assert rank([allm[k] for k,b in enumerate(blades) if len(b)%2==0])==2*4**(l-1)
    for sgn in (1,-1):
        B=GA.scal(F(1,2),GA.add(one,GA.scal(sgn,G))); mb=mat(B)
        assert all(mb[i][j]==(1 if i==j and (-1)**len(subs[i])==sgn else 0) for i in range(len(S)) for j in range(len(S)))
    print('l=%d ok: commutant dim %d, blocks of size %d, adjoint = transpose'%(l,kdim,2**(l-1)))
    return sq,S,P0,G,subs,mat
if __name__=='__main__':
    run(2); sq,S,P0,G,subs,mat=run(3)
    # non-uniqueness of the state extension without "vanishes on odd": a=s_{} (block +), b=s_{0} (block -)
    y=GA.add(S[0],S[1])   # subs[0]=(), subs[1]=(0,)
    print('subs',subs[0],subs[1])
    def omega_p(x):  # vector state of (s_a+s_b)/sqrt2 : (1/2) sum m_IJ over I,J in {a,b}
        m=mat(x); return F(1,2)*(m[0][0]+m[1][1]+m[0][1]+m[1][0])
    def omega_e(x):
        m=mat(x); return F(1,2)*(m[0][0]+m[1][1])
    e1=GA.gen(0)
    print('odd e_1: extension-with-cross-terms',omega_p(e1),' even-only',omega_e(e1))
    import random; random.seed(1)
    for t in range(30):
        x={b:F(random.randint(-3,3)) for b in GA.all_blades(6) if len(b)%2==0 and random.random()<0.3}
        assert omega_p(x)==omega_e(x)
        z={b:F(random.randint(-3,3)) for b in GA.all_blades(6) if random.random()<0.2}
        from even_blocks import inv_dag as d
        assert omega_p(M(z,inv_dag(z,sq),sq))>=0
    print('both are states agreeing on even elements; differ on e_1')
