import sympy as sp, itertools
I=sp.I
def fock(nm):
    # Jordan-Wigner creation operators c_j^dagger on 2^nm states
    s_minus=sp.Matrix([[0,0],[1,0]]); Z=sp.diag(1,-1); E=sp.eye(2)
    ops=[]
    for j in range(nm):
        m=sp.Matrix([[1]])
        for k in range(nm):
            m=sp.kronecker_product(m, Z if k<j else (s_minus if k==j else E))
        ops.append(m)
    return ops
# ---- P4: five modes
cd=fock(5); c=[m.T for m in cd]; dim=32
gam=[]
for j in range(5):
    gam += [cd[j]+c[j], -I*(cd[j]-c[j])]     # v_j = (g1 + I g2)/2 = creation
om=sp.eye(dim)
for g in gam: om=om*g
num=[cd[j]*c[j] for j in range(5)]; N=sum(num,sp.zeros(dim))
Gam=sp.diag(*[(-1)**int(N[i,i]) for i in range(dim)])
print("omega^2 = -1:", om*om==-sp.eye(dim), "| omega = I*Gamma:", om==I*Gam)
T=sp.eye(dim)
for j in range(5): T=T*cd[j]
print("omega T omega^-1 = -T:", om*T*om.inv()==-T)
# charges: slots = modes 0,1 ; pairs = modes 2,3,4 ; Y=(3n-2k)/6 ; B-L = 1-2k/3 ; X=5(B-L)-4Y
n=num[0]+num[1]; k=num[2]+num[3]+num[4]; Id=sp.eye(dim)
Y=(3*n-2*k)/6; BL=Id-sp.Rational(2,3)*k; X=5*BL-4*Y
print("[Y,T]=0:", Y*T-T*Y==sp.zeros(dim), "| [B-L,T]=-2T:", BL*T-T*BL==-2*T, "| X = 5-2N:", X==5*Id-2*N)
ex=lambda D,a: sp.diag(*[sp.exp(a*D[i,i]) for i in range(dim)])
print("omega = exp(I pi X/2):", sp.simplify(ex(X,I*sp.pi/2)-om)==sp.zeros(dim))
z=ex(Y,2*sp.pi*I); g=om*z; gi=g.inv()
print("omega*exp(2 pi I Y) fixes the four slot generators:", all(sp.simplify(g*gam[p]*gi-gam[p])==sp.zeros(dim) for p in range(4)),
      "| flips them without the Y factor:", all(om*gam[p]*om.inv()==-gam[p] for p in range(4)),
      "| still flips T:", sp.simplify(g*T*gi+T)==sp.zeros(dim))
print("omega*exp(2 pi I Y) = exp(5 pi I (B-L)/2):", sp.simplify(g-ex(BL,5*sp.pi*I/2))==sp.zeros(dim))
# is -1 or omega*z in the SM torus x centres?  eigenvalues of omega z on V_+ by (n,k):
print("omega z on states (n,k,N even):", sorted({(int(n[i,i]),int(k[i,i]),sp.simplify(g[i,i])) for i in range(dim) if int(N[i,i])%2==0}))
# ---- P5: four modes, block at K=0
cd=fock(4); w=[m.T for m in cd]; v=cd
m_,M_=sp.symbols('m M',real=True)
D=w[0]*w[3]+w[2]*w[1]; S=w[2]*w[3]
H=m_*(D+D.T)+M_*(S+S.T)
x=sp.symbols('x')
cp=sp.factor(H.charpoly(x).as_expr())
print("char poly of H (16 states):", cp)
print("--- sign conventions")
cd=fock(5); c=[m.T for m in cd]; dim=32
print("omega = -I (-1)^N:", om==-I*Gam, "| with n_j := v_j^* v_j (hole number), prod(1-2n_j) = -(-1)^N:",
      sp.prod([sp.eye(dim)-2*c[j]*cd[j] for j in range(5)],start=sp.eye(dim))==-Gam)
print("omega = exp(-I pi X/2):", sp.simplify(ex(X,-I*sp.pi/2)-om)==sp.zeros(dim),
      "| omega*exp(-2 pi I Y) = exp(-5 pi I (B-L)/2):", sp.simplify(om*ex(Y,-2*sp.pi*I)-ex(BL,-5*sp.pi*I/2))==sp.zeros(dim))
