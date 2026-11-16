"""R1: textbook chemical-potential computation of B/(B-L) (Harvey-Turner style), independent of the Gram form.
Per-state chemical potentials; fermion density weight 1, boson weight 2 (massless, small mu)."""
from fractions import Fraction as F

def solve(A, b):
    n=len(A); M=[r[:]+[v] for r,v in zip(A,b)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]!=0); M[c],M[p]=M[p],M[c]
        pv=M[c][c]; M[c]=[x/pv for x in M[c]]
        for i in range(n):
            if i!=c and M[i][c]!=0:
                f=M[i][c]; M[i]=[a-f*bb for a,bb in zip(M[i],M[c])]
    return [M[i][n] for i in range(n)]

def symmetric(Nf, NH):
    # unknowns: muQ, muu (u_R), mud (d_R), muL, mue (e_R), muH ; normalise B-L via one more equation
    # Yukawa: muu = muQ + muH ; mud = muQ - muH ; mue = muL - muH
    # sphaleron: Nf (3 muQ + muL) = 0 ; hypercharge: Nf(muQ + 2 muu - mud - muL - mue) + 2 NH muH = 0
    # normalisation: B - L = 1 with B = Nf(2muQ + muu + mud), L = Nf(2 muL + mue)
    A=[[1,-1,0,0,0,1],[1,0,-1,0,0,-1],[0,0,0,1,-1,-1],[3,0,0,1,0,0],
       [Nf,2*Nf,-Nf,-Nf,-Nf,2*NH],[2*Nf,Nf,Nf,-2*Nf,-Nf,0]]
    A=[[F(x) for x in r] for r in A]
    b=[F(0),F(0),F(0),F(0),F(0),F(1)]
    muQ,muu,mud,muL,mue,muH=solve(A,b)
    return Nf*(2*muQ+muu+mud)

def broken(Nf, NH, Wdof=2):
    # unknowns: muuL, mudL, muuR, mudR, munu, mueL, mueR, muW ; neutral Higgs mu0 = 0, charged Higgs mu_+ = muW
    # W: muuL = mudL + muW ; munu = mueL + muW
    # Yukawa with mu0=0: muuR = muuL, mudR = mudL, mueR = mueL
    # sphaleron: Nf(3 muuL + ... ) -> per family: 3*(muuL+mudL)/... standard: Nf( (muuL+2mudL) + munu )=0  [HT: u_L + 2 d_L + nu_L]
    # Q_em = 0: quarks: Nf*3*(2/3 muuL + 2/3 muuR - 1/3 mudL - 1/3 mudR) + leptons Nf*(-mueL - mueR) + bosons:
    #   W^+ charge +1, Wdof states x2 (boson); charged Higgs components NH x2 (boson), charge +1, mu = muW
    A=[[1,-1,0,0,0,0,0,-1],[0,0,0,0,1,-1,0,-1],[1,0,-1,0,0,0,0,0],[0,1,0,-1,0,0,0,0],[0,0,0,0,0,1,-1,0],
       [1,2,0,0,1,0,0,0],
       [2*Nf,-Nf,2*Nf,-Nf,0,-Nf,-Nf,2*Wdof+2*NH]]
    # B = Nf*(3*(muuL+mudL)/3 ... ) per state baryon 1/3: B = Nf*( (3muuL+3mudL+3muuR+3mudR)/3 )
    Bv=[Nf,Nf,Nf,Nf,0,0,0,0]; Lv=[0,0,0,0,Nf,Nf,Nf,0]
    A.append([x-y for x,y in zip(Bv,Lv)])
    A=[[F(x) for x in r] for r in A]
    b=[F(0)]*7+[F(1)]
    mu=solve(A,b)
    return sum(F(x)*m for x,m in zip(Bv,mu))

csym=lambda N,H: F(8*N+4*H,22*N+13*H)
cbr=lambda N,H: F(8*N+4*(H+2),24*N+13*(H+2))
for N,H in ((3,1),(3,2),(2,3),(4,1),(1,0),(5,4)):
    s=symmetric(N,H); b=broken(N,H)
    print(f"Nf={N} NH={H}: sym {s} formula {csym(N,H)} {'OK' if s==csym(N,H) else 'DIFF'} | broken {b} formula {cbr(N,H)} {'OK' if b==cbr(N,H) else 'DIFF'}")
print("broken with massive W (3 dof), Nf=3,NH=1:", broken(3,1,3))
nb=F(87,10)
print("(B-L)/s range x1e-11:", float(nb/F(28,79)), float(nb/F(12,37)))
