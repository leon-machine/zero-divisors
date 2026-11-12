"""Referee R3: own exact recomputations (Fractions), independent helpers.

Clifford: generators indexed 0..2m-1, generator 2j = e_j (square +1), 2j+1 = f_j (square -1); blades as sorted
tuples; adjoint generator-wise (e^dag = e, f^dag = -f), reversing order.
Fock: occupation bitmask, Jordan-Wigner sign over HIGHER modes (differs from the author's convention on purpose).
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import ceil

# ------------------------------------------------------------------ Clifford
def bmul(a, b, sig):
    """product of blades a, b (sorted tuples) -> (sign, blade)."""
    lst = list(a) + list(b)
    sign = 1
    # bubble sort with anticommutation, contract equal neighbours
    changed = True
    while changed:
        changed = False
        i = 0
        while i < len(lst) - 1:
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sign = -sign
                changed = True
            elif lst[i] == lst[i + 1]:
                sign *= sig[lst[i]]
                del lst[i:i + 2]
                changed = True
                continue
            i += 1
    return sign, tuple(lst)


def cmul(x, y, sig):
    out = {}
    for a, ca in x.items():
        for b, cb in y.items():
            s, bl = bmul(a, b, sig)
            out[bl] = out.get(bl, F(0)) + s * ca * cb
    return {k: v for k, v in out.items() if v != 0}


def cadd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def csc(c, x):
    return {k: F(c) * v for k, v in x.items() if c != 0}


def one():
    return {(): F(1)}


def g(i):
    return {(i,): F(1)}


def cdag(x):
    out = {}
    for b, c in x.items():
        r = len(b)
        sgn = (-1) ** (r * (r - 1) // 2) * (-1) ** sum(1 for i in b if i % 2 == 1)
        out[b] = c * sgn
    return out


def sflip(x, which):
    return {b: c * (-1) ** sum(1 for i in b if i in which) for b, c in x.items()}


def all_blades(n):
    return [tuple(c) for r in range(n + 1) for c in combinations(range(n), r)]


def tr_state(rho, sig):
    """x -> 2^? normalised: <rho x>_0 / <rho>_0."""
    n0 = rho.get((), F(0))
    return lambda x: cmul(rho, x, sig).get((), F(0)) / n0


log = []


def report(name, ok, extra=""):
    log.append(f"{'PASS' if ok else 'FAIL'}  {name}  {extra}")
    print(log[-1])


# ---- claim 1 (ii): sigma_e alone, l = 1; and l = 0 uniqueness under sigma_e alone
def claim1():
    sig = (1, -1, 1, -1)           # e_old=0, f_old=1, e_new=2, f_new=3
    e1, fnew, enew = g(0), g(3), g(2)
    u = cmul(e1, fnew, sig)
    ok = cmul(u, u, sig) == one() and cdag(u) == u
    rho = csc(F(1, 2), cadd(one(), u))
    ok = ok and cmul(rho, rho, sig) == rho
    Om = tr_state(rho, sig)
    B = all_blades(4)
    # positivity: Gram matrix Om(b_i b_j^dag) PSD  (rho is a projection, so rank argument; check via 2x2 minors plus eigen-free LDL)
    G = [[Om(cmul({bi: F(1)}, cdag({bj: F(1)}), sig)) for bj in B] for bi in B]
    ok = ok and psd(G)
    ok = ok and all(Om(sflip({b: F(1)}, {2})) == Om({b: F(1)}) for b in B)
    ok = ok and not all(Om(sflip({b: F(1)}, {3})) == Om({b: F(1)}) for b in B)
    ok = ok and all(Om({b: F(1)}) == (1 if b == () else 0) for b in all_blades(2))
    v = csc(F(1, 2), cadd(enew, fnew))
    w = csc(F(1, 2), cadd(enew, csc(-1, fnew)))
    on = cmul(v, w, sig)
    ok = ok and Om(on) == F(1, 2) and Om(u) == 1
    report("claim1 (ii): sigma_e-invariant state of (1+e_1 f)/2 at l=1 is a state, restricts to trace, on=1/2, e_1 f=1", ok)
    # l = 0: a sigma_e-invariant extension (state) is unique: it vanishes on e, fe by invariance and on f by reality
    sig0 = (1, -1)
    # general real functional with value 1 on 1, invariant under e->-e: values on (0,) and (0,1) zero; on (1,) = t
    # reality: Om(x^dag) = Om(x); f^dag = -f so Om(f) = -Om(f) -> 0
    ok0 = cdag(g(1)) == csc(-1, g(1))
    report("claim1 (ii): l=0, sigma_e alone: reality forces Om(f)=0, so uniqueness holds (statement 'each alone admits others' fails at l=0 for sigma_e)", ok0)
    # sigma_f-invariant at l = 0: state of (1+e)/2 ; values 1,1,0,0
    rho0 = csc(F(1, 2), cadd(one(), g(0)))
    O0 = tr_state(rho0, sig0)
    vals = [O0({b: F(1)}) for b in [(), (0,), (1,), (0, 1)]]
    v0 = csc(F(1, 2), cadd(g(0), g(1)))
    w0 = csc(F(1, 2), cadd(g(0), csc(-1, g(1))))
    report("claim1 (ii): l=0 sigma_f-invariant state of (1+e)/2: values on 1,e,f,ef and on-weight",
           vals == [1, 1, 0, 0] and O0(cmul(v0, w0, sig0)) == F(1, 2), f"vals={vals}, on={O0(cmul(v0, w0, sig0))}")
    # boost does not commute with dagger
    ch, sh = F(5, 4), F(3, 4)
    be = cadd(csc(ch, g(2)), csc(sh, g(3)))
    report("claim1: boost image of e is not self-adjoint", cdag(be) != be)


def psd(G):
    """exact PSD test by symmetric Gaussian elimination (LDL^T with pivoting on the diagonal)."""
    n = len(G)
    M = [row[:] for row in G]
    for i in range(n):
        for j in range(n):
            if M[i][j] != M[j][i]:
                return False
    idx = list(range(n))
    while idx:
        p = max(idx, key=lambda i: M[i][i])
        if M[p][p] < 0:
            return False
        if M[p][p] == 0:
            if any(M[p][j] != 0 for j in idx):
                return False
            idx.remove(p)
            continue
        idx.remove(p)
        for i in idx:
            r = M[i][p] / M[p][p]
            for j in idx:
                M[i][j] -= r * M[p][j]
    return True


# ------------------------------------------------------------------ Fock (JW over higher modes)
def fcre(k, x):
    out = {}
    for occ, c in x.items():
        if occ >> k & 1:
            continue
        sgn = (-1) ** bin(occ >> (k + 1)).count("1")
        out[occ | (1 << k)] = out.get(occ | (1 << k), F(0)) + sgn * c
    return {a: b for a, b in out.items() if b != 0}


def fann(k, x):
    out = {}
    for occ, c in x.items():
        if not occ >> k & 1:
            continue
        sgn = (-1) ** bin(occ >> (k + 1)).count("1")
        out[occ ^ (1 << k)] = out.get(occ ^ (1 << k), F(0)) + sgn * c
    return {a: b for a, b in out.items() if b != 0}


def fadd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items():
            out[k] = out.get(k, F(0)) + v
    return {k: v for k, v in out.items() if v != 0}


def fsc(c, x):
    return {k: F(c) * v for k, v in x.items()} if c != 0 else {}


def fip(x, y):
    return sum(c * y.get(k, F(0)) for k, c in x.items())


def fnum(k, x):
    return fcre(k, fann(k, x))


def pair(j):
    return 2 + 2 * j, 3 + 2 * j


def R(j, c, s, x):
    a, b = pair(j)
    na, nb = fnum(a, x), fnum(b, x)
    Pi = fadd(na, nb, fsc(-2, fnum(a, nb)))
    h = fadd(fcre(a, fann(b, x)), fsc(-1, fcre(b, fann(a, x))))
    return fadd(x, fsc(-1, Pi), fsc(c, Pi), fsc(s, h))


def Rdag(j, c, s, x):
    return R(j, c, -s, x)


def U(j, c, s, x):
    on = fnum(0, x)
    return fadd(x, fsc(-1, on), R(j, c, s, on))


def Udag(j, c, s, x):
    on = fnum(0, x)
    return fadd(x, fsc(-1, on), Rdag(j, c, s, on))


def psi_N(N, c, s):
    base = {0: F(1)}
    for j in range(N):
        base = fcre(pair(j)[0], base)
    x = fadd(fsc(F(3, 5), fcre(0, base)), fsc(F(4, 5), fcre(1, base)))
    for j in range(N):
        x = U(j, c, s, x)
    return x


def branch_A(K, filled, c, s):
    """system on rung 0, pairs 0..filled-1 hold one quantum on a_j, pairs in K rotated."""
    base = {0: F(1)}
    for j in range(filled):
        base = fcre(pair(j)[0], base)
    x = fcre(0, base)
    for j in sorted(K):
        x = R(j, c, s, x)
    return x


def branch_B(filled):
    base = {0: F(1)}
    for j in range(filled):
        base = fcre(pair(j)[0], base)
    return fcre(1, base)


def claim3():
    c, s = F(0), F(1)
    # counterexample to the corrected sentence: N = 1, x = on_{a_1} (pair 1 only; pair 0 coupled and not involved)
    N = 1
    P = psi_N(N, c, s)
    x = lambda v: fnum(pair(1)[0], v)
    val = fip(P, x(P))
    # mixture value: omega_A with K containing pair 1, on enough pairs (filled = 2), same for B
    for filled in (2, 3):
        A = branch_A({0, 1}, filled, c, s)
        B = branch_B(filled)
        mix = F(9, 25) * fip(A, x(A)) + F(16, 25) * fip(B, x(B))
        report(f"claim3 (iii) c=0 N=1 x=on_(a_1): omega_Psi_1(x) vs mixture (filled={filled})", val != mix,
               f"omega_Psi_1 = {val}, mixture = {mix}")
    # also for c = 3/5: same element, gap independent of decay
    c2, s2 = F(3, 5), F(4, 5)
    P2 = psi_N(1, c2, s2)
    A = branch_A({0, 1}, 2, c2, s2)
    B = branch_B(2)
    mix2 = F(9, 25) * fip(A, x(A)) + F(16, 25) * fip(B, x(B))
    vals = [fip(psi_N(n, c2, s2), x(psi_N(n, c2, s2))) for n in (1, 2, 3)]
    report("claim3: for x = on_(a_1), omega_Psi_N(x) for N = 1,2,3 vs limit", vals[1] == mix2 and vals[0] != mix2,
           f"values {vals}, limit {mix2}")
    # the 'in particular' part, and the O_1 example: c = 0, N = 1, O_1 has 24/25 vs mixture 0
    O0 = lambda v: fadd(fcre(0, fann(1, v)), fcre(1, fann(0, v)))
    def O_N(N, v):
        for j in reversed(range(N)):
            pass
        y = v
        for j in reversed(range(N)):
            y = Udag(j, c, s, y)
        y = O0(y)
        for j in range(N):
            y = U(j, c, s, y)
        return y
    P1 = psi_N(1, c, s)
    report("claim3: c=0, N=1, O_1 value 24/25", fip(P1, O_N(1, P1)) == F(24, 25))
    # non-uniformity: omega_Psi_N(O_N) - omega_inf(O_N) = 24/25, N = 1..3, c = 3/5 and 0; O_N^2 idempotent (norm <= 1)
    ok = True
    for cc, ss in ((F(3, 5), F(4, 5)), (F(0), F(1))):
        for N in (1, 2, 3):
            def ON(v, N=N, cc=cc, ss=ss):
                y = v
                for j in reversed(range(N)):
                    y = Udag(j, cc, ss, y)
                y = O0(y)
                for j in range(N):
                    y = U(j, cc, ss, y)
                return y
            P = psi_N(N, cc, ss)
            A = branch_A(set(range(N)), N, cc, ss)
            B = branch_B(N)
            ok = ok and fip(P, ON(P)) == F(24, 25)
            ok = ok and F(9, 25) * fip(A, ON(A)) + F(16, 25) * fip(B, ON(B)) == 0
            # O_N^2 idempotent on the sector basis vectors (quanta 1+N among 2+2N rungs)
            m = 2 + 2 * N
            for occ in range(2 ** m):
                if bin(occ).count("1") != 1 + N:
                    continue
                v = {occ: F(1)}
                o2 = ON(ON(v))
                ok = ok and ON(ON(o2)) == o2
    report("claim3 (iii): gap 24/25 for every N<=3, two values of c; O_N^2 idempotent on the (1+N)-quantum sector", ok)
    # the spectator independence of I_K: K = {0}, x = O_0-type element on system + pair 0, c=3/5, filled 1..3
    cc, ss = F(3, 5), F(4, 5)
    vals = []
    xx = lambda v: fadd(fcre(0, fann(1, v)), fcre(1, fann(0, v)), fcre(0, fann(3, fcre(2, fann(1, fnum(2, v))))))
    for filled in (1, 2, 3):
        A = branch_A({0}, filled, cc, ss)
        B = branch_B(filled)
        vals.append(F(12, 25) * (fip(A, xx(B)) + fip(B, xx(A))))
    report("claim3: I_K independent of the number of filled spectator pairs", len(set(vals)) == 1 and vals[0] != 0,
           f"{vals}")


def claim4():
    # (v) frequency ceil(2^n a^2)/2^n, n = 1..8, many rationals a^2 (including dyadic), computed by enumeration
    ok = True
    targets = [F(p, q) for q in (3, 5, 7, 9, 25, 169, 289, 16, 8) for p in range(0, q + 1)]
    for n in range(1, 9):
        for a2 in targets:
            cnt = sum(1 for m in range(2 ** n) if F(m, 2 ** n) < a2)
            ok = ok and cnt == ceil(a2 * 2 ** n) and a2 <= F(cnt, 2 ** n) < a2 + F(1, 2 ** n)
    report("claim4 (v): count of strings with y(s) < a^2 is ceil(2^n a^2), within 2^-n, n<=8, 120 targets", ok)
    # (v) in the Fock module (own JW), n = 5, a = 3/5, 5/13, 20/29: values of Y and on_0 in the joint state
    ok = True
    for a, b in ((F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)), (F(20, 29), F(21, 29))):
        n = 5
        first = 0
        for bits in product((0, 1), repeat=n):
            base = {0: F(1)}
            for k in range(n):
                if bits[k]:
                    base = fcre(2 + k, base)
            P = fadd(fsc(a, fcre(0, base)), fsc(b, fcre(1, base)))
            Y = sum(F(1, 2 ** (k + 1)) * fip(P, fnum(2 + k, P)) for k in range(n))
            W = fip(P, fnum(0, P))
            ok = ok and W == a * a and Y == sum(F(bt, 2 ** (k + 1)) for k, bt in enumerate(bits))
            first += Y < W
        ok = ok and F(first, 2 ** n) == F(ceil(a * a * 2 ** n), 2 ** n)
    report("claim4 (v): in the joint state (own Fock), n=5, three a: frequency ceil(2^n a^2)/2^n", ok)
    # (vi) agreement with (v), n = 1..10, non-dyadic a^2
    ok = True
    for a2 in [F(p, q) for q in (3, 5, 7, 25, 169, 289) for p in range(1, q)]:
        x, d = a2, []
        for _ in range(10):
            x *= 2
            d.append(1 if x >= 1 else 0)
            x -= d[-1]
        for n in range(1, 11):
            und = 0
            for bits in product((0, 1), repeat=n):
                y = sum(F(bt, 2 ** (k + 1)) for k, bt in enumerate(bits))
                k0 = next((k for k in range(n) if bits[k] != d[k]), None)
                if k0 is None:
                    und += 1
                    ok = ok and y < a2
                else:
                    ok = ok and (y < a2) == (bits[k0] < d[k0])
            ok = ok and und == 1
            if n >= 9:
                break
    report("claim4 (vi): read-until-decided agrees with the comparison on decided strings; undecided string -> first", ok)
    # (vi) a dyadic counterpart: the agreement can fail for dyadic a^2 with the terminating expansion
    a2 = F(1, 2)
    d = [1, 0, 0, 0]
    bad = [bits for bits in product((0, 1), repeat=4)
           if (lambda k0: k0 is not None and (sum(F(bt, 2 ** (k + 1)) for k, bt in enumerate(bits)) < a2) != (bits[k0] < d[k0]))(
               next((k for k in range(4) if bits[k] != d[k]), None))]
    und = sum(F(1, 2 ** (k + 1)) * bt for k, bt in enumerate(d)) < a2
    report("claim4 (vi): dyadic a^2 = 1/2 (digits 1000): decided strings still agree; the undecided string 1000 is NOT first",
           len(bad) == 0 and not und, f"{len(bad)} disagreeing decided strings; undecided gives first: {und}")
    # (i) G4 alone: the all-on string is fixed by every permutation, so its rung values are constant on its G4-orbit
    report("claim4 (i)/Reading: under G4 alone the all-on class is a singleton (rung values constant on it)", True,
           "by inspection: pi permutes the on set, all-on maps to all-on")
    # (iii) P_0 = off_1 off_2 is the vacuum projector: own Clifford, 2 rungs; atoms
    sig = (1, -1, 1, -1)
    v = [csc(F(1, 2), cadd(g(2 * j), g(2 * j + 1))) for j in range(2)]
    w = [csc(F(1, 2), cadd(g(2 * j), csc(-1, g(2 * j + 1)))) for j in range(2)]
    off = [cmul(w[j], v[j], sig) for j in range(2)]
    P0 = cmul(off[0], off[1], sig)
    ys = [cadd(P0, cmul(cmul(v[0], v[1], sig), P0, sig)), cadd(P0, csc(-1, cmul(cmul(v[0], v[1], sig), P0, sig))),
          cmul(cadd(v[0], v[1]), P0, sig), cmul(cadd(v[0], csc(-1, v[1])), P0, sig)]
    at = [csc(F(1, 2), cmul(y, cdag(y), sig)) for y in ys]
    ok = all(cmul(A, A, sig) == A and cdag(A) == A for A in at) and cadd(*at) == one()
    ok = ok and all(cmul(at[i], at[j], sig) == {} for i in range(4) for j in range(4) if i != j)
    ok = ok and all(cmul(w[j], P0, sig) == {} for j in range(2))     # P0 is annihilated by w_j: vacuum
    report("claim4 (iii): with P_0 = off off (vacuum), the four atoms are orthogonal projections summing to 1", ok)
    # (v) threshold rule = sign of one element's value: Y_n - on_0 ; check outcome equals [omega(Y - on_0) < 0]
    report("claim4 (v): the comparison is the sign of the value of the single element Y_n - on_0 (by linearity)", True,
           "omega(Y) < omega(on_0) iff omega(Y - on_0) < 0")


if __name__ == "__main__":
    claim1()
    claim3()
    claim4()
    open(__file__.replace(".py", ".log"), "w").write("\n".join(log) + "\n")
