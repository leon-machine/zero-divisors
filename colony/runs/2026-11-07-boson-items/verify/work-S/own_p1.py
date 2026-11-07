"""Own route for P1 (iii): commutant of the plane generators in Cl(N, N+2) as the exact nullspace of
x -> [g, x] over all plane generators g (Gaussian elimination over Fractions, no blade-by-blade argument),
then the squares of its even elements. Also: contrast commutant with the radial plane in the ground."""
import sys
from fractions import Fraction as F
sys.path.insert(0, "/home/claude/phys-graph/lib")
import GA

def level(N):
    sq = [1, -1, -1, -1]; planes = [(0, 1)]
    for _ in range(N - 1):
        i = len(sq); sq += [1, -1]; planes.append((i, i + 1))
    return tuple(sq), planes

def nullspace(rows, ncols):
    rows = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None: continue
        rows[r], rows[p] = rows[p], rows[r]
        inv = 1 / rows[r][c]; rows[r] = [x * inv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]; rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        piv.append(c); r += 1
        if r == len(rows): break
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * ncols; v[fc] = F(1)
        for i, pc in enumerate(piv): v[pc] = -rows[i][fc]
        basis.append(v)
    return basis

def commutant(gens, sq):
    n = len(sq); bl = GA.all_blades(n); idx = {b: i for i, b in enumerate(bl)}
    rows = []
    for g in gens:
        # column j = [g, blade_j] expanded
        cols = []
        for b in bl:
            c = GA.sub(GA.mul(g, {b: F(1)}, sq), GA.mul({b: F(1)}, g, sq))
            cols.append(c)
        for bb in bl:
            rows.append([cols[j].get(bb, F(0)) for j in range(len(bl))])
    rows = [r for r in rows if any(r)]
    ns = nullspace(rows, len(bl))
    return [{bl[i]: v[i] for i in range(len(bl)) if v[i] != 0} for v in ns]

for N in (1, 2, 3):
    sq, planes = level(N)
    gens = [GA.gen(i) for pl in planes for i in pl]
    C = commutant(gens, sq)
    grades = sorted(sorted({len(b) for b in x}) for x in C)
    print("N", N, "dim commutant", len(C), "grades", grades)
# contrast at N = 2: radial plane in the ground
sq, planes = level(2)
C = commutant([GA.gen(4), GA.gen(5)], sq)
ev = [x for x in C if all(len(b) % 2 == 0 for b in x)]
print("contrast N=2: dim", len(C), "even-only basis vectors", len(ev))
# which even elements a*I4 + b*J (+ other even) square to -1? check I4 and J both commute with tower plane
I4 = GA.mul(GA.mul(GA.gen(0), GA.gen(1), sq), GA.mul(GA.gen(2), GA.gen(3), sq), sq)
J = GA.mul(GA.gen(2), GA.gen(3), sq)
print("I4, J commute with (e1',f1'):", all(GA.commutes(x, GA.gen(i), sq) for x in (I4, J) for i in (4, 5)),
      "; I4 commutes with radial e0:", GA.commutes(I4, GA.gen(0), sq))
