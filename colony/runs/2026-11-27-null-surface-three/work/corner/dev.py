import sys, os, importlib.util, time
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
spec = importlib.util.spec_from_file_location("ck", os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_new.py"))
ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
