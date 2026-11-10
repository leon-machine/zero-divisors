# fixes-NB (fix round step 1), proposal synthesis.invariant-forms-on-the-fock-module-and-the-pair-counts-of-a-next-level

Verdict addressed: OVERSTATED (mathematics sound), verify/R2.md section 2. All edits in place in proposals/<id>/.
runcheck: 3/3 PASS. check4: pending (orchestrator). validate: pending (orchestrator).

## Fixes applied
(a) The step at three is not the ascent. Restated at formal (iv), formal (v), technical, lay, one-liner, proof and
    extraction note: under the invariant symmetric form the eight states are the vectors of four pairs; four is also
    the next floor's pair count, an equality of counts at k = 3 only, not an identification; no isometry with the
    vector space of B_4 is compatible with the action of B_3; from four the rule gives eight, not five. The false lay
    sentence ("exactly the single step the proved tower takes") is gone; (v) now ends "one pair per rung, which
    neither rule is". Proof: the bivectors of B_3 annihilate no state (v_j w_j - w_j v_j is +1 or -1 on every basis
    state) and commute with v_4, w_4. Check: common kernel of the 15 bivectors on F_3 is zero (rank 8) and they commute
    with the new pair in Cl(4,4). I accept the referee's computation; mine agrees.
(b) "Both rules use the stored words" removed. Now: the first rule's counts are the stored ones; the second rule
    does not reproduce them (8 and 256 recur only as state counts); that it is another reading of the stored phrase
    is labelled a judgement at formal (v), technical, lay, one-liner and in the note.
1.  std-algebra.chevalley-pairing@1 and std-algebra.fock-representation@1 added to the derivation and touched by the
    checks; (i), (ii) for eps = +1 and the grade pairing of (iii) are stated as restatements (roles of the two null
    families exchanged; identification up to a factor by the uniqueness clause). Novelty narrowed in the note to
    beta_-, uniqueness for each eps, neutral signature and Witt index, and the counts. beta_-(psi, phi) =
    beta_+(alpha psi, phi) added with its one-line proof. correspondence.chevalley-pairing and
    synthesis.invariant-forms-on-spinor-ideal-factor-through-reversion named in the note as neighbours (not pinned:
    nothing is used from them). "Cited from memory" replaced by what review confirmed on the web (Gualtieri 2.4 for
    beta_+) and what stays from memory (Harvey).
2.  Notation |J| in place of C; "Proposition" for the trichotomy; rider added at formal (v), technical, lay and proof
    that the comparison is of sizes only, the stored count being of registered units and not of ladder pairs
    (synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping@1 and
    synthesis.de-sitter-mode-count@3 added to the derivation and touched).
3.  "Hyperbolic over any field of characteristic not two, signature (2^(k-1), 2^(k-1)) over an ordered field."
4.  (v) says the second rule uses beta_- at k = 3 (the only symmetric form there) and either form from k = 4 on.
5.  First-rule content cut to one sentence plus its counts; the sibling stays a "sibling result, intended citation"
    sentence in the note (step 2 turns it into a citation).
6.  No change (coverage kinds); coverage text updated for the new assertions.
Rule 4 of FIXROUND: "no stored result selects one rule" carries "argued, from a search and not an audit" at formal,
technical, lay and one-liner. Title changed (78 characters): "The two invariant forms on the Fock module and the pair
counts of a next level". One-liner says "each unique up to a factor".

## Rebuttal (one, with evidence)
Fix 2, bracket attribution: the referee says 2^407 < |J| < 2^408 is not in standard-model.trichotomy-what-kind-number@11.
It is not in its statement levels, but it is in its proof (store/claims/standard-model.trichotomy-what-kind-number/proof-main.tex:
"2^{407} < \pi N^{2}/\ln 2 < 2^{408} for the horizon capacity") and its check asserts it
(check_units_statement_numbers: bit_length - 1 == 407 over the quoted range). So the pin stays, and the text now
says "the bracket stated in the proof of" that Proposition. The base proposal can use the same wording.

## Not done
Sibling references are not citations yet (step 2). My findings file's link 1 (the triality lead) is superseded by
(a) in its strong form: the identification with rung four's VECTORS fails equivariantly, as the referee computed; what
remains true is that F_3 is the even half of F_4 as a module of the three-pair spin group (signature (4,4) computed).

## Step 2 (base stored at version 1)
runcheck: 3/3 PASS. check4: pending (orchestrator). validate: pending (orchestrator).
- Uses edge synthesis.exponential-reading-of-the-tower-is-the-iterated-fock-functor-not-the-ascent@1 added; claimrefs
  to its clauses (i), (ii), (v) in formal (iv), (v), technical and proof; premise() call in
  check_counts_at_three_and_the_two_iterations. The "sibling result" sentence in the note is now a citation.
- Repeat of base (i) dropped: clause (v) is retitled "A second rule for a next level", names the first rule by
  citation with its stored counts in one sentence, and proves only the second rule. The check no longer recomputes
  3, 8, 256, 2^256 or the 1e77 bracket.
- Bracket comparison: kept only this rule's own terms (2^127 and 2^(2^127 - 1)), "given" the bracket and the
  registered-units rider quoted from base (v). The pins on standard-model.trichotomy-what-kind-number,
  synthesis.de-sitter-mode-count and the two-arrays result are removed with their premise() calls, since the base
  carries them. My step 1 rebuttal on the bracket's source is thereby moot for this proposal.
- The two fours kept apart at formal (iv), technical and note: mine is a Witt index; the base's (ii) is the pair
  count after one ascent; they agree as numbers at k = 3 only.
- Derivation now: tower.fock-module-one-qubit-per-rung@6, tower.witt-index-quantum-capacity@5,
  std-algebra.chevalley-pairing@1, std-algebra.fock-representation@1, and the base @1.
