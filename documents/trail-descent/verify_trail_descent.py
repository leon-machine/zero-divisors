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
  "num:4.1",
  "num:5.5",
  "num:5.7",
  "num:6.3",
  "num:7.2",
  "num:7.3",
  "num:7.6"
 ]
}
CHECKS = [('singularity.descent-what-it-erases', 'claims/singularity.descent-what-it-erases', 'check.py::check_occupation_projector'), ('singularity.descent-what-it-erases', 'claims/singularity.descent-what-it-erases', 'check.py::check_pinching_keeps_diagonal_erases_coherences'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_descent_is_parity_average'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_range_kernel_and_uniqueness'), ('singularity.descent-parity-average', 'claims/singularity.descent-parity-average', 'check.py::check_preserves_alpha_invariant_states'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_descended_marginal_is_diagonal_gibbs'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_beta_unique_and_endpoints'), ('singularity.descended-form-state-independent', 'claims/singularity.descended-form-state-independent', 'check.py::check_zero_weight_mode'), ('singularity.modular-structure-completed-pair', 'claims/singularity.modular-structure-completed-pair', 'check.py::check_sigma_is_unit_boost_bivector'), ('singularity.modular-structure-completed-pair', 'claims/singularity.modular-structure-completed-pair', 'check.py::check_rotor_flow_opposite_weights'), ('singularity.modular-structure-completed-pair', 'claims/singularity.modular-structure-completed-pair', 'check.py::check_spectral_projectors_are_descent_projectors'), ('singularity.modular-structure-completed-pair', 'claims/singularity.modular-structure-completed-pair', 'check.py::check_rotor_flow_unique_within_real_rotors'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_invariance_forces_one_eigenspace'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_cyclic_separating_only_on_the_number_basis'), ('singularity.schmidt-forcing-proved-outright', 'claims/singularity.schmidt-forcing-proved-outright', 'check.py::check_phase_convention_gives_cos_sin'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_invariant_cyclic_state_descends_to_kms_beta_free'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_hawking_temperature_and_fermi_dirac'), ('singularity.modular-descent', 'claims/singularity.modular-descent', 'check.py::check_hypotheses_sufficient_not_necessary'), ('descent-lift.kraus-form-descent-even-states', 'claims/descent-lift.kraus-form-descent-even-states', 'check.py::check_kraus_sum_is_pinching'), ('descent-lift.kraus-form-descent-even-states', 'claims/descent-lift.kraus-form-descent-even-states', 'check.py::check_kraus_rank_is_choi_rank'), ('descent-lift.kraus-form-descent-even-states', 'claims/descent-lift.kraus-form-descent-even-states', 'check.py::check_even_sector_monomials_pair_up'), ('descent-lift.kraus-form-descent-even-states', 'claims/descent-lift.kraus-form-descent-even-states', 'check.py::check_pair_example'), ('descent-lift.lift-costs-one-rung-per-mode', 'claims/descent-lift.lift-costs-one-rung-per-mode', 'check.py::check_record_count_and_lift_form'), ('descent-lift.lift-costs-one-rung-per-mode', 'claims/descent-lift.lift-costs-one-rung-per-mode', 'check.py::check_even_sector_of_k_rungs'), ('descent-lift.lift-costs-one-rung-per-mode', 'claims/descent-lift.lift-costs-one-rung-per-mode', 'check.py::check_lift_with_nu_rungs'), ('descent-lift.lift-costs-one-rung-per-mode', 'claims/descent-lift.lift-costs-one-rung-per-mode', 'check.py::check_factorisation_and_coupling'), ('descent-lift.lift-costs-one-rung-per-mode', 'claims/descent-lift.lift-costs-one-rung-per-mode', 'check.py::check_lift_needs_number_change'), ('descent-lift.parity-alone-forces-second-rung', 'claims/descent-lift.parity-alone-forces-second-rung', 'check.py::check_one_rung_candidates_induce_descent'), ('descent-lift.parity-alone-forces-second-rung', 'claims/descent-lift.parity-alone-forces-second-rung', 'check.py::check_both_one_rung_candidates_are_odd'), ('descent-lift.parity-alone-forces-second-rung', 'claims/descent-lift.parity-alone-forces-second-rung', 'check.py::check_two_rung_occupation_copy_is_even_lift'), ('descent-lift.classical-shared-bit-reduced-view-pure', 'claims/descent-lift.classical-shared-bit-reduced-view-pure', 'check.py::check_joint_state_and_marginals'), ('descent-lift.classical-shared-bit-reduced-view-pure', 'claims/descent-lift.classical-shared-bit-reduced-view-pure', 'check.py::check_schmidt_coefficients_move_to_pair_record_cut'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_descent_is_parity_average_and_pinching'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_even_subalgebra'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_supplied_class_is_joint_number_diagonal'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_vacuum_stabilisers_and_tangent'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_pairing_rotation_witness'), ('descent-lift.imported-descent-modes-univalence-supplied-class', 'claims/descent-lift.imported-descent-modes-univalence-supplied-class', 'check.py::check_thermofield_marginals_gibbs'), ('singularity.pseudo-inverse-identities-hyperbolic-atom', 'claims/singularity.pseudo-inverse-identities-hyperbolic-atom', 'check.py::check_pseudo_inverse_identities'), ('singularity.pseudo-inverse-identities-hyperbolic-atom', 'claims/singularity.pseudo-inverse-identities-hyperbolic-atom', 'check.py::check_atom_is_car_and_zero_divisor'), ('std-algebra.bivector-exponential', 'claims/std-algebra.bivector-exponential', 'check.py::check_powers_collapse'), ('std-algebra.bivector-exponential', 'claims/std-algebra.bivector-exponential', 'check.py::check_closed_forms_are_rotors'), ('std-algebra.cl11-matrix', 'claims/std-algebra.cl11-matrix', 'check.py::check_hyperbolic_plane_is_m2r'), ('std-algebra.witt-basis-car', 'claims/std-algebra.witt-basis-car', 'check.py::check_null_pairs_satisfy_the_car')]

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
