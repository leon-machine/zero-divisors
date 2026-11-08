"""Is H - H_N = H_so10 on localised window vectors (all charge sectors), or even on every window vector?"""
import sys, itertools, importlib.util
from fractions import Fraction as F
sys.path.insert(0, '/home/claude/phys-graph/lib')
spec = importlib.util.spec_from_file_location('ck', 'synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split/check.py')
ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
import fock
so = ck._so10(); D = ck._dual(so); lam = ck._lam(so, D, so[1])
one = ck._one(16)
def test(L, s, psi):
    W = ck._Win(16, L)
    hso = ck._vsc(1 / (2 + lam), W.sug(so, D, psi))
    hn = ck._vsc(F(1, 2), W.sug([one], [ck._vsc_m(F(1, 16), one)], psi))
    h = W.energy(psi)
    return ck._vadd(h, ck._vsc(-1, ck._vadd(hso, hn)))
L, s = 6, 3
W = ck._Win(16, L)
Om = W.sea(s)
cases = {
 'Omega': Om,
 'one particle added (charge +1)': fock.cre_on(W.idx(4, 3), Om),
 'one hole (charge -1)': fock.ann_on(W.idx(9, 2), Om),
 'two particles same level': fock.cre_on(W.idx(2, 3), fock.cre_on(W.idx(11, 3), Om)),
 'particle-hole level 2': fock.cre_on(W.idx(1, 4), fock.ann_on(W.idx(6, 2), Om)),
 'particle-hole across': fock.cre_on(W.idx(1, 3), fock.ann_on(W.idx(6, 1), Om)),
}
for k, v in cases.items():
    r = test(L, s, v)
    print(k, 'zero' if not r else ('nonzero', len(r)))
# arbitrary small window state
W2 = ck._Win(16, 2)
for t in range(3):
    S = sum(1 << W2.idx(x, k) for x in range(16) for k in range(2) if (x * 5 + k * 3 + t) % 4 == 0)
    r = test(2, 0, {S: F(1)})
    print('raw window L=2 state', t, 'zero' if not r else ('nonzero', len(r)))
