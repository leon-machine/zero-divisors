# Fixes C2B, run 2026-11-09-bridges (fix round, after verify/R1.md)

Edited in place in proposals/<id>/; ids unchanged. Only runcheck was run (both checks pass: 6 and 6 functions).

## synthesis.three-rungs-do-not-complete-the-quarter-turn-lens-walls-on-any-side (SOUND WITH FIXES, 1-5)
1. Title: now "Three rungs fail on quarter-turn lens walls from dimension five (five given spin class)"
   (87 characters). One-liner and lay level carry the same scope; the lay level says two can suffice on the
   three-dimensional wall.
2. Background: (G) replaced by (G+), stated as an extension of the stored (G) (which has only the Euler class of an
   oriented plane bundle): cohomology with local coefficients from the equivariant cochains, and the single
   obstruction in twisted H^2 for a plane bundle that need not be orientable. Formal level, closing sentence, proof,
   extraction note and coverage all say (G+).
3. Clause (3): 4 <= k <= 5 on every side of L^5(4) with the sibling's explicit map (named in words, not a premise);
   4 <= k <= 6 kept on L^7(4); the proof says the same.
4. Clause (2): "for every n" in place of "(computed for n <= 6; the complex is periodic)"; coverage says the computed
   range is a control.
5. Lay level: "in dimension five and above" added to the sentence that states the result.
Also: the extraction note cross-references the definite-side sibling, which names this proposal's twisted cohomology
as intended citation (coordinator's ruling: the twisted cohomology stays here).

## synthesis.order-four-elements-with-square-the-grading-and-the-majorana-element (SOUND WITH FIXES, 1-6)
1. Sign and definition: N_j = v_j v_j^* (occupation, v_j creation); omega = -I (-1)^N, so -I on the sixteen and +I
   on the conjugate sixteen, for the orientation gamma_1 ... gamma_10. Corrected in clause (2), one-liner, technical
   level, proof and clause (4) (signed count -16 for omega). Check: the chirality function now asserts
   omega = -I (-1)^N and not +I (-1)^N, builds the projector of the empty state, verifies that every v_j^*
   annihilates it, that it is even, that omega acts on it by -I, and by +I on a one-mode state.
2. Dirac terms: clause (3) now says every mass form (grades 1, 3, 5) anticommutes with omega, Dirac terms included;
   omega z, z the element -1 of su(2)_L on the slot doublet (equivalently omega exp(-2 pi I Y), which differs by a
   central element of su(3)), fixes the four slot vectors, so a Dirac term keeps omega modulo the Standard Model
   group; T is invariant under that group, so nothing compensates. Last sentence restated as the referee words it.
   New check function check_dirac_terms_keep_the_pseudoscalar_modulo_the_gauge_group (exact): z is -1 on the slot
   generators, +1 on the pair generators, commutes with T; omega z commutes with the slot generators and reverses T;
   omega anticommutes with sample blades of grades 1, 3, 5. I used z, not exp(-2 pi I Y), in the check because the
   latter has cube roots of unity (no exact rational form); the proof gives the relation between the two on states.
3. omega = exp(-(pi/2) I X), X = 5(B - L) - 4Y = 5 - 2N, in clause (2) and the proof; omega named as the classical
   generator of the centre of Spin(10), the Z_4 in U(1)_X, "classical, not new", in formal, technical and note. The
   parity of T is stated as its X charge modulo 4 (the link to the mass-terms sibling, named in words).
4. Labels: "no condition on the content can come from it" and "no stage at which it is both a symmetry and not a
   gauge transformation" are marked argued, with the proved content listed beside each; the lay level carries
   "(argued)".
5. Clause (2) says conjugation by omega is the grading automorphism (order two) and the order-four action is on the
   module, omega^2 = -1 the parity of one-fermion states.
6. Clause (1) and proof: for one mode -I a k is again a generator (the twist is the quarter turn of the mode).

## Bridge leads (findings/bridges.md)
- B1: folded in (fix 2 above). My earlier link sentence "a Dirac term commutes with omega" was wrong; the corrected
  statement is omega modulo the Standard Model group, and the balanced signed count 8 - 8 is omega z, noted in
  clause (4).
- B2 (P^2 = (-1)^m; the lens deck rotor squares to the volume element): consistent with my Y3 findings; no text
  change needed in either proposal. Not tested by script.
- B3 (45 + 210 orbits): matches the Y4 computation in my findings (the 210 of weight 1); findings only.
- B6 (the descent is the parity average): agrees with my N6 note; findings only.

check4: pending (orchestrator)
