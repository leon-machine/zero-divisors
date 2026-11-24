# Fixes P-B, run 2026-11-24-three-routes

## synthesis.local-records-give-the-chsh-bound-without-positivity-and-reversal-on-one-party-keeps-them
Verdict (verify/R-P.md, section 3): SOUND WITH FIXES, one sentence overstated. All five fixes applied in place in
proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml). Nothing rebutted: the referee's
counterexample is correct and is now in the check.

1. Overstatement, restated at every level. "The same values on every product of local observables" was false.
   Recomputed: X_1 Z_1 X_2 Z_2 = -K is a product of four local observables, the reversal negates it, lambda_{-1}
   gives 1 and lambda_{+1} gives -1. Now stated: the reversed functional has the state's values on every product
   ab with ONE local observable b of party 2 (so on products of one observable of each party) and the state's
   weight on every sequence (palindrome) of local records; it can differ on products with two observables of
   party 2 that do not commute. Changed in formal (iv), technical, one-liner, Reading (b), the note, proof (iv);
   the lay sentence speaks of records and stands. Check: a new block asserts the counterexample (the product is
   -K, is negated, values 1 and -1, the two party-2 observables do not commute).
   Does the rest survive? Title: "do not fix (P)" is about records, which are palindromes, and stands. The id's
   "keeps them" refers to local records and stands; the id is unchanged. Independence reading (b), (c): unchanged
   in substance, because the conditions it lists (weights at local settings, no signalling, the bound, coarse
   counts) are all weights of records; one clause added to (b) saying the agreement is on weights of records, not
   on values of all products. The value of (X_1 Z_1)(X_2 Z_2) is not the weight of any sequence of local records
   (each factor X_j Z_j is anti-self-adjoint), so it is not a local datum in the real algebra; clause (vii) says
   when it becomes one.
2. Named hypothesis. (CP) is now in the title ("Under (CP) local records bound CHSH without (P) and do not fix
   (P): reversal on one party", 89 characters) and named in the one-liner. The conditions of clause (iii) are in
   the one-liner in words, as before.
3. Uncited use removed. Proof (v) now derives the weights (1 - u - v - c uv)/4 of lambda_c and that lambda_c is
   non-negative on all x x^dagger exactly at c = -1 (density 4 P_s, P_s a self-adjoint idempotent); the stored
   clause is "recalled for comparison" and not used; no uses edge added. Formal (v) reworded to match. Check: the
   weight identity at five c and four sign pairs, and P_s idempotent and self-adjoint.
4. Clause (vii) and Reading (d): "a product of one self-adjoint element of each party"; (vii) now also says that
   without the unit K is a product of local observables only with two anti-commuting ones per party.
5. Clause (i): the identity uses only A_i^2 = 1; the y y^dagger form uses self-adjointness, B_j^2 = 1 and the
   commutation.
Overlap: the note's sentence on the reading that every rational projector labels a record now cites, in text only,
"filed alongside, synthesis.under-rp-record-weights-bound-the-chsh-sum-of-correlators-on-two-modes". No merge.
runcheck: 6 PASS. check4: pending (orchestrator).

Also corrected in my own findings (attack-P-B.md): the overstated sentence in the results list, and the
"Unexpected links" entry on orientation (below).

## Bridge pass
- B4(c): no sentence of the proposal is contradicted (Reading (d) already calls the reversal the partial
  transposition where I_4 is present). In my findings the phrase "a resemblance" is replaced by the exact
  statement, labelled argued: with I_4 adjoined a self-adjoint element of party 2 is s + I_4 a (s self-adjoint,
  a anti-self-adjoint in party 2's real algebra) and the reversal sends it to s - I_4 a, so the reversal is the
  orientation datum I_4 -> -I_4 reversed for that party only. It identifies the model and derives nothing. Not
  added to the proposal (it would be new content in a fix round).
- B5: agrees with the audit row on the recording premises (they name no weights, no sign and no list of record
  projectors); nothing to correct.

## Repin on acceptance
None needed by this proposal (its pins are to stored versions). If the proposal filed alongside on two or more
modes is accepted, clause (iii) extends from a first party of exactly two modes to two or more; that would be a
new version, not a repin.

## Next steps
- B4(c) as a clause: state and check, in Cl(3,5) or with a party of several modes, that the reversal is the
  conjugation I_4 -> -I_4 on one party's self-adjoint elements, and decide whether any stored premise ties the two
  parties' orientations (the flag as datum is per solution, not per party).
- B5, adversarial side (four modes): under the restricted hypothesis that record labels are sector projectors of
  Witt flags adapted to the split, test whether the reversal of a state on two modes per party is excluded, i.e.
  whether some flag-sector projector of the four-mode algebra is not a product of local ones and gets a negative
  weight. Not computed.
- The conjecture that non-negative weights of local records at every number of copies force a state or the
  reversal of one.

## Decisions for Leon
Unchanged from findings/attack-P-B.md (six items); the fix round adds none and removes none. In brief: (1) whether
a projector that is not a product of local ones can label a record (the fork on which independence of (P) turns);
(2) restating the open problem's "why" once (CP) is stored; (3) a scope sentence in (P) against Krein expectation
values; (4) whether the parties' observables include I_4 times an anti-self-adjoint element; (5) imports of the
literature cited from memory, only if wanted; (6) the maintainer's edits to the open-problem record.

## Second pass (verify/R-2.md, section 4: SOUND WITH FIXES; clauses (iv) and (v) confirmed by an independent route)
1. Title: "Under (CP) one party's values bound CHSH without (P); local record weights do not fix (P)" (89
   characters). (CP) now goes with values of one party; the statement on weights of local records stands on its
   own. The reversal on one party, which the referee's longer wording also named, did not fit in 90 characters and
   is left to the one-liner, which names it and still names Hypothesis (CP).
2. Formal (iv): "(the weights of sequences of local records)" added after "each lying in A or in B", so the title's
   term is defined in the formal level.
3. Reading (c): "(P) is not implied by any condition on the weights of local records (it implies all of them)" in
   place of "(P) is independent of the conditions on local records". No other level of the entity or the proof
   says "independent" of (P) (searched); the lay level says "whether positivity is an extra assumption comes down
   to ...", which is left as it is.
In my findings (attack-P-B.md) the word "independent" for (P) on the two-party scope should be read in the same
one-way sense: not implied by conditions on weights of local records.
runcheck: 6 PASS (check.py unchanged in this pass). check4: pending (orchestrator).

## After the change of base (HEAD f9f3bee; main now stores the size-four theorem, version 1)
1. References. No sentence of the proposal referred to the withdrawn proposal (searched entity.md, proof-main.tex,
   check.py, coverage.yaml); the only "filed alongside" citation is to the proposal under (RP) on two modes, which
   stands. No sentence said that more than two modes is not done for additive weights. The earlier line in this
   file under "Repin on acceptance" about "the proposal filed alongside on two or more modes" is superseded by
   item 2.
2. Clause (iii) carried out for a first party of m >= 2 modes (not left as a pointer). The proof needs exactly two
   things of the party's algebra, and the stored theorem
   synthesis.additive-weights-on-the-rational-projectors-are-linear-in-every-size-from-four supplies both for every
   m >= 2: its clause (i) (the algebra of m modes is Mat_{2^m}(Q) with the adjoint the transpose, self-adjoint
   idempotents the symmetric idempotents) and its clause (iii) (additive weights are restrictions of a linear map
   with symmetric coefficients). The rest of the argument (s^2 as a non-negative combination of rank-one
   projectors by columns; projectors span the self-adjoint elements; the sum of the four values) is unchanged and
   does not depend on the size. Restated at every level: formal (iii) ("m >= 2"), Reading (a), technical ("two or
   more modes", with the remark that one mode is excluded), one-liner, the note, proof (iii) (the isomorphism is
   now written phi, to keep m for the number of modes). Uses edge added with the stored pin @1; the stored
   theorem holds given no premise, so the proposal still rests on none. The two-mode theorem stays pinned @1 (clause
   (vi) uses its clause (i), and (iii) cites it for m = 2).
   Check: new function check_weights_of_records_of_one_party_of_three_modes_give_the_bound (four modes, party 1
   holding three; a density that is not a state, weight -1/2 on a self-adjoint idempotent; non-negative weights
   at the four setting pairs; V = -34/13; the four conditional forms of party 1 have no negative direction on the
   64 blades of its algebra; the four values sum to 4 + 2t^2 - 2tV). It touches the new premise. coverage.yaml
   and checked_by updated. Not done: k other than Q in clause (iii).
runcheck: 7 PASS. check4: pending (orchestrator).

## Third pass (verify/R-3.md, section 2: SOUND WITH FIXES; the extension of clause (iii) to m >= 2 confirmed)
All five fixes applied in place; no statement changed in substance, check.py unchanged.
1. One-liner: the parenthesis on clause (iii) now reads "over Q, for a party of two or more modes, from
   non-negative additive weights of its records given each outcome of the other party, with the same marginal for
   both of the other party's settings".
2. Technical: "Over the rationals" and "whose sum over the other party's two outcomes does not depend on its
   setting" added to the sentence on a party of two or more modes.
3. Reading (a): "over Q" and "(in particular their sum over the other party's outcomes is the same for both of its
   settings)" added.
4. Note and the last sentence of proof (iii): the check "exhibits" one mu for a first party of three modes (and
   one for two) that comes from a functional that is not a state, with the bound; the passage from additive to
   linear is the stored theorems' and is not recomputed.
5. Proof (iii): why the first party's algebra with the adjoint is the algebra of m modes (blades in e_j, f_j,
   j <= m, are a basis; the adjoint restricts); "over the nonzero columns".
runcheck: 7 PASS. check4: pending (orchestrator).
