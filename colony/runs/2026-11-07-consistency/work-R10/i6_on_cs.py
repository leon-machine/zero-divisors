import sys; sys.path.insert(0,'/home/claude/phys-graph/lib')
import GA
from fractions import Fraction as F
# generators 0..5 = a1,a2,b1,b2,b3,b4 ; 6 = e (odd extension)
base=[1,1,-1,-1,-1,-1]
I6=GA.mul(GA.mul(GA.mul(GA.gen(0),GA.gen(1),base+[0]),GA.mul(GA.gen(2),GA.gen(3),base+[0]),base+[0]),GA.mul(GA.gen(4),GA.gen(5),base+[0]),base+[0])
I6sq=GA.mul(I6,I6,base+[0]); print('I6^2',I6sq)
Qe=-I6sq[()]
sq=tuple(base+[Qe])
m=lambda *xs: __import__('functools').reduce(lambda a,b:GA.mul(a,b,sq),xs)
g=GA.gen; A=GA.add; s=GA.scal
I7=m(I6,g(6)); print('I7^2',m(I7,I7), 'central:',all(GA.commutes(I7,g(k),sq) for k in range(7)))
for sgn in (1,-1):
    w1=A(g(0),g(2)); w1p=s(F(1,2),GA.sub(g(0),g(2)))
    w2=A(g(1),g(3)); w2p=s(F(1,2),GA.sub(g(1),g(3)))
    w3=A(g(4),s(sgn,m(I7,g(5)))); w3p=s(F(-1,2),GA.sub(g(4),s(sgn,m(I7,g(5)))))
    # check duality
    dot=lambda x,y: s(F(1,2),A(m(x,y),m(y,x)))
    ok=all(dot(a,b)=={():F(int(i==j))} for i,a in enumerate([w1,w2,w3]) for j,b in enumerate([w1p,w2p,w3p]))
    f=m(w1p,w2p,w3p)
    lhs=m(I6,f)
    print('w3 = b3 %s I7 b4: dual pair ok'%('+' if sgn>0 else '-'),ok,' I6 f == +I7 f:',GA.eq(lhs,m(I7,f)),' I6 f == -I7 f:',GA.eq(lhs,GA.neg(m(I7,f))))
    # on an even state w1 w2 f and odd state w1 f
    print('   even state w1w2f: I6 = -I7?',GA.eq(m(I6,w1,w2,f),GA.neg(m(I7,w1,w2,f))),' odd state w1 f: I6 = +I7?',GA.eq(m(I6,w1,f),m(I7,w1,f)))
print('--- with the store definition I6 = I4 E, I4 = a2 b2 b3 b4 (T09 e0..e3), E = e+ e- = a1 b1')
I4=m(g(1),g(3),g(4),g(5)); E=m(g(0),g(2)); I6s=m(I4,E)
print('I4 E == a1a2b1b2b3b4 ?',GA.eq(I6s,I6),' == minus ?',GA.eq(I6s,GA.neg(I6)))
w1p=s(F(1,2),GA.sub(g(0),g(2))); w2p=s(F(1,2),GA.sub(g(1),g(3))); w3p=s(F(-1,2),GA.sub(g(4),m(I7,g(5))))
f=m(w1p,w2p,w3p)
print('with w3 = b3 + I7 b4: I4E f == +I7 f ?',GA.eq(m(I6s,f),m(I7,f)))
# I7 defined as I6 e: with which I6? redo with I7' = (I4E) e
I7b=m(I6s,g(6)); print('note: (I4E) e = -(a1..b4) e:',GA.eq(I7b,GA.neg(I7)))
print('--- self-consistent store convention: I6s = I4 E, I7s = I6s e, w3 = b3 + I7s b4')
w3p=s(F(-1,2),GA.sub(g(4),m(I7b,g(5)))); w3=A(g(4),m(I7b,g(5)))
fs=m(w1p,w2p,w3p)
print('vacuum nonzero',fs!={}, ' w3 null', m(w3,w3)=={} , ' <w3,w3p>=1', GA.eq(s(F(1,2),A(m(w3,w3p),m(w3p,w3))),GA.sc(1)))
print('I6s on CS = +I7s ?',GA.eq(m(I6s,fs),m(I7b,fs)),' = -I7s ?',GA.eq(m(I6s,fs),GA.neg(m(I7b,fs))))
print('even state too:',GA.eq(m(I6s,g(0),g(1),fs),m(I7b,g(0),g(1),fs)))
