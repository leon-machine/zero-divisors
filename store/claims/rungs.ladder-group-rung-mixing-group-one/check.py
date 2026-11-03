"""rungs.ladder-group-rung-mixing-group-one: exact checks.

Fock model of the n-th rung's module, n = 1, 2, 3: modes 0..n-1 are the new rung modes v_1..v_n, modes
n..n+2 the three old pairs of W; Jordan-Wigner creation and annihilation operators act on basis states
(bitmasks) with exact integer signs, a basis state being a^dag_(m1) ... a^dag_(mk) |0> with m1 < ... < mk, so
the state with rung r and pair set S is e_r (x) f_S (the wedge basis of Lambda W in the same order). The
rung-mixing generator of X in gl(n) (the complexification of u(n)) is sum X_rs a^dag_r a_s over the rung
modes, the pair-mixing generator of Y in gl(3) the same over the pair modes.
(1) On the sector Lambda^1 R_n (x) Lambda^even W = C^n (x) CS, for every elementary X the rung-mixing
    operator equals X (x) 1 (the ladder action U (x) 1 on the n-tuple of conformal spinors), exactly, and
    nothing leaves the sector.
(2) For every elementary Y the pair-mixing operator acts on the same sector as 1 (x) Lambda^even(Y),
    with Lambda^even(Y) the derivation on the wedge basis computed independently of the Fock signs.
"""
from fractions import Fraction as F  # noqa: F401
from itertools import combinations

import GA  # noqa: F401
import fock
from tp_premise import premise

RUNGS = [1, 2, 3]


# a_i^dag, a_i on sparse Fock states {bitmask: coefficient} (LSB, Jordan-Wigner) and their sum, from lib/fock.py
cre, ann, st_add = fock.cre_on, fock.ann_on, fock.vadd


def bilinear(X, modes, st):
    """sum_rs X_rs a^dag_(modes r) a_(modes s) on a Fock state."""
    terms = []
    for r in range(len(modes)):
        for s in range(len(modes)):
            if X[r][s]:
                terms.append({b: X[r][s] * c for b, c in cre(modes[r], ann(modes[s], st)).items()})
    return st_add(*terms) if terms else {}


def mask(modes):
    return sum(1 << m for m in modes)


def _wedge(seq):
    if len(set(seq)) < len(seq):
        return 0, None
    seq = list(seq)
    sign = 1
    for i in range(len(seq)):
        for j in range(len(seq) - 1 - i):
            if seq[j] > seq[j + 1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                sign = -sign
    return sign, tuple(seq)


def derive(Y, S):
    out = {}
    for t, s in enumerate(S):
        for r in range(len(Y)):
            if Y[r][s]:
                sg, T = _wedge(S[:t] + (r,) + S[t + 1:])
                if sg:
                    out[T] = out.get(T, 0) + sg * Y[r][s]
    return {T: c for T, c in out.items() if c}


def unit(n, i, j):
    return [[1 if (a, b) == (i, j) else 0 for b in range(n)] for a in range(n)]


def sector(n):
    """(r, S, Fock state) for one rung mode r and an even pair set S."""
    out = []
    for r in range(n):
        for k in (0, 2):
            for S in combinations(range(3), k):
                out.append((r, S, {mask([r] + [n + a for a in S]): 1}))
    return out


def check_rung_mixing_is_the_ladder_action():
    premise("rungs.imported-ladder-automorphism-group-no-lepton")
    premise("rungs.rung-spinor-module-mixings")
    ok = True
    count = 0
    for n in RUNGS:
        rungs = list(range(n))
        ok = ok and len(sector(n)) == 4 * n
        for i in range(n):
            for j in range(n):
                X = unit(n, i, j)
                for r, S, st in sector(n):
                    img = bilinear(X, rungs, st)
                    want = st_add(*[{mask([q] + [n + a for a in S]): X[q][r]} for q in range(n) if X[q][r]])
                    ok = ok and img == want
                    count += 1
    _tp_rv = (ok and count == 4 * (1 + 8 + 27)); assert _tp_rv is not False, "check_rung_mixing_is_the_ladder_action"; return _tp_rv


def check_pair_mixing_acts_on_the_spinor_factor():
    premise("rungs.rung-spinor-module-mixings")
    ok = True
    for n in RUNGS:
        pairs = [n, n + 1, n + 2]
        for a in range(3):
            for b in range(3):
                Y = unit(3, a, b)
                for r, S, st in sector(n):
                    img = bilinear(Y, pairs, st)
                    want = st_add(*[{mask([r] + [n + t for t in T]): c} for T, c in derive(Y, S).items()])
                    ok = ok and img == want
                    ok = ok and all(bin(m >> n).count("1") % 2 == 0 and bin(m & ((1 << n) - 1)).count("1") == 1
                                    for m in img)
    _tp_rv = (ok); assert _tp_rv is not False, "check_pair_mixing_acts_on_the_spinor_factor"; return _tp_rv
