"""The norm released locally on isotropic fields: exact checks.

Cl(1,3), generators e0 (+1), e1, e2, e3 (-1), the store's flat spacetime. A homogeneous, isotropic,
reflection-invariant gravitational field with flat slices is, on functions of t = e0 . x only,
  hb^{-1}(e0) = n e0,  hb^{-1}(e_i) = a e_i,  Omega(e0) = 0,  Omega(e_i) = y e_i e0,
with n, a > 0 and y free (torsion allowed), and the norm u = -Q(V) = 3/Lambda a field u(t).
Time derivatives enter as independent sample numbers (jets): ad, yd, ud for the first derivatives.
(1) Kinematics by the stored definitions: the field strength R(a ^ b), the torsion
    D_0 g_i - D_i g_0 = (ad - n y) e_i, the curvature operator with eigenvalues A = yd/(n a) on e0 e_i and
    B = y^2/a^2 on e_i e_j, the Einstein map G(e0) = -3B e0, G(e_i) = -(2A + B) e_i.
(2) The frozen-point MacDowell-Mansouri density u eps(F, F), F(a ^ b) = R(a ^ b) + g_a ^ g_b / u, summed
    over the 24 orderings against the pseudoscalar, equals 24 times
      Lred = u yd y^2 - a^2 yd - n a y^2 + n a^3/u.
(3) The Euler-Lagrange expressions of Lred, by exact differentiation with dual numbers:
      d/du: yd y^2 - n a^3/u^2;  d/dn: a^3 (1/u - B);  d/da: n a^2 (3/u - 2A - B);
      y: 2a(ad - n y) - ud y^2.
(4) Elimination: with the frame equations 3B = 3/u + rho, 2A + B = 3/u - p (rho, p in units of
    8 pi G), A B - u^{-2} = ((3/u)(rho - 3p) - rho(rho + 3p))/18, one twenty-fourth of the stored clock
    density (4/3)(Lambda(rho - 3p) - rho(rho + 3p)) at Lambda = 3/u.
(5) Dust: 3/u = rho, y = -2 ad/n, (ad/(n a))^2 = rho/6, deceleration parameter 1/2, all four equations
    solved along the whole curve (jets of the closed form); the Friedmann rate rho/3 and a constant
    norm do not solve them.
(6) Radiation has no solution; the general barotropic value 3/u = rho(1 + 3w)/(1 - 3w).
(7) Vacuum: A = B = 1/u, F = 0, and every positive u(t) solves all four equations with
    ad/(n a) = u^{-1/2} + ud/(2 n u).
Exact arithmetic only (Fractions); fixed sample tables.
"""
from fractions import Fraction as F
from itertools import permutations
import GA
from tp_premise import premise

SQ = (1, -1, -1, -1)
R4 = range(4)
SPACE = (1, 2, 3)
PS = (0, 1, 2, 3)
DENSITY_FACTOR = F(24)
ELIM_DEN = F(9)
CLOCK_RATIO = F(24)
CLOCK_COEFF = F(4, 3)
DUST_RATE_DEN = F(6)
FRIEDMANN_RATE_DEN = F(3)
DECEL = F(1, 2)
TORSION_RATIO = F(-2)
HALF = F(1, 2)
THREE = F(3)
TWO = F(2)
# samples (n, a, y, yd, u): general jets, not solutions
JETS = [(F(1), F(2), F(3), F(5), F(7)), (F(2, 3), F(5, 4), F(-7, 2), F(1, 3), F(3, 5)),
        (F(3), F(1, 2), F(2, 5), F(-4), F(9, 2)), (F(5, 7), F(3), F(-1), F(2, 9), F(1, 4))]
RATES = [(F(1), F(-2)), (F(-3, 4), F(5, 3)), (F(2, 7), F(1, 2))]   # (ad, ud)
FLUIDS = [(F(6), F(0)), (F(3, 2), F(1, 5)), (F(5), F(5, 3)), (F(2, 3), F(-1, 9))]   # (rho, p)
# dust curve samples (k, s, n): rho = 6 k^2 / a^3 at a = s^2
DUST = [(F(1), F(1), F(1)), (F(2, 3), F(3, 2), F(1)), (F(5), F(1, 2), F(7, 3))]
EOS = [F(0), F(1, 5), F(-1, 4), F(2, 7)]
RADIATION_W = F(1, 3)
# vacuum samples (q, a, n, ud): u = q^2
VAC = [(F(1), F(1), F(1), F(0)), (F(3, 2), F(2), F(1), F(5)), (F(2), F(1, 3), F(4, 5), F(-7, 2)),
       (F(1, 5), F(3), F(2), F(1, 9))]


def _m(*xs):
    out = xs[0]
    for z in xs[1:]:
        out = GA.mul(out, z, SQ)
    return out


def _comm(x, z):
    return GA.scal(HALF, GA.sub(_m(x, z), _m(z, x)))


def _e(i):
    return GA.gen(i)


def _frame(n, a):
    return [GA.scal(n, _e(0))] + [GA.scal(a, _e(i)) for i in SPACE]


def _omega(y):
    return [{}] + [GA.scal(y, _m(_e(i), _e(0))) for i in SPACE]


def _field_strength(y, yd):
    """R(e_mu ^ e_nu) = d_mu Omega(e_nu) - d_nu Omega(e_mu) + Omega(e_mu) x Omega(e_nu); fields depend on t only."""
    Om = _omega(y)
    dOm = _omega(yd)
    R = {}
    for mu in R4:
        for nu in R4:
            t1 = dOm[nu] if mu == 0 else {}
            t2 = dOm[mu] if nu == 0 else {}
            R[mu, nu] = GA.add(GA.sub(t1, t2), _comm(Om[mu], Om[nu]))
    return R


def _wedge2(x, z):
    return GA.scal(HALF, GA.sub(_m(x, z), _m(z, x)))


def _lorentz_block(n, a, y, yd, u):
    R = _field_strength(y, yd)
    g = _frame(n, a)
    return {k: GA.add(R[k], GA.scal(1 / u, _wedge2(g[k[0]], g[k[1]]))) for k in R}


def _sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def _density(n, a, y, yd, u):
    """u * sum over orderings of sign * coefficient of e0 e1 e2 e3 in F(mu nu) ^ F(rho sigma)."""
    Fb = _lorentz_block(n, a, y, yd, u)
    tot = F(0)
    for p in permutations(R4):
        prod = _m(Fb[p[0], p[1]], Fb[p[2], p[3]])
        tot += _sign(p) * prod.get(PS, F(0))
    return u * tot


class D:
    """Dual number over the rationals: exact first derivative."""

    def __init__(self, v, d=0):
        self.v = F(v)
        self.d = F(d)

    def __add__(self, o):
        o = o if isinstance(o, D) else D(o)
        return D(self.v + o.v, self.d + o.d)

    __radd__ = __add__

    def __neg__(self):
        return D(-self.v, -self.d)

    def __sub__(self, o):
        o = o if isinstance(o, D) else D(o)
        return D(self.v - o.v, self.d - o.d)

    def __rsub__(self, o):
        return D(o) - self

    def __mul__(self, o):
        o = o if isinstance(o, D) else D(o)
        return D(self.v * o.v, self.v * o.d + self.d * o.v)

    __rmul__ = __mul__

    def inv(self):
        return D(1 / self.v, -self.d / (self.v * self.v))


def _lred(n, a, y, yd, u):
    uinv = u.inv() if isinstance(u, D) else 1 / u
    return u * yd * y * y - a * a * yd - n * a * y * y + n * a * a * a * uinv


def _val(x):
    return x.v if isinstance(x, D) else F(x)


def _partial(args, k):
    dargs = [D(x, 1 if i == k else 0) for i, x in enumerate(args)]
    return _lred(*dargs).d


def _momentum(a, y, u):
    """dLred/d(yd) = u y^2 - a^2, as a function for dual differentiation."""
    return u * y * y - a * a


def _equations(n, a, ad, y, yd, u, ud, rho, p):
    """The four equations: frame (time), frame (space), norm, connection; each zero on a solution."""
    A = yd / (n * a)
    B = y * y / (a * a)
    return (THREE * B - THREE / u - rho,
            TWO * A + B - THREE / u + p,
            A * B - 1 / (u * u),
            TWO * a * (ad - n * y) - ud * y * y)


def check_field_strength_torsion_and_einstein_map_of_the_isotropic_field():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for (n, a, y, yd, u) in JETS:
        R = _field_strength(y, yd)
        g = _frame(n, a)
        A = yd / (n * a)
        B = y * y / (a * a)
        for i in SPACE:
            # curvature operator on physical bivectors: -R(hb(B)); hb(e0 e_i) = e0 ^ e_i / (n a)
            cop = GA.scal(-1 / (n * a), R[0, i])
            GA.check("curvature operator on e0 e_i is A e0 e_i", GA.eq(cop, GA.scal(A, _m(_e(0), _e(i)))))
            for j in SPACE:
                if i != j:
                    cop = GA.scal(-1 / (a * a), R[i, j])
                    GA.check("curvature operator on e_i e_j is B e_i e_j",
                             GA.eq(cop, GA.scal(B, _m(_e(i), _e(j)))))
        for (ad, ud) in RATES:
            Om = _omega(y)
            for i in SPACE:
                # torsion: D_0 g_i - D_i g_0 with D_a v = a . grad v + Omega(a) x v
                tor = GA.sub(GA.scal(ad, _e(i)), _comm(Om[i], g[0]))
                GA.check("torsion on e0 ^ e_i is (ad - n y) e_i", GA.eq(tor, GA.scal(ad - n * y, _e(i))))
                for j in SPACE:
                    if i != j:
                        tor = GA.sub(_comm(Om[i], g[j]), _comm(Om[j], g[i]))
                        GA.check("spatial torsion vanishes", GA.is_zero(tor))
        # Ricci and Einstein maps from the eigenvalues, contraction with the reciprocal frame
        ric0 = sum((A for _ in SPACE), F(0))
        ricj = A + (len(SPACE) - 1) * B
        scal = ric0 + len(SPACE) * ricj
        GA.check("Einstein map: G(e0) = -3B e0", ric0 - scal / 2 == -THREE * B)
        GA.check("Einstein map: G(e_i) = -(2A + B) e_i", ricj - scal / 2 == -(TWO * A + B))


def check_frozen_point_density_on_the_isotropic_field_is_the_reduced_lagrangian():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("dark-energy.frozen-point-makes-stelle-west-vector")
    for (n, a, y, yd, u) in JETS:
        dens = _density(n, a, y, yd, u)
        GA.check("density = 24 Lred", dens == DENSITY_FACTOR * _lred(n, a, y, yd, u))
        A = yd / (n * a)
        B = y * y / (a * a)
        GA.check("Lred = n a^3 u (A - 1/u)(B - 1/u)",
                 _lred(n, a, y, yd, u) == n * a ** 3 * u * (A - 1 / u) * (B - 1 / u))
        GA.check("density is not the Einstein-Cartan part alone",
                 dens != DENSITY_FACTOR * (-a * a * yd - n * a * y * y))
    # de Sitter: y = a/q, yd = n a/q^2, u = q^2 gives F = 0
    for (q, a, n, ud) in VAC:
        Fb = _lorentz_block(n, a, a / q, n * a / (q * q), q * q)
        GA.check("Lorentz block vanishes on the de Sitter values", all(GA.is_zero(x) for x in Fb.values()))


def check_euler_lagrange_expressions_of_the_reduced_lagrangian():
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    premise("synthesis.promoted-norm-weyl-clock-flat-weight")
    for (n, a, y, yd, u) in JETS:
        args = (n, a, y, yd, u)
        A = yd / (n * a)
        B = y * y / (a * a)
        GA.check("norm equation: dL/du = yd y^2 - n a^3/u^2 = n a^3 (A B - 1/u^2)",
                 _partial(args, 4) == yd * y * y - n * a ** 3 / (u * u) == n * a ** 3 * (A * B - 1 / (u * u)))
        GA.check("frame equation (time): dL/dn = a^3 (1/u - B)", _partial(args, 0) == a ** 3 * (1 / u - B))
        GA.check("frame equation (space): dL/da = n a^2 (3/u - 2A - B)",
                 _partial(args, 1) == n * a * a * (THREE / u - TWO * A - B))
        for (ad, ud) in RATES:
            # connection equation: dL/dy - d/dt dL/d(yd), the momentum differentiated along (ad, yd, ud)
            mom_dot = (_momentum(D(a, 1), y, u).d * ad + _momentum(a, D(y, 1), u).d * yd
                       + _momentum(a, y, D(u, 1)).d * ud)
            el_y = _partial(args, 2) - mom_dot
            GA.check("connection equation: 2a(ad - n y) - ud y^2", el_y == TWO * a * (ad - n * y) - ud * y * y)
            if ud != 0:
                GA.check("a varying norm sources torsion: the torsion-free value does not solve it",
                         TWO * a * (ad - n * (ad / n)) - ud * y * y != 0)


def check_elimination_gives_the_stored_clock_density():
    premise("synthesis.promoted-norm-weyl-clock-flat-weight")
    for (rho, p) in FLUIDS:
        for (n, a, y, yd, u) in JETS:
            B = 1 / u + rho / THREE
            A = (THREE / u - p - B) / TWO
            lhs = A * B - 1 / (u * u)
            elim = (THREE / u) * (rho - THREE * p) - rho * (rho + THREE * p)
            GA.check("A B - 1/u^2 = elimination/18", lhs == elim / ELIM_DEN)
            L = THREE / u
            clock = CLOCK_COEFF * (L * (rho - THREE * p) - rho * (rho + THREE * p))
            GA.check("the stored clock density E - (8/3) Lambda^2 is 24 (A B - 1/u^2)", clock == CLOCK_RATIO * lhs)


def check_dust_solution_tracks_the_density_and_decelerates():
    premise("synthesis.promoted-norm-weyl-clock-flat-weight")
    premise("synthesis.stelle-west-norm-is-no-local-output")
    for (k, s, n) in DUST:
        # closed form along the curve, parameter a: rho = 6k^2/a^3, u = 3/rho, y = -2k a^(-1/2),
        # ad = n k a^(-1/2); at a = s^2 all values are rational, and so are the derivatives
        a = s * s
        rho = 6 * k * k / a ** 3
        u = THREE / rho
        y = TORSION_RATIO * k / s
        ad = n * k / s
        dy_da = k / s ** 3
        du_da = THREE * a * a / (TWO * k * k)
        yd = dy_da * ad
        ud = du_da * ad
        eqs = _equations(n, a, ad, y, yd, u, ud, rho, F(0))
        GA.check("dust: all four equations hold on the tracking curve", all(x == 0 for x in eqs))
        H = ad / (n * a)
        GA.check("dust: Lambda = 3/u equals 8 pi G rho", THREE / u == rho)
        GA.check("dust: H^2 = rho/6, half the Friedmann value rho/3",
                 H * H == rho / DUST_RATE_DEN and H * H != rho / FRIEDMANN_RATE_DEN)
        GA.check("dust: y = -2 ad/n, twice the torsion-free value with opposite sign", y == TORSION_RATIO * ad / n)
        # second derivative of a in proper time: d/dtau (k a^(-1/2)) = -(k/2) a^(-3/2) (ad/n)
        add_ = -(k / TWO) / s ** 3 * (ad / n)
        GA.check("dust: deceleration parameter 1/2", -add_ * a / ((ad / n) ** 2) == DECEL)
        GA.check("dust: the tracking norm is not constant", ud != 0)
        # wrong candidates fail
        bad = _equations(n, a, ad, ad / n, yd, u, ud, rho, F(0))
        GA.check("dust: the torsion-free connection y = ad/n does not solve the equations", any(x != 0 for x in bad))
        bad = _equations(n, a, ad, y, yd, TWO * u, F(0), rho, F(0))
        GA.check("dust: a different norm does not solve the equations", any(x != 0 for x in bad))
        # the norm equation alone, with the two frame equations, forces 3/u = rho for dust
        for mult in (HALF, TWO, THREE):
            uu = mult * u
            B = 1 / uu + rho / THREE
            A = (THREE / uu - B) / TWO
            GA.check("dust: 3/u != rho violates the norm equation", A * B - 1 / (uu * uu) != 0)


def check_radiation_has_no_solution_and_barotropic_value():
    premise("synthesis.promoted-norm-weyl-clock-flat-weight")
    for (rho, _p) in FLUIDS:
        for (n, a, y, yd, u) in JETS:
            p = RADIATION_W * rho
            elim = (THREE / u) * (rho - THREE * p) - rho * (rho + THREE * p)
            GA.check("radiation: the elimination is -2 rho^2, nonzero for every norm", elim == -TWO * rho * rho != 0)
        for w in EOS:
            p = w * rho
            L = rho * (1 + THREE * w) / (1 - THREE * w)
            elim = L * (rho - THREE * p) - rho * (rho + THREE * p)
            GA.check("barotropic: Lambda = rho (1 + 3w)/(1 - 3w) solves the elimination", elim == 0)
            GA.check("barotropic: Lambda / rho is not 1 unless w = 0", (L == rho) == (w == 0))


def check_vacuum_leaves_the_norm_a_free_function():
    premise("synthesis.stelle-west-norm-is-no-local-output")
    premise("dark-energy.imported-macdowell-mansouri-theorem-stelle-west")
    for (q, a, n, ud) in VAC:
        u = q * q
        y = a / q
        # the rate fixed by the norm's own rate: ad/(n a) = 1/q + ud/(2 n u)
        ad = n * a * (1 / q + ud / (TWO * n * u))
        # yd from y = a u^(-1/2): yd = ad/q - a ud/(2 q^3)
        yd = ad / q - a * ud / (TWO * q ** 3)
        eqs = _equations(n, a, ad, y, yd, u, ud, F(0), F(0))
        GA.check("vacuum: all four equations hold for an arbitrary rate of the norm", all(x == 0 for x in eqs))
        GA.check("vacuum: the Lorentz block vanishes", all(GA.is_zero(x) for x in _lorentz_block(n, a, y, yd, u).values()))
        H = ad / (n * a)
        GA.check("vacuum: the expansion rate is 1/q + ud/(2 n u), not fixed by u alone",
                 H == 1 / q + ud / (TWO * n * u) and (H * H == 1 / u) == (ud == 0))
        if ud != 0:
            bad = _equations(n, a, n * a / q, y, yd, u, ud, F(0), F(0))
            GA.check("vacuum: with a varying norm the de Sitter rate does not solve the connection equation",
                     any(x != 0 for x in bad))
