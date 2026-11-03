"""odd-extensions.every-path-mirror-crosses-two-time: exact checks.

The sign-change graph at dimension four is built from the 16 sign assignments of four Clifford
generators (GA.py squares tuples): an edge changes the square of one generator. Its image on
signatures (p, 4 - p) is computed, with the residue p - q mod 8. The checks: every edge moves p by
one and the residue by +-2; the non-revisiting walks from (1,3) to (3,1) (enumerated up to length
six) are exactly one, through (2,2) at residue 0; every walk with revisits up to length eight from
(1,3) to (3,1) passes (2,2); (0,4), at residue 4, has the single neighbour (1,3). The squares of
the generators are read back from GA (e_i^2) rather than from the tuple.
"""
from itertools import product

import GA
from pyutil import get_or_set

ASSIGNMENTS = list(product((1, -1), repeat=4))


def sig_of(sq):
    p = sum(1 for i in range(4) if GA.mul(GA.gen(i), GA.gen(i), sq) == GA.sc(1))
    return (p, 4 - p)


def residue(s):
    return (s[0] - s[1]) % 8


def sig_edges():
    out = set()
    for a in ASSIGNMENTS:
        for i in range(4):
            b = tuple(-x if j == i else x for j, x in enumerate(a))
            out.add((sig_of(a), sig_of(b)))
    return out


def walks(edges, start, end, maxlen, revisit):
    nbr = {}
    for s, t in edges:
        get_or_set(nbr, s, set()).add(t)
    out, stack = [], [[start]]
    while stack:
        w = stack.pop()
        if w[-1] == end and len(w) > 1:
            out.append(w)
            continue
        if len(w) - 1 >= maxlen:
            continue
        for t in sorted(nbr.get(w[-1], ())):
            if revisit or t not in w:
                stack.append(w + [t])
    return out


def check_sign_change_moves_residue_by_two():
    E = sig_edges()
    ok = len({sig_of(a) for a in ASSIGNMENTS}) == 5
    ok = ok and all(abs(s[0] - t[0]) == 1 for s, t in E)
    ok = ok and {(residue(t) - residue(s)) % 8 for s, t in E} == {2, 6}
    ok = ok and len(E) == 8
    GA.check("a sign change moves (p, 4-p) by one step and the residue by +-2", ok)
    return ok


def check_every_path_crosses_two_two():
    E = sig_edges()
    simple = walks(E, (1, 3), (3, 1), 6, False)
    ok = simple == [[(1, 3), (2, 2), (3, 1)]]
    allw = walks(E, (1, 3), (3, 1), 8, True)
    ok = ok and len(allw) > 1 and all((2, 2) in w for w in allw)
    ok = ok and residue((2, 2)) == 0 and residue((1, 3)) == 6 and residue((3, 1)) == 2
    GA.check("every walk from (1,3) to (3,1) passes (2,2), residue 0; one non-revisiting walk", ok)
    return ok


def check_euclidean_dead_end():
    E = sig_edges()
    nbr04 = sorted({t for s, t in E if s == (0, 4)})
    ok = nbr04 == [(1, 3)] and residue((0, 4)) == 4
    nbr13 = sorted({t for s, t in E if s == (1, 3)})
    ok = ok and nbr13 == [(0, 4), (2, 2)]
    GA.check("(0,4) at residue 4 has (1,3) as its only neighbour; (1,3) has (0,4) and (2,2)", ok)
    return ok
