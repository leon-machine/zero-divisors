import sys, os, importlib.util, time
LAB = "/home/claude/zero-divisors"
sys.path.insert(0, os.path.join(LAB, "lib"))
import tp_premise, GA
tp_premise.configure(os.path.join(LAB, "store"))
spec = importlib.util.spec_from_file_location("ck", "check_new.py")
ck = importlib.util.module_from_spec(spec); spec.loader.exec_module(ck)
globals().update({k: v for k, v in vars(ck).items() if not k.startswith("__")})
h, wgt, zeta, zfix, zoff, ztan = corner_samples()
dens = corner(potential(displacement(ztan), XIB, COEF)[B03])
total = integrate(dens, LO[1:], HI[1:])
print("total", total, -2 * edge_flux(ztan), dens)
print(check_pairing_with_a_displacement_is_the_field_equation_plus_a_divergence())
