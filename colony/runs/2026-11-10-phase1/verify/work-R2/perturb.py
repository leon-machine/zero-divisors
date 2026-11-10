"""Referee R2: targeted perturbations of the two checks. Writes perturbed copies beside itself and runs them."""
import os, subprocess, sys
LAB = "/home/claude/phys-graph"
W = os.path.dirname(os.path.abspath(__file__))
P1 = "synthesis.stretched-horizon-count-on-kerr-gives-the-area-law-at-every-spin"
P2 = "synthesis.no-spin-independent-curvature-level-set-carries-the-count-to-slow-kerr"
CASES = [
 (P1, "p1a_flip_rotation_sense", "k = [F(-1), -S / P, F(0), a * (1 - u * u)]", "k = [F(-1), -S / P, F(0), -a * (1 - u * u)]"),
 (P1, "p1b_double_H", "H = M * r / S", "H = 2 * M * r / S"),
 (P1, "p1c_kappa_minus_with_Pp", "km = (rp - rm) / (2 * Pm)", "km = (rp - rm) / (2 * Pp)"),
 (P1, "p1d_proper_distance_factor", "ell2_over_delta = 4 * Sig0 / (2 * s)", "ell2_over_delta = 2 * Sig0 / (2 * s)"),
 (P1, "p1e_rho0_three", "assert NU_PI * kp * 2 * 2 / kp == F(1, 4)", "assert NU_PI * kp * 2 * 3 / kp == F(1, 4)"),
 (P1, "p1f_temp_ratio", "ratio[2] == M * rp / (2 * s * s)", "ratio[2] == M * M / (s * s)"),
 (P1, "p1g_eta_uu", "eta[2][2] = S / (1 - u * u)", "eta[2][2] = P / (1 - u * u)"),
 (P2, "p2a_drop_last_term", "return R * (2 * M - R) - a * a - (1 - u * u) * a ** 4 * u * u / (R * R)", "return R * (2 * M - R) - a * a"),
 (P2, "p2b_flip_Rprime", "Rp = -a * a * u / R ", "Rp = a * a * u / R "),
 (P2, "p2c_double_H", "H = M * r / S", "H = 2 * M * r / S"),
 (P2, "p2d_delta_coefficient_one", "delta = F(5, 2) * a * a / (rho * (2 * M - rho))", "delta = F(1, 1) * a * a / (rho * (2 * M - rho))"),
 (P2, "p2e_Rprime_zero", "Rp = -a * a * u / R ", "Rp = 0 * a * a * u / R "),
 (P2, "p2f_quarter_bound", "p = [F(1), F(-1, 4)]", "p = [F(1), F(-1, 3)]"),
 (P2, "p2g_strictness_one_sixth", "assert a * a / (M * M) <= eps / 9", "assert a * a / (M * M) <= eps / 300"),
]
for prop, name, old, new in CASES:
    src = open(os.path.join(LAB, "proposals", prop, "check.py")).read()
    assert src.count(old) >= 1, (name, "pattern not found")
    out = os.path.join(W, name + ".py")
    open(out, "w").write(src.replace(old, new))
    r = subprocess.run([sys.executable, os.path.join(LAB, "colony", "runcheck.py"), out], capture_output=True, text=True,
                       env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    lines = [l.split("   ")[0] for l in r.stdout.splitlines() if l.startswith(("PASS", "FAIL"))]
    print(name, "->", "ALL PASS (insensitive)" if r.returncode == 0 else "FAILS: " + ", ".join(l for l in lines if l.startswith("FAIL")))
