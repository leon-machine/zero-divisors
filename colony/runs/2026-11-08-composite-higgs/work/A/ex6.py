import numpy as np, itertools
Om=3; F=3; n=F*Om; D=1<<n
def mode(f,b): return F*b+f
def cre(i):
    M=np.zeros((D,D))
    for s in range(D):
        if not s>>i&1:
            M[s|(1<<i),s]=(-1)**bin(s&((1<<i)-1)).count('1')
    return M
v={(f,b):cre(mode(f,b)) for f in range(F) for b in range(Om)}
w={k:m.T for k,m in v.items()}
E=lambda i,j: sum(v[(i,b)]@w[(j,b)] for b in range(Om))
P=lambda i,j: sum(w[(i,b)]@w[(j,b)] for b in range(Om))
W=sum(P(i,j).T@P(i,j) for i in range(F) for j in range(i+1,F))
N=sum(E(i,i) for i in range(F))
Cu3=sum(E(i,j)@E(j,i) for i in range(F) for j in range(F))
L=lambda b,c: sum(v[(i,b)]@w[(i,c)]-v[(i,c)]@w[(i,b)] for i in range(F))
CO=sum(L(b,c).T@L(b,c) for b in range(Om) for c in range(b+1,Om))
lhs=W; rhs=N*(Om+2)/2-Cu3/2-CO/2
print('identity err', np.abs(lhs-rhs).max())
# try fit general: W = a N + b N^2 + c Cu3 + d CO
