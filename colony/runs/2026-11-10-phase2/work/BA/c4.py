from c3 import *
def eye(n): return [[F(int(i == j)) for j in range(n)] for i in range(n)]
def shear(n, i, j, c=1):
    A = eye(n); A[i][j] = F(c); B = eye(n); B[i][j] = F(-c); return A, B
def diag(n, i, t):
    A = eye(n); A[i][i] = F(t); B = eye(n); B[i][i] = F(1) / t; return A, B
mats3 = [(eye(3), eye(3)), diag(3, 0, 2), diag(3, 1, 3), diag(3, 2, 5), shear(3, 0, 1), shear(3, 1, 2), shear(3, 2, 0), shear(3,1,0)]
for n in range(4, 9):
    t = time.time(); d, ker = common_real_functionals(3, mats3[:n]); print('l=3, first', n, 'splits: dim', d, round(time.time() - t, 2))
