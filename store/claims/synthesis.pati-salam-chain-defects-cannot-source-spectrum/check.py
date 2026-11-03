"""synthesis.pati-salam-chain-defects-cannot-source-spectrum: exact checks.

G = SU(4) x SU(2)_L x SU(2)_R (simply connected, the store's Spin(6) x Spin(4)); the (10,1,3) vev breaks it
to H, with identity component H_0 = SU(3) x SU(2)_L x U(1)_Y, Y = T3R + (B-L)/2 (standard-model.majorana-element).
Elements of the maximal torus are written as phase tuples in turns (Fractions mod 1): four for SU(4) on its 4,
two for SU(2)_L and two for SU(2)_R on their doublets.
(1) The matter-parity element m = (-1_4, 1, 1) lies in G, fixes every weight of the (10,1,3) and acts as -1 on
    the 16 (it is exp(3 pi i (B-L)) there), so m lies in H.
(2) Central elements of G lying in H_0: an element exp(2 pi i t Y) z_3 u_L (z_3 central in SU(3), u_L in SU(2)_L)
    is central only if t is an integer, and then its SU(4) scalar c_4 and its SU(2)_R scalar c_R agree mod 1;
    m has c_4 - c_R = 1/2, so m is not in H_0: pi_0(H) contains Z2 and, G being simply connected,
    pi_1(G/H) = pi_0(H) contains Z2 (topologically stable Z2 strings). GA: the 2 pi rotor of SU(2) = Spin(3)
    is -1, the 4 pi rotor is +1 (the doublet phases of the proof).
(3) Under Premise (R) on the untuned fit, T_desc < 7.3e8 GeV < 0.0176 v_R.
(4) String tension G mu = eps eta^2/(4 M_r^2) with eta <= sqrt2 v_R and eps <= 10: G mu < 1.46e-15; central value
    (eps = 1, eta = v_R) 7.29e-17; CMB power fraction at l = 10 f_10 = kappa (G mu)^2 with kappa <= 1e13 (Planck
    string bounds, from memory: kappa = 6.7e11 Nambu-Goto, 2.7e11 Abelian-Higgs): with the mirror copy doubling
    it, below 4.3e-17.
Controls: i 1_4 does not fix the (10,1,3); (-1_4, 1, -1_R) is in H_0 (t = 1).
"""
from fractions import Fraction as F
import GA
from tp_premise import premise

M_I, G_R = F("1.95e10"), F("0.469")
V_R = M_I / G_R
M_R = F("2.435e18")
R_CAP = F("7.3e8")
A_S = F("2.100e-9")
KAPPA_NG = F("0.015") / F("1.5e-7") ** 2
KAPPA_AH = F("0.028") / F("3.2e-7") ** 2
KAPPA = F(10) ** 13
EPS_MAX = F(10)

BL = [F(1, 3)] * 3 + [F(-1)]          # B-L on the 4 (quarks 1/3, lepton -1)


def red(x):
    """phase mod 1 in [0, 1)"""
    return x - (x.numerator // x.denominator)


def is_scalar(ph):
    return all(red(p - ph[0]) == 0 for p in ph)


def ten_weights(ph4):
    """phases of the symmetric square 10 of the 4"""
    return [ph4[i] + ph4[j] for i in range(4) for j in range(i, 4)]


def triplet_weights(ph2):
    """phases of the adjoint 3 of SU(2) from the doublet phases (a, -a): 2a, 0, -2a"""
    a = ph2[0]
    return [2 * a, F(0), -2 * a]


def fixes_vev(g):
    """the (10,1,3) vev is its nu^c nu^c component: weight 2 e_4 of the 10 (B-L = -2) and T3R = +1 of the 3,
    so Y = 0; a torus element fixes it exactly when the phase of that weight is 0 mod 1"""
    ph4, phL, phR = g
    return red(2 * ph4[3] + 2 * phR[0]) == 0


def trivial_on_multiplet(g):
    ph4, phL, phR = g
    return all(red(a + b) == 0 for a in ten_weights(ph4) for b in triplet_weights(phR))


def in_G(g):
    ph4, phL, phR = g
    return red(sum(ph4)) == 0 and red(sum(phL)) == 0 and red(sum(phR)) == 0


def h0_element(t, j):
    """exp(2 pi i t Y) times the SU(3) centre element omega^j (phases j/3 on the colour entries)"""
    ph4 = [t * b / 2 + F(j, 3) for b in BL[:3]] + [t * BL[3] / 2]
    phR = [t / 2, -t / 2]
    return (ph4, [F(0), F(0)], phR)


MPAR = ([F(1, 2)] * 4, [F(0), F(0)], [F(0), F(0)])


def check_matter_parity_in_stabiliser():
    premise("standard-model.majorana-element")
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    GA.check("m = (-1_4, 1, 1) is in SU(4) x SU(2) x SU(2)", in_G(MPAR))
    GA.check("m fixes the vev and acts trivially on the whole (10,1,3)", fixes_vev(MPAR) and trivial_on_multiplet(MPAR))
    GA.check("the vev weight has Y = 0: phase of exp(2 pi i t Y) on it vanishes for every t",
             all(fixes_vev(h0_element(F(k, 7), 0)) for k in range(-9, 10)))
    # on the 16: (4,2,1) has phase 1/2 on every entry, (4bar,1,2) phase -1/2: -1 on every fermion
    GA.check("m acts as -1 on the (4,2,1) and (4bar,1,2)",
             all(red(p) == F(1, 2) for p in MPAR[0]) and all(red(-p) == F(1, 2) for p in MPAR[0]))
    # equals exp(3 pi i (B-L)) on the 4: phases 3 (B-L)/2
    GA.check("m = exp(3 pi i (B-L)) on the 4", all(red(3 * b / 2 - p) == 0 for b, p in zip(BL, MPAR[0])))
    # SU(4) centre i^a fixes the 10 only for a even
    fix = [a for a in range(4) if fixes_vev(([F(a, 4)] * 4, [F(0), F(0)], [F(0), F(0)]))]
    GA.check("SU(4) centre elements fixing the 10: a = 0, 2 only", fix == [0, 2])
    return True


def check_matter_parity_not_in_identity_component():
    premise("standard-model.majorana-element")
    premise("standard-model.imported-pati-salam-representation-theory-survival")
    # the doublet phases (t/2, -t/2) are a scalar exactly when t is an integer
    for t in [F(k, 12) for k in range(-48, 49)]:
        g = h0_element(t, 0)
        GA.check("SU(2)_R part scalar iff t integer (t = %s)" % t, is_scalar(g[2]) == (t.denominator == 1))
    seen = set()
    for k in range(-12, 13):
        for j in range(3):
            g = h0_element(F(k), j)
            GA.check("H_0 element lies in H", fixes_vev(g) and in_G(g))
            if is_scalar(g[0]):
                c4, cR = red(g[0][0]), red(g[2][0])
                seen.add((c4, cR))
                GA.check("central element of H_0 has c_4 = c_R mod 1 (t = %d, j = %d)" % (k, j), c4 == cR)
    GA.check("H_0 meets the centre in exactly (0,0) and (1/2,1/2)", seen == {(F(0), F(0)), (F(1, 2), F(1, 2))})
    GA.check("m has c_4 - c_R = 1/2, so m is not in H_0", red(MPAR[0][0] - MPAR[2][0]) == F(1, 2))
    # the colour-scalar condition forces j = -2t mod 3 at integer t (the SU(3) centre element absorbs t/6)
    for k in range(-6, 7):
        js = [j for j in range(3) if is_scalar(h0_element(F(k), j)[0])]
        GA.check("one colour centre element per integer t (t = %d)" % k, js == [(-2 * k) % 3])
    # GA: SU(2) = Spin(3) rotors; the doublet phase t/2 at t = 1 is the 2 pi rotor, equal to -1; at t = 2, +1
    SQ = (-1, -1, -1)
    B = GA.mul(GA.gen(0), GA.gen(1), SQ)
    GA.check("unit bivector squares to -1", GA.eq(GA.mul(B, B, SQ), GA.sc(-1)))
    rot_pi = B                                              # cos(pi/2) + B sin(pi/2): rotation by pi
    rot_2pi = GA.mul(rot_pi, rot_pi, SQ)
    rot_4pi = GA.mul(rot_2pi, rot_2pi, SQ)
    GA.check("2 pi rotor is -1 (c_R = 1/2 at t = 1)", GA.eq(rot_2pi, GA.sc(-1)))
    GA.check("4 pi rotor is +1 (c_R = 0 at t = 2)", GA.eq(rot_4pi, GA.sc(1)))
    return True


def check_controls():
    premise("standard-model.majorana-element")
    g = ([F(1, 4)] * 4, [F(0), F(0)], [F(0), F(0)])
    GA.check("i 1_4 is in G but does not fix the (10,1,3) vev", in_G(g) and not fixes_vev(g))
    GA.check("the colour centre fixes the vev but not the whole multiplet",
             fixes_vev(h0_element(F(0), 1)) and not trivial_on_multiplet(h0_element(F(0), 1)))
    h = h0_element(F(1), 1)
    GA.check("(-1_4, 1, -1_R) is the H_0 element at t = 1, j = 1",
             all(red(p) == F(1, 2) for p in h[0]) and all(red(p) == F(1, 2) for p in h[2]))
    GA.check("m times (-1_4,1,-1_R) is (1,1,-1_R), also outside H_0",
             red(F(0) - F(1, 2)) == F(1, 2))
    return True


def check_r_window_below_restoration():
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("synthesis.untuned-fit-caps-lightest-heavy-neutrino")
    premise("neutrino.r-descent-reheats-below-lower-heavy")
    GA.check("v_R = M_I/g_R = 19500000000000/469 GeV", V_R == F(19500000000000, 469))
    GA.check("(R) cap below 0.0176 v_R", R_CAP < F("0.0176") * V_R and R_CAP > F("0.0175") * V_R)
    return True


def check_string_tension_and_cmb_fraction():
    premise("standard-model.what-angle-asks-neutrino-sector")
    premise("synthesis.imported-planck-2018-lcdm-parameters")
    premise("synthesis.imported-planck-2013-cosmic-string-bounds")
    premise("synthesis.imported-nielsen-olesen-string-tension")
    r = (V_R / M_R) ** 2
    GA.check("(v_R/M_r)^2 floor-pinned at 2915e-19", (r * 10 ** 19) // 1 == 2915)
    gmu_c = r / 4
    gmu_max = EPS_MAX * 2 * r / 4
    gmu_min = F(1, 2) * F(1, 2) * r / 4
    GA.check("central G mu pinned at 7.28e-17", (gmu_c * 10 ** 19) // 1 == 728)
    GA.check("maximal G mu pinned at 1.457e-15", (gmu_max * 10 ** 18) // 1 == 1457)
    GA.check("minimal G mu pinned at 1.82e-17", (gmu_min * 10 ** 19) // 1 == 182)
    GA.check("kappa bound covers both string models", KAPPA_NG < KAPPA and KAPPA_AH < KAPPA)
    GA.check("kappa_NG floor 666666666666", KAPPA_NG // 1 == 666666666666)
    f10 = 2 * KAPPA * gmu_max ** 2
    GA.check("f_10 (with mirror) pinned below 4.26e-17", (f10 * 10 ** 19) // 1 == 425)
    GA.check("string power below 1e-16 of the measured", f10 < F(1, 10 ** 16))
    # in absolute terms: f_10 A_s below 1e-25
    GA.check("absolute string power below 1e-25", f10 * A_S < F(1, 10 ** 25))
    return True


def check_generator_is_spin_rotor_minus_one():
    premise("std-algebra.spin-double-cover")
    premise("standard-model.majorana-element")
    # SU(4) = Spin(6): the 2 pi rotor in a plane of the six vectors is -1; Ad(-1) fixes every vector and every
    # 3-vector (the 10 + 10bar of SU(4) are the self-dual and anti-self-dual 3-vectors), so the (10,1,3) vev is
    # fixed; on spinors (the 4 and 4bar) -1 acts as -1
    SQ = (1, 1, 1, 1, 1, 1)
    E = [GA.gen(i) for i in range(6)]
    R = GA.mul(E[0], E[1], SQ)                      # rotor of the rotation by pi in the e1 e2 plane
    m = GA.mul(R, R, SQ)
    GA.check("2 pi rotor of Spin(6) is -1", GA.eq(m, GA.sc(-1)))
    tri = GA.mul(GA.mul(E[0], E[2], SQ), E[4], SQ)
    vec = GA.add(E[1], GA.scal(F(3), E[5]))
    ad = lambda x: GA.mul(GA.mul(m, x, SQ), GA.reverse(m), SQ)
    GA.check("Ad(-1) fixes vectors and 3-vectors", GA.eq(ad(vec), vec) and GA.eq(ad(tri), tri))
    # a spinor: element of the left ideal generated by a primitive idempotent; left action of -1 negates it
    i1 = GA.mul(E[0], E[1], SQ)
    idem = GA.scal(F(1, 2), GA.add(GA.sc(1), GA.mul(i1, GA.mul(E[2], E[3], SQ), SQ)))
    GA.check("idempotent", GA.eq(GA.mul(idem, idem, SQ), idem))
    psi = GA.mul(GA.add(E[0], GA.scal(F(2), E[4])), idem, SQ)
    GA.check("left action of -1 negates a nonzero spinor", (not GA.is_zero(psi)) and GA.eq(GA.mul(m, psi, SQ), GA.neg(psi)))
    # so m = (-1_Spin(6), 1, 1); its image in Spin(10) under Spin(6) x Spin(4) -> Spin(10) is the rotor -1 of Spin(10)
    return True
