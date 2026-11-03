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
 ]
}
CHECKS = [('std-algebra.vector-squares', 'claims/std-algebra.vector-squares', 'check.py::check_anticommutator_is_twice_the_polar_form'), ('std-algebra.blade-basis', 'claims/std-algebra.blade-basis', 'check.py::check_symbol_images_independent'), ('std-algebra.involution-properties', 'claims/std-algebra.involution-properties', 'check.py::check_involutions_on_products_and_grades'), ('primer.centre', 'claims/primer.centre', 'check.py::check_centre_by_linear_algebra'), ('primer.centre', 'claims/primer.centre', 'check.py::check_central_blades_higher_n'), ('std-algebra.reflection', 'claims/std-algebra.reflection', 'check.py::check_sandwich_is_reflection'), ('std-algebra.spin-double-cover', 'claims/std-algebra.spin-double-cover', 'check.py::check_spin_homomorphism_and_kernel'), ('std-algebra.spin-double-cover', 'claims/std-algebra.spin-double-cover', 'check.py::check_kernel_is_plus_minus_one'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_hyperbolic_partner_in_a_plane'), ('std-algebra.witt-decomposition', 'claims/std-algebra.witt-decomposition', 'check.py::check_witt_decomposition_and_maximal_null_subspace'), ('std-algebra.periodicity', 'claims/std-algebra.periodicity', 'check.py::check_small_tensor_identities'), ('std-algebra.periodicity', 'claims/std-algebra.periodicity', 'check.py::check_table_invariants'), ('std-algebra.periodicity', 'claims/std-algebra.periodicity', 'check.py::check_periodicity_of_the_invariant'), ('std-algebra.witt-basis-car', 'claims/std-algebra.witt-basis-car', 'check.py::check_null_pairs_satisfy_the_car'), ('std-algebra.fock-representation', 'claims/std-algebra.fock-representation', 'check.py::check_wedge_and_contraction_give_the_whole_matrix_algebra'), ('std-algebra.fock-representation', 'claims/std-algebra.fock-representation', 'check.py::check_fock_space_is_the_left_ideal_of_the_vacuum'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_tau_is_automorphism_and_twisted_adjoint'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_vector_is_reflection'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_kernel_is_plus_minus_one'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_surjectivity_samples'), ('std-algebra.cartan-dieudonne', 'claims/std-algebra.cartan-dieudonne', 'check.py::check_isometries_factor_into_reflections'), ('std-algebra.cartan-dieudonne', 'claims/std-algebra.cartan-dieudonne', 'check.py::check_degenerate_counterexample'), ('std-algebra.cl11-matrix', 'claims/std-algebra.cl11-matrix', 'check.py::check_hyperbolic_plane_is_m2r'), ('std-algebra.existence-uniqueness', 'claims/std-algebra.existence-uniqueness', 'check.py::check_model_squares_to_form'), ('std-algebra.functoriality', 'claims/std-algebra.functoriality', 'check.py::check_isometry_extends_multiplicatively'), ('std-algebra.grade-decomposition', 'claims/std-algebra.grade-decomposition', 'check.py::check_antisymmetrised_products_have_one_grade'), ('std-algebra.inverse-of-vector', 'claims/std-algebra.inverse-of-vector', 'check.py::check_invertible_iff_nonnull'), ('std-algebra.inverse-of-vector', 'claims/std-algebra.inverse-of-vector', 'check.py::check_versor_norm'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_blade_table'), ('std-algebra.orthogonal-anticommute', 'claims/std-algebra.orthogonal-anticommute', 'check.py::check_anticommute_iff_orthogonal'), ('std-algebra.polarisation', 'claims/std-algebra.polarisation', 'check.py::check_polarisation'), ('std-algebra.sylvester-inertia', 'claims/std-algebra.sylvester-inertia', 'check.py::check_inertia_under_congruence'), ('std-algebra.tensor-rules', 'claims/std-algebra.tensor-rules', 'check.py::check_tensor_rule'), ('std-algebra.z2-grading', 'claims/std-algebra.z2-grading', 'check.py::check_parity_and_grade_range')]

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
