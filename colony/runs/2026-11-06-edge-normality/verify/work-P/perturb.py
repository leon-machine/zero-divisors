"""Referee P perturbation runner: copy a check.py, apply one textual substitution, run runcheck, report."""
import os, subprocess, sys
LAB = "/home/claude/phys-graph"
HERE = os.path.dirname(os.path.abspath(__file__))
P1 = LAB + "/proposals/synthesis.geometric-modular-conjugations-on-a-generator-give-the-null-ground-state/check.py"
P2 = LAB + "/proposals/synthesis.modular-data-on-a-generator-fix-neither-the-translation-lift-nor-the-sign-of-i/check.py"
CASES = [
    ("P1-band-edge", P1, "return -(A(2) - A(0)) + (0 - A(2))", "return -(A(3) - A(0)) + (0 - A(3))"),
    ("P1-vacuum-gram", P1, "G[m][n] == F(_fact(m) * _fact(n), m + n + 1))", "G[m][n] == F(_fact(m) * _fact(n), m + n + 2))"),
    ("P1-eta-sign", P1, "for eta, want in ((-1, (5, 0)), (1, (0, 5))):", "for eta, want in ((1, (5, 0)), (-1, (0, 5))):"),
    ("P1-two-cuts", P1, "for a in (0, 1):", "for a in (0, F(1, 2)):"),
    ("P2-W-sign", P2, "assert modular_conjugation_case([[c, s]], [0], [1], [[I]])", "assert modular_conjugation_case([[c, s]], [0], [1], [[-I]])"),
    ("P2-sigma", P2, "sigma = F(-1) ** len(block)", "sigma = F(-1) ** (len(block) + 1)"),
    ("P2-hankel-phase", P2, "c_vac, c_sea = QI(0, -1), QI(0, 1)", "c_vac, c_sea = QI(0, 1), QI(0, -1)"),
    ("P2-GA-B", P2, "I4, B, J = m(g[0], g[1], g[2], g[3]), m(g[0], g[3]), m(g[1], g[2])", "I4, B, J = m(g[0], g[1], g[2], g[3]), m(g[0], g[1]), m(g[1], g[2])"),
]
only = sys.argv[1:]
for name, src, old, new in CASES:
    if only and name not in only:
        continue
    text = open(src).read()
    assert text.count(old) == 1, (name, text.count(old))
    d = os.path.join(HERE, name)
    os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "check.py"), "w").write(text.replace(old, new))
    r = subprocess.run([sys.executable, LAB + "/colony/runcheck.py", os.path.join(d, "check.py")], capture_output=True, text=True)
    fails = [l for l in r.stdout.splitlines() if l.startswith("FAIL check_")]
    print(f"{name}: exit {r.returncode}; failing functions: {[f.split()[1] for f in fails]}")
