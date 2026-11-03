"""dark-matter.mirror-share-assembled: exact checks of the computable factors.

(i) The mode ratio. The derived matter is built from the conformal spin group, that is from the
    even subalgebra of the conformal ambient algebra. Signature reversal identifies the two:
    phi(e_I) = (-1)^(|I|/2) e'_I, with e'_j the generator of opposite square, is computed to be
    multiplicative on all 32 x 32 pairs of even blades of Cl(2,4) -> Cl(4,2) and bijective (rank
    32), so the two towers' derived state spaces, Lambda(C^2 + C^3) of five conformal spinor
    modes, are one space: n_2/n_6 = 2^5/2^5 = 1.
(ii) The mass ratio on the burning branch: with the record masses m_p = 938.272 MeV,
    m(4He) = 3727.379 MeV and our helium fraction Y_p = 0.245, our mean mass per baryon rounds to
    936.7 MeV, a mirror burnt entirely to helium has m(4He)/4 = 931.8 MeV, and the ratio m_2/m_6
    rounds to 0.995: one to half a percent (1 - m_2/m_6 rounds to 0.005).
(iii) The asymmetry ratio is premised on P2 and is not computed.
The temperature independence (iv) is a statement about which inputs enter, not a computation.
"""
from fractions import Fraction as F
from itertools import combinations

import GA
from tp_premise import premise

M_P = F(938272, 1000)                   # MeV
M_HE4 = F(3727379, 1000)                # MeV
Y_P = F(245, 1000)
SQ24, SQ42 = GA.sig(2, 4), GA.sig(4, 2)
# index map: a generator of square +1 in Cl(2,4) goes to one of square -1 in Cl(4,2), and back
IDX = {0: 4, 1: 5, 2: 0, 3: 1, 4: 2, 5: 3}
EVEN = [b for k in range(0, 7, 2) for b in combinations(range(6), k)]


def phi_blade(b):
    x = GA.sc(1)
    for i in b:
        x = GA.mul(x, GA.gen(IDX[i]), SQ42)
    sign = (-1) ** (len(b) // 2)
    return GA.scal(sign, x)


def phi(x):
    return GA.add(*[GA.scal(c, phi_blade(b)) for b, c in x.items()]) if x else {}


def check_mode_ratio_is_one():
    premise("dark-matter.mirror-tower-copy-one")
    premise("dark-matter.mode-counts-two-modules-which-one")
    premise("dark-matter.imported-inputs-standard-model-chain")
    assert all(SQ42[IDX[i]] == -SQ24[i] for i in range(6))
    assert len(EVEN) == 32
    for b1 in EVEN:
        for b2 in EVEN:
            prod = GA.mul({b1: F(1)}, {b2: F(1)}, SQ24)
            assert GA.eq(phi(prod), GA.mul(phi_blade(b1), phi_blade(b2), SQ42))
    allb = GA.all_blades(6)
    images = [[phi_blade(b).get(c, F(0)) for c in allb] for b in EVEN]
    assert GA.rank_of_vectors(images) == 32
    # the derived state space Lambda(C^2 + C^3): one basis vector per subset of the five modes
    states = [S for k in range(6) for S in combinations(range(5), k)]
    assert len(states) == 32
    return True


def burning_branch_ratio():
    ours = (1 - Y_P) * M_P + Y_P * M_HE4 / 4
    mirror = M_HE4 / 4
    return ours, mirror, mirror / ours


def check_mass_ratio_half_percent():
    premise("dark-matter.mirror-share-one-how-fragile")
    premise("dark-matter.p2-indifference")
    ours, mirror, r = burning_branch_ratio()
    assert round(ours * 10) == 9367 and round(mirror * 10) == 9318
    assert F(round(r * 1000), 1000) == F(995, 1000)
    assert F(round((1 - r) * 1000), 1000) == F(5, 1000)
    return True
