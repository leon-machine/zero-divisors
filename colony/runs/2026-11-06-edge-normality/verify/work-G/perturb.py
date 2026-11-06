"""Apply one textual perturbation to a proposal's check.py, run runcheck, report FAIL lines."""
import subprocess, sys, os
LAB = "/home/claude/phys-graph"
W = os.path.join(LAB, "colony/runs/2026-11-06-edge-normality/verify/work-G")
pid, label, old, new = sys.argv[1:5]
src = open(os.path.join(LAB, "proposals", pid, "check.py")).read()
assert src.count(old) >= 1, "pattern not found: " + old
mod = src.replace(old, new, 1)
d = os.path.join(W, "pert", label)
os.makedirs(d, exist_ok=True)
path = os.path.join(d, "check.py")
open(path, "w").write(mod)
r = subprocess.run([sys.executable, os.path.join(LAB, "colony/runcheck.py"), path], capture_output=True, text=True)
out = (r.stdout + r.stderr)
fails = [l for l in out.splitlines() if l.startswith("FAIL")]
print(f"[{label}] exit={r.returncode} fails={len(fails)}")
for l in fails: print("   ", l[:200])
