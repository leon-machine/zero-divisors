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
 "verify_BOS.py": [
  "id:E0",
  "id:E1",
  "id:E2.0",
  "id:E2.1",
  "id:E2.1c",
  "id:E2.2",
  "id:E2.3",
  "id:E2.4",
  "id:E3",
  "id:E3b",
  "id:E3c",
  "id:E3g",
  "id:E4",
  "id:S1.1",
  "id:S1.2",
  "id:S1.3",
  "id:S2.1",
  "id:S2.2",
  "id:S2.3",
  "id:S2.4",
  "id:S2.5",
  "id:S3",
  "id:V2"
 ],
 "verify_GA2Q.py": [
  "id:Q1.0",
  "id:Q1.1",
  "id:Q1.2",
  "id:Q2.1",
  "id:Q2.2",
  "id:Q2.3",
  "id:Q3.1",
  "id:Q3.2",
  "id:Q3.3",
  "id:Q3.4",
  "id:Q4.1",
  "id:Q5",
  "id:Q6.1",
  "id:Q6.2",
  "id:Q6.3",
  "id:Q6.4",
  "id:Q7"
 ],
 "verify_GRV.py": [
  "id:G2",
  "id:G3",
  "id:G3b",
  "id:G4",
  "id:G4c",
  "id:G4m",
  "id:G4q",
  "id:G5",
  "id:G5c",
  "id:G6"
 ],
 "verify_INT.py": [
  "id:B1",
  "id:C1.1",
  "id:C1.2",
  "id:C1.3",
  "id:C1.4",
  "id:C2.1",
  "id:C2.2",
  "id:C2.3",
  "id:C2.4",
  "id:C3",
  "id:C3b",
  "id:M1.1",
  "id:M1.2",
  "id:M1.3",
  "id:M1.4",
  "id:M1.5",
  "id:M2.0",
  "id:M2.1",
  "id:M2.2",
  "id:M2.3"
 ],
 "verify_PHO.py": [
  "id:C1",
  "id:C1q",
  "id:C2",
  "id:C2c",
  "id:C3",
  "id:C3h",
  "id:C4",
  "id:C4c",
  "id:F1.1",
  "id:F1.2",
  "id:M1",
  "id:M2a",
  "id:M2b",
  "id:M2c",
  "id:M2d",
  "id:M2e",
  "id:M3.1",
  "id:M3.2",
  "id:T1",
  "id:T2",
  "id:T3"
 ],
 "verify_QFT.py": [
  "id:A1.1",
  "id:A1.2",
  "id:A1.3",
  "id:A1.4",
  "id:A1.5",
  "id:A1.6",
  "id:A1.7",
  "id:A1.8",
  "id:A4.4",
  "id:A4.5",
  "id:A4.6",
  "id:A5.1",
  "id:A5.2",
  "id:A5.3",
  "id:A5.4",
  "id:A5.5",
  "id:B1.0",
  "id:B1.1",
  "id:B1.2",
  "id:B1.3",
  "id:B1.4",
  "id:B1.5",
  "id:B1.6",
  "id:B1.7",
  "id:B1.8",
  "id:B2.1",
  "id:D1.1",
  "id:D2.1",
  "id:D2.2",
  "id:D2.3",
  "id:D2.4",
  "id:D2.5",
  "id:D2.6",
  "id:D2.7",
  "id:D2.8",
  "id:D3.1",
  "id:D3.2",
  "id:D3.3",
  "id:D4.1",
  "id:D4.2",
  "id:D4.3",
  "id:D4.4"
 ],
 "verify_SMC.py": [
  "id:C3",
  "id:C4",
  "id:C6a",
  "id:C6b",
  "id:C6c",
  "id:C6d",
  "id:C6e"
 ],
 "verify_T03.py": [
  "num:3.1",
  "num:3.2"
 ],
 "verify_T09.py": [
  "label:lem:weyl"
 ],
 "verify_T12.py": [
  "label:prop:content",
  "label:thm:hypercharge"
 ],
 "verify_TWGA.py": [
  "id:E1.1",
  "id:E1.2a",
  "id:E1.2b",
  "id:E1.3a",
  "id:E1.3b",
  "id:E1.3c",
  "id:E1.3d",
  "id:E1.4a",
  "id:E1.4b",
  "id:E1.4c",
  "id:E1.4d",
  "id:E1.4e",
  "id:E1.5a",
  "id:E1.5b",
  "id:E1.5c",
  "id:E1.5d",
  "id:E1.5e",
  "id:E1.6a",
  "id:E1.6b",
  "id:E1.6c",
  "id:E1.6d",
  "id:E1.7a",
  "id:E1.7b",
  "id:E1.7c",
  "id:E1.7d",
  "id:E3.1a",
  "id:E3.1b",
  "id:E3.1c",
  "id:E3.2a",
  "id:E3.2b",
  "id:E3.2c",
  "id:E3.2d",
  "id:E3.2e",
  "id:E3.2f"
 ]
}
CHECKS = [('field-theory.imported-tower-limit', 'claims/field-theory.imported-tower-limit', 'check.py::check_planes_generate_car'), ('field-theory.imported-tower-limit', 'claims/field-theory.imported-tower-limit', 'check.py::check_rungs_are_full_matrix_algebras'), ('field-theory.imported-statistics-no-go-palatial-algebra', 'claims/field-theory.imported-statistics-no-go-palatial-algebra', 'check.py::check_no_finite_dimensional_representation'), ('field-theory.imported-statistics-no-go-palatial-algebra', 'claims/field-theory.imported-statistics-no-go-palatial-algebra', 'check.py::check_polynomial_realisation'), ('field-theory.imported-one-datum-massive-law', 'claims/field-theory.imported-one-datum-massive-law', 'check.py::check_pseudoscalar_excluded_and_commutant_four_dimensional'), ('field-theory.imported-one-datum-massive-law', 'claims/field-theory.imported-one-datum-massive-law', 'check.py::check_complex_structures_form_hyperboloid'), ('field-theory.imported-one-datum-massive-law', 'claims/field-theory.imported-one-datum-massive-law', 'check.py::check_imaginary_unit_and_rest_frame_one_choice'), ('field-theory.ground-does-not-attach-modes', 'claims/field-theory.ground-does-not-attach-modes', 'check.py::check_even_ground_commutes_with_modes'), ('field-theory.ground-does-not-attach-modes', 'claims/field-theory.ground-does-not-attach-modes', 'check.py::check_translations_and_lorentz_rotors_act_trivially'), ('field-theory.ground-does-not-attach-modes', 'claims/field-theory.ground-does-not-attach-modes', 'check.py::check_covariance_forces_constant_mode_functions'), ('field-theory.twistor-attachment', 'claims/field-theory.twistor-attachment', 'check.py::check_oscillator_module_spectrum_and_twistor_form'), ('field-theory.twistor-attachment', 'claims/field-theory.twistor-attachment', 'check.py::check_u22_preserves_positive_energy_helicity_modules'), ('field-theory.twistor-attachment', 'claims/field-theory.twistor-attachment', 'check.py::check_kernels_exchange_parity_is_spin_statistics'), ('field-theory.boost-modes', 'claims/field-theory.boost-modes', 'check.py::check_real_rapidity_is_not_a_star_map'), ('field-theory.boost-modes', 'claims/field-theory.boost-modes', 'check.py::check_uniform_real_boost_unbounded'), ('field-theory.boost-modes', 'claims/field-theory.boost-modes', 'check.py::check_imaginary_rapidity_is_unitary_phase'), ('field-theory.path-integral-inside-tower', 'claims/field-theory.path-integral-inside-tower', 'check.py::check_grassmann_variables_are_rungs'), ('field-theory.path-integral-inside-tower', 'claims/field-theory.path-integral-inside-tower', 'check.py::check_exact_slicing_is_trace'), ('field-theory.path-integral-inside-tower', 'claims/field-theory.path-integral-inside-tower', 'check.py::check_continuum_limit_gibbs_and_fermi_dirac'), ('field-theory.path-integral-inside-tower', 'claims/field-theory.path-integral-inside-tower', 'check.py::check_two_point_function_matsubara'), ('field-theory.where-each-lives', 'claims/field-theory.where-each-lives', 'check.py::check_centres_and_I6'), ('field-theory.where-each-lives', 'claims/field-theory.where-each-lives', 'check.py::check_conformal_spinor_ideal_and_commutant'), ('field-theory.where-each-lives', 'claims/field-theory.where-each-lives', 'check.py::check_two_chiral_doublets'), ('field-theory.where-each-lives', 'claims/field-theory.where-each-lives', 'check.py::check_massless_complex_structure_is_pseudoscalar'), ('field-theory.second-quantisation', 'claims/field-theory.second-quantisation', 'check.py::check_lambda_is_orthogonal_projector_onto_ker_k'), ('field-theory.second-quantisation', 'claims/field-theory.second-quantisation', 'check.py::check_field_anticommutator_is_local_kernel'), ('field-theory.second-quantisation', 'claims/field-theory.second-quantisation', 'check.py::check_bilinears_are_second_quantised_operators'), ('field-theory.second-quantisation', 'claims/field-theory.second-quantisation', 'check.py::check_mixed_chirality_split_forced_by_i_equals_I4'), ('field-theory.mass', 'claims/field-theory.mass', 'check.py::check_pairing_on_one_chirality'), ('field-theory.mass', 'claims/field-theory.mass', 'check.py::check_charge_two_under_common_phase'), ('field-theory.mass', 'claims/field-theory.mass', 'check.py::check_massive_plane_wave_couples_opposite_charges'), ('field-theory.mass', 'claims/field-theory.mass', 'check.py::check_pseudoscalar_is_not_the_massive_complex_structure'), ('field-theory.contact-interactions-tower', 'claims/field-theory.contact-interactions-tower', 'check.py::check_contact_term_structure'), ('field-theory.contact-interactions-tower', 'claims/field-theory.contact-interactions-tower', 'check.py::check_matrix_element_and_s_squared_law'), ('field-theory.contact-interactions-tower', 'claims/field-theory.contact-interactions-tower', 'check.py::check_crossed_amplitude_u_squared_law'), ('field-theory.contact-interactions-tower', 'claims/field-theory.contact-interactions-tower', 'check.py::check_boosted_frames'), ('field-theory.no-canonical-commutation-relations-tower', 'claims/field-theory.no-canonical-commutation-relations-tower', 'check.py::check_scalar_part_is_a_trace_on_every_floor'), ('field-theory.no-canonical-commutation-relations-tower', 'claims/field-theory.no-canonical-commutation-relations-tower', 'check.py::check_matrix_trace_kills_commutators'), ('field-theory.no-canonical-commutation-relations-tower', 'claims/field-theory.no-canonical-commutation-relations-tower', 'check.py::check_composite_pair_is_not_excluded'), ('field-theory.composite-scalars-mean-field-level', 'claims/field-theory.composite-scalars-mean-field-level', 'check.py::check_block_spectrum_and_dispersion'), ('field-theory.composite-scalars-mean-field-level', 'claims/field-theory.composite-scalars-mean-field-level', 'check.py::check_pairing_tower_threshold'), ('field-theory.composite-scalars-mean-field-level', 'claims/field-theory.composite-scalars-mean-field-level', 'check.py::check_gap_equation'), ('field-theory.composite-scalars-mean-field-level', 'claims/field-theory.composite-scalars-mean-field-level', 'check.py::check_axial_phase_flat_direction'), ('field-theory.composite-gauge-bosons-what-excluded', 'claims/field-theory.composite-gauge-bosons-what-excluded', 'check.py::check_current_transforms_as_a_vector'), ('field-theory.composite-gauge-bosons-what-excluded', 'claims/field-theory.composite-gauge-bosons-what-excluded', 'check.py::check_vector_condensate_breaks_lorentz'), ('field-theory.elementary-photon-ga', 'claims/field-theory.elementary-photon-ga', 'check.py::check_kinematics_and_conservation'), ('field-theory.elementary-photon-ga', 'claims/field-theory.elementary-photon-ga', 'check.py::check_helicity_eigen_relation'), ('field-theory.elementary-photon-ga', 'claims/field-theory.elementary-photon-ga', 'check.py::check_sesquilinear_and_helicity_sum'), ('field-theory.elementary-photon-ga', 'claims/field-theory.elementary-photon-ga', 'check.py::check_coulomb_gauge_equals_covariant'), ('field-theory.elementary-photon-ga', 'claims/field-theory.elementary-photon-ga', 'check.py::check_massive_vector_contact_limit'), ('field-theory.fock-space-maxwell-modes', 'claims/field-theory.fock-space-maxwell-modes', 'check.py::check_bargmann_fock_ccr_and_adjoint'), ('field-theory.fock-space-maxwell-modes', 'claims/field-theory.fock-space-maxwell-modes', 'check.py::check_one_complex_mode_per_null_momentum'), ('field-theory.fock-space-maxwell-modes', 'claims/field-theory.fock-space-maxwell-modes', 'check.py::check_positive_frequency_is_positive_helicity'), ('field-theory.fock-space-maxwell-modes', 'claims/field-theory.fock-space-maxwell-modes', 'check.py::check_riemann_silberstein_field'), ('field-theory.coupled-system-tree-level', 'claims/field-theory.coupled-system-tree-level', 'check.py::check_vertex_self_adjoint_and_charge_conserving'), ('field-theory.coupled-system-tree-level', 'claims/field-theory.coupled-system-tree-level', 'check.py::check_second_order_amplitude_distinguishable'), ('field-theory.coupled-system-tree-level', 'claims/field-theory.coupled-system-tree-level', 'check.py::check_coulomb_term_and_both_helicities_needed'), ('field-theory.coupled-system-tree-level', 'claims/field-theory.coupled-system-tree-level', 'check.py::check_ga_product_vertex_same_amplitude'), ('field-theory.coupled-system-tree-level', 'claims/field-theory.coupled-system-tree-level', 'check.py::check_identical_fermions_exchange_sign'), ('field-theory.how-close-tower-comes-ccr', 'claims/field-theory.how-close-tower-comes-ccr', 'check.py::check_commutator_is_n_minus_number'), ('field-theory.how-close-tower-comes-ccr', 'claims/field-theory.how-close-tower-comes-ccr', 'check.py::check_quasi_spin_su2'), ('field-theory.how-close-tower-comes-ccr', 'claims/field-theory.how-close-tower-comes-ccr', 'check.py::check_finite_ladder'), ('field-theory.conserved-numbers-mass-block', 'claims/field-theory.conserved-numbers-mass-block', 'check.py::check_quasiparticles_diagonalise_the_block'), ('field-theory.conserved-numbers-mass-block', 'claims/field-theory.conserved-numbers-mass-block', 'check.py::check_rung_numbers_not_conserved_massive_vacuum'), ('field-theory.conserved-numbers-mass-block', 'claims/field-theory.conserved-numbers-mass-block', 'check.py::check_charge_in_rung_algebra'), ('field-theory.operator-newtonian-coupling', 'claims/field-theory.operator-newtonian-coupling', 'check.py::check_operator_coupling_gives_registered_phase'), ('field-theory.operator-newtonian-coupling', 'claims/field-theory.operator-newtonian-coupling', 'check.py::check_no_self_interaction_unlike_mean_field'), ('field-theory.operator-newtonian-coupling', 'claims/field-theory.operator-newtonian-coupling', 'check.py::check_massive_sources_quasi_particles_and_block_charges'), ('field-theory.operator-newtonian-coupling', 'claims/field-theory.operator-newtonian-coupling', 'check.py::check_rigid_composites_monopole_plus_a_squared'), ('field-theory.assignments-survive', 'claims/field-theory.assignments-survive', 'check.py::check_listing_and_conjugate_anomaly_free'), ('field-theory.assignments-survive', 'claims/field-theory.assignments-survive', 'check.py::check_exactly_four_patterns'), ('field-theory.assignments-survive', 'claims/field-theory.assignments-survive', 'check.py::check_conjugate_representations_with_i4'), ('field-theory.orientation-relocated', 'claims/field-theory.orientation-relocated', 'check.py::check_e_plus_maps_halves_and_swaps_doublets'), ('field-theory.orientation-relocated', 'claims/field-theory.orientation-relocated', 'check.py::check_unit_J_distinguishes_halves'), ('field-theory.orientation-relocated', 'claims/field-theory.orientation-relocated', 'check.py::check_sign_of_unit_relocates_orientation'), ('correspondence.statistics-no-go', 'claims/correspondence.statistics-no-go', 'check.py::check_trace_argument_in_finite_dimensions'), ('correspondence.statistics-no-go', 'claims/correspondence.statistics-no-go', 'check.py::check_cl24_commutators_have_no_scalar_part'), ('correspondence.statistics-no-go', 'claims/correspondence.statistics-no-go', 'check.py::check_ladder_pairs_satisfy_car_in_cl24'), ('correspondence.symmetrised-quadratics-palatial-algebra', 'claims/correspondence.symmetrised-quadratics-palatial-algebra', 'check.py::check_adjoint_action_on_generators'), ('correspondence.symmetrised-quadratics-palatial-algebra', 'claims/correspondence.symmetrised-quadratics-palatial-algebra', 'check.py::check_lie_homomorphism_and_injective'), ('correspondence.symmetrised-quadratics-palatial-algebra', 'claims/correspondence.symmetrised-quadratics-palatial-algebra', 'check.py::check_symmetric_minus_normal_is_half_trace'), ('one-relation.one-datum-not-two-imaginary-unit', 'claims/one-relation.one-datum-not-two-imaginary-unit', 'check.py::check_commutant_of_c'), ('one-relation.one-datum-not-two-imaginary-unit', 'claims/one-relation.one-datum-not-two-imaginary-unit', 'check.py::check_complex_structures_are_a_two_sheeted_hyperboloid'), ('one-relation.one-datum-not-two-imaginary-unit', 'claims/one-relation.one-datum-not-two-imaginary-unit', 'check.py::check_j_to_gamma0_bijection'), ('one-relation.one-datum-not-two-imaginary-unit', 'claims/one-relation.one-datum-not-two-imaginary-unit', 'check.py::check_joint_commutant_is_the_spin_plane_u1'), ('one-relation.one-datum-not-two-imaginary-unit', 'claims/one-relation.one-datum-not-two-imaginary-unit', 'check.py::check_alignment_and_ideal_picture'), ('standard-model.hypercharge-global-form-pair-counting-consistency', 'claims/standard-model.hypercharge-global-form-pair-counting-consistency', 'check.py::check_orientation_fixed_by_anomaly'), ('standard-model.hypercharge-global-form-pair-counting-consistency', 'claims/standard-model.hypercharge-global-form-pair-counting-consistency', 'check.py::check_one_handed_singlet_spectrum'), ('standard-model.hypercharge-global-form-pair-counting-consistency', 'claims/standard-model.hypercharge-global-form-pair-counting-consistency', 'check.py::check_anomaly_free_and_unique'), ('standard-model.hypercharge-global-form-pair-counting-consistency', 'claims/standard-model.hypercharge-global-form-pair-counting-consistency', 'check.py::check_hypotheses_necessary'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_cells_are_quark_doublet'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_doublets_under_s'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_no_doublet_without_s'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_single_spinor_sector'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_tower_vectors_satisfy_the_car'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_fock_adjointness'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_ground_factor_commutes_and_correctors_unitary'), ('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_twisted_ground_copy'), ('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_plane_algebra_is_full_matrix_algebra'), ('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_commuting_copies_tensor_isomorphism'), ('tower.volume-elements-planes', 'claims/tower.volume-elements-planes', 'check.py::check_plane_volume_elements'), ('tower.volume-elements-planes', 'claims/tower.volume-elements-planes', 'check.py::check_product_omega_k')]

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
