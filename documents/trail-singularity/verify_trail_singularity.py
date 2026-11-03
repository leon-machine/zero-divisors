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
 "verify_T01.py": [
  "num:3.3",
  "num:3.6"
 ],
 "verify_T03.py": [
  "num:3.6"
 ],
 "verify_T04.py": [
  "num:4.4",
  "num:4.5"
 ],
 "verify_T05.py": [
  "num:2.2",
  "num:2.3",
  "num:2.4",
  "num:2.5",
  "num:2.6",
  "num:2.7",
  "num:3.1",
  "num:6.1"
 ]
}
CHECKS = [('singularity.unipotent-ray', 'claims/singularity.unipotent-ray', 'check.py::check_p_squares_to_zero'), ('singularity.unipotent-ray', 'claims/singularity.unipotent-ray', 'check.py::check_closed_form_inverse_horizon_included'), ('singularity.unipotent-ray', 'claims/singularity.unipotent-ray', 'check.py::check_trajectory_is_unipotent_ray'), ('singularity.connection-bivector-computed', 'claims/singularity.connection-bivector-computed', 'check.py::check_beta_identities_in_q_r_beta'), ('singularity.connection-bivector-computed', 'claims/singularity.connection-bivector-computed', 'check.py::check_stated_connection_solves_torsion_uniquely'), ('singularity.connection-bivector-computed', 'claims/singularity.connection-bivector-computed', 'check.py::check_connection_on_radial_plane'), ('singularity.solution-where-divergence-lies', 'claims/singularity.solution-where-divergence-lies', 'check.py::check_radial_curvature_from_gauge_field'), ('singularity.solution-where-divergence-lies', 'claims/singularity.solution-where-divergence-lies', 'check.py::check_vacuum_curvature_spectrum'), ('singularity.solution-where-divergence-lies', 'claims/singularity.solution-where-divergence-lies', 'check.py::check_gauge_field_unimodular'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_radial_plane_is_hb_invariant'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_shape_operator_matches_gauge_curvature'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_shape_operator_spectrum'), ('singularity.non-removability-invariant-argument', 'claims/singularity.non-removability-invariant-argument', 'check.py::check_kretschmann_from_gauge_curvature'), ('singularity.non-removability-invariant-argument', 'claims/singularity.non-removability-invariant-argument', 'check.py::check_rotation_gauge_invariance'), ('singularity.degeneration-exactly', 'claims/singularity.degeneration-exactly', 'check.py::check_rescaled_map_limit_rank_one'), ('singularity.degeneration-exactly', 'claims/singularity.degeneration-exactly', 'check.py::check_rescaled_metric_limit_form'), ('singularity.degeneration-exactly', 'claims/singularity.degeneration-exactly', 'check.py::check_folded_direction_is_null_for_limit_form_only'), ('singularity.cones-fold', 'claims/singularity.cones-fold', 'check.py::check_null_directions_of_the_physical_cone'), ('singularity.cones-fold', 'claims/singularity.cones-fold', 'check.py::check_horizon_null_pair'), ('singularity.cones-fold', 'claims/singularity.cones-fold', 'check.py::check_cones_fold_onto_e_r'), ('singularity.cones-fold', 'claims/singularity.cones-fold', 'check.py::check_limit_direction_is_null_kernel_direction'), ('singularity.type-n-only-type-n', 'claims/singularity.type-n-only-type-n', 'check.py::check_no_type_c_and_quaternionic_matrix_form'), ('singularity.type-n-only-type-n', 'claims/singularity.type-n-only-type-n', 'check.py::check_type_n_at_the_singularity'), ('singularity.type-n-only-type-n', 'claims/singularity.type-n-only-type-n', 'check.py::check_type_p_present_and_self_repairing'), ('singularity.type-n-only-type-n', 'claims/singularity.type-n-only-type-n', 'check.py::check_tower_floors_have_no_type_c'), ('singularity.imported-one-sided-completion-singularity', 'claims/singularity.imported-one-sided-completion-singularity', 'check.py::check_completed_form_nondegenerate_no_shadow_wall'), ('singularity.imported-one-sided-completion-singularity', 'claims/singularity.imported-one-sided-completion-singularity', 'check.py::check_ladder_pair_exactly_over_boundary'), ('singularity.imported-one-sided-completion-singularity', 'claims/singularity.imported-one-sided-completion-singularity', 'check.py::check_dying_line_trivialised_by_rain_potential'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_classification_table'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_split_summands_isomorphic_and_simple'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_cotangent_subalgebra_is_degenerate_algebra'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_off_wall_complement_is_hyperbolic_plane'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_ladder_pair_exists_exactly_on_wall'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_signature_constant_on_physical_side'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_wrong_coupling_sign_fails'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_fibres_locally_free_and_physical_type'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_determinant_identity_and_no_shadow_wall'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_signature_two_four_on_the_whole_closure'), ('sheaf.one-sided-completion-singularity', 'claims/sheaf.one-sided-completion-singularity', 'check.py::check_ladder_pair_exactly_over_the_boundary'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_gram_matrix_of_the_cometric'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_nondegenerate_off_the_wall'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_corank_one_on_the_wall'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_first_order_degeneration'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_schwarzschild_frame_transition'), ('sheaf.schwarzschild-degeneration-boundary-tame', 'claims/sheaf.schwarzschild-degeneration-boundary-tame', 'check.py::check_rain_identity'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_blade_table'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_anticommute_iff_orthogonal'), ('std-algebra.sta-matrix', 'claims/std-algebra.sta-matrix', 'check.py::check_quaternionic_and_dirac_readings'), ('std-algebra.sta-matrix', 'claims/std-algebra.sta-matrix', 'check.py::check_spacetime_split'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_clock_and_centre_frozen'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_full_corner_is_ground'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_physical_tower_is_quaternionic'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_type_c_iff_p_minus_q_one_mod_four'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_eps_pm_identities_and_exchange'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_splitting_into_two_ideals'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_definite_forms_have_no_null_vectors'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_mixed_forms_have_a_null_cone_of_dimension_n_minus_one'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_null_vectors_are_non_invertible_zero_divisors')]

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
