# Restater T1: sweep section 1 (B1 to B22 except B14) and C1, C2

Run 2026-11-08-frozen-point-datum, Stage 2. Every proposal is the next version of the stored entity (same id), built
from a copy of the stored folder; edit scripts work/T1/bNN.py (helpers work/T1/rt.py, gate work/T1/gate.sh); logs in
verify/final/T1-<id>.*.log and verify/final/<id>.validate.json. Hand-made folders moved aside to work/T1/aside/.

## Route
propose_claim ACCEPTS a higher version of a stored id: it reports `replaces_existing: true`, runs the amendment rules
(E603 to E608: credit kept and extended, an `amendments` entry with kind and defect) and registers the folder. Tried
first on synthesis.de-sitter-static-boost-frozen-point (verify/final/T1-synthesis.de-sitter-static-boost-frozen-point.propose.log).
Every proposal below is registered that way; coverage.yaml (and nothing else: propose_claim writes entity.md, proofs
and check.py, which were compared identical with cmp) was copied back. `tp accept --update` keeps stored-only files
(orig-proof-main.tex).
Each entity carries: the maintainer note extraction.maintainer_pass_2026_11_08 (by: ai-maintainer-pass), the credit
entry {Claude Opus 5.5, restated with H as the rational datum, v+1, run 2026-11-08-frozen-point-datum}, and an
`amendments` entry {version v+1, kind restatement, defect, evidence} (required by validate_draft for a raised version:
E605).

## Per id
