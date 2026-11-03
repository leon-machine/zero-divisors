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
  "label:thm:purespinor",
  "label:thm:states"
 ],
 "verify_T12.py": [
  "label:prop:content",
  "label:prop:ladder",
  "label:prop:raw",
  "label:thm:algebra",
  "label:thm:global"
 ],
 "verify_T12_lepton.py": [
  "label:prop:content",
  "label:prop:orientation",
  "label:prop:selfconj",
  "label:prop:twoactions"
 ]
}
CHECKS = [('lepton.imported-twistor-state-pair-system-excitations', 'claims/lepton.imported-twistor-state-pair-system-excitations', 'check.py::check_fock_module_irreducible_with_two_halves'), ('lepton.imported-twistor-state-pair-system-excitations', 'claims/lepton.imported-twistor-state-pair-system-excitations', 'check.py::check_each_conformal_spinor_is_a_fock_vacuum'), ('lepton.imported-twistor-state-pair-system-excitations', 'claims/lepton.imported-twistor-state-pair-system-excitations', 'check.py::check_excitations_from_a_dual_complement_span_the_module'), ('lepton.imported-automorphism-group-section-hypercharge-generator', 'claims/lepton.imported-automorphism-group-section-hypercharge-generator', 'check.py::check_kernel_and_section'), ('lepton.imported-automorphism-group-section-hypercharge-generator', 'claims/lepton.imported-automorphism-group-section-hypercharge-generator', 'check.py::check_z6_quotient'), ('lepton.imported-automorphism-group-section-hypercharge-generator', 'claims/lepton.imported-automorphism-group-section-hypercharge-generator', 'check.py::check_centre_is_hypercharge_line'), ('lepton.imported-automorphism-group-section-hypercharge-generator', 'claims/lepton.imported-automorphism-group-section-hypercharge-generator', 'check.py::check_y_acts_by_the_abelian_weight'), ('lepton.imported-tensor-ledger-contains-no-lepton', 'claims/lepton.imported-tensor-ledger-contains-no-lepton', 'check.py::check_decomposition_and_weight'), ('lepton.imported-tensor-ledger-contains-no-lepton', 'claims/lepton.imported-tensor-ledger-contains-no-lepton', 'check.py::check_no_lepton_doublet'), ('lepton.imported-tensor-ledger-contains-no-lepton', 'claims/lepton.imported-tensor-ledger-contains-no-lepton', 'check.py::check_row_filling_states_are_the_4_1'), ('lepton.imported-free-sector-anomaly-conditions', 'claims/lepton.imported-free-sector-anomaly-conditions', 'check.py::check_free_sector_content'), ('lepton.imported-free-sector-anomaly-conditions', 'claims/lepton.imported-free-sector-anomaly-conditions', 'check.py::check_opposite_handedness_enters_conjugated'), ('lepton.imported-duality-pair-system', 'claims/lepton.imported-duality-pair-system', 'check.py::check_characters_match'), ('lepton.imported-duality-pair-system', 'claims/lepton.imported-duality-pair-system', 'check.py::check_equivariant_pairings'), ('lepton.content-constituent-space', 'claims/lepton.content-constituent-space', 'check.py::check_constituent_content_and_weights'), ('lepton.content-constituent-space', 'claims/lepton.content-constituent-space', 'check.py::check_odd_and_even_halves'), ('lepton.content-constituent-space', 'claims/lepton.content-constituent-space', 'check.py::check_duality_on_the_section'), ('lepton.content-constituent-space', 'claims/lepton.content-constituent-space', 'check.py::check_lattice_condition'), ('lepton.unit-action-cell-action', 'claims/lepton.unit-action-cell-action', 'check.py::check_one_pair_identification_is_isomorphism'), ('lepton.unit-action-cell-action', 'claims/lepton.unit-action-cell-action', 'check.py::check_cell_span_exceeds_constituents'), ('lepton.unit-action-cell-action', 'claims/lepton.unit-action-cell-action', 'check.py::check_weights_and_spin_of_the_two_actions'), ('lepton.self-conjugacy-forces-determinant-one-group', 'claims/lepton.self-conjugacy-forces-determinant-one-group', 'check.py::check_not_self_dual_under_full_group'), ('lepton.self-conjugacy-forces-determinant-one-group', 'claims/lepton.self-conjugacy-forces-determinant-one-group', 'check.py::check_self_dual_iff_determinant_one'), ('lepton.self-conjugacy-forces-determinant-one-group', 'claims/lepton.self-conjugacy-forces-determinant-one-group', 'check.py::check_dimension_twelve'), ('lepton.self-conjugacy-forces-determinant-one-group', 'claims/lepton.self-conjugacy-forces-determinant-one-group', 'check.py::check_twisted_action_is_self_conjugate'), ('lepton.relative-handedness-slotted-free-sectors', 'claims/lepton.relative-handedness-slotted-free-sectors', 'check.py::check_first_listing_is_one_generation_anomaly_free'), ('lepton.relative-handedness-slotted-free-sectors', 'claims/lepton.relative-handedness-slotted-free-sectors', 'check.py::check_second_listing_is_anomalous'), ('lepton.relative-handedness-slotted-free-sectors', 'claims/lepton.relative-handedness-slotted-free-sectors', 'check.py::check_consistency_fixes_relative_handedness'), ('correspondence.fock-model-complexified-ascended-algebra', 'claims/correspondence.fock-model-complexified-ascended-algebra', 'check.py::check_isotropic_pair_and_clifford_relations'), ('correspondence.fock-model-complexified-ascended-algebra', 'claims/correspondence.fock-model-complexified-ascended-algebra', 'check.py::check_blade_products_span_all_endomorphisms'), ('correspondence.fock-model-complexified-ascended-algebra', 'claims/correspondence.fock-model-complexified-ascended-algebra', 'check.py::check_chirality_halves_and_even_subalgebra'), ('correspondence.fock-model-complexified-ascended-algebra', 'claims/correspondence.fock-model-complexified-ascended-algebra', 'check.py::check_dual_pairs_conjugate_under_orthogonal_group'), ('correspondence.twistors-are-states-three-ladder-pairs', 'claims/correspondence.twistors-are-states-three-ladder-pairs', 'check.py::check_every_conformal_spinor_is_pure'), ('correspondence.twistors-are-states-three-ladder-pairs', 'claims/correspondence.twistors-are-states-three-ladder-pairs', 'check.py::check_vacuum_of_own_three_pair_system'), ('correspondence.twistors-are-states-three-ladder-pairs', 'claims/correspondence.twistors-are-states-three-ladder-pairs', 'check.py::check_states_not_operators_and_disjoint_families'), ('standard-model.gauge-algebra-minimal-massive-composite', 'claims/standard-model.gauge-algebra-minimal-massive-composite', 'check.py::check_maximal_hierarchy_is_seventeen'), ('standard-model.gauge-algebra-minimal-massive-composite', 'claims/standard-model.gauge-algebra-minimal-massive-composite', 'check.py::check_mass_first_at_two_constituents'), ('standard-model.gauge-algebra-minimal-massive-composite', 'claims/standard-model.gauge-algebra-minimal-massive-composite', 'check.py::check_minimal_massive_is_standard_model'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_kernel_and_coset_rescaling'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_z6_kernel_exactly'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_su5_splitting_subgroup'), ('standard-model.global-form-quotient-determined', 'claims/standard-model.global-form-quotient-determined', 'check.py::check_charge_lattice'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_fock_module_irreducible_with_two_halves'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_each_conformal_spinor_is_a_fock_vacuum'), ('standard-model.imported-pair-systems-two-chirality-halves', 'claims/standard-model.imported-pair-systems-two-chirality-halves', 'check.py::check_excitations_from_a_dual_complement_span_the_module'), ('standard-model.internal-symmetry-ladder', 'claims/standard-model.internal-symmetry-ladder', 'check.py::check_momentum_preservation_forces_unitarity'), ('standard-model.internal-symmetry-ladder', 'claims/standard-model.internal-symmetry-ladder', 'check.py::check_unitaries_preserve_and_others_fail'), ('standard-model.internal-symmetry-ladder', 'claims/standard-model.internal-symmetry-ladder', 'check.py::check_un_is_sun_times_u1_mod_zn'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_cells_are_quark_doublet'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_doublets_under_s'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_no_doublet_without_s'), ('standard-model.quarks-leptons-two-level-fermion-content', 'claims/standard-model.quarks-leptons-two-level-fermion-content', 'check.py::check_single_spinor_sector'), ('standard-model.raw-representation-content-state-space', 'claims/standard-model.raw-representation-content-state-space', 'check.py::check_cauchy_table_by_degree'), ('standard-model.raw-representation-content-state-space', 'claims/standard-model.raw-representation-content-state-space', 'check.py::check_cauchy_characters'), ('standard-model.raw-representation-content-state-space', 'claims/standard-model.raw-representation-content-state-space', 'check.py::check_single_spinor_sector')]

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
