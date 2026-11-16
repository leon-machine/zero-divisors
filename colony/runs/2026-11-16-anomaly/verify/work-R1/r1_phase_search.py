import sys, itertools
sys.path.insert(0,'.')
from r1_phase import *
# exhaustive: 2x2 symmetric entries in {0,1,I}, nonzero p, look for a3 != 0 with p non-monomial; and check a3 = -(2j-n)(q1-q2)
vals=[C(0),C(1),I]
bad=0; cnt=0; nz=0
for e in itertools.product(vals,repeat=6):
    Y2=mat([[e[0],e[1]],[e[1],e[2]]]); Yt2=mat([[e[3],e[4]],[e[4],e[5]]])
    c0=det(Yt2); c2=det(Y2); c1=det(ma(Y2,Yt2))-c0-c2
    coeffs=[c0,c1,c2]  # coefficient of a^j b^(2-j), j=0,1,2
    if all(c==0 for c in coeffs): continue
    cnt+=1
    s=symmetries(Y2,Yt2)
    if any(x[0]!=0 for x in s):
        nz+=1
        js=[j for j in range(3) if coeffs[j]!=0]
        if len(js)!=1: bad+=1; print("COUNTER to (v):",e)
        else:
            j=js[0]
            if not all(a==-(2*j-2)*d for a,d in s): bad+=1; print("formula fails",e,s)
print("2x2 symmetric over {0,1,i}, p!=0:",cnt,"with a3!=0:",nz,"violations of (v):",bad)
# 3x3 diagonal and permutation-type pairs, entries {0,1}
bad=0;nz=0;cnt=0
for e in itertools.product([0,1],repeat=6):
    Y3=mat([[e[0],0,0],[0,e[1],0],[0,0,e[2]]]); Yt3=mat([[e[3],0,0],[0,e[4],0],[0,0,e[5]]])
    # p(a,b)=prod(a e_i + b e_{i+3})
    s=symmetries(Y3,Yt3)
    import itertools as it
    if any((e[i],e[i+3])==(0,0) for i in range(3)): continue
    cnt+=1
    j=sum(1 for i in range(3) if e[i]==1 and e[i+3]==0)
    mono=all(not(e[i]==1 and e[i+3]==1) for i in range(3))
    if any(x[0]!=0 for x in s):
        nz+=1
        if not mono: bad+=1; print("COUNTER 3x3 diag",e)
print("3x3 diagonal pairs p!=0:",cnt,"a3!=0:",nz,"violations:",bad)
# lift-locus counter-model: Y=1, Yt=N nilpotent, alpha beta=-H^2: masses all nonzero, symmetry with a3 != 0
one=mat([[1,0,0],[0,1,0],[0,0,1]]); N=mat([[0,1,0],[0,0,1],[0,0,0]])
al=C(Fr(1,10)); be=C(-10)  # alpha beta = -1 = -H^2 with H=1
Mu=ma(ms(al,one),ms(be.conj(),N)); Md=ma(ms(be,one),ms(al.conj(),N))
print("det Mu, det Md on lift locus:",det(Mu),det(Md))
def dag(A): return [[x.conj() for x in r] for r in T(A)]
Hu=mm(Mu,dag(Mu)); Hd=mm(Md,dag(Md))
comm=ma(mm(Hu,Hd),ms(C(-1),mm(Hd,Hu)))
print("[Hu,Hd] nonzero (so V != 1):", any(x!=0 for r in comm for x in r))
print("symmetries a3,(q1-q2):",symmetries(one,N))
# also Y=diag(1,1,0), Yt=diag(0,0,1) at alpha=0 (cone family point): massless quark
