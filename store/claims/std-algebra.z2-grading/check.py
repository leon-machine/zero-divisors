from fractions import Fraction as F
from itertools import combinations

import GA
import stdalg as S
from tp_premise import premise


def check_parity_and_grade_range():
    premise("std-algebra.involution-properties")
    premise("std-algebra.grade-decomposition")
    ok = True
    tested = 0
    for p, q, r in S.signatures(4):
        sq = GA.sig(p, q, r)
        n = len(sq)
        ok = ok and len([b for b in GA.all_blades(n) if len(b) % 2 == 0]) == 2 ** (n - 1)
        x = S.sample(n, 2)
        y = S.sample(n, 5)
        for j in range(n + 1):
            for k in range(n + 1):
                prod = GA.mul(S.grade(x, j), S.grade(y, k), sq)
                allowed = {abs(j - k) + 2 * m for m in range(min(j, k) + 1)}
                ok = ok and all(len(b) in allowed for b in prod)
                ok = ok and all(len(b) % 2 == (j + k) % 2 for b in prod)
                tested += 1
    ok = ok and tested == 3 * 4 + 6 * 9 + 10 * 16 + 15 * 25
    GA.check("parity rule, dim Cl+ = 2^(n-1), and grades of a j-vector times a k-vector", ok)
    return ok
