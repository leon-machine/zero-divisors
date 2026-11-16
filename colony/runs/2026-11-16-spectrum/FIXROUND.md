# Fix round, run 2026-11-16-spectrum (role: fixer in colony/BRIEF.md)

A blind referee has reviewed all five proposals. The report is `colony/runs/2026-11-16-spectrum/verify/R1.md`.
Read the sections for the proposals YOU filed, plus the closing sections "Overlaps and conflicts" and "The
physics, in one paragraph".

Numbering in the report: 1 = synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit (SA),
2 = synthesis.quasi-free-deposit-has-white-energy-noise-unless-pure-and-stationary (SA),
3 = synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape (SB),
4 = synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta (SB),
5 = synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise version 5 (SB).

## Leon's decisions (made during the referee round; they bind the wording)
- The descent slice is left free: no reading is adopted. The slice's local density parameter (equivalently its
  expansion datum) is recorded as a free datum of the descent. (UE) and (LC) stay named hypotheses, never
  postulates; no text may say or imply that the series holds one of them.
- The ceiling on the descent temperature under (UE) is a conditional, rough remark inside proposal 1 (no
  low-multipole analysis claimed; its closeness to the stored 7.3e8 GeV ceiling a coincidence, said once). The
  maintainer adds an attack item to the open problem for the proper analysis; do not write that yourself.
- "Deposit quanta lie below the Planck mass" stays a named hypothesis of proposal 4 only. Attack item 3 is then
  closed under the flat readings given that hypothesis and open under (UE): the title, one-liner and lay level of
  proposal 4 must say exactly that and no more.
- The four stored entries that use the flat reading without naming it will be reworded by the maintainer; your
  proposals may say what those stored texts state at their current versions, accurately, and nothing about the
  rewording.

## One convention for the readings (the referee's recommendation, adopted)
- (UE): uniform expansion of the slice. (LC): flat slice (local criticality). These are the two slice hypotheses,
  defined in proposal 1.
- (FR) := (LC) with the deposit at rest on the slice. (FM) := (LC) with the deposit's own longitudinal momentum
  noise. These are the two flat-slice readings.
- Proposal 4 renames (C0), (C1), (CA) to (FR), (FM), (UE). Proposal 2's hypothesis (C) becomes "(UE)" with
  gamma = 3/2, the gamma = 9/4 case kept as a named variant. Proposal 5 keeps (FR), (FM), (UE).
- Letters: v for the velocity relative to the slice normal; X = a_d H_d / k in statements; reserve kappa for the
  expansion perturbation of the slice (proposals 2 and 4 rename their other uses of kappa). The sign convention
  of the conserved amplitude is stated once in each proposal that uses it.

## For each of your proposals
1. Apply every fix the referee lists, in place in `proposals/<id>/`, at every level (title, one-liner, formal,
   technical, lay, proof, check). The two errors the referee names (the sign of H kappa in proposal 5's note;
   "beta = 0" under (CA) in proposal 4) are corrected, not footnoted.
2. OVERSTATED (proposal 3): restate to the referee's weaker true statement at every level, including the title
   if it claims more than the restated result. The counter-model (point placements that are not a lattice carry
   the placement's own structure factor through the c term) goes into the statement as the boundary of the
   result. If you think the referee is wrong, rebut only with a computation written into your fixes file.
3. Numerical results never appear above the proof text as established unless they are exact rational brackets
   that a check verifies.
4. Duplication: proposals 4 and 5 re-derive the three readings and the radiation-era projection from memory.
   Drop the re-derivation and cite proposal 1 in the text only ("filed alongside, <id>"); proposal ids are not
   store ids, so never put them in `uses`. Keep only what each proposal needs for its own clauses.
5. Pins to versions that exist only as proposals fail validation: keep the current stored pins and list the
   repins under "Repin on acceptance" in your fixes file (the referee lists them).
6. Maintainer-only items (assumes edges, new imported or postulate entities, status changes): do not do them;
   list them under "Decisions for Leon" only if they are not already decided above.
7. Store text must not mention attackers, referees, the run, other agents or the method. House style: no em
   dashes; never "honest"/"honestly"; never "load-bearing"; Q(v) for the square of a vector; macros only from
   store/notation.yaml; geometric algebra and Gauge Theory Gravity language.
8. Weak checks: where the referee shows a perturbation that still passes, strengthen the check so it fails.
9. After each proposal run ONLY `python3 colony/runcheck.py proposals/<id>/check.py`. Do NOT run check4.py or
   validate_draft: the orchestrator runs both centrally after the round and returns failures. Never kill other
   processes; never spawn agents; do not commit or push.

Write `colony/runs/2026-11-16-spectrum/findings/fixes-<SA|SB>.md`: per proposal, the verdict, what changed, the
runcheck result, "check4: pending (orchestrator)"; then "Repin on acceptance" and "Decisions for Leon". Your final
reply is a short summary of that file.
