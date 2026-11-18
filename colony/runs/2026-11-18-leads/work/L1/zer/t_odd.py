import sys, time, importlib.util
LAB = "/home/claude/phys-graph"
sys.path.insert(0, LAB + "/lib")
import tp_premise
tp_premise.configure(LAB + "/store")
spec = importlib.util.spec_from_file_location("stored", LAB + "/store/claims/synthesis.horizon-channels-of-the-linearised-gravitational-field-are-two-dimensional/check.py")
st = importlib.util.module_from_spec(spec); spec.loader.exec_module(st)
from fractions import Fraction as F
from uring import U
z, s0, c0 = U.z(), U.s(), U.c()
M = F(1)
t0 = time.time()
n = 0
for L in (F(7, 2),):
    for mono in st.MONOMIALS:
        for which in (0, 1):
            for (a, b) in ((F(1), F(0)), (F(0), F(1))):
                st.odd_case(M, 2 * M / (1 - z * z), z, s0, c0, L, st.basis_jet(mono, which), a, b)
                n += 1
                print(n, round(time.time() - t0, 2), flush=True)
