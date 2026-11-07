"""SA work: spin and statistics on a tower level Cl(N, N+2). Exact (Fractions, GA)."""
import sys, itertools
sys.path.insert(0, "/home/claude/phys-graph/lib")
from fractions import Fraction as F
import GA
from galib import *
import galib

def U_of(mul, n, u):
    """U = prod_k (1 + (u - 1) n_k), u = e^{theta J/2} a unit of span{1, J}."""
    out = GA.sc(1)
    um1 = GA.sub(u, GA.sc(1))
    for nk in n:
        out = mul(out, GA.add(GA.sc(1), mul(um1, nk)))
    return out


def unit(c, d, J):
    return GA.add(GA.sc(c), GA.scal(d, J))


for N in (1, 2, 3):
    s, mul, J, v, w, n, Gam, I = level(N)
    # Pythagorean points of the circle: u = c + d J, c^2 + d^2 = 1
    u1 = unit(F(3, 5), F(4, 5), J)
    u2 = unit(F(5, 13), F(-12, 13), J)
    U1, U2 = U_of(mul, n, u1), U_of(mul, n, u2)
    U12 = U_of(mul, n, mul(u1, u2))
    chk(f"N={N}: U unitary, U(a)U(b) = U(a+b)", GA.eq(mul(dag(U1, s), U1), GA.sc(1)) and GA.eq(mul(U1, U2), U12))
    U1inv = dag(U1, s)
    u1inv = dag(u1, s)
    okw = all(GA.eq(mul(mul(U1, w[k]), U1inv), mul(u1inv, w[k])) for k in range(N))
    okv = all(GA.eq(mul(mul(U1, v[k]), U1inv), mul(u1, v[k])) for k in range(N))
    chk(f"N={N}: Ad U(theta) w = e^(-theta J/2) w (left action of the kernel rotor), v -> e^(theta J/2) v", okw and okv)
    # the kernel rotor rotates kernel vectors by theta: R g1 R~ with R = u^{-1} = e^{-theta J/2}
    R = u1inv
    g1r = mul(mul(R, GA.gen(0)), GA.reverse(R))
    # rotation by theta: cos theta = c^2 - d^2 = 9/25 - 16/25 = -7/25, sin theta = 2cd = 24/25
    chk(f"N={N}: kernel rotor e^(-theta J/2) rotates g1 by theta in the kernel plane",
        GA.eq(g1r, GA.add(GA.scal(F(-7, 25), GA.gen(0)), GA.scal(F(24, 25), GA.gen(1)))) or
        GA.eq(g1r, GA.add(GA.scal(F(-7, 25), GA.gen(0)), GA.scal(F(-24, 25), GA.gen(1)))))
    print("   R g1 R~ =", g1r)
    U2pi = U_of(mul, n, GA.sc(-1))
    Upi = U_of(mul, n, J)
    chk(f"N={N}: U(2 pi) = Gamma; U(pi)^2 = Gamma", GA.eq(U2pi, Gam) and GA.eq(mul(Upi, Upi), Gam))
    # Klein twist V = (1 + J Gamma)(1 + J)^{-1}; (1 + J)^{-1} = (1 - J)/2
    V = mul(GA.add(GA.sc(1), mul(J, Gam)), GA.scal(F(1, 2), GA.sub(GA.sc(1), J)))
    JG = mul(J, Gam)
    chk(f"N={N}: Klein twist V^2 = Gamma, V V^dag = 1, J Gamma = +-I_n",
        GA.eq(mul(V, V), Gam) and GA.eq(mul(V, dag(V, s)), GA.sc(1)) and (GA.eq(JG, I) or GA.eq(JG, GA.neg(I))))
    print("   J Gamma = I_n ?", GA.eq(JG, I), " = -I_n ?", GA.eq(JG, GA.neg(I)))
    # weights
    if N >= 2:
        c = mul(w[0], w[1])
        b = mul(v[0], w[1])
        chk(f"N={N}: pairing w1 w2 weight 1 (Ad U = u^-2), hopping weight 0",
            GA.eq(mul(mul(U1, c), U1inv), mul(mul(u1inv, u1inv), c)) and GA.eq(mul(mul(U1, b), U1inv), b))
    # 2 pi sign: odd transport elements -1, even +1, on all transport blades
    okpar = True
    tg = list(range(2, len(s)))
    import itertools
    for k in range(0, len(tg) + 1):
        for bl in itertools.combinations(tg, k):
            x = {bl: F(1)}
            y = mul(mul(U2pi, x), dag(U2pi, s))
            okpar &= GA.eq(y, x if k % 2 == 0 else GA.neg(x))
    chk(f"N={N}: Ad U(2 pi) is the grading on all transport blades", okpar)

# graded locality and the collective brackets
print("\nGraded locality and collective brackets, blocks of two modes, product state")
for NB in (1, 2, 3):
    N = 2 * NB
    s, mul, J, v, w, n, Gam, I = level(N)
    # odd and even test elements on block 0: x1 = w_0, x2 = w_0 n_1 (cubic, odd), y = v_0 w_1 (hop), c = w_0 w_1
    def copy(x, blk):
        # shift planes by 2*blk modes: generators 2 + 2k -> 2 + 2(k + 2 blk)
        out = {}
        for bl, cc in x.items():
            nb = tuple(i if i < 2 else i + 4 * blk for i in bl)
            out[nb] = cc
        return out
    odd1 = w[0]
    odd2 = mul(w[0], n[1])
    odd3 = GA.add(v[0], mul(mul(v[0], v[1]), w[1]))
    ev1 = mul(v[0], w[1])
    ev2 = mul(w[0], w[1])
    ev3 = GA.add(ev1, mul(J, dag(ev1, s)))
    ok = True
    for a in range(NB):
        for bb in range(NB):
            if a == bb:
                continue
            for x in (odd1, odd2, odd3):
                for y in (odd1, odd2, odd3, dag(odd2, s)):
                    ok &= GA.is_zero(acomm(mul, copy(x, a), copy(y, bb)))
                for y in (ev1, ev2, ev3):
                    ok &= GA.is_zero(comm(mul, copy(x, a), copy(y, bb)))
            for x in (ev1, ev2, ev3):
                for y in (ev1, ev2, ev3, dag(ev2, s)):
                    ok &= GA.is_zero(comm(mul, copy(x, a), copy(y, bb)))
    chk(f"{NB} blocks: odd copies anticommute, even copies commute with everything on other blocks", ok)
    # fluctuation brackets: F(x) = sum_k x_k (unnormalised); odd: {F(x), F(y)} = sum_k {x_k, y_k}
    Fx = GA.add(*[copy(odd2, a) for a in range(NB)])
    Fy = dag(Fx, s)
    lhs = acomm(mul, Fx, Fy)
    rhs = GA.add(*[copy(acomm(mul, odd2, dag(odd2, s)), a) for a in range(NB)])
    chk(f"{NB} blocks: {{F(x), F(x)*}} = sum_k {{x_k, x_k*}} for odd cubic x = w_0 n_1", GA.eq(lhs, rhs))
    Ex = GA.add(*[copy(ev3, a) for a in range(NB)])
    lhs = comm(mul, Ex, dag(Ex, s))
    rhs = GA.add(*[copy(comm(mul, ev3, dag(ev3, s)), a) for a in range(NB)])
    chk(f"{NB} blocks: [F(x), F(x)*] = sum_k [x_k, x_k*] for even x = b + J b*", GA.eq(lhs, rhs))
    # and the wrong brackets do not collapse: for odd x the commutator keeps cross terms (NB >= 2)
    if NB >= 2:
        Fx = GA.add(*[copy(odd1, a) for a in range(NB)])
        lhs = comm(mul, Fx, dag(Fx, s))
        rhs = GA.add(*[copy(comm(mul, odd1, dag(odd1, s)), a) for a in range(NB)])
        chk(f"{NB} blocks: for odd x the commutator is NOT the sum of single-block commutators", not GA.eq(lhs, rhs))

print("\nALL:", galib.OK)
