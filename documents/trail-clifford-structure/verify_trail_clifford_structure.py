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
 "verify_T00.py": [
  "num:9.2"
 ],
 "verify_T01.py": [
  "num:6.3",
  "num:6.4"
 ],
 "verify_T04.py": [
  "num:2.6"
 ],
 "verify_T14.py": [
  "label:thm:soldered",
  "label:thm:types"
 ],
 "verify_T14a.py": [
  "num:2.3"
 ]
}
CHECKS = [('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_blades_are_a_basis'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants_polynomial'), ('transport.classification-real-clifford-algebras', 'claims/transport.classification-real-clifford-algebras', 'check.py::check_eight_entry_table'), ('transport.classification-real-clifford-algebras', 'claims/transport.classification-real-clifford-algebras', 'check.py::check_matrix_sizes_sample'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_omega_plus_one_doubling'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_omega_minus_one_complexification'), ('odd-extensions.doubling-or-complexification', 'claims/odd-extensions.doubling-or-complexification', 'check.py::check_even_subalgebra_identities'), ('transport.classification-idempotent-orbits', 'claims/transport.classification-idempotent-orbits', 'check.py::check_orbits_are_rank_classes'), ('transport.classification-idempotent-orbits', 'claims/transport.classification-idempotent-orbits', 'check.py::check_complement_conjugate_iff_balanced'), ('transport.classification-idempotent-orbits', 'claims/transport.classification-idempotent-orbits', 'check.py::check_central_iff_singleton_orbit'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_centre_of_matrix_algebra'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_matrix_algebra_over_simple_is_simple'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_block_flattening'), ('tower.matrix-amplification-structural-properties', 'claims/tower.matrix-amplification-structural-properties', 'check.py::check_matrices_over_direct_sum'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_signature_is_read_off_the_generating_subspace'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_abstract_isomorphisms_not_soldered'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_this_world_and_r4_are_mat2_quaternions'), ('primer.commutation-rule', 'claims/primer.commutation-rule', 'check.py::check_commutation_rule'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_tau_is_automorphism_and_twisted_adjoint'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_vector_is_reflection'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_kernel_is_plus_minus_one'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_surjectivity_samples'), ('primer.sign', 'claims/primer.sign', 'check.py::check_omega_square'), ('primer.sign', 'claims/primer.sign', 'check.py::check_exponent_parity_identity'), ('primer.centre', 'claims/primer.centre', 'check.py::check_centre_by_linear_algebra'), ('primer.centre', 'claims/primer.centre', 'check.py::check_central_blades_higher_n'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_type_table_on_p3_representatives'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_type_is_a_residue_invariant'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_intrinsic_groups'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_volume_element_on_the_odd_residues'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_odd_volume_element_central_with_square'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_n5_square_is_minus_one_to_q'), ('odd-extensions.volume-element-odd-dimension', 'claims/odd-extensions.volume-element-odd-dimension', 'check.py::check_even_control_not_central'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_classification_table'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_split_summands_isomorphic_and_simple'), ('std-algebra.blade-basis', 'claims/std-algebra.blade-basis', 'check.py::check_symbol_images_independent'), ('std-algebra.morita-amplification', 'claims/std-algebra.morita-amplification', 'check.py::check_centre_and_ideals_of_the_amplification'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_blade_table'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_anticommute_iff_orthogonal'), ('std-algebra.sylvester-inertia', 'claims/std-algebra.sylvester-inertia', 'check.py::check_inertia_under_congruence'), ('std-algebra.z2-grading', 'claims/std-algebra.z2-grading', 'check.py::check_parity_and_grade_range'), ('transport.units-span', 'claims/transport.units-span', 'check.py::check_every_element_is_a_sum_of_two_units'), ('transport.units-span', 'claims/transport.units-span', 'check.py::check_singular_sets_are_the_eigenvalues')]

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
