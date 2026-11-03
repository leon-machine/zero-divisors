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
  "num:10.4",
  "num:10.6",
  "num:11.4",
  "num:11.5",
  "num:11.6",
  "num:11.7",
  "num:12.3",
  "num:7.21",
  "num:9.3"
 ],
 "verify_T08.py": [
  "label:asm:spreading",
  "label:cor:holographic",
  "label:lem:inventory",
  "label:prop:arealaw",
  "label:prop:volume",
  "label:thm:count",
  "label:thm:epoch",
  "num:4.12",
  "num:4.4"
 ]
}
CHECKS = [('scrambling.mode-count', 'claims/scrambling.mode-count', 'check.py::check_mode_count_placement'), ('scrambling.area-law-test', 'claims/scrambling.area-law-test', 'check.py::check_area_law_iff_half_mass'), ('scrambling.area-law-test', 'claims/scrambling.area-law-test', 'check.py::check_causal_epoch_order_m'), ('scrambling.area-law-test', 'claims/scrambling.area-law-test', 'check.py::check_lifetime_scaling'), ('scrambling.epoch-modular-period-two-unknowns-become', 'claims/scrambling.epoch-modular-period-two-unknowns-become', 'check.py::check_epoch_is_the_modular_period'), ('scrambling.epoch-modular-period-two-unknowns-become', 'claims/scrambling.epoch-modular-period-two-unknowns-become', 'check.py::check_density_prediction_both_directions'), ('scrambling.spreading-law-chaos-bound-saturated', 'claims/scrambling.spreading-law-chaos-bound-saturated', 'check.py::check_boost_flow_scales_ladders_exponentially'), ('scrambling.spreading-law-chaos-bound-saturated', 'claims/scrambling.spreading-law-chaos-bound-saturated', 'check.py::check_spreading_threshold_is_log_n'), ('scrambling.spreading-law-chaos-bound-saturated', 'claims/scrambling.spreading-law-chaos-bound-saturated', 'check.py::check_rate_is_modular_rate'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_pinching_structure'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_key_lemma_moment_form'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_entropy_identity_exact'), ('singularity.eviction-window-thermal-product-radiation-entropy', 'claims/singularity.eviction-window-thermal-product-radiation-entropy', 'check.py::check_window_is_thermal_product'), ('singularity.eviction-window-thermal-product-radiation-entropy', 'claims/singularity.eviction-window-thermal-product-radiation-entropy', 'check.py::check_envelope_endpoint_and_rising_branch'), ('singularity.eviction-window-thermal-product-radiation-entropy', 'claims/singularity.eviction-window-thermal-product-radiation-entropy', 'check.py::check_falling_branch_and_idealisation'), ('singularity.envelope-endpoint-why-boundary-mode-locality', 'claims/singularity.envelope-endpoint-why-boundary-mode-locality', 'check.py::check_envelope_and_endpoint_under_diagonal_dynamics'), ('singularity.envelope-endpoint-why-boundary-mode-locality', 'claims/singularity.envelope-endpoint-why-boundary-mode-locality', 'check.py::check_locality_premise_is_necessary'), ('singularity.what-event-returns-radiation', 'claims/singularity.what-event-returns-radiation', 'check.py::check_block_entropy_and_returned_information'), ('singularity.what-event-returns-radiation', 'claims/singularity.what-event-returns-radiation', 'check.py::check_evicted_qubit_correlated_with_radiation_not_partner'), ('singularity.what-event-returns-radiation', 'claims/singularity.what-event-returns-radiation', 'check.py::check_idealisation_returns_two_ln_two'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_intrinsic_flows_are_bivector_flows'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_single_pair_is_the_boost'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_inventory_by_clock_criterion'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_pairing_trichotomy'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_rotated_modes_atom_boosts_and_so_nn'), ('scrambling.clock-inventory-boundary-modes', 'claims/scrambling.clock-inventory-boundary-modes', 'check.py::check_witt_eigenspaces_isotropic_and_dual'), ('scrambling.imported-modes-modular-inventory', 'claims/scrambling.imported-modes-modular-inventory', 'check.py::check_boost_bivector_weights_and_spectral_projectors'), ('scrambling.imported-modes-modular-inventory', 'claims/scrambling.imported-modes-modular-inventory', 'check.py::check_unique_flow_up_to_reparametrisation'), ('scrambling.imported-modes-modular-inventory', 'claims/scrambling.imported-modes-modular-inventory', 'check.py::check_surface_gravity_normalisation'), ('scrambling.imported-modes-modular-inventory', 'claims/scrambling.imported-modes-modular-inventory', 'check.py::check_euclidean_continuation_period_and_reality'), ('scrambling.integer-holographic-form-identification', 'claims/scrambling.integer-holographic-form-identification', 'check.py::check_epoch_volume_is_beta_squared'), ('scrambling.integer-holographic-form-identification', 'claims/scrambling.integer-holographic-form-identification', 'check.py::check_density_iff_integer_count'), ('scrambling.integer-holographic-form-identification', 'claims/scrambling.integer-holographic-form-identification', 'check.py::check_naive_overshoot_is_area_coefficient'), ('scrambling.residue-each-convention', 'claims/scrambling.residue-each-convention', 'check.py::check_residues_in_both_conventions'), ('scrambling.residue-each-convention', 'claims/scrambling.residue-each-convention', 'check.py::check_conventions_differ_by_ln2'), ('scrambling.residue-each-convention', 'claims/scrambling.residue-each-convention', 'check.py::check_one_helicity_per_mode'), ('scrambling.slice-volume-exactly-per-unit-killing', 'claims/scrambling.slice-volume-exactly-per-unit-killing', 'check.py::check_induced_slice_geometry_and_volume'), ('scrambling.slice-volume-exactly-per-unit-killing', 'claims/scrambling.slice-volume-exactly-per-unit-killing', 'check.py::check_cutoff_gives_exactly_eight_pi_m'), ('singularity.causal-epoch-computed-exactly', 'claims/singularity.causal-epoch-computed-exactly', 'check.py::check_integrand_partial_fractions_antiderivative'), ('singularity.causal-epoch-computed-exactly', 'claims/singularity.causal-epoch-computed-exactly', 'check.py::check_closed_form_inside_riemann_bracket'), ('singularity.causal-epoch-computed-exactly', 'claims/singularity.causal-epoch-computed-exactly', 'check.py::check_expansion_remainder_and_energy_independence'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_complexified_rotor_period_four_pi'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_module_form_and_conjugation_period'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_euclidean_rotation_is_no_real_rotor'), ('singularity.no-attic-derived-model', 'claims/singularity.no-attic-derived-model', 'check.py::check_two_sectors_exhaust_the_qubits'), ('singularity.no-attic-derived-model', 'claims/singularity.no-attic-derived-model', 'check.py::check_sector_spectra_agree'), ('singularity.no-attic-derived-model', 'claims/singularity.no-attic-derived-model', 'check.py::check_evicted_correlations_stay_in_the_sectors'), ('singularity.purity-correlation-transfer-recovery', 'claims/singularity.purity-correlation-transfer-recovery', 'check.py::check_global_purity_and_pure_radiation_at_completion'), ('singularity.purity-correlation-transfer-recovery', 'claims/singularity.purity-correlation-transfer-recovery', 'check.py::check_pair_coherence_damped_by_visibility'), ('singularity.purity-correlation-transfer-recovery', 'claims/singularity.purity-correlation-transfer-recovery', 'check.py::check_correlators_carry_the_gate_pattern'), ('singularity.stretched-singularity-count', 'claims/singularity.stretched-singularity-count', 'check.py::check_induced_metric_on_the_slice'), ('singularity.stretched-singularity-count', 'claims/singularity.stretched-singularity-count', 'check.py::check_slice_volume_identities'), ('singularity.stretched-singularity-count', 'claims/singularity.stretched-singularity-count', 'check.py::check_mode_rate_keeps_hawking_time'), ('singularity.stretched-singularity-count', 'claims/singularity.stretched-singularity-count', 'check.py::check_fixed_cutoff_radius_fails')]

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
