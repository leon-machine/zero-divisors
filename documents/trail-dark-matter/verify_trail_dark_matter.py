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
 "verify_T14.py": [
  "label:cor:whocarries",
  "label:fact:sminputs",
  "label:lem:projection",
  "label:prop:audit",
  "label:prop:count",
  "label:prop:massbound",
  "label:prop:residues",
  "label:thm:mirror",
  "label:thm:soldered",
  "label:thm:types"
 ],
 "verify_T14c.py": [
  "id:A1",
  "id:A2",
  "id:A3",
  "id:A4",
  "id:A5",
  "id:B4",
  "id:B5",
  "id:B6",
  "id:B7",
  "id:C1",
  "id:C2",
  "id:D10",
  "id:D11",
  "id:D12",
  "id:D1a",
  "id:D1b",
  "id:D2",
  "id:D3",
  "id:D4",
  "id:D5",
  "id:D6",
  "id:D7",
  "id:D8",
  "id:D9",
  "id:E1",
  "id:E2",
  "id:E3",
  "id:E4",
  "id:F2"
 ]
}
CHECKS = [('dark-matter.towers-are-residues-single-clock-filter', 'claims/dark-matter.towers-are-residues-single-clock-filter', 'check.py::check_towers_are_the_eight_residues'), ('dark-matter.towers-are-residues-single-clock-filter', 'claims/dark-matter.towers-are-residues-single-clock-filter', 'check.py::check_reversal_convention_and_types'), ('dark-matter.towers-are-residues-single-clock-filter', 'claims/dark-matter.towers-are-residues-single-clock-filter', 'check.py::check_census_lowest_causal'), ('dark-matter.towers-are-residues-single-clock-filter', 'claims/dark-matter.towers-are-residues-single-clock-filter', 'check.py::check_sort_under_p3'), ('dark-matter.towers-are-residues-single-clock-filter', 'claims/dark-matter.towers-are-residues-single-clock-filter', 'check.py::check_window_sensitivity'), ('dark-matter.mirror-tower-copy-one', 'claims/dark-matter.mirror-tower-copy-one', 'check.py::check_even_subalgebras_and_spin_groups_agree'), ('dark-matter.mirror-tower-copy-one', 'claims/dark-matter.mirror-tower-copy-one', 'check.py::check_complexified_fibres_and_ground_types'), ('dark-matter.mirror-tower-copy-one', 'claims/dark-matter.mirror-tower-copy-one', 'check.py::check_standard_model_running_and_mean_mass_ratio'), ('dark-matter.mirror-tower-copy-one', 'claims/dark-matter.mirror-tower-copy-one', 'check.py::check_p2_caveat_mirror_at_our_temperature'), ('dark-matter.superselected-hence-dark-exactly-stable', 'claims/dark-matter.superselected-hence-dark-exactly-stable', 'check.py::check_ascent_preserves_residue'), ('dark-matter.superselected-hence-dark-exactly-stable', 'claims/dark-matter.superselected-hence-dark-exactly-stable', 'check.py::check_completion_is_matrix_amplification'), ('dark-matter.superselected-hence-dark-exactly-stable', 'claims/dark-matter.superselected-hence-dark-exactly-stable', 'check.py::check_no_soldered_map_between_residues'), ('dark-matter.population-count-one-share-half-percent', 'claims/dark-matter.population-count-one-share-half-percent', 'check.py::check_asymmetric_share_is_the_mirror_alone'), ('dark-matter.population-count-one-share-half-percent', 'claims/dark-matter.population-count-one-share-half-percent', 'check.py::check_observed_ratio_and_uncertainty'), ('dark-matter.population-count-one-share-half-percent', 'claims/dark-matter.population-count-one-share-half-percent', 'check.py::check_remainder'), ('dark-matter.population-count-one-share-half-percent', 'claims/dark-matter.population-count-one-share-half-percent', 'check.py::check_unit_ball_expression_returns_the_remainder'), ('dark-matter.unit-ball-rule', 'claims/dark-matter.unit-ball-rule', 'check.py::check_shares'), ('dark-matter.unit-ball-rule', 'claims/dark-matter.unit-ball-rule', 'check.py::check_dark_towers_and_dimensions'), ('dark-matter.unit-ball-rule', 'claims/dark-matter.unit-ball-rule', 'check.py::check_total'), ('dark-tower-matter.gauge-algebras', 'claims/dark-tower-matter.gauge-algebras', 'check.py::check_three_dimensional_algebra_is_so2_plus_so2'), ('dark-tower-matter.gauge-algebras', 'claims/dark-tower-matter.gauge-algebras', 'check.py::check_three_dimensional_global_form'), ('dark-tower-matter.gauge-algebras', 'claims/dark-tower-matter.gauge-algebras', 'check.py::check_five_dimensional_algebra_is_u3'), ('dark-matter.imported-eight-towers-mod-8-clock', 'claims/dark-matter.imported-eight-towers-mod-8-clock', 'check.py::check_ascent_is_matrix_amplification_one_step'), ('dark-matter.imported-eight-towers-mod-8-clock', 'claims/dark-matter.imported-eight-towers-mod-8-clock', 'check.py::check_ascent_is_matrix_amplification_two_steps'), ('dark-matter.imported-eight-towers-mod-8-clock', 'claims/dark-matter.imported-eight-towers-mod-8-clock', 'check.py::check_period_eight'), ('dark-matter.imported-eight-towers-mod-8-clock', 'claims/dark-matter.imported-eight-towers-mod-8-clock', 'check.py::check_eight_towers'), ('dark-matter.imported-inputs-standard-model-chain', 'claims/dark-matter.imported-inputs-standard-model-chain', 'check.py::check_even_subalgebra_is_mat4_c'), ('dark-matter.imported-inputs-standard-model-chain', 'claims/dark-matter.imported-inputs-standard-model-chain', 'check.py::check_helicity_form_lives_on_the_twistor_ideal'), ('dark-matter.imported-inputs-standard-model-chain', 'claims/dark-matter.imported-inputs-standard-model-chain', 'check.py::check_mass_formula_identity'), ('dark-matter.imported-inputs-standard-model-chain', 'claims/dark-matter.imported-inputs-standard-model-chain', 'check.py::check_fock_module_is_irreducible_spinor_module'), ('dark-matter.mirror-share-one-how-fragile', 'claims/dark-matter.mirror-share-one-how-fragile', 'check.py::check_mean_mass_per_baryon_share'), ('dark-matter.mirror-share-one-how-fragile', 'claims/dark-matter.mirror-share-one-how-fragile', 'check.py::check_one_loop_bound_and_chain'), ('dark-matter.mirror-share-one-how-fragile', 'claims/dark-matter.mirror-share-one-how-fragile', 'check.py::check_one_flavour_factors_over_the_ceiling_range'), ('dark-matter.mirror-share-one-how-fragile', 'claims/dark-matter.mirror-share-one-how-fragile', 'check.py::check_coupling_departure_window'), ('dark-matter.no-coupling-rule-odd-towers-follows', 'claims/dark-matter.no-coupling-rule-odd-towers-follows', 'check.py::check_coupling_is_dimensionful_off_four'), ('dark-matter.no-coupling-rule-odd-towers-follows', 'claims/dark-matter.no-coupling-rule-odd-towers-follows', 'check.py::check_odd_towers_off_the_reversal_orbit'), ('dark-matter.projection-every-towers-content-dilutes-ones', 'claims/dark-matter.projection-every-towers-content-dilutes-ones', 'check.py::check_projected_dilution_matches_this_tower'), ('dark-matter.projection-every-towers-content-dilutes-ones', 'claims/dark-matter.projection-every-towers-content-dilutes-ones', 'check.py::check_single_sheet_reading_is_excluded'), ('dark-matter.radiation-audit-what-theorem-closes-what', 'claims/dark-matter.radiation-audit-what-theorem-closes-what', 'check.py::check_one_photon_like_species_breaks_the_cap'), ('dark-matter.radiation-audit-what-theorem-closes-what', 'claims/dark-matter.radiation-audit-what-theorem-closes-what', 'check.py::check_ground_level_and_vector_like_odd_towers'), ('dark-matter.radiation-audit-what-theorem-closes-what', 'claims/dark-matter.radiation-audit-what-theorem-closes-what', 'check.py::check_closing_margins_on_the_interval'), ('dark-matter.radiation-audit-what-theorem-closes-what', 'claims/dark-matter.radiation-audit-what-theorem-closes-what', 'check.py::check_mirror_atomic_cross_section'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_signature_is_read_off_the_generating_subspace'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_abstract_isomorphisms_not_soldered'), ('dark-matter.residue-soldered-invariant-not-algebraic-one', 'claims/dark-matter.residue-soldered-invariant-not-algebraic-one', 'check.py::check_this_world_and_r4_are_mat2_quaternions'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_type_table_on_p3_representatives'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_type_is_a_residue_invariant'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_intrinsic_groups'), ('dark-matter.type-residue-what-each-tower-can', 'claims/dark-matter.type-residue-what-each-tower-can', 'check.py::check_volume_element_on_the_odd_residues'), ('dark-matter.which-towers-can-carry-arrow', 'claims/dark-matter.which-towers-can-carry-arrow', 'check.py::check_oriented_and_causal_towers'), ('dark-matter.which-towers-can-carry-arrow', 'claims/dark-matter.which-towers-can-carry-arrow', 'check.py::check_fork_conformal_spinors_are_real'), ('dark-matter.which-towers-can-carry-arrow', 'claims/dark-matter.which-towers-can-carry-arrow', 'check.py::check_mass_begins_at_two_on_the_fork'), ('dark-tower-matter.constituents-field', 'claims/dark-tower-matter.constituents-field', 'check.py::check_fields_by_corner_at_both_levels'), ('dark-tower-matter.constituents-field', 'claims/dark-tower-matter.constituents-field', 'check.py::check_fields_by_direct_commutant'), ('dark-tower-matter.constituents-field', 'claims/dark-tower-matter.constituents-field', 'check.py::check_field_is_not_a_function_of_omega_squared'), ('dark-tower-matter.ladder', 'claims/dark-tower-matter.ladder', 'check.py::check_unitary_mixings_preserve_momentum'), ('dark-tower-matter.ladder', 'claims/dark-tower-matter.ladder', 'check.py::check_only_unitary_mixings'), ('dark-tower-matter.ladder', 'claims/dark-tower-matter.ladder', 'check.py::check_momentum_preserving_groups'), ('dark-tower-matter.pairs', 'claims/dark-tower-matter.pairs', 'check.py::check_real_witt_index'), ('dark-tower-matter.pairs', 'claims/dark-tower-matter.pairs', 'check.py::check_complex_witt_index'), ('dark-tower-matter.pairs', 'claims/dark-tower-matter.pairs', 'check.py::check_unit_fixed_up_to_sign'), ('dark-tower-matter.third-pairs-unit-five-dimensions', 'claims/dark-tower-matter.third-pairs-unit-five-dimensions', 'check.py::check_r3_unit_and_three_pairs'), ('dark-tower-matter.third-pairs-unit-five-dimensions', 'claims/dark-tower-matter.third-pairs-unit-five-dimensions', 'check.py::check_r3_units_anticommuting_with_i7'), ('dark-tower-matter.third-pairs-unit-five-dimensions', 'claims/dark-tower-matter.third-pairs-unit-five-dimensions', 'check.py::check_r5_no_canonical_unit'), ('dark-tower-matter.third-pairs-unit-five-dimensions', 'claims/dark-tower-matter.third-pairs-unit-five-dimensions', 'check.py::check_r5_third_pair_for_every_unit'), ('dark-tower-matter.third-pairs-unit-five-dimensions', 'claims/dark-tower-matter.third-pairs-unit-five-dimensions', 'check.py::check_r5_units_conjugate'), ('dark-tower-matter.where-mass-begins', 'claims/dark-tower-matter.where-mass-begins', 'check.py::check_dimensions_three_four_pair_law'), ('dark-tower-matter.where-mass-begins', 'claims/dark-tower-matter.where-mass-begins', 'check.py::check_dimension_five_single_law'), ('dark-tower-matter.where-mass-begins', 'claims/dark-tower-matter.where-mass-begins', 'check.py::check_momenta_in_one_half_space'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_walls_displaced_successively'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_each_wall_is_a_simple_corank_one_zero'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_one_hyperbolic_plane_per_wall'), ('sheaf.infinite-wall-sequence', 'claims/sheaf.infinite-wall-sequence', 'check.py::check_radical_lines_have_global_sections')]

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
