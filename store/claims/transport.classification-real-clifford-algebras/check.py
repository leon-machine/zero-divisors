"""transport.classification-real-clifford-algebras: exact checks.

The statement restates the primer's classification as an eight-entry table in d = p - q mod 8.
The exact Wedderburn invariants are computed by the primer's classifier (semisimple trace form,
centre from the blades commuting with every generator, a primitive idempotent f whose corner
f A f is identified exactly as R, C or H, and dim(A f) = k dim D), taken from the premise's
check through premise(); this check holds the eight-entry table and tests it on every
signature with n = p + q <= 8 (45 signatures), together with the simplicity clause
"simple except d in {1, 5}".
"""
import GA
from tp_premise import premise


def check_eight_entry_table():
    ex = premise("primer.classification-real-clifford-algebras")
    clifford_type = ex["clifford_type"]
    # d: (D, summands)
    table = [("R", 1), ("R", 2), ("R", 1), ("C", 1), ("H", 1), ("H", 2), ("H", 1), ("C", 1)]
    dimD = {"R": 1, "C": 2, "H": 4}
    ok = True
    count = 0
    for n in range(0, 9):
        for p in range(n + 1):
            q = n - p
            d = (p - q) % 8
            t = clifford_type(p, q)
            D, s = table[d]
            k = t["k"]
            ok = ok and t["semisimple"] and t["D"] == D and t["summands"] == s and k is not None
            ok = ok and s * k * k * dimD[D] == 2 ** n and t["left_ideal_dim"] == k * dimD[D]
            # simple (centre a field) exactly when d is not 1 or 5
            ok = ok and ((t["centre"] == "R+R") == (d in (1, 5)))
            count += 1
    ok = ok and count == 45
    GA.check("d-table of Cl(p,q) for all 45 signatures with n <= 8", ok)
    return ok


def check_matrix_sizes_sample():
    ex = premise("primer.classification-real-clifford-algebras")
    clifford_type = ex["clifford_type"]
    # independently tabulated sizes k (entry Mat_k(D), or Mat_k(D) + Mat_k(D))
    expect = {(1, 3): ("H", 2), (3, 1): ("R", 4), (0, 4): ("H", 2), (4, 0): ("H", 2),
              (2, 2): ("R", 4), (0, 5): ("C", 4), (3, 3): ("R", 8), (1, 4): ("H", 2),
              (0, 8): ("R", 16), (6, 0): ("H", 4), (2, 0): ("R", 2), (0, 2): ("H", 1)}
    ok = True
    for (p, q), (D, k) in expect.items():
        t = clifford_type(p, q)
        ok = ok and t["D"] == D and t["k"] == k
    GA.check("matrix sizes k of twelve sample signatures", ok)
    return ok
