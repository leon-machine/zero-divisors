"""perturb.py src dst 'old' 'new' [count]: exact-string replacement, fails loudly if old not found."""
import sys
src, dst, old, new = sys.argv[1:5]
t = open(src).read()
n = t.count(old)
assert n >= 1, f"pattern not found: {old!r}"
cnt = int(sys.argv[5]) if len(sys.argv) > 5 else -1
open(dst, "w").write(t.replace(old, new, cnt))
print(f"replaced {n if cnt < 0 else min(n, cnt)} occurrence(s)")
