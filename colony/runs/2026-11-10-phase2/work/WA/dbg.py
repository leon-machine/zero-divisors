import sys,os
sys.path.insert(0,'lib'); sys.path.insert(0,'tp')
import importlib.util
import tp_premise
spec=importlib.util.spec_from_file_location('c',sys.argv[1]); c=importlib.util.module_from_spec(spec); spec.loader.exec_module(c)
F=c.F
two, quarter = c.twisted(F(1, 2), 2), c.twisted(F(1, 4), 1)
three, sixth, mid = c.twisted(F(1, 2), 3), c.twisted(F(1, 6), 1), c.twisted(F(1, 2), 1)
for i in range(3):
    print(i, c.same(two[i], c.iscale(2, quarter[i])), c.same(three[i], c.iadd(mid[i], c.iscale(2, sixth[i]))), float(two[i][1]-two[i][0]), float(quarter[i][1]-quarter[i][0]))
print(float(quarter[0][0]), float(sixth[0][0]))
