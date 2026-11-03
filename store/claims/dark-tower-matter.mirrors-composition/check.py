"""dark-tower-matter.mirrors-composition: exact check of the one closed-form input.

Checked: the copied lepton number "our tower's sphaleron value L/B = -51/28". In the symmetric
electroweak phase with N_f generations and N_H Higgs doublets, the chemical potentials
(mu_Q, mu_u, mu_d, mu_L, mu_e, mu_H) obey the sphaleron condition N_f (3 mu_Q + mu_L) = 0, the
Yukawa equilibria mu_u = mu_Q + mu_H, mu_d = mu_Q - mu_H, mu_e = mu_L - mu_H, and hypercharge
neutrality N_f (mu_Q + 2 mu_u - mu_d - mu_L - mu_e) + 2 N_H mu_H = 0 (asymmetry per degree of
freedom proportional to mu, doubled for bosons). The solution space, computed as an exact kernel, is
one-dimensional, and B = N_f (2 mu_Q + mu_u + mu_d), L = N_f (2 mu_L + mu_e) give L/B = -51/28 at
N_f = 3, N_H = 1 (B = 28/79 (B - L)); a second N_H gives a different ratio (control).
Not computable here: the decimal results (i)-(iii) and the closing remark, which come from the
supplementary MIR and CHECK_COS scripts (Fermi-Dirac equilibria, a nucleosynthesis network,
fixed-point iterations) that are not in the lab.
"""
from fractions import Fraction as F

import GA
from tp_premise import premise


def equilibrium(nf, nh):
    # columns: mu_Q, mu_u, mu_d, mu_L, mu_e, mu_H
    rows = [
        [3 * nf, 0, 0, nf, 0, 0],
        [-1, 1, 0, 0, 0, -1],
        [-1, 0, 1, 0, 0, 1],
        [0, 0, 0, -1, 1, 1],
        [nf, 2 * nf, -nf, -nf, -nf, 2 * nh],
    ]
    ker = GA.field_kernel([[F(x) for x in r] for r in rows])
    assert len(ker) == 1
    mQ, mu, md, mL, me, mH = ker[0]
    B = nf * (2 * mQ + mu + md)
    L = nf * (2 * mL + me)
    return B, L


def check_sphaleron_lepton_to_baryon():
    premise("dark-matter.mirror-tower-copy-one")
    B, L = equilibrium(3, 1)
    assert L / B == F(-51, 28)
    assert B / (B - L) == F(28, 79)
    B2, L2 = equilibrium(3, 2)
    assert L2 / B2 != F(-51, 28)
    return True
