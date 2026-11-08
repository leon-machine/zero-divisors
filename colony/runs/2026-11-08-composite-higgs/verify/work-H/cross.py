"""Cross-check the counterexample with the proposal's own GA-based sector matrices and exact inertia:
n_b = 5, P = 3, (Kp, Kc, GS, GD) = (0, 0, 1, 1/2), omega_D = 3/2 > 0: number of levels of sector (2,2,2) below E(P,0) = -9."""
import sys, os
sys.path.insert(0, 'lib'); sys.path.insert(0, 'proposals/synthesis.two-species-floor-pairing-has-a-gapped-doublet-pair-mode-that-closes-where-it-condenses')
import tp_premise; tp_premise.configure('store')
import check as C
from fractions import Fraction as F
cp = (F(0), F(0), F(1), F(1, 2))
for om, P, sec in [(5, 3, (2, 2, 2)), (5, 3, (3, 3, 0))]:
    rows = C.sector_matrix(om, sec, lambda st: C.Hop(om, cp, st))
    E0 = -cp[2] * P * (om - P + 1)
    print(om, P, sec, 'dim', len(rows), 'inertia of H - E(P,0) (pos, neg, zero):', C.inertia(C.shifted(rows, E0, 1)))
