"""Mutation runs of the new check functions on scratch copies (never in store/)."""
import sys, importlib.util, shutil, os
sys.path.insert(0, "/home/claude/phys-graph/lib")
import tp_premise
tp_premise.configure("/home/claude/phys-graph/store")
HERE = os.environ.get("MUT_DIR", "/tmp")  # scratch copies are written here, never in store/
ST = "/home/claude/phys-graph/store/claims/"
CASES = [
 ("dark-energy.gravity-pre-metric-forces-degenerate-exactly", "check_gtg_hodge_star_is_the_cometric_duality",
  "out = gtg.m_scal(1 / abs(d), gtg.m_mul(I4,", "out = gtg.m_scal(1 / d, gtg.m_mul(I4,", "det hb in place of |det hb|"),
 ("dark-energy.gravity-pre-metric-forces-degenerate-exactly", "check_gtg_hodge_star_is_the_cometric_duality",
  "G = [[sum(hb[i][k] * _adjoint(hb)[k][j]", "G = [[sum(_adjoint(hb)[i][k] * hb[k][j]", "G = hb^T hb"),
 ("dark-energy.stelle-west-vector-frozen-point", "check_tractor_gauge_field_slots_and_bracket",
  "OT = GA.add(Om, GA.neg(wedge(NI, A)), wedge(N0, p_map(A)))", "OT = GA.add(Om, wedge(NI, A), wedge(N0, p_map(A)))", "+ninf ^ A"),
 ("synthesis.black-hole-data-do-not-fix-field-equations", "check_gtg_black_hole_data",
  "return gtg.m_scal(-gtg.sp(gtg.m_mul(B, SIGMA)), SIGMA)", "return gtg.m_scal(gtg.sp(gtg.m_mul(B, SIGMA)), SIGMA)", "Wald direction +<B s> s"),
 ("synthesis.killing-horizon-value-factor-is-the-generator-boost", "check_gtg_pg_torsion_equation_and_killing_line",
  "(lambda r: F(2, 3) * r, F(3, 2), F(-4, 3), F(-2, 3))", "(lambda r: F(2, 3) * r, F(3, 2), F(4, 3), F(2, 3))", "de Sitter +H with f' sign flipped"),
 ("synthesis.nondiagonal-kasner-residue-weighted-shear", "check_gtg_torsion_equation_gives_the_boost_block",
  "== -sym[l][m] / t for l in range(3))", "== sym[l][m] / t for l in range(3))", "boost block +sym(B)"),
 ("synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons", "check_gtg_reduction_with_base_forms_as_background_multivectors",
  "BG5 = (1, -1, -1, -1, -1)", "BG5 = (7, 3, -2, 5, 11)", "background signature replaced by nonsense squares"),
 ("synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons", "check_gtg_reduction_with_base_forms_as_background_multivectors",
  "BG5 = (1, -1, -1, -1, -1)", "BG5 = (0, 0, 0, 0, 0)", "background signature replaced by zero squares (Grassmann)"),
 ("synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet", "check_gtg_ingoing_generator_is_affine_and_horizon_rate",
  "kt = {(0,): gtg.Jet.const(1, 4), (1,): -1 - beta}", "kt = {(0,): gtg.Jet.const(1, 4), (1,): gtg.Jet.const(-1, 4)}", "control with the physical velocity g0 - g1"),
 ("synthesis.two-frozen-points-conformally-flat", "check_gtg_parallel_tractors_flat_strength_and_einstein_scale",
  "OT = gtg.m_neg(gtg.wedge(GNI, gtg.e(a), S24))", "OT = gtg.wedge(GNI, gtg.e(a), S24)", "+ninf ^ a"),
 ("synthesis.cosmological-horizon-completed-pair", "check_gtg_dilation_field_curvature_selects_no_plane",
  "gtg.m_scal(-lam / (6 * sigma), gtg.wedge(x, gtg.e(mu)))", "gtg.m_scal(lam / (6 * sigma), gtg.wedge(x, gtg.e(mu)))", "Omega sign"),
]
for i, (ent, fn, old, new, label) in enumerate(CASES):
    src = open(ST + ent + "/check.py").read()
    assert src.count(old) == 1, (ent, old)
    path = os.path.join(HERE, f"mut_{i}.py")
    open(path, "w").write(src.replace(old, new))
    spec = importlib.util.spec_from_file_location(f"mut_{i}", path)
    mo = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mo)
        getattr(mo, fn)()
        res = "still PASSES"
    except AssertionError:
        res = "fails (caught)"
    except Exception as e:
        res = "errors: " + type(e).__name__ + " " + str(e)[:80]
    print(f"MUT {ent.split('.')[1][:40]:40s} {label:55s} -> {res}")
