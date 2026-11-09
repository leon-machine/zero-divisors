# Fixes C3B (fix round, run 2026-11-09-solvable)

Proposal: synthesis.light-ray-recurrence-test-verdict-on-generations-is-set-by-the-scalar-content (id kept).
Referee: verify/R2.md section 2, verdict OVERSTATED. Restated to the referee's true weaker statement at every level.

## Fixes applied
1. Restatement (OVERSTATED). The counting result is now conditional on the "additive reading": boson null data
   (vectors, scalar doublets, eps = 1 graviton) counted as real arrays beside the sixteen Weyl arrays per generation,
   stated as outside the CAR scope of (N+) and of the window reading and not J3's reading. Clauses (i)-(v) are
   labelled "under the additive reading"; new clause (vi): under J3's reading (integer-weight channels are currents of
   the arrays) c = 16 n_g and both tests give 3 | n_g. Closing paragraph: the scalar and graviton content set the
   verdict only under the additive reading.
   - Title: "Light-ray recurrence test: with additive bosons, scalars and graviton set the verdict" (85 chars; the
     referee's suggested title is 110 chars, over the E124 limit of 90, so shortened with the same condition).
   - One-liner, technical, lay rewritten with the condition; lay now says the series' own rule (J3) treats these
     fields as built from the matter sea, in which case the multiple-of-three answer stands.
   - Graviton: removed "the store has no field-theoretic graviton"; now: J3's species (every massless field)
     include the graviton, so counted additively eps = 1 and no content passes.
   - Extraction note: Leon's planned narrowing of J3 to spin 2 (FIXROUND override 4) noted as argued: afterwards
     vectors and scalars are no longer J3 currents, graviton channels stay, so the additive reading with eps = 0
     would apply.
2. Non-abelian vector count: marked "argued, not proved" (formal, technical, proof). Scalar integer weight: marked
   argued; the proof notes that the cited clause (vi) covers vectors and bivectors only.
3. The -kappa/24 of a real array: no longer attributed to an unproved Schwarzian remark. Re-derived in the proof,
   (kappa/2) zeta(-1) = -kappa/24 with zeta(-1) = -B_2(1)/2 by exact series inversion, with +kappa/48 at the half
   offset as contrast; new check function check_real_array_zero_point_and_the_j3_reading. The sibling
   synthesis.one-window-parity-recurrence-of-the-light-ray-sea-needs-twenty-four-arrays (iv) is named in the
   extraction note as the intended citation (override 3: no proposal-to-proposal citation). That the boson zero
   point equals the null-ordered window value is stated as part of the additive reading.
4. Unit: the phase is written with J, the unit of the boundary-mode arrays; on the continuum light ray I_4, same
   condition. Check uses J = g1 g2 (J^2 = -1) instead of I_4. Also stated: the grading is normalised +1 on the sea,
   and the two-window test is U = +-P (c = 60 checked as passing the sign-free form, failing the one-window form).
5. Prior art: added Garcia-Etxebarria and Montero's mod-9 baryon-triality condition (3 | n_g); "the conclusion
   3 | n_g is prior art (Wang: 8 n_g = 0 mod 24, c = 1/2 per Weyl)"; Wan-Wang-Yau reworded to its abstract;
   JHEP 08 (2019) 003 kept.
6. Premises (override 2): (Q)@3 and the window reading@1 named in the extraction note under "premises used, assumes
   edge for the maintainer"; no assumes edge added. J3 and (Q) cited by claimref in the formal text (both already in
   the past cone through the null-ordering result), not added to uses.

## Check
runcheck: 6/6 functions PASS (python3 colony/runcheck.py proposals/<id>/check.py).
check4: pending (orchestrator). validate_draft: pending (orchestrator).
Note for the orchestrator: two claimrefs (singularity.q-joint-quasi-freeness-s-wave, hawking.joint-j3-s-wave-reduction)
are to entities in the cone but not in uses, as in the stored null-ordering entity's text; if validate flags them,
replace by plain names.
