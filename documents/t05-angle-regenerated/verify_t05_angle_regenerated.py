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
  "num:4.6"
 ],
 "verify_T05.py": [
  "num:7.16",
  "num:7.18",
  "num:7.2",
  "num:7.3"
 ]
}
CHECKS = [('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_boost_invariant_cyclic_separating_states'), ('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_marginal_is_gibbs_at_the_sample_point'), ('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_intertwining_automorphisms_act_through_sign'), ('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_surface_gravity_and_euclidean_period'), ('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_kms_relations_fix_each_mode_marginal'), ('angle.imported-singularity-papers-state-selection', 'claims/angle.imported-singularity-papers-state-selection', 'check.py::check_supplied_class_ultralocal_and_sea_level_occupancies'), ('angle.imported-conformal-model-null-rotations', 'claims/angle.imported-conformal-model-null-rotations', 'check.py::check_conformal_model'), ('angle.imported-conformal-model-null-rotations', 'claims/angle.imported-conformal-model-null-rotations', 'check.py::check_null_rotations_isomorphic_to_u'), ('angle.wedge-reflection-translations-are-ascent', 'claims/angle.wedge-reflection-translations-are-ascent', 'check.py::check_boost_rotor'), ('angle.wedge-reflection-translations-are-ascent', 'claims/angle.wedge-reflection-translations-are-ascent', 'check.py::check_imaginary_rapidity_is_the_wedge_reflection'), ('angle.wedge-reflection-translations-are-ascent', 'claims/angle.wedge-reflection-translations-are-ascent', 'check.py::check_null_rotations_translate_points_in_the_completion'), ('angle.within-supplied-class-spectrum-condition-selects', 'claims/angle.within-supplied-class-spectrum-condition-selects', 'check.py::check_unique_ground_state_is_a_product_number_state'), ('angle.within-supplied-class-spectrum-condition-selects', 'claims/angle.within-supplied-class-spectrum-condition-selects', 'check.py::check_degenerate_ground_space_selects_nothing'), ('angle.hop-across-cut', 'claims/angle.hop-across-cut', 'check.py::check_spectrum_and_unique_ground_state'), ('angle.hop-across-cut', 'claims/angle.hop-across-cut', 'check.py::check_generator_outside_supplied_class'), ('angle.hop-across-cut', 'claims/angle.hop-across-cut', 'check.py::check_parity_and_marginals'), ('angle.hop-across-cut', 'claims/angle.hop-across-cut', 'check.py::check_boost_eigenvector_statements'), ('angle.hop-sea-filled-pairing', 'claims/angle.hop-sea-filled-pairing', 'check.py::check_v_is_the_particle_hole_automorphism'), ('angle.hop-sea-filled-pairing', 'claims/angle.hop-sea-filled-pairing', 'check.py::check_image_state_and_pairing_generator'), ('angle.hop-sea-filled-pairing', 'claims/angle.hop-sea-filled-pairing', 'check.py::check_equal_frequency_boost_becomes_number_difference'), ('angle.value-parameter-dynamics', 'claims/angle.value-parameter-dynamics', 'check.py::check_ground_state_eigenvalue_and_marginal'), ('angle.value-parameter-dynamics', 'claims/angle.value-parameter-dynamics', 'check.py::check_gap_identities_and_sign_condition'), ('angle.value-parameter-dynamics', 'claims/angle.value-parameter-dynamics', 'check.py::check_gibbs_parameter_fixed_by_ratio_and_sign_of_t'), ('singularity.class-relative-no-go-no-supplied', 'claims/singularity.class-relative-no-go-no-supplied', 'check.py::check_supplied_generators_commute_with_every_occupation'), ('singularity.class-relative-no-go-no-supplied', 'claims/singularity.class-relative-no-go-no-supplied', 'check.py::check_pairing_generators_lie_outside_the_class'), ('singularity.computed', 'claims/singularity.computed', 'check.py::check_killing_field_and_its_norm'), ('singularity.computed', 'claims/singularity.computed', 'check.py::check_redshifted_acceleration_of_static_observers'), ('singularity.computed', 'claims/singularity.computed', 'check.py::check_surface_gravity_on_the_horizon_locus'), ('singularity.euclidean-section-period', 'claims/singularity.euclidean-section-period', 'check.py::check_wick_rotated_derived_metric'), ('singularity.euclidean-section-period', 'claims/singularity.euclidean-section-period', 'check.py::check_slope_is_half_f_prime'), ('singularity.euclidean-section-period', 'claims/singularity.euclidean-section-period', 'check.py::check_tip_expansion'), ('singularity.euclidean-section-period', 'claims/singularity.euclidean-section-period', 'check.py::check_regular_tip_iff_period_eight_pi_m'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_invariant_cyclic_state_descends_to_kms_beta_free'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_hawking_temperature_and_fermi_dirac'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_hypotheses_sufficient_not_necessary'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_commuting_automorphisms_fix_gibbs'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_reversing_automorphisms_flip_beta'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_reparametrisation_rescales_beta'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_only_orientation_flip_intertwines'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_invariance_forces_one_eigenspace'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_cyclic_separating_only_on_the_number_basis'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_phase_convention_gives_cos_sin'), ('transport.group-null-rotations', 'claims/transport.group-null-rotations', 'check.py::check_group_law_and_injectivity'), ('transport.group-null-rotations', 'claims/transport.group-null-rotations', 'check.py::check_null_rotations_are_rotors_fixing_v'), ('transport.group-null-rotations', 'claims/transport.group-null-rotations', 'check.py::check_levi_equivariance'), ('transport.totality', 'claims/transport.totality', 'check.py::check_iota_well_defined_total_involution'), ('transport.totality', 'claims/transport.totality', 'check.py::check_reciprocal_on_invertible_vectors'), ('transport.totality', 'claims/transport.totality', 'check.py::check_null_points_go_to_ideal_points_continuously')]

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
