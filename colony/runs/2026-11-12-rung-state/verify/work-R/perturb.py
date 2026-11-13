"""Targeted perturbations of the two authors' checks, run on copies (the originals are not touched)."""
import os, subprocess, sys
LAB = "/home/claude/phys-graph"
C1 = LAB + "/store/claims/synthesis.state-of-a-new-rung-unique-symmetric-extension-is-the-half-weight/check.py"
C2 = LAB + "/store/claims/synthesis.selector-candidates-on-the-tower-integer-states-parity-deterministic-laws/check.py"
HERE = os.path.dirname(os.path.abspath(__file__))
P = [
 ("C1-adjoint-is-reverse", C1, [("def dagger(x):\n", "def dagger(x):\n    return GA.reverse(x)\n")]),
 ("C1-psd-always-true", C1, [('    G = [row[:] for row in G]\n', '    return True\n')]),
 ("C1-exchange-alone", C1, [("syms = [{ie}, {jf}, {ie, jf}]", "syms = [{jf}]")]),
 ("C1-sigma_e-alone", C1, [("syms = [{ie}, {jf}, {ie, jf}]", "syms = [{ie}]")]),
 ("C1-only-joint-flip", C1, [("syms = [{ie}, {jf}, {ie, jf}]", "syms = [{ie, jf}]")]),
 ("C2-adjoint-is-reverse", C2, [("def dagger(x):\n", "def dagger(x):\n    return GA.reverse(x)\n")]),
 ("C2-wrong-weights-3-4", C2, [("scal(F(3, 5), v(0)), scal(F(4, 5), v(1))), mul(v(2)", "scal(F(4, 5), v(0)), scal(F(3, 5), v(1))), mul(v(2)")]),
 ("C2-psd-always-true", C2, [('    G = [row[:] for row in G]\n', '    return True\n')]),
]
for name, src, reps in P:
    s = open(src).read()
    for a, b in reps:
        assert a in s, (name, a)
        s = s.replace(a, b, 1)
    out = os.path.join(HERE, "pert_" + name.replace("-", "_") + ".py")
    open(out, "w").write(s)
    r = subprocess.run([sys.executable, LAB + "/colony/runcheck.py", out], capture_output=True, text=True)
    res = [l.split()[1] + ":" + l.split()[0] for l in r.stdout.splitlines() if l.startswith(("PASS check", "FAIL check"))]
    print(name, "->", "; ".join(res))
    os.remove(out)
