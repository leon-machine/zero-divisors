"""R1 independent recomputation: phase symmetries of M_u = a1 Y + a2 Yt, M_d = conj(a2) Y + conj(a1) Yt
(Phi_1 = alpha, Phi_2 = conj beta). Own Gaussian-rational arithmetic and own elimination."""
from fractions import Fraction as Fr
from itertools import product

class C:
    __slots__=("r","i")
    def __init__(s,r=0,i=0): s.r=Fr(r); s.i=Fr(i)
    def __add__(s,o): o=cc(o); return C(s.r+o.r,s.i+o.i)
    __radd__=__add__
    def __sub__(s,o): o=cc(o); return C(s.r-o.r,s.i-o.i)
    def __mul__(s,o): o=cc(o); return C(s.r*o.r-s.i*o.i, s.r*o.i+s.i*o.r)
    __rmul__=__mul__
    def conj(s): return C(s.r,-s.i)
    def __eq__(s,o): o=cc(o); return s.r==o.r and s.i==o.i
    def __repr__(s): return f"({s.r}{'+' if s.i>=0 else ''}{s.i}i)"
def cc(x): return x if isinstance(x,C) else C(x)
I=C(0,1)
def Z(n,m=None): m=n if m is None else m; return [[C() for _ in range(m)] for _ in range(n)]
def mm(A,B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))),C()) for j in range(len(B[0]))] for i in range(len(A))]
def ma(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def ms(c,A): return [[c*x for x in r] for r in A]
def T(A): return [list(r) for r in zip(*A)]
def tr(A): return sum((A[i][i] for i in range(len(A))),C())
def det(A):
    n=len(A)
    if n==1: return A[0][0]
    t=C()
    for j in range(n):
        mn=[r[:j]+r[j+1:] for r in A[1:]]
        t=t+(C(-1) if j%2 else C(1))*A[0][j]*det(mn)
    return t
def mat(rows): return [[cc(x) for x in r] for r in rows]

def ah_basis(n):
    out=[]
    for a in range(n):
        M=Z(n); M[a][a]=I; out.append(M)
    for a in range(n):
        for b in range(a+1,n):
            M=Z(n); M[a][b]=C(1); M[b][a]=C(-1); out.append(M)
            M=Z(n); M[a][b]=I; M[b][a]=I; out.append(M)
    return out

def kernel(rows,ncol):
    rows=[r[:] for r in rows]; piv=[]; r0=0
    for c in range(ncol):
        p=next((i for i in range(r0,len(rows)) if rows[i][c]!=0),None)
        if p is None: continue
        rows[r0],rows[p]=rows[p],rows[r0]
        pv=rows[r0][c]; rows[r0]=[x/pv for x in rows[r0]]
        for i in range(len(rows)):
            if i!=r0 and rows[i][c]!=0:
                f=rows[i][c]; rows[i]=[a-f*b for a,b in zip(rows[i],rows[r0])]
        piv.append(c); r0+=1
    free=[c for c in range(ncol) if c not in piv]; ker=[]
    for f in free:
        v=[Fr(0)]*ncol; v[f]=Fr(1)
        for i,c in enumerate(piv): v[c]=-rows[i][f]
        ker.append(v)
    return ker

def symmetries(Y,Yt):
    n=len(Y); bn=ah_basis(n); b2=ah_basis(2)
    # build the linear map: unknown vector -> (dMu coefficient of Phi1, Phi2; dMd coefficient of conjPhi1, conjPhi2)
    # M_u = Phi1 Y + Phi2 Yt ; M_d = conj(Phi2) Y + conj(Phi1) Yt
    A={1:Y,2:Yt}; Bc={1:Yt,2:Y}   # M_d = sum_j conj(Phi_j) Bc[j]
    cols=[]
    def blocks(KQ,Ku,Kd,KP):
        out=[]
        for j in (1,2):
            up=ma(mm(T(KQ),A[j]),mm(A[j],Ku))
            for i in (1,2): up=ma(up,ms(KP[i-1][j-1],A[i]))
            dn=ma(mm(T(KQ),Bc[j]),mm(Bc[j],Kd))
            for i in (1,2): dn=ma(dn,ms(KP[i-1][j-1].conj(),Bc[i]))
            out+= [up,dn]
        return out
    z=Z(n); z2=Z(2)
    gens=[]
    for K in bn: gens.append((K,z,z,z2))
    for K in bn: gens.append((z,K,z,z2))
    for K in bn: gens.append((z,z,K,z2))
    for K in b2: gens.append((z,z,z,K))
    for g in gens:
        bl=blocks(*g); col=[]
        for M in bl:
            for r in M:
                for x in r: col+= [x.r,x.i]
        cols.append(col)
    rows=[list(r) for r in zip(*cols)]
    ker=kernel(rows,len(gens))
    res=[]
    for v in ker:
        KQ=Z(n);Ku=Z(n);Kd=Z(n);KP=Z(2)
        for coef,(a,b,c,d) in zip(v,gens):
            KQ=ma(KQ,ms(C(coef),a));Ku=ma(Ku,ms(C(coef),b));Kd=ma(Kd,ms(C(coef),c));KP=ma(KP,ms(C(coef),d))
        S=tr(KQ)*2+tr(Ku)+tr(Kd)
        res.append((S.i,KP[0][0].i-KP[1][1].i))
    return res

if __name__=="__main__":
    n=3
    one=mat([[1,0,0],[0,1,0],[0,0,1]])
    N=mat([[0,1,0],[0,0,1],[0,0,0]])
    print("Y=1, Yt=nilpotent:", symmetries(one,N))
    # stored-type complex symmetric invertible pair (my own numbers)
    Y=mat([[1,C(2,1),0],[C(2,1),C(0,1),3],[0,3,C(1,-1)]])
    Yt=mat([[C(0,2),1,C(1,1)],[1,4,0],[C(1,1),0,-1]])
    print("det",det(Y),det(Yt))
    print("generic symmetric invertible:", symmetries(Y,Yt))
    # singular Y only
    Ys=mat([[1,1,0],[1,1,0],[0,0,2]])
    print("det Ys",det(Ys)," syms:",symmetries(Ys,Yt))
    # exhaustive small search over symmetric 2x2 0/1 matrices and 3x3 diagonal-ish: find any a3 != 0 with non-monomial p
    import itertools
    found=0; tot=0
    vals=[0,1]
    for e in itertools.product(vals,repeat=6):
        Y2=mat([[e[0],e[1]],[e[1],e[2]]]); Yt2=mat([[e[3],e[4]],[e[4],e[5]]])
        tot+=1
        s=symmetries(Y2,Yt2)
        nz=[x for x in s if x[0]!=0]
        # binary form coefficients
        p=[det(ma(ms(C(a),Y2),ms(C(1-a),Yt2))) for a in (0,1)]
        if nz:
            # monomial test: det(aY+bYt) coefficients
            c0=det(Yt2); c2=det(Y2); c1=det(ma(Y2,Yt2))-c0-c2
            mono=sum(1 for c in (c0,c1,c2) if c!=0)
            if mono!=1: print("NON-MONOMIAL WITH a3:",e,s)
            found+=1
    print("2x2 0/1 symmetric pairs:",tot,"with a3!=0:",found)
