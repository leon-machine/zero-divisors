"""R1: own recomputation of the stage determinant and the quarter-turn clause (proposal 2)."""
import sys; sys.path.insert(0,'.')
from r1_phase import C, Fr, I, mat, mm, ma, ms, T, det, tr
import itertools
J=mat([[1,1,1]]*3); E=mat([[0,0,0],[0,0,0],[0,0,1]]); P=mat([[0,1,0],[1,0,0],[0,0,1]])
def X(p,q,r,s): return [[p,q,r],[C(0)-q,C(0)-p,C(0)-r],[s,C(0)-s,C(0)]]
def M(c,d,Xm): return ms(c, ma(J, ms(d, ma(E,Xm))))
# 1. general formula on a grid of Gaussian-rational entries
bad=0;n=0
vals=[C(1),C(-2),C(0,1),C(1,-3),C(Fr(1,2),2)]
for p,q,r,s in itertools.product(vals,repeat=4):
    for d in (C(Fr(1,3)),C(-2),C(1,1)):
        n+=1
        lhs=det(ma(J,ms(d,ma(E,X(p,q,r,s)))))
        xy=(p-q-s*2)*(p+q-r*2)*C(Fr(1,3))
        rhs=C(-3)*d*d*xy+d*d*d*(q*q-p*p)
        if not lhs==rhs: bad+=1
print("det formula: cases",n,"failures",bad)
# 2. one-type symmetric: Theta = (cu cd)^3 (du dd)^2 (tu td)^2 R with R = prod((p-2r)^2 + d p^2)
def theta(cu,du,tu,pu,ru,cd,dd,td,pd,rd):
    Mu=M(cu,du,ms(tu,X(pu,C(0),ru,ru))); Md=M(cd,dd,ms(td,X(pd,C(0),rd,rd)))
    return det(Mu)*det(Md), Mu, Md
# quarter turn, one real sector: sign check, delta>0 vs delta<0
for du in (Fr(1,5), Fr(-3,1)):
    th,Mu,Md=theta(C(7),C(du),C(0,2),C(2),C(-1), C(2),C(Fr(1,3)),C(3),C(1),C(3))
    Ru=(2-2*(-1))**2+du*4
    print(f"delta_u={du}: Theta={th}, R_u={Ru}, sign c_u c_d=+1 -> claimed sign of Theta is -1")
# cos phi = 0 exactly at quarter turn: compute phi from B B^dagger off-diagonal, y_q = t (p-2r)/sqrt3 ; phase of conj(y)
# verify realness of Theta as function of arg t_u at t_d real: sample units z=(3+4i)/5 etc.
for tu in (C(Fr(3,5),Fr(4,5)), C(0,1), C(1), C(Fr(-7,25),Fr(24,25))):
    th,_,_=theta(C(7),C(Fr(1,5)),tu,C(2),C(-1), C(2),C(Fr(1,3)),C(3),C(1),C(3))
    print("t_u",tu,"Theta real:",th.i==0)
th,Mu,Md=theta(C(7),C(-5),C(0,2),C(2),C(-1), C(2),C(Fr(1,3)),C(3),C(1),C(3))
print("delta_u=-5 (R_u=-4): Theta=",th," -> sign +, contrary to the stated -sgn(c_u c_d) = -1")
