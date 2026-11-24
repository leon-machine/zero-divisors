# Fixes, G-B, run 2026-11-24-three-routes

## synthesis.helicity-two-composites-of-light-ray-fermions-on-a-generator-and-off-the-null-plane
Verdict: SOUND WITH FIXES (clauses (i) to (v) reproduced by the referee). Nothing rebutted.

What changed (entity.md at every level, proof-main.tex, check.py; title unchanged, it names the subject and
asserts nothing):
1. Clause (v), hidden hypothesis stated: the medium's elements commute with the matter factor AND with the unit
   J, with J^2 = -1, J* = -J and J commuting with the matter factor; "coupled at a point, no constraint" is now
   part of the clause. The proof says where each hypothesis is used. Same in the technical level and one-liner.
2. Clause (iii): "normalised expectation" with the formula, the squared norm 2 of psi_1 stated; "the commutator
   of rho_q(id) with its adjoint has normalised expectation 4q". Added to the clause and the proof that a
   commutator that is not a number holds for every composite of free fields and so shows little alone.
   Added, after checking it myself: (X_4*)^2 Omega is not zero, squared norm 36 against 200 for a canonical
   mode of sea value 10 (the referee's remark that the square is nonzero at q = 4, now with its number).
3. Claims narrowed. One-liner, technical level and the maintainer decision in the note now say "the lowest
   helicity-two four-fermion modes on a generator are not a free part in the sense of the stored lattice
   result's clause (4)". Reading (a) is stated "for the families X_q and V_q", lists what is not treated
   (linear combinations, other flavour structures, six or more fermions) and labels "no helicity-two composite
   on a generator is canonical" as argued; the lay level says the same in plain words. The Reading is headed
   "argued throughout; nothing in it is proved here". Weinberg and Witten is named as the general tool, with
   its hypothesis (a Lorentz-covariant conserved stress, which free fermion fields satisfy), cited from
   memory and used in no proof.
4. Reading (b): said to be standard kinematics and to rest on (a), the parallel sector being the sector on one
   generator.
5. Reading (c): restricted to coupling at a point with no constraint. "Two ways and not three" removed: two
   ways are named and the list is said not to be shown complete. "A composite ... is neither" replaced by the
   referee's wording: the modes do not supply the state-independent linear response of a canonical free part;
   as part of a causal medium they would meet commutation by (v) and belong to the second way.
6. New paragraph "Constraints" in the Reading, citing in text only the lattice model of the first-order field
   filed alongside (synthesis.spin-two-lattice-model-static-slaved-field-fails-and-dressed-pair-detection-
   commutes): the constrained part is a matter element at equal time and needs a dressing; whether a medium
   without canonical variables can carry one is shown in neither result; the single-mass obstruction (centre
   of mass, a charge of the constraints) does not depend on what the free part is made of.
7. Bridge B2, one sentence labelled argued in the Reading: the spin-two response of the stored free content is
   a continuum with no pole at null momentum, a pole needs the induced Einstein-Hilbert term, whose
   coefficient the store holds to be cut-off dependent (a mention of the stored result, not a premise).
8. "Where a response linear in the source would give -a" dropped (it normalised the commutator function to 1
   without saying so); now "depends on the medium's state and is not proportional to the kick angle".
9. Literature dates: de Broglie 1932 to 1934; Sakharov 1967.
10. Check: check_commutator_of_the_composite_is_not_a_number now also asserts the squared norms (1, 2, 1) of
   the three vectors and the q = 4 value 36 < 200. The referee's two perturbations already failed the check;
   no weak check was reported.

runcheck: 5 of 5 PASS after the edits.
check4: pending (orchestrator). validate_draft: pending (orchestrator).
One thing for the orchestrator to watch at the central gate: the Reading and the note contain the id of the
proposal filed alongside as plain text (FIXROUND rule 6), not as a claim reference. If the validator objects
to an unknown id in text, replace it by the words "the lattice model of the first-order field filed alongside".
Two stored ids are newly mentioned by claim reference in the Reading and are not in `uses`:
synthesis.series-content-induces-a-newton-coupling-only-through-an-unfixed-cut-off and (already there)
hawking.joint-j3-s-wave-reduction.

## Bridge entries
- B7 (recoil factor): recomputed. The bridge pass is right: the entangling term is bilinear in the two
  displacements, G m_A m_B dx_A dx_B / d^3, and the recoil body gives G m_A m_B dx_A dx_B / R^3, ratio
  (d/R)^3. My (d/R)^2 was the ratio of the path-dependent forces, not of the phases. The number was never in
  the proposal; it is corrected in findings/attack-G-B.md (two places), with the remark that the factor is
  geometric and need not be small.
- B2: applied (item 7 above).
- B1 and B3: leads and a decision, below.

## Repin on acceptance
None. Every pin is to a stored version. If the proposal filed alongside is accepted, the plain-text citation
in the Reading and the note can become a claim reference (maintainer).

## Next steps
- B1: under the second way (the field as the response of the stored quantum fields) the state-independent
  anomalous stress of the trace-anomaly proposal is automatically part of the source, being the local part of
  that response; the canonical-pair way says nothing about it. Not pursued; not in the proposal's text because
  it would cite a result that is not stored.
- B2: the weight of the spin-two continuum of the stored content (296 in the units of the stored channel
  weights, by the bridge pass's count) against the induced coefficient: a computation for a later run on
  op.einstein-from-the-field-theory.
- Whether a medium without canonical variables can carry the dressing the gravitational constraints need
  (the referee points to lattice gauge theories with compact or finite groups). Open in both G proposals.
- From the attack round, still open: general linear combinations of helicity-two four-fermion modes and six or
  more fermions; the contraction over many generators at helicity two; bilinears with transverse derivatives;
  the second-order size of a composite's failure; the one-dimensional positive statement with its zero mode.

## Decisions for Leon
1. Accept the proposal as narrowed. Its proved content is clauses (i), (ii), (iv), (v) and the computed
   values of (iii); everything about composites in general and about the ways of meeting the requirement is
   argued.
2. Whether to record on the open problem the two ways named (a canonical pair; the field as the response of
   the stored quantum fields, narrowed by the stored cut-off result), as an attack item labelled argued and
   not as a classification.
3. B3: the registered prediction pred.gravity-entangles-standard-phase is conditional on P-i to P-vi, and the
   notebook glosses P-v as "no free radiative part", which the requirement of 18 November rejects. The phase
   stands; the premise list does not. Restate the kill condition with P-v replaced by its successor, or say
   why P-v stays. (I did not read P-v's wording; this is the bridge pass's lookup.)
4. If the open problem is restated from the two G results, say there that the single-mass obstruction holds
   whatever the free part is made of.
5. Prior art to read before citing as established: Galley, Giacomini and Selby 2022; Pryce 1938; both from
   memory.
