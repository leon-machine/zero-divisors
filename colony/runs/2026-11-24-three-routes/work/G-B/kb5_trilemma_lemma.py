"""KB5: in the stored two-path model, an element of the matter algebra Cl(1,1) that commutes with the path
projector P_1 and with one mixing detection U^{-1} P_1 U (pq != 0) is a number. Exact (GA).
Also KB3: the first-order signal of the stored device result is linear in the coherence (a, b)."""
import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
import GA
SQ = (1, -1)
e1, e2 = GA.gen(0), GA.gen(1)
v = GA.scal(F(1, 2), GA.add(e1, e2)); w = GA.scal(F(1, 2), GA.sub(e1, e2))
P1 = GA.mul(v, w, SQ)
basis = [GA.sc(1), e1, e2, GA.mul(e1, e2, SQ)]
def comm(a, b): return GA.sub(GA.mul(a, b, SQ), GA.mul(b, a, SQ))
def vec(x): return [x.get(b, 0) for b in [(), (0,), (1,), (0, 1)]]
for (p, q) in [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(1), F(0))]:
    U = GA.add(GA.sc(p), GA.scal(q, e2)); Ui = GA.sub(GA.sc(p), GA.scal(q, e2))
    O = GA.mul(GA.mul(Ui, P1, SQ), U, SQ)
    # linear map F -> ([F, P1], [F, O]) on the four basis elements; its kernel is the commutant
    rows = [vec(comm(b, P1)) + vec(comm(b, O)) for b in basis]
    rank = GA.rank_of_vectors(rows)
    print("recombiner", p, q, " dimension of {F : [F,P1] = [F,O] = 0} =", 4 - rank)
