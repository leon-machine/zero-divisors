# Items for AP1 (from AP2)

Entities AP1 claimed in claimed-apply.txt on which AP2 has a decided item. Apply in your version bump and record each
in your maintainer_pass_decisions note.

## B1 consequence. synthesis.boost-evolution-on-generators-is-one-unitary-group (uses edge and check premise call)
- Why: Leon's answer 4 (B1) lowers scrambling.spreading-law-chaos-bound-saturated to conjectured (AP2 has applied it,
  version 5 -> 6). This result uses it (`scrambling.spreading-law-chaos-bound-saturated@5` in derivation main) only to
  restate its chaos-bound comparison ("The chaos-bound comparison of Assumption ... restated on this basis"), not as a
  premise of its own clauses. With the edge kept, its effective status drops to conjectured and layer 3 gives E204.
- Fix (as AP2 applied to synthesis.phase-flow-is-time-rotor-flow-kms-continuation, synthesis.number-diagonal-dynamics-
  spreads-nothing and synthesis.affine-cell-boost-spreads-without-scrambling): delete the line
  `  - scrambling.spreading-law-chaos-bound-saturated@5` from derivations/main/uses; delete the line
  `    premise("scrambling.spreading-law-chaos-bound-saturated")` from check.py (line 223, in the check that calls it),
  then runcheck; keep the \claimref in the formal and proof text as a citation for comparison. Note sentence: "Consequence
  of Leon's answer 4 (B1): scrambling.spreading-law-chaos-bound-saturated is now conjectured; this result restates its
  chaos-bound comparison and does not rest on its truth, so the uses edge becomes a text mention and the check's premise()
  call for it is removed."

## G8. scrambling.return-delay-scrambling-log-recovered
- Done by AP2 with B1 (same entity, version 2 -> 3): status conjectured, the modular-time sentence in the formal, flow_note
  rotor. Nothing for AP1 to do.

## D1. synthesis.schwarzschild-horizon-translations-are-no-conformal-symmetry (AP1 has A5 on it)
- Decision (DECISIONS D1, routine): repoint the citation of synthesis.positive-null-energy-gives-r-premises@7 (cited only
  for the dilation of its setup) to synthesis.null-vacuum-on-a-horizon-generator@1 (i): in derivations/main/uses replace
  `synthesis.positive-null-energy-gives-r-premises@7` by `synthesis.null-vacuum-on-a-horizon-generator@1`, and the
  matching \claimref in the formal/proof text (it should cite clause (i) of the null-vacuum result for the dilation).
  This drops (N+) from its holds_given. If its check.py calls premise("synthesis.positive-null-energy-gives-r-premises"),
  change it to premise("synthesis.null-vacuum-on-a-horizon-generator") and runcheck (E404 otherwise).
