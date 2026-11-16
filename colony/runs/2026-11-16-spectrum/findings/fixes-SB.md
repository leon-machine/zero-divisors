# fixes-SB : fix round, run 2026-11-16-spectrum (proposals 3, 4, 5 of the referee's report)

All fixes applied in place in proposals/<id>/. Only `python3 colony/runcheck.py proposals/<id>/check.py` was run.
No rebuttal: every point of the referee was accepted. Scratch: work/SB/fix_p4.py, work/SB/fix_p5.py (the edits to
proposals 4 and 5 as scripts), work/SB/p3_check_before_fix.py and p4_entity_before_fix.md (pre-fix copies).

## Proposal 3  synthesis.exchangeable-deposits-carry-two-numbers-and-no-spectral-shape
Verdict: OVERSTATED. Accepted; restated at every level to the referee's weaker statement.
- Title (was "An exchangeable deposit carries two numbers and no spectral shape"): now
  "An exchangeable deposit supplies two second moments; any shape is the placement's" (81 characters). The id is
  unchanged.
- Formal (ii): the white cases are now exactly two, (a) cells that tile the slice (sum g_i = 1) and (b) point
  cells on a periodic lattice; the counter-model is in the statement as "Boundary of the statement": for point
  cells off a lattice the second term is c times the placement's structure factor, with the two-cell example
  (variances v and 2(v - c)).
- Formal (iv): "in particular" before the bound on e, and the other eigenvalue's bound n - 1 <= e <= n added.
- Formal, consequence: the referee's wording; the pre-metric reading is now labelled "Reading (argued)" and
  names both carriers (the state's invariance group, or the placement).
- Technical, lay, one-liner, extraction note: restated to match; the lay level says "featureless noise in the
  matter" and that the conversion to ripples depends on a reading the theory leaves free.
- Proof: the tiling argument, the off-lattice formula and the two-cell example added to (ii); the other
  eigenvalue in (iv); the consequence paragraph says what is argued.
- Check: new function check_placements_tiling_lattice_and_off_lattice (ring of six sites: lattice and
  sublattice, equal and unequal tilings, the off-lattice placement {0, 1, 3} with N S_pl = 1, 3, 1, and the two
  cells a quarter circle apart); added to checked_by. Every block of assertions in all five functions now has a
  GA.check label naming its clause. coverage.yaml added (five functions).
- runcheck: 5 of 5 functions PASS. check4: pending (orchestrator).

## Proposal 4  synthesis.sparse-fermion-deposit-reaches-the-amplitude-on-a-flat-slice-only-with-super-planckian-quanta
Verdict: SOUND WITH FIXES. All applied.
- "some quantum", not "quanta each": formal consequence, technical, lay, one-liner, extraction note, proof.
- (UE) (was (CA)): the velocity coefficient is |beta| = 2X on every slice, corrected in the statement;
  D = (3/2) X^2 (1 + 1/X) sqrt(s), threshold 2 pi A/(9 (2f + eta) X (1 + 1/X)^2); the check verifies the new
  form; the number "below 2.5e-30" is unchanged (the factor only lowers it).
- Readings renamed (C0), (C1), (CA) -> (FR), (FM), (UE); the physical wavenumber kappa -> k_d (kappa is left
  for the expansion perturbation); the velocity u -> v.
- The from-memory derivation of the conversions is dropped; the coefficients are cited in text from the result
  filed alongside (synthesis.descent-slice-constraints-and-the-three-readings-of-a-white-deposit), not in `uses`.
- Leon's decision applied: "the deposit's quanta lie below the Planck mass" is now Hypothesis (QP), named in the
  formal statement as a hypothesis of this result only. Title, one-liner and lay level say: closed under the two
  flat-slice readings given (QP), open under (UE), no reading adopted. New title (88 characters):
  "Sparse fermion deposits: closed on flat slices for sub-Planckian quanta, open under (UE)". The id is unchanged
  (it still reads "...only-with-super-planckian-quanta"; renaming an id is the maintainer's).
- Lay: the two sentences the referee named are corrected ("a sizeable fraction of, or more than, the mass
  inside the Hubble region"; "would behave as black holes rather than particles (argued)").
- Setting: the g internal states at a momentum share one energy (the referee's remark on (i)).
- "At every reheating temperature of the window" is now "at both ends of the window", with the statement
  between the ends marked argued.
- Check: labels on every block; coverage.yaml added (three functions).
- runcheck: 3 of 3 functions PASS. check4: pending (orchestrator).

## Proposal 5  synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise (version 5, restatement)
Verdict: SOUND WITH FIXES. All six applied.
1. The note's constraint: (k/a)^2 psi - H kappa_theta = -4 pi G rho delta (sign of the expansion term corrected).
2. The two stored proof sentences that were still unconditional now carry "(under (FR))"; the appended paragraph
   opens by saying so; the amendment's defect lists the proof.
3. Explicit signs: R_inf = psi + delta/4 - 2 H q/(rho + p), psi in the convention of the derived metric's
   1 - 2 psi (labelled as the metric reading), and R_inf = -zeta_inf stated once.
4. The uniform-density variable is written as the stored Fact's zeta; under (FR) "+delta/4 on the slice,
   -delta/4 afterwards", in the Fact's convention. The check's assertion was rewritten to that convention.
5. Lay: (FR) described as "space in each region is flat and the matter at rest in it", not as a time shift.
6. (FR) defined exactly: (LC) with v = 0 on the slice.
Also: the from-memory derivation is dropped from the note and the proof; the conversion is cited in text from the
result filed alongside, not in `uses`. The proof keeps only the thermal ratio (this entity's own) and one
paragraph saying what the check re-verifies as evidence for the amendment. Leon's decision applied: the note
says the series adopts no reading and the slice's expansion datum is free. The velocity is v throughout. The
aggregated GA.check of the new function is split into eight labelled ones. coverage.yaml added for all six
functions (the stored entity had none; the five stored records describe the stored functions by their own
labels).
- runcheck: 6 of 6 functions PASS. check4: pending (orchestrator).

## Repin on acceptance
- If version 5 of synthesis.quasi-free-deposit-is-vacuum-plus-shot-noise is accepted: proposals 3 and 4 pin it
  at @4 and repin to @5 (clauses (i), (ii) and (iv), which they use, are unchanged). Proposals 1 and 2 likewise
  (their fixer's file).
- If proposal 1 is accepted: add it to `uses` of proposal 4 and of the version-5 entity (both cite it in text
  only, by id, as "filed alongside"), and replace those phrases by a claimref.

## Decisions for Leon
None new. The three made during the referee round are applied (slice left free; (QP) a hypothesis of proposal
4 only; one convention for the readings). Two maintainer items, not decisions: the id of proposal 4 still names
the old emphasis, and the id of proposal 3 still says "no spectral shape"; both titles are corrected, and an id
change, if wanted, is a maintainer rename.
