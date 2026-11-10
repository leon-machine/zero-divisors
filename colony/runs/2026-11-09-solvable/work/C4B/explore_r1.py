import os, sys
LAB='/home/claude/phys-graph'
sys.path.insert(0, LAB+'/lib'); sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tp_premise; tp_premise.configure(LAB+'/store')
from gjbase import *
TD = tr(T)
TT = mm(T, TD); DT = mm(TD, T)
def xy(E, name):
    s, a = forms(mm(W4, E))
    c = combo(s, S10, SGJ) if s else (F(0), F(0))
    print(name, 'sym->(x10,yGJ)=', c, ' anti nonzero:', a != {})
cands = {'1': ONE, 'TTd': TT, 'TdT': DT, 'anti {T,Td}': madd(TT, DT), 'comm [T,Td]': madd(TT, msc(F(-1), DT)),
         'PP': PP, 'MX': MX, 'RR': RR, 'G4': madd(PP, MX, RR)}
# degree parts of TT^dag
for k in range(0, 11, 2):
    gk = assemble({m: c for m, c in EX.items() if len(m[0]) + len(m[1]) == k})
    cands['G%d' % k] = gk
# su(4) casimir on pairs: sum over generators v_a w_b of the pair modes (u(3)) plus B-L ... use sum_{a,b} E_ab E_ba
C3 = {}
for a in PAIRS:
    for b in PAIRS:
        C3 = madd(C3, mm(mm(V[a], W[b]), mm(V[b], W[a])))
cands['u3 casimir'] = C3
cands['(B-L)^2'] = mm(BL, BL)
for n, E in cands.items():
    xy(E, n)
# form of S10 entries
print('S10 lepton/quark entry abs', {abs(v) for k, v in S10.items() if nw(k[0]) in (0, 3)}, {abs(v) for k, v in S10.items() if nw(k[0]) in (1, 2)})
print('SGJ lepton/quark', {abs(v) for k, v in SGJ.items() if nw(k[0]) in (0, 3)}, {abs(v) for k, v in SGJ.items() if nw(k[0]) in (1, 2)})
for k in sorted(S10):
    print(k, S10[k], SGJ.get(k))
