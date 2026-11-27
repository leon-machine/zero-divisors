"""Find the bivector potential K_xi[h] with  omega(h, D_xi) = 2 E[h](xi) + div K  (symbols)."""
import sys, os, importlib.util
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("r1", os.path.join(LAB, "store/claims/synthesis.null-plane-data-of-the-first-order-gravitational-field-are-the-shear-of-the-generators/check.py"))
r1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(r1)
globals().update({k: v for k, v in vars(r1).items() if not k.startswith("__")})
import random
random.seed(3)

def rv():
    return vec([random.randint(-5, 5) for _ in range(4)])
def rs():
    return sym([random.randint(-5, 5) for _ in range(10)])

def cands(H, p1, xi, p2):
    """candidate bivectors; derivatives of h -> p1, of xi -> p2"""
    t = tr_map(H)
    d = apply(H, p1)                     # div h
    A1 = wedge(xi, d)
    A2 = scal(t, wedge(xi, p1))
    A3 = wedge(p1, apply(H, xi))
    B1 = scal(t, wedge(p2, xi))
    B2 = {}
    B3 = {}
    for a in range(D):
        # e_a . grad xi -> (e_a.p2) xi ;  grad(xi . e_a) -> (xi.e_a) p2
        B2 = add(B2, scal(dot(E[a], p2), wedge(apply(H, REC[a]), xi)))
        B3 = add(B3, scal(dot(E[a], xi), wedge(apply(H, REC[a]), p2)))
    return [A1, A2, A3, B1, B2, B3]

def divK(K, p):
    # (grad . K) -> p . K  (vector)
    return vdotB(p, K)

BL = [(i, j) for i in range(4) for j in range(i + 1, 4)]
rows = []; rhs = []
for trial in range(6):
    H, p1, xi, p2 = rs(), rv(), rv(), rv()
    Dxi = outer(p2, xi)      # a -> (a.p2) xi + (a.xi) p2
    lhs = sub(omega(H, p1, Dxi, p2), scal(2, apply(einstein(H, p1), xi)))
    cs = [divK(K, add(p1, p2)) for K in cands(H, p1, xi, p2)]
    for i in range(4):
        rows.append([c.get((i,), F(0)) for c in cs]); rhs.append(lhs.get((i,), F(0)))
# solve least squares exactly: use GA.mat_rank & elimination
import sympy
M = sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in r] for r in rows])
b = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in rhs])
print("rank", M.rank(), (M.row_join(b)).rank())
sol = M.gauss_jordan_solve(b)
print(sol)
