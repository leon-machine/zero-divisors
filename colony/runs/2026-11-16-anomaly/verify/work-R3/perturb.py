import sys, subprocess, os
src, outdir, old, new = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
t = open(src).read()
assert t.count(old) >= 1, "pattern not found: " + old
os.makedirs(outdir, exist_ok=True)
open(os.path.join(outdir, "check.py"), "w").write(t.replace(old, new, 1))
r = subprocess.run(["python3", "colony/runcheck.py", os.path.join(outdir, "check.py")], capture_output=True, text=True)
out = r.stdout + r.stderr
fails = [l for l in out.splitlines() if l.startswith("FAIL") or "Error" in l]
print("exit", r.returncode, "| fails:", fails[:4] if fails else "NONE")
