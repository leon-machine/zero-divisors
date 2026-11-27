import sys, os, importlib.util, time
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
src = open("check.py").read().replace("ELIMINATED_AREA2", "None").replace("ELIMINATED_AREA", "None").replace("CUT_AREA", "None")
ns = {"__name__": "ck"}
exec(compile(src, "check.py", "exec"), ns)
globals().update(ns)
from fractions import Fraction as F
t0 = time.time()
h = eliminated_vacuum_field(ELIMINATED_SEED)
print("elim", time.time() - t0, pzero(peinstein(h)), not vzero(papply(h, NU)), bool(curvature_component(h)), not bool(curvature_component(displacement(sample_vector(BRACKET_SEED)))))
xi, g = cutoff_boost(); Dxi = displacement(xi)
flux = window_total(vdot(NU, pomega(h, Dxi)))
area = corner_total(g * tr_perp(h) * F(1, 2))
print("flux", flux, "area", area, flux == -2 * area)
h2 = padd(h, sample_field(OFF_SHELL_SEED))
flux2 = window_total(vdot(NU, pomega(h2, Dxi)))
bulk = window_total(vdot(NU, papply(peinstein(h2), xi)) * 2)
area2 = corner_total(g * tr_perp(h2) * F(1, 2))
print("off", flux2 == bulk - 2 * area2, bulk, area2, time.time() - t0)
hg = gauge_sample(GAUGE_SEED); lam = X[0]; da = ptrace(hg) * F(1, 2); nEn = vdot(NU, papply(peinstein(hg), NU))
for u0 in CUTS:
    K = -F(1, 8) * window_from((lam - u0) * nEn, u0)
    area = cut_total(da - (lam - u0) * dn(da), FAR) - cut_total(da, u0)
    print(u0, 2 * K == F(1, 4) * area, area)
t0 = time.time(); print(check_pairing_with_a_displacement_is_the_field_equation_plus_a_divergence(), time.time() - t0)
t0 = time.time(); print(check_bivectors_bilinear_in_the_field_and_the_flow_with_one_derivative_are_six(), time.time() - t0)
t0 = time.time(); print(check_flux_of_the_boost_variation_is_the_quadratic_boost_generator(), time.time() - t0)
t0 = time.time(); print(check_dual_of_the_boost_plane_is_the_corner_plane_and_the_periods(), time.time() - t0)
t0 = time.time(); print(check_flux_of_a_vacuum_field_against_the_corner_boost_is_a_pure_corner_term(), time.time() - t0)
