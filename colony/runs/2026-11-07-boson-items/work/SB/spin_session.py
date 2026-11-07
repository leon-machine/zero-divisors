"""SB, bos.spin-statistics: spin on the ladder as the one-particle rotation U(theta) = exp(theta J L),
L = sum_j s_j n_j, evaluated exactly at multiples of pi. Kill conditions K1-K3 in findings/attack-SB.md."""
import sys; sys.path.insert(0, '/home/claude/phys-graph/lib')
from fractions import Fraction as F
import GA
mul, add, sub, neg, scal, sc, gen, eq = GA.mul, GA.add, GA.sub, GA.neg, GA.scal, GA.sc, GA.gen, GA.eq
ok_all = True
def chk(label, ok):
    global ok_all; ok_all &= bool(ok); print(("PASS " if ok else "FAIL ") + label)

def build(N):
    sq = [-1, -1]; planes = []
    for k in range(N):
        i = len(sq); sq += [1, -1]; planes.append((i, i + 1))
    return tuple(sq), planes
def dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g * (g - 1) // 2) * (-1) ** sum(1 for i in b if sq[i] == -1)
        out[b] = c * s
    return {b: c for b, c in out.items() if c != 0}
def prod(xs, sq):
    r = sc(1)
    for x in xs: r = mul(r, x, sq)
    return r

def phase(m, s, J):
    """exp(m pi J s) for integer m and s in (1/2)Z: cos + J sin at a multiple of pi/2."""
    t = (2 * m * s) % 4   # angle in units of pi/2
    assert t.denominator == 1
    return [sc(1), J, sc(-1), neg(J)][int(t)]

def U(m, spins, ops, J, sq):
    """U(m pi) = prod_j (1 - n_j + exp(m pi J s_j) n_j)."""
    return prod([add(sub(sc(1), n), mul(phase(m, s, J), n, sq)) for s, n in zip(spins, ops['n'])], sq)

def setup(N):
    sq, planes = build(N)
    J = mul(gen(0), gen(1), sq)
    v = [scal(F(1, 2), add(gen(p), gen(m))) for p, m in planes]
    w = [scal(F(1, 2), sub(gen(p), gen(m))) for p, m in planes]
    n = [mul(v[j], w[j], sq) for j in range(N)]
    pl = [mul(gen(p), gen(m), sq) for p, m in planes]
    return sq, J, dict(v=v, w=w, n=n, pl=pl)

print("1. U(2pi) = product of plane pseudoscalars e_j f_j over half-integer s_j (K1)")
import itertools
half = [F(1, 2), F(3, 2), F(-1, 2)]; whole = [F(0), F(1), F(-1)]
for N in (1, 2, 3):
    sq, J, o = setup(N)
    chk(f"N={N}: n_j = (1 - e_j f_j)/2", all(eq(o['n'][j], scal(F(1, 2), sub(sc(1), o['pl'][j]))) for j in range(N)))
    Gam = prod(o['pl'], sq)
    for spins in itertools.product([F(1, 2), F(0), F(-1, 2), F(1), F(3, 2)], repeat=N):
        U2 = U(2, spins, o, J, sq); U1 = U(1, spins, o, J, sq)
        S = [j for j in range(N) if spins[j].denominator == 2]
        good = eq(U2, prod([o['pl'][j] for j in S], sq))
        good &= eq(mul(U1, U1, sq), U2)                                   # group law U(pi)^2 = U(2pi)
        good &= eq(mul(dag(U1, sq), U1, sq), sc(1))                       # unitary
        good &= GA.commutes(U1, J, sq)
        Ui = dag(U1, sq)
        good &= all(eq(mul(mul(U1, o['w'][j], sq), Ui, sq), mul(phase(-1, spins[j], J), o['w'][j], sq)) for j in range(N))
        good &= all(eq(mul(mul(U1, o['v'][j], sq), Ui, sq), mul(phase(1, spins[j], J), o['v'][j], sq)) for j in range(N))
        U2i = dag(U2, sq)
        adU_is_parity = all(eq(mul(mul(U2, x, sq), U2i, sq), mul(mul(Gam, x, sq), Gam, sq)) for x in o['w'] + o['v'])
        good &= (adU_is_parity == (len(S) == N))
        if not good: chk(f"N={N} spins={spins}", False)
    chk(f"N={N}: all spin assignments in {{-1/2,0,1/2,1,3/2}}^N: U(2pi) = prod over half-integer planes, U(pi)^2 = U(2pi), "
        f"unitary, commutes with J, U(pi) w_j U(pi)^-1 = exp(-pi J s_j) w_j, and Ad U(2pi) = Ad Gamma iff every s_j half-integer", True)
    allhalf = U(2, [F(1, 2)] * N, o, J, sq)
    chk(f"N={N}: all s_j = 1/2: U(2pi) = Gamma exactly", eq(allhalf, Gam))

print("\n2. Counter-model: blocks with a spin-1/2 lower mode and a spin-0 upper mode (K2)")
for Nb in (1, 2, 3):
    sq, J, o = setup(2 * Nb)
    spins = [F(1, 2), F(0)] * Nb
    U2 = U(2, spins, o, J, sq); U2i = dag(U2, sq)
    b = [mul(o['v'][2 * i], o['w'][2 * i + 1], sq) for i in range(Nb)]
    chk(f"Nb={Nb}: each hopping element b_i = v_(1i) w_(2i) has U(2pi) b U(2pi)^-1 = -b (half-integer spin)",
        all(eq(mul(mul(U2, x, sq), U2i, sq), neg(x)) for x in b))
    chk(f"Nb={Nb}: hopping elements and adjoints of distinct blocks commute (Bose statistics)",
        all(GA.commutes(b[i], y, sq) for i in range(Nb) for j in range(Nb) if j != i for y in (b[j], dag(b[j], sq))))
    upper = [o['w'][2 * i + 1] for i in range(Nb)]
    chk(f"Nb={Nb}: each spin-0 upper mode is 2pi-invariant (integer spin) and anticommutes with every other mode",
        all(eq(mul(mul(U2, x, sq), U2i, sq), x) for x in upper) and
        all(GA.anticommutes(upper[0], y, sq) for y in o['w'][1:] + o['v'][2:]))
    # Holstein-Primakoff ladder on the polarised idempotent (lower filled, upper empty)
    Bs = add(*[dag(x, sq) for x in b]); Bc = add(*b)            # sqrt(N) B*, sqrt(N) B
    C = sub(mul(Bc, Bs, sq), mul(Bs, Bc, sq))                    # N [B, B*]
    P = prod([mul(o['n'][2 * i], sub(sc(1), o['n'][2 * i + 1]), sq) for i in range(Nb)], sq)
    vec = P; good = True
    for k in range(Nb + 1):
        good &= vec != {} and eq(mul(C, vec, sq), scal(F(Nb - 2 * k), vec))
        vec = mul(Bs, vec, sq)
    good &= vec == {}
    chk(f"Nb={Nb}: on (B*)^k P_pol, N[B,B*] = N - 2k (so [B,B*] = 1 - 2k/N), nonzero for k <= N, (B*)^(N+1) P_pol = 0", good)

print("\n3. Rotations the tower supplies by itself give integer spin to every element (K3)")
for N in (1, 2):
    sq, J, o = setup(N)
    chk(f"N={N}: J commutes with every transport generator, so Ad exp(theta J/2) is the identity on the transport algebra; J^2 = -1",
        all(GA.commutes(J, gen(i), sq) for i in range(2, len(sq))) and eq(mul(J, J, sq), sc(-1)))
sq, J, o = setup(2)
(e0, f0), (e1, f1) = (gen(2), gen(3)), (gen(4), gen(5))
L = sub(mul(o['v'][0], o['w'][1], sq), mul(o['v'][1], o['w'][0], sq))
B1, B2 = mul(e0, e1, sq), mul(f0, f1, sq)
chk("real mode rotation L = v_0 w_1 - v_1 w_0 = (e_0 e_1 - f_0 f_1)/2, two commuting bivectors each squaring to -1",
    eq(L, scal(F(1, 2), sub(B1, B2))) and GA.commutes(B1, B2, sq) and eq(mul(B1, B1, sq), sc(-1)) and eq(mul(B2, B2, sq), sc(-1)))
# exp(2 pi L) = exp(pi B1) exp(-pi B2) = (-1)(-1) = +1; its half-speed version exp(pi L) = exp(pi B1/2) exp(-pi B2/2) = B1 (-B2)
half_rot = mul(B1, neg(B2), sq)
chk("exp(pi L) = B1(-B2) rotates (w_0, w_1) by pi: w -> -w; exp(2 pi L) = (B1(-B2))^2 = +1",
    all(eq(mul(mul(half_rot, x, sq), dag(half_rot, sq), sq), neg(x)) for x in o['w']) and eq(mul(half_rot, half_rot, sq), sc(1)))
chk("and exp(pi L) = (e_0 f_0)(e_1 f_1) = Gamma of the two planes up to sign",
    eq(half_rot, mul(o['pl'][0], o['pl'][1], sq)) or eq(half_rot, neg(mul(o['pl'][0], o['pl'][1], sq))))
print("\nALL PASS" if ok_all else "\nSOME FAIL")
