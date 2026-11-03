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
 "verify_T11.py": [
  "label:thm:grip"
 ],
 "verify_T15.py": [
  "label:lem:breaking",
  "label:lem:s3",
  "label:prop:empty",
  "label:prop:leptogenesis",
  "label:prop:rankone",
  "label:prop:seesaw"
 ]
}
CHECKS = [('neutrino.empty-twistor', 'claims/neutrino.empty-twistor', 'check.py::check_single_spinor_singlets'), ('neutrino.empty-twistor', 'claims/neutrino.empty-twistor', 'check.py::check_anomaly_solution_set_is_the_span'), ('neutrino.empty-twistor', 'claims/neutrino.empty-twistor', 'check.py::check_ray_family_and_collapse'), ('neutrino.empty-twistor', 'claims/neutrino.empty-twistor', 'check.py::check_anomaly_invisible_on_the_lattice'), ('neutrino.seesaw-what-gauge-invariance-proves-what', 'claims/neutrino.seesaw-what-gauge-invariance-proves-what', 'check.py::check_cosmological_term_magnitudes'), ('neutrino.seesaw-what-gauge-invariance-proves-what', 'claims/neutrino.seesaw-what-gauge-invariance-proves-what', 'check.py::check_unique_neutral_bilinear'), ('neutrino.seesaw-what-gauge-invariance-proves-what', 'claims/neutrino.seesaw-what-gauge-invariance-proves-what', 'check.py::check_block_elimination'), ('neutrino.seesaw-what-gauge-invariance-proves-what', 'claims/neutrino.seesaw-what-gauge-invariance-proves-what', 'check.py::check_scalar_seesaw_bound'), ('neutrino.invariant-symmetric-matrices', 'claims/neutrino.invariant-symmetric-matrices', 'check.py::check_characterisation'), ('neutrino.invariant-symmetric-matrices', 'claims/neutrino.invariant-symmetric-matrices', 'check.py::check_spectrum_and_determinant'), ('neutrino.invariant-symmetric-matrices', 'claims/neutrino.invariant-symmetric-matrices', 'check.py::check_inverse_and_projector_forms'), ('neutrino.rank-one-seesaw-ordering-sum-double', 'claims/neutrino.rank-one-seesaw-ordering-sum-double', 'check.py::check_democratic_block_decomposition'), ('neutrino.rank-one-seesaw-ordering-sum-double', 'claims/neutrino.rank-one-seesaw-ordering-sum-double', 'check.py::check_normal_ordering'), ('neutrino.rank-one-seesaw-ordering-sum-double', 'claims/neutrino.rank-one-seesaw-ordering-sum-double', 'check.py::check_sum_and_floor'), ('neutrino.rank-one-seesaw-ordering-sum-double', 'claims/neutrino.rank-one-seesaw-ordering-sum-double', 'check.py::check_double_beta_values'), ('neutrino.breaking-relation', 'claims/neutrino.breaking-relation', 'check.py::check_exact_identity_and_majorana_only_breaking'), ('neutrino.breaking-relation', 'claims/neutrino.breaking-relation', 'check.py::check_reference_direction_scale'), ('neutrino.breaking-relation', 'claims/neutrino.breaking-relation', 'check.py::check_leading_order_compression_eigenvalues'), ('neutrino.breaking-relation', 'claims/neutrino.breaking-relation', 'check.py::check_instances_diagonalised_exactly'), ('neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'claims/neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'check.py::check_alignment_kills_decay_asymmetries'), ('neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'claims/neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'check.py::check_washout_strength_and_resonant_pair'), ('neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'claims/neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'check.py::check_real_breaking_kills_interference'), ('neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'claims/neutrino.leptogenesis-suppressed-alignment-reheating-premise-new', 'check.py::check_unification_above_heavy_scale'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_deformed_bracket_is_pairing_with_frozen_point'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_mass_is_grip_norm_identity_in_lambda'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_flat_shadow_is_symplectic_area'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_point_supported_composite'), ('mass.exact-join', 'claims/mass.exact-join', 'check.py::check_massless_locus'), ('neutrino.imported-ceiling-under-hypothesis-u-arrow', 'claims/neutrino.imported-ceiling-under-hypothesis-u-arrow', 'check.py::check_seesaw_inversion_and_light_root'), ('neutrino.imported-ceiling-under-hypothesis-u-arrow', 'claims/neutrino.imported-ceiling-under-hypothesis-u-arrow', 'check.py::check_two_ends_of_the_range'), ('neutrino.imported-derived-content-singlets', 'claims/neutrino.imported-derived-content-singlets', 'check.py::check_doublet_content'), ('neutrino.imported-derived-content-singlets', 'claims/neutrino.imported-derived-content-singlets', 'check.py::check_single_spinor_singlets'), ('neutrino.imported-derived-content-singlets', 'claims/neutrino.imported-derived-content-singlets', 'check.py::check_anomaly_conditions_hold_and_determine'), ('neutrino.imported-derived-content-singlets', 'claims/neutrino.imported-derived-content-singlets', 'check.py::check_z6_lattice'), ('neutrino.imported-indifference-faces-democratic-alignment-rank', 'claims/neutrino.imported-indifference-faces-democratic-alignment-rank', 'check.py::check_democratic_line_and_invariant_forms'), ('neutrino.imported-indifference-faces-democratic-alignment-rank', 'claims/neutrino.imported-indifference-faces-democratic-alignment-rank', 'check.py::check_rank_one_spectrum'), ('neutrino.imported-indifference-faces-democratic-alignment-rank', 'claims/neutrino.imported-indifference-faces-democratic-alignment-rank', 'check.py::check_s3_protects_light_pair')]

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
