import sys, os
src, dst, old, new = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
t = open(src).read()
assert t.count(old) >= 1, ("not found", old)
open(dst, "w").write(t.replace(old, new))
