"""Referee H: a T3 = +1/2 doublet component with M^2 != 0 (M = E_{up,s} + E_{s,down}); compare |B^p Omega|^2
with the M^2 = 0 quasi-spin formula (p!)^2 e_p over q rank(M) = 2q unit values, C(2q, p)."""
import sys; sys.path.insert(0,'.')
from fock import cre, ann
from fractions import Fraction as F
from math import comb, factorial
KS=(-2,-1,0,1); CH=3
def mode(k,a): return (k+2)*CH+a
def rho_star(q,M,st):
    out={}
    for s,c in st.items():
        for k in KS:
            if k+q not in KS: continue
            for a in range(CH):
                for b in range(CH):
                    if M[b][a]!=0:   # (M*)_{ab} = M_{ba}; term a*_{k+q,a} a_{k,b}
                        r=ann(mode(k,b),s)
                        if r is None: continue
                        r2=cre(mode(k+q,a),r[1])
                        if r2 is None: continue
                        out[r2[1]]=out.get(r2[1],0)+c*M[b][a]*r[0]*r2[0]
    return {k:v for k,v in out.items() if v!=0}
sea=0
for k in KS:
    if k<0:
        for a in range(CH): sea|=1<<mode(k,a)
for name,M in [('E_up,s (M^2=0)',[[0,0,1],[0,0,0],[0,0,0]]),('E_up,s + E_s,down (M^2=E_up,down)',[[0,0,1],[0,0,0],[0,1,0]])]:
    for q in (1,2):
        st={sea:1}; row=[]
        for p in range(2*q+2):
            row.append(sum(v*v for v in st.values())); st=rho_star(q,M,st)
        r=1 if 'M^2=0' in name else 2
        pred=[factorial(p)**2*comb(q*r,p) for p in range(2*q+2)]
        print(name,'q',q,'norms',row,'(p!)^2 C(q rank,p)',pred)
