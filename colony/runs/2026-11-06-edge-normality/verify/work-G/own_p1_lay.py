# Does adding an anisotropic (0,2) plane switch real <-> quaternionic?  Arf of q_(p,q) from GA squares.
from fractions import Fraction as F
import sys
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA
def arf(p, q):
    n = p + q; S = GA.sig(p, q); minus = 0
    for m in range(2 ** n):
        bl = tuple(i for i in range(n) if m >> i & 1)
        if GA.mul({bl: F(1)}, {bl: F(1)}, S)[()] == -1: minus += 1
    return 1 if minus > 2 ** (n - 1) else 0
for p, q in ((0, 0), (2, 0), (1, 1), (0, 2), (4, 0), (3, 1)):
    print(f"Cl({p},{q}) Arf={arf(p,q)}  ->  Cl({p},{q+2}) Arf={arf(p,q+2)};  Arf(q_({q},{p}))+1 = {(arf(q,p)+1)%2}")
