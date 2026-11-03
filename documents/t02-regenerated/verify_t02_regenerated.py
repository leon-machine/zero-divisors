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
 "verify_T02.py": [
  "num:2.3",
  "num:2.5"
 ],
 "verify_T04.py": [
  "num:2.6"
 ]
}
CHECKS = [('conformal.blade-basis-persists-under-degeneracy', 'claims/conformal.blade-basis-persists-under-degeneracy', 'check.py::check_blades_form_a_basis_for_any_form_and_basis'), ('conformal.minimal-nondegenerate-completion', 'claims/conformal.minimal-nondegenerate-completion', 'check.py::check_no_completion_below_m_plus_r'), ('conformal.minimal-nondegenerate-completion', 'claims/conformal.minimal-nondegenerate-completion', 'check.py::check_minimal_completions_signature'), ('conformal.minimal-nondegenerate-completion', 'claims/conformal.minimal-nondegenerate-completion', 'check.py::check_minimal_completion_unique_fixing_w'), ('conformal.minimal-nondegenerate-completion', 'claims/conformal.minimal-nondegenerate-completion', 'check.py::check_embedding_into_cl_p_plus_r_q_plus_r'), ('conformal.nilpotent-ideal-becomes-unit-ideal', 'claims/conformal.nilpotent-ideal-becomes-unit-ideal', 'check.py::check_radical_ideal_dimension_and_nilpotency'), ('conformal.nilpotent-ideal-becomes-unit-ideal', 'claims/conformal.nilpotent-ideal-becomes-unit-ideal', 'check.py::check_model_completion_unit_ideal'), ('conformal.nilpotent-ideal-becomes-unit-ideal', 'claims/conformal.nilpotent-ideal-becomes-unit-ideal', 'check.py::check_any_completion_unit_ideal_hyperbolic_partner'), ('conformal.principal-case', 'claims/conformal.principal-case', 'check.py::check_minimal_completion_is_cga'), ('conformal.principal-case', 'claims/conformal.principal-case', 'check.py::check_completion_unique_fixing_v'), ('conformal.principal-case', 'claims/conformal.principal-case', 'check.py::check_pga_embeds_in_cga'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_blades_are_a_basis'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants'), ('sheaf.blade-basis-degenerate-forms-included', 'claims/sheaf.blade-basis-degenerate-forms-included', 'check.py::check_structure_constants_polynomial'), ('std-algebra.functoriality', 'claims/std-algebra.functoriality', 'check.py::check_isometry_extends_multiplicatively'), ('std-algebra.vector-squares', 'claims/std-algebra.vector-squares', 'check.py::check_anticommutator_is_twice_the_polar_form')]

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
