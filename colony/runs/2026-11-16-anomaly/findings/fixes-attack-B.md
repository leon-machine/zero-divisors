# Fixes, attack-B, run 2026-11-16-anomaly

Fixer for two proposals. Edited in place in proposals/<id>/ (entity.md at every level, proof-main.tex, check.py).
Ran only `python3 colony/runcheck.py proposals/<id>/check.py`. Nothing in store/ touched, nothing committed.

## 1. synthesis.colour-angle-fixed-by-no-stored-conjugation-and-relaxed-by-no-stored-field (R1: OVERSTATED)

Restated to the weaker true statement at every level. The id is kept (FIXROUND rule); the title is new.

New title: "Colour angle term under the stored maps; no colour-anomalous phase of the rung coupling" (87 characters).
New one-liner (in substance): the grade-four part of the colour field square is fixed by the stored CPT
conjugation IF it acts on the colour index by an automorphism or anti-automorphism (both stored conventions);
among outermorphisms of vector isometries it is reversed exactly by determinant -1 (the duality map reverses it
too); it is carried to the mirror up to the sign of the identification of orientations (+ for the stored
reversal); on the covariant coupling with both family matrices invertible and no further doublet or coloured
fermion every phase symmetry has colour coefficient 0; none of the stored maps examined fixes the angle, and no
field among the rung field's components relaxes it (completeness of both lists argued).

Referee points (R1 section 1, "Exact fixes" and the body):
1. Title, one-liner, lay: "relaxed by no stored field" overstated. FIXED. Title as above. One-liner, technical,
   lay and Reading (c) now say: proved for the covariant rung coupling with both family matrices invertible;
   "no stored field relaxes the angle" is labelled argued, the list of stored fields not shown complete. The
   extraction note records the restatement and that the id keeps the first wording.
2. "Reversed only by orientation-reversing maps" is false outside outermorphisms. FIXED. Formal (i), technical
   and one-liner restrict the statement to maps acting by the outermorphism of a vector isometry (exactly those
   of determinant -1) and state the counterexample: the duality map F -> I_4 F reverses the term and is the
   outermorphism of no linear map (proof: such a map would have determinant +1 and fix the four-form). Check:
   the reversal under duality and the reversal of <F1 F2>_0, which the five isometries keep, are computed.
3. The action of C on the colour index is not stored. FIXED. Formal (ii) names it as a hypothesis (automorphism
   or anti-automorphism of su(3); the premise leaves the gauge sector premised); the proof covers the
   anti-automorphism case; the check adds the transposition. Invariance in BOTH conventions of clause (5) is
   now stated and proved (phi(XY) = YX, grade-four part unchanged, six-form reversed) and computed in the check.
   This also corrects my own earlier caveat, which had the whole-integrand convention inverting the sign: it
   inverts the six-form, not the four-form.
4. Mirror sign depends on an identification. FIXED, with one addition from the store. Formal (iii) now states
   that sigma o Ad(gamma_0) is also an isomorphism, sends I_4 to -I'_4 and carries the term with the opposite
   sign (computed in the check, multiplicativity included), so the sign is that of the identification of
   orientations and the common-ceiling premise equates the two angles only up to it. Addition (a store lookup,
   not a rebuttal of the referee's algebra): the store does hold one explicit identification, the tower-top
   reversal x_i x_j -> -y_i y_j of synthesis.tower-top-pair-forgets-reversal (i), which is sigma; for it the
   sign is +. The copy theorem itself names none, as the referee says. Both statements are now in (iii).
   New uses edge: synthesis.tower-top-pair-forgets-reversal@2.
5. The list of stored maps was incomplete. FIXED. Reading (a) names the list as a list (not a search) and adds:
   c -> c* (acts on rung values only); the rung boost at I_4-imaginary rapidity (moves gamma_0, fixes every
   spacetime bivector and I_4: computed in Cl of spacetime with two rung planes at cos = -7/25); omega (fixes
   every bivector of the ten: computed); left-right parity D = gamma_5 gamma_9 (a rotor of the ten, keeps
   <XY>_0, moves the colour algebra to a conjugate one: computed); the exchange of set and clear (an
   automorphism of the gauge algebra, stored); the tower-top reversal (sigma). New check function
   check_further_stored_maps_fix_the_four_form; new uses edge standard-model.left-right-parity-what-breaks-it@8.
6. Two hypotheses on the field content. FIXED. Formal (iv) states them (no further field with the doublets'
   gauge charges, no further coloured fermion) and Reading (c) repeats them as the limits of the proof. Lay
   text now reads "provided both of its coupling matrices are invertible, which is so when no quark is massless
   at the simplest vacuum".
Orchestrator's notes: all five covered by points 1 to 6.
Check hygiene (FIXROUND): two premise() calls removed from functions that compute nothing of the premise
(the copy theorem in the signature check, the Chern-Weil Fact in the trace-form check); both stay in uses and
are cited in the proof.
Rebuttals: none. The referee's counter-model (Y = 1, Y~ = E12 + E23 on the lift locus, masses nonzero, a_3 = 3) is
an instance of clause (v) (j = 3; my own check has the same nilpotent model), and the text already carried the
cone condition; the lay sentence is corrected as asked.
Not changed: clauses (v) to (viii), which the referee found correct as stated.
runcheck: 10 of 10 functions PASS.
check4: pending (orchestrator)

## 2. synthesis.order-four-structure-on-real-projective-walls-and-the-signed-count-modulo-sixteen (R2: SOUND WITH FIXES)

Referee points (R2, "Fixes (exact)") and the orchestrator's notes:
1. Reading (b) citation error. FIXED. The forcing at a stage with u(5) and its abelian factor gauged is now
   attributed to the mixed gravitational and cubic conditions of standard-model.imported-anomaly-coefficients
   applied to X = 5 - 2N; the text says the neutral-singlet theorem leaves the bit free for an algebra inside
   u(5) and is cited only for Pati-Salam and so(10). The sums are in formal (vi) and the proof and are
   recomputed in the check: 0 and 0 on sixteen; -5 and -125 on fifteen; -10 with the full state as singlet
   (whose X is 3 modulo 4, also checked). New uses edge: standard-model.imported-anomaly-coefficients@1.
2. (vi). FIXED. Conjugacy into the maximal torus added (stated as a classical fact, not derived); "sixteen such
   elements" is now "sixteen sign patterns (the elements of the image)"; 16 is stated to be the largest modulus
   for which the count is a function of the class, with the proof (both counts attained, differences exactly
   16) and a gcd computed in the check. The text says the modulus comes from the arithmetic of the involutions
   with no anomaly statement used.
3. Naming. FIXED. (H1) and the technical level now say: half the spectral asymmetry, xi = eta(0)/2 = +-1/16 per
   component of the sixteen, eta(0) = +-1/8; and that the sibling proposal works on the six-space with all
   squares -1, this one with +1, both with J^2 = -1.
4. (H2). FIXED: "must be trivial if u is gauged" (a necessary condition).
5. (K). KEPT as the named condition, with the referee's alternative recorded in the statement (on flat sides the
   obstruction is the pull-back of the extension class, x^2 exactly when the lift has square -1; not written out).
   "With a definite physical side" is now in the one-liner, the technical level and Reading (c), with the
   Lorentzian (1,5) case named.
6. Check. FIXED. The lens part is no longer a restated formula: x^2 is computed from the stored diagonal (number
   of pairs r < j in the group, 6 for order four, 1 for order two), w from (1 + u)^(k+1) in Z_2[u]/(u^(k+1)),
   and the same route at order two is required to reproduce the Whitney classes of projective space computed
   in the first half (a control that fails if the coefficient rule is wrong). (15 * 3) % 16 == 13 replaced by
   (-15 * 3) % 16 == 3, the stated count. The pseudoscalar table now runs to 2m = 8. The wall-rung-count
   premise call moved to the function that computes the jump (Cl(6,2)); it was untouched where it stood.
7. Lay level. FIXED as worded by the referee, with "argued, not proved" added to the sentence on the series.
8. Attribution. FIXED: Tachikawa and Yonekura marked from memory and not verified at source.
Orchestrator: the extraction note and Reading (a), (b) now state the branches plainly. Branch 1 only conditionally
on the unimported statement, and then true for three generations, not for every generation number; branch 2 at
the argued level (Reading (b) is headed "argued, not proved"); branch 3 not addressed; nothing at the proved level.
Rebuttals: none.
Title unchanged ("Order-four structure on real projective walls; the signed count is defined modulo 16").
runcheck: 3 of 3 functions PASS.
check4: pending (orchestrator)

## New decisions for Leon created by the fixes
1. How the stored CPT conjugation acts on the gauge sector. The colour-angle result now rests on a named
   hypothesis (automorphism or anti-automorphism on the colour index) that the premise does not state. A
   sentence added to dark-matter.premise-cpt-covariance would remove the hypothesis; it is a premise edit.
2. Which identification of the two towers' orientations the common-ceiling-coupling premise is read with. With
   the stored tower-top reversal the two angles are equal; with its composite with a reflection they are
   opposite. The premise equates "every other coupling" without saying which; for the angle the choice matters.
3. Import (L2) and (K) (and the conjugacy of maximal tori) as Facts, or leave the order-four result conditional
   on them as written. They will not show in "holds given" (referee R2).
4. When the spectral-asymmetry proposal is accepted, hypothesis (H1) of the order-four result should become a
   uses edge (maintainer edit; referee R2).
5. Noted by referee R1, not a defect of the proposal: the rung entities read phases in span{1, I_4}, the Fock
   module's unit in the premises is I_7, and C fixes I_4, so C is linear with respect to the unit in which the
   mass phase is read. Whether that is intended is a question about the stored conventions.
