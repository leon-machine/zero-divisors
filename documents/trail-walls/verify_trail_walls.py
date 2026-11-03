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
 "verify_T04.py": [
  "num:2.6",
  "num:3.1",
  "num:3.4",
  "num:4.2",
  "num:4.3",
  "num:4.4",
  "num:4.5",
  "num:5.2",
  "num:6.1",
  "num:6.2"
 ]
}
CHECKS = [('sheaf.local-freeness-constant-rank', 'claims/sheaf.local-freeness-constant-rank', 'check.py::check_constant_rank_sixteen_through_degeneration'), ('sheaf.local-freeness-constant-rank', 'claims/sheaf.local-freeness-constant-rank', 'check.py::check_structure_functions_polynomial_in_gram'), ('sheaf.degeneration-sheaf', 'claims/sheaf.degeneration-sheaf', 'check.py::check_wall_fibre_ideal_and_quotient'), ('sheaf.degeneration-sheaf', 'claims/sheaf.degeneration-sheaf', 'check.py::check_non_orthogonal_wall_fibres'), ('sheaf.degeneration-sheaf', 'claims/sheaf.degeneration-sheaf', 'check.py::check_ideal_supported_exactly_on_the_wall'), ('sheaf.degeneration-sheaf', 'claims/sheaf.degeneration-sheaf', 'check.py::check_physical_fibres_are_mat2_quaternions'), ('sheaf.exceptional-algebra-deformation-normal-cone', 'claims/sheaf.exceptional-algebra-deformation-normal-cone', 'check.py::check_rescaled_limit_and_signature'), ('sheaf.exceptional-algebra-deformation-normal-cone', 'claims/sheaf.exceptional-algebra-deformation-normal-cone', 'check.py::check_special_fibre_is_the_limit_algebra'), ('sheaf.exceptional-algebra-deformation-normal-cone', 'claims/sheaf.exceptional-algebra-deformation-normal-cone', 'check.py::check_limit_independent_of_choices'), ('sheaf.wall-gram', 'claims/sheaf.wall-gram', 'check.py::check_block_gram_and_determinant'), ('sheaf.wall-gram', 'claims/sheaf.wall-gram', 'check.py::check_hyperbolic_plane_and_orthocomplement'), ('sheaf.wall-gram', 'claims/sheaf.wall-gram', 'check.py::check_orthogonal_splitting_and_wall_signature'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_signature_constant_on_physical_side'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_wrong_coupling_sign_fails'), ('sheaf.one-sided-completion', 'claims/sheaf.one-sided-completion', 'check.py::check_fibres_locally_free_and_physical_type'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_cotangent_subalgebra_is_degenerate_algebra'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_off_wall_complement_is_hyperbolic_plane'), ('sheaf.localised-transport', 'claims/sheaf.localised-transport', 'check.py::check_ladder_pair_exists_exactly_on_wall'), ('sheaf.metrics-residue-square-root-twist', 'claims/sheaf.metrics-residue-square-root-twist', 'check.py::check_residue_is_inverse_transversality'), ('sheaf.metrics-residue-square-root-twist', 'claims/sheaf.metrics-residue-square-root-twist', 'check.py::check_residue_weights'), ('sheaf.metrics-residue-square-root-twist', 'claims/sheaf.metrics-residue-square-root-twist', 'check.py::check_partner_line_is_dual_to_dying_line'), ('sheaf.conservation-degeneracy-located', 'claims/sheaf.conservation-degeneracy-located', 'check.py::check_degeneracy_locus_is_the_zero_of_F'), ('sheaf.conservation-degeneracy-located', 'claims/sheaf.conservation-degeneracy-located', 'check.py::check_signatures_mu_nu_positive'), ('sheaf.conservation-degeneracy-located', 'claims/sheaf.conservation-degeneracy-located', 'check.py::check_signatures_mu_nu_negative_and_schwarzschild'), ('sheaf.conservation-degeneracy-located', 'claims/sheaf.conservation-degeneracy-located', 'check.py::check_no_two_sided_constant_signature'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_walls_displaced_successively'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_each_wall_is_a_simple_corank_one_zero'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_one_hyperbolic_plane_per_wall'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_radical_lines_have_global_sections'), ('primer.commutation-rule', 'claims/primer.commutation-rule', 'check.py::check_commutation_rule'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_blades_are_a_basis'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants_polynomial'), ('sheaf.determinant-identity-blow-up-expansion', 'claims/sheaf.determinant-identity-blow-up-expansion', 'check.py::check_schur_complement_and_determinant_identity'), ('sheaf.determinant-identity-blow-up-expansion', 'claims/sheaf.determinant-identity-blow-up-expansion', 'check.py::check_blow_up_expansion'), ('sheaf.imported-classification-values', 'claims/sheaf.imported-classification-values', 'check.py::check_five_values'), ('sheaf.imported-classification-values', 'claims/sheaf.imported-classification-values', 'check.py::check_centres_of_the_odd_values'), ('sheaf.invariant-form-t3', 'claims/sheaf.invariant-form-t3', 'check.py::check_radical_and_tangential_vanishing'), ('sheaf.invariant-form-t3', 'claims/sheaf.invariant-form-t3', 'check.py::check_independent_of_extension'), ('sheaf.invariant-form-t3', 'claims/sheaf.invariant-form-t3', 'check.py::check_scales_by_c_squared'), ('sheaf.resolution-ideal-theoretically', 'claims/sheaf.resolution-ideal-theoretically', 'check.py::check_partner_makes_unit_ideal'), ('sheaf.resolution-ideal-theoretically', 'claims/sheaf.resolution-ideal-theoretically', 'check.py::check_null_partner_needs_the_normalisation'), ('sheaf.resolution-ideal-theoretically', 'claims/sheaf.resolution-ideal-theoretically', 'check.py::check_degenerate_fibre_ideal_square_zero'), ('sheaf.tame-wall-induction', 'claims/sheaf.tame-wall-induction', 'check.py::check_shadow_wall_is_a_simple_regular_level_set'), ('sheaf.tame-wall-induction', 'claims/sheaf.tame-wall-induction', 'check.py::check_radical_line_is_an_adjugate_column'), ('sheaf.tame-wall-induction', 'claims/sheaf.tame-wall-induction', 'check.py::check_jacobi_formula_gives_transversality'), ('std-algebra.existence-uniqueness', 'claims/std-algebra.existence-uniqueness', 'check.py::check_model_squares_to_form'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_ideal_is_spanned_by_radical_blades'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_nilpotency_index_is_r_plus_one'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_quotient_is_clifford_algebra_of_reduced_space'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_j_is_the_largest_nilpotent_ideal'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_null_hyperplane_of_spacetime'), ('std-algebra.radical-ideal-and-quotient', 'claims/std-algebra.radical-ideal-and-quotient', 'check.py::check_non_diagonal_gram_matrices'), ('std-algebra.sylvester-inertia', 'claims/std-algebra.sylvester-inertia', 'check.py::check_inertia_under_congruence'), ('std-algebra.vector-squares', 'claims/std-algebra.vector-squares', 'check.py::check_anticommutator_is_twice_the_polar_form')]

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
