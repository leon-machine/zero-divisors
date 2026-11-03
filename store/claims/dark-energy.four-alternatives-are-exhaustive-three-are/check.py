"""dark-energy.four-alternatives-are-exhaustive-three-are: exact check on all small finite theories.

The Definition (obj.dark-energy.four-ways-number-enters-theory-shape) is applied verbatim to every finite model
with two parameter values mu_1, mu_2, solution spaces S_mu of two solutions each (four solutions in all), every
quantity q on the solutions with values in {0, 1, 2} (81 functions; on finite solution spaces conservation is
automatic) and every kinematic isomorphism structure on the four solutions (all 15 set partitions):
(K) q is constant on each kinematic class; (D) q is constant on the union; (P) q is constant on each S_mu but
not on the union; (I) q is not constant on some S_mu.
Checked: every q is exactly one of (D), (P), (I), with the counts 3, 6 and 72 derived by hand (3 constants;
3 x 3 per-space constants minus the 3 constants; 81 - 9); (K) occurs together with each of (D), (P), (I), and its
negation occurs with (P) and with (I) but never with (D): (D) implies (K) (a constant factors through every
kinematic class): (K) can hold together with any of them and is excluded by none, (D) implies (K), and (P)
and (I) are compatible with (K) and with its negation, as the statement now says; every q that is neither (K), (D) nor (I) is (P), and such q exist,
so "not kinematic, not dynamical, therefore initial data" fails exactly on the (P) cases.
The claim has no premises (the Definition is an object, not a claim); no premise() call.
"""
from itertools import product

import GA

SOLS = [(0, 0), (0, 1), (1, 0), (1, 1)]   # (parameter index, solution index)
VALUES = (0, 1, 2)


def partitions(items):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for p in partitions(rest):
        for i in range(len(p)):
            yield p[:i] + [[first] + p[i]] + p[i + 1:]
        yield [[first]] + p


def classify(q, part):
    const = lambda xs: len({q[x] for x in xs}) == 1
    per_space = [[s for s in SOLS if s[0] == mu] for mu in (0, 1)]
    K = all(const(block) for block in part)
    D = const(SOLS)
    P = all(const(S) for S in per_space) and not D
    I = not all(const(S) for S in per_space)
    return K, D, P, I


def check_trichotomy_and_independence():
    parts = list(partitions(SOLS))
    qs = [dict(zip(SOLS, vals)) for vals in product(VALUES, repeat=len(SOLS))]
    ok = len(parts) == 15 and len(qs) == 81
    counts = {"D": 0, "P": 0, "I": 0}
    combos = set()
    p_only = 0
    for q in qs:
        _, D, P, I = classify(q, parts[0])
        ok = ok and (D + P + I) == 1
        counts["D" if D else "P" if P else "I"] += 1
        for part in parts:
            K, D, P, I = classify(q, part)
            combos.add((K, "D" if D else "P" if P else "I"))
            if not K and not D and not I:
                ok = ok and P
                p_only += 1
            if not K and not D:
                ok = ok and (I != P)
    ok = ok and counts == {"D": 3, "P": 6, "I": 72}
    # (K) holds with each of the three; its negation holds with (P) and (I) but never with (D): a constant q
    # factors through every kinematic class, so (D) implies (K)
    ok = ok and combos == {(True, "D"), (True, "P"), (True, "I"), (False, "P"), (False, "I")}
    ok = ok and p_only > 0
    GA.check("D, P, I partition the conserved quantities; K excluded by none, D implies K; not K, D, I implies P", ok)
    return ok
