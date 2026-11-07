import sys, importlib.util, time
sys.path.insert(0, "/home/claude/phys-graph/lib")
pairs = {
 "dark-energy.gravity-pre-metric-forces-degenerate-exactly": ["check_gtg_star_free_density_is_a_divergence","check_gtg_hodge_star_is_the_cometric_duality","check_gtg_star_has_no_limit_at_a_corank_one_wall"],
 "dark-energy.stelle-west-vector-frozen-point": ["check_tractor_gauge_field_slots_and_bracket"],
 "synthesis.black-hole-data-do-not-fix-field-equations": ["check_gtg_black_hole_data"],
 "synthesis.collapsing-hole-flux-from-ground-state-on-the-ingoing-sheet": ["check_gtg_ingoing_generator_is_affine_and_horizon_rate"],
 "synthesis.cosmological-horizon-completed-pair": ["check_gtg_dilation_field_curvature_selects_no_plane"],
 "synthesis.frozen-point-reduces-the-connection-only-when-infinitely-stiff": ["check_gtg_readings_of_the_curvature_operator"],
 "synthesis.killing-horizon-value-factor-is-the-generator-boost": ["check_gtg_pg_torsion_equation_and_killing_line"],
 "synthesis.macdowell-mansouri-is-the-frozen-point-reduction-of-five-dimensional-chern-simons": ["check_gtg_reduction_with_base_forms_as_background_multivectors"],
 "synthesis.nondiagonal-kasner-residue-weighted-shear": ["check_gtg_torsion_equation_gives_the_boost_block"],
 "synthesis.two-frozen-points-conformally-flat": ["check_gtg_parallel_tractors_flat_strength_and_einstein_scale"],
}
import tp_premise; tp_premise.configure("/home/claude/phys-graph/store")
only = sys.argv[1:]
for ent, fns in pairs.items():
    if only and not any(o in ent for o in only): continue
    path = f"/home/claude/phys-graph/store/claims/{ent}/check.py"
    spec = importlib.util.spec_from_file_location("chk_"+ent.replace(".","_").replace("-","_"), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for fn in fns:
        t=time.time()
        try:
            r = getattr(m, fn)(); print("PASS", ent, fn, round(time.time()-t,1))
        except Exception as e:
            print("FAIL", ent, fn, type(e).__name__, e)
