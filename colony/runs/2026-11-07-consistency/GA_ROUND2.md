# GA rewrite, round 2 (entities outside the first lists)

Same rules and bookkeeping as GA_REWRITE.md, with one change: an entity already version-bumped in this run (its
version is above the one in store/lock or the 8eef5a4 version) keeps its version; add your credit entry and note
to that version. Your list is the pattern-scan file below PLUS the non-owned entities that the readers name as
using non-GA language in their reports colony/runs/2026-11-07-consistency/consistency-R*.md and xsubject-R*.md
(search the For-Leon and GA sections for "differential forms", "tensor", "tractor components", "Cartan",
"connection forms", "Newman-Penrose", "spin coefficient", "metric", "Hodge", "Pauli", "gamma matrices",
"matrix reading", "complexification"): add each such id to your list if it is not on the other rewriter's list,
not in GA_OWNED.txt and not already handled (check ga-tensor.md, ga-forms.md, ga-matrices.md).
- gravity rewriter: colony/runs/2026-11-07-consistency/ga2_gravity.txt (tensor indices, forms, Hodge star,
  tractor components, line elements, Newman-Penrose and spin coefficients, connection forms).
- matrices rewriter: colony/runs/2026-11-07-consistency/ga2_matrices.txt (Pauli/Dirac/gamma matrices, matrix
  readings, explicit matrices that are not Gram/mass/numerical, unnamed complexifications).
Write ga2-<kind>.md and reply with counts and the Not-rewritten list. Before finishing, run one tp check (layers
1,2,3) filtered to your ids.
