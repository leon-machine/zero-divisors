# Fixes C2A, run 2026-11-09-bridges (after verify/R1.md)

Only `runcheck.py` was run. Ids are unchanged; one title changed.

## 1. synthesis.definite-side-rung-count-on-the-quarter-turn-lens-wall-of-dimension-five (SOUND WITH FIXES)
1. Applied. The wrong recollection (level m + 1 exactly for m = 1, 2, 4, 8) is removed from the extraction note and
   replaced by Stolz's theorem as given in the published review (m + 1 for m = 0, 2; m + 2 for m = 1, 3, 4, 5, 7;
   m + 3 for m = 6 modulo 8, m >= 2), marked "paper not read", with the review's remark on m = 4 modulo 8, the
   consequences k_+(L^5(4)) = 5, k_+(L^7(4)) = 6 as prior art not derived, and where the bound ceil(3(n+1)/2) is
   sharp (n = 1, 2, 3, 5) and where not (n = 4, 6, 7).
2. Applied. The upper bound is labelled likely classical in clause (2) and in the note; not claimed as new.
3. Applied. Clause (3), the closing paragraph, the proof and coverage now say "(G+)": the stored (G) extended by
   cellular cohomology with local coefficients and the primary obstruction in H^r twisted by w_1, stated as not
   stored. The sentence that the three-component map needs no background is added.
4. Applied (first option). "d = 0 mod 8: the squaring test does not obstruct; whether four components suffice is
   not decided". Lay level reworded. The proof names the further inputs that would decide it and does not use them.
5. Applied. "The obstruction is not zero, H^5 having the single nonzero class x u^2".
6. Applied. (T2) restated with the flag-bundle map p (p^*V a sum of line bundles, p^* injective with Z and Z_2
   coefficients); the proof pulls back by p and uses naturality of Sq^2. Clutching and Hermitian metrics are
   listed as elementary constructions. The lower bound stays conditional on (T).
7. Applied. The mirror-image vector is \bar w_1 in the statement, technical level and proof (m1 in the check).
8. Applied. The extraction note names synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side
   as intended citation: twisted cohomology is its clause (2); jointly 4 <= k <= 5 on every side of the L^5(4)
   walls and k = 5 on the definite side given (T). No claimref (a proposal cannot cite a proposal).
9. Kept: conditionality in title, one-liner, lay and formal levels.
Not applied (maintainer-only): an `assumes: sheaf.tameness` edge (the referee's item (b) for Leon).
Check: 6 functions pass under runcheck (table wording only; no assertion changed).

## 2. synthesis.vacuum-polarisation-kernel-on-a-gravitational-field-has-the-flat-leading-part-and-no-weyl-term-of-degree-four
Verdict OVERSTATED with one coefficient WRONG. The sign is NOT disputed: against the stored convention
(obj.synthesis.gtg-flat-spacetime-gauge-fields (c): curvature operator = minus the covariant field strength) my
gauge had field strength +Riem where the store requires -Riem. Recomputed exactly in the corrected check:
a.D R = +(1/4) Riem(a ^ xi) R, D R = +(1/4) Ric(xi) R, D U = +(1/12) Ric(xi) R; de Sitter Riem(B) = (L/3) B gives
D U = (L/12) xi, and the old relative sign gives -(5/12) L xi, now asserted to be rejected.
Restated to the weaker statement (a)-(d) on every level: title (now "One-loop parametrix trace on a torsion-free
field: rotors cancel, first order is Ricci"), one-liner, formal, technical, lay, note, proof, check, coverage.
1. Applied. Signs and coefficient corrected everywhere; gauge Omega(a)(x0 + z) = -(1/2) Riem(z ^ a).
2. Applied. The check asserts that the gauge's field strength is -Riem and that the opposite gauge gives +Riem; the
   -5/12 assertion is replaced by +1/12; de Sitter test added for L = 3, 1, -6 (fails for the wrong sign).
3. Applied. Pi^0 is defined without the Van Vleck factor; (i) says the leading part is Delta Pi^0; (iii) says Weyl
   enters at degree 3 through derivatives and at degree 2 through Delta = 1 + (1/180) tr K^2 (cited, not derived).
   New check function: the tidal map of the Weyl-type samples has zero trace and nonzero trace of its square.
4. Applied. Scope (one loop, parametrix trace form, torsion-free, normal coordinates at x', transported index) opens
   the formal statement and the one-liner; "torsion-free" is in the title and, in plain words, in the lay level.
5. Applied. The kernel with an extension problem is the time-ordered one (sigma + I_4 0 in both factors, off the
   diagonal); the Wightman product is said to need no extension. "From the same side" is dropped as a rule.
6. Applied. The rules are enlarged ((SD1) sd of sigma^-k log^j sigma, (SD2) smooth-function rule, (SD3)
   subadditivity, (SD4) higher-order Hadamard form) and moved to the extraction note, each cited from memory, so
   the maintainer's Fact can be written to fit; also the first transport equation, the protraction identity and
   the exact form of local covariance with scaling the reduction to Z_3 would need.
7. Applied as "argued": the scalar coincidence value of V is stated as resting on the first transport equation
   and clause (ii); not derived.
8. Applied as far as a fixer can: the protraction identity is stated as a hypothesis with its meaning (first
   Bianchi identity of a torsion-free field), said not to be stored, and listed in the note as an import for the
   maintainer. The object carrying the convention is added under `about` and cited.
9. Applied. (iv), one-liner and lay level: 15 local terms per index pair with coefficient FUNCTIONS of x'; the
   Ward-preserving freedom on a fixed field is still a function space (the example d(c F)); the reduction to Z_3
   needs local covariance with scaling (argued).
10. Applied. (i) proved; (ii) proved given the stored (computed) Taylor data and the protraction identity; (iii)
    and (iv) argued. "Is the first half of clause (v)" now reads "supports ... does not prove it".
11. Applied. The relative sign of the mass-mass and leading terms is said not to be fixed by the stripped trace form.
Also: the frame/chart caveat (the full curvature operator appears at degree 4 in another frame) is in the formal
statement; the rotor is no longer written as a bare R next to the field strength; the draft's sign error is
recorded in the note. The id still says "no weyl term of degree four": true in the stated scope, argued; ids are
not renamed.
Check: 6 functions pass under runcheck (one new: check_tidal_map_of_a_weyl_type_operator, added to checked_by and
coverage). The sign test is by construction a statement about the gauge chosen; what ties it to the store is the
stored relation Riem = -R, read from the object, not machine-checked against the object's text.

## Bridge links addressed to me
- B1, B2 (order-four element, P^2 = (-1)^m): concern Y3, where I filed nothing; consistent with my computed
  omega^2 = -1 at ten generators and "every five-blade is odd". B1 corrects my findings line: every mass form has
  odd grade, so all anticommute with omega, Dirac forms included; my sentence "a Majorana term breaks the
  order-four element" holds only modulo the gauge group. No proposal text of mine is affected.
- B5 (extension count in dimension d): one sentence added to the kernel proposal's note (degree 2d - 2,
  omega = d - 2, not used). Nothing else in my text depends on it.
- B7 (Cl(5,5) against Cl(10,0)): accepted; my findings' caveat "a different real form" is wrong in substance (both
  are isomorphic by the stored classification, with no preferred isomorphism). The coincidence stays a coincidence.
  Findings only; no proposal text.

## For Leon (unchanged or new)
- The lower bound five stays conditional on (T) as worded in fix 6; (G+) is a second background extension.
- The kernel result no longer lifts clause (v) of the stored vacuum-polarisation theorem; the Facts to be written
  (scaling-degree rules, transport equation, protraction identity, local covariance with scaling) are listed in its
  extraction note in the form the result needs.

check4: pending (orchestrator)
