import sys
LAB='/home/claude/zero-divisors'
sys.path.insert(0, LAB+'/lib')
import tp_premise, GA, gtg
tp_premise.configure(LAB+'/store')
import importlib.util
path=LAB+'/store/claims/synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated/check.py'
spec = importlib.util.spec_from_file_location("chk", path)
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
F=c.F; HIGH=c.HIGH; LOW=c.LOW
b = [F(1), F(0), F(-3, 2), F(1, 2)]
q = [F(2), F(2), F(-1)]
for lam1 in c.DUST_POINTS:
    bl = c.shifted(b, lam1)
    w22 = c.s_scal(-6, c.rational_series([1], c.shifted(q, lam1), HIGH))
    wave = c.Wave([[[], []], [[], w22]], ((0, 0), (0, bl[1] / bl[0])), c.point(lam1), LOW)
    print(lam1, c.padded(c.s_mul(w22, bl, HIGH), HIGH) == c.padded(c.s_der(c.s_der(bl)), HIGH),
          c.padded(wave.Ec[1][1], LOW) == c.padded(c.s_scal(1 / bl[0], bl), LOW), len(wave.Ec[1][1]),
          "reach", lam1 + 2 / -wave.theta().v, c.sign(wave.shear2().v - wave.k_ric_k(wave.curvature())))
for cc in c.SMOOTH_WAVES:
    bt = [F(0), F(-1), F(0), -cc]
    for lam1 in c.SMOOTH_POINTS:
        t1 = 1 - lam1
        bl = c.shifted(bt, -t1)
        g = c.s_scal(6 * cc, c.rational_series([1], [1 + cc * t1 * t1, -2 * cc * t1, cc], HIGH))
        print(cc, lam1, "bl", bl, c.padded(c.s_mul(g, bl, HIGH), HIGH) == c.padded(c.s_der(c.s_der(bl)), HIGH))
        if t1:
            wave = c.Wave([[c.s_scal(-1, g), []], [[], g]], ((c.S11_SAMPLE, 0), (0, bl[1] / bl[0])), c.point(lam1), LOW)
            print("  ", c.jzero(c.vdot(wave.K, wave.K)), c.sign(wave.theta().v - c.S11_SAMPLE), c.padded(wave.Ec[1][1], LOW) == c.padded(c.s_scal(1 / bl[0], bl), LOW))
        else:
            wave = c.Wave([[c.s_scal(-1, g), []], [[], g]], c.S_ZERO, c.point(lam1), LOW)
            print("  ", bl[0], bl[1], gtg.bb_dot(gtg.wedge(c.NV, c.E[2], c.S13), wave.curvature()(gtg.wedge(c.NV, c.E[2], c.S13)), c.S13), 6*cc)
        print("  ", wave.fld.torsion_free(), gtg.ricci_flat(wave.curvature(), c.S13))
