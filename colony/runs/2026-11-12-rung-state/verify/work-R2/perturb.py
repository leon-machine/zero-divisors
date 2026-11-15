"""Referee R2: targeted perturbations of the two new check.py files. Each perturbation is a text substitution;
the perturbed copy is run with colony/runcheck.py and the PASS/FAIL lines are recorded."""
import os
import subprocess
import sys

LAB = "/home/claude/phys-graph"
HERE = os.path.dirname(os.path.abspath(__file__))
C3 = LAB + "/store/claims/synthesis.records-of-unbounded-length-on-the-tower-interference-factor-and-limit/check.py"
C4 = LAB + "/store/claims/synthesis.infinite-strings-tail-classes-and-no-reading-law-inside-the-algebra/check.py"

PERTS = [
    # (name, source, old, new, what a sound check should do)
    ("C3_wrong_exponent", C3, "factor = c ** (N - len(K))", "factor = c ** (N - len(K) - 1)", "FAIL (i)"),
    ("C3_record_written_on_both_branches", C3,
     "    on = num(0, x)\n    return vadd(x, vsc(-1, on), rot(j, c, s, on))",
     "    return rot(j, c, s, x)", "FAIL (i)"),
    ("C3_drop_odd_words", C3, "for word in product(range(4), repeat=len(rungs)):   # a full",
     "for word in (w for w in product(range(4), repeat=len(rungs)) if sum(1 for o in w if o in (1, 2)) % 2 == 0):   # a full",
     "info: if it still passes except for the count, odd words were never informative"),
    ("C3_rotor_mode_sign_flipped_in_HS", C3, "Pa = [[c * c, -c * s], [-c * s, s * s]]", "Pa = [[c * c, c * s], [c * s, s * s]]",
     "info: (iv) check is insensitive to the mode actually produced"),
    ("C3_HS_uses_a_made_up_mode", C3, "Pa = [[c * c, -c * s], [-c * s, s * s]]", "Pa = [[s * s, -c * s], [-c * s, c * c]]",
     "info: (iv) check's HS number does not come from the branch vectors"),
    ("C3_bell_element_not_conjugated", C3, "    for j in range(N):\n        x = couple(j, c, s, x)\n    return x",
     "    return x", "FAIL (ii)"),
    ("C4_lemma_bound_loosened", C4, "ok = ok and (is_const or two_valued_points <= 4)", "ok = ok and (is_const or two_valued_points <= 6)",
     "info: if it passes, the bound is not what is being tested"),
    ("C4_nonquadratic_form", C4, "q = [a * a * M[0][0] + 2 * a * b * M[0][1] + b * b * M[1][1] for a, b in UNIT_VECTORS]",
     "q = [a ** 4 * M[0][0] + 2 * a * b * M[0][1] + b ** 4 * M[1][1] for a, b in UNIT_VECTORS]", "FAIL (iv)"),
    ("C4_only_number_tests_replaced_by_identity", C4, '"on_0": lambda x: num(0, x),', '"on_0": lambda x: x,',
     "info: constant forms count changes"),
    ("C4_flip_e_instead_of_f", C4, "ok = ok and flip(P[s], {2 * j + 1}) == P[t]", "ok = ok and flip(P[s], {2 * j}) == P[t]",
     "info: sigma_e also exchanges on/off, so should still pass"),
    ("C4_wrong_flip_target", C4, "t = tuple(b ^ (1 if i == j else 0) for i, b in enumerate(s))",
     "t = tuple(b ^ (1 if i == (j + 1) % n else 0) for i, b in enumerate(s))", "FAIL (i)"),
    ("C4_atom_not_normalised", C4, "mul(add(v(0), v(1)), P0, S)", "mul(add(v(0), scal(F(2), v(1))), P0, S)", "FAIL (iii)"),
    ("C4_wrong_target_weight", C4, "    p = F(9, 25)\n    digits = []", "    p = F(9, 26)\n    digits = []", "FAIL (v)? (period differs)"),
]

os.makedirs(os.path.join(HERE, "pert"), exist_ok=True)
for name, src, old, new, expect in PERTS:
    text = open(src).read()
    assert text.count(old) == 1, (name, text.count(old))
    path = os.path.join(HERE, "pert", name + "_check.py")
    open(path, "w").write(text.replace(old, new))
    r = subprocess.run([sys.executable, LAB + "/colony/runcheck.py", path], capture_output=True, text=True, timeout=900)
    lines = [l for l in r.stdout.splitlines() if l.startswith(("PASS check", "FAIL"))]
    print(f"== {name}  (expected: {expect})")
    for l in lines:
        print("   " + l.split("   premises")[0][:150])
    if r.stderr.strip():
        print("   stderr:", r.stderr.strip().splitlines()[-1][:200])
