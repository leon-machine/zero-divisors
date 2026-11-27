import sys, time, os, cProfile, pstats
LAB='/home/claude/zero-divisors'
sys.path.insert(0, LAB+'/lib')
import tp_premise, GA, gtg
tp_premise.configure(LAB+'/store')
import importlib.util
path=LAB+'/store/claims/synthesis.null-surface-data-at-any-field-strength-the-focusing-equation-integrated/check.py'
spec = importlib.util.spec_from_file_location("chk", path)
c = importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
F = c.F
# check 1 pieces
tot = 0
for w in c.PROFILES:
    wave = c.Wave(c.profile(w), c.S_ZERO, c.X0, c.LOW, solved=True)
    fld = wave.fld
    Rop = wave.curvature()
    planes = 0; okc = True
    for a in range(4):
        for b in range(a + 1, 4):
            Bab = gtg.wedge(c.E[a], c.E[b], c.S13)
            v = gtg.bdot(Bab, c.LV, c.S13)
            hv = {}
            for i, ei in enumerate(c.TR):
                for j, ej in enumerate(c.TR):
                    hv = gtg.m_add(hv, gtg.m_scal(-2 * c.w_at(wave.w, i, j) * gtg.vdot(v, c.E[ej], c.S13), c.E[ei]))
            want = gtg.m_scal(F(-1, 2), gtg.wedge(c.LV, hv, c.S13))
            okc = okc and GA.eq(Rop(Bab), want)
            planes += 0 if GA.is_zero(want) else 1
    print("curv ok", okc, "planes", planes, "torsion", fld.torsion_free(), "det", c.det(fld.hb_matrix()),
          "om eq", all(c.mzero(gtg.m_sub(fld.om[k], wave.om_closed[k])) for k in range(4)),
          "hbinv l", GA.eq(fld.hb_inv(c.LV), c.LV), "H", wave.H.v)
    tot += planes
print("total planes", tot)
# matter orders
n = c.HIGH - 1
t0 = time.time()
pr = cProfile.Profile(); pr.enable()
mat = c.plane_data_series(c.W_MATTER, n)
pr.disable()
print("time", time.time() - t0)
pstats.Stats(pr).sort_stats('cumulative').print_stats(14)
for j in range(0, 9):
    print("rho d^%d" % j, [str(x) for x in c.orders(mat, lambda d: d[3], j)])
for j in range(0, 8):
    print("theta d^%d" % j, [str(x) for x in c.orders(mat, lambda d: d[0], j)])
