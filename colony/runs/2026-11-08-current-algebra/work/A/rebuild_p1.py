import re
d = 'synthesis.standard-model-currents-of-the-sixteen-channels-levels-and-window-sugawara-split/'
s = open('full_check_backup.py').read()
def remove_def(s, name):
    a = s.index("def %s(" % name)
    m = re.compile(r"\n(def |class |# -{10}|[A-Z_]+ = )").search(s, a + 5)
    b = m.start() + 1 if m else len(s)
    return s[:a] + s[b:]
for fn in ("check_window_energy_is_the_u_n_sugawara_form", "check_so10_currents_carry_the_su16_energy_at_levels_one_and_two",
           "_so10_level_one_energies", "_so10_complement_casimir", "_tower_planes_ok", "_energy_residual",
           "_identity_on_all_states", "_identity_on_samples", "_so10"):
    s = remove_def(s, fn)
s = s.rstrip() + "\n"
old_cas = s[s.index("def check_adjoint_casimirs_and_central_charges():"):s.index("def check_split_commutes_on_localised_window_vectors():")]
new_cas = '''def check_adjoint_casimirs_and_central_charges():
    premise("synthesis.cpt-closure-forces-slot-module-and-chirality")
    data = _factor_data()
    lam = {d[0]: d[3] for d in data}
    GA.check("adjoint Casimirs in the trace-dual basis: su(3) 3/2, su(2) 1, abelian 0",
             [lam["su3"], lam["su2"], lam["Y"], lam["N"]] == [F(3, 2), 1, 0, 0])
    GA.check("gl(16) Casimir on a traceless element: 32", _gl_casimir_value(NC) == 32)
    c = lambda d, l: F(2 * d, 1) / (2 + l)
    GA.check("c = 2 dim / (2 + lam): su(3) 32/7, su(2) 2, u(1) 1, su(16) 15",
             [c(8, lam["su3"]), c(3, lam["su2"]), c(1, lam["Y"]), c(255, _gl_casimir_value(NC))]
             == [F(32, 7), 2, 1, 15])
    GA.check("coset: 16 - 32/7 - 2 - 1 - 1 = 52/7", 16 - c(8, lam["su3"]) - c(3, lam["su2"]) - 2 == F(52, 7))
    return True


'''
s = s.replace(old_cas, new_cas)
s = s.replace('''    premise("synthesis.null-vacuum-on-a-horizon-generator")
    data = _factor_data()
    own, other, coset''', '''    premise("synthesis.null-vacuum-on-a-horizon-generator")
    premise("synthesis.exact-window-sugawara-identity-and-luttinger-normal-modes-of-tower-density-waves")
    data = _factor_data()
    own, other, coset''')
s = s.replace("SMALL_CASES = ((1, 4), (2, 3), (3, 3))\nPLANES = 3\n", "")
s = s.replace("""(3) (n + 1) H = sum_{q>=1} (sum_xy J(E_yx)_{-q} J(E_xy)_q + N_{-q} N_q) + (G_0 + N_0^2)/2 on every basis state,
    n = 1, 2, 3, and on sample states of the sixteen channels.
""", "")
a = s.index("(7) so(10) of all bilinears"); b = s.index('"""', a)
s = s[:a] + s[b:]
s = s.replace("(4) Adjoint Casimirs lam = 3/2 (su(3)), 1 (su(2)), 4 (so(10)), 2n on su(n)", "(3) Adjoint Casimirs lam = 3/2 (su(3)), 1 (su(2)), 2n on su(n)")
s = s.replace("(5) On localised", "(4) On localised").replace("(6) ||L^f", "(5) ||L^f")
open(d + 'check.py', 'w').write(s)
