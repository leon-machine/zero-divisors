"""Referee G, own route (Fock space, exact): photon proposal (v). ||[eps_m, eps_l*] Omega||^2 = 2(l - m)||MM*||_F^2,
central value m tr MM*, for channel-matrices M over generators with entries in span{1, J} (the check used real M only)."""
import sys; sys.path.insert(0, sys.path[0])
from fock import *
import itertools

def run(Ng, L, h, M, pairs):
    modes = [(g, a, k) for g in range(Ng) for a in '+-' for k in range(1, L + 1)]
    fk = Fock(modes)
    Om = {frozenset((g, a, k) for g in range(Ng) for a in '+-' for k in range(1, h + 1)): ONE}
    def eps(m):
        return Bilinear(fk, [(M[g][hh], (g, '+', k), (hh, '-', k + m)) for g in range(Ng) for hh in range(Ng)
                             for k in range(1, L + 1) if 1 <= k + m <= L])
    MMs = [[(lambda s: s)(sum_n([nmul(M[g][x], nconj(M[gp][x])) for x in range(Ng)])) for gp in range(Ng)] for g in range(Ng)]
    fro = sum(nabs2(MMs[g][gp]) for g in range(Ng) for gp in range(Ng))
    tr = sum(MMs[g][g][0] for g in range(Ng))
    out = []
    for m, l in pairs:
        D = comm(eps(m), eps(l).adj(), Om)
        out.append((m, l, norm2(D), 2 * (l - m) * fro if l > m else 0))
    cen = [inner(Om, comm(eps(m), eps(m).adj(), Om)) for m in (1,)]
    return out, cen, tr, fro

def sum_n(xs):
    s = ZERO
    for x in xs: s = nadd(s, x)
    return s

J = num(0, 1)
cases = [
    (2, 4, 2, [[num(1), J], [num(2), num(0, -1)]], [(0, 1), (0, 2), (-1, 1), (1, 2), (2, 1)]),
    (2, 3, 1, [[num(1, 1), num(0)], [num(0), num(1, -1)]], [(0, 1)]),        # unitary-scalar MM* = 2: equality case
    (3, 2, 1, [[num(1), J, num(0)], [num(0), num(1), num(1, 1)], [num(2), num(0), num(-1)]], [(0, 1)]),
    (3, 2, 1, [[num(1), num(0), num(0)], [num(0), num(1), num(0)], [num(0), num(0), num(1)]], [(0, 1)]),
]
for Ng, L, h, M, pairs in cases:
    out, cen, tr, fro = run(Ng, L, h, M, pairs)
    print('N =', Ng, 'L =', L, 'h =', h, ' tr MM* =', tr, ' ||MM*||_F^2 =', fro, ' central <[eps_1, eps_1*]> =', cen,
          ' bound 2 tr^2/N =', F(2) * tr * tr / Ng)
    for m, l, got, want in out:
        print('   (m, l) =', (m, l), ' ||D Omega||^2 =', got, ' 2(l - m)||MM*||^2 =', want, ' OK' if got == want else ' MISMATCH')
