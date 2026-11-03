"""singularity.computed: exact checks in Gauge Theory Gravity.

Flat background Cl(1,3) (GA.py, (+,-,-,-)) with labels (t, r, theta, phi); the stored Schwarzschild field
hb = 1 - beta P, P(a) = (a . e_t) e_r, beta = sqrt(2M/r): hb^{-1}(e_t) = gamma0 + beta gamma1,
hb^{-1}(e_r) = gamma1, angular r gamma2, r sin(theta) gamma3, with its torsion-free rotation-gauge field
(checked by the torsion equation; exact first-order jets at rational points with beta, sqrt(1 - beta^2),
sin, cos rational). (v . D) is computed as D_{hb(v)} = hb(v) . nabla + Omega(hb(v)) x. Computed:
(1) K = hb^{-1}(e_t) has Q(K) = 1 - beta^2 = f = 1 - 2M/r, and K is a Killing field: the map
    A -> (A . D) K is antisymmetric in the flat product on the physical frame;
(2) static observers v = K/sqrt f: their acceleration a = (v . D) v is spacelike and the redshifted
    acceleration satisfies sqrt f sqrt(-Q(a)) = f'(r)/2 = M/r^2 at every sampled r > 2M;
(3) on the horizon locus (beta = 1, r = 2M): (K . D) K = kappa K with kappa = 1/(4M), equal to f'(2M)/2,
    for several masses.
"""
from fractions import Fraction as F

import GA
import gtg
from tp_premise import premise


# ---- GTG engine: lib/gtg.py (jets, fields, multivector helpers; DICTIONARY conventions) ----
S13 = gtg.S13
m_val = gtg.m_val
vec = gtg.vec


def field_cov(fld, A, V):
    """(A . D) V = D_{hb(A)} V for constant physical components A and a jet vector field V (value)."""
    return fld.cov_phys(A, V)
# ---- end of engine ----


OUT = [(F(4, 5), F(3, 5), F(1, 2)), (F(3, 5), F(4, 5), F(1, 2)), (F(5, 13), F(12, 13), F(3, 2)),
       (F(8, 17), F(15, 17), F(2))]                                    # (beta, sqrt f, M), r > 2M
MASSES = [F(1, 2), F(3, 2), F(5)]


def pg_field(b0, M, s0=F(3, 5), c0=F(4, 5)):
    """Schwarzschild in the PG gauge with beta = b0 at the point; returns (field, r0, beta jet)."""
    r0 = 2 * M / (b0 * b0)
    fld = gtg.schwarzschild_pg(M, r0, s0, c0)
    return fld, r0, fld.TH[1][0]


def killing_field(fld):
    """K = hb^{-1}(e_t) as a physical vector field with jet components."""
    return vec([fld.TH[a][0] for a in range(4)])


def check_killing_field_and_its_norm():
    premise("singularity.imported-surface-gravity-redshifted-acceleration")
    ok = True
    for b0, F0, M in OUT:
        fld, r0, be = pg_field(b0, M)
        ok = ok and fld.torsion_free()
        K = killing_field(fld)
        ok = ok and GA.dot(m_val(K), m_val(K), S13) == 1 - b0 * b0 == 1 - 2 * M / r0 == F0 * F0
        DK = [field_cov(fld, [F(1) if i == c else F(0) for i in range(4)], K) for c in range(4)]
        ok = ok and all(GA.dot(GA.gen(b), DK[a], S13) + GA.dot(GA.gen(a), DK[b], S13) == 0
                        for a in range(4) for b in range(4))
        ok = ok and any(DK[a] != {} for a in range(4))
    _tp_rv = (ok); assert _tp_rv is not False, "check_killing_field_and_its_norm"; return _tp_rv


def check_redshifted_acceleration_of_static_observers():
    premise("singularity.imported-surface-gravity-redshifted-acceleration")
    ok = True
    for b0, F0, M in OUT:
        fld, r0, be = pg_field(b0, M)
        sf = (1 - be * be).pw(F(1, 2))
        v = vec([fld.TH[a][0] / sf for a in range(4)])
        acc = field_cov(fld, [x / F0 for x in (F(1), b0, F(0), F(0))], v)
        Qa = GA.dot(acc, acc, S13)
        fprime = 2 * M / r0 ** 2
        ok = ok and Qa < 0 and F0 * F0 * (-Qa) == (fprime / 2) ** 2 and fprime / 2 == M / r0 ** 2
    _tp_rv = (ok); assert _tp_rv is not False, "check_redshifted_acceleration_of_static_observers"; return _tp_rv


def check_surface_gravity_on_the_horizon_locus():
    premise("singularity.imported-surface-gravity-redshifted-acceleration")
    ok = True
    for M in MASSES:
        fld, r0, be = pg_field(F(1), M)
        K = killing_field(fld)
        ok = ok and r0 == 2 * M and GA.dot(m_val(K), m_val(K), S13) == 0
        DKK = field_cov(fld, [F(1), F(1), F(0), F(0)], K)
        ok = ok and GA.eq(DKK, GA.scal(1 / (4 * M), m_val(K)))
        ok = ok and (2 * M / r0 ** 2) / 2 == 1 / (4 * M)
    _tp_rv = (ok); assert _tp_rv is not False, "check_surface_gravity_on_the_horizon_locus"; return _tp_rv
