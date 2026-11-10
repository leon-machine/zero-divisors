from ba import *
import random
random.seed(1)
for n in range(1, 7):
    for p in range(n + 1):
        q = n - p
        sq = GA.sig(p, q)
        blades = [b for b in GA.all_blades(n) if b]
        res = set()
        orders = [blades, blades[::-1]] + [random.sample(blades, len(blades)) for _ in range(3 if n < 6 else 1)]
        for od in orders:
            gens, grp = maximal_T(sq, od)
            # maximality: no blade of square 1 commuting with all gens outside +-T
            for b in blades:
                if bsq(b, sq) == 1 and all(bcomm(b, g) for g in gens): assert b in grp, (p, q, b)
            P = idem(sq, gens)
            assert dag(P, sq) == P and clean(prod(sq, P, P)) == P and s0(P) == F(1, 2 ** len(gens))
            res.add((len(gens),) + corner_dims(sq, P))
        print((p, q), sorted(res))
