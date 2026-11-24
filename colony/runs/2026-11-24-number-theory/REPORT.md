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
