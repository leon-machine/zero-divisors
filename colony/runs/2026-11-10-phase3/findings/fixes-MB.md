# fixes-MB: fix round for the constituent-momentum proposal

Proposal: synthesis.constituent-momentum-is-the-unique-spin-covariant-quadratic-vector-on-the-spinor-ideal
(referee R2, verdict SOUND WITH FIXES). Id unchanged. All fixes applied in place in proposals/<id>/.
runcheck: 6 of 6 functions pass (about 20 s in total). check4: pending (orchestrator). validate: pending (orchestrator).

## Fixes applied

1. Title (G1, fix 1). The referee's wording is longer than 90 characters, so the title is now
   "Causal towers of dimension 3 to 5: j the only covariant quadratic vector of a constituent" (89 characters). It
   carries the dimension range and "a constituent"; "up to a real factor" did not fit and is stated at every level
   (formal (i), technical, lay, one-liner), and the extraction note says the title's "only" means no more than that.
2. One-liner (G1, G4, fix 2). Now says: one constituent; covariant under the connected spin group, real-quadratic,
   no reflections; classical fact placed on the series' ideals; two-constituent spaces of dimension 3, 4, 6;
   "assuming a spinor part and momentum quadratic and covariant".
3. Lay (G1, G3, G4, fix 3). Added: "turn" means continuous rotations and boosts, not reflections; a standard fact
   about spinors placed in the series' algebra; for two constituents mixed terms are allowed in three, four and
   five dimensions alike.
4. Formal (ii) and technical (G3, fix 4). The count of invariant quadratic forms "agrees with
   synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion (iii), which is not used here" (claimref in
   the formal level; no uses edge, since H1 is in that result's past cone). Formal (iii) now says it is a
   restatement of dark-tower-matter.where-mass-begins (ii) in terms of s. Formal (i) and the technical level say
   the uniqueness is classical spinor algebra.
5. Formal preamble (fix 5). One sentence: covariance is under the Lie algebra of bivectors, hence the connected
   group; no reflection; left action only, the right action of the field not imposed; beta real-bilinear.
6. Dimension five supplied (G2, fix 6, the recommended option). New check function
   check_cross_block_has_the_dimension_of_the_field_so_two_constituents_give_three_four_six: exact rank of the
   covariance system for real bilinear maps S x S -> V with no symmetry imposed, in all six towers: 1, 2, 4 for
   n = 3, 4, 5, with <x e_t rev(w)>_1 a nonzero solution. My computation agrees with the referee's table (cross
   block 1, 2, 4; two-constituent spaces 3, 4, 6). Clause (iv) is restated: counts 3, 4, 6 by the block
   decomposition (proof (iv) rewritten), "proved in the six towers", and the referee's corollary added (cross terms
   odd under a sign change of one constituent, so covariance plus that invariance leaves a j(psi_1) + b j(psi_2);
   additivity is absence of a cross term plus equal weights). "Not computed" removed from every level; the direct
   S + S rank for n = 3, 4 is kept as a second route. checked_by and coverage.yaml updated (new function, kind
   complete).
7. Citation (fix 7). Van Proeyen is cited "from memory, the section not verified"; the section number is removed.
   Prior art only, not a premise.
8. Proof (iii), the referee's shortening: "(2s - lambda) j = 0 in a polynomial ring without zero divisors and j is
   not the zero polynomial" replaces the dense-open-set step.
9. G5, notation of the grade projection: left as \langle \rangle_1 (the store's \ip macro takes two arguments;
   check4 and validate passed with this form). No change.

## Rule on outside dates

Nothing dated from outside the store appears in the proposal at any level or in its note; it never did. The remark
on when the unit-ball section entered T14 exists only in findings/attack-MB.md, where it is flagged as coming from
the user's memory notes and not from the store. It stays out of every store text; the store-quotable basis for the
fit count is dark-matter.status-rule (i), (ii), (vi) and dark-matter.unit-ball-rule ("found by solving for the
observed value", "chosen with it known").

## Rebuttals

None. Every referee number was reproduced.

## Left for the orchestrator or maintainer

- check4 and validate_draft on the edited folder.
- The new check function takes roughly 12 s; each mutant run is well inside the 60 s limit.
