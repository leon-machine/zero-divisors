"""synthesis.cold-mirror-needs-non-equilibrium-descent: exact checks on a window.

Window: two boundary modes per tower (this tower: modes 0, 1; the mirror: modes 2, 3), frequencies
w and 2w in both towers (the reversal intertwines the two one-particle Hamiltonians), realised as
a_j = (e_j + f_j)/2 in Cl(4,4) with e_j^2 = +1, f_j^2 = -1, so that the CAR relations hold
exactly over the rationals. The normalised trace of the simple algebra Cl(4,4) = Mat(16, R) is
the scalar part. A Gibbs factor exp(-beta w N) = 1 + (x - 1) N for the projector N, with
x = exp(-beta w) kept as an exact rational; the shared clock means the mirror's modes carry the
same x, x^2 as ours. tau_{i beta} multiplies a_j by 1/x_j and a_j^* by x_j.
"""
from fractions import Fraction as F
import GA
from GA import mul, add, sub, scal, sc, gen
from tp_premise import premise

NM = 4                                   # modes 0..3
SQ = tuple([1] * NM + [-1] * NM)         # e_j at index j, f_j at index NM + j


def a(j):
    return scal(F(1, 2), add(gen(j), gen(NM + j)))


def ad(j):
    return scal(F(1, 2), sub(gen(j), gen(NM + j)))


def m(*xs):
    out = sc(1)
    for x in xs:
        out = mul(out, x, SQ)
    return out


def num(j):
    return m(ad(j), a(j))


def tr(x):
    return x.get((), F(0))


def gibbs_factor(xs):
    """prod_j (1 + (x_j - 1) N_j): the unnormalised density with occupation parameters xs."""
    rho = sc(1)
    for j, xj in enumerate(xs):
        rho = mul(rho, add(sc(1), scal(xj - 1, num(j))), SQ)
    return rho


def state(rho):
    z = tr(rho)
    return lambda X: tr(mul(rho, X, SQ)) / z


def kms_holds(rho, xs):
    """KMS at the clock with occupation parameters xs, for the state tr(rho .)/tr(rho).

    The trace form is nondegenerate, so omega(A B) = omega(B tau_{i beta}(A)) for every B is
    equivalent to rho A = tau_{i beta}(A) rho; it suffices to test the generators A = a_j, a_j^*.
    """
    for j, xj in enumerate(xs):
        for A, tA in ((a(j), scal(1 / xj, a(j))), (ad(j), scal(xj, ad(j)))):
            if mul(rho, A, SQ) != mul(tA, rho, SQ):
                return False
    return True


def swap(x):
    """The reversal on the window: modes 0 <-> 2, 1 <-> 3 (an automorphism; it intertwines H)."""
    perm = {0: 2, 1: 3, 2: 0, 3: 1}
    perm.update({NM + k: NM + v for k, v in list(perm.items())})
    out = {}
    for b, c in x.items():
        img = [perm[i] for i in b]
        # reorder the permuted blade with signs
        y = sc(c)
        for i in img:
            y = mul(y, gen(i), SQ)
        out = add(out, y)
    return out


def H(ws):
    return add(*[scal(w, num(j)) for j, w in enumerate(ws)])


def check_car_window():
    premise("obj.hawking.boundary-mode-algebra-windows-boost-dynamics")
    for j in range(NM):
        for k in range(NM):
            acomm = add(m(a(j), ad(k)), m(ad(k), a(j)))
            assert acomm == (sc(1) if j == k else {})
            assert add(m(a(j), a(k)), m(a(k), a(j))) == {}
    # the reversal is an automorphism carrying the tower's modes to the mirror's
    for j in range(NM):
        assert swap(a(j)) == a({0: 2, 1: 3, 2: 0, 3: 1}[j])
    return True


WINDOW_PREMISES = (
    "hawking.gibbs-states-are-kms-conversely-finite",
    "hawking.i-state",
    "hawking.imported-quasi-free-states-car-algebra",
    "hawking.imported-kms-passes-inductive-limits",
)


def fd(x):
    """Fermi-Dirac occupation for the Gibbs parameter x = exp(-beta w)."""
    return x / (1 + x)


def check_shared_clock_forces_xi_one():
    for p in WINDOW_PREMISES:
        premise(p)
    # explicit occupations: x = 1/3, 2/5, 1/7 give n = 1/4, 2/7, 1/8 on the w modes
    # and x^2 = 1/9, 4/25, 1/49 give n = 1/10, 4/29, 1/50 on the 2w modes
    expected = {F(1, 3): (F(1, 4), F(1, 10)), F(2, 5): (F(2, 7), F(4, 29)),
                F(1, 7): (F(1, 8), F(1, 50))}
    for x, (nw, n2w) in expected.items():
        clock = [x, x * x, x, x * x]                     # one beta, w and 2w in each tower
        rho = gibbs_factor(clock)
        om = state(rho)
        assert kms_holds(rho, clock)
        # occupations forced by KMS on (a_j^*, a_j): n_j = x_j (1 - n_j), equal across the orbit
        assert [om(num(j)) for j in range(NM)] == [nw, n2w, nw, n2w]
        assert om(m(num(0), num(2))) == nw * nw           # product across the towers
        # any product state with the mirror at another parameter fails KMS for the shared clock
        for y in (x * x, F(1, 2) * x, F(1, 3) * x):
            other = [x, x * x, y, y * y]
            assert not kms_holds(gibbs_factor(other), clock)
    return True


def check_two_clocks_persist():
    premise("dark-matter.superselected-hence-dark-exactly-stable")
    for p in WINDOW_PREMISES:
        premise(p)
    Hj = H([F(1), F(2), F(1), F(2)])                     # decoupled: no cross term
    # (x, y) and the explicit occupations of modes 0 and 2: fd(1/3) = 1/4, fd(1/9) = 1/10,
    # fd(2/5) = 2/7, fd(1/11) = 1/12
    cases = (((F(1, 3), F(1, 9)), (F(1, 4), F(1, 10))),
             ((F(2, 5), F(1, 11)), (F(2, 7), F(1, 12))))
    for (x, y), (n0, n2) in cases:
        rho = gibbs_factor([x, x * x, y, y * y])
        om = state(rho)
        assert (om(num(0)), om(num(2))) == (n0, n2)
        # stationary under the decoupled dynamics: [rho, H] = 0
        assert sub(mul(rho, Hj, SQ), mul(Hj, rho, SQ)) == {}
        # KMS for the shared clock at no parameter z (KMS on mode 0 forces z = x, on mode 2 z = y)
        assert not kms_holds(rho, [x, x * x, x, x * x])
        assert not kms_holds(rho, [y, y * y, y, y * y])
        # KMS for the two-clock flow: the mirror's modes run at another rate
        assert kms_holds(rho, [x, x * x, y, y * y])
        # the decoupling is what keeps it stationary: a hopping between partner modes 0 and 2
        # (the cross term superselection forbids) does not commute with the two-temperature state
        hop = add(m(ad(0), a(2)), m(ad(2), a(0)))
        Hx = add(Hj, hop)
        comm = sub(mul(rho, Hx, SQ), mul(Hx, rho, SQ))
        # exactly: tr(A [rho, hop]) / tr(rho) = -omega([A, hop]) with A = a2^* a0, and
        # [a2^* a0, a0^* a2] = N2 - N0, so the obstruction to stationarity is the occupation gap
        lhs = tr(mul(m(ad(2), a(0)), comm, SQ)) / tr(rho)
        assert lhs == n0 - n2 and lhs != 0
        # while at equal temperatures the same hopping commutes with the product state
        rho_eq = gibbs_factor([x, x * x, x, x * x])
        assert sub(mul(rho_eq, hop, SQ), mul(hop, rho_eq, SQ)) == {}
    return True


def check_law_symmetric_realisation_asymmetric():
    for p in WINDOW_PREMISES:
        premise(p)
    premise("dark-matter.superselected-hence-dark-exactly-stable")
    x, y = F(1, 3), F(1, 9)                              # fd(x) = 1/4, fd(y) = 1/10
    r1 = gibbs_factor([x, x * x, y, y * y])
    r2 = gibbs_factor([y, y * y, x, x * x])
    assert tr(r1) == tr(r2)
    assert swap(r1) == r2 and swap(r2) == r1
    mix = scal(F(1, 2), add(r1, r2))
    assert swap(mix) == mix                              # invariant under the reversal
    Hj = H([F(1), F(2), F(1), F(2)])
    assert sub(mul(mix, Hj, SQ), mul(Hj, mix, SQ)) == {}  # stationary
    om = state(mix)
    # explicit marginals and correlation: <N0> = <N2> = (1/4 + 1/10)/2 = 7/40,
    # <N0 N2> = (1/4)(1/10) = 1/40, against the product 49/1600: not quasi-free
    assert om(num(0)) == F(7, 40) and om(num(2)) == F(7, 40)
    assert om(m(num(0), num(2))) == F(1, 40)
    assert om(num(0)) * om(num(2)) == F(49, 1600)
    # no cross two-point function, normal or anomalous
    assert om(m(ad(0), a(2))) == 0 and om(m(a(0), a(2))) == 0
    # not KMS for the shared clock at any parameter: KMS on mode 0 forces z = n0/(1 - n0) = 7/33
    z = F(7, 40) / (1 - F(7, 40))
    assert z == F(7, 33)
    assert not kms_holds(mix, [z, z * z, z, z * z])
    # each component has unequal temperatures in the two towers: 1/4 against 1/10
    o1 = state(r1)
    assert (o1(num(0)), o1(num(2))) == (F(1, 4), F(1, 10))
    return True


def check_reading_under_m():
    """The cosmological reading under (M): exact content of the numbers it quotes."""
    premise("dark-matter.open-channels-their-costs")
    premise("dark-tower-matter.mirrors-temperature-p2")
    coeff = F(7447, 1000)                  # Delta N_eff = 7.447 xi^4 (open-channels-their-costs)
    cap = F(3, 10)                         # the Planck cap on Delta N_eff used there
    # xi = 1, the value (i) gives for a descent in equilibrium: 7.447, quoted as 7.45
    assert abs(coeff - F(745, 100)) <= F(1, 200)
    assert coeff > 24 * cap                # excluded by a factor of about 25
    # the threshold 0.448: below it the cap holds, at 0.449 it fails
    assert coeff * F(448, 1000) ** 4 <= cap
    assert coeff * F(449, 1000) ** 4 > cap
    return True
