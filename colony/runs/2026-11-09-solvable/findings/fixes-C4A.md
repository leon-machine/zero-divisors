# fixes-C4A (fix round, run 2026-11-09-solvable)

check4: pending (orchestrator). Only runcheck.py was run.

## synthesis.bott-shifted-model-leaves-the-odd-towers-dimension-free (R2 3, OVERSTATED; restated, id kept)
Referee accepted: my own new check confirms that U3 fails at (10,1) and (1,10). The field there is R, as in every
causal member of residues 1 and 7, the real Witt index of hatV is 2, and the pair count floor((n+2)/2) exceeds 2
for n > 3. No rebuttal.
- Title: "The five-dimensional towers' dimension is free; Premise U fixes the three-dimensional ones" (90 chars).
- M_8 now shifts only residues 3 and 5, to (12,1) and (1,12). Residues 1 and 7 stay at (2,1) and (1,2) in both
  models.
- Formal, at every level, now has five clauses:
  - (i) The split is unchanged. Added: the constituent field is invariant under the shift, and the complex Witt
    index of hatV (the pair count) is not invariant (2 -> 6 at residues 1, 7; 3 -> 7 at residues 3, 5).
  - (ii) Independence at residues 3 and 5 only. The audit now covers U (U3 holds because the field there is H),
    H2, (S), and R2 flagged as met only in its dimension-generic reading. It also lists the remaining cone
    postulates: T14's (U), P4, P5, CPT covariance, flag as datum, (I), (P), (Q), (R), (L, U), slot module, common
    ceiling, tameness, indifference.
  - (iii) New: at residues 1 and 7, U3 with the stored pair count admits only the lowest causal member, so P3's
    lowest-causal clause there follows from U.
  - (iv) (W), now about the shifted representatives at residues 3 and 5.
  - (v) Cost: the ratio becomes 1 + 8/3 + 1920/pi^5, in (9.9, 10.0). The value 10.56 is removed everywhere.
- "Every stored structural selector" is corrected (the pair count changes).
- Technical, lay and one-liner restated to match.
- Extraction note: U is listed as "premises used, assumes edge for the maintainer" (override 2).
- New uses: synthesis.gauge-algebra-by-tower@1, dark-tower-matter.constituents-field@2,
  dark-tower-matter.residue-seven-unit@3.
- Check changes:
  - New function check_premise_u_admits_the_shift_only_at_residues_three_and_five. Over every causal member of
    residues 1, 7, 3, 5 up to dimension 21 it computes the GA real Witt index of hatV (= 2), the field (stored
    table reproduced), and the U3 admission (only (2,1) and (1,2) at residues 1, 7; all five members at 3, 5). It
    also checks that the conformal pseudoscalar of Cl(2,11) is central, squares to -1 and has odd grade.
  - The type-data function is renamed check_type_data_invariant_and_pair_count_not and now asserts that the pair
    count is not invariant.
  - The ratio, (W) and model functions are updated to the restated M_8. coverage.yaml is updated.
- runcheck: exit 0, 8 of 8 functions pass.

## synthesis.no-rule-p2-licenses-gives-the-thickness-of-r3 (R2 4, SOUND WITH FIXES)
- Title: "No rule P2 licenses, on the orbit reading of licensing, gives the thickness of R3". The same qualifier is
  in the one-liner and lay.
- (ii) now opens by saying that P2 as stored licenses no filling rule and that the clause concerns its orbit
  extension. The proof says the same.
- (i) and the proof list the missing cone postulates with one line each: P4, P5, T14's (U), (I), (P), (Q), (R),
  (L, U), slot module, common ceiling, indifference, tameness. None names the thickness.
- New sentence in (iii), the technical and the proof: the charge branch for all four odd towers gives
  T = 1 + 4/eps, which equals 5.364 at eps = 1000/1091 (about 0.917). So the fit moves from R3 to eps and is not
  removed; equal filling gives 5. The lay is reworded so it no longer suggests the licensed rules miss the
  observed value.
- Check: assertions added for eps = 1000/1091 in (0.916, 0.917), 1 + 4/eps = 5.364 and the equal-filling value 5.
  coverage.yaml updated.
- runcheck: exit 0, 4 of 4 functions pass.

## synthesis.the-residue-requires-two-arrays-per-unit-on-average-and-fixes-no-grouping (R2 5, SOUND WITH FIXES)
- J3, in (i) and the proof: J3 with (Q) v3 partitions the arrays into channels, one array per helicity channel.
  It supplies a candidate grouping, citing capacity-per-mode (iii), but no premise identifies a registered unit
  with a channel or a pair of channels, so the grouping stays free.
- C2: (i) and the proof flag that reading nu as a density of registered units of arrays is the problem's framing,
  not (C2)'s literal text.
- Audit list completed in the proof: P1-P5, R1-R3, H1, T14's (U), (I), (L, U), common ceiling, indifference,
  tameness.
- Assumes edges are not added (override 2). (Q)@3, (C2)@4 and the window reading @1 are named in the extraction
  note under "premises used, assumes edge for the maintainer".
- J3 caveat (override 4), in (iii) formal and proof: under J3's reading of integer-weight channels as array
  currents, c = 16 n_g, and the 24 units per light ray at n_g = 3 stands.
- The check is unchanged.
- runcheck: exit 0, 3 of 3 functions pass.
