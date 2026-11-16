"""A3 scratch: bilinear forms on the sixteen invariant under colour and electric charge; B - L weights; flavour."""
import sys
sys.path.insert(0, '/home/claude/phys-graph/lib'); sys.path.insert(0, '.')
from fractions import Fraction as F
import GA
from a23 import *   # noqa (prints a table; fine for scratch)
print('-----')
# bilinear forms: basis E_{S,T}, S, T even; form(psi, phi) = psi_S phi_T. A generator g acts by
# (g.b)(psi, phi) = -b(g psi, phi) - b(psi, g phi). Invariant forms = kernel.
PAIRS = [(S, T) for S in EVEN for T in EVEN]
PIDX = {p: i for i, p in enumerate(PAIRS)}
def action_rows(ops_list, diag=None):
    rows = []
    for ops in ops_list:
        img = {S: word(ops, {S: F(1)}) for S in EVEN}
        # (g.b)_{S,T} = -sum_U b_{U,T} g_{U,S} - sum_U b_{S,U} g_{U,T}; set to zero for each (S,T)
        for S in EVEN:
            for T in EVEN:
                row = {}
                for U, c in img[S].items():
                    row[PIDX[(U, T)]] = row.get(PIDX[(U, T)], 0)+c
                for U, c in img[T].items():
                    row[PIDX[(S, U)]] = row.get(PIDX[(S, U)], 0)+c
                if row:
                    r = [F(0)]*256
                    for k, v in row.items(): r[k] = v
                    rows.append(r)
    return rows
colour = [[("v", a), ("w", b)] for a in PAIR for b in PAIR if a != b]
rows = action_rows(colour)
# Cartan and charge conditions: zero weight under lam, lam2, Q
for fn in (lam, lam2, qem):
    for (S, T) in PAIRS:
        if fn(S)+fn(T) != 0:
            r = [F(0)]*256; r[PIDX[(S, T)]] = F(1); rows.append(r)
ker = GA.field_kernel(rows)
print('forms invariant under su(3) + u(1)_Q:', len(ker))
from collections import Counter
cnt = Counter()
for k in ker:
    supp = [PAIRS[i] for i, v in enumerate(k) if v != 0]
    w = {bml(S)+bml(T) for S, T in supp}
    names = {(NAMES[jk(S)], NAMES[jk(T)]) for S, T in supp}
    t3w = {t3(S)+t3(T) for S, T in supp}
    cnt[(tuple(sorted(w)), tuple(sorted(names)), tuple(sorted(t3w)))] += 1
for k, v in sorted(cnt.items(), key=str): print(v, k)
# the Majorana element and the nu nu element
top = [("v", i) for i in MODES]
print('T on even states:', {tuple(sorted(S)): word(top, {S: F(1)}) for S in EVEN if word(top, {S: F(1)})})
# B - L weights of the 45 bivectors and of the slot vectors on all 32 states
def weight_of(ops):
    ws = set()
    for S in STATES:
        for T in word(ops, {S: F(1)}):
            ws.add(bml(T)-bml(S))
    return ws
kinds = Counter()
allmodes = MODES
for a in allmodes:
    for b in allmodes:
        if a < b:
            for ka in "vw":
                for kb in "vw":
                    ws = weight_of([(ka, a), (kb, b)])
                    typ = ('pair-pair' if b <= 3 else 'slot-slot' if a >= 4 else 'pair-slot')
                    kinds[(typ, tuple(sorted(ws)))] += 1
        if a != b:
            pass
for k, v in sorted(kinds.items(), key=str): print(v, k)
print('slot vectors:', [weight_of([(k, i)]) for k in "vw" for i in SLOT], ' T:', weight_of(top))
print('pair vectors:', [weight_of([(k, i)]) for k in "vw" for i in PAIR])
