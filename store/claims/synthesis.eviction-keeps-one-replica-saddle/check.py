"""synthesis.eviction-keeps-one-replica-saddle: exact checks (rational arithmetic only).

(i)   a window member's thermal marginal diag(c^2, s^2) is rho = (1 + r e3)/2 in the Pauli algebra
      Cl(3,0), r = c^2 - s^2, with purity Tr rho^2 = 2 <rho^2>_0 = (1 + r^2)/2 = c^4 + s^4; purities
      multiply over a product window (explicit Kronecker products); zero weight (r = 0) gives 1/2;
(ii)  at zero weight, the eviction configuration at stage j (j radiated qubits, window of w members
      each maximally entangled with a distinct radiated qubit, evicted pairs wholly in the
      radiation) has radiation purity exactly 2^{-w}; along a run with capacity n_cap(j) the window
      is w = min(j, n_cap) and the purity is max(2^{-j}, 2^{-n_cap}): one saddle;
(iii) the Haar average purity on C^m (x) C^n is (m + n)/(mn + 1), from the symmetric-subspace
      projector (I + F)/(D(D + 1)) and exact traces of the swap operators; it lies below the
      two-saddle planar value 1/m + 1/n by (m + n)/(mn(mn + 1));
(iv)  at the crossing (j = n_cap, m = n): eviction purity 1/m, two-saddle 2/m (ratio exactly 2,
      Renyi-2 deficit ln 2), Haar 2m/(m^2 + 1) (ratio 2m^2/(m^2 + 1) in (2 - 2/m^2, 2)); away from
      it the two-saddle ratio to eviction is 1 + 2^{-|j - n_cap|}.
"""
from fractions import Fraction as F
import GA
from tp_premise import premise


def kron(A, B):
    return [[a * b for a in ra for b in rb] for ra in A for rb in B]


def mat_trace_sq(R):
    n = len(R)
    return sum(R[i][k] * R[k][i] for i in range(n) for k in range(n))


def check_member_purity_in_pauli_algebra():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    sq = (1, 1, 1)
    e3 = GA.gen(2)
    ok = True
    mats = []
    for c2 in (F(1, 2), F(2, 3), F(5, 7)):
        s2 = 1 - c2
        r = c2 - s2
        rho = GA.add(GA.sc(F(1, 2)), GA.scal(r / 2, e3))
        rho2 = GA.mul(rho, rho, sq)
        pur = 2 * rho2.get((), F(0))                 # Tr = 2 <.>_0 on the Pauli algebra
        ok = ok and pur == (1 + r * r) / 2 and pur == c2 * c2 + s2 * s2
        mats.append([[c2, F(0)], [F(0), s2]])
    ok = ok and mats[0][0][0] ** 2 + mats[0][1][1] ** 2 == F(1, 2)   # zero weight: 1/2
    P = kron(kron(mats[0], mats[1]), mats[2])
    prod = 1
    for M in mats:
        prod *= mat_trace_sq(M)
    ok = ok and mat_trace_sq(P) == prod
    GA.check("(i) member purity c^4 + s^4 = 2<rho^2>_0 in Cl(3,0); purities multiply over a "
             "product window; 1/2 at zero weight", ok)
    return ok


def eviction_state(j, w):
    """Qubits: radiation r_0..r_{j-1}, window members m_0..m_{w-1}; member i is maximally entangled
    with r_i; for i >= w the radiated qubit r_i is paired with an evicted partner, which is itself
    radiation (r_i and its partner e_i together in |00> + |11>). Returns the amplitude dict over
    (radiation bits incl. evicted partners, window bits) and the radiation register size."""
    amps = {}
    for bits in range(2 ** j):
        b = [(bits >> i) & 1 for i in range(j)]
        rad = tuple(b) + tuple(b[w:])          # evicted partners copy their radiated qubit
        win = tuple(b[:w])
        amps[(rad, win)] = amps.get((rad, win), 0) + 1
    return amps


def radiation_purity(amps):
    norm = sum(a * a for a in amps.values())
    # rho_R[rad, rad'] = sum_win a(rad, win) a(rad', win) / norm
    by_win = {}
    for (rad, win), a in amps.items():
        by_win.setdefault(win, {})[rad] = a
    rho = {}
    for win, col in by_win.items():
        for r1, a1 in col.items():
            for r2, a2 in col.items():
                rho[(r1, r2)] = rho.get((r1, r2), 0) + a1 * a2
    tr2 = sum(v * rho.get((r2, r1), 0) for (r1, r2), v in rho.items())
    return F(tr2, norm * norm)


def check_eviction_purity_is_one_saddle():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("synthesis.eviction-deficit-against-page-deficit")
    ok = True
    for j in range(1, 7):
        for w in range(0, j + 1):
            ok = ok and radiation_purity(eviction_state(j, w)) == F(1, 2 ** w)
    # a run: capacity n_cap falls by one each stage from 6, radiated count j rises by one
    for j in range(0, 7):
        ncap = 6 - j
        w = min(j, ncap)
        pur = radiation_purity(eviction_state(j, w)) if j > 0 else F(1)
        ok = ok and pur == max(F(1, 2 ** j), F(1, 2 ** ncap))
    GA.check("(ii) zero weight: eviction radiation purity 2^{-w} exactly; along a run it is "
             "max(2^{-j}, 2^{-n_cap}), a single saddle", ok)
    return ok


def haar_purity(m, n):
    """<Tr rho_A^2> = (Tr[F_A] + Tr[F F_A]) / (D(D + 1)) on (C^m (x) C^n)^{(x) 2}."""
    D = m * n
    t1 = 0          # Tr F_A: |a1 b1 a2 b2> -> |a2 b1 a1 b2>, diagonal iff a1 = a2
    t2 = 0          # Tr F F_A: -> |a1 b2 a2 b1>, diagonal iff b1 = b2
    for a1 in range(m):
        for b1 in range(n):
            for a2 in range(m):
                for b2 in range(n):
                    t1 += 1 if a1 == a2 else 0
                    t2 += 1 if b1 == b2 else 0
    return F(t1 + t2, D * (D + 1))


def check_haar_purity_against_two_saddles():
    premise("singularity.imported-page-average-entropy-subsystem")
    premise("synthesis.eviction-deficit-against-page-deficit")
    ok = True
    table = {(2, 2): F(4, 5), (2, 3): F(5, 7), (3, 3): F(3, 5), (2, 4): F(2, 3),
             (3, 5): F(1, 2), (4, 4): F(8, 17)}
    for (m, n), want in table.items():
        h = haar_purity(m, n)
        ok = ok and h == want and h == F(m + n, m * n + 1)
        planar = F(1, m) + F(1, n)
        ok = ok and planar - h == F(m + n, m * n * (m * n + 1)) and planar > h
        ok = ok and h > max(F(1, m), F(1, n))          # strictly above the one-saddle value
    GA.check("(iii) Haar purity (m + n)/(mn + 1) exactly; below the two-saddle 1/m + 1/n by "
             "(m + n)/(mn(mn + 1)), above the single saddle", ok)
    return ok


def check_crossing_ratios():
    premise("singularity.eviction-window-thermal-product-radiation-entropy")
    premise("singularity.imported-page-average-entropy-subsystem")
    ok = True
    for m in (2, 4, 8, 16):
        ev = F(1, m)
        two = F(1, m) + F(1, m)
        hr = haar_purity(m, m) / ev if m <= 8 else F(2 * m * m, m * m + 1)
        ok = ok and two / ev == 2
        ok = ok and hr == F(2 * m * m, m * m + 1) and 2 - F(2, m * m) < hr < 2
    for j in range(0, 7):
        ncap = 6 - j
        ev = max(F(1, 2 ** j), F(1, 2 ** ncap))
        two = F(1, 2 ** j) + F(1, 2 ** ncap)
        ok = ok and two / ev == 1 + F(1, 2 ** abs(j - ncap))
    GA.check("(iv) at the crossing two-saddle/eviction purity = 2 (Renyi-2 deficit ln 2), "
             "Haar/eviction = 2m^2/(m^2 + 1); elsewhere 1 + 2^{-|j - n_cap|}", ok)
    return ok


def run():
    return all([check_member_purity_in_pauli_algebra(), check_eviction_purity_is_one_saddle(),
                check_haar_purity_against_two_saddles(), check_crossing_ratios()])


if __name__ == "__main__":
    import sys
    sys.exit(0 if run() else 1)
