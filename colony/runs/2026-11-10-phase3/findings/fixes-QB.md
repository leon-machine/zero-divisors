# fixes-QB: fix round step 1 (referee R3)

Applied in place in proposals/<id>/. Only colony/runcheck.py was run. check4: pending (orchestrator).
validate: pending (orchestrator). No rebuttals.

## 1. synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion (SOUND WITH FIXES)
Final clause labels: (i) proved (every bivector map, every dimension and signature); (ii) proved (every field;
labelled as the classical first Bianchi identity with torsion); (iii) proved (the identity, the cyclic vector form,
d_a calR(a ^ b) = calR(b), and now the symmetry of the Ricci map in every dimension by contraction), its two
converse examples computed; (iv) computed for d = 3, 4, 5, the general dimension count and pair symmetry cited.
- Fix 1 (converse): formal (iii), technical, one-liner and proof now say the converse fails, with the referee's
  example (Omega = 0, coframe not a gradient: torsion, zero curvature) and a second with nonzero curvature (the
  conformal coframe with twice its torsion-free Omega; computed on a sample, not proved in general). The check
  carries both (in check_cyclic_trivector_is_the_covariant_curl_of_the_torsion, helper converse_examples; sample
  data in module constants so the mutation count is unchanged). Reproduced before editing: both have torsion and
  vanishing protraction.
- Fix 2 (credit): the note's "what is added" replaced: nothing in the derivation is new; the inversion is the
  source's steps (5.4), (5.5) as one formula; clause (ii) is the classical identity with torsion (Cartan's structure
  equation differentiated), said in the formal beside the clause and in the note.
- Fix 3 (Ricci symmetry for all d): added to (iii) and its proof by contraction, d_b . (d_a ^ M(a ^ b)) = d_a ^ M(a)
  (the source's (5.11)); clause (iv) no longer carries it; the check adds d_a ^ calR(a) = 0 on the six fields.
- Fix 4 (optional, dimension count for all d; d = 6): not taken; stays cited.
- Fix 5: coverage.yaml gains the two new clauses; kinds unchanged.
- Fix 6 (pin the object's version): maintainer; uses stays [] because an object in uses raises W209 and a premise()
  call on it raises E404 without it.
runcheck: 4 of 4 pass.

## 2. synthesis.curved-field-vacuum-polarisation-freedom-is-five-local-covariant-constants-of-which-one-is-transverse (OVERSTATED at title and lay)
Restated to the referee's statement at every level; id unchanged.
- Title: "Given imported local covariance, curved vacuum-polarisation extensions differ by 5 terms" (88 characters;
  the referee's wording is over the 90 limit, this keeps its content: conditional, about the difference of extensions).
- One-liner: "(imported, cited from memory, sourced for scalar fields)" inserted; ending now "(proved given those
  inputs); whether a transverse local covariant extension exists is argued only, so the stored clause stays argued".
- Formal: head sentence added (Fact from memory, scalar-field sources, Dirac current part of the import; difference
  of two extensions only; the stored kernel is the parametrix trace); (i) heading says the rotor-invariance of the
  coefficients is the proof's reading of the Fact; (ii) "are excluded" replaced by "do not occur in the difference
  of two transverse extensions; the Ricci term occurs only inside D.(D ^ A), the Maxwell operator, minimal coupling",
  plus "nothing is said about the finite curvature dependence of the kernel"; (iii) begins "If transverse local
  covariant extensions exist"; after (iv): "Clause (iv) of the cited curved-field theorem therefore stays argued",
  with Zahn 1311.7661 beside 1210.4031 (abstract level only).
- Technical: conditional wording, the scalar-field sourcing sentence, the Maxwell-operator reading, "the argued
  clause of the stored result stays argued".
- Lay: the "fixed strength" sentence replaced by the referee's text; "the theorem relied on was proved for a simpler
  kind of field than the electron's" added; last sentence kept and extended ("the open point ... stays open").
- Proof: (i) and (iii) carry the same two conditions.
- Note: the five constants named as the five quadratic local actions of dimension four, standard power counting,
  nothing new in quantum field theory; Zahn 1311.7661; entity status proved covers (i) to (iii) as conditional
  statements, (iv) argued; "sibling, intended citation" sentence for hypothesis (PI) (step 2).
- Check and coverage: unchanged. runcheck: 3 of 3 pass.
- Not done in step 1, by rule 3: replacing hypothesis (PI) by a uses edge to the protraction identity.

## For step 2
After acceptance of the protraction identity: uses edge to it @1 (clause (iii): the identity, the Ricci-vector
contraction and the Ricci symmetry, now in (iii) for every dimension), claimref in the formal and in the proof of
(i) and (ii), "Hypothesis (PI)" removed from formal, one-liner and proof; premise() call added in the two check
functions that rely on it.

## Step 2 (after acceptance of the protraction identity at version 1)
Curved-field proposal only. check4: pending (orchestrator).
- uses: synthesis.protraction-identity-of-the-curvature-operator-from-vanishing-torsion@1 added.
- Formal: "Hypothesis (PI)" replaced by a citation of its clause (iii) (the identity and the Ricci symmetry), with a
  note that the stored curved-field theorem still carries it as a hypothesis; clause (i) heading and count reworded;
  no "(PI)" remains at any level. One-liner: the identity is no longer listed among the givens. Technical: named
  as a stored theorem. Proof: both uses ((i), the count; (ii), Ricci symmetry) cite clause (iii) by claimref.
- Note: hypothesis sentence replaced; the "sibling, intended citation" sentence removed.
- Check: premise() on the identity added in check_invariant_local_terms_of_dimension_two_for_two_vector_slots
  (the count 2) and in check_divergence_of_the_field_strength_is_laplacian_minus_gradient_divergence_plus_ricci
  (Ricci symmetry on the torsion-free field). Coverage: the untouched-premise reason no longer mentions (PI).
- runcheck: 3 of 3 pass.
