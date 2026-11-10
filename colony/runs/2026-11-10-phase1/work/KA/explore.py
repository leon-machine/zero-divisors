from fractions import Fraction as F
def metric(M,a,r,u):
    S=r*r+a*a*u*u; P=r*r+a*a
    eta=[[F(0)]*4 for _ in range(4)]
    eta[0][0]=F(-1); eta[1][1]=S/P; eta[2][2]=S/(1-u*u); eta[3][3]=P*(1-u*u)
    k=[F(-1),-S/P,F(0),a*(1-u*u)]
    H=M*r/S
    return [[eta[i][j]+2*H*k[i]*k[j] for j in range(4)] for i in range(4)]
def det3(m):
    return (m[0][0]*(m[1][1]*m[2][2]-m[1][2]*m[2][1])-m[0][1]*(m[1][0]*m[2][2]-m[1][2]*m[2][0])+m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
def gram(g,vs):
    return [[sum(v[i]*g[i][j]*w[j] for i in range(4) for j in range(4)) for w in vs] for v in vs]
# 1. r=const
for (M,a,r,u,Om) in [(F(5),F(3),F(7),F(1,3),F(2,7)),(F(5),F(3),F(4),F(-2,5),F(0)),(F(13),F(5),F(30),F(3,4),F(1,9)),(F(5),F(4),F(1,2),F(1,7),F(3))]:
    g=metric(M,a,r,u)
    vs=[[F(1),0,0,Om],[0,0,F(1),0],[0,0,0,F(1)]]
    d=det3(gram(g,vs)); De=r*r-2*M*r+a*a; S=r*r+a*a*u*u
    print(d, -De*S, d==-De*S)
# 2. Sigma=rho^2 surface param by u: r(u), dr/du = -a^2 u / r ; need r rational: choose a u, r rational
for (M,a,r,u) in [(F(5),F(3),F(4),F(1,3)),(F(50),F(2),F(3),F(1,2)),(F(7),F(1),F(2),F(3,5))]:
    g=metric(M,a,r,u); rho2=r*r+a*a*u*u
    vs=[[F(1),0,0,0],[0,-a*a*u/r,F(1),0],[0,0,0,F(1)]]
    d=det3(gram(g,vs))
    pred=-(rho2/r)**2*(r*r+a*a*(1-u*u)-2*M*r**3/rho2)
    print(d,pred,d==pred)
