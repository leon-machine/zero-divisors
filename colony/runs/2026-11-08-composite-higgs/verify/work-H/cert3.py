"""Exact: doublet-condensed couplings (K=0, G_S=1, G_D=3; omega_D<0), n_b=4, P=2. Count levels below the stretched
threshold E(0,P)+G_D n_b = -6 in the stretched sector (0,2,2) and in (1,1,2) (same N_psi, N_chi), by exact inertia."""
import sys; sys.path.insert(0,'.')
from fock import *
from fractions import Fraction as F
for nb,P in [(4,2),(5,2)]:
    cp=(F(0),F(0),F(1),F(3)); GD=cp[3]
    Eb=-GD*P*(nb-P+1); thr=Eb+GD*nb
    out=[]
    for sec in [(0,P,P),(1,P-1,P)]:
        bs,M=matrix(nb,sec,*cp,exact=True)
        A=[[M[i][j]-(thr if i==j else 0) for j in range(len(M))] for i in range(len(M))]
        p,n,z=inertia(A)
        Ab=[[M[i][j]-(Eb if i==j else 0) for j in range(len(M))] for i in range(len(M))]
        pb,nbelow,zb=inertia(Ab)
        out.append((sec,len(bs),'levels below threshold',n,'levels below band',nbelow,'band multiplicity',zb))
    print(f"n_b={nb} P={P} band {Eb} threshold {thr}:",out)
