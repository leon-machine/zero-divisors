"""S2 scratch: the determinant phase on the stored completion. Exact over the Gaussian rationals (unit = I_4)."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
from GA import QI
I = QI(0, 1)

def mat(rows): return [[QI(x) for x in r] for r in rows]
def mm(A, B): return [[sum((A[i][k]*B[k][j] for k in range(len(B))), QI(0)) for j in range(len(B[0]))] for i in range(len(A))]
def madd(A, B): return [[a+b for a, b in zip(r, s)] for r, s in zip(A, B)]
def msc(c, A): return [[QI(c)*a for a in r] for r in A]
def conj(A): return [[a.conj() for a in r] for r in A]
def tr(A): return [list(r) for r in zip(*A)]
def dag(A): return tr(conj(A))
def det(A):
    n = len(A)
    if n == 1: return A[0][0]
    if n == 2: return A[0][0]*A[1][1]-A[0][1]*A[1][0]
    s = QI(0)
    for j in range(n):
        minor = [r[:j]+r[j+1:] for r in A[1:]]
        s = s + (QI(-1) if j % 2 else QI(1))*A[0][j]*det(minor)
    return s
def comm(A, B): return madd(mm(A, B), msc(-1, mm(B, A)))
def H(M): return mm(M, dag(M))
def D(Mu, Md): return det(comm(H(Mu), H(Md)))
def masses(al, be, Y, Yt):
    Mu = madd(msc(al, Y), msc(be.conj(), Yt))
    Md = madd(msc(be, Y), msc(al.conj(), Yt))
    return Mu, Md
def charpoly3(Hm):
    # coefficients (tr, second invariant, det) of a 3x3 matrix
    t = Hm[0][0]+Hm[1][1]+Hm[2][2]
    H2 = mm(Hm, Hm)
    t2 = H2[0][0]+H2[1][1]+H2[2][2]
    return (t, (t*t-t2)/QI(2), det(Hm))

# sample symmetric complex matrices
Y = mat([[QI(1, 2), QI(0, 1), 2], [QI(0, 1), 3, QI(1, -1)], [2, QI(1, -1), QI(5, 1)]])
Yt = mat([[2, QI(1, 1), QI(0, 3)], [QI(1, 1), QI(-1, 2), 1], [QI(0, 3), 1, QI(4, -1)]])
al, be = QI(F(1, 3), 0), QI(-3, 0)     # lift family: alpha = H^2/lambda, beta = -lambda (real)
Mu, Md = masses(al, be, Y, Yt)
print('det(MuMd)=', det(Mu)*det(Md), ' D=', D(Mu, Md))

# (i) inverse map
m2 = al*al.conj()-be*be.conj()          # = 2 m(c)
Yrec = msc(QI(1)/m2, madd(msc(al.conj(), Mu), msc(-be.conj(), Md)))
Ytrec = msc(QI(1)/m2, madd(msc(al, Md), msc(-be, Mu)))
print('inverse ok:', Yrec == Y, Ytrec == Yt)
# complex alpha, beta
al2, be2 = QI(2, 1), QI(-1, 3)
Mu2, Md2 = masses(al2, be2, Y, Yt)
m22 = al2*al2.conj()-be2*be2.conj()
print('inverse ok (complex frame):', msc(QI(1)/m22, madd(msc(al2.conj(), Mu2), msc(-be2.conj(), Md2))) == Y,
      msc(QI(1)/m22, madd(msc(al2, Md2), msc(-be2, Mu2))) == Yt)
# rephasing M_u -> z M_u with |z|=1 rational point of the circle: z = (3+4I)/5
z = QI(F(3, 5), F(4, 5))
Mu_z = msc(z, Mu)
Yz = msc(QI(1)/m2, madd(msc(al.conj(), Mu_z), msc(-be.conj(), Md)))
Ytz = msc(QI(1)/m2, madd(msc(al, Md), msc(-be, Mu_z)))
Mu3, Md3 = masses(al, be, Yz, Ytz)
print('rephased: H_u same', H(Mu3) == H(Mu), 'H_d same', H(Md3) == H(Md), 'D same', D(Mu3, Md3) == D(Mu, Md),
      'det ratio', det(Mu3)*det(Md3)/(det(Mu)*det(Md)), 'z^3', z*z*z, 'sym', Yz == tr(Yz), Ytz == tr(Ytz))
# hypercharge phase alpha -> z alpha, beta -> conj(z) beta
Mu4, Md4 = masses(z*al2, z.conj()*be2, Y, Yt)
print('hypercharge phase leaves det:', det(Mu4)*det(Md4) == det(Mu2)*det(Md2))
# common phase c -> z c
Mu5, Md5 = masses(z*al2, z*be2, Y, Yt)
print('common phase changes det:', det(Mu5)*det(Md5) == det(Mu2)*det(Md2))
# balanced frame |alpha| = |beta|
al6, be6 = QI(3, 4), QI(0, 5)
Mu6, Md6 = masses(al6, be6, Y, Yt)
print('balanced: Md = (beta/alpha) Mu', Md6 == msc(be6/al6, Mu6), 'D', D(Mu6, Md6))

# (iii a) real
Yr = mat([[1, 2, 0], [2, -3, 1], [0, 1, 5]]); Ytr = mat([[2, 1, 3], [1, 0, -1], [3, -1, 4]])
Mur, Mdr = masses(al, be, Yr, Ytr)
print('real: det', det(Mur)*det(Mdr), 'D', D(Mur, Mdr))
# (iii b) self-conjugate: Yt = conj(Y), any complex frame
Mus, Mds = masses(al2, be2, Y, conj(Y))
print('self-conj: Md == conj(Mu)', Mds == conj(Mus), 'det', det(Mus)*det(Mds), 'D', D(Mus, Mds),
      'charpoly equal', charpoly3(H(Mus)) == tuple(c.conj() for c in charpoly3(H(Mds))), charpoly3(H(Mus)))
# (iii c) Hermitian Y, Yt, real frame
Yh = mat([[1, QI(2, 1), QI(0, -1)], [QI(2, -1), 3, QI(1, 1)], [QI(0, 1), QI(1, -1), -2]])
Yth = mat([[2, QI(0, 3), 1], [QI(0, -3), 1, QI(2, -1)], [1, QI(2, 1), 5]])
Muh, Mdh = masses(al, be, Yh, Yth)
print('hermitian: Mu herm', Muh == dag(Muh), 'det', det(Muh)*det(Mdh), 'D', D(Muh, Mdh),
      charpoly3(H(Muh)), charpoly3(H(Mdh)))
# hermitian with complex frame: not hermitian
Muh2, Mdh2 = masses(al2, be2, Yh, Yth)
print('hermitian, complex frame: det', det(Muh2)*det(Mdh2))
