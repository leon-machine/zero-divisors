import time
from fractions import Fraction as F
from itertools import product, combinations
from core import *

t0 = time.time()
G = closure(GENS)
n = len(G)
idx = {R: i for i, R in enumerate(G)}
MUL = [[idx[m(a, b)] for b in G] for a in G]
INV = [idx[rev(a)] for a in G]
print('table', time.time() - t0)
W = [(4 * R[0] - 1) / 3 for R in G]           # normalised real trace
CH = [(4 * R[0] - 1, 4 * R[POS[IDX]]) for R in G]  # chi as (re, im)
ID = idx[ONE]


def cm(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def cconj(a):
    return (a[0], -a[1])


# gluing in normalised trace: avg_U w(XU) w(U~Y) = w(XY)/18
ok = True
for X in range(n):
    for Y in range(n):
        s = sum(W[MUL[X][U]] * W[MUL[INV[U]][Y]] for U in range(n)) / n
        ok &= s == W[MUL[X][Y]] / 18
print('gluing w 1/18', ok, time.time() - t0)
# complex gluing: avg chi(XU) chi(U~Y) = chi(XY)/3 ; avg chi(XU)chi(YU)=0
ok1 = ok2 = True
for X in range(n):
    for Y in range(n):
        s = [F(0), F(0)]
        s2 = [F(0), F(0)]
        for U in range(n):
            p = cm(CH[MUL[X][U]], CH[MUL[INV[U]][Y]])
            q = cm(CH[MUL[X][U]], CH[MUL[Y][U]])
            s[0] += p[0]; s[1] += p[1]; s2[0] += q[0]; s2[1] += q[1]
        c = CH[MUL[X][Y]]
        ok1 &= (s[0] / n, s[1] / n) == (c[0] / 3, c[1] / 3)
        ok2 &= s2 == [0, 0]
print('complex gluing', ok1, ok2, time.time() - t0)
# cubic: avg chi^3 = 1, chi^2 chibar = 0, |chi|^2 = 1
def avg(f):
    s = [F(0), F(0)]
    for U in range(n):
        v = f(U)
        s[0] += v[0]; s[1] += v[1]
    return (s[0] / n, s[1] / n)
print('chi^3', avg(lambda U: cm(cm(CH[U], CH[U]), CH[U])), 'chi^2 chibar',
      avg(lambda U: cm(cm(CH[U], CH[U]), cconj(CH[U]))), '|chi|^2', avg(lambda U: cm(CH[U], cconj(CH[U]))),
      'chi', avg(lambda U: CH[U]), 'chi^2', avg(lambda U: cm(CH[U], CH[U])))

# Wilson loops in tree gauge: links vertical V[x][y] x=1..R, plaquette (x,y) = V[x+1,y] V[x,y]^{-1}
def rect(R, T):
    total = F(0)
    free = [(x, y) for x in range(1, R + 1) for y in range(T)]
    for vals in product(range(n), repeat=len(free)):
        V = dict(zip(free, vals))
        for y in range(T):
            V[(0, y)] = ID
        b = ID
        for y in range(T):
            b = MUL[b][V[(R, y)]]
        val = W[b]
        for x in range(R):
            for y in range(T):
                val *= W[MUL[V[(x + 1, y)]][INV[V[(x, y)]]]]
        total += val
    return total / n ** len(free)
print('1x1', rect(1, 1), F(1, 18))
print('2x1', rect(2, 1), F(1, 18 ** 2), time.time() - t0)

# Polyakov N_t=1, r=1: P(x)=chi(Ux)/3, P(y)*; plaquette w(Ux S Uy^-1 S^-1); gauge S=1
s = [F(0), F(0)]
for a in range(n):
    for b in range(n):
        v = cm(CH[a], cconj(CH[b]))
        wv = W[MUL[a][INV[b]]]
        s[0] += v[0] * wv; s[1] += v[1] * wv
print('Polyakov Nt=1 r=1', (s[0] / n ** 2 / 9, s[1] / n ** 2 / 9), F(1, 162))
# baryonic three lines at N_t = 1
Fu = []
for U in range(n):
    acc = [F(0), F(0)]
    for V in range(n):
        wv = W[MUL[U][INV[V]]]
        acc[0] += CH[V][0] * wv; acc[1] += CH[V][1] * wv
    Fu.append((acc[0] / n / 3, acc[1] / n / 3))
print('F(U) == chi(U)/54 ?', all(Fu[U] == (CH[U][0] / 54, CH[U][1] / 54) for U in range(n)))
print('baryon Nt=1', avg(lambda U: cm(cm(Fu[U], Fu[U]), Fu[U])), F(1, 27 * 18 ** 3))
print('two lines PP (N-ality 2)', avg(lambda U: cm(Fu[U], Fu[U])))
print(time.time() - t0)
