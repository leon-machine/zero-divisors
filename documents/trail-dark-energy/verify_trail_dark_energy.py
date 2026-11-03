"""Verify script assembled from the claims in this document.
Runs each claim's own check and the tagged checks of the series verify
scripts it relies on.  Exact arithmetic throughout (GA.py)."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
LAB = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path[:0] = [os.path.join(LAB, 'lib'), LAB]
import GA
from tp import evidence
from tp.model import load_store
from tp.validate import legacy_path
STORE = os.path.join(LAB, 'store')
LEGACY_DIR = os.path.normpath(os.path.join(STORE, '../legacy'))
LEGACY = {
 "verify_T06.py": [
  "num:4.4",
  "num:4.5",
  "num:4.7"
 ],
 "verify_T10.py": [
  "label:fact:frozen",
  "label:lem:sw",
  "label:prop:goldstone",
  "label:prop:parameter",
  "label:prop:w",
  "label:thm:action"
 ],
 "verify_T12.py": [
  "label:prop:trichotomy"
 ]
}
CHECKS = [('dark-energy.imported-frozen-point-geometry', 'claims/dark-energy.imported-frozen-point-geometry', 'check.py::check_tractor_gauge_field_reproduces_connection'), ('dark-energy.imported-frozen-point-geometry', 'claims/dark-energy.imported-frozen-point-geometry', 'check.py::check_vacuum_iff_null_scale_tractor_parallel'), ('dark-energy.imported-frozen-point-geometry', 'claims/dark-energy.imported-frozen-point-geometry', 'check.py::check_stabilisers_reductive_and_parabolic'), ('dark-energy.stelle-west-vector-frozen-point', 'claims/dark-energy.stelle-west-vector-frozen-point', 'check.py::check_constraints_and_slots'), ('dark-energy.stelle-west-vector-frozen-point', 'claims/dark-energy.stelle-west-vector-frozen-point', 'check.py::check_de_sitter_field_soldering_and_parallel_frozen_point'), ('dark-energy.stelle-west-vector-frozen-point', 'claims/dark-energy.stelle-west-vector-frozen-point', 'check.py::check_gauge_field_is_omega_plus_frame_wedge_w'), ('dark-energy.stelle-west-vector-frozen-point', 'claims/dark-energy.stelle-west-vector-frozen-point', 'check.py::check_bracket_of_soldering_bivectors'), ('dark-energy.frozen-point-makes-stelle-west-vector', 'claims/dark-energy.frozen-point-makes-stelle-west-vector', 'check.py::check_reduction_and_curvature_in_i_perp'), ('dark-energy.frozen-point-makes-stelle-west-vector', 'claims/dark-energy.frozen-point-makes-stelle-west-vector', 'check.py::check_stelle_west_datum_and_lorentz_block'), ('dark-energy.frozen-point-makes-stelle-west-vector', 'claims/dark-energy.frozen-point-makes-stelle-west-vector', 'check.py::check_action_prefactor_expansion_and_invariance'), ('dark-energy.point-infinity-has-no-physical-fluctuation', 'claims/dark-energy.point-infinity-has-no-physical-fluctuation', 'check.py::check_constrained_fluctuations_nine'), ('dark-energy.point-infinity-has-no-physical-fluctuation', 'claims/dark-energy.point-infinity-has-no-physical-fluctuation', 'check.py::check_broken_generators_act_bijectively'), ('dark-energy.point-infinity-has-no-physical-fluctuation', 'claims/dark-energy.point-infinity-has-no-physical-fluctuation', 'check.py::check_integrand_invariant_under_ambient_group'), ('dark-energy.point-infinity-has-no-physical-fluctuation', 'claims/dark-energy.point-infinity-has-no-physical-fluctuation', 'check.py::check_fluctuation_is_gauge_on_de_sitter_field'), ('dark-energy.vacuum-region-registration-condition', 'claims/dark-energy.vacuum-region-registration-condition', 'check.py::check_norm_constant_and_w_minus_one'), ('dark-energy.vacuum-region-registration-condition', 'claims/dark-energy.vacuum-region-registration-condition', 'check.py::check_general_scale_tractor_norm_is_r_over_twelve'), ('dark-energy.four-alternatives-are-exhaustive-three-are', 'claims/dark-energy.four-alternatives-are-exhaustive-three-are', 'check.py::check_trichotomy_and_independence'), ('dark-energy.under-action-written-norm-parameter-laws', 'claims/dark-energy.under-action-written-norm-parameter-laws', 'check.py::check_fixed_lambda_nine_and_de_sitter_scale'), ('dark-energy.under-action-written-norm-parameter-laws', 'claims/dark-energy.under-action-written-norm-parameter-laws', 'check.py::check_n_varies_with_lambda'), ('dark-energy.under-action-written-norm-parameter-laws', 'claims/dark-energy.under-action-written-norm-parameter-laws', 'check.py::check_varying_lambda_single_norm_mode'), ('odd-extensions.transport-constrains-frozen-point-only-through', 'claims/odd-extensions.transport-constrains-frozen-point-only-through', 'check.py::check_unique_canonical_partner'), ('odd-extensions.transport-constrains-frozen-point-only-through', 'claims/odd-extensions.transport-constrains-frozen-point-only-through', 'check.py::check_norm_is_two_ab'), ('odd-extensions.transport-constrains-frozen-point-only-through', 'claims/odd-extensions.transport-constrains-frozen-point-only-through', 'check.py::check_orbits_are_level_sets'), ('odd-extensions.transport-constrains-frozen-point-only-through', 'claims/odd-extensions.transport-constrains-frozen-point-only-through', 'check.py::check_two_signs_non_isomorphic'), ('dark-energy.imported-walls-sphere-theorem', 'claims/dark-energy.imported-walls-sphere-theorem', 'check.py::check_radical_and_simple_pole'), ('dark-energy.imported-walls-sphere-theorem', 'claims/dark-energy.imported-walls-sphere-theorem', 'check.py::check_clifford_algebra_continues_with_square_zero_ideal'), ('dark-energy.imported-walls-sphere-theorem', 'claims/dark-energy.imported-walls-sphere-theorem', 'check.py::check_witt_partner_exactly_at_the_wall'), ('dark-energy.imported-walls-sphere-theorem', 'claims/dark-energy.imported-walls-sphere-theorem', 'check.py::check_principal_su2_carried_by_boundary_bilinears'), ('interior.covariant-form-vacuum-equations', 'claims/interior.covariant-form-vacuum-equations', 'check.py::check_derivative_of_the_scale_tractor_is_minus_schouten'), ('interior.covariant-form-vacuum-equations', 'claims/interior.covariant-form-vacuum-equations', 'check.py::check_parallel_iff_vacuum'), ('interior.covariant-form-vacuum-equations', 'claims/interior.covariant-form-vacuum-equations', 'check.py::check_parallel_null_tractor_without_field_equations'), ('interior.covariant-form-vacuum-equations', 'claims/interior.covariant-form-vacuum-equations', 'check.py::check_structure_algebra_so24'), ('interior.non-null-stabilisers-section-they-act', 'claims/interior.non-null-stabilisers-section-they-act', 'check.py::check_stabiliser_is_so_of_the_complement'), ('interior.non-null-stabilisers-section-they-act', 'claims/interior.non-null-stabilisers-section-they-act', 'check.py::check_section_is_the_pseudosphere_with_transitive_isometries'), ('interior.non-null-stabilisers-section-they-act', 'claims/interior.non-null-stabilisers-section-they-act', 'check.py::check_polar_infinity_spacelike_or_timelike'), ('interior.scale-tractor-leaves-cone', 'claims/interior.scale-tractor-leaves-cone', 'check.py::check_einstein_scale_tractor_is_parallel'), ('interior.scale-tractor-leaves-cone', 'claims/interior.scale-tractor-leaves-cone', 'check.py::check_only_rho_lambda_over_six_and_only_einstein'), ('interior.scale-tractor-leaves-cone', 'claims/interior.scale-tractor-leaves-cone', 'check.py::check_norm_is_lambda_over_three'), ('interior.sign-fixed-internally', 'claims/interior.sign-fixed-internally', 'check.py::check_displayed_sign_attaches_de_sitter'), ('interior.sign-fixed-internally', 'claims/interior.sign-fixed-internally', 'check.py::check_opposite_sign_attaches_anti_de_sitter'), ('interior.stabiliser-rotates-parabolic-reductive', 'claims/interior.stabiliser-rotates-parabolic-reductive', 'check.py::check_stabiliser_dimension_and_shape'), ('interior.stabiliser-rotates-parabolic-reductive', 'claims/interior.stabiliser-rotates-parabolic-reductive', 'check.py::check_reductive_or_parabolic'), ('interior.stabiliser-rotates-parabolic-reductive', 'claims/interior.stabiliser-rotates-parabolic-reductive', 'check.py::check_section_and_polar_infinity'), ('odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'claims/odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'check.py::check_lower_bound_dimension'), ('odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'claims/odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'check.py::check_minimal_completions_signature'), ('odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'claims/odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'check.py::check_minimal_completion_unique_fixing_v'), ('odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'claims/odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'check.py::check_type_n_increment_forced'), ('odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'claims/odd-extensions.imported-minimal-completion-degenerate-algebra-rule', 'check.py::check_type_c_sign_forgotten'), ('odd-extensions.twistor-algebra', 'claims/odd-extensions.twistor-algebra', 'check.py::check_even_subalgebra_is_cl23_cl41_and_mat4c'), ('odd-extensions.twistor-algebra', 'claims/odd-extensions.twistor-algebra', 'check.py::check_both_oriented_shadows_inside_even_subalgebra'), ('odd-extensions.twistor-algebra', 'claims/odd-extensions.twistor-algebra', 'check.py::check_conformal_spinors_are_the_module_of_the_even_subalgebra'), ('odd-extensions.twistor-algebra', 'claims/odd-extensions.twistor-algebra', 'check.py::check_signature_reversal_changes_the_centre'), ('standard-model.trichotomy-what-kind-number', 'claims/standard-model.trichotomy-what-kind-number', 'check.py::check_rescaling_kinematics'), ('standard-model.trichotomy-what-kind-number', 'claims/standard-model.trichotomy-what-kind-number', 'check.py::check_n_varies_across_lambda'), ('standard-model.trichotomy-what-kind-number', 'claims/standard-model.trichotomy-what-kind-number', 'check.py::check_units_statement_numbers')]

def main():
    global _STORE, _LDIR
    _STORE = load_store(STORE)
    _LDIR = _STORE.config.get('legacy_scripts_dir')
    ok = True
    for script, tags in LEGACY.items():
        res = evidence.run_legacy(legacy_path(_STORE, _LDIR, script),
                                  os.path.join(STORE, '.tp-cache'))
        hits = [(l, r) for l, r in res if evidence.label_keys(l) & set(tags)]
        bad = [l for l, r in hits if not r]
        GA.check(f'{script}: {len(hits)} tagged checks', bool(hits) and not bad)
        ok &= bool(hits) and not bad
    for cid, folder, ref in CHECKS:
        fname, func = ref.split('::')
        path = os.path.join(STORE, folder)
        src = open(os.path.join(path, fname)).read()
        r = evidence.run_check(STORE, path, src, func)
        GA.check(f'{cid}: {ref}', r['ok'])
        ok &= r['ok']
    print(('ALL PASS' if ok else 'FAILURES: ' + str(len(GA.FAILURES))))
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(main())
