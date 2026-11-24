import sys, os, importlib.util
LAB="/home/claude/leon-machine/zero-divisors"
sys.path.insert(0, LAB+"/lib"); import tp_premise, GA
tp_premise.configure(LAB+"/store")
path, fn = sys.argv[1], sys.argv[2]
sys.path.insert(0, os.path.dirname(os.path.abspath(path)))
spec=importlib.util.spec_from_file_location("m", path); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
n=len(GA.FAILURES); r=getattr(m,fn)(); print(fn, "PASS" if (r is not False and len(GA.FAILURES)==n) else "FAIL")
