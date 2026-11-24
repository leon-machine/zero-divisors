"""P-B scratch: reversal on one party (K-B1), two copies (K-B2), the certificate (K-B3), Krein adjoint (K-B5).
Exact arithmetic (Fractions, lib/GA.py)."""
import sys
sys.path.insert(0, '/home/claude/leon-machine/zero-divisors/lib')
from fractions import Fraction as F
from itertools import product
import GA

def setup(n):
    sq = tuple([1, -1] * n)
    ONE = GA.sc(1)
    def pr(*xs):
        r = ONE
        for x in xs:
            r = GA.mul(r, x, sq)
        return r
    e = [GA.gen(2 * k) for k in range(n)]
    f = [GA.gen(2 * k + 1) for k in range(n)]
    p = [pr(f[k], e[k]) for k in range(n)]
    X, Z, Y = [], [], []
    for j in range(n):
        x = e[j]
        for i in range(j):
            x = pr(x, p[i])
        X.append(x); Z.append(p[j]); Y.append(pr(x, p[j]))
    return sq, ONE, pr, e, f, p, X, Z, Y

def dag(x, sq):
    out = {}
    for b, c in x.items():
        g = len(b); s = (-1) ** (g * (g - 1) // 2)
        for i in b:
            s *= sq[i]
        out[b] = c * s
    return out

def s0(x):
    return x.get((), F(0))

def lin(*terms):
    r = {}
    for c, x in terms:
        r = GA.add(r, GA.scal(F(c), x))
    return r

ok = True
def chk(label, cond):
    global ok
    print(('PASS  ' if cond else 'FAIL  ') + label)
    ok = ok and cond

# ---------------- two modes -----------------
sq, ONE, pr, e, f, p, X, Z, Y = setup(2)
U, V, K = pr(X[0], X[1]), pr(Z[0], Z[1]), pr(e[0], f[1])
chk('K = -Y1 Y2, U V = -K', GA.eq(K, GA.neg(pr(Y[0], Y[1]))) and GA.eq(pr(U, V), GA.neg(K)))
def mono(n, X, Z, Y, pr, ONE, word):
    r = ONE
    for j, w in enumerate(word):
        if w == 1: r = pr(r, X[j])
        elif w == 2: r = pr(r, Z[j])
        elif w == 3: r = pr(r, Y[j])
    return r
words2 = list(product(range(4), repeat=2))
monos2 = {w: mono(2, X, Z, Y, pr, ONE, w) for w in words2}
chk('two modes: 16 monomials are signed blades, all different',
    all(len(m) == 1 and abs(list(m.values())[0]) == 1 for m in monos2.values())
    and len({list(m.keys())[0] for m in monos2.values()}) == 16)
chk('dagger of a monomial is (-1)^(number of Y) times it',
    all(GA.eq(dag(m, sq), GA.scal((-1) ** sum(1 for w in wd if w == 3), m)) for wd, m in monos2.items()))
def gammaB(x, monos, bob):
    """reversal on Bob's qubits: sign (-1)^(number of Y factors on Bob's qubits) on each monomial."""
    out = {}
    for wd, m in monos.items():
        (b, c), = m.items()
        if b in x:
            out[b] = x[b] * (-1) ** sum(1 for j in bob if wd[j] == 3)
    return out
def M(c):
    return lin((1, ONE), (-1, U), (-1, V), (c, K))
chk('Gamma_B(M_c) = M_{-c}', all(GA.eq(gammaB(M(c), monos2, [1]), M(-c)) for c in [F(-1), F(0), F(1), F(1, 2), F(3)]))
def atom(u, v):
    return GA.scal(F(1, 4), pr(lin((1, ONE), (u, U)), lin((1, ONE), (v, V))))
w = {(u, v): s0(pr(M(1), atom(u, v))) for u in (1, -1) for v in (1, -1)}
print('   lambda_{+1} on the four joint outcomes of U, V:', w)
chk('lambda_{+1}: weight -1/2 at (+,+), 1/2 at the other three', w[(1, 1)] == F(-1, 2) and all(w[k] == F(1, 2) for k in w if k != (1, 1)))
blades = [{b: F(1)} for b in GA.all_blades(4)]
def gram(Mel, sqx, bl, prx):
    return [[s0(prx(Mel, x, dag(y, sqx))) for y in bl] for x in bl]
print('   inertia of lambda_{+1}(x y^dagger):', GA.congruence_signature(gram(M(1), sq, blades, pr)))
print('   inertia of lambda_{-1}(x y^dagger):', GA.congruence_signature(gram(M(-1), sq, blades, pr)))
# local products: lambda_c the same for all c on the nine products
loc = [pr(s, t) for s in (ONE, X[0], Z[0]) for t in (ONE, X[1], Z[1])]
chk('lambda_{+1} = lambda_{-1} on the nine local products', all(s0(pr(M(1), x)) == s0(pr(M(-1), x)) for x in loc))

# certificate, two modes, sample directions (not anticommuting in general)
def unit(s):
    s = F(s); return ((1 - s * s) / (1 + s * s), 2 * s / (1 + s * s))
def cert_ok(prx, ONEx, A0, A1, B0, B1, ts):
    S, D = GA.add(A0, A1), GA.sub(A0, A1)
    C = GA.add(prx(S, B0), prx(D, B1))
    for t in ts:
        t = F(t)
        Fp, Fm = lin((F(1, 2), ONEx), (F(1, 2), B0)), lin((F(1, 2), ONEx), (F(-1, 2), B0))
        Gp, Gm = lin((F(1, 2), ONEx), (F(1, 2), B1)), lin((F(1, 2), ONEx), (F(-1, 2), B1))
        sm, sp = lin((1, S), (-t, ONEx)), lin((1, S), (t, ONEx))
        dm, dp = lin((1, D), (-t, ONEx)), lin((1, D), (t, ONEx))
        rhs = GA.add(prx(sm, sm, Fp), prx(sp, sp, Fm), prx(dm, dm, Gp), prx(dp, dp, Gm))
        lhs = lin((4 + 2 * t * t, ONEx), (-2 * t, C))
        if not GA.eq(lhs, rhs):
            return False
    return True
good = True
for sa, sb, sc_, sd in [(0, 1, 0, 1), (F(1, 2), 2, F(-1, 3), 3), (F(2, 3), F(-5, 4), 1, F(1, 7))]:
    (x, z), (x2, z2), (x3, z3), (x4, z4) = unit(sa), unit(sb), unit(sc_), unit(sd)
    A0, A1 = lin((x, X[0]), (z, Z[0])), lin((x2, X[0]), (z2, Z[0]))
    B0, B1 = lin((x3, X[1]), (z3, Z[1])), lin((x4, X[1]), (z4, Z[1]))
    good = good and cert_ok(pr, ONE, A0, A1, B0, B1, [0, 1, -1, F(3, 2), F(7, 5)])
chk('certificate 4 + 2t^2 - 2tC = sum of four squares s^2 F (two modes, three configurations, five t)', good)
# the box
A0, A1, B0, B1 = X[0], Z[0], X[1], Z[1]
S, D = GA.add(A0, A1), GA.sub(A0, A1)
C0 = GA.add(pr(S, B0), pr(D, B1))
box = GA.add(ONE, C0)
t = F(1)
terms = []
for (ss, sgn_t, Bq, sgnB) in [(S, -1, B0, 1), (S, 1, B0, -1), (D, -1, B1, 1), (D, 1, B1, -1)]:
    s_ = lin((1, ss), (sgn_t * t, ONE)); Fq = lin((F(1, 2), ONE), (F(sgnB, 2), Bq))
    terms.append(s0(pr(box, s_, s_, Fq)))
print('   box: values of the four squares at t = 1:', terms, 'sum', sum(terms))
chk('box: the four squares at t = 1 sum to 4 + 2 - 2*4 = -2', sum(terms) == -2)
# conditional functionals of lambda_{+1} on Alice's algebra are positive for every outcome of Bob's directions
condok = True
al = [ONE, X[0], Z[0], Y[0]]
for sb in [0, 1, F(1, 2), F(-5, 4), 3]:
    xb, zb = unit(sb)
    for sg in (1, -1):
        Fq = lin((F(1, 2), ONE), (F(sg, 2), lin((xb, X[1]), (zb, Z[1]))))
        G = [[s0(pr(M(1), a1, dag(a2, sq), Fq)) for a2 in al] for a1 in al]
        pos, negs, zer = GA.congruence_signature(G)
        condok = condok and negs == 0
chk('lambda_{+1}: Alice conditional forms given Bob outcomes have no negative direction', condok)

# ---------------- four modes: two per party, two copies -----------------
sq4, ONE4, pr4, e4, f4, p4, X4, Z4, Y4 = setup(4)
words4 = list(product(range(4), repeat=4))
monos4 = {wd: mono(4, X4, Z4, Y4, pr4, ONE4, wd) for wd in words4}
chk('four modes: 256 monomials are signed blades, all different',
    all(len(m) == 1 and abs(list(m.values())[0]) == 1 for m in monos4.values())
    and len({list(m.keys())[0] for m in monos4.values()}) == 256)
chk('four modes: dagger of a monomial is (-1)^(number of Y) times it',
    all(GA.eq(dag(m, sq4), GA.scal((-1) ** sum(1 for w_ in wd if w_ == 3), m)) for wd, m in monos4.items()))
gensA = [e4[0], f4[0], e4[1], f4[1]]
GamA = pr4(p4[0], p4[1])
gensB = [pr4(GamA, v) for v in (e4[2], f4[2], e4[3], f4[3])]
chk('twisted generators of Bob commute with Alice generators', all(GA.commutes(a, b, sq4) for a in gensA for b in gensB))
def in_span_of(x, keys):
    return all(b in keys for b in x)
# Bob's qubit monomials lie in the algebra generated by the twisted generators: check X_2, Z_2, X_3, Z_3
tb = {'e2': gensB[0], 'f2': gensB[1], 'e3': gensB[2], 'f3': gensB[3]}
Z2t = pr4(tb['f2'], tb['e2']); Z3t = pr4(tb['f3'], tb['e3'])
chk('Bob qubits from twisted generators: X_2 = +-Gam e_2, Z_2 = (Gam f_2)(Gam e_2), X_3 = +-(Gam e_3) Z_2, Z_3',
    (GA.eq(X4[2], tb['e2']) or GA.eq(X4[2], GA.neg(tb['e2']))) and (GA.eq(Z4[2], Z2t) or GA.eq(Z4[2], GA.neg(Z2t)))
    and (GA.eq(X4[3], pr4(tb['e3'], Z2t)) or GA.eq(X4[3], GA.neg(pr4(tb['e3'], Z2t))))
    and (GA.eq(Z4[3], Z3t) or GA.eq(Z4[3], GA.neg(Z3t))))
def Mab(a, b, c):
    return lin((1, ONE4), (-1, pr4(X4[a], X4[b])), (-1, pr4(Z4[a], Z4[b])), (-c, pr4(Y4[a], Y4[b])))
def R(c):
    return pr4(Mab(0, 2, c), Mab(1, 3, c))
def lam1(c, w1, w2):
    # value of the two-mode lambda_c on the monomial (w1 on Alice's qubit, w2 on Bob's)
    if (w1, w2) == (0, 0): return F(1)
    if (w1, w2) in ((1, 1), (2, 2)): return F(-1)
    if (w1, w2) == (3, 3): return -F(c)
    return F(0)
cs = [F(-1), F(0), F(1), F(1, 2), F(3)]
prodok = True
for c in cs:
    Rc = R(c)
    for wd, m in monos4.items():
        # monomial = (q0 q2 part)(q1 q3 part) up to sign; value should factor up to that sign
        m02 = mono(4, X4, Z4, Y4, pr4, ONE4, (wd[0], 0, wd[2], 0))
        m13 = mono(4, X4, Z4, Y4, pr4, ONE4, (0, wd[1], 0, wd[3]))
        val = s0(pr4(Rc, m02, m13))
        if val != lam1(c, wd[0], wd[2]) * lam1(c, wd[1], wd[3]):
            prodok = False
chk('two copies: <R_c x>_0 is the product functional lambda_c x lambda_c (256 monomials, five c)', prodok)
def bell(a, b, s, t_):
    return GA.scal(F(1, 4), pr4(lin((1, ONE4), (s, pr4(X4[a], X4[b]))), lin((1, ONE4), (t_, pr4(Z4[a], Z4[b])))))
wok = True
for c in cs:
    Rc = R(c)
    for s, t_, s2, t2 in product((1, -1), repeat=4):
        PA, PB = bell(0, 1, s, t_), bell(2, 3, s2, t2)
        val = s0(pr4(Rc, PA, PB))
        if val != F(1, 16) * (1 + s * s2 + t_ * t2 + s * s2 * t_ * t2 * c * c):
            wok = False
chk('two copies: weight of (atom of Alice two modes)(atom of Bob two modes) = (1 + ss\' + tt\' + ss\'tt\' c^2)/16', wok)
PA, PB = bell(0, 1, 1, 1), bell(2, 3, -1, -1)
chk('the products of atoms are self-adjoint idempotents', GA.eq(pr4(PA, PB, PA, PB), pr4(PA, PB)) and GA.eq(dag(pr4(PA, PB), sq4), pr4(PA, PB)))
print('   c = 1/2: weights', s0(pr4(R(F(1, 2)), PA, PB)), ' c = 3:', s0(pr4(R(3), bell(0, 1, 1, 1), bell(2, 3, 1, -1))))
chk('Gamma_B(R_c) = R_{-c} on four modes', all(GA.eq(gammaB(R(c), monos4, [2, 3]), R(-c)) for c in cs))
saA = [monos4[(a, b, 0, 0)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
saB = [monos4[(0, 0, a, b)] for a in range(4) for b in range(4) if ((a == 3) + (b == 3)) % 2 == 0]
Rp, Rm = R(1), R(-1)
chk('two copies: lambda_{+1}^2 = lambda_{-1}^2 on all 100 products of self-adjoint monomials of the two parties',
    len(saA) == 10 and len(saB) == 10 and all(s0(pr4(Rp, a, b)) == s0(pr4(Rm, a, b)) for a in saA for b in saB))
chk('R_{-1} is 16 times a self-adjoint idempotent (a state)', GA.eq(pr4(Rm, Rm), GA.scal(16, Rm)) and GA.eq(dag(Rm, sq4), Rm))
Pneg = bell(0, 2, 1, 1)
print('   lambda_{+1} x lambda_{+1} on the (+,+) atom of copy one:', s0(pr4(Rp, Pneg)))
chk('lambda_{+1}^2 is not a state: -1/2 on a self-adjoint idempotent', s0(pr4(Rp, Pneg)) == F(-1, 2))
# certificate with two modes per party, parity-even observables
A0, A1 = pr4(X4[0], X4[1]), Z4[0]
B0, B1 = lin((F(3, 5), pr4(X4[2], X4[3])), (F(4, 5), Z4[2])), Z4[3]
obs = all(GA.eq(pr4(x, x), ONE4) and GA.eq(dag(x, sq4), x) for x in (A0, A1, B0, B1))
chk('certificate on four modes (observables that neither commute nor anticommute within a party)',
    obs and cert_ok(pr4, ONE4, A0, A1, B0, B1, [1, F(-2, 3), F(7, 5)]))

# ---------------- Krein adjoint of a ghost floor -----------------
v = [GA.scal(F(1, 2), GA.add(e[k], f[k])) for k in range(2)]   # creators b^*, d^*
wv = [GA.scal(F(1, 2), GA.sub(e[k], f[k])) for k in range(2)]  # annihilators b, d
chk('CAR on the floor', GA.eq(GA.add(pr(v[0], wv[0]), pr(wv[0], v[0])), ONE) and GA.is_zero(GA.add(pr(v[0], wv[1]), pr(wv[1], v[0]))))
Sinv = GA.sub(ONE, pr(GA.sub(v[0], v[1]), GA.sub(wv[0], wv[1])))
chk('S^2 = 1, S self-adjoint, S b S = d', GA.eq(pr(Sinv, Sinv), ONE) and GA.eq(dag(Sinv, sq), Sinv) and GA.eq(pr(Sinv, wv[0], Sinv), wv[1]))
def kdag(x):
    return pr(Sinv, dag(x, sq), Sinv)
chk('Krein adjoint of b is d^*', GA.eq(kdag(wv[0]), v[1]))
G1 = [[s0(pr(x, dag(y, sq))) for y in blades] for x in blades]
G2 = [[s0(pr(x, kdag(y))) for y in blades] for x in blades]
print('   inertia of <x y^dagger>_0:', GA.congruence_signature(G1), '  of <x y^ddagger>_0 (Krein adjoint):', GA.congruence_signature(G2))
Pi0 = pr(wv[0], v[0], wv[1], v[1])   # vacuum projector: annihilated by b, d
chk('vacuum projector', GA.is_zero(pr(wv[0], Pi0)) and GA.is_zero(pr(wv[1], Pi0)) and GA.eq(pr(Pi0, Pi0), Pi0))
psi = pr(GA.add(GA.scal(2, ONE), GA.sub(v[0], v[1])), Pi0)
kn = s0(pr(dag(psi, sq), Sinv, psi))
Eneg = GA.scal(F(1, 2), GA.sub(ONE, Sinv))
val = s0(pr(dag(psi, sq), Sinv, Eneg, psi)) / kn
print('   Krein norm of psi (times <Pi0>):', kn, '  Krein value of (1 - S)/2:', val)
chk('(1 - S)/2 is a self-adjoint idempotent with Krein value -1 on a vector of positive Krein norm',
    GA.eq(pr(Eneg, Eneg), Eneg) and GA.eq(dag(Eneg, sq), Eneg) and kn > 0 and val == -1)
print('ALL OK' if ok else 'SOME FAILED')
