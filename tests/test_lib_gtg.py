"""Tests for lib/gtg.py: the store's GTG conventions (DICTIONARY.md C1-C11, sections 11, 12, 16) pinned
with exact values, and cross-validation against the engines the check writers pasted into checks
(L12 engine, L09 engine and tractor block, L10 gtgcore and twcore, the T13 engine). Engine files are
exec'd in a namespace with GA and Fraction only when present (they define functions only); the
expected values that matter are also pinned as constants. Run:
python3 -m unittest discover -s tests -t .
"""
import ast
import inspect
import os
import sys
import unittest
from fractions import Fraction as F

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIB = os.path.join(ROOT, "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

import GA  # noqa: E402
import gtg  # noqa: E402

FIX = os.path.join(ROOT, "tests", "fixtures", "gtg")   # engines the check writers pasted into checks
L12_ENGINE = os.path.join(FIX, "L12_engine.py")
L09_ENGINE = os.path.join(FIX, "L09_engine.py")
L09_TRACTOR = os.path.join(FIX, "L09_tractor.py")
L10_GTG = os.path.join(FIX, "L10_gtgcore.py")
L10_TW = os.path.join(FIX, "L10_twcore.py")
T13_CHECK = os.path.join(ROOT, "store", "claims", "interior.interior-connection-exactly", "check.py")

e = GA.gen
S = gtg.S13


def _load(path):
    """Exec a pasted engine file in a namespace with GA and F (the engines define functions only)."""
    ns = {"GA": GA, "F": F, "__name__": "engine_under_test"}
    with open(path) as fh:
        exec(compile(fh.read(), path, "exec"), ns)
    return ns


def _t13_available():
    if not os.path.exists(T13_CHECK):
        return False
    with open(T13_CHECK) as fh:
        return "class J(object)" in fh.read()


def sig_r():
    """sigma_r = e_r e_t = gamma_1 gamma_0 (C6)."""
    return GA.mul(e(1), e(0), S)


class TestConventions(unittest.TestCase):
    def test_signature_and_sign_constants(self):
        self.assertEqual(S, (1, -1, -1, -1))
        self.assertEqual(gtg.lorentz_sig(5), (1, -1, -1, -1, -1))
        self.assertEqual(gtg.STORE_SIGN, -1)
        self.assertEqual(gtg.RIC_O_SIGN, -1)
        self.assertEqual(gtg.S24, (1, -1, -1, -1, 1, -1))

    def test_commutator_product_is_halved(self):
        self.assertEqual(gtg.comm(e(0), e(1)), {(0, 1): F(1)})
        B = gtg.biv(0, 1)
        self.assertEqual(gtg.comm(B, e(0)), {(1,): F(-1)})     # (e0 ^ e1) . e0 = -e1
        self.assertEqual(gtg.bdot(B, e(1)), {(0,): F(-1)})
        self.assertEqual(gtg.inner_vb(e(1), B), {(0,): F(1)})

    def test_null_pair_and_conformal_point(self):
        n0, ni = gtg.N0, gtg.NINF
        self.assertEqual(gtg.vdot(n0, ni, gtg.S24), 1)
        self.assertEqual(gtg.vdot(n0, n0, gtg.S24), 0)
        self.assertEqual(gtg.vdot(ni, ni, gtg.S24), 0)
        x = gtg.vec([F(2), F(1), F(-3), F(1, 2)])
        X = gtg.conformal_point(x)
        self.assertEqual(gtg.vdot(X, X, gtg.S24), 0)
        self.assertEqual(gtg.slots(X), (-gtg.vdot(x, x) / 2, x, F(1)))       # (sigma, mu, rho)
        I = gtg.scale_tractor(F(3, 4))
        self.assertEqual(gtg.vdot(I, I, gtg.S24), F(3, 4) / 3)
        self.assertEqual(gtg.slots(I), (F(1), {}, F(1, 8)))

    def test_jets(self):
        self.assertEqual(gtg.Jet(), 0)
        self.assertFalse(gtg.Jet())
        r = gtg.Jet.var(1, F(2), order=3)
        y = r * r * r
        self.assertEqual(y.v, 8)
        self.assertEqual(y.g, (0, 12, 0, 0))
        self.assertEqual(y.d(1).d(1).v, 12)
        self.assertEqual(y.d(1).d(1).d(1).v, 6)
        s = (2 / r).pw(F(1, 2))                                    # sqrt(2/r) at r = 2: 1
        self.assertEqual(s.v, 1)
        self.assertEqual(s.g[1], F(-1, 4))                          # -sqrt(2) r^{-3/2}/2
        self.assertEqual(s.d(1).d(1).v, F(3, 16))
        self.assertEqual((1 / r).d(1).v, F(-1, 4))
        sn, cs = gtg.sincos(2, F(3, 5), F(4, 5), order=2)
        self.assertEqual((sn * sn + cs * cs), gtg.Jet.const(1))
        self.assertEqual(sn.d(2).d(2).v, F(-3, 5))
        ex = gtg.jexp(gtg.Jet.var(0, F(0), order=3), F(1))
        self.assertEqual([ex.coeff((k, 0, 0, 0)) for k in range(4)], [1, 1, F(1, 2), F(1, 6)])
        with self.assertRaises(ValueError):
            gtg.Jet.var(0, F(1), order=1).d(0).d(0)


class TestSchwarzschild(unittest.TestCase):
    M = F(1)

    def test_pg_values_store_sign(self):
        M, r = self.M, F(8)                                         # beta = 1/2
        fld = gtg.schwarzschild_pg(M, r, F(3, 5), F(4, 5))
        self.assertTrue(fld.torsion_free())
        self.assertEqual(fld.torsion_rank(), 24)
        self.assertEqual(fld.Omega(0), GA.scal(M / r ** 2, sig_r()))       # stored connection, C10
        Rc = fld.curvature()
        k = M / r ** 3
        self.assertEqual(gtg.apply_op(Rc, sig_r()), GA.scal(2 * k, sig_r()))  # +2M/r^3 (C6)
        for p in [(0, 2), (0, 3), (1, 2), (1, 3)]:
            self.assertEqual(Rc[p], {p: -k})                         # mixed planes -M/r^3
        self.assertEqual(Rc[(2, 3)], {(2, 3): 2 * k})
        self.assertTrue(gtg.ricci_flat(Rc))
        self.assertEqual(gtg.ricci_scalar(Rc), 0)
        self.assertEqual(gtg.kretschmann(Rc), 48 * M ** 2 / r ** 6)
        self.assertEqual(gtg.op_planes(gtg.op_type_d(M / (2 * r ** 3), sig_r())), Rc)
        W = gtg.weyl_op(Rc)
        self.assertEqual(W, Rc)
        self.assertEqual(gtg.euler_density(Rc), 48 * M ** 2 / r ** 6)

    def test_pg_metric_and_hb(self):
        beta = F(1, 2)
        fld = gtg.schwarzschild_pg(self.M, F(8), F(3, 5), F(4, 5))
        g = fld.metric()
        self.assertEqual([g[0][0], g[0][1], g[1][1]], [1 - beta ** 2, -beta, -1])
        self.assertEqual(fld.hb_inv(e(0)), gtg.vec([1, beta]))     # K = hb^{-1}(e_t) = e_t + beta e_r
        self.assertEqual(fld.hb(fld.hb_inv(e(0))), e(0))

    def test_surface_gravity_at_horizon(self):
        M = F(1, 2)                                                  # r = 2M = 1, beta = 1
        fld = gtg.schwarzschild_pg(M, F(1), F(3, 5), F(4, 5))
        K = fld.hb_inv(e(0))
        self.assertEqual(GA.dot(K, K, S), 0)
        DK = gtg.comm(fld.Omega(0), K)
        self.assertEqual(DK, GA.scal(1 / (4 * M), K))                # kappa = 1/4M (C10, section 8)

    def test_inside_horizon_and_solved_connection(self):
        fld = gtg.schwarzschild_pg(self.M, F(1, 2), F(3, 5), F(4, 5))    # beta = 2
        self.assertTrue(fld.torsion_free())
        self.assertEqual(gtg.kretschmann(fld.curvature()), 48 * self.M ** 2 / F(1, 2) ** 6)
        solved = gtg.Field(fld.TH)
        for c in range(4):
            self.assertEqual(solved.omega(c), fld.omega(c))
        self.assertEqual(solved.curvature(), fld.curvature())

    def test_static_and_pg_agree(self):
        r0 = F(50, 9)                                                # beta = 3/5, sqrt(f) = 4/5
        st = gtg.schwarzschild_static(self.M, r0, F(3, 5), F(4, 5))
        pg = gtg.schwarzschild_pg(self.M, r0, F(3, 5), F(4, 5))
        self.assertTrue(st.torsion_free())
        self.assertEqual(st.curvature(), pg.curvature())

    def test_kerr_schild_form(self):
        x0 = [F(0), F(1), F(2), F(2)]                                # r = 3
        fld = gtg.schwarzschild_ks(self.M, x0)
        self.assertTrue(fld.torsion_free())
        Rc = fld.curvature()
        self.assertTrue(gtg.ricci_flat(Rc))
        self.assertEqual(gtg.kretschmann(Rc), 48 * self.M ** 2 / F(3) ** 6)
        self.assertEqual(fld.metric()[0][0], 1 - 2 * self.M / 3)

    def test_c11_sign_identifications(self):
        M, r = F(1), F(1)
        c3 = M / r ** 3
        R = gtg.op_type_d(c3 / 2, sig_r())
        want = {(0, 1): 2 * c3, (0, 2): -c3, (0, 3): -c3, (2, 3): -2 * c3, (1, 2): c3, (1, 3): c3}
        for (a, b), v in want.items():                              # MTW 31.4 components in (+,-,-,-)
            self.assertEqual(gtg.riem_o(R, e(a), e(b), e(a), e(b)), v)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        lhs = GA.dot(gtg.riemann_endo_apply(R, e(a), e(b), e(c)), e(d), S)
                        self.assertEqual(lhs, gtg.riem_o(R, e(d), e(c), e(a), e(b)))
        k = GA.add(e(0), e(1))
        for a in range(4):
            for b in range(4):                                      # vacuum: W = calR
                self.assertEqual(gtg.weyl_null(R, k, e(a), e(b)), gtg.riem_o(R, k, e(a), k, e(b)))
        self.assertEqual(gtg.weyl_null(R, k, e(2), e(2)), 0)                  # radial k is principal
        self.assertEqual(gtg.weyl_null(R, GA.add(e(0), e(2)), e(1), e(1)), 3 * c3)
        lam = F(3, 5)
        Rd = gtg.op_const(lam / 3)
        for a in range(4):
            for b in range(4):
                if a != b:
                    self.assertEqual(gtg.riem_o(Rd, e(a), e(b), e(a), e(b)), -(lam / 3) * S[a] * S[b])

    def test_store_from_ldg(self):
        R_ldg = gtg.op_type_d(F(-1, 2), sig_r())                     # L19 Sec. 5, M = r = 1
        R = gtg.store_from_ldg(R_ldg)
        self.assertEqual(R(sig_r()), GA.scal(2, sig_r()))


class TestOtherFields(unittest.TestCase):
    def test_de_sitter_flat_and_pg(self):
        H = F(1, 2)
        lam = 3 * H * H
        fld = gtg.de_sitter_flat(H, F(3))
        self.assertTrue(fld.torsion_free())
        self.assertEqual(fld.omega(1), {(0, 1): -H})                   # C10
        Rc = fld.curvature()
        self.assertEqual(Rc, gtg.op_planes(gtg.op_const(lam / 3)))     # calR(B) = (Lambda/3) B
        for m in range(4):
            self.assertEqual(gtg.ricci(Rc, e(m)), GA.scal(lam, e(m)))
            self.assertEqual(gtg.einstein_residual(Rc, e(m), lam), {})
        self.assertEqual(gtg.ricci_scalar(Rc), 4 * lam)
        self.assertTrue(all(not w for w in gtg.weyl_op(Rc).values()))
        pg = gtg.de_sitter_pg(H, F(1), F(3, 5), F(4, 5))
        self.assertTrue(pg.torsion_free())
        self.assertEqual(pg.curvature(), Rc)
        self.assertEqual(pg.hb_inv(e(0)), gtg.vec([1, -H]))            # beta = -rH at r = 1

    def test_sds_pg_and_defaults(self):
        lam = F(9, 32)
        self.assertEqual(gtg.f_static(lam=lam)(F(2)), 1 - lam * 4 / 3)       # M, Q default to 0
        r0 = F(2)
        M = (F(9, 16) - lam * r0 * r0 / 3) * r0 / 2                 # beta^2 = 2M/r + Lambda r^2/3 = (3/4)^2
        pg = gtg.pg_field(r0, F(3, 5), F(4, 5), gtg.beta_kottler(M, lam))
        self.assertEqual(pg.hb_inv(e(0)), gtg.vec([1, F(3, 4)]))
        self.assertTrue(pg.torsion_free())
        Rc = pg.curvature()
        for m in range(4):
            self.assertEqual(gtg.einstein_residual(Rc, e(m), lam), {})
        self.assertEqual(gtg.apply_op(gtg.weyl_op(Rc), sig_r()), GA.scal(2 * M / 8, sig_r()))
        self.assertEqual(gtg.m_rev(GA.mul(gtg.biv(0, 1), e(2), S)), GA.neg(GA.mul(gtg.biv(0, 1), e(2), S)))
        self.assertEqual(gtg.m_rev(gtg.biv(0, 1)), gtg.biv(1, 0))
        x = GA.add(GA.sc(2), e(1), gtg.biv(0, 3), gtg.pseudoscalar())
        self.assertEqual(gtg.m_rev(x), GA.reverse(x))

    def test_sds_and_rn(self):
        lam = F(3, 16)
        M = gtg.mass_for_root(2, F(1, 2), lam=lam)
        self.assertEqual(M, F(1, 2))
        fld = gtg.static_field(F(2), F(3, 5), F(4, 5), gtg.f_static(M, lam=lam))
        Rc = fld.curvature()
        W = gtg.weyl_op(Rc)
        self.assertEqual(gtg.apply_op(W, sig_r()), GA.scal(2 * M / 8, sig_r()))   # w_h = 2M/r^3 (C11)
        P = gtg.schouten(Rc)
        for m in range(4):
            self.assertEqual(gtg.einstein_residual(Rc, e(m), lam), {})
            self.assertEqual(P(e(m)), GA.scal(lam / 6, e(m)))
        Mrn = gtg.mass_for_root(2, F(1, 2), Q=1)
        rn = gtg.static_field(F(2), F(3, 5), F(4, 5), gtg.f_static(Mrn, Q=1))
        Rr, r = rn.curvature(), F(2)
        self.assertEqual(gtg.ricci_scalar(Rr), 0)
        self.assertEqual(gtg.kretschmann(Rr), (48 * Mrn ** 2 * r ** 2 - 96 * Mrn * r + 56) / r ** 8)
        ks = gtg.rn_ks(Mrn, 1, [F(0), F(0), F(0), F(2)])
        self.assertEqual(gtg.kretschmann(ks.curvature()), gtg.kretschmann(Rr))

    def test_kasner_hubble_normalised(self):
        p = [F(2, 3), F(2, 3), F(-1, 3)]
        tau, fld = gtg.kasner_field(p, 2)
        self.assertEqual(tau, 8)
        for i in (1, 2, 3):
            self.assertEqual(GA.scal(tau, fld.omega(i)), {(0, i): -p[i - 1]})   # -p_i B_i
        Rc = fld.curvature()
        self.assertTrue(gtg.ricci_flat(Rc))
        self.assertEqual(gtg.kretschmann(Rc), F(64, 27) / tau ** 4)            # -16 p1 p2 p3 / t^4
        tau2, data = gtg.kasner_data(p, 2)
        self.assertEqual(gtg.synchronous_from_data(data).curvature(), Rc)

    def test_flrw_against_coordinate_ricci(self):
        a, ad, add = F(3, 2), F(5, 7), F(2, 3)
        Rc = gtg.flrw_flat(a, ad, add).curvature()
        self.assertEqual(gtg.ric_o(Rc, e(0), e(0)), -3 * add / a)              # R_00 = -3 a''/a
        self.assertEqual(gtg.ric_o(Rc, e(1), e(1)), add / a + 2 * ad ** 2 / a ** 2)

    def test_d_dimensions(self):
        for d in (3, 5, 6):
            H = F(1, 3)
            fld = gtg.de_sitter_flat(H, F(2), d=d)
            sq = fld.sq
            lam = H * H * (d - 1) * (d - 2) / 2
            Rc = fld.curvature()
            self.assertEqual(Rc, gtg.op_planes(gtg.op_const(2 * lam / ((d - 1) * (d - 2))), sq))
            P = gtg.schouten(Rc, sq)
            for m in range(d):
                self.assertEqual(gtg.einstein_residual(Rc, e(m), lam, sq), {})
                self.assertEqual(P(e(m)), GA.scal(lam / ((d - 1) * (d - 2)), e(m)))
            self.assertTrue(all(not w for w in gtg.weyl_op(Rc, sq).values()))
            self.assertEqual(gtg.kretschmann(Rc, sq), 8 * d * lam ** 2 / ((d - 1) * (d - 2) ** 2))
        for sq in [(1, -1, -1), (1, -1, -1, -1, -1), (1, 1, -1, -1, -1)]:
            d = len(sq)
            T = lambda a, d=d, sq=sq: gtg.m_add(*[GA.scal(F((m + 1) * (n + 1) + m + n, 3) * GA.dot(a, gtg.er(m, sq), sq),
                                                          gtg.er(n, sq)) for m in range(d) for n in range(d)])
            R = gtg.op_kn(T, sq)
            P = gtg.schouten(R, sq)
            for m in range(d):
                self.assertEqual(P(e(m)), T(e(m)))
            self.assertTrue(all(not w for w in gtg.weyl_op(R, sq).values()))


class TestTractor(unittest.TestCase):
    def test_de_sitter_tractor_flat_and_scale_tractor_parallel(self):
        H = F(1, 2)
        lam = 3 * H * H
        fld = gtg.de_sitter_flat(H, F(3), order=2)
        self.assertTrue(all(not v for v in gtg.tractor_curvature(fld).values()))
        P = gtg.schouten(fld.curvature())
        I = gtg.scale_tractor(lam)
        for c in range(4):
            self.assertEqual(gtg.dT_const(fld, c, P, I), {})
            self.assertEqual(gtg.dT_const(fld, c, P, gtg.NINF), GA.scal(-lam / 6, e(c)))
        self.assertNotEqual(gtg.dT_const(fld, 0, P, gtg.scale_tractor(lam + 1)), {})

    def test_schwarzschild_tractor_strength_is_minus_weyl(self):
        fld = gtg.schwarzschild_pg(F(1), F(8), F(3, 5), F(4, 5), order=2)
        Rc = fld.curvature()
        TC = gtg.tractor_curvature(fld)
        for k in Rc:
            self.assertEqual(TC[k], GA.neg(gtg.weyl_op(Rc)[k]))

    def test_sds_tractor_strength_and_curvature_jets(self):
        lam = F(3, 16)
        M = gtg.mass_for_root(2, F(1, 2), lam=lam)
        fld = gtg.static_field(F(2), F(3, 5), F(4, 5), gtg.f_static(M, lam=lam), order=2)
        Rc = fld.curvature()
        self.assertEqual({k: gtg.m_val(v) for k, v in fld.curvature_jet().items()}, Rc)
        TC = gtg.tractor_curvature(fld)
        W = gtg.weyl_op(Rc)
        for k in Rc:
            self.assertEqual(TC[k], GA.neg(W[k]))

    def test_lie_tools_stabiliser(self):
        sq = GA.sig(2, 4)
        n0, ni = gtg.null_pair(sq, 1, 5)                          # L09's layout
        I = GA.add(n0, GA.scal(F(1, 8), ni))
        stab = gtg.stabiliser(I, sq)
        self.assertEqual(len(stab), 10)
        self.assertEqual(len(gtg.lie_closure(stab, sq)), 10)
        self.assertEqual(gtg.killing_rank(gtg.lie_closure(stab, sq), sq), 10)
        self.assertTrue(all(gtg.annihilates(B, I, sq) for B in stab))
        self.assertEqual(len(gtg.stabiliser(n0, sq)), 10)          # the vector n0; its line adds the dilation
        D = gtg.wedge(n0, ni, sq)
        self.assertEqual(gtg.comm(D, n0, sq), n0)                  # (n0 ^ ninf) . n0 = n0


class TestEngineCrossValidation(unittest.TestCase):
    @unittest.skipUnless(os.path.exists(L12_ENGINE), "L12 engine not present")
    def test_l12_engine(self):
        E = _load(L12_ENGINE)
        M = F(1)
        r0 = 2 * M / (1 - F(9, 25))
        old = E["static_field"](r0, F(3, 5), F(4, 5), lambda r: (1 - 2 * M / r, 2 * M / (r * r)))
        new = gtg.schwarzschild_static(M, r0, F(3, 5), F(4, 5))
        self.assertEqual(old.curvature(), new.curvature())
        for c in range(4):
            self.assertEqual(E["m_val"](old.om[c]), new.omega(c))
        old = E["pg_field"](F(1, 2), F(3, 5), F(4, 5), F(1))
        new = gtg.schwarzschild_pg(F(1), F(1, 2), F(3, 5), F(4, 5))
        self.assertEqual(old.curvature(), new.curvature())
        self.assertEqual(E["m_val"](old.Om[0]), new.Omega(0))
        lam, Fw = F(3, 4), F(1, 2)
        Ms = F(2) * (1 - Fw ** 2 - lam * 4 / 3) / 2
        self.assertEqual(Ms, gtg.mass_for_root(2, Fw, lam=lam))
        old = E["static_field"](F(2), F(3, 5), F(4, 5), lambda r: (1 - 2 * Ms / r - lam * r * r / 3, 2 * Ms / (r * r) - 2 * lam * r / 3))
        new = gtg.static_field(F(2), F(3, 5), F(4, 5), gtg.f_static(Ms, lam=lam))
        Ro, Rn = old.curvature(), new.curvature()
        self.assertEqual(Ro, Rn)
        Po, Pn = E["schouten"](Ro), gtg.schouten(Rn)
        self.assertEqual(E["ricci_scalar"](Ro), gtg.ricci_scalar(Rn))
        V = E["tractor"](F(2), GA.add(GA.gen(0), GA.scal(3, GA.gen(2))), F(-1, 3))
        self.assertEqual(V, gtg.tractor(F(2), GA.add(GA.gen(0), GA.scal(3, GA.gen(2))), F(-1, 3)))
        for c in range(4):
            self.assertEqual(Po(E["fv"](c)), Pn(e(c)))
            self.assertEqual(E["omega_T"](old, c, Po), gtg.omega_T(new, c, Pn))
            dV = E["dT_const"](old, c, Po, V)
            self.assertEqual(dV, gtg.dT_const(new, c, Pn, V))
            self.assertEqual(E["slots"](dV), gtg.slots(dV))
        old, new = E["ds_flat_field"](F(1, 2), F(3)), gtg.de_sitter_flat(F(1, 2), F(3))
        self.assertEqual(old.curvature(), new.curvature())

    @unittest.skipUnless(os.path.exists(L09_ENGINE), "L09 engine not present")
    def test_l09_engine(self):
        E = _load(L09_ENGINE)
        for r0, w in [(F(1, 2), F(1)), (F(1, 2), F(3, 2))]:
            old, lam_o, _ = E["interior_field"](r0, w, F(3, 5), F(4, 5))
            new, lam_n, _ = gtg.sync_interior_field(r0, w, F(3, 5), F(4, 5))
            self.assertEqual(lam_o, lam_n)
            self.assertEqual(old.curvature(), new.curvature())
            self.assertEqual(E["torsion_rank"](old), new.torsion_rank())
            Rc = new.curvature()
            for b in range(4):
                self.assertEqual(E["ricci"](Rc, b), gtg.ricci(Rc, e(b)))
            for c in range(4):
                A = [F(1) if i == c else F(0) for i in range(4)]
                for b in range(4):
                    Vo = E["vec"]([E["J"](1 if i == b else 0) for i in range(4)])
                    Vn = gtg.vec([gtg.Jet.const(1 if i == b else 0) for i in range(4)])
                    self.assertEqual(E["field_cov"](old, A, Vo), new.cov_phys(A, Vn))
            gens = [new.omega(c) for c in range(4)]
            self.assertEqual(E["lie_dim"](gens, S), gtg.lie_dim(gens, S))

    @unittest.skipUnless(os.path.exists(L09_TRACTOR), "L09 tractor block not present")
    def test_l09_tractor_block(self):
        T = _load(L09_TRACTOR)
        sq = GA.sig(2, 4)
        n0, ni = gtg.null_pair(sq, 1, 5)
        self.assertEqual((T["N0"], T["NINF"]), (n0, ni))
        for lam in (F(3, 4), F(-3, 2), F(0)):
            I = T["scale_tractor"](lam)
            self.assertEqual(I, GA.add(n0, GA.scal(lam / 6, ni)))
            so, sn = T["stabiliser"](I), gtg.stabiliser(I, sq)
            self.assertEqual(len(so), len(sn))
            self.assertEqual(T["t_rank"](so + sn), len(sn))
            Lo, Ln = T["lie_closure"](so), gtg.lie_closure(sn, sq)
            self.assertEqual(len(Lo), len(Ln))
            self.assertEqual(T["killing_rank"](Lo), gtg.killing_rank(Ln, sq))

    @unittest.skipUnless(os.path.exists(L10_GTG), "L10 gtgcore not present")
    def test_l10_gtgcore(self):
        E = _load(L10_GTG)
        for p, base in [([F(2, 3), F(2, 3), F(-1, 3)], 2), ([F(1, 2), F(1, 3), F(1, 5)], 2)]:
            tau, data = E["kasner"](p, base)
            self.assertEqual((tau, data), gtg.kasner_data(p, base))
            old, new = E["Synchronous"](data), gtg.synchronous_from_data(data)
            self.assertEqual(old.torsion_free(), new.torsion_free())
            Rc = new.curvature()
            for m, n in E["PLANES"]:
                self.assertEqual(old.calR(gtg.biv(m, n)), gtg.apply_op(Rc, gtg.biv(m, n)))
                self.assertEqual(old.R_bg(m, n), new.strength(m, n))
            self.assertEqual(old.scalar(), gtg.ricci_scalar(Rc))
            self.assertEqual(old.kretschmann(), gtg.kretschmann(Rc))
            self.assertEqual(old.ricci_sq(), gtg.ricci_sq(Rc))
            P = gtg.schouten(Rc)
            for m in range(4):
                self.assertEqual(old.ricci(e(m)), gtg.ricci(Rc, e(m)))
                self.assertEqual(old.schouten(e(m)), P(e(m)))
                self.assertEqual(old.Omega(m), new.Omega(m))
                self.assertEqual(old.omega_T(m, old.schouten), gtg.omega_T_bg(new, m, P))

    @unittest.skipUnless(os.path.exists(L10_TW), "L10 twcore not present")
    def test_l10_twcore(self):
        E = _load(L10_TW)
        q = GA.qi
        I = gtg.tw_i_lam(F(1, 6))
        self.assertEqual(I, E["i_lam"](F(1, 6)))
        for a in (0, 2, 5):
            self.assertEqual(gtg.tw_spin_preimage(gtg.TW_EAMB[a], I), E["spin_preimage"](E["EAMB"][a], I))
        Zs = [[q(1), q(0, 1), q(2), q(-1, 1)], [q(0), q(1), q(1, -1), q(3)]]
        self.assertEqual(gtg.tw_grip(Zs, I), E["grip"](Zs, I))
        self.assertEqual(gtg.tw_casimir(Zs, gtg.TW_EAMB), E["casimir"](Zs, E["EAMB"]))
        self.assertEqual(gtg.tw_internal_casimir(*Zs), E["internal_casimir"](*Zs))
        self.assertEqual(gtg.tw_xreal(1, 2, 3, 4), E["xreal"](1, 2, 3, 4))
        x = gtg.tw_xslot([1, 2, 3, 4])
        self.assertEqual(gtg.tw_xpoint(x), E["xpoint"](E["xslot"]([1, 2, 3, 4])))
        self.assertEqual(gtg.tw_amb_pair(gtg.tw_xpoint(x), gtg.tw_xpoint(x)), q(0))
        A = gtg.tw_spin_preimage(gtg.TW_EAMB[1], gtg.TW_EAMB[4])
        self.assertEqual(gtg.tw_in_su22(A), E["in_su22"](A))
        xp = gtg.tw_xpoint(gtg.tw_xslot([1, 2, 3, 4]))
        self.assertEqual(gtg.tw_spin_preimage(xp, I), E["spin_preimage"](E["xpoint"](E["xslot"]([1, 2, 3, 4])), I))
        pairs = [(gtg.TW_EAMB[a], gtg.TW_EAMB[b]) for a in range(6) for b in range(a + 1, 6)] + [(xp, I)]
        for U, V in pairs:
            A = gtg.tw_spin_preimage(U, V)
            self.assertEqual(sum((A[i][i] for i in range(4)), q(0)), q(0))
            self.assertEqual([gtg.tw_act(A, gtg.TW_EAMB[c]) for c in range(6)],
                             [gtg.tw_rot(U, V, gtg.TW_EAMB[c]) for c in range(6)])
        pi = [q(2), q(1, -1)]
        self.assertEqual(gtg.tw_on_line([1, 2, 3, 4], pi), E["on_line"]([1, 2, 3, 4], pi))
        Z = gtg.tw_on_line([1, 2, 3, 4], pi)
        self.assertEqual(Z[:2], [-q(1) * pi[1] + q(2) * pi[0], -q(3) * pi[1] + q(4) * pi[0]])

    @unittest.skipUnless(_t13_available(), "T13 engine already migrated")
    def test_t13_engine(self):
        E = _load(T13_CHECK)
        for k, s0, c0 in [(F(1, 2), F(3, 5), F(4, 5)), (F(2), F(4, 5), F(3, 5))]:
            old, r0, _ = E["interior_field"](k, s0, c0)
            new, lam, _ = gtg.sync_interior_field(k * k / (1 + k * k), 1 / k, s0, c0)
            self.assertEqual(lam, 0)
            for c in range(4):
                self.assertEqual(E["m_val"](old.om[c]), new.omega(c))
            self.assertEqual(E["torsion_rank"](old), new.torsion_rank())
            bad, _, _ = gtg.sync_interior_field(k * k / (1 + k * k), 1 / k, s0, c0, boost_sign=1)
            self.assertFalse(bad.torsion_free())
            self.assertTrue(new.torsion_free())
            z = (GA.add(GA.gen(0), GA.gen(1)), {})
            m = (GA.gen(2), GA.gen(3))
            B = GA.mul(GA.gen(0), GA.gen(2), S)
            self.assertEqual(gtg.cdot(gtg.cbdot((B, {}), z), m), E["pv"](B))


class TestLibraryRules(unittest.TestCase):
    def test_static_rules_and_docstrings(self):
        from tp import evidence
        path = os.path.join(LIB, "gtg.py")
        src = open(path).read()
        self.assertEqual([p for p in evidence.static_problems(src) if p[0] != "E403"], [])
        tree = ast.parse(src)
        self.assertFalse([n.lineno for n in ast.walk(tree) if isinstance(n, ast.Attribute) and n.attr == "setdefault"])
        names = {n.name for n in tree.body if isinstance(n, (ast.FunctionDef, ast.ClassDef))}
        for name in names:
            if name.startswith("_"):
                continue
            doc = inspect.getdoc(getattr(gtg, name))
            self.assertTrue(doc and doc.splitlines()[0].strip(), name)


if __name__ == "__main__":
    unittest.main()


class StaticFieldExplicitDerivative(unittest.TestCase):
    """static_field(fprime=...) lets a check state f' as data; foreign jets read through m_val."""

    def test_fprime_matches_differentiation_and_detects_a_wrong_one(self):
        import gtg
        from fractions import Fraction as Fr
        M = Fr(7, 8)
        a = gtg.static_field(Fr(4), Fr(3, 5), Fr(4, 5), gtg.f_static(M))
        b = gtg.static_field(Fr(4), Fr(3, 5), Fr(4, 5), gtg.f_static(M), fprime=lambda r: 2 * M / (r * r))
        c = gtg.static_field(Fr(4), Fr(3, 5), Fr(4, 5), gtg.f_static(M), fprime=lambda r: 3 * M / (r * r))
        self.assertEqual(a.curvature(), b.curvature())
        self.assertNotEqual(a.curvature(), c.curvature())

    def test_m_val_reads_foreign_jets(self):
        import gtg
        from fractions import Fraction as Fr

        class K:
            v = Fr(2)
            g = None
        self.assertEqual(gtg.m_val({(0,): K()}), {(0,): Fr(2)})
