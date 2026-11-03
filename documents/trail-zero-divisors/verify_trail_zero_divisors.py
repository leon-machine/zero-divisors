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
  "num:2.6",
  "num:2.7",
  "num:2.8",
  "num:3.3",
  "num:3.6",
  "num:5.4",
  "num:7.8"
 ]
}
CHECKS = [('transport.noinverse', 'claims/transport.noinverse', 'check.py::check_null_vector_squares_to_zero_and_multiplication_has_half_rank'), ('transport.noinverse', 'claims/transport.noinverse', 'check.py::check_no_inverse_in_larger_algebras'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_definite_forms_have_no_null_vectors'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_mixed_forms_have_a_null_cone_of_dimension_n_minus_one'), ('transport.existence-locus-type-n', 'claims/transport.existence-locus-type-n', 'check.py::check_null_vectors_are_non_invertible_zero_divisors'), ('transport.exceptional-division-algebras', 'claims/transport.exceptional-division-algebras', 'check.py::check_witnesses_exist_exactly_off_the_exceptional_lists'), ('transport.exceptional-division-algebras', 'claims/transport.exceptional-division-algebras', 'check.py::check_exceptional_algebras_are_sums_of_division_algebras'), ('transport.exceptional-division-algebras', 'claims/transport.exceptional-division-algebras', 'check.py::check_verdicts_match_the_classification_table'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_type_c_iff_p_minus_q_one_mod_four'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_eps_pm_identities_and_exchange'), ('transport.existence-classification-type-c', 'claims/transport.existence-classification-type-c', 'check.py::check_splitting_into_two_ideals'), ('transport.existence-locus-type-p', 'claims/transport.existence-locus-type-p', 'check.py::check_noncentral_idempotent_exactly_off_the_five'), ('transport.existence-locus-type-p', 'claims/transport.existence-locus-type-p', 'check.py::check_idempotents_of_the_five_are_central'), ('transport.existence-locus-type-p', 'claims/transport.existence-locus-type-p', 'check.py::check_orthogonal_vector_pair_gives_type_p'), ('transport.regularity-localises-zero-divisors-idempotents', 'claims/transport.regularity-localises-zero-divisors-idempotents', 'check.py::check_regularity_and_idempotents'), ('transport.regularity-localises-zero-divisors-idempotents', 'claims/transport.regularity-localises-zero-divisors-idempotents', 'check.py::check_controls_invertible_and_quaternions'), ('transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'claims/transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'check.py::check_every_zero_divisor_annihilated_both_sides'), ('transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'claims/transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'check.py::check_simple_signatures_only_noncentral_annihilators'), ('transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'claims/transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'check.py::check_split_signatures_central_or_type_p'), ('transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'claims/transport.exhaustiveness-every-zero-divisor-annihilated-idempotent', 'check.py::check_isotropic_origin_in_mixed_signatures'), ('transport.no-go-level-elements', 'claims/transport.no-go-level-elements', 'check.py::check_pseudo_inverse_normal_form'), ('transport.no-go-level-elements', 'claims/transport.no-go-level-elements', 'check.py::check_null_rotations_fix_v_and_shear_w0'), ('transport.no-go-level-elements', 'claims/transport.no-go-level-elements', 'check.py::check_no_pseudo_inverse_fixed_by_null_rotations'), ('transport.no-transport-terminates', 'claims/transport.no-transport-terminates', 'check.py::check_rule_one_completion_carries_type_n'), ('transport.no-transport-terminates', 'claims/transport.no-transport-terminates', 'check.py::check_rule_two_completion_carries_type_p'), ('transport.no-transport-terminates', 'claims/transport.no-transport-terminates', 'check.py::check_no_completion_is_a_division_algebra'), ('primer.commutation-rule', 'claims/primer.commutation-rule', 'check.py::check_commutation_rule'), ('std-algebra.blade-basis', 'claims/std-algebra.blade-basis', 'check.py::check_symbol_images_independent'), ('std-algebra.involution-properties', 'claims/std-algebra.involution-properties', 'check.py::check_involutions_on_products_and_grades'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_blade_table'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_anticommute_iff_orthogonal'), ('std-algebra.vector-squares', 'claims/std-algebra.vector-squares', 'check.py::check_anticommutator_is_twice_the_polar_form'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_hyperbolic_partner_in_a_plane'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_witt_decomposition_and_maximal_null_subspace'), ('transport.centre', 'claims/transport.centre', 'check.py::check_centre_by_kernel'), ('transport.centre', 'claims/transport.centre', 'check.py::check_centre_blade_wise'), ('transport.classification-real-clifford-algebras', 'claims/transport.classification-real-clifford-algebras', 'check.py::check_eight_entry_table'), ('transport.classification-real-clifford-algebras', 'claims/transport.classification-real-clifford-algebras', 'check.py::check_matrix_sizes_sample'), ('transport.matrix-units-peirce-isomorphism', 'claims/transport.matrix-units-peirce-isomorphism', 'check.py::check_matrix_unit_relations'), ('transport.matrix-units-peirce-isomorphism', 'claims/transport.matrix-units-peirce-isomorphism', 'check.py::check_peirce_isomorphism'), ('transport.rule-2-ideal-fusion-sharp-form', 'claims/transport.rule-2-ideal-fusion-sharp-form', 'check.py::check_matrix_units_and_corner'), ('transport.rule-2-ideal-fusion-sharp-form', 'claims/transport.rule-2-ideal-fusion-sharp-form', 'check.py::check_fused_algebra_simple_centre_r'), ('transport.rule-2-ideal-fusion-sharp-form', 'claims/transport.rule-2-ideal-fusion-sharp-form', 'check.py::check_eps_exchanged_by_ad_nu'), ('transport.rule-2-ideal-fusion-sharp-form', 'claims/transport.rule-2-ideal-fusion-sharp-form', 'check.py::check_two_ascents_isomorphic_fixing_corner'), ('transport.sign', 'claims/transport.sign', 'check.py::check_omega_square_closed_forms'), ('transport.sign', 'claims/transport.sign', 'check.py::check_reversal_sign_count'), ('transport.sign', 'claims/transport.sign', 'check.py::check_depends_only_on_p_minus_q'), ('transport.splitting-along-hyperbolic-plane', 'claims/transport.splitting-along-hyperbolic-plane', 'check.py::check_hyperbolic_pair_and_unique_expansion'), ('transport.splitting-along-hyperbolic-plane', 'claims/transport.splitting-along-hyperbolic-plane', 'check.py::check_left_multiplication_by_v_injective_on_cl_u')]

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
