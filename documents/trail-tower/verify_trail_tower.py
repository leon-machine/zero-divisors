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
  "num:3.6",
  "num:7.1"
 ],
 "verify_T03.py": [
  "num:3.1",
  "num:3.2",
  "num:3.6",
  "num:4.1",
  "num:4.2",
  "num:4.3",
  "num:5.1",
  "num:5.2",
  "num:5.4"
 ],
 "verify_T08.py": [
  "num:4.11"
 ],
 "verify_T14a.py": [
  "num:2.3"
 ]
}
CHECKS = [('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_twisted_ground_copy'), ('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_plane_algebra_is_full_matrix_algebra'), ('tower.commuting-copies', 'claims/tower.commuting-copies', 'check.py::check_commuting_copies_tensor_isomorphism'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_clock_and_centre_frozen'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_full_corner_is_ground'), ('tower.rigidity-clock-frozen', 'claims/tower.rigidity-clock-frozen', 'check.py::check_physical_tower_is_quaternionic'), ('tower.ladder-pairs-satisfy-car-vectors', 'claims/tower.ladder-pairs-satisfy-car-vectors', 'check.py::check_car_as_vectors'), ('tower.ladder-pairs-satisfy-car-vectors', 'claims/tower.ladder-pairs-satisfy-car-vectors', 'check.py::check_new_rung_touches_nothing'), ('tower.fock-module-one-qubit-per-rung', 'claims/tower.fock-module-one-qubit-per-rung', 'check.py::check_w_is_maximal_isotropic'), ('tower.fock-module-one-qubit-per-rung', 'claims/tower.fock-module-one-qubit-per-rung', 'check.py::check_chevalley_module_and_vacuum'), ('tower.fock-module-one-qubit-per-rung', 'claims/tower.fock-module-one-qubit-per-rung', 'check.py::check_irreducible'), ('tower.fock-module-one-qubit-per-rung', 'claims/tower.fock-module-one-qubit-per-rung', 'check.py::check_one_qubit_per_rung'), ('tower.witt-index-quantum-capacity', 'claims/tower.witt-index-quantum-capacity', 'check.py::check_mode_family_attains_witt_index'), ('tower.witt-index-quantum-capacity', 'claims/tower.witt-index-quantum-capacity', 'check.py::check_witt_subspace_is_maximal'), ('tower.witt-index-quantum-capacity', 'claims/tower.witt-index-quantum-capacity', 'check.py::check_each_rung_adds_one_mode'), ('tower.algebraic-limit-even-charge', 'claims/tower.algebraic-limit-even-charge', 'check.py::check_transported_connecting_map_is_corrected_doubling'), ('tower.algebraic-limit-even-charge', 'claims/tower.algebraic-limit-even-charge', 'check.py::check_intertwiners_make_the_embeddings_block_doublings'), ('tower.algebraic-limit-even-charge', 'claims/tower.algebraic-limit-even-charge', 'check.py::check_limit_is_clifford_algebra_of_the_union'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_tower_vectors_satisfy_the_car'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_fock_adjointness'), ('tower.car-limit-even-charge', 'claims/tower.car-limit-even-charge', 'check.py::check_ground_factor_commutes_and_correctors_unitary'), ('tower.answers-iteration-question', 'claims/tower.answers-iteration-question', 'check.py::check_clock_never_ticks'), ('tower.answers-iteration-question', 'claims/tower.answers-iteration-question', 'check.py::check_one_qubit_per_rung'), ('scrambling.pair-mode-qubit-one-object', 'claims/scrambling.pair-mode-qubit-one-object', 'check.py::check_two_pairs_satisfy_car_in_cl24'), ('scrambling.pair-mode-qubit-one-object', 'claims/scrambling.pair-mode-qubit-one-object', 'check.py::check_no_third_pair'), ('scrambling.pair-mode-qubit-one-object', 'claims/scrambling.pair-mode-qubit-one-object', 'check.py::check_pair_is_one_qubit'), ('odd-extensions.four-extensions-oriented-pair', 'claims/odd-extensions.four-extensions-oriented-pair', 'check.py::check_omega_squares_and_residues'), ('odd-extensions.four-extensions-oriented-pair', 'claims/odd-extensions.four-extensions-oriented-pair', 'check.py::check_structures'), ('odd-extensions.four-extensions-oriented-pair', 'claims/odd-extensions.four-extensions-oriented-pair', 'check.py::check_even_parts_are_the_stated_shadows'), ('odd-extensions.four-extensions-oriented-pair', 'claims/odd-extensions.four-extensions-oriented-pair', 'check.py::check_convention_free_rule'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_omega_plus_one_doubling'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_omega_minus_one_complexification'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_even_subalgebra_identities'), ('odd-extensions.imported-representatives-dimension-nearest-four-types', 'claims/odd-extensions.imported-representatives-dimension-nearest-four-types', 'check.py::check_representatives_and_sterile'), ('odd-extensions.imported-representatives-dimension-nearest-four-types', 'claims/odd-extensions.imported-representatives-dimension-nearest-four-types', 'check.py::check_shadow_types'), ('odd-extensions.imported-representatives-dimension-nearest-four-types', 'claims/odd-extensions.imported-representatives-dimension-nearest-four-types', 'check.py::check_type_depends_on_residue_alone'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_odd_volume_element_central_with_square'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_n5_square_is_minus_one_to_q'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_even_control_not_central'), ('std-algebra.blade-basis', 'claims/std-algebra.blade-basis', 'check.py::check_symbol_images_independent'), ('std-algebra.existence-uniqueness', 'claims/std-algebra.existence-uniqueness', 'check.py::check_model_squares_to_form'), ('std-algebra.sta-matrix', 'claims/std-algebra.sta-matrix', 'check.py::check_quaternionic_and_dirac_readings'), ('std-algebra.sta-matrix', 'claims/std-algebra.sta-matrix', 'check.py::check_spacetime_split'), ('std-algebra.vector-squares', 'claims/std-algebra.vector-squares', 'check.py::check_anticommutator_is_twice_the_polar_form'), ('std-algebra.witt-basis-car', 'claims/std-algebra.witt-basis-car', 'check.py::check_null_pairs_satisfy_the_car'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_hyperbolic_partner_in_a_plane'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_witt_decomposition_and_maximal_null_subspace'), ('tower.compatibility-connecting-maps-transported', 'claims/tower.compatibility-connecting-maps-transported', 'check.py::check_identification_data'), ('tower.compatibility-connecting-maps-transported', 'claims/tower.compatibility-connecting-maps-transported', 'check.py::check_transported_connecting_map_is_ad_v_theta'), ('tower.compatibility-connecting-maps-transported', 'claims/tower.compatibility-connecting-maps-transported', 'check.py::check_naive_corrector_and_labelling_convention'), ('tower.grade-twist-when-it-inner', 'claims/tower.grade-twist-when-it-inner', 'check.py::check_embedding_is_twisted_diagonal'), ('tower.grade-twist-when-it-inner', 'claims/tower.grade-twist-when-it-inner', 'check.py::check_even_charge_volume_element_implements_twist'), ('tower.grade-twist-when-it-inner', 'claims/tower.grade-twist-when-it-inner', 'check.py::check_inner_exactly_for_even_charge'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_centre_of_matrix_algebra'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_matrix_algebra_over_simple_is_simple'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_block_flattening'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_matrices_over_direct_sum'), ('tower.structure-tower-c-norms', 'claims/tower.structure-tower-c-norms', 'check.py::check_star_exists_unique_antimultiplicative'), ('tower.structure-tower-c-norms', 'claims/tower.structure-tower-c-norms', 'check.py::check_frame_unitary_and_ladder_adjoint'), ('tower.structure-tower-c-norms', 'claims/tower.structure-tower-c-norms', 'check.py::check_maps_and_correctors_compatible'), ('tower.structure-tower-c-norms', 'claims/tower.structure-tower-c-norms', 'check.py::check_even_floors_are_full_matrix_star_algebras'), ('tower.volume-elements-planes', 'claims/tower.volume-elements-planes', 'check.py::check_plane_volume_elements'), ('tower.volume-elements-planes', 'claims/tower.volume-elements-planes', 'check.py::check_product_omega_k'), ('tower.wall-package', 'claims/tower.wall-package', 'check.py::check_completion_nondegenerate_up_to_the_wall'), ('tower.wall-package', 'claims/tower.wall-package', 'check.py::check_degeneracy_relocated_to_shadow_wall'), ('tower.wall-package', 'claims/tower.wall-package', 'check.py::check_iterated_walls_tame_one_plane_each'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_type_c_iff_p_minus_q_one_mod_four'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_eps_pm_identities_and_exchange'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_splitting_into_two_ideals'), ('transport.rule-1-morita-trivial', 'claims/transport.rule-1-morita-trivial', 'check.py::check_ladder_pair_matrix_units_and_corner'), ('transport.rule-1-morita-trivial', 'claims/transport.rule-1-morita-trivial', 'check.py::check_twisted_diagonal_and_mat2'), ('transport.rule-1-morita-trivial', 'claims/transport.rule-1-morita-trivial', 'check.py::check_morita_invariants_preserved')]

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
