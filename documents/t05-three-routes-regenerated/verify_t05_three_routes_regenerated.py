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
 "verify_T05.py": [
  "num:5.7",
  "num:9.6"
 ],
 "verify_three_routes.py": [
  "num:2.2",
  "num:2.4",
  "num:2.5",
  "num:3.3",
  "num:3.4",
  "num:3.5",
  "num:4.1",
  "num:4.2"
 ]
}
CHECKS = [('three-routes.imported-boundary-gram-ladder', 'claims/three-routes.imported-boundary-gram-ladder', 'check.py::check_boundary_gram_and_radical'), ('three-routes.imported-boundary-gram-ladder', 'claims/three-routes.imported-boundary-gram-ladder', 'check.py::check_completed_form_nondegenerate_on_physical_closure'), ('three-routes.imported-boundary-gram-ladder', 'claims/three-routes.imported-boundary-gram-ladder', 'check.py::check_ladder_pair_exactly_over_boundary'), ('three-routes.it-sheaf-risk-resolves-into-standing', 'claims/three-routes.it-sheaf-risk-resolves-into-standing', 'check.py::check_fibrewise_even_part_is_subalgebra'), ('three-routes.it-sheaf-risk-resolves-into-standing', 'claims/three-routes.it-sheaf-risk-resolves-into-standing', 'check.py::check_even_families_glue_and_form_an_algebra'), ('three-routes.it-sheaf-risk-resolves-into-standing', 'claims/three-routes.it-sheaf-risk-resolves-into-standing', 'check.py::check_parity_insensitive_to_ladder_rescaling'), ('three-routes.it-sheaf-risk-resolves-into-standing', 'claims/three-routes.it-sheaf-risk-resolves-into-standing', 'check.py::check_untwisted_ladder_exists_iff_w1_zero'), ('three-routes.it-sheaf-risk-resolves-into-standing', 'claims/three-routes.it-sheaf-risk-resolves-into-standing', 'check.py::check_even_part_does_not_see_the_twist'), ('three-routes.stalks-are-pointwise-metric-levels', 'claims/three-routes.stalks-are-pointwise-metric-levels', 'check.py::check_projection_is_smooth_idempotent_constant_rank'), ('three-routes.stalks-are-pointwise-metric-levels', 'claims/three-routes.stalks-are-pointwise-metric-levels', 'check.py::check_range_is_even_part_kernel_odd_part'), ('three-routes.stalks-are-pointwise-metric-levels', 'claims/three-routes.stalks-are-pointwise-metric-levels', 'check.py::check_even_germs_are_the_stalk'), ('three-routes.join-disqualified-wrong-stalks', 'claims/three-routes.join-disqualified-wrong-stalks', 'check.py::check_join_is_the_whole_ledger'), ('three-routes.join-disqualified-wrong-stalks', 'claims/three-routes.join-disqualified-wrong-stalks', 'check.py::check_join_has_elements_odd_at_each_point'), ('three-routes.base-unipotents-their-action-candidates', 'claims/three-routes.base-unipotents-their-action-candidates', 'check.py::check_unipotents_are_isometries_fixing_k'), ('three-routes.base-unipotents-their-action-candidates', 'claims/three-routes.base-unipotents-their-action-candidates', 'check.py::check_dual_action_translates_candidates'), ('three-routes.radical-gauge-closes-solve', 'claims/three-routes.radical-gauge-closes-solve', 'check.py::check_image_is_ker_k'), ('three-routes.radical-gauge-closes-solve', 'claims/three-routes.radical-gauge-closes-solve', 'check.py::check_unique_modulo_radical'), ('three-routes.radical-gauge-closes-solve', 'claims/three-routes.radical-gauge-closes-solve', 'check.py::check_normalisation_fixes_the_gauge'), ('three-routes.change-transversal-canonical-isomorphism-completions', 'claims/three-routes.change-transversal-canonical-isomorphism-completions', 'check.py::check_intertwiner_on_boundary_data'), ('three-routes.change-transversal-canonical-isomorphism-completions', 'claims/three-routes.change-transversal-canonical-isomorphism-completions', 'check.py::check_normalised_representative_is_choice_free'), ('three-routes.change-transversal-canonical-isomorphism-completions', 'claims/three-routes.change-transversal-canonical-isomorphism-completions', 'check.py::check_ladder_carried_to_ladder'), ('three-routes.no-equivariant-value-boundary', 'claims/three-routes.no-equivariant-value-boundary', 'check.py::check_theta_is_automorphism_of_completed_structure'), ('three-routes.no-equivariant-value-boundary', 'claims/three-routes.no-equivariant-value-boundary', 'check.py::check_dual_action_is_free_translation'), ('three-routes.function-linear-maps-preserve-supports', 'claims/three-routes.function-linear-maps-preserve-supports', 'check.py::check_function_linear_maps_are_bundle_maps'), ('three-routes.function-linear-maps-preserve-supports', 'claims/three-routes.function-linear-maps-preserve-supports', 'check.py::check_supports_are_preserved'), ('three-routes.function-linear-maps-preserve-supports', 'claims/three-routes.function-linear-maps-preserve-supports', 'check.py::check_hopping_is_not_function_linear'), ('three-routes.support-preserving-families-quantise-without-hopping', 'claims/three-routes.support-preserving-families-quantise-without-hopping', 'check.py::check_bundle_maps_conserve_every_occupation'), ('three-routes.support-preserving-families-quantise-without-hopping', 'claims/three-routes.support-preserving-families-quantise-without-hopping', 'check.py::check_cross_components_hop'), ('three-routes.support-preserving-families-quantise-without-hopping', 'claims/three-routes.support-preserving-families-quantise-without-hopping', 'check.py::check_cross_point_diagonal_products_are_not_hopping'), ('three-routes.class-relative-no-go', 'claims/three-routes.class-relative-no-go', 'check.py::check_function_linear_maps_are_diagonal'), ('three-routes.class-relative-no-go', 'claims/three-routes.class-relative-no-go', 'check.py::check_bundle_maps_quantise_without_hopping'), ('three-routes.class-relative-no-go', 'claims/three-routes.class-relative-no-go', 'check.py::check_off_diagonal_generators_hop'), ('singularity.finite-truncation-meet-big-fibres-equals', 'claims/singularity.finite-truncation-meet-big-fibres-equals', 'check.py::check_meet_of_big_fibres_is_joint_diagonal'), ('singularity.finite-truncation-meet-big-fibres-equals', 'claims/singularity.finite-truncation-meet-big-fibres-equals', 'check.py::check_join_of_small_fibres_is_the_same_algebra'), ('singularity.finite-truncation-meet-big-fibres-equals', 'claims/singularity.finite-truncation-meet-big-fibres-equals', 'check.py::check_range_of_joint_descent_is_the_same_algebra'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_determinant_identity_and_no_shadow_wall'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_signature_two_four_on_the_whole_closure'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_ladder_pair_exactly_over_the_boundary'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_gram_matrix_of_the_cometric'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_nondegenerate_off_the_wall'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_corank_one_on_the_wall'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_first_order_degeneration'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_schwarzschild_frame_transition'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_rain_identity'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_descent_is_parity_average'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_range_kernel_and_uniqueness'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_preserves_alpha_invariant_states'), ('singularity.p-reduced-metric-level-reading-many', 'claims/singularity.p-reduced-metric-level-reading-many', 'check.py::check_modewise_descents_commute_and_compose_to_joint_pinching'), ('singularity.p-reduced-metric-level-reading-many', 'claims/singularity.p-reduced-metric-level-reading-many', 'check.py::check_fixed_subalgebra_dimension_and_uniqueness_step'), ('singularity.p-reduced-metric-level-reading-many', 'claims/singularity.p-reduced-metric-level-reading-many', 'check.py::check_meet_is_joint_diagonal_smaller_than_parity_even'), ('std-algebra.functoriality', 'claims/std-algebra.functoriality', 'check.py::check_isometry_extends_multiplicatively')]

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
