# fixes-WB: fix round step 1, run 2026-11-10-phase2

Proposal: proposals/synthesis.window-energy-tests-with-free-spacing-admit-twists-half-third-and-quarter (id unchanged).
Referee: verify/R3.md section 3, SOUND WITH FIXES. All eight items applied except the sibling citations (step 2).
No rebuttal. runcheck: 5/5 functions pass. check4: pending (orchestrator). validate: pending (orchestrator).

| R3 item | fix | where |
|---|---|---|
| 1 conclusion partly stored | synthesis.q-splits-maximum-entropy-affine-weights@6 added to `uses`, cited by claimref in the closing sentence and the proof; novelty narrowed to "the two energy equalities do not fix the slope" (they admit beta c = 2 pi, 4 pi, 2 pi sqrt(3/2)) | extraction note, formal closing, technical, lay, one-liner, proof; premise() in the parity check |
| 2 only twist 1/3 is independent | title now "Window energy tests with free spacing also admit the half-arrays and an array at twist 1/3" (90 characters); heading of (ii) reworded; sentence "the second is one particle-hole half of the first (its even or odd sublattice) ... the third is the only new one" in (ii), technical, lay, one-liner, note | entity.md |
| 3 entropy conclusion rests on one point | closing sentence says the entropy per unit Killing time differs only through (sqrt(2/3), 1/3), which fails the parity clause and the stored evenness criterion | formal closing, technical, lay |
| 4 univalence | Remark 2, not a clause, worded as the referee rules: odd resonance 1/3 + 4/3 - 5/3 = 0, criterion fails, stationary non-even states exist, the array is not excluded (Gibbs state even by clause 2); also "the flow at one modular period is not a constant phase at all" in (iv). synthesis.univalence-from-even-stationary-dynamics@5 added to `uses`; new check function check_odd_resonance_at_twist_one_third (in checked_by and coverage.yaml) | entity.md, proof, check.py, coverage.yaml |
| 5 exhaustiveness wording | lay: "at least three ... (a numerical scan finds no more, which is not a proof)"; technical: "examined by a numerical scan only, not proved"; one-liner: "no fourth point is found by a numerical scan (computed, not proved)"; Remark 1 kept outside the theorem | entity.md |
| 6 "assume no reading" | labelled argued at clause level, with the cone's contents ((Q), (N+), J3, the window reading) named, in formal, proof and note. No assumes edge added; left to the maintainer as before | entity.md, proof |
| 7 sibling citations | NOT done (step 2). The note names both siblings as intended citations: the base for twist 1/2 at general r, the twist-integral proposal for the product into halves | extraction note |
| 8 literature flags | kept "from memory" | unchanged |

Things the orchestrator's gate may flag:
- coverage.yaml lists the new check under clause label "Remark 2"; if the validator wants a clause of the theorem,
  "(iv)" is the nearest (the remark comments on the points of (ii) and (iv)).
- The mutation test has not been run on the new check function (fixers do not run check4). Its literals are the
  resonance triple and the sample range.
- The stored evenness theorem is stated for finitely many modes; the remark applies it to a finite set containing
  the three resonant modes, and says so in the proof.

Maintainer note passed on from R3 (outside the proposal): the window reading's "What it is for (i)" and refutation
condition (b) should carry "at spacing kappa" if this result is accepted.
