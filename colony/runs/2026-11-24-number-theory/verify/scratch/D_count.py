import sys; sys.path.insert(0,'lib'); sys.path.insert(0,'proposals/synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points')
import tp_premise; tp_premise.configure('store')
import importlib.util
spec=importlib.util.spec_from_file_location('c','proposals/synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points/check.py'); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
u=[0]
print(m.sign_on(m.D_A,m.Q_LO,-1,u), m.sign_on(m.Q_HI,m.T_LO,1,u), m.sign_on(m.T_HI,m.H_LO,-1,u), u[0])
# tail bound size at worst place
for d in (m.D_A, m.F(1,2)):
    j=m.thermal_jet(m.iv(d))
    print(float(m.F(j[0][1]-j[0][0], m.P)))
