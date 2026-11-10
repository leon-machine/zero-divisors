# Fix round, run 2026-11-09-solvable

Referee reports: colony/runs/2026-11-09-solvable/verify/R1.md and verify/R2.md. Read your proposals' sections in full; the
required fixes there are your fixes, with the overrides below. Apply every fix in place in proposals/<id>/ at every level
(title, one-liner, formal, technical, lay, proof, extraction note, check). OVERSTATED proposals are restated to the
referee's true weaker statement at every level; numbers never appear above the proof text that proves them. Keep every
stored file. Run ONLY `PYTHONDONTWRITEBYTECODE=1 python3 colony/runcheck.py proposals/<id>/check.py`; never check4,
validate_draft or tp check (the orchestrator reruns them centrally). Write findings/fixes-<name>.md with
"check4: pending (orchestrator)". Rebut a fix only with a computation. Do not edit store/, commit, push or spawn agents.

## Overrides (Leon's decisions and store rules)
1. No new imported Facts. Leon decided (this run) that the lens-space inputs (cohomology rings, T Sigma + R, q1 and p1,
   the K-ring, lambda-operations, Sq^1) are NOT imported. Instead state them in the formal statement as explicit
   hypotheses ("Given the classical facts (L1)-(L3), cited from memory and not in the store: ..."), so each result is a
   conditional theorem, and say in the extraction note that deriving them is an open item. The same for completeness of
   spinor harmonics and the exact/co-exact split (horizon channels). Existing stored Facts may be cited and pinned (for
   example synthesis.imported-whitney-product-formula-and-projective-space@1,
   synthesis.imported-brst-kugo-ojima-strocchi-and-gribov@1).
2. No new assumes edges in proposals (maintainer-only, E203). Where a referee asks to add a postulate to `assumes` (for
   example (Q)@3, the window reading, C2), do not add it: name it in the extraction note under "premises used, assumes edge
   for the maintainer" and the orchestrator will put it to Leon.
3. No proposal can cite another proposal (E201). Overlap rulings that ask one proposal to cite a sibling are done by the
   maintainer after acceptance: remove the duplicated content only where the referee says it is duplicated with no loss,
   otherwise keep it, and add one sentence in the extraction note naming the sibling id as the intended citation.
4. J3 caveat (R2 points 1, 2, 5; R1 point 3): the stored postulate hawking.joint-j3-s-wave-reduction reads integer-weight
   channels as currents of the arrays; Leon has decided to narrow it to spin 2 once the horizon-channel derivation is
   accepted. State every boson-counting reading relative to J3 as R2 says.

## Assignments
- C1A: synthesis.two-rungs-need-the-doubled-dying-line-stably-trivial (R1 1), synthesis.horizon-channels-of-scalar-dirac-and-maxwell-fields-are-two-dimensional (R1 3: the T~ repair with a parity test in the check; narrow the J3 claim).
- C1B: synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (R1 2).
- C2A: synthesis.field-level-brst-of-the-two-doublets-and-the-thooft-feynman-gauge (R1 4: the (1/2) kappa normalisation, xi, a kinetic-term check, the stationarity hypothesis), synthesis.joint-clifford-clause-is-an-instance-of-the-signed-direction-postulates (R1 8), synthesis.gauge-factor-sugawara-parts-satisfy-virasoro-relations-on-the-band (R1 6, optional fixes only).
- C2B: synthesis.higgs-sector-brst-does-not-fix-the-breaking-pattern-of-two-doublets (R1 5; align the doublet conventions with the field-level proposal: use its realisation), synthesis.koide-middle-mass-bound-closes-the-remaining-quark-dressing-class (R1 7).
- C3A: synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (R2 1).
- C3B: synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (R2 2, OVERSTATED: restate; the id stays).
- C4A: synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free (R2 3, OVERSTATED: restate to residues 3 and 5, with the U3 result at residues 1 and 7 stated as what fixes the window there; the id stays), synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (R2 4), synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (R2 5).
- C4B: synthesis.georgi-jarlskog-weight-free-on-the-stored-relations (R2 6), synthesis.d-term-level-free-at-fixed-n (R2 7).
