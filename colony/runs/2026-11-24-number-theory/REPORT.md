# Report, run 2026-11-24-number-theory

Request (Leon, 24 November): where does number theory cross-pollinate with the open problems of the graph; then
"work on all of them, and work in GA where possible". Lean method: one attacker, one blind referee (Claude Opus
5.5), one fix round. Branch run/2026-11-24-number-theory from main at 58338e0.

## State
Five results, refereed blind (all five SOUND WITH FIXES), fixes applied, evidence gate clean on each (0 errors;
logs in verify/check4-final/). With Leon's permission of 24 November they are placed in `store/claims/` on this
branch and submitted as one pull request; nothing reaches main until he merges. Bookkeeping paragraphs are added
to op.positivity-of-values, op.wall-class-invariant and op.residue-killing-weights. No stored entity is edited.
Checks run in the workspace: layers 1 to 3 of the whole store before and after (0 errors, 0 warnings both
times); layer 4 with the mutation test on the five new entities in place (0 errors, five "weak under
perturbation" warnings); the 22 check functions rerun from the store. A full layer-4 run of the whole store was
not completed in the workspace; the pull request's required check runs it. Lock, layer-4 record and site data
are left for the merge.

## Results (each labelled)
1. synthesis.positive-rationals-are-the-squares-of-the-even-subalgebra-of-cl-three (proved; classical).
   Lagrange's theorem by the descent x -> x y~/m in the even subalgebra of Cl_Q(3,0); Q has one ordering and its
   positive cone is {x x~}; no rational bivector squares to -7; positive semidefinite rational matrices are sums
   of at most 4n squares y y^T. Transport-absent.
2. synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four (proved, given the
   stored theorem for size four). Additive weights on the symmetric idempotents of M_n(Q) are linear for every
   n >= 4, so for two or more modes; with the sign condition they are the states of (P). The first step named in
   the stored note is false (e_1 and e_2+e_3+e_4+2e_5; the number 7). For one mode the statement is false
   (referee's counterexample, now checked). Rests entirely on the stored two-mode theorem (review: draft).
3. synthesis.order-of-the-doubled-dying-line-on-quarter-turn-lens-walls-is-a-valuation-in-the-ring-of-the-
   quarter-turn (proved). ord(1 - chi^2) = 2^ceil(n/2) in the stored K-ring for every n, by 2 = J(J-1)^2 in Z[J];
   rung bound k >= 1 + ceil(n/2) for every n (conditional, as stored, on the lambda-operations); order
   2^ceil(2n/N) for the N-th turn, N a power of two.
4. synthesis.thermal-test-on-the-ground-conic-holds-at-exactly-three-points (proved; signs machine-verified by
   integer interval arithmetic). No fourth array passes both energy tests: Remark 1 of the stored theorem is a
   theorem.
5. synthesis.character-sums-over-the-twist-fibres-of-an-array-are-dirichlet-l-values (proved given three
   classical hypotheses). A dictionary: 2L(0, chi) and -L(-1, chi)/M. No constraint, no prediction.

## Routes that failed
- Twisted spectral asymmetries on the lens spaces: they give the same order and nothing beyond complex K-theory;
  q_1 stays the input on L^5(4).
- Invariance under the whole modular group of the window: nothing beyond the stored recurrences.
- Withdrawn: "Euler products belong to the algebras without zero divisors" (false as stated).
- The Riemann hypothesis and mass: not reopened; the six notes of 29 September stand.

## Referee
verify/referee-R1.md. Two findings of substance: the weights theorem overclaimed at one mode (title and clause
(iv); fixed, id renamed), and the L-value result had a wrong divisibility hypothesis in clause (v) (fixed).
Smaller fixes in the other three, all applied. The referee did not re-referee the stored two-mode theorem.

## Decisions for Leon
1. Merge the pull request, or ask for any of the five to be dropped from it first.
2. Whether result 2 should wait for a line-by-line review of the stored two-mode theorem it rests on, and for
   Mushtari (2001) to be read.
3. Import Stolz (1989) as a Fact for the definite-side rung counts of all quarter-turn lens walls
   (m+1, m+2, m+3 by m modulo 8, m = n+1; agrees with the stored 3, 5, 6), or leave it as prior art in a note.
4. Import (H1) to (H3) of result 5 as Facts, or leave them as in-statement hypotheses.
5. Follow-up edits to stored text on acceptance: the note of the two-mode theorem (its "first step" sentence);
   clause (2) of synthesis.lens-space-walls-need-more-rungs-than-the-mod-two-height (pointer to result 3);
   Remark 1 of the window-energy theorem (pointer to result 4); op.positivity-of-values and
   op.wall-class-invariant (bookkeeping).
6. The rational-partition-value reading for the count unit (findings, B3 remark): recommended not adopted.

## Second round, same day: imports, amendments, and the items left open on the pull request

Asked for by Leon on 24 November: import Stolz (1989); import the three classical hypotheses of result 5; amend
the three stored texts the new results supersede; resolve the open items (the unreviewed two-mode theorem, the
unread prior art, the required check).

### What was added
- Four imported Facts (status imported, no checks): Stolz's level theorem (m >= 2); Hurwitz zeta values and
  Dirichlet L-functions as Hurwitz sums; the class number formula at 0 for negative fundamental discriminants;
  the divisor-sum formula for L(-1, chi_D), D > 1 fundamental. Reading levels: Stolz through its zbMATH review
  and two later papers that quote it (Furuta, Kametani, Matsue and Minami 2007; Meyer 1998), the paper not read;
  the other three from memory, with the statements tested numerically by the referee (611 negative and 909
  positive fundamental discriminants, 0 failures).
- One derived result: synthesis.definite-side-rung-count-on-every-quarter-turn-lens-wall-is-the-level. PROVED
  GIVEN THE IMPORT, assuming tameness. k_+ = n+2 (n = 1, 7), n+4 (n = 5), n+3 otherwise modulo 8. Its whole
  content is the import plus the stored reduction. The one value beyond what the store held, 6 on L^7(4), sits
  in the residue m = 4 modulo 8, where by the review the paper's general bounds differ; flagged at every level.
- Result 5 rewired to the three imports; result 3 restructured so that the rung bound is stated only in the
  lens-wall result (no cycle).

### Amendments to stored results
- lens-space-walls-need-more-rungs: version 2 -> 3, restatement of clause (2) (order 2^ceil(n/2) for every n,
  bound 1 + ceil(n/2)), clause (4) bound r -> r + 1, new uses edge to result 3. Dependant three-rungs repinned.
- window-energy-tests-with-free-spacing: version 1 -> 2, Remark 1, technical, lay and one-liner now say there
  is no fourth point, proved in result 4 (no edge; result 4 uses this theorem).
- two-mode theorem: note only, version kept. The "first step" sentence replaced; prior-art paragraph corrected.

### Referees (both blind, Opus)
- R2, the two-mode theorem line by line: SOUND WITH FIXES, wording and labels only. Every finite step of clause
  (iii) recomputed with separate code; refutation attempts (box test, class functions) found nothing. Prior
  art: nothing read proves a trace form on the orthogonal rational projections; Mushtari 2001 read in full
  through a summarising tool; Mushtari 1995 (where the question is posed) and 1998 through abstracts only.
  Novelty of clause (iii): supportable, not established. Report: verify/referee-R2.md.
- R3, this round's additions: every item SOUND or SOUND WITH FIXES; no circular dependence. Fixes applied:
  the m = 4 caveat on Stolz and on the derived result; tameness (assumes edge and wording); the uncited bound
  k >= 4 (three-rungs added to uses); D > 1 in the divisor-sum import; s != 1 in the Hurwitz import; stale
  clause (4) of the lens-wall result; stale technical level of the window-energy theorem; a rung bound still
  drawn in result 3's clause (iv), now a remark. Report: verify/referee-R3.md.
- Not applied: the stale clause labels in the comments of the two-mode theorem's check file (a check file is
  part of the locked content; changing comments would need a new version for no gain in evidence).

### Gates
Store layers 1 to 3: 0 errors, 0 warnings. Evidence layer with mutation tests on every entity changed in this
round: 0 errors (logs in verify/check4-round2/, earlier pass on all thirteen before the fixes).

### Effect on the open problems
None closed. op.wall-class-invariant: definite side of the quarter-turn family known in every dimension, given
the import; indefinite sides, other walls and the integral datum stay open. op.positivity-of-values: the rest
of the two-mode theorem's review and prior art recorded; (P) neither derived nor shown independent.
op.residue-killing-weights: no movement on the count unit.

### Decisions for Leon (second round)
1. Read Stolz's paper at the case m = 4 modulo 8 (or Crabb's independent proof, Contemp. Math. 96 (1989)
   109-124) before building on the value 6 for L^7(4).
2. Read Mushtari, Int. J. Theor. Phys. 34 (1995) 1627 before any public novelty claim for the two-mode theorem.
3. The assumes edge to tameness and the uses edge to the three-rungs result on the new derived result were
   added on the referee's advice; say if either should go.
4. Whether to raise any of these from review: draft.
