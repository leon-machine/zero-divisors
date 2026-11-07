"""Own route for P4: which spin assignments give EVERY even element (all products of two modes) integer spin,
i.e. Ad U_s(2 pi) fixing all of them? Claim of the Reading: exactly the all-half-integer ones. Test N = 2, 3.
U_s(2 pi) is built here directly as prod_j (1 - 2 n_j)^{[2 s_j odd]} from the CAR (own route: the parity of
2 s_j decides the factor), and compared with the proposal's U."""
import sys, itertools
from fractions import Fraction as F
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
sys.path.insert(0, ".")
import importlib.util
spec = importlib.util.spec_from_file_location("p4", "p4.py"); p4 = importlib.util.module_from_spec(spec)
import tp_premise; tp_premise.configure("/home/claude/phys-graph/store"); spec.loader.exec_module(p4)
SP = [F(1, 2), F(0), F(-1, 2), F(1), F(3, 2)]
for N in (2, 3):
    sq, J, e, f, v, w, n, om = p4._setup(N)
    pairs = [GA.mul(a, b, sq) for a in v + w for b in v + w]
    good = []
    for spins in itertools.product(SP, repeat=N):
        U = GA.sc(1)
        for s, nj in zip(spins, n):
            if (2 * s) % 2 == 1:
                U = GA.mul(U, GA.sub(GA.sc(1), GA.scal(2, nj)), sq)
        assert GA.eq(U, p4._U(2, spins, n, J, sq))
        if all(GA.eq(p4._ad(U, x, sq), x) for x in pairs):
            good.append(tuple(str(s) for s in spins))
    kinds = {("half" if all(F(s).denominator == 2 for s in g) else "int" if all(F(s).denominator == 1 for s in g) else "mixed") for g in good}
    print("N", N, ": assignments with every pair of modes 2pi-invariant:", len(good), "of", 5 ** N, "; kinds:", sorted(kinds))
    # explicit counterexample to the Reading: all spins 0, hopping elements of disjoint blocks commute and are fixed
    U0 = p4._U(2, [F(0)] * N, n, J, sq)
    print("   all s_j = 0: U(2pi) == 1:", GA.eq(U0, GA.sc(1)), "; w_0 has integer spin and anticommutes with w_1:",
          GA.anticommutes(w[0], w[1], sq))
