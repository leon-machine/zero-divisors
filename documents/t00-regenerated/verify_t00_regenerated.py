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
  "num:9.2",
  "num:9.6"
 ]
}
CHECKS = [('primer.commutation-rule', 'claims/primer.commutation-rule', 'check.py::check_commutation_rule'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_tau_is_automorphism_and_twisted_adjoint'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_vector_is_reflection'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_kernel_is_plus_minus_one'), ('primer.twisted-adjoint-action', 'claims/primer.twisted-adjoint-action', 'check.py::check_surjectivity_samples'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_classification_table'), ('primer.classification-real-clifford-algebras', 'claims/primer.classification-real-clifford-algebras', 'check.py::check_split_summands_isomorphic_and_simple'), ('primer.centre', 'claims/primer.centre', 'check.py::check_centre_by_linear_algebra'), ('primer.centre', 'claims/primer.centre', 'check.py::check_central_blades_higher_n'), ('primer.sign', 'claims/primer.sign', 'check.py::check_omega_square'), ('primer.sign', 'claims/primer.sign', 'check.py::check_exponent_parity_identity'), ('primer.splitting-along-hyperbolic-plane', 'claims/primer.splitting-along-hyperbolic-plane', 'check.py::check_hyperbolic_pair_and_plane_basis'), ('primer.splitting-along-hyperbolic-plane', 'claims/primer.splitting-along-hyperbolic-plane', 'check.py::check_unique_split_expansion'), ('primer.splitting-along-hyperbolic-plane', 'claims/primer.splitting-along-hyperbolic-plane', 'check.py::check_left_mult_by_v_injective')]

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
