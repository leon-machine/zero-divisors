import sys, importlib.util
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
import tp_premise
tp_premise.configure('/home/claude/leon-machine/zero-divisors/store')
from fractions import Fraction as F
spec = importlib.util.spec_from_file_location("stored", '/home/claude/leon-machine/zero-divisors/store/claims/synthesis.first-order-gravitational-field-has-two-free-directions-at-null-momentum-and-four-constraints/check.py')
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
st = m.ST(4)
def G3(H, kap):
    out = [[F(0)]*3 for _ in range(3)]
    for i in range(3):
        j, k = [q for q in range(3) if q != i]
        out[i][i] = -F(1,2)*(kap[k]**2*H[j][j] + kap[j]**2*H[k][k] - 2*kap[j]*kap[k]*H[j][k])
    for i in range(3):
        for j in range(3):
            if i != j:
                k = 3-i-j
                out[i][j] = -F(1,2)*(-kap[k]**2*H[i][j] + kap[i]*kap[k]*H[j][k] + kap[j]*kap[k]*H[i][k] - kap[i]*kap[j]*H[k][k])
    return out
def D3(H, kap):
    return -(sum(kap[i]*kap[j]*H[i][j] for i in range(3) for j in range(3) if i != j) - sum(kap[k]**2*H[i][i] for i in range(3) for k in range(3) if k != i))
def C3(H, kap):
    return [sum(kap[j]*H[i][j] for j in range(3)) for i in range(3)]
Hs = [[F(2),F(-1),F(3)],[F(-1),F(5),F(7)],[F(3),F(7),F(-4)]]
for (w, kap) in [(F(3), (F(1),F(2),F(-2))), (F(-2), (F(3),F(0),F(4))), (F(5), (F(1),F(1),F(7)))]:
    H = [[F(0)]*4 for _ in range(4)]
    for i in range(3):
        for j in range(3):
            H[i+1][j+1] = Hs[i][j]
    E = st.einstein(H, st.vec((w,)+kap))
    tr = sum(Hs[i][i] for i in range(3))
    g3 = G3(Hs, kap); d3 = D3(Hs, kap); c3 = C3(Hs, kap)
    Pi = [[F(1,2)*(Hs[i][j] - (tr if i == j else 0)) for j in range(3)] for i in range(3)]   # pi of h' = h: 1/2(h - delta tr h)
    print("E00", E[0][0], "D3", d3, "ratio", E[0][0]/d3 if d3 else None)
    cp = C3(Pi, kap)
    print("E0i", [E[0][i+1] for i in range(3)], "w*C(pi)", [w*cp[i] for i in range(3)])
    print("Eij - (a w^2 Pi + b G3):")
    for i in range(3):
        print([ (E[i+1][j+1], w*w*Pi[i][j], g3[i][j]) for j in range(3)])
