"""Adversarial test of the S2 claims: symmetric one-type stages with pure-grade coefficients (each stage coefficient a
real number or a real multiple of I_4): real determinant, nonzero commutator invariant, unequal spectra."""
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
from GA import QI
I = QI(0, 1)
def M(rows): return [[x if isinstance(x, QI) else QI(F(x)) for x in r] for r in rows]
def mm(A, B): return [[sum((A[i][k]*B[k][j] for k in range(3)), QI(0)) for j in range(3)] for i in range(3)]
def add(*Ms):
    out = [[QI(0)]*3 for _ in range(3)]
    for A in Ms: out = [[a+b for a, b in zip(r, s)] for r, s in zip(out, A)]
    return out
def sc(c, A): return [[(c if isinstance(c, QI) else QI(F(c)))*a for a in r] for r in A]
def dag(A): return [[A[j][i].conj() for j in range(3)] for i in range(3)]
def det(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1]) - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
def comm(A, B): return add(mm(A, B), sc(-1, mm(B, A)))
J = M([[1]*3]*3); E = M([[0,0,0],[0,0,0],[0,0,1]])
S1 = M([[1,0,0],[0,-1,0],[0,0,0]]); S2 = M([[0,0,1],[0,0,-1],[1,-1,0]])
def stage(delta, t1, t2): return add(J, sc(delta, add(E, sc(t1, S1), sc(t2, S2))))
for name, tu in (("up stage at a quarter turn", (I*QI(F(1,3)), I*QI(F(1,5)))), ("up stage real", (QI(F(1,3)), QI(F(1,5)))),
                 ("up stage at an eighth turn (3+4I)/5", (QI(F(3,5),F(4,5))*QI(F(1,3)), QI(F(3,5),F(4,5))*QI(F(1,5))))):
    Md = stage(F(1,7), QI(F(1,2)), QI(F(1,4)))
    Mu = stage(F(1,11), *tu)
    Hu, Hd = mm(Mu, dag(Mu)), mm(Md, dag(Md))
    print(name, "| det Mu", det(Mu), "| det Md", det(Md), "| D", det(comm(Hu, Hd)), "| tr Hu, tr Hd", sum((Hu[i][i] for i in range(3)), QI(0)), sum((Hd[i][i] for i in range(3)), QI(0)))
