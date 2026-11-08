"""Exact variational certificate: a rational trial vector in a sector with N_chi = 2 whose Rayleigh quotient lies
below the singlet band E(P,0) at a coupling with omega_D > 0 (singlet-condensed regime) and n_b - P + 1 >= 3."""
import sys; sys.path.insert(0,'.')
from fock import *
from fractions import Fraction as F
import numpy as np
def cert(nb,P,sec,Kp,Kc,GS,GD,den=64):
    bs,M=matrix(nb,sec,float(Kp),float(Kc),float(GS),float(GD))
    w,V=np.linalg.eigh(M); v=V[:,0]
    x=[F(round(c*den)) for c in v]
    # exact H x via operator words
    idx={s:i for i,s in enumerate(bs)}
    terms=[(-GS,wd) for _,wd in op_terms(nb,'SS')]+[(-GD,wd) for _,wd in op_terms(nb,'B0')]+[(-GD,wd) for _,wd in op_terms(nb,'B1')]
    Hx=[F(0)]*len(bs)
    kin=Kp*(sec[0]+sec[1])+Kc*sec[2]
    for j,s in enumerate(bs):
        if x[j]==0: continue
        Hx[j]+=kin*x[j]
        for cf,wd in terms:
            r=apply_word(wd,s)
            if r: Hx[idx[r[1]]]+=cf*r[0]*x[j]
    rq=sum(a*b for a,b in zip(x,Hx))/sum(a*a for a in x)
    band=2*Kp*P-GS*P*(nb-P+1)
    wD=(Kc-Kp)+(GS-GD)*(nb-P+1)
    print(f"n_b={nb} P={P} sector={sec} (Kp,Kc,GS,GD)=({Kp},{Kc},{GS},{GD}) omega_D={wD} m={nb-P+1}: numeric lowest {w[0]:.6f}; "
          f"exact Rayleigh quotient {float(rq):.6f} ({rq}) vs singlet band E(P,0)={band}: below band: {rq<band}")
if __name__=="__main__": cert(5,3,(2,2,2),F(0),F(0),F(1),F(1,2))
if __name__=="__main__": cert(6,3,(2,2,2),F(0),F(0),F(1),F(4,5))
if __name__=="__main__": cert(7,3,(2,2,2),F(0),F(0),F(1),F(9,10),den=1<<16)
