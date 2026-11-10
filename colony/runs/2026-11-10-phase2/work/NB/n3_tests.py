"""NB scratch, N3: exact tests of the independence statement (no gate; record only)."""
from fractions import Fraction as F
# D-term vacuum (stored): m* = c xi, c = g'^2/(g^2+g'^2); N* = sqrt(m*^2 + H^4); v^2 = 2 N*; N^2 = 1/(G H^2)
# two models with rational H, equal xi G and couplings, different N
def model(G, H, m, Nstar):
    assert Nstar * Nstar == m * m + H ** 4
    return dict(N2=1 / (G * H * H), mG=m * G, vMP4=4 * G * G * Nstar * Nstar, vH4=4 * Nstar * Nstar / H ** 4)
G1 = F(1, 100)
a = model(G1, F(2), F(3), F(5))
b = model(G1 * 2 / 5, F(2), F(15, 2), F(17, 2))
assert a['mG'] == b['mG'] and a['N2'] != b['N2']
for M in (a, b):   # (v/M_P)^4 = 4 (m* G)^2 + 4 N^-4 ; (v/H)^4 = 4 (m* G)^2 N^4 + 4
    assert M['vMP4'] == 4 * M['mG'] ** 2 + 4 / M['N2'] ** 2
    assert M['vH4'] == 4 * M['mG'] ** 2 * M['N2'] ** 2 + 4
assert a['vMP4'] != b['vMP4']
print('models', a, b)
# a dilation acting on every scale (G -> G/s^2, H -> sH, m -> s^2 m) fixes N, m G and v/M_P: not the move
s = F(3)
c = model(G1 / s ** 2, 2 * s, 3 * s * s, 5 * s * s)
assert (c['N2'], c['mG'], c['vMP4']) == (a['N2'], a['mG'], a['vMP4'])
# horizon count under the two residues, record bracket N in (1.0, 1.04)e61: 3 N^2 < 2^407
for N in (F(10) ** 61, F(104, 100) * F(10) ** 61):
    assert 2 ** 406 < 3 * N * N < 2 ** 407
print('ok')
