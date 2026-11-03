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
 "verify_T09.py": [
  "label:thm:incidence"
 ],
 "verify_T11.py": [
  "label:cor:series",
  "label:fact:chart",
  "label:fact:frozen",
  "label:lem:chartiso",
  "label:lem:dsscale",
  "label:lem:five",
  "label:prop:area",
  "label:prop:weight",
  "label:thm:dictionary",
  "label:thm:grip"
 ],
 "verify_T12.py": [
  "label:prop:singlet",
  "label:thm:global"
 ]
}
CHECKS = [('mass.de-sitter-scale-frozen-point', 'claims/mass.de-sitter-scale-frozen-point', 'check.py::check_scale_tractor_parallel_with_norm'), ('mass.de-sitter-scale-frozen-point', 'claims/mass.de-sitter-scale-frozen-point', 'check.py::check_gauge_field_sigma_is_de_sitter'), ('mass.de-sitter-scale-frozen-point', 'claims/mass.de-sitter-scale-frozen-point', 'check.py::check_frozen_point_unique_constant_vector'), ('mass.de-sitter-scale-frozen-point', 'claims/mass.de-sitter-scale-frozen-point', 'check.py::check_frozen_point_norm_and_null_limit'), ('mass.mass-symplectic-area-two-twistor-formula', 'claims/mass.mass-symplectic-area-two-twistor-formula', 'check.py::check_single_spinor_is_null'), ('mass.mass-symplectic-area-two-twistor-formula', 'claims/mass.mass-symplectic-area-two-twistor-formula', 'check.py::check_two_spinor_mass_is_symplectic_area'), ('mass.mass-symplectic-area-two-twistor-formula', 'claims/mass.mass-symplectic-area-two-twistor-formula', 'check.py::check_aligned_null_and_mass_grows_with_misalignment'), ('mass.five-broken-generators', 'claims/mass.five-broken-generators', 'check.py::check_omega_nondegenerate_iff_non_null'), ('mass.five-broken-generators', 'claims/mass.five-broken-generators', 'check.py::check_stabiliser_ten_complement_five'), ('mass.five-broken-generators', 'claims/mass.five-broken-generators', 'check.py::check_real_form_de_sitter_and_anti_de_sitter'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_deformed_bracket_is_pairing_with_frozen_point'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_mass_is_grip_norm_identity_in_lambda'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_flat_shadow_is_symplectic_area'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_point_supported_composite'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_massless_locus'), ('mass.mass-weight-dictionary', 'claims/mass.mass-weight-dictionary', 'check.py::check_mass_is_minus_w_w_plus_n_minus_one_times_norm'), ('mass.mass-weight-dictionary', 'claims/mass.mass-weight-dictionary', 'check.py::check_four_dimensions_in_lambda_and_frozen_point'), ('mass.weight-polynomial-two-series', 'claims/mass.weight-polynomial-two-series', 'check.py::check_massless_pair_and_shadow_symmetry'), ('mass.weight-polynomial-two-series', 'claims/mass.weight-polynomial-two-series', 'check.py::check_conformally_coupled_weight'), ('mass.weight-polynomial-two-series', 'claims/mass.weight-polynomial-two-series', 'check.py::check_real_weights_complementary_series'), ('mass.weight-polynomial-two-series', 'claims/mass.weight-polynomial-two-series', 'check.py::check_principal_series_and_expansion'), ('mass.weight-composite', 'claims/mass.weight-composite', 'check.py::check_induced_weight_principal_series'), ('mass.weight-composite', 'claims/mass.weight-composite', 'check.py::check_real_weight_exactly_below_threshold'), ('mass.weight-composite', 'claims/mass.weight-composite', 'check.py::check_leading_order_im_w'), ('standard-model.mass-bracket-charged-singlet', 'claims/standard-model.mass-bracket-charged-singlet', 'check.py::check_bracket_transforms_by_determinant'), ('standard-model.mass-bracket-charged-singlet', 'claims/standard-model.mass-bracket-charged-singlet', 'check.py::check_modulus_is_mass_phase_is_gauge'), ('standard-model.mass-bracket-charged-singlet', 'claims/standard-model.mass-bracket-charged-singlet', 'check.py::check_hypercharge_weight_six_singlet'), ('correspondence.incidence-relation-chart', 'claims/correspondence.incidence-relation-chart', 'check.py::check_expansion_and_chart'), ('correspondence.incidence-relation-chart', 'claims/correspondence.incidence-relation-chart', 'check.py::check_coverage_of_the_affine_chart'), ('correspondence.incidence-relation-chart', 'claims/correspondence.incidence-relation-chart', 'check.py::check_consequences_incidence_and_stabilisers'), ('mass.chart-form-spin-isomorphism', 'claims/mass.chart-form-spin-isomorphism', 'check.py::check_grading_element'), ('mass.chart-form-spin-isomorphism', 'claims/mass.chart-form-spin-isomorphism', 'check.py::check_translations_block'), ('mass.chart-form-spin-isomorphism', 'claims/mass.chart-form-spin-isomorphism', 'check.py::check_special_conformal_block'), ('mass.imported-flat-model-twistor-chart-infinity', 'claims/mass.imported-flat-model-twistor-chart-infinity', 'check.py::check_null_embedding_and_forced_coefficient'), ('mass.imported-flat-model-twistor-chart-infinity', 'claims/mass.imported-flat-model-twistor-chart-infinity', 'check.py::check_simple_iff_null_and_planes'), ('mass.imported-flat-model-twistor-chart-infinity', 'claims/mass.imported-flat-model-twistor-chart-infinity', 'check.py::check_scale_function_is_sigma_slot'), ('mass.imported-flat-model-twistor-chart-infinity', 'claims/mass.imported-flat-model-twistor-chart-infinity', 'check.py::check_sl_action_is_isomorphism_onto_so'), ('mass.imported-flat-model-twistor-chart-infinity', 'claims/mass.imported-flat-model-twistor-chart-infinity', 'check.py::check_infinity_bivector_simple_iff_flat'), ('mass.imported-frozen-point-tractor-connection', 'claims/mass.imported-frozen-point-tractor-connection', 'check.py::check_displayed_connection_slots'), ('mass.imported-frozen-point-tractor-connection', 'claims/mass.imported-frozen-point-tractor-connection', 'check.py::check_frozen_point_parallel_with_rho_j_over_n'), ('mass.imported-frozen-point-tractor-connection', 'claims/mass.imported-frozen-point-tractor-connection', 'check.py::check_stabiliser_de_sitter_group_and_sign'), ('mass.imported-frozen-point-tractor-connection', 'claims/mass.imported-frozen-point-tractor-connection', 'check.py::check_general_n_rho_is_j_over_n'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_kernel_and_coset_rescaling'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_z6_kernel_exactly'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_su5_splitting_subgroup'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_charge_lattice'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_fock_module_irreducible_with_two_halves'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_each_conformal_spinor_is_a_fock_vacuum'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_excitations_from_a_dual_complement_span_the_module')]

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
