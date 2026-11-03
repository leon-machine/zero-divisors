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
  "num:5.5",
  "num:5.7",
  "num:6.1",
  "num:6.2",
  "num:7.1",
  "num:7.10",
  "num:7.13",
  "num:7.15",
  "num:7.16",
  "num:7.21",
  "num:7.28",
  "num:7.31",
  "num:7.6",
  "num:9.3",
  "num:9.4"
 ],
 "verify_state_selection.py": [
  "num:5.2",
  "num:7.1"
 ]
}
CHECKS = [('state-selection.euclidean-partner-curvature-selected', 'claims/state-selection.euclidean-partner-curvature-selected', 'check.py::check_pair_is_doubled_eigenplane'), ('state-selection.euclidean-partner-curvature-selected', 'claims/state-selection.euclidean-partner-curvature-selected', 'check.py::check_elliptic_rotor_periods'), ('state-selection.euclidean-partner-curvature-selected', 'claims/state-selection.euclidean-partner-curvature-selected', 'check.py::check_hyperbolic_and_elliptic_flows_share_the_pair'), ('state-selection.euclidean-partner-curvature-selected', 'claims/state-selection.euclidean-partner-curvature-selected', 'check.py::check_chiral_halves_carry_r_theta_and_r_minus_theta'), ('state-selection.rate-discharge-hypothesis-iii', 'claims/state-selection.rate-discharge-hypothesis-iii', 'check.py::check_kms_state_is_the_faithful_gibbs_state'), ('state-selection.rate-discharge-hypothesis-iii', 'claims/state-selection.rate-discharge-hypothesis-iii', 'check.py::check_one_beta_for_all_modes'), ('state-selection.rate-discharge-hypothesis-iii', 'claims/state-selection.rate-discharge-hypothesis-iii', 'check.py::check_conjugation_closes_at_two_pi'), ('state-selection.rate-discharge-hypothesis-iii', 'claims/state-selection.rate-discharge-hypothesis-iii', 'check.py::check_calibration_beta_is_eight_pi_m'), ('state-selection.where-fermi-dirac-comes', 'claims/state-selection.where-fermi-dirac-comes', 'check.py::check_euclidean_rotor_period'), ('state-selection.where-fermi-dirac-comes', 'claims/state-selection.where-fermi-dirac-comes', 'check.py::check_even_sector_periodic_odd_sector_antiperiodic'), ('state-selection.where-fermi-dirac-comes', 'claims/state-selection.where-fermi-dirac-comes', 'check.py::check_anticommutator_gives_fermi_dirac'), ('state-selection.partner-purification-are-canonical', 'claims/state-selection.partner-purification-are-canonical', 'check.py::check_gns_vector_cyclic_and_separating'), ('state-selection.partner-purification-are-canonical', 'claims/state-selection.partner-purification-are-canonical', 'check.py::check_commutant_is_partner_copy_via_modular_conjugation'), ('state-selection.partner-purification-are-canonical', 'claims/state-selection.partner-purification-are-canonical', 'check.py::check_purifications_differ_by_partner_unitary'), ('state-selection.partner-purification-are-canonical', 'claims/state-selection.partner-purification-are-canonical', 'check.py::check_gibbs_state_gives_thermofield_double'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_descent_is_parity_average'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_range_kernel_and_uniqueness'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_preserves_alpha_invariant_states'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_descended_marginal_is_diagonal_gibbs'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_beta_unique_and_endpoints'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_zero_weight_mode'), ('singularity.ascended-marginals-are-diagonal', 'claims/singularity.ascended-marginals-are-diagonal', 'check.py::check_even_units_have_zero_ladder_expectation_and_diagonal_marginals'), ('singularity.ascended-marginals-are-diagonal', 'claims/singularity.ascended-marginals-are-diagonal', 'check.py::check_even_state_marginals_are_descended_gibbs'), ('singularity.ascended-marginals-are-diagonal', 'claims/singularity.ascended-marginals-are-diagonal', 'check.py::check_parity_protection_is_special_case'), ('singularity.kms-uniqueness-factor', 'claims/singularity.kms-uniqueness-factor', 'check.py::check_kms_iff_gibbs'), ('singularity.kms-uniqueness-factor', 'claims/singularity.kms-uniqueness-factor', 'check.py::check_kms_states_form_a_line_in_beta'), ('singularity.universality-temperature-under-g', 'claims/singularity.universality-temperature-under-g', 'check.py::check_g_gives_one_temperature'), ('singularity.universality-temperature-under-g', 'claims/singularity.universality-temperature-under-g', 'check.py::check_product_satisfies_g_only_at_equal_betas'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_commuting_automorphisms_fix_gibbs'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_reversing_automorphisms_flip_beta'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_reparametrisation_rescales_beta'), ('singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'claims/singularity.rate-rigidity-temperature-not-algebra-intrinsic', 'check.py::check_only_orientation_flip_intertwines'), ('singularity.exact-equilibrium-over-determines-boundary-modes', 'claims/singularity.exact-equilibrium-over-determines-boundary-modes', 'check.py::check_geometric_state_is_product'), ('singularity.exact-equilibrium-over-determines-boundary-modes', 'claims/singularity.exact-equilibrium-over-determines-boundary-modes', 'check.py::check_zero_correlation_and_zero_deficit'), ('singularity.exact-equilibrium-over-determines-boundary-modes', 'claims/singularity.exact-equilibrium-over-determines-boundary-modes', 'check.py::check_correlated_state_carries_the_deficit'), ('singularity.number-diagonal-dynamics-models-scrambling-derived', 'claims/singularity.number-diagonal-dynamics-models-scrambling-derived', 'check.py::check_sigma_algebra_is_the_diagonal_algebra'), ('singularity.number-diagonal-dynamics-models-scrambling-derived', 'claims/singularity.number-diagonal-dynamics-models-scrambling-derived', 'check.py::check_exponentials_are_diagonal_and_conserve_populations'), ('singularity.number-diagonal-dynamics-models-scrambling-derived', 'claims/singularity.number-diagonal-dynamics-models-scrambling-derived', 'check.py::check_controlled_z_in_algebra_and_hop_outside'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_radial_plane_is_hb_invariant'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_shape_operator_matches_gauge_curvature'), ('singularity.curvature-gauge-field-exact-shape-decoupling', 'claims/singularity.curvature-gauge-field-exact-shape-decoupling', 'check.py::check_shape_operator_spectrum'), ('singularity.deficit-carried-quanta-correlations', 'claims/singularity.deficit-carried-quanta-correlations', 'check.py::check_diagonal_marginals_pass_through_descent'), ('singularity.deficit-carried-quanta-correlations', 'claims/singularity.deficit-carried-quanta-correlations', 'check.py::check_deficit_is_total_correlation_drop_mixed'), ('singularity.deficit-carried-quanta-correlations', 'claims/singularity.deficit-carried-quanta-correlations', 'check.py::check_pure_state_deficit_is_whole_descended_entropy'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_pinching_structure'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_key_lemma_moment_form'), ('singularity.deficit-theorem-cost-descent-exactly', 'claims/singularity.deficit-theorem-cost-descent-exactly', 'check.py::check_entropy_identity_exact'), ('singularity.descent-what-it-erases', 'claims/singularity.descent-what-it-erases', 'check.py::check_occupation_projector'), ('singularity.descent-what-it-erases', 'claims/singularity.descent-what-it-erases', 'check.py::check_pinching_keeps_diagonal_erases_coherences'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_complexified_rotor_period_four_pi'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_module_form_and_conjugation_period'), ('singularity.euclidean-rotor-where-it-lies', 'claims/singularity.euclidean-rotor-where-it-lies', 'check.py::check_euclidean_rotation_is_no_real_rotor'), ('singularity.modular-theory-matrix-factor-proved-outright', 'claims/singularity.modular-theory-matrix-factor-proved-outright', 'check.py::check_cyclic_and_separating_iff_weights_positive'), ('singularity.modular-theory-matrix-factor-proved-outright', 'claims/singularity.modular-theory-matrix-factor-proved-outright', 'check.py::check_tomita_polar_decomposition'), ('singularity.modular-theory-matrix-factor-proved-outright', 'claims/singularity.modular-theory-matrix-factor-proved-outright', 'check.py::check_modular_flow_and_kms'), ('singularity.plane-rate', 'claims/singularity.plane-rate', 'check.py::check_pair_selected_invariantly'), ('singularity.plane-rate', 'claims/singularity.plane-rate', 'check.py::check_surface_gravity_from_the_connection'), ('singularity.plane-rate', 'claims/singularity.plane-rate', 'check.py::check_two_pi_rapidity_is_eight_pi_m')]

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
