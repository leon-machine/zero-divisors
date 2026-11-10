# fixes-EA, step 1: the base
Proposal: synthesis.chsh-bound-for-two-subsystems-of-a-clifford-algebra-by-a-rational-certificate (id unchanged; title
now "CHSH bound under positivity of values (P): certificate, blade lemma and Cl(2,2) realisation"). Fixed in place in
proposals/<id>/ (entity.md, proof-main.tex, check.py, coverage.yaml). Pre-fix copies: work/EA/aside/base-*-before-fixround.*.
Only runcheck was run: 8 of 8 functions PASS.

## (P), verbatim in the formal level
"Hypothesis (P), positivity of values: values are given by a state, a k-linear omega : Cl_k(p,q) -> k with
omega(1) = 1, omega(x x^dagger) >= 0 and omega(x^dagger) = omega(x) for all x; (P) is assumed, not derived."
LaTeX: \emph{Hypothesis (P), positivity of values:} values are given by a \emph{state}, a $k$-linear
$\omega : \Cl_{k}(p,q) \to k$ with $\omega(1) = 1$, $\omega(xx^{\dagger}) \ge 0$ and $\omega(x^{\dagger}) = \omega(x)$
for all $x$; (P) is assumed, not derived.
Also at one-liner ("Under Hypothesis (P) (values are given by a state, a linear omega with omega(1) = 1,
omega(x x^dagger) >= 0, omega(x^dagger) = omega(x); assumed, not derived)"), technical and lay. Symbol omega throughout.
The note says (P) is adopted and is to become an assumes edge.

## Final clause labels of the base (for siblings to cite)
(i) the identity: C^dagger = C, C^2 = 4 - XY.
(ii) the certificate: 8 - C^2 = (Z^dagger Z + S_A^2 + S_B^2)/2; X^dagger X = 4 - S_A^2.
(iii) the bound under (P): w(C)^2 <= w(C^2) <= 8; strict over Q; refinement; value 8 forces w(S_A^2) = w(S_B^2) = 0;
      commuting pair gives C^2 = 4. Uses only positivity and normalisation.
(iv) blade lemma: C^2 = 4 + 4K, K = -A1 A2 B1 B2, KC = CK = C, C^3 = 8C, <C>_0 = <K>_0 = 0; the functionals
      w_r = <(1+K)(1+rC) .>_0 satisfy (P) exactly when 8 r^2 <= 1, values 8r, w_r(C^2) = 8.
(v) without positivity the value 4 occurs: lambda = <(1+C) .>_0.
(vi) self-adjointness for one fixed frame is needed (17/4; boosted frame).
(vii) the Cl(2,2) realisation: one mode against the Klein-twisted other mode, parity-odd directions;
      C^2 = 4 + 4 (a1^a2)(b1^b2) e1 f2; anticommutation forced for directions; parity paragraph, both settings.
(viii) the saturating state of (vii) at blade settings; unique at these settings.
(ix) anticommutation only on the state: the three-mode example.

## Fixes
1 (C2 in formal; clause retitled; boosted frame; lay qualified): APPLIED. The C2 sentence is in the formal preamble
  verbatim; clause (vi) carries the referee's text; check computes the partner's square, the anticommutation and -9/4.
2 (C5, Cl(3,0)/Cl(1,3) parenthesis): APPLIED by moving it to the note as "sibling result, not used", with the
  wording that it concerns two commuting pairs inside one copy and says nothing against Bell violation for two
  systems; removed from formal and technical.
3 (C5, value 4 without positivity): APPLIED, proved in place as clause (v) with a check.
4 (C3): APPLIED. mode-split edge removed; tower.commuting-copies@5 pinned; the three lines on the twist proved in
  place in (vii). "The completion postulate is not used" reworded to "no step of the proof uses real coefficients".
  The descent-parity-average@5 edge is KEPT, with the caveat that its total-parity form is a definition.
  The mode-split entity remains under lineage.motivated_by only.
5 (uniqueness wording): APPLIED: "at these settings"; proved on self-adjoint elements, and with the reality clause
  of (P) (now part of (P)) equality on all elements; the proof marks where reality is used.
6 (status line of the bound): APPLIED, and the check now also samples the second inequality, so the status line
  reads "the check samples the two inequalities and not the strictness".
7 (C6): APPLIED, one sentence in the formal level.
8 (receive blade lemma and three-mode example): APPLIED as clauses (iv) and (ix), restated from the siblings' proofs,
  with new checks (blade configurations in signatures (2,2) and (3,1); the three-mode example).
C2: APPLIED (see 1). C3: APPLIED (see 4). C5: APPLIED (see 2, 3; no formal clause rests on a proposal).
C6: APPLIED (see 7). C1: (P) as above. C4: the base uses (x, z) for directions and no (c, s); nothing to change.
Parity decision: both settings recorded side by side in (vii), technical, lay and note; neither called physical.
Also changed: the positivity proof of (iv) corrected in transcription to y = Pi x (the sibling text had the same
form); clause (viii) no longer cites the mode-split theorem for the reduction (it only states the two projections).
NOT done / to watch at the gate: the mutation test (W413) on the three new check functions has not been run by me.

# fixes-EA, step 2: the rationals and three-party proposals (after the base was stored at version 1)
Both fixed in place in proposals/<id>/; pre-fix copies in work/EA/aside/*-before-fixround.*. Only runcheck was run:
rationals 3 of 3 PASS, three-party 4 of 4 PASS. Both now cite the base @1 (uses edge + claimref) and state (P)
verbatim as in the base at formal level, "Under (P)" in the one-liner, one sentence in technical and lay; the C2
sentence is in both formal levels; the mode-split edge is removed from both.

## synthesis.chsh-over-the-rationals-pure-states-on-a-circle-and-the-pell-records
Title: "CHSH over the rationals at fixed settings: a circle of pure states and a Pell sequence".
1 ("records"): APPLIED. The word is dropped. Clause (v) is headed "the values that meet the denominator law with
  equality, a Pell sequence"; it says the S_n are NOT the running maxima of all state values (280/99 > 82/29 at
  denominator 99 < 169, checked), and adds, labelled computed, that among pure-state values of the sector the running
  maxima are exactly 2, 14/5, 82/29, 478/169 for denominators up to 400 (my check; the referee's range was 1200).
  Lay sentence replaced by the referee's wording. Index of the sequence renamed n (k is the field in the base).
2 (C4): APPLIED. Rotor components are (c_u, s_u) everywhere (formal and proof); S_n = 2(c_u - s_u) with s_u < 0 is
  said once; rho_infinity is "the stored pair state with r = 0 and amplitude product -1/2", written out; the note
  says the parity result's 2(z + x) is the same number for the mirror state.
3 (C1): APPLIED, including the lay sentence (one arrangement of measurements; assumes (P)).
4 (scope): APPLIED: "at fixed settings" in the title, "at these settings" in clauses (iv), (v), technical, one-liner.
5 (not decided, in technical): APPLIED.
6 (C2, C3, completion sentence): APPLIED. The configuration is cited from the base clauses (iv), (vii), (viii); no
  twist edge is needed; the pair-state identity is an explicit identity of elements; "no step of the proof uses
  real coefficients".
7 (cite the base for the single bound; keep the disc): APPLIED. The preliminaries and the copy of the identity are
  replaced by a citation; clause (i) keeps the disc.
8 ("(reading)"): APPLIED.
9: nothing to do.

## synthesis.three-party-trade-off-of-chsh-values-and-the-local-value-two
Title: "Three-party trade-off of CHSH values under positivity (P), and the values 2 and 4".
1 (same settings): APPLIED in the formal preamble, clauses (ii) and (v), technical, lay and one-liner.
2 (the 14/5 state): APPLIED. Written out as (4/5) y' rho_0 y'^dagger with rho_0 = (1/4)(1 + e1.e2p1)(1 - p1p2),
  y' = 1 - (1/2) e2p1p2; said not to be the pair state of (v); "times any state of mode 3" replaced by "for every
  state with value 14/5, for instance this one times (1 + p3)/2".
3 (C4): APPLIED: "amplitudes" in clause (v); (x, z) for directions.
4 (vacuous loop): APPLIED. The loop now asserts the values are exactly 0 and coverage.yaml calls it a trivial
  sample and no evidence for the bound; a state entangled across all three parties is added with pinned values
  (24/13, 30/17), sum of squares 318564/48841.
5 (horizon remark): APPLIED. Labelled "Remark (horizon), not a result" in the note with its three supports (stored
  pair-state reading, same settings, parity-odd elements) and "empty under parity superselection"; the technical
  sentence carries the label.
6 (Toner-Verstraete): APPLIED: cited as checked (quant-ph/0611001, Theorem 1, arbitrary dimension, same
  measurements for A, tight on the circle; here only (2, 2) over Q).
7 (clause (iii) wording; C^2 = 4 as a citation): APPLIED, citing base clauses (iii), (v), (vi). The single-pair
  bound "taken alone" is dropped from clause (ii) and its proof.
8 (C2, C3): APPLIED. tower.commuting-copies@5 pinned for the two twists, with the lines proved in place; the pair
  state of (v) is written out and its idempotency proved by a degree argument (a polynomial of degree at most 2 in
  (r, cs) vanishing at five points of the conic r^2 + 4(cs)^2 = 1), with the five points in the check.
9: nothing to do.
Not run by me: check4, validate_draft, the mutation test on the changed check functions.

check4: pending (orchestrator)
