"""R2 helper: apply a text perturbation to a copy of a proposal's check.py and run it with runcheck.

usage: python3 perturb.py <proposal-id> <tag> <old> <new> [count]
The copy is written to work-R2/pert_<tag>/check.py; prints the runcheck PASS/FAIL lines.
"""
import os
import subprocess
import sys

LAB = "/home/claude/phys-graph"
W = os.path.join(LAB, "colony/runs/2026-11-09-solvable/verify/work-R2")
pid, tag, old, new = sys.argv[1:5]
count = int(sys.argv[5]) if len(sys.argv) > 5 else 1
src = open(os.path.join(LAB, "proposals", pid, "check.py")).read()
n = src.count(old)
if n == 0:
    sys.exit(f"perturbation {tag}: old text not found")
out = src.replace(old, new, count)
d = os.path.join(W, f"pert_{tag}")
os.makedirs(d, exist_ok=True)
open(os.path.join(d, "check.py"), "w").write(out)
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
r = subprocess.run([sys.executable, os.path.join(LAB, "colony/runcheck.py"), os.path.join(d, "check.py")],
                   capture_output=True, text=True, env=env, cwd=LAB)
lines = [ln for ln in (r.stdout + r.stderr).splitlines() if ln.startswith(("PASS check", "FAIL check", "ERROR", "Traceback"))]
print(f"[{tag}] occurrences={n} replaced={min(n, count)}")
for ln in lines:
    print("   ", ln[:200])
