# Fixes B (fix round, referee C)

check4: pending (orchestrator). validate_one: pending (orchestrator). Only runcheck.py was run.

## B1: synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (OVERSTATED -> restated)
Restated to the referee's weaker statement at every level: the term (beta/18)^A from a rectangle's own plaquettes is
shared (the leading term for SU(3), by its centre; for G, which has no centre, not shown to be leading).
- Restatement: one-liner rewritten to the referee's statement (every term of link degree <= 3 shared; own-plaquette
  term, leading for SU(3) only; plaquette differs at beta^3, 0 vs 1/972; gap at the identity; reading argued).
  Technical: "leading coefficient ... of every rectangular loop" -> "the term (beta/18)^A that a rectangle's own
  plaquettes contribute ... (leading for the colour group, by its centre; for the finite group not shown to be
  leading)", "leading plaquette correlators" -> "tube terms of plaquette correlators"; the closing sentence is now
  labelled a reading. Formal (iv): added "for SU(3) it is the leading term, by its centre, while for G ... it is not
  shown to be leading". Lay: "the first terms" -> "many of the first terms". Extraction note: same restatement.
  Check renamed check_gluing_rule_and_leading_loop_coefficients_agree -> check_gluing_rule_and_own_plaquette_loop_terms_agree
  (entity, coverage, check).
- C.md fix 2 (reading): formal Reading and proof Step 6 now say that for G a fundamental line can end on sheets
  through the degree-four invariant t^4, so its large loops need not follow the rectangle's own term (argued, not
  computed). The optional theta-graph computation (FIXROUND B1.5) was not done; it is mentioned only as the
  argued mechanism, with no number.
- Fix 1 (Schur): proof Step 2 and formal (i) now prove the centre trivial by Schur: the real maps commuting with the
  four generators are span{1, j} (computed in the check, dimension 2, containing 1 and j), so G is irreducible on the
  J-complex 3-space and central elements are J-scalars; the only J-scalar in G is 1. The sampled cube-root search is
  replaced by the algebra (a^3 - 3ab^2 = 1, b(3a^2 - b^2) = 0 gives b = 0 or b^2 = 3/4) and a check that 3/4 is not
  a rational square.
- Fix 2 (store survey): removed from formal, technical, lay and proof Step 9 ((b), (c) deleted); moved to the
  extraction note as a labelled "store survey" (a statement about the store's contents, not tracked by the
  derivation). The weak-coupling freezing of finite groups stays argued, cited from memory, not imported.
- Fix 3 (prior art): Petcher and Weingarten (Phys. Rev. D 22 (1980) 2465) now cited for discrete subgroups of SU(2);
  Bhanot and Rebbi (Phys. Rev. D 24 (1981) 3319) for SU(3).
- Fix 4 (pins): the field-level BRST entity and the one-loop running entity are no longer \claimref'd (proof
  Conventions and Step 9 name them in prose); uses unchanged (they stay in lineage.motivated_by). Pinning the
  one-loop entity would bring its Krein-form premise into holds_given, so prose was chosen.
- FIXROUND sibling sentence: the extraction note names this entity as the intended home of the degree-three lemma
  (to be cited by synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube and by
  synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling) and says it is to
  cite synthesis.colour-centre-flux-bounds-polyakov-lines-and-the-leading-glueball-tube for the SU(3) leading-order
  statements.
- runcheck: 6/6 PASS.

## B2: synthesis.colour-triplets-give-the-fundamental-colour-loop-a-perimeter-law-at-strong-coupling (SOUND WITH FIXES)
- Fix 1: title -> "Colour triplets give the fundamental colour loop a perimeter law at infinite coupling" (id unchanged).
- Fix 2: the formal summary now reads "So at beta = 0 a frozen colour triplet gives every simple loop exactly a
  perimeter law, and Wilson quarks give every rectangle a leading hopping term of perimeter form. (Argued:) at small
  beta > 0 the perimeter term exceeds the area-law term (beta/18)^RT for large loops; this compares leading terms only
  and is not a bound on the full expectation." Proof Step 6 adds the same caveat.
- Fix 3: technical: "at infinite coupling", "exactly a perimeter law" (frozen) and "of perimeter form at leading
  hopping order" (quarks); "the physical colour question is the one with quarks" labelled "As a reading (argued)".
  Lay: exact for fixed charges, at leading order of the hopping expansion for moving quarks; the QCD sentence is
  marked "on this reading". One-liner and extraction note: same qualifications.
- Fix 4: n_g is now "an input of the stored one-loop running coefficients, 3 at the imported values" (formal reading
  and proof Step 6).
- Fix 5: the Fradkin-Shenker Fact and the one-loop entity are cited in prose only (no \claimref); uses unchanged.
- Fix 6: kept the outside_ga declaration (the recast as the Clifford algebra of a zero form was not cheap) and
  extended it: the spinors are the minimal left ideal Cl(4,0)f, f = (1 + d1d2d3d4)/2, with complex unit right
  multiplication by d1d2, identified with j on colour. New check check_spinor_ideal_and_its_complex_unit (entity,
  coverage): f idempotent, the ideal 8-dimensional, (R_{d1d2})^2 = -1 commuting with the left action, the real trace of
  every corner product on the ideal is 8<x>_0 = -16 and its trace composed with the unit is 0, so the complex spin
  trace is 4<x>_0. Proof Step 5 now states this.
- Fix 7: Wilson fermions with r = 1 and the hopping expansion attributed to Wilson's 1975 Erice lectures, "cited from
  memory, not verified at source".
- FIXROUND sibling sentence: the extraction note names
  synthesis.a-finite-subgroup-of-colour-shares-its-strong-coupling-expansion-through-link-degree-three (iii) as the
  intended home of the order-96 group and its degree-four invariants.
- runcheck: 5/5 PASS (four original checks plus the new one).
