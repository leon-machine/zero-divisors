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

check4: pending (orchestrator)
