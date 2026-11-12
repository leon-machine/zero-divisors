"""Referee R3: perturbations of the new or changed check functions (copies in pert/; store untouched)."""
import os, subprocess, sys
LAB = "/home/claude/phys-graph"
HERE = os.path.dirname(os.path.abspath(__file__))
C1 = LAB + "/store/claims/synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight/check.py"
C3 = LAB + "/store/claims/synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit/check.py"
C4 = LAB + "/store/claims/synthesis.infinite-strings-tail-classes-and-reading-rules-linear-and-not/check.py"
PERTS = [
    ("C1_u_uses_new_e", C1, "    u = mul(e(0), f(1), S)\n", "    u = mul(e(0), e(1), S)\n", "FAIL (e_0 e_new is not sigma_e-invariant)"),
    ("C1_drop_restriction_test", C1, "        ok = ok and Om(b) == (1 if b == {(): F(1)} else 0)\n", "        pass\n", "PASS (info: restriction line removed)"),
    ("C3_one_pair_not_rotated", C3, "            GA_, GB_ = one_particle(A, m)", "            A, B = branches(N, c, s, range(N - 1))\n            GA_, GB_ = one_particle(A, m)", "FAIL (iv)"),
    ("C3_mode_sign_flipped", C3, "ok = ok and GA_[2][3] == -c * s", "ok = ok and GA_[2][3] == c * s", "FAIL (iv) unless c = 0 ... c=3/5 present"),
    ("C4_rule_shifted", C4, "            outcome = yval < wval\n", "            outcome = yval < wval - F(1, 32)\n", "FAIL (v)"),
    ("C4_rule_nonstrict", C4, "            outcome = yval < wval\n", "            outcome = yval <= wval\n", "PASS expected (non-dyadic a^2; harmless)"),
    ("C4_agreement_reversed", C4, "(outcome == (bits[k0] < digits[k0]))", "(outcome == (bits[k0] > digits[k0]))", "FAIL (vi)"),
    ("C4_perm_e_to_f", C4, "perm = {0: 2, 1: 3, 2: 0, 3: 1, 4: 4, 5: 5}", "perm = {0: 3, 1: 2, 2: 1, 3: 0, 4: 4, 5: 5}", "FAIL (squares change)"),
    ("C4_perm_not_bijective_on_strings", C4, "string_proj((s[1], s[0], s[2]), S)", "string_proj((s[0], s[1], s[2]), S)", "FAIL"),
]
os.makedirs(os.path.join(HERE, "pert"), exist_ok=True)
for name, src, old, new, expect in PERTS:
    text = open(src).read()
    assert text.count(old) == 1, (name, text.count(old))
    d = os.path.join(HERE, "pert", name)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, "check.py")
    open(path, "w").write(text.replace(old, new))
    r = subprocess.run([sys.executable, LAB + "/colony/runcheck.py", path], capture_output=True, text=True, timeout=900)
    lines = [l for l in r.stdout.splitlines() if l.startswith(("PASS check", "FAIL"))]
    print(f"== {name}  (expected: {expect})")
    for l in lines:
        print("   " + l.split("   premises")[0][:150])
    if r.stderr.strip():
        print("   stderr:", r.stderr.strip().splitlines()[-1][:200])
