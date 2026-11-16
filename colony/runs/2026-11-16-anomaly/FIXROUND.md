# Fix round, run 2026-11-16-anomaly

Two blind referees (Claude Opus 5.5) have reported: verify/R1.md (the two strong-CP proposals and the B - L
proposal) and verify/R2.md (the two order-four proposals). You may now read both. Role: fixer (BRIEF.md).

Rules
- Apply every referee fix in place in proposals/<id>/ (entity.md at every level: title, one-liner, formal,
  technical, lay; proof-main.tex; check.py). An OVERSTATED proposal is restated to the weaker true statement at
  every level, title included; if the title changes so that the id no longer describes the result, keep the id
  (the orchestrator flags the restatement for Leon) unless the referee's statement needs a new one.
- Rebut a referee only with a computation, recorded in your fixes file.
- Tighten every check the referee found vacuous, tautological or hard-coded: the check must compute the thing.
  Remove premise() calls from check functions that do not use the premise.
- Nothing is promoted: argued stays argued. Numbers never appear above the proof text that derives them.
- Run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`. Never check4.py, validate_draft or tp check (the
  orchestrator runs them centrally afterwards and returns failures). Do not edit store/, do not commit.
- House style as in BRIEF.md.
- Write colony/runs/2026-11-16-anomaly/findings/fixes-<your-name>.md: per proposal, each referee point and what
  you did (fixed / rebutted with which computation / not applicable and why), ending "check4: pending
  (orchestrator)". Add any new decision for Leon the fixes create.

Orchestrator's notes on particular points
- Colour-angle proposal (OVERSTATED). Restate: "relaxed by no stored field" becomes a statement about the rung
  field's coupling with both family matrices invertible, with completeness over the store's fields labelled
  argued; "reversed only by orientation-reversing maps" is restricted to maps induced by vector isometries (the
  duality rotation is the counterexample); the mirror clause states the choice of isomorphism it depends on (or
  is weakened to what holds for both choices); the hypothesis that the stored conjugation acts on colour by an
  automorphism is named; the list of stored maps is extended by the ones the referee names (each fixes the term).
- Determinant-phase proposal. The sign rule of the quarter-turn clause is wrong for negative delta_q (referee's
  counterexample): state the rule that is true for every sign, or state the hypothesis, and add the
  counterexample to the check. State c_q real as a hypothesis. Say at the formal level that a half turn of the
  physical angle conserves CP and is not excluded by the stored linear neutron bound (cite the source the referee
  checked), so "real determinant" is two cases with different status.
- B - L proposal. Name the mixed gravitational pairing of B - L on the fifteen states (trace -1 per family
  without the singlet) as a channel, with what is known of its rate labelled as literature or argued. The doublet
  count is argued: say so in the one-liner and lay text. Replace the vacuous doublet-mass assertion in the check.
- Spectral-asymmetry proposal. Add a named background clause for the classical analysis used (essential
  self-adjointness of the Dirac operator on a closed manifold, density, the Mellin lemma), in the manner of the
  stored lens-space theorem's (G); compute the parity sign pattern in the check instead of hard-coding it; drop
  the unused slot-statistics premise calls; "per component of the sixteen" in place of "per Weyl component";
  "matched with" in place of "identified with" for J and I; credit the Clifford-analysis literature for the
  Fischer decomposition.
- Order-four-structure proposal. Correct Reading (b): the forcing at a stage with the abelian factor gauged comes
  from the imported anomaly coefficients applied to X (sum 0 on sixteen, -5 on fifteen), not from the
  neutral-singlet theorem, which says u(5) leaves the bit free. Say that the modulus 16 is intrinsic to the
  arithmetic of the involutions (counts differ by 16) if you can prove it as the referee did; add the conjugacy
  sentence for the maximal torus; align the naming of 1/16 (xi) and 1/8 (the asymmetry) with the other proposal;
  replace the tautological lens-space check by a computation. State plainly which branch of the problem's success
  clause the pair reaches and at what level: branch 1 conditional on the unimported statement (and true for three
  generations, not for every generation number), branch 2 argued.
